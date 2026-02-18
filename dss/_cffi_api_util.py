from __future__ import annotations
import os, warnings
from functools import partial, wraps
from weakref import ref, WeakKeyDictionary
import numpy as np
from ._types import Float64Array, Int32Array, Int8Array, ComplexArray, ComplexArray, Complex
from typing import Any, AnyStr, Callable, List, Union, Iterator, Optional, TYPE_CHECKING
from .enums import AltDSSEvent
from dss_python_backend.events import get_manager_for_ctx
from .error import DSSException

if TYPE_CHECKING:
    try:
        from altdss import DSSObject, Bus as AltBus, AltDSS
    except:
        pass

AltDSS_PyContext = None
try:
    if os.environ.get('DSS_EXTENSIONS_FASTDSS', '') != '0':
        # Try to import the fast backend
        from dss_python_backend._fastdss import AltDSS_PyContext
    else:
        warnings.warn("DSS-Extensions: DSS_EXTENSIONS_FASTDSS environment variable is set to 0; using the legacy full CFFI backend.")
except:
    warnings.warn("DSS-Extensions: Could not import the FastDSS backend; using the legacy full CFFI backend.")


if AltDSS_PyContext is None:
    # Import the prepared function info if the fast implementation from 
    # AltDSS_PyContext is not available.
    import dss_python_backend._func_info as _func_info

# Assumed UTF8; unless the fast C extension is not used, this now has no effect,
# but was left to avoid breaking it for downstream users.
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

    Currently, this also affects all Python packages from DSS-Extensions:
    
    - DSS-Python (`dss` package): done to allow easier migration from COM.
    
    - OpenDSSDirect.py (`opendssdirect` package): mostly done by accident due to the same base classes.

    - AltDSS-Python (`altdss` package): done to allow users to employ the 
      case-insensitive mechanism to address DSS properties in Python code.

    Since there is a small performance overhead, users are recommended to enable this
    mechanism during a transition period, before adjusting the code.
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

    elif getattr(Base, '__getattr__', None) == Base._getattr or getattr(Base, '__getattr__', None) == Base._getattr_case_check:
        del Base.__setattr__
        del Base.__getattr__


def _is_case_insensitive() -> bool:
    return (getattr(Base, '__getattr__', None) == Base._getattr or getattr(Base, '__getattr__', None) == Base._getattr_case_check)


# For backwards compatibility, will be removed for version 1.0
DssException = DSSException
use_com_compat = set_case_insensitive_attributes

