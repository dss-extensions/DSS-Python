from __future__ import absolute_import
import numpy as np

freeze = True
_case_insensitive = False
codec = 'cp1252' #TODO: check which encoding FreePascal defaults to, on Linux

def use_com_compat(value=True):
    global _case_insensitive
    _case_insensitive = value

def prepare_com_compat(variables):
    global freeze

    import inspect
    old_freeze = freeze
    try:
        freeze = False
        for v in variables.values():
            if inspect.isclass(v) and issubclass(v, FrozenDssClass) and v != FrozenDssClass:
                v._dss_original_attributes = {a for a in dir(v) if not a.startswith('_')}

                lowercase_map = {a.lower(): a for a in v._dss_original_attributes}
                v._dss_atributes = lowercase_map

    finally:
        freeze = old_freeze


# workaround to make a __slots__ equivalent restriction compatible with Python 2 and 3
class FrozenDssClass(object):
    _isfrozen = False

    def __getattr__(self, key):
        if key.startswith('_'):
            return object.__getattribute__(self, key)

        if _case_insensitive:
            key = self._dss_atributes.get(key.lower(), key)

        return object.__getattribute__(self, key)


    def __setattr__(self, key, value):
        if _case_insensitive:
            okey = key
            key = self._dss_atributes.get(key.lower(), None)
            if key is None:
                raise TypeError("%r is a frozen class (attribute not found even ignoring case)" % self)

        if self._isfrozen and key not in self._dss_original_attributes:
            raise TypeError("%r is a frozen class" % self)

        object.__setattr__(self, key, value)



CACHE_PTR_STRING_VECTOR = 0
CACHE_PTR_DOUBLE_VECTOR = 1
CACHE_PTR_INT32_VECTOR = 2

