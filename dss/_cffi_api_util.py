import os, warnings
from functools import partial
import numpy as np

# UTF8 under testing
codec = 'UTF8'

interface_classes = set()

warn_wrong_case = False

def set_case_insensitive_attributes(use=True, warn=False):
    '''
    This function is provided to allow easier migration from `win32com.client`.
    
    When used with late bindings, `win32com` allows using mixed-case names for
    any of the COM-related items. When migrating or testing with DSS Python,
    users can then use this function to continue using the same code, optionally
    emitting warnings when the canonical casing is different from the one used.
    Note that there is a small overhead for allowing case-insensitive names,
    thus is not recommended to continue using it after migration/adjustments to
    the user code.
    '''
    if use:
        global warn_wrong_case
        warn_wrong_case = warn
        if warn_wrong_case:
            Base.__getattr__ = Base._getattr_case_check
            Base.__setattr__ = Base._setattr_case_check
        else:
            Base.__getattr__ = Base._getattr
            Base.__setattr__ = Base._setattr

    elif Base.__getattr__ == Base._getattr or Base.__getattr__ == Base._getattr_case_check:
        del Base.__setattr__
        del Base.__getattr__


class DSSException(Exception):
    def __str__(self):
        return f'(#{self.args[0]}) {self.args[1]}'


# For backwards compatibility
DssException = DSSException
use_com_compat = set_case_insensitive_attributes

class CtxLib:
    '''
    Exposes a CFFI Lib object pre-binding the DSSContext (`ctx`) object to the
    `ctx_*` functions.
    '''
    def __init__(self, ctx, lib):
        done = set()

        # First, process all `ctx_*`` functions
        for name, value in vars(lib).items():
            is_ctx = name.startswith('ctx_')
            if not is_ctx and not name.startswith('Batch_Create'):
                continue

            # Keep the basic management functions alone
            if name not in ('ctx_New', 'ctx_Dispose', 'ctx_Get_Prime', 'ctx_Set_Prime', ):
                if is_ctx:
                    name = name[4:]

                setattr(self, name, partial(value, ctx))
            else:            
                setattr(self, name, value)

            done.add(name)

        # Then the remaining fields
        for name, value in vars(lib).items():
            if name.startswith('ctx_') or name in done:
                continue

            setattr(self, name, value)


class Base(object):
    __slots__ = [
        '_lib',
        '_api_util',
        '_get_string',
        '_get_float64_array',
        '_get_float64_gr_array',
        '_get_int32_array',
        '_get_int32_gr_array',
        '_get_int8_array',
        '_get_int8_gr_array',
        '_get_string_array',
        '_prepare_float64_array',
        '_prepare_int32_array',
        '_prepare_string_array',
        '_errorPtr',
    ]

    def __init__(self, api_util):
        self._lib = api_util.lib
        self._api_util = api_util
        self._get_string = api_util.get_string
        self._get_float64_array = api_util.get_float64_array
        self._get_float64_gr_array = api_util.get_float64_gr_array
        self._get_int32_array = api_util.get_int32_array
        self._get_int32_gr_array = api_util.get_int32_gr_array
        self._get_int8_array = api_util.get_int8_array
        self._get_int8_gr_array = api_util.get_int8_gr_array
        self._get_string_array = api_util.get_string_array
        self._prepare_float64_array = api_util.prepare_float64_array
        self._prepare_int32_array = api_util.prepare_int32_array
        self._prepare_string_array = api_util.prepare_string_array
        self._errorPtr = self._lib.Error_Get_NumberPtr()

        cls = type(self)
        if cls not in interface_classes:
            interface_classes.add(cls)
            cls._dss_original_attributes = {a for a in dir(self) if not a.startswith('_')}
            lowercase_map = {a.lower(): a for a in cls._dss_original_attributes}
            cls._dss_attributes = lowercase_map


    def _check_for_error(self, result=None):
        '''Checks for an OpenDSS error. Raises an exception if any, otherwise returns the `result` parameter.'''
        if self._errorPtr[0]:
            error_num = self._errorPtr[0]
            self._errorPtr[0] = 0
            raise DSSException(error_num, self._get_string(self._lib.Error_Get_Description()))
            
        return result

    # for backwards compatibility
    CheckForError = _check_for_error

    def _getattr(self, key):
        if key.startswith('_'):
            return object.__getattribute__(self, key)

        key = self.__class__._dss_attributes.get(key.lower(), key)
        return object.__getattribute__(self, key)

    def _getattr_case_check(self, key):
        if key.startswith('_'):
            return object.__getattribute__(self, key)

        correct_key = self.__class__._dss_attributes.get(key.lower(), key)
        if key != correct_key:
            warnings.warn('Wrong case for getter {}.{}: {}'.format(self.__class__.__name__, correct_key, key))

        return object.__getattribute__(self, correct_key)

    def _setattr(self, key, value):
        key = self.__class__._dss_attributes.get(key.lower(), key)
        object.__setattr__(self, key, value)

    def _setattr_case_check(self, key, value):
        correct_key = self.__class__._dss_attributes.get(key.lower(), key)
        if key != correct_key:
            warnings.warn('Wrong case for setter {}.{}: {}'.format(self.__class__.__name__, correct_key, key))

        key = self.__class__._dss_attributes.get(key.lower(), key)
        object.__setattr__(self, key, value)

    def _decode_and_free_string(self, s) -> str:
        res = self._ffi.string(s).decode(self._api_util.codec)
        self._lib.DSS_Dispose_String(s)
        self._check_for_error()
        return res