class CtxLib:
    '''
    Exposes a CFFI Lib object pre-binding the DSSContext (`ctx`) object to the
    `ctx_*` functions, suppressing the `ctx_` prefix. This allows much simpler
    backwards compatibility.
    '''

    _CtxSettings_UseExceptions = 1 << 0
    _CtxSettings_AdvancedTypes = 1 << 1
    _CtxSettings_ODDPyStrings = 1 << 2 # TODO: check if we still need this with the new defaults
    _CtxSettings_UseLists = 1 << 3

    def get_float64_array(self, func, *args) -> Float64Array:
        ptr = self._ffi.new('double**')
        cnt = self._ffi.new('int32_t[4]')
        func(ptr, cnt, *args)
        res = np.frombuffer(self._ffi.buffer(ptr[0], cnt[0] * 8), dtype=np.float64).copy()
        self.DSS_Dispose_PDouble(ptr)

        if cnt[3] and (self.settings_ptr[0] & (1 << 1)): # self.advanced_types:
            # If the last element is filled, we have a matrix.  Otherwise, the 
            # matrix feature is disabled or the result is indeed a vector
            return res.reshape((cnt[2], cnt[3]), order='F')

        return res

    def get_complex128_array(self, func, *args) -> ComplexArray:
        if not (self.settings_ptr[0] & (1 << 1)): # self.advanced_types:
            return self.get_float64_array(func, *args)

        # Currently we use the same as API as get_float64_array, may change later
        ptr = self._ffi.new('double**')
        cnt = self._ffi.new('int32_t[4]')
        func(ptr, cnt, *args)
        res = np.frombuffer(self._ffi.buffer(ptr[0], cnt[0] * 8), dtype=complex).copy()
        self.DSS_Dispose_PDouble(ptr)

        if cnt[3]:
            # If the last element is filled, we have a matrix.  Otherwise, the 
            # matrix feature is disabled or the result is indeed a vector
            return res.reshape((cnt[2], cnt[3]), order='F')

        return res

    def get_fcomplex128_array(self, func, *args) -> Union[ComplexArray, None]:
        # Currently we use the same as API as get_float64_array, may change later
        ptr = self._ffi.new('double**')
        cnt = self._ffi.new('int32_t[4]')
        func(ptr, cnt, *args)
        if cnt[0] == 1: # empty
            res = None
        else:
            res = np.frombuffer(self._ffi.buffer(ptr[0], cnt[0] * 8), dtype=complex).copy()
        self.DSS_Dispose_PDouble(ptr)

        if cnt[3]:
            # If the last element is filled, we have a matrix.  Otherwise, the 
            # matrix feature is disabled or the result is indeed a vector
            return res.reshape((cnt[2], cnt[3]), order='F')

        return res

    # def get_complex128_array2(self, func, *args) -> ComplexArray:
    #     if not (self.settings_ptr[0] & (1 << 1)): # self.advanced_types:
    #         return self.get_float64_array2(func, *args)

    #     # Currently we use the same as API as get_float64_array, may change later
    #     ptr = self._ffi.new('double**')
    #     cnt = self._ffi.new('int32_t[4]')
    #     func(ptr, cnt, *args)
    #     ptr = self._ffi.cast('double _Complex **', ptr)
    #     res = self._unpack(ptr[0], cnt[0] >> 1)
    #     self.DSS_Dispose_PDouble(ptr)
    #     return res


    def get_complex128_simple(self, func, *args) -> Complex:
        if not (self.settings_ptr[0] & (1 << 1)): # self.advanced_types:
            return self.get_float64_array(func, *args)

        # Currently we use the same as API as get_float64_array, may change later
        ptr = self._ffi.new('double**')
        cnt = self._ffi.new('int32_t[4]')
        func(ptr, cnt, *args)
        try:
            assert cnt[0] == 2, ('Unexpected number of elements returned by API', cnt[0])
            return self._ffi.cast('double _Complex**', ptr)[0][0]
        finally:
            self.DSS_Dispose_PDouble(ptr)

    def get_fcomplex128_simple(self, func, *args) -> Complex:
        # Currently we use the same as API as get_float64_array, may change later
        ptr = self._ffi.new('double**')
        cnt = self._ffi.new('int32_t[4]')
        func(ptr, cnt, *args)
        try:
            assert cnt[0] == 2, ('Unexpected number of elements returned by API', cnt[0])
            return self._ffi.cast('double _Complex**', ptr)[0][0]
        finally:
            self.DSS_Dispose_PDouble(ptr)


    # def get_complex128_simple2(self, func, *args) -> List[Union[complex, float]]:
    #     if not (self.settings_ptr[0] & (1 << 1)): # self.advanced_types:
    #         return self.get_float64_array2(func, *args)

    #     # Currently we use the same as API as get_float64_array, may change later
    #     ptr = self._ffi.new('double**')
    #     cnt = self._ffi.new('int32_t[4]')
    #     func(ptr, cnt, *args)
    #     try:
    #         assert cnt[0] == 2, ('Unexpected number of elements returned by API', cnt[0])
    #         return self._ffi.cast('double _Complex**', ptr)[0][0]
    #     finally:
    #         self.DSS_Dispose_PDouble(ptr)


    def get_float64_gr_array(self) -> Float64Array:
        ptr, cnt = self.gr_float64_pointers
        settings = self.settings_ptr[0]
        if (settings & (1 << 3)): # self.prefer_lists:
            return self._unpack(ptr[0], cnt[0])
        if cnt[3] and (settings & (1 << 1)): # self.advanced_types:
            return np.frombuffer(self._ffi.buffer(ptr[0], cnt[0] * 8), dtype=np.float64).copy().reshape((cnt[2], cnt[3]), order='F')
        
        return np.frombuffer(self._ffi.buffer(ptr[0], cnt[0] * 8), dtype=np.float64).copy()


    def get_complex128_gr_array(self) -> ComplexArray:
        settings = self.settings_ptr[0]
        if not (settings & (1 << 1)): # self.advanced_types:
            return self.get_float64_gr_array()

        # Currently we use the same as API as get_float64_array, may change later
        ptr, cnt = self.gr_float64_pointers
        if (settings & (1 << 3)): # self.prefer_lists:
            ptr = self._ffi.cast('double _Complex **', ptr)
            return self._unpack(ptr[0], cnt[0] >> 1)

        if cnt[3] and (settings & (1 << 1)): # self.advanced_types:
            return np.frombuffer(self._ffi.buffer(ptr[0], cnt[0] * 8), dtype=complex).copy().reshape((cnt[2], cnt[3]), order='F')
        
        return np.frombuffer(self._ffi.buffer(ptr[0], cnt[0] * 8), dtype=complex).copy()


    def get_fcomplex128_gr_array(self) -> ComplexArray:
        # This one does not need to check "prefer_lists"
        # Currently we use the same as API as get_float64_array, may change later
        ptr, cnt = self.gr_float64_pointers
        if cnt[3] and (self.settings_ptr[0] & (1 << 1)): # self.advanced_types:
            return np.frombuffer(self._ffi.buffer(ptr[0], cnt[0] * 8), dtype=complex).copy().reshape((cnt[2], cnt[3]), order='F')
        
        return np.frombuffer(self._ffi.buffer(ptr[0], cnt[0] * 8), dtype=complex).copy()


    def get_complex128_gr_simple(self) -> Complex:
        if not (self.settings_ptr[0] & (1 << 1)): # self.advanced_types:
            return self.get_float64_gr_array()

        # Currently we use the same as API as get_float64_array, may change later
        ptr, cnt = self.gr_cfloat64_pointers
        assert cnt[0] == 2, ('Unexpected number of elements returned by API', cnt[0])
        return ptr[0][0]


    def get_fcomplex128_gr_simple(self) -> Complex:
        # Currently we use the same as API as get_float64_array, may change later
        ptr, cnt = self.gr_cfloat64_pointers
        assert cnt[0] == 2, ('Unexpected number of elements returned by API', cnt[0])
        return ptr[0][0]


    def get_int32_array(self, func: Callable, *args) -> Int32Array:
        ptr = self._ffi.new('int32_t**')
        cnt = self._ffi.new('int32_t[4]')
        func(ptr, cnt, *args)
        res = np.frombuffer(self._ffi.buffer(ptr[0], cnt[0] * 4), dtype=np.int32).copy()
        self.DSS_Dispose_PInteger(ptr)

        if cnt[3] and (self.settings_ptr[0] & (1 << 1)): # self.advanced_types:
            # If the last element is filled, we have a matrix.  Otherwise, the 
            # matrix feature is disabled or the result is indeed a vector
            return res.reshape((cnt[2], cnt[3]))

        return res


    def get_int32_gr_array(self) -> Int32Array:
        ptr, cnt = self.gr_int32_pointers
        settings = self.settings_ptr[0]
        if (settings & (1 << 3)): # self.prefer_lists:
            return self._unpack(ptr[0], cnt[0])
        if cnt[3] and (settings & (1 << 1)): # self.advanced_types:
            return np.frombuffer(self._ffi.buffer(ptr[0], cnt[0] * 4), dtype=np.int32).copy().reshape((cnt[2], cnt[3]))

        return np.frombuffer(self._ffi.buffer(ptr[0], cnt[0] * 4), dtype=np.int32).copy()


    def get_int8_array(self, func: Callable, *args: Any) -> Int8Array:
        ptr = self._ffi.new('int8_t**')
        cnt = self._ffi.new('int32_t[4]')
        func(ptr, cnt, *args)
        res = np.frombuffer(self._ffi.buffer(ptr[0], cnt[0] * 1), dtype=np.int8).copy()
        self.DSS_Dispose_PByte(ptr)

        if cnt[3] and (self.settings_ptr[0] & (1 << 1)): # self.advanced_types:
            # If the last element is filled, we have a matrix.  Otherwise, the 
            # matrix feature is disabled or the result is indeed a vector
            return res.reshape((cnt[2], cnt[3]))

        return res


    def get_int8_gr_array(self) -> Int8Array:
        ptr, cnt = self.gr_int8_pointers
        settings = self.settings_ptr[0]
        if (settings & (1 << 3)): # self.prefer_lists:
            return self._unpack(ptr[0], cnt[0])
        if cnt[3] and (settings & (1 << 1)): # self.advanced_types:
            return np.frombuffer(self._ffi.buffer(ptr[0], cnt[0] * 1), dtype=np.int8).copy().reshape((cnt[2], cnt[3]), order='F')

        return np.frombuffer(self._ffi.buffer(ptr[0], cnt[0] * 1), dtype=np.int8).copy()


    def get_string_array(self, func: Callable, *args: Any) -> List[str]:
        ptr = self._ffi.new('char***')
        cnt = self._ffi.new('int32_t[4]')
        func(ptr, cnt, *args)
        if not cnt[0]:
            res = []
        else:
            actual_ptr = ptr[0]
            if actual_ptr == self._ffi.NULL:
                res = []
            else:
                codec = self._api_util.codec
                str_ptrs = self._unpack(actual_ptr, cnt[0])
                #res = [(str(self._ffi.string(str_ptr).decode(codec)) if (str_ptr != self._ffi.NULL) else None) for str_ptr in str_ptrs]
                res = [(self._ffi.string(str_ptr).decode(codec) if (str_ptr != self._ffi.NULL) else u'') for str_ptr in str_ptrs]

        self.DSS_Dispose_PPAnsiChar(ptr, cnt[1])
        return res


    # def get_string_array2(self, func, *args): # for compatibility with OpenDSSDirect.py
    #     ptr = self._ffi.new('char***')
    #     cnt = self._ffi.new('int32_t[4]')
    #     func(ptr, cnt, *args)

    #     if not cnt[0]:
    #         res = []
    #     else:
    #         actual_ptr = ptr[0]
    #         if actual_ptr == self._ffi.NULL:
    #             res = []
    #         else:
    #             codec = self._api_util.codec
    #             res = [(str(self._ffi.string(actual_ptr[i]).decode(codec)) if (actual_ptr[i] != self._ffi.NULL) else '') for i in range(cnt[0])]
    #             if res == [u'']:
    #                 # most COM methods return an empty array as an
    #                 # array with an empty string
    #                 res = []

    #         if len(res) == 1 and res[0].lower() == 'none':
    #             res = []

    #     self.DSS_Dispose_PPAnsiChar(ptr, cnt[1])
    #     return res


    def get_float64_array2(self, func, *args):
        ptr = self._ffi.new('double**')
        cnt = self._ffi.new('int32_t[4]')
        func(ptr, cnt, *args)
        if not cnt[0]:
            res = []
        else:
            res = self._unpack(ptr[0], cnt[0])

        self.DSS_Dispose_PDouble(ptr)
        return res

    def get_int32_array2(self, func, *args):
        ptr = self._ffi.new('int32_t**')
        cnt = self._ffi.new('int32_t[4]')
        func(ptr, cnt, *args)
        if not cnt[0]:
            res = None
        else:
            res = self._unpack(ptr[0], cnt[0])

        self.DSS_Dispose_PInteger(ptr)
        return res

    # def get_int8_array2(self, func, *args):
    #     ptr = self._ffi.new('int8_t**')
    #     cnt = self._ffi.new('int32_t[4]')
    #     func(ptr, cnt, *args)
    #     if not cnt[0]:
    #         res = None
    #     else:
    #         res = self._unpack(ptr[0], cnt[0])

    #     self.DSS_Dispose_PByte(ptr)
    #     return res

    def _get_strs_ctx(self, errorPtr, ctx, func: Callable, *args: Any) -> List[str]:
        ffi = self._ffi
        codec = self._api_util.codec
        settings = self.settings_ptr[0]
        ptr = ffi.new('char***')
        cnt = ffi.new('int32_t[4]')
        func(ctx, ptr, cnt, *args)
        if errorPtr[0] and (settings & 1): # self.using_exceptions:
            error_num = errorPtr[0]
            errorPtr[0] = 0
            self.DSS_Dispose_PPAnsiChar(ptr, cnt[1])
            raise DSSException(error_num, self.Error_Get_Description())

        if not cnt[0]:
            res = []
        else:
            actual_ptr = ptr[0]
            if actual_ptr == ffi.NULL:
                res = []
            else:
                str_ptrs = ffi.unpack(actual_ptr, cnt[0])
                res = [(ffi.string(str_ptr).decode(codec) if (str_ptr) else '') for str_ptr in str_ptrs]

        if (settings & (1 << 2)): # self.oddpy_strs:
            # originally on get_string_array2, for compatibility with OpenDSSDirect.py
            if res == ['']:
                # most COM methods return an empty array as an
                # array with an empty string
                res = []

            if len(res) == 1 and res[0].lower() == 'none':
                res = []            

        self.DSS_Dispose_PPAnsiChar(ptr, cnt[1])
        return res


    def _get_bool_ctx(self, errorPtr, ctx, func: Callable, *args):
        result = bool(func(ctx, *args))
        if errorPtr[0] and self.using_exceptions:
            error_num = errorPtr[0]
            errorPtr[0] = 0
            raise DSSException(error_num, self.Error_Get_Description())
            
        return result != 0


    def _get_str_ctx(self, errorPtr, ctx, func: Callable, *args):
        codec = self._api_util.codec
        ffi = self._ffi
        result = func(ctx, *args)
        if errorPtr[0] and self.using_exceptions:
            error_num = errorPtr[0]
            errorPtr[0] = 0
            raise DSSException(error_num, self.Error_Get_Description())
            
        if result:
            return ffi.string(result).decode(codec)

        return ''


    def _str_arg_wrapper(self, f: Callable) -> Callable:
        @wraps(f)
        def f_wrapper(s, *args):
            if not isinstance(s, bytes):
                s = s.encode(self._api_util.codec)

            return f(s, *args)

        return f_wrapper


    def _prepare_api_functions_slow(self, done):
        '''
        Wrap the C functions with a Python-level function to converter
        strings and lists of strings from C.
        (slow in CPython) 
        '''
        ctx = self._ctx
        lib = self._lib
        errorPtr = self._errorPtr
        t = _func_info.t
        api_util = self._api_util
        is_oddie = api_util._is_oddie
        wrappers = {
            t.fastdss_types_u16: ('', self._get_bool_ctx,),
            t.fastdss_types_str: ('', self._get_str_ctx,),
            t.fastdss_types_strs: ('', self._get_strs_ctx,),
            t.fastdss_types_gr_f64s: ('_GR', self._error_checked_ctx_gr, self.get_float64_gr_array),
            t.fastdss_types_gr_i32s: ('_GR', self._error_checked_ctx_gr, self.get_int32_gr_array),
            t.fastdss_types_gr_i8s: ('_GR', self._error_checked_ctx_gr, self.get_int8_gr_array),
            t.fastdss_types_gr_z128: ('_GR', self._error_checked_ctx_gr, self.get_complex128_gr_simple),
            t.fastdss_types_gr_z128s: ('_GR', self._error_checked_ctx_gr, self.get_complex128_gr_array),
        }

        arg_no_wrapper = lambda f: f
        default_wrapper = ('', self._error_checked_ctx, )

        for res_type, arg_type, ctx_names in _func_info.funcs:
            arg_wrapper = arg_no_wrapper
            if arg_type == t.fastdss_types_str:
                arg_wrapper = self._str_arg_wrapper

            suffix, wrapper, *wrapper_args = wrappers.get(res_type, default_wrapper)
            for name in ctx_names:
                if name in done:
                    continue

                name += suffix
                if name in done:
                    continue

                try:
                    func = getattr(lib, name)
                except AttributeError:
                    if is_oddie:
                        continue
                        
                    raise
                
                prepared_func = arg_wrapper(partial(wrapper, errorPtr, ctx, func, *wrapper_args))
                setattr(self, name, prepared_func)

        done.update(vars(self).keys())


    def _prepare_api_functions(self, done, settings_ptr):
        self._settings_ptr = settings_ptr
        if AltDSS_PyContext is None:
            self._prepare_api_functions_slow(done)
            return

        ctx = self._ctx
        ffi = self._ffi
        ctx_int = int(ffi.cast('uintptr_t', ctx))
        lib_int = int(ffi.cast('uintptr_t', self._api_util.lib_unpatched))
        settings_ptr_int = int(ffi.cast('uintptr_t', self._settings_ptr))
        self._fast = AltDSS_PyContext(ctx_int, lib_int, settings_ptr_int, DSSException, done, self)

    def _error_checked(self, _errorPtr, f, *args):
        result = f(*args)
        if _errorPtr[0] and self.using_exceptions:
            error_num = _errorPtr[0]
            _errorPtr[0] = 0
            raise DSSException(error_num, self.Error_Get_Description())
            
        return result

    def _error_checked_ctx(self, _errorPtr, ctx, f, *args):
        result = f(ctx, *args)
        if _errorPtr[0] and self.using_exceptions:
            error_num = _errorPtr[0]
            _errorPtr[0] = 0
            raise DSSException(error_num, self.Error_Get_Description())
            
        return result

    def _error_checked_ctx_gr(self, _errorPtr, ctx, f, _res_func, *args):
        f(ctx, *args)
        if _errorPtr[0] and self.using_exceptions:
            error_num = _errorPtr[0]
            _errorPtr[0] = 0
            raise DSSException(error_num, self.Error_Get_Description())
            
        return _res_func()


    @property
    def using_exceptions(self) -> bool:
        return (self.settings_ptr[0] & CtxLib._CtxSettings_UseExceptions) != 0

    @using_exceptions.setter
    def using_exceptions(self, do_enable: bool):
        if do_enable:
            self.settings_ptr[0] = self.settings_ptr[0] | CtxLib._CtxSettings_UseExceptions
        else:
            self.settings_ptr[0] = self.settings_ptr[0] & ~CtxLib._CtxSettings_UseExceptions


    @property
    def prefer_lists(self) -> bool:
        return (self.settings_ptr[0] & CtxLib._CtxSettings_UseLists) != 0

    @prefer_lists.setter
    def prefer_lists(self, value: bool):
        settings_ptr = self.settings_ptr
        if value:
            settings_ptr[0] = settings_ptr[0] | CtxLib._CtxSettings_UseLists
        else:
            settings_ptr[0] = settings_ptr[0] & ~CtxLib._CtxSettings_UseLists


    @property
    def oddpy_strs(self) -> bool:
        return (self.settings_ptr[0] & CtxLib._CtxSettings_ODDPyStrings) != 0

    @oddpy_strs.setter
    def oddpy_strs(self, value: bool):
        settings_ptr = self.settings_ptr
        if value:
            settings_ptr[0] = settings_ptr[0] | CtxLib._CtxSettings_ODDPyStrings
        else:
            settings_ptr[0] = settings_ptr[0] & ~CtxLib._CtxSettings_ODDPyStrings



    @property
    def advanced_types(self) -> bool:
        return (self.settings_ptr[0] & CtxLib._CtxSettings_AdvancedTypes) != 0

    @advanced_types.setter
    def advanced_types(self, value: bool):
        settings_ptr = self.settings_ptr
        if value:
            settings_ptr[0] = settings_ptr[0] | CtxLib._CtxSettings_AdvancedTypes
        else:
            settings_ptr[0] = settings_ptr[0] & ~CtxLib._CtxSettings_AdvancedTypes

    def __init__(self, api_util, settings_ptr):
        self._api_util = api_util # this is not ready, don't use it yet
        lib = self._lib = api_util.lib_unpatched
        ctx = self._ctx = api_util.ctx
        ffi = self._ffi = api_util.ffi
        self._unpack = ffi.unpack
        self.settings_ptr = settings_ptr
        self.gr_float64_pointers = api_util.gr_float64_pointers
        self.gr_int32_pointers = api_util.gr_int32_pointers
        self.gr_int8_pointers = api_util.gr_int8_pointers
        self.gr_cfloat64_pointers = api_util.gr_cfloat64_pointers
        
        self._errorPtr = _errorPtr = lib.Error_Get_NumberPtr(ctx)
        #TODO: test if a pointer is better than keeping this
        self._prepared_funcs = []

        # Wrap most of the API to provide simpler Python access
        done = set(('Error_Get_Description', 'Error_Get_Number',))

        self._prepare_api_functions(done, settings_ptr)
        self.Error_Get_Description = lambda: self._api_util.get_string(lib.Error_Get_Description(ctx))
        self.Error_Get_Number = lambda: lib.Error_Get_Number(ctx)
        
        skip_funcs = {
            'ctx_New', 'ctx_Dispose', 'ctx_Get_Prime', 'ctx_Set_Prime', 'Error_Set_Description', 'Error_Get_NumberPtr', 'ctx_ZIP_Extract_GR',
            'DSS_BeginPascalThread', 'DSS_WaitPascalThread', 'DSS_SetPropertiesMO', 'DSS_SetMessagesMO',
            'engineName', 'isAltDSS', 'libHandle', 'versionSignature',
        }

        skip_prefixes = (
            'Oddie_', 'DSS_Dispose_', 'CmathLib_', 'DSSimComs_', 'Alt_', 'Obj_', 'Batch_',
        )

        force_include_prefixes = (
            'Batch_Create', 'Batch_Filter',
        )

        # First, process all `ctx_*` functions

        for name in dir(lib):
            if name in done:
                continue
            
            if name.startswith(skip_prefixes) and not name.startswith(force_include_prefixes):
                continue

            # Note: NULL function pointers here are fine since CFFI v1.13 (released in 2019).
            value = getattr(lib, name)

            # Keep the basic management functions alone
            if name in skip_funcs:
                if name.startswith('DSSEvents_') or name == 'Error_Set_Description':
                    setattr(self, name, partial(value, ctx))
                else:
                    setattr(self, name, value)

                done.add(name)
                continue

            if name.endswith('_GR'):
                # A few GR functions that don't have dedicated low-level mapping
                wrapper_func, res_func = self._error_checked_ctx_gr, self.get_float64_gr_array
                setattr(self, name, partial(wrapper_func, _errorPtr, ctx, value, res_func))
                done.add(name)
                continue

            # General functions and array setters are only error checked, no special handling yet
            setattr(self, name, partial(self._error_checked, _errorPtr, partial(value, ctx)))
            done.add(name)

        # Then the new Alt_* family
        for name in dir(lib):
            if (not name.startswith('Alt_')) or name in done: #TODO: What about Obj_ and Batch_?
                continue

            value = getattr(lib, name)

            if name.startswith('Alt_Bus'):
                setattr(self, name, partial(self._error_checked, _errorPtr, partial(value, ctx)))
            else:
                setattr(self, name, partial(self._error_checked, _errorPtr, value))

            done.add(name)

        # Finally the remaining fields
        for name in dir(lib):
            if name.startswith('ctx_') or name in done:
                continue

            setattr(self, name, getattr(lib, name))
            # if isinstance(value, int):
            #     setattr(self, name, value)
            # else:
            #     setattr(self, name, partial(self._error_checked, _errorPtr, value))


