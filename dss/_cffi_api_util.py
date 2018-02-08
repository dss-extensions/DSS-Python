from __future__ import absolute_import
from ._dss_capi import lib, ffi
import numpy as np

freeze = True
_case_insensitive = False
codec = 'cp1252'

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
            if inspect.isclass(v) and issubclass(v, FrozenClass) and v != FrozenClass:
                lowercase_map = {a.lower(): a for a in dir(v) if not a.startswith('_')}
                v._dss_atributes = lowercase_map
                
    finally:
        freeze = old_freeze
    

# workaround to make a __slots__ equivalent restriction compatible with Python 2 and 3
class FrozenClass(object):
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
                raise TypeError( "%r is a frozen class" % self)
    
        if self._isfrozen and not hasattr(self, key):
            raise TypeError( "%r is a frozen class" % self )
            
        object.__setattr__(self, key, value)


def get_string(b):
    return ffi.string(b).decode(codec)
    
def get_float64_array(func, *args):
    ptr = ffi.new('double**')
    cnt = ffi.new('int32_t*')
    func(ptr, cnt, *args)
    if not cnt[0]:
        res = None
    else:
        res = np.frombuffer(ffi.buffer(ptr[0], cnt[0] * 8), dtype=np.float).copy()

    lib.DSS_Dispose_PDouble(ptr)
    return res
        
    
    
def get_int32_array(func, *args):
    ptr = ffi.new('int32_t**')
    cnt = ffi.new('int32_t*')
    func(ptr, cnt, *args)
    if not cnt[0]:
        res = None
    else:
        res = np.frombuffer(ffi.buffer(ptr[0], cnt[0] * 4), dtype=np.int32).copy()
    
    lib.DSS_Dispose_PInteger(ptr)
    return res
        
        
def get_int8_array(func, *args):
    ptr = ffi.new('int8_t**')
    cnt = ffi.new('int32_t*')
    func(ptr, cnt, *args)
    if not cnt[0]:
        res = None
    else:
        res = np.frombuffer(ffi.buffer(ptr[0], cnt[0] * 1), dtype=np.int8).copy()
    
    lib.DSS_Dispose_PByte(ptr)
    return res
    
        
def get_string_array(func, *args):
    ptr = ffi.new('char***')
    cnt = ffi.new('int32_t*')
    func(ptr, cnt, *args)
    if not cnt[0]:
        res = []
    else:
        actual_ptr = ptr[0]
        if actual_ptr == ffi.NULL:
            res = []
        else:
            res = [(str(ffi.string(actual_ptr[i]).decode(codec)) if (actual_ptr[i] != ffi.NULL) else None) for i in range(cnt[0])]
    
    lib.DSS_Dispose_PPAnsiChar(ptr, cnt[0])
    return res
    
    
    
def prepare_float64_array(value):
    if type(value) is not np.ndarray or value.dtype != np.float64:
        value = np.array(value, dtype=np.float64)
    
    ptr = ffi.cast('double*', ffi.from_buffer(data.data))
    cnt = data.size
    return value, ptr, cnt
   
def prepare_int32_array(value):
    if type(value) is not np.ndarray or value.dtype != np.int32:
        value = np.array(value, dtype=np.int32)
    
    ptr = ffi.cast('int32_t*', ffi.from_buffer(data.data))
    cnt = data.size
    return value, ptr, cnt
   

def prepare_string_array(value):
    raise NotImplementedError
   

# This might be useful for methods like Get_Channel that are exposed as Channel[] and Channel()
# def arrayfunc(func):
    # class ArrayFuncWrapper:
        # def __call__(self, v):
            # return func(self, v)
            
        # def __getitem__(self, v):
            # return func(self, v)

    # return ArrayFuncWrapper()