class CffiApiUtil(object):
    def __init__(self, ffi, lib, ctx=None):
        self.owns_ctx = True
        self.codec = codec
        self.ctx = ctx
        self.ffi = ffi
        self.lib_unpatched = lib
        if ctx is None:
            self.lib = lib
        else:
            self.lib = CtxLib(ctx, lib)

        self.init_buffers()

    def __delete__(self):
        if self.ctx is None:
            return
             
        if self.lib.ctx_Get_Prime() != self.ctx and self.owns_ctx:
            self.lib.ctx_Dispose(self.ctx)

    def init_buffers(self):
        tmp_string_pointers = (self.ffi.new('char****'), self.ffi.new('int32_t**'))
        tmp_float64_pointers = (self.ffi.new('double***'), self.ffi.new('int32_t**'))
        tmp_int32_pointers = (self.ffi.new('int32_t***'), self.ffi.new('int32_t**'))
        tmp_int8_pointers = (self.ffi.new('int8_t***'), self.ffi.new('int32_t**'))

        # reorder pointers so data pointers are first, count pointers last
        ptr_args = [
            ptr
            for ptrs in zip(tmp_string_pointers, tmp_float64_pointers, tmp_int32_pointers, tmp_int8_pointers)
            for ptr in ptrs
        ]
        self.lib.DSS_GetGRPointers(*ptr_args)

        # we don't need to keep the extra indirections
        self.gr_string_pointers = (tmp_string_pointers[0][0], tmp_string_pointers[1][0])
        self.gr_float64_pointers = (tmp_float64_pointers[0][0], tmp_float64_pointers[1][0])
        self.gr_int32_pointers = (tmp_int32_pointers[0][0], tmp_int32_pointers[1][0])
        self.gr_int8_pointers = (tmp_int8_pointers[0][0], tmp_int8_pointers[1][0])

    def clear_buffers(self):
        self.lib.DSS_DisposeGRData()
        self.lib.DSS_ResetStringBuffer()
        self.init_buffers()

    def get_string(self, b):
        if b != self.ffi.NULL:
            return self.ffi.string(b).decode(self.codec)
        return u''

    def get_float64_array(self, func, *args):
        ptr = self.ffi.new('double**')
        cnt = self.ffi.new('int32_t[4]')
        func(ptr, cnt, *args)
        res = np.frombuffer(self.ffi.buffer(ptr[0], cnt[0] * 8), dtype=np.float64).copy()
        self.lib.DSS_Dispose_PDouble(ptr)

        if cnt[3] != 0:
            # If the last element is filled, we have a matrix.  Otherwise, the 
            # matrix feature is disabled or the result is indeed a vector
            return res.reshape((cnt[2], cnt[3]))

        return res


    def get_float64_gr_array(self):
        ptr, cnt = self.gr_float64_pointers
        if cnt[3] != 0:
            return np.frombuffer(self.ffi.buffer(ptr[0], cnt[0] * 8), dtype=np.float64).copy().reshape((cnt[2], cnt[3]))
        
        return np.frombuffer(self.ffi.buffer(ptr[0], cnt[0] * 8), dtype=np.float64).copy()

    def get_int32_array(self, func, *args):
        ptr = self.ffi.new('int32_t**')
        cnt = self.ffi.new('int32_t[4]')
        func(ptr, cnt, *args)
        res = np.frombuffer(self.ffi.buffer(ptr[0], cnt[0] * 4), dtype=np.int32).copy()
        self.lib.DSS_Dispose_PInteger(ptr)

        if cnt[3] != 0:
            # If the last element is filled, we have a matrix.  Otherwise, the 
            # matrix feature is disabled or the result is indeed a vector
            return res.reshape((cnt[2], cnt[3]))

        return res


    def get_ptr_array(self, func, *args):
        ptr = self.ffi.new('void***')
        cnt = self.ffi.new('int32_t[4]')
        func(ptr, cnt, *args)
        res = np.frombuffer(self.ffi.buffer(ptr[0], cnt[0] * np.dtype(np.uintp).itemsize), dtype=np.uintp).copy()
        self.lib.DSS_Dispose_PPointer(ptr)
        return res

    def get_int32_gr_array(self):
        ptr, cnt = self.gr_int32_pointers
        if cnt[3] != 0:
            return np.frombuffer(self.ffi.buffer(ptr[0], cnt[0] * 4), dtype=np.int32).copy().reshape((cnt[2], cnt[3]))

        return np.frombuffer(self.ffi.buffer(ptr[0], cnt[0] * 4), dtype=np.int32).copy()


    def get_int8_array(self, func, *args):
        ptr = self.ffi.new('int8_t**')
        cnt = self.ffi.new('int32_t[4]')
        func(ptr, cnt, *args)
        res = np.frombuffer(self.ffi.buffer(ptr[0], cnt[0] * 1), dtype=np.int8).copy()
        self.lib.DSS_Dispose_PByte(ptr)

        if cnt[3] != 0:
            # If the last element is filled, we have a matrix.  Otherwise, the 
            # matrix feature is disabled or the result is indeed a vector
            return res.reshape((cnt[2], cnt[3]))

        return res

    def get_int8_gr_array(self):
        ptr, cnt = self.gr_int8_pointers
        if cnt[3] != 0:
            return np.frombuffer(self.ffi.buffer(ptr[0], cnt[0] * 1), dtype=np.int8).copy().reshape((cnt[2], cnt[3]))

        return np.frombuffer(self.ffi.buffer(ptr[0], cnt[0] * 1), dtype=np.int8).copy()

    def get_string_array(self, func, *args):
        ptr = self.ffi.new('char***')
        cnt = self.ffi.new('int32_t[4]')
        func(ptr, cnt, *args)
        if not cnt[0]:
            res = []
        else:
            actual_ptr = ptr[0]
            if actual_ptr == self.ffi.NULL:
                res = []
            else:
                codec = self.codec
                str_ptrs = self.ffi.unpack(actual_ptr, cnt[0])
                #res = [(str(self.ffi.string(str_ptr).decode(codec)) if (str_ptr != self.ffi.NULL) else None) for str_ptr in str_ptrs]
                res = [(self.ffi.string(str_ptr).decode(codec) if (str_ptr != self.ffi.NULL) else u'') for str_ptr in str_ptrs]

        self.lib.DSS_Dispose_PPAnsiChar(ptr, cnt[1])
        return res

    def get_string_array2(self, func, *args): # for compatibility with OpenDSSDirect.py
        ptr = self.ffi.new('char***')
        cnt = self.ffi.new('int32_t[4]')
        func(ptr, cnt, *args)

        if not cnt[0]:
            res = []
        else:
            actual_ptr = ptr[0]
            if actual_ptr == self.ffi.NULL:
                res = []
            else:
                codec = self.codec
                res = [(str(self.ffi.string(actual_ptr[i]).decode(codec)) if (actual_ptr[i] != self.ffi.NULL) else '') for i in range(cnt[0])]
                if res == [u'']:
                    # most COM methods return an empty array as an
                    # array with an empty string
                    res = []

            if len(res) == 1 and res[0].lower() == 'none':
                res = []

        self.lib.DSS_Dispose_PPAnsiChar(ptr, cnt[1])
        return res

    def get_float64_array2(self, func, *args):
        ptr = self.ffi.new('double**')
        cnt = self.ffi.new('int32_t[4]')
        func(ptr, cnt, *args)
        if not cnt[0]:
            res = []
        else:
            res = self.ffi.unpack(ptr[0], cnt[0])

        self.lib.DSS_Dispose_PDouble(ptr)
        return res

    def get_float64_gr_array2(self):
        ptr, cnt = self.gr_float64_pointers
        return self.ffi.unpack(ptr[0], cnt[0])

    def get_int32_array2(self, func, *args):
        ptr = self.ffi.new('int32_t**')
        cnt = self.ffi.new('int32_t[4]')
        func(ptr, cnt, *args)
        if not cnt[0]:
            res = None
        else:
            res = self.ffi.unpack(ptr[0], cnt[0])

        self.lib.DSS_Dispose_PInteger(ptr)
        return res

    def get_int32_gr_array2(self):
        ptr, cnt = self.gr_int32_pointers
        return self.ffi.unpack(ptr[0], cnt[0])

    def get_int8_array2(self, func, *args):
        ptr = self.ffi.new('int8_t**')
        cnt = self.ffi.new('int32_t[4]')
        func(ptr, cnt, *args)
        if not cnt[0]:
            res = None
        else:
            res = self.ffi.unpack(ptr[0], cnt[0])

        self.lib.DSS_Dispose_PByte(ptr)
        return res

    def get_int8_gr_array2(self):
        ptr, cnt = self.gr_int8_pointers
        return self.ffi.unpack(ptr[0], cnt[0])


    def prepare_float64_array(self, value):
        if type(value) is not np.ndarray or value.dtype != np.float64:
            value = np.array(value, dtype=np.float64)

        ptr = self.ffi.cast('double*', self.ffi.from_buffer(value.data))
        cnt = value.size
        return value, ptr, cnt

    def prepare_int32_array(self, value):
        if type(value) is not np.ndarray or value.dtype != np.int32:
            value = np.array(value, dtype=np.int32)

        ptr = self.ffi.cast('int32_t*', self.ffi.from_buffer(value.data))
        cnt = value.size
        return value, ptr, cnt

    def prepare_string_array(self, value):
        if value is None:
            raise ValueError("Value cannot be None!")

        ptrs = []
        value_enc = []
        codec = self.codec
        for v in value:
            if type(v) is not bytes:
                v = v.encode(codec)
                value_enc.append(v)

            ptrs.append(self.ffi.new("char[]", v))

        # Need to keep reference to every pointer to they don't get
        # garbage collected too early
        return value_enc or value, ptrs, len(ptrs)