class Base:
    __slots__ = [
        '_lib',
        '_api_util',
        '_set_string_array',
        '_prepare_float64_array',
        '_prepare_int32_array',
        '_prepare_string_array',
        '_prepare_complex128_array',
        '_prepare_complex128_simple',
        '_errorPtr',
        '_frozen_attrs',
    ]

    using_exceptions = True
    _oddpy = False

    def __init__(self, api_util):
        object.__setattr__(self, '_frozen_attrs', False)
        self._api_util = api_util
        self._lib = api_util._get_lib(self._oddpy)

        self._prepare_complex128_array = api_util.prepare_complex128_array
        self._prepare_complex128_simple = api_util.prepare_complex128_simple
        self._set_string_array = api_util.set_string_array
        self._prepare_float64_array = api_util.prepare_float64_array
        self._prepare_int32_array = api_util.prepare_int32_array
        self._prepare_string_array = api_util.prepare_string_array
        self._errorPtr = self._api_util._errorPtr

        cls = type(self)
        if cls not in interface_classes:
            interface_classes.add(cls)
            cls._dss_original_attributes = {a for a in dir(self) if not a.startswith('_')}
            lowercase_map = {a.lower(): a for a in cls._dss_original_attributes}
            cls._dss_attributes = lowercase_map


    def _check_for_error(self, result=None):
        """
        Checks for a DSS engine error (on the default configuration).

        By default, raises an exception if any error is detected, otherwise returns the `result` parameter.
        
        If the user disabled exceptions, any error is simply ignored. Note that, in this case, manually
        calling this function would have no purpose/effects.

        Note that, **in the future**, we may try showing a popup form like EPRI's OpenDSS does on Windows
        if AllowForms is True. This behavior is not very portable though and not adequate for automated scripts.
        """
        if self._errorPtr[0] and Base.using_exceptions:
            error_num = self._errorPtr[0]
            self._errorPtr[0] = 0
            raise DSSException(error_num, self._lib.Error_Get_Description())
            
        return result

    def _getattr(self, key):
        if key[0] == '_':
            return object.__getattribute__(self, key)

        key = self.__class__._dss_attributes.get(key.lower(), key)
        return object.__getattribute__(self, key)

    def _getattr_case_check(self, key):
        if key[0] == '_':
            return object.__getattribute__(self, key)

        correct_key = self.__class__._dss_attributes.get(key.lower(), key)
        if key != correct_key:
            warnings.warn('Wrong capitalization for attribute (getter) {}.{}: {}'.format(self.__class__.__name__, correct_key, key), stacklevel=2)

        return object.__getattribute__(self, correct_key)

    def _setattr(self, key, value):
        if key[0] == '_':
            object.__setattr__(self, key, value)
            return

        key = self.__class__._dss_attributes.get(key.lower(), key)
        object.__setattr__(self, key, value)

    def _setattr_case_check(self, key, value):
        if key[0] == '_':
            object.__setattr__(self, key, value)
            return

        correct_key = self.__class__._dss_attributes.get(key.lower(), key)
        if key != correct_key:
            warnings.warn('Wrong capitalization for attribute (setter) {}.{}: {}'.format(self.__class__.__name__, correct_key, key))

        key = self.__class__._dss_attributes.get(key.lower(), key)
        object.__setattr__(self, key, value)

    def _decode_and_free_string(self, s) -> str:
        if s == self._ffi.NULL:
            return None

        res = self._ffi.string(s).decode(self._api_util.codec)
        self._lib.DSS_Dispose_String(s)
        self._check_for_error()
        return res


