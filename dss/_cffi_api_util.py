from __future__ import absolute_import
import numpy as np
import os

# The codec was changed to ASCII in version 0.10.0. 
# A rewrite of DSS C-API is expected to return UTF8Strings in the future
codec = 'ascii' #TODO: check which encoding FreePascal defaults to, on Linux

interface_classes = set()

def use_com_compat(value=True):
    if value:
        Base.__getattr__ = Base._getattr
        Base.__setattr__ = Base._setattr
    elif Base.__getattr__ == Base._getattr:
        del Base.__setattr__
        del Base.__getattr__ 
    
class Base(object):
    __slots__ = []
    
    def __init__(self):
        cls = type(self)
        if cls not in interface_classes:
            interface_classes.add(cls)
            cls._dss_original_attributes = {a for a in dir(self) if not a.startswith('_')}
            lowercase_map = {a.lower(): a for a in cls._dss_original_attributes}
            cls._dss_attributes = lowercase_map

    def _getattr(self, key):
        if key.startswith('_'):
            return object.__getattribute__(self, key)

        key = self.__class__._dss_attributes.get(key.lower(), key)
        return object.__getattribute__(self, key)

    def _setattr(self, key, value):
        key = self.__class__._dss_attributes.get(key.lower(), key)
        object.__setattr__(self, key, value)
    
    
class CffiApiUtil(object):
    def __init__(self, ffi, lib):
        self.ffi = ffi
        self.lib = lib
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
        

    def clear_buffers():
        self.lib.DSS_DisposeGRData()
        self.lib.DSS_ResetStringBuffer()

    def get_string(self, b):
        return self.ffi.string(b).decode(codec)

    def get_float64_array(self, func, *args):
        ptr = self.ffi.new('double**')
        cnt = self.ffi.new('int32_t[2]')
        func(ptr, cnt, *args)
        res = np.fromstring(self.ffi.buffer(ptr[0], cnt[0] * 8), dtype=np.float)
        self.lib.DSS_Dispose_PDouble(ptr)
        return res

    def get_float64_gr_array(self):
        ptr, cnt = self.gr_float64_pointers
        return np.fromstring(self.ffi.buffer(ptr[0], cnt[0] * 8), dtype=np.float)
        
    def get_int32_array(self, func, *args):
        ptr = self.ffi.new('int32_t**')
        cnt = self.ffi.new('int32_t[2]')
        func(ptr, cnt, *args)
        res = np.fromstring(self.ffi.buffer(ptr[0], cnt[0] * 4), dtype=np.int32)
        self.lib.DSS_Dispose_PInteger(ptr)
        return res
        
    def get_int32_gr_array(self):
        ptr, cnt = self.gr_int32_pointers
        return np.fromstring(self.ffi.buffer(ptr[0], cnt[0] * 4), dtype=np.int32)

    def get_int8_array(self, func, *args):
        ptr = self.ffi.new('int8_t**')
        cnt = self.ffi.new('int32_t[2]')
        func(ptr, cnt, *args)
        res = np.fromstring(self.ffi.buffer(ptr[0], cnt[0] * 1), dtype=np.int8)
        self.lib.DSS_Dispose_PByte(ptr)
        return res

    def get_int8_gr_array(self):
        ptr, cnt = self.gr_int8_pointers
        return np.fromstring(self.ffi.buffer(ptr[0], cnt[0] * 1), dtype=np.int8)
        
    def get_string_array(self, func, *args):
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
                str_ptrs = self.ffi.unpack(actual_ptr, cnt[0])
                #res = [(str(self.ffi.string(str_ptr).decode(codec)) if (str_ptr != self.ffi.NULL) else None) for str_ptr in str_ptrs]
                res = [(self.ffi.string(str_ptr).decode(codec) if (str_ptr != self.ffi.NULL) else None) for str_ptr in str_ptrs]

        self.lib.DSS_Dispose_PPAnsiChar(ptr, cnt[1])
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

    def get_float64_gr_array2(self):
        ptr, cnt = self.gr_float64_pointers
        return self.ffi.unpack(ptr[0], cnt[0])
        
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

    def get_int32_gr_array2(self):
        ptr, cnt = self.gr_int32_pointers
        return self.ffi.unpack(ptr[0], cnt[0])
        
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
        for v in value:
            if type(v) is not bytes:
                v = v.encode(codec)

            ptrs.append(self.ffi.new("char[]", v))

        # Need to keep reference to every pointer to they don't get
        # garbage collected too early
        return value, ptrs, len(ptrs)


