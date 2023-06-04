import warnings
from functools import partial
import numpy as np
from ._types import Float64Array, Int32Array, Int8Array, ComplexArray, Float64ArrayOrComplexArray, Float64ArrayOrSimpleComplex
from typing import Any, AnyStr, Callable, List #, Iterator

# UTF8 under testing
codec = 'UTF8'

interface_classes = set()

warn_wrong_case = False

def set_case_insensitive_attributes(use: bool = True, warn: bool = False):
    '''
    This function is provided to allow easier migration from `win32com.client`.
    
    When used with late bindings, `win32com` allows using mixed-case names for
    any of the COM-related items. When migrating or testing with DSS-Python,
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


# For backwards compatibility, will be removed for version 1.0
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


class Base:
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
        '_set_string_array',
        '_prepare_float64_array',
        '_prepare_int32_array',
        '_prepare_string_array',
        '_get_complex128_array',
        '_get_complex128_simple',
        '_get_complex128_gr_array',
        '_get_complex128_gr_simple',
        '_prepare_complex128_array',
        '_prepare_complex128_simple',
        '_errorPtr',
    ]

    _use_exceptions = True

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
        self._set_string_array = api_util.set_string_array
        self._prepare_float64_array = api_util.prepare_float64_array
        self._prepare_int32_array = api_util.prepare_int32_array
        self._prepare_string_array = api_util.prepare_string_array
        self._errorPtr = self._lib.Error_Get_NumberPtr()
        
        self._prepare_complex128_array = api_util.prepare_complex128_array
        self._prepare_complex128_simple = api_util.prepare_complex128_simple
        self._get_complex128_array = api_util.get_complex128_array
        self._get_complex128_simple = api_util.get_complex128_simple
        self._get_complex128_gr_array = api_util.get_complex128_gr_array
        self._get_complex128_gr_simple = api_util.get_complex128_gr_simple

        cls = type(self)
        if cls not in interface_classes:
            interface_classes.add(cls)
            cls._dss_original_attributes = {a for a in dir(self) if not a.startswith('_')}
            lowercase_map = {a.lower(): a for a in cls._dss_original_attributes}
            cls._dss_attributes = lowercase_map


    @staticmethod
    def _enable_exceptions(do_enable: bool):
        """
        Controls whether the automatic error checking mechanism is enable, i.e., if
        the DSS engine errors (from the `Error` interface) are mapped exception when
        detected. 
        
        **When disabled, the user takes responsibility for checking for errors.**
        This can be done through the `Error` interface. When `Error.Number` is not
        zero, there should be an error message in `Error.Description`. This is compatible
        with the behavior on the official OpenDSS (Windows-only COM implementation) when 
        `AllowForms` is disabled.

        Users can also use the DSS command `Export ErrorLog` to inspect for errors.

        **WARNING:** This is a global setting, affects all DSS instances from DSS-Python 
        and OpenDSSDirect.py.
        """
        Base._use_exceptions = bool(do_enable)

    def _check_for_error(self, result=None):
        """
        Checks for a DSS engine error (on the default configuration).

        By default, raises an exception if any error is detected, otherwise returns the `result` parameter.
        
        If the user disabled exceptions, any error is simply ignored. Note that, in this case, manually
        calling this function would have no purpose/effects.

        Note that, **in the future**, we may try showing a popup form like the official OpenDSS does on Windows
        if AllowForms is True. This behavior is not very portable though and not adequate for automated scripts.
        """
        if self._errorPtr[0] and Base._use_exceptions:
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

        self._allow_complex = False
        self.init_buffers()



    # def __delete__(self):
    #     if self.ctx is None:
    #         return
             
    #     if self.lib.ctx_Get_Prime() != self.ctx and self.owns_ctx:
    #         self.lib.ctx_Dispose(self.ctx)

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

        # also keep a casted version for complex floats
        self.gr_cfloat64_pointers = (self.ffi.cast('double _Complex**', tmp_float64_pointers[0][0]), tmp_float64_pointers[1][0])

    def clear_buffers(self):
        self.lib.DSS_DisposeGRData()
        self.lib.DSS_ResetStringBuffer()
        self.init_buffers()

    def get_string(self, b) -> str:
        if b != self.ffi.NULL:
            return self.ffi.string(b).decode(self.codec)
        return u''

    def get_float64_array(self, func, *args) -> Float64Array:
        ptr = self.ffi.new('double**')
        cnt = self.ffi.new('int32_t[4]')
        func(ptr, cnt, *args)
        res = np.frombuffer(self.ffi.buffer(ptr[0], cnt[0] * 8), dtype=np.float64).copy()
        self.lib.DSS_Dispose_PDouble(ptr)

        if self._allow_complex and cnt[3]:
            # If the last element is filled, we have a matrix.  Otherwise, the 
            # matrix feature is disabled or the result is indeed a vector
            return res.reshape((cnt[2], cnt[3]), order='F')

        return res


    def get_complex128_array(self, func, *args) -> Float64ArrayOrComplexArray:
        if not self._allow_complex:
            return self.get_float64_array(func, *args)

        # Currently we use the same as API as get_float64_array, may change later
        ptr = self.ffi.new('double**')
        cnt = self.ffi.new('int32_t[4]')
        func(ptr, cnt, *args)
        res = np.frombuffer(self.ffi.buffer(ptr[0], cnt[0] * 8), dtype=complex).copy()
        self.lib.DSS_Dispose_PDouble(ptr)

        if cnt[3]:
            # If the last element is filled, we have a matrix.  Otherwise, the 
            # matrix feature is disabled or the result is indeed a vector
            return res.reshape((cnt[2], cnt[3]), order='F')

        return res


    def get_complex128_simple(self, func, *args) -> Float64ArrayOrSimpleComplex:
        if not self._allow_complex:
            return self.get_float64_array(func, *args)

        # Currently we use the same as API as get_float64_array, may change later
        ptr = self.ffi.new('double**')
        cnt = self.ffi.new('int32_t[4]')
        func(ptr, cnt, *args)
        try:
            assert cnt[0] == 2, ('Unexpected number of elements returned by API', cnt[0])
            return self.ffi.cast('double _Complex**', ptr)[0][0]
        finally:
            self.lib.DSS_Dispose_PDouble(ptr)


    def get_float64_gr_array(self) -> Float64Array:
        ptr, cnt = self.gr_float64_pointers
        if self._allow_complex and cnt[3]:
            return np.frombuffer(self.ffi.buffer(ptr[0], cnt[0] * 8), dtype=np.float64).copy().reshape((cnt[2], cnt[3]), order='F')
        
        return np.frombuffer(self.ffi.buffer(ptr[0], cnt[0] * 8), dtype=np.float64).copy()


    def get_complex128_gr_array(self) -> ComplexArray:
        if not self._allow_complex:
            return self.get_float64_gr_array()

        # Currently we use the same as API as get_float64_array, may change later
        ptr, cnt = self.gr_float64_pointers
        if self._allow_complex and cnt[3]:
            return np.frombuffer(self.ffi.buffer(ptr[0], cnt[0] * 8), dtype=complex).copy().reshape((cnt[2], cnt[3]), order='F')
        
        return np.frombuffer(self.ffi.buffer(ptr[0], cnt[0] * 8), dtype=complex).copy()


    def get_complex128_gr_simple(self) -> Float64ArrayOrSimpleComplex:
        if not self._allow_complex:
            return self.get_float64_gr_array()

        # Currently we use the same as API as get_float64_array, may change later
        ptr, cnt = self.gr_cfloat64_pointers
        assert cnt[0] == 2, ('Unexpected number of elements returned by API', cnt[0])
        return ptr[0][0]


    def get_int32_array(self, func: Callable, *args) -> Int32Array:
        ptr = self.ffi.new('int32_t**')
        cnt = self.ffi.new('int32_t[4]')
        func(ptr, cnt, *args)
        res = np.frombuffer(self.ffi.buffer(ptr[0], cnt[0] * 4), dtype=np.int32).copy()
        self.lib.DSS_Dispose_PInteger(ptr)

        if self._allow_complex and cnt[3]:
            # If the last element is filled, we have a matrix.  Otherwise, the 
            # matrix feature is disabled or the result is indeed a vector
            return res.reshape((cnt[2], cnt[3]))

        return res


    def get_ptr_array(self, func: Callable, *args):
        ptr = self.ffi.new('void***')
        cnt = self.ffi.new('int32_t[4]')
        func(ptr, cnt, *args)
        res = np.frombuffer(self.ffi.buffer(ptr[0], cnt[0] * np.dtype(np.uintp).itemsize), dtype=np.uintp).copy()
        self.lib.DSS_Dispose_PPointer(ptr)
        return res

    def get_int32_gr_array(self) -> Int32Array:
        ptr, cnt = self.gr_int32_pointers
        if self._allow_complex and cnt[3]:
            return np.frombuffer(self.ffi.buffer(ptr[0], cnt[0] * 4), dtype=np.int32).copy().reshape((cnt[2], cnt[3]))

        return np.frombuffer(self.ffi.buffer(ptr[0], cnt[0] * 4), dtype=np.int32).copy()


    def get_int8_array(self, func: Callable, *args: Any) -> Int8Array:
        ptr = self.ffi.new('int8_t**')
        cnt = self.ffi.new('int32_t[4]')
        func(ptr, cnt, *args)
        res = np.frombuffer(self.ffi.buffer(ptr[0], cnt[0] * 1), dtype=np.int8).copy()
        self.lib.DSS_Dispose_PByte(ptr)

        if self._allow_complex and cnt[3]:
            # If the last element is filled, we have a matrix.  Otherwise, the 
            # matrix feature is disabled or the result is indeed a vector
            return res.reshape((cnt[2], cnt[3]))

        return res

    def get_int8_gr_array(self) -> Int8Array:
        ptr, cnt = self.gr_int8_pointers
        if self._allow_complex and cnt[3]:
            return np.frombuffer(self.ffi.buffer(ptr[0], cnt[0] * 1), dtype=np.int8).copy().reshape((cnt[2], cnt[3]), order='F')

        return np.frombuffer(self.ffi.buffer(ptr[0], cnt[0] * 1), dtype=np.int8).copy()

    def get_string_array(self, func: Callable, *args: Any) -> List[str]:
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


    def set_string_array(self, func: Callable, value: List[AnyStr], *args):
        value, value_ptr, value_count = self.prepare_string_array(value)
        func(value_ptr, value_count, *args)


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
            value = np.asarray(value, dtype=np.float64)

        ptr = self.ffi.cast('double*', self.ffi.from_buffer(value.data))
        cnt = value.size
        return value, ptr, cnt

    def prepare_complex128_array(self, value):
        if isinstance(value, (np.complex128, complex)):
            value = np.asarray([value], dtype=np.complex128).view(dtype=np.float64)
        elif (isinstance(value, np.array) and value.dtype in (np.complex128, np.complex64)):
            value = np.asarray(value, dtype=np.complex128).view(dtype=np.float64)
        elif type(value) is not np.ndarray or value.dtype != np.float64:
            value = np.asarray(value, dtype=np.float64)

        ptr = self.ffi.cast('double*', self.ffi.from_buffer(value.data))
        cnt = value.size
        return value, ptr, cnt


    def prepare_complex128_simple(self, value: complex):
        if isinstance(value, (np.complex128, complex)):
            value = np.asarray([value], dtype=np.complex128).view(dtype=np.float64)
        elif (isinstance(value, np.array) and value.dtype in (np.complex128, np.complex64)):
            value = np.asarray(value, dtype=np.complex128).view(dtype=np.float64)
        elif type(value) is not np.ndarray or value.dtype != np.float64:
            value = np.asarray(value, dtype=np.float64)

        ptr = self.ffi.cast('double*', self.ffi.from_buffer(value.data))
        cnt = value.size
        if cnt != 2:
            raise TypeError('A scalar complex number or an array of 2 scalar values is required.')

        return value, ptr, cnt


    def prepare_int32_array(self, value):
        if type(value) is not np.ndarray or value.dtype != np.int32:
            value = np.array(value, dtype=np.int32)

        ptr = self.ffi.cast('int32_t*', self.ffi.from_buffer(value.data))
        cnt = value.size
        return value, ptr, cnt

    def prepare_string_array(self, value: List[AnyStr]):
        if value is None:
            raise ValueError("Value cannot be None!")

        ptrs = []
        value_enc = []
        codec = self.codec
        for v in value:
            if v is not None:
                if type(v) is not bytes:
                    v = v.encode(codec)
                    value_enc.append(v)

                ptrs.append(self.ffi.new("char[]", v))
            else:
                ptrs.append(self.ffi.NULL)

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
    def First(self) -> int:
        '''Sets the first object of this type active. Returns 0 if none.'''
        return self.CheckForError(self._Get_First())

    @property
    def Next(self) -> int:
        '''Sets next object of this type active. Returns 0 if no more.'''
        return self.CheckForError(self._Get_Next())

    @property
    def Count(self) -> int:
        '''Number of objects of this type'''
        return self.CheckForError(self._Get_Count())

    def __len__(self) -> int:
        return self.CheckForError(self._Get_Count())

    def __iter__(self):
        '''(API Extension)'''
        idx = self.CheckForError(self._Get_First())
        while idx != 0:
            yield self
            idx = self.CheckForError(self._Get_Next())

    @property
    def AllNames(self) -> List[str]:
        '''Array of all names of this object type'''
        return self.CheckForError(self._get_string_array(self._Get_AllNames))

    @property
    def Name(self) -> str:
        '''Gets the current name or sets the active object of this type by name'''
        return self._get_string(self.CheckForError(self._Get_Name()))

    @Name.setter
    def Name(self, Value: AnyStr):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self.CheckForError(self._Set_Name(Value)))
        
    @property
    def idx(self) -> int:
        '''
        Gets the current index or sets the active object of this type by index
        
        While the official API included this for some classes, this is an 
        API Extension for:

        - Capacitors
        - CapControls
        - ISources
        - LineCodes
        - Lines
        - LoadShapes
        - Meters
        - Monitors
        - RegControls
        - Sensors
        - SwtControls
        - Transformers
        - Vsources
        - XYCurves

        (API Extension) 
        '''
        return self.CheckForError(self._Get_idx())

    @idx.setter
    def idx(self, Value: int):
        self.CheckForError(self._Set_idx(Value))
        