def altdss_python_util_callback(ctx, event_code, step, ptr):
    # print(ctx_util.ctx, AltDSSEvent(event_code), step, ptr)
    ctx_util = AltDSSAPIUtil._ctx_to_util[ctx]

    if event_code == AltDSSEvent.ReprocessBuses:
        ctx_util.reprocess_buses_callback(step)
        return

    if event_code == AltDSSEvent.Clear:
        ctx_util.clear_callback(step)
        return


class AltDSSAPIUtil:
    '''
    An internal class with various API and DSSContext management functions and structures.
    '''
    _ctx_to_util = WeakKeyDictionary()

    _altdss: AltDSS

    def __init__(self, ffi, lib, ctx=None, is_oddie=False, parent: Optional[AltDSSAPIUtil] = None):
        self._opendssdirect = None
        self._dss_python = None
        self._altdss = None
        self._is_oddie = is_oddie
        self.owns_ctx = True
        self.codec = codec
        self.ctx = ctx
        self.ffi = ffi
        self.lib_unpatched = lib
        self._batch_refs = []
        self._bus_refs = []
        self._obj_refs = []
        self._bus_ref_to_name = None
        self._is_clearing = False
        self._map_objs = True
        self._parent = parent
        if ctx is None:
            self.lib = lib
            ctx = lib.ctx_Get_Prime()
            self.ctx = ctx

        self.init_buffers()
        self.settings_ptr = settings_ptr_dsspy = ffi.new('int32_t*')

        # If a parent is provided, copy the settings
        if self._parent is None:
            settings_ptr_dsspy[0] = CtxLib._CtxSettings_UseExceptions
        else:
            settings_ptr_dsspy[0] = self._parent.settings_ptr[0]

        self.lib = CtxLib(self, settings_ptr_dsspy)
        self.lib_odd = None
        if ctx not in AltDSSAPIUtil._ctx_to_util:
            AltDSSAPIUtil._ctx_to_util[ctx] = self

        self.track_objects = True
        self.register_callbacks()
        if self._parent is None :
            self.lib_odd = None
        elif self._parent.lib_odd is not None:
            self.lib_odd = self._get_lib(True)


    def _get_lib(self, oddpy: bool):
        '''
        Returns a context lib, optionally prepared for OpenDSSDirect.py

        This should be removed as we unify settings across the modules later.
        '''
        if not oddpy: # and (AltDSS_PyContext is None):
            if self.lib is None:
                if self.settings_ptr is None:
                    self.settings_ptr = self.ffi.new('int32_t*')
                    if self._parent is not None:
                        self.settings_ptr[0] = self._parent.settings_ptr[0]
                    else:
                        self.settings_ptr[0] = self.settings_ptr[0] & ~CtxLib._CtxSettings_ODDPyStrings

                self.lib = CtxLib(self, self.settings_ptr)

            return self.lib

        # Check it the current lib is OK
        if self.lib_odd is not None:
            return self.lib_odd

        # Return a new lib object with the correct settings
        
        self.settings_oddpy_ptr = self.ffi.new('int32_t*')
        if self._parent is not None:
            self.settings_oddpy_ptr[0] = self._parent.settings_oddpy_ptr[0]
        else:
            self.settings_oddpy_ptr[0] = self.settings_ptr[0] | CtxLib._CtxSettings_ODDPyStrings

        self.lib_odd = CtxLib(self, self.settings_oddpy_ptr)
        return self.lib_odd


    def _check_for_error(self, result=None):
        """
        Checks for a DSS engine error (on the default configuration).

        By default, raises an exception if any error is detected, otherwise returns the `result` parameter.
        
        If the user disabled exceptions, any error is simply ignored. Note that, in this case, manually
        calling this function would have no purpose/effects.

        Note that, **in the future**, we may try showing a popup form like EPRI's OpenDSS does on Windows
        if AllowForms is True. This behavior is not very portable though and not adequate for automated scripts.
        """
        if self._errorPtr[0] and Base.using_exceptions:
            error_num = self._errorPtr[0]
            self._errorPtr[0] = 0
            raise DSSException(error_num, self.lib.Error_Get_Description())
            
        return result


    def reprocess_buses_callback(self, step: int):
        '''
        Used internally to remap buses to Python objects after the bus list is built.
        '''
        if self._is_clearing:
            return

        if step == 0:
            # Drop dead references
            self._bus_refs = [b for b in self._bus_refs if b() is not None]

            # Create a name to object dict, dropping the weakref wrapper
            self._bus_ref_to_name = [
                (b(), b().Name)
                for b in self._bus_refs
            ]
            return

        if step != 1:
            return
        
        # Now try to remap the objects; on exception, just invalidate everything
        try:
            ptrs = self.lib.Alt_Bus_GetListPtr()
            names = self.lib.Circuit_Get_AllBusNames()
        except:
            for bus_ref in self._bus_refs:
                bus_ref()._invalidate_ptr()

            self._bus_refs.clear()
            return

        self._bus_refs.clear()

        if len(names) == 0:
            # No buses to rebind, invalidate all
            for old_bus, _ in self._bus_ref_to_name:
                old_bus._invalidate_ptr()

            return

        name_to_new_ptr = {name: ptrs[idx] for idx, name in enumerate(names)}
        for old_bus, old_name in self._bus_ref_to_name:
            new_ptr = name_to_new_ptr.get(old_name)
            if new_ptr is None:
                # This bus was removed, just invalidate it
                old_bus._invalidate_ptr()
                continue

            # Successfully remapped the object to the live pointer, so keep a reference
            old_bus._ptr = new_ptr
            self._bus_refs.append(ref(old_bus))


    def clear_callback(self, step: int):
        if step == 0:
            # Mark that we're clearing
            self._is_clearing = True
            return

        if step != 1:
            return
        
        for bus_ref in self._bus_refs:
            bus = bus_ref()
            if bus is not None:
                bus._invalidate_ptr()

        for batch_ref in self._batch_refs:
            batch = batch_ref()
            if batch is not None:
                batch._invalidate_ptr()

        for obj_ref in self._obj_refs:
            obj = obj_ref()
            if obj is not None:
                obj._invalidate_ptr()

        self._batch_refs.clear()
        self._bus_refs.clear()
        self._obj_refs.clear()

        self._is_clearing = False


    def register_callbacks(self):
        if self._is_oddie:
            return

        mgr = get_manager_for_ctx(self.ctx)
        # if multiple calls, the extras are ignored
        mgr.register_func(AltDSSEvent.Clear, altdss_python_util_callback)
        mgr.register_func(AltDSSEvent.ReprocessBuses, altdss_python_util_callback)

    def unregister_callbacks(self):
        if self._is_oddie:
            return
        mgr = get_manager_for_ctx(self.ctx)
        mgr.unregister_func(AltDSSEvent.Clear, altdss_python_util_callback)
        mgr.unregister_func(AltDSSEvent.ReprocessBuses, altdss_python_util_callback)

    def __del__(self):
        # The base context itself will die, no need to do anything else currently. Callbacks for AltDSS need to be cleared.
        if self._is_oddie:
            return

        self.clear_callback(0)
        self.clear_callback(1)
        self.unregister_callbacks()

    #     self.lib.DSSEvents_UnregisterAlt(AltDSSEvent.Clear, self.lib_unpatched.altdss_python_util_callback)
    #     self.lib.DSSEvents_UnregisterAlt(AltDSSEvent.ReprocessBuses, self.lib_unpatched.altdss_python_util_callback)
    #     if self.ctx is None:
    #         return
             
    #     if self.lib.ctx_Get_Prime() != self.ctx and self.owns_ctx:
    #         self.lib.ctx_Dispose(self.ctx)

    def track_batch(self, batch):
        if self.track_objects:
            self._batch_refs.append(ref(batch))

    def track_bus(self, bus):
        if self.track_objects:
            self._bus_refs.append(ref(bus))

    def track_obj(self, obj):
        if self.track_objects:
            self._obj_refs.append(ref(obj))

    def init_buffers(self):
        lib = self.lib_unpatched
        tmp_float64_pointers = (self.ffi.new('double***'), self.ffi.new('int32_t**'))
        tmp_int32_pointers = (self.ffi.new('int32_t***'), self.ffi.new('int32_t**'))
        tmp_int8_pointers = (self.ffi.new('int8_t***'), self.ffi.new('int32_t**'))

        # reorder pointers so data pointers are first, count pointers last
        ptr_args = [
            ptr
            for ptrs in zip(tmp_float64_pointers, tmp_int32_pointers, tmp_int8_pointers)
            for ptr in ptrs
        ]
        lib.DSS_GetGRPointers(self.ctx, *ptr_args)

        # we don't need to keep the extra indirections
        self.gr_float64_pointers = (tmp_float64_pointers[0][0], tmp_float64_pointers[1][0])
        self.gr_int32_pointers = (tmp_int32_pointers[0][0], tmp_int32_pointers[1][0])
        self.gr_int8_pointers = (tmp_int8_pointers[0][0], tmp_int8_pointers[1][0])

        # also keep a casted version for complex floats
        self.gr_cfloat64_pointers = (self.ffi.cast('double _Complex**', tmp_float64_pointers[0][0]), tmp_float64_pointers[1][0])

        self._errorPtr = lib.Error_Get_NumberPtr(self.ctx)


    def clear_buffers(self):
        self.lib.DSS_DisposeGRData()
        self.lib.DSS_ResetStringBuffer()
        self.init_buffers()

    def get_string(self, b) -> str:
        if b:
            return self.ffi.string(b).decode(self.codec)
        return ''

    def get_ptr_array(self, func: Callable, *args):
        ptr = self.ffi.new('void***')
        cnt = self.ffi.new('int32_t[4]')
        func(ptr, cnt, *args)
        res = np.frombuffer(self.ffi.buffer(ptr[0], cnt[0] * np.dtype(np.uintp).itemsize), dtype=np.uintp).copy()
        self.lib.DSS_Dispose_PPointer(ptr)
        return res

    def set_string_array(self, func: Callable, value: List[AnyStr], *args):
        value, value_ptr, value_count = self.prepare_string_array(value)
        func(value_ptr, value_count, *args)

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


    def prepare_complex128_simple(self, value: Complex):
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
                if not isinstance(v, bytes):
                    v = v.encode(codec)
                    value_enc.append(v)

                ptrs.append(self.ffi.new("char[]", v))
            else:
                ptrs.append(self.ffi.NULL)

        # Need to keep reference to every pointer to they don't get
        # garbage collected too early
        return value_enc or value, ptrs, len(ptrs)


    def get_dss_obj(self, ptr) -> Optional[DSSObject]:
        '''
        Get an AltDSS DSSObj instance. For internal use, but might be useful for advanced users.
        The user must ensure the pointer is valid.
        '''
        if not ptr:
            return None

        from AltDSS import DSSObj
        if self._altdss is not None:
            altdss = self._altdss
        else:
            from AltDSS import AltDSS
            altdss = AltDSS._get_instance(ctx=self.ctx, api_util=self)
            
        cls_idx = self._lib.Obj_GetClassIdx(ptr)
        pycls = DSSObj._idx_to_cls[cls_idx]
        return pycls(self, ptr)

    def get_bus_obj(self, ptr) -> Optional[AltBus]:
        '''
        Get an AltDSS Bus instance. For internal use, but might be useful for advanced users.
        The user must ensure the pointer is valid.
        '''
        from AltDSS import Bus as AltBus
        if self._altdss is not None:
            altdss = self._altdss
        else:
            from AltDSS import AltDSS
            altdss = AltDSS._get_instance(ctx=self.ctx, api_util=self)

        return AltBus(self, ptr)            