class Iterable(Base):
    __slots__ = [
        '_Get_First',
        '_Get_Next',
        '_Get_Count',
        '_Get_AllNames',
        '_Get_Name',
        '_Set_Name',
        '_Get_idx',
        '_Set_idx'
    ]
    
    def __init__(self, api_util):
        Base.__init__(self, api_util)
        
        prefix = type(self).__name__[1:]
        self._Get_First = getattr(self._lib, '{}_Get_First'.format(prefix))
        self._Get_Next = getattr(self._lib, '{}_Get_Next'.format(prefix))
        self._Get_Count = getattr(self._lib, '{}_Get_Count'.format(prefix))
        self._Get_AllNames = getattr(self._lib, '{}_Get_AllNames'.format(prefix))
        self._Get_Name = getattr(self._lib, '{}_Get_Name'.format(prefix))
        self._Set_Name = getattr(self._lib, '{}_Set_Name'.format(prefix))
        self._Get_idx = getattr(self._lib, '{}_Get_idx'.format(prefix))
        self._Set_idx = getattr(self._lib, '{}_Set_idx'.format(prefix))

    @property
    def First(self):
        '''Sets the first object of this type active. Returns 0 if none.'''
        return self.CheckForError(self._Get_First())

    @property
    def Next(self):
        '''(read-only) Sets next object of this type active. Returns 0 if no more.'''
        return self.CheckForError(self._Get_Next())

    @property
    def Count(self):
        '''Number of objects of this type'''
        return self.CheckForError(self._Get_Count())

    def __len__(self):
        return self.CheckForError(self._Get_Count())

    def __iter__(self):
        idx = self.CheckForError(self._Get_First())
        while idx != 0:
            yield self
            idx = self.CheckForError(self._Get_Next())

    @property
    def AllNames(self):
        '''Array of all names of this object type'''
        return self.CheckForError(self._get_string_array(self._Get_AllNames))

    @property
    def Name(self):
        '''Gets the current name or sets the active object of this type by name'''
        return self._get_string(self.CheckForError(self._Get_Name()))

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self.CheckForError(self._Set_Name(Value)))
        
    @property
    def idx(self):
        '''Gets the current index or sets the active object of this type by index'''
        return self.CheckForError(self._Get_idx())

    @idx.setter
    def idx(self, Value):
        self.CheckForError(self._Set_idx(Value))
        