class CffiApiUtil(object):
    def __init__(self, ffi, lib):
        self.cached_buffers = [(None, None), (None, None), (None, None)]

        self.ffi = ffi
        self.lib = lib

        ptr = self.ffi.new('char***')
        cnt = self.ffi.new('int32_t[2]') # ffi initializes this to 0
        self.cached_buffers[CACHE_PTR_STRING_VECTOR] = (ptr, cnt)

        ptr = self.ffi.new('double**')
        cnt = self.ffi.new('int32_t[2]')
        self.cached_buffers[CACHE_PTR_DOUBLE_VECTOR] = (ptr, cnt)

        ptr = self.ffi.new('int32_t**')
        cnt = self.ffi.new('int32_t[2]')
        self.cached_buffers[CACHE_PTR_INT32_VECTOR] = (ptr, cnt)



    def clear_buffers():
        ptr, cnt = self.cached_buffers.get(CACHE_PTR_STRING_VECTOR)
        if ptr:
            self.lib.DSS_Dispose_PPAnsiChar(ptr, cnt[1])

        ptr = self.ffi.new('char***')
        cnt = self.ffi.new('int32_t[2]') # ffi initializes this to 0
        self.cached_buffers[CACHE_PTR_STRING_VECTOR] = (ptr, cnt)


        ptr, cnt = self.cached_buffers.get(CACHE_PTR_DOUBLE_VECTOR)
        if ptr:
            self.lib.DSS_Dispose_PDouble(ptr)

        ptr = self.ffi.new('double**')
        cnt = self.ffi.new('int32_t[2]')
        self.cached_buffers[CACHE_PTR_DOUBLE_VECTOR] = (ptr, cnt)


        ptr, cnt = self.cached_buffers[CACHE_PTR_INT32_VECTOR]
        if ptr:
            self.lib.DSS_Dispose_PInteger(ptr)

        ptr = self.ffi.new('int32_t**')
        cnt = self.ffi.new('int32_t[2]')
        self.cached_buffers[CACHE_PTR_INT32_VECTOR] = (ptr, cnt)

    def get_string(self, b):
        return self.ffi.string(b).decode(codec)

    def get_float64_array(self, func, *args):
        ptr, cnt = self.cached_buffers[CACHE_PTR_DOUBLE_VECTOR]

        func(ptr, cnt, *args)
        if not cnt[0]:
            res = None
        else:
            res = np.frombuffer(self.ffi.buffer(ptr[0], cnt[0] * 8), dtype=np.float).copy()

        #self.lib.DSS_Dispose_PDouble(ptr)
        return res

    def get_int32_array(self, func, *args):
        ptr, cnt = self.cached_buffers[CACHE_PTR_INT32_VECTOR]
        func(ptr, cnt, *args)
        if not cnt[0]:
            res = None
        else:
            res = np.frombuffer(self.ffi.buffer(ptr[0], cnt[0] * 4), dtype=np.int32).copy()

        #self.lib.DSS_Dispose_PInteger(ptr)
        return res

    def get_int8_array(self, func, *args):
        ptr = self.ffi.new('int8_t**')
        cnt = self.ffi.new('int32_t[2]')
        func(ptr, cnt, *args)
        if not cnt[0]:
            res = None
        else:
            res = np.frombuffer(self.ffi.buffer(ptr[0], cnt[0] * 1), dtype=np.int8).copy()

        self.lib.DSS_Dispose_PByte(ptr)
        return res

    def get_string_array(self, func, *args):
        ptr, cnt = self.cached_buffers[CACHE_PTR_STRING_VECTOR]

        func(ptr, cnt, *args)
        if not cnt[0]:
            res = []
        else:
            actual_ptr = ptr[0]
            if actual_ptr == self.ffi.NULL:
                res = []
            else:
                res = [(str(self.ffi.string(actual_ptr[i]).decode(codec)) if (actual_ptr[i] != self.ffi.NULL) else None) for i in range(cnt[0])]

        #self.lib.DSS_Dispose_PPAnsiChar(ptr, cnt[1])
        return res

    def get_string_array2(self, func, *args): # for compatibility with OpenDSSDirect.py
        ptr = self.ffi.new('char***')
        cnt = self.ffi.new('int32_t[2]')
        func(ptr, cnt, *args)

        if not cnt[0]:
            res = []
        else:
            actual_ptr = ptr[0]
            if actual_ptr == self.ffi.NULL:
                res = []
            else:
                res = [(str(self.ffi.string(actual_ptr[i]).decode(codec)) if (actual_ptr[i] != self.ffi.NULL) else '') for i in range(cnt[0])]
                if res == ['']:
                    # most COM methods return an empty array as an
                    # array with an empty string
                    res = []

            if len(res) == 1 and res[0].lower() == 'none':
                res = []

        self.lib.DSS_Dispose_PPAnsiChar(ptr, cnt[1])
        return res

    def get_float64_array2(self, func, *args):
        ptr = self.ffi.new('double**')
        cnt = self.ffi.new('int32_t[2]')
        func(ptr, cnt, *args)
        if not cnt[0]:
            res = None
        else:
            res = self.ffi.unpack(ptr[0], cnt[0])

        self.lib.DSS_Dispose_PDouble(ptr)
        return res

    def get_int32_array2(self, func, *args):
        ptr = self.ffi.new('int32_t**')
        cnt = self.ffi.new('int32_t[2]')
        func(ptr, cnt, *args)
        if not cnt[0]:
            res = None
        else:
            res = self.ffi.unpack(ptr[0], cnt[0])

        self.lib.DSS_Dispose_PInteger(ptr)
        return res

    def get_int8_array2(self, func, *args):
        ptr = self.ffi.new('int8_t**')
        cnt = self.ffi.new('int32_t[2]')
        func(ptr, cnt, *args)
        if not cnt[0]:
            res = None
        else:
            res = self.ffi.unpack(ptr[0], cnt[0])

        self.lib.DSS_Dispose_PByte(ptr)
        return res


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
        for v in value:
            if type(v) is not bytes:
                v = v.encode(codec)

            ptrs.append(self.ffi.new("char[]", v))

        # Need to keep reference to every pointer to they don't get
        # garbage collected too early
        return value, ptrs, len(ptrs)