def _oddie_not_impl():
    raise NotImplementedError("This API requires a function that is not implemented in EPRI's OpenDSS engine.")

class Iterable(Base):
    __slots__ = [
        '_Get_First',
        '_Get_Next',
        '_Get_Count',
        '_Get_AllNames',
        '_Get_Name',
        '_Set_Name',
        '_Get_idx',
        '_Set_idx',
        '_Get_Pointer',
    ]
    
    def __init__(self, api_util):
        Base.__init__(self, api_util)
        
        prefix = type(self).__name__[1:]
        self._Get_First = getattr(self._lib, '{}_Get_First'.format(prefix), _oddie_not_impl)
        self._Get_Next = getattr(self._lib, '{}_Get_Next'.format(prefix), _oddie_not_impl)
        self._Get_Count = getattr(self._lib, '{}_Get_Count'.format(prefix), _oddie_not_impl)
        self._Get_AllNames = getattr(self._lib, '{}_Get_AllNames'.format(prefix), _oddie_not_impl)
        self._Get_Name = getattr(self._lib, '{}_Get_Name'.format(prefix), _oddie_not_impl)
        self._Set_Name = getattr(self._lib, '{}_Set_Name'.format(prefix), _oddie_not_impl)
        self._Get_idx = getattr(self._lib, '{}_Get_idx'.format(prefix), _oddie_not_impl)
        self._Set_idx = getattr(self._lib, '{}_Set_idx'.format(prefix), _oddie_not_impl)
        self._Get_Pointer = getattr(self._lib, '{}_Get_Pointer'.format(prefix), _oddie_not_impl)

    @property
    def First(self) -> int:
        '''Sets the first object of this type active. Returns 0 if none.'''
        return self._Get_First()

    @property
    def Next(self) -> int:
        '''Sets next object of this type active. Returns 0 if no more.'''
        return self._Get_Next()

    @property
    def Count(self) -> int:
        '''Number of objects of this type'''
        return self._Get_Count()

    def __len__(self) -> int:
        return self._Get_Count()

    def __iter__(self) -> Iterator[Iterable]:
        '''
        Get an iterator of the object collection.
        
        Note that OpenDSS, via the classic APIs, only allow a single object of a specific type
        to be activated. That is, you cannot use references of distinct objects and interact
        with both at the same time, or keep a reference to use later. You need to reactivate
        the target object or ensure it is the active one.

        For an alternative, consider using our AltDSS-Python package.

        **(API Extension)**
        '''
        idx = self._Get_First()
        while idx != 0:
            yield self
            idx = self._Get_Next()

    @property
    def AllNames(self) -> List[str]:
        '''Array of all names of this object type'''
        return self._Get_AllNames()

    @property
    def Name(self) -> str:
        '''Gets the current name or sets the active object of this type by name'''
        return self._Get_Name()

    @Name.setter
    def Name(self, Value: AnyStr):
        self._Set_Name(Value)
        
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

        **(API Extension)** 
        '''
        return self._Get_idx()

    @idx.setter
    def idx(self, Value: int):
        self._Set_idx(Value)

    def to_altdss(self) -> DSSObject:
        '''
        Returns a Python object for the current active DSS object in this interface.

        Requires AltDSS-Python.

        *Available only for the AltDSS engine.*

        **(API Extension)**
        '''
        ptr = self._Get_Pointer()
        return self._api_util.get_dss_obj(ptr)


# For backwards compat
CffiApiUtil = AltDSSAPIUtil