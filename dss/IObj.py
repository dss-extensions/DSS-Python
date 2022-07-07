'''
This module exposes base objects for the pythonic Obj and Batch interfaces from DSS C-API.
These interfaces are unique to DSS Extensions, they are not present in the official OpenDSS.

Copyright (c) 2021-2022 Paulo Meira
Copyright (c) 2021-2022 DSS Extensions contributors
'''
from typing import Union, List, AnyStr
import numpy as np
import numpy.typing as npt
from .enums import DSSJSONFlags

try:
    from enum import IntEnum
except:
    from aenum import IntEnum

from ._cffi_api_util import Base

class BatchFloat64ArrayProxy:
    def __init__(self, batch, idx):
        self._batch = batch
        self._idx = idx
        self._lib = batch._api_util.lib

    def to_array(self):
        batch = self._batch
        return batch._get_float64_array(
            batch._lib.Batch_GetFloat64,
            batch.pointer[0],
            batch.count[0],
            self._idx
        )

    def __call__(self):
        return self.to_array()

    def __len__(self):
        return self._batch.count[0]

    def __mul__(self, other):
        return self.to_array() * other

    def __truediv__(self, other):
        return self.to_array() / other

    def __floordiv__(self, other):
        return self.to_array() // other

    def __add__(self, other):
        return self.to_array() + other

    def __sub__(self, other):
        return self.to_array() - other

    def __array__(self):
        return self.to_array()

    def __iadd__(self, other):
        batch = self._batch

        if np.isscalar(other):
            self._lib.Batch_Float64(
                batch.pointer[0], 
                batch.count[0],
                self._idx,
                self._lib.BatchOperation_Increment,
                other
            )
            return self

        if len(other) != batch.count[0]:
            raise ValueError(f"Number of elements ({len(other)}) doesn't match the batch size ({batch.count[0]})")

        data = self.to_array() + other
        data, data_ptr, _ = batch._prepare_float64_array(data)
        batch._lib.Batch_SetFloat64Array(
            batch.pointer[0], 
            batch.count[0], 
            self._idx,
            data_ptr
        )
        batch._check_for_error()
        return self

    def __isub__(self, other):
        return self.__iadd__(-other)

    def __imul__(self, other):
        batch = self._batch

        if np.isscalar(other):
            self._lib.Batch_Float64(
                batch.pointer[0], 
                batch.count[0], 
                self._idx,
                self._lib.BatchOperation_Multiply,
                other
            )
            return self

        if len(other) != batch.count[0]:
            raise ValueError(f"Number of elements ({len(other)}) doesn't match the batch size ({batch.count[0]})")

        data = self.to_array() * other
        data, data_ptr, _ = batch._prepare_float64_array(data)
        self._lib.Batch_SetFloat64Array(
            batch.pointer[0], 
            batch.count[0], 
            data_ptr
        )
        batch._check_for_error()
        return self

    def __idiv__(self, other):
        batch = self._batch

        if np.isscalar(other):
            self._lib.Batch_Float64(
                batch.pointer[0], 
                batch.count[0], 
                self._idx,
                self._lib.BatchOperation_Multiply,
                1 / other
            )
            return self

        if len(other) != batch.count[0]:
            raise ValueError(f"Number of elements ({len(other)}) doesn't match the batch size ({batch.count[0]})")

        data = self.to_array() / other
        data, data_ptr, _ = batch._prepare_float64_array(data)
        self._lib.Batch_SetFloat64Array(
            batch.pointer[0], 
            batch.count[0], 
            data_ptr
        )
        batch._check_for_error()
        return self


class BatchInt32ArrayProxy:
    def __init__(self, batch, idx):#, kind):
        self._batch = batch
        self._idx = idx
        self._lib = batch._api_util.lib

    def to_array(self):
        batch = self._batch
        return batch._get_int32_array(
            batch._lib.Batch_GetInt32,
            batch.pointer[0],
            batch.count[0],
            self._idx
        )

    def __call__(self):
        return self.to_array()

    def __len__(self):
        return self._batch.count[0]

    def __mul__(self, other):
        return self.to_array() * other

    def __truediv__(self, other):
        return self.to_array() / other

    def __floordiv__(self, other):
        return self.to_array() // other
    
    def __add__(self, other):
        return self.to_array() + other

    def __sub__(self, other):
        return self.to_array() - other

    def __array__(self):
        return self.to_array()

    def __iadd__(self, other):
        batch = self._batch

        if np.isscalar(other):
            self._lib.Batch_Int32(
                batch.pointer[0], 
                batch.count[0], 
                self._idx,
                self._lib.BatchOperation_Increment,
                other
            )
            return self

        if len(other) != batch.count[0]:
            raise ValueError(f"Number of elements ({len(other)}) doesn't match the batch size ({batch.count[0]})")

        data = self.to_array() + other
        data, data_ptr, _ = batch._api_util.prepare_int32_array(data)
        batch._lib.Batch_SetInt32Array(
            batch.pointer[0], 
            batch.count[0],
            self._idx,
            data_ptr
        )
        batch._check_for_error()
        return self

    def __isub__(self, other):
        return self.__iadd__(-other)

    def __imul__(self, other):
        batch = self._batch

        if np.isscalar(other):
            self._lib.Batch_Int32(
                batch.pointer[0], 
                batch.count[0],
                self._idx,
                self._lib.BatchOperation_Multiply,
                other
            )
            return self

        if len(other) != batch.count[0]:
            raise ValueError(f"Number of elements ({len(other)}) doesn't match the batch size ({batch.count[0]})")

        data = self.to_array() * other
        data, data_ptr, _ = batch._prepare_int32_array(data)
        self._lib.Batch_SetInt32Array(
            batch.pointer[0], 
            batch.count[0], 
            data_ptr
        )
        batch._check_for_error()
        return self

    def __idiv__(self, other):
        batch = self._batch

        if np.isscalar(other):
            self._lib.Batch_Int32(
                batch.pointer[0], 
                batch.count[0],
                self._idx,
                self._lib.BatchOperation_Multiply,
                1 / other
            )
            return self

        if len(other) != batch.count[0]:
            raise ValueError(f"Number of elements ({len(other)}) doesn't match the batch size ({batch.count[0]})")

        data = self.to_array() / other
        data, data_ptr, _ = batch._prepare_int32_array(data)
        self._lib.Batch_SetInt32Array(
            batch.pointer[0], 
            batch.count[0], 
            data_ptr
        )
        batch._check_for_error()
        return self



class DSSObj(Base):
    # _properties_by_idx = {
    #     1: ('kV', 'Obj_SetDouble')
    # }
    # _properties_by_name = {
    #     'kV': (1, 'Obj_SetDouble')
    # }

    def __init__(self, api_util, ptr):
        Base.__init__(self, api_util)
        self._ptr = ptr
        self._ffi = api_util.ffi
        self._get_int32_list = api_util.get_int32_array2

    # def __getitem__(self, name_or_idx):
    #     if isinstance(name_or_idx, int):
    #         funcname, *_ = self._properties_by_idx[name_or_idx]
    #         return getattr(self._lib, funcname)(name_or_idx)

    #     if type(name_or_idx) is bytes:
    #         name_or_idx = name_or_idx.decode(self._api_util.codec)

    #     idx, funcname, *_ = self._properties_by_name[name_or_idx]
    #     return getattr(self._lib, funcname)(idx)

    # def to_dict(self):
    #     return {
    #         name: getattr(self._lib, funcname)(idx)
    #         for (name, (idx, funcname, *_)) in self._properties_by_name.items()
    #     }

    def to_json(self, options: Union[int, DSSJSONFlags] = 0):
        '''
        Returns an element's data as a JSON-encoded string.

        The `options` parameter contains bit-flags to toggle specific features.

        By default (`options = 0`), only the properties explicitly set. The properties are returned in the order they are set in the input.
        As a reminder, OpenDSS is sensitive to the order of the properties.

        The `options` bit-flags are available in the `DSSJSONFlags` enum.
        Values used by this function are:

        - `Full`: if set, all properties are returned, ordered by property index instead.
        - `SkipRedundant`: if used with `Full`, all properties except redundant and unused ones are returned.
        - `EnumAsInt`: enumerated properties are returned as integer values instead of strings.
        - `FullNames`: any element reference will use the full name (`{class name}.{element name}`) even if not required.
        - `Pretty`: more whitespace is used in the output for a "prettier" format.

        **NOT IMPLEMENTED YET**:
        - `State`: include run-time state information
        - `Debug`: include debug information

        Other bit-flags are reserved for future uses. Please use `DSSJSONFlags` enum to avoid potential conflicts.

        (API Extension)
        '''
        s = self._lib.Obj_ToJSON(self._ptr, options)
        self._check_for_error()
        return self._ffi.string(s).decode(self._api_util.codec)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and (other._ptr == self._ptr)

    def __repr__(self):
        # This could probably be done in DSS C-API instead (equivalent to SaveWrite)
        ffi = self._api_util.ffi
        # seq = sorted(enumerate(ffi.unpack(self._lib.Obj_GetPropSeqPtr(self._ptr, ffi.NULL), self._lib.Obj_GetNumProperties(self._ptr)), start=1), key=lambda v: v[1])
        # vals = []
        # for propidx, propseq in seq:
        #     if propseq:
        #         vals.append(f'{self._properties_by_idx[propidx][0]}={self[propidx]}')

        return f'<{self._cls_name}.{self.name}>'# {" ".join(vals)}'

    @property
    def name(self) -> str:
        s = self._lib.Obj_GetName(self._ptr)
        self._check_for_error()
        return self._ffi.string(s).decode(self._api_util.codec)

    def _get_complex(self, idx: int) -> complex:
        return self._get_float64_array(
            self._lib.Obj_GetFloat64Array, 
            self._ptr,
            idx
        ).astype(complex)[0]

    def _set_complex(self, idx: int, value: complex):
        data = np.array([complex(value)])
        data, data_ptr, cnt_ptr = self._prepare_float64_array(data)
        self._lib.Obj_SetFloat64Array(self._ptr, data_ptr, cnt_ptr)
        self._check_for_error()

    def _get_prop_string(self, idx: int) -> str:
        s = self._lib.Obj_GetString(self._ptr, idx)
        return self._decode_and_free_string(s)

    def _set_string(self, idx: int, value: AnyStr):
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Obj_SetString(self._ptr, idx, value)
        self._check_for_error()

    def _set_float64_array(self, idx: int, value: npt.NDArray[np.float64]):
        value, value_ptr, value_count = self._prepare_float64_array(value)
        self._lib.Obj_SetFloat64Array(self._ptr, idx, value_ptr, value_count)
        self._check_for_error()

    def _set_int32_array(self, idx: int, value: npt.NDArray[np.int32]):
        value, value_ptr, value_count = self._prepare_int32_array(value)
        self._lib.Obj_SetInt32Array(self._ptr, idx, value_ptr, value_count)
        self._check_for_error()

    def _set_string_array(self, idx: int, value: List[AnyStr]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, idx, value_ptr, value_count)
        self._check_for_error()

    def _get_obj(self, idx: int, pycls):
        other_ptr = self._lib.Obj_GetObject(self._ptr, idx)
        self._check_for_error()
        if other_ptr == self._ffi.NULL:
            return None

        if pycls is None:
            cls_idx = self._lib.Obj_GetClassIdx(other_ptr)
            pycls = self._iobj._idx_to_cls[cls_idx]

        return pycls(self._api_util, other_ptr)

    def _set_obj(self, idx: int, other):
        if other is not None:
            other_ptr = other._ptr
        else:
            other_ptr = self._ffi.NULL

        self._lib.Obj_SetObject(self._ptr, idx, other_ptr)
        self._check_for_error()

    def _get_obj_array(self, idx: int, pycls):
        ptr = self._ffi.new('void***')
        cnt = self._ffi.new('int32_t[2]')
        self._lib.Obj_GetObjectArray(ptr, cnt, self._ptr, idx)
        if not cnt[0]:
            self._lib.DSS_Dispose_PPointer(ptr)
            self._check_for_error()
            return []

        # wrap the results with Python classes
        if pycls is None:
            res = []
            for other_ptr in self._ffi.unpack(ptr[0], cnt[0]):
                cls_idx = self._lib.Obj_GetClassIdx(other_ptr)
                pycls = self._iobj._idx_to_cls[cls_idx]
                res.append(pycls(self._api_util, other_ptr))
        else:
            res = [
                pycls(self._api_util, other_ptr)
                for other_ptr in self._ffi.unpack(ptr[0], cnt[0])
            ]

        self._lib.DSS_Dispose_PPointer(ptr)
        self._check_for_error()
        return res

    def _set_obj_array(self, idx: int, other):
        if other is None or not other:
            other_ptr = self._ffi.NULL
            other_cnt = 0
        else:
            other_cnt = len(other)
            other_ptr = self.ffi.new('void*[]', other_cnt)
            other_ptr[:] = [o._ptr for o in other]
            
        self._lib.Obj_SetObjectArray(self._ptr, idx, other_ptr, other_cnt)
        self._check_for_error()        


class DSSBatch(Base):

    #TODO: keep property name for debugging? Or maybe use from the parent object

    def __init__(self, api_util, **kwargs):
        if len(kwargs) > 1:
            raise ValueError('Exactly one argument is expected.')
        
        Base.__init__(self, api_util)
        self._ffi = api_util.ffi

        self.pointer = self._ffi.new('void***')
        self.count = self._ffi.new('int32_t[2]')
        if len(kwargs) == 0:
            self._lib.Batch_CreateByClass(self.pointer, self.count, self._cls_idx)
            self._check_for_error()
            return
            
        regexp = kwargs.get('re')
        if regexp is not None:
            if not isinstance(regexp, bytes):
                regexp = regexp.encode(self._api_util.codec)

            self._lib.Batch_CreateByRegExp(self.pointer, self.count, self._cls_idx, regexp)
            self._check_for_error()
            return

        idx = kwargs.get('idx')
        if regexp is not None:
            idx, idx_ptr, idx_cnt = self._prepare_int32_array(idx)
            self._lib.Batch_CreateByIndex(self.pointer, self.count, self._cls_idx, idx_ptr, idx_cnt)
            self._check_for_error()
            return

        (prop_name, intval), = kwargs.items()
        prop_idx = self._obj_cls._cls_prop_idx.get(prop_name.lower())
        if prop_idx is None:
            raise ValueError('Invalid property name "{}"'.format(prop_name))
        self._lib.Batch_CreateByInt32Property(self.pointer, self.count, self._cls_idx, prop_idx, intval)
        self._check_for_error()

    def to_json(self, options: Union[int, DSSJSONFlags] = 0):
        '''
        Returns the data (as a list) of the elements in a batch as a JSON-encoded string.

        The `options` parameter contains bit-flags to toggle specific features.
        See `Obj_ToJSON` (C-API) for more, or `DSSObj.to_json` in Python.
        
        Additionally, the `ExcludeDisabled` flag can be used to excluded disabled elements from the output.

        (API Extension)
        '''
        s = self._lib.Batch_ToJSON(self.pointer[0], self.count[0], options)
        self._check_for_error()
        return self._ffi.string(s).decode(self._api_util.codec)

    def __eq__(self, other):
        return self is other

    def __len__(self):
        if self.count is None or self.count == self._ffi.NULL:
            return 0

        return self.count[0]

    def __iter__(self):
        for ptr in self._ffi.unpack(self.pointer[0], self.count[0]):
            yield self._obj_cls(self._api_util, ptr)

    def __getitem__(self, idx0):
        #TODO: decide if we keep it 0-based or 1-based here
        '''Get element at 0-based index of the batch pointer array'''
        if idx0 >= len(self) or idx0 < 0:
            raise IndexError

        ptr = self.pointer[0][idx0]
        return self._obj_cls(self._api_util, ptr)

    def _set_batch_float64_array(self, idx: int, value):
        if isinstance(value, BatchFloat64ArrayProxy):
            if self is value._batch and value._idx == idx:
                # ignore if we're setting to property to itself
                return

            value = value.to_array()

        if np.isscalar(value):
            self._lib.Batch_Float64(
                self.pointer[0], 
                self.count[0], 
                idx,
                self._lib.BatchOperation_Set,
                value
            )
            return

        data, data_ptr, data_cnt = self._prepare_float64_array(value)
        if data_cnt != self.count[0]:
            raise ValueError("Number of elements must match")

        self._lib.Batch_SetFloat64Array(
            self.pointer[0], 
            self.count[0], 
            data_ptr,
            idx
        )


    def _set_batch_int32_array(self, idx: int, value):
        if isinstance(value, BatchInt32ArrayProxy):
            if self is value._batch and value._idx == idx:
                # ignore if we're setting to property to itself
                return

            value = value.to_array()

        if np.isscalar(value):
            self._lib.Batch_Int32(
                self.pointer[0], 
                self.count[0], 
                idx,
                self._lib.BatchOperation_Set,
                value
            )
            return
        
        data, data_ptr, data_cnt = self._prepare_float64_array(value)
        if data_cnt != self.count[0]:
            raise ValueError("Number of elements must match")

        self._lib.Batch_SetInt32Array(
            self.pointer[0], 
            self.count[0], 
            data_ptr,
            idx
        )

    def _set_batch_string(self, idx: int, value: AnyStr):
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], idx, value)

    def _set_batch_obj(self, idx: int, other):
        if other is not None:
            other_ptr = other._ptr
        else:
            other_ptr = self._ffi.NULL

        self._lib.Batch_SetObject(self.pointer[0], self.count[0], idx, other_ptr)
        self._check_for_error()


    def _get_string_ll(self, idx: int):
        return [   
            self._get_string_array(self._lib.Obj_GetStringArray, x, idx) 
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]


    @property
    def name(self) -> List[str]:
        res = [
            self._ffi.string(self._lib.Obj_GetName(ptr)).decode(self._api_util.codec)
            for ptr in self._ffi.unpack(self.pointer[0], self.count[0])
        ]
        self._check_for_error()
        return res
        

    def _get_batch_obj_array(self, idx: int, pycls):
        if self.count[0] == 0:
            return []

        obj = self._obj_cls(self._api_util, self.pointer[0])
        res = []
        for ptr in self._ffi.unpack(self.pointer[0], self.count[0]):
            obj._ptr = ptr
            res.append(obj._get_obj_array(idx, pycls))

        return res

    def _set_batch_obj_array(self, idx: int, other):
        if self.count[0] == 0:
            return

        if other is None or not other:
            other_ptr = self._ffi.NULL
            other_cnt = 0
            self._lib.Batch_SetObjectArray(self.pointer[0], self.count[0], idx, other_ptr, other_cnt)
            self._check_for_error()
            return
        elif isinstance(other[0], DSSObj):
            other_ptr = self.ffi.new('void*[]', len(other))
            other_ptr[:] = [o._ptr for o in other]
            self._lib.Batch_SetObjectArray(self.pointer[0], self.count[0], idx, other_ptr, len(other))
            return            

        obj = self._obj_cls(self._api_util, self.pointer[0])
        res = []
        for other_objs, ptr in zip(other, self._ffi.unpack(self.pointer[0], self.count[0])):
            # this could be optimized to reuse the pointers, but it's not usually in
            # the hot path
            obj._ptr = ptr
            obj._set_obj_array(idx, other_objs)


class IDSSObj(Base):
    def __init__(self, iobj, cls_idx, obj_cls, batch_cls):
        Base.__init__(self, iobj._api_util)
        self._iobj = iobj
        self.cls_idx = cls_idx
        self._obj_cls = obj_cls
        self._batch_cls = batch_cls
        iobj._idx_to_cls[cls_idx] = self

    def batch(self, **kwargs):
        '''
        Creates a new batch hanlder of (existing) objects
        '''
        return self._batch_cls(self._api_util, **kwargs)

    def new(self, name: str, begin_edit=True, activate=False):
        if not isinstance(name, bytes):
            name = name.encode(self._api_util.codec)

        ptr = self._api_util.lib.Obj_New(
            self._api_util.ctx,
            self.cls_idx,
            name,
            activate,
            begin_edit
        )

        if ptr == self._api_util.ffi.NULL:
            raise ValueError('Could not create object "{}".'.format(name))

        return self._obj_cls(self._api_util, ptr)

    def find(self, name_or_idx):
        lib = self._lib

        if isinstance(name_or_idx, int):
            ptr = lib.Obj_GetHandleByIdx(self._api_util.ctx, self.cls_idx, name_or_idx)
            if ptr == self._api_util.ffi.NULL:
                raise ValueError('Could not find object by index "{}".'.format(name_or_idx))
        else:
            if type(name_or_idx) is not bytes:
                name_or_idx = name_or_idx.encode(self._api_util.codec)
            
            ptr = lib.Obj_GetHandleByName(self._api_util.ctx, self.cls_idx, name_or_idx)
            if ptr == self._api_util.ffi.NULL:
                raise ValueError('Could not find object by name "{}".'.format(name_or_idx))

        return self._obj_cls(self._api_util, ptr)

    def __len__(self):
        return self._lib.Obj_GetCount(self._api_util.ctx, self.cls_idx)

    def __iter__(self):
        for idx in range(len(self)):
            ptr = self._lib.Obj_GetHandleByIdx(self._api_util.ctx, self.cls_idx, idx + 1)
            yield self._obj_cls(self._api_util, ptr)

    def __getitem__(self, name_or_idx):
        return self.find(name_or_idx)


# Global enumerations
class EarthModel(IntEnum):
    """Earth Model (DSS enumeration)"""
    Carson = 1 # Carson
    FullCarson = 2 # FullCarson
    Deri = 3 # Deri

class LineType(IntEnum):
    """Line Type (DSS enumeration)"""
    oh = 1 # oh
    ug = 2 # ug
    ug_ts = 3 # ug_ts
    ug_cn = 4 # ug_cn
    swt_ldbrk = 5 # swt_ldbrk
    swt_fuse = 6 # swt_fuse
    swt_sect = 7 # swt_sect
    swt_rec = 8 # swt_rec
    swt_disc = 9 # swt_disc
    swt_brk = 10 # swt_brk
    swt_elbow = 11 # swt_elbow

class DimensionUnits(IntEnum):
    """Dimension Units (DSS enumeration)"""
    none = 0 # none
    mi = 1 # mi
    kft = 2 # kft
    km = 3 # km
    m = 4 # m
    ft = 5 # ft
    inch = 6 # in
    cm = 7 # cm
    mm = 8 # mm
    meter = 4 # meter
    miles = 1 # miles

class ScanType(IntEnum):
    """Scan Type (DSS enumeration)"""
    none = -1 # None
    Zero = 0 # Zero
    Positive = 1 # Positive

class SequenceType(IntEnum):
    """Sequence Type (DSS enumeration)"""
    Negative = -1 # Negative
    Zero = 0 # Zero
    Positive = 1 # Positive

class Connection(IntEnum):
    """Connection (DSS enumeration)"""
    wye = 0 # wye
    delta = 1 # delta
    y = 0 # y
    ln = 0 # ln
    ll = 1 # ll

class CoreType(IntEnum):
    """Core Type (DSS enumeration)"""
    shell = 0 # shell
    one_phase = 1 # 1-phase
    three_leg = 3 # 3-leg
    four_leg = 4 # 4-leg
    five_leg = 5 # 5-leg
    core_1_phase = 9 # core-1-phase

class PhaseSequence(IntEnum):
    """Phase Sequence (DSS enumeration)"""
    Lag = 0 # Lag
    Lead = 1 # Lead
    ANSI = 0 # ANSI
    Euro = 1 # Euro

class LoadSolutionModel(IntEnum):
    """Load Solution Model (DSS enumeration)"""
    PowerFlow = 1 # PowerFlow
    Admittance = 2 # Admittance

class RandomType(IntEnum):
    """Random Type (DSS enumeration)"""
    none = 0 # None
    Gaussian = 1 # Gaussian
    Uniform = 2 # Uniform
    LogNormal = 3 # LogNormal

class ControlMode(IntEnum):
    """Control Mode (DSS enumeration)"""
    Off = -1 # Off
    Static = 0 # Static
    Event = 1 # Event
    Time = 2 # Time
    MultiRate = 3 # MultiRate

class SolutionMode(IntEnum):
    """Solution Mode (DSS enumeration)"""
    Snap = 0 # Snap
    Daily = 1 # Daily
    Yearly = 2 # Yearly
    M1 = 3 # M1
    LD1 = 4 # LD1
    PeakDay = 5 # PeakDay
    DutyCycle = 6 # DutyCycle
    Direct = 7 # Direct
    MF = 8 # MF
    FaultStudy = 9 # FaultStudy
    M2 = 10 # M2
    M3 = 11 # M3
    LD2 = 12 # LD2
    AutoAdd = 13 # AutoAdd
    Dynamic = 14 # Dynamic
    Harmonic = 15 # Harmonic
    Time = 16 # Time
    HarmonicT = 17 # HarmonicT
    Snapshot = 0 # Snapshot

class SolutionAlgorithm(IntEnum):
    """Solution Algorithm (DSS enumeration)"""
    Normal = 0 # Normal
    Newton = 1 # Newton

class CircuitModel(IntEnum):
    """Circuit Model (DSS enumeration)"""
    Multiphase = 0 # Multiphase
    Positive = 1 # Positive

class AutoAddDeviceType(IntEnum):
    """AutoAdd Device Type (DSS enumeration)"""
    Generator = 1 # Generator
    Capacitor = 2 # Capacitor

class LoadShapeClass(IntEnum):
    """Load Shape Class (DSS enumeration)"""
    none = -1 # None
    Daily = 0 # Daily
    Yearly = 1 # Yearly
    Duty = 2 # Duty

class MonitoredPhase(IntEnum):
    """Monitored Phase (DSS enumeration)"""
    min = -3 # min
    max = -2 # max
    avg = -1 # avg


class LineCode(DSSObj):
    _cls_name = 'LineCode'
    _cls_idx = 1
    _cls_prop_idx = {
        'nphases': 1,
        'r1': 2,
        'x1': 3,
        'r0': 4,
        'x0': 5,
        'c1': 6,
        'c0': 7,
        'units': 8,
        'rmatrix': 9,
        'xmatrix': 10,
        'cmatrix': 11,
        'basefreq': 12,
        'normamps': 13,
        'emergamps': 14,
        'faultrate': 15,
        'pctperm': 16,
        'repair': 17,
        'kron': 18,
        'rg': 19,
        'xg': 20,
        'rho': 21,
        'neutral': 22,
        'b1': 23,
        'b0': 24,
        'seasons': 25,
        'ratings': 26,
        'linetype': 27,
        'like': 28,
    }

    @property
    def nphases(self) -> int:
        """
        DSS property name: nphases
        DSS property index: 1
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @nphases.setter
    def nphases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def r1(self) -> float:
        """
        DSS property name: r1
        DSS property index: 2
        """
        return self._lib.Obj_GetFloat64(self._ptr, 2)

    @r1.setter
    def r1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 2, value)

    @property
    def x1(self) -> float:
        """
        DSS property name: x1
        DSS property index: 3
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @x1.setter
    def x1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def r0(self) -> float:
        """
        DSS property name: r0
        DSS property index: 4
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @r0.setter
    def r0(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def x0(self) -> float:
        """
        DSS property name: x0
        DSS property index: 5
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @x0.setter
    def x0(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def C1(self) -> float:
        """
        DSS property name: C1
        DSS property index: 6
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    @C1.setter
    def C1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 6, value)

    @property
    def C0(self) -> float:
        """
        DSS property name: C0
        DSS property index: 7
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @C0.setter
    def C0(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def units(self) -> DimensionUnits:
        """
    DSS property name: units
    DSS property index: 8
    """
        return DimensionUnits(self._lib.Obj_GetInt32(self._ptr, 8))

    @units.setter
    def units(self, value: Union[AnyStr, int, DimensionUnits]):
        if not isinstance(value, int):
            self._set_string(8, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 8, value)

    @property
    def units_str(self) -> str:
        """
        DSS property name: units
        DSS property index: 8
        """
        return self._get_prop_string(8)

    @units_str.setter
    def units_str(self, value: AnyStr):
        self.units = value

    @property
    def rmatrix(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: rmatrix
        DSS property index: 9
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 9)

    @rmatrix.setter
    def rmatrix(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(9, value)

    @property
    def xmatrix(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: xmatrix
        DSS property index: 10
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 10)

    @xmatrix.setter
    def xmatrix(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(10, value)

    @property
    def cmatrix(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: cmatrix
        DSS property index: 11
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 11)

    @cmatrix.setter
    def cmatrix(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(11, value)

    @property
    def baseFreq(self) -> float:
        """
        DSS property name: baseFreq
        DSS property index: 12
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @baseFreq.setter
    def baseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def normamps(self) -> float:
        """
        DSS property name: normamps
        DSS property index: 13
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @normamps.setter
    def normamps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def emergamps(self) -> float:
        """
        DSS property name: emergamps
        DSS property index: 14
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @emergamps.setter
    def emergamps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def faultrate(self) -> float:
        """
        DSS property name: faultrate
        DSS property index: 15
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @faultrate.setter
    def faultrate(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def pctperm(self) -> float:
        """
        DSS property name: pctperm
        DSS property index: 16
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    @pctperm.setter
    def pctperm(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 16, value)

    @property
    def repair(self) -> float:
        """
        DSS property name: repair
        DSS property index: 17
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    @repair.setter
    def repair(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 17, value)

    def Kron(self, value: bool):
        """
        DSS property name: Kron
        DSS property index: 18
        """
        self._lib.Obj_SetInt32(self._ptr, 18, value)

    @property
    def Rg(self) -> float:
        """
        DSS property name: Rg
        DSS property index: 19
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    @Rg.setter
    def Rg(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 19, value)

    @property
    def Xg(self) -> float:
        """
        DSS property name: Xg
        DSS property index: 20
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    @Xg.setter
    def Xg(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 20, value)

    @property
    def rho(self) -> float:
        """
        DSS property name: rho
        DSS property index: 21
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @rho.setter
    def rho(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    @property
    def neutral(self) -> int:
        """
        DSS property name: neutral
        DSS property index: 22
        """
        return self._lib.Obj_GetInt32(self._ptr, 22)

    @neutral.setter
    def neutral(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 22, value)

    @property
    def B1(self) -> float:
        """
        DSS property name: B1
        DSS property index: 23
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    @B1.setter
    def B1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 23, value)

    @property
    def B0(self) -> float:
        """
        DSS property name: B0
        DSS property index: 24
        """
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    @B0.setter
    def B0(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 24, value)

    @property
    def Seasons(self) -> int:
        """
        DSS property name: Seasons
        DSS property index: 25
        """
        return self._lib.Obj_GetInt32(self._ptr, 25)

    @Seasons.setter
    def Seasons(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 25, value)

    @property
    def Ratings(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: Ratings
        DSS property index: 26
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 26)

    @Ratings.setter
    def Ratings(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(26, value)

    @property
    def linetype(self) -> LineType:
        """
    DSS property name: LineType
    DSS property index: 27
    """
        return LineType(self._lib.Obj_GetInt32(self._ptr, 27))

    @linetype.setter
    def linetype(self, value: Union[AnyStr, int, LineType]):
        if not isinstance(value, int):
            self._set_string(27, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 27, value)

    @property
    def linetype_str(self) -> str:
        """
        DSS property name: LineType
        DSS property index: 27
        """
        return self._get_prop_string(27)

    @linetype_str.setter
    def linetype_str(self, value: AnyStr):
        self.linetype = value

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 28
        """
        self._set_string(28, value)

class LoadShape(DSSObj):
    _cls_name = 'LoadShape'
    _cls_idx = 2
    _cls_prop_idx = {
        'npts': 1,
        'interval': 2,
        'mult': 3,
        'hour': 4,
        'mean': 5,
        'stddev': 6,
        'csvfile': 7,
        'sngfile': 8,
        'dblfile': 9,
        'action': 10,
        'qmult': 11,
        'useactual': 12,
        'pmax': 13,
        'qmax': 14,
        'sinterval': 15,
        'minterval': 16,
        'pbase': 17,
        'qbase': 18,
        'pmult': 19,
        'pqcsvfile': 20,
        'memorymapping': 21,
        'like': 22,
    }

    # Class-specific enumerations
    class LoadShapeAction(IntEnum):
        """LoadShape: Action (DSS enumeration for LoadShape)"""
        Normalize = 0 # Normalize
        DblSave = 1 # DblSave
        SngSave = 2 # SngSave


    @property
    def npts(self) -> int:
        """
        DSS property name: npts
        DSS property index: 1
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @npts.setter
    def npts(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def interval(self) -> float:
        """
        DSS property name: interval
        DSS property index: 2
        """
        return self._lib.Obj_GetFloat64(self._ptr, 2)

    @interval.setter
    def interval(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 2, value)

    @property
    def mult(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: mult
        DSS property index: 3
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 3)

    @mult.setter
    def mult(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(3, value)

    @property
    def hour(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: hour
        DSS property index: 4
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 4)

    @hour.setter
    def hour(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(4, value)

    @property
    def mean(self) -> float:
        """
        DSS property name: mean
        DSS property index: 5
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @mean.setter
    def mean(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def stddev(self) -> float:
        """
        DSS property name: stddev
        DSS property index: 6
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    @stddev.setter
    def stddev(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 6, value)

    @property
    def csvfile(self) -> str:
        """
        DSS property name: csvfile
        DSS property index: 7
        """
        return self._get_prop_string(7)

    @csvfile.setter
    def csvfile(self, value: AnyStr):
        self._set_string(7, value)

    @property
    def sngfile(self) -> str:
        """
        DSS property name: sngfile
        DSS property index: 8
        """
        return self._get_prop_string(8)

    @sngfile.setter
    def sngfile(self, value: AnyStr):
        self._set_string(8, value)

    @property
    def dblfile(self) -> str:
        """
        DSS property name: dblfile
        DSS property index: 9
        """
        return self._get_prop_string(9)

    @dblfile.setter
    def dblfile(self, value: AnyStr):
        self._set_string(9, value)

    def action(self, value: Union[str, bytes, int, LoadShapeAction]):
        """
        DSS property name: action
        DSS property index: 10
        """
        if isinstance(value, int):
            self._lib.Obj_SetInt32(self._ptr, 10, value)
            return

        self._set_string(10, value)

    @property
    def qmult(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: qmult
        DSS property index: 11
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 11)

    @qmult.setter
    def qmult(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(11, value)

    @property
    def UseActual(self) -> bool:
        """
        DSS property name: UseActual
        DSS property index: 12
        """
        return self._lib.Obj_GetInt32(self._ptr, 12) != 0

    @UseActual.setter
    def UseActual(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 12, value)

    @property
    def Pmax(self) -> float:
        """
        DSS property name: Pmax
        DSS property index: 13
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @Pmax.setter
    def Pmax(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def Qmax(self) -> float:
        """
        DSS property name: Qmax
        DSS property index: 14
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @Qmax.setter
    def Qmax(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def sinterval(self) -> float:
        """
        DSS property name: sinterval
        DSS property index: 15
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @sinterval.setter
    def sinterval(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def minterval(self) -> float:
        """
        DSS property name: minterval
        DSS property index: 16
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    @minterval.setter
    def minterval(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 16, value)

    @property
    def Pbase(self) -> float:
        """
        DSS property name: Pbase
        DSS property index: 17
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    @Pbase.setter
    def Pbase(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 17, value)

    @property
    def Qbase(self) -> float:
        """
        DSS property name: Qbase
        DSS property index: 18
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    @Qbase.setter
    def Qbase(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 18, value)

    @property
    def Pmult(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: Pmult
        DSS property index: 19
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 19)

    @Pmult.setter
    def Pmult(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(19, value)

    @property
    def PQCSVFile(self) -> str:
        """
        DSS property name: PQCSVFile
        DSS property index: 20
        """
        return self._get_prop_string(20)

    @PQCSVFile.setter
    def PQCSVFile(self, value: AnyStr):
        self._set_string(20, value)

    @property
    def MemoryMapping(self) -> bool:
        """
        DSS property name: MemoryMapping
        DSS property index: 21
        """
        return self._lib.Obj_GetInt32(self._ptr, 21) != 0

    @MemoryMapping.setter
    def MemoryMapping(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 21, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 22
        """
        self._set_string(22, value)

class TShape(DSSObj):
    _cls_name = 'TShape'
    _cls_idx = 3
    _cls_prop_idx = {
        'npts': 1,
        'interval': 2,
        'temp': 3,
        'hour': 4,
        'mean': 5,
        'stddev': 6,
        'csvfile': 7,
        'sngfile': 8,
        'dblfile': 9,
        'sinterval': 10,
        'minterval': 11,
        'action': 12,
        'like': 13,
    }

    # Class-specific enumerations
    class TShapeAction(IntEnum):
        """TShape: Action (DSS enumeration for TShape)"""
        DblSave = 0 # DblSave
        SngSave = 1 # SngSave


    @property
    def npts(self) -> int:
        """
        DSS property name: npts
        DSS property index: 1
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @npts.setter
    def npts(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def interval(self) -> float:
        """
        DSS property name: interval
        DSS property index: 2
        """
        return self._lib.Obj_GetFloat64(self._ptr, 2)

    @interval.setter
    def interval(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 2, value)

    @property
    def temp(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: temp
        DSS property index: 3
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 3)

    @temp.setter
    def temp(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(3, value)

    @property
    def hour(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: hour
        DSS property index: 4
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 4)

    @hour.setter
    def hour(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(4, value)

    @property
    def mean(self) -> float:
        """
        DSS property name: mean
        DSS property index: 5
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @mean.setter
    def mean(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def stddev(self) -> float:
        """
        DSS property name: stddev
        DSS property index: 6
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    @stddev.setter
    def stddev(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 6, value)

    @property
    def csvfile(self) -> str:
        """
        DSS property name: csvfile
        DSS property index: 7
        """
        return self._get_prop_string(7)

    @csvfile.setter
    def csvfile(self, value: AnyStr):
        self._set_string(7, value)

    @property
    def sngfile(self) -> str:
        """
        DSS property name: sngfile
        DSS property index: 8
        """
        return self._get_prop_string(8)

    @sngfile.setter
    def sngfile(self, value: AnyStr):
        self._set_string(8, value)

    @property
    def dblfile(self) -> str:
        """
        DSS property name: dblfile
        DSS property index: 9
        """
        return self._get_prop_string(9)

    @dblfile.setter
    def dblfile(self, value: AnyStr):
        self._set_string(9, value)

    @property
    def sinterval(self) -> float:
        """
        DSS property name: sinterval
        DSS property index: 10
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @sinterval.setter
    def sinterval(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def minterval(self) -> float:
        """
        DSS property name: minterval
        DSS property index: 11
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @minterval.setter
    def minterval(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    def action(self, value: Union[str, bytes, int, TShapeAction]):
        """
        DSS property name: action
        DSS property index: 12
        """
        if isinstance(value, int):
            self._lib.Obj_SetInt32(self._ptr, 12, value)
            return

        self._set_string(12, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 13
        """
        self._set_string(13, value)

class PriceShape(DSSObj):
    _cls_name = 'PriceShape'
    _cls_idx = 4
    _cls_prop_idx = {
        'npts': 1,
        'interval': 2,
        'price': 3,
        'hour': 4,
        'mean': 5,
        'stddev': 6,
        'csvfile': 7,
        'sngfile': 8,
        'dblfile': 9,
        'sinterval': 10,
        'minterval': 11,
        'action': 12,
        'like': 13,
    }

    # Class-specific enumerations
    class PriceShapeAction(IntEnum):
        """PriceShape: Action (DSS enumeration for PriceShape)"""
        DblSave = 0 # DblSave
        SngSave = 1 # SngSave


    @property
    def npts(self) -> int:
        """
        DSS property name: npts
        DSS property index: 1
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @npts.setter
    def npts(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def interval(self) -> float:
        """
        DSS property name: interval
        DSS property index: 2
        """
        return self._lib.Obj_GetFloat64(self._ptr, 2)

    @interval.setter
    def interval(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 2, value)

    @property
    def price(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: price
        DSS property index: 3
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 3)

    @price.setter
    def price(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(3, value)

    @property
    def hour(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: hour
        DSS property index: 4
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 4)

    @hour.setter
    def hour(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(4, value)

    @property
    def mean(self) -> float:
        """
        DSS property name: mean
        DSS property index: 5
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @mean.setter
    def mean(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def stddev(self) -> float:
        """
        DSS property name: stddev
        DSS property index: 6
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    @stddev.setter
    def stddev(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 6, value)

    @property
    def csvfile(self) -> str:
        """
        DSS property name: csvfile
        DSS property index: 7
        """
        return self._get_prop_string(7)

    @csvfile.setter
    def csvfile(self, value: AnyStr):
        self._set_string(7, value)

    @property
    def sngfile(self) -> str:
        """
        DSS property name: sngfile
        DSS property index: 8
        """
        return self._get_prop_string(8)

    @sngfile.setter
    def sngfile(self, value: AnyStr):
        self._set_string(8, value)

    @property
    def dblfile(self) -> str:
        """
        DSS property name: dblfile
        DSS property index: 9
        """
        return self._get_prop_string(9)

    @dblfile.setter
    def dblfile(self, value: AnyStr):
        self._set_string(9, value)

    @property
    def sinterval(self) -> float:
        """
        DSS property name: sinterval
        DSS property index: 10
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @sinterval.setter
    def sinterval(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def minterval(self) -> float:
        """
        DSS property name: minterval
        DSS property index: 11
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @minterval.setter
    def minterval(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    def action(self, value: Union[str, bytes, int, PriceShapeAction]):
        """
        DSS property name: action
        DSS property index: 12
        """
        if isinstance(value, int):
            self._lib.Obj_SetInt32(self._ptr, 12, value)
            return

        self._set_string(12, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 13
        """
        self._set_string(13, value)

class XYcurve(DSSObj):
    _cls_name = 'XYcurve'
    _cls_idx = 5
    _cls_prop_idx = {
        'npts': 1,
        'points': 2,
        'yarray': 3,
        'xarray': 4,
        'csvfile': 5,
        'sngfile': 6,
        'dblfile': 7,
        'x': 8,
        'y': 9,
        'xshift': 10,
        'yshift': 11,
        'xscale': 12,
        'yscale': 13,
        'like': 14,
    }

    @property
    def npts(self) -> int:
        """
        DSS property name: npts
        DSS property index: 1
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @npts.setter
    def npts(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def Points(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: Points
        DSS property index: 2
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 2)

    @Points.setter
    def Points(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(2, value)

    @property
    def Yarray(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: Yarray
        DSS property index: 3
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 3)

    @Yarray.setter
    def Yarray(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(3, value)

    @property
    def Xarray(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: Xarray
        DSS property index: 4
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 4)

    @Xarray.setter
    def Xarray(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(4, value)

    @property
    def csvfile(self) -> str:
        """
        DSS property name: csvfile
        DSS property index: 5
        """
        return self._get_prop_string(5)

    @csvfile.setter
    def csvfile(self, value: AnyStr):
        self._set_string(5, value)

    @property
    def sngfile(self) -> str:
        """
        DSS property name: sngfile
        DSS property index: 6
        """
        return self._get_prop_string(6)

    @sngfile.setter
    def sngfile(self, value: AnyStr):
        self._set_string(6, value)

    @property
    def dblfile(self) -> str:
        """
        DSS property name: dblfile
        DSS property index: 7
        """
        return self._get_prop_string(7)

    @dblfile.setter
    def dblfile(self, value: AnyStr):
        self._set_string(7, value)

    @property
    def x(self) -> float:
        """
        DSS property name: x
        DSS property index: 8
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @x.setter
    def x(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def y(self) -> float:
        """
        DSS property name: y
        DSS property index: 9
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @y.setter
    def y(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def Xshift(self) -> float:
        """
        DSS property name: Xshift
        DSS property index: 10
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @Xshift.setter
    def Xshift(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def Yshift(self) -> float:
        """
        DSS property name: Yshift
        DSS property index: 11
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @Yshift.setter
    def Yshift(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def Xscale(self) -> float:
        """
        DSS property name: Xscale
        DSS property index: 12
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @Xscale.setter
    def Xscale(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def Yscale(self) -> float:
        """
        DSS property name: Yscale
        DSS property index: 13
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @Yscale.setter
    def Yscale(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 14
        """
        self._set_string(14, value)

class GrowthShape(DSSObj):
    _cls_name = 'GrowthShape'
    _cls_idx = 6
    _cls_prop_idx = {
        'npts': 1,
        'year': 2,
        'mult': 3,
        'csvfile': 4,
        'sngfile': 5,
        'dblfile': 6,
        'like': 7,
    }

    @property
    def npts(self) -> int:
        """
        DSS property name: npts
        DSS property index: 1
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @npts.setter
    def npts(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def year(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: year
        DSS property index: 2
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 2)

    @year.setter
    def year(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(2, value)

    @property
    def mult(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: mult
        DSS property index: 3
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 3)

    @mult.setter
    def mult(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(3, value)

    @property
    def csvfile(self) -> str:
        """
        DSS property name: csvfile
        DSS property index: 4
        """
        return self._get_prop_string(4)

    @csvfile.setter
    def csvfile(self, value: AnyStr):
        self._set_string(4, value)

    @property
    def sngfile(self) -> str:
        """
        DSS property name: sngfile
        DSS property index: 5
        """
        return self._get_prop_string(5)

    @sngfile.setter
    def sngfile(self, value: AnyStr):
        self._set_string(5, value)

    @property
    def dblfile(self) -> str:
        """
        DSS property name: dblfile
        DSS property index: 6
        """
        return self._get_prop_string(6)

    @dblfile.setter
    def dblfile(self, value: AnyStr):
        self._set_string(6, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 7
        """
        self._set_string(7, value)

class TCC_Curve(DSSObj):
    _cls_name = 'TCC_Curve'
    _cls_idx = 7
    _cls_prop_idx = {
        'npts': 1,
        'c_array': 2,
        't_array': 3,
        'like': 4,
    }

    @property
    def npts(self) -> int:
        """
        DSS property name: npts
        DSS property index: 1
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @npts.setter
    def npts(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def C_array(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: C_array
        DSS property index: 2
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 2)

    @C_array.setter
    def C_array(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(2, value)

    @property
    def T_array(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: T_array
        DSS property index: 3
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 3)

    @T_array.setter
    def T_array(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(3, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 4
        """
        self._set_string(4, value)

class Spectrum(DSSObj):
    _cls_name = 'Spectrum'
    _cls_idx = 8
    _cls_prop_idx = {
        'numharm': 1,
        'harmonic': 2,
        'pctmag': 3,
        '%mag': 3,
        'angle': 4,
        'csvfile': 5,
        'like': 6,
    }

    @property
    def NumHarm(self) -> int:
        """
        DSS property name: NumHarm
        DSS property index: 1
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @NumHarm.setter
    def NumHarm(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def harmonic(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: harmonic
        DSS property index: 2
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 2)

    @harmonic.setter
    def harmonic(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(2, value)

    @property
    def pctmag(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: %mag
        DSS property index: 3
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 3)

    @pctmag.setter
    def pctmag(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(3, value)

    @property
    def angle(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: angle
        DSS property index: 4
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 4)

    @angle.setter
    def angle(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(4, value)

    @property
    def CSVFile(self) -> str:
        """
        DSS property name: CSVFile
        DSS property index: 5
        """
        return self._get_prop_string(5)

    @CSVFile.setter
    def CSVFile(self, value: AnyStr):
        self._set_string(5, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 6
        """
        self._set_string(6, value)

class WireData(DSSObj):
    _cls_name = 'WireData'
    _cls_idx = 9
    _cls_prop_idx = {
        'rdc': 1,
        'rac': 2,
        'runits': 3,
        'gmrac': 4,
        'gmrunits': 5,
        'radius': 6,
        'radunits': 7,
        'normamps': 8,
        'emergamps': 9,
        'diam': 10,
        'seasons': 11,
        'ratings': 12,
        'capradius': 13,
        'like': 14,
    }

    @property
    def Rdc(self) -> float:
        """
        DSS property name: Rdc
        DSS property index: 1
        """
        return self._lib.Obj_GetFloat64(self._ptr, 1)

    @Rdc.setter
    def Rdc(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 1, value)

    @property
    def Rac(self) -> float:
        """
        DSS property name: Rac
        DSS property index: 2
        """
        return self._lib.Obj_GetFloat64(self._ptr, 2)

    @Rac.setter
    def Rac(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 2, value)

    @property
    def Runits(self) -> DimensionUnits:
        """
    DSS property name: Runits
    DSS property index: 3
    """
        return DimensionUnits(self._lib.Obj_GetInt32(self._ptr, 3))

    @Runits.setter
    def Runits(self, value: Union[AnyStr, int, DimensionUnits]):
        if not isinstance(value, int):
            self._set_string(3, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 3, value)

    @property
    def Runits_str(self) -> str:
        """
        DSS property name: Runits
        DSS property index: 3
        """
        return self._get_prop_string(3)

    @Runits_str.setter
    def Runits_str(self, value: AnyStr):
        self.Runits = value

    @property
    def GMRac(self) -> float:
        """
        DSS property name: GMRac
        DSS property index: 4
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @GMRac.setter
    def GMRac(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def GMRunits(self) -> DimensionUnits:
        """
    DSS property name: GMRunits
    DSS property index: 5
    """
        return DimensionUnits(self._lib.Obj_GetInt32(self._ptr, 5))

    @GMRunits.setter
    def GMRunits(self, value: Union[AnyStr, int, DimensionUnits]):
        if not isinstance(value, int):
            self._set_string(5, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 5, value)

    @property
    def GMRunits_str(self) -> str:
        """
        DSS property name: GMRunits
        DSS property index: 5
        """
        return self._get_prop_string(5)

    @GMRunits_str.setter
    def GMRunits_str(self, value: AnyStr):
        self.GMRunits = value

    @property
    def radius(self) -> float:
        """
        DSS property name: radius
        DSS property index: 6
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    @radius.setter
    def radius(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 6, value)

    @property
    def radunits(self) -> DimensionUnits:
        """
    DSS property name: radunits
    DSS property index: 7
    """
        return DimensionUnits(self._lib.Obj_GetInt32(self._ptr, 7))

    @radunits.setter
    def radunits(self, value: Union[AnyStr, int, DimensionUnits]):
        if not isinstance(value, int):
            self._set_string(7, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 7, value)

    @property
    def radunits_str(self) -> str:
        """
        DSS property name: radunits
        DSS property index: 7
        """
        return self._get_prop_string(7)

    @radunits_str.setter
    def radunits_str(self, value: AnyStr):
        self.radunits = value

    @property
    def normamps(self) -> float:
        """
        DSS property name: normamps
        DSS property index: 8
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @normamps.setter
    def normamps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def emergamps(self) -> float:
        """
        DSS property name: emergamps
        DSS property index: 9
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @emergamps.setter
    def emergamps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def diam(self) -> float:
        """
        DSS property name: diam
        DSS property index: 10
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @diam.setter
    def diam(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def Seasons(self) -> int:
        """
        DSS property name: Seasons
        DSS property index: 11
        """
        return self._lib.Obj_GetInt32(self._ptr, 11)

    @Seasons.setter
    def Seasons(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 11, value)

    @property
    def Ratings(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: Ratings
        DSS property index: 12
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 12)

    @Ratings.setter
    def Ratings(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(12, value)

    @property
    def Capradius(self) -> float:
        """
        DSS property name: Capradius
        DSS property index: 13
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @Capradius.setter
    def Capradius(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 14
        """
        self._set_string(14, value)

class CNData(DSSObj):
    _cls_name = 'CNData'
    _cls_idx = 10
    _cls_prop_idx = {
        'k': 1,
        'diastrand': 2,
        'gmrstrand': 3,
        'rstrand': 4,
        'epsr': 5,
        'inslayer': 6,
        'diains': 7,
        'diacable': 8,
        'rdc': 9,
        'rac': 10,
        'runits': 11,
        'gmrac': 12,
        'gmrunits': 13,
        'radius': 14,
        'radunits': 15,
        'normamps': 16,
        'emergamps': 17,
        'diam': 18,
        'seasons': 19,
        'ratings': 20,
        'capradius': 21,
        'like': 22,
    }

    @property
    def k(self) -> int:
        """
        DSS property name: k
        DSS property index: 1
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @k.setter
    def k(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def DiaStrand(self) -> float:
        """
        DSS property name: DiaStrand
        DSS property index: 2
        """
        return self._lib.Obj_GetFloat64(self._ptr, 2)

    @DiaStrand.setter
    def DiaStrand(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 2, value)

    @property
    def GmrStrand(self) -> float:
        """
        DSS property name: GmrStrand
        DSS property index: 3
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @GmrStrand.setter
    def GmrStrand(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def Rstrand(self) -> float:
        """
        DSS property name: Rstrand
        DSS property index: 4
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @Rstrand.setter
    def Rstrand(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def EpsR(self) -> float:
        """
        DSS property name: EpsR
        DSS property index: 5
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @EpsR.setter
    def EpsR(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def InsLayer(self) -> float:
        """
        DSS property name: InsLayer
        DSS property index: 6
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    @InsLayer.setter
    def InsLayer(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 6, value)

    @property
    def DiaIns(self) -> float:
        """
        DSS property name: DiaIns
        DSS property index: 7
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @DiaIns.setter
    def DiaIns(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def DiaCable(self) -> float:
        """
        DSS property name: DiaCable
        DSS property index: 8
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @DiaCable.setter
    def DiaCable(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def Rdc(self) -> float:
        """
        DSS property name: Rdc
        DSS property index: 9
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @Rdc.setter
    def Rdc(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def Rac(self) -> float:
        """
        DSS property name: Rac
        DSS property index: 10
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @Rac.setter
    def Rac(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def Runits(self) -> DimensionUnits:
        """
    DSS property name: Runits
    DSS property index: 11
    """
        return DimensionUnits(self._lib.Obj_GetInt32(self._ptr, 11))

    @Runits.setter
    def Runits(self, value: Union[AnyStr, int, DimensionUnits]):
        if not isinstance(value, int):
            self._set_string(11, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 11, value)

    @property
    def Runits_str(self) -> str:
        """
        DSS property name: Runits
        DSS property index: 11
        """
        return self._get_prop_string(11)

    @Runits_str.setter
    def Runits_str(self, value: AnyStr):
        self.Runits = value

    @property
    def GMRac(self) -> float:
        """
        DSS property name: GMRac
        DSS property index: 12
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @GMRac.setter
    def GMRac(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def GMRunits(self) -> DimensionUnits:
        """
    DSS property name: GMRunits
    DSS property index: 13
    """
        return DimensionUnits(self._lib.Obj_GetInt32(self._ptr, 13))

    @GMRunits.setter
    def GMRunits(self, value: Union[AnyStr, int, DimensionUnits]):
        if not isinstance(value, int):
            self._set_string(13, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 13, value)

    @property
    def GMRunits_str(self) -> str:
        """
        DSS property name: GMRunits
        DSS property index: 13
        """
        return self._get_prop_string(13)

    @GMRunits_str.setter
    def GMRunits_str(self, value: AnyStr):
        self.GMRunits = value

    @property
    def radius(self) -> float:
        """
        DSS property name: radius
        DSS property index: 14
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @radius.setter
    def radius(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def radunits(self) -> DimensionUnits:
        """
    DSS property name: radunits
    DSS property index: 15
    """
        return DimensionUnits(self._lib.Obj_GetInt32(self._ptr, 15))

    @radunits.setter
    def radunits(self, value: Union[AnyStr, int, DimensionUnits]):
        if not isinstance(value, int):
            self._set_string(15, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 15, value)

    @property
    def radunits_str(self) -> str:
        """
        DSS property name: radunits
        DSS property index: 15
        """
        return self._get_prop_string(15)

    @radunits_str.setter
    def radunits_str(self, value: AnyStr):
        self.radunits = value

    @property
    def normamps(self) -> float:
        """
        DSS property name: normamps
        DSS property index: 16
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    @normamps.setter
    def normamps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 16, value)

    @property
    def emergamps(self) -> float:
        """
        DSS property name: emergamps
        DSS property index: 17
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    @emergamps.setter
    def emergamps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 17, value)

    @property
    def diam(self) -> float:
        """
        DSS property name: diam
        DSS property index: 18
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    @diam.setter
    def diam(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 18, value)

    @property
    def Seasons(self) -> int:
        """
        DSS property name: Seasons
        DSS property index: 19
        """
        return self._lib.Obj_GetInt32(self._ptr, 19)

    @Seasons.setter
    def Seasons(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 19, value)

    @property
    def Ratings(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: Ratings
        DSS property index: 20
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 20)

    @Ratings.setter
    def Ratings(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(20, value)

    @property
    def Capradius(self) -> float:
        """
        DSS property name: Capradius
        DSS property index: 21
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @Capradius.setter
    def Capradius(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 22
        """
        self._set_string(22, value)

class TSData(DSSObj):
    _cls_name = 'TSData'
    _cls_idx = 11
    _cls_prop_idx = {
        'diashield': 1,
        'tapelayer': 2,
        'tapelap': 3,
        'epsr': 4,
        'inslayer': 5,
        'diains': 6,
        'diacable': 7,
        'rdc': 8,
        'rac': 9,
        'runits': 10,
        'gmrac': 11,
        'gmrunits': 12,
        'radius': 13,
        'radunits': 14,
        'normamps': 15,
        'emergamps': 16,
        'diam': 17,
        'seasons': 18,
        'ratings': 19,
        'capradius': 20,
        'like': 21,
    }

    @property
    def DiaShield(self) -> float:
        """
        DSS property name: DiaShield
        DSS property index: 1
        """
        return self._lib.Obj_GetFloat64(self._ptr, 1)

    @DiaShield.setter
    def DiaShield(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 1, value)

    @property
    def TapeLayer(self) -> float:
        """
        DSS property name: TapeLayer
        DSS property index: 2
        """
        return self._lib.Obj_GetFloat64(self._ptr, 2)

    @TapeLayer.setter
    def TapeLayer(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 2, value)

    @property
    def TapeLap(self) -> float:
        """
        DSS property name: TapeLap
        DSS property index: 3
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @TapeLap.setter
    def TapeLap(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def EpsR(self) -> float:
        """
        DSS property name: EpsR
        DSS property index: 4
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @EpsR.setter
    def EpsR(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def InsLayer(self) -> float:
        """
        DSS property name: InsLayer
        DSS property index: 5
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @InsLayer.setter
    def InsLayer(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def DiaIns(self) -> float:
        """
        DSS property name: DiaIns
        DSS property index: 6
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    @DiaIns.setter
    def DiaIns(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 6, value)

    @property
    def DiaCable(self) -> float:
        """
        DSS property name: DiaCable
        DSS property index: 7
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @DiaCable.setter
    def DiaCable(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def Rdc(self) -> float:
        """
        DSS property name: Rdc
        DSS property index: 8
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @Rdc.setter
    def Rdc(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def Rac(self) -> float:
        """
        DSS property name: Rac
        DSS property index: 9
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @Rac.setter
    def Rac(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def Runits(self) -> DimensionUnits:
        """
    DSS property name: Runits
    DSS property index: 10
    """
        return DimensionUnits(self._lib.Obj_GetInt32(self._ptr, 10))

    @Runits.setter
    def Runits(self, value: Union[AnyStr, int, DimensionUnits]):
        if not isinstance(value, int):
            self._set_string(10, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 10, value)

    @property
    def Runits_str(self) -> str:
        """
        DSS property name: Runits
        DSS property index: 10
        """
        return self._get_prop_string(10)

    @Runits_str.setter
    def Runits_str(self, value: AnyStr):
        self.Runits = value

    @property
    def GMRac(self) -> float:
        """
        DSS property name: GMRac
        DSS property index: 11
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @GMRac.setter
    def GMRac(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def GMRunits(self) -> DimensionUnits:
        """
    DSS property name: GMRunits
    DSS property index: 12
    """
        return DimensionUnits(self._lib.Obj_GetInt32(self._ptr, 12))

    @GMRunits.setter
    def GMRunits(self, value: Union[AnyStr, int, DimensionUnits]):
        if not isinstance(value, int):
            self._set_string(12, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 12, value)

    @property
    def GMRunits_str(self) -> str:
        """
        DSS property name: GMRunits
        DSS property index: 12
        """
        return self._get_prop_string(12)

    @GMRunits_str.setter
    def GMRunits_str(self, value: AnyStr):
        self.GMRunits = value

    @property
    def radius(self) -> float:
        """
        DSS property name: radius
        DSS property index: 13
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @radius.setter
    def radius(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def radunits(self) -> DimensionUnits:
        """
    DSS property name: radunits
    DSS property index: 14
    """
        return DimensionUnits(self._lib.Obj_GetInt32(self._ptr, 14))

    @radunits.setter
    def radunits(self, value: Union[AnyStr, int, DimensionUnits]):
        if not isinstance(value, int):
            self._set_string(14, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 14, value)

    @property
    def radunits_str(self) -> str:
        """
        DSS property name: radunits
        DSS property index: 14
        """
        return self._get_prop_string(14)

    @radunits_str.setter
    def radunits_str(self, value: AnyStr):
        self.radunits = value

    @property
    def normamps(self) -> float:
        """
        DSS property name: normamps
        DSS property index: 15
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @normamps.setter
    def normamps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def emergamps(self) -> float:
        """
        DSS property name: emergamps
        DSS property index: 16
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    @emergamps.setter
    def emergamps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 16, value)

    @property
    def diam(self) -> float:
        """
        DSS property name: diam
        DSS property index: 17
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    @diam.setter
    def diam(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 17, value)

    @property
    def Seasons(self) -> int:
        """
        DSS property name: Seasons
        DSS property index: 18
        """
        return self._lib.Obj_GetInt32(self._ptr, 18)

    @Seasons.setter
    def Seasons(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 18, value)

    @property
    def Ratings(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: Ratings
        DSS property index: 19
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 19)

    @Ratings.setter
    def Ratings(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(19, value)

    @property
    def Capradius(self) -> float:
        """
        DSS property name: Capradius
        DSS property index: 20
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    @Capradius.setter
    def Capradius(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 20, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 21
        """
        self._set_string(21, value)

class LineSpacing(DSSObj):
    _cls_name = 'LineSpacing'
    _cls_idx = 12
    _cls_prop_idx = {
        'nconds': 1,
        'nphases': 2,
        'x': 3,
        'h': 4,
        'units': 5,
        'like': 6,
    }

    @property
    def nconds(self) -> int:
        """
        DSS property name: nconds
        DSS property index: 1
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @nconds.setter
    def nconds(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def nphases(self) -> int:
        """
        DSS property name: nphases
        DSS property index: 2
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @nphases.setter
    def nphases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def x(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: x
        DSS property index: 3
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 3)

    @x.setter
    def x(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(3, value)

    @property
    def h(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: h
        DSS property index: 4
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 4)

    @h.setter
    def h(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(4, value)

    @property
    def units(self) -> DimensionUnits:
        """
    DSS property name: units
    DSS property index: 5
    """
        return DimensionUnits(self._lib.Obj_GetInt32(self._ptr, 5))

    @units.setter
    def units(self, value: Union[AnyStr, int, DimensionUnits]):
        if not isinstance(value, int):
            self._set_string(5, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 5, value)

    @property
    def units_str(self) -> str:
        """
        DSS property name: units
        DSS property index: 5
        """
        return self._get_prop_string(5)

    @units_str.setter
    def units_str(self, value: AnyStr):
        self.units = value

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 6
        """
        self._set_string(6, value)

class LineGeometry(DSSObj):
    _cls_name = 'LineGeometry'
    _cls_idx = 13
    _cls_prop_idx = {
        'nconds': 1,
        'nphases': 2,
        'cond': 3,
        'wire': 4,
        'x': 5,
        'h': 6,
        'units': 7,
        'normamps': 8,
        'emergamps': 9,
        'reduce': 10,
        'spacing': 11,
        'wires': 12,
        'cncable': 13,
        'tscable': 14,
        'cncables': 15,
        'tscables': 16,
        'seasons': 17,
        'ratings': 18,
        'linetype': 19,
        'like': 20,
    }

    @property
    def nconds(self) -> int:
        """
        DSS property name: nconds
        DSS property index: 1
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @nconds.setter
    def nconds(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def nphases(self) -> int:
        """
        DSS property name: nphases
        DSS property index: 2
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @nphases.setter
    def nphases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def cond(self) -> int:
        """
        DSS property name: cond
        DSS property index: 3
        """
        return self._lib.Obj_GetInt32(self._ptr, 3)

    @cond.setter
    def cond(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 3, value)

    @property
    def wire(self) -> List[str]:
        """
        DSS property name: wire
        DSS property index: 4
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 4)

    @wire.setter
    def wire(self, value: List[Union[AnyStr, WireData]]):
        if value is None or len(value) == 0 or not isinstance(value[0], DSSObj):
            self._set_string_array(4, value)
            return

        self._set_obj_array(4, value)

    @property
    def wire_obj(self) -> List[WireData]:
        """
        DSS property name: wire
        DSS property index: 4
        """
        return self._get_obj_array(4, WireData)

    @wire_obj.setter
    def wire_obj(self, value: List[WireData]):
        self._set_obj_array(4, value)

    @property
    def x(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: x
        DSS property index: 5
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 5)

    @x.setter
    def x(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(5, value)

    @property
    def h(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: h
        DSS property index: 6
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 6)

    @h.setter
    def h(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(6, value)

    @property
    def units(self) -> DimensionUnits:
        """
    DSS property name: units
    DSS property index: 7
    """
        return DimensionUnits(self._lib.Obj_GetInt32(self._ptr, 7))

    @units.setter
    def units(self, value: Union[AnyStr, int, DimensionUnits]):
        if not isinstance(value, int):
            self._set_string(7, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 7, value)

    @property
    def units_str(self) -> str:
        """
        DSS property name: units
        DSS property index: 7
        """
        return self._get_prop_string(7)

    @units_str.setter
    def units_str(self, value: AnyStr):
        self.units = value

    @property
    def normamps(self) -> float:
        """
        DSS property name: normamps
        DSS property index: 8
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @normamps.setter
    def normamps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def emergamps(self) -> float:
        """
        DSS property name: emergamps
        DSS property index: 9
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @emergamps.setter
    def emergamps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def reduce(self) -> bool:
        """
        DSS property name: reduce
        DSS property index: 10
        """
        return self._lib.Obj_GetInt32(self._ptr, 10) != 0

    @reduce.setter
    def reduce(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 10, value)

    @property
    def spacing(self) -> str:
        """
        DSS property name: spacing
        DSS property index: 11
        """
        return self._get_prop_string(11)

    @spacing.setter
    def spacing(self, value: Union[AnyStr, LineSpacing]):
        if isinstance(value, DSSObj):
            self._set_obj(11, value)
            return

        self._set_string(11, value)

    @property
    def spacing_obj(self) -> LineSpacing:
        """
        DSS property name: spacing
        DSS property index: 11
        """
        return self._get_obj(11, LineSpacing)

    @spacing_obj.setter
    def spacing_obj(self, value: LineSpacing):
        self._set_obj(11, value)

    @property
    def wires(self) -> List[str]:
        """
        DSS property name: wires
        DSS property index: 12
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 12)

    @wires.setter
    def wires(self, value: List[Union[AnyStr, WireData]]):
        if value is None or len(value) == 0 or not isinstance(value[0], DSSObj):
            self._set_string_array(12, value)
            return

        self._set_obj_array(12, value)

    @property
    def wires_obj(self) -> List[WireData]:
        """
        DSS property name: wires
        DSS property index: 12
        """
        return self._get_obj_array(12, WireData)

    @wires_obj.setter
    def wires_obj(self, value: List[WireData]):
        self._set_obj_array(12, value)

    @property
    def cncable(self) -> List[str]:
        """
        DSS property name: cncable
        DSS property index: 13
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 13)

    @cncable.setter
    def cncable(self, value: List[Union[AnyStr, CNData]]):
        if value is None or len(value) == 0 or not isinstance(value[0], DSSObj):
            self._set_string_array(13, value)
            return

        self._set_obj_array(13, value)

    @property
    def cncable_obj(self) -> List[CNData]:
        """
        DSS property name: cncable
        DSS property index: 13
        """
        return self._get_obj_array(13, CNData)

    @cncable_obj.setter
    def cncable_obj(self, value: List[CNData]):
        self._set_obj_array(13, value)

    @property
    def tscable(self) -> List[str]:
        """
        DSS property name: tscable
        DSS property index: 14
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 14)

    @tscable.setter
    def tscable(self, value: List[Union[AnyStr, TSData]]):
        if value is None or len(value) == 0 or not isinstance(value[0], DSSObj):
            self._set_string_array(14, value)
            return

        self._set_obj_array(14, value)

    @property
    def tscable_obj(self) -> List[TSData]:
        """
        DSS property name: tscable
        DSS property index: 14
        """
        return self._get_obj_array(14, TSData)

    @tscable_obj.setter
    def tscable_obj(self, value: List[TSData]):
        self._set_obj_array(14, value)

    @property
    def cncables(self) -> List[str]:
        """
        DSS property name: cncables
        DSS property index: 15
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 15)

    @cncables.setter
    def cncables(self, value: List[Union[AnyStr, CNData]]):
        if value is None or len(value) == 0 or not isinstance(value[0], DSSObj):
            self._set_string_array(15, value)
            return

        self._set_obj_array(15, value)

    @property
    def cncables_obj(self) -> List[CNData]:
        """
        DSS property name: cncables
        DSS property index: 15
        """
        return self._get_obj_array(15, CNData)

    @cncables_obj.setter
    def cncables_obj(self, value: List[CNData]):
        self._set_obj_array(15, value)

    @property
    def tscables(self) -> List[str]:
        """
        DSS property name: tscables
        DSS property index: 16
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 16)

    @tscables.setter
    def tscables(self, value: List[Union[AnyStr, TSData]]):
        if value is None or len(value) == 0 or not isinstance(value[0], DSSObj):
            self._set_string_array(16, value)
            return

        self._set_obj_array(16, value)

    @property
    def tscables_obj(self) -> List[TSData]:
        """
        DSS property name: tscables
        DSS property index: 16
        """
        return self._get_obj_array(16, TSData)

    @tscables_obj.setter
    def tscables_obj(self, value: List[TSData]):
        self._set_obj_array(16, value)

    @property
    def Seasons(self) -> int:
        """
        DSS property name: Seasons
        DSS property index: 17
        """
        return self._lib.Obj_GetInt32(self._ptr, 17)

    @Seasons.setter
    def Seasons(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 17, value)

    @property
    def Ratings(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: Ratings
        DSS property index: 18
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 18)

    @Ratings.setter
    def Ratings(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(18, value)

    @property
    def linetype(self) -> LineType:
        """
    DSS property name: LineType
    DSS property index: 19
    """
        return LineType(self._lib.Obj_GetInt32(self._ptr, 19))

    @linetype.setter
    def linetype(self, value: Union[AnyStr, int, LineType]):
        if not isinstance(value, int):
            self._set_string(19, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 19, value)

    @property
    def linetype_str(self) -> str:
        """
        DSS property name: LineType
        DSS property index: 19
        """
        return self._get_prop_string(19)

    @linetype_str.setter
    def linetype_str(self, value: AnyStr):
        self.linetype = value

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 20
        """
        self._set_string(20, value)

class XfmrCode(DSSObj):
    _cls_name = 'XfmrCode'
    _cls_idx = 14
    _cls_prop_idx = {
        'phases': 1,
        'windings': 2,
        'wdg': 3,
        'conn': 4,
        'kv': 5,
        'kva': 6,
        'tap': 7,
        'pctr': 8,
        '%r': 8,
        'rneut': 9,
        'xneut': 10,
        'conns': 11,
        'kvs': 12,
        'kvas': 13,
        'taps': 14,
        'xhl': 15,
        'xht': 16,
        'xlt': 17,
        'xscarray': 18,
        'thermal': 19,
        'n': 20,
        'm': 21,
        'flrise': 22,
        'hsrise': 23,
        'pctloadloss': 24,
        '%loadloss': 24,
        'pctnoloadloss': 25,
        '%noloadloss': 25,
        'normhkva': 26,
        'emerghkva': 27,
        'maxtap': 28,
        'mintap': 29,
        'numtaps': 30,
        'pctimag': 31,
        '%imag': 31,
        'ppm_antifloat': 32,
        'pctrs': 33,
        '%rs': 33,
        'x12': 34,
        'x13': 35,
        'x23': 36,
        'rdcohms': 37,
        'seasons': 38,
        'ratings': 39,
        'like': 40,
    }

    @property
    def phases(self) -> int:
        """
        DSS property name: phases
        DSS property index: 1
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @phases.setter
    def phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def windings(self) -> int:
        """
        DSS property name: windings
        DSS property index: 2
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @windings.setter
    def windings(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def wdg(self) -> int:
        """
        DSS property name: wdg
        DSS property index: 3
        """
        return self._lib.Obj_GetInt32(self._ptr, 3)

    @wdg.setter
    def wdg(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 3, value)

    @property
    def conn(self) -> List[Connection]:
        """
        DSS property name: conn
        DSS property index: 4
        """
        return [Connection(val) for val in self._get_int32_list(self._lib.Obj_GetInt32Array, self._ptr, 4)]

    @conn.setter
    def conn(self, value: Union[List[Union[int,Connection]], List[AnyStr]]):
        if not isinstance(value, int):
            self._set_string_array(4, value)
            return    
        self._set_int32_array(4, value)

    @property
    def conn_str(self) -> List[str]:
        """
        DSS property name: conn
        DSS property index: 4
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 4)

    @conn_str.setter
    def conn_str(self, value: AnyStr):
        self.conn = value

    @property
    def kV(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: kV
        DSS property index: 5
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 5)

    @kV.setter
    def kV(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(5, value)

    @property
    def kVA(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: kVA
        DSS property index: 6
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 6)

    @kVA.setter
    def kVA(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(6, value)

    @property
    def tap(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: tap
        DSS property index: 7
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 7)

    @tap.setter
    def tap(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(7, value)

    @property
    def pctR(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: %R
        DSS property index: 8
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 8)

    @pctR.setter
    def pctR(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(8, value)

    @property
    def Rneut(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: Rneut
        DSS property index: 9
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 9)

    @Rneut.setter
    def Rneut(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(9, value)

    @property
    def Xneut(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: Xneut
        DSS property index: 10
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 10)

    @Xneut.setter
    def Xneut(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(10, value)

    @property
    def conns(self) -> List[Connection]:
        """
        DSS property name: conns
        DSS property index: 11
        """
        return [Connection(val) for val in self._get_int32_list(self._lib.Obj_GetInt32Array, self._ptr, 11)]

    @conns.setter
    def conns(self, value: Union[List[Union[int,Connection]], List[AnyStr]]):
        if not isinstance(value, int):
            self._set_string_array(11, value)
            return    
        self._set_int32_array(11, value)

    @property
    def conns_str(self) -> List[str]:
        """
        DSS property name: conns
        DSS property index: 11
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 11)

    @conns_str.setter
    def conns_str(self, value: AnyStr):
        self.conns = value

    @property
    def kVs(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: kVs
        DSS property index: 12
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 12)

    @kVs.setter
    def kVs(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(12, value)

    @property
    def kVAs(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: kVAs
        DSS property index: 13
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 13)

    @kVAs.setter
    def kVAs(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(13, value)

    @property
    def taps(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: taps
        DSS property index: 14
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 14)

    @taps.setter
    def taps(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(14, value)

    @property
    def Xhl(self) -> float:
        """
        DSS property name: Xhl
        DSS property index: 15
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @Xhl.setter
    def Xhl(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def Xht(self) -> float:
        """
        DSS property name: Xht
        DSS property index: 16
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    @Xht.setter
    def Xht(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 16, value)

    @property
    def Xlt(self) -> float:
        """
        DSS property name: Xlt
        DSS property index: 17
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    @Xlt.setter
    def Xlt(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 17, value)

    @property
    def Xscarray(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: Xscarray
        DSS property index: 18
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 18)

    @Xscarray.setter
    def Xscarray(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(18, value)

    @property
    def thermal(self) -> float:
        """
        DSS property name: thermal
        DSS property index: 19
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    @thermal.setter
    def thermal(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 19, value)

    @property
    def n(self) -> float:
        """
        DSS property name: n
        DSS property index: 20
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    @n.setter
    def n(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 20, value)

    @property
    def m(self) -> float:
        """
        DSS property name: m
        DSS property index: 21
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @m.setter
    def m(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    @property
    def flrise(self) -> float:
        """
        DSS property name: flrise
        DSS property index: 22
        """
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    @flrise.setter
    def flrise(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 22, value)

    @property
    def hsrise(self) -> float:
        """
        DSS property name: hsrise
        DSS property index: 23
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    @hsrise.setter
    def hsrise(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 23, value)

    @property
    def pctloadloss(self) -> float:
        """
        DSS property name: %loadloss
        DSS property index: 24
        """
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    @pctloadloss.setter
    def pctloadloss(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 24, value)

    @property
    def pctnoloadloss(self) -> float:
        """
        DSS property name: %noloadloss
        DSS property index: 25
        """
        return self._lib.Obj_GetFloat64(self._ptr, 25)

    @pctnoloadloss.setter
    def pctnoloadloss(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 25, value)

    @property
    def normhkVA(self) -> float:
        """
        DSS property name: normhkVA
        DSS property index: 26
        """
        return self._lib.Obj_GetFloat64(self._ptr, 26)

    @normhkVA.setter
    def normhkVA(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 26, value)

    @property
    def emerghkVA(self) -> float:
        """
        DSS property name: emerghkVA
        DSS property index: 27
        """
        return self._lib.Obj_GetFloat64(self._ptr, 27)

    @emerghkVA.setter
    def emerghkVA(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 27, value)

    @property
    def MaxTap(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: MaxTap
        DSS property index: 28
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 28)

    @MaxTap.setter
    def MaxTap(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(28, value)

    @property
    def MinTap(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: MinTap
        DSS property index: 29
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 29)

    @MinTap.setter
    def MinTap(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(29, value)

    @property
    def NumTaps(self) -> npt.NDArray[np.int32]:
        """
        DSS property name: NumTaps
        DSS property index: 30
        """
        return self._get_int32_array(self._lib.Obj_GetInt32Array, self._ptr, 30)

    @NumTaps.setter
    def NumTaps(self, value: npt.NDArray[np.int32]):
        self._set_int32_array(30, value)

    @property
    def pctimag(self) -> float:
        """
        DSS property name: %imag
        DSS property index: 31
        """
        return self._lib.Obj_GetFloat64(self._ptr, 31)

    @pctimag.setter
    def pctimag(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 31, value)

    @property
    def ppm_antifloat(self) -> float:
        """
        DSS property name: ppm_antifloat
        DSS property index: 32
        """
        return self._lib.Obj_GetFloat64(self._ptr, 32)

    @ppm_antifloat.setter
    def ppm_antifloat(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 32, value)

    @property
    def pctRs(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: %Rs
        DSS property index: 33
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 33)

    @pctRs.setter
    def pctRs(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(33, value)

    @property
    def X12(self) -> float:
        """
        DSS property name: X12
        DSS property index: 34
        """
        return self._lib.Obj_GetFloat64(self._ptr, 34)

    @X12.setter
    def X12(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 34, value)

    @property
    def X13(self) -> float:
        """
        DSS property name: X13
        DSS property index: 35
        """
        return self._lib.Obj_GetFloat64(self._ptr, 35)

    @X13.setter
    def X13(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 35, value)

    @property
    def X23(self) -> float:
        """
        DSS property name: X23
        DSS property index: 36
        """
        return self._lib.Obj_GetFloat64(self._ptr, 36)

    @X23.setter
    def X23(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 36, value)

    @property
    def RdcOhms(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: RdcOhms
        DSS property index: 37
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 37)

    @RdcOhms.setter
    def RdcOhms(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(37, value)

    @property
    def Seasons(self) -> int:
        """
        DSS property name: Seasons
        DSS property index: 38
        """
        return self._lib.Obj_GetInt32(self._ptr, 38)

    @Seasons.setter
    def Seasons(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 38, value)

    @property
    def Ratings(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: Ratings
        DSS property index: 39
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 39)

    @Ratings.setter
    def Ratings(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(39, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 40
        """
        self._set_string(40, value)

class Line(DSSObj):
    _cls_name = 'Line'
    _cls_idx = 15
    _cls_prop_idx = {
        'bus1': 1,
        'bus2': 2,
        'linecode': 3,
        'length': 4,
        'phases': 5,
        'r1': 6,
        'x1': 7,
        'r0': 8,
        'x0': 9,
        'c1': 10,
        'c0': 11,
        'rmatrix': 12,
        'xmatrix': 13,
        'cmatrix': 14,
        'switch': 15,
        'rg': 16,
        'xg': 17,
        'rho': 18,
        'geometry': 19,
        'units': 20,
        'spacing': 21,
        'wires': 22,
        'earthmodel': 23,
        'cncables': 24,
        'tscables': 25,
        'b1': 26,
        'b0': 27,
        'seasons': 28,
        'ratings': 29,
        'linetype': 30,
        'normamps': 31,
        'emergamps': 32,
        'faultrate': 33,
        'pctperm': 34,
        'repair': 35,
        'basefreq': 36,
        'enabled': 37,
        'like': 38,
    }

    @property
    def bus1(self) -> str:
        """
        DSS property name: bus1
        DSS property index: 1
        """
        return self._get_prop_string(1)

    @bus1.setter
    def bus1(self, value: AnyStr):
        self._set_string(1, value)

    @property
    def bus2(self) -> str:
        """
        DSS property name: bus2
        DSS property index: 2
        """
        return self._get_prop_string(2)

    @bus2.setter
    def bus2(self, value: AnyStr):
        self._set_string(2, value)

    @property
    def linecode(self) -> str:
        """
        DSS property name: linecode
        DSS property index: 3
        """
        return self._get_prop_string(3)

    @linecode.setter
    def linecode(self, value: Union[AnyStr, LineCode]):
        if isinstance(value, DSSObj):
            self._set_obj(3, value)
            return

        self._set_string(3, value)

    @property
    def linecode_obj(self) -> LineCode:
        """
        DSS property name: linecode
        DSS property index: 3
        """
        return self._get_obj(3, LineCode)

    @linecode_obj.setter
    def linecode_obj(self, value: LineCode):
        self._set_obj(3, value)

    @property
    def length(self) -> float:
        """
        DSS property name: length
        DSS property index: 4
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @length.setter
    def length(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def phases(self) -> int:
        """
        DSS property name: phases
        DSS property index: 5
        """
        return self._lib.Obj_GetInt32(self._ptr, 5)

    @phases.setter
    def phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 5, value)

    @property
    def r1(self) -> float:
        """
        DSS property name: r1
        DSS property index: 6
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    @r1.setter
    def r1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 6, value)

    @property
    def x1(self) -> float:
        """
        DSS property name: x1
        DSS property index: 7
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @x1.setter
    def x1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def r0(self) -> float:
        """
        DSS property name: r0
        DSS property index: 8
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @r0.setter
    def r0(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def x0(self) -> float:
        """
        DSS property name: x0
        DSS property index: 9
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @x0.setter
    def x0(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def C1(self) -> float:
        """
        DSS property name: C1
        DSS property index: 10
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @C1.setter
    def C1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def C0(self) -> float:
        """
        DSS property name: C0
        DSS property index: 11
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @C0.setter
    def C0(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def rmatrix(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: rmatrix
        DSS property index: 12
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 12)

    @rmatrix.setter
    def rmatrix(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(12, value)

    @property
    def xmatrix(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: xmatrix
        DSS property index: 13
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 13)

    @xmatrix.setter
    def xmatrix(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(13, value)

    @property
    def cmatrix(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: cmatrix
        DSS property index: 14
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 14)

    @cmatrix.setter
    def cmatrix(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(14, value)

    @property
    def Switch(self) -> bool:
        """
        DSS property name: Switch
        DSS property index: 15
        """
        return self._lib.Obj_GetInt32(self._ptr, 15) != 0

    @Switch.setter
    def Switch(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 15, value)

    @property
    def Rg(self) -> float:
        """
        DSS property name: Rg
        DSS property index: 16
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    @Rg.setter
    def Rg(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 16, value)

    @property
    def Xg(self) -> float:
        """
        DSS property name: Xg
        DSS property index: 17
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    @Xg.setter
    def Xg(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 17, value)

    @property
    def rho(self) -> float:
        """
        DSS property name: rho
        DSS property index: 18
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    @rho.setter
    def rho(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 18, value)

    @property
    def geometry(self) -> str:
        """
        DSS property name: geometry
        DSS property index: 19
        """
        return self._get_prop_string(19)

    @geometry.setter
    def geometry(self, value: Union[AnyStr, LineGeometry]):
        if isinstance(value, DSSObj):
            self._set_obj(19, value)
            return

        self._set_string(19, value)

    @property
    def geometry_obj(self) -> LineGeometry:
        """
        DSS property name: geometry
        DSS property index: 19
        """
        return self._get_obj(19, LineGeometry)

    @geometry_obj.setter
    def geometry_obj(self, value: LineGeometry):
        self._set_obj(19, value)

    @property
    def units(self) -> DimensionUnits:
        """
    DSS property name: units
    DSS property index: 20
    """
        return DimensionUnits(self._lib.Obj_GetInt32(self._ptr, 20))

    @units.setter
    def units(self, value: Union[AnyStr, int, DimensionUnits]):
        if not isinstance(value, int):
            self._set_string(20, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 20, value)

    @property
    def units_str(self) -> str:
        """
        DSS property name: units
        DSS property index: 20
        """
        return self._get_prop_string(20)

    @units_str.setter
    def units_str(self, value: AnyStr):
        self.units = value

    @property
    def spacing(self) -> str:
        """
        DSS property name: spacing
        DSS property index: 21
        """
        return self._get_prop_string(21)

    @spacing.setter
    def spacing(self, value: Union[AnyStr, LineSpacing]):
        if isinstance(value, DSSObj):
            self._set_obj(21, value)
            return

        self._set_string(21, value)

    @property
    def spacing_obj(self) -> LineSpacing:
        """
        DSS property name: spacing
        DSS property index: 21
        """
        return self._get_obj(21, LineSpacing)

    @spacing_obj.setter
    def spacing_obj(self, value: LineSpacing):
        self._set_obj(21, value)

    @property
    def wires(self) -> List[str]:
        """
        DSS property name: wires
        DSS property index: 22
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 22)

    @wires.setter
    def wires(self, value: List[Union[AnyStr, WireData]]):
        if value is None or len(value) == 0 or not isinstance(value[0], DSSObj):
            self._set_string_array(22, value)
            return

        self._set_obj_array(22, value)

    @property
    def wires_obj(self) -> List[WireData]:
        """
        DSS property name: wires
        DSS property index: 22
        """
        return self._get_obj_array(22, WireData)

    @wires_obj.setter
    def wires_obj(self, value: List[WireData]):
        self._set_obj_array(22, value)

    @property
    def earthmodel(self) -> EarthModel:
        """
    DSS property name: EarthModel
    DSS property index: 23
    """
        return EarthModel(self._lib.Obj_GetInt32(self._ptr, 23))

    @earthmodel.setter
    def earthmodel(self, value: Union[AnyStr, int, EarthModel]):
        if not isinstance(value, int):
            self._set_string(23, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 23, value)

    @property
    def earthmodel_str(self) -> str:
        """
        DSS property name: EarthModel
        DSS property index: 23
        """
        return self._get_prop_string(23)

    @earthmodel_str.setter
    def earthmodel_str(self, value: AnyStr):
        self.earthmodel = value

    @property
    def cncables(self) -> List[str]:
        """
        DSS property name: cncables
        DSS property index: 24
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 24)

    @cncables.setter
    def cncables(self, value: List[Union[AnyStr, CNData]]):
        if value is None or len(value) == 0 or not isinstance(value[0], DSSObj):
            self._set_string_array(24, value)
            return

        self._set_obj_array(24, value)

    @property
    def cncables_obj(self) -> List[CNData]:
        """
        DSS property name: cncables
        DSS property index: 24
        """
        return self._get_obj_array(24, CNData)

    @cncables_obj.setter
    def cncables_obj(self, value: List[CNData]):
        self._set_obj_array(24, value)

    @property
    def tscables(self) -> List[str]:
        """
        DSS property name: tscables
        DSS property index: 25
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 25)

    @tscables.setter
    def tscables(self, value: List[Union[AnyStr, TSData]]):
        if value is None or len(value) == 0 or not isinstance(value[0], DSSObj):
            self._set_string_array(25, value)
            return

        self._set_obj_array(25, value)

    @property
    def tscables_obj(self) -> List[TSData]:
        """
        DSS property name: tscables
        DSS property index: 25
        """
        return self._get_obj_array(25, TSData)

    @tscables_obj.setter
    def tscables_obj(self, value: List[TSData]):
        self._set_obj_array(25, value)

    @property
    def B1(self) -> float:
        """
        DSS property name: B1
        DSS property index: 26
        """
        return self._lib.Obj_GetFloat64(self._ptr, 26)

    @B1.setter
    def B1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 26, value)

    @property
    def B0(self) -> float:
        """
        DSS property name: B0
        DSS property index: 27
        """
        return self._lib.Obj_GetFloat64(self._ptr, 27)

    @B0.setter
    def B0(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 27, value)

    @property
    def Seasons(self) -> int:
        """
        DSS property name: Seasons
        DSS property index: 28
        """
        return self._lib.Obj_GetInt32(self._ptr, 28)

    @Seasons.setter
    def Seasons(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 28, value)

    @property
    def Ratings(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: Ratings
        DSS property index: 29
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 29)

    @Ratings.setter
    def Ratings(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(29, value)

    @property
    def linetype(self) -> LineType:
        """
    DSS property name: LineType
    DSS property index: 30
    """
        return LineType(self._lib.Obj_GetInt32(self._ptr, 30))

    @linetype.setter
    def linetype(self, value: Union[AnyStr, int, LineType]):
        if not isinstance(value, int):
            self._set_string(30, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 30, value)

    @property
    def linetype_str(self) -> str:
        """
        DSS property name: LineType
        DSS property index: 30
        """
        return self._get_prop_string(30)

    @linetype_str.setter
    def linetype_str(self, value: AnyStr):
        self.linetype = value

    @property
    def normamps(self) -> float:
        """
        DSS property name: normamps
        DSS property index: 31
        """
        return self._lib.Obj_GetFloat64(self._ptr, 31)

    @normamps.setter
    def normamps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 31, value)

    @property
    def emergamps(self) -> float:
        """
        DSS property name: emergamps
        DSS property index: 32
        """
        return self._lib.Obj_GetFloat64(self._ptr, 32)

    @emergamps.setter
    def emergamps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 32, value)

    @property
    def faultrate(self) -> float:
        """
        DSS property name: faultrate
        DSS property index: 33
        """
        return self._lib.Obj_GetFloat64(self._ptr, 33)

    @faultrate.setter
    def faultrate(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 33, value)

    @property
    def pctperm(self) -> float:
        """
        DSS property name: pctperm
        DSS property index: 34
        """
        return self._lib.Obj_GetFloat64(self._ptr, 34)

    @pctperm.setter
    def pctperm(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 34, value)

    @property
    def repair(self) -> float:
        """
        DSS property name: repair
        DSS property index: 35
        """
        return self._lib.Obj_GetFloat64(self._ptr, 35)

    @repair.setter
    def repair(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 35, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 36
        """
        return self._lib.Obj_GetFloat64(self._ptr, 36)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 36, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 37
        """
        return self._lib.Obj_GetInt32(self._ptr, 37) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 37, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 38
        """
        self._set_string(38, value)

class Vsource(DSSObj):
    _cls_name = 'Vsource'
    _cls_idx = 16
    _cls_prop_idx = {
        'bus1': 1,
        'basekv': 2,
        'pu': 3,
        'angle': 4,
        'frequency': 5,
        'phases': 6,
        'mvasc3': 7,
        'mvasc1': 8,
        'x1r1': 9,
        'x0r0': 10,
        'isc3': 11,
        'isc1': 12,
        'r1': 13,
        'x1': 14,
        'r0': 15,
        'x0': 16,
        'scantype': 17,
        'sequence': 18,
        'bus2': 19,
        'z1': 20,
        'z0': 21,
        'z2': 22,
        'puz1': 23,
        'puz0': 24,
        'puz2': 25,
        'basemva': 26,
        'yearly': 27,
        'daily': 28,
        'duty': 29,
        'model': 30,
        'puzideal': 31,
        'spectrum': 32,
        'basefreq': 33,
        'enabled': 34,
        'like': 35,
    }

    # Class-specific enumerations
    class VSourceModel(IntEnum):
        """VSource: Model (DSS enumeration for Vsource)"""
        Thevenin = 0 # Thevenin
        Ideal = 1 # Ideal


    @property
    def bus1(self) -> str:
        """
        DSS property name: bus1
        DSS property index: 1
        """
        return self._get_prop_string(1)

    @bus1.setter
    def bus1(self, value: AnyStr):
        self._set_string(1, value)

    @property
    def basekv(self) -> float:
        """
        DSS property name: basekv
        DSS property index: 2
        """
        return self._lib.Obj_GetFloat64(self._ptr, 2)

    @basekv.setter
    def basekv(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 2, value)

    @property
    def pu(self) -> float:
        """
        DSS property name: pu
        DSS property index: 3
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @pu.setter
    def pu(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def angle(self) -> float:
        """
        DSS property name: angle
        DSS property index: 4
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @angle.setter
    def angle(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def frequency(self) -> float:
        """
        DSS property name: frequency
        DSS property index: 5
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @frequency.setter
    def frequency(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def phases(self) -> int:
        """
        DSS property name: phases
        DSS property index: 6
        """
        return self._lib.Obj_GetInt32(self._ptr, 6)

    @phases.setter
    def phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 6, value)

    @property
    def MVAsc3(self) -> float:
        """
        DSS property name: MVAsc3
        DSS property index: 7
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @MVAsc3.setter
    def MVAsc3(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def MVAsc1(self) -> float:
        """
        DSS property name: MVAsc1
        DSS property index: 8
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @MVAsc1.setter
    def MVAsc1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def x1r1(self) -> float:
        """
        DSS property name: x1r1
        DSS property index: 9
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @x1r1.setter
    def x1r1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def x0r0(self) -> float:
        """
        DSS property name: x0r0
        DSS property index: 10
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @x0r0.setter
    def x0r0(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def Isc3(self) -> float:
        """
        DSS property name: Isc3
        DSS property index: 11
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @Isc3.setter
    def Isc3(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def Isc1(self) -> float:
        """
        DSS property name: Isc1
        DSS property index: 12
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @Isc1.setter
    def Isc1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def R1(self) -> float:
        """
        DSS property name: R1
        DSS property index: 13
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @R1.setter
    def R1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def X1(self) -> float:
        """
        DSS property name: X1
        DSS property index: 14
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @X1.setter
    def X1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def R0(self) -> float:
        """
        DSS property name: R0
        DSS property index: 15
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @R0.setter
    def R0(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def X0(self) -> float:
        """
        DSS property name: X0
        DSS property index: 16
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    @X0.setter
    def X0(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 16, value)

    @property
    def scantype(self) -> ScanType:
        """
    DSS property name: ScanType
    DSS property index: 17
    """
        return ScanType(self._lib.Obj_GetInt32(self._ptr, 17))

    @scantype.setter
    def scantype(self, value: Union[AnyStr, int, ScanType]):
        if not isinstance(value, int):
            self._set_string(17, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 17, value)

    @property
    def scantype_str(self) -> str:
        """
        DSS property name: ScanType
        DSS property index: 17
        """
        return self._get_prop_string(17)

    @scantype_str.setter
    def scantype_str(self, value: AnyStr):
        self.scantype = value

    @property
    def Sequence(self) -> SequenceType:
        """
    DSS property name: Sequence
    DSS property index: 18
    """
        return SequenceType(self._lib.Obj_GetInt32(self._ptr, 18))

    @Sequence.setter
    def Sequence(self, value: Union[AnyStr, int, SequenceType]):
        if not isinstance(value, int):
            self._set_string(18, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 18, value)

    @property
    def Sequence_str(self) -> str:
        """
        DSS property name: Sequence
        DSS property index: 18
        """
        return self._get_prop_string(18)

    @Sequence_str.setter
    def Sequence_str(self, value: AnyStr):
        self.Sequence = value

    @property
    def bus2(self) -> str:
        """
        DSS property name: bus2
        DSS property index: 19
        """
        return self._get_prop_string(19)

    @bus2.setter
    def bus2(self, value: AnyStr):
        self._set_string(19, value)

    @property
    def Z1(self) -> complex:
        """
        DSS property name: Z1
        DSS property index: 20
        """
        return self._get_complex(20)

    @Z1.setter
    def Z1(self, value: complex):
        self._set_complex(20, value)

    @property
    def Z0(self) -> complex:
        """
        DSS property name: Z0
        DSS property index: 21
        """
        return self._get_complex(21)

    @Z0.setter
    def Z0(self, value: complex):
        self._set_complex(21, value)

    @property
    def Z2(self) -> complex:
        """
        DSS property name: Z2
        DSS property index: 22
        """
        return self._get_complex(22)

    @Z2.setter
    def Z2(self, value: complex):
        self._set_complex(22, value)

    @property
    def puZ1(self) -> complex:
        """
        DSS property name: puZ1
        DSS property index: 23
        """
        return self._get_complex(23)

    @puZ1.setter
    def puZ1(self, value: complex):
        self._set_complex(23, value)

    @property
    def puZ0(self) -> complex:
        """
        DSS property name: puZ0
        DSS property index: 24
        """
        return self._get_complex(24)

    @puZ0.setter
    def puZ0(self, value: complex):
        self._set_complex(24, value)

    @property
    def puZ2(self) -> complex:
        """
        DSS property name: puZ2
        DSS property index: 25
        """
        return self._get_complex(25)

    @puZ2.setter
    def puZ2(self, value: complex):
        self._set_complex(25, value)

    @property
    def baseMVA(self) -> float:
        """
        DSS property name: baseMVA
        DSS property index: 26
        """
        return self._lib.Obj_GetFloat64(self._ptr, 26)

    @baseMVA.setter
    def baseMVA(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 26, value)

    @property
    def Yearly(self) -> str:
        """
        DSS property name: Yearly
        DSS property index: 27
        """
        return self._get_prop_string(27)

    @Yearly.setter
    def Yearly(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(27, value)
            return

        self._set_string(27, value)

    @property
    def Yearly_obj(self) -> LoadShape:
        """
        DSS property name: Yearly
        DSS property index: 27
        """
        return self._get_obj(27, LoadShape)

    @Yearly_obj.setter
    def Yearly_obj(self, value: LoadShape):
        self._set_obj(27, value)

    @property
    def Daily(self) -> str:
        """
        DSS property name: Daily
        DSS property index: 28
        """
        return self._get_prop_string(28)

    @Daily.setter
    def Daily(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(28, value)
            return

        self._set_string(28, value)

    @property
    def Daily_obj(self) -> LoadShape:
        """
        DSS property name: Daily
        DSS property index: 28
        """
        return self._get_obj(28, LoadShape)

    @Daily_obj.setter
    def Daily_obj(self, value: LoadShape):
        self._set_obj(28, value)

    @property
    def Duty(self) -> str:
        """
        DSS property name: Duty
        DSS property index: 29
        """
        return self._get_prop_string(29)

    @Duty.setter
    def Duty(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(29, value)
            return

        self._set_string(29, value)

    @property
    def Duty_obj(self) -> LoadShape:
        """
        DSS property name: Duty
        DSS property index: 29
        """
        return self._get_obj(29, LoadShape)

    @Duty_obj.setter
    def Duty_obj(self, value: LoadShape):
        self._set_obj(29, value)

    @property
    def Model(self) -> VSourceModel:
        """
    DSS property name: Model
    DSS property index: 30
    """
        return VSourceModel(self._lib.Obj_GetInt32(self._ptr, 30))

    @Model.setter
    def Model(self, value: Union[AnyStr, int, VSourceModel]):
        if not isinstance(value, int):
            self._set_string(30, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 30, value)

    @property
    def Model_str(self) -> str:
        """
        DSS property name: Model
        DSS property index: 30
        """
        return self._get_prop_string(30)

    @Model_str.setter
    def Model_str(self, value: AnyStr):
        self.Model = value

    @property
    def puZideal(self) -> complex:
        """
        DSS property name: puZideal
        DSS property index: 31
        """
        return self._get_complex(31)

    @puZideal.setter
    def puZideal(self, value: complex):
        self._set_complex(31, value)

    @property
    def spectrum(self) -> str:
        """
        DSS property name: spectrum
        DSS property index: 32
        """
        return self._get_prop_string(32)

    @spectrum.setter
    def spectrum(self, value: Union[AnyStr, Spectrum]):
        if isinstance(value, DSSObj):
            self._set_obj(32, value)
            return

        self._set_string(32, value)

    @property
    def spectrum_obj(self) -> Spectrum:
        """
        DSS property name: spectrum
        DSS property index: 32
        """
        return self._get_obj(32, Spectrum)

    @spectrum_obj.setter
    def spectrum_obj(self, value: Spectrum):
        self._set_obj(32, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 33
        """
        return self._lib.Obj_GetFloat64(self._ptr, 33)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 33, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 34
        """
        return self._lib.Obj_GetInt32(self._ptr, 34) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 34, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 35
        """
        self._set_string(35, value)

class Isource(DSSObj):
    _cls_name = 'Isource'
    _cls_idx = 17
    _cls_prop_idx = {
        'bus1': 1,
        'amps': 2,
        'angle': 3,
        'frequency': 4,
        'phases': 5,
        'scantype': 6,
        'sequence': 7,
        'yearly': 8,
        'daily': 9,
        'duty': 10,
        'bus2': 11,
        'spectrum': 12,
        'basefreq': 13,
        'enabled': 14,
        'like': 15,
    }

    @property
    def bus1(self) -> str:
        """
        DSS property name: bus1
        DSS property index: 1
        """
        return self._get_prop_string(1)

    @bus1.setter
    def bus1(self, value: AnyStr):
        self._set_string(1, value)

    @property
    def amps(self) -> float:
        """
        DSS property name: amps
        DSS property index: 2
        """
        return self._lib.Obj_GetFloat64(self._ptr, 2)

    @amps.setter
    def amps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 2, value)

    @property
    def angle(self) -> float:
        """
        DSS property name: angle
        DSS property index: 3
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @angle.setter
    def angle(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def frequency(self) -> float:
        """
        DSS property name: frequency
        DSS property index: 4
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @frequency.setter
    def frequency(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def phases(self) -> int:
        """
        DSS property name: phases
        DSS property index: 5
        """
        return self._lib.Obj_GetInt32(self._ptr, 5)

    @phases.setter
    def phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 5, value)

    @property
    def scantype(self) -> ScanType:
        """
    DSS property name: scantype
    DSS property index: 6
    """
        return ScanType(self._lib.Obj_GetInt32(self._ptr, 6))

    @scantype.setter
    def scantype(self, value: Union[AnyStr, int, ScanType]):
        if not isinstance(value, int):
            self._set_string(6, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 6, value)

    @property
    def scantype_str(self) -> str:
        """
        DSS property name: scantype
        DSS property index: 6
        """
        return self._get_prop_string(6)

    @scantype_str.setter
    def scantype_str(self, value: AnyStr):
        self.scantype = value

    @property
    def sequence(self) -> SequenceType:
        """
    DSS property name: sequence
    DSS property index: 7
    """
        return SequenceType(self._lib.Obj_GetInt32(self._ptr, 7))

    @sequence.setter
    def sequence(self, value: Union[AnyStr, int, SequenceType]):
        if not isinstance(value, int):
            self._set_string(7, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 7, value)

    @property
    def sequence_str(self) -> str:
        """
        DSS property name: sequence
        DSS property index: 7
        """
        return self._get_prop_string(7)

    @sequence_str.setter
    def sequence_str(self, value: AnyStr):
        self.sequence = value

    @property
    def Yearly(self) -> str:
        """
        DSS property name: Yearly
        DSS property index: 8
        """
        return self._get_prop_string(8)

    @Yearly.setter
    def Yearly(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(8, value)
            return

        self._set_string(8, value)

    @property
    def Yearly_obj(self) -> LoadShape:
        """
        DSS property name: Yearly
        DSS property index: 8
        """
        return self._get_obj(8, LoadShape)

    @Yearly_obj.setter
    def Yearly_obj(self, value: LoadShape):
        self._set_obj(8, value)

    @property
    def Daily(self) -> str:
        """
        DSS property name: Daily
        DSS property index: 9
        """
        return self._get_prop_string(9)

    @Daily.setter
    def Daily(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(9, value)
            return

        self._set_string(9, value)

    @property
    def Daily_obj(self) -> LoadShape:
        """
        DSS property name: Daily
        DSS property index: 9
        """
        return self._get_obj(9, LoadShape)

    @Daily_obj.setter
    def Daily_obj(self, value: LoadShape):
        self._set_obj(9, value)

    @property
    def Duty(self) -> str:
        """
        DSS property name: Duty
        DSS property index: 10
        """
        return self._get_prop_string(10)

    @Duty.setter
    def Duty(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(10, value)
            return

        self._set_string(10, value)

    @property
    def Duty_obj(self) -> LoadShape:
        """
        DSS property name: Duty
        DSS property index: 10
        """
        return self._get_obj(10, LoadShape)

    @Duty_obj.setter
    def Duty_obj(self, value: LoadShape):
        self._set_obj(10, value)

    @property
    def Bus2(self) -> str:
        """
        DSS property name: Bus2
        DSS property index: 11
        """
        return self._get_prop_string(11)

    @Bus2.setter
    def Bus2(self, value: AnyStr):
        self._set_string(11, value)

    @property
    def spectrum(self) -> str:
        """
        DSS property name: spectrum
        DSS property index: 12
        """
        return self._get_prop_string(12)

    @spectrum.setter
    def spectrum(self, value: Union[AnyStr, Spectrum]):
        if isinstance(value, DSSObj):
            self._set_obj(12, value)
            return

        self._set_string(12, value)

    @property
    def spectrum_obj(self) -> Spectrum:
        """
        DSS property name: spectrum
        DSS property index: 12
        """
        return self._get_obj(12, Spectrum)

    @spectrum_obj.setter
    def spectrum_obj(self, value: Spectrum):
        self._set_obj(12, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 13
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 14
        """
        return self._lib.Obj_GetInt32(self._ptr, 14) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 14, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 15
        """
        self._set_string(15, value)

class VCCS(DSSObj):
    _cls_name = 'VCCS'
    _cls_idx = 18
    _cls_prop_idx = {
        'bus1': 1,
        'phases': 2,
        'prated': 3,
        'vrated': 4,
        'ppct': 5,
        'bp1': 6,
        'bp2': 7,
        'filter': 8,
        'fsample': 9,
        'rmsmode': 10,
        'imaxpu': 11,
        'vrmstau': 12,
        'irmstau': 13,
        'spectrum': 14,
        'basefreq': 15,
        'enabled': 16,
        'like': 17,
    }

    @property
    def bus1(self) -> str:
        """
        DSS property name: bus1
        DSS property index: 1
        """
        return self._get_prop_string(1)

    @bus1.setter
    def bus1(self, value: AnyStr):
        self._set_string(1, value)

    @property
    def phases(self) -> int:
        """
        DSS property name: phases
        DSS property index: 2
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @phases.setter
    def phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def prated(self) -> float:
        """
        DSS property name: prated
        DSS property index: 3
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @prated.setter
    def prated(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def vrated(self) -> float:
        """
        DSS property name: vrated
        DSS property index: 4
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @vrated.setter
    def vrated(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def ppct(self) -> float:
        """
        DSS property name: ppct
        DSS property index: 5
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @ppct.setter
    def ppct(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def bp1(self) -> str:
        """
        DSS property name: bp1
        DSS property index: 6
        """
        return self._get_prop_string(6)

    @bp1.setter
    def bp1(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(6, value)
            return

        self._set_string(6, value)

    @property
    def bp1_obj(self) -> XYcurve:
        """
        DSS property name: bp1
        DSS property index: 6
        """
        return self._get_obj(6, XYcurve)

    @bp1_obj.setter
    def bp1_obj(self, value: XYcurve):
        self._set_obj(6, value)

    @property
    def bp2(self) -> str:
        """
        DSS property name: bp2
        DSS property index: 7
        """
        return self._get_prop_string(7)

    @bp2.setter
    def bp2(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(7, value)
            return

        self._set_string(7, value)

    @property
    def bp2_obj(self) -> XYcurve:
        """
        DSS property name: bp2
        DSS property index: 7
        """
        return self._get_obj(7, XYcurve)

    @bp2_obj.setter
    def bp2_obj(self, value: XYcurve):
        self._set_obj(7, value)

    @property
    def filter(self) -> str:
        """
        DSS property name: filter
        DSS property index: 8
        """
        return self._get_prop_string(8)

    @filter.setter
    def filter(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(8, value)
            return

        self._set_string(8, value)

    @property
    def filter_obj(self) -> XYcurve:
        """
        DSS property name: filter
        DSS property index: 8
        """
        return self._get_obj(8, XYcurve)

    @filter_obj.setter
    def filter_obj(self, value: XYcurve):
        self._set_obj(8, value)

    @property
    def fsample(self) -> float:
        """
        DSS property name: fsample
        DSS property index: 9
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @fsample.setter
    def fsample(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def rmsmode(self) -> bool:
        """
        DSS property name: rmsmode
        DSS property index: 10
        """
        return self._lib.Obj_GetInt32(self._ptr, 10) != 0

    @rmsmode.setter
    def rmsmode(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 10, value)

    @property
    def imaxpu(self) -> float:
        """
        DSS property name: imaxpu
        DSS property index: 11
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @imaxpu.setter
    def imaxpu(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def vrmstau(self) -> float:
        """
        DSS property name: vrmstau
        DSS property index: 12
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @vrmstau.setter
    def vrmstau(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def irmstau(self) -> float:
        """
        DSS property name: irmstau
        DSS property index: 13
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @irmstau.setter
    def irmstau(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def spectrum(self) -> str:
        """
        DSS property name: spectrum
        DSS property index: 14
        """
        return self._get_prop_string(14)

    @spectrum.setter
    def spectrum(self, value: Union[AnyStr, Spectrum]):
        if isinstance(value, DSSObj):
            self._set_obj(14, value)
            return

        self._set_string(14, value)

    @property
    def spectrum_obj(self) -> Spectrum:
        """
        DSS property name: spectrum
        DSS property index: 14
        """
        return self._get_obj(14, Spectrum)

    @spectrum_obj.setter
    def spectrum_obj(self, value: Spectrum):
        self._set_obj(14, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 15
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 16
        """
        return self._lib.Obj_GetInt32(self._ptr, 16) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 16, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 17
        """
        self._set_string(17, value)

class Load(DSSObj):
    _cls_name = 'Load'
    _cls_idx = 19
    _cls_prop_idx = {
        'phases': 1,
        'bus1': 2,
        'kv': 3,
        'kw': 4,
        'pf': 5,
        'model': 6,
        'yearly': 7,
        'daily': 8,
        'duty': 9,
        'growth': 10,
        'conn': 11,
        'kvar': 12,
        'rneut': 13,
        'xneut': 14,
        'status': 15,
        'cls': 16,
        'class': 16,
        'vminpu': 17,
        'vmaxpu': 18,
        'vminnorm': 19,
        'vminemerg': 20,
        'xfkva': 21,
        'allocationfactor': 22,
        'kva': 23,
        'pctmean': 24,
        '%mean': 24,
        'pctstddev': 25,
        '%stddev': 25,
        'cvrwatts': 26,
        'cvrvars': 27,
        'kwh': 28,
        'kwhdays': 29,
        'cfactor': 30,
        'cvrcurve': 31,
        'numcust': 32,
        'zipv': 33,
        'pctseriesrl': 34,
        '%seriesrl': 34,
        'relweight': 35,
        'vlowpu': 36,
        'puxharm': 37,
        'xrharm': 38,
        'spectrum': 39,
        'basefreq': 40,
        'enabled': 41,
        'like': 42,
    }

    # Class-specific enumerations
    class LoadModel(IntEnum):
        """Load: Model (DSS enumeration for Load)"""
        ConstantPQ = 1 # Constant PQ
        ConstantZ = 2 # Constant Z
        Motor = 3 # Motor (constant P, quadratic Q)
        CVR = 4 # CVR (linear P, quadratic Q)
        ConstantI = 5 # Constant I
        ConstantP_fixedQ = 6 # Constant P, fixed Q
        ConstantP_fixedX = 7 # Constant P, fixed X
        ZIPV = 8 # ZIPV

    class LoadStatus(IntEnum):
        """Load: Status (DSS enumeration for Load)"""
        Variable = 0 # Variable
        Fixed = 1 # Fixed
        Exempt = 2 # Exempt


    @property
    def phases(self) -> int:
        """
        DSS property name: phases
        DSS property index: 1
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @phases.setter
    def phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def bus1(self) -> str:
        """
        DSS property name: bus1
        DSS property index: 2
        """
        return self._get_prop_string(2)

    @bus1.setter
    def bus1(self, value: AnyStr):
        self._set_string(2, value)

    @property
    def kV(self) -> float:
        """
        DSS property name: kV
        DSS property index: 3
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @kV.setter
    def kV(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def kW(self) -> float:
        """
        DSS property name: kW
        DSS property index: 4
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @kW.setter
    def kW(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def pf(self) -> float:
        """
        DSS property name: pf
        DSS property index: 5
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @pf.setter
    def pf(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def model(self) -> LoadModel:
        """
        DSS property name: model
        DSS property index: 6
        """
        return LoadModel(self._lib.Obj_GetInt32(self._ptr, 6))

    @model.setter
    def model(self, value: Union[int, LoadModel]):
        self._lib.Obj_SetInt32(self._ptr, 6, value)

    @property
    def yearly(self) -> str:
        """
        DSS property name: yearly
        DSS property index: 7
        """
        return self._get_prop_string(7)

    @yearly.setter
    def yearly(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(7, value)
            return

        self._set_string(7, value)

    @property
    def yearly_obj(self) -> LoadShape:
        """
        DSS property name: yearly
        DSS property index: 7
        """
        return self._get_obj(7, LoadShape)

    @yearly_obj.setter
    def yearly_obj(self, value: LoadShape):
        self._set_obj(7, value)

    @property
    def daily(self) -> str:
        """
        DSS property name: daily
        DSS property index: 8
        """
        return self._get_prop_string(8)

    @daily.setter
    def daily(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(8, value)
            return

        self._set_string(8, value)

    @property
    def daily_obj(self) -> LoadShape:
        """
        DSS property name: daily
        DSS property index: 8
        """
        return self._get_obj(8, LoadShape)

    @daily_obj.setter
    def daily_obj(self, value: LoadShape):
        self._set_obj(8, value)

    @property
    def duty(self) -> str:
        """
        DSS property name: duty
        DSS property index: 9
        """
        return self._get_prop_string(9)

    @duty.setter
    def duty(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(9, value)
            return

        self._set_string(9, value)

    @property
    def duty_obj(self) -> LoadShape:
        """
        DSS property name: duty
        DSS property index: 9
        """
        return self._get_obj(9, LoadShape)

    @duty_obj.setter
    def duty_obj(self, value: LoadShape):
        self._set_obj(9, value)

    @property
    def growth(self) -> str:
        """
        DSS property name: growth
        DSS property index: 10
        """
        return self._get_prop_string(10)

    @growth.setter
    def growth(self, value: Union[AnyStr, GrowthShape]):
        if isinstance(value, DSSObj):
            self._set_obj(10, value)
            return

        self._set_string(10, value)

    @property
    def growth_obj(self) -> GrowthShape:
        """
        DSS property name: growth
        DSS property index: 10
        """
        return self._get_obj(10, GrowthShape)

    @growth_obj.setter
    def growth_obj(self, value: GrowthShape):
        self._set_obj(10, value)

    @property
    def conn(self) -> Connection:
        """
    DSS property name: conn
    DSS property index: 11
    """
        return Connection(self._lib.Obj_GetInt32(self._ptr, 11))

    @conn.setter
    def conn(self, value: Union[AnyStr, int, Connection]):
        if not isinstance(value, int):
            self._set_string(11, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 11, value)

    @property
    def conn_str(self) -> str:
        """
        DSS property name: conn
        DSS property index: 11
        """
        return self._get_prop_string(11)

    @conn_str.setter
    def conn_str(self, value: AnyStr):
        self.conn = value

    @property
    def kvar(self) -> float:
        """
        DSS property name: kvar
        DSS property index: 12
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @kvar.setter
    def kvar(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def Rneut(self) -> float:
        """
        DSS property name: Rneut
        DSS property index: 13
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @Rneut.setter
    def Rneut(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def Xneut(self) -> float:
        """
        DSS property name: Xneut
        DSS property index: 14
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @Xneut.setter
    def Xneut(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def status(self) -> LoadStatus:
        """
    DSS property name: status
    DSS property index: 15
    """
        return LoadStatus(self._lib.Obj_GetInt32(self._ptr, 15))

    @status.setter
    def status(self, value: Union[AnyStr, int, LoadStatus]):
        if not isinstance(value, int):
            self._set_string(15, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 15, value)

    @property
    def status_str(self) -> str:
        """
        DSS property name: status
        DSS property index: 15
        """
        return self._get_prop_string(15)

    @status_str.setter
    def status_str(self, value: AnyStr):
        self.status = value

    @property
    def cls(self) -> int:
        """
        DSS property name: class
        DSS property index: 16
        """
        return self._lib.Obj_GetInt32(self._ptr, 16)

    @cls.setter
    def cls(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 16, value)

    @property
    def Vminpu(self) -> float:
        """
        DSS property name: Vminpu
        DSS property index: 17
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    @Vminpu.setter
    def Vminpu(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 17, value)

    @property
    def Vmaxpu(self) -> float:
        """
        DSS property name: Vmaxpu
        DSS property index: 18
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    @Vmaxpu.setter
    def Vmaxpu(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 18, value)

    @property
    def Vminnorm(self) -> float:
        """
        DSS property name: Vminnorm
        DSS property index: 19
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    @Vminnorm.setter
    def Vminnorm(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 19, value)

    @property
    def Vminemerg(self) -> float:
        """
        DSS property name: Vminemerg
        DSS property index: 20
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    @Vminemerg.setter
    def Vminemerg(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 20, value)

    @property
    def xfkVA(self) -> float:
        """
        DSS property name: xfkVA
        DSS property index: 21
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @xfkVA.setter
    def xfkVA(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    @property
    def allocationfactor(self) -> float:
        """
        DSS property name: allocationfactor
        DSS property index: 22
        """
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    @allocationfactor.setter
    def allocationfactor(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 22, value)

    @property
    def kVA(self) -> float:
        """
        DSS property name: kVA
        DSS property index: 23
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    @kVA.setter
    def kVA(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 23, value)

    @property
    def pctmean(self) -> float:
        """
        DSS property name: %mean
        DSS property index: 24
        """
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    @pctmean.setter
    def pctmean(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 24, value)

    @property
    def pctstddev(self) -> float:
        """
        DSS property name: %stddev
        DSS property index: 25
        """
        return self._lib.Obj_GetFloat64(self._ptr, 25)

    @pctstddev.setter
    def pctstddev(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 25, value)

    @property
    def CVRwatts(self) -> float:
        """
        DSS property name: CVRwatts
        DSS property index: 26
        """
        return self._lib.Obj_GetFloat64(self._ptr, 26)

    @CVRwatts.setter
    def CVRwatts(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 26, value)

    @property
    def CVRvars(self) -> float:
        """
        DSS property name: CVRvars
        DSS property index: 27
        """
        return self._lib.Obj_GetFloat64(self._ptr, 27)

    @CVRvars.setter
    def CVRvars(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 27, value)

    @property
    def kwh(self) -> float:
        """
        DSS property name: kwh
        DSS property index: 28
        """
        return self._lib.Obj_GetFloat64(self._ptr, 28)

    @kwh.setter
    def kwh(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 28, value)

    @property
    def kwhdays(self) -> float:
        """
        DSS property name: kwhdays
        DSS property index: 29
        """
        return self._lib.Obj_GetFloat64(self._ptr, 29)

    @kwhdays.setter
    def kwhdays(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 29, value)

    @property
    def Cfactor(self) -> float:
        """
        DSS property name: Cfactor
        DSS property index: 30
        """
        return self._lib.Obj_GetFloat64(self._ptr, 30)

    @Cfactor.setter
    def Cfactor(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 30, value)

    @property
    def CVRcurve(self) -> str:
        """
        DSS property name: CVRcurve
        DSS property index: 31
        """
        return self._get_prop_string(31)

    @CVRcurve.setter
    def CVRcurve(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(31, value)
            return

        self._set_string(31, value)

    @property
    def CVRcurve_obj(self) -> LoadShape:
        """
        DSS property name: CVRcurve
        DSS property index: 31
        """
        return self._get_obj(31, LoadShape)

    @CVRcurve_obj.setter
    def CVRcurve_obj(self, value: LoadShape):
        self._set_obj(31, value)

    @property
    def NumCust(self) -> int:
        """
        DSS property name: NumCust
        DSS property index: 32
        """
        return self._lib.Obj_GetInt32(self._ptr, 32)

    @NumCust.setter
    def NumCust(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 32, value)

    @property
    def ZIPV(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: ZIPV
        DSS property index: 33
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 33)

    @ZIPV.setter
    def ZIPV(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(33, value)

    @property
    def pctSeriesRL(self) -> float:
        """
        DSS property name: %SeriesRL
        DSS property index: 34
        """
        return self._lib.Obj_GetFloat64(self._ptr, 34)

    @pctSeriesRL.setter
    def pctSeriesRL(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 34, value)

    @property
    def RelWeight(self) -> float:
        """
        DSS property name: RelWeight
        DSS property index: 35
        """
        return self._lib.Obj_GetFloat64(self._ptr, 35)

    @RelWeight.setter
    def RelWeight(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 35, value)

    @property
    def Vlowpu(self) -> float:
        """
        DSS property name: Vlowpu
        DSS property index: 36
        """
        return self._lib.Obj_GetFloat64(self._ptr, 36)

    @Vlowpu.setter
    def Vlowpu(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 36, value)

    @property
    def puXharm(self) -> float:
        """
        DSS property name: puXharm
        DSS property index: 37
        """
        return self._lib.Obj_GetFloat64(self._ptr, 37)

    @puXharm.setter
    def puXharm(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 37, value)

    @property
    def XRharm(self) -> float:
        """
        DSS property name: XRharm
        DSS property index: 38
        """
        return self._lib.Obj_GetFloat64(self._ptr, 38)

    @XRharm.setter
    def XRharm(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 38, value)

    @property
    def spectrum(self) -> str:
        """
        DSS property name: spectrum
        DSS property index: 39
        """
        return self._get_prop_string(39)

    @spectrum.setter
    def spectrum(self, value: Union[AnyStr, Spectrum]):
        if isinstance(value, DSSObj):
            self._set_obj(39, value)
            return

        self._set_string(39, value)

    @property
    def spectrum_obj(self) -> Spectrum:
        """
        DSS property name: spectrum
        DSS property index: 39
        """
        return self._get_obj(39, Spectrum)

    @spectrum_obj.setter
    def spectrum_obj(self, value: Spectrum):
        self._set_obj(39, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 40
        """
        return self._lib.Obj_GetFloat64(self._ptr, 40)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 40, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 41
        """
        return self._lib.Obj_GetInt32(self._ptr, 41) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 41, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 42
        """
        self._set_string(42, value)

class Transformer(DSSObj):
    _cls_name = 'Transformer'
    _cls_idx = 20
    _cls_prop_idx = {
        'phases': 1,
        'windings': 2,
        'wdg': 3,
        'bus': 4,
        'conn': 5,
        'kv': 6,
        'kva': 7,
        'tap': 8,
        'pctr': 9,
        '%r': 9,
        'rneut': 10,
        'xneut': 11,
        'buses': 12,
        'conns': 13,
        'kvs': 14,
        'kvas': 15,
        'taps': 16,
        'xhl': 17,
        'xht': 18,
        'xlt': 19,
        'xscarray': 20,
        'thermal': 21,
        'n': 22,
        'm': 23,
        'flrise': 24,
        'hsrise': 25,
        'pctloadloss': 26,
        '%loadloss': 26,
        'pctnoloadloss': 27,
        '%noloadloss': 27,
        'normhkva': 28,
        'emerghkva': 29,
        'sub': 30,
        'maxtap': 31,
        'mintap': 32,
        'numtaps': 33,
        'subname': 34,
        'pctimag': 35,
        '%imag': 35,
        'ppm_antifloat': 36,
        'pctrs': 37,
        '%rs': 37,
        'bank': 38,
        'xfmrcode': 39,
        'xrconst': 40,
        'x12': 41,
        'x13': 42,
        'x23': 43,
        'leadlag': 44,
        'wdgcurrents': 45,
        'core': 46,
        'rdcohms': 47,
        'seasons': 48,
        'ratings': 49,
        'normamps': 50,
        'emergamps': 51,
        'faultrate': 52,
        'pctperm': 53,
        'repair': 54,
        'basefreq': 55,
        'enabled': 56,
        'like': 57,
    }

    @property
    def phases(self) -> int:
        """
        DSS property name: phases
        DSS property index: 1
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @phases.setter
    def phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def windings(self) -> int:
        """
        DSS property name: windings
        DSS property index: 2
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @windings.setter
    def windings(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def wdg(self) -> int:
        """
        DSS property name: wdg
        DSS property index: 3
        """
        return self._lib.Obj_GetInt32(self._ptr, 3)

    @wdg.setter
    def wdg(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 3, value)

    @property
    def bus(self) -> List[str]:
        """
        DSS property name: bus
        DSS property index: 4
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 4)

    @bus.setter
    def bus(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 4, value_ptr, value_count)
        self._check_for_error()

    @property
    def conn(self) -> List[Connection]:
        """
        DSS property name: conn
        DSS property index: 5
        """
        return [Connection(val) for val in self._get_int32_list(self._lib.Obj_GetInt32Array, self._ptr, 5)]

    @conn.setter
    def conn(self, value: Union[List[Union[int,Connection]], List[AnyStr]]):
        if not isinstance(value, int):
            self._set_string_array(5, value)
            return    
        self._set_int32_array(5, value)

    @property
    def conn_str(self) -> List[str]:
        """
        DSS property name: conn
        DSS property index: 5
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 5)

    @conn_str.setter
    def conn_str(self, value: AnyStr):
        self.conn = value

    @property
    def kV(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: kV
        DSS property index: 6
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 6)

    @kV.setter
    def kV(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(6, value)

    @property
    def kVA(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: kVA
        DSS property index: 7
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 7)

    @kVA.setter
    def kVA(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(7, value)

    @property
    def tap(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: tap
        DSS property index: 8
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 8)

    @tap.setter
    def tap(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(8, value)

    @property
    def pctR(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: %R
        DSS property index: 9
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 9)

    @pctR.setter
    def pctR(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(9, value)

    @property
    def Rneut(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: Rneut
        DSS property index: 10
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 10)

    @Rneut.setter
    def Rneut(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(10, value)

    @property
    def Xneut(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: Xneut
        DSS property index: 11
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 11)

    @Xneut.setter
    def Xneut(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(11, value)

    @property
    def buses(self) -> List[str]:
        """
        DSS property name: buses
        DSS property index: 12
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 12)

    @buses.setter
    def buses(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 12, value_ptr, value_count)
        self._check_for_error()

    @property
    def conns(self) -> List[Connection]:
        """
        DSS property name: conns
        DSS property index: 13
        """
        return [Connection(val) for val in self._get_int32_list(self._lib.Obj_GetInt32Array, self._ptr, 13)]

    @conns.setter
    def conns(self, value: Union[List[Union[int,Connection]], List[AnyStr]]):
        if not isinstance(value, int):
            self._set_string_array(13, value)
            return    
        self._set_int32_array(13, value)

    @property
    def conns_str(self) -> List[str]:
        """
        DSS property name: conns
        DSS property index: 13
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 13)

    @conns_str.setter
    def conns_str(self, value: AnyStr):
        self.conns = value

    @property
    def kVs(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: kVs
        DSS property index: 14
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 14)

    @kVs.setter
    def kVs(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(14, value)

    @property
    def kVAs(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: kVAs
        DSS property index: 15
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 15)

    @kVAs.setter
    def kVAs(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(15, value)

    @property
    def taps(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: taps
        DSS property index: 16
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 16)

    @taps.setter
    def taps(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(16, value)

    @property
    def XHL(self) -> float:
        """
        DSS property name: XHL
        DSS property index: 17
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    @XHL.setter
    def XHL(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 17, value)

    @property
    def XHT(self) -> float:
        """
        DSS property name: XHT
        DSS property index: 18
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    @XHT.setter
    def XHT(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 18, value)

    @property
    def XLT(self) -> float:
        """
        DSS property name: XLT
        DSS property index: 19
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    @XLT.setter
    def XLT(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 19, value)

    @property
    def Xscarray(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: Xscarray
        DSS property index: 20
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 20)

    @Xscarray.setter
    def Xscarray(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(20, value)

    @property
    def thermal(self) -> float:
        """
        DSS property name: thermal
        DSS property index: 21
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @thermal.setter
    def thermal(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    @property
    def n(self) -> float:
        """
        DSS property name: n
        DSS property index: 22
        """
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    @n.setter
    def n(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 22, value)

    @property
    def m(self) -> float:
        """
        DSS property name: m
        DSS property index: 23
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    @m.setter
    def m(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 23, value)

    @property
    def flrise(self) -> float:
        """
        DSS property name: flrise
        DSS property index: 24
        """
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    @flrise.setter
    def flrise(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 24, value)

    @property
    def hsrise(self) -> float:
        """
        DSS property name: hsrise
        DSS property index: 25
        """
        return self._lib.Obj_GetFloat64(self._ptr, 25)

    @hsrise.setter
    def hsrise(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 25, value)

    @property
    def pctloadloss(self) -> float:
        """
        DSS property name: %loadloss
        DSS property index: 26
        """
        return self._lib.Obj_GetFloat64(self._ptr, 26)

    @pctloadloss.setter
    def pctloadloss(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 26, value)

    @property
    def pctnoloadloss(self) -> float:
        """
        DSS property name: %noloadloss
        DSS property index: 27
        """
        return self._lib.Obj_GetFloat64(self._ptr, 27)

    @pctnoloadloss.setter
    def pctnoloadloss(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 27, value)

    @property
    def normhkVA(self) -> float:
        """
        DSS property name: normhkVA
        DSS property index: 28
        """
        return self._lib.Obj_GetFloat64(self._ptr, 28)

    @normhkVA.setter
    def normhkVA(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 28, value)

    @property
    def emerghkVA(self) -> float:
        """
        DSS property name: emerghkVA
        DSS property index: 29
        """
        return self._lib.Obj_GetFloat64(self._ptr, 29)

    @emerghkVA.setter
    def emerghkVA(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 29, value)

    @property
    def sub(self) -> bool:
        """
        DSS property name: sub
        DSS property index: 30
        """
        return self._lib.Obj_GetInt32(self._ptr, 30) != 0

    @sub.setter
    def sub(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 30, value)

    @property
    def MaxTap(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: MaxTap
        DSS property index: 31
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 31)

    @MaxTap.setter
    def MaxTap(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(31, value)

    @property
    def MinTap(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: MinTap
        DSS property index: 32
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 32)

    @MinTap.setter
    def MinTap(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(32, value)

    @property
    def NumTaps(self) -> npt.NDArray[np.int32]:
        """
        DSS property name: NumTaps
        DSS property index: 33
        """
        return self._get_int32_array(self._lib.Obj_GetInt32Array, self._ptr, 33)

    @NumTaps.setter
    def NumTaps(self, value: npt.NDArray[np.int32]):
        self._set_int32_array(33, value)

    @property
    def subname(self) -> str:
        """
        DSS property name: subname
        DSS property index: 34
        """
        return self._get_prop_string(34)

    @subname.setter
    def subname(self, value: AnyStr):
        self._set_string(34, value)

    @property
    def pctimag(self) -> float:
        """
        DSS property name: %imag
        DSS property index: 35
        """
        return self._lib.Obj_GetFloat64(self._ptr, 35)

    @pctimag.setter
    def pctimag(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 35, value)

    @property
    def ppm_antifloat(self) -> float:
        """
        DSS property name: ppm_antifloat
        DSS property index: 36
        """
        return self._lib.Obj_GetFloat64(self._ptr, 36)

    @ppm_antifloat.setter
    def ppm_antifloat(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 36, value)

    @property
    def pctRs(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: %Rs
        DSS property index: 37
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 37)

    @pctRs.setter
    def pctRs(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(37, value)

    @property
    def bank(self) -> str:
        """
        DSS property name: bank
        DSS property index: 38
        """
        return self._get_prop_string(38)

    @bank.setter
    def bank(self, value: AnyStr):
        self._set_string(38, value)

    @property
    def xfmrcode(self) -> str:
        """
        DSS property name: XfmrCode
        DSS property index: 39
        """
        return self._get_prop_string(39)

    @xfmrcode.setter
    def xfmrcode(self, value: Union[AnyStr, XfmrCode]):
        if isinstance(value, DSSObj):
            self._set_obj(39, value)
            return

        self._set_string(39, value)

    @property
    def xfmrcode_obj(self) -> XfmrCode:
        """
        DSS property name: XfmrCode
        DSS property index: 39
        """
        return self._get_obj(39, XfmrCode)

    @xfmrcode_obj.setter
    def xfmrcode_obj(self, value: XfmrCode):
        self._set_obj(39, value)

    @property
    def XRConst(self) -> bool:
        """
        DSS property name: XRConst
        DSS property index: 40
        """
        return self._lib.Obj_GetInt32(self._ptr, 40) != 0

    @XRConst.setter
    def XRConst(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 40, value)

    @property
    def X12(self) -> float:
        """
        DSS property name: X12
        DSS property index: 41
        """
        return self._lib.Obj_GetFloat64(self._ptr, 41)

    @X12.setter
    def X12(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 41, value)

    @property
    def X13(self) -> float:
        """
        DSS property name: X13
        DSS property index: 42
        """
        return self._lib.Obj_GetFloat64(self._ptr, 42)

    @X13.setter
    def X13(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 42, value)

    @property
    def X23(self) -> float:
        """
        DSS property name: X23
        DSS property index: 43
        """
        return self._lib.Obj_GetFloat64(self._ptr, 43)

    @X23.setter
    def X23(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 43, value)

    @property
    def LeadLag(self) -> PhaseSequence:
        """
    DSS property name: LeadLag
    DSS property index: 44
    """
        return PhaseSequence(self._lib.Obj_GetInt32(self._ptr, 44))

    @LeadLag.setter
    def LeadLag(self, value: Union[AnyStr, int, PhaseSequence]):
        if not isinstance(value, int):
            self._set_string(44, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 44, value)

    @property
    def LeadLag_str(self) -> str:
        """
        DSS property name: LeadLag
        DSS property index: 44
        """
        return self._get_prop_string(44)

    @LeadLag_str.setter
    def LeadLag_str(self, value: AnyStr):
        self.LeadLag = value

    def WdgCurrents(self) -> str:
        """
        DSS property name: WdgCurrents
        DSS property index: 45
        """
        # []
        # StringSilentROFunction
        return self._get_prop_string(self._lib.Obj_GetString(self._ptr, 45))

    @property
    def Core(self) -> CoreType:
        """
    DSS property name: Core
    DSS property index: 46
    """
        return CoreType(self._lib.Obj_GetInt32(self._ptr, 46))

    @Core.setter
    def Core(self, value: Union[AnyStr, int, CoreType]):
        if not isinstance(value, int):
            self._set_string(46, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 46, value)

    @property
    def Core_str(self) -> str:
        """
        DSS property name: Core
        DSS property index: 46
        """
        return self._get_prop_string(46)

    @Core_str.setter
    def Core_str(self, value: AnyStr):
        self.Core = value

    @property
    def RdcOhms(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: RdcOhms
        DSS property index: 47
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 47)

    @RdcOhms.setter
    def RdcOhms(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(47, value)

    @property
    def Seasons(self) -> int:
        """
        DSS property name: Seasons
        DSS property index: 48
        """
        return self._lib.Obj_GetInt32(self._ptr, 48)

    @Seasons.setter
    def Seasons(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 48, value)

    @property
    def Ratings(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: Ratings
        DSS property index: 49
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 49)

    @Ratings.setter
    def Ratings(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(49, value)

    @property
    def normamps(self) -> float:
        """
        DSS property name: normamps
        DSS property index: 50
        """
        return self._lib.Obj_GetFloat64(self._ptr, 50)

    @normamps.setter
    def normamps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 50, value)

    @property
    def emergamps(self) -> float:
        """
        DSS property name: emergamps
        DSS property index: 51
        """
        return self._lib.Obj_GetFloat64(self._ptr, 51)

    @emergamps.setter
    def emergamps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 51, value)

    @property
    def faultrate(self) -> float:
        """
        DSS property name: faultrate
        DSS property index: 52
        """
        return self._lib.Obj_GetFloat64(self._ptr, 52)

    @faultrate.setter
    def faultrate(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 52, value)

    @property
    def pctperm(self) -> float:
        """
        DSS property name: pctperm
        DSS property index: 53
        """
        return self._lib.Obj_GetFloat64(self._ptr, 53)

    @pctperm.setter
    def pctperm(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 53, value)

    @property
    def repair(self) -> float:
        """
        DSS property name: repair
        DSS property index: 54
        """
        return self._lib.Obj_GetFloat64(self._ptr, 54)

    @repair.setter
    def repair(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 54, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 55
        """
        return self._lib.Obj_GetFloat64(self._ptr, 55)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 55, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 56
        """
        return self._lib.Obj_GetInt32(self._ptr, 56) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 56, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 57
        """
        self._set_string(57, value)

class Capacitor(DSSObj):
    _cls_name = 'Capacitor'
    _cls_idx = 22
    _cls_prop_idx = {
        'bus1': 1,
        'bus2': 2,
        'phases': 3,
        'kvar': 4,
        'kv': 5,
        'conn': 6,
        'cmatrix': 7,
        'cuf': 8,
        'r': 9,
        'xl': 10,
        'harm': 11,
        'numsteps': 12,
        'states': 13,
        'normamps': 14,
        'emergamps': 15,
        'faultrate': 16,
        'pctperm': 17,
        'repair': 18,
        'basefreq': 19,
        'enabled': 20,
        'like': 21,
    }

    @property
    def bus1(self) -> str:
        """
        DSS property name: bus1
        DSS property index: 1
        """
        return self._get_prop_string(1)

    @bus1.setter
    def bus1(self, value: AnyStr):
        self._set_string(1, value)

    @property
    def bus2(self) -> str:
        """
        DSS property name: bus2
        DSS property index: 2
        """
        return self._get_prop_string(2)

    @bus2.setter
    def bus2(self, value: AnyStr):
        self._set_string(2, value)

    @property
    def phases(self) -> int:
        """
        DSS property name: phases
        DSS property index: 3
        """
        return self._lib.Obj_GetInt32(self._ptr, 3)

    @phases.setter
    def phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 3, value)

    @property
    def kvar(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: kvar
        DSS property index: 4
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 4)

    @kvar.setter
    def kvar(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(4, value)

    @property
    def kv(self) -> float:
        """
        DSS property name: kv
        DSS property index: 5
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @kv.setter
    def kv(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def conn(self) -> Connection:
        """
    DSS property name: conn
    DSS property index: 6
    """
        return Connection(self._lib.Obj_GetInt32(self._ptr, 6))

    @conn.setter
    def conn(self, value: Union[AnyStr, int, Connection]):
        if not isinstance(value, int):
            self._set_string(6, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 6, value)

    @property
    def conn_str(self) -> str:
        """
        DSS property name: conn
        DSS property index: 6
        """
        return self._get_prop_string(6)

    @conn_str.setter
    def conn_str(self, value: AnyStr):
        self.conn = value

    @property
    def cmatrix(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: cmatrix
        DSS property index: 7
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 7)

    @cmatrix.setter
    def cmatrix(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(7, value)

    @property
    def cuf(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: cuf
        DSS property index: 8
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 8)

    @cuf.setter
    def cuf(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(8, value)

    @property
    def R(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: R
        DSS property index: 9
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 9)

    @R.setter
    def R(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(9, value)

    @property
    def XL(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: XL
        DSS property index: 10
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 10)

    @XL.setter
    def XL(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(10, value)

    @property
    def Harm(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: Harm
        DSS property index: 11
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 11)

    @Harm.setter
    def Harm(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(11, value)

    @property
    def Numsteps(self) -> int:
        """
        DSS property name: Numsteps
        DSS property index: 12
        """
        return self._lib.Obj_GetInt32(self._ptr, 12)

    @Numsteps.setter
    def Numsteps(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 12, value)

    @property
    def states(self) -> npt.NDArray[np.int32]:
        """
        DSS property name: states
        DSS property index: 13
        """
        return self._get_int32_array(self._lib.Obj_GetInt32Array, self._ptr, 13)

    @states.setter
    def states(self, value: npt.NDArray[np.int32]):
        self._set_int32_array(13, value)

    @property
    def normamps(self) -> float:
        """
        DSS property name: normamps
        DSS property index: 14
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @normamps.setter
    def normamps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def emergamps(self) -> float:
        """
        DSS property name: emergamps
        DSS property index: 15
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @emergamps.setter
    def emergamps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def faultrate(self) -> float:
        """
        DSS property name: faultrate
        DSS property index: 16
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    @faultrate.setter
    def faultrate(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 16, value)

    @property
    def pctperm(self) -> float:
        """
        DSS property name: pctperm
        DSS property index: 17
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    @pctperm.setter
    def pctperm(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 17, value)

    @property
    def repair(self) -> float:
        """
        DSS property name: repair
        DSS property index: 18
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    @repair.setter
    def repair(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 18, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 19
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 19, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 20
        """
        return self._lib.Obj_GetInt32(self._ptr, 20) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 20, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 21
        """
        self._set_string(21, value)

class Reactor(DSSObj):
    _cls_name = 'Reactor'
    _cls_idx = 23
    _cls_prop_idx = {
        'bus1': 1,
        'bus2': 2,
        'phases': 3,
        'kvar': 4,
        'kv': 5,
        'conn': 6,
        'rmatrix': 7,
        'xmatrix': 8,
        'parallel': 9,
        'r': 10,
        'x': 11,
        'rp': 12,
        'z1': 13,
        'z2': 14,
        'z0': 15,
        'z': 16,
        'rcurve': 17,
        'lcurve': 18,
        'lmh': 19,
        'normamps': 20,
        'emergamps': 21,
        'faultrate': 22,
        'pctperm': 23,
        'repair': 24,
        'basefreq': 25,
        'enabled': 26,
        'like': 27,
    }

    @property
    def bus1(self) -> str:
        """
        DSS property name: bus1
        DSS property index: 1
        """
        return self._get_prop_string(1)

    @bus1.setter
    def bus1(self, value: AnyStr):
        self._set_string(1, value)

    @property
    def bus2(self) -> str:
        """
        DSS property name: bus2
        DSS property index: 2
        """
        return self._get_prop_string(2)

    @bus2.setter
    def bus2(self, value: AnyStr):
        self._set_string(2, value)

    @property
    def phases(self) -> int:
        """
        DSS property name: phases
        DSS property index: 3
        """
        return self._lib.Obj_GetInt32(self._ptr, 3)

    @phases.setter
    def phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 3, value)

    @property
    def kvar(self) -> float:
        """
        DSS property name: kvar
        DSS property index: 4
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @kvar.setter
    def kvar(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def kv(self) -> float:
        """
        DSS property name: kv
        DSS property index: 5
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @kv.setter
    def kv(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def conn(self) -> Connection:
        """
    DSS property name: conn
    DSS property index: 6
    """
        return Connection(self._lib.Obj_GetInt32(self._ptr, 6))

    @conn.setter
    def conn(self, value: Union[AnyStr, int, Connection]):
        if not isinstance(value, int):
            self._set_string(6, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 6, value)

    @property
    def conn_str(self) -> str:
        """
        DSS property name: conn
        DSS property index: 6
        """
        return self._get_prop_string(6)

    @conn_str.setter
    def conn_str(self, value: AnyStr):
        self.conn = value

    @property
    def Rmatrix(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: Rmatrix
        DSS property index: 7
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 7)

    @Rmatrix.setter
    def Rmatrix(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(7, value)

    @property
    def Xmatrix(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: Xmatrix
        DSS property index: 8
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 8)

    @Xmatrix.setter
    def Xmatrix(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(8, value)

    @property
    def Parallel(self) -> bool:
        """
        DSS property name: Parallel
        DSS property index: 9
        """
        return self._lib.Obj_GetInt32(self._ptr, 9) != 0

    @Parallel.setter
    def Parallel(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 9, value)

    @property
    def R(self) -> float:
        """
        DSS property name: R
        DSS property index: 10
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @R.setter
    def R(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def X(self) -> float:
        """
        DSS property name: X
        DSS property index: 11
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @X.setter
    def X(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def Rp(self) -> float:
        """
        DSS property name: Rp
        DSS property index: 12
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @Rp.setter
    def Rp(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def Z1(self) -> complex:
        """
        DSS property name: Z1
        DSS property index: 13
        """
        return self._get_complex(13)

    @Z1.setter
    def Z1(self, value: complex):
        self._set_complex(13, value)

    @property
    def Z2(self) -> complex:
        """
        DSS property name: Z2
        DSS property index: 14
        """
        return self._get_complex(14)

    @Z2.setter
    def Z2(self, value: complex):
        self._set_complex(14, value)

    @property
    def Z0(self) -> complex:
        """
        DSS property name: Z0
        DSS property index: 15
        """
        return self._get_complex(15)

    @Z0.setter
    def Z0(self, value: complex):
        self._set_complex(15, value)

    @property
    def Z(self) -> complex:
        """
        DSS property name: Z
        DSS property index: 16
        """
        return self._get_complex(16)

    @Z.setter
    def Z(self, value: complex):
        self._set_complex(16, value)

    @property
    def RCurve(self) -> str:
        """
        DSS property name: RCurve
        DSS property index: 17
        """
        return self._get_prop_string(17)

    @RCurve.setter
    def RCurve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(17, value)
            return

        self._set_string(17, value)

    @property
    def RCurve_obj(self) -> XYcurve:
        """
        DSS property name: RCurve
        DSS property index: 17
        """
        return self._get_obj(17, XYcurve)

    @RCurve_obj.setter
    def RCurve_obj(self, value: XYcurve):
        self._set_obj(17, value)

    @property
    def LCurve(self) -> str:
        """
        DSS property name: LCurve
        DSS property index: 18
        """
        return self._get_prop_string(18)

    @LCurve.setter
    def LCurve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(18, value)
            return

        self._set_string(18, value)

    @property
    def LCurve_obj(self) -> XYcurve:
        """
        DSS property name: LCurve
        DSS property index: 18
        """
        return self._get_obj(18, XYcurve)

    @LCurve_obj.setter
    def LCurve_obj(self, value: XYcurve):
        self._set_obj(18, value)

    @property
    def LmH(self) -> float:
        """
        DSS property name: LmH
        DSS property index: 19
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    @LmH.setter
    def LmH(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 19, value)

    @property
    def normamps(self) -> float:
        """
        DSS property name: normamps
        DSS property index: 20
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    @normamps.setter
    def normamps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 20, value)

    @property
    def emergamps(self) -> float:
        """
        DSS property name: emergamps
        DSS property index: 21
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @emergamps.setter
    def emergamps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    @property
    def faultrate(self) -> float:
        """
        DSS property name: faultrate
        DSS property index: 22
        """
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    @faultrate.setter
    def faultrate(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 22, value)

    @property
    def pctperm(self) -> float:
        """
        DSS property name: pctperm
        DSS property index: 23
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    @pctperm.setter
    def pctperm(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 23, value)

    @property
    def repair(self) -> float:
        """
        DSS property name: repair
        DSS property index: 24
        """
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    @repair.setter
    def repair(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 24, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 25
        """
        return self._lib.Obj_GetFloat64(self._ptr, 25)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 25, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 26
        """
        return self._lib.Obj_GetInt32(self._ptr, 26) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 26, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 27
        """
        self._set_string(27, value)

class CapControl(DSSObj):
    _cls_name = 'CapControl'
    _cls_idx = 24
    _cls_prop_idx = {
        'element': 1,
        'terminal': 2,
        'capacitor': 3,
        'type': 4,
        'ptratio': 5,
        'ctratio': 6,
        'onsetting': 7,
        'offsetting': 8,
        'delay': 9,
        'voltoverride': 10,
        'vmax': 11,
        'vmin': 12,
        'delayoff': 13,
        'deadtime': 14,
        'ctphase': 15,
        'ptphase': 16,
        'vbus': 17,
        'eventlog': 18,
        'usermodel': 19,
        'userdata': 20,
        'pctminkvar': 21,
        'reset': 22,
        'basefreq': 23,
        'enabled': 24,
        'like': 25,
    }

    # Class-specific enumerations
    class CapControlType(IntEnum):
        """CapControl: Type (DSS enumeration for CapControl)"""
        Current = 0 # Current
        Voltage = 1 # Voltage
        kvar = 2 # kvar
        Time = 3 # Time
        PowerFactor = 4 # PowerFactor


    @property
    def element(self) -> str:
        """
        DSS property name: element
        DSS property index: 1
        """
        return self._get_prop_string(1)

    @element.setter
    def element(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_obj(1, value)
            return

        self._set_string(1, value)

    @property
    def element_obj(self) -> DSSObj:
        """
        DSS property name: element
        DSS property index: 1
        """
        return self._get_obj(1, None)

    @element_obj.setter
    def element_obj(self, value: DSSObj):
        self._set_obj(1, value)

    @property
    def terminal(self) -> int:
        """
        DSS property name: terminal
        DSS property index: 2
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @terminal.setter
    def terminal(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def capacitor(self) -> str:
        """
        DSS property name: capacitor
        DSS property index: 3
        """
        return self._get_prop_string(3)

    @capacitor.setter
    def capacitor(self, value: Union[AnyStr, Capacitor]):
        if isinstance(value, DSSObj):
            self._set_obj(3, value)
            return

        self._set_string(3, value)

    @property
    def capacitor_obj(self) -> Capacitor:
        """
        DSS property name: capacitor
        DSS property index: 3
        """
        return self._get_obj(3, Capacitor)

    @capacitor_obj.setter
    def capacitor_obj(self, value: Capacitor):
        self._set_obj(3, value)

    @property
    def type(self) -> CapControlType:
        """
    DSS property name: type
    DSS property index: 4
    """
        return CapControlType(self._lib.Obj_GetInt32(self._ptr, 4))

    @type.setter
    def type(self, value: Union[AnyStr, int, CapControlType]):
        if not isinstance(value, int):
            self._set_string(4, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 4, value)

    @property
    def type_str(self) -> str:
        """
        DSS property name: type
        DSS property index: 4
        """
        return self._get_prop_string(4)

    @type_str.setter
    def type_str(self, value: AnyStr):
        self.type = value

    @property
    def PTratio(self) -> float:
        """
        DSS property name: PTratio
        DSS property index: 5
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @PTratio.setter
    def PTratio(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def CTratio(self) -> float:
        """
        DSS property name: CTratio
        DSS property index: 6
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    @CTratio.setter
    def CTratio(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 6, value)

    @property
    def ONsetting(self) -> float:
        """
        DSS property name: ONsetting
        DSS property index: 7
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @ONsetting.setter
    def ONsetting(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def OFFsetting(self) -> float:
        """
        DSS property name: OFFsetting
        DSS property index: 8
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @OFFsetting.setter
    def OFFsetting(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def Delay(self) -> float:
        """
        DSS property name: Delay
        DSS property index: 9
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @Delay.setter
    def Delay(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def VoltOverride(self) -> bool:
        """
        DSS property name: VoltOverride
        DSS property index: 10
        """
        return self._lib.Obj_GetInt32(self._ptr, 10) != 0

    @VoltOverride.setter
    def VoltOverride(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 10, value)

    @property
    def Vmax(self) -> float:
        """
        DSS property name: Vmax
        DSS property index: 11
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @Vmax.setter
    def Vmax(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def Vmin(self) -> float:
        """
        DSS property name: Vmin
        DSS property index: 12
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @Vmin.setter
    def Vmin(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def DelayOFF(self) -> float:
        """
        DSS property name: DelayOFF
        DSS property index: 13
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @DelayOFF.setter
    def DelayOFF(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def DeadTime(self) -> float:
        """
        DSS property name: DeadTime
        DSS property index: 14
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @DeadTime.setter
    def DeadTime(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def CTPhase(self) -> Union[MonitoredPhase, int]:
        """
    DSS property name: CTPhase
    DSS property index: 15
    """
        value = self._lib.Obj_GetInt32(self._ptr, 15)
        if value > 0:
            return value

        return MonitoredPhase(value)

    @CTPhase.setter
    def CTPhase(self, value: Union[AnyStr, int, MonitoredPhase]):
        if not isinstance(value, int):
            self._set_string(15, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 15, value)

    @property
    def CTPhase_str(self) -> str:
        """
        DSS property name: CTPhase
        DSS property index: 15
        """
        return self._get_prop_string(15)

    @CTPhase_str.setter
    def CTPhase_str(self, value: AnyStr):
        self.CTPhase = value

    @property
    def PTPhase(self) -> Union[MonitoredPhase, int]:
        """
    DSS property name: PTPhase
    DSS property index: 16
    """
        value = self._lib.Obj_GetInt32(self._ptr, 16)
        if value > 0:
            return value

        return MonitoredPhase(value)

    @PTPhase.setter
    def PTPhase(self, value: Union[AnyStr, int, MonitoredPhase]):
        if not isinstance(value, int):
            self._set_string(16, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 16, value)

    @property
    def PTPhase_str(self) -> str:
        """
        DSS property name: PTPhase
        DSS property index: 16
        """
        return self._get_prop_string(16)

    @PTPhase_str.setter
    def PTPhase_str(self, value: AnyStr):
        self.PTPhase = value

    @property
    def VBus(self) -> str:
        """
        DSS property name: VBus
        DSS property index: 17
        """
        return self._get_prop_string(17)

    @VBus.setter
    def VBus(self, value: AnyStr):
        self._set_string(17, value)

    @property
    def EventLog(self) -> bool:
        """
        DSS property name: EventLog
        DSS property index: 18
        """
        return self._lib.Obj_GetInt32(self._ptr, 18) != 0

    @EventLog.setter
    def EventLog(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 18, value)

    @property
    def UserModel(self) -> str:
        """
        DSS property name: UserModel
        DSS property index: 19
        """
        return self._get_prop_string(19)

    @UserModel.setter
    def UserModel(self, value: AnyStr):
        self._set_string(19, value)

    @property
    def UserData(self) -> str:
        """
        DSS property name: UserData
        DSS property index: 20
        """
        return self._get_prop_string(20)

    @UserData.setter
    def UserData(self, value: AnyStr):
        self._set_string(20, value)

    @property
    def pctMinkvar(self) -> float:
        """
        DSS property name: pctMinkvar
        DSS property index: 21
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @pctMinkvar.setter
    def pctMinkvar(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    def Reset(self, value: bool):
        """
        DSS property name: Reset
        DSS property index: 22
        """
        self._lib.Obj_SetInt32(self._ptr, 22, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 23
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 23, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 24
        """
        return self._lib.Obj_GetInt32(self._ptr, 24) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 24, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 25
        """
        self._set_string(25, value)

class Fault(DSSObj):
    _cls_name = 'Fault'
    _cls_idx = 25
    _cls_prop_idx = {
        'bus1': 1,
        'bus2': 2,
        'phases': 3,
        'r': 4,
        'pctstddev': 5,
        '%stddev': 5,
        'gmatrix': 6,
        'ontime': 7,
        'temporary': 8,
        'minamps': 9,
        'normamps': 10,
        'emergamps': 11,
        'faultrate': 12,
        'pctperm': 13,
        'repair': 14,
        'basefreq': 15,
        'enabled': 16,
        'like': 17,
    }

    @property
    def bus1(self) -> str:
        """
        DSS property name: bus1
        DSS property index: 1
        """
        return self._get_prop_string(1)

    @bus1.setter
    def bus1(self, value: AnyStr):
        self._set_string(1, value)

    @property
    def bus2(self) -> str:
        """
        DSS property name: bus2
        DSS property index: 2
        """
        return self._get_prop_string(2)

    @bus2.setter
    def bus2(self, value: AnyStr):
        self._set_string(2, value)

    @property
    def phases(self) -> int:
        """
        DSS property name: phases
        DSS property index: 3
        """
        return self._lib.Obj_GetInt32(self._ptr, 3)

    @phases.setter
    def phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 3, value)

    @property
    def r(self) -> float:
        """
        DSS property name: r
        DSS property index: 4
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @r.setter
    def r(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def pctstddev(self) -> float:
        """
        DSS property name: %stddev
        DSS property index: 5
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @pctstddev.setter
    def pctstddev(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def Gmatrix(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: Gmatrix
        DSS property index: 6
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 6)

    @Gmatrix.setter
    def Gmatrix(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(6, value)

    @property
    def ONtime(self) -> float:
        """
        DSS property name: ONtime
        DSS property index: 7
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @ONtime.setter
    def ONtime(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def temporary(self) -> bool:
        """
        DSS property name: temporary
        DSS property index: 8
        """
        return self._lib.Obj_GetInt32(self._ptr, 8) != 0

    @temporary.setter
    def temporary(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 8, value)

    @property
    def MinAmps(self) -> float:
        """
        DSS property name: MinAmps
        DSS property index: 9
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @MinAmps.setter
    def MinAmps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def normamps(self) -> float:
        """
        DSS property name: normamps
        DSS property index: 10
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @normamps.setter
    def normamps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def emergamps(self) -> float:
        """
        DSS property name: emergamps
        DSS property index: 11
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @emergamps.setter
    def emergamps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def faultrate(self) -> float:
        """
        DSS property name: faultrate
        DSS property index: 12
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @faultrate.setter
    def faultrate(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def pctperm(self) -> float:
        """
        DSS property name: pctperm
        DSS property index: 13
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @pctperm.setter
    def pctperm(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def repair(self) -> float:
        """
        DSS property name: repair
        DSS property index: 14
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @repair.setter
    def repair(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 15
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 16
        """
        return self._lib.Obj_GetInt32(self._ptr, 16) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 16, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 17
        """
        self._set_string(17, value)

class Generator(DSSObj):
    _cls_name = 'Generator'
    _cls_idx = 26
    _cls_prop_idx = {
        'phases': 1,
        'bus1': 2,
        'kv': 3,
        'kw': 4,
        'pf': 5,
        'kvar': 6,
        'model': 7,
        'vminpu': 8,
        'vmaxpu': 9,
        'yearly': 10,
        'daily': 11,
        'duty': 12,
        'dispmode': 13,
        'dispvalue': 14,
        'conn': 15,
        'status': 16,
        'cls': 17,
        'class': 17,
        'vpu': 18,
        'maxkvar': 19,
        'minkvar': 20,
        'pvfactor': 21,
        'forceon': 22,
        'kva': 23,
        'mva': 24,
        'xd': 25,
        'xdp': 26,
        'xdpp': 27,
        'h': 28,
        'd': 29,
        'usermodel': 30,
        'userdata': 31,
        'shaftmodel': 32,
        'shaftdata': 33,
        'dutystart': 34,
        'debugtrace': 35,
        'balanced': 36,
        'xrdp': 37,
        'usefuel': 38,
        'fuelkwh': 39,
        'pctfuel': 40,
        '%fuel': 40,
        'pctreserve': 41,
        '%reserve': 41,
        'refuel': 42,
        'spectrum': 43,
        'basefreq': 44,
        'enabled': 45,
        'like': 46,
    }

    # Class-specific enumerations
    class GeneratorDispatchMode(IntEnum):
        """Generator: Dispatch Mode (DSS enumeration for Generator)"""
        Default = 0 # Default
        LoadLevel = 1 # LoadLevel
        Price = 2 # Price

    class GeneratorStatus(IntEnum):
        """Generator: Status (DSS enumeration for Generator)"""
        Variable = 0 # Variable
        Fixed = 1 # Fixed


    @property
    def phases(self) -> int:
        """
        DSS property name: phases
        DSS property index: 1
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @phases.setter
    def phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def bus1(self) -> str:
        """
        DSS property name: bus1
        DSS property index: 2
        """
        return self._get_prop_string(2)

    @bus1.setter
    def bus1(self, value: AnyStr):
        self._set_string(2, value)

    @property
    def kv(self) -> float:
        """
        DSS property name: kv
        DSS property index: 3
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @kv.setter
    def kv(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def kW(self) -> float:
        """
        DSS property name: kW
        DSS property index: 4
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @kW.setter
    def kW(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def pf(self) -> float:
        """
        DSS property name: pf
        DSS property index: 5
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @pf.setter
    def pf(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def kvar(self) -> float:
        """
        DSS property name: kvar
        DSS property index: 6
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    @kvar.setter
    def kvar(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 6, value)

    @property
    def model(self) -> int:
        """
        DSS property name: model
        DSS property index: 7
        """
        return self._lib.Obj_GetInt32(self._ptr, 7)

    @model.setter
    def model(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 7, value)

    @property
    def Vminpu(self) -> float:
        """
        DSS property name: Vminpu
        DSS property index: 8
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @Vminpu.setter
    def Vminpu(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def Vmaxpu(self) -> float:
        """
        DSS property name: Vmaxpu
        DSS property index: 9
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @Vmaxpu.setter
    def Vmaxpu(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def yearly(self) -> str:
        """
        DSS property name: yearly
        DSS property index: 10
        """
        return self._get_prop_string(10)

    @yearly.setter
    def yearly(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(10, value)
            return

        self._set_string(10, value)

    @property
    def yearly_obj(self) -> LoadShape:
        """
        DSS property name: yearly
        DSS property index: 10
        """
        return self._get_obj(10, LoadShape)

    @yearly_obj.setter
    def yearly_obj(self, value: LoadShape):
        self._set_obj(10, value)

    @property
    def daily(self) -> str:
        """
        DSS property name: daily
        DSS property index: 11
        """
        return self._get_prop_string(11)

    @daily.setter
    def daily(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(11, value)
            return

        self._set_string(11, value)

    @property
    def daily_obj(self) -> LoadShape:
        """
        DSS property name: daily
        DSS property index: 11
        """
        return self._get_obj(11, LoadShape)

    @daily_obj.setter
    def daily_obj(self, value: LoadShape):
        self._set_obj(11, value)

    @property
    def duty(self) -> str:
        """
        DSS property name: duty
        DSS property index: 12
        """
        return self._get_prop_string(12)

    @duty.setter
    def duty(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(12, value)
            return

        self._set_string(12, value)

    @property
    def duty_obj(self) -> LoadShape:
        """
        DSS property name: duty
        DSS property index: 12
        """
        return self._get_obj(12, LoadShape)

    @duty_obj.setter
    def duty_obj(self, value: LoadShape):
        self._set_obj(12, value)

    @property
    def dispmode(self) -> GeneratorDispatchMode:
        """
    DSS property name: dispmode
    DSS property index: 13
    """
        return GeneratorDispatchMode(self._lib.Obj_GetInt32(self._ptr, 13))

    @dispmode.setter
    def dispmode(self, value: Union[AnyStr, int, GeneratorDispatchMode]):
        if not isinstance(value, int):
            self._set_string(13, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 13, value)

    @property
    def dispmode_str(self) -> str:
        """
        DSS property name: dispmode
        DSS property index: 13
        """
        return self._get_prop_string(13)

    @dispmode_str.setter
    def dispmode_str(self, value: AnyStr):
        self.dispmode = value

    @property
    def dispvalue(self) -> float:
        """
        DSS property name: dispvalue
        DSS property index: 14
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @dispvalue.setter
    def dispvalue(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def conn(self) -> Connection:
        """
    DSS property name: conn
    DSS property index: 15
    """
        return Connection(self._lib.Obj_GetInt32(self._ptr, 15))

    @conn.setter
    def conn(self, value: Union[AnyStr, int, Connection]):
        if not isinstance(value, int):
            self._set_string(15, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 15, value)

    @property
    def conn_str(self) -> str:
        """
        DSS property name: conn
        DSS property index: 15
        """
        return self._get_prop_string(15)

    @conn_str.setter
    def conn_str(self, value: AnyStr):
        self.conn = value

    @property
    def status(self) -> GeneratorStatus:
        """
    DSS property name: status
    DSS property index: 16
    """
        return GeneratorStatus(self._lib.Obj_GetInt32(self._ptr, 16))

    @status.setter
    def status(self, value: Union[AnyStr, int, GeneratorStatus]):
        if not isinstance(value, int):
            self._set_string(16, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 16, value)

    @property
    def status_str(self) -> str:
        """
        DSS property name: status
        DSS property index: 16
        """
        return self._get_prop_string(16)

    @status_str.setter
    def status_str(self, value: AnyStr):
        self.status = value

    @property
    def cls(self) -> int:
        """
        DSS property name: class
        DSS property index: 17
        """
        return self._lib.Obj_GetInt32(self._ptr, 17)

    @cls.setter
    def cls(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 17, value)

    @property
    def Vpu(self) -> float:
        """
        DSS property name: Vpu
        DSS property index: 18
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    @Vpu.setter
    def Vpu(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 18, value)

    @property
    def maxkvar(self) -> float:
        """
        DSS property name: maxkvar
        DSS property index: 19
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    @maxkvar.setter
    def maxkvar(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 19, value)

    @property
    def minkvar(self) -> float:
        """
        DSS property name: minkvar
        DSS property index: 20
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    @minkvar.setter
    def minkvar(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 20, value)

    @property
    def pvfactor(self) -> float:
        """
        DSS property name: pvfactor
        DSS property index: 21
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @pvfactor.setter
    def pvfactor(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    @property
    def forceon(self) -> bool:
        """
        DSS property name: forceon
        DSS property index: 22
        """
        return self._lib.Obj_GetInt32(self._ptr, 22) != 0

    @forceon.setter
    def forceon(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 22, value)

    @property
    def kVA(self) -> float:
        """
        DSS property name: kVA
        DSS property index: 23
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    @kVA.setter
    def kVA(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 23, value)

    @property
    def MVA(self) -> float:
        """
        DSS property name: MVA
        DSS property index: 24
        """
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    @MVA.setter
    def MVA(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 24, value)

    @property
    def Xd(self) -> float:
        """
        DSS property name: Xd
        DSS property index: 25
        """
        return self._lib.Obj_GetFloat64(self._ptr, 25)

    @Xd.setter
    def Xd(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 25, value)

    @property
    def Xdp(self) -> float:
        """
        DSS property name: Xdp
        DSS property index: 26
        """
        return self._lib.Obj_GetFloat64(self._ptr, 26)

    @Xdp.setter
    def Xdp(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 26, value)

    @property
    def Xdpp(self) -> float:
        """
        DSS property name: Xdpp
        DSS property index: 27
        """
        return self._lib.Obj_GetFloat64(self._ptr, 27)

    @Xdpp.setter
    def Xdpp(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 27, value)

    @property
    def H(self) -> float:
        """
        DSS property name: H
        DSS property index: 28
        """
        return self._lib.Obj_GetFloat64(self._ptr, 28)

    @H.setter
    def H(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 28, value)

    @property
    def D(self) -> float:
        """
        DSS property name: D
        DSS property index: 29
        """
        return self._lib.Obj_GetFloat64(self._ptr, 29)

    @D.setter
    def D(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 29, value)

    @property
    def UserModel(self) -> str:
        """
        DSS property name: UserModel
        DSS property index: 30
        """
        return self._get_prop_string(30)

    @UserModel.setter
    def UserModel(self, value: AnyStr):
        self._set_string(30, value)

    @property
    def UserData(self) -> str:
        """
        DSS property name: UserData
        DSS property index: 31
        """
        return self._get_prop_string(31)

    @UserData.setter
    def UserData(self, value: AnyStr):
        self._set_string(31, value)

    @property
    def ShaftModel(self) -> str:
        """
        DSS property name: ShaftModel
        DSS property index: 32
        """
        return self._get_prop_string(32)

    @ShaftModel.setter
    def ShaftModel(self, value: AnyStr):
        self._set_string(32, value)

    @property
    def ShaftData(self) -> str:
        """
        DSS property name: ShaftData
        DSS property index: 33
        """
        return self._get_prop_string(33)

    @ShaftData.setter
    def ShaftData(self, value: AnyStr):
        self._set_string(33, value)

    @property
    def DutyStart(self) -> float:
        """
        DSS property name: DutyStart
        DSS property index: 34
        """
        return self._lib.Obj_GetFloat64(self._ptr, 34)

    @DutyStart.setter
    def DutyStart(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 34, value)

    @property
    def debugtrace(self) -> bool:
        """
        DSS property name: debugtrace
        DSS property index: 35
        """
        return self._lib.Obj_GetInt32(self._ptr, 35) != 0

    @debugtrace.setter
    def debugtrace(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 35, value)

    @property
    def Balanced(self) -> bool:
        """
        DSS property name: Balanced
        DSS property index: 36
        """
        return self._lib.Obj_GetInt32(self._ptr, 36) != 0

    @Balanced.setter
    def Balanced(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 36, value)

    @property
    def XRdp(self) -> float:
        """
        DSS property name: XRdp
        DSS property index: 37
        """
        return self._lib.Obj_GetFloat64(self._ptr, 37)

    @XRdp.setter
    def XRdp(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 37, value)

    @property
    def UseFuel(self) -> bool:
        """
        DSS property name: UseFuel
        DSS property index: 38
        """
        return self._lib.Obj_GetInt32(self._ptr, 38) != 0

    @UseFuel.setter
    def UseFuel(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 38, value)

    @property
    def FuelkWh(self) -> float:
        """
        DSS property name: FuelkWh
        DSS property index: 39
        """
        return self._lib.Obj_GetFloat64(self._ptr, 39)

    @FuelkWh.setter
    def FuelkWh(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 39, value)

    @property
    def pctFuel(self) -> float:
        """
        DSS property name: %Fuel
        DSS property index: 40
        """
        return self._lib.Obj_GetFloat64(self._ptr, 40)

    @pctFuel.setter
    def pctFuel(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 40, value)

    @property
    def pctReserve(self) -> float:
        """
        DSS property name: %Reserve
        DSS property index: 41
        """
        return self._lib.Obj_GetFloat64(self._ptr, 41)

    @pctReserve.setter
    def pctReserve(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 41, value)

    def Refuel(self, value: bool):
        """
        DSS property name: Refuel
        DSS property index: 42
        """
        self._lib.Obj_SetInt32(self._ptr, 42, value)

    @property
    def spectrum(self) -> str:
        """
        DSS property name: spectrum
        DSS property index: 43
        """
        return self._get_prop_string(43)

    @spectrum.setter
    def spectrum(self, value: Union[AnyStr, Spectrum]):
        if isinstance(value, DSSObj):
            self._set_obj(43, value)
            return

        self._set_string(43, value)

    @property
    def spectrum_obj(self) -> Spectrum:
        """
        DSS property name: spectrum
        DSS property index: 43
        """
        return self._get_obj(43, Spectrum)

    @spectrum_obj.setter
    def spectrum_obj(self, value: Spectrum):
        self._set_obj(43, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 44
        """
        return self._lib.Obj_GetFloat64(self._ptr, 44)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 44, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 45
        """
        return self._lib.Obj_GetInt32(self._ptr, 45) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 45, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 46
        """
        self._set_string(46, value)

class GenDispatcher(DSSObj):
    _cls_name = 'GenDispatcher'
    _cls_idx = 27
    _cls_prop_idx = {
        'element': 1,
        'terminal': 2,
        'kwlimit': 3,
        'kwband': 4,
        'kvarlimit': 5,
        'genlist': 6,
        'weights': 7,
        'basefreq': 8,
        'enabled': 9,
        'like': 10,
    }

    @property
    def Element(self) -> str:
        """
        DSS property name: Element
        DSS property index: 1
        """
        return self._get_prop_string(1)

    @Element.setter
    def Element(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_obj(1, value)
            return

        self._set_string(1, value)

    @property
    def Element_obj(self) -> DSSObj:
        """
        DSS property name: Element
        DSS property index: 1
        """
        return self._get_obj(1, None)

    @Element_obj.setter
    def Element_obj(self, value: DSSObj):
        self._set_obj(1, value)

    @property
    def Terminal(self) -> int:
        """
        DSS property name: Terminal
        DSS property index: 2
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @Terminal.setter
    def Terminal(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def kWLimit(self) -> float:
        """
        DSS property name: kWLimit
        DSS property index: 3
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @kWLimit.setter
    def kWLimit(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def kWBand(self) -> float:
        """
        DSS property name: kWBand
        DSS property index: 4
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @kWBand.setter
    def kWBand(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def kvarlimit(self) -> float:
        """
        DSS property name: kvarlimit
        DSS property index: 5
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @kvarlimit.setter
    def kvarlimit(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def GenList(self) -> List[str]:
        """
        DSS property name: GenList
        DSS property index: 6
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 6)

    @GenList.setter
    def GenList(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 6, value_ptr, value_count)
        self._check_for_error()

    @property
    def Weights(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: Weights
        DSS property index: 7
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 7)

    @Weights.setter
    def Weights(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(7, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 8
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 9
        """
        return self._lib.Obj_GetInt32(self._ptr, 9) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 9, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 10
        """
        self._set_string(10, value)

class Storage(DSSObj):
    _cls_name = 'Storage'
    _cls_idx = 28
    _cls_prop_idx = {
        'phases': 1,
        'bus1': 2,
        'kv': 3,
        'conn': 4,
        'kw': 5,
        'kvar': 6,
        'pf': 7,
        'kva': 8,
        'pctcutin': 9,
        '%cutin': 9,
        'pctcutout': 10,
        '%cutout': 10,
        'effcurve': 11,
        'varfollowinverter': 12,
        'kvarmax': 13,
        'kvarmaxabs': 14,
        'wattpriority': 15,
        'pfpriority': 16,
        'pctpminnovars': 17,
        '%pminnovars': 17,
        'pctpminkvarmax': 18,
        '%pminkvarmax': 18,
        'kwrated': 19,
        'pctkwrated': 20,
        '%kwrated': 20,
        'kwhrated': 21,
        'kwhstored': 22,
        'pctstored': 23,
        '%stored': 23,
        'pctreserve': 24,
        '%reserve': 24,
        'state': 25,
        'pctdischarge': 26,
        '%discharge': 26,
        'pctcharge': 27,
        '%charge': 27,
        'pcteffcharge': 28,
        '%effcharge': 28,
        'pcteffdischarge': 29,
        '%effdischarge': 29,
        'pctidlingkw': 30,
        '%idlingkw': 30,
        'pctr': 31,
        '%r': 31,
        'pctx': 32,
        '%x': 32,
        'model': 33,
        'vminpu': 34,
        'vmaxpu': 35,
        'balanced': 36,
        'limitcurrent': 37,
        'yearly': 38,
        'daily': 39,
        'duty': 40,
        'dispmode': 41,
        'dischargetrigger': 42,
        'chargetrigger': 43,
        'timechargetrig': 44,
        'cls': 45,
        'class': 45,
        'dynadll': 46,
        'dynadata': 47,
        'usermodel': 48,
        'userdata': 49,
        'debugtrace': 50,
        'spectrum': 51,
        'basefreq': 52,
        'enabled': 53,
        'like': 54,
    }

    # Class-specific enumerations
    class StorageState(IntEnum):
        """Storage: State (DSS enumeration for Storage)"""
        Charging = -1 # Charging
        Idling = 0 # Idling
        Discharging = 1 # Discharging

    class StorageDispatchMode(IntEnum):
        """Storage: Dispatch Mode (DSS enumeration for Storage)"""
        Default = 0 # Default
        LoadLevel = 1 # LoadLevel
        Price = 2 # Price
        External = 3 # External
        Follow = 4 # Follow


    @property
    def phases(self) -> int:
        """
        DSS property name: phases
        DSS property index: 1
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @phases.setter
    def phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def bus1(self) -> str:
        """
        DSS property name: bus1
        DSS property index: 2
        """
        return self._get_prop_string(2)

    @bus1.setter
    def bus1(self, value: AnyStr):
        self._set_string(2, value)

    @property
    def kv(self) -> float:
        """
        DSS property name: kv
        DSS property index: 3
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @kv.setter
    def kv(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def conn(self) -> Connection:
        """
    DSS property name: conn
    DSS property index: 4
    """
        return Connection(self._lib.Obj_GetInt32(self._ptr, 4))

    @conn.setter
    def conn(self, value: Union[AnyStr, int, Connection]):
        if not isinstance(value, int):
            self._set_string(4, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 4, value)

    @property
    def conn_str(self) -> str:
        """
        DSS property name: conn
        DSS property index: 4
        """
        return self._get_prop_string(4)

    @conn_str.setter
    def conn_str(self, value: AnyStr):
        self.conn = value

    @property
    def kW(self) -> float:
        """
        DSS property name: kW
        DSS property index: 5
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @kW.setter
    def kW(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def kvar(self) -> float:
        """
        DSS property name: kvar
        DSS property index: 6
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    @kvar.setter
    def kvar(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 6, value)

    @property
    def pf(self) -> float:
        """
        DSS property name: pf
        DSS property index: 7
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @pf.setter
    def pf(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def kVA(self) -> float:
        """
        DSS property name: kVA
        DSS property index: 8
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @kVA.setter
    def kVA(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def pctCutin(self) -> float:
        """
        DSS property name: %Cutin
        DSS property index: 9
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @pctCutin.setter
    def pctCutin(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def pctCutout(self) -> float:
        """
        DSS property name: %Cutout
        DSS property index: 10
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @pctCutout.setter
    def pctCutout(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def EffCurve(self) -> str:
        """
        DSS property name: EffCurve
        DSS property index: 11
        """
        return self._get_prop_string(11)

    @EffCurve.setter
    def EffCurve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(11, value)
            return

        self._set_string(11, value)

    @property
    def EffCurve_obj(self) -> XYcurve:
        """
        DSS property name: EffCurve
        DSS property index: 11
        """
        return self._get_obj(11, XYcurve)

    @EffCurve_obj.setter
    def EffCurve_obj(self, value: XYcurve):
        self._set_obj(11, value)

    @property
    def VarFollowInverter(self) -> bool:
        """
        DSS property name: VarFollowInverter
        DSS property index: 12
        """
        return self._lib.Obj_GetInt32(self._ptr, 12) != 0

    @VarFollowInverter.setter
    def VarFollowInverter(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 12, value)

    @property
    def kvarMax(self) -> float:
        """
        DSS property name: kvarMax
        DSS property index: 13
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @kvarMax.setter
    def kvarMax(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def kvarMaxAbs(self) -> float:
        """
        DSS property name: kvarMaxAbs
        DSS property index: 14
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @kvarMaxAbs.setter
    def kvarMaxAbs(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def WattPriority(self) -> bool:
        """
        DSS property name: WattPriority
        DSS property index: 15
        """
        return self._lib.Obj_GetInt32(self._ptr, 15) != 0

    @WattPriority.setter
    def WattPriority(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 15, value)

    @property
    def PFPriority(self) -> bool:
        """
        DSS property name: PFPriority
        DSS property index: 16
        """
        return self._lib.Obj_GetInt32(self._ptr, 16) != 0

    @PFPriority.setter
    def PFPriority(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 16, value)

    @property
    def pctPminNoVars(self) -> float:
        """
        DSS property name: %PminNoVars
        DSS property index: 17
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    @pctPminNoVars.setter
    def pctPminNoVars(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 17, value)

    @property
    def pctPminkvarMax(self) -> float:
        """
        DSS property name: %PminkvarMax
        DSS property index: 18
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    @pctPminkvarMax.setter
    def pctPminkvarMax(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 18, value)

    @property
    def kWrated(self) -> float:
        """
        DSS property name: kWrated
        DSS property index: 19
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    @kWrated.setter
    def kWrated(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 19, value)

    @property
    def pctkWrated(self) -> float:
        """
        DSS property name: %kWrated
        DSS property index: 20
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    @pctkWrated.setter
    def pctkWrated(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 20, value)

    @property
    def kWhrated(self) -> float:
        """
        DSS property name: kWhrated
        DSS property index: 21
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @kWhrated.setter
    def kWhrated(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    @property
    def kWhstored(self) -> float:
        """
        DSS property name: kWhstored
        DSS property index: 22
        """
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    @kWhstored.setter
    def kWhstored(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 22, value)

    @property
    def pctstored(self) -> float:
        """
        DSS property name: %stored
        DSS property index: 23
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    @pctstored.setter
    def pctstored(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 23, value)

    @property
    def pctreserve(self) -> float:
        """
        DSS property name: %reserve
        DSS property index: 24
        """
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    @pctreserve.setter
    def pctreserve(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 24, value)

    @property
    def State(self) -> StorageState:
        """
    DSS property name: State
    DSS property index: 25
    """
        return StorageState(self._lib.Obj_GetInt32(self._ptr, 25))

    @State.setter
    def State(self, value: Union[AnyStr, int, StorageState]):
        if not isinstance(value, int):
            self._set_string(25, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 25, value)

    @property
    def State_str(self) -> str:
        """
        DSS property name: State
        DSS property index: 25
        """
        return self._get_prop_string(25)

    @State_str.setter
    def State_str(self, value: AnyStr):
        self.State = value

    @property
    def pctDischarge(self) -> float:
        """
        DSS property name: %Discharge
        DSS property index: 26
        """
        return self._lib.Obj_GetFloat64(self._ptr, 26)

    @pctDischarge.setter
    def pctDischarge(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 26, value)

    @property
    def pctCharge(self) -> float:
        """
        DSS property name: %Charge
        DSS property index: 27
        """
        return self._lib.Obj_GetFloat64(self._ptr, 27)

    @pctCharge.setter
    def pctCharge(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 27, value)

    @property
    def pctEffCharge(self) -> float:
        """
        DSS property name: %EffCharge
        DSS property index: 28
        """
        return self._lib.Obj_GetFloat64(self._ptr, 28)

    @pctEffCharge.setter
    def pctEffCharge(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 28, value)

    @property
    def pctEffDischarge(self) -> float:
        """
        DSS property name: %EffDischarge
        DSS property index: 29
        """
        return self._lib.Obj_GetFloat64(self._ptr, 29)

    @pctEffDischarge.setter
    def pctEffDischarge(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 29, value)

    @property
    def pctIdlingkW(self) -> float:
        """
        DSS property name: %IdlingkW
        DSS property index: 30
        """
        return self._lib.Obj_GetFloat64(self._ptr, 30)

    @pctIdlingkW.setter
    def pctIdlingkW(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 30, value)

    @property
    def pctR(self) -> float:
        """
        DSS property name: %R
        DSS property index: 31
        """
        return self._lib.Obj_GetFloat64(self._ptr, 31)

    @pctR.setter
    def pctR(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 31, value)

    @property
    def pctX(self) -> float:
        """
        DSS property name: %X
        DSS property index: 32
        """
        return self._lib.Obj_GetFloat64(self._ptr, 32)

    @pctX.setter
    def pctX(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 32, value)

    @property
    def model(self) -> int:
        """
        DSS property name: model
        DSS property index: 33
        """
        return self._lib.Obj_GetInt32(self._ptr, 33)

    @model.setter
    def model(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 33, value)

    @property
    def Vminpu(self) -> float:
        """
        DSS property name: Vminpu
        DSS property index: 34
        """
        return self._lib.Obj_GetFloat64(self._ptr, 34)

    @Vminpu.setter
    def Vminpu(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 34, value)

    @property
    def Vmaxpu(self) -> float:
        """
        DSS property name: Vmaxpu
        DSS property index: 35
        """
        return self._lib.Obj_GetFloat64(self._ptr, 35)

    @Vmaxpu.setter
    def Vmaxpu(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 35, value)

    @property
    def Balanced(self) -> bool:
        """
        DSS property name: Balanced
        DSS property index: 36
        """
        return self._lib.Obj_GetInt32(self._ptr, 36) != 0

    @Balanced.setter
    def Balanced(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 36, value)

    @property
    def LimitCurrent(self) -> bool:
        """
        DSS property name: LimitCurrent
        DSS property index: 37
        """
        return self._lib.Obj_GetInt32(self._ptr, 37) != 0

    @LimitCurrent.setter
    def LimitCurrent(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 37, value)

    @property
    def yearly(self) -> str:
        """
        DSS property name: yearly
        DSS property index: 38
        """
        return self._get_prop_string(38)

    @yearly.setter
    def yearly(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(38, value)
            return

        self._set_string(38, value)

    @property
    def yearly_obj(self) -> LoadShape:
        """
        DSS property name: yearly
        DSS property index: 38
        """
        return self._get_obj(38, LoadShape)

    @yearly_obj.setter
    def yearly_obj(self, value: LoadShape):
        self._set_obj(38, value)

    @property
    def daily(self) -> str:
        """
        DSS property name: daily
        DSS property index: 39
        """
        return self._get_prop_string(39)

    @daily.setter
    def daily(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(39, value)
            return

        self._set_string(39, value)

    @property
    def daily_obj(self) -> LoadShape:
        """
        DSS property name: daily
        DSS property index: 39
        """
        return self._get_obj(39, LoadShape)

    @daily_obj.setter
    def daily_obj(self, value: LoadShape):
        self._set_obj(39, value)

    @property
    def duty(self) -> str:
        """
        DSS property name: duty
        DSS property index: 40
        """
        return self._get_prop_string(40)

    @duty.setter
    def duty(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(40, value)
            return

        self._set_string(40, value)

    @property
    def duty_obj(self) -> LoadShape:
        """
        DSS property name: duty
        DSS property index: 40
        """
        return self._get_obj(40, LoadShape)

    @duty_obj.setter
    def duty_obj(self, value: LoadShape):
        self._set_obj(40, value)

    @property
    def DispMode(self) -> StorageDispatchMode:
        """
    DSS property name: DispMode
    DSS property index: 41
    """
        return StorageDispatchMode(self._lib.Obj_GetInt32(self._ptr, 41))

    @DispMode.setter
    def DispMode(self, value: Union[AnyStr, int, StorageDispatchMode]):
        if not isinstance(value, int):
            self._set_string(41, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 41, value)

    @property
    def DispMode_str(self) -> str:
        """
        DSS property name: DispMode
        DSS property index: 41
        """
        return self._get_prop_string(41)

    @DispMode_str.setter
    def DispMode_str(self, value: AnyStr):
        self.DispMode = value

    @property
    def DischargeTrigger(self) -> float:
        """
        DSS property name: DischargeTrigger
        DSS property index: 42
        """
        return self._lib.Obj_GetFloat64(self._ptr, 42)

    @DischargeTrigger.setter
    def DischargeTrigger(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 42, value)

    @property
    def ChargeTrigger(self) -> float:
        """
        DSS property name: ChargeTrigger
        DSS property index: 43
        """
        return self._lib.Obj_GetFloat64(self._ptr, 43)

    @ChargeTrigger.setter
    def ChargeTrigger(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 43, value)

    @property
    def TimeChargeTrig(self) -> float:
        """
        DSS property name: TimeChargeTrig
        DSS property index: 44
        """
        return self._lib.Obj_GetFloat64(self._ptr, 44)

    @TimeChargeTrig.setter
    def TimeChargeTrig(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 44, value)

    @property
    def cls(self) -> int:
        """
        DSS property name: class
        DSS property index: 45
        """
        return self._lib.Obj_GetInt32(self._ptr, 45)

    @cls.setter
    def cls(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 45, value)

    @property
    def DynaDLL(self) -> str:
        """
        DSS property name: DynaDLL
        DSS property index: 46
        """
        return self._get_prop_string(46)

    @DynaDLL.setter
    def DynaDLL(self, value: AnyStr):
        self._set_string(46, value)

    @property
    def DynaData(self) -> str:
        """
        DSS property name: DynaData
        DSS property index: 47
        """
        return self._get_prop_string(47)

    @DynaData.setter
    def DynaData(self, value: AnyStr):
        self._set_string(47, value)

    @property
    def UserModel(self) -> str:
        """
        DSS property name: UserModel
        DSS property index: 48
        """
        return self._get_prop_string(48)

    @UserModel.setter
    def UserModel(self, value: AnyStr):
        self._set_string(48, value)

    @property
    def UserData(self) -> str:
        """
        DSS property name: UserData
        DSS property index: 49
        """
        return self._get_prop_string(49)

    @UserData.setter
    def UserData(self, value: AnyStr):
        self._set_string(49, value)

    @property
    def debugtrace(self) -> bool:
        """
        DSS property name: debugtrace
        DSS property index: 50
        """
        return self._lib.Obj_GetInt32(self._ptr, 50) != 0

    @debugtrace.setter
    def debugtrace(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 50, value)

    @property
    def spectrum(self) -> str:
        """
        DSS property name: spectrum
        DSS property index: 51
        """
        return self._get_prop_string(51)

    @spectrum.setter
    def spectrum(self, value: Union[AnyStr, Spectrum]):
        if isinstance(value, DSSObj):
            self._set_obj(51, value)
            return

        self._set_string(51, value)

    @property
    def spectrum_obj(self) -> Spectrum:
        """
        DSS property name: spectrum
        DSS property index: 51
        """
        return self._get_obj(51, Spectrum)

    @spectrum_obj.setter
    def spectrum_obj(self, value: Spectrum):
        self._set_obj(51, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 52
        """
        return self._lib.Obj_GetFloat64(self._ptr, 52)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 52, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 53
        """
        return self._lib.Obj_GetInt32(self._ptr, 53) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 53, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 54
        """
        self._set_string(54, value)

class StorageController(DSSObj):
    _cls_name = 'StorageController'
    _cls_idx = 29
    _cls_prop_idx = {
        'element': 1,
        'terminal': 2,
        'monphase': 3,
        'kwtarget': 4,
        'kwtargetlow': 5,
        'pctkwband': 6,
        '%kwband': 6,
        'kwband': 7,
        'pctkwbandlow': 8,
        '%kwbandlow': 8,
        'kwbandlow': 9,
        'elementlist': 10,
        'weights': 11,
        'modedischarge': 12,
        'modecharge': 13,
        'timedischargetrigger': 14,
        'timechargetrigger': 15,
        'pctratekw': 16,
        '%ratekw': 16,
        'pctratecharge': 17,
        '%ratecharge': 17,
        'pctreserve': 18,
        '%reserve': 18,
        'kwhtotal': 19,
        'kwtotal': 20,
        'kwhactual': 21,
        'kwactual': 22,
        'kwneed': 23,
        'yearly': 24,
        'daily': 25,
        'duty': 26,
        'eventlog': 27,
        'inhibittime': 28,
        'tup': 29,
        'tflat': 30,
        'tdn': 31,
        'kwthreshold': 32,
        'dispfactor': 33,
        'resetlevel': 34,
        'seasons': 35,
        'seasontargets': 36,
        'seasontargetslow': 37,
        'basefreq': 38,
        'enabled': 39,
        'like': 40,
    }

    # Class-specific enumerations
    class StorageControllerDischargemode(IntEnum):
        """StorageController: Discharge mode (DSS enumeration for StorageController)"""
        Peakshave = 5 # Peakshave
        Follow = 1 # Follow
        Support = 3 # Support
        Loadshape = 2 # Loadshape
        Time = 4 # Time
        Schedule = 6 # Schedule
        I_Peakshave = 8 # I-Peakshave

    class StorageControllerChargemode(IntEnum):
        """StorageController: Charge mode (DSS enumeration for StorageController)"""
        Loadshape = 2 # Loadshape
        Time = 4 # Time
        PeakshaveLow = 7 # PeakshaveLow
        I_PeakshaveLow = 9 # I-PeakshaveLow


    @property
    def Element(self) -> str:
        """
        DSS property name: Element
        DSS property index: 1
        """
        return self._get_prop_string(1)

    @Element.setter
    def Element(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_obj(1, value)
            return

        self._set_string(1, value)

    @property
    def Element_obj(self) -> DSSObj:
        """
        DSS property name: Element
        DSS property index: 1
        """
        return self._get_obj(1, None)

    @Element_obj.setter
    def Element_obj(self, value: DSSObj):
        self._set_obj(1, value)

    @property
    def Terminal(self) -> int:
        """
        DSS property name: Terminal
        DSS property index: 2
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @Terminal.setter
    def Terminal(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def MonPhase(self) -> Union[MonitoredPhase, int]:
        """
    DSS property name: MonPhase
    DSS property index: 3
    """
        value = self._lib.Obj_GetInt32(self._ptr, 3)
        if value > 0:
            return value

        return MonitoredPhase(value)

    @MonPhase.setter
    def MonPhase(self, value: Union[AnyStr, int, MonitoredPhase]):
        if not isinstance(value, int):
            self._set_string(3, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 3, value)

    @property
    def MonPhase_str(self) -> str:
        """
        DSS property name: MonPhase
        DSS property index: 3
        """
        return self._get_prop_string(3)

    @MonPhase_str.setter
    def MonPhase_str(self, value: AnyStr):
        self.MonPhase = value

    @property
    def kWTarget(self) -> float:
        """
        DSS property name: kWTarget
        DSS property index: 4
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @kWTarget.setter
    def kWTarget(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def kWTargetLow(self) -> float:
        """
        DSS property name: kWTargetLow
        DSS property index: 5
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @kWTargetLow.setter
    def kWTargetLow(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def pctkWBand(self) -> float:
        """
        DSS property name: %kWBand
        DSS property index: 6
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    @pctkWBand.setter
    def pctkWBand(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 6, value)

    @property
    def kWBand(self) -> float:
        """
        DSS property name: kWBand
        DSS property index: 7
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @kWBand.setter
    def kWBand(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def pctkWBandLow(self) -> float:
        """
        DSS property name: %kWBandLow
        DSS property index: 8
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @pctkWBandLow.setter
    def pctkWBandLow(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def kWBandLow(self) -> float:
        """
        DSS property name: kWBandLow
        DSS property index: 9
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @kWBandLow.setter
    def kWBandLow(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def ElementList(self) -> List[str]:
        """
        DSS property name: ElementList
        DSS property index: 10
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 10)

    @ElementList.setter
    def ElementList(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 10, value_ptr, value_count)
        self._check_for_error()

    @property
    def Weights(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: Weights
        DSS property index: 11
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 11)

    @Weights.setter
    def Weights(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(11, value)

    @property
    def ModeDischarge(self) -> StorageControllerDischargemode:
        """
    DSS property name: ModeDischarge
    DSS property index: 12
    """
        return StorageControllerDischargemode(self._lib.Obj_GetInt32(self._ptr, 12))

    @ModeDischarge.setter
    def ModeDischarge(self, value: Union[AnyStr, int, StorageControllerDischargemode]):
        if not isinstance(value, int):
            self._set_string(12, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 12, value)

    @property
    def ModeDischarge_str(self) -> str:
        """
        DSS property name: ModeDischarge
        DSS property index: 12
        """
        return self._get_prop_string(12)

    @ModeDischarge_str.setter
    def ModeDischarge_str(self, value: AnyStr):
        self.ModeDischarge = value

    @property
    def ModeCharge(self) -> StorageControllerChargemode:
        """
    DSS property name: ModeCharge
    DSS property index: 13
    """
        return StorageControllerChargemode(self._lib.Obj_GetInt32(self._ptr, 13))

    @ModeCharge.setter
    def ModeCharge(self, value: Union[AnyStr, int, StorageControllerChargemode]):
        if not isinstance(value, int):
            self._set_string(13, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 13, value)

    @property
    def ModeCharge_str(self) -> str:
        """
        DSS property name: ModeCharge
        DSS property index: 13
        """
        return self._get_prop_string(13)

    @ModeCharge_str.setter
    def ModeCharge_str(self, value: AnyStr):
        self.ModeCharge = value

    @property
    def TimeDischargeTrigger(self) -> float:
        """
        DSS property name: TimeDischargeTrigger
        DSS property index: 14
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @TimeDischargeTrigger.setter
    def TimeDischargeTrigger(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def TimeChargeTrigger(self) -> float:
        """
        DSS property name: TimeChargeTrigger
        DSS property index: 15
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @TimeChargeTrigger.setter
    def TimeChargeTrigger(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def pctRatekW(self) -> float:
        """
        DSS property name: %RatekW
        DSS property index: 16
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    @pctRatekW.setter
    def pctRatekW(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 16, value)

    @property
    def pctRateCharge(self) -> float:
        """
        DSS property name: %RateCharge
        DSS property index: 17
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    @pctRateCharge.setter
    def pctRateCharge(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 17, value)

    @property
    def pctReserve(self) -> float:
        """
        DSS property name: %Reserve
        DSS property index: 18
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    @pctReserve.setter
    def pctReserve(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 18, value)

    @property
    def kWhTotal(self) -> float:
        """
        DSS property name: kWhTotal
        DSS property index: 19
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    @kWhTotal.setter
    def kWhTotal(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 19, value)

    @property
    def kWTotal(self) -> float:
        """
        DSS property name: kWTotal
        DSS property index: 20
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    @kWTotal.setter
    def kWTotal(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 20, value)

    @property
    def kWhActual(self) -> float:
        """
        DSS property name: kWhActual
        DSS property index: 21
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @kWhActual.setter
    def kWhActual(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    @property
    def kWActual(self) -> float:
        """
        DSS property name: kWActual
        DSS property index: 22
        """
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    @kWActual.setter
    def kWActual(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 22, value)

    @property
    def kWneed(self) -> float:
        """
        DSS property name: kWneed
        DSS property index: 23
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    @kWneed.setter
    def kWneed(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 23, value)

    @property
    def Yearly(self) -> str:
        """
        DSS property name: Yearly
        DSS property index: 24
        """
        return self._get_prop_string(24)

    @Yearly.setter
    def Yearly(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(24, value)
            return

        self._set_string(24, value)

    @property
    def Yearly_obj(self) -> LoadShape:
        """
        DSS property name: Yearly
        DSS property index: 24
        """
        return self._get_obj(24, LoadShape)

    @Yearly_obj.setter
    def Yearly_obj(self, value: LoadShape):
        self._set_obj(24, value)

    @property
    def Daily(self) -> str:
        """
        DSS property name: Daily
        DSS property index: 25
        """
        return self._get_prop_string(25)

    @Daily.setter
    def Daily(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(25, value)
            return

        self._set_string(25, value)

    @property
    def Daily_obj(self) -> LoadShape:
        """
        DSS property name: Daily
        DSS property index: 25
        """
        return self._get_obj(25, LoadShape)

    @Daily_obj.setter
    def Daily_obj(self, value: LoadShape):
        self._set_obj(25, value)

    @property
    def Duty(self) -> str:
        """
        DSS property name: Duty
        DSS property index: 26
        """
        return self._get_prop_string(26)

    @Duty.setter
    def Duty(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(26, value)
            return

        self._set_string(26, value)

    @property
    def Duty_obj(self) -> LoadShape:
        """
        DSS property name: Duty
        DSS property index: 26
        """
        return self._get_obj(26, LoadShape)

    @Duty_obj.setter
    def Duty_obj(self, value: LoadShape):
        self._set_obj(26, value)

    @property
    def EventLog(self) -> bool:
        """
        DSS property name: EventLog
        DSS property index: 27
        """
        return self._lib.Obj_GetInt32(self._ptr, 27) != 0

    @EventLog.setter
    def EventLog(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 27, value)

    @property
    def InhibitTime(self) -> int:
        """
        DSS property name: InhibitTime
        DSS property index: 28
        """
        return self._lib.Obj_GetInt32(self._ptr, 28)

    @InhibitTime.setter
    def InhibitTime(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 28, value)

    @property
    def Tup(self) -> float:
        """
        DSS property name: Tup
        DSS property index: 29
        """
        return self._lib.Obj_GetFloat64(self._ptr, 29)

    @Tup.setter
    def Tup(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 29, value)

    @property
    def TFlat(self) -> float:
        """
        DSS property name: TFlat
        DSS property index: 30
        """
        return self._lib.Obj_GetFloat64(self._ptr, 30)

    @TFlat.setter
    def TFlat(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 30, value)

    @property
    def Tdn(self) -> float:
        """
        DSS property name: Tdn
        DSS property index: 31
        """
        return self._lib.Obj_GetFloat64(self._ptr, 31)

    @Tdn.setter
    def Tdn(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 31, value)

    @property
    def kWThreshold(self) -> float:
        """
        DSS property name: kWThreshold
        DSS property index: 32
        """
        return self._lib.Obj_GetFloat64(self._ptr, 32)

    @kWThreshold.setter
    def kWThreshold(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 32, value)

    @property
    def DispFactor(self) -> float:
        """
        DSS property name: DispFactor
        DSS property index: 33
        """
        return self._lib.Obj_GetFloat64(self._ptr, 33)

    @DispFactor.setter
    def DispFactor(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 33, value)

    @property
    def ResetLevel(self) -> float:
        """
        DSS property name: ResetLevel
        DSS property index: 34
        """
        return self._lib.Obj_GetFloat64(self._ptr, 34)

    @ResetLevel.setter
    def ResetLevel(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 34, value)

    @property
    def Seasons(self) -> int:
        """
        DSS property name: Seasons
        DSS property index: 35
        """
        return self._lib.Obj_GetInt32(self._ptr, 35)

    @Seasons.setter
    def Seasons(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 35, value)

    @property
    def SeasonTargets(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: SeasonTargets
        DSS property index: 36
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 36)

    @SeasonTargets.setter
    def SeasonTargets(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(36, value)

    @property
    def SeasonTargetsLow(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: SeasonTargetsLow
        DSS property index: 37
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 37)

    @SeasonTargetsLow.setter
    def SeasonTargetsLow(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(37, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 38
        """
        return self._lib.Obj_GetFloat64(self._ptr, 38)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 38, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 39
        """
        return self._lib.Obj_GetInt32(self._ptr, 39) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 39, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 40
        """
        self._set_string(40, value)

class Relay(DSSObj):
    _cls_name = 'Relay'
    _cls_idx = 30
    _cls_prop_idx = {
        'monitoredobj': 1,
        'monitoredterm': 2,
        'switchedobj': 3,
        'switchedterm': 4,
        'type': 5,
        'phasecurve': 6,
        'groundcurve': 7,
        'phasetrip': 8,
        'groundtrip': 9,
        'tdphase': 10,
        'tdground': 11,
        'phaseinst': 12,
        'groundinst': 13,
        'reset': 14,
        'shots': 15,
        'recloseintervals': 16,
        'delay': 17,
        'overvoltcurve': 18,
        'undervoltcurve': 19,
        'kvbase': 20,
        'pctpickup47': 21,
        '47%pickup': 21,
        'baseamps46': 22,
        '46baseamps': 22,
        'pctpickup46': 23,
        '46%pickup': 23,
        'isqt46': 24,
        '46isqt': 24,
        'variable': 25,
        'overtrip': 26,
        'undertrip': 27,
        'breakertime': 28,
        'action': 29,
        'z1mag': 30,
        'z1ang': 31,
        'z0mag': 32,
        'z0ang': 33,
        'mphase': 34,
        'mground': 35,
        'eventlog': 36,
        'debugtrace': 37,
        'distreverse': 38,
        'normal': 39,
        'state': 40,
        'doc_tiltanglelow': 41,
        'doc_tiltanglehigh': 42,
        'doc_tripsettinglow': 43,
        'doc_tripsettinghigh': 44,
        'doc_tripsettingmag': 45,
        'doc_delayinner': 46,
        'doc_phasecurveinner': 47,
        'doc_phasetripinner': 48,
        'doc_tdphaseinner': 49,
        'basefreq': 50,
        'enabled': 51,
        'like': 52,
    }

    # Class-specific enumerations
    class RelayType(IntEnum):
        """Relay: Type (DSS enumeration for Relay)"""
        Current = 0 # Current
        Voltage = 1 # Voltage
        ReversePower = 3 # ReversePower
        relay46 = 4 # 46
        relay47 = 5 # 47
        Generic = 6 # Generic
        Distance = 7 # Distance
        TD21 = 8 # TD21
        DOC = 9 # DOC

    class RelayAction(IntEnum):
        """Relay: Action (DSS enumeration for Relay)"""
        close = 2 # close
        open = 1 # open
        trip = 1 # trip

    class RelayState(IntEnum):
        """Relay: State (DSS enumeration for Relay)"""
        closed = 2 # closed
        open = 1 # open
        trip = 1 # trip


    @property
    def MonitoredObj(self) -> str:
        """
        DSS property name: MonitoredObj
        DSS property index: 1
        """
        return self._get_prop_string(1)

    @MonitoredObj.setter
    def MonitoredObj(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_obj(1, value)
            return

        self._set_string(1, value)

    @property
    def MonitoredObj_obj(self) -> DSSObj:
        """
        DSS property name: MonitoredObj
        DSS property index: 1
        """
        return self._get_obj(1, None)

    @MonitoredObj_obj.setter
    def MonitoredObj_obj(self, value: DSSObj):
        self._set_obj(1, value)

    @property
    def MonitoredTerm(self) -> int:
        """
        DSS property name: MonitoredTerm
        DSS property index: 2
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @MonitoredTerm.setter
    def MonitoredTerm(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def SwitchedObj(self) -> str:
        """
        DSS property name: SwitchedObj
        DSS property index: 3
        """
        return self._get_prop_string(3)

    @SwitchedObj.setter
    def SwitchedObj(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_obj(3, value)
            return

        self._set_string(3, value)

    @property
    def SwitchedObj_obj(self) -> DSSObj:
        """
        DSS property name: SwitchedObj
        DSS property index: 3
        """
        return self._get_obj(3, None)

    @SwitchedObj_obj.setter
    def SwitchedObj_obj(self, value: DSSObj):
        self._set_obj(3, value)

    @property
    def SwitchedTerm(self) -> int:
        """
        DSS property name: SwitchedTerm
        DSS property index: 4
        """
        return self._lib.Obj_GetInt32(self._ptr, 4)

    @SwitchedTerm.setter
    def SwitchedTerm(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 4, value)

    @property
    def type(self) -> RelayType:
        """
    DSS property name: type
    DSS property index: 5
    """
        return RelayType(self._lib.Obj_GetInt32(self._ptr, 5))

    @type.setter
    def type(self, value: Union[AnyStr, int, RelayType]):
        if not isinstance(value, int):
            self._set_string(5, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 5, value)

    @property
    def type_str(self) -> str:
        """
        DSS property name: type
        DSS property index: 5
        """
        return self._get_prop_string(5)

    @type_str.setter
    def type_str(self, value: AnyStr):
        self.type = value

    @property
    def Phasecurve(self) -> str:
        """
        DSS property name: Phasecurve
        DSS property index: 6
        """
        return self._get_prop_string(6)

    @Phasecurve.setter
    def Phasecurve(self, value: Union[AnyStr, TCC_Curve]):
        if isinstance(value, DSSObj):
            self._set_obj(6, value)
            return

        self._set_string(6, value)

    @property
    def Phasecurve_obj(self) -> TCC_Curve:
        """
        DSS property name: Phasecurve
        DSS property index: 6
        """
        return self._get_obj(6, TCC_Curve)

    @Phasecurve_obj.setter
    def Phasecurve_obj(self, value: TCC_Curve):
        self._set_obj(6, value)

    @property
    def Groundcurve(self) -> str:
        """
        DSS property name: Groundcurve
        DSS property index: 7
        """
        return self._get_prop_string(7)

    @Groundcurve.setter
    def Groundcurve(self, value: Union[AnyStr, TCC_Curve]):
        if isinstance(value, DSSObj):
            self._set_obj(7, value)
            return

        self._set_string(7, value)

    @property
    def Groundcurve_obj(self) -> TCC_Curve:
        """
        DSS property name: Groundcurve
        DSS property index: 7
        """
        return self._get_obj(7, TCC_Curve)

    @Groundcurve_obj.setter
    def Groundcurve_obj(self, value: TCC_Curve):
        self._set_obj(7, value)

    @property
    def PhaseTrip(self) -> float:
        """
        DSS property name: PhaseTrip
        DSS property index: 8
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @PhaseTrip.setter
    def PhaseTrip(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def GroundTrip(self) -> float:
        """
        DSS property name: GroundTrip
        DSS property index: 9
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @GroundTrip.setter
    def GroundTrip(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def TDPhase(self) -> float:
        """
        DSS property name: TDPhase
        DSS property index: 10
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @TDPhase.setter
    def TDPhase(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def TDGround(self) -> float:
        """
        DSS property name: TDGround
        DSS property index: 11
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @TDGround.setter
    def TDGround(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def PhaseInst(self) -> float:
        """
        DSS property name: PhaseInst
        DSS property index: 12
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @PhaseInst.setter
    def PhaseInst(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def GroundInst(self) -> float:
        """
        DSS property name: GroundInst
        DSS property index: 13
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @GroundInst.setter
    def GroundInst(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def Reset(self) -> float:
        """
        DSS property name: Reset
        DSS property index: 14
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @Reset.setter
    def Reset(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def Shots(self) -> int:
        """
        DSS property name: Shots
        DSS property index: 15
        """
        return self._lib.Obj_GetInt32(self._ptr, 15)

    @Shots.setter
    def Shots(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 15, value)

    @property
    def RecloseIntervals(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: RecloseIntervals
        DSS property index: 16
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 16)

    @RecloseIntervals.setter
    def RecloseIntervals(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(16, value)

    @property
    def Delay(self) -> float:
        """
        DSS property name: Delay
        DSS property index: 17
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    @Delay.setter
    def Delay(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 17, value)

    @property
    def Overvoltcurve(self) -> str:
        """
        DSS property name: Overvoltcurve
        DSS property index: 18
        """
        return self._get_prop_string(18)

    @Overvoltcurve.setter
    def Overvoltcurve(self, value: Union[AnyStr, TCC_Curve]):
        if isinstance(value, DSSObj):
            self._set_obj(18, value)
            return

        self._set_string(18, value)

    @property
    def Overvoltcurve_obj(self) -> TCC_Curve:
        """
        DSS property name: Overvoltcurve
        DSS property index: 18
        """
        return self._get_obj(18, TCC_Curve)

    @Overvoltcurve_obj.setter
    def Overvoltcurve_obj(self, value: TCC_Curve):
        self._set_obj(18, value)

    @property
    def Undervoltcurve(self) -> str:
        """
        DSS property name: Undervoltcurve
        DSS property index: 19
        """
        return self._get_prop_string(19)

    @Undervoltcurve.setter
    def Undervoltcurve(self, value: Union[AnyStr, TCC_Curve]):
        if isinstance(value, DSSObj):
            self._set_obj(19, value)
            return

        self._set_string(19, value)

    @property
    def Undervoltcurve_obj(self) -> TCC_Curve:
        """
        DSS property name: Undervoltcurve
        DSS property index: 19
        """
        return self._get_obj(19, TCC_Curve)

    @Undervoltcurve_obj.setter
    def Undervoltcurve_obj(self, value: TCC_Curve):
        self._set_obj(19, value)

    @property
    def kvbase(self) -> float:
        """
        DSS property name: kvbase
        DSS property index: 20
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    @kvbase.setter
    def kvbase(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 20, value)

    @property
    def pctPickup47(self) -> float:
        """
        DSS property name: 47%Pickup
        DSS property index: 21
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @pctPickup47.setter
    def pctPickup47(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    @property
    def BaseAmps46(self) -> float:
        """
        DSS property name: 46BaseAmps
        DSS property index: 22
        """
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    @BaseAmps46.setter
    def BaseAmps46(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 22, value)

    @property
    def pctPickup46(self) -> float:
        """
        DSS property name: 46%Pickup
        DSS property index: 23
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    @pctPickup46.setter
    def pctPickup46(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 23, value)

    @property
    def isqt46(self) -> float:
        """
        DSS property name: 46isqt
        DSS property index: 24
        """
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    @isqt46.setter
    def isqt46(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 24, value)

    @property
    def Variable(self) -> str:
        """
        DSS property name: Variable
        DSS property index: 25
        """
        return self._get_prop_string(25)

    @Variable.setter
    def Variable(self, value: AnyStr):
        self._set_string(25, value)

    @property
    def overtrip(self) -> float:
        """
        DSS property name: overtrip
        DSS property index: 26
        """
        return self._lib.Obj_GetFloat64(self._ptr, 26)

    @overtrip.setter
    def overtrip(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 26, value)

    @property
    def undertrip(self) -> float:
        """
        DSS property name: undertrip
        DSS property index: 27
        """
        return self._lib.Obj_GetFloat64(self._ptr, 27)

    @undertrip.setter
    def undertrip(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 27, value)

    @property
    def Breakertime(self) -> float:
        """
        DSS property name: Breakertime
        DSS property index: 28
        """
        return self._lib.Obj_GetFloat64(self._ptr, 28)

    @Breakertime.setter
    def Breakertime(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 28, value)

    @property
    def action(self) -> RelayAction:
        """
    DSS property name: action
    DSS property index: 29
    """
        return RelayAction(self._lib.Obj_GetInt32(self._ptr, 29))

    @action.setter
    def action(self, value: Union[AnyStr, int, RelayAction]):
        if not isinstance(value, int):
            self._set_string(29, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 29, value)

    @property
    def action_str(self) -> str:
        """
        DSS property name: action
        DSS property index: 29
        """
        return self._get_prop_string(29)

    @action_str.setter
    def action_str(self, value: AnyStr):
        self.action = value

    @property
    def Z1mag(self) -> float:
        """
        DSS property name: Z1mag
        DSS property index: 30
        """
        return self._lib.Obj_GetFloat64(self._ptr, 30)

    @Z1mag.setter
    def Z1mag(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 30, value)

    @property
    def Z1ang(self) -> float:
        """
        DSS property name: Z1ang
        DSS property index: 31
        """
        return self._lib.Obj_GetFloat64(self._ptr, 31)

    @Z1ang.setter
    def Z1ang(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 31, value)

    @property
    def Z0mag(self) -> float:
        """
        DSS property name: Z0mag
        DSS property index: 32
        """
        return self._lib.Obj_GetFloat64(self._ptr, 32)

    @Z0mag.setter
    def Z0mag(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 32, value)

    @property
    def Z0ang(self) -> float:
        """
        DSS property name: Z0ang
        DSS property index: 33
        """
        return self._lib.Obj_GetFloat64(self._ptr, 33)

    @Z0ang.setter
    def Z0ang(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 33, value)

    @property
    def Mphase(self) -> float:
        """
        DSS property name: Mphase
        DSS property index: 34
        """
        return self._lib.Obj_GetFloat64(self._ptr, 34)

    @Mphase.setter
    def Mphase(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 34, value)

    @property
    def Mground(self) -> float:
        """
        DSS property name: Mground
        DSS property index: 35
        """
        return self._lib.Obj_GetFloat64(self._ptr, 35)

    @Mground.setter
    def Mground(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 35, value)

    @property
    def EventLog(self) -> bool:
        """
        DSS property name: EventLog
        DSS property index: 36
        """
        return self._lib.Obj_GetInt32(self._ptr, 36) != 0

    @EventLog.setter
    def EventLog(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 36, value)

    @property
    def DebugTrace(self) -> bool:
        """
        DSS property name: DebugTrace
        DSS property index: 37
        """
        return self._lib.Obj_GetInt32(self._ptr, 37) != 0

    @DebugTrace.setter
    def DebugTrace(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 37, value)

    @property
    def DistReverse(self) -> bool:
        """
        DSS property name: DistReverse
        DSS property index: 38
        """
        return self._lib.Obj_GetInt32(self._ptr, 38) != 0

    @DistReverse.setter
    def DistReverse(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 38, value)

    @property
    def Normal(self) -> RelayState:
        """
    DSS property name: Normal
    DSS property index: 39
    """
        return RelayState(self._lib.Obj_GetInt32(self._ptr, 39))

    @Normal.setter
    def Normal(self, value: Union[AnyStr, int, RelayState]):
        if not isinstance(value, int):
            self._set_string(39, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 39, value)

    @property
    def Normal_str(self) -> str:
        """
        DSS property name: Normal
        DSS property index: 39
        """
        return self._get_prop_string(39)

    @Normal_str.setter
    def Normal_str(self, value: AnyStr):
        self.Normal = value

    @property
    def State(self) -> RelayState:
        """
    DSS property name: State
    DSS property index: 40
    """
        return RelayState(self._lib.Obj_GetInt32(self._ptr, 40))

    @State.setter
    def State(self, value: Union[AnyStr, int, RelayState]):
        if not isinstance(value, int):
            self._set_string(40, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 40, value)

    @property
    def State_str(self) -> str:
        """
        DSS property name: State
        DSS property index: 40
        """
        return self._get_prop_string(40)

    @State_str.setter
    def State_str(self, value: AnyStr):
        self.State = value

    @property
    def DOC_TiltAngleLow(self) -> float:
        """
        DSS property name: DOC_TiltAngleLow
        DSS property index: 41
        """
        return self._lib.Obj_GetFloat64(self._ptr, 41)

    @DOC_TiltAngleLow.setter
    def DOC_TiltAngleLow(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 41, value)

    @property
    def DOC_TiltAngleHigh(self) -> float:
        """
        DSS property name: DOC_TiltAngleHigh
        DSS property index: 42
        """
        return self._lib.Obj_GetFloat64(self._ptr, 42)

    @DOC_TiltAngleHigh.setter
    def DOC_TiltAngleHigh(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 42, value)

    @property
    def DOC_TripSettingLow(self) -> float:
        """
        DSS property name: DOC_TripSettingLow
        DSS property index: 43
        """
        return self._lib.Obj_GetFloat64(self._ptr, 43)

    @DOC_TripSettingLow.setter
    def DOC_TripSettingLow(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 43, value)

    @property
    def DOC_TripSettingHigh(self) -> float:
        """
        DSS property name: DOC_TripSettingHigh
        DSS property index: 44
        """
        return self._lib.Obj_GetFloat64(self._ptr, 44)

    @DOC_TripSettingHigh.setter
    def DOC_TripSettingHigh(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 44, value)

    @property
    def DOC_TripSettingMag(self) -> float:
        """
        DSS property name: DOC_TripSettingMag
        DSS property index: 45
        """
        return self._lib.Obj_GetFloat64(self._ptr, 45)

    @DOC_TripSettingMag.setter
    def DOC_TripSettingMag(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 45, value)

    @property
    def DOC_DelayInner(self) -> float:
        """
        DSS property name: DOC_DelayInner
        DSS property index: 46
        """
        return self._lib.Obj_GetFloat64(self._ptr, 46)

    @DOC_DelayInner.setter
    def DOC_DelayInner(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 46, value)

    @property
    def DOC_PhaseCurveInner(self) -> float:
        """
        DSS property name: DOC_PhaseCurveInner
        DSS property index: 47
        """
        return self._lib.Obj_GetFloat64(self._ptr, 47)

    @DOC_PhaseCurveInner.setter
    def DOC_PhaseCurveInner(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 47, value)

    @property
    def DOC_PhaseTripInner(self) -> float:
        """
        DSS property name: DOC_PhaseTripInner
        DSS property index: 48
        """
        return self._lib.Obj_GetFloat64(self._ptr, 48)

    @DOC_PhaseTripInner.setter
    def DOC_PhaseTripInner(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 48, value)

    @property
    def DOC_TDPhaseInner(self) -> str:
        """
        DSS property name: DOC_TDPhaseInner
        DSS property index: 49
        """
        return self._get_prop_string(49)

    @DOC_TDPhaseInner.setter
    def DOC_TDPhaseInner(self, value: Union[AnyStr, TCC_Curve]):
        if isinstance(value, DSSObj):
            self._set_obj(49, value)
            return

        self._set_string(49, value)

    @property
    def DOC_TDPhaseInner_obj(self) -> TCC_Curve:
        """
        DSS property name: DOC_TDPhaseInner
        DSS property index: 49
        """
        return self._get_obj(49, TCC_Curve)

    @DOC_TDPhaseInner_obj.setter
    def DOC_TDPhaseInner_obj(self, value: TCC_Curve):
        self._set_obj(49, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 50
        """
        return self._lib.Obj_GetFloat64(self._ptr, 50)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 50, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 51
        """
        return self._lib.Obj_GetInt32(self._ptr, 51) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 51, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 52
        """
        self._set_string(52, value)

class Recloser(DSSObj):
    _cls_name = 'Recloser'
    _cls_idx = 31
    _cls_prop_idx = {
        'monitoredobj': 1,
        'monitoredterm': 2,
        'switchedobj': 3,
        'switchedterm': 4,
        'numfast': 5,
        'phasefast': 6,
        'phasedelayed': 7,
        'groundfast': 8,
        'grounddelayed': 9,
        'phasetrip': 10,
        'groundtrip': 11,
        'phaseinst': 12,
        'groundinst': 13,
        'reset': 14,
        'shots': 15,
        'recloseintervals': 16,
        'delay': 17,
        'action': 18,
        'tdphfast': 19,
        'tdgrfast': 20,
        'tdphdelayed': 21,
        'tdgrdelayed': 22,
        'normal': 23,
        'state': 24,
        'basefreq': 25,
        'enabled': 26,
        'like': 27,
    }

    # Class-specific enumerations
    class RecloserAction(IntEnum):
        """Recloser: Action (DSS enumeration for Recloser)"""
        close = 2 # close
        open = 1 # open
        trip = 1 # trip

    class RecloserState(IntEnum):
        """Recloser: State (DSS enumeration for Recloser)"""
        closed = 2 # closed
        open = 1 # open
        trip = 1 # trip


    @property
    def MonitoredObj(self) -> str:
        """
        DSS property name: MonitoredObj
        DSS property index: 1
        """
        return self._get_prop_string(1)

    @MonitoredObj.setter
    def MonitoredObj(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_obj(1, value)
            return

        self._set_string(1, value)

    @property
    def MonitoredObj_obj(self) -> DSSObj:
        """
        DSS property name: MonitoredObj
        DSS property index: 1
        """
        return self._get_obj(1, None)

    @MonitoredObj_obj.setter
    def MonitoredObj_obj(self, value: DSSObj):
        self._set_obj(1, value)

    @property
    def MonitoredTerm(self) -> int:
        """
        DSS property name: MonitoredTerm
        DSS property index: 2
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @MonitoredTerm.setter
    def MonitoredTerm(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def SwitchedObj(self) -> str:
        """
        DSS property name: SwitchedObj
        DSS property index: 3
        """
        return self._get_prop_string(3)

    @SwitchedObj.setter
    def SwitchedObj(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_obj(3, value)
            return

        self._set_string(3, value)

    @property
    def SwitchedObj_obj(self) -> DSSObj:
        """
        DSS property name: SwitchedObj
        DSS property index: 3
        """
        return self._get_obj(3, None)

    @SwitchedObj_obj.setter
    def SwitchedObj_obj(self, value: DSSObj):
        self._set_obj(3, value)

    @property
    def SwitchedTerm(self) -> int:
        """
        DSS property name: SwitchedTerm
        DSS property index: 4
        """
        return self._lib.Obj_GetInt32(self._ptr, 4)

    @SwitchedTerm.setter
    def SwitchedTerm(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 4, value)

    @property
    def NumFast(self) -> int:
        """
        DSS property name: NumFast
        DSS property index: 5
        """
        return self._lib.Obj_GetInt32(self._ptr, 5)

    @NumFast.setter
    def NumFast(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 5, value)

    @property
    def PhaseFast(self) -> str:
        """
        DSS property name: PhaseFast
        DSS property index: 6
        """
        return self._get_prop_string(6)

    @PhaseFast.setter
    def PhaseFast(self, value: Union[AnyStr, TCC_Curve]):
        if isinstance(value, DSSObj):
            self._set_obj(6, value)
            return

        self._set_string(6, value)

    @property
    def PhaseFast_obj(self) -> TCC_Curve:
        """
        DSS property name: PhaseFast
        DSS property index: 6
        """
        return self._get_obj(6, TCC_Curve)

    @PhaseFast_obj.setter
    def PhaseFast_obj(self, value: TCC_Curve):
        self._set_obj(6, value)

    @property
    def PhaseDelayed(self) -> str:
        """
        DSS property name: PhaseDelayed
        DSS property index: 7
        """
        return self._get_prop_string(7)

    @PhaseDelayed.setter
    def PhaseDelayed(self, value: Union[AnyStr, TCC_Curve]):
        if isinstance(value, DSSObj):
            self._set_obj(7, value)
            return

        self._set_string(7, value)

    @property
    def PhaseDelayed_obj(self) -> TCC_Curve:
        """
        DSS property name: PhaseDelayed
        DSS property index: 7
        """
        return self._get_obj(7, TCC_Curve)

    @PhaseDelayed_obj.setter
    def PhaseDelayed_obj(self, value: TCC_Curve):
        self._set_obj(7, value)

    @property
    def GroundFast(self) -> str:
        """
        DSS property name: GroundFast
        DSS property index: 8
        """
        return self._get_prop_string(8)

    @GroundFast.setter
    def GroundFast(self, value: Union[AnyStr, TCC_Curve]):
        if isinstance(value, DSSObj):
            self._set_obj(8, value)
            return

        self._set_string(8, value)

    @property
    def GroundFast_obj(self) -> TCC_Curve:
        """
        DSS property name: GroundFast
        DSS property index: 8
        """
        return self._get_obj(8, TCC_Curve)

    @GroundFast_obj.setter
    def GroundFast_obj(self, value: TCC_Curve):
        self._set_obj(8, value)

    @property
    def GroundDelayed(self) -> str:
        """
        DSS property name: GroundDelayed
        DSS property index: 9
        """
        return self._get_prop_string(9)

    @GroundDelayed.setter
    def GroundDelayed(self, value: Union[AnyStr, TCC_Curve]):
        if isinstance(value, DSSObj):
            self._set_obj(9, value)
            return

        self._set_string(9, value)

    @property
    def GroundDelayed_obj(self) -> TCC_Curve:
        """
        DSS property name: GroundDelayed
        DSS property index: 9
        """
        return self._get_obj(9, TCC_Curve)

    @GroundDelayed_obj.setter
    def GroundDelayed_obj(self, value: TCC_Curve):
        self._set_obj(9, value)

    @property
    def PhaseTrip(self) -> float:
        """
        DSS property name: PhaseTrip
        DSS property index: 10
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @PhaseTrip.setter
    def PhaseTrip(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def GroundTrip(self) -> float:
        """
        DSS property name: GroundTrip
        DSS property index: 11
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @GroundTrip.setter
    def GroundTrip(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def PhaseInst(self) -> float:
        """
        DSS property name: PhaseInst
        DSS property index: 12
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @PhaseInst.setter
    def PhaseInst(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def GroundInst(self) -> float:
        """
        DSS property name: GroundInst
        DSS property index: 13
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @GroundInst.setter
    def GroundInst(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def Reset(self) -> float:
        """
        DSS property name: Reset
        DSS property index: 14
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @Reset.setter
    def Reset(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def Shots(self) -> int:
        """
        DSS property name: Shots
        DSS property index: 15
        """
        return self._lib.Obj_GetInt32(self._ptr, 15)

    @Shots.setter
    def Shots(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 15, value)

    @property
    def RecloseIntervals(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: RecloseIntervals
        DSS property index: 16
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 16)

    @RecloseIntervals.setter
    def RecloseIntervals(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(16, value)

    @property
    def Delay(self) -> float:
        """
        DSS property name: Delay
        DSS property index: 17
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    @Delay.setter
    def Delay(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 17, value)

    @property
    def Action(self) -> RecloserAction:
        """
    DSS property name: Action
    DSS property index: 18
    """
        return RecloserAction(self._lib.Obj_GetInt32(self._ptr, 18))

    @Action.setter
    def Action(self, value: Union[AnyStr, int, RecloserAction]):
        if not isinstance(value, int):
            self._set_string(18, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 18, value)

    @property
    def Action_str(self) -> str:
        """
        DSS property name: Action
        DSS property index: 18
        """
        return self._get_prop_string(18)

    @Action_str.setter
    def Action_str(self, value: AnyStr):
        self.Action = value

    @property
    def TDPhFast(self) -> float:
        """
        DSS property name: TDPhFast
        DSS property index: 19
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    @TDPhFast.setter
    def TDPhFast(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 19, value)

    @property
    def TDGrFast(self) -> float:
        """
        DSS property name: TDGrFast
        DSS property index: 20
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    @TDGrFast.setter
    def TDGrFast(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 20, value)

    @property
    def TDPhDelayed(self) -> float:
        """
        DSS property name: TDPhDelayed
        DSS property index: 21
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @TDPhDelayed.setter
    def TDPhDelayed(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    @property
    def TDGrDelayed(self) -> float:
        """
        DSS property name: TDGrDelayed
        DSS property index: 22
        """
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    @TDGrDelayed.setter
    def TDGrDelayed(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 22, value)

    @property
    def Normal(self) -> RecloserState:
        """
    DSS property name: Normal
    DSS property index: 23
    """
        return RecloserState(self._lib.Obj_GetInt32(self._ptr, 23))

    @Normal.setter
    def Normal(self, value: Union[AnyStr, int, RecloserState]):
        if not isinstance(value, int):
            self._set_string(23, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 23, value)

    @property
    def Normal_str(self) -> str:
        """
        DSS property name: Normal
        DSS property index: 23
        """
        return self._get_prop_string(23)

    @Normal_str.setter
    def Normal_str(self, value: AnyStr):
        self.Normal = value

    @property
    def State(self) -> RecloserState:
        """
    DSS property name: State
    DSS property index: 24
    """
        return RecloserState(self._lib.Obj_GetInt32(self._ptr, 24))

    @State.setter
    def State(self, value: Union[AnyStr, int, RecloserState]):
        if not isinstance(value, int):
            self._set_string(24, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 24, value)

    @property
    def State_str(self) -> str:
        """
        DSS property name: State
        DSS property index: 24
        """
        return self._get_prop_string(24)

    @State_str.setter
    def State_str(self, value: AnyStr):
        self.State = value

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 25
        """
        return self._lib.Obj_GetFloat64(self._ptr, 25)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 25, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 26
        """
        return self._lib.Obj_GetInt32(self._ptr, 26) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 26, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 27
        """
        self._set_string(27, value)

class Fuse(DSSObj):
    _cls_name = 'Fuse'
    _cls_idx = 32
    _cls_prop_idx = {
        'monitoredobj': 1,
        'monitoredterm': 2,
        'switchedobj': 3,
        'switchedterm': 4,
        'fusecurve': 5,
        'ratedcurrent': 6,
        'delay': 7,
        'action': 8,
        'normal': 9,
        'state': 10,
        'basefreq': 11,
        'enabled': 12,
        'like': 13,
    }

    # Class-specific enumerations
    class FuseAction(IntEnum):
        """Fuse: Action (DSS enumeration for Fuse)"""
        close = 2 # close
        open = 1 # open

    class FuseState(IntEnum):
        """Fuse: State (DSS enumeration for Fuse)"""
        closed = 2 # closed
        open = 1 # open


    @property
    def MonitoredObj(self) -> str:
        """
        DSS property name: MonitoredObj
        DSS property index: 1
        """
        return self._get_prop_string(1)

    @MonitoredObj.setter
    def MonitoredObj(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_obj(1, value)
            return

        self._set_string(1, value)

    @property
    def MonitoredObj_obj(self) -> DSSObj:
        """
        DSS property name: MonitoredObj
        DSS property index: 1
        """
        return self._get_obj(1, None)

    @MonitoredObj_obj.setter
    def MonitoredObj_obj(self, value: DSSObj):
        self._set_obj(1, value)

    @property
    def MonitoredTerm(self) -> int:
        """
        DSS property name: MonitoredTerm
        DSS property index: 2
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @MonitoredTerm.setter
    def MonitoredTerm(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def SwitchedObj(self) -> str:
        """
        DSS property name: SwitchedObj
        DSS property index: 3
        """
        return self._get_prop_string(3)

    @SwitchedObj.setter
    def SwitchedObj(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_obj(3, value)
            return

        self._set_string(3, value)

    @property
    def SwitchedObj_obj(self) -> DSSObj:
        """
        DSS property name: SwitchedObj
        DSS property index: 3
        """
        return self._get_obj(3, None)

    @SwitchedObj_obj.setter
    def SwitchedObj_obj(self, value: DSSObj):
        self._set_obj(3, value)

    @property
    def SwitchedTerm(self) -> int:
        """
        DSS property name: SwitchedTerm
        DSS property index: 4
        """
        return self._lib.Obj_GetInt32(self._ptr, 4)

    @SwitchedTerm.setter
    def SwitchedTerm(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 4, value)

    @property
    def FuseCurve(self) -> str:
        """
        DSS property name: FuseCurve
        DSS property index: 5
        """
        return self._get_prop_string(5)

    @FuseCurve.setter
    def FuseCurve(self, value: Union[AnyStr, TCC_Curve]):
        if isinstance(value, DSSObj):
            self._set_obj(5, value)
            return

        self._set_string(5, value)

    @property
    def FuseCurve_obj(self) -> TCC_Curve:
        """
        DSS property name: FuseCurve
        DSS property index: 5
        """
        return self._get_obj(5, TCC_Curve)

    @FuseCurve_obj.setter
    def FuseCurve_obj(self, value: TCC_Curve):
        self._set_obj(5, value)

    @property
    def RatedCurrent(self) -> float:
        """
        DSS property name: RatedCurrent
        DSS property index: 6
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    @RatedCurrent.setter
    def RatedCurrent(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 6, value)

    @property
    def Delay(self) -> float:
        """
        DSS property name: Delay
        DSS property index: 7
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @Delay.setter
    def Delay(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    def Action(self, value: Union[str, bytes, int, FuseAction]):
        """
        DSS property name: Action
        DSS property index: 8
        """
        if isinstance(value, int):
            self._lib.Obj_SetInt32(self._ptr, 8, value)
            return

        self._set_string(8, value)

    @property
    def Normal(self) -> List[FuseState]:
        """
        DSS property name: Normal
        DSS property index: 9
        """
        return [FuseState(val) for val in self._get_int32_list(self._lib.Obj_GetInt32Array, self._ptr, 9)]

    @Normal.setter
    def Normal(self, value: Union[List[Union[int,FuseState]], List[AnyStr]]):
        if not isinstance(value, int):
            self._set_string_array(9, value)
            return    
        self._set_int32_array(9, value)

    @property
    def Normal_str(self) -> List[str]:
        """
        DSS property name: Normal
        DSS property index: 9
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 9)

    @Normal_str.setter
    def Normal_str(self, value: AnyStr):
        self.Normal = value

    @property
    def State(self) -> List[FuseState]:
        """
        DSS property name: State
        DSS property index: 10
        """
        return [FuseState(val) for val in self._get_int32_list(self._lib.Obj_GetInt32Array, self._ptr, 10)]

    @State.setter
    def State(self, value: Union[List[Union[int,FuseState]], List[AnyStr]]):
        if not isinstance(value, int):
            self._set_string_array(10, value)
            return    
        self._set_int32_array(10, value)

    @property
    def State_str(self) -> List[str]:
        """
        DSS property name: State
        DSS property index: 10
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 10)

    @State_str.setter
    def State_str(self, value: AnyStr):
        self.State = value

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 11
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 12
        """
        return self._lib.Obj_GetInt32(self._ptr, 12) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 12, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 13
        """
        self._set_string(13, value)

class SwtControl(DSSObj):
    _cls_name = 'SwtControl'
    _cls_idx = 33
    _cls_prop_idx = {
        'switchedobj': 1,
        'switchedterm': 2,
        'action': 3,
        'lock': 4,
        'delay': 5,
        'normal': 6,
        'state': 7,
        'reset': 8,
        'basefreq': 9,
        'enabled': 10,
        'like': 11,
    }

    # Class-specific enumerations
    class SwtControlAction(IntEnum):
        """SwtControl: Action (DSS enumeration for SwtControl)"""
        close = 2 # close
        open = 1 # open

    class SwtControlState(IntEnum):
        """SwtControl: State (DSS enumeration for SwtControl)"""
        closed = 2 # closed
        open = 1 # open


    @property
    def SwitchedObj(self) -> str:
        """
        DSS property name: SwitchedObj
        DSS property index: 1
        """
        return self._get_prop_string(1)

    @SwitchedObj.setter
    def SwitchedObj(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_obj(1, value)
            return

        self._set_string(1, value)

    @property
    def SwitchedObj_obj(self) -> DSSObj:
        """
        DSS property name: SwitchedObj
        DSS property index: 1
        """
        return self._get_obj(1, None)

    @SwitchedObj_obj.setter
    def SwitchedObj_obj(self, value: DSSObj):
        self._set_obj(1, value)

    @property
    def SwitchedTerm(self) -> int:
        """
        DSS property name: SwitchedTerm
        DSS property index: 2
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @SwitchedTerm.setter
    def SwitchedTerm(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def Action(self) -> SwtControlAction:
        """
    DSS property name: Action
    DSS property index: 3
    """
        return SwtControlAction(self._lib.Obj_GetInt32(self._ptr, 3))

    @Action.setter
    def Action(self, value: Union[AnyStr, int, SwtControlAction]):
        if not isinstance(value, int):
            self._set_string(3, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 3, value)

    @property
    def Action_str(self) -> str:
        """
        DSS property name: Action
        DSS property index: 3
        """
        return self._get_prop_string(3)

    @Action_str.setter
    def Action_str(self, value: AnyStr):
        self.Action = value

    @property
    def Lock(self) -> bool:
        """
        DSS property name: Lock
        DSS property index: 4
        """
        return self._lib.Obj_GetInt32(self._ptr, 4) != 0

    @Lock.setter
    def Lock(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 4, value)

    @property
    def Delay(self) -> float:
        """
        DSS property name: Delay
        DSS property index: 5
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @Delay.setter
    def Delay(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def Normal(self) -> SwtControlState:
        """
    DSS property name: Normal
    DSS property index: 6
    """
        return SwtControlState(self._lib.Obj_GetInt32(self._ptr, 6))

    @Normal.setter
    def Normal(self, value: Union[AnyStr, int, SwtControlState]):
        if not isinstance(value, int):
            self._set_string(6, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 6, value)

    @property
    def Normal_str(self) -> str:
        """
        DSS property name: Normal
        DSS property index: 6
        """
        return self._get_prop_string(6)

    @Normal_str.setter
    def Normal_str(self, value: AnyStr):
        self.Normal = value

    @property
    def State(self) -> SwtControlState:
        """
    DSS property name: State
    DSS property index: 7
    """
        return SwtControlState(self._lib.Obj_GetInt32(self._ptr, 7))

    @State.setter
    def State(self, value: Union[AnyStr, int, SwtControlState]):
        if not isinstance(value, int):
            self._set_string(7, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 7, value)

    @property
    def State_str(self) -> str:
        """
        DSS property name: State
        DSS property index: 7
        """
        return self._get_prop_string(7)

    @State_str.setter
    def State_str(self, value: AnyStr):
        self.State = value

    def Reset(self, value: bool):
        """
        DSS property name: Reset
        DSS property index: 8
        """
        self._lib.Obj_SetInt32(self._ptr, 8, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 9
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 10
        """
        return self._lib.Obj_GetInt32(self._ptr, 10) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 10, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 11
        """
        self._set_string(11, value)

class PVSystem(DSSObj):
    _cls_name = 'PVSystem'
    _cls_idx = 34
    _cls_prop_idx = {
        'phases': 1,
        'bus1': 2,
        'kv': 3,
        'irradiance': 4,
        'pmpp': 5,
        'pctpmpp': 6,
        '%pmpp': 6,
        'temperature': 7,
        'pf': 8,
        'conn': 9,
        'kvar': 10,
        'kva': 11,
        'pctcutin': 12,
        '%cutin': 12,
        'pctcutout': 13,
        '%cutout': 13,
        'effcurve': 14,
        'ptcurve': 15,
        'p-tcurve': 15,
        'pctr': 16,
        '%r': 16,
        'pctx': 17,
        '%x': 17,
        'model': 18,
        'vminpu': 19,
        'vmaxpu': 20,
        'balanced': 21,
        'limitcurrent': 22,
        'yearly': 23,
        'daily': 24,
        'duty': 25,
        'tyearly': 26,
        'tdaily': 27,
        'tduty': 28,
        'cls': 29,
        'class': 29,
        'usermodel': 30,
        'userdata': 31,
        'debugtrace': 32,
        'varfollowinverter': 33,
        'dutystart': 34,
        'wattpriority': 35,
        'pfpriority': 36,
        'pctpminnovars': 37,
        '%pminnovars': 37,
        'pctpminkvarmax': 38,
        '%pminkvarmax': 38,
        'kvarmax': 39,
        'kvarmaxabs': 40,
        'spectrum': 41,
        'basefreq': 42,
        'enabled': 43,
        'like': 44,
    }

    @property
    def phases(self) -> int:
        """
        DSS property name: phases
        DSS property index: 1
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @phases.setter
    def phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def bus1(self) -> str:
        """
        DSS property name: bus1
        DSS property index: 2
        """
        return self._get_prop_string(2)

    @bus1.setter
    def bus1(self, value: AnyStr):
        self._set_string(2, value)

    @property
    def kv(self) -> float:
        """
        DSS property name: kv
        DSS property index: 3
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @kv.setter
    def kv(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def irradiance(self) -> float:
        """
        DSS property name: irradiance
        DSS property index: 4
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @irradiance.setter
    def irradiance(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def Pmpp(self) -> float:
        """
        DSS property name: Pmpp
        DSS property index: 5
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @Pmpp.setter
    def Pmpp(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def pctPmpp(self) -> float:
        """
        DSS property name: %Pmpp
        DSS property index: 6
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    @pctPmpp.setter
    def pctPmpp(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 6, value)

    @property
    def Temperature(self) -> float:
        """
        DSS property name: Temperature
        DSS property index: 7
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @Temperature.setter
    def Temperature(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def pf(self) -> float:
        """
        DSS property name: pf
        DSS property index: 8
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @pf.setter
    def pf(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def conn(self) -> Connection:
        """
    DSS property name: conn
    DSS property index: 9
    """
        return Connection(self._lib.Obj_GetInt32(self._ptr, 9))

    @conn.setter
    def conn(self, value: Union[AnyStr, int, Connection]):
        if not isinstance(value, int):
            self._set_string(9, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 9, value)

    @property
    def conn_str(self) -> str:
        """
        DSS property name: conn
        DSS property index: 9
        """
        return self._get_prop_string(9)

    @conn_str.setter
    def conn_str(self, value: AnyStr):
        self.conn = value

    @property
    def kvar(self) -> float:
        """
        DSS property name: kvar
        DSS property index: 10
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @kvar.setter
    def kvar(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def kVA(self) -> float:
        """
        DSS property name: kVA
        DSS property index: 11
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @kVA.setter
    def kVA(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def pctCutin(self) -> float:
        """
        DSS property name: %Cutin
        DSS property index: 12
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @pctCutin.setter
    def pctCutin(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def pctCutout(self) -> float:
        """
        DSS property name: %Cutout
        DSS property index: 13
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @pctCutout.setter
    def pctCutout(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def EffCurve(self) -> str:
        """
        DSS property name: EffCurve
        DSS property index: 14
        """
        return self._get_prop_string(14)

    @EffCurve.setter
    def EffCurve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(14, value)
            return

        self._set_string(14, value)

    @property
    def EffCurve_obj(self) -> XYcurve:
        """
        DSS property name: EffCurve
        DSS property index: 14
        """
        return self._get_obj(14, XYcurve)

    @EffCurve_obj.setter
    def EffCurve_obj(self, value: XYcurve):
        self._set_obj(14, value)

    @property
    def PTCurve(self) -> str:
        """
        DSS property name: P-TCurve
        DSS property index: 15
        """
        return self._get_prop_string(15)

    @PTCurve.setter
    def PTCurve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(15, value)
            return

        self._set_string(15, value)

    @property
    def PTCurve_obj(self) -> XYcurve:
        """
        DSS property name: P-TCurve
        DSS property index: 15
        """
        return self._get_obj(15, XYcurve)

    @PTCurve_obj.setter
    def PTCurve_obj(self, value: XYcurve):
        self._set_obj(15, value)

    @property
    def pctR(self) -> float:
        """
        DSS property name: %R
        DSS property index: 16
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    @pctR.setter
    def pctR(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 16, value)

    @property
    def pctX(self) -> float:
        """
        DSS property name: %X
        DSS property index: 17
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    @pctX.setter
    def pctX(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 17, value)

    @property
    def model(self) -> int:
        """
        DSS property name: model
        DSS property index: 18
        """
        return self._lib.Obj_GetInt32(self._ptr, 18)

    @model.setter
    def model(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 18, value)

    @property
    def Vminpu(self) -> float:
        """
        DSS property name: Vminpu
        DSS property index: 19
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    @Vminpu.setter
    def Vminpu(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 19, value)

    @property
    def Vmaxpu(self) -> float:
        """
        DSS property name: Vmaxpu
        DSS property index: 20
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    @Vmaxpu.setter
    def Vmaxpu(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 20, value)

    @property
    def Balanced(self) -> bool:
        """
        DSS property name: Balanced
        DSS property index: 21
        """
        return self._lib.Obj_GetInt32(self._ptr, 21) != 0

    @Balanced.setter
    def Balanced(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 21, value)

    @property
    def LimitCurrent(self) -> bool:
        """
        DSS property name: LimitCurrent
        DSS property index: 22
        """
        return self._lib.Obj_GetInt32(self._ptr, 22) != 0

    @LimitCurrent.setter
    def LimitCurrent(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 22, value)

    @property
    def yearly(self) -> str:
        """
        DSS property name: yearly
        DSS property index: 23
        """
        return self._get_prop_string(23)

    @yearly.setter
    def yearly(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(23, value)
            return

        self._set_string(23, value)

    @property
    def yearly_obj(self) -> LoadShape:
        """
        DSS property name: yearly
        DSS property index: 23
        """
        return self._get_obj(23, LoadShape)

    @yearly_obj.setter
    def yearly_obj(self, value: LoadShape):
        self._set_obj(23, value)

    @property
    def daily(self) -> str:
        """
        DSS property name: daily
        DSS property index: 24
        """
        return self._get_prop_string(24)

    @daily.setter
    def daily(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(24, value)
            return

        self._set_string(24, value)

    @property
    def daily_obj(self) -> LoadShape:
        """
        DSS property name: daily
        DSS property index: 24
        """
        return self._get_obj(24, LoadShape)

    @daily_obj.setter
    def daily_obj(self, value: LoadShape):
        self._set_obj(24, value)

    @property
    def duty(self) -> str:
        """
        DSS property name: duty
        DSS property index: 25
        """
        return self._get_prop_string(25)

    @duty.setter
    def duty(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(25, value)
            return

        self._set_string(25, value)

    @property
    def duty_obj(self) -> LoadShape:
        """
        DSS property name: duty
        DSS property index: 25
        """
        return self._get_obj(25, LoadShape)

    @duty_obj.setter
    def duty_obj(self, value: LoadShape):
        self._set_obj(25, value)

    @property
    def Tyearly(self) -> str:
        """
        DSS property name: Tyearly
        DSS property index: 26
        """
        return self._get_prop_string(26)

    @Tyearly.setter
    def Tyearly(self, value: Union[AnyStr, TShape]):
        if isinstance(value, DSSObj):
            self._set_obj(26, value)
            return

        self._set_string(26, value)

    @property
    def Tyearly_obj(self) -> TShape:
        """
        DSS property name: Tyearly
        DSS property index: 26
        """
        return self._get_obj(26, TShape)

    @Tyearly_obj.setter
    def Tyearly_obj(self, value: TShape):
        self._set_obj(26, value)

    @property
    def Tdaily(self) -> str:
        """
        DSS property name: Tdaily
        DSS property index: 27
        """
        return self._get_prop_string(27)

    @Tdaily.setter
    def Tdaily(self, value: Union[AnyStr, TShape]):
        if isinstance(value, DSSObj):
            self._set_obj(27, value)
            return

        self._set_string(27, value)

    @property
    def Tdaily_obj(self) -> TShape:
        """
        DSS property name: Tdaily
        DSS property index: 27
        """
        return self._get_obj(27, TShape)

    @Tdaily_obj.setter
    def Tdaily_obj(self, value: TShape):
        self._set_obj(27, value)

    @property
    def Tduty(self) -> str:
        """
        DSS property name: Tduty
        DSS property index: 28
        """
        return self._get_prop_string(28)

    @Tduty.setter
    def Tduty(self, value: Union[AnyStr, TShape]):
        if isinstance(value, DSSObj):
            self._set_obj(28, value)
            return

        self._set_string(28, value)

    @property
    def Tduty_obj(self) -> TShape:
        """
        DSS property name: Tduty
        DSS property index: 28
        """
        return self._get_obj(28, TShape)

    @Tduty_obj.setter
    def Tduty_obj(self, value: TShape):
        self._set_obj(28, value)

    @property
    def cls(self) -> int:
        """
        DSS property name: class
        DSS property index: 29
        """
        return self._lib.Obj_GetInt32(self._ptr, 29)

    @cls.setter
    def cls(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 29, value)

    @property
    def UserModel(self) -> str:
        """
        DSS property name: UserModel
        DSS property index: 30
        """
        return self._get_prop_string(30)

    @UserModel.setter
    def UserModel(self, value: AnyStr):
        self._set_string(30, value)

    @property
    def UserData(self) -> str:
        """
        DSS property name: UserData
        DSS property index: 31
        """
        return self._get_prop_string(31)

    @UserData.setter
    def UserData(self, value: AnyStr):
        self._set_string(31, value)

    @property
    def debugtrace(self) -> bool:
        """
        DSS property name: debugtrace
        DSS property index: 32
        """
        return self._lib.Obj_GetInt32(self._ptr, 32) != 0

    @debugtrace.setter
    def debugtrace(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 32, value)

    @property
    def VarFollowInverter(self) -> bool:
        """
        DSS property name: VarFollowInverter
        DSS property index: 33
        """
        return self._lib.Obj_GetInt32(self._ptr, 33) != 0

    @VarFollowInverter.setter
    def VarFollowInverter(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 33, value)

    @property
    def DutyStart(self) -> float:
        """
        DSS property name: DutyStart
        DSS property index: 34
        """
        return self._lib.Obj_GetFloat64(self._ptr, 34)

    @DutyStart.setter
    def DutyStart(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 34, value)

    @property
    def WattPriority(self) -> bool:
        """
        DSS property name: WattPriority
        DSS property index: 35
        """
        return self._lib.Obj_GetInt32(self._ptr, 35) != 0

    @WattPriority.setter
    def WattPriority(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 35, value)

    @property
    def PFPriority(self) -> bool:
        """
        DSS property name: PFPriority
        DSS property index: 36
        """
        return self._lib.Obj_GetInt32(self._ptr, 36) != 0

    @PFPriority.setter
    def PFPriority(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 36, value)

    @property
    def pctPminNoVars(self) -> float:
        """
        DSS property name: %PminNoVars
        DSS property index: 37
        """
        return self._lib.Obj_GetFloat64(self._ptr, 37)

    @pctPminNoVars.setter
    def pctPminNoVars(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 37, value)

    @property
    def pctPminkvarMax(self) -> float:
        """
        DSS property name: %PminkvarMax
        DSS property index: 38
        """
        return self._lib.Obj_GetFloat64(self._ptr, 38)

    @pctPminkvarMax.setter
    def pctPminkvarMax(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 38, value)

    @property
    def kvarMax(self) -> float:
        """
        DSS property name: kvarMax
        DSS property index: 39
        """
        return self._lib.Obj_GetFloat64(self._ptr, 39)

    @kvarMax.setter
    def kvarMax(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 39, value)

    @property
    def kvarMaxAbs(self) -> float:
        """
        DSS property name: kvarMaxAbs
        DSS property index: 40
        """
        return self._lib.Obj_GetFloat64(self._ptr, 40)

    @kvarMaxAbs.setter
    def kvarMaxAbs(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 40, value)

    @property
    def spectrum(self) -> str:
        """
        DSS property name: spectrum
        DSS property index: 41
        """
        return self._get_prop_string(41)

    @spectrum.setter
    def spectrum(self, value: Union[AnyStr, Spectrum]):
        if isinstance(value, DSSObj):
            self._set_obj(41, value)
            return

        self._set_string(41, value)

    @property
    def spectrum_obj(self) -> Spectrum:
        """
        DSS property name: spectrum
        DSS property index: 41
        """
        return self._get_obj(41, Spectrum)

    @spectrum_obj.setter
    def spectrum_obj(self, value: Spectrum):
        self._set_obj(41, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 42
        """
        return self._lib.Obj_GetFloat64(self._ptr, 42)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 42, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 43
        """
        return self._lib.Obj_GetInt32(self._ptr, 43) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 43, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 44
        """
        self._set_string(44, value)

class UPFC(DSSObj):
    _cls_name = 'UPFC'
    _cls_idx = 35
    _cls_prop_idx = {
        'bus1': 1,
        'bus2': 2,
        'refkv': 3,
        'pf': 4,
        'frequency': 5,
        'phases': 6,
        'xs': 7,
        'tol1': 8,
        'mode': 9,
        'vpqmax': 10,
        'losscurve': 11,
        'vhlimit': 12,
        'vllimit': 13,
        'climit': 14,
        'refkv2': 15,
        'kvarlimit': 16,
        'spectrum': 17,
        'basefreq': 18,
        'enabled': 19,
        'like': 20,
    }

    @property
    def bus1(self) -> str:
        """
        DSS property name: bus1
        DSS property index: 1
        """
        return self._get_prop_string(1)

    @bus1.setter
    def bus1(self, value: AnyStr):
        self._set_string(1, value)

    @property
    def bus2(self) -> str:
        """
        DSS property name: bus2
        DSS property index: 2
        """
        return self._get_prop_string(2)

    @bus2.setter
    def bus2(self, value: AnyStr):
        self._set_string(2, value)

    @property
    def refkv(self) -> float:
        """
        DSS property name: refkv
        DSS property index: 3
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @refkv.setter
    def refkv(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def pf(self) -> float:
        """
        DSS property name: pf
        DSS property index: 4
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @pf.setter
    def pf(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def frequency(self) -> float:
        """
        DSS property name: frequency
        DSS property index: 5
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @frequency.setter
    def frequency(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def phases(self) -> int:
        """
        DSS property name: phases
        DSS property index: 6
        """
        return self._lib.Obj_GetInt32(self._ptr, 6)

    @phases.setter
    def phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 6, value)

    @property
    def Xs(self) -> float:
        """
        DSS property name: Xs
        DSS property index: 7
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @Xs.setter
    def Xs(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def Tol1(self) -> float:
        """
        DSS property name: Tol1
        DSS property index: 8
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @Tol1.setter
    def Tol1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def Mode(self) -> int:
        """
        DSS property name: Mode
        DSS property index: 9
        """
        return self._lib.Obj_GetInt32(self._ptr, 9)

    @Mode.setter
    def Mode(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 9, value)

    @property
    def VpqMax(self) -> float:
        """
        DSS property name: VpqMax
        DSS property index: 10
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @VpqMax.setter
    def VpqMax(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def LossCurve(self) -> str:
        """
        DSS property name: LossCurve
        DSS property index: 11
        """
        return self._get_prop_string(11)

    @LossCurve.setter
    def LossCurve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(11, value)
            return

        self._set_string(11, value)

    @property
    def LossCurve_obj(self) -> XYcurve:
        """
        DSS property name: LossCurve
        DSS property index: 11
        """
        return self._get_obj(11, XYcurve)

    @LossCurve_obj.setter
    def LossCurve_obj(self, value: XYcurve):
        self._set_obj(11, value)

    @property
    def VHLimit(self) -> float:
        """
        DSS property name: VHLimit
        DSS property index: 12
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @VHLimit.setter
    def VHLimit(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def VLLimit(self) -> float:
        """
        DSS property name: VLLimit
        DSS property index: 13
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @VLLimit.setter
    def VLLimit(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def CLimit(self) -> float:
        """
        DSS property name: CLimit
        DSS property index: 14
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @CLimit.setter
    def CLimit(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def refkv2(self) -> float:
        """
        DSS property name: refkv2
        DSS property index: 15
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @refkv2.setter
    def refkv2(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def kvarLimit(self) -> float:
        """
        DSS property name: kvarLimit
        DSS property index: 16
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    @kvarLimit.setter
    def kvarLimit(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 16, value)

    @property
    def spectrum(self) -> str:
        """
        DSS property name: spectrum
        DSS property index: 17
        """
        return self._get_prop_string(17)

    @spectrum.setter
    def spectrum(self, value: Union[AnyStr, Spectrum]):
        if isinstance(value, DSSObj):
            self._set_obj(17, value)
            return

        self._set_string(17, value)

    @property
    def spectrum_obj(self) -> Spectrum:
        """
        DSS property name: spectrum
        DSS property index: 17
        """
        return self._get_obj(17, Spectrum)

    @spectrum_obj.setter
    def spectrum_obj(self, value: Spectrum):
        self._set_obj(17, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 18
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 18, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 19
        """
        return self._lib.Obj_GetInt32(self._ptr, 19) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 19, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 20
        """
        self._set_string(20, value)

class UPFCControl(DSSObj):
    _cls_name = 'UPFCControl'
    _cls_idx = 36
    _cls_prop_idx = {
        'upfclist': 1,
        'basefreq': 2,
        'enabled': 3,
        'like': 4,
    }

    @property
    def UPFCList(self) -> List[str]:
        """
        DSS property name: UPFCList
        DSS property index: 1
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 1)

    @UPFCList.setter
    def UPFCList(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 1, value_ptr, value_count)
        self._check_for_error()

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 2
        """
        return self._lib.Obj_GetFloat64(self._ptr, 2)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 2, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 3
        """
        return self._lib.Obj_GetInt32(self._ptr, 3) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 3, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 4
        """
        self._set_string(4, value)

class ESPVLControl(DSSObj):
    _cls_name = 'ESPVLControl'
    _cls_idx = 37
    _cls_prop_idx = {
        'element': 1,
        'terminal': 2,
        'type': 3,
        'kwband': 4,
        'kvarlimit': 5,
        'localcontrollist': 6,
        'localcontrolweights': 7,
        'pvsystemlist': 8,
        'pvsystemweights': 9,
        'storagelist': 10,
        'storageweights': 11,
        'basefreq': 12,
        'enabled': 13,
        'like': 14,
    }

    # Class-specific enumerations
    class ESPVLControlType(IntEnum):
        """ESPVLControl: Type (DSS enumeration for ESPVLControl)"""
        SystemController = 1 # SystemController
        LocalController = 2 # LocalController


    @property
    def Element(self) -> str:
        """
        DSS property name: Element
        DSS property index: 1
        """
        return self._get_prop_string(1)

    @Element.setter
    def Element(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_obj(1, value)
            return

        self._set_string(1, value)

    @property
    def Element_obj(self) -> DSSObj:
        """
        DSS property name: Element
        DSS property index: 1
        """
        return self._get_obj(1, None)

    @Element_obj.setter
    def Element_obj(self, value: DSSObj):
        self._set_obj(1, value)

    @property
    def Terminal(self) -> int:
        """
        DSS property name: Terminal
        DSS property index: 2
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @Terminal.setter
    def Terminal(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def Type(self) -> ESPVLControlType:
        """
    DSS property name: Type
    DSS property index: 3
    """
        return ESPVLControlType(self._lib.Obj_GetInt32(self._ptr, 3))

    @Type.setter
    def Type(self, value: Union[AnyStr, int, ESPVLControlType]):
        if not isinstance(value, int):
            self._set_string(3, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 3, value)

    @property
    def Type_str(self) -> str:
        """
        DSS property name: Type
        DSS property index: 3
        """
        return self._get_prop_string(3)

    @Type_str.setter
    def Type_str(self, value: AnyStr):
        self.Type = value

    @property
    def kWBand(self) -> float:
        """
        DSS property name: kWBand
        DSS property index: 4
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @kWBand.setter
    def kWBand(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def kvarlimit(self) -> float:
        """
        DSS property name: kvarlimit
        DSS property index: 5
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @kvarlimit.setter
    def kvarlimit(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def LocalControlList(self) -> List[str]:
        """
        DSS property name: LocalControlList
        DSS property index: 6
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 6)

    @LocalControlList.setter
    def LocalControlList(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 6, value_ptr, value_count)
        self._check_for_error()

    @property
    def LocalControlWeights(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: LocalControlWeights
        DSS property index: 7
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 7)

    @LocalControlWeights.setter
    def LocalControlWeights(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(7, value)

    @property
    def PVSystemList(self) -> List[str]:
        """
        DSS property name: PVSystemList
        DSS property index: 8
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 8)

    @PVSystemList.setter
    def PVSystemList(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 8, value_ptr, value_count)
        self._check_for_error()

    @property
    def PVSystemWeights(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: PVSystemWeights
        DSS property index: 9
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 9)

    @PVSystemWeights.setter
    def PVSystemWeights(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(9, value)

    @property
    def StorageList(self) -> List[str]:
        """
        DSS property name: StorageList
        DSS property index: 10
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 10)

    @StorageList.setter
    def StorageList(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 10, value_ptr, value_count)
        self._check_for_error()

    @property
    def StorageWeights(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: StorageWeights
        DSS property index: 11
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 11)

    @StorageWeights.setter
    def StorageWeights(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(11, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 12
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 13
        """
        return self._lib.Obj_GetInt32(self._ptr, 13) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 13, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 14
        """
        self._set_string(14, value)

class IndMach012(DSSObj):
    _cls_name = 'IndMach012'
    _cls_idx = 38
    _cls_prop_idx = {
        'phases': 1,
        'bus1': 2,
        'kv': 3,
        'kw': 4,
        'pf': 5,
        'conn': 6,
        'kva': 7,
        'h': 8,
        'd': 9,
        'purs': 10,
        'puxs': 11,
        'purr': 12,
        'puxr': 13,
        'puxm': 14,
        'slip': 15,
        'maxslip': 16,
        'slipoption': 17,
        'yearly': 18,
        'daily': 19,
        'duty': 20,
        'debugtrace': 21,
        'spectrum': 22,
        'basefreq': 23,
        'enabled': 24,
        'like': 25,
    }

    # Class-specific enumerations
    class IndMach012SlipOption(IntEnum):
        """IndMach012: Slip Option (DSS enumeration for IndMach012)"""
        VariableSlip = 0 # VariableSlip
        FixedSlip = 1 # FixedSlip


    @property
    def phases(self) -> int:
        """
        DSS property name: phases
        DSS property index: 1
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @phases.setter
    def phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def bus1(self) -> str:
        """
        DSS property name: bus1
        DSS property index: 2
        """
        return self._get_prop_string(2)

    @bus1.setter
    def bus1(self, value: AnyStr):
        self._set_string(2, value)

    @property
    def kv(self) -> float:
        """
        DSS property name: kv
        DSS property index: 3
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @kv.setter
    def kv(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def kW(self) -> float:
        """
        DSS property name: kW
        DSS property index: 4
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @kW.setter
    def kW(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def pf(self) -> float:
        """
        DSS property name: pf
        DSS property index: 5
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @pf.setter
    def pf(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def conn(self) -> Connection:
        """
    DSS property name: conn
    DSS property index: 6
    """
        return Connection(self._lib.Obj_GetInt32(self._ptr, 6))

    @conn.setter
    def conn(self, value: Union[AnyStr, int, Connection]):
        if not isinstance(value, int):
            self._set_string(6, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 6, value)

    @property
    def conn_str(self) -> str:
        """
        DSS property name: conn
        DSS property index: 6
        """
        return self._get_prop_string(6)

    @conn_str.setter
    def conn_str(self, value: AnyStr):
        self.conn = value

    @property
    def kVA(self) -> float:
        """
        DSS property name: kVA
        DSS property index: 7
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @kVA.setter
    def kVA(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def H(self) -> float:
        """
        DSS property name: H
        DSS property index: 8
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @H.setter
    def H(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def D(self) -> float:
        """
        DSS property name: D
        DSS property index: 9
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @D.setter
    def D(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def puRs(self) -> float:
        """
        DSS property name: puRs
        DSS property index: 10
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @puRs.setter
    def puRs(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def puXs(self) -> float:
        """
        DSS property name: puXs
        DSS property index: 11
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @puXs.setter
    def puXs(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def puRr(self) -> float:
        """
        DSS property name: puRr
        DSS property index: 12
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @puRr.setter
    def puRr(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def puXr(self) -> float:
        """
        DSS property name: puXr
        DSS property index: 13
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @puXr.setter
    def puXr(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def puXm(self) -> float:
        """
        DSS property name: puXm
        DSS property index: 14
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @puXm.setter
    def puXm(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def Slip(self) -> float:
        """
        DSS property name: Slip
        DSS property index: 15
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @Slip.setter
    def Slip(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def MaxSlip(self) -> float:
        """
        DSS property name: MaxSlip
        DSS property index: 16
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    @MaxSlip.setter
    def MaxSlip(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 16, value)

    @property
    def SlipOption(self) -> IndMach012SlipOption:
        """
    DSS property name: SlipOption
    DSS property index: 17
    """
        return IndMach012SlipOption(self._lib.Obj_GetInt32(self._ptr, 17))

    @SlipOption.setter
    def SlipOption(self, value: Union[AnyStr, int, IndMach012SlipOption]):
        if not isinstance(value, int):
            self._set_string(17, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 17, value)

    @property
    def SlipOption_str(self) -> str:
        """
        DSS property name: SlipOption
        DSS property index: 17
        """
        return self._get_prop_string(17)

    @SlipOption_str.setter
    def SlipOption_str(self, value: AnyStr):
        self.SlipOption = value

    @property
    def Yearly(self) -> str:
        """
        DSS property name: Yearly
        DSS property index: 18
        """
        return self._get_prop_string(18)

    @Yearly.setter
    def Yearly(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(18, value)
            return

        self._set_string(18, value)

    @property
    def Yearly_obj(self) -> LoadShape:
        """
        DSS property name: Yearly
        DSS property index: 18
        """
        return self._get_obj(18, LoadShape)

    @Yearly_obj.setter
    def Yearly_obj(self, value: LoadShape):
        self._set_obj(18, value)

    @property
    def Daily(self) -> str:
        """
        DSS property name: Daily
        DSS property index: 19
        """
        return self._get_prop_string(19)

    @Daily.setter
    def Daily(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(19, value)
            return

        self._set_string(19, value)

    @property
    def Daily_obj(self) -> LoadShape:
        """
        DSS property name: Daily
        DSS property index: 19
        """
        return self._get_obj(19, LoadShape)

    @Daily_obj.setter
    def Daily_obj(self, value: LoadShape):
        self._set_obj(19, value)

    @property
    def Duty(self) -> str:
        """
        DSS property name: Duty
        DSS property index: 20
        """
        return self._get_prop_string(20)

    @Duty.setter
    def Duty(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(20, value)
            return

        self._set_string(20, value)

    @property
    def Duty_obj(self) -> LoadShape:
        """
        DSS property name: Duty
        DSS property index: 20
        """
        return self._get_obj(20, LoadShape)

    @Duty_obj.setter
    def Duty_obj(self, value: LoadShape):
        self._set_obj(20, value)

    @property
    def Debugtrace(self) -> bool:
        """
        DSS property name: Debugtrace
        DSS property index: 21
        """
        return self._lib.Obj_GetInt32(self._ptr, 21) != 0

    @Debugtrace.setter
    def Debugtrace(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 21, value)

    @property
    def spectrum(self) -> str:
        """
        DSS property name: spectrum
        DSS property index: 22
        """
        return self._get_prop_string(22)

    @spectrum.setter
    def spectrum(self, value: Union[AnyStr, Spectrum]):
        if isinstance(value, DSSObj):
            self._set_obj(22, value)
            return

        self._set_string(22, value)

    @property
    def spectrum_obj(self) -> Spectrum:
        """
        DSS property name: spectrum
        DSS property index: 22
        """
        return self._get_obj(22, Spectrum)

    @spectrum_obj.setter
    def spectrum_obj(self, value: Spectrum):
        self._set_obj(22, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 23
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 23, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 24
        """
        return self._lib.Obj_GetInt32(self._ptr, 24) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 24, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 25
        """
        self._set_string(25, value)

class GICsource(DSSObj):
    _cls_name = 'GICsource'
    _cls_idx = 39
    _cls_prop_idx = {
        'volts': 1,
        'angle': 2,
        'frequency': 3,
        'phases': 4,
        'en': 5,
        'ee': 6,
        'lat1': 7,
        'lon1': 8,
        'lat2': 9,
        'lon2': 10,
        'spectrum': 11,
        'basefreq': 12,
        'enabled': 13,
        'like': 14,
    }

    @property
    def Volts(self) -> float:
        """
        DSS property name: Volts
        DSS property index: 1
        """
        return self._lib.Obj_GetFloat64(self._ptr, 1)

    @Volts.setter
    def Volts(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 1, value)

    @property
    def angle(self) -> float:
        """
        DSS property name: angle
        DSS property index: 2
        """
        return self._lib.Obj_GetFloat64(self._ptr, 2)

    @angle.setter
    def angle(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 2, value)

    @property
    def frequency(self) -> float:
        """
        DSS property name: frequency
        DSS property index: 3
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @frequency.setter
    def frequency(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def phases(self) -> int:
        """
        DSS property name: phases
        DSS property index: 4
        """
        return self._lib.Obj_GetInt32(self._ptr, 4)

    @phases.setter
    def phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 4, value)

    @property
    def EN(self) -> float:
        """
        DSS property name: EN
        DSS property index: 5
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @EN.setter
    def EN(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def EE(self) -> float:
        """
        DSS property name: EE
        DSS property index: 6
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    @EE.setter
    def EE(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 6, value)

    @property
    def Lat1(self) -> float:
        """
        DSS property name: Lat1
        DSS property index: 7
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @Lat1.setter
    def Lat1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def Lon1(self) -> float:
        """
        DSS property name: Lon1
        DSS property index: 8
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @Lon1.setter
    def Lon1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def Lat2(self) -> float:
        """
        DSS property name: Lat2
        DSS property index: 9
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @Lat2.setter
    def Lat2(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def Lon2(self) -> float:
        """
        DSS property name: Lon2
        DSS property index: 10
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @Lon2.setter
    def Lon2(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def spectrum(self) -> str:
        """
        DSS property name: spectrum
        DSS property index: 11
        """
        return self._get_prop_string(11)

    @spectrum.setter
    def spectrum(self, value: Union[AnyStr, Spectrum]):
        if isinstance(value, DSSObj):
            self._set_obj(11, value)
            return

        self._set_string(11, value)

    @property
    def spectrum_obj(self) -> Spectrum:
        """
        DSS property name: spectrum
        DSS property index: 11
        """
        return self._get_obj(11, Spectrum)

    @spectrum_obj.setter
    def spectrum_obj(self, value: Spectrum):
        self._set_obj(11, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 12
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 13
        """
        return self._lib.Obj_GetInt32(self._ptr, 13) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 13, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 14
        """
        self._set_string(14, value)

class AutoTrans(DSSObj):
    _cls_name = 'AutoTrans'
    _cls_idx = 40
    _cls_prop_idx = {
        'phases': 1,
        'windings': 2,
        'wdg': 3,
        'bus': 4,
        'conn': 5,
        'kv': 6,
        'kva': 7,
        'tap': 8,
        'pctr': 9,
        '%r': 9,
        'rdcohms': 10,
        'core': 11,
        'buses': 12,
        'conns': 13,
        'kvs': 14,
        'kvas': 15,
        'taps': 16,
        'xhx': 17,
        'xht': 18,
        'xxt': 19,
        'xscarray': 20,
        'thermal': 21,
        'n': 22,
        'm': 23,
        'flrise': 24,
        'hsrise': 25,
        'pctloadloss': 26,
        '%loadloss': 26,
        'pctnoloadloss': 27,
        '%noloadloss': 27,
        'normhkva': 28,
        'emerghkva': 29,
        'sub': 30,
        'maxtap': 31,
        'mintap': 32,
        'numtaps': 33,
        'subname': 34,
        'pctimag': 35,
        '%imag': 35,
        'ppm_antifloat': 36,
        'pctrs': 37,
        '%rs': 37,
        'xrconst': 38,
        'leadlag': 39,
        'wdgcurrents': 40,
        'normamps': 41,
        'emergamps': 42,
        'faultrate': 43,
        'pctperm': 44,
        'repair': 45,
        'basefreq': 46,
        'enabled': 47,
        'like': 48,
    }

    # Class-specific enumerations
    class AutoTransConnection(IntEnum):
        """AutoTrans: Connection (DSS enumeration for AutoTrans)"""
        wye = 0 # wye
        delta = 1 # delta
        series = 2 # series
        y = 0 # y
        ln = 0 # ln
        ll = 1 # ll


    @property
    def phases(self) -> int:
        """
        DSS property name: phases
        DSS property index: 1
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @phases.setter
    def phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def windings(self) -> int:
        """
        DSS property name: windings
        DSS property index: 2
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @windings.setter
    def windings(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def wdg(self) -> int:
        """
        DSS property name: wdg
        DSS property index: 3
        """
        return self._lib.Obj_GetInt32(self._ptr, 3)

    @wdg.setter
    def wdg(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 3, value)

    @property
    def bus(self) -> List[str]:
        """
        DSS property name: bus
        DSS property index: 4
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 4)

    @bus.setter
    def bus(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 4, value_ptr, value_count)
        self._check_for_error()

    @property
    def conn(self) -> List[AutoTransConnection]:
        """
        DSS property name: conn
        DSS property index: 5
        """
        return [AutoTransConnection(val) for val in self._get_int32_list(self._lib.Obj_GetInt32Array, self._ptr, 5)]

    @conn.setter
    def conn(self, value: Union[List[Union[int,AutoTransConnection]], List[AnyStr]]):
        if not isinstance(value, int):
            self._set_string_array(5, value)
            return    
        self._set_int32_array(5, value)

    @property
    def conn_str(self) -> List[str]:
        """
        DSS property name: conn
        DSS property index: 5
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 5)

    @conn_str.setter
    def conn_str(self, value: AnyStr):
        self.conn = value

    @property
    def kV(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: kV
        DSS property index: 6
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 6)

    @kV.setter
    def kV(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(6, value)

    @property
    def kVA(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: kVA
        DSS property index: 7
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 7)

    @kVA.setter
    def kVA(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(7, value)

    @property
    def tap(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: tap
        DSS property index: 8
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 8)

    @tap.setter
    def tap(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(8, value)

    @property
    def pctR(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: %R
        DSS property index: 9
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 9)

    @pctR.setter
    def pctR(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(9, value)

    @property
    def Rdcohms(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: Rdcohms
        DSS property index: 10
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 10)

    @Rdcohms.setter
    def Rdcohms(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(10, value)

    @property
    def Core(self) -> CoreType:
        """
    DSS property name: Core
    DSS property index: 11
    """
        return CoreType(self._lib.Obj_GetInt32(self._ptr, 11))

    @Core.setter
    def Core(self, value: Union[AnyStr, int, CoreType]):
        if not isinstance(value, int):
            self._set_string(11, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 11, value)

    @property
    def Core_str(self) -> str:
        """
        DSS property name: Core
        DSS property index: 11
        """
        return self._get_prop_string(11)

    @Core_str.setter
    def Core_str(self, value: AnyStr):
        self.Core = value

    @property
    def buses(self) -> List[str]:
        """
        DSS property name: buses
        DSS property index: 12
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 12)

    @buses.setter
    def buses(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 12, value_ptr, value_count)
        self._check_for_error()

    @property
    def conns(self) -> List[AutoTransConnection]:
        """
        DSS property name: conns
        DSS property index: 13
        """
        return [AutoTransConnection(val) for val in self._get_int32_list(self._lib.Obj_GetInt32Array, self._ptr, 13)]

    @conns.setter
    def conns(self, value: Union[List[Union[int,AutoTransConnection]], List[AnyStr]]):
        if not isinstance(value, int):
            self._set_string_array(13, value)
            return    
        self._set_int32_array(13, value)

    @property
    def conns_str(self) -> List[str]:
        """
        DSS property name: conns
        DSS property index: 13
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 13)

    @conns_str.setter
    def conns_str(self, value: AnyStr):
        self.conns = value

    @property
    def kVs(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: kVs
        DSS property index: 14
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 14)

    @kVs.setter
    def kVs(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(14, value)

    @property
    def kVAs(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: kVAs
        DSS property index: 15
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 15)

    @kVAs.setter
    def kVAs(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(15, value)

    @property
    def taps(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: taps
        DSS property index: 16
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 16)

    @taps.setter
    def taps(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(16, value)

    @property
    def XHX(self) -> float:
        """
        DSS property name: XHX
        DSS property index: 17
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    @XHX.setter
    def XHX(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 17, value)

    @property
    def XHT(self) -> float:
        """
        DSS property name: XHT
        DSS property index: 18
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    @XHT.setter
    def XHT(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 18, value)

    @property
    def XXT(self) -> float:
        """
        DSS property name: XXT
        DSS property index: 19
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    @XXT.setter
    def XXT(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 19, value)

    @property
    def XSCarray(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: XSCarray
        DSS property index: 20
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 20)

    @XSCarray.setter
    def XSCarray(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(20, value)

    @property
    def thermal(self) -> float:
        """
        DSS property name: thermal
        DSS property index: 21
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @thermal.setter
    def thermal(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    @property
    def n(self) -> float:
        """
        DSS property name: n
        DSS property index: 22
        """
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    @n.setter
    def n(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 22, value)

    @property
    def m(self) -> float:
        """
        DSS property name: m
        DSS property index: 23
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    @m.setter
    def m(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 23, value)

    @property
    def flrise(self) -> float:
        """
        DSS property name: flrise
        DSS property index: 24
        """
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    @flrise.setter
    def flrise(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 24, value)

    @property
    def hsrise(self) -> float:
        """
        DSS property name: hsrise
        DSS property index: 25
        """
        return self._lib.Obj_GetFloat64(self._ptr, 25)

    @hsrise.setter
    def hsrise(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 25, value)

    @property
    def pctloadloss(self) -> float:
        """
        DSS property name: %loadloss
        DSS property index: 26
        """
        return self._lib.Obj_GetFloat64(self._ptr, 26)

    @pctloadloss.setter
    def pctloadloss(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 26, value)

    @property
    def pctnoloadloss(self) -> float:
        """
        DSS property name: %noloadloss
        DSS property index: 27
        """
        return self._lib.Obj_GetFloat64(self._ptr, 27)

    @pctnoloadloss.setter
    def pctnoloadloss(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 27, value)

    @property
    def normhkVA(self) -> float:
        """
        DSS property name: normhkVA
        DSS property index: 28
        """
        return self._lib.Obj_GetFloat64(self._ptr, 28)

    @normhkVA.setter
    def normhkVA(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 28, value)

    @property
    def emerghkVA(self) -> float:
        """
        DSS property name: emerghkVA
        DSS property index: 29
        """
        return self._lib.Obj_GetFloat64(self._ptr, 29)

    @emerghkVA.setter
    def emerghkVA(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 29, value)

    @property
    def sub(self) -> bool:
        """
        DSS property name: sub
        DSS property index: 30
        """
        return self._lib.Obj_GetInt32(self._ptr, 30) != 0

    @sub.setter
    def sub(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 30, value)

    @property
    def MaxTap(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: MaxTap
        DSS property index: 31
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 31)

    @MaxTap.setter
    def MaxTap(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(31, value)

    @property
    def MinTap(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: MinTap
        DSS property index: 32
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 32)

    @MinTap.setter
    def MinTap(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(32, value)

    @property
    def NumTaps(self) -> npt.NDArray[np.int32]:
        """
        DSS property name: NumTaps
        DSS property index: 33
        """
        return self._get_int32_array(self._lib.Obj_GetInt32Array, self._ptr, 33)

    @NumTaps.setter
    def NumTaps(self, value: npt.NDArray[np.int32]):
        self._set_int32_array(33, value)

    @property
    def subname(self) -> str:
        """
        DSS property name: subname
        DSS property index: 34
        """
        return self._get_prop_string(34)

    @subname.setter
    def subname(self, value: AnyStr):
        self._set_string(34, value)

    @property
    def pctimag(self) -> float:
        """
        DSS property name: %imag
        DSS property index: 35
        """
        return self._lib.Obj_GetFloat64(self._ptr, 35)

    @pctimag.setter
    def pctimag(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 35, value)

    @property
    def ppm_antifloat(self) -> float:
        """
        DSS property name: ppm_antifloat
        DSS property index: 36
        """
        return self._lib.Obj_GetFloat64(self._ptr, 36)

    @ppm_antifloat.setter
    def ppm_antifloat(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 36, value)

    @property
    def pctRs(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: %Rs
        DSS property index: 37
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 37)

    @pctRs.setter
    def pctRs(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(37, value)

    @property
    def XRConst(self) -> bool:
        """
        DSS property name: XRConst
        DSS property index: 38
        """
        return self._lib.Obj_GetInt32(self._ptr, 38) != 0

    @XRConst.setter
    def XRConst(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 38, value)

    @property
    def LeadLag(self) -> PhaseSequence:
        """
    DSS property name: LeadLag
    DSS property index: 39
    """
        return PhaseSequence(self._lib.Obj_GetInt32(self._ptr, 39))

    @LeadLag.setter
    def LeadLag(self, value: Union[AnyStr, int, PhaseSequence]):
        if not isinstance(value, int):
            self._set_string(39, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 39, value)

    @property
    def LeadLag_str(self) -> str:
        """
        DSS property name: LeadLag
        DSS property index: 39
        """
        return self._get_prop_string(39)

    @LeadLag_str.setter
    def LeadLag_str(self, value: AnyStr):
        self.LeadLag = value

    def WdgCurrents(self) -> str:
        """
        DSS property name: WdgCurrents
        DSS property index: 40
        """
        # []
        # StringSilentROFunction
        return self._get_prop_string(self._lib.Obj_GetString(self._ptr, 40))

    @property
    def normamps(self) -> float:
        """
        DSS property name: normamps
        DSS property index: 41
        """
        return self._lib.Obj_GetFloat64(self._ptr, 41)

    @normamps.setter
    def normamps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 41, value)

    @property
    def emergamps(self) -> float:
        """
        DSS property name: emergamps
        DSS property index: 42
        """
        return self._lib.Obj_GetFloat64(self._ptr, 42)

    @emergamps.setter
    def emergamps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 42, value)

    @property
    def faultrate(self) -> float:
        """
        DSS property name: faultrate
        DSS property index: 43
        """
        return self._lib.Obj_GetFloat64(self._ptr, 43)

    @faultrate.setter
    def faultrate(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 43, value)

    @property
    def pctperm(self) -> float:
        """
        DSS property name: pctperm
        DSS property index: 44
        """
        return self._lib.Obj_GetFloat64(self._ptr, 44)

    @pctperm.setter
    def pctperm(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 44, value)

    @property
    def repair(self) -> float:
        """
        DSS property name: repair
        DSS property index: 45
        """
        return self._lib.Obj_GetFloat64(self._ptr, 45)

    @repair.setter
    def repair(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 45, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 46
        """
        return self._lib.Obj_GetFloat64(self._ptr, 46)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 46, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 47
        """
        return self._lib.Obj_GetInt32(self._ptr, 47) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 47, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 48
        """
        self._set_string(48, value)

class RegControl(DSSObj):
    _cls_name = 'RegControl'
    _cls_idx = 21
    _cls_prop_idx = {
        'transformer': 1,
        'winding': 2,
        'vreg': 3,
        'band': 4,
        'ptratio': 5,
        'ctprim': 6,
        'r': 7,
        'x': 8,
        'bus': 9,
        'delay': 10,
        'reversible': 11,
        'revvreg': 12,
        'revband': 13,
        'revr': 14,
        'revx': 15,
        'tapdelay': 16,
        'debugtrace': 17,
        'maxtapchange': 18,
        'inversetime': 19,
        'tapwinding': 20,
        'vlimit': 21,
        'ptphase': 22,
        'revthreshold': 23,
        'revdelay': 24,
        'revneutral': 25,
        'eventlog': 26,
        'remoteptratio': 27,
        'tapnum': 28,
        'reset': 29,
        'ldc_z': 30,
        'rev_z': 31,
        'cogen': 32,
        'basefreq': 33,
        'enabled': 34,
        'like': 35,
    }

    # Class-specific enumerations
    class RegControlPhaseSelection(IntEnum):
        """RegControl: Phase Selection (DSS enumeration for RegControl)"""
        min = -3 # min
        max = -2 # max


    @property
    def transformer(self) -> str:
        """
        DSS property name: transformer
        DSS property index: 1
        """
        return self._get_prop_string(1)

    @transformer.setter
    def transformer(self, value: Union[AnyStr, Transformer, AutoTrans]):
        if isinstance(value, DSSObj):
            self._set_obj(1, value)
            return

        self._set_string(1, value)

    @property
    def transformer_obj(self) -> DSSObj:
        """
        DSS property name: transformer
        DSS property index: 1
        """
        return self._get_obj(1, None)

    @transformer_obj.setter
    def transformer_obj(self, value: Union[Transformer, AutoTrans]):
        self._set_obj(1, value)

    @property
    def winding(self) -> int:
        """
        DSS property name: winding
        DSS property index: 2
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @winding.setter
    def winding(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def vreg(self) -> float:
        """
        DSS property name: vreg
        DSS property index: 3
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @vreg.setter
    def vreg(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def band(self) -> float:
        """
        DSS property name: band
        DSS property index: 4
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @band.setter
    def band(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def ptratio(self) -> float:
        """
        DSS property name: ptratio
        DSS property index: 5
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @ptratio.setter
    def ptratio(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def CTprim(self) -> float:
        """
        DSS property name: CTprim
        DSS property index: 6
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    @CTprim.setter
    def CTprim(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 6, value)

    @property
    def R(self) -> float:
        """
        DSS property name: R
        DSS property index: 7
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @R.setter
    def R(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def X(self) -> float:
        """
        DSS property name: X
        DSS property index: 8
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @X.setter
    def X(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def bus(self) -> str:
        """
        DSS property name: bus
        DSS property index: 9
        """
        return self._get_prop_string(9)

    @bus.setter
    def bus(self, value: AnyStr):
        self._set_string(9, value)

    @property
    def delay(self) -> float:
        """
        DSS property name: delay
        DSS property index: 10
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @delay.setter
    def delay(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def reversible(self) -> bool:
        """
        DSS property name: reversible
        DSS property index: 11
        """
        return self._lib.Obj_GetInt32(self._ptr, 11) != 0

    @reversible.setter
    def reversible(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 11, value)

    @property
    def revvreg(self) -> float:
        """
        DSS property name: revvreg
        DSS property index: 12
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @revvreg.setter
    def revvreg(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def revband(self) -> float:
        """
        DSS property name: revband
        DSS property index: 13
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @revband.setter
    def revband(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def revR(self) -> float:
        """
        DSS property name: revR
        DSS property index: 14
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @revR.setter
    def revR(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def revX(self) -> float:
        """
        DSS property name: revX
        DSS property index: 15
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @revX.setter
    def revX(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def tapdelay(self) -> float:
        """
        DSS property name: tapdelay
        DSS property index: 16
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    @tapdelay.setter
    def tapdelay(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 16, value)

    @property
    def debugtrace(self) -> bool:
        """
        DSS property name: debugtrace
        DSS property index: 17
        """
        return self._lib.Obj_GetInt32(self._ptr, 17) != 0

    @debugtrace.setter
    def debugtrace(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 17, value)

    @property
    def maxtapchange(self) -> int:
        """
        DSS property name: maxtapchange
        DSS property index: 18
        """
        return self._lib.Obj_GetInt32(self._ptr, 18)

    @maxtapchange.setter
    def maxtapchange(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 18, value)

    @property
    def inversetime(self) -> bool:
        """
        DSS property name: inversetime
        DSS property index: 19
        """
        return self._lib.Obj_GetInt32(self._ptr, 19) != 0

    @inversetime.setter
    def inversetime(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 19, value)

    @property
    def tapwinding(self) -> int:
        """
        DSS property name: tapwinding
        DSS property index: 20
        """
        return self._lib.Obj_GetInt32(self._ptr, 20)

    @tapwinding.setter
    def tapwinding(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 20, value)

    @property
    def vlimit(self) -> float:
        """
        DSS property name: vlimit
        DSS property index: 21
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @vlimit.setter
    def vlimit(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    @property
    def PTphase(self) -> Union[RegControlPhaseSelection, int]:
        """
    DSS property name: PTphase
    DSS property index: 22
    """
        value = self._lib.Obj_GetInt32(self._ptr, 22)
        if value > 0:
            return value

        return RegControlPhaseSelection(value)

    @PTphase.setter
    def PTphase(self, value: Union[AnyStr, int, RegControlPhaseSelection]):
        if not isinstance(value, int):
            self._set_string(22, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 22, value)

    @property
    def PTphase_str(self) -> str:
        """
        DSS property name: PTphase
        DSS property index: 22
        """
        return self._get_prop_string(22)

    @PTphase_str.setter
    def PTphase_str(self, value: AnyStr):
        self.PTphase = value

    @property
    def revThreshold(self) -> float:
        """
        DSS property name: revThreshold
        DSS property index: 23
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    @revThreshold.setter
    def revThreshold(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 23, value)

    @property
    def revDelay(self) -> float:
        """
        DSS property name: revDelay
        DSS property index: 24
        """
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    @revDelay.setter
    def revDelay(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 24, value)

    @property
    def revNeutral(self) -> bool:
        """
        DSS property name: revNeutral
        DSS property index: 25
        """
        return self._lib.Obj_GetInt32(self._ptr, 25) != 0

    @revNeutral.setter
    def revNeutral(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 25, value)

    @property
    def EventLog(self) -> bool:
        """
        DSS property name: EventLog
        DSS property index: 26
        """
        return self._lib.Obj_GetInt32(self._ptr, 26) != 0

    @EventLog.setter
    def EventLog(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 26, value)

    @property
    def RemotePTRatio(self) -> float:
        """
        DSS property name: RemotePTRatio
        DSS property index: 27
        """
        return self._lib.Obj_GetFloat64(self._ptr, 27)

    @RemotePTRatio.setter
    def RemotePTRatio(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 27, value)

    @property
    def TapNum(self) -> int:
        """
        DSS property name: TapNum
        DSS property index: 28
        """
        return self._lib.Obj_GetInt32(self._ptr, 28)

    @TapNum.setter
    def TapNum(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 28, value)

    def Reset(self, value: bool):
        """
        DSS property name: Reset
        DSS property index: 29
        """
        self._lib.Obj_SetInt32(self._ptr, 29, value)

    @property
    def LDC_Z(self) -> float:
        """
        DSS property name: LDC_Z
        DSS property index: 30
        """
        return self._lib.Obj_GetFloat64(self._ptr, 30)

    @LDC_Z.setter
    def LDC_Z(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 30, value)

    @property
    def rev_Z(self) -> float:
        """
        DSS property name: rev_Z
        DSS property index: 31
        """
        return self._lib.Obj_GetFloat64(self._ptr, 31)

    @rev_Z.setter
    def rev_Z(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 31, value)

    @property
    def Cogen(self) -> bool:
        """
        DSS property name: Cogen
        DSS property index: 32
        """
        return self._lib.Obj_GetInt32(self._ptr, 32) != 0

    @Cogen.setter
    def Cogen(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 32, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 33
        """
        return self._lib.Obj_GetFloat64(self._ptr, 33)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 33, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 34
        """
        return self._lib.Obj_GetInt32(self._ptr, 34) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 34, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 35
        """
        self._set_string(35, value)

class InvControl(DSSObj):
    _cls_name = 'InvControl'
    _cls_idx = 41
    _cls_prop_idx = {
        'derlist': 1,
        'mode': 2,
        'combimode': 3,
        'vvc_curve1': 4,
        'hysteresis_offset': 5,
        'voltage_curvex_ref': 6,
        'avgwindowlen': 7,
        'voltwatt_curve': 8,
        'dbvmin': 9,
        'dbvmax': 10,
        'argralowv': 11,
        'argrahiv': 12,
        'dynreacavgwindowlen': 13,
        'deltaq_factor': 14,
        'voltagechangetolerance': 15,
        'varchangetolerance': 16,
        'voltwattyaxis': 17,
        'rateofchangemode': 18,
        'lpftau': 19,
        'risefalllimit': 20,
        'deltap_factor': 21,
        'eventlog': 22,
        'refreactivepower': 23,
        'activepchangetolerance': 24,
        'monvoltagecalc': 25,
        'monbus': 26,
        'monbusesvbase': 27,
        'voltwattch_curve': 28,
        'wattpf_curve': 29,
        'wattvar_curve': 30,
        'pvsystemlist': 31,
        'vsetpoint': 32,
        'basefreq': 33,
        'enabled': 34,
        'like': 35,
    }

    # Class-specific enumerations
    class InvControlControlMode(IntEnum):
        """InvControl: Control Mode (DSS enumeration for InvControl)"""
        Voltvar = 1 # Voltvar
        VoltWatt = 2 # VoltWatt
        DynamicReaccurr = 3 # DynamicReaccurr
        WattPF = 4 # WattPF
        Wattvar = 5 # Wattvar
        AVR = 6 # AVR

    class InvControlCombiMode(IntEnum):
        """InvControl: Combi Mode (DSS enumeration for InvControl)"""
        VV_VW = 1 # VV_VW
        VV_DRC = 2 # VV_DRC

    class InvControlVoltageCurveXRef(IntEnum):
        """InvControl: Voltage Curve X Ref (DSS enumeration for InvControl)"""
        Rated = 0 # Rated
        Avg = 1 # Avg
        RAvg = 2 # RAvg

    class InvControlVoltWattYAxis(IntEnum):
        """InvControl: Volt-watt Y-Axis (DSS enumeration for InvControl)"""
        PAvailablePU = 0 # PAvailablePU
        PMPPPU = 1 # PMPPPU
        PctPMPPPU = 2 # PctPMPPPU
        KVARatingPU = 3 # KVARatingPU

    class InvControlRateOfChangeMode(IntEnum):
        """InvControl: Rate-of-change Mode (DSS enumeration for InvControl)"""
        Inactive = 0 # Inactive
        LPF = 1 # LPF
        RiseFall = 2 # RiseFall

    class InvControlReactivePowerReference(IntEnum):
        """InvControl: Reactive Power Reference (DSS enumeration for InvControl)"""
        VARAVAL = 0 # VARAVAL
        VARMAX = 1 # VARMAX


    @property
    def DERList(self) -> List[str]:
        """
        DSS property name: DERList
        DSS property index: 1
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 1)

    @DERList.setter
    def DERList(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 1, value_ptr, value_count)
        self._check_for_error()

    @property
    def Mode(self) -> InvControlControlMode:
        """
    DSS property name: Mode
    DSS property index: 2
    """
        return InvControlControlMode(self._lib.Obj_GetInt32(self._ptr, 2))

    @Mode.setter
    def Mode(self, value: Union[AnyStr, int, InvControlControlMode]):
        if not isinstance(value, int):
            self._set_string(2, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def Mode_str(self) -> str:
        """
        DSS property name: Mode
        DSS property index: 2
        """
        return self._get_prop_string(2)

    @Mode_str.setter
    def Mode_str(self, value: AnyStr):
        self.Mode = value

    @property
    def CombiMode(self) -> InvControlCombiMode:
        """
    DSS property name: CombiMode
    DSS property index: 3
    """
        return InvControlCombiMode(self._lib.Obj_GetInt32(self._ptr, 3))

    @CombiMode.setter
    def CombiMode(self, value: Union[AnyStr, int, InvControlCombiMode]):
        if not isinstance(value, int):
            self._set_string(3, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 3, value)

    @property
    def CombiMode_str(self) -> str:
        """
        DSS property name: CombiMode
        DSS property index: 3
        """
        return self._get_prop_string(3)

    @CombiMode_str.setter
    def CombiMode_str(self, value: AnyStr):
        self.CombiMode = value

    @property
    def vvc_curve1(self) -> str:
        """
        DSS property name: vvc_curve1
        DSS property index: 4
        """
        return self._get_prop_string(4)

    @vvc_curve1.setter
    def vvc_curve1(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(4, value)
            return

        self._set_string(4, value)

    @property
    def vvc_curve1_obj(self) -> XYcurve:
        """
        DSS property name: vvc_curve1
        DSS property index: 4
        """
        return self._get_obj(4, XYcurve)

    @vvc_curve1_obj.setter
    def vvc_curve1_obj(self, value: XYcurve):
        self._set_obj(4, value)

    @property
    def hysteresis_offset(self) -> float:
        """
        DSS property name: hysteresis_offset
        DSS property index: 5
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @hysteresis_offset.setter
    def hysteresis_offset(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def voltage_curvex_ref(self) -> InvControlVoltageCurveXRef:
        """
    DSS property name: voltage_curvex_ref
    DSS property index: 6
    """
        return InvControlVoltageCurveXRef(self._lib.Obj_GetInt32(self._ptr, 6))

    @voltage_curvex_ref.setter
    def voltage_curvex_ref(self, value: Union[AnyStr, int, InvControlVoltageCurveXRef]):
        if not isinstance(value, int):
            self._set_string(6, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 6, value)

    @property
    def voltage_curvex_ref_str(self) -> str:
        """
        DSS property name: voltage_curvex_ref
        DSS property index: 6
        """
        return self._get_prop_string(6)

    @voltage_curvex_ref_str.setter
    def voltage_curvex_ref_str(self, value: AnyStr):
        self.voltage_curvex_ref = value

    @property
    def avgwindowlen(self) -> int:
        """
        DSS property name: avgwindowlen
        DSS property index: 7
        """
        return self._lib.Obj_GetInt32(self._ptr, 7)

    @avgwindowlen.setter
    def avgwindowlen(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 7, value)

    @property
    def voltwatt_curve(self) -> str:
        """
        DSS property name: voltwatt_curve
        DSS property index: 8
        """
        return self._get_prop_string(8)

    @voltwatt_curve.setter
    def voltwatt_curve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(8, value)
            return

        self._set_string(8, value)

    @property
    def voltwatt_curve_obj(self) -> XYcurve:
        """
        DSS property name: voltwatt_curve
        DSS property index: 8
        """
        return self._get_obj(8, XYcurve)

    @voltwatt_curve_obj.setter
    def voltwatt_curve_obj(self, value: XYcurve):
        self._set_obj(8, value)

    @property
    def DbVMin(self) -> float:
        """
        DSS property name: DbVMin
        DSS property index: 9
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @DbVMin.setter
    def DbVMin(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def DbVMax(self) -> float:
        """
        DSS property name: DbVMax
        DSS property index: 10
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @DbVMax.setter
    def DbVMax(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def ArGraLowV(self) -> float:
        """
        DSS property name: ArGraLowV
        DSS property index: 11
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @ArGraLowV.setter
    def ArGraLowV(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def ArGraHiV(self) -> float:
        """
        DSS property name: ArGraHiV
        DSS property index: 12
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @ArGraHiV.setter
    def ArGraHiV(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def DynReacavgwindowlen(self) -> int:
        """
        DSS property name: DynReacavgwindowlen
        DSS property index: 13
        """
        return self._lib.Obj_GetInt32(self._ptr, 13)

    @DynReacavgwindowlen.setter
    def DynReacavgwindowlen(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 13, value)

    @property
    def deltaQ_Factor(self) -> float:
        """
        DSS property name: deltaQ_Factor
        DSS property index: 14
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @deltaQ_Factor.setter
    def deltaQ_Factor(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def VoltageChangeTolerance(self) -> float:
        """
        DSS property name: VoltageChangeTolerance
        DSS property index: 15
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @VoltageChangeTolerance.setter
    def VoltageChangeTolerance(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def VarChangeTolerance(self) -> float:
        """
        DSS property name: VarChangeTolerance
        DSS property index: 16
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    @VarChangeTolerance.setter
    def VarChangeTolerance(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 16, value)

    @property
    def VoltwattYAxis(self) -> InvControlVoltWattYAxis:
        """
    DSS property name: VoltwattYAxis
    DSS property index: 17
    """
        return InvControlVoltWattYAxis(self._lib.Obj_GetInt32(self._ptr, 17))

    @VoltwattYAxis.setter
    def VoltwattYAxis(self, value: Union[AnyStr, int, InvControlVoltWattYAxis]):
        if not isinstance(value, int):
            self._set_string(17, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 17, value)

    @property
    def VoltwattYAxis_str(self) -> str:
        """
        DSS property name: VoltwattYAxis
        DSS property index: 17
        """
        return self._get_prop_string(17)

    @VoltwattYAxis_str.setter
    def VoltwattYAxis_str(self, value: AnyStr):
        self.VoltwattYAxis = value

    @property
    def RateofChangeMode(self) -> InvControlRateOfChangeMode:
        """
    DSS property name: RateofChangeMode
    DSS property index: 18
    """
        return InvControlRateOfChangeMode(self._lib.Obj_GetInt32(self._ptr, 18))

    @RateofChangeMode.setter
    def RateofChangeMode(self, value: Union[AnyStr, int, InvControlRateOfChangeMode]):
        if not isinstance(value, int):
            self._set_string(18, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 18, value)

    @property
    def RateofChangeMode_str(self) -> str:
        """
        DSS property name: RateofChangeMode
        DSS property index: 18
        """
        return self._get_prop_string(18)

    @RateofChangeMode_str.setter
    def RateofChangeMode_str(self, value: AnyStr):
        self.RateofChangeMode = value

    @property
    def LPFTau(self) -> float:
        """
        DSS property name: LPFTau
        DSS property index: 19
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    @LPFTau.setter
    def LPFTau(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 19, value)

    @property
    def RiseFallLimit(self) -> float:
        """
        DSS property name: RiseFallLimit
        DSS property index: 20
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    @RiseFallLimit.setter
    def RiseFallLimit(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 20, value)

    @property
    def deltaP_Factor(self) -> float:
        """
        DSS property name: deltaP_Factor
        DSS property index: 21
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @deltaP_Factor.setter
    def deltaP_Factor(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    @property
    def EventLog(self) -> bool:
        """
        DSS property name: EventLog
        DSS property index: 22
        """
        return self._lib.Obj_GetInt32(self._ptr, 22) != 0

    @EventLog.setter
    def EventLog(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 22, value)

    @property
    def RefReactivePower(self) -> InvControlReactivePowerReference:
        """
    DSS property name: RefReactivePower
    DSS property index: 23
    """
        return InvControlReactivePowerReference(self._lib.Obj_GetInt32(self._ptr, 23))

    @RefReactivePower.setter
    def RefReactivePower(self, value: Union[AnyStr, int, InvControlReactivePowerReference]):
        if not isinstance(value, int):
            self._set_string(23, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 23, value)

    @property
    def RefReactivePower_str(self) -> str:
        """
        DSS property name: RefReactivePower
        DSS property index: 23
        """
        return self._get_prop_string(23)

    @RefReactivePower_str.setter
    def RefReactivePower_str(self, value: AnyStr):
        self.RefReactivePower = value

    @property
    def ActivePChangeTolerance(self) -> float:
        """
        DSS property name: ActivePChangeTolerance
        DSS property index: 24
        """
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    @ActivePChangeTolerance.setter
    def ActivePChangeTolerance(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 24, value)

    @property
    def monVoltageCalc(self) -> Union[MonitoredPhase, int]:
        """
    DSS property name: monVoltageCalc
    DSS property index: 25
    """
        value = self._lib.Obj_GetInt32(self._ptr, 25)
        if value > 0:
            return value

        return MonitoredPhase(value)

    @monVoltageCalc.setter
    def monVoltageCalc(self, value: Union[AnyStr, int, MonitoredPhase]):
        if not isinstance(value, int):
            self._set_string(25, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 25, value)

    @property
    def monVoltageCalc_str(self) -> str:
        """
        DSS property name: monVoltageCalc
        DSS property index: 25
        """
        return self._get_prop_string(25)

    @monVoltageCalc_str.setter
    def monVoltageCalc_str(self, value: AnyStr):
        self.monVoltageCalc = value

    @property
    def monBus(self) -> List[str]:
        """
        DSS property name: monBus
        DSS property index: 26
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 26)

    @monBus.setter
    def monBus(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 26, value_ptr, value_count)
        self._check_for_error()

    @property
    def MonBusesVbase(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: MonBusesVbase
        DSS property index: 27
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 27)

    @MonBusesVbase.setter
    def MonBusesVbase(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(27, value)

    @property
    def voltwattCH_curve(self) -> str:
        """
        DSS property name: voltwattCH_curve
        DSS property index: 28
        """
        return self._get_prop_string(28)

    @voltwattCH_curve.setter
    def voltwattCH_curve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(28, value)
            return

        self._set_string(28, value)

    @property
    def voltwattCH_curve_obj(self) -> XYcurve:
        """
        DSS property name: voltwattCH_curve
        DSS property index: 28
        """
        return self._get_obj(28, XYcurve)

    @voltwattCH_curve_obj.setter
    def voltwattCH_curve_obj(self, value: XYcurve):
        self._set_obj(28, value)

    @property
    def wattpf_curve(self) -> str:
        """
        DSS property name: wattpf_curve
        DSS property index: 29
        """
        return self._get_prop_string(29)

    @wattpf_curve.setter
    def wattpf_curve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(29, value)
            return

        self._set_string(29, value)

    @property
    def wattpf_curve_obj(self) -> XYcurve:
        """
        DSS property name: wattpf_curve
        DSS property index: 29
        """
        return self._get_obj(29, XYcurve)

    @wattpf_curve_obj.setter
    def wattpf_curve_obj(self, value: XYcurve):
        self._set_obj(29, value)

    @property
    def wattvar_curve(self) -> str:
        """
        DSS property name: wattvar_curve
        DSS property index: 30
        """
        return self._get_prop_string(30)

    @wattvar_curve.setter
    def wattvar_curve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(30, value)
            return

        self._set_string(30, value)

    @property
    def wattvar_curve_obj(self) -> XYcurve:
        """
        DSS property name: wattvar_curve
        DSS property index: 30
        """
        return self._get_obj(30, XYcurve)

    @wattvar_curve_obj.setter
    def wattvar_curve_obj(self, value: XYcurve):
        self._set_obj(30, value)

    @property
    def PVSystemList(self) -> List[str]:
        """
        DSS property name: PVSystemList
        DSS property index: 31
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 31)

    @PVSystemList.setter
    def PVSystemList(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 31, value_ptr, value_count)
        self._check_for_error()

    @property
    def Vsetpoint(self) -> float:
        """
        DSS property name: Vsetpoint
        DSS property index: 32
        """
        return self._lib.Obj_GetFloat64(self._ptr, 32)

    @Vsetpoint.setter
    def Vsetpoint(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 32, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 33
        """
        return self._lib.Obj_GetFloat64(self._ptr, 33)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 33, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 34
        """
        return self._lib.Obj_GetInt32(self._ptr, 34) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 34, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 35
        """
        self._set_string(35, value)

class ExpControl(DSSObj):
    _cls_name = 'ExpControl'
    _cls_idx = 42
    _cls_prop_idx = {
        'pvsystemlist': 1,
        'vreg': 2,
        'slope': 3,
        'vregtau': 4,
        'qbias': 5,
        'vregmin': 6,
        'vregmax': 7,
        'qmaxlead': 8,
        'qmaxlag': 9,
        'eventlog': 10,
        'deltaq_factor': 11,
        'preferq': 12,
        'tresponse': 13,
        'derlist': 14,
        'basefreq': 15,
        'enabled': 16,
        'like': 17,
    }

    @property
    def PVSystemList(self) -> List[str]:
        """
        DSS property name: PVSystemList
        DSS property index: 1
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 1)

    @PVSystemList.setter
    def PVSystemList(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 1, value_ptr, value_count)
        self._check_for_error()

    @property
    def Vreg(self) -> float:
        """
        DSS property name: Vreg
        DSS property index: 2
        """
        return self._lib.Obj_GetFloat64(self._ptr, 2)

    @Vreg.setter
    def Vreg(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 2, value)

    @property
    def Slope(self) -> float:
        """
        DSS property name: Slope
        DSS property index: 3
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @Slope.setter
    def Slope(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def VregTau(self) -> float:
        """
        DSS property name: VregTau
        DSS property index: 4
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @VregTau.setter
    def VregTau(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def Qbias(self) -> float:
        """
        DSS property name: Qbias
        DSS property index: 5
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @Qbias.setter
    def Qbias(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def VregMin(self) -> float:
        """
        DSS property name: VregMin
        DSS property index: 6
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    @VregMin.setter
    def VregMin(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 6, value)

    @property
    def VregMax(self) -> float:
        """
        DSS property name: VregMax
        DSS property index: 7
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @VregMax.setter
    def VregMax(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def QmaxLead(self) -> float:
        """
        DSS property name: QmaxLead
        DSS property index: 8
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @QmaxLead.setter
    def QmaxLead(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def QmaxLag(self) -> float:
        """
        DSS property name: QmaxLag
        DSS property index: 9
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @QmaxLag.setter
    def QmaxLag(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def EventLog(self) -> bool:
        """
        DSS property name: EventLog
        DSS property index: 10
        """
        return self._lib.Obj_GetInt32(self._ptr, 10) != 0

    @EventLog.setter
    def EventLog(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 10, value)

    @property
    def DeltaQ_factor(self) -> float:
        """
        DSS property name: DeltaQ_factor
        DSS property index: 11
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @DeltaQ_factor.setter
    def DeltaQ_factor(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def PreferQ(self) -> bool:
        """
        DSS property name: PreferQ
        DSS property index: 12
        """
        return self._lib.Obj_GetInt32(self._ptr, 12) != 0

    @PreferQ.setter
    def PreferQ(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 12, value)

    @property
    def Tresponse(self) -> float:
        """
        DSS property name: Tresponse
        DSS property index: 13
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @Tresponse.setter
    def Tresponse(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def DERList(self) -> List[str]:
        """
        DSS property name: DERList
        DSS property index: 14
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 14)

    @DERList.setter
    def DERList(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 14, value_ptr, value_count)
        self._check_for_error()

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 15
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 16
        """
        return self._lib.Obj_GetInt32(self._ptr, 16) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 16, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 17
        """
        self._set_string(17, value)

class GICLine(DSSObj):
    _cls_name = 'GICLine'
    _cls_idx = 43
    _cls_prop_idx = {
        'bus1': 1,
        'bus2': 2,
        'volts': 3,
        'angle': 4,
        'frequency': 5,
        'phases': 6,
        'r': 7,
        'x': 8,
        'c': 9,
        'en': 10,
        'ee': 11,
        'lat1': 12,
        'lon1': 13,
        'lat2': 14,
        'lon2': 15,
        'spectrum': 16,
        'basefreq': 17,
        'enabled': 18,
        'like': 19,
    }

    @property
    def bus1(self) -> str:
        """
        DSS property name: bus1
        DSS property index: 1
        """
        return self._get_prop_string(1)

    @bus1.setter
    def bus1(self, value: AnyStr):
        self._set_string(1, value)

    @property
    def bus2(self) -> str:
        """
        DSS property name: bus2
        DSS property index: 2
        """
        return self._get_prop_string(2)

    @bus2.setter
    def bus2(self, value: AnyStr):
        self._set_string(2, value)

    @property
    def Volts(self) -> float:
        """
        DSS property name: Volts
        DSS property index: 3
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @Volts.setter
    def Volts(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def Angle(self) -> float:
        """
        DSS property name: Angle
        DSS property index: 4
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @Angle.setter
    def Angle(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def frequency(self) -> float:
        """
        DSS property name: frequency
        DSS property index: 5
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @frequency.setter
    def frequency(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def phases(self) -> int:
        """
        DSS property name: phases
        DSS property index: 6
        """
        return self._lib.Obj_GetInt32(self._ptr, 6)

    @phases.setter
    def phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 6, value)

    @property
    def R(self) -> float:
        """
        DSS property name: R
        DSS property index: 7
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @R.setter
    def R(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def X(self) -> float:
        """
        DSS property name: X
        DSS property index: 8
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @X.setter
    def X(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def C(self) -> float:
        """
        DSS property name: C
        DSS property index: 9
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @C.setter
    def C(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def EN(self) -> float:
        """
        DSS property name: EN
        DSS property index: 10
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @EN.setter
    def EN(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def EE(self) -> float:
        """
        DSS property name: EE
        DSS property index: 11
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @EE.setter
    def EE(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def Lat1(self) -> float:
        """
        DSS property name: Lat1
        DSS property index: 12
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @Lat1.setter
    def Lat1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def Lon1(self) -> float:
        """
        DSS property name: Lon1
        DSS property index: 13
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @Lon1.setter
    def Lon1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def Lat2(self) -> float:
        """
        DSS property name: Lat2
        DSS property index: 14
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @Lat2.setter
    def Lat2(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def Lon2(self) -> float:
        """
        DSS property name: Lon2
        DSS property index: 15
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @Lon2.setter
    def Lon2(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def spectrum(self) -> str:
        """
        DSS property name: spectrum
        DSS property index: 16
        """
        return self._get_prop_string(16)

    @spectrum.setter
    def spectrum(self, value: Union[AnyStr, Spectrum]):
        if isinstance(value, DSSObj):
            self._set_obj(16, value)
            return

        self._set_string(16, value)

    @property
    def spectrum_obj(self) -> Spectrum:
        """
        DSS property name: spectrum
        DSS property index: 16
        """
        return self._get_obj(16, Spectrum)

    @spectrum_obj.setter
    def spectrum_obj(self, value: Spectrum):
        self._set_obj(16, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 17
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 17, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 18
        """
        return self._lib.Obj_GetInt32(self._ptr, 18) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 18, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 19
        """
        self._set_string(19, value)

class GICTransformer(DSSObj):
    _cls_name = 'GICTransformer'
    _cls_idx = 44
    _cls_prop_idx = {
        'bush': 1,
        'busnh': 2,
        'busx': 3,
        'busnx': 4,
        'phases': 5,
        'type': 6,
        'r1': 7,
        'r2': 8,
        'kvll1': 9,
        'kvll2': 10,
        'mva': 11,
        'varcurve': 12,
        'pctr1': 13,
        '%r1': 13,
        'pctr2': 14,
        '%r2': 14,
        'k': 15,
        'normamps': 16,
        'emergamps': 17,
        'faultrate': 18,
        'pctperm': 19,
        'repair': 20,
        'basefreq': 21,
        'enabled': 22,
        'like': 23,
    }

    # Class-specific enumerations
    class GICTransformerType(IntEnum):
        """GICTransformer: Type (DSS enumeration for GICTransformer)"""
        GSU = 1 # GSU
        Auto = 2 # Auto
        YY = 3 # YY


    @property
    def BusH(self) -> str:
        """
        DSS property name: BusH
        DSS property index: 1
        """
        return self._get_prop_string(1)

    @BusH.setter
    def BusH(self, value: AnyStr):
        self._set_string(1, value)

    @property
    def BusNH(self) -> str:
        """
        DSS property name: BusNH
        DSS property index: 2
        """
        return self._get_prop_string(2)

    @BusNH.setter
    def BusNH(self, value: AnyStr):
        self._set_string(2, value)

    @property
    def BusX(self) -> str:
        """
        DSS property name: BusX
        DSS property index: 3
        """
        return self._get_prop_string(3)

    @BusX.setter
    def BusX(self, value: AnyStr):
        self._set_string(3, value)

    @property
    def BusNX(self) -> str:
        """
        DSS property name: BusNX
        DSS property index: 4
        """
        return self._get_prop_string(4)

    @BusNX.setter
    def BusNX(self, value: AnyStr):
        self._set_string(4, value)

    @property
    def phases(self) -> int:
        """
        DSS property name: phases
        DSS property index: 5
        """
        return self._lib.Obj_GetInt32(self._ptr, 5)

    @phases.setter
    def phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 5, value)

    @property
    def Type(self) -> GICTransformerType:
        """
    DSS property name: Type
    DSS property index: 6
    """
        return GICTransformerType(self._lib.Obj_GetInt32(self._ptr, 6))

    @Type.setter
    def Type(self, value: Union[AnyStr, int, GICTransformerType]):
        if not isinstance(value, int):
            self._set_string(6, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 6, value)

    @property
    def Type_str(self) -> str:
        """
        DSS property name: Type
        DSS property index: 6
        """
        return self._get_prop_string(6)

    @Type_str.setter
    def Type_str(self, value: AnyStr):
        self.Type = value

    @property
    def R1(self) -> float:
        """
        DSS property name: R1
        DSS property index: 7
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @R1.setter
    def R1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def R2(self) -> float:
        """
        DSS property name: R2
        DSS property index: 8
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @R2.setter
    def R2(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def KVLL1(self) -> float:
        """
        DSS property name: KVLL1
        DSS property index: 9
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @KVLL1.setter
    def KVLL1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def KVLL2(self) -> float:
        """
        DSS property name: KVLL2
        DSS property index: 10
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @KVLL2.setter
    def KVLL2(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def MVA(self) -> float:
        """
        DSS property name: MVA
        DSS property index: 11
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @MVA.setter
    def MVA(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def VarCurve(self) -> str:
        """
        DSS property name: VarCurve
        DSS property index: 12
        """
        return self._get_prop_string(12)

    @VarCurve.setter
    def VarCurve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(12, value)
            return

        self._set_string(12, value)

    @property
    def VarCurve_obj(self) -> XYcurve:
        """
        DSS property name: VarCurve
        DSS property index: 12
        """
        return self._get_obj(12, XYcurve)

    @VarCurve_obj.setter
    def VarCurve_obj(self, value: XYcurve):
        self._set_obj(12, value)

    @property
    def pctR1(self) -> float:
        """
        DSS property name: %R1
        DSS property index: 13
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @pctR1.setter
    def pctR1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def pctR2(self) -> float:
        """
        DSS property name: %R2
        DSS property index: 14
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @pctR2.setter
    def pctR2(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def K(self) -> float:
        """
        DSS property name: K
        DSS property index: 15
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @K.setter
    def K(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def normamps(self) -> float:
        """
        DSS property name: normamps
        DSS property index: 16
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    @normamps.setter
    def normamps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 16, value)

    @property
    def emergamps(self) -> float:
        """
        DSS property name: emergamps
        DSS property index: 17
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    @emergamps.setter
    def emergamps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 17, value)

    @property
    def faultrate(self) -> float:
        """
        DSS property name: faultrate
        DSS property index: 18
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    @faultrate.setter
    def faultrate(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 18, value)

    @property
    def pctperm(self) -> float:
        """
        DSS property name: pctperm
        DSS property index: 19
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    @pctperm.setter
    def pctperm(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 19, value)

    @property
    def repair(self) -> float:
        """
        DSS property name: repair
        DSS property index: 20
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    @repair.setter
    def repair(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 20, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 21
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 22
        """
        return self._lib.Obj_GetInt32(self._ptr, 22) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 22, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 23
        """
        self._set_string(23, value)

class VSConverter(DSSObj):
    _cls_name = 'VSConverter'
    _cls_idx = 45
    _cls_prop_idx = {
        'phases': 1,
        'bus1': 2,
        'kvac': 3,
        'kvdc': 4,
        'kw': 5,
        'ndc': 6,
        'rac': 7,
        'xac': 8,
        'm0': 9,
        'd0': 10,
        'mmin': 11,
        'mmax': 12,
        'iacmax': 13,
        'idcmax': 14,
        'vacref': 15,
        'pacref': 16,
        'qacref': 17,
        'vdcref': 18,
        'vscmode': 19,
        'spectrum': 20,
        'basefreq': 21,
        'enabled': 22,
        'like': 23,
    }

    # Class-specific enumerations
    class VSConverterControlMode(IntEnum):
        """VSConverter: Control Mode (DSS enumeration for VSConverter)"""
        Fixed = 0 # Fixed
        PacVac = 1 # PacVac
        PacQac = 2 # PacQac
        VdcVac = 3 # VdcVac
        VdcQac = 4 # VdcQac


    @property
    def phases(self) -> int:
        """
        DSS property name: phases
        DSS property index: 1
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @phases.setter
    def phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def Bus1(self) -> str:
        """
        DSS property name: Bus1
        DSS property index: 2
        """
        return self._get_prop_string(2)

    @Bus1.setter
    def Bus1(self, value: AnyStr):
        self._set_string(2, value)

    @property
    def kVac(self) -> float:
        """
        DSS property name: kVac
        DSS property index: 3
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @kVac.setter
    def kVac(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def kVdc(self) -> float:
        """
        DSS property name: kVdc
        DSS property index: 4
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @kVdc.setter
    def kVdc(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def kW(self) -> float:
        """
        DSS property name: kW
        DSS property index: 5
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @kW.setter
    def kW(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def Ndc(self) -> int:
        """
        DSS property name: Ndc
        DSS property index: 6
        """
        return self._lib.Obj_GetInt32(self._ptr, 6)

    @Ndc.setter
    def Ndc(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 6, value)

    @property
    def Rac(self) -> float:
        """
        DSS property name: Rac
        DSS property index: 7
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @Rac.setter
    def Rac(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def Xac(self) -> float:
        """
        DSS property name: Xac
        DSS property index: 8
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @Xac.setter
    def Xac(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def m0(self) -> float:
        """
        DSS property name: m0
        DSS property index: 9
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @m0.setter
    def m0(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def d0(self) -> float:
        """
        DSS property name: d0
        DSS property index: 10
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @d0.setter
    def d0(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def Mmin(self) -> float:
        """
        DSS property name: Mmin
        DSS property index: 11
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @Mmin.setter
    def Mmin(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def Mmax(self) -> float:
        """
        DSS property name: Mmax
        DSS property index: 12
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @Mmax.setter
    def Mmax(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def Iacmax(self) -> float:
        """
        DSS property name: Iacmax
        DSS property index: 13
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @Iacmax.setter
    def Iacmax(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def Idcmax(self) -> float:
        """
        DSS property name: Idcmax
        DSS property index: 14
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @Idcmax.setter
    def Idcmax(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def Vacref(self) -> float:
        """
        DSS property name: Vacref
        DSS property index: 15
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @Vacref.setter
    def Vacref(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def Pacref(self) -> float:
        """
        DSS property name: Pacref
        DSS property index: 16
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    @Pacref.setter
    def Pacref(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 16, value)

    @property
    def Qacref(self) -> float:
        """
        DSS property name: Qacref
        DSS property index: 17
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    @Qacref.setter
    def Qacref(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 17, value)

    @property
    def Vdcref(self) -> float:
        """
        DSS property name: Vdcref
        DSS property index: 18
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    @Vdcref.setter
    def Vdcref(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 18, value)

    @property
    def VscMode(self) -> VSConverterControlMode:
        """
    DSS property name: VscMode
    DSS property index: 19
    """
        return VSConverterControlMode(self._lib.Obj_GetInt32(self._ptr, 19))

    @VscMode.setter
    def VscMode(self, value: Union[AnyStr, int, VSConverterControlMode]):
        if not isinstance(value, int):
            self._set_string(19, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 19, value)

    @property
    def VscMode_str(self) -> str:
        """
        DSS property name: VscMode
        DSS property index: 19
        """
        return self._get_prop_string(19)

    @VscMode_str.setter
    def VscMode_str(self, value: AnyStr):
        self.VscMode = value

    @property
    def spectrum(self) -> str:
        """
        DSS property name: spectrum
        DSS property index: 20
        """
        return self._get_prop_string(20)

    @spectrum.setter
    def spectrum(self, value: Union[AnyStr, Spectrum]):
        if isinstance(value, DSSObj):
            self._set_obj(20, value)
            return

        self._set_string(20, value)

    @property
    def spectrum_obj(self) -> Spectrum:
        """
        DSS property name: spectrum
        DSS property index: 20
        """
        return self._get_obj(20, Spectrum)

    @spectrum_obj.setter
    def spectrum_obj(self, value: Spectrum):
        self._set_obj(20, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 21
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 22
        """
        return self._lib.Obj_GetInt32(self._ptr, 22) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 22, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 23
        """
        self._set_string(23, value)

class Monitor(DSSObj):
    _cls_name = 'Monitor'
    _cls_idx = 46
    _cls_prop_idx = {
        'element': 1,
        'terminal': 2,
        'mode': 3,
        'action': 4,
        'residual': 5,
        'vipolar': 6,
        'ppolar': 7,
        'basefreq': 8,
        'enabled': 9,
        'like': 10,
    }

    # Class-specific enumerations
    class MonitorAction(IntEnum):
        """Monitor: Action (DSS enumeration for Monitor)"""
        Clear = 0 # Clear
        Save = 1 # Save
        Take = 2 # Take
        Process = 3 # Process
        Reset = 0 # Reset


    @property
    def element(self) -> str:
        """
        DSS property name: element
        DSS property index: 1
        """
        return self._get_prop_string(1)

    @element.setter
    def element(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_obj(1, value)
            return

        self._set_string(1, value)

    @property
    def element_obj(self) -> DSSObj:
        """
        DSS property name: element
        DSS property index: 1
        """
        return self._get_obj(1, None)

    @element_obj.setter
    def element_obj(self, value: DSSObj):
        self._set_obj(1, value)

    @property
    def terminal(self) -> int:
        """
        DSS property name: terminal
        DSS property index: 2
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @terminal.setter
    def terminal(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def mode(self) -> int:
        """
        DSS property name: mode
        DSS property index: 3
        """
        return self._lib.Obj_GetInt32(self._ptr, 3)

    @mode.setter
    def mode(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 3, value)

    def action(self, value: Union[str, bytes, int, MonitorAction]):
        """
        DSS property name: action
        DSS property index: 4
        """
        if isinstance(value, int):
            self._lib.Obj_SetInt32(self._ptr, 4, value)
            return

        self._set_string(4, value)

    @property
    def residual(self) -> bool:
        """
        DSS property name: residual
        DSS property index: 5
        """
        return self._lib.Obj_GetInt32(self._ptr, 5) != 0

    @residual.setter
    def residual(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 5, value)

    @property
    def VIPolar(self) -> bool:
        """
        DSS property name: VIPolar
        DSS property index: 6
        """
        return self._lib.Obj_GetInt32(self._ptr, 6) != 0

    @VIPolar.setter
    def VIPolar(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 6, value)

    @property
    def PPolar(self) -> bool:
        """
        DSS property name: PPolar
        DSS property index: 7
        """
        return self._lib.Obj_GetInt32(self._ptr, 7) != 0

    @PPolar.setter
    def PPolar(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 7, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 8
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 9
        """
        return self._lib.Obj_GetInt32(self._ptr, 9) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 9, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 10
        """
        self._set_string(10, value)

class EnergyMeter(DSSObj):
    _cls_name = 'EnergyMeter'
    _cls_idx = 47
    _cls_prop_idx = {
        'element': 1,
        'terminal': 2,
        'action': 3,
        'option': 4,
        'kvanormal': 5,
        'kvaemerg': 6,
        'peakcurrent': 7,
        'zonelist': 8,
        'localonly': 9,
        'mask': 10,
        'losses': 11,
        'linelosses': 12,
        'xfmrlosses': 13,
        'seqlosses': 14,
        'threepaselosses': 15,
        '3phaselosses': 15,
        'vbaselosses': 16,
        'phasevoltagereport': 17,
        'int_rate': 18,
        'int_duration': 19,
        'saifi': 20,
        'saifikw': 21,
        'saidi': 22,
        'caidi': 23,
        'custinterrupts': 24,
        'basefreq': 25,
        'enabled': 26,
        'like': 27,
    }

    # Class-specific enumerations
    class EnergyMeterAction(IntEnum):
        """EnergyMeter: Action (DSS enumeration for EnergyMeter)"""
        Allocate = 0 # Allocate
        Clear = 1 # Clear
        Reduce = 2 # Reduce
        Save = 3 # Save
        Take = 4 # Take
        ZoneDump = 5 # ZoneDump


    @property
    def element(self) -> str:
        """
        DSS property name: element
        DSS property index: 1
        """
        return self._get_prop_string(1)

    @element.setter
    def element(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_obj(1, value)
            return

        self._set_string(1, value)

    @property
    def element_obj(self) -> DSSObj:
        """
        DSS property name: element
        DSS property index: 1
        """
        return self._get_obj(1, None)

    @element_obj.setter
    def element_obj(self, value: DSSObj):
        self._set_obj(1, value)

    @property
    def terminal(self) -> int:
        """
        DSS property name: terminal
        DSS property index: 2
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @terminal.setter
    def terminal(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    def action(self, value: Union[str, bytes, int, EnergyMeterAction]):
        """
        DSS property name: action
        DSS property index: 3
        """
        if isinstance(value, int):
            self._lib.Obj_SetInt32(self._ptr, 3, value)
            return

        self._set_string(3, value)

    @property
    def option(self) -> List[str]:
        """
        DSS property name: option
        DSS property index: 4
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 4)

    @option.setter
    def option(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 4, value_ptr, value_count)
        self._check_for_error()

    @property
    def kVAnormal(self) -> float:
        """
        DSS property name: kVAnormal
        DSS property index: 5
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @kVAnormal.setter
    def kVAnormal(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def kVAemerg(self) -> float:
        """
        DSS property name: kVAemerg
        DSS property index: 6
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    @kVAemerg.setter
    def kVAemerg(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 6, value)

    @property
    def peakcurrent(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: peakcurrent
        DSS property index: 7
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 7)

    @peakcurrent.setter
    def peakcurrent(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(7, value)

    @property
    def Zonelist(self) -> List[str]:
        """
        DSS property name: Zonelist
        DSS property index: 8
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 8)

    @Zonelist.setter
    def Zonelist(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 8, value_ptr, value_count)
        self._check_for_error()

    @property
    def LocalOnly(self) -> bool:
        """
        DSS property name: LocalOnly
        DSS property index: 9
        """
        return self._lib.Obj_GetInt32(self._ptr, 9) != 0

    @LocalOnly.setter
    def LocalOnly(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 9, value)

    @property
    def Mask(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: Mask
        DSS property index: 10
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 10)

    @Mask.setter
    def Mask(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(10, value)

    @property
    def Losses(self) -> bool:
        """
        DSS property name: Losses
        DSS property index: 11
        """
        return self._lib.Obj_GetInt32(self._ptr, 11) != 0

    @Losses.setter
    def Losses(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 11, value)

    @property
    def LineLosses(self) -> bool:
        """
        DSS property name: LineLosses
        DSS property index: 12
        """
        return self._lib.Obj_GetInt32(self._ptr, 12) != 0

    @LineLosses.setter
    def LineLosses(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 12, value)

    @property
    def XfmrLosses(self) -> bool:
        """
        DSS property name: XfmrLosses
        DSS property index: 13
        """
        return self._lib.Obj_GetInt32(self._ptr, 13) != 0

    @XfmrLosses.setter
    def XfmrLosses(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 13, value)

    @property
    def SeqLosses(self) -> bool:
        """
        DSS property name: SeqLosses
        DSS property index: 14
        """
        return self._lib.Obj_GetInt32(self._ptr, 14) != 0

    @SeqLosses.setter
    def SeqLosses(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 14, value)

    @property
    def threePaseLosses(self) -> bool:
        """
        DSS property name: 3phaseLosses
        DSS property index: 15
        """
        return self._lib.Obj_GetInt32(self._ptr, 15) != 0

    @threePaseLosses.setter
    def threePaseLosses(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 15, value)

    @property
    def VbaseLosses(self) -> bool:
        """
        DSS property name: VbaseLosses
        DSS property index: 16
        """
        return self._lib.Obj_GetInt32(self._ptr, 16) != 0

    @VbaseLosses.setter
    def VbaseLosses(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 16, value)

    @property
    def PhaseVoltageReport(self) -> bool:
        """
        DSS property name: PhaseVoltageReport
        DSS property index: 17
        """
        return self._lib.Obj_GetInt32(self._ptr, 17) != 0

    @PhaseVoltageReport.setter
    def PhaseVoltageReport(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 17, value)

    @property
    def Int_Rate(self) -> float:
        """
        DSS property name: Int_Rate
        DSS property index: 18
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    @Int_Rate.setter
    def Int_Rate(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 18, value)

    @property
    def Int_Duration(self) -> float:
        """
        DSS property name: Int_Duration
        DSS property index: 19
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    @Int_Duration.setter
    def Int_Duration(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 19, value)

    @property
    def SAIFI(self) -> float:
        """
        DSS property name: SAIFI
        DSS property index: 20
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    @SAIFI.setter
    def SAIFI(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 20, value)

    @property
    def SAIFIkW(self) -> float:
        """
        DSS property name: SAIFIkW
        DSS property index: 21
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @SAIFIkW.setter
    def SAIFIkW(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    @property
    def SAIDI(self) -> float:
        """
        DSS property name: SAIDI
        DSS property index: 22
        """
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    @SAIDI.setter
    def SAIDI(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 22, value)

    @property
    def CAIDI(self) -> float:
        """
        DSS property name: CAIDI
        DSS property index: 23
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    @CAIDI.setter
    def CAIDI(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 23, value)

    @property
    def CustInterrupts(self) -> float:
        """
        DSS property name: CustInterrupts
        DSS property index: 24
        """
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    @CustInterrupts.setter
    def CustInterrupts(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 24, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 25
        """
        return self._lib.Obj_GetFloat64(self._ptr, 25)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 25, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 26
        """
        return self._lib.Obj_GetInt32(self._ptr, 26) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 26, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 27
        """
        self._set_string(27, value)

class Sensor(DSSObj):
    _cls_name = 'Sensor'
    _cls_idx = 48
    _cls_prop_idx = {
        'element': 1,
        'terminal': 2,
        'kvbase': 3,
        'clear': 4,
        'kvs': 5,
        'currents': 6,
        'kws': 7,
        'kvars': 8,
        'conn': 9,
        'deltadirection': 10,
        'pcterror': 11,
        '%error': 11,
        'weight': 12,
        'basefreq': 13,
        'enabled': 14,
        'like': 15,
    }

    @property
    def element(self) -> str:
        """
        DSS property name: element
        DSS property index: 1
        """
        return self._get_prop_string(1)

    @element.setter
    def element(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_obj(1, value)
            return

        self._set_string(1, value)

    @property
    def element_obj(self) -> DSSObj:
        """
        DSS property name: element
        DSS property index: 1
        """
        return self._get_obj(1, None)

    @element_obj.setter
    def element_obj(self, value: DSSObj):
        self._set_obj(1, value)

    @property
    def terminal(self) -> int:
        """
        DSS property name: terminal
        DSS property index: 2
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @terminal.setter
    def terminal(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def kvbase(self) -> float:
        """
        DSS property name: kvbase
        DSS property index: 3
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @kvbase.setter
    def kvbase(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def clear(self) -> bool:
        """
        DSS property name: clear
        DSS property index: 4
        """
        return self._lib.Obj_GetInt32(self._ptr, 4) != 0

    @clear.setter
    def clear(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 4, value)

    @property
    def kVs(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: kVs
        DSS property index: 5
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 5)

    @kVs.setter
    def kVs(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(5, value)

    @property
    def currents(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: currents
        DSS property index: 6
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 6)

    @currents.setter
    def currents(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(6, value)

    @property
    def kWs(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: kWs
        DSS property index: 7
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 7)

    @kWs.setter
    def kWs(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(7, value)

    @property
    def kvars(self) -> npt.NDArray[np.float64]:
        """
        DSS property name: kvars
        DSS property index: 8
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 8)

    @kvars.setter
    def kvars(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(8, value)

    @property
    def conn(self) -> Connection:
        """
    DSS property name: conn
    DSS property index: 9
    """
        return Connection(self._lib.Obj_GetInt32(self._ptr, 9))

    @conn.setter
    def conn(self, value: Union[AnyStr, int, Connection]):
        if not isinstance(value, int):
            self._set_string(9, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 9, value)

    @property
    def conn_str(self) -> str:
        """
        DSS property name: conn
        DSS property index: 9
        """
        return self._get_prop_string(9)

    @conn_str.setter
    def conn_str(self, value: AnyStr):
        self.conn = value

    @property
    def Deltadirection(self) -> int:
        """
        DSS property name: Deltadirection
        DSS property index: 10
        """
        return self._lib.Obj_GetInt32(self._ptr, 10)

    @Deltadirection.setter
    def Deltadirection(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 10, value)

    @property
    def pctError(self) -> float:
        """
        DSS property name: %Error
        DSS property index: 11
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @pctError.setter
    def pctError(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def Weight(self) -> float:
        """
        DSS property name: Weight
        DSS property index: 12
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @Weight.setter
    def Weight(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def basefreq(self) -> float:
        """
        DSS property name: basefreq
        DSS property index: 13
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @basefreq.setter
    def basefreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def enabled(self) -> bool:
        """
        DSS property name: enabled
        DSS property index: 14
        """
        return self._lib.Obj_GetInt32(self._ptr, 14) != 0

    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 14, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 15
        """
        self._set_string(15, value)

class LineCodeBatch(DSSBatch):
    _cls_name = 'LineCode'
    _obj_cls = LineCode
    _cls_idx = 1


    @property
    def nphases(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: nphases
        DSS property index: 1
        """
        return BatchInt32ArrayProxy(self, 1)

    @nphases.setter
    def nphases(self, value):
        self._set_batch_int32_array(1, value)

    @property
    def r1(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: r1
        DSS property index: 2
        """
        return BatchFloat64ArrayProxy(self, 2)

    @r1.setter
    def r1(self, value):
        self._set_batch_float64_array(2, value)

    @property
    def x1(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: x1
        DSS property index: 3
        """
        return BatchFloat64ArrayProxy(self, 3)

    @x1.setter
    def x1(self, value):
        self._set_batch_float64_array(3, value)

    @property
    def r0(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: r0
        DSS property index: 4
        """
        return BatchFloat64ArrayProxy(self, 4)

    @r0.setter
    def r0(self, value):
        self._set_batch_float64_array(4, value)

    @property
    def x0(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: x0
        DSS property index: 5
        """
        return BatchFloat64ArrayProxy(self, 5)

    @x0.setter
    def x0(self, value):
        self._set_batch_float64_array(5, value)

    @property
    def C1(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: C1
        DSS property index: 6
        """
        return BatchFloat64ArrayProxy(self, 6)

    @C1.setter
    def C1(self, value):
        self._set_batch_float64_array(6, value)

    @property
    def C0(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: C0
        DSS property index: 7
        """
        return BatchFloat64ArrayProxy(self, 7)

    @C0.setter
    def C0(self, value):
        self._set_batch_float64_array(7, value)

    @property
    def units(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: units
        DSS property index: 8
        """
        return BatchInt32ArrayProxy(self, 8)

    @units.setter
    def units(self, value: Union[AnyStr, int, DimensionUnits, List[AnyStr], List[Union[int, DimensionUnits]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(8, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(8, value)

    @property
    def units_str(self) -> str:
        """
        DSS property name: units
        DSS property index: 8
        """
        return self._get_prop_string(8)

    @units_str.setter
    def units_str(self, value: AnyStr):
        self.units = value

    @property
    def rmatrix(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: rmatrix
        DSS property index: 9
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 9)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @rmatrix.setter
    def rmatrix(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(9, value)

    @property
    def xmatrix(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: xmatrix
        DSS property index: 10
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 10)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @xmatrix.setter
    def xmatrix(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(10, value)

    @property
    def cmatrix(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: cmatrix
        DSS property index: 11
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 11)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @cmatrix.setter
    def cmatrix(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(11, value)

    @property
    def baseFreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: baseFreq
        DSS property index: 12
        """
        return BatchFloat64ArrayProxy(self, 12)

    @baseFreq.setter
    def baseFreq(self, value):
        self._set_batch_float64_array(12, value)

    @property
    def normamps(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: normamps
        DSS property index: 13
        """
        return BatchFloat64ArrayProxy(self, 13)

    @normamps.setter
    def normamps(self, value):
        self._set_batch_float64_array(13, value)

    @property
    def emergamps(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: emergamps
        DSS property index: 14
        """
        return BatchFloat64ArrayProxy(self, 14)

    @emergamps.setter
    def emergamps(self, value):
        self._set_batch_float64_array(14, value)

    @property
    def faultrate(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: faultrate
        DSS property index: 15
        """
        return BatchFloat64ArrayProxy(self, 15)

    @faultrate.setter
    def faultrate(self, value):
        self._set_batch_float64_array(15, value)

    @property
    def pctperm(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: pctperm
        DSS property index: 16
        """
        return BatchFloat64ArrayProxy(self, 16)

    @pctperm.setter
    def pctperm(self, value):
        self._set_batch_float64_array(16, value)

    @property
    def repair(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: repair
        DSS property index: 17
        """
        return BatchFloat64ArrayProxy(self, 17)

    @repair.setter
    def repair(self, value):
        self._set_batch_float64_array(17, value)

    def Kron(self, value: bool):
        """
        DSS property name: Kron
        DSS property index: 18
        """
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 18, value)

    @property
    def Rg(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Rg
        DSS property index: 19
        """
        return BatchFloat64ArrayProxy(self, 19)

    @Rg.setter
    def Rg(self, value):
        self._set_batch_float64_array(19, value)

    @property
    def Xg(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Xg
        DSS property index: 20
        """
        return BatchFloat64ArrayProxy(self, 20)

    @Xg.setter
    def Xg(self, value):
        self._set_batch_float64_array(20, value)

    @property
    def rho(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: rho
        DSS property index: 21
        """
        return BatchFloat64ArrayProxy(self, 21)

    @rho.setter
    def rho(self, value):
        self._set_batch_float64_array(21, value)

    @property
    def neutral(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: neutral
        DSS property index: 22
        """
        return BatchInt32ArrayProxy(self, 22)

    @neutral.setter
    def neutral(self, value):
        self._set_batch_int32_array(22, value)

    @property
    def B1(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: B1
        DSS property index: 23
        """
        return BatchFloat64ArrayProxy(self, 23)

    @B1.setter
    def B1(self, value):
        self._set_batch_float64_array(23, value)

    @property
    def B0(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: B0
        DSS property index: 24
        """
        return BatchFloat64ArrayProxy(self, 24)

    @B0.setter
    def B0(self, value):
        self._set_batch_float64_array(24, value)

    @property
    def Seasons(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Seasons
        DSS property index: 25
        """
        return BatchInt32ArrayProxy(self, 25)

    @Seasons.setter
    def Seasons(self, value):
        self._set_batch_int32_array(25, value)

    @property
    def Ratings(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: Ratings
        DSS property index: 26
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 26)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Ratings.setter
    def Ratings(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(26, value)

    @property
    def linetype(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: LineType
        DSS property index: 27
        """
        return BatchInt32ArrayProxy(self, 27)

    @linetype.setter
    def linetype(self, value: Union[AnyStr, int, LineType, List[AnyStr], List[Union[int, LineType]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(27, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(27, value)

    @property
    def linetype_str(self) -> str:
        """
        DSS property name: LineType
        DSS property index: 27
        """
        return self._get_prop_string(27)

    @linetype_str.setter
    def linetype_str(self, value: AnyStr):
        self.linetype = value

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 28
        """
        self._set_batch_string(28, value)

class LoadShapeBatch(DSSBatch):
    _cls_name = 'LoadShape'
    _obj_cls = LoadShape
    _cls_idx = 2


    @property
    def npts(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: npts
        DSS property index: 1
        """
        return BatchInt32ArrayProxy(self, 1)

    @npts.setter
    def npts(self, value):
        self._set_batch_int32_array(1, value)

    @property
    def interval(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: interval
        DSS property index: 2
        """
        return BatchFloat64ArrayProxy(self, 2)

    @interval.setter
    def interval(self, value):
        self._set_batch_float64_array(2, value)

    @property
    def mult(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: mult
        DSS property index: 3
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 3)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @mult.setter
    def mult(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(3, value)

    @property
    def hour(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: hour
        DSS property index: 4
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 4)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @hour.setter
    def hour(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(4, value)

    @property
    def mean(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: mean
        DSS property index: 5
        """
        return BatchFloat64ArrayProxy(self, 5)

    @mean.setter
    def mean(self, value):
        self._set_batch_float64_array(5, value)

    @property
    def stddev(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: stddev
        DSS property index: 6
        """
        return BatchFloat64ArrayProxy(self, 6)

    @stddev.setter
    def stddev(self, value):
        self._set_batch_float64_array(6, value)

    @property
    def csvfile(self) -> List[str]:
        """
        DSS property name: csvfile
        DSS property index: 7
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 7) 

    @csvfile.setter
    def csvfile(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 7, value)

    @property
    def sngfile(self) -> List[str]:
        """
        DSS property name: sngfile
        DSS property index: 8
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 8) 

    @sngfile.setter
    def sngfile(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 8, value)

    @property
    def dblfile(self) -> List[str]:
        """
        DSS property name: dblfile
        DSS property index: 9
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 9) 

    @dblfile.setter
    def dblfile(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 9, value)

    def action(self, value: Union[str, bytes, int]):
        """
        DSS property name: action
        DSS property index: 10
        """
        if isinstance(value, int):
            self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 10, value)
        else:
            self._set_batch_string(10, value)

    @property
    def qmult(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: qmult
        DSS property index: 11
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 11)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @qmult.setter
    def qmult(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(11, value)

    @property
    def UseActual(self) -> List[bool]:
        """
        DSS property name: UseActual
        DSS property index: 12
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 12)
        ]
    @UseActual.setter
    def UseActual(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 12, value)

    @property
    def Pmax(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Pmax
        DSS property index: 13
        """
        return BatchFloat64ArrayProxy(self, 13)

    @Pmax.setter
    def Pmax(self, value):
        self._set_batch_float64_array(13, value)

    @property
    def Qmax(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Qmax
        DSS property index: 14
        """
        return BatchFloat64ArrayProxy(self, 14)

    @Qmax.setter
    def Qmax(self, value):
        self._set_batch_float64_array(14, value)

    @property
    def sinterval(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: sinterval
        DSS property index: 15
        """
        return BatchFloat64ArrayProxy(self, 15)

    @sinterval.setter
    def sinterval(self, value):
        self._set_batch_float64_array(15, value)

    @property
    def minterval(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: minterval
        DSS property index: 16
        """
        return BatchFloat64ArrayProxy(self, 16)

    @minterval.setter
    def minterval(self, value):
        self._set_batch_float64_array(16, value)

    @property
    def Pbase(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Pbase
        DSS property index: 17
        """
        return BatchFloat64ArrayProxy(self, 17)

    @Pbase.setter
    def Pbase(self, value):
        self._set_batch_float64_array(17, value)

    @property
    def Qbase(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Qbase
        DSS property index: 18
        """
        return BatchFloat64ArrayProxy(self, 18)

    @Qbase.setter
    def Qbase(self, value):
        self._set_batch_float64_array(18, value)

    @property
    def Pmult(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: Pmult
        DSS property index: 19
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 19)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Pmult.setter
    def Pmult(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(19, value)

    @property
    def PQCSVFile(self) -> List[str]:
        """
        DSS property name: PQCSVFile
        DSS property index: 20
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 20) 

    @PQCSVFile.setter
    def PQCSVFile(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 20, value)

    @property
    def MemoryMapping(self) -> List[bool]:
        """
        DSS property name: MemoryMapping
        DSS property index: 21
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 21)
        ]
    @MemoryMapping.setter
    def MemoryMapping(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 21, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 22
        """
        self._set_batch_string(22, value)

class TShapeBatch(DSSBatch):
    _cls_name = 'TShape'
    _obj_cls = TShape
    _cls_idx = 3


    @property
    def npts(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: npts
        DSS property index: 1
        """
        return BatchInt32ArrayProxy(self, 1)

    @npts.setter
    def npts(self, value):
        self._set_batch_int32_array(1, value)

    @property
    def interval(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: interval
        DSS property index: 2
        """
        return BatchFloat64ArrayProxy(self, 2)

    @interval.setter
    def interval(self, value):
        self._set_batch_float64_array(2, value)

    @property
    def temp(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: temp
        DSS property index: 3
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 3)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @temp.setter
    def temp(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(3, value)

    @property
    def hour(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: hour
        DSS property index: 4
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 4)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @hour.setter
    def hour(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(4, value)

    @property
    def mean(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: mean
        DSS property index: 5
        """
        return BatchFloat64ArrayProxy(self, 5)

    @mean.setter
    def mean(self, value):
        self._set_batch_float64_array(5, value)

    @property
    def stddev(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: stddev
        DSS property index: 6
        """
        return BatchFloat64ArrayProxy(self, 6)

    @stddev.setter
    def stddev(self, value):
        self._set_batch_float64_array(6, value)

    @property
    def csvfile(self) -> List[str]:
        """
        DSS property name: csvfile
        DSS property index: 7
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 7) 

    @csvfile.setter
    def csvfile(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 7, value)

    @property
    def sngfile(self) -> List[str]:
        """
        DSS property name: sngfile
        DSS property index: 8
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 8) 

    @sngfile.setter
    def sngfile(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 8, value)

    @property
    def dblfile(self) -> List[str]:
        """
        DSS property name: dblfile
        DSS property index: 9
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 9) 

    @dblfile.setter
    def dblfile(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 9, value)

    @property
    def sinterval(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: sinterval
        DSS property index: 10
        """
        return BatchFloat64ArrayProxy(self, 10)

    @sinterval.setter
    def sinterval(self, value):
        self._set_batch_float64_array(10, value)

    @property
    def minterval(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: minterval
        DSS property index: 11
        """
        return BatchFloat64ArrayProxy(self, 11)

    @minterval.setter
    def minterval(self, value):
        self._set_batch_float64_array(11, value)

    def action(self, value: Union[str, bytes, int]):
        """
        DSS property name: action
        DSS property index: 12
        """
        if isinstance(value, int):
            self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 12, value)
        else:
            self._set_batch_string(12, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 13
        """
        self._set_batch_string(13, value)

class PriceShapeBatch(DSSBatch):
    _cls_name = 'PriceShape'
    _obj_cls = PriceShape
    _cls_idx = 4


    @property
    def npts(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: npts
        DSS property index: 1
        """
        return BatchInt32ArrayProxy(self, 1)

    @npts.setter
    def npts(self, value):
        self._set_batch_int32_array(1, value)

    @property
    def interval(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: interval
        DSS property index: 2
        """
        return BatchFloat64ArrayProxy(self, 2)

    @interval.setter
    def interval(self, value):
        self._set_batch_float64_array(2, value)

    @property
    def price(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: price
        DSS property index: 3
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 3)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @price.setter
    def price(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(3, value)

    @property
    def hour(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: hour
        DSS property index: 4
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 4)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @hour.setter
    def hour(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(4, value)

    @property
    def mean(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: mean
        DSS property index: 5
        """
        return BatchFloat64ArrayProxy(self, 5)

    @mean.setter
    def mean(self, value):
        self._set_batch_float64_array(5, value)

    @property
    def stddev(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: stddev
        DSS property index: 6
        """
        return BatchFloat64ArrayProxy(self, 6)

    @stddev.setter
    def stddev(self, value):
        self._set_batch_float64_array(6, value)

    @property
    def csvfile(self) -> List[str]:
        """
        DSS property name: csvfile
        DSS property index: 7
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 7) 

    @csvfile.setter
    def csvfile(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 7, value)

    @property
    def sngfile(self) -> List[str]:
        """
        DSS property name: sngfile
        DSS property index: 8
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 8) 

    @sngfile.setter
    def sngfile(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 8, value)

    @property
    def dblfile(self) -> List[str]:
        """
        DSS property name: dblfile
        DSS property index: 9
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 9) 

    @dblfile.setter
    def dblfile(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 9, value)

    @property
    def sinterval(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: sinterval
        DSS property index: 10
        """
        return BatchFloat64ArrayProxy(self, 10)

    @sinterval.setter
    def sinterval(self, value):
        self._set_batch_float64_array(10, value)

    @property
    def minterval(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: minterval
        DSS property index: 11
        """
        return BatchFloat64ArrayProxy(self, 11)

    @minterval.setter
    def minterval(self, value):
        self._set_batch_float64_array(11, value)

    def action(self, value: Union[str, bytes, int]):
        """
        DSS property name: action
        DSS property index: 12
        """
        if isinstance(value, int):
            self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 12, value)
        else:
            self._set_batch_string(12, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 13
        """
        self._set_batch_string(13, value)

class XYcurveBatch(DSSBatch):
    _cls_name = 'XYcurve'
    _obj_cls = XYcurve
    _cls_idx = 5


    @property
    def npts(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: npts
        DSS property index: 1
        """
        return BatchInt32ArrayProxy(self, 1)

    @npts.setter
    def npts(self, value):
        self._set_batch_int32_array(1, value)

    @property
    def Points(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: Points
        DSS property index: 2
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 2)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Points.setter
    def Points(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(2, value)

    @property
    def Yarray(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: Yarray
        DSS property index: 3
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 3)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Yarray.setter
    def Yarray(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(3, value)

    @property
    def Xarray(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: Xarray
        DSS property index: 4
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 4)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Xarray.setter
    def Xarray(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(4, value)

    @property
    def csvfile(self) -> List[str]:
        """
        DSS property name: csvfile
        DSS property index: 5
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 5) 

    @csvfile.setter
    def csvfile(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 5, value)

    @property
    def sngfile(self) -> List[str]:
        """
        DSS property name: sngfile
        DSS property index: 6
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 6) 

    @sngfile.setter
    def sngfile(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 6, value)

    @property
    def dblfile(self) -> List[str]:
        """
        DSS property name: dblfile
        DSS property index: 7
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 7) 

    @dblfile.setter
    def dblfile(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 7, value)

    @property
    def x(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: x
        DSS property index: 8
        """
        return BatchFloat64ArrayProxy(self, 8)

    @x.setter
    def x(self, value):
        self._set_batch_float64_array(8, value)

    @property
    def y(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: y
        DSS property index: 9
        """
        return BatchFloat64ArrayProxy(self, 9)

    @y.setter
    def y(self, value):
        self._set_batch_float64_array(9, value)

    @property
    def Xshift(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Xshift
        DSS property index: 10
        """
        return BatchFloat64ArrayProxy(self, 10)

    @Xshift.setter
    def Xshift(self, value):
        self._set_batch_float64_array(10, value)

    @property
    def Yshift(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Yshift
        DSS property index: 11
        """
        return BatchFloat64ArrayProxy(self, 11)

    @Yshift.setter
    def Yshift(self, value):
        self._set_batch_float64_array(11, value)

    @property
    def Xscale(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Xscale
        DSS property index: 12
        """
        return BatchFloat64ArrayProxy(self, 12)

    @Xscale.setter
    def Xscale(self, value):
        self._set_batch_float64_array(12, value)

    @property
    def Yscale(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Yscale
        DSS property index: 13
        """
        return BatchFloat64ArrayProxy(self, 13)

    @Yscale.setter
    def Yscale(self, value):
        self._set_batch_float64_array(13, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 14
        """
        self._set_batch_string(14, value)

class GrowthShapeBatch(DSSBatch):
    _cls_name = 'GrowthShape'
    _obj_cls = GrowthShape
    _cls_idx = 6


    @property
    def npts(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: npts
        DSS property index: 1
        """
        return BatchInt32ArrayProxy(self, 1)

    @npts.setter
    def npts(self, value):
        self._set_batch_int32_array(1, value)

    @property
    def year(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: year
        DSS property index: 2
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 2)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @year.setter
    def year(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(2, value)

    @property
    def mult(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: mult
        DSS property index: 3
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 3)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @mult.setter
    def mult(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(3, value)

    @property
    def csvfile(self) -> List[str]:
        """
        DSS property name: csvfile
        DSS property index: 4
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 4) 

    @csvfile.setter
    def csvfile(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 4, value)

    @property
    def sngfile(self) -> List[str]:
        """
        DSS property name: sngfile
        DSS property index: 5
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 5) 

    @sngfile.setter
    def sngfile(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 5, value)

    @property
    def dblfile(self) -> List[str]:
        """
        DSS property name: dblfile
        DSS property index: 6
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 6) 

    @dblfile.setter
    def dblfile(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 6, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 7
        """
        self._set_batch_string(7, value)

class TCC_CurveBatch(DSSBatch):
    _cls_name = 'TCC_Curve'
    _obj_cls = TCC_Curve
    _cls_idx = 7


    @property
    def npts(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: npts
        DSS property index: 1
        """
        return BatchInt32ArrayProxy(self, 1)

    @npts.setter
    def npts(self, value):
        self._set_batch_int32_array(1, value)

    @property
    def C_array(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: C_array
        DSS property index: 2
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 2)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @C_array.setter
    def C_array(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(2, value)

    @property
    def T_array(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: T_array
        DSS property index: 3
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 3)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @T_array.setter
    def T_array(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(3, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 4
        """
        self._set_batch_string(4, value)

class SpectrumBatch(DSSBatch):
    _cls_name = 'Spectrum'
    _obj_cls = Spectrum
    _cls_idx = 8


    @property
    def NumHarm(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: NumHarm
        DSS property index: 1
        """
        return BatchInt32ArrayProxy(self, 1)

    @NumHarm.setter
    def NumHarm(self, value):
        self._set_batch_int32_array(1, value)

    @property
    def harmonic(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: harmonic
        DSS property index: 2
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 2)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @harmonic.setter
    def harmonic(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(2, value)

    @property
    def pctmag(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: %mag
        DSS property index: 3
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 3)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @pctmag.setter
    def pctmag(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(3, value)

    @property
    def angle(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: angle
        DSS property index: 4
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 4)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @angle.setter
    def angle(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(4, value)

    @property
    def CSVFile(self) -> List[str]:
        """
        DSS property name: CSVFile
        DSS property index: 5
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 5) 

    @CSVFile.setter
    def CSVFile(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 5, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 6
        """
        self._set_batch_string(6, value)

class WireDataBatch(DSSBatch):
    _cls_name = 'WireData'
    _obj_cls = WireData
    _cls_idx = 9


    @property
    def Rdc(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Rdc
        DSS property index: 1
        """
        return BatchFloat64ArrayProxy(self, 1)

    @Rdc.setter
    def Rdc(self, value):
        self._set_batch_float64_array(1, value)

    @property
    def Rac(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Rac
        DSS property index: 2
        """
        return BatchFloat64ArrayProxy(self, 2)

    @Rac.setter
    def Rac(self, value):
        self._set_batch_float64_array(2, value)

    @property
    def Runits(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Runits
        DSS property index: 3
        """
        return BatchInt32ArrayProxy(self, 3)

    @Runits.setter
    def Runits(self, value: Union[AnyStr, int, DimensionUnits, List[AnyStr], List[Union[int, DimensionUnits]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(3, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(3, value)

    @property
    def Runits_str(self) -> str:
        """
        DSS property name: Runits
        DSS property index: 3
        """
        return self._get_prop_string(3)

    @Runits_str.setter
    def Runits_str(self, value: AnyStr):
        self.Runits = value

    @property
    def GMRac(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: GMRac
        DSS property index: 4
        """
        return BatchFloat64ArrayProxy(self, 4)

    @GMRac.setter
    def GMRac(self, value):
        self._set_batch_float64_array(4, value)

    @property
    def GMRunits(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: GMRunits
        DSS property index: 5
        """
        return BatchInt32ArrayProxy(self, 5)

    @GMRunits.setter
    def GMRunits(self, value: Union[AnyStr, int, DimensionUnits, List[AnyStr], List[Union[int, DimensionUnits]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(5, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(5, value)

    @property
    def GMRunits_str(self) -> str:
        """
        DSS property name: GMRunits
        DSS property index: 5
        """
        return self._get_prop_string(5)

    @GMRunits_str.setter
    def GMRunits_str(self, value: AnyStr):
        self.GMRunits = value

    @property
    def radius(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: radius
        DSS property index: 6
        """
        return BatchFloat64ArrayProxy(self, 6)

    @radius.setter
    def radius(self, value):
        self._set_batch_float64_array(6, value)

    @property
    def radunits(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: radunits
        DSS property index: 7
        """
        return BatchInt32ArrayProxy(self, 7)

    @radunits.setter
    def radunits(self, value: Union[AnyStr, int, DimensionUnits, List[AnyStr], List[Union[int, DimensionUnits]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(7, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(7, value)

    @property
    def radunits_str(self) -> str:
        """
        DSS property name: radunits
        DSS property index: 7
        """
        return self._get_prop_string(7)

    @radunits_str.setter
    def radunits_str(self, value: AnyStr):
        self.radunits = value

    @property
    def normamps(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: normamps
        DSS property index: 8
        """
        return BatchFloat64ArrayProxy(self, 8)

    @normamps.setter
    def normamps(self, value):
        self._set_batch_float64_array(8, value)

    @property
    def emergamps(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: emergamps
        DSS property index: 9
        """
        return BatchFloat64ArrayProxy(self, 9)

    @emergamps.setter
    def emergamps(self, value):
        self._set_batch_float64_array(9, value)

    @property
    def diam(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: diam
        DSS property index: 10
        """
        return BatchFloat64ArrayProxy(self, 10)

    @diam.setter
    def diam(self, value):
        self._set_batch_float64_array(10, value)

    @property
    def Seasons(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Seasons
        DSS property index: 11
        """
        return BatchInt32ArrayProxy(self, 11)

    @Seasons.setter
    def Seasons(self, value):
        self._set_batch_int32_array(11, value)

    @property
    def Ratings(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: Ratings
        DSS property index: 12
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 12)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Ratings.setter
    def Ratings(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(12, value)

    @property
    def Capradius(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Capradius
        DSS property index: 13
        """
        return BatchFloat64ArrayProxy(self, 13)

    @Capradius.setter
    def Capradius(self, value):
        self._set_batch_float64_array(13, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 14
        """
        self._set_batch_string(14, value)

class CNDataBatch(DSSBatch):
    _cls_name = 'CNData'
    _obj_cls = CNData
    _cls_idx = 10


    @property
    def k(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: k
        DSS property index: 1
        """
        return BatchInt32ArrayProxy(self, 1)

    @k.setter
    def k(self, value):
        self._set_batch_int32_array(1, value)

    @property
    def DiaStrand(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: DiaStrand
        DSS property index: 2
        """
        return BatchFloat64ArrayProxy(self, 2)

    @DiaStrand.setter
    def DiaStrand(self, value):
        self._set_batch_float64_array(2, value)

    @property
    def GmrStrand(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: GmrStrand
        DSS property index: 3
        """
        return BatchFloat64ArrayProxy(self, 3)

    @GmrStrand.setter
    def GmrStrand(self, value):
        self._set_batch_float64_array(3, value)

    @property
    def Rstrand(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Rstrand
        DSS property index: 4
        """
        return BatchFloat64ArrayProxy(self, 4)

    @Rstrand.setter
    def Rstrand(self, value):
        self._set_batch_float64_array(4, value)

    @property
    def EpsR(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: EpsR
        DSS property index: 5
        """
        return BatchFloat64ArrayProxy(self, 5)

    @EpsR.setter
    def EpsR(self, value):
        self._set_batch_float64_array(5, value)

    @property
    def InsLayer(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: InsLayer
        DSS property index: 6
        """
        return BatchFloat64ArrayProxy(self, 6)

    @InsLayer.setter
    def InsLayer(self, value):
        self._set_batch_float64_array(6, value)

    @property
    def DiaIns(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: DiaIns
        DSS property index: 7
        """
        return BatchFloat64ArrayProxy(self, 7)

    @DiaIns.setter
    def DiaIns(self, value):
        self._set_batch_float64_array(7, value)

    @property
    def DiaCable(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: DiaCable
        DSS property index: 8
        """
        return BatchFloat64ArrayProxy(self, 8)

    @DiaCable.setter
    def DiaCable(self, value):
        self._set_batch_float64_array(8, value)

    @property
    def Rdc(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Rdc
        DSS property index: 9
        """
        return BatchFloat64ArrayProxy(self, 9)

    @Rdc.setter
    def Rdc(self, value):
        self._set_batch_float64_array(9, value)

    @property
    def Rac(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Rac
        DSS property index: 10
        """
        return BatchFloat64ArrayProxy(self, 10)

    @Rac.setter
    def Rac(self, value):
        self._set_batch_float64_array(10, value)

    @property
    def Runits(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Runits
        DSS property index: 11
        """
        return BatchInt32ArrayProxy(self, 11)

    @Runits.setter
    def Runits(self, value: Union[AnyStr, int, DimensionUnits, List[AnyStr], List[Union[int, DimensionUnits]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(11, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(11, value)

    @property
    def Runits_str(self) -> str:
        """
        DSS property name: Runits
        DSS property index: 11
        """
        return self._get_prop_string(11)

    @Runits_str.setter
    def Runits_str(self, value: AnyStr):
        self.Runits = value

    @property
    def GMRac(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: GMRac
        DSS property index: 12
        """
        return BatchFloat64ArrayProxy(self, 12)

    @GMRac.setter
    def GMRac(self, value):
        self._set_batch_float64_array(12, value)

    @property
    def GMRunits(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: GMRunits
        DSS property index: 13
        """
        return BatchInt32ArrayProxy(self, 13)

    @GMRunits.setter
    def GMRunits(self, value: Union[AnyStr, int, DimensionUnits, List[AnyStr], List[Union[int, DimensionUnits]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(13, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(13, value)

    @property
    def GMRunits_str(self) -> str:
        """
        DSS property name: GMRunits
        DSS property index: 13
        """
        return self._get_prop_string(13)

    @GMRunits_str.setter
    def GMRunits_str(self, value: AnyStr):
        self.GMRunits = value

    @property
    def radius(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: radius
        DSS property index: 14
        """
        return BatchFloat64ArrayProxy(self, 14)

    @radius.setter
    def radius(self, value):
        self._set_batch_float64_array(14, value)

    @property
    def radunits(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: radunits
        DSS property index: 15
        """
        return BatchInt32ArrayProxy(self, 15)

    @radunits.setter
    def radunits(self, value: Union[AnyStr, int, DimensionUnits, List[AnyStr], List[Union[int, DimensionUnits]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(15, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(15, value)

    @property
    def radunits_str(self) -> str:
        """
        DSS property name: radunits
        DSS property index: 15
        """
        return self._get_prop_string(15)

    @radunits_str.setter
    def radunits_str(self, value: AnyStr):
        self.radunits = value

    @property
    def normamps(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: normamps
        DSS property index: 16
        """
        return BatchFloat64ArrayProxy(self, 16)

    @normamps.setter
    def normamps(self, value):
        self._set_batch_float64_array(16, value)

    @property
    def emergamps(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: emergamps
        DSS property index: 17
        """
        return BatchFloat64ArrayProxy(self, 17)

    @emergamps.setter
    def emergamps(self, value):
        self._set_batch_float64_array(17, value)

    @property
    def diam(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: diam
        DSS property index: 18
        """
        return BatchFloat64ArrayProxy(self, 18)

    @diam.setter
    def diam(self, value):
        self._set_batch_float64_array(18, value)

    @property
    def Seasons(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Seasons
        DSS property index: 19
        """
        return BatchInt32ArrayProxy(self, 19)

    @Seasons.setter
    def Seasons(self, value):
        self._set_batch_int32_array(19, value)

    @property
    def Ratings(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: Ratings
        DSS property index: 20
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 20)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Ratings.setter
    def Ratings(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(20, value)

    @property
    def Capradius(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Capradius
        DSS property index: 21
        """
        return BatchFloat64ArrayProxy(self, 21)

    @Capradius.setter
    def Capradius(self, value):
        self._set_batch_float64_array(21, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 22
        """
        self._set_batch_string(22, value)

class TSDataBatch(DSSBatch):
    _cls_name = 'TSData'
    _obj_cls = TSData
    _cls_idx = 11


    @property
    def DiaShield(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: DiaShield
        DSS property index: 1
        """
        return BatchFloat64ArrayProxy(self, 1)

    @DiaShield.setter
    def DiaShield(self, value):
        self._set_batch_float64_array(1, value)

    @property
    def TapeLayer(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: TapeLayer
        DSS property index: 2
        """
        return BatchFloat64ArrayProxy(self, 2)

    @TapeLayer.setter
    def TapeLayer(self, value):
        self._set_batch_float64_array(2, value)

    @property
    def TapeLap(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: TapeLap
        DSS property index: 3
        """
        return BatchFloat64ArrayProxy(self, 3)

    @TapeLap.setter
    def TapeLap(self, value):
        self._set_batch_float64_array(3, value)

    @property
    def EpsR(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: EpsR
        DSS property index: 4
        """
        return BatchFloat64ArrayProxy(self, 4)

    @EpsR.setter
    def EpsR(self, value):
        self._set_batch_float64_array(4, value)

    @property
    def InsLayer(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: InsLayer
        DSS property index: 5
        """
        return BatchFloat64ArrayProxy(self, 5)

    @InsLayer.setter
    def InsLayer(self, value):
        self._set_batch_float64_array(5, value)

    @property
    def DiaIns(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: DiaIns
        DSS property index: 6
        """
        return BatchFloat64ArrayProxy(self, 6)

    @DiaIns.setter
    def DiaIns(self, value):
        self._set_batch_float64_array(6, value)

    @property
    def DiaCable(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: DiaCable
        DSS property index: 7
        """
        return BatchFloat64ArrayProxy(self, 7)

    @DiaCable.setter
    def DiaCable(self, value):
        self._set_batch_float64_array(7, value)

    @property
    def Rdc(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Rdc
        DSS property index: 8
        """
        return BatchFloat64ArrayProxy(self, 8)

    @Rdc.setter
    def Rdc(self, value):
        self._set_batch_float64_array(8, value)

    @property
    def Rac(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Rac
        DSS property index: 9
        """
        return BatchFloat64ArrayProxy(self, 9)

    @Rac.setter
    def Rac(self, value):
        self._set_batch_float64_array(9, value)

    @property
    def Runits(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Runits
        DSS property index: 10
        """
        return BatchInt32ArrayProxy(self, 10)

    @Runits.setter
    def Runits(self, value: Union[AnyStr, int, DimensionUnits, List[AnyStr], List[Union[int, DimensionUnits]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(10, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(10, value)

    @property
    def Runits_str(self) -> str:
        """
        DSS property name: Runits
        DSS property index: 10
        """
        return self._get_prop_string(10)

    @Runits_str.setter
    def Runits_str(self, value: AnyStr):
        self.Runits = value

    @property
    def GMRac(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: GMRac
        DSS property index: 11
        """
        return BatchFloat64ArrayProxy(self, 11)

    @GMRac.setter
    def GMRac(self, value):
        self._set_batch_float64_array(11, value)

    @property
    def GMRunits(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: GMRunits
        DSS property index: 12
        """
        return BatchInt32ArrayProxy(self, 12)

    @GMRunits.setter
    def GMRunits(self, value: Union[AnyStr, int, DimensionUnits, List[AnyStr], List[Union[int, DimensionUnits]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(12, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(12, value)

    @property
    def GMRunits_str(self) -> str:
        """
        DSS property name: GMRunits
        DSS property index: 12
        """
        return self._get_prop_string(12)

    @GMRunits_str.setter
    def GMRunits_str(self, value: AnyStr):
        self.GMRunits = value

    @property
    def radius(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: radius
        DSS property index: 13
        """
        return BatchFloat64ArrayProxy(self, 13)

    @radius.setter
    def radius(self, value):
        self._set_batch_float64_array(13, value)

    @property
    def radunits(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: radunits
        DSS property index: 14
        """
        return BatchInt32ArrayProxy(self, 14)

    @radunits.setter
    def radunits(self, value: Union[AnyStr, int, DimensionUnits, List[AnyStr], List[Union[int, DimensionUnits]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(14, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(14, value)

    @property
    def radunits_str(self) -> str:
        """
        DSS property name: radunits
        DSS property index: 14
        """
        return self._get_prop_string(14)

    @radunits_str.setter
    def radunits_str(self, value: AnyStr):
        self.radunits = value

    @property
    def normamps(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: normamps
        DSS property index: 15
        """
        return BatchFloat64ArrayProxy(self, 15)

    @normamps.setter
    def normamps(self, value):
        self._set_batch_float64_array(15, value)

    @property
    def emergamps(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: emergamps
        DSS property index: 16
        """
        return BatchFloat64ArrayProxy(self, 16)

    @emergamps.setter
    def emergamps(self, value):
        self._set_batch_float64_array(16, value)

    @property
    def diam(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: diam
        DSS property index: 17
        """
        return BatchFloat64ArrayProxy(self, 17)

    @diam.setter
    def diam(self, value):
        self._set_batch_float64_array(17, value)

    @property
    def Seasons(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Seasons
        DSS property index: 18
        """
        return BatchInt32ArrayProxy(self, 18)

    @Seasons.setter
    def Seasons(self, value):
        self._set_batch_int32_array(18, value)

    @property
    def Ratings(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: Ratings
        DSS property index: 19
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 19)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Ratings.setter
    def Ratings(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(19, value)

    @property
    def Capradius(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Capradius
        DSS property index: 20
        """
        return BatchFloat64ArrayProxy(self, 20)

    @Capradius.setter
    def Capradius(self, value):
        self._set_batch_float64_array(20, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 21
        """
        self._set_batch_string(21, value)

class LineSpacingBatch(DSSBatch):
    _cls_name = 'LineSpacing'
    _obj_cls = LineSpacing
    _cls_idx = 12


    @property
    def nconds(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: nconds
        DSS property index: 1
        """
        return BatchInt32ArrayProxy(self, 1)

    @nconds.setter
    def nconds(self, value):
        self._set_batch_int32_array(1, value)

    @property
    def nphases(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: nphases
        DSS property index: 2
        """
        return BatchInt32ArrayProxy(self, 2)

    @nphases.setter
    def nphases(self, value):
        self._set_batch_int32_array(2, value)

    @property
    def x(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: x
        DSS property index: 3
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 3)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @x.setter
    def x(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(3, value)

    @property
    def h(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: h
        DSS property index: 4
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 4)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @h.setter
    def h(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(4, value)

    @property
    def units(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: units
        DSS property index: 5
        """
        return BatchInt32ArrayProxy(self, 5)

    @units.setter
    def units(self, value: Union[AnyStr, int, DimensionUnits, List[AnyStr], List[Union[int, DimensionUnits]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(5, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(5, value)

    @property
    def units_str(self) -> str:
        """
        DSS property name: units
        DSS property index: 5
        """
        return self._get_prop_string(5)

    @units_str.setter
    def units_str(self, value: AnyStr):
        self.units = value

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 6
        """
        self._set_batch_string(6, value)

class LineGeometryBatch(DSSBatch):
    _cls_name = 'LineGeometry'
    _obj_cls = LineGeometry
    _cls_idx = 13


    @property
    def nconds(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: nconds
        DSS property index: 1
        """
        return BatchInt32ArrayProxy(self, 1)

    @nconds.setter
    def nconds(self, value):
        self._set_batch_int32_array(1, value)

    @property
    def nphases(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: nphases
        DSS property index: 2
        """
        return BatchInt32ArrayProxy(self, 2)

    @nphases.setter
    def nphases(self, value):
        self._set_batch_int32_array(2, value)

    @property
    def cond(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: cond
        DSS property index: 3
        """
        return BatchInt32ArrayProxy(self, 3)

    @cond.setter
    def cond(self, value):
        self._set_batch_int32_array(3, value)

    @property
    def wire(self) -> List[List[str]]:
        """
        DSS property name: wire
        DSS property index: 4
        """
        return self._get_string_ll(4)

    @wire.setter
    def wire(self, value: Union[List[Union[AnyStr, WireData]], List[List[Union[AnyStr, WireData]]]]):
        if not len(value):
            return

        if isinstance(value[0], (bytes, str)):
            value, value_ptr, value_count = self._prepare_string_array(value)
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetStringArray(x, 4, value_ptr, value_count)

            self._check_for_error()
            return

        self._set_batch_obj_array(4, value)

    @property
    def wire_obj(self) -> List[List[WireData]]:
        """
        DSS property name: wire
        DSS property index: 4
        """
        return self._get_batch_obj_array(4, WireData)

    @wire_obj.setter
    def wire_obj(self, value: Union[List[WireData], List[List[WireData]]]):
        self._set_batch_obj_array(4, value)

    @property
    def x(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: x
        DSS property index: 5
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 5)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @x.setter
    def x(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(5, value)

    @property
    def h(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: h
        DSS property index: 6
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 6)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @h.setter
    def h(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(6, value)

    @property
    def units(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: units
        DSS property index: 7
        """
        return BatchInt32ArrayProxy(self, 7)

    @units.setter
    def units(self, value: Union[AnyStr, int, DimensionUnits, List[AnyStr], List[Union[int, DimensionUnits]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(7, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(7, value)

    @property
    def units_str(self) -> str:
        """
        DSS property name: units
        DSS property index: 7
        """
        return self._get_prop_string(7)

    @units_str.setter
    def units_str(self, value: AnyStr):
        self.units = value

    @property
    def normamps(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: normamps
        DSS property index: 8
        """
        return BatchFloat64ArrayProxy(self, 8)

    @normamps.setter
    def normamps(self, value):
        self._set_batch_float64_array(8, value)

    @property
    def emergamps(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: emergamps
        DSS property index: 9
        """
        return BatchFloat64ArrayProxy(self, 9)

    @emergamps.setter
    def emergamps(self, value):
        self._set_batch_float64_array(9, value)

    @property
    def reduce(self) -> List[bool]:
        """
        DSS property name: reduce
        DSS property index: 10
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 10)
        ]
    @reduce.setter
    def reduce(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 10, value)

    @property
    def spacing(self) -> List[str]:
        """
        DSS property name: spacing
        DSS property index: 11
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 11)

    @spacing.setter
    def spacing(self, value: Union[AnyStr, LineSpacing]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(11, value)
            return

        self._set_batch_string(11, value)

    @property
    def spacing_obj(self) -> List[str]:
        """
        DSS property name: spacing
        DSS property index: 11
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 11)

    @spacing_obj.setter
    def spacing_obj(self, value: LineSpacing):
        self._set_batch_string(11, value)

    @property
    def wires(self) -> List[List[str]]:
        """
        DSS property name: wires
        DSS property index: 12
        """
        return self._get_string_ll(12)

    @wires.setter
    def wires(self, value: Union[List[Union[AnyStr, WireData]], List[List[Union[AnyStr, WireData]]]]):
        if not len(value):
            return

        if isinstance(value[0], (bytes, str)):
            value, value_ptr, value_count = self._prepare_string_array(value)
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetStringArray(x, 12, value_ptr, value_count)

            self._check_for_error()
            return

        self._set_batch_obj_array(12, value)

    @property
    def wires_obj(self) -> List[List[WireData]]:
        """
        DSS property name: wires
        DSS property index: 12
        """
        return self._get_batch_obj_array(12, WireData)

    @wires_obj.setter
    def wires_obj(self, value: Union[List[WireData], List[List[WireData]]]):
        self._set_batch_obj_array(12, value)

    @property
    def cncable(self) -> List[List[str]]:
        """
        DSS property name: cncable
        DSS property index: 13
        """
        return self._get_string_ll(13)

    @cncable.setter
    def cncable(self, value: Union[List[Union[AnyStr, CNData]], List[List[Union[AnyStr, CNData]]]]):
        if not len(value):
            return

        if isinstance(value[0], (bytes, str)):
            value, value_ptr, value_count = self._prepare_string_array(value)
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetStringArray(x, 13, value_ptr, value_count)

            self._check_for_error()
            return

        self._set_batch_obj_array(13, value)

    @property
    def cncable_obj(self) -> List[List[CNData]]:
        """
        DSS property name: cncable
        DSS property index: 13
        """
        return self._get_batch_obj_array(13, CNData)

    @cncable_obj.setter
    def cncable_obj(self, value: Union[List[CNData], List[List[CNData]]]):
        self._set_batch_obj_array(13, value)

    @property
    def tscable(self) -> List[List[str]]:
        """
        DSS property name: tscable
        DSS property index: 14
        """
        return self._get_string_ll(14)

    @tscable.setter
    def tscable(self, value: Union[List[Union[AnyStr, TSData]], List[List[Union[AnyStr, TSData]]]]):
        if not len(value):
            return

        if isinstance(value[0], (bytes, str)):
            value, value_ptr, value_count = self._prepare_string_array(value)
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetStringArray(x, 14, value_ptr, value_count)

            self._check_for_error()
            return

        self._set_batch_obj_array(14, value)

    @property
    def tscable_obj(self) -> List[List[TSData]]:
        """
        DSS property name: tscable
        DSS property index: 14
        """
        return self._get_batch_obj_array(14, TSData)

    @tscable_obj.setter
    def tscable_obj(self, value: Union[List[TSData], List[List[TSData]]]):
        self._set_batch_obj_array(14, value)

    @property
    def cncables(self) -> List[List[str]]:
        """
        DSS property name: cncables
        DSS property index: 15
        """
        return self._get_string_ll(15)

    @cncables.setter
    def cncables(self, value: Union[List[Union[AnyStr, CNData]], List[List[Union[AnyStr, CNData]]]]):
        if not len(value):
            return

        if isinstance(value[0], (bytes, str)):
            value, value_ptr, value_count = self._prepare_string_array(value)
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetStringArray(x, 15, value_ptr, value_count)

            self._check_for_error()
            return

        self._set_batch_obj_array(15, value)

    @property
    def cncables_obj(self) -> List[List[CNData]]:
        """
        DSS property name: cncables
        DSS property index: 15
        """
        return self._get_batch_obj_array(15, CNData)

    @cncables_obj.setter
    def cncables_obj(self, value: Union[List[CNData], List[List[CNData]]]):
        self._set_batch_obj_array(15, value)

    @property
    def tscables(self) -> List[List[str]]:
        """
        DSS property name: tscables
        DSS property index: 16
        """
        return self._get_string_ll(16)

    @tscables.setter
    def tscables(self, value: Union[List[Union[AnyStr, TSData]], List[List[Union[AnyStr, TSData]]]]):
        if not len(value):
            return

        if isinstance(value[0], (bytes, str)):
            value, value_ptr, value_count = self._prepare_string_array(value)
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetStringArray(x, 16, value_ptr, value_count)

            self._check_for_error()
            return

        self._set_batch_obj_array(16, value)

    @property
    def tscables_obj(self) -> List[List[TSData]]:
        """
        DSS property name: tscables
        DSS property index: 16
        """
        return self._get_batch_obj_array(16, TSData)

    @tscables_obj.setter
    def tscables_obj(self, value: Union[List[TSData], List[List[TSData]]]):
        self._set_batch_obj_array(16, value)

    @property
    def Seasons(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Seasons
        DSS property index: 17
        """
        return BatchInt32ArrayProxy(self, 17)

    @Seasons.setter
    def Seasons(self, value):
        self._set_batch_int32_array(17, value)

    @property
    def Ratings(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: Ratings
        DSS property index: 18
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 18)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Ratings.setter
    def Ratings(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(18, value)

    @property
    def linetype(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: LineType
        DSS property index: 19
        """
        return BatchInt32ArrayProxy(self, 19)

    @linetype.setter
    def linetype(self, value: Union[AnyStr, int, LineType, List[AnyStr], List[Union[int, LineType]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(19, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(19, value)

    @property
    def linetype_str(self) -> str:
        """
        DSS property name: LineType
        DSS property index: 19
        """
        return self._get_prop_string(19)

    @linetype_str.setter
    def linetype_str(self, value: AnyStr):
        self.linetype = value

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 20
        """
        self._set_batch_string(20, value)

class XfmrCodeBatch(DSSBatch):
    _cls_name = 'XfmrCode'
    _obj_cls = XfmrCode
    _cls_idx = 14


    @property
    def phases(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: phases
        DSS property index: 1
        """
        return BatchInt32ArrayProxy(self, 1)

    @phases.setter
    def phases(self, value):
        self._set_batch_int32_array(1, value)

    @property
    def windings(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: windings
        DSS property index: 2
        """
        return BatchInt32ArrayProxy(self, 2)

    @windings.setter
    def windings(self, value):
        self._set_batch_int32_array(2, value)

    @property
    def wdg(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: wdg
        DSS property index: 3
        """
        return BatchInt32ArrayProxy(self, 3)

    @wdg.setter
    def wdg(self, value):
        self._set_batch_int32_array(3, value)

    @property
    def conn(self) -> List[npt.NDArray[np.int32]]:
        """
        DSS property name: conn
        DSS property index: 4
        """
        return [
            self._get_int32_array(self._lib.Obj_GetInt32Array, x, 4)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @conn.setter
    def conn(self, value: Union[List[Union[int,Connection]], List[AnyStr]]): #TODO: list of lists
        if len(value) and not isinstance(value[0], int):
            value, value_ptr, value_count = self._prepare_string_array(value)
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetStringArray(x, 4, value_ptr, value_count)

            self._check_for_error()
            return

        self._set_batch_int32_array(4, value)

    @property
    def conn_str(self) -> List[List[str]]:
        """
        DSS property name: conn
        DSS property index: 4
        """
        return self._get_string_ll(4)

    @conn_str.setter
    def conn_str(self, value: AnyStr):
        self.conn = value

    @property
    def kV(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: kV
        DSS property index: 5
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 5)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @kV.setter
    def kV(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(5, value)

    @property
    def kVA(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: kVA
        DSS property index: 6
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 6)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @kVA.setter
    def kVA(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(6, value)

    @property
    def tap(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: tap
        DSS property index: 7
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 7)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @tap.setter
    def tap(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(7, value)

    @property
    def pctR(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: %R
        DSS property index: 8
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 8)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @pctR.setter
    def pctR(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(8, value)

    @property
    def Rneut(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: Rneut
        DSS property index: 9
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 9)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Rneut.setter
    def Rneut(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(9, value)

    @property
    def Xneut(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: Xneut
        DSS property index: 10
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 10)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Xneut.setter
    def Xneut(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(10, value)

    @property
    def conns(self) -> List[npt.NDArray[np.int32]]:
        """
        DSS property name: conns
        DSS property index: 11
        """
        return [
            self._get_int32_array(self._lib.Obj_GetInt32Array, x, 11)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @conns.setter
    def conns(self, value: Union[List[Union[int,Connection]], List[AnyStr]]): #TODO: list of lists
        if len(value) and not isinstance(value[0], int):
            value, value_ptr, value_count = self._prepare_string_array(value)
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetStringArray(x, 11, value_ptr, value_count)

            self._check_for_error()
            return

        self._set_batch_int32_array(11, value)

    @property
    def conns_str(self) -> List[List[str]]:
        """
        DSS property name: conns
        DSS property index: 11
        """
        return self._get_string_ll(11)

    @conns_str.setter
    def conns_str(self, value: AnyStr):
        self.conns = value

    @property
    def kVs(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: kVs
        DSS property index: 12
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 12)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @kVs.setter
    def kVs(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(12, value)

    @property
    def kVAs(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: kVAs
        DSS property index: 13
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 13)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @kVAs.setter
    def kVAs(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(13, value)

    @property
    def taps(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: taps
        DSS property index: 14
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 14)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @taps.setter
    def taps(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(14, value)

    @property
    def Xhl(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Xhl
        DSS property index: 15
        """
        return BatchFloat64ArrayProxy(self, 15)

    @Xhl.setter
    def Xhl(self, value):
        self._set_batch_float64_array(15, value)

    @property
    def Xht(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Xht
        DSS property index: 16
        """
        return BatchFloat64ArrayProxy(self, 16)

    @Xht.setter
    def Xht(self, value):
        self._set_batch_float64_array(16, value)

    @property
    def Xlt(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Xlt
        DSS property index: 17
        """
        return BatchFloat64ArrayProxy(self, 17)

    @Xlt.setter
    def Xlt(self, value):
        self._set_batch_float64_array(17, value)

    @property
    def Xscarray(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: Xscarray
        DSS property index: 18
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 18)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Xscarray.setter
    def Xscarray(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(18, value)

    @property
    def thermal(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: thermal
        DSS property index: 19
        """
        return BatchFloat64ArrayProxy(self, 19)

    @thermal.setter
    def thermal(self, value):
        self._set_batch_float64_array(19, value)

    @property
    def n(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: n
        DSS property index: 20
        """
        return BatchFloat64ArrayProxy(self, 20)

    @n.setter
    def n(self, value):
        self._set_batch_float64_array(20, value)

    @property
    def m(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: m
        DSS property index: 21
        """
        return BatchFloat64ArrayProxy(self, 21)

    @m.setter
    def m(self, value):
        self._set_batch_float64_array(21, value)

    @property
    def flrise(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: flrise
        DSS property index: 22
        """
        return BatchFloat64ArrayProxy(self, 22)

    @flrise.setter
    def flrise(self, value):
        self._set_batch_float64_array(22, value)

    @property
    def hsrise(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: hsrise
        DSS property index: 23
        """
        return BatchFloat64ArrayProxy(self, 23)

    @hsrise.setter
    def hsrise(self, value):
        self._set_batch_float64_array(23, value)

    @property
    def pctloadloss(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %loadloss
        DSS property index: 24
        """
        return BatchFloat64ArrayProxy(self, 24)

    @pctloadloss.setter
    def pctloadloss(self, value):
        self._set_batch_float64_array(24, value)

    @property
    def pctnoloadloss(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %noloadloss
        DSS property index: 25
        """
        return BatchFloat64ArrayProxy(self, 25)

    @pctnoloadloss.setter
    def pctnoloadloss(self, value):
        self._set_batch_float64_array(25, value)

    @property
    def normhkVA(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: normhkVA
        DSS property index: 26
        """
        return BatchFloat64ArrayProxy(self, 26)

    @normhkVA.setter
    def normhkVA(self, value):
        self._set_batch_float64_array(26, value)

    @property
    def emerghkVA(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: emerghkVA
        DSS property index: 27
        """
        return BatchFloat64ArrayProxy(self, 27)

    @emerghkVA.setter
    def emerghkVA(self, value):
        self._set_batch_float64_array(27, value)

    @property
    def MaxTap(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: MaxTap
        DSS property index: 28
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 28)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @MaxTap.setter
    def MaxTap(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(28, value)

    @property
    def MinTap(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: MinTap
        DSS property index: 29
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 29)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @MinTap.setter
    def MinTap(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(29, value)

    @property
    def NumTaps(self) -> List[npt.NDArray[np.int32]]:
        """
        DSS property name: NumTaps
        DSS property index: 30
        """
        return [
            self._get_int32_array(self._lib.Obj_GetInt32Array, x, 30)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @NumTaps.setter
    def NumTaps(self, value: npt.NDArray[np.int32]): #TODO: list of arrays, matrix
        self._set_batch_int32_array(30, value)

    @property
    def pctimag(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %imag
        DSS property index: 31
        """
        return BatchFloat64ArrayProxy(self, 31)

    @pctimag.setter
    def pctimag(self, value):
        self._set_batch_float64_array(31, value)

    @property
    def ppm_antifloat(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: ppm_antifloat
        DSS property index: 32
        """
        return BatchFloat64ArrayProxy(self, 32)

    @ppm_antifloat.setter
    def ppm_antifloat(self, value):
        self._set_batch_float64_array(32, value)

    @property
    def pctRs(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: %Rs
        DSS property index: 33
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 33)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @pctRs.setter
    def pctRs(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(33, value)

    @property
    def X12(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: X12
        DSS property index: 34
        """
        return BatchFloat64ArrayProxy(self, 34)

    @X12.setter
    def X12(self, value):
        self._set_batch_float64_array(34, value)

    @property
    def X13(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: X13
        DSS property index: 35
        """
        return BatchFloat64ArrayProxy(self, 35)

    @X13.setter
    def X13(self, value):
        self._set_batch_float64_array(35, value)

    @property
    def X23(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: X23
        DSS property index: 36
        """
        return BatchFloat64ArrayProxy(self, 36)

    @X23.setter
    def X23(self, value):
        self._set_batch_float64_array(36, value)

    @property
    def RdcOhms(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: RdcOhms
        DSS property index: 37
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 37)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @RdcOhms.setter
    def RdcOhms(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(37, value)

    @property
    def Seasons(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Seasons
        DSS property index: 38
        """
        return BatchInt32ArrayProxy(self, 38)

    @Seasons.setter
    def Seasons(self, value):
        self._set_batch_int32_array(38, value)

    @property
    def Ratings(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: Ratings
        DSS property index: 39
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 39)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Ratings.setter
    def Ratings(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(39, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 40
        """
        self._set_batch_string(40, value)

class LineBatch(DSSBatch):
    _cls_name = 'Line'
    _obj_cls = Line
    _cls_idx = 15


    @property
    def bus1(self) -> List[str]:
        """
        DSS property name: bus1
        DSS property index: 1
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1) 

    @bus1.setter
    def bus1(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 1, value)

    @property
    def bus2(self) -> List[str]:
        """
        DSS property name: bus2
        DSS property index: 2
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 2) 

    @bus2.setter
    def bus2(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 2, value)

    @property
    def linecode(self) -> List[str]:
        """
        DSS property name: linecode
        DSS property index: 3
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 3)

    @linecode.setter
    def linecode(self, value: Union[AnyStr, LineCode]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(3, value)
            return

        self._set_batch_string(3, value)

    @property
    def linecode_obj(self) -> List[str]:
        """
        DSS property name: linecode
        DSS property index: 3
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 3)

    @linecode_obj.setter
    def linecode_obj(self, value: LineCode):
        self._set_batch_string(3, value)

    @property
    def length(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: length
        DSS property index: 4
        """
        return BatchFloat64ArrayProxy(self, 4)

    @length.setter
    def length(self, value):
        self._set_batch_float64_array(4, value)

    @property
    def phases(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: phases
        DSS property index: 5
        """
        return BatchInt32ArrayProxy(self, 5)

    @phases.setter
    def phases(self, value):
        self._set_batch_int32_array(5, value)

    @property
    def r1(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: r1
        DSS property index: 6
        """
        return BatchFloat64ArrayProxy(self, 6)

    @r1.setter
    def r1(self, value):
        self._set_batch_float64_array(6, value)

    @property
    def x1(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: x1
        DSS property index: 7
        """
        return BatchFloat64ArrayProxy(self, 7)

    @x1.setter
    def x1(self, value):
        self._set_batch_float64_array(7, value)

    @property
    def r0(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: r0
        DSS property index: 8
        """
        return BatchFloat64ArrayProxy(self, 8)

    @r0.setter
    def r0(self, value):
        self._set_batch_float64_array(8, value)

    @property
    def x0(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: x0
        DSS property index: 9
        """
        return BatchFloat64ArrayProxy(self, 9)

    @x0.setter
    def x0(self, value):
        self._set_batch_float64_array(9, value)

    @property
    def C1(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: C1
        DSS property index: 10
        """
        return BatchFloat64ArrayProxy(self, 10)

    @C1.setter
    def C1(self, value):
        self._set_batch_float64_array(10, value)

    @property
    def C0(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: C0
        DSS property index: 11
        """
        return BatchFloat64ArrayProxy(self, 11)

    @C0.setter
    def C0(self, value):
        self._set_batch_float64_array(11, value)

    @property
    def rmatrix(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: rmatrix
        DSS property index: 12
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 12)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @rmatrix.setter
    def rmatrix(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(12, value)

    @property
    def xmatrix(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: xmatrix
        DSS property index: 13
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 13)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @xmatrix.setter
    def xmatrix(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(13, value)

    @property
    def cmatrix(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: cmatrix
        DSS property index: 14
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 14)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @cmatrix.setter
    def cmatrix(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(14, value)

    @property
    def Switch(self) -> List[bool]:
        """
        DSS property name: Switch
        DSS property index: 15
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 15)
        ]
    @Switch.setter
    def Switch(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 15, value)

    @property
    def Rg(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Rg
        DSS property index: 16
        """
        return BatchFloat64ArrayProxy(self, 16)

    @Rg.setter
    def Rg(self, value):
        self._set_batch_float64_array(16, value)

    @property
    def Xg(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Xg
        DSS property index: 17
        """
        return BatchFloat64ArrayProxy(self, 17)

    @Xg.setter
    def Xg(self, value):
        self._set_batch_float64_array(17, value)

    @property
    def rho(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: rho
        DSS property index: 18
        """
        return BatchFloat64ArrayProxy(self, 18)

    @rho.setter
    def rho(self, value):
        self._set_batch_float64_array(18, value)

    @property
    def geometry(self) -> List[str]:
        """
        DSS property name: geometry
        DSS property index: 19
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 19)

    @geometry.setter
    def geometry(self, value: Union[AnyStr, LineGeometry]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(19, value)
            return

        self._set_batch_string(19, value)

    @property
    def geometry_obj(self) -> List[str]:
        """
        DSS property name: geometry
        DSS property index: 19
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 19)

    @geometry_obj.setter
    def geometry_obj(self, value: LineGeometry):
        self._set_batch_string(19, value)

    @property
    def units(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: units
        DSS property index: 20
        """
        return BatchInt32ArrayProxy(self, 20)

    @units.setter
    def units(self, value: Union[AnyStr, int, DimensionUnits, List[AnyStr], List[Union[int, DimensionUnits]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(20, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(20, value)

    @property
    def units_str(self) -> str:
        """
        DSS property name: units
        DSS property index: 20
        """
        return self._get_prop_string(20)

    @units_str.setter
    def units_str(self, value: AnyStr):
        self.units = value

    @property
    def spacing(self) -> List[str]:
        """
        DSS property name: spacing
        DSS property index: 21
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 21)

    @spacing.setter
    def spacing(self, value: Union[AnyStr, LineSpacing]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(21, value)
            return

        self._set_batch_string(21, value)

    @property
    def spacing_obj(self) -> List[str]:
        """
        DSS property name: spacing
        DSS property index: 21
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 21)

    @spacing_obj.setter
    def spacing_obj(self, value: LineSpacing):
        self._set_batch_string(21, value)

    @property
    def wires(self) -> List[List[str]]:
        """
        DSS property name: wires
        DSS property index: 22
        """
        return self._get_string_ll(22)

    @wires.setter
    def wires(self, value: Union[List[Union[AnyStr, WireData]], List[List[Union[AnyStr, WireData]]]]):
        if not len(value):
            return

        if isinstance(value[0], (bytes, str)):
            value, value_ptr, value_count = self._prepare_string_array(value)
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetStringArray(x, 22, value_ptr, value_count)

            self._check_for_error()
            return

        self._set_batch_obj_array(22, value)

    @property
    def wires_obj(self) -> List[List[WireData]]:
        """
        DSS property name: wires
        DSS property index: 22
        """
        return self._get_batch_obj_array(22, WireData)

    @wires_obj.setter
    def wires_obj(self, value: Union[List[WireData], List[List[WireData]]]):
        self._set_batch_obj_array(22, value)

    @property
    def earthmodel(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: EarthModel
        DSS property index: 23
        """
        return BatchInt32ArrayProxy(self, 23)

    @earthmodel.setter
    def earthmodel(self, value: Union[AnyStr, int, EarthModel, List[AnyStr], List[Union[int, EarthModel]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(23, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(23, value)

    @property
    def earthmodel_str(self) -> str:
        """
        DSS property name: EarthModel
        DSS property index: 23
        """
        return self._get_prop_string(23)

    @earthmodel_str.setter
    def earthmodel_str(self, value: AnyStr):
        self.earthmodel = value

    @property
    def cncables(self) -> List[List[str]]:
        """
        DSS property name: cncables
        DSS property index: 24
        """
        return self._get_string_ll(24)

    @cncables.setter
    def cncables(self, value: Union[List[Union[AnyStr, CNData]], List[List[Union[AnyStr, CNData]]]]):
        if not len(value):
            return

        if isinstance(value[0], (bytes, str)):
            value, value_ptr, value_count = self._prepare_string_array(value)
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetStringArray(x, 24, value_ptr, value_count)

            self._check_for_error()
            return

        self._set_batch_obj_array(24, value)

    @property
    def cncables_obj(self) -> List[List[CNData]]:
        """
        DSS property name: cncables
        DSS property index: 24
        """
        return self._get_batch_obj_array(24, CNData)

    @cncables_obj.setter
    def cncables_obj(self, value: Union[List[CNData], List[List[CNData]]]):
        self._set_batch_obj_array(24, value)

    @property
    def tscables(self) -> List[List[str]]:
        """
        DSS property name: tscables
        DSS property index: 25
        """
        return self._get_string_ll(25)

    @tscables.setter
    def tscables(self, value: Union[List[Union[AnyStr, TSData]], List[List[Union[AnyStr, TSData]]]]):
        if not len(value):
            return

        if isinstance(value[0], (bytes, str)):
            value, value_ptr, value_count = self._prepare_string_array(value)
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetStringArray(x, 25, value_ptr, value_count)

            self._check_for_error()
            return

        self._set_batch_obj_array(25, value)

    @property
    def tscables_obj(self) -> List[List[TSData]]:
        """
        DSS property name: tscables
        DSS property index: 25
        """
        return self._get_batch_obj_array(25, TSData)

    @tscables_obj.setter
    def tscables_obj(self, value: Union[List[TSData], List[List[TSData]]]):
        self._set_batch_obj_array(25, value)

    @property
    def B1(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: B1
        DSS property index: 26
        """
        return BatchFloat64ArrayProxy(self, 26)

    @B1.setter
    def B1(self, value):
        self._set_batch_float64_array(26, value)

    @property
    def B0(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: B0
        DSS property index: 27
        """
        return BatchFloat64ArrayProxy(self, 27)

    @B0.setter
    def B0(self, value):
        self._set_batch_float64_array(27, value)

    @property
    def Seasons(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Seasons
        DSS property index: 28
        """
        return BatchInt32ArrayProxy(self, 28)

    @Seasons.setter
    def Seasons(self, value):
        self._set_batch_int32_array(28, value)

    @property
    def Ratings(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: Ratings
        DSS property index: 29
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 29)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Ratings.setter
    def Ratings(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(29, value)

    @property
    def linetype(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: LineType
        DSS property index: 30
        """
        return BatchInt32ArrayProxy(self, 30)

    @linetype.setter
    def linetype(self, value: Union[AnyStr, int, LineType, List[AnyStr], List[Union[int, LineType]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(30, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(30, value)

    @property
    def linetype_str(self) -> str:
        """
        DSS property name: LineType
        DSS property index: 30
        """
        return self._get_prop_string(30)

    @linetype_str.setter
    def linetype_str(self, value: AnyStr):
        self.linetype = value

    @property
    def normamps(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: normamps
        DSS property index: 31
        """
        return BatchFloat64ArrayProxy(self, 31)

    @normamps.setter
    def normamps(self, value):
        self._set_batch_float64_array(31, value)

    @property
    def emergamps(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: emergamps
        DSS property index: 32
        """
        return BatchFloat64ArrayProxy(self, 32)

    @emergamps.setter
    def emergamps(self, value):
        self._set_batch_float64_array(32, value)

    @property
    def faultrate(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: faultrate
        DSS property index: 33
        """
        return BatchFloat64ArrayProxy(self, 33)

    @faultrate.setter
    def faultrate(self, value):
        self._set_batch_float64_array(33, value)

    @property
    def pctperm(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: pctperm
        DSS property index: 34
        """
        return BatchFloat64ArrayProxy(self, 34)

    @pctperm.setter
    def pctperm(self, value):
        self._set_batch_float64_array(34, value)

    @property
    def repair(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: repair
        DSS property index: 35
        """
        return BatchFloat64ArrayProxy(self, 35)

    @repair.setter
    def repair(self, value):
        self._set_batch_float64_array(35, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 36
        """
        return BatchFloat64ArrayProxy(self, 36)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(36, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 37
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 37)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 37, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 38
        """
        self._set_batch_string(38, value)

class VsourceBatch(DSSBatch):
    _cls_name = 'Vsource'
    _obj_cls = Vsource
    _cls_idx = 16


    @property
    def bus1(self) -> List[str]:
        """
        DSS property name: bus1
        DSS property index: 1
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1) 

    @bus1.setter
    def bus1(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 1, value)

    @property
    def basekv(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basekv
        DSS property index: 2
        """
        return BatchFloat64ArrayProxy(self, 2)

    @basekv.setter
    def basekv(self, value):
        self._set_batch_float64_array(2, value)

    @property
    def pu(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: pu
        DSS property index: 3
        """
        return BatchFloat64ArrayProxy(self, 3)

    @pu.setter
    def pu(self, value):
        self._set_batch_float64_array(3, value)

    @property
    def angle(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: angle
        DSS property index: 4
        """
        return BatchFloat64ArrayProxy(self, 4)

    @angle.setter
    def angle(self, value):
        self._set_batch_float64_array(4, value)

    @property
    def frequency(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: frequency
        DSS property index: 5
        """
        return BatchFloat64ArrayProxy(self, 5)

    @frequency.setter
    def frequency(self, value):
        self._set_batch_float64_array(5, value)

    @property
    def phases(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: phases
        DSS property index: 6
        """
        return BatchInt32ArrayProxy(self, 6)

    @phases.setter
    def phases(self, value):
        self._set_batch_int32_array(6, value)

    @property
    def MVAsc3(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: MVAsc3
        DSS property index: 7
        """
        return BatchFloat64ArrayProxy(self, 7)

    @MVAsc3.setter
    def MVAsc3(self, value):
        self._set_batch_float64_array(7, value)

    @property
    def MVAsc1(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: MVAsc1
        DSS property index: 8
        """
        return BatchFloat64ArrayProxy(self, 8)

    @MVAsc1.setter
    def MVAsc1(self, value):
        self._set_batch_float64_array(8, value)

    @property
    def x1r1(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: x1r1
        DSS property index: 9
        """
        return BatchFloat64ArrayProxy(self, 9)

    @x1r1.setter
    def x1r1(self, value):
        self._set_batch_float64_array(9, value)

    @property
    def x0r0(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: x0r0
        DSS property index: 10
        """
        return BatchFloat64ArrayProxy(self, 10)

    @x0r0.setter
    def x0r0(self, value):
        self._set_batch_float64_array(10, value)

    @property
    def Isc3(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Isc3
        DSS property index: 11
        """
        return BatchFloat64ArrayProxy(self, 11)

    @Isc3.setter
    def Isc3(self, value):
        self._set_batch_float64_array(11, value)

    @property
    def Isc1(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Isc1
        DSS property index: 12
        """
        return BatchFloat64ArrayProxy(self, 12)

    @Isc1.setter
    def Isc1(self, value):
        self._set_batch_float64_array(12, value)

    @property
    def R1(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: R1
        DSS property index: 13
        """
        return BatchFloat64ArrayProxy(self, 13)

    @R1.setter
    def R1(self, value):
        self._set_batch_float64_array(13, value)

    @property
    def X1(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: X1
        DSS property index: 14
        """
        return BatchFloat64ArrayProxy(self, 14)

    @X1.setter
    def X1(self, value):
        self._set_batch_float64_array(14, value)

    @property
    def R0(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: R0
        DSS property index: 15
        """
        return BatchFloat64ArrayProxy(self, 15)

    @R0.setter
    def R0(self, value):
        self._set_batch_float64_array(15, value)

    @property
    def X0(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: X0
        DSS property index: 16
        """
        return BatchFloat64ArrayProxy(self, 16)

    @X0.setter
    def X0(self, value):
        self._set_batch_float64_array(16, value)

    @property
    def scantype(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: ScanType
        DSS property index: 17
        """
        return BatchInt32ArrayProxy(self, 17)

    @scantype.setter
    def scantype(self, value: Union[AnyStr, int, ScanType, List[AnyStr], List[Union[int, ScanType]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(17, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(17, value)

    @property
    def scantype_str(self) -> str:
        """
        DSS property name: ScanType
        DSS property index: 17
        """
        return self._get_prop_string(17)

    @scantype_str.setter
    def scantype_str(self, value: AnyStr):
        self.scantype = value

    @property
    def Sequence(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Sequence
        DSS property index: 18
        """
        return BatchInt32ArrayProxy(self, 18)

    @Sequence.setter
    def Sequence(self, value: Union[AnyStr, int, SequenceType, List[AnyStr], List[Union[int, SequenceType]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(18, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(18, value)

    @property
    def Sequence_str(self) -> str:
        """
        DSS property name: Sequence
        DSS property index: 18
        """
        return self._get_prop_string(18)

    @Sequence_str.setter
    def Sequence_str(self, value: AnyStr):
        self.Sequence = value

    @property
    def bus2(self) -> List[str]:
        """
        DSS property name: bus2
        DSS property index: 19
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 19) 

    @bus2.setter
    def bus2(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 19, value)

    @property
    def Z1(self) -> List[complex]:
        """
        DSS property name: Z1
        DSS property index: 20
        """
        return [   
            self._get_float64_array(
                self._lib.Obj_GetFloat64Array, 
                x,
                20,
            ).astype(complex)[0]
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Z1.setter
    def Z1(self, value: Union[complex, List[complex]]):
        if isinstance(value, complex):
            value, value_ptr, value_count = self._prepare_float64_array([value.real, value.imag])
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetFloat64Array(x, 20, value_ptr, value_count)
            return

        values = value
        if len(values) != self.count[0]:
            raise ValueError('Number of elements provided must match the number of objects in the batch.')

        value, value_ptr, value_count = self._prepare_float64_array([0, 0])
        for v, x in zip(values, self._ffi.unpack(self.pointer[0], self.count[0])):
            value[0] = v.real
            value[1] = v.imag
            self._lib.Obj_SetFloat64Array(x, 20, value_ptr, value_count)

    @property
    def Z0(self) -> List[complex]:
        """
        DSS property name: Z0
        DSS property index: 21
        """
        return [   
            self._get_float64_array(
                self._lib.Obj_GetFloat64Array, 
                x,
                21,
            ).astype(complex)[0]
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Z0.setter
    def Z0(self, value: Union[complex, List[complex]]):
        if isinstance(value, complex):
            value, value_ptr, value_count = self._prepare_float64_array([value.real, value.imag])
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetFloat64Array(x, 21, value_ptr, value_count)
            return

        values = value
        if len(values) != self.count[0]:
            raise ValueError('Number of elements provided must match the number of objects in the batch.')

        value, value_ptr, value_count = self._prepare_float64_array([0, 0])
        for v, x in zip(values, self._ffi.unpack(self.pointer[0], self.count[0])):
            value[0] = v.real
            value[1] = v.imag
            self._lib.Obj_SetFloat64Array(x, 21, value_ptr, value_count)

    @property
    def Z2(self) -> List[complex]:
        """
        DSS property name: Z2
        DSS property index: 22
        """
        return [   
            self._get_float64_array(
                self._lib.Obj_GetFloat64Array, 
                x,
                22,
            ).astype(complex)[0]
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Z2.setter
    def Z2(self, value: Union[complex, List[complex]]):
        if isinstance(value, complex):
            value, value_ptr, value_count = self._prepare_float64_array([value.real, value.imag])
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetFloat64Array(x, 22, value_ptr, value_count)
            return

        values = value
        if len(values) != self.count[0]:
            raise ValueError('Number of elements provided must match the number of objects in the batch.')

        value, value_ptr, value_count = self._prepare_float64_array([0, 0])
        for v, x in zip(values, self._ffi.unpack(self.pointer[0], self.count[0])):
            value[0] = v.real
            value[1] = v.imag
            self._lib.Obj_SetFloat64Array(x, 22, value_ptr, value_count)

    @property
    def puZ1(self) -> List[complex]:
        """
        DSS property name: puZ1
        DSS property index: 23
        """
        return [   
            self._get_float64_array(
                self._lib.Obj_GetFloat64Array, 
                x,
                23,
            ).astype(complex)[0]
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @puZ1.setter
    def puZ1(self, value: Union[complex, List[complex]]):
        if isinstance(value, complex):
            value, value_ptr, value_count = self._prepare_float64_array([value.real, value.imag])
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetFloat64Array(x, 23, value_ptr, value_count)
            return

        values = value
        if len(values) != self.count[0]:
            raise ValueError('Number of elements provided must match the number of objects in the batch.')

        value, value_ptr, value_count = self._prepare_float64_array([0, 0])
        for v, x in zip(values, self._ffi.unpack(self.pointer[0], self.count[0])):
            value[0] = v.real
            value[1] = v.imag
            self._lib.Obj_SetFloat64Array(x, 23, value_ptr, value_count)

    @property
    def puZ0(self) -> List[complex]:
        """
        DSS property name: puZ0
        DSS property index: 24
        """
        return [   
            self._get_float64_array(
                self._lib.Obj_GetFloat64Array, 
                x,
                24,
            ).astype(complex)[0]
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @puZ0.setter
    def puZ0(self, value: Union[complex, List[complex]]):
        if isinstance(value, complex):
            value, value_ptr, value_count = self._prepare_float64_array([value.real, value.imag])
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetFloat64Array(x, 24, value_ptr, value_count)
            return

        values = value
        if len(values) != self.count[0]:
            raise ValueError('Number of elements provided must match the number of objects in the batch.')

        value, value_ptr, value_count = self._prepare_float64_array([0, 0])
        for v, x in zip(values, self._ffi.unpack(self.pointer[0], self.count[0])):
            value[0] = v.real
            value[1] = v.imag
            self._lib.Obj_SetFloat64Array(x, 24, value_ptr, value_count)

    @property
    def puZ2(self) -> List[complex]:
        """
        DSS property name: puZ2
        DSS property index: 25
        """
        return [   
            self._get_float64_array(
                self._lib.Obj_GetFloat64Array, 
                x,
                25,
            ).astype(complex)[0]
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @puZ2.setter
    def puZ2(self, value: Union[complex, List[complex]]):
        if isinstance(value, complex):
            value, value_ptr, value_count = self._prepare_float64_array([value.real, value.imag])
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetFloat64Array(x, 25, value_ptr, value_count)
            return

        values = value
        if len(values) != self.count[0]:
            raise ValueError('Number of elements provided must match the number of objects in the batch.')

        value, value_ptr, value_count = self._prepare_float64_array([0, 0])
        for v, x in zip(values, self._ffi.unpack(self.pointer[0], self.count[0])):
            value[0] = v.real
            value[1] = v.imag
            self._lib.Obj_SetFloat64Array(x, 25, value_ptr, value_count)

    @property
    def baseMVA(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: baseMVA
        DSS property index: 26
        """
        return BatchFloat64ArrayProxy(self, 26)

    @baseMVA.setter
    def baseMVA(self, value):
        self._set_batch_float64_array(26, value)

    @property
    def Yearly(self) -> List[str]:
        """
        DSS property name: Yearly
        DSS property index: 27
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 27)

    @Yearly.setter
    def Yearly(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(27, value)
            return

        self._set_batch_string(27, value)

    @property
    def Yearly_obj(self) -> List[str]:
        """
        DSS property name: Yearly
        DSS property index: 27
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 27)

    @Yearly_obj.setter
    def Yearly_obj(self, value: LoadShape):
        self._set_batch_string(27, value)

    @property
    def Daily(self) -> List[str]:
        """
        DSS property name: Daily
        DSS property index: 28
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 28)

    @Daily.setter
    def Daily(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(28, value)
            return

        self._set_batch_string(28, value)

    @property
    def Daily_obj(self) -> List[str]:
        """
        DSS property name: Daily
        DSS property index: 28
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 28)

    @Daily_obj.setter
    def Daily_obj(self, value: LoadShape):
        self._set_batch_string(28, value)

    @property
    def Duty(self) -> List[str]:
        """
        DSS property name: Duty
        DSS property index: 29
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 29)

    @Duty.setter
    def Duty(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(29, value)
            return

        self._set_batch_string(29, value)

    @property
    def Duty_obj(self) -> List[str]:
        """
        DSS property name: Duty
        DSS property index: 29
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 29)

    @Duty_obj.setter
    def Duty_obj(self, value: LoadShape):
        self._set_batch_string(29, value)

    @property
    def Model(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Model
        DSS property index: 30
        """
        return BatchInt32ArrayProxy(self, 30)

    @Model.setter
    def Model(self, value: Union[AnyStr, int, Vsource.VSourceModel, List[AnyStr], List[Union[int, Vsource.VSourceModel]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(30, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(30, value)

    @property
    def Model_str(self) -> str:
        """
        DSS property name: Model
        DSS property index: 30
        """
        return self._get_prop_string(30)

    @Model_str.setter
    def Model_str(self, value: AnyStr):
        self.Model = value

    @property
    def puZideal(self) -> List[complex]:
        """
        DSS property name: puZideal
        DSS property index: 31
        """
        return [   
            self._get_float64_array(
                self._lib.Obj_GetFloat64Array, 
                x,
                31,
            ).astype(complex)[0]
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @puZideal.setter
    def puZideal(self, value: Union[complex, List[complex]]):
        if isinstance(value, complex):
            value, value_ptr, value_count = self._prepare_float64_array([value.real, value.imag])
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetFloat64Array(x, 31, value_ptr, value_count)
            return

        values = value
        if len(values) != self.count[0]:
            raise ValueError('Number of elements provided must match the number of objects in the batch.')

        value, value_ptr, value_count = self._prepare_float64_array([0, 0])
        for v, x in zip(values, self._ffi.unpack(self.pointer[0], self.count[0])):
            value[0] = v.real
            value[1] = v.imag
            self._lib.Obj_SetFloat64Array(x, 31, value_ptr, value_count)

    @property
    def spectrum(self) -> List[str]:
        """
        DSS property name: spectrum
        DSS property index: 32
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 32)

    @spectrum.setter
    def spectrum(self, value: Union[AnyStr, Spectrum]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(32, value)
            return

        self._set_batch_string(32, value)

    @property
    def spectrum_obj(self) -> List[str]:
        """
        DSS property name: spectrum
        DSS property index: 32
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 32)

    @spectrum_obj.setter
    def spectrum_obj(self, value: Spectrum):
        self._set_batch_string(32, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 33
        """
        return BatchFloat64ArrayProxy(self, 33)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(33, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 34
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 34)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 34, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 35
        """
        self._set_batch_string(35, value)

class IsourceBatch(DSSBatch):
    _cls_name = 'Isource'
    _obj_cls = Isource
    _cls_idx = 17


    @property
    def bus1(self) -> List[str]:
        """
        DSS property name: bus1
        DSS property index: 1
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1) 

    @bus1.setter
    def bus1(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 1, value)

    @property
    def amps(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: amps
        DSS property index: 2
        """
        return BatchFloat64ArrayProxy(self, 2)

    @amps.setter
    def amps(self, value):
        self._set_batch_float64_array(2, value)

    @property
    def angle(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: angle
        DSS property index: 3
        """
        return BatchFloat64ArrayProxy(self, 3)

    @angle.setter
    def angle(self, value):
        self._set_batch_float64_array(3, value)

    @property
    def frequency(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: frequency
        DSS property index: 4
        """
        return BatchFloat64ArrayProxy(self, 4)

    @frequency.setter
    def frequency(self, value):
        self._set_batch_float64_array(4, value)

    @property
    def phases(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: phases
        DSS property index: 5
        """
        return BatchInt32ArrayProxy(self, 5)

    @phases.setter
    def phases(self, value):
        self._set_batch_int32_array(5, value)

    @property
    def scantype(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: scantype
        DSS property index: 6
        """
        return BatchInt32ArrayProxy(self, 6)

    @scantype.setter
    def scantype(self, value: Union[AnyStr, int, ScanType, List[AnyStr], List[Union[int, ScanType]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(6, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(6, value)

    @property
    def scantype_str(self) -> str:
        """
        DSS property name: scantype
        DSS property index: 6
        """
        return self._get_prop_string(6)

    @scantype_str.setter
    def scantype_str(self, value: AnyStr):
        self.scantype = value

    @property
    def sequence(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: sequence
        DSS property index: 7
        """
        return BatchInt32ArrayProxy(self, 7)

    @sequence.setter
    def sequence(self, value: Union[AnyStr, int, SequenceType, List[AnyStr], List[Union[int, SequenceType]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(7, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(7, value)

    @property
    def sequence_str(self) -> str:
        """
        DSS property name: sequence
        DSS property index: 7
        """
        return self._get_prop_string(7)

    @sequence_str.setter
    def sequence_str(self, value: AnyStr):
        self.sequence = value

    @property
    def Yearly(self) -> List[str]:
        """
        DSS property name: Yearly
        DSS property index: 8
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 8)

    @Yearly.setter
    def Yearly(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(8, value)
            return

        self._set_batch_string(8, value)

    @property
    def Yearly_obj(self) -> List[str]:
        """
        DSS property name: Yearly
        DSS property index: 8
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 8)

    @Yearly_obj.setter
    def Yearly_obj(self, value: LoadShape):
        self._set_batch_string(8, value)

    @property
    def Daily(self) -> List[str]:
        """
        DSS property name: Daily
        DSS property index: 9
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 9)

    @Daily.setter
    def Daily(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(9, value)
            return

        self._set_batch_string(9, value)

    @property
    def Daily_obj(self) -> List[str]:
        """
        DSS property name: Daily
        DSS property index: 9
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 9)

    @Daily_obj.setter
    def Daily_obj(self, value: LoadShape):
        self._set_batch_string(9, value)

    @property
    def Duty(self) -> List[str]:
        """
        DSS property name: Duty
        DSS property index: 10
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 10)

    @Duty.setter
    def Duty(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(10, value)
            return

        self._set_batch_string(10, value)

    @property
    def Duty_obj(self) -> List[str]:
        """
        DSS property name: Duty
        DSS property index: 10
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 10)

    @Duty_obj.setter
    def Duty_obj(self, value: LoadShape):
        self._set_batch_string(10, value)

    @property
    def Bus2(self) -> List[str]:
        """
        DSS property name: Bus2
        DSS property index: 11
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 11) 

    @Bus2.setter
    def Bus2(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 11, value)

    @property
    def spectrum(self) -> List[str]:
        """
        DSS property name: spectrum
        DSS property index: 12
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 12)

    @spectrum.setter
    def spectrum(self, value: Union[AnyStr, Spectrum]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(12, value)
            return

        self._set_batch_string(12, value)

    @property
    def spectrum_obj(self) -> List[str]:
        """
        DSS property name: spectrum
        DSS property index: 12
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 12)

    @spectrum_obj.setter
    def spectrum_obj(self, value: Spectrum):
        self._set_batch_string(12, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 13
        """
        return BatchFloat64ArrayProxy(self, 13)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(13, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 14
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 14)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 14, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 15
        """
        self._set_batch_string(15, value)

class VCCSBatch(DSSBatch):
    _cls_name = 'VCCS'
    _obj_cls = VCCS
    _cls_idx = 18


    @property
    def bus1(self) -> List[str]:
        """
        DSS property name: bus1
        DSS property index: 1
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1) 

    @bus1.setter
    def bus1(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 1, value)

    @property
    def phases(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: phases
        DSS property index: 2
        """
        return BatchInt32ArrayProxy(self, 2)

    @phases.setter
    def phases(self, value):
        self._set_batch_int32_array(2, value)

    @property
    def prated(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: prated
        DSS property index: 3
        """
        return BatchFloat64ArrayProxy(self, 3)

    @prated.setter
    def prated(self, value):
        self._set_batch_float64_array(3, value)

    @property
    def vrated(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: vrated
        DSS property index: 4
        """
        return BatchFloat64ArrayProxy(self, 4)

    @vrated.setter
    def vrated(self, value):
        self._set_batch_float64_array(4, value)

    @property
    def ppct(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: ppct
        DSS property index: 5
        """
        return BatchFloat64ArrayProxy(self, 5)

    @ppct.setter
    def ppct(self, value):
        self._set_batch_float64_array(5, value)

    @property
    def bp1(self) -> List[str]:
        """
        DSS property name: bp1
        DSS property index: 6
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 6)

    @bp1.setter
    def bp1(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(6, value)
            return

        self._set_batch_string(6, value)

    @property
    def bp1_obj(self) -> List[str]:
        """
        DSS property name: bp1
        DSS property index: 6
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 6)

    @bp1_obj.setter
    def bp1_obj(self, value: XYcurve):
        self._set_batch_string(6, value)

    @property
    def bp2(self) -> List[str]:
        """
        DSS property name: bp2
        DSS property index: 7
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 7)

    @bp2.setter
    def bp2(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(7, value)
            return

        self._set_batch_string(7, value)

    @property
    def bp2_obj(self) -> List[str]:
        """
        DSS property name: bp2
        DSS property index: 7
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 7)

    @bp2_obj.setter
    def bp2_obj(self, value: XYcurve):
        self._set_batch_string(7, value)

    @property
    def filter(self) -> List[str]:
        """
        DSS property name: filter
        DSS property index: 8
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 8)

    @filter.setter
    def filter(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(8, value)
            return

        self._set_batch_string(8, value)

    @property
    def filter_obj(self) -> List[str]:
        """
        DSS property name: filter
        DSS property index: 8
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 8)

    @filter_obj.setter
    def filter_obj(self, value: XYcurve):
        self._set_batch_string(8, value)

    @property
    def fsample(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: fsample
        DSS property index: 9
        """
        return BatchFloat64ArrayProxy(self, 9)

    @fsample.setter
    def fsample(self, value):
        self._set_batch_float64_array(9, value)

    @property
    def rmsmode(self) -> List[bool]:
        """
        DSS property name: rmsmode
        DSS property index: 10
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 10)
        ]
    @rmsmode.setter
    def rmsmode(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 10, value)

    @property
    def imaxpu(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: imaxpu
        DSS property index: 11
        """
        return BatchFloat64ArrayProxy(self, 11)

    @imaxpu.setter
    def imaxpu(self, value):
        self._set_batch_float64_array(11, value)

    @property
    def vrmstau(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: vrmstau
        DSS property index: 12
        """
        return BatchFloat64ArrayProxy(self, 12)

    @vrmstau.setter
    def vrmstau(self, value):
        self._set_batch_float64_array(12, value)

    @property
    def irmstau(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: irmstau
        DSS property index: 13
        """
        return BatchFloat64ArrayProxy(self, 13)

    @irmstau.setter
    def irmstau(self, value):
        self._set_batch_float64_array(13, value)

    @property
    def spectrum(self) -> List[str]:
        """
        DSS property name: spectrum
        DSS property index: 14
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 14)

    @spectrum.setter
    def spectrum(self, value: Union[AnyStr, Spectrum]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(14, value)
            return

        self._set_batch_string(14, value)

    @property
    def spectrum_obj(self) -> List[str]:
        """
        DSS property name: spectrum
        DSS property index: 14
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 14)

    @spectrum_obj.setter
    def spectrum_obj(self, value: Spectrum):
        self._set_batch_string(14, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 15
        """
        return BatchFloat64ArrayProxy(self, 15)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(15, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 16
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 16)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 16, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 17
        """
        self._set_batch_string(17, value)

class LoadBatch(DSSBatch):
    _cls_name = 'Load'
    _obj_cls = Load
    _cls_idx = 19


    @property
    def phases(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: phases
        DSS property index: 1
        """
        return BatchInt32ArrayProxy(self, 1)

    @phases.setter
    def phases(self, value):
        self._set_batch_int32_array(1, value)

    @property
    def bus1(self) -> List[str]:
        """
        DSS property name: bus1
        DSS property index: 2
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 2) 

    @bus1.setter
    def bus1(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 2, value)

    @property
    def kV(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kV
        DSS property index: 3
        """
        return BatchFloat64ArrayProxy(self, 3)

    @kV.setter
    def kV(self, value):
        self._set_batch_float64_array(3, value)

    @property
    def kW(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kW
        DSS property index: 4
        """
        return BatchFloat64ArrayProxy(self, 4)

    @kW.setter
    def kW(self, value):
        self._set_batch_float64_array(4, value)

    @property
    def pf(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: pf
        DSS property index: 5
        """
        return BatchFloat64ArrayProxy(self, 5)

    @pf.setter
    def pf(self, value):
        self._set_batch_float64_array(5, value)

    @property
    def model(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: model
        DSS property index: 6
        """
        return BatchInt32ArrayProxy(self, 6)

    @model.setter
    def model(self, value):
        self._set_batch_int32_array(6, value)

    @property
    def yearly(self) -> List[str]:
        """
        DSS property name: yearly
        DSS property index: 7
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 7)

    @yearly.setter
    def yearly(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(7, value)
            return

        self._set_batch_string(7, value)

    @property
    def yearly_obj(self) -> List[str]:
        """
        DSS property name: yearly
        DSS property index: 7
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 7)

    @yearly_obj.setter
    def yearly_obj(self, value: LoadShape):
        self._set_batch_string(7, value)

    @property
    def daily(self) -> List[str]:
        """
        DSS property name: daily
        DSS property index: 8
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 8)

    @daily.setter
    def daily(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(8, value)
            return

        self._set_batch_string(8, value)

    @property
    def daily_obj(self) -> List[str]:
        """
        DSS property name: daily
        DSS property index: 8
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 8)

    @daily_obj.setter
    def daily_obj(self, value: LoadShape):
        self._set_batch_string(8, value)

    @property
    def duty(self) -> List[str]:
        """
        DSS property name: duty
        DSS property index: 9
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 9)

    @duty.setter
    def duty(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(9, value)
            return

        self._set_batch_string(9, value)

    @property
    def duty_obj(self) -> List[str]:
        """
        DSS property name: duty
        DSS property index: 9
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 9)

    @duty_obj.setter
    def duty_obj(self, value: LoadShape):
        self._set_batch_string(9, value)

    @property
    def growth(self) -> List[str]:
        """
        DSS property name: growth
        DSS property index: 10
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 10)

    @growth.setter
    def growth(self, value: Union[AnyStr, GrowthShape]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(10, value)
            return

        self._set_batch_string(10, value)

    @property
    def growth_obj(self) -> List[str]:
        """
        DSS property name: growth
        DSS property index: 10
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 10)

    @growth_obj.setter
    def growth_obj(self, value: GrowthShape):
        self._set_batch_string(10, value)

    @property
    def conn(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: conn
        DSS property index: 11
        """
        return BatchInt32ArrayProxy(self, 11)

    @conn.setter
    def conn(self, value: Union[AnyStr, int, Connection, List[AnyStr], List[Union[int, Connection]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(11, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(11, value)

    @property
    def conn_str(self) -> str:
        """
        DSS property name: conn
        DSS property index: 11
        """
        return self._get_prop_string(11)

    @conn_str.setter
    def conn_str(self, value: AnyStr):
        self.conn = value

    @property
    def kvar(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kvar
        DSS property index: 12
        """
        return BatchFloat64ArrayProxy(self, 12)

    @kvar.setter
    def kvar(self, value):
        self._set_batch_float64_array(12, value)

    @property
    def Rneut(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Rneut
        DSS property index: 13
        """
        return BatchFloat64ArrayProxy(self, 13)

    @Rneut.setter
    def Rneut(self, value):
        self._set_batch_float64_array(13, value)

    @property
    def Xneut(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Xneut
        DSS property index: 14
        """
        return BatchFloat64ArrayProxy(self, 14)

    @Xneut.setter
    def Xneut(self, value):
        self._set_batch_float64_array(14, value)

    @property
    def status(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: status
        DSS property index: 15
        """
        return BatchInt32ArrayProxy(self, 15)

    @status.setter
    def status(self, value: Union[AnyStr, int, Load.LoadStatus, List[AnyStr], List[Union[int, Load.LoadStatus]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(15, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(15, value)

    @property
    def status_str(self) -> str:
        """
        DSS property name: status
        DSS property index: 15
        """
        return self._get_prop_string(15)

    @status_str.setter
    def status_str(self, value: AnyStr):
        self.status = value

    @property
    def cls(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: class
        DSS property index: 16
        """
        return BatchInt32ArrayProxy(self, 16)

    @cls.setter
    def cls(self, value):
        self._set_batch_int32_array(16, value)

    @property
    def Vminpu(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Vminpu
        DSS property index: 17
        """
        return BatchFloat64ArrayProxy(self, 17)

    @Vminpu.setter
    def Vminpu(self, value):
        self._set_batch_float64_array(17, value)

    @property
    def Vmaxpu(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Vmaxpu
        DSS property index: 18
        """
        return BatchFloat64ArrayProxy(self, 18)

    @Vmaxpu.setter
    def Vmaxpu(self, value):
        self._set_batch_float64_array(18, value)

    @property
    def Vminnorm(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Vminnorm
        DSS property index: 19
        """
        return BatchFloat64ArrayProxy(self, 19)

    @Vminnorm.setter
    def Vminnorm(self, value):
        self._set_batch_float64_array(19, value)

    @property
    def Vminemerg(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Vminemerg
        DSS property index: 20
        """
        return BatchFloat64ArrayProxy(self, 20)

    @Vminemerg.setter
    def Vminemerg(self, value):
        self._set_batch_float64_array(20, value)

    @property
    def xfkVA(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: xfkVA
        DSS property index: 21
        """
        return BatchFloat64ArrayProxy(self, 21)

    @xfkVA.setter
    def xfkVA(self, value):
        self._set_batch_float64_array(21, value)

    @property
    def allocationfactor(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: allocationfactor
        DSS property index: 22
        """
        return BatchFloat64ArrayProxy(self, 22)

    @allocationfactor.setter
    def allocationfactor(self, value):
        self._set_batch_float64_array(22, value)

    @property
    def kVA(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kVA
        DSS property index: 23
        """
        return BatchFloat64ArrayProxy(self, 23)

    @kVA.setter
    def kVA(self, value):
        self._set_batch_float64_array(23, value)

    @property
    def pctmean(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %mean
        DSS property index: 24
        """
        return BatchFloat64ArrayProxy(self, 24)

    @pctmean.setter
    def pctmean(self, value):
        self._set_batch_float64_array(24, value)

    @property
    def pctstddev(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %stddev
        DSS property index: 25
        """
        return BatchFloat64ArrayProxy(self, 25)

    @pctstddev.setter
    def pctstddev(self, value):
        self._set_batch_float64_array(25, value)

    @property
    def CVRwatts(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: CVRwatts
        DSS property index: 26
        """
        return BatchFloat64ArrayProxy(self, 26)

    @CVRwatts.setter
    def CVRwatts(self, value):
        self._set_batch_float64_array(26, value)

    @property
    def CVRvars(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: CVRvars
        DSS property index: 27
        """
        return BatchFloat64ArrayProxy(self, 27)

    @CVRvars.setter
    def CVRvars(self, value):
        self._set_batch_float64_array(27, value)

    @property
    def kwh(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kwh
        DSS property index: 28
        """
        return BatchFloat64ArrayProxy(self, 28)

    @kwh.setter
    def kwh(self, value):
        self._set_batch_float64_array(28, value)

    @property
    def kwhdays(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kwhdays
        DSS property index: 29
        """
        return BatchFloat64ArrayProxy(self, 29)

    @kwhdays.setter
    def kwhdays(self, value):
        self._set_batch_float64_array(29, value)

    @property
    def Cfactor(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Cfactor
        DSS property index: 30
        """
        return BatchFloat64ArrayProxy(self, 30)

    @Cfactor.setter
    def Cfactor(self, value):
        self._set_batch_float64_array(30, value)

    @property
    def CVRcurve(self) -> List[str]:
        """
        DSS property name: CVRcurve
        DSS property index: 31
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 31)

    @CVRcurve.setter
    def CVRcurve(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(31, value)
            return

        self._set_batch_string(31, value)

    @property
    def CVRcurve_obj(self) -> List[str]:
        """
        DSS property name: CVRcurve
        DSS property index: 31
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 31)

    @CVRcurve_obj.setter
    def CVRcurve_obj(self, value: LoadShape):
        self._set_batch_string(31, value)

    @property
    def NumCust(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: NumCust
        DSS property index: 32
        """
        return BatchInt32ArrayProxy(self, 32)

    @NumCust.setter
    def NumCust(self, value):
        self._set_batch_int32_array(32, value)

    @property
    def ZIPV(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: ZIPV
        DSS property index: 33
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 33)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @ZIPV.setter
    def ZIPV(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(33, value)

    @property
    def pctSeriesRL(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %SeriesRL
        DSS property index: 34
        """
        return BatchFloat64ArrayProxy(self, 34)

    @pctSeriesRL.setter
    def pctSeriesRL(self, value):
        self._set_batch_float64_array(34, value)

    @property
    def RelWeight(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: RelWeight
        DSS property index: 35
        """
        return BatchFloat64ArrayProxy(self, 35)

    @RelWeight.setter
    def RelWeight(self, value):
        self._set_batch_float64_array(35, value)

    @property
    def Vlowpu(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Vlowpu
        DSS property index: 36
        """
        return BatchFloat64ArrayProxy(self, 36)

    @Vlowpu.setter
    def Vlowpu(self, value):
        self._set_batch_float64_array(36, value)

    @property
    def puXharm(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: puXharm
        DSS property index: 37
        """
        return BatchFloat64ArrayProxy(self, 37)

    @puXharm.setter
    def puXharm(self, value):
        self._set_batch_float64_array(37, value)

    @property
    def XRharm(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: XRharm
        DSS property index: 38
        """
        return BatchFloat64ArrayProxy(self, 38)

    @XRharm.setter
    def XRharm(self, value):
        self._set_batch_float64_array(38, value)

    @property
    def spectrum(self) -> List[str]:
        """
        DSS property name: spectrum
        DSS property index: 39
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 39)

    @spectrum.setter
    def spectrum(self, value: Union[AnyStr, Spectrum]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(39, value)
            return

        self._set_batch_string(39, value)

    @property
    def spectrum_obj(self) -> List[str]:
        """
        DSS property name: spectrum
        DSS property index: 39
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 39)

    @spectrum_obj.setter
    def spectrum_obj(self, value: Spectrum):
        self._set_batch_string(39, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 40
        """
        return BatchFloat64ArrayProxy(self, 40)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(40, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 41
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 41)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 41, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 42
        """
        self._set_batch_string(42, value)

class TransformerBatch(DSSBatch):
    _cls_name = 'Transformer'
    _obj_cls = Transformer
    _cls_idx = 20


    @property
    def phases(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: phases
        DSS property index: 1
        """
        return BatchInt32ArrayProxy(self, 1)

    @phases.setter
    def phases(self, value):
        self._set_batch_int32_array(1, value)

    @property
    def windings(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: windings
        DSS property index: 2
        """
        return BatchInt32ArrayProxy(self, 2)

    @windings.setter
    def windings(self, value):
        self._set_batch_int32_array(2, value)

    @property
    def wdg(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: wdg
        DSS property index: 3
        """
        return BatchInt32ArrayProxy(self, 3)

    @wdg.setter
    def wdg(self, value):
        self._set_batch_int32_array(3, value)

    @property
    def bus(self) -> List[List[str]]:
        """
        DSS property name: bus
        DSS property index: 4
        """
        return self._get_string_ll(4)

    @bus.setter
    def bus(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._ffi.unpack(self.pointer[0], self.count[0]):
            self._lib.Obj_SetStringArray(x, 4, value_ptr, value_count)

        self._check_for_error()

    @property
    def conn(self) -> List[npt.NDArray[np.int32]]:
        """
        DSS property name: conn
        DSS property index: 5
        """
        return [
            self._get_int32_array(self._lib.Obj_GetInt32Array, x, 5)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @conn.setter
    def conn(self, value: Union[List[Union[int,Connection]], List[AnyStr]]): #TODO: list of lists
        if len(value) and not isinstance(value[0], int):
            value, value_ptr, value_count = self._prepare_string_array(value)
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetStringArray(x, 5, value_ptr, value_count)

            self._check_for_error()
            return

        self._set_batch_int32_array(5, value)

    @property
    def conn_str(self) -> List[List[str]]:
        """
        DSS property name: conn
        DSS property index: 5
        """
        return self._get_string_ll(5)

    @conn_str.setter
    def conn_str(self, value: AnyStr):
        self.conn = value

    @property
    def kV(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: kV
        DSS property index: 6
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 6)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @kV.setter
    def kV(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(6, value)

    @property
    def kVA(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: kVA
        DSS property index: 7
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 7)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @kVA.setter
    def kVA(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(7, value)

    @property
    def tap(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: tap
        DSS property index: 8
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 8)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @tap.setter
    def tap(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(8, value)

    @property
    def pctR(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: %R
        DSS property index: 9
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 9)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @pctR.setter
    def pctR(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(9, value)

    @property
    def Rneut(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: Rneut
        DSS property index: 10
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 10)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Rneut.setter
    def Rneut(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(10, value)

    @property
    def Xneut(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: Xneut
        DSS property index: 11
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 11)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Xneut.setter
    def Xneut(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(11, value)

    @property
    def buses(self) -> List[List[str]]:
        """
        DSS property name: buses
        DSS property index: 12
        """
        return self._get_string_ll(12)

    @buses.setter
    def buses(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._ffi.unpack(self.pointer[0], self.count[0]):
            self._lib.Obj_SetStringArray(x, 12, value_ptr, value_count)

        self._check_for_error()

    @property
    def conns(self) -> List[npt.NDArray[np.int32]]:
        """
        DSS property name: conns
        DSS property index: 13
        """
        return [
            self._get_int32_array(self._lib.Obj_GetInt32Array, x, 13)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @conns.setter
    def conns(self, value: Union[List[Union[int,Connection]], List[AnyStr]]): #TODO: list of lists
        if len(value) and not isinstance(value[0], int):
            value, value_ptr, value_count = self._prepare_string_array(value)
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetStringArray(x, 13, value_ptr, value_count)

            self._check_for_error()
            return

        self._set_batch_int32_array(13, value)

    @property
    def conns_str(self) -> List[List[str]]:
        """
        DSS property name: conns
        DSS property index: 13
        """
        return self._get_string_ll(13)

    @conns_str.setter
    def conns_str(self, value: AnyStr):
        self.conns = value

    @property
    def kVs(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: kVs
        DSS property index: 14
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 14)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @kVs.setter
    def kVs(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(14, value)

    @property
    def kVAs(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: kVAs
        DSS property index: 15
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 15)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @kVAs.setter
    def kVAs(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(15, value)

    @property
    def taps(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: taps
        DSS property index: 16
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 16)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @taps.setter
    def taps(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(16, value)

    @property
    def XHL(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: XHL
        DSS property index: 17
        """
        return BatchFloat64ArrayProxy(self, 17)

    @XHL.setter
    def XHL(self, value):
        self._set_batch_float64_array(17, value)

    @property
    def XHT(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: XHT
        DSS property index: 18
        """
        return BatchFloat64ArrayProxy(self, 18)

    @XHT.setter
    def XHT(self, value):
        self._set_batch_float64_array(18, value)

    @property
    def XLT(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: XLT
        DSS property index: 19
        """
        return BatchFloat64ArrayProxy(self, 19)

    @XLT.setter
    def XLT(self, value):
        self._set_batch_float64_array(19, value)

    @property
    def Xscarray(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: Xscarray
        DSS property index: 20
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 20)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Xscarray.setter
    def Xscarray(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(20, value)

    @property
    def thermal(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: thermal
        DSS property index: 21
        """
        return BatchFloat64ArrayProxy(self, 21)

    @thermal.setter
    def thermal(self, value):
        self._set_batch_float64_array(21, value)

    @property
    def n(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: n
        DSS property index: 22
        """
        return BatchFloat64ArrayProxy(self, 22)

    @n.setter
    def n(self, value):
        self._set_batch_float64_array(22, value)

    @property
    def m(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: m
        DSS property index: 23
        """
        return BatchFloat64ArrayProxy(self, 23)

    @m.setter
    def m(self, value):
        self._set_batch_float64_array(23, value)

    @property
    def flrise(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: flrise
        DSS property index: 24
        """
        return BatchFloat64ArrayProxy(self, 24)

    @flrise.setter
    def flrise(self, value):
        self._set_batch_float64_array(24, value)

    @property
    def hsrise(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: hsrise
        DSS property index: 25
        """
        return BatchFloat64ArrayProxy(self, 25)

    @hsrise.setter
    def hsrise(self, value):
        self._set_batch_float64_array(25, value)

    @property
    def pctloadloss(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %loadloss
        DSS property index: 26
        """
        return BatchFloat64ArrayProxy(self, 26)

    @pctloadloss.setter
    def pctloadloss(self, value):
        self._set_batch_float64_array(26, value)

    @property
    def pctnoloadloss(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %noloadloss
        DSS property index: 27
        """
        return BatchFloat64ArrayProxy(self, 27)

    @pctnoloadloss.setter
    def pctnoloadloss(self, value):
        self._set_batch_float64_array(27, value)

    @property
    def normhkVA(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: normhkVA
        DSS property index: 28
        """
        return BatchFloat64ArrayProxy(self, 28)

    @normhkVA.setter
    def normhkVA(self, value):
        self._set_batch_float64_array(28, value)

    @property
    def emerghkVA(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: emerghkVA
        DSS property index: 29
        """
        return BatchFloat64ArrayProxy(self, 29)

    @emerghkVA.setter
    def emerghkVA(self, value):
        self._set_batch_float64_array(29, value)

    @property
    def sub(self) -> List[bool]:
        """
        DSS property name: sub
        DSS property index: 30
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 30)
        ]
    @sub.setter
    def sub(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 30, value)

    @property
    def MaxTap(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: MaxTap
        DSS property index: 31
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 31)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @MaxTap.setter
    def MaxTap(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(31, value)

    @property
    def MinTap(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: MinTap
        DSS property index: 32
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 32)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @MinTap.setter
    def MinTap(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(32, value)

    @property
    def NumTaps(self) -> List[npt.NDArray[np.int32]]:
        """
        DSS property name: NumTaps
        DSS property index: 33
        """
        return [
            self._get_int32_array(self._lib.Obj_GetInt32Array, x, 33)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @NumTaps.setter
    def NumTaps(self, value: npt.NDArray[np.int32]): #TODO: list of arrays, matrix
        self._set_batch_int32_array(33, value)

    @property
    def subname(self) -> List[str]:
        """
        DSS property name: subname
        DSS property index: 34
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 34) 

    @subname.setter
    def subname(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 34, value)

    @property
    def pctimag(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %imag
        DSS property index: 35
        """
        return BatchFloat64ArrayProxy(self, 35)

    @pctimag.setter
    def pctimag(self, value):
        self._set_batch_float64_array(35, value)

    @property
    def ppm_antifloat(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: ppm_antifloat
        DSS property index: 36
        """
        return BatchFloat64ArrayProxy(self, 36)

    @ppm_antifloat.setter
    def ppm_antifloat(self, value):
        self._set_batch_float64_array(36, value)

    @property
    def pctRs(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: %Rs
        DSS property index: 37
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 37)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @pctRs.setter
    def pctRs(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(37, value)

    @property
    def bank(self) -> List[str]:
        """
        DSS property name: bank
        DSS property index: 38
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 38) 

    @bank.setter
    def bank(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 38, value)

    @property
    def xfmrcode(self) -> List[str]:
        """
        DSS property name: XfmrCode
        DSS property index: 39
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 39)

    @xfmrcode.setter
    def xfmrcode(self, value: Union[AnyStr, XfmrCode]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(39, value)
            return

        self._set_batch_string(39, value)

    @property
    def xfmrcode_obj(self) -> List[str]:
        """
        DSS property name: XfmrCode
        DSS property index: 39
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 39)

    @xfmrcode_obj.setter
    def xfmrcode_obj(self, value: XfmrCode):
        self._set_batch_string(39, value)

    @property
    def XRConst(self) -> List[bool]:
        """
        DSS property name: XRConst
        DSS property index: 40
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 40)
        ]
    @XRConst.setter
    def XRConst(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 40, value)

    @property
    def X12(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: X12
        DSS property index: 41
        """
        return BatchFloat64ArrayProxy(self, 41)

    @X12.setter
    def X12(self, value):
        self._set_batch_float64_array(41, value)

    @property
    def X13(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: X13
        DSS property index: 42
        """
        return BatchFloat64ArrayProxy(self, 42)

    @X13.setter
    def X13(self, value):
        self._set_batch_float64_array(42, value)

    @property
    def X23(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: X23
        DSS property index: 43
        """
        return BatchFloat64ArrayProxy(self, 43)

    @X23.setter
    def X23(self, value):
        self._set_batch_float64_array(43, value)

    @property
    def LeadLag(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: LeadLag
        DSS property index: 44
        """
        return BatchInt32ArrayProxy(self, 44)

    @LeadLag.setter
    def LeadLag(self, value: Union[AnyStr, int, PhaseSequence, List[AnyStr], List[Union[int, PhaseSequence]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(44, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(44, value)

    @property
    def LeadLag_str(self) -> str:
        """
        DSS property name: LeadLag
        DSS property index: 44
        """
        return self._get_prop_string(44)

    @LeadLag_str.setter
    def LeadLag_str(self, value: AnyStr):
        self.LeadLag = value

    def WdgCurrents(self) -> List[str]:
        """
        DSS property name: WdgCurrents
        DSS property index: 45
        """
        # []
        # StringSilentROFunction
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 45)

    @property
    def Core(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Core
        DSS property index: 46
        """
        return BatchInt32ArrayProxy(self, 46)

    @Core.setter
    def Core(self, value: Union[AnyStr, int, CoreType, List[AnyStr], List[Union[int, CoreType]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(46, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(46, value)

    @property
    def Core_str(self) -> str:
        """
        DSS property name: Core
        DSS property index: 46
        """
        return self._get_prop_string(46)

    @Core_str.setter
    def Core_str(self, value: AnyStr):
        self.Core = value

    @property
    def RdcOhms(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: RdcOhms
        DSS property index: 47
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 47)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @RdcOhms.setter
    def RdcOhms(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(47, value)

    @property
    def Seasons(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Seasons
        DSS property index: 48
        """
        return BatchInt32ArrayProxy(self, 48)

    @Seasons.setter
    def Seasons(self, value):
        self._set_batch_int32_array(48, value)

    @property
    def Ratings(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: Ratings
        DSS property index: 49
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 49)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Ratings.setter
    def Ratings(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(49, value)

    @property
    def normamps(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: normamps
        DSS property index: 50
        """
        return BatchFloat64ArrayProxy(self, 50)

    @normamps.setter
    def normamps(self, value):
        self._set_batch_float64_array(50, value)

    @property
    def emergamps(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: emergamps
        DSS property index: 51
        """
        return BatchFloat64ArrayProxy(self, 51)

    @emergamps.setter
    def emergamps(self, value):
        self._set_batch_float64_array(51, value)

    @property
    def faultrate(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: faultrate
        DSS property index: 52
        """
        return BatchFloat64ArrayProxy(self, 52)

    @faultrate.setter
    def faultrate(self, value):
        self._set_batch_float64_array(52, value)

    @property
    def pctperm(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: pctperm
        DSS property index: 53
        """
        return BatchFloat64ArrayProxy(self, 53)

    @pctperm.setter
    def pctperm(self, value):
        self._set_batch_float64_array(53, value)

    @property
    def repair(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: repair
        DSS property index: 54
        """
        return BatchFloat64ArrayProxy(self, 54)

    @repair.setter
    def repair(self, value):
        self._set_batch_float64_array(54, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 55
        """
        return BatchFloat64ArrayProxy(self, 55)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(55, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 56
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 56)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 56, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 57
        """
        self._set_batch_string(57, value)

class CapacitorBatch(DSSBatch):
    _cls_name = 'Capacitor'
    _obj_cls = Capacitor
    _cls_idx = 22


    @property
    def bus1(self) -> List[str]:
        """
        DSS property name: bus1
        DSS property index: 1
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1) 

    @bus1.setter
    def bus1(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 1, value)

    @property
    def bus2(self) -> List[str]:
        """
        DSS property name: bus2
        DSS property index: 2
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 2) 

    @bus2.setter
    def bus2(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 2, value)

    @property
    def phases(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: phases
        DSS property index: 3
        """
        return BatchInt32ArrayProxy(self, 3)

    @phases.setter
    def phases(self, value):
        self._set_batch_int32_array(3, value)

    @property
    def kvar(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: kvar
        DSS property index: 4
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 4)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @kvar.setter
    def kvar(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(4, value)

    @property
    def kv(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kv
        DSS property index: 5
        """
        return BatchFloat64ArrayProxy(self, 5)

    @kv.setter
    def kv(self, value):
        self._set_batch_float64_array(5, value)

    @property
    def conn(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: conn
        DSS property index: 6
        """
        return BatchInt32ArrayProxy(self, 6)

    @conn.setter
    def conn(self, value: Union[AnyStr, int, Connection, List[AnyStr], List[Union[int, Connection]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(6, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(6, value)

    @property
    def conn_str(self) -> str:
        """
        DSS property name: conn
        DSS property index: 6
        """
        return self._get_prop_string(6)

    @conn_str.setter
    def conn_str(self, value: AnyStr):
        self.conn = value

    @property
    def cmatrix(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: cmatrix
        DSS property index: 7
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 7)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @cmatrix.setter
    def cmatrix(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(7, value)

    @property
    def cuf(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: cuf
        DSS property index: 8
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 8)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @cuf.setter
    def cuf(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(8, value)

    @property
    def R(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: R
        DSS property index: 9
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 9)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @R.setter
    def R(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(9, value)

    @property
    def XL(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: XL
        DSS property index: 10
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 10)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @XL.setter
    def XL(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(10, value)

    @property
    def Harm(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: Harm
        DSS property index: 11
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 11)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Harm.setter
    def Harm(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(11, value)

    @property
    def Numsteps(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Numsteps
        DSS property index: 12
        """
        return BatchInt32ArrayProxy(self, 12)

    @Numsteps.setter
    def Numsteps(self, value):
        self._set_batch_int32_array(12, value)

    @property
    def states(self) -> List[npt.NDArray[np.int32]]:
        """
        DSS property name: states
        DSS property index: 13
        """
        return [
            self._get_int32_array(self._lib.Obj_GetInt32Array, x, 13)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @states.setter
    def states(self, value: npt.NDArray[np.int32]): #TODO: list of arrays, matrix
        self._set_batch_int32_array(13, value)

    @property
    def normamps(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: normamps
        DSS property index: 14
        """
        return BatchFloat64ArrayProxy(self, 14)

    @normamps.setter
    def normamps(self, value):
        self._set_batch_float64_array(14, value)

    @property
    def emergamps(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: emergamps
        DSS property index: 15
        """
        return BatchFloat64ArrayProxy(self, 15)

    @emergamps.setter
    def emergamps(self, value):
        self._set_batch_float64_array(15, value)

    @property
    def faultrate(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: faultrate
        DSS property index: 16
        """
        return BatchFloat64ArrayProxy(self, 16)

    @faultrate.setter
    def faultrate(self, value):
        self._set_batch_float64_array(16, value)

    @property
    def pctperm(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: pctperm
        DSS property index: 17
        """
        return BatchFloat64ArrayProxy(self, 17)

    @pctperm.setter
    def pctperm(self, value):
        self._set_batch_float64_array(17, value)

    @property
    def repair(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: repair
        DSS property index: 18
        """
        return BatchFloat64ArrayProxy(self, 18)

    @repair.setter
    def repair(self, value):
        self._set_batch_float64_array(18, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 19
        """
        return BatchFloat64ArrayProxy(self, 19)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(19, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 20
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 20)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 20, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 21
        """
        self._set_batch_string(21, value)

class ReactorBatch(DSSBatch):
    _cls_name = 'Reactor'
    _obj_cls = Reactor
    _cls_idx = 23


    @property
    def bus1(self) -> List[str]:
        """
        DSS property name: bus1
        DSS property index: 1
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1) 

    @bus1.setter
    def bus1(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 1, value)

    @property
    def bus2(self) -> List[str]:
        """
        DSS property name: bus2
        DSS property index: 2
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 2) 

    @bus2.setter
    def bus2(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 2, value)

    @property
    def phases(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: phases
        DSS property index: 3
        """
        return BatchInt32ArrayProxy(self, 3)

    @phases.setter
    def phases(self, value):
        self._set_batch_int32_array(3, value)

    @property
    def kvar(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kvar
        DSS property index: 4
        """
        return BatchFloat64ArrayProxy(self, 4)

    @kvar.setter
    def kvar(self, value):
        self._set_batch_float64_array(4, value)

    @property
    def kv(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kv
        DSS property index: 5
        """
        return BatchFloat64ArrayProxy(self, 5)

    @kv.setter
    def kv(self, value):
        self._set_batch_float64_array(5, value)

    @property
    def conn(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: conn
        DSS property index: 6
        """
        return BatchInt32ArrayProxy(self, 6)

    @conn.setter
    def conn(self, value: Union[AnyStr, int, Connection, List[AnyStr], List[Union[int, Connection]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(6, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(6, value)

    @property
    def conn_str(self) -> str:
        """
        DSS property name: conn
        DSS property index: 6
        """
        return self._get_prop_string(6)

    @conn_str.setter
    def conn_str(self, value: AnyStr):
        self.conn = value

    @property
    def Rmatrix(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: Rmatrix
        DSS property index: 7
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 7)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Rmatrix.setter
    def Rmatrix(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(7, value)

    @property
    def Xmatrix(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: Xmatrix
        DSS property index: 8
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 8)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Xmatrix.setter
    def Xmatrix(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(8, value)

    @property
    def Parallel(self) -> List[bool]:
        """
        DSS property name: Parallel
        DSS property index: 9
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 9)
        ]
    @Parallel.setter
    def Parallel(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 9, value)

    @property
    def R(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: R
        DSS property index: 10
        """
        return BatchFloat64ArrayProxy(self, 10)

    @R.setter
    def R(self, value):
        self._set_batch_float64_array(10, value)

    @property
    def X(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: X
        DSS property index: 11
        """
        return BatchFloat64ArrayProxy(self, 11)

    @X.setter
    def X(self, value):
        self._set_batch_float64_array(11, value)

    @property
    def Rp(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Rp
        DSS property index: 12
        """
        return BatchFloat64ArrayProxy(self, 12)

    @Rp.setter
    def Rp(self, value):
        self._set_batch_float64_array(12, value)

    @property
    def Z1(self) -> List[complex]:
        """
        DSS property name: Z1
        DSS property index: 13
        """
        return [   
            self._get_float64_array(
                self._lib.Obj_GetFloat64Array, 
                x,
                13,
            ).astype(complex)[0]
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Z1.setter
    def Z1(self, value: Union[complex, List[complex]]):
        if isinstance(value, complex):
            value, value_ptr, value_count = self._prepare_float64_array([value.real, value.imag])
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetFloat64Array(x, 13, value_ptr, value_count)
            return

        values = value
        if len(values) != self.count[0]:
            raise ValueError('Number of elements provided must match the number of objects in the batch.')

        value, value_ptr, value_count = self._prepare_float64_array([0, 0])
        for v, x in zip(values, self._ffi.unpack(self.pointer[0], self.count[0])):
            value[0] = v.real
            value[1] = v.imag
            self._lib.Obj_SetFloat64Array(x, 13, value_ptr, value_count)

    @property
    def Z2(self) -> List[complex]:
        """
        DSS property name: Z2
        DSS property index: 14
        """
        return [   
            self._get_float64_array(
                self._lib.Obj_GetFloat64Array, 
                x,
                14,
            ).astype(complex)[0]
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Z2.setter
    def Z2(self, value: Union[complex, List[complex]]):
        if isinstance(value, complex):
            value, value_ptr, value_count = self._prepare_float64_array([value.real, value.imag])
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetFloat64Array(x, 14, value_ptr, value_count)
            return

        values = value
        if len(values) != self.count[0]:
            raise ValueError('Number of elements provided must match the number of objects in the batch.')

        value, value_ptr, value_count = self._prepare_float64_array([0, 0])
        for v, x in zip(values, self._ffi.unpack(self.pointer[0], self.count[0])):
            value[0] = v.real
            value[1] = v.imag
            self._lib.Obj_SetFloat64Array(x, 14, value_ptr, value_count)

    @property
    def Z0(self) -> List[complex]:
        """
        DSS property name: Z0
        DSS property index: 15
        """
        return [   
            self._get_float64_array(
                self._lib.Obj_GetFloat64Array, 
                x,
                15,
            ).astype(complex)[0]
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Z0.setter
    def Z0(self, value: Union[complex, List[complex]]):
        if isinstance(value, complex):
            value, value_ptr, value_count = self._prepare_float64_array([value.real, value.imag])
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetFloat64Array(x, 15, value_ptr, value_count)
            return

        values = value
        if len(values) != self.count[0]:
            raise ValueError('Number of elements provided must match the number of objects in the batch.')

        value, value_ptr, value_count = self._prepare_float64_array([0, 0])
        for v, x in zip(values, self._ffi.unpack(self.pointer[0], self.count[0])):
            value[0] = v.real
            value[1] = v.imag
            self._lib.Obj_SetFloat64Array(x, 15, value_ptr, value_count)

    @property
    def Z(self) -> List[complex]:
        """
        DSS property name: Z
        DSS property index: 16
        """
        return [   
            self._get_float64_array(
                self._lib.Obj_GetFloat64Array, 
                x,
                16,
            ).astype(complex)[0]
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Z.setter
    def Z(self, value: Union[complex, List[complex]]):
        if isinstance(value, complex):
            value, value_ptr, value_count = self._prepare_float64_array([value.real, value.imag])
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetFloat64Array(x, 16, value_ptr, value_count)
            return

        values = value
        if len(values) != self.count[0]:
            raise ValueError('Number of elements provided must match the number of objects in the batch.')

        value, value_ptr, value_count = self._prepare_float64_array([0, 0])
        for v, x in zip(values, self._ffi.unpack(self.pointer[0], self.count[0])):
            value[0] = v.real
            value[1] = v.imag
            self._lib.Obj_SetFloat64Array(x, 16, value_ptr, value_count)

    @property
    def RCurve(self) -> List[str]:
        """
        DSS property name: RCurve
        DSS property index: 17
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 17)

    @RCurve.setter
    def RCurve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(17, value)
            return

        self._set_batch_string(17, value)

    @property
    def RCurve_obj(self) -> List[str]:
        """
        DSS property name: RCurve
        DSS property index: 17
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 17)

    @RCurve_obj.setter
    def RCurve_obj(self, value: XYcurve):
        self._set_batch_string(17, value)

    @property
    def LCurve(self) -> List[str]:
        """
        DSS property name: LCurve
        DSS property index: 18
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 18)

    @LCurve.setter
    def LCurve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(18, value)
            return

        self._set_batch_string(18, value)

    @property
    def LCurve_obj(self) -> List[str]:
        """
        DSS property name: LCurve
        DSS property index: 18
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 18)

    @LCurve_obj.setter
    def LCurve_obj(self, value: XYcurve):
        self._set_batch_string(18, value)

    @property
    def LmH(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: LmH
        DSS property index: 19
        """
        return BatchFloat64ArrayProxy(self, 19)

    @LmH.setter
    def LmH(self, value):
        self._set_batch_float64_array(19, value)

    @property
    def normamps(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: normamps
        DSS property index: 20
        """
        return BatchFloat64ArrayProxy(self, 20)

    @normamps.setter
    def normamps(self, value):
        self._set_batch_float64_array(20, value)

    @property
    def emergamps(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: emergamps
        DSS property index: 21
        """
        return BatchFloat64ArrayProxy(self, 21)

    @emergamps.setter
    def emergamps(self, value):
        self._set_batch_float64_array(21, value)

    @property
    def faultrate(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: faultrate
        DSS property index: 22
        """
        return BatchFloat64ArrayProxy(self, 22)

    @faultrate.setter
    def faultrate(self, value):
        self._set_batch_float64_array(22, value)

    @property
    def pctperm(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: pctperm
        DSS property index: 23
        """
        return BatchFloat64ArrayProxy(self, 23)

    @pctperm.setter
    def pctperm(self, value):
        self._set_batch_float64_array(23, value)

    @property
    def repair(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: repair
        DSS property index: 24
        """
        return BatchFloat64ArrayProxy(self, 24)

    @repair.setter
    def repair(self, value):
        self._set_batch_float64_array(24, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 25
        """
        return BatchFloat64ArrayProxy(self, 25)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(25, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 26
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 26)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 26, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 27
        """
        self._set_batch_string(27, value)

class CapControlBatch(DSSBatch):
    _cls_name = 'CapControl'
    _obj_cls = CapControl
    _cls_idx = 24


    @property
    def element(self) -> List[str]:
        """
        DSS property name: element
        DSS property index: 1
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @element.setter
    def element(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(1, value)
            return

        self._set_batch_string(1, value)

    @property
    def element_obj(self) -> List[str]:
        """
        DSS property name: element
        DSS property index: 1
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @element_obj.setter
    def element_obj(self, value: DSSObj):
        self._set_batch_string(1, value)

    @property
    def terminal(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: terminal
        DSS property index: 2
        """
        return BatchInt32ArrayProxy(self, 2)

    @terminal.setter
    def terminal(self, value):
        self._set_batch_int32_array(2, value)

    @property
    def capacitor(self) -> List[str]:
        """
        DSS property name: capacitor
        DSS property index: 3
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 3)

    @capacitor.setter
    def capacitor(self, value: Union[AnyStr, Capacitor]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(3, value)
            return

        self._set_batch_string(3, value)

    @property
    def capacitor_obj(self) -> List[str]:
        """
        DSS property name: capacitor
        DSS property index: 3
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 3)

    @capacitor_obj.setter
    def capacitor_obj(self, value: Capacitor):
        self._set_batch_string(3, value)

    @property
    def type(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: type
        DSS property index: 4
        """
        return BatchInt32ArrayProxy(self, 4)

    @type.setter
    def type(self, value: Union[AnyStr, int, CapControl.CapControlType, List[AnyStr], List[Union[int, CapControl.CapControlType]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(4, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(4, value)

    @property
    def type_str(self) -> str:
        """
        DSS property name: type
        DSS property index: 4
        """
        return self._get_prop_string(4)

    @type_str.setter
    def type_str(self, value: AnyStr):
        self.type = value

    @property
    def PTratio(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: PTratio
        DSS property index: 5
        """
        return BatchFloat64ArrayProxy(self, 5)

    @PTratio.setter
    def PTratio(self, value):
        self._set_batch_float64_array(5, value)

    @property
    def CTratio(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: CTratio
        DSS property index: 6
        """
        return BatchFloat64ArrayProxy(self, 6)

    @CTratio.setter
    def CTratio(self, value):
        self._set_batch_float64_array(6, value)

    @property
    def ONsetting(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: ONsetting
        DSS property index: 7
        """
        return BatchFloat64ArrayProxy(self, 7)

    @ONsetting.setter
    def ONsetting(self, value):
        self._set_batch_float64_array(7, value)

    @property
    def OFFsetting(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: OFFsetting
        DSS property index: 8
        """
        return BatchFloat64ArrayProxy(self, 8)

    @OFFsetting.setter
    def OFFsetting(self, value):
        self._set_batch_float64_array(8, value)

    @property
    def Delay(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Delay
        DSS property index: 9
        """
        return BatchFloat64ArrayProxy(self, 9)

    @Delay.setter
    def Delay(self, value):
        self._set_batch_float64_array(9, value)

    @property
    def VoltOverride(self) -> List[bool]:
        """
        DSS property name: VoltOverride
        DSS property index: 10
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 10)
        ]
    @VoltOverride.setter
    def VoltOverride(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 10, value)

    @property
    def Vmax(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Vmax
        DSS property index: 11
        """
        return BatchFloat64ArrayProxy(self, 11)

    @Vmax.setter
    def Vmax(self, value):
        self._set_batch_float64_array(11, value)

    @property
    def Vmin(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Vmin
        DSS property index: 12
        """
        return BatchFloat64ArrayProxy(self, 12)

    @Vmin.setter
    def Vmin(self, value):
        self._set_batch_float64_array(12, value)

    @property
    def DelayOFF(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: DelayOFF
        DSS property index: 13
        """
        return BatchFloat64ArrayProxy(self, 13)

    @DelayOFF.setter
    def DelayOFF(self, value):
        self._set_batch_float64_array(13, value)

    @property
    def DeadTime(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: DeadTime
        DSS property index: 14
        """
        return BatchFloat64ArrayProxy(self, 14)

    @DeadTime.setter
    def DeadTime(self, value):
        self._set_batch_float64_array(14, value)

    @property
    def CTPhase(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: CTPhase
        DSS property index: 15
        """
        return BatchInt32ArrayProxy(self, 15)

    @CTPhase.setter
    def CTPhase(self, value: Union[AnyStr, int, MonitoredPhase, List[AnyStr], List[Union[int, MonitoredPhase]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(15, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(15, value)

    @property
    def CTPhase_str(self) -> str:
        """
        DSS property name: CTPhase
        DSS property index: 15
        """
        return self._get_prop_string(15)

    @CTPhase_str.setter
    def CTPhase_str(self, value: AnyStr):
        self.CTPhase = value

    @property
    def PTPhase(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: PTPhase
        DSS property index: 16
        """
        return BatchInt32ArrayProxy(self, 16)

    @PTPhase.setter
    def PTPhase(self, value: Union[AnyStr, int, MonitoredPhase, List[AnyStr], List[Union[int, MonitoredPhase]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(16, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(16, value)

    @property
    def PTPhase_str(self) -> str:
        """
        DSS property name: PTPhase
        DSS property index: 16
        """
        return self._get_prop_string(16)

    @PTPhase_str.setter
    def PTPhase_str(self, value: AnyStr):
        self.PTPhase = value

    @property
    def VBus(self) -> List[str]:
        """
        DSS property name: VBus
        DSS property index: 17
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 17) 

    @VBus.setter
    def VBus(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 17, value)

    @property
    def EventLog(self) -> List[bool]:
        """
        DSS property name: EventLog
        DSS property index: 18
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 18)
        ]
    @EventLog.setter
    def EventLog(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 18, value)

    @property
    def UserModel(self) -> List[str]:
        """
        DSS property name: UserModel
        DSS property index: 19
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 19) 

    @UserModel.setter
    def UserModel(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 19, value)

    @property
    def UserData(self) -> List[str]:
        """
        DSS property name: UserData
        DSS property index: 20
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 20) 

    @UserData.setter
    def UserData(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 20, value)

    @property
    def pctMinkvar(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: pctMinkvar
        DSS property index: 21
        """
        return BatchFloat64ArrayProxy(self, 21)

    @pctMinkvar.setter
    def pctMinkvar(self, value):
        self._set_batch_float64_array(21, value)

    def Reset(self, value: bool):
        """
        DSS property name: Reset
        DSS property index: 22
        """
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 22, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 23
        """
        return BatchFloat64ArrayProxy(self, 23)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(23, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 24
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 24)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 24, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 25
        """
        self._set_batch_string(25, value)

class FaultBatch(DSSBatch):
    _cls_name = 'Fault'
    _obj_cls = Fault
    _cls_idx = 25


    @property
    def bus1(self) -> List[str]:
        """
        DSS property name: bus1
        DSS property index: 1
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1) 

    @bus1.setter
    def bus1(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 1, value)

    @property
    def bus2(self) -> List[str]:
        """
        DSS property name: bus2
        DSS property index: 2
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 2) 

    @bus2.setter
    def bus2(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 2, value)

    @property
    def phases(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: phases
        DSS property index: 3
        """
        return BatchInt32ArrayProxy(self, 3)

    @phases.setter
    def phases(self, value):
        self._set_batch_int32_array(3, value)

    @property
    def r(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: r
        DSS property index: 4
        """
        return BatchFloat64ArrayProxy(self, 4)

    @r.setter
    def r(self, value):
        self._set_batch_float64_array(4, value)

    @property
    def pctstddev(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %stddev
        DSS property index: 5
        """
        return BatchFloat64ArrayProxy(self, 5)

    @pctstddev.setter
    def pctstddev(self, value):
        self._set_batch_float64_array(5, value)

    @property
    def Gmatrix(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: Gmatrix
        DSS property index: 6
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 6)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Gmatrix.setter
    def Gmatrix(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(6, value)

    @property
    def ONtime(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: ONtime
        DSS property index: 7
        """
        return BatchFloat64ArrayProxy(self, 7)

    @ONtime.setter
    def ONtime(self, value):
        self._set_batch_float64_array(7, value)

    @property
    def temporary(self) -> List[bool]:
        """
        DSS property name: temporary
        DSS property index: 8
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 8)
        ]
    @temporary.setter
    def temporary(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 8, value)

    @property
    def MinAmps(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: MinAmps
        DSS property index: 9
        """
        return BatchFloat64ArrayProxy(self, 9)

    @MinAmps.setter
    def MinAmps(self, value):
        self._set_batch_float64_array(9, value)

    @property
    def normamps(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: normamps
        DSS property index: 10
        """
        return BatchFloat64ArrayProxy(self, 10)

    @normamps.setter
    def normamps(self, value):
        self._set_batch_float64_array(10, value)

    @property
    def emergamps(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: emergamps
        DSS property index: 11
        """
        return BatchFloat64ArrayProxy(self, 11)

    @emergamps.setter
    def emergamps(self, value):
        self._set_batch_float64_array(11, value)

    @property
    def faultrate(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: faultrate
        DSS property index: 12
        """
        return BatchFloat64ArrayProxy(self, 12)

    @faultrate.setter
    def faultrate(self, value):
        self._set_batch_float64_array(12, value)

    @property
    def pctperm(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: pctperm
        DSS property index: 13
        """
        return BatchFloat64ArrayProxy(self, 13)

    @pctperm.setter
    def pctperm(self, value):
        self._set_batch_float64_array(13, value)

    @property
    def repair(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: repair
        DSS property index: 14
        """
        return BatchFloat64ArrayProxy(self, 14)

    @repair.setter
    def repair(self, value):
        self._set_batch_float64_array(14, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 15
        """
        return BatchFloat64ArrayProxy(self, 15)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(15, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 16
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 16)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 16, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 17
        """
        self._set_batch_string(17, value)

class GeneratorBatch(DSSBatch):
    _cls_name = 'Generator'
    _obj_cls = Generator
    _cls_idx = 26


    @property
    def phases(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: phases
        DSS property index: 1
        """
        return BatchInt32ArrayProxy(self, 1)

    @phases.setter
    def phases(self, value):
        self._set_batch_int32_array(1, value)

    @property
    def bus1(self) -> List[str]:
        """
        DSS property name: bus1
        DSS property index: 2
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 2) 

    @bus1.setter
    def bus1(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 2, value)

    @property
    def kv(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kv
        DSS property index: 3
        """
        return BatchFloat64ArrayProxy(self, 3)

    @kv.setter
    def kv(self, value):
        self._set_batch_float64_array(3, value)

    @property
    def kW(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kW
        DSS property index: 4
        """
        return BatchFloat64ArrayProxy(self, 4)

    @kW.setter
    def kW(self, value):
        self._set_batch_float64_array(4, value)

    @property
    def pf(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: pf
        DSS property index: 5
        """
        return BatchFloat64ArrayProxy(self, 5)

    @pf.setter
    def pf(self, value):
        self._set_batch_float64_array(5, value)

    @property
    def kvar(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kvar
        DSS property index: 6
        """
        return BatchFloat64ArrayProxy(self, 6)

    @kvar.setter
    def kvar(self, value):
        self._set_batch_float64_array(6, value)

    @property
    def model(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: model
        DSS property index: 7
        """
        return BatchInt32ArrayProxy(self, 7)

    @model.setter
    def model(self, value):
        self._set_batch_int32_array(7, value)

    @property
    def Vminpu(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Vminpu
        DSS property index: 8
        """
        return BatchFloat64ArrayProxy(self, 8)

    @Vminpu.setter
    def Vminpu(self, value):
        self._set_batch_float64_array(8, value)

    @property
    def Vmaxpu(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Vmaxpu
        DSS property index: 9
        """
        return BatchFloat64ArrayProxy(self, 9)

    @Vmaxpu.setter
    def Vmaxpu(self, value):
        self._set_batch_float64_array(9, value)

    @property
    def yearly(self) -> List[str]:
        """
        DSS property name: yearly
        DSS property index: 10
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 10)

    @yearly.setter
    def yearly(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(10, value)
            return

        self._set_batch_string(10, value)

    @property
    def yearly_obj(self) -> List[str]:
        """
        DSS property name: yearly
        DSS property index: 10
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 10)

    @yearly_obj.setter
    def yearly_obj(self, value: LoadShape):
        self._set_batch_string(10, value)

    @property
    def daily(self) -> List[str]:
        """
        DSS property name: daily
        DSS property index: 11
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 11)

    @daily.setter
    def daily(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(11, value)
            return

        self._set_batch_string(11, value)

    @property
    def daily_obj(self) -> List[str]:
        """
        DSS property name: daily
        DSS property index: 11
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 11)

    @daily_obj.setter
    def daily_obj(self, value: LoadShape):
        self._set_batch_string(11, value)

    @property
    def duty(self) -> List[str]:
        """
        DSS property name: duty
        DSS property index: 12
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 12)

    @duty.setter
    def duty(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(12, value)
            return

        self._set_batch_string(12, value)

    @property
    def duty_obj(self) -> List[str]:
        """
        DSS property name: duty
        DSS property index: 12
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 12)

    @duty_obj.setter
    def duty_obj(self, value: LoadShape):
        self._set_batch_string(12, value)

    @property
    def dispmode(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: dispmode
        DSS property index: 13
        """
        return BatchInt32ArrayProxy(self, 13)

    @dispmode.setter
    def dispmode(self, value: Union[AnyStr, int, Generator.GeneratorDispatchMode, List[AnyStr], List[Union[int, Generator.GeneratorDispatchMode]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(13, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(13, value)

    @property
    def dispmode_str(self) -> str:
        """
        DSS property name: dispmode
        DSS property index: 13
        """
        return self._get_prop_string(13)

    @dispmode_str.setter
    def dispmode_str(self, value: AnyStr):
        self.dispmode = value

    @property
    def dispvalue(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: dispvalue
        DSS property index: 14
        """
        return BatchFloat64ArrayProxy(self, 14)

    @dispvalue.setter
    def dispvalue(self, value):
        self._set_batch_float64_array(14, value)

    @property
    def conn(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: conn
        DSS property index: 15
        """
        return BatchInt32ArrayProxy(self, 15)

    @conn.setter
    def conn(self, value: Union[AnyStr, int, Connection, List[AnyStr], List[Union[int, Connection]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(15, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(15, value)

    @property
    def conn_str(self) -> str:
        """
        DSS property name: conn
        DSS property index: 15
        """
        return self._get_prop_string(15)

    @conn_str.setter
    def conn_str(self, value: AnyStr):
        self.conn = value

    @property
    def status(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: status
        DSS property index: 16
        """
        return BatchInt32ArrayProxy(self, 16)

    @status.setter
    def status(self, value: Union[AnyStr, int, Generator.GeneratorStatus, List[AnyStr], List[Union[int, Generator.GeneratorStatus]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(16, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(16, value)

    @property
    def status_str(self) -> str:
        """
        DSS property name: status
        DSS property index: 16
        """
        return self._get_prop_string(16)

    @status_str.setter
    def status_str(self, value: AnyStr):
        self.status = value

    @property
    def cls(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: class
        DSS property index: 17
        """
        return BatchInt32ArrayProxy(self, 17)

    @cls.setter
    def cls(self, value):
        self._set_batch_int32_array(17, value)

    @property
    def Vpu(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Vpu
        DSS property index: 18
        """
        return BatchFloat64ArrayProxy(self, 18)

    @Vpu.setter
    def Vpu(self, value):
        self._set_batch_float64_array(18, value)

    @property
    def maxkvar(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: maxkvar
        DSS property index: 19
        """
        return BatchFloat64ArrayProxy(self, 19)

    @maxkvar.setter
    def maxkvar(self, value):
        self._set_batch_float64_array(19, value)

    @property
    def minkvar(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: minkvar
        DSS property index: 20
        """
        return BatchFloat64ArrayProxy(self, 20)

    @minkvar.setter
    def minkvar(self, value):
        self._set_batch_float64_array(20, value)

    @property
    def pvfactor(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: pvfactor
        DSS property index: 21
        """
        return BatchFloat64ArrayProxy(self, 21)

    @pvfactor.setter
    def pvfactor(self, value):
        self._set_batch_float64_array(21, value)

    @property
    def forceon(self) -> List[bool]:
        """
        DSS property name: forceon
        DSS property index: 22
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 22)
        ]
    @forceon.setter
    def forceon(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 22, value)

    @property
    def kVA(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kVA
        DSS property index: 23
        """
        return BatchFloat64ArrayProxy(self, 23)

    @kVA.setter
    def kVA(self, value):
        self._set_batch_float64_array(23, value)

    @property
    def MVA(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: MVA
        DSS property index: 24
        """
        return BatchFloat64ArrayProxy(self, 24)

    @MVA.setter
    def MVA(self, value):
        self._set_batch_float64_array(24, value)

    @property
    def Xd(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Xd
        DSS property index: 25
        """
        return BatchFloat64ArrayProxy(self, 25)

    @Xd.setter
    def Xd(self, value):
        self._set_batch_float64_array(25, value)

    @property
    def Xdp(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Xdp
        DSS property index: 26
        """
        return BatchFloat64ArrayProxy(self, 26)

    @Xdp.setter
    def Xdp(self, value):
        self._set_batch_float64_array(26, value)

    @property
    def Xdpp(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Xdpp
        DSS property index: 27
        """
        return BatchFloat64ArrayProxy(self, 27)

    @Xdpp.setter
    def Xdpp(self, value):
        self._set_batch_float64_array(27, value)

    @property
    def H(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: H
        DSS property index: 28
        """
        return BatchFloat64ArrayProxy(self, 28)

    @H.setter
    def H(self, value):
        self._set_batch_float64_array(28, value)

    @property
    def D(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: D
        DSS property index: 29
        """
        return BatchFloat64ArrayProxy(self, 29)

    @D.setter
    def D(self, value):
        self._set_batch_float64_array(29, value)

    @property
    def UserModel(self) -> List[str]:
        """
        DSS property name: UserModel
        DSS property index: 30
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 30) 

    @UserModel.setter
    def UserModel(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 30, value)

    @property
    def UserData(self) -> List[str]:
        """
        DSS property name: UserData
        DSS property index: 31
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 31) 

    @UserData.setter
    def UserData(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 31, value)

    @property
    def ShaftModel(self) -> List[str]:
        """
        DSS property name: ShaftModel
        DSS property index: 32
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 32) 

    @ShaftModel.setter
    def ShaftModel(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 32, value)

    @property
    def ShaftData(self) -> List[str]:
        """
        DSS property name: ShaftData
        DSS property index: 33
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 33) 

    @ShaftData.setter
    def ShaftData(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 33, value)

    @property
    def DutyStart(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: DutyStart
        DSS property index: 34
        """
        return BatchFloat64ArrayProxy(self, 34)

    @DutyStart.setter
    def DutyStart(self, value):
        self._set_batch_float64_array(34, value)

    @property
    def debugtrace(self) -> List[bool]:
        """
        DSS property name: debugtrace
        DSS property index: 35
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 35)
        ]
    @debugtrace.setter
    def debugtrace(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 35, value)

    @property
    def Balanced(self) -> List[bool]:
        """
        DSS property name: Balanced
        DSS property index: 36
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 36)
        ]
    @Balanced.setter
    def Balanced(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 36, value)

    @property
    def XRdp(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: XRdp
        DSS property index: 37
        """
        return BatchFloat64ArrayProxy(self, 37)

    @XRdp.setter
    def XRdp(self, value):
        self._set_batch_float64_array(37, value)

    @property
    def UseFuel(self) -> List[bool]:
        """
        DSS property name: UseFuel
        DSS property index: 38
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 38)
        ]
    @UseFuel.setter
    def UseFuel(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 38, value)

    @property
    def FuelkWh(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: FuelkWh
        DSS property index: 39
        """
        return BatchFloat64ArrayProxy(self, 39)

    @FuelkWh.setter
    def FuelkWh(self, value):
        self._set_batch_float64_array(39, value)

    @property
    def pctFuel(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %Fuel
        DSS property index: 40
        """
        return BatchFloat64ArrayProxy(self, 40)

    @pctFuel.setter
    def pctFuel(self, value):
        self._set_batch_float64_array(40, value)

    @property
    def pctReserve(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %Reserve
        DSS property index: 41
        """
        return BatchFloat64ArrayProxy(self, 41)

    @pctReserve.setter
    def pctReserve(self, value):
        self._set_batch_float64_array(41, value)

    def Refuel(self, value: bool):
        """
        DSS property name: Refuel
        DSS property index: 42
        """
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 42, value)

    @property
    def spectrum(self) -> List[str]:
        """
        DSS property name: spectrum
        DSS property index: 43
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 43)

    @spectrum.setter
    def spectrum(self, value: Union[AnyStr, Spectrum]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(43, value)
            return

        self._set_batch_string(43, value)

    @property
    def spectrum_obj(self) -> List[str]:
        """
        DSS property name: spectrum
        DSS property index: 43
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 43)

    @spectrum_obj.setter
    def spectrum_obj(self, value: Spectrum):
        self._set_batch_string(43, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 44
        """
        return BatchFloat64ArrayProxy(self, 44)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(44, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 45
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 45)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 45, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 46
        """
        self._set_batch_string(46, value)

class GenDispatcherBatch(DSSBatch):
    _cls_name = 'GenDispatcher'
    _obj_cls = GenDispatcher
    _cls_idx = 27


    @property
    def Element(self) -> List[str]:
        """
        DSS property name: Element
        DSS property index: 1
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @Element.setter
    def Element(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(1, value)
            return

        self._set_batch_string(1, value)

    @property
    def Element_obj(self) -> List[str]:
        """
        DSS property name: Element
        DSS property index: 1
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @Element_obj.setter
    def Element_obj(self, value: DSSObj):
        self._set_batch_string(1, value)

    @property
    def Terminal(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Terminal
        DSS property index: 2
        """
        return BatchInt32ArrayProxy(self, 2)

    @Terminal.setter
    def Terminal(self, value):
        self._set_batch_int32_array(2, value)

    @property
    def kWLimit(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kWLimit
        DSS property index: 3
        """
        return BatchFloat64ArrayProxy(self, 3)

    @kWLimit.setter
    def kWLimit(self, value):
        self._set_batch_float64_array(3, value)

    @property
    def kWBand(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kWBand
        DSS property index: 4
        """
        return BatchFloat64ArrayProxy(self, 4)

    @kWBand.setter
    def kWBand(self, value):
        self._set_batch_float64_array(4, value)

    @property
    def kvarlimit(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kvarlimit
        DSS property index: 5
        """
        return BatchFloat64ArrayProxy(self, 5)

    @kvarlimit.setter
    def kvarlimit(self, value):
        self._set_batch_float64_array(5, value)

    @property
    def GenList(self) -> List[List[str]]:
        """
        DSS property name: GenList
        DSS property index: 6
        """
        return self._get_string_ll(6)

    @GenList.setter
    def GenList(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._ffi.unpack(self.pointer[0], self.count[0]):
            self._lib.Obj_SetStringArray(x, 6, value_ptr, value_count)

        self._check_for_error()

    @property
    def Weights(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: Weights
        DSS property index: 7
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 7)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Weights.setter
    def Weights(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(7, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 8
        """
        return BatchFloat64ArrayProxy(self, 8)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(8, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 9
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 9)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 9, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 10
        """
        self._set_batch_string(10, value)

class StorageBatch(DSSBatch):
    _cls_name = 'Storage'
    _obj_cls = Storage
    _cls_idx = 28


    @property
    def phases(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: phases
        DSS property index: 1
        """
        return BatchInt32ArrayProxy(self, 1)

    @phases.setter
    def phases(self, value):
        self._set_batch_int32_array(1, value)

    @property
    def bus1(self) -> List[str]:
        """
        DSS property name: bus1
        DSS property index: 2
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 2) 

    @bus1.setter
    def bus1(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 2, value)

    @property
    def kv(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kv
        DSS property index: 3
        """
        return BatchFloat64ArrayProxy(self, 3)

    @kv.setter
    def kv(self, value):
        self._set_batch_float64_array(3, value)

    @property
    def conn(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: conn
        DSS property index: 4
        """
        return BatchInt32ArrayProxy(self, 4)

    @conn.setter
    def conn(self, value: Union[AnyStr, int, Connection, List[AnyStr], List[Union[int, Connection]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(4, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(4, value)

    @property
    def conn_str(self) -> str:
        """
        DSS property name: conn
        DSS property index: 4
        """
        return self._get_prop_string(4)

    @conn_str.setter
    def conn_str(self, value: AnyStr):
        self.conn = value

    @property
    def kW(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kW
        DSS property index: 5
        """
        return BatchFloat64ArrayProxy(self, 5)

    @kW.setter
    def kW(self, value):
        self._set_batch_float64_array(5, value)

    @property
    def kvar(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kvar
        DSS property index: 6
        """
        return BatchFloat64ArrayProxy(self, 6)

    @kvar.setter
    def kvar(self, value):
        self._set_batch_float64_array(6, value)

    @property
    def pf(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: pf
        DSS property index: 7
        """
        return BatchFloat64ArrayProxy(self, 7)

    @pf.setter
    def pf(self, value):
        self._set_batch_float64_array(7, value)

    @property
    def kVA(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kVA
        DSS property index: 8
        """
        return BatchFloat64ArrayProxy(self, 8)

    @kVA.setter
    def kVA(self, value):
        self._set_batch_float64_array(8, value)

    @property
    def pctCutin(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %Cutin
        DSS property index: 9
        """
        return BatchFloat64ArrayProxy(self, 9)

    @pctCutin.setter
    def pctCutin(self, value):
        self._set_batch_float64_array(9, value)

    @property
    def pctCutout(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %Cutout
        DSS property index: 10
        """
        return BatchFloat64ArrayProxy(self, 10)

    @pctCutout.setter
    def pctCutout(self, value):
        self._set_batch_float64_array(10, value)

    @property
    def EffCurve(self) -> List[str]:
        """
        DSS property name: EffCurve
        DSS property index: 11
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 11)

    @EffCurve.setter
    def EffCurve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(11, value)
            return

        self._set_batch_string(11, value)

    @property
    def EffCurve_obj(self) -> List[str]:
        """
        DSS property name: EffCurve
        DSS property index: 11
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 11)

    @EffCurve_obj.setter
    def EffCurve_obj(self, value: XYcurve):
        self._set_batch_string(11, value)

    @property
    def VarFollowInverter(self) -> List[bool]:
        """
        DSS property name: VarFollowInverter
        DSS property index: 12
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 12)
        ]
    @VarFollowInverter.setter
    def VarFollowInverter(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 12, value)

    @property
    def kvarMax(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kvarMax
        DSS property index: 13
        """
        return BatchFloat64ArrayProxy(self, 13)

    @kvarMax.setter
    def kvarMax(self, value):
        self._set_batch_float64_array(13, value)

    @property
    def kvarMaxAbs(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kvarMaxAbs
        DSS property index: 14
        """
        return BatchFloat64ArrayProxy(self, 14)

    @kvarMaxAbs.setter
    def kvarMaxAbs(self, value):
        self._set_batch_float64_array(14, value)

    @property
    def WattPriority(self) -> List[bool]:
        """
        DSS property name: WattPriority
        DSS property index: 15
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 15)
        ]
    @WattPriority.setter
    def WattPriority(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 15, value)

    @property
    def PFPriority(self) -> List[bool]:
        """
        DSS property name: PFPriority
        DSS property index: 16
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 16)
        ]
    @PFPriority.setter
    def PFPriority(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 16, value)

    @property
    def pctPminNoVars(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %PminNoVars
        DSS property index: 17
        """
        return BatchFloat64ArrayProxy(self, 17)

    @pctPminNoVars.setter
    def pctPminNoVars(self, value):
        self._set_batch_float64_array(17, value)

    @property
    def pctPminkvarMax(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %PminkvarMax
        DSS property index: 18
        """
        return BatchFloat64ArrayProxy(self, 18)

    @pctPminkvarMax.setter
    def pctPminkvarMax(self, value):
        self._set_batch_float64_array(18, value)

    @property
    def kWrated(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kWrated
        DSS property index: 19
        """
        return BatchFloat64ArrayProxy(self, 19)

    @kWrated.setter
    def kWrated(self, value):
        self._set_batch_float64_array(19, value)

    @property
    def pctkWrated(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %kWrated
        DSS property index: 20
        """
        return BatchFloat64ArrayProxy(self, 20)

    @pctkWrated.setter
    def pctkWrated(self, value):
        self._set_batch_float64_array(20, value)

    @property
    def kWhrated(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kWhrated
        DSS property index: 21
        """
        return BatchFloat64ArrayProxy(self, 21)

    @kWhrated.setter
    def kWhrated(self, value):
        self._set_batch_float64_array(21, value)

    @property
    def kWhstored(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kWhstored
        DSS property index: 22
        """
        return BatchFloat64ArrayProxy(self, 22)

    @kWhstored.setter
    def kWhstored(self, value):
        self._set_batch_float64_array(22, value)

    @property
    def pctstored(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %stored
        DSS property index: 23
        """
        return BatchFloat64ArrayProxy(self, 23)

    @pctstored.setter
    def pctstored(self, value):
        self._set_batch_float64_array(23, value)

    @property
    def pctreserve(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %reserve
        DSS property index: 24
        """
        return BatchFloat64ArrayProxy(self, 24)

    @pctreserve.setter
    def pctreserve(self, value):
        self._set_batch_float64_array(24, value)

    @property
    def State(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: State
        DSS property index: 25
        """
        return BatchInt32ArrayProxy(self, 25)

    @State.setter
    def State(self, value: Union[AnyStr, int, Storage.StorageState, List[AnyStr], List[Union[int, Storage.StorageState]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(25, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(25, value)

    @property
    def State_str(self) -> str:
        """
        DSS property name: State
        DSS property index: 25
        """
        return self._get_prop_string(25)

    @State_str.setter
    def State_str(self, value: AnyStr):
        self.State = value

    @property
    def pctDischarge(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %Discharge
        DSS property index: 26
        """
        return BatchFloat64ArrayProxy(self, 26)

    @pctDischarge.setter
    def pctDischarge(self, value):
        self._set_batch_float64_array(26, value)

    @property
    def pctCharge(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %Charge
        DSS property index: 27
        """
        return BatchFloat64ArrayProxy(self, 27)

    @pctCharge.setter
    def pctCharge(self, value):
        self._set_batch_float64_array(27, value)

    @property
    def pctEffCharge(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %EffCharge
        DSS property index: 28
        """
        return BatchFloat64ArrayProxy(self, 28)

    @pctEffCharge.setter
    def pctEffCharge(self, value):
        self._set_batch_float64_array(28, value)

    @property
    def pctEffDischarge(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %EffDischarge
        DSS property index: 29
        """
        return BatchFloat64ArrayProxy(self, 29)

    @pctEffDischarge.setter
    def pctEffDischarge(self, value):
        self._set_batch_float64_array(29, value)

    @property
    def pctIdlingkW(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %IdlingkW
        DSS property index: 30
        """
        return BatchFloat64ArrayProxy(self, 30)

    @pctIdlingkW.setter
    def pctIdlingkW(self, value):
        self._set_batch_float64_array(30, value)

    @property
    def pctR(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %R
        DSS property index: 31
        """
        return BatchFloat64ArrayProxy(self, 31)

    @pctR.setter
    def pctR(self, value):
        self._set_batch_float64_array(31, value)

    @property
    def pctX(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %X
        DSS property index: 32
        """
        return BatchFloat64ArrayProxy(self, 32)

    @pctX.setter
    def pctX(self, value):
        self._set_batch_float64_array(32, value)

    @property
    def model(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: model
        DSS property index: 33
        """
        return BatchInt32ArrayProxy(self, 33)

    @model.setter
    def model(self, value):
        self._set_batch_int32_array(33, value)

    @property
    def Vminpu(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Vminpu
        DSS property index: 34
        """
        return BatchFloat64ArrayProxy(self, 34)

    @Vminpu.setter
    def Vminpu(self, value):
        self._set_batch_float64_array(34, value)

    @property
    def Vmaxpu(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Vmaxpu
        DSS property index: 35
        """
        return BatchFloat64ArrayProxy(self, 35)

    @Vmaxpu.setter
    def Vmaxpu(self, value):
        self._set_batch_float64_array(35, value)

    @property
    def Balanced(self) -> List[bool]:
        """
        DSS property name: Balanced
        DSS property index: 36
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 36)
        ]
    @Balanced.setter
    def Balanced(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 36, value)

    @property
    def LimitCurrent(self) -> List[bool]:
        """
        DSS property name: LimitCurrent
        DSS property index: 37
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 37)
        ]
    @LimitCurrent.setter
    def LimitCurrent(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 37, value)

    @property
    def yearly(self) -> List[str]:
        """
        DSS property name: yearly
        DSS property index: 38
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 38)

    @yearly.setter
    def yearly(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(38, value)
            return

        self._set_batch_string(38, value)

    @property
    def yearly_obj(self) -> List[str]:
        """
        DSS property name: yearly
        DSS property index: 38
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 38)

    @yearly_obj.setter
    def yearly_obj(self, value: LoadShape):
        self._set_batch_string(38, value)

    @property
    def daily(self) -> List[str]:
        """
        DSS property name: daily
        DSS property index: 39
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 39)

    @daily.setter
    def daily(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(39, value)
            return

        self._set_batch_string(39, value)

    @property
    def daily_obj(self) -> List[str]:
        """
        DSS property name: daily
        DSS property index: 39
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 39)

    @daily_obj.setter
    def daily_obj(self, value: LoadShape):
        self._set_batch_string(39, value)

    @property
    def duty(self) -> List[str]:
        """
        DSS property name: duty
        DSS property index: 40
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 40)

    @duty.setter
    def duty(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(40, value)
            return

        self._set_batch_string(40, value)

    @property
    def duty_obj(self) -> List[str]:
        """
        DSS property name: duty
        DSS property index: 40
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 40)

    @duty_obj.setter
    def duty_obj(self, value: LoadShape):
        self._set_batch_string(40, value)

    @property
    def DispMode(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: DispMode
        DSS property index: 41
        """
        return BatchInt32ArrayProxy(self, 41)

    @DispMode.setter
    def DispMode(self, value: Union[AnyStr, int, Storage.StorageDispatchMode, List[AnyStr], List[Union[int, Storage.StorageDispatchMode]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(41, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(41, value)

    @property
    def DispMode_str(self) -> str:
        """
        DSS property name: DispMode
        DSS property index: 41
        """
        return self._get_prop_string(41)

    @DispMode_str.setter
    def DispMode_str(self, value: AnyStr):
        self.DispMode = value

    @property
    def DischargeTrigger(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: DischargeTrigger
        DSS property index: 42
        """
        return BatchFloat64ArrayProxy(self, 42)

    @DischargeTrigger.setter
    def DischargeTrigger(self, value):
        self._set_batch_float64_array(42, value)

    @property
    def ChargeTrigger(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: ChargeTrigger
        DSS property index: 43
        """
        return BatchFloat64ArrayProxy(self, 43)

    @ChargeTrigger.setter
    def ChargeTrigger(self, value):
        self._set_batch_float64_array(43, value)

    @property
    def TimeChargeTrig(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: TimeChargeTrig
        DSS property index: 44
        """
        return BatchFloat64ArrayProxy(self, 44)

    @TimeChargeTrig.setter
    def TimeChargeTrig(self, value):
        self._set_batch_float64_array(44, value)

    @property
    def cls(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: class
        DSS property index: 45
        """
        return BatchInt32ArrayProxy(self, 45)

    @cls.setter
    def cls(self, value):
        self._set_batch_int32_array(45, value)

    @property
    def DynaDLL(self) -> List[str]:
        """
        DSS property name: DynaDLL
        DSS property index: 46
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 46) 

    @DynaDLL.setter
    def DynaDLL(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 46, value)

    @property
    def DynaData(self) -> List[str]:
        """
        DSS property name: DynaData
        DSS property index: 47
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 47) 

    @DynaData.setter
    def DynaData(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 47, value)

    @property
    def UserModel(self) -> List[str]:
        """
        DSS property name: UserModel
        DSS property index: 48
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 48) 

    @UserModel.setter
    def UserModel(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 48, value)

    @property
    def UserData(self) -> List[str]:
        """
        DSS property name: UserData
        DSS property index: 49
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 49) 

    @UserData.setter
    def UserData(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 49, value)

    @property
    def debugtrace(self) -> List[bool]:
        """
        DSS property name: debugtrace
        DSS property index: 50
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 50)
        ]
    @debugtrace.setter
    def debugtrace(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 50, value)

    @property
    def spectrum(self) -> List[str]:
        """
        DSS property name: spectrum
        DSS property index: 51
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 51)

    @spectrum.setter
    def spectrum(self, value: Union[AnyStr, Spectrum]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(51, value)
            return

        self._set_batch_string(51, value)

    @property
    def spectrum_obj(self) -> List[str]:
        """
        DSS property name: spectrum
        DSS property index: 51
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 51)

    @spectrum_obj.setter
    def spectrum_obj(self, value: Spectrum):
        self._set_batch_string(51, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 52
        """
        return BatchFloat64ArrayProxy(self, 52)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(52, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 53
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 53)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 53, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 54
        """
        self._set_batch_string(54, value)

class StorageControllerBatch(DSSBatch):
    _cls_name = 'StorageController'
    _obj_cls = StorageController
    _cls_idx = 29


    @property
    def Element(self) -> List[str]:
        """
        DSS property name: Element
        DSS property index: 1
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @Element.setter
    def Element(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(1, value)
            return

        self._set_batch_string(1, value)

    @property
    def Element_obj(self) -> List[str]:
        """
        DSS property name: Element
        DSS property index: 1
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @Element_obj.setter
    def Element_obj(self, value: DSSObj):
        self._set_batch_string(1, value)

    @property
    def Terminal(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Terminal
        DSS property index: 2
        """
        return BatchInt32ArrayProxy(self, 2)

    @Terminal.setter
    def Terminal(self, value):
        self._set_batch_int32_array(2, value)

    @property
    def MonPhase(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: MonPhase
        DSS property index: 3
        """
        return BatchInt32ArrayProxy(self, 3)

    @MonPhase.setter
    def MonPhase(self, value: Union[AnyStr, int, MonitoredPhase, List[AnyStr], List[Union[int, MonitoredPhase]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(3, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(3, value)

    @property
    def MonPhase_str(self) -> str:
        """
        DSS property name: MonPhase
        DSS property index: 3
        """
        return self._get_prop_string(3)

    @MonPhase_str.setter
    def MonPhase_str(self, value: AnyStr):
        self.MonPhase = value

    @property
    def kWTarget(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kWTarget
        DSS property index: 4
        """
        return BatchFloat64ArrayProxy(self, 4)

    @kWTarget.setter
    def kWTarget(self, value):
        self._set_batch_float64_array(4, value)

    @property
    def kWTargetLow(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kWTargetLow
        DSS property index: 5
        """
        return BatchFloat64ArrayProxy(self, 5)

    @kWTargetLow.setter
    def kWTargetLow(self, value):
        self._set_batch_float64_array(5, value)

    @property
    def pctkWBand(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %kWBand
        DSS property index: 6
        """
        return BatchFloat64ArrayProxy(self, 6)

    @pctkWBand.setter
    def pctkWBand(self, value):
        self._set_batch_float64_array(6, value)

    @property
    def kWBand(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kWBand
        DSS property index: 7
        """
        return BatchFloat64ArrayProxy(self, 7)

    @kWBand.setter
    def kWBand(self, value):
        self._set_batch_float64_array(7, value)

    @property
    def pctkWBandLow(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %kWBandLow
        DSS property index: 8
        """
        return BatchFloat64ArrayProxy(self, 8)

    @pctkWBandLow.setter
    def pctkWBandLow(self, value):
        self._set_batch_float64_array(8, value)

    @property
    def kWBandLow(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kWBandLow
        DSS property index: 9
        """
        return BatchFloat64ArrayProxy(self, 9)

    @kWBandLow.setter
    def kWBandLow(self, value):
        self._set_batch_float64_array(9, value)

    @property
    def ElementList(self) -> List[List[str]]:
        """
        DSS property name: ElementList
        DSS property index: 10
        """
        return self._get_string_ll(10)

    @ElementList.setter
    def ElementList(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._ffi.unpack(self.pointer[0], self.count[0]):
            self._lib.Obj_SetStringArray(x, 10, value_ptr, value_count)

        self._check_for_error()

    @property
    def Weights(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: Weights
        DSS property index: 11
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 11)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Weights.setter
    def Weights(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(11, value)

    @property
    def ModeDischarge(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: ModeDischarge
        DSS property index: 12
        """
        return BatchInt32ArrayProxy(self, 12)

    @ModeDischarge.setter
    def ModeDischarge(self, value: Union[AnyStr, int, StorageController.StorageControllerDischargemode, List[AnyStr], List[Union[int, StorageController.StorageControllerDischargemode]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(12, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(12, value)

    @property
    def ModeDischarge_str(self) -> str:
        """
        DSS property name: ModeDischarge
        DSS property index: 12
        """
        return self._get_prop_string(12)

    @ModeDischarge_str.setter
    def ModeDischarge_str(self, value: AnyStr):
        self.ModeDischarge = value

    @property
    def ModeCharge(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: ModeCharge
        DSS property index: 13
        """
        return BatchInt32ArrayProxy(self, 13)

    @ModeCharge.setter
    def ModeCharge(self, value: Union[AnyStr, int, StorageController.StorageControllerChargemode, List[AnyStr], List[Union[int, StorageController.StorageControllerChargemode]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(13, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(13, value)

    @property
    def ModeCharge_str(self) -> str:
        """
        DSS property name: ModeCharge
        DSS property index: 13
        """
        return self._get_prop_string(13)

    @ModeCharge_str.setter
    def ModeCharge_str(self, value: AnyStr):
        self.ModeCharge = value

    @property
    def TimeDischargeTrigger(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: TimeDischargeTrigger
        DSS property index: 14
        """
        return BatchFloat64ArrayProxy(self, 14)

    @TimeDischargeTrigger.setter
    def TimeDischargeTrigger(self, value):
        self._set_batch_float64_array(14, value)

    @property
    def TimeChargeTrigger(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: TimeChargeTrigger
        DSS property index: 15
        """
        return BatchFloat64ArrayProxy(self, 15)

    @TimeChargeTrigger.setter
    def TimeChargeTrigger(self, value):
        self._set_batch_float64_array(15, value)

    @property
    def pctRatekW(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %RatekW
        DSS property index: 16
        """
        return BatchFloat64ArrayProxy(self, 16)

    @pctRatekW.setter
    def pctRatekW(self, value):
        self._set_batch_float64_array(16, value)

    @property
    def pctRateCharge(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %RateCharge
        DSS property index: 17
        """
        return BatchFloat64ArrayProxy(self, 17)

    @pctRateCharge.setter
    def pctRateCharge(self, value):
        self._set_batch_float64_array(17, value)

    @property
    def pctReserve(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %Reserve
        DSS property index: 18
        """
        return BatchFloat64ArrayProxy(self, 18)

    @pctReserve.setter
    def pctReserve(self, value):
        self._set_batch_float64_array(18, value)

    @property
    def kWhTotal(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kWhTotal
        DSS property index: 19
        """
        return BatchFloat64ArrayProxy(self, 19)

    @kWhTotal.setter
    def kWhTotal(self, value):
        self._set_batch_float64_array(19, value)

    @property
    def kWTotal(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kWTotal
        DSS property index: 20
        """
        return BatchFloat64ArrayProxy(self, 20)

    @kWTotal.setter
    def kWTotal(self, value):
        self._set_batch_float64_array(20, value)

    @property
    def kWhActual(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kWhActual
        DSS property index: 21
        """
        return BatchFloat64ArrayProxy(self, 21)

    @kWhActual.setter
    def kWhActual(self, value):
        self._set_batch_float64_array(21, value)

    @property
    def kWActual(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kWActual
        DSS property index: 22
        """
        return BatchFloat64ArrayProxy(self, 22)

    @kWActual.setter
    def kWActual(self, value):
        self._set_batch_float64_array(22, value)

    @property
    def kWneed(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kWneed
        DSS property index: 23
        """
        return BatchFloat64ArrayProxy(self, 23)

    @kWneed.setter
    def kWneed(self, value):
        self._set_batch_float64_array(23, value)

    @property
    def Yearly(self) -> List[str]:
        """
        DSS property name: Yearly
        DSS property index: 24
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 24)

    @Yearly.setter
    def Yearly(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(24, value)
            return

        self._set_batch_string(24, value)

    @property
    def Yearly_obj(self) -> List[str]:
        """
        DSS property name: Yearly
        DSS property index: 24
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 24)

    @Yearly_obj.setter
    def Yearly_obj(self, value: LoadShape):
        self._set_batch_string(24, value)

    @property
    def Daily(self) -> List[str]:
        """
        DSS property name: Daily
        DSS property index: 25
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 25)

    @Daily.setter
    def Daily(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(25, value)
            return

        self._set_batch_string(25, value)

    @property
    def Daily_obj(self) -> List[str]:
        """
        DSS property name: Daily
        DSS property index: 25
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 25)

    @Daily_obj.setter
    def Daily_obj(self, value: LoadShape):
        self._set_batch_string(25, value)

    @property
    def Duty(self) -> List[str]:
        """
        DSS property name: Duty
        DSS property index: 26
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 26)

    @Duty.setter
    def Duty(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(26, value)
            return

        self._set_batch_string(26, value)

    @property
    def Duty_obj(self) -> List[str]:
        """
        DSS property name: Duty
        DSS property index: 26
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 26)

    @Duty_obj.setter
    def Duty_obj(self, value: LoadShape):
        self._set_batch_string(26, value)

    @property
    def EventLog(self) -> List[bool]:
        """
        DSS property name: EventLog
        DSS property index: 27
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 27)
        ]
    @EventLog.setter
    def EventLog(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 27, value)

    @property
    def InhibitTime(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: InhibitTime
        DSS property index: 28
        """
        return BatchInt32ArrayProxy(self, 28)

    @InhibitTime.setter
    def InhibitTime(self, value):
        self._set_batch_int32_array(28, value)

    @property
    def Tup(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Tup
        DSS property index: 29
        """
        return BatchFloat64ArrayProxy(self, 29)

    @Tup.setter
    def Tup(self, value):
        self._set_batch_float64_array(29, value)

    @property
    def TFlat(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: TFlat
        DSS property index: 30
        """
        return BatchFloat64ArrayProxy(self, 30)

    @TFlat.setter
    def TFlat(self, value):
        self._set_batch_float64_array(30, value)

    @property
    def Tdn(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Tdn
        DSS property index: 31
        """
        return BatchFloat64ArrayProxy(self, 31)

    @Tdn.setter
    def Tdn(self, value):
        self._set_batch_float64_array(31, value)

    @property
    def kWThreshold(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kWThreshold
        DSS property index: 32
        """
        return BatchFloat64ArrayProxy(self, 32)

    @kWThreshold.setter
    def kWThreshold(self, value):
        self._set_batch_float64_array(32, value)

    @property
    def DispFactor(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: DispFactor
        DSS property index: 33
        """
        return BatchFloat64ArrayProxy(self, 33)

    @DispFactor.setter
    def DispFactor(self, value):
        self._set_batch_float64_array(33, value)

    @property
    def ResetLevel(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: ResetLevel
        DSS property index: 34
        """
        return BatchFloat64ArrayProxy(self, 34)

    @ResetLevel.setter
    def ResetLevel(self, value):
        self._set_batch_float64_array(34, value)

    @property
    def Seasons(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Seasons
        DSS property index: 35
        """
        return BatchInt32ArrayProxy(self, 35)

    @Seasons.setter
    def Seasons(self, value):
        self._set_batch_int32_array(35, value)

    @property
    def SeasonTargets(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: SeasonTargets
        DSS property index: 36
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 36)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @SeasonTargets.setter
    def SeasonTargets(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(36, value)

    @property
    def SeasonTargetsLow(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: SeasonTargetsLow
        DSS property index: 37
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 37)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @SeasonTargetsLow.setter
    def SeasonTargetsLow(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(37, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 38
        """
        return BatchFloat64ArrayProxy(self, 38)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(38, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 39
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 39)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 39, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 40
        """
        self._set_batch_string(40, value)

class RelayBatch(DSSBatch):
    _cls_name = 'Relay'
    _obj_cls = Relay
    _cls_idx = 30


    @property
    def MonitoredObj(self) -> List[str]:
        """
        DSS property name: MonitoredObj
        DSS property index: 1
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @MonitoredObj.setter
    def MonitoredObj(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(1, value)
            return

        self._set_batch_string(1, value)

    @property
    def MonitoredObj_obj(self) -> List[str]:
        """
        DSS property name: MonitoredObj
        DSS property index: 1
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @MonitoredObj_obj.setter
    def MonitoredObj_obj(self, value: DSSObj):
        self._set_batch_string(1, value)

    @property
    def MonitoredTerm(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: MonitoredTerm
        DSS property index: 2
        """
        return BatchInt32ArrayProxy(self, 2)

    @MonitoredTerm.setter
    def MonitoredTerm(self, value):
        self._set_batch_int32_array(2, value)

    @property
    def SwitchedObj(self) -> List[str]:
        """
        DSS property name: SwitchedObj
        DSS property index: 3
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 3)

    @SwitchedObj.setter
    def SwitchedObj(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(3, value)
            return

        self._set_batch_string(3, value)

    @property
    def SwitchedObj_obj(self) -> List[str]:
        """
        DSS property name: SwitchedObj
        DSS property index: 3
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 3)

    @SwitchedObj_obj.setter
    def SwitchedObj_obj(self, value: DSSObj):
        self._set_batch_string(3, value)

    @property
    def SwitchedTerm(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: SwitchedTerm
        DSS property index: 4
        """
        return BatchInt32ArrayProxy(self, 4)

    @SwitchedTerm.setter
    def SwitchedTerm(self, value):
        self._set_batch_int32_array(4, value)

    @property
    def type(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: type
        DSS property index: 5
        """
        return BatchInt32ArrayProxy(self, 5)

    @type.setter
    def type(self, value: Union[AnyStr, int, Relay.RelayType, List[AnyStr], List[Union[int, Relay.RelayType]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(5, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(5, value)

    @property
    def type_str(self) -> str:
        """
        DSS property name: type
        DSS property index: 5
        """
        return self._get_prop_string(5)

    @type_str.setter
    def type_str(self, value: AnyStr):
        self.type = value

    @property
    def Phasecurve(self) -> List[str]:
        """
        DSS property name: Phasecurve
        DSS property index: 6
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 6)

    @Phasecurve.setter
    def Phasecurve(self, value: Union[AnyStr, TCC_Curve]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(6, value)
            return

        self._set_batch_string(6, value)

    @property
    def Phasecurve_obj(self) -> List[str]:
        """
        DSS property name: Phasecurve
        DSS property index: 6
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 6)

    @Phasecurve_obj.setter
    def Phasecurve_obj(self, value: TCC_Curve):
        self._set_batch_string(6, value)

    @property
    def Groundcurve(self) -> List[str]:
        """
        DSS property name: Groundcurve
        DSS property index: 7
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 7)

    @Groundcurve.setter
    def Groundcurve(self, value: Union[AnyStr, TCC_Curve]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(7, value)
            return

        self._set_batch_string(7, value)

    @property
    def Groundcurve_obj(self) -> List[str]:
        """
        DSS property name: Groundcurve
        DSS property index: 7
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 7)

    @Groundcurve_obj.setter
    def Groundcurve_obj(self, value: TCC_Curve):
        self._set_batch_string(7, value)

    @property
    def PhaseTrip(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: PhaseTrip
        DSS property index: 8
        """
        return BatchFloat64ArrayProxy(self, 8)

    @PhaseTrip.setter
    def PhaseTrip(self, value):
        self._set_batch_float64_array(8, value)

    @property
    def GroundTrip(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: GroundTrip
        DSS property index: 9
        """
        return BatchFloat64ArrayProxy(self, 9)

    @GroundTrip.setter
    def GroundTrip(self, value):
        self._set_batch_float64_array(9, value)

    @property
    def TDPhase(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: TDPhase
        DSS property index: 10
        """
        return BatchFloat64ArrayProxy(self, 10)

    @TDPhase.setter
    def TDPhase(self, value):
        self._set_batch_float64_array(10, value)

    @property
    def TDGround(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: TDGround
        DSS property index: 11
        """
        return BatchFloat64ArrayProxy(self, 11)

    @TDGround.setter
    def TDGround(self, value):
        self._set_batch_float64_array(11, value)

    @property
    def PhaseInst(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: PhaseInst
        DSS property index: 12
        """
        return BatchFloat64ArrayProxy(self, 12)

    @PhaseInst.setter
    def PhaseInst(self, value):
        self._set_batch_float64_array(12, value)

    @property
    def GroundInst(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: GroundInst
        DSS property index: 13
        """
        return BatchFloat64ArrayProxy(self, 13)

    @GroundInst.setter
    def GroundInst(self, value):
        self._set_batch_float64_array(13, value)

    @property
    def Reset(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Reset
        DSS property index: 14
        """
        return BatchFloat64ArrayProxy(self, 14)

    @Reset.setter
    def Reset(self, value):
        self._set_batch_float64_array(14, value)

    @property
    def Shots(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Shots
        DSS property index: 15
        """
        return BatchInt32ArrayProxy(self, 15)

    @Shots.setter
    def Shots(self, value):
        self._set_batch_int32_array(15, value)

    @property
    def RecloseIntervals(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: RecloseIntervals
        DSS property index: 16
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 16)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @RecloseIntervals.setter
    def RecloseIntervals(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(16, value)

    @property
    def Delay(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Delay
        DSS property index: 17
        """
        return BatchFloat64ArrayProxy(self, 17)

    @Delay.setter
    def Delay(self, value):
        self._set_batch_float64_array(17, value)

    @property
    def Overvoltcurve(self) -> List[str]:
        """
        DSS property name: Overvoltcurve
        DSS property index: 18
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 18)

    @Overvoltcurve.setter
    def Overvoltcurve(self, value: Union[AnyStr, TCC_Curve]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(18, value)
            return

        self._set_batch_string(18, value)

    @property
    def Overvoltcurve_obj(self) -> List[str]:
        """
        DSS property name: Overvoltcurve
        DSS property index: 18
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 18)

    @Overvoltcurve_obj.setter
    def Overvoltcurve_obj(self, value: TCC_Curve):
        self._set_batch_string(18, value)

    @property
    def Undervoltcurve(self) -> List[str]:
        """
        DSS property name: Undervoltcurve
        DSS property index: 19
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 19)

    @Undervoltcurve.setter
    def Undervoltcurve(self, value: Union[AnyStr, TCC_Curve]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(19, value)
            return

        self._set_batch_string(19, value)

    @property
    def Undervoltcurve_obj(self) -> List[str]:
        """
        DSS property name: Undervoltcurve
        DSS property index: 19
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 19)

    @Undervoltcurve_obj.setter
    def Undervoltcurve_obj(self, value: TCC_Curve):
        self._set_batch_string(19, value)

    @property
    def kvbase(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kvbase
        DSS property index: 20
        """
        return BatchFloat64ArrayProxy(self, 20)

    @kvbase.setter
    def kvbase(self, value):
        self._set_batch_float64_array(20, value)

    @property
    def pctPickup47(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: 47%Pickup
        DSS property index: 21
        """
        return BatchFloat64ArrayProxy(self, 21)

    @pctPickup47.setter
    def pctPickup47(self, value):
        self._set_batch_float64_array(21, value)

    @property
    def BaseAmps46(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: 46BaseAmps
        DSS property index: 22
        """
        return BatchFloat64ArrayProxy(self, 22)

    @BaseAmps46.setter
    def BaseAmps46(self, value):
        self._set_batch_float64_array(22, value)

    @property
    def pctPickup46(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: 46%Pickup
        DSS property index: 23
        """
        return BatchFloat64ArrayProxy(self, 23)

    @pctPickup46.setter
    def pctPickup46(self, value):
        self._set_batch_float64_array(23, value)

    @property
    def isqt46(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: 46isqt
        DSS property index: 24
        """
        return BatchFloat64ArrayProxy(self, 24)

    @isqt46.setter
    def isqt46(self, value):
        self._set_batch_float64_array(24, value)

    @property
    def Variable(self) -> List[str]:
        """
        DSS property name: Variable
        DSS property index: 25
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 25) 

    @Variable.setter
    def Variable(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 25, value)

    @property
    def overtrip(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: overtrip
        DSS property index: 26
        """
        return BatchFloat64ArrayProxy(self, 26)

    @overtrip.setter
    def overtrip(self, value):
        self._set_batch_float64_array(26, value)

    @property
    def undertrip(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: undertrip
        DSS property index: 27
        """
        return BatchFloat64ArrayProxy(self, 27)

    @undertrip.setter
    def undertrip(self, value):
        self._set_batch_float64_array(27, value)

    @property
    def Breakertime(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Breakertime
        DSS property index: 28
        """
        return BatchFloat64ArrayProxy(self, 28)

    @Breakertime.setter
    def Breakertime(self, value):
        self._set_batch_float64_array(28, value)

    @property
    def action(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: action
        DSS property index: 29
        """
        return BatchInt32ArrayProxy(self, 29)

    @action.setter
    def action(self, value: Union[AnyStr, int, Relay.RelayAction, List[AnyStr], List[Union[int, Relay.RelayAction]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(29, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(29, value)

    @property
    def action_str(self) -> str:
        """
        DSS property name: action
        DSS property index: 29
        """
        return self._get_prop_string(29)

    @action_str.setter
    def action_str(self, value: AnyStr):
        self.action = value

    @property
    def Z1mag(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Z1mag
        DSS property index: 30
        """
        return BatchFloat64ArrayProxy(self, 30)

    @Z1mag.setter
    def Z1mag(self, value):
        self._set_batch_float64_array(30, value)

    @property
    def Z1ang(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Z1ang
        DSS property index: 31
        """
        return BatchFloat64ArrayProxy(self, 31)

    @Z1ang.setter
    def Z1ang(self, value):
        self._set_batch_float64_array(31, value)

    @property
    def Z0mag(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Z0mag
        DSS property index: 32
        """
        return BatchFloat64ArrayProxy(self, 32)

    @Z0mag.setter
    def Z0mag(self, value):
        self._set_batch_float64_array(32, value)

    @property
    def Z0ang(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Z0ang
        DSS property index: 33
        """
        return BatchFloat64ArrayProxy(self, 33)

    @Z0ang.setter
    def Z0ang(self, value):
        self._set_batch_float64_array(33, value)

    @property
    def Mphase(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Mphase
        DSS property index: 34
        """
        return BatchFloat64ArrayProxy(self, 34)

    @Mphase.setter
    def Mphase(self, value):
        self._set_batch_float64_array(34, value)

    @property
    def Mground(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Mground
        DSS property index: 35
        """
        return BatchFloat64ArrayProxy(self, 35)

    @Mground.setter
    def Mground(self, value):
        self._set_batch_float64_array(35, value)

    @property
    def EventLog(self) -> List[bool]:
        """
        DSS property name: EventLog
        DSS property index: 36
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 36)
        ]
    @EventLog.setter
    def EventLog(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 36, value)

    @property
    def DebugTrace(self) -> List[bool]:
        """
        DSS property name: DebugTrace
        DSS property index: 37
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 37)
        ]
    @DebugTrace.setter
    def DebugTrace(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 37, value)

    @property
    def DistReverse(self) -> List[bool]:
        """
        DSS property name: DistReverse
        DSS property index: 38
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 38)
        ]
    @DistReverse.setter
    def DistReverse(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 38, value)

    @property
    def Normal(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Normal
        DSS property index: 39
        """
        return BatchInt32ArrayProxy(self, 39)

    @Normal.setter
    def Normal(self, value: Union[AnyStr, int, Relay.RelayState, List[AnyStr], List[Union[int, Relay.RelayState]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(39, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(39, value)

    @property
    def Normal_str(self) -> str:
        """
        DSS property name: Normal
        DSS property index: 39
        """
        return self._get_prop_string(39)

    @Normal_str.setter
    def Normal_str(self, value: AnyStr):
        self.Normal = value

    @property
    def State(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: State
        DSS property index: 40
        """
        return BatchInt32ArrayProxy(self, 40)

    @State.setter
    def State(self, value: Union[AnyStr, int, Relay.RelayState, List[AnyStr], List[Union[int, Relay.RelayState]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(40, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(40, value)

    @property
    def State_str(self) -> str:
        """
        DSS property name: State
        DSS property index: 40
        """
        return self._get_prop_string(40)

    @State_str.setter
    def State_str(self, value: AnyStr):
        self.State = value

    @property
    def DOC_TiltAngleLow(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: DOC_TiltAngleLow
        DSS property index: 41
        """
        return BatchFloat64ArrayProxy(self, 41)

    @DOC_TiltAngleLow.setter
    def DOC_TiltAngleLow(self, value):
        self._set_batch_float64_array(41, value)

    @property
    def DOC_TiltAngleHigh(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: DOC_TiltAngleHigh
        DSS property index: 42
        """
        return BatchFloat64ArrayProxy(self, 42)

    @DOC_TiltAngleHigh.setter
    def DOC_TiltAngleHigh(self, value):
        self._set_batch_float64_array(42, value)

    @property
    def DOC_TripSettingLow(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: DOC_TripSettingLow
        DSS property index: 43
        """
        return BatchFloat64ArrayProxy(self, 43)

    @DOC_TripSettingLow.setter
    def DOC_TripSettingLow(self, value):
        self._set_batch_float64_array(43, value)

    @property
    def DOC_TripSettingHigh(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: DOC_TripSettingHigh
        DSS property index: 44
        """
        return BatchFloat64ArrayProxy(self, 44)

    @DOC_TripSettingHigh.setter
    def DOC_TripSettingHigh(self, value):
        self._set_batch_float64_array(44, value)

    @property
    def DOC_TripSettingMag(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: DOC_TripSettingMag
        DSS property index: 45
        """
        return BatchFloat64ArrayProxy(self, 45)

    @DOC_TripSettingMag.setter
    def DOC_TripSettingMag(self, value):
        self._set_batch_float64_array(45, value)

    @property
    def DOC_DelayInner(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: DOC_DelayInner
        DSS property index: 46
        """
        return BatchFloat64ArrayProxy(self, 46)

    @DOC_DelayInner.setter
    def DOC_DelayInner(self, value):
        self._set_batch_float64_array(46, value)

    @property
    def DOC_PhaseCurveInner(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: DOC_PhaseCurveInner
        DSS property index: 47
        """
        return BatchFloat64ArrayProxy(self, 47)

    @DOC_PhaseCurveInner.setter
    def DOC_PhaseCurveInner(self, value):
        self._set_batch_float64_array(47, value)

    @property
    def DOC_PhaseTripInner(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: DOC_PhaseTripInner
        DSS property index: 48
        """
        return BatchFloat64ArrayProxy(self, 48)

    @DOC_PhaseTripInner.setter
    def DOC_PhaseTripInner(self, value):
        self._set_batch_float64_array(48, value)

    @property
    def DOC_TDPhaseInner(self) -> List[str]:
        """
        DSS property name: DOC_TDPhaseInner
        DSS property index: 49
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 49)

    @DOC_TDPhaseInner.setter
    def DOC_TDPhaseInner(self, value: Union[AnyStr, TCC_Curve]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(49, value)
            return

        self._set_batch_string(49, value)

    @property
    def DOC_TDPhaseInner_obj(self) -> List[str]:
        """
        DSS property name: DOC_TDPhaseInner
        DSS property index: 49
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 49)

    @DOC_TDPhaseInner_obj.setter
    def DOC_TDPhaseInner_obj(self, value: TCC_Curve):
        self._set_batch_string(49, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 50
        """
        return BatchFloat64ArrayProxy(self, 50)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(50, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 51
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 51)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 51, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 52
        """
        self._set_batch_string(52, value)

class RecloserBatch(DSSBatch):
    _cls_name = 'Recloser'
    _obj_cls = Recloser
    _cls_idx = 31


    @property
    def MonitoredObj(self) -> List[str]:
        """
        DSS property name: MonitoredObj
        DSS property index: 1
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @MonitoredObj.setter
    def MonitoredObj(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(1, value)
            return

        self._set_batch_string(1, value)

    @property
    def MonitoredObj_obj(self) -> List[str]:
        """
        DSS property name: MonitoredObj
        DSS property index: 1
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @MonitoredObj_obj.setter
    def MonitoredObj_obj(self, value: DSSObj):
        self._set_batch_string(1, value)

    @property
    def MonitoredTerm(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: MonitoredTerm
        DSS property index: 2
        """
        return BatchInt32ArrayProxy(self, 2)

    @MonitoredTerm.setter
    def MonitoredTerm(self, value):
        self._set_batch_int32_array(2, value)

    @property
    def SwitchedObj(self) -> List[str]:
        """
        DSS property name: SwitchedObj
        DSS property index: 3
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 3)

    @SwitchedObj.setter
    def SwitchedObj(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(3, value)
            return

        self._set_batch_string(3, value)

    @property
    def SwitchedObj_obj(self) -> List[str]:
        """
        DSS property name: SwitchedObj
        DSS property index: 3
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 3)

    @SwitchedObj_obj.setter
    def SwitchedObj_obj(self, value: DSSObj):
        self._set_batch_string(3, value)

    @property
    def SwitchedTerm(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: SwitchedTerm
        DSS property index: 4
        """
        return BatchInt32ArrayProxy(self, 4)

    @SwitchedTerm.setter
    def SwitchedTerm(self, value):
        self._set_batch_int32_array(4, value)

    @property
    def NumFast(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: NumFast
        DSS property index: 5
        """
        return BatchInt32ArrayProxy(self, 5)

    @NumFast.setter
    def NumFast(self, value):
        self._set_batch_int32_array(5, value)

    @property
    def PhaseFast(self) -> List[str]:
        """
        DSS property name: PhaseFast
        DSS property index: 6
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 6)

    @PhaseFast.setter
    def PhaseFast(self, value: Union[AnyStr, TCC_Curve]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(6, value)
            return

        self._set_batch_string(6, value)

    @property
    def PhaseFast_obj(self) -> List[str]:
        """
        DSS property name: PhaseFast
        DSS property index: 6
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 6)

    @PhaseFast_obj.setter
    def PhaseFast_obj(self, value: TCC_Curve):
        self._set_batch_string(6, value)

    @property
    def PhaseDelayed(self) -> List[str]:
        """
        DSS property name: PhaseDelayed
        DSS property index: 7
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 7)

    @PhaseDelayed.setter
    def PhaseDelayed(self, value: Union[AnyStr, TCC_Curve]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(7, value)
            return

        self._set_batch_string(7, value)

    @property
    def PhaseDelayed_obj(self) -> List[str]:
        """
        DSS property name: PhaseDelayed
        DSS property index: 7
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 7)

    @PhaseDelayed_obj.setter
    def PhaseDelayed_obj(self, value: TCC_Curve):
        self._set_batch_string(7, value)

    @property
    def GroundFast(self) -> List[str]:
        """
        DSS property name: GroundFast
        DSS property index: 8
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 8)

    @GroundFast.setter
    def GroundFast(self, value: Union[AnyStr, TCC_Curve]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(8, value)
            return

        self._set_batch_string(8, value)

    @property
    def GroundFast_obj(self) -> List[str]:
        """
        DSS property name: GroundFast
        DSS property index: 8
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 8)

    @GroundFast_obj.setter
    def GroundFast_obj(self, value: TCC_Curve):
        self._set_batch_string(8, value)

    @property
    def GroundDelayed(self) -> List[str]:
        """
        DSS property name: GroundDelayed
        DSS property index: 9
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 9)

    @GroundDelayed.setter
    def GroundDelayed(self, value: Union[AnyStr, TCC_Curve]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(9, value)
            return

        self._set_batch_string(9, value)

    @property
    def GroundDelayed_obj(self) -> List[str]:
        """
        DSS property name: GroundDelayed
        DSS property index: 9
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 9)

    @GroundDelayed_obj.setter
    def GroundDelayed_obj(self, value: TCC_Curve):
        self._set_batch_string(9, value)

    @property
    def PhaseTrip(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: PhaseTrip
        DSS property index: 10
        """
        return BatchFloat64ArrayProxy(self, 10)

    @PhaseTrip.setter
    def PhaseTrip(self, value):
        self._set_batch_float64_array(10, value)

    @property
    def GroundTrip(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: GroundTrip
        DSS property index: 11
        """
        return BatchFloat64ArrayProxy(self, 11)

    @GroundTrip.setter
    def GroundTrip(self, value):
        self._set_batch_float64_array(11, value)

    @property
    def PhaseInst(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: PhaseInst
        DSS property index: 12
        """
        return BatchFloat64ArrayProxy(self, 12)

    @PhaseInst.setter
    def PhaseInst(self, value):
        self._set_batch_float64_array(12, value)

    @property
    def GroundInst(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: GroundInst
        DSS property index: 13
        """
        return BatchFloat64ArrayProxy(self, 13)

    @GroundInst.setter
    def GroundInst(self, value):
        self._set_batch_float64_array(13, value)

    @property
    def Reset(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Reset
        DSS property index: 14
        """
        return BatchFloat64ArrayProxy(self, 14)

    @Reset.setter
    def Reset(self, value):
        self._set_batch_float64_array(14, value)

    @property
    def Shots(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Shots
        DSS property index: 15
        """
        return BatchInt32ArrayProxy(self, 15)

    @Shots.setter
    def Shots(self, value):
        self._set_batch_int32_array(15, value)

    @property
    def RecloseIntervals(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: RecloseIntervals
        DSS property index: 16
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 16)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @RecloseIntervals.setter
    def RecloseIntervals(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(16, value)

    @property
    def Delay(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Delay
        DSS property index: 17
        """
        return BatchFloat64ArrayProxy(self, 17)

    @Delay.setter
    def Delay(self, value):
        self._set_batch_float64_array(17, value)

    @property
    def Action(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Action
        DSS property index: 18
        """
        return BatchInt32ArrayProxy(self, 18)

    @Action.setter
    def Action(self, value: Union[AnyStr, int, Recloser.RecloserAction, List[AnyStr], List[Union[int, Recloser.RecloserAction]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(18, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(18, value)

    @property
    def Action_str(self) -> str:
        """
        DSS property name: Action
        DSS property index: 18
        """
        return self._get_prop_string(18)

    @Action_str.setter
    def Action_str(self, value: AnyStr):
        self.Action = value

    @property
    def TDPhFast(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: TDPhFast
        DSS property index: 19
        """
        return BatchFloat64ArrayProxy(self, 19)

    @TDPhFast.setter
    def TDPhFast(self, value):
        self._set_batch_float64_array(19, value)

    @property
    def TDGrFast(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: TDGrFast
        DSS property index: 20
        """
        return BatchFloat64ArrayProxy(self, 20)

    @TDGrFast.setter
    def TDGrFast(self, value):
        self._set_batch_float64_array(20, value)

    @property
    def TDPhDelayed(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: TDPhDelayed
        DSS property index: 21
        """
        return BatchFloat64ArrayProxy(self, 21)

    @TDPhDelayed.setter
    def TDPhDelayed(self, value):
        self._set_batch_float64_array(21, value)

    @property
    def TDGrDelayed(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: TDGrDelayed
        DSS property index: 22
        """
        return BatchFloat64ArrayProxy(self, 22)

    @TDGrDelayed.setter
    def TDGrDelayed(self, value):
        self._set_batch_float64_array(22, value)

    @property
    def Normal(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Normal
        DSS property index: 23
        """
        return BatchInt32ArrayProxy(self, 23)

    @Normal.setter
    def Normal(self, value: Union[AnyStr, int, Recloser.RecloserState, List[AnyStr], List[Union[int, Recloser.RecloserState]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(23, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(23, value)

    @property
    def Normal_str(self) -> str:
        """
        DSS property name: Normal
        DSS property index: 23
        """
        return self._get_prop_string(23)

    @Normal_str.setter
    def Normal_str(self, value: AnyStr):
        self.Normal = value

    @property
    def State(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: State
        DSS property index: 24
        """
        return BatchInt32ArrayProxy(self, 24)

    @State.setter
    def State(self, value: Union[AnyStr, int, Recloser.RecloserState, List[AnyStr], List[Union[int, Recloser.RecloserState]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(24, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(24, value)

    @property
    def State_str(self) -> str:
        """
        DSS property name: State
        DSS property index: 24
        """
        return self._get_prop_string(24)

    @State_str.setter
    def State_str(self, value: AnyStr):
        self.State = value

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 25
        """
        return BatchFloat64ArrayProxy(self, 25)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(25, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 26
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 26)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 26, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 27
        """
        self._set_batch_string(27, value)

class FuseBatch(DSSBatch):
    _cls_name = 'Fuse'
    _obj_cls = Fuse
    _cls_idx = 32


    @property
    def MonitoredObj(self) -> List[str]:
        """
        DSS property name: MonitoredObj
        DSS property index: 1
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @MonitoredObj.setter
    def MonitoredObj(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(1, value)
            return

        self._set_batch_string(1, value)

    @property
    def MonitoredObj_obj(self) -> List[str]:
        """
        DSS property name: MonitoredObj
        DSS property index: 1
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @MonitoredObj_obj.setter
    def MonitoredObj_obj(self, value: DSSObj):
        self._set_batch_string(1, value)

    @property
    def MonitoredTerm(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: MonitoredTerm
        DSS property index: 2
        """
        return BatchInt32ArrayProxy(self, 2)

    @MonitoredTerm.setter
    def MonitoredTerm(self, value):
        self._set_batch_int32_array(2, value)

    @property
    def SwitchedObj(self) -> List[str]:
        """
        DSS property name: SwitchedObj
        DSS property index: 3
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 3)

    @SwitchedObj.setter
    def SwitchedObj(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(3, value)
            return

        self._set_batch_string(3, value)

    @property
    def SwitchedObj_obj(self) -> List[str]:
        """
        DSS property name: SwitchedObj
        DSS property index: 3
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 3)

    @SwitchedObj_obj.setter
    def SwitchedObj_obj(self, value: DSSObj):
        self._set_batch_string(3, value)

    @property
    def SwitchedTerm(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: SwitchedTerm
        DSS property index: 4
        """
        return BatchInt32ArrayProxy(self, 4)

    @SwitchedTerm.setter
    def SwitchedTerm(self, value):
        self._set_batch_int32_array(4, value)

    @property
    def FuseCurve(self) -> List[str]:
        """
        DSS property name: FuseCurve
        DSS property index: 5
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 5)

    @FuseCurve.setter
    def FuseCurve(self, value: Union[AnyStr, TCC_Curve]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(5, value)
            return

        self._set_batch_string(5, value)

    @property
    def FuseCurve_obj(self) -> List[str]:
        """
        DSS property name: FuseCurve
        DSS property index: 5
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 5)

    @FuseCurve_obj.setter
    def FuseCurve_obj(self, value: TCC_Curve):
        self._set_batch_string(5, value)

    @property
    def RatedCurrent(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: RatedCurrent
        DSS property index: 6
        """
        return BatchFloat64ArrayProxy(self, 6)

    @RatedCurrent.setter
    def RatedCurrent(self, value):
        self._set_batch_float64_array(6, value)

    @property
    def Delay(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Delay
        DSS property index: 7
        """
        return BatchFloat64ArrayProxy(self, 7)

    @Delay.setter
    def Delay(self, value):
        self._set_batch_float64_array(7, value)

    def Action(self, value: Union[str, bytes, int]):
        """
        DSS property name: Action
        DSS property index: 8
        """
        if isinstance(value, int):
            self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 8, value)
        else:
            self._set_batch_string(8, value)

    @property
    def Normal(self) -> List[npt.NDArray[np.int32]]:
        """
        DSS property name: Normal
        DSS property index: 9
        """
        return [
            self._get_int32_array(self._lib.Obj_GetInt32Array, x, 9)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Normal.setter
    def Normal(self, value: Union[List[Union[int,Fuse.FuseState]], List[AnyStr]]): #TODO: list of lists
        if len(value) and not isinstance(value[0], int):
            value, value_ptr, value_count = self._prepare_string_array(value)
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetStringArray(x, 9, value_ptr, value_count)

            self._check_for_error()
            return

        self._set_batch_int32_array(9, value)

    @property
    def Normal_str(self) -> List[List[str]]:
        """
        DSS property name: Normal
        DSS property index: 9
        """
        return self._get_string_ll(9)

    @Normal_str.setter
    def Normal_str(self, value: AnyStr):
        self.Normal = value

    @property
    def State(self) -> List[npt.NDArray[np.int32]]:
        """
        DSS property name: State
        DSS property index: 10
        """
        return [
            self._get_int32_array(self._lib.Obj_GetInt32Array, x, 10)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @State.setter
    def State(self, value: Union[List[Union[int,Fuse.FuseState]], List[AnyStr]]): #TODO: list of lists
        if len(value) and not isinstance(value[0], int):
            value, value_ptr, value_count = self._prepare_string_array(value)
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetStringArray(x, 10, value_ptr, value_count)

            self._check_for_error()
            return

        self._set_batch_int32_array(10, value)

    @property
    def State_str(self) -> List[List[str]]:
        """
        DSS property name: State
        DSS property index: 10
        """
        return self._get_string_ll(10)

    @State_str.setter
    def State_str(self, value: AnyStr):
        self.State = value

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 11
        """
        return BatchFloat64ArrayProxy(self, 11)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(11, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 12
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 12)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 12, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 13
        """
        self._set_batch_string(13, value)

class SwtControlBatch(DSSBatch):
    _cls_name = 'SwtControl'
    _obj_cls = SwtControl
    _cls_idx = 33


    @property
    def SwitchedObj(self) -> List[str]:
        """
        DSS property name: SwitchedObj
        DSS property index: 1
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @SwitchedObj.setter
    def SwitchedObj(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(1, value)
            return

        self._set_batch_string(1, value)

    @property
    def SwitchedObj_obj(self) -> List[str]:
        """
        DSS property name: SwitchedObj
        DSS property index: 1
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @SwitchedObj_obj.setter
    def SwitchedObj_obj(self, value: DSSObj):
        self._set_batch_string(1, value)

    @property
    def SwitchedTerm(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: SwitchedTerm
        DSS property index: 2
        """
        return BatchInt32ArrayProxy(self, 2)

    @SwitchedTerm.setter
    def SwitchedTerm(self, value):
        self._set_batch_int32_array(2, value)

    @property
    def Action(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Action
        DSS property index: 3
        """
        return BatchInt32ArrayProxy(self, 3)

    @Action.setter
    def Action(self, value: Union[AnyStr, int, SwtControl.SwtControlAction, List[AnyStr], List[Union[int, SwtControl.SwtControlAction]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(3, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(3, value)

    @property
    def Action_str(self) -> str:
        """
        DSS property name: Action
        DSS property index: 3
        """
        return self._get_prop_string(3)

    @Action_str.setter
    def Action_str(self, value: AnyStr):
        self.Action = value

    @property
    def Lock(self) -> List[bool]:
        """
        DSS property name: Lock
        DSS property index: 4
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 4)
        ]
    @Lock.setter
    def Lock(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 4, value)

    @property
    def Delay(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Delay
        DSS property index: 5
        """
        return BatchFloat64ArrayProxy(self, 5)

    @Delay.setter
    def Delay(self, value):
        self._set_batch_float64_array(5, value)

    @property
    def Normal(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Normal
        DSS property index: 6
        """
        return BatchInt32ArrayProxy(self, 6)

    @Normal.setter
    def Normal(self, value: Union[AnyStr, int, SwtControl.SwtControlState, List[AnyStr], List[Union[int, SwtControl.SwtControlState]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(6, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(6, value)

    @property
    def Normal_str(self) -> str:
        """
        DSS property name: Normal
        DSS property index: 6
        """
        return self._get_prop_string(6)

    @Normal_str.setter
    def Normal_str(self, value: AnyStr):
        self.Normal = value

    @property
    def State(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: State
        DSS property index: 7
        """
        return BatchInt32ArrayProxy(self, 7)

    @State.setter
    def State(self, value: Union[AnyStr, int, SwtControl.SwtControlState, List[AnyStr], List[Union[int, SwtControl.SwtControlState]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(7, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(7, value)

    @property
    def State_str(self) -> str:
        """
        DSS property name: State
        DSS property index: 7
        """
        return self._get_prop_string(7)

    @State_str.setter
    def State_str(self, value: AnyStr):
        self.State = value

    def Reset(self, value: bool):
        """
        DSS property name: Reset
        DSS property index: 8
        """
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 8, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 9
        """
        return BatchFloat64ArrayProxy(self, 9)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(9, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 10
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 10)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 10, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 11
        """
        self._set_batch_string(11, value)

class PVSystemBatch(DSSBatch):
    _cls_name = 'PVSystem'
    _obj_cls = PVSystem
    _cls_idx = 34


    @property
    def phases(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: phases
        DSS property index: 1
        """
        return BatchInt32ArrayProxy(self, 1)

    @phases.setter
    def phases(self, value):
        self._set_batch_int32_array(1, value)

    @property
    def bus1(self) -> List[str]:
        """
        DSS property name: bus1
        DSS property index: 2
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 2) 

    @bus1.setter
    def bus1(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 2, value)

    @property
    def kv(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kv
        DSS property index: 3
        """
        return BatchFloat64ArrayProxy(self, 3)

    @kv.setter
    def kv(self, value):
        self._set_batch_float64_array(3, value)

    @property
    def irradiance(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: irradiance
        DSS property index: 4
        """
        return BatchFloat64ArrayProxy(self, 4)

    @irradiance.setter
    def irradiance(self, value):
        self._set_batch_float64_array(4, value)

    @property
    def Pmpp(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Pmpp
        DSS property index: 5
        """
        return BatchFloat64ArrayProxy(self, 5)

    @Pmpp.setter
    def Pmpp(self, value):
        self._set_batch_float64_array(5, value)

    @property
    def pctPmpp(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %Pmpp
        DSS property index: 6
        """
        return BatchFloat64ArrayProxy(self, 6)

    @pctPmpp.setter
    def pctPmpp(self, value):
        self._set_batch_float64_array(6, value)

    @property
    def Temperature(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Temperature
        DSS property index: 7
        """
        return BatchFloat64ArrayProxy(self, 7)

    @Temperature.setter
    def Temperature(self, value):
        self._set_batch_float64_array(7, value)

    @property
    def pf(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: pf
        DSS property index: 8
        """
        return BatchFloat64ArrayProxy(self, 8)

    @pf.setter
    def pf(self, value):
        self._set_batch_float64_array(8, value)

    @property
    def conn(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: conn
        DSS property index: 9
        """
        return BatchInt32ArrayProxy(self, 9)

    @conn.setter
    def conn(self, value: Union[AnyStr, int, Connection, List[AnyStr], List[Union[int, Connection]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(9, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(9, value)

    @property
    def conn_str(self) -> str:
        """
        DSS property name: conn
        DSS property index: 9
        """
        return self._get_prop_string(9)

    @conn_str.setter
    def conn_str(self, value: AnyStr):
        self.conn = value

    @property
    def kvar(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kvar
        DSS property index: 10
        """
        return BatchFloat64ArrayProxy(self, 10)

    @kvar.setter
    def kvar(self, value):
        self._set_batch_float64_array(10, value)

    @property
    def kVA(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kVA
        DSS property index: 11
        """
        return BatchFloat64ArrayProxy(self, 11)

    @kVA.setter
    def kVA(self, value):
        self._set_batch_float64_array(11, value)

    @property
    def pctCutin(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %Cutin
        DSS property index: 12
        """
        return BatchFloat64ArrayProxy(self, 12)

    @pctCutin.setter
    def pctCutin(self, value):
        self._set_batch_float64_array(12, value)

    @property
    def pctCutout(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %Cutout
        DSS property index: 13
        """
        return BatchFloat64ArrayProxy(self, 13)

    @pctCutout.setter
    def pctCutout(self, value):
        self._set_batch_float64_array(13, value)

    @property
    def EffCurve(self) -> List[str]:
        """
        DSS property name: EffCurve
        DSS property index: 14
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 14)

    @EffCurve.setter
    def EffCurve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(14, value)
            return

        self._set_batch_string(14, value)

    @property
    def EffCurve_obj(self) -> List[str]:
        """
        DSS property name: EffCurve
        DSS property index: 14
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 14)

    @EffCurve_obj.setter
    def EffCurve_obj(self, value: XYcurve):
        self._set_batch_string(14, value)

    @property
    def PTCurve(self) -> List[str]:
        """
        DSS property name: P-TCurve
        DSS property index: 15
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 15)

    @PTCurve.setter
    def PTCurve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(15, value)
            return

        self._set_batch_string(15, value)

    @property
    def PTCurve_obj(self) -> List[str]:
        """
        DSS property name: P-TCurve
        DSS property index: 15
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 15)

    @PTCurve_obj.setter
    def PTCurve_obj(self, value: XYcurve):
        self._set_batch_string(15, value)

    @property
    def pctR(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %R
        DSS property index: 16
        """
        return BatchFloat64ArrayProxy(self, 16)

    @pctR.setter
    def pctR(self, value):
        self._set_batch_float64_array(16, value)

    @property
    def pctX(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %X
        DSS property index: 17
        """
        return BatchFloat64ArrayProxy(self, 17)

    @pctX.setter
    def pctX(self, value):
        self._set_batch_float64_array(17, value)

    @property
    def model(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: model
        DSS property index: 18
        """
        return BatchInt32ArrayProxy(self, 18)

    @model.setter
    def model(self, value):
        self._set_batch_int32_array(18, value)

    @property
    def Vminpu(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Vminpu
        DSS property index: 19
        """
        return BatchFloat64ArrayProxy(self, 19)

    @Vminpu.setter
    def Vminpu(self, value):
        self._set_batch_float64_array(19, value)

    @property
    def Vmaxpu(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Vmaxpu
        DSS property index: 20
        """
        return BatchFloat64ArrayProxy(self, 20)

    @Vmaxpu.setter
    def Vmaxpu(self, value):
        self._set_batch_float64_array(20, value)

    @property
    def Balanced(self) -> List[bool]:
        """
        DSS property name: Balanced
        DSS property index: 21
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 21)
        ]
    @Balanced.setter
    def Balanced(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 21, value)

    @property
    def LimitCurrent(self) -> List[bool]:
        """
        DSS property name: LimitCurrent
        DSS property index: 22
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 22)
        ]
    @LimitCurrent.setter
    def LimitCurrent(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 22, value)

    @property
    def yearly(self) -> List[str]:
        """
        DSS property name: yearly
        DSS property index: 23
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 23)

    @yearly.setter
    def yearly(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(23, value)
            return

        self._set_batch_string(23, value)

    @property
    def yearly_obj(self) -> List[str]:
        """
        DSS property name: yearly
        DSS property index: 23
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 23)

    @yearly_obj.setter
    def yearly_obj(self, value: LoadShape):
        self._set_batch_string(23, value)

    @property
    def daily(self) -> List[str]:
        """
        DSS property name: daily
        DSS property index: 24
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 24)

    @daily.setter
    def daily(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(24, value)
            return

        self._set_batch_string(24, value)

    @property
    def daily_obj(self) -> List[str]:
        """
        DSS property name: daily
        DSS property index: 24
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 24)

    @daily_obj.setter
    def daily_obj(self, value: LoadShape):
        self._set_batch_string(24, value)

    @property
    def duty(self) -> List[str]:
        """
        DSS property name: duty
        DSS property index: 25
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 25)

    @duty.setter
    def duty(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(25, value)
            return

        self._set_batch_string(25, value)

    @property
    def duty_obj(self) -> List[str]:
        """
        DSS property name: duty
        DSS property index: 25
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 25)

    @duty_obj.setter
    def duty_obj(self, value: LoadShape):
        self._set_batch_string(25, value)

    @property
    def Tyearly(self) -> List[str]:
        """
        DSS property name: Tyearly
        DSS property index: 26
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 26)

    @Tyearly.setter
    def Tyearly(self, value: Union[AnyStr, TShape]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(26, value)
            return

        self._set_batch_string(26, value)

    @property
    def Tyearly_obj(self) -> List[str]:
        """
        DSS property name: Tyearly
        DSS property index: 26
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 26)

    @Tyearly_obj.setter
    def Tyearly_obj(self, value: TShape):
        self._set_batch_string(26, value)

    @property
    def Tdaily(self) -> List[str]:
        """
        DSS property name: Tdaily
        DSS property index: 27
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 27)

    @Tdaily.setter
    def Tdaily(self, value: Union[AnyStr, TShape]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(27, value)
            return

        self._set_batch_string(27, value)

    @property
    def Tdaily_obj(self) -> List[str]:
        """
        DSS property name: Tdaily
        DSS property index: 27
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 27)

    @Tdaily_obj.setter
    def Tdaily_obj(self, value: TShape):
        self._set_batch_string(27, value)

    @property
    def Tduty(self) -> List[str]:
        """
        DSS property name: Tduty
        DSS property index: 28
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 28)

    @Tduty.setter
    def Tduty(self, value: Union[AnyStr, TShape]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(28, value)
            return

        self._set_batch_string(28, value)

    @property
    def Tduty_obj(self) -> List[str]:
        """
        DSS property name: Tduty
        DSS property index: 28
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 28)

    @Tduty_obj.setter
    def Tduty_obj(self, value: TShape):
        self._set_batch_string(28, value)

    @property
    def cls(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: class
        DSS property index: 29
        """
        return BatchInt32ArrayProxy(self, 29)

    @cls.setter
    def cls(self, value):
        self._set_batch_int32_array(29, value)

    @property
    def UserModel(self) -> List[str]:
        """
        DSS property name: UserModel
        DSS property index: 30
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 30) 

    @UserModel.setter
    def UserModel(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 30, value)

    @property
    def UserData(self) -> List[str]:
        """
        DSS property name: UserData
        DSS property index: 31
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 31) 

    @UserData.setter
    def UserData(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 31, value)

    @property
    def debugtrace(self) -> List[bool]:
        """
        DSS property name: debugtrace
        DSS property index: 32
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 32)
        ]
    @debugtrace.setter
    def debugtrace(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 32, value)

    @property
    def VarFollowInverter(self) -> List[bool]:
        """
        DSS property name: VarFollowInverter
        DSS property index: 33
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 33)
        ]
    @VarFollowInverter.setter
    def VarFollowInverter(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 33, value)

    @property
    def DutyStart(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: DutyStart
        DSS property index: 34
        """
        return BatchFloat64ArrayProxy(self, 34)

    @DutyStart.setter
    def DutyStart(self, value):
        self._set_batch_float64_array(34, value)

    @property
    def WattPriority(self) -> List[bool]:
        """
        DSS property name: WattPriority
        DSS property index: 35
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 35)
        ]
    @WattPriority.setter
    def WattPriority(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 35, value)

    @property
    def PFPriority(self) -> List[bool]:
        """
        DSS property name: PFPriority
        DSS property index: 36
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 36)
        ]
    @PFPriority.setter
    def PFPriority(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 36, value)

    @property
    def pctPminNoVars(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %PminNoVars
        DSS property index: 37
        """
        return BatchFloat64ArrayProxy(self, 37)

    @pctPminNoVars.setter
    def pctPminNoVars(self, value):
        self._set_batch_float64_array(37, value)

    @property
    def pctPminkvarMax(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %PminkvarMax
        DSS property index: 38
        """
        return BatchFloat64ArrayProxy(self, 38)

    @pctPminkvarMax.setter
    def pctPminkvarMax(self, value):
        self._set_batch_float64_array(38, value)

    @property
    def kvarMax(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kvarMax
        DSS property index: 39
        """
        return BatchFloat64ArrayProxy(self, 39)

    @kvarMax.setter
    def kvarMax(self, value):
        self._set_batch_float64_array(39, value)

    @property
    def kvarMaxAbs(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kvarMaxAbs
        DSS property index: 40
        """
        return BatchFloat64ArrayProxy(self, 40)

    @kvarMaxAbs.setter
    def kvarMaxAbs(self, value):
        self._set_batch_float64_array(40, value)

    @property
    def spectrum(self) -> List[str]:
        """
        DSS property name: spectrum
        DSS property index: 41
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 41)

    @spectrum.setter
    def spectrum(self, value: Union[AnyStr, Spectrum]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(41, value)
            return

        self._set_batch_string(41, value)

    @property
    def spectrum_obj(self) -> List[str]:
        """
        DSS property name: spectrum
        DSS property index: 41
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 41)

    @spectrum_obj.setter
    def spectrum_obj(self, value: Spectrum):
        self._set_batch_string(41, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 42
        """
        return BatchFloat64ArrayProxy(self, 42)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(42, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 43
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 43)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 43, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 44
        """
        self._set_batch_string(44, value)

class UPFCBatch(DSSBatch):
    _cls_name = 'UPFC'
    _obj_cls = UPFC
    _cls_idx = 35


    @property
    def bus1(self) -> List[str]:
        """
        DSS property name: bus1
        DSS property index: 1
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1) 

    @bus1.setter
    def bus1(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 1, value)

    @property
    def bus2(self) -> List[str]:
        """
        DSS property name: bus2
        DSS property index: 2
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 2) 

    @bus2.setter
    def bus2(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 2, value)

    @property
    def refkv(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: refkv
        DSS property index: 3
        """
        return BatchFloat64ArrayProxy(self, 3)

    @refkv.setter
    def refkv(self, value):
        self._set_batch_float64_array(3, value)

    @property
    def pf(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: pf
        DSS property index: 4
        """
        return BatchFloat64ArrayProxy(self, 4)

    @pf.setter
    def pf(self, value):
        self._set_batch_float64_array(4, value)

    @property
    def frequency(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: frequency
        DSS property index: 5
        """
        return BatchFloat64ArrayProxy(self, 5)

    @frequency.setter
    def frequency(self, value):
        self._set_batch_float64_array(5, value)

    @property
    def phases(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: phases
        DSS property index: 6
        """
        return BatchInt32ArrayProxy(self, 6)

    @phases.setter
    def phases(self, value):
        self._set_batch_int32_array(6, value)

    @property
    def Xs(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Xs
        DSS property index: 7
        """
        return BatchFloat64ArrayProxy(self, 7)

    @Xs.setter
    def Xs(self, value):
        self._set_batch_float64_array(7, value)

    @property
    def Tol1(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Tol1
        DSS property index: 8
        """
        return BatchFloat64ArrayProxy(self, 8)

    @Tol1.setter
    def Tol1(self, value):
        self._set_batch_float64_array(8, value)

    @property
    def Mode(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Mode
        DSS property index: 9
        """
        return BatchInt32ArrayProxy(self, 9)

    @Mode.setter
    def Mode(self, value):
        self._set_batch_int32_array(9, value)

    @property
    def VpqMax(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: VpqMax
        DSS property index: 10
        """
        return BatchFloat64ArrayProxy(self, 10)

    @VpqMax.setter
    def VpqMax(self, value):
        self._set_batch_float64_array(10, value)

    @property
    def LossCurve(self) -> List[str]:
        """
        DSS property name: LossCurve
        DSS property index: 11
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 11)

    @LossCurve.setter
    def LossCurve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(11, value)
            return

        self._set_batch_string(11, value)

    @property
    def LossCurve_obj(self) -> List[str]:
        """
        DSS property name: LossCurve
        DSS property index: 11
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 11)

    @LossCurve_obj.setter
    def LossCurve_obj(self, value: XYcurve):
        self._set_batch_string(11, value)

    @property
    def VHLimit(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: VHLimit
        DSS property index: 12
        """
        return BatchFloat64ArrayProxy(self, 12)

    @VHLimit.setter
    def VHLimit(self, value):
        self._set_batch_float64_array(12, value)

    @property
    def VLLimit(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: VLLimit
        DSS property index: 13
        """
        return BatchFloat64ArrayProxy(self, 13)

    @VLLimit.setter
    def VLLimit(self, value):
        self._set_batch_float64_array(13, value)

    @property
    def CLimit(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: CLimit
        DSS property index: 14
        """
        return BatchFloat64ArrayProxy(self, 14)

    @CLimit.setter
    def CLimit(self, value):
        self._set_batch_float64_array(14, value)

    @property
    def refkv2(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: refkv2
        DSS property index: 15
        """
        return BatchFloat64ArrayProxy(self, 15)

    @refkv2.setter
    def refkv2(self, value):
        self._set_batch_float64_array(15, value)

    @property
    def kvarLimit(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kvarLimit
        DSS property index: 16
        """
        return BatchFloat64ArrayProxy(self, 16)

    @kvarLimit.setter
    def kvarLimit(self, value):
        self._set_batch_float64_array(16, value)

    @property
    def spectrum(self) -> List[str]:
        """
        DSS property name: spectrum
        DSS property index: 17
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 17)

    @spectrum.setter
    def spectrum(self, value: Union[AnyStr, Spectrum]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(17, value)
            return

        self._set_batch_string(17, value)

    @property
    def spectrum_obj(self) -> List[str]:
        """
        DSS property name: spectrum
        DSS property index: 17
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 17)

    @spectrum_obj.setter
    def spectrum_obj(self, value: Spectrum):
        self._set_batch_string(17, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 18
        """
        return BatchFloat64ArrayProxy(self, 18)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(18, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 19
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 19)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 19, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 20
        """
        self._set_batch_string(20, value)

class UPFCControlBatch(DSSBatch):
    _cls_name = 'UPFCControl'
    _obj_cls = UPFCControl
    _cls_idx = 36


    @property
    def UPFCList(self) -> List[List[str]]:
        """
        DSS property name: UPFCList
        DSS property index: 1
        """
        return self._get_string_ll(1)

    @UPFCList.setter
    def UPFCList(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._ffi.unpack(self.pointer[0], self.count[0]):
            self._lib.Obj_SetStringArray(x, 1, value_ptr, value_count)

        self._check_for_error()

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 2
        """
        return BatchFloat64ArrayProxy(self, 2)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(2, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 3
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 3)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 3, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 4
        """
        self._set_batch_string(4, value)

class ESPVLControlBatch(DSSBatch):
    _cls_name = 'ESPVLControl'
    _obj_cls = ESPVLControl
    _cls_idx = 37


    @property
    def Element(self) -> List[str]:
        """
        DSS property name: Element
        DSS property index: 1
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @Element.setter
    def Element(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(1, value)
            return

        self._set_batch_string(1, value)

    @property
    def Element_obj(self) -> List[str]:
        """
        DSS property name: Element
        DSS property index: 1
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @Element_obj.setter
    def Element_obj(self, value: DSSObj):
        self._set_batch_string(1, value)

    @property
    def Terminal(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Terminal
        DSS property index: 2
        """
        return BatchInt32ArrayProxy(self, 2)

    @Terminal.setter
    def Terminal(self, value):
        self._set_batch_int32_array(2, value)

    @property
    def Type(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Type
        DSS property index: 3
        """
        return BatchInt32ArrayProxy(self, 3)

    @Type.setter
    def Type(self, value: Union[AnyStr, int, ESPVLControl.ESPVLControlType, List[AnyStr], List[Union[int, ESPVLControl.ESPVLControlType]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(3, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(3, value)

    @property
    def Type_str(self) -> str:
        """
        DSS property name: Type
        DSS property index: 3
        """
        return self._get_prop_string(3)

    @Type_str.setter
    def Type_str(self, value: AnyStr):
        self.Type = value

    @property
    def kWBand(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kWBand
        DSS property index: 4
        """
        return BatchFloat64ArrayProxy(self, 4)

    @kWBand.setter
    def kWBand(self, value):
        self._set_batch_float64_array(4, value)

    @property
    def kvarlimit(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kvarlimit
        DSS property index: 5
        """
        return BatchFloat64ArrayProxy(self, 5)

    @kvarlimit.setter
    def kvarlimit(self, value):
        self._set_batch_float64_array(5, value)

    @property
    def LocalControlList(self) -> List[List[str]]:
        """
        DSS property name: LocalControlList
        DSS property index: 6
        """
        return self._get_string_ll(6)

    @LocalControlList.setter
    def LocalControlList(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._ffi.unpack(self.pointer[0], self.count[0]):
            self._lib.Obj_SetStringArray(x, 6, value_ptr, value_count)

        self._check_for_error()

    @property
    def LocalControlWeights(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: LocalControlWeights
        DSS property index: 7
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 7)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @LocalControlWeights.setter
    def LocalControlWeights(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(7, value)

    @property
    def PVSystemList(self) -> List[List[str]]:
        """
        DSS property name: PVSystemList
        DSS property index: 8
        """
        return self._get_string_ll(8)

    @PVSystemList.setter
    def PVSystemList(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._ffi.unpack(self.pointer[0], self.count[0]):
            self._lib.Obj_SetStringArray(x, 8, value_ptr, value_count)

        self._check_for_error()

    @property
    def PVSystemWeights(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: PVSystemWeights
        DSS property index: 9
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 9)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @PVSystemWeights.setter
    def PVSystemWeights(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(9, value)

    @property
    def StorageList(self) -> List[List[str]]:
        """
        DSS property name: StorageList
        DSS property index: 10
        """
        return self._get_string_ll(10)

    @StorageList.setter
    def StorageList(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._ffi.unpack(self.pointer[0], self.count[0]):
            self._lib.Obj_SetStringArray(x, 10, value_ptr, value_count)

        self._check_for_error()

    @property
    def StorageWeights(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: StorageWeights
        DSS property index: 11
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 11)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @StorageWeights.setter
    def StorageWeights(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(11, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 12
        """
        return BatchFloat64ArrayProxy(self, 12)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(12, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 13
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 13)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 13, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 14
        """
        self._set_batch_string(14, value)

class IndMach012Batch(DSSBatch):
    _cls_name = 'IndMach012'
    _obj_cls = IndMach012
    _cls_idx = 38


    @property
    def phases(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: phases
        DSS property index: 1
        """
        return BatchInt32ArrayProxy(self, 1)

    @phases.setter
    def phases(self, value):
        self._set_batch_int32_array(1, value)

    @property
    def bus1(self) -> List[str]:
        """
        DSS property name: bus1
        DSS property index: 2
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 2) 

    @bus1.setter
    def bus1(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 2, value)

    @property
    def kv(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kv
        DSS property index: 3
        """
        return BatchFloat64ArrayProxy(self, 3)

    @kv.setter
    def kv(self, value):
        self._set_batch_float64_array(3, value)

    @property
    def kW(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kW
        DSS property index: 4
        """
        return BatchFloat64ArrayProxy(self, 4)

    @kW.setter
    def kW(self, value):
        self._set_batch_float64_array(4, value)

    @property
    def pf(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: pf
        DSS property index: 5
        """
        return BatchFloat64ArrayProxy(self, 5)

    @pf.setter
    def pf(self, value):
        self._set_batch_float64_array(5, value)

    @property
    def conn(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: conn
        DSS property index: 6
        """
        return BatchInt32ArrayProxy(self, 6)

    @conn.setter
    def conn(self, value: Union[AnyStr, int, Connection, List[AnyStr], List[Union[int, Connection]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(6, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(6, value)

    @property
    def conn_str(self) -> str:
        """
        DSS property name: conn
        DSS property index: 6
        """
        return self._get_prop_string(6)

    @conn_str.setter
    def conn_str(self, value: AnyStr):
        self.conn = value

    @property
    def kVA(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kVA
        DSS property index: 7
        """
        return BatchFloat64ArrayProxy(self, 7)

    @kVA.setter
    def kVA(self, value):
        self._set_batch_float64_array(7, value)

    @property
    def H(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: H
        DSS property index: 8
        """
        return BatchFloat64ArrayProxy(self, 8)

    @H.setter
    def H(self, value):
        self._set_batch_float64_array(8, value)

    @property
    def D(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: D
        DSS property index: 9
        """
        return BatchFloat64ArrayProxy(self, 9)

    @D.setter
    def D(self, value):
        self._set_batch_float64_array(9, value)

    @property
    def puRs(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: puRs
        DSS property index: 10
        """
        return BatchFloat64ArrayProxy(self, 10)

    @puRs.setter
    def puRs(self, value):
        self._set_batch_float64_array(10, value)

    @property
    def puXs(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: puXs
        DSS property index: 11
        """
        return BatchFloat64ArrayProxy(self, 11)

    @puXs.setter
    def puXs(self, value):
        self._set_batch_float64_array(11, value)

    @property
    def puRr(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: puRr
        DSS property index: 12
        """
        return BatchFloat64ArrayProxy(self, 12)

    @puRr.setter
    def puRr(self, value):
        self._set_batch_float64_array(12, value)

    @property
    def puXr(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: puXr
        DSS property index: 13
        """
        return BatchFloat64ArrayProxy(self, 13)

    @puXr.setter
    def puXr(self, value):
        self._set_batch_float64_array(13, value)

    @property
    def puXm(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: puXm
        DSS property index: 14
        """
        return BatchFloat64ArrayProxy(self, 14)

    @puXm.setter
    def puXm(self, value):
        self._set_batch_float64_array(14, value)

    @property
    def Slip(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Slip
        DSS property index: 15
        """
        return BatchFloat64ArrayProxy(self, 15)

    @Slip.setter
    def Slip(self, value):
        self._set_batch_float64_array(15, value)

    @property
    def MaxSlip(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: MaxSlip
        DSS property index: 16
        """
        return BatchFloat64ArrayProxy(self, 16)

    @MaxSlip.setter
    def MaxSlip(self, value):
        self._set_batch_float64_array(16, value)

    @property
    def SlipOption(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: SlipOption
        DSS property index: 17
        """
        return BatchInt32ArrayProxy(self, 17)

    @SlipOption.setter
    def SlipOption(self, value: Union[AnyStr, int, IndMach012.IndMach012SlipOption, List[AnyStr], List[Union[int, IndMach012.IndMach012SlipOption]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(17, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(17, value)

    @property
    def SlipOption_str(self) -> str:
        """
        DSS property name: SlipOption
        DSS property index: 17
        """
        return self._get_prop_string(17)

    @SlipOption_str.setter
    def SlipOption_str(self, value: AnyStr):
        self.SlipOption = value

    @property
    def Yearly(self) -> List[str]:
        """
        DSS property name: Yearly
        DSS property index: 18
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 18)

    @Yearly.setter
    def Yearly(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(18, value)
            return

        self._set_batch_string(18, value)

    @property
    def Yearly_obj(self) -> List[str]:
        """
        DSS property name: Yearly
        DSS property index: 18
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 18)

    @Yearly_obj.setter
    def Yearly_obj(self, value: LoadShape):
        self._set_batch_string(18, value)

    @property
    def Daily(self) -> List[str]:
        """
        DSS property name: Daily
        DSS property index: 19
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 19)

    @Daily.setter
    def Daily(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(19, value)
            return

        self._set_batch_string(19, value)

    @property
    def Daily_obj(self) -> List[str]:
        """
        DSS property name: Daily
        DSS property index: 19
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 19)

    @Daily_obj.setter
    def Daily_obj(self, value: LoadShape):
        self._set_batch_string(19, value)

    @property
    def Duty(self) -> List[str]:
        """
        DSS property name: Duty
        DSS property index: 20
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 20)

    @Duty.setter
    def Duty(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(20, value)
            return

        self._set_batch_string(20, value)

    @property
    def Duty_obj(self) -> List[str]:
        """
        DSS property name: Duty
        DSS property index: 20
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 20)

    @Duty_obj.setter
    def Duty_obj(self, value: LoadShape):
        self._set_batch_string(20, value)

    @property
    def Debugtrace(self) -> List[bool]:
        """
        DSS property name: Debugtrace
        DSS property index: 21
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 21)
        ]
    @Debugtrace.setter
    def Debugtrace(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 21, value)

    @property
    def spectrum(self) -> List[str]:
        """
        DSS property name: spectrum
        DSS property index: 22
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 22)

    @spectrum.setter
    def spectrum(self, value: Union[AnyStr, Spectrum]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(22, value)
            return

        self._set_batch_string(22, value)

    @property
    def spectrum_obj(self) -> List[str]:
        """
        DSS property name: spectrum
        DSS property index: 22
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 22)

    @spectrum_obj.setter
    def spectrum_obj(self, value: Spectrum):
        self._set_batch_string(22, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 23
        """
        return BatchFloat64ArrayProxy(self, 23)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(23, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 24
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 24)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 24, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 25
        """
        self._set_batch_string(25, value)

class GICsourceBatch(DSSBatch):
    _cls_name = 'GICsource'
    _obj_cls = GICsource
    _cls_idx = 39


    @property
    def Volts(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Volts
        DSS property index: 1
        """
        return BatchFloat64ArrayProxy(self, 1)

    @Volts.setter
    def Volts(self, value):
        self._set_batch_float64_array(1, value)

    @property
    def angle(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: angle
        DSS property index: 2
        """
        return BatchFloat64ArrayProxy(self, 2)

    @angle.setter
    def angle(self, value):
        self._set_batch_float64_array(2, value)

    @property
    def frequency(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: frequency
        DSS property index: 3
        """
        return BatchFloat64ArrayProxy(self, 3)

    @frequency.setter
    def frequency(self, value):
        self._set_batch_float64_array(3, value)

    @property
    def phases(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: phases
        DSS property index: 4
        """
        return BatchInt32ArrayProxy(self, 4)

    @phases.setter
    def phases(self, value):
        self._set_batch_int32_array(4, value)

    @property
    def EN(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: EN
        DSS property index: 5
        """
        return BatchFloat64ArrayProxy(self, 5)

    @EN.setter
    def EN(self, value):
        self._set_batch_float64_array(5, value)

    @property
    def EE(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: EE
        DSS property index: 6
        """
        return BatchFloat64ArrayProxy(self, 6)

    @EE.setter
    def EE(self, value):
        self._set_batch_float64_array(6, value)

    @property
    def Lat1(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Lat1
        DSS property index: 7
        """
        return BatchFloat64ArrayProxy(self, 7)

    @Lat1.setter
    def Lat1(self, value):
        self._set_batch_float64_array(7, value)

    @property
    def Lon1(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Lon1
        DSS property index: 8
        """
        return BatchFloat64ArrayProxy(self, 8)

    @Lon1.setter
    def Lon1(self, value):
        self._set_batch_float64_array(8, value)

    @property
    def Lat2(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Lat2
        DSS property index: 9
        """
        return BatchFloat64ArrayProxy(self, 9)

    @Lat2.setter
    def Lat2(self, value):
        self._set_batch_float64_array(9, value)

    @property
    def Lon2(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Lon2
        DSS property index: 10
        """
        return BatchFloat64ArrayProxy(self, 10)

    @Lon2.setter
    def Lon2(self, value):
        self._set_batch_float64_array(10, value)

    @property
    def spectrum(self) -> List[str]:
        """
        DSS property name: spectrum
        DSS property index: 11
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 11)

    @spectrum.setter
    def spectrum(self, value: Union[AnyStr, Spectrum]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(11, value)
            return

        self._set_batch_string(11, value)

    @property
    def spectrum_obj(self) -> List[str]:
        """
        DSS property name: spectrum
        DSS property index: 11
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 11)

    @spectrum_obj.setter
    def spectrum_obj(self, value: Spectrum):
        self._set_batch_string(11, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 12
        """
        return BatchFloat64ArrayProxy(self, 12)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(12, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 13
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 13)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 13, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 14
        """
        self._set_batch_string(14, value)

class AutoTransBatch(DSSBatch):
    _cls_name = 'AutoTrans'
    _obj_cls = AutoTrans
    _cls_idx = 40


    @property
    def phases(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: phases
        DSS property index: 1
        """
        return BatchInt32ArrayProxy(self, 1)

    @phases.setter
    def phases(self, value):
        self._set_batch_int32_array(1, value)

    @property
    def windings(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: windings
        DSS property index: 2
        """
        return BatchInt32ArrayProxy(self, 2)

    @windings.setter
    def windings(self, value):
        self._set_batch_int32_array(2, value)

    @property
    def wdg(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: wdg
        DSS property index: 3
        """
        return BatchInt32ArrayProxy(self, 3)

    @wdg.setter
    def wdg(self, value):
        self._set_batch_int32_array(3, value)

    @property
    def bus(self) -> List[List[str]]:
        """
        DSS property name: bus
        DSS property index: 4
        """
        return self._get_string_ll(4)

    @bus.setter
    def bus(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._ffi.unpack(self.pointer[0], self.count[0]):
            self._lib.Obj_SetStringArray(x, 4, value_ptr, value_count)

        self._check_for_error()

    @property
    def conn(self) -> List[npt.NDArray[np.int32]]:
        """
        DSS property name: conn
        DSS property index: 5
        """
        return [
            self._get_int32_array(self._lib.Obj_GetInt32Array, x, 5)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @conn.setter
    def conn(self, value: Union[List[Union[int,AutoTrans.AutoTransConnection]], List[AnyStr]]): #TODO: list of lists
        if len(value) and not isinstance(value[0], int):
            value, value_ptr, value_count = self._prepare_string_array(value)
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetStringArray(x, 5, value_ptr, value_count)

            self._check_for_error()
            return

        self._set_batch_int32_array(5, value)

    @property
    def conn_str(self) -> List[List[str]]:
        """
        DSS property name: conn
        DSS property index: 5
        """
        return self._get_string_ll(5)

    @conn_str.setter
    def conn_str(self, value: AnyStr):
        self.conn = value

    @property
    def kV(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: kV
        DSS property index: 6
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 6)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @kV.setter
    def kV(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(6, value)

    @property
    def kVA(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: kVA
        DSS property index: 7
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 7)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @kVA.setter
    def kVA(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(7, value)

    @property
    def tap(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: tap
        DSS property index: 8
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 8)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @tap.setter
    def tap(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(8, value)

    @property
    def pctR(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: %R
        DSS property index: 9
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 9)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @pctR.setter
    def pctR(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(9, value)

    @property
    def Rdcohms(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: Rdcohms
        DSS property index: 10
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 10)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Rdcohms.setter
    def Rdcohms(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(10, value)

    @property
    def Core(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Core
        DSS property index: 11
        """
        return BatchInt32ArrayProxy(self, 11)

    @Core.setter
    def Core(self, value: Union[AnyStr, int, CoreType, List[AnyStr], List[Union[int, CoreType]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(11, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(11, value)

    @property
    def Core_str(self) -> str:
        """
        DSS property name: Core
        DSS property index: 11
        """
        return self._get_prop_string(11)

    @Core_str.setter
    def Core_str(self, value: AnyStr):
        self.Core = value

    @property
    def buses(self) -> List[List[str]]:
        """
        DSS property name: buses
        DSS property index: 12
        """
        return self._get_string_ll(12)

    @buses.setter
    def buses(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._ffi.unpack(self.pointer[0], self.count[0]):
            self._lib.Obj_SetStringArray(x, 12, value_ptr, value_count)

        self._check_for_error()

    @property
    def conns(self) -> List[npt.NDArray[np.int32]]:
        """
        DSS property name: conns
        DSS property index: 13
        """
        return [
            self._get_int32_array(self._lib.Obj_GetInt32Array, x, 13)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @conns.setter
    def conns(self, value: Union[List[Union[int,AutoTrans.AutoTransConnection]], List[AnyStr]]): #TODO: list of lists
        if len(value) and not isinstance(value[0], int):
            value, value_ptr, value_count = self._prepare_string_array(value)
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetStringArray(x, 13, value_ptr, value_count)

            self._check_for_error()
            return

        self._set_batch_int32_array(13, value)

    @property
    def conns_str(self) -> List[List[str]]:
        """
        DSS property name: conns
        DSS property index: 13
        """
        return self._get_string_ll(13)

    @conns_str.setter
    def conns_str(self, value: AnyStr):
        self.conns = value

    @property
    def kVs(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: kVs
        DSS property index: 14
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 14)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @kVs.setter
    def kVs(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(14, value)

    @property
    def kVAs(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: kVAs
        DSS property index: 15
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 15)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @kVAs.setter
    def kVAs(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(15, value)

    @property
    def taps(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: taps
        DSS property index: 16
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 16)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @taps.setter
    def taps(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(16, value)

    @property
    def XHX(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: XHX
        DSS property index: 17
        """
        return BatchFloat64ArrayProxy(self, 17)

    @XHX.setter
    def XHX(self, value):
        self._set_batch_float64_array(17, value)

    @property
    def XHT(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: XHT
        DSS property index: 18
        """
        return BatchFloat64ArrayProxy(self, 18)

    @XHT.setter
    def XHT(self, value):
        self._set_batch_float64_array(18, value)

    @property
    def XXT(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: XXT
        DSS property index: 19
        """
        return BatchFloat64ArrayProxy(self, 19)

    @XXT.setter
    def XXT(self, value):
        self._set_batch_float64_array(19, value)

    @property
    def XSCarray(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: XSCarray
        DSS property index: 20
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 20)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @XSCarray.setter
    def XSCarray(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(20, value)

    @property
    def thermal(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: thermal
        DSS property index: 21
        """
        return BatchFloat64ArrayProxy(self, 21)

    @thermal.setter
    def thermal(self, value):
        self._set_batch_float64_array(21, value)

    @property
    def n(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: n
        DSS property index: 22
        """
        return BatchFloat64ArrayProxy(self, 22)

    @n.setter
    def n(self, value):
        self._set_batch_float64_array(22, value)

    @property
    def m(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: m
        DSS property index: 23
        """
        return BatchFloat64ArrayProxy(self, 23)

    @m.setter
    def m(self, value):
        self._set_batch_float64_array(23, value)

    @property
    def flrise(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: flrise
        DSS property index: 24
        """
        return BatchFloat64ArrayProxy(self, 24)

    @flrise.setter
    def flrise(self, value):
        self._set_batch_float64_array(24, value)

    @property
    def hsrise(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: hsrise
        DSS property index: 25
        """
        return BatchFloat64ArrayProxy(self, 25)

    @hsrise.setter
    def hsrise(self, value):
        self._set_batch_float64_array(25, value)

    @property
    def pctloadloss(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %loadloss
        DSS property index: 26
        """
        return BatchFloat64ArrayProxy(self, 26)

    @pctloadloss.setter
    def pctloadloss(self, value):
        self._set_batch_float64_array(26, value)

    @property
    def pctnoloadloss(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %noloadloss
        DSS property index: 27
        """
        return BatchFloat64ArrayProxy(self, 27)

    @pctnoloadloss.setter
    def pctnoloadloss(self, value):
        self._set_batch_float64_array(27, value)

    @property
    def normhkVA(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: normhkVA
        DSS property index: 28
        """
        return BatchFloat64ArrayProxy(self, 28)

    @normhkVA.setter
    def normhkVA(self, value):
        self._set_batch_float64_array(28, value)

    @property
    def emerghkVA(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: emerghkVA
        DSS property index: 29
        """
        return BatchFloat64ArrayProxy(self, 29)

    @emerghkVA.setter
    def emerghkVA(self, value):
        self._set_batch_float64_array(29, value)

    @property
    def sub(self) -> List[bool]:
        """
        DSS property name: sub
        DSS property index: 30
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 30)
        ]
    @sub.setter
    def sub(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 30, value)

    @property
    def MaxTap(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: MaxTap
        DSS property index: 31
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 31)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @MaxTap.setter
    def MaxTap(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(31, value)

    @property
    def MinTap(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: MinTap
        DSS property index: 32
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 32)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @MinTap.setter
    def MinTap(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(32, value)

    @property
    def NumTaps(self) -> List[npt.NDArray[np.int32]]:
        """
        DSS property name: NumTaps
        DSS property index: 33
        """
        return [
            self._get_int32_array(self._lib.Obj_GetInt32Array, x, 33)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @NumTaps.setter
    def NumTaps(self, value: npt.NDArray[np.int32]): #TODO: list of arrays, matrix
        self._set_batch_int32_array(33, value)

    @property
    def subname(self) -> List[str]:
        """
        DSS property name: subname
        DSS property index: 34
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 34) 

    @subname.setter
    def subname(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 34, value)

    @property
    def pctimag(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %imag
        DSS property index: 35
        """
        return BatchFloat64ArrayProxy(self, 35)

    @pctimag.setter
    def pctimag(self, value):
        self._set_batch_float64_array(35, value)

    @property
    def ppm_antifloat(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: ppm_antifloat
        DSS property index: 36
        """
        return BatchFloat64ArrayProxy(self, 36)

    @ppm_antifloat.setter
    def ppm_antifloat(self, value):
        self._set_batch_float64_array(36, value)

    @property
    def pctRs(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: %Rs
        DSS property index: 37
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 37)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @pctRs.setter
    def pctRs(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(37, value)

    @property
    def XRConst(self) -> List[bool]:
        """
        DSS property name: XRConst
        DSS property index: 38
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 38)
        ]
    @XRConst.setter
    def XRConst(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 38, value)

    @property
    def LeadLag(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: LeadLag
        DSS property index: 39
        """
        return BatchInt32ArrayProxy(self, 39)

    @LeadLag.setter
    def LeadLag(self, value: Union[AnyStr, int, PhaseSequence, List[AnyStr], List[Union[int, PhaseSequence]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(39, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(39, value)

    @property
    def LeadLag_str(self) -> str:
        """
        DSS property name: LeadLag
        DSS property index: 39
        """
        return self._get_prop_string(39)

    @LeadLag_str.setter
    def LeadLag_str(self, value: AnyStr):
        self.LeadLag = value

    def WdgCurrents(self) -> List[str]:
        """
        DSS property name: WdgCurrents
        DSS property index: 40
        """
        # []
        # StringSilentROFunction
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 40)

    @property
    def normamps(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: normamps
        DSS property index: 41
        """
        return BatchFloat64ArrayProxy(self, 41)

    @normamps.setter
    def normamps(self, value):
        self._set_batch_float64_array(41, value)

    @property
    def emergamps(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: emergamps
        DSS property index: 42
        """
        return BatchFloat64ArrayProxy(self, 42)

    @emergamps.setter
    def emergamps(self, value):
        self._set_batch_float64_array(42, value)

    @property
    def faultrate(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: faultrate
        DSS property index: 43
        """
        return BatchFloat64ArrayProxy(self, 43)

    @faultrate.setter
    def faultrate(self, value):
        self._set_batch_float64_array(43, value)

    @property
    def pctperm(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: pctperm
        DSS property index: 44
        """
        return BatchFloat64ArrayProxy(self, 44)

    @pctperm.setter
    def pctperm(self, value):
        self._set_batch_float64_array(44, value)

    @property
    def repair(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: repair
        DSS property index: 45
        """
        return BatchFloat64ArrayProxy(self, 45)

    @repair.setter
    def repair(self, value):
        self._set_batch_float64_array(45, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 46
        """
        return BatchFloat64ArrayProxy(self, 46)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(46, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 47
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 47)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 47, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 48
        """
        self._set_batch_string(48, value)

class RegControlBatch(DSSBatch):
    _cls_name = 'RegControl'
    _obj_cls = RegControl
    _cls_idx = 21


    @property
    def transformer(self) -> List[str]:
        """
        DSS property name: transformer
        DSS property index: 1
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @transformer.setter
    def transformer(self, value: Union[AnyStr, Transformer, AutoTrans]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(1, value)
            return

        self._set_batch_string(1, value)

    @property
    def transformer_obj(self) -> List[str]:
        """
        DSS property name: transformer
        DSS property index: 1
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @transformer_obj.setter
    def transformer_obj(self, value: Union[Transformer, AutoTrans]):
        self._set_batch_string(1, value)

    @property
    def winding(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: winding
        DSS property index: 2
        """
        return BatchInt32ArrayProxy(self, 2)

    @winding.setter
    def winding(self, value):
        self._set_batch_int32_array(2, value)

    @property
    def vreg(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: vreg
        DSS property index: 3
        """
        return BatchFloat64ArrayProxy(self, 3)

    @vreg.setter
    def vreg(self, value):
        self._set_batch_float64_array(3, value)

    @property
    def band(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: band
        DSS property index: 4
        """
        return BatchFloat64ArrayProxy(self, 4)

    @band.setter
    def band(self, value):
        self._set_batch_float64_array(4, value)

    @property
    def ptratio(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: ptratio
        DSS property index: 5
        """
        return BatchFloat64ArrayProxy(self, 5)

    @ptratio.setter
    def ptratio(self, value):
        self._set_batch_float64_array(5, value)

    @property
    def CTprim(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: CTprim
        DSS property index: 6
        """
        return BatchFloat64ArrayProxy(self, 6)

    @CTprim.setter
    def CTprim(self, value):
        self._set_batch_float64_array(6, value)

    @property
    def R(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: R
        DSS property index: 7
        """
        return BatchFloat64ArrayProxy(self, 7)

    @R.setter
    def R(self, value):
        self._set_batch_float64_array(7, value)

    @property
    def X(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: X
        DSS property index: 8
        """
        return BatchFloat64ArrayProxy(self, 8)

    @X.setter
    def X(self, value):
        self._set_batch_float64_array(8, value)

    @property
    def bus(self) -> List[str]:
        """
        DSS property name: bus
        DSS property index: 9
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 9) 

    @bus.setter
    def bus(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 9, value)

    @property
    def delay(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: delay
        DSS property index: 10
        """
        return BatchFloat64ArrayProxy(self, 10)

    @delay.setter
    def delay(self, value):
        self._set_batch_float64_array(10, value)

    @property
    def reversible(self) -> List[bool]:
        """
        DSS property name: reversible
        DSS property index: 11
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 11)
        ]
    @reversible.setter
    def reversible(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 11, value)

    @property
    def revvreg(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: revvreg
        DSS property index: 12
        """
        return BatchFloat64ArrayProxy(self, 12)

    @revvreg.setter
    def revvreg(self, value):
        self._set_batch_float64_array(12, value)

    @property
    def revband(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: revband
        DSS property index: 13
        """
        return BatchFloat64ArrayProxy(self, 13)

    @revband.setter
    def revband(self, value):
        self._set_batch_float64_array(13, value)

    @property
    def revR(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: revR
        DSS property index: 14
        """
        return BatchFloat64ArrayProxy(self, 14)

    @revR.setter
    def revR(self, value):
        self._set_batch_float64_array(14, value)

    @property
    def revX(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: revX
        DSS property index: 15
        """
        return BatchFloat64ArrayProxy(self, 15)

    @revX.setter
    def revX(self, value):
        self._set_batch_float64_array(15, value)

    @property
    def tapdelay(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: tapdelay
        DSS property index: 16
        """
        return BatchFloat64ArrayProxy(self, 16)

    @tapdelay.setter
    def tapdelay(self, value):
        self._set_batch_float64_array(16, value)

    @property
    def debugtrace(self) -> List[bool]:
        """
        DSS property name: debugtrace
        DSS property index: 17
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 17)
        ]
    @debugtrace.setter
    def debugtrace(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 17, value)

    @property
    def maxtapchange(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: maxtapchange
        DSS property index: 18
        """
        return BatchInt32ArrayProxy(self, 18)

    @maxtapchange.setter
    def maxtapchange(self, value):
        self._set_batch_int32_array(18, value)

    @property
    def inversetime(self) -> List[bool]:
        """
        DSS property name: inversetime
        DSS property index: 19
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 19)
        ]
    @inversetime.setter
    def inversetime(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 19, value)

    @property
    def tapwinding(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: tapwinding
        DSS property index: 20
        """
        return BatchInt32ArrayProxy(self, 20)

    @tapwinding.setter
    def tapwinding(self, value):
        self._set_batch_int32_array(20, value)

    @property
    def vlimit(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: vlimit
        DSS property index: 21
        """
        return BatchFloat64ArrayProxy(self, 21)

    @vlimit.setter
    def vlimit(self, value):
        self._set_batch_float64_array(21, value)

    @property
    def PTphase(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: PTphase
        DSS property index: 22
        """
        return BatchInt32ArrayProxy(self, 22)

    @PTphase.setter
    def PTphase(self, value: Union[AnyStr, int, RegControl.RegControlPhaseSelection, List[AnyStr], List[Union[int, RegControl.RegControlPhaseSelection]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(22, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(22, value)

    @property
    def PTphase_str(self) -> str:
        """
        DSS property name: PTphase
        DSS property index: 22
        """
        return self._get_prop_string(22)

    @PTphase_str.setter
    def PTphase_str(self, value: AnyStr):
        self.PTphase = value

    @property
    def revThreshold(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: revThreshold
        DSS property index: 23
        """
        return BatchFloat64ArrayProxy(self, 23)

    @revThreshold.setter
    def revThreshold(self, value):
        self._set_batch_float64_array(23, value)

    @property
    def revDelay(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: revDelay
        DSS property index: 24
        """
        return BatchFloat64ArrayProxy(self, 24)

    @revDelay.setter
    def revDelay(self, value):
        self._set_batch_float64_array(24, value)

    @property
    def revNeutral(self) -> List[bool]:
        """
        DSS property name: revNeutral
        DSS property index: 25
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 25)
        ]
    @revNeutral.setter
    def revNeutral(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 25, value)

    @property
    def EventLog(self) -> List[bool]:
        """
        DSS property name: EventLog
        DSS property index: 26
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 26)
        ]
    @EventLog.setter
    def EventLog(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 26, value)

    @property
    def RemotePTRatio(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: RemotePTRatio
        DSS property index: 27
        """
        return BatchFloat64ArrayProxy(self, 27)

    @RemotePTRatio.setter
    def RemotePTRatio(self, value):
        self._set_batch_float64_array(27, value)

    @property
    def TapNum(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: TapNum
        DSS property index: 28
        """
        return BatchInt32ArrayProxy(self, 28)

    @TapNum.setter
    def TapNum(self, value):
        self._set_batch_int32_array(28, value)

    def Reset(self, value: bool):
        """
        DSS property name: Reset
        DSS property index: 29
        """
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 29, value)

    @property
    def LDC_Z(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: LDC_Z
        DSS property index: 30
        """
        return BatchFloat64ArrayProxy(self, 30)

    @LDC_Z.setter
    def LDC_Z(self, value):
        self._set_batch_float64_array(30, value)

    @property
    def rev_Z(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: rev_Z
        DSS property index: 31
        """
        return BatchFloat64ArrayProxy(self, 31)

    @rev_Z.setter
    def rev_Z(self, value):
        self._set_batch_float64_array(31, value)

    @property
    def Cogen(self) -> List[bool]:
        """
        DSS property name: Cogen
        DSS property index: 32
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 32)
        ]
    @Cogen.setter
    def Cogen(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 32, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 33
        """
        return BatchFloat64ArrayProxy(self, 33)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(33, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 34
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 34)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 34, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 35
        """
        self._set_batch_string(35, value)

class InvControlBatch(DSSBatch):
    _cls_name = 'InvControl'
    _obj_cls = InvControl
    _cls_idx = 41


    @property
    def DERList(self) -> List[List[str]]:
        """
        DSS property name: DERList
        DSS property index: 1
        """
        return self._get_string_ll(1)

    @DERList.setter
    def DERList(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._ffi.unpack(self.pointer[0], self.count[0]):
            self._lib.Obj_SetStringArray(x, 1, value_ptr, value_count)

        self._check_for_error()

    @property
    def Mode(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Mode
        DSS property index: 2
        """
        return BatchInt32ArrayProxy(self, 2)

    @Mode.setter
    def Mode(self, value: Union[AnyStr, int, InvControl.InvControlControlMode, List[AnyStr], List[Union[int, InvControl.InvControlControlMode]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(2, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(2, value)

    @property
    def Mode_str(self) -> str:
        """
        DSS property name: Mode
        DSS property index: 2
        """
        return self._get_prop_string(2)

    @Mode_str.setter
    def Mode_str(self, value: AnyStr):
        self.Mode = value

    @property
    def CombiMode(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: CombiMode
        DSS property index: 3
        """
        return BatchInt32ArrayProxy(self, 3)

    @CombiMode.setter
    def CombiMode(self, value: Union[AnyStr, int, InvControl.InvControlCombiMode, List[AnyStr], List[Union[int, InvControl.InvControlCombiMode]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(3, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(3, value)

    @property
    def CombiMode_str(self) -> str:
        """
        DSS property name: CombiMode
        DSS property index: 3
        """
        return self._get_prop_string(3)

    @CombiMode_str.setter
    def CombiMode_str(self, value: AnyStr):
        self.CombiMode = value

    @property
    def vvc_curve1(self) -> List[str]:
        """
        DSS property name: vvc_curve1
        DSS property index: 4
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 4)

    @vvc_curve1.setter
    def vvc_curve1(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(4, value)
            return

        self._set_batch_string(4, value)

    @property
    def vvc_curve1_obj(self) -> List[str]:
        """
        DSS property name: vvc_curve1
        DSS property index: 4
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 4)

    @vvc_curve1_obj.setter
    def vvc_curve1_obj(self, value: XYcurve):
        self._set_batch_string(4, value)

    @property
    def hysteresis_offset(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: hysteresis_offset
        DSS property index: 5
        """
        return BatchFloat64ArrayProxy(self, 5)

    @hysteresis_offset.setter
    def hysteresis_offset(self, value):
        self._set_batch_float64_array(5, value)

    @property
    def voltage_curvex_ref(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: voltage_curvex_ref
        DSS property index: 6
        """
        return BatchInt32ArrayProxy(self, 6)

    @voltage_curvex_ref.setter
    def voltage_curvex_ref(self, value: Union[AnyStr, int, InvControl.InvControlVoltageCurveXRef, List[AnyStr], List[Union[int, InvControl.InvControlVoltageCurveXRef]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(6, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(6, value)

    @property
    def voltage_curvex_ref_str(self) -> str:
        """
        DSS property name: voltage_curvex_ref
        DSS property index: 6
        """
        return self._get_prop_string(6)

    @voltage_curvex_ref_str.setter
    def voltage_curvex_ref_str(self, value: AnyStr):
        self.voltage_curvex_ref = value

    @property
    def avgwindowlen(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: avgwindowlen
        DSS property index: 7
        """
        return BatchInt32ArrayProxy(self, 7)

    @avgwindowlen.setter
    def avgwindowlen(self, value):
        self._set_batch_int32_array(7, value)

    @property
    def voltwatt_curve(self) -> List[str]:
        """
        DSS property name: voltwatt_curve
        DSS property index: 8
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 8)

    @voltwatt_curve.setter
    def voltwatt_curve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(8, value)
            return

        self._set_batch_string(8, value)

    @property
    def voltwatt_curve_obj(self) -> List[str]:
        """
        DSS property name: voltwatt_curve
        DSS property index: 8
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 8)

    @voltwatt_curve_obj.setter
    def voltwatt_curve_obj(self, value: XYcurve):
        self._set_batch_string(8, value)

    @property
    def DbVMin(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: DbVMin
        DSS property index: 9
        """
        return BatchFloat64ArrayProxy(self, 9)

    @DbVMin.setter
    def DbVMin(self, value):
        self._set_batch_float64_array(9, value)

    @property
    def DbVMax(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: DbVMax
        DSS property index: 10
        """
        return BatchFloat64ArrayProxy(self, 10)

    @DbVMax.setter
    def DbVMax(self, value):
        self._set_batch_float64_array(10, value)

    @property
    def ArGraLowV(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: ArGraLowV
        DSS property index: 11
        """
        return BatchFloat64ArrayProxy(self, 11)

    @ArGraLowV.setter
    def ArGraLowV(self, value):
        self._set_batch_float64_array(11, value)

    @property
    def ArGraHiV(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: ArGraHiV
        DSS property index: 12
        """
        return BatchFloat64ArrayProxy(self, 12)

    @ArGraHiV.setter
    def ArGraHiV(self, value):
        self._set_batch_float64_array(12, value)

    @property
    def DynReacavgwindowlen(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: DynReacavgwindowlen
        DSS property index: 13
        """
        return BatchInt32ArrayProxy(self, 13)

    @DynReacavgwindowlen.setter
    def DynReacavgwindowlen(self, value):
        self._set_batch_int32_array(13, value)

    @property
    def deltaQ_Factor(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: deltaQ_Factor
        DSS property index: 14
        """
        return BatchFloat64ArrayProxy(self, 14)

    @deltaQ_Factor.setter
    def deltaQ_Factor(self, value):
        self._set_batch_float64_array(14, value)

    @property
    def VoltageChangeTolerance(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: VoltageChangeTolerance
        DSS property index: 15
        """
        return BatchFloat64ArrayProxy(self, 15)

    @VoltageChangeTolerance.setter
    def VoltageChangeTolerance(self, value):
        self._set_batch_float64_array(15, value)

    @property
    def VarChangeTolerance(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: VarChangeTolerance
        DSS property index: 16
        """
        return BatchFloat64ArrayProxy(self, 16)

    @VarChangeTolerance.setter
    def VarChangeTolerance(self, value):
        self._set_batch_float64_array(16, value)

    @property
    def VoltwattYAxis(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: VoltwattYAxis
        DSS property index: 17
        """
        return BatchInt32ArrayProxy(self, 17)

    @VoltwattYAxis.setter
    def VoltwattYAxis(self, value: Union[AnyStr, int, InvControl.InvControlVoltWattYAxis, List[AnyStr], List[Union[int, InvControl.InvControlVoltWattYAxis]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(17, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(17, value)

    @property
    def VoltwattYAxis_str(self) -> str:
        """
        DSS property name: VoltwattYAxis
        DSS property index: 17
        """
        return self._get_prop_string(17)

    @VoltwattYAxis_str.setter
    def VoltwattYAxis_str(self, value: AnyStr):
        self.VoltwattYAxis = value

    @property
    def RateofChangeMode(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: RateofChangeMode
        DSS property index: 18
        """
        return BatchInt32ArrayProxy(self, 18)

    @RateofChangeMode.setter
    def RateofChangeMode(self, value: Union[AnyStr, int, InvControl.InvControlRateOfChangeMode, List[AnyStr], List[Union[int, InvControl.InvControlRateOfChangeMode]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(18, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(18, value)

    @property
    def RateofChangeMode_str(self) -> str:
        """
        DSS property name: RateofChangeMode
        DSS property index: 18
        """
        return self._get_prop_string(18)

    @RateofChangeMode_str.setter
    def RateofChangeMode_str(self, value: AnyStr):
        self.RateofChangeMode = value

    @property
    def LPFTau(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: LPFTau
        DSS property index: 19
        """
        return BatchFloat64ArrayProxy(self, 19)

    @LPFTau.setter
    def LPFTau(self, value):
        self._set_batch_float64_array(19, value)

    @property
    def RiseFallLimit(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: RiseFallLimit
        DSS property index: 20
        """
        return BatchFloat64ArrayProxy(self, 20)

    @RiseFallLimit.setter
    def RiseFallLimit(self, value):
        self._set_batch_float64_array(20, value)

    @property
    def deltaP_Factor(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: deltaP_Factor
        DSS property index: 21
        """
        return BatchFloat64ArrayProxy(self, 21)

    @deltaP_Factor.setter
    def deltaP_Factor(self, value):
        self._set_batch_float64_array(21, value)

    @property
    def EventLog(self) -> List[bool]:
        """
        DSS property name: EventLog
        DSS property index: 22
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 22)
        ]
    @EventLog.setter
    def EventLog(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 22, value)

    @property
    def RefReactivePower(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: RefReactivePower
        DSS property index: 23
        """
        return BatchInt32ArrayProxy(self, 23)

    @RefReactivePower.setter
    def RefReactivePower(self, value: Union[AnyStr, int, InvControl.InvControlReactivePowerReference, List[AnyStr], List[Union[int, InvControl.InvControlReactivePowerReference]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(23, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(23, value)

    @property
    def RefReactivePower_str(self) -> str:
        """
        DSS property name: RefReactivePower
        DSS property index: 23
        """
        return self._get_prop_string(23)

    @RefReactivePower_str.setter
    def RefReactivePower_str(self, value: AnyStr):
        self.RefReactivePower = value

    @property
    def ActivePChangeTolerance(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: ActivePChangeTolerance
        DSS property index: 24
        """
        return BatchFloat64ArrayProxy(self, 24)

    @ActivePChangeTolerance.setter
    def ActivePChangeTolerance(self, value):
        self._set_batch_float64_array(24, value)

    @property
    def monVoltageCalc(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: monVoltageCalc
        DSS property index: 25
        """
        return BatchInt32ArrayProxy(self, 25)

    @monVoltageCalc.setter
    def monVoltageCalc(self, value: Union[AnyStr, int, MonitoredPhase, List[AnyStr], List[Union[int, MonitoredPhase]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(25, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(25, value)

    @property
    def monVoltageCalc_str(self) -> str:
        """
        DSS property name: monVoltageCalc
        DSS property index: 25
        """
        return self._get_prop_string(25)

    @monVoltageCalc_str.setter
    def monVoltageCalc_str(self, value: AnyStr):
        self.monVoltageCalc = value

    @property
    def monBus(self) -> List[List[str]]:
        """
        DSS property name: monBus
        DSS property index: 26
        """
        return self._get_string_ll(26)

    @monBus.setter
    def monBus(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._ffi.unpack(self.pointer[0], self.count[0]):
            self._lib.Obj_SetStringArray(x, 26, value_ptr, value_count)

        self._check_for_error()

    @property
    def MonBusesVbase(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: MonBusesVbase
        DSS property index: 27
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 27)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @MonBusesVbase.setter
    def MonBusesVbase(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(27, value)

    @property
    def voltwattCH_curve(self) -> List[str]:
        """
        DSS property name: voltwattCH_curve
        DSS property index: 28
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 28)

    @voltwattCH_curve.setter
    def voltwattCH_curve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(28, value)
            return

        self._set_batch_string(28, value)

    @property
    def voltwattCH_curve_obj(self) -> List[str]:
        """
        DSS property name: voltwattCH_curve
        DSS property index: 28
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 28)

    @voltwattCH_curve_obj.setter
    def voltwattCH_curve_obj(self, value: XYcurve):
        self._set_batch_string(28, value)

    @property
    def wattpf_curve(self) -> List[str]:
        """
        DSS property name: wattpf_curve
        DSS property index: 29
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 29)

    @wattpf_curve.setter
    def wattpf_curve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(29, value)
            return

        self._set_batch_string(29, value)

    @property
    def wattpf_curve_obj(self) -> List[str]:
        """
        DSS property name: wattpf_curve
        DSS property index: 29
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 29)

    @wattpf_curve_obj.setter
    def wattpf_curve_obj(self, value: XYcurve):
        self._set_batch_string(29, value)

    @property
    def wattvar_curve(self) -> List[str]:
        """
        DSS property name: wattvar_curve
        DSS property index: 30
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 30)

    @wattvar_curve.setter
    def wattvar_curve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(30, value)
            return

        self._set_batch_string(30, value)

    @property
    def wattvar_curve_obj(self) -> List[str]:
        """
        DSS property name: wattvar_curve
        DSS property index: 30
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 30)

    @wattvar_curve_obj.setter
    def wattvar_curve_obj(self, value: XYcurve):
        self._set_batch_string(30, value)

    @property
    def PVSystemList(self) -> List[List[str]]:
        """
        DSS property name: PVSystemList
        DSS property index: 31
        """
        return self._get_string_ll(31)

    @PVSystemList.setter
    def PVSystemList(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._ffi.unpack(self.pointer[0], self.count[0]):
            self._lib.Obj_SetStringArray(x, 31, value_ptr, value_count)

        self._check_for_error()

    @property
    def Vsetpoint(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Vsetpoint
        DSS property index: 32
        """
        return BatchFloat64ArrayProxy(self, 32)

    @Vsetpoint.setter
    def Vsetpoint(self, value):
        self._set_batch_float64_array(32, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 33
        """
        return BatchFloat64ArrayProxy(self, 33)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(33, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 34
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 34)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 34, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 35
        """
        self._set_batch_string(35, value)

class ExpControlBatch(DSSBatch):
    _cls_name = 'ExpControl'
    _obj_cls = ExpControl
    _cls_idx = 42


    @property
    def PVSystemList(self) -> List[List[str]]:
        """
        DSS property name: PVSystemList
        DSS property index: 1
        """
        return self._get_string_ll(1)

    @PVSystemList.setter
    def PVSystemList(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._ffi.unpack(self.pointer[0], self.count[0]):
            self._lib.Obj_SetStringArray(x, 1, value_ptr, value_count)

        self._check_for_error()

    @property
    def Vreg(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Vreg
        DSS property index: 2
        """
        return BatchFloat64ArrayProxy(self, 2)

    @Vreg.setter
    def Vreg(self, value):
        self._set_batch_float64_array(2, value)

    @property
    def Slope(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Slope
        DSS property index: 3
        """
        return BatchFloat64ArrayProxy(self, 3)

    @Slope.setter
    def Slope(self, value):
        self._set_batch_float64_array(3, value)

    @property
    def VregTau(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: VregTau
        DSS property index: 4
        """
        return BatchFloat64ArrayProxy(self, 4)

    @VregTau.setter
    def VregTau(self, value):
        self._set_batch_float64_array(4, value)

    @property
    def Qbias(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Qbias
        DSS property index: 5
        """
        return BatchFloat64ArrayProxy(self, 5)

    @Qbias.setter
    def Qbias(self, value):
        self._set_batch_float64_array(5, value)

    @property
    def VregMin(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: VregMin
        DSS property index: 6
        """
        return BatchFloat64ArrayProxy(self, 6)

    @VregMin.setter
    def VregMin(self, value):
        self._set_batch_float64_array(6, value)

    @property
    def VregMax(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: VregMax
        DSS property index: 7
        """
        return BatchFloat64ArrayProxy(self, 7)

    @VregMax.setter
    def VregMax(self, value):
        self._set_batch_float64_array(7, value)

    @property
    def QmaxLead(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: QmaxLead
        DSS property index: 8
        """
        return BatchFloat64ArrayProxy(self, 8)

    @QmaxLead.setter
    def QmaxLead(self, value):
        self._set_batch_float64_array(8, value)

    @property
    def QmaxLag(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: QmaxLag
        DSS property index: 9
        """
        return BatchFloat64ArrayProxy(self, 9)

    @QmaxLag.setter
    def QmaxLag(self, value):
        self._set_batch_float64_array(9, value)

    @property
    def EventLog(self) -> List[bool]:
        """
        DSS property name: EventLog
        DSS property index: 10
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 10)
        ]
    @EventLog.setter
    def EventLog(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 10, value)

    @property
    def DeltaQ_factor(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: DeltaQ_factor
        DSS property index: 11
        """
        return BatchFloat64ArrayProxy(self, 11)

    @DeltaQ_factor.setter
    def DeltaQ_factor(self, value):
        self._set_batch_float64_array(11, value)

    @property
    def PreferQ(self) -> List[bool]:
        """
        DSS property name: PreferQ
        DSS property index: 12
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 12)
        ]
    @PreferQ.setter
    def PreferQ(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 12, value)

    @property
    def Tresponse(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Tresponse
        DSS property index: 13
        """
        return BatchFloat64ArrayProxy(self, 13)

    @Tresponse.setter
    def Tresponse(self, value):
        self._set_batch_float64_array(13, value)

    @property
    def DERList(self) -> List[List[str]]:
        """
        DSS property name: DERList
        DSS property index: 14
        """
        return self._get_string_ll(14)

    @DERList.setter
    def DERList(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._ffi.unpack(self.pointer[0], self.count[0]):
            self._lib.Obj_SetStringArray(x, 14, value_ptr, value_count)

        self._check_for_error()

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 15
        """
        return BatchFloat64ArrayProxy(self, 15)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(15, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 16
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 16)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 16, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 17
        """
        self._set_batch_string(17, value)

class GICLineBatch(DSSBatch):
    _cls_name = 'GICLine'
    _obj_cls = GICLine
    _cls_idx = 43


    @property
    def bus1(self) -> List[str]:
        """
        DSS property name: bus1
        DSS property index: 1
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1) 

    @bus1.setter
    def bus1(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 1, value)

    @property
    def bus2(self) -> List[str]:
        """
        DSS property name: bus2
        DSS property index: 2
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 2) 

    @bus2.setter
    def bus2(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 2, value)

    @property
    def Volts(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Volts
        DSS property index: 3
        """
        return BatchFloat64ArrayProxy(self, 3)

    @Volts.setter
    def Volts(self, value):
        self._set_batch_float64_array(3, value)

    @property
    def Angle(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Angle
        DSS property index: 4
        """
        return BatchFloat64ArrayProxy(self, 4)

    @Angle.setter
    def Angle(self, value):
        self._set_batch_float64_array(4, value)

    @property
    def frequency(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: frequency
        DSS property index: 5
        """
        return BatchFloat64ArrayProxy(self, 5)

    @frequency.setter
    def frequency(self, value):
        self._set_batch_float64_array(5, value)

    @property
    def phases(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: phases
        DSS property index: 6
        """
        return BatchInt32ArrayProxy(self, 6)

    @phases.setter
    def phases(self, value):
        self._set_batch_int32_array(6, value)

    @property
    def R(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: R
        DSS property index: 7
        """
        return BatchFloat64ArrayProxy(self, 7)

    @R.setter
    def R(self, value):
        self._set_batch_float64_array(7, value)

    @property
    def X(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: X
        DSS property index: 8
        """
        return BatchFloat64ArrayProxy(self, 8)

    @X.setter
    def X(self, value):
        self._set_batch_float64_array(8, value)

    @property
    def C(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: C
        DSS property index: 9
        """
        return BatchFloat64ArrayProxy(self, 9)

    @C.setter
    def C(self, value):
        self._set_batch_float64_array(9, value)

    @property
    def EN(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: EN
        DSS property index: 10
        """
        return BatchFloat64ArrayProxy(self, 10)

    @EN.setter
    def EN(self, value):
        self._set_batch_float64_array(10, value)

    @property
    def EE(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: EE
        DSS property index: 11
        """
        return BatchFloat64ArrayProxy(self, 11)

    @EE.setter
    def EE(self, value):
        self._set_batch_float64_array(11, value)

    @property
    def Lat1(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Lat1
        DSS property index: 12
        """
        return BatchFloat64ArrayProxy(self, 12)

    @Lat1.setter
    def Lat1(self, value):
        self._set_batch_float64_array(12, value)

    @property
    def Lon1(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Lon1
        DSS property index: 13
        """
        return BatchFloat64ArrayProxy(self, 13)

    @Lon1.setter
    def Lon1(self, value):
        self._set_batch_float64_array(13, value)

    @property
    def Lat2(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Lat2
        DSS property index: 14
        """
        return BatchFloat64ArrayProxy(self, 14)

    @Lat2.setter
    def Lat2(self, value):
        self._set_batch_float64_array(14, value)

    @property
    def Lon2(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Lon2
        DSS property index: 15
        """
        return BatchFloat64ArrayProxy(self, 15)

    @Lon2.setter
    def Lon2(self, value):
        self._set_batch_float64_array(15, value)

    @property
    def spectrum(self) -> List[str]:
        """
        DSS property name: spectrum
        DSS property index: 16
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 16)

    @spectrum.setter
    def spectrum(self, value: Union[AnyStr, Spectrum]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(16, value)
            return

        self._set_batch_string(16, value)

    @property
    def spectrum_obj(self) -> List[str]:
        """
        DSS property name: spectrum
        DSS property index: 16
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 16)

    @spectrum_obj.setter
    def spectrum_obj(self, value: Spectrum):
        self._set_batch_string(16, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 17
        """
        return BatchFloat64ArrayProxy(self, 17)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(17, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 18
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 18)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 18, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 19
        """
        self._set_batch_string(19, value)

class GICTransformerBatch(DSSBatch):
    _cls_name = 'GICTransformer'
    _obj_cls = GICTransformer
    _cls_idx = 44


    @property
    def BusH(self) -> List[str]:
        """
        DSS property name: BusH
        DSS property index: 1
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1) 

    @BusH.setter
    def BusH(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 1, value)

    @property
    def BusNH(self) -> List[str]:
        """
        DSS property name: BusNH
        DSS property index: 2
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 2) 

    @BusNH.setter
    def BusNH(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 2, value)

    @property
    def BusX(self) -> List[str]:
        """
        DSS property name: BusX
        DSS property index: 3
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 3) 

    @BusX.setter
    def BusX(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 3, value)

    @property
    def BusNX(self) -> List[str]:
        """
        DSS property name: BusNX
        DSS property index: 4
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 4) 

    @BusNX.setter
    def BusNX(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 4, value)

    @property
    def phases(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: phases
        DSS property index: 5
        """
        return BatchInt32ArrayProxy(self, 5)

    @phases.setter
    def phases(self, value):
        self._set_batch_int32_array(5, value)

    @property
    def Type(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Type
        DSS property index: 6
        """
        return BatchInt32ArrayProxy(self, 6)

    @Type.setter
    def Type(self, value: Union[AnyStr, int, GICTransformer.GICTransformerType, List[AnyStr], List[Union[int, GICTransformer.GICTransformerType]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(6, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(6, value)

    @property
    def Type_str(self) -> str:
        """
        DSS property name: Type
        DSS property index: 6
        """
        return self._get_prop_string(6)

    @Type_str.setter
    def Type_str(self, value: AnyStr):
        self.Type = value

    @property
    def R1(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: R1
        DSS property index: 7
        """
        return BatchFloat64ArrayProxy(self, 7)

    @R1.setter
    def R1(self, value):
        self._set_batch_float64_array(7, value)

    @property
    def R2(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: R2
        DSS property index: 8
        """
        return BatchFloat64ArrayProxy(self, 8)

    @R2.setter
    def R2(self, value):
        self._set_batch_float64_array(8, value)

    @property
    def KVLL1(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: KVLL1
        DSS property index: 9
        """
        return BatchFloat64ArrayProxy(self, 9)

    @KVLL1.setter
    def KVLL1(self, value):
        self._set_batch_float64_array(9, value)

    @property
    def KVLL2(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: KVLL2
        DSS property index: 10
        """
        return BatchFloat64ArrayProxy(self, 10)

    @KVLL2.setter
    def KVLL2(self, value):
        self._set_batch_float64_array(10, value)

    @property
    def MVA(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: MVA
        DSS property index: 11
        """
        return BatchFloat64ArrayProxy(self, 11)

    @MVA.setter
    def MVA(self, value):
        self._set_batch_float64_array(11, value)

    @property
    def VarCurve(self) -> List[str]:
        """
        DSS property name: VarCurve
        DSS property index: 12
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 12)

    @VarCurve.setter
    def VarCurve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(12, value)
            return

        self._set_batch_string(12, value)

    @property
    def VarCurve_obj(self) -> List[str]:
        """
        DSS property name: VarCurve
        DSS property index: 12
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 12)

    @VarCurve_obj.setter
    def VarCurve_obj(self, value: XYcurve):
        self._set_batch_string(12, value)

    @property
    def pctR1(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %R1
        DSS property index: 13
        """
        return BatchFloat64ArrayProxy(self, 13)

    @pctR1.setter
    def pctR1(self, value):
        self._set_batch_float64_array(13, value)

    @property
    def pctR2(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %R2
        DSS property index: 14
        """
        return BatchFloat64ArrayProxy(self, 14)

    @pctR2.setter
    def pctR2(self, value):
        self._set_batch_float64_array(14, value)

    @property
    def K(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: K
        DSS property index: 15
        """
        return BatchFloat64ArrayProxy(self, 15)

    @K.setter
    def K(self, value):
        self._set_batch_float64_array(15, value)

    @property
    def normamps(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: normamps
        DSS property index: 16
        """
        return BatchFloat64ArrayProxy(self, 16)

    @normamps.setter
    def normamps(self, value):
        self._set_batch_float64_array(16, value)

    @property
    def emergamps(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: emergamps
        DSS property index: 17
        """
        return BatchFloat64ArrayProxy(self, 17)

    @emergamps.setter
    def emergamps(self, value):
        self._set_batch_float64_array(17, value)

    @property
    def faultrate(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: faultrate
        DSS property index: 18
        """
        return BatchFloat64ArrayProxy(self, 18)

    @faultrate.setter
    def faultrate(self, value):
        self._set_batch_float64_array(18, value)

    @property
    def pctperm(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: pctperm
        DSS property index: 19
        """
        return BatchFloat64ArrayProxy(self, 19)

    @pctperm.setter
    def pctperm(self, value):
        self._set_batch_float64_array(19, value)

    @property
    def repair(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: repair
        DSS property index: 20
        """
        return BatchFloat64ArrayProxy(self, 20)

    @repair.setter
    def repair(self, value):
        self._set_batch_float64_array(20, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 21
        """
        return BatchFloat64ArrayProxy(self, 21)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(21, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 22
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 22)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 22, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 23
        """
        self._set_batch_string(23, value)

class VSConverterBatch(DSSBatch):
    _cls_name = 'VSConverter'
    _obj_cls = VSConverter
    _cls_idx = 45


    @property
    def phases(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: phases
        DSS property index: 1
        """
        return BatchInt32ArrayProxy(self, 1)

    @phases.setter
    def phases(self, value):
        self._set_batch_int32_array(1, value)

    @property
    def Bus1(self) -> List[str]:
        """
        DSS property name: Bus1
        DSS property index: 2
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 2) 

    @Bus1.setter
    def Bus1(self, value: AnyStr): #TODO: list of AnyStr
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Batch_SetString(self.pointer[0], self.count[0], 2, value)

    @property
    def kVac(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kVac
        DSS property index: 3
        """
        return BatchFloat64ArrayProxy(self, 3)

    @kVac.setter
    def kVac(self, value):
        self._set_batch_float64_array(3, value)

    @property
    def kVdc(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kVdc
        DSS property index: 4
        """
        return BatchFloat64ArrayProxy(self, 4)

    @kVdc.setter
    def kVdc(self, value):
        self._set_batch_float64_array(4, value)

    @property
    def kW(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kW
        DSS property index: 5
        """
        return BatchFloat64ArrayProxy(self, 5)

    @kW.setter
    def kW(self, value):
        self._set_batch_float64_array(5, value)

    @property
    def Ndc(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Ndc
        DSS property index: 6
        """
        return BatchInt32ArrayProxy(self, 6)

    @Ndc.setter
    def Ndc(self, value):
        self._set_batch_int32_array(6, value)

    @property
    def Rac(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Rac
        DSS property index: 7
        """
        return BatchFloat64ArrayProxy(self, 7)

    @Rac.setter
    def Rac(self, value):
        self._set_batch_float64_array(7, value)

    @property
    def Xac(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Xac
        DSS property index: 8
        """
        return BatchFloat64ArrayProxy(self, 8)

    @Xac.setter
    def Xac(self, value):
        self._set_batch_float64_array(8, value)

    @property
    def m0(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: m0
        DSS property index: 9
        """
        return BatchFloat64ArrayProxy(self, 9)

    @m0.setter
    def m0(self, value):
        self._set_batch_float64_array(9, value)

    @property
    def d0(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: d0
        DSS property index: 10
        """
        return BatchFloat64ArrayProxy(self, 10)

    @d0.setter
    def d0(self, value):
        self._set_batch_float64_array(10, value)

    @property
    def Mmin(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Mmin
        DSS property index: 11
        """
        return BatchFloat64ArrayProxy(self, 11)

    @Mmin.setter
    def Mmin(self, value):
        self._set_batch_float64_array(11, value)

    @property
    def Mmax(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Mmax
        DSS property index: 12
        """
        return BatchFloat64ArrayProxy(self, 12)

    @Mmax.setter
    def Mmax(self, value):
        self._set_batch_float64_array(12, value)

    @property
    def Iacmax(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Iacmax
        DSS property index: 13
        """
        return BatchFloat64ArrayProxy(self, 13)

    @Iacmax.setter
    def Iacmax(self, value):
        self._set_batch_float64_array(13, value)

    @property
    def Idcmax(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Idcmax
        DSS property index: 14
        """
        return BatchFloat64ArrayProxy(self, 14)

    @Idcmax.setter
    def Idcmax(self, value):
        self._set_batch_float64_array(14, value)

    @property
    def Vacref(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Vacref
        DSS property index: 15
        """
        return BatchFloat64ArrayProxy(self, 15)

    @Vacref.setter
    def Vacref(self, value):
        self._set_batch_float64_array(15, value)

    @property
    def Pacref(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Pacref
        DSS property index: 16
        """
        return BatchFloat64ArrayProxy(self, 16)

    @Pacref.setter
    def Pacref(self, value):
        self._set_batch_float64_array(16, value)

    @property
    def Qacref(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Qacref
        DSS property index: 17
        """
        return BatchFloat64ArrayProxy(self, 17)

    @Qacref.setter
    def Qacref(self, value):
        self._set_batch_float64_array(17, value)

    @property
    def Vdcref(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Vdcref
        DSS property index: 18
        """
        return BatchFloat64ArrayProxy(self, 18)

    @Vdcref.setter
    def Vdcref(self, value):
        self._set_batch_float64_array(18, value)

    @property
    def VscMode(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: VscMode
        DSS property index: 19
        """
        return BatchInt32ArrayProxy(self, 19)

    @VscMode.setter
    def VscMode(self, value: Union[AnyStr, int, VSConverter.VSConverterControlMode, List[AnyStr], List[Union[int, VSConverter.VSConverterControlMode]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(19, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(19, value)

    @property
    def VscMode_str(self) -> str:
        """
        DSS property name: VscMode
        DSS property index: 19
        """
        return self._get_prop_string(19)

    @VscMode_str.setter
    def VscMode_str(self, value: AnyStr):
        self.VscMode = value

    @property
    def spectrum(self) -> List[str]:
        """
        DSS property name: spectrum
        DSS property index: 20
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 20)

    @spectrum.setter
    def spectrum(self, value: Union[AnyStr, Spectrum]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(20, value)
            return

        self._set_batch_string(20, value)

    @property
    def spectrum_obj(self) -> List[str]:
        """
        DSS property name: spectrum
        DSS property index: 20
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 20)

    @spectrum_obj.setter
    def spectrum_obj(self, value: Spectrum):
        self._set_batch_string(20, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 21
        """
        return BatchFloat64ArrayProxy(self, 21)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(21, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 22
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 22)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 22, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 23
        """
        self._set_batch_string(23, value)

class MonitorBatch(DSSBatch):
    _cls_name = 'Monitor'
    _obj_cls = Monitor
    _cls_idx = 46


    @property
    def element(self) -> List[str]:
        """
        DSS property name: element
        DSS property index: 1
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @element.setter
    def element(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(1, value)
            return

        self._set_batch_string(1, value)

    @property
    def element_obj(self) -> List[str]:
        """
        DSS property name: element
        DSS property index: 1
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @element_obj.setter
    def element_obj(self, value: DSSObj):
        self._set_batch_string(1, value)

    @property
    def terminal(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: terminal
        DSS property index: 2
        """
        return BatchInt32ArrayProxy(self, 2)

    @terminal.setter
    def terminal(self, value):
        self._set_batch_int32_array(2, value)

    @property
    def mode(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: mode
        DSS property index: 3
        """
        return BatchInt32ArrayProxy(self, 3)

    @mode.setter
    def mode(self, value):
        self._set_batch_int32_array(3, value)

    def action(self, value: Union[str, bytes, int]):
        """
        DSS property name: action
        DSS property index: 4
        """
        if isinstance(value, int):
            self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 4, value)
        else:
            self._set_batch_string(4, value)

    @property
    def residual(self) -> List[bool]:
        """
        DSS property name: residual
        DSS property index: 5
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 5)
        ]
    @residual.setter
    def residual(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 5, value)

    @property
    def VIPolar(self) -> List[bool]:
        """
        DSS property name: VIPolar
        DSS property index: 6
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 6)
        ]
    @VIPolar.setter
    def VIPolar(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 6, value)

    @property
    def PPolar(self) -> List[bool]:
        """
        DSS property name: PPolar
        DSS property index: 7
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 7)
        ]
    @PPolar.setter
    def PPolar(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 7, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 8
        """
        return BatchFloat64ArrayProxy(self, 8)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(8, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 9
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 9)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 9, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 10
        """
        self._set_batch_string(10, value)

class EnergyMeterBatch(DSSBatch):
    _cls_name = 'EnergyMeter'
    _obj_cls = EnergyMeter
    _cls_idx = 47


    @property
    def element(self) -> List[str]:
        """
        DSS property name: element
        DSS property index: 1
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @element.setter
    def element(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(1, value)
            return

        self._set_batch_string(1, value)

    @property
    def element_obj(self) -> List[str]:
        """
        DSS property name: element
        DSS property index: 1
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @element_obj.setter
    def element_obj(self, value: DSSObj):
        self._set_batch_string(1, value)

    @property
    def terminal(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: terminal
        DSS property index: 2
        """
        return BatchInt32ArrayProxy(self, 2)

    @terminal.setter
    def terminal(self, value):
        self._set_batch_int32_array(2, value)

    def action(self, value: Union[str, bytes, int]):
        """
        DSS property name: action
        DSS property index: 3
        """
        if isinstance(value, int):
            self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 3, value)
        else:
            self._set_batch_string(3, value)

    @property
    def option(self) -> List[List[str]]:
        """
        DSS property name: option
        DSS property index: 4
        """
        return self._get_string_ll(4)

    @option.setter
    def option(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._ffi.unpack(self.pointer[0], self.count[0]):
            self._lib.Obj_SetStringArray(x, 4, value_ptr, value_count)

        self._check_for_error()

    @property
    def kVAnormal(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kVAnormal
        DSS property index: 5
        """
        return BatchFloat64ArrayProxy(self, 5)

    @kVAnormal.setter
    def kVAnormal(self, value):
        self._set_batch_float64_array(5, value)

    @property
    def kVAemerg(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kVAemerg
        DSS property index: 6
        """
        return BatchFloat64ArrayProxy(self, 6)

    @kVAemerg.setter
    def kVAemerg(self, value):
        self._set_batch_float64_array(6, value)

    @property
    def peakcurrent(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: peakcurrent
        DSS property index: 7
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 7)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @peakcurrent.setter
    def peakcurrent(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(7, value)

    @property
    def Zonelist(self) -> List[List[str]]:
        """
        DSS property name: Zonelist
        DSS property index: 8
        """
        return self._get_string_ll(8)

    @Zonelist.setter
    def Zonelist(self, value: List[str]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._ffi.unpack(self.pointer[0], self.count[0]):
            self._lib.Obj_SetStringArray(x, 8, value_ptr, value_count)

        self._check_for_error()

    @property
    def LocalOnly(self) -> List[bool]:
        """
        DSS property name: LocalOnly
        DSS property index: 9
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 9)
        ]
    @LocalOnly.setter
    def LocalOnly(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 9, value)

    @property
    def Mask(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: Mask
        DSS property index: 10
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 10)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Mask.setter
    def Mask(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(10, value)

    @property
    def Losses(self) -> List[bool]:
        """
        DSS property name: Losses
        DSS property index: 11
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 11)
        ]
    @Losses.setter
    def Losses(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 11, value)

    @property
    def LineLosses(self) -> List[bool]:
        """
        DSS property name: LineLosses
        DSS property index: 12
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 12)
        ]
    @LineLosses.setter
    def LineLosses(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 12, value)

    @property
    def XfmrLosses(self) -> List[bool]:
        """
        DSS property name: XfmrLosses
        DSS property index: 13
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 13)
        ]
    @XfmrLosses.setter
    def XfmrLosses(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 13, value)

    @property
    def SeqLosses(self) -> List[bool]:
        """
        DSS property name: SeqLosses
        DSS property index: 14
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 14)
        ]
    @SeqLosses.setter
    def SeqLosses(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 14, value)

    @property
    def threePaseLosses(self) -> List[bool]:
        """
        DSS property name: 3phaseLosses
        DSS property index: 15
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 15)
        ]
    @threePaseLosses.setter
    def threePaseLosses(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 15, value)

    @property
    def VbaseLosses(self) -> List[bool]:
        """
        DSS property name: VbaseLosses
        DSS property index: 16
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 16)
        ]
    @VbaseLosses.setter
    def VbaseLosses(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 16, value)

    @property
    def PhaseVoltageReport(self) -> List[bool]:
        """
        DSS property name: PhaseVoltageReport
        DSS property index: 17
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 17)
        ]
    @PhaseVoltageReport.setter
    def PhaseVoltageReport(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 17, value)

    @property
    def Int_Rate(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Int_Rate
        DSS property index: 18
        """
        return BatchFloat64ArrayProxy(self, 18)

    @Int_Rate.setter
    def Int_Rate(self, value):
        self._set_batch_float64_array(18, value)

    @property
    def Int_Duration(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Int_Duration
        DSS property index: 19
        """
        return BatchFloat64ArrayProxy(self, 19)

    @Int_Duration.setter
    def Int_Duration(self, value):
        self._set_batch_float64_array(19, value)

    @property
    def SAIFI(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: SAIFI
        DSS property index: 20
        """
        return BatchFloat64ArrayProxy(self, 20)

    @SAIFI.setter
    def SAIFI(self, value):
        self._set_batch_float64_array(20, value)

    @property
    def SAIFIkW(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: SAIFIkW
        DSS property index: 21
        """
        return BatchFloat64ArrayProxy(self, 21)

    @SAIFIkW.setter
    def SAIFIkW(self, value):
        self._set_batch_float64_array(21, value)

    @property
    def SAIDI(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: SAIDI
        DSS property index: 22
        """
        return BatchFloat64ArrayProxy(self, 22)

    @SAIDI.setter
    def SAIDI(self, value):
        self._set_batch_float64_array(22, value)

    @property
    def CAIDI(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: CAIDI
        DSS property index: 23
        """
        return BatchFloat64ArrayProxy(self, 23)

    @CAIDI.setter
    def CAIDI(self, value):
        self._set_batch_float64_array(23, value)

    @property
    def CustInterrupts(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: CustInterrupts
        DSS property index: 24
        """
        return BatchFloat64ArrayProxy(self, 24)

    @CustInterrupts.setter
    def CustInterrupts(self, value):
        self._set_batch_float64_array(24, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 25
        """
        return BatchFloat64ArrayProxy(self, 25)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(25, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 26
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 26)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 26, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 27
        """
        self._set_batch_string(27, value)

class SensorBatch(DSSBatch):
    _cls_name = 'Sensor'
    _obj_cls = Sensor
    _cls_idx = 48


    @property
    def element(self) -> List[str]:
        """
        DSS property name: element
        DSS property index: 1
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @element.setter
    def element(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_batch_obj(1, value)
            return

        self._set_batch_string(1, value)

    @property
    def element_obj(self) -> List[str]:
        """
        DSS property name: element
        DSS property index: 1
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @element_obj.setter
    def element_obj(self, value: DSSObj):
        self._set_batch_string(1, value)

    @property
    def terminal(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: terminal
        DSS property index: 2
        """
        return BatchInt32ArrayProxy(self, 2)

    @terminal.setter
    def terminal(self, value):
        self._set_batch_int32_array(2, value)

    @property
    def kvbase(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: kvbase
        DSS property index: 3
        """
        return BatchFloat64ArrayProxy(self, 3)

    @kvbase.setter
    def kvbase(self, value):
        self._set_batch_float64_array(3, value)

    @property
    def clear(self) -> List[bool]:
        """
        DSS property name: clear
        DSS property index: 4
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 4)
        ]
    @clear.setter
    def clear(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 4, value)

    @property
    def kVs(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: kVs
        DSS property index: 5
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 5)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @kVs.setter
    def kVs(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(5, value)

    @property
    def currents(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: currents
        DSS property index: 6
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 6)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @currents.setter
    def currents(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(6, value)

    @property
    def kWs(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: kWs
        DSS property index: 7
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 7)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @kWs.setter
    def kWs(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(7, value)

    @property
    def kvars(self) -> List[npt.NDArray[np.float64]]:
        """
        DSS property name: kvars
        DSS property index: 8
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 8)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @kvars.setter
    def kvars(self, value: npt.NDArray[np.float64]):
        self._set_float64_array(8, value)

    @property
    def conn(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: conn
        DSS property index: 9
        """
        return BatchInt32ArrayProxy(self, 9)

    @conn.setter
    def conn(self, value: Union[AnyStr, int, Connection, List[AnyStr], List[Union[int, Connection]]]):
        if isinstance(value, str) or isinstance(value, bytes):
            self._set_batch_string(9, value)
            return

        if not isinstance(value, int) and (isinstance(value[0], str) or isinstance(value[0], bytes)):
            raise NotImplemented

        self._set_batch_int32_array(9, value)

    @property
    def conn_str(self) -> str:
        """
        DSS property name: conn
        DSS property index: 9
        """
        return self._get_prop_string(9)

    @conn_str.setter
    def conn_str(self, value: AnyStr):
        self.conn = value

    @property
    def Deltadirection(self) -> BatchInt32ArrayProxy:
        """
        DSS property name: Deltadirection
        DSS property index: 10
        """
        return BatchInt32ArrayProxy(self, 10)

    @Deltadirection.setter
    def Deltadirection(self, value):
        self._set_batch_int32_array(10, value)

    @property
    def pctError(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: %Error
        DSS property index: 11
        """
        return BatchFloat64ArrayProxy(self, 11)

    @pctError.setter
    def pctError(self, value):
        self._set_batch_float64_array(11, value)

    @property
    def Weight(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: Weight
        DSS property index: 12
        """
        return BatchFloat64ArrayProxy(self, 12)

    @Weight.setter
    def Weight(self, value):
        self._set_batch_float64_array(12, value)

    @property
    def basefreq(self) -> BatchFloat64ArrayProxy:
        """
        DSS property name: basefreq
        DSS property index: 13
        """
        return BatchFloat64ArrayProxy(self, 13)

    @basefreq.setter
    def basefreq(self, value):
        self._set_batch_float64_array(13, value)

    @property
    def enabled(self) -> List[bool]:
        """
        DSS property name: enabled
        DSS property index: 14
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 14)
        ]
    @enabled.setter
    def enabled(self, value: bool):
        self._lib.Batch_SetInt32(self.pointer[0], self.count[0], 14, value)

    def like(self, value: AnyStr):
        """
        DSS property name: like
        DSS property index: 15
        """
        self._set_batch_string(15, value)

class IObj(Base):
    __slots__ = [
        'LineCode',
        'LoadShape',
        'TShape',
        'PriceShape',
        'XYcurve',
        'GrowthShape',
        'TCC_Curve',
        'Spectrum',
        'WireData',
        'CNData',
        'TSData',
        'LineSpacing',
        'LineGeometry',
        'XfmrCode',
        'Line',
        'Vsource',
        'Isource',
        'VCCS',
        'Load',
        'Transformer',
        'Capacitor',
        'Reactor',
        'CapControl',
        'Fault',
        'Generator',
        'GenDispatcher',
        'Storage',
        'StorageController',
        'Relay',
        'Recloser',
        'Fuse',
        'SwtControl',
        'PVSystem',
        'UPFC',
        'UPFCControl',
        'ESPVLControl',
        'IndMach012',
        'GICsource',
        'AutoTrans',
        'RegControl',
        'InvControl',
        'ExpControl',
        'GICLine',
        'GICTransformer',
        'VSConverter',
        'Monitor',
        'EnergyMeter',
        'Sensor',
        '_idx_to_cls',
    ]

    def __init__(self, api_util):
        Base.__init__(self, api_util)
        self._idx_to_cls = dict()

        self.LineCode = IDSSObj(self, 1, LineCode, LineCodeBatch)
        self.LoadShape = IDSSObj(self, 2, LoadShape, LoadShapeBatch)
        self.TShape = IDSSObj(self, 3, TShape, TShapeBatch)
        self.PriceShape = IDSSObj(self, 4, PriceShape, PriceShapeBatch)
        self.XYcurve = IDSSObj(self, 5, XYcurve, XYcurveBatch)
        self.GrowthShape = IDSSObj(self, 6, GrowthShape, GrowthShapeBatch)
        self.TCC_Curve = IDSSObj(self, 7, TCC_Curve, TCC_CurveBatch)
        self.Spectrum = IDSSObj(self, 8, Spectrum, SpectrumBatch)
        self.WireData = IDSSObj(self, 9, WireData, WireDataBatch)
        self.CNData = IDSSObj(self, 10, CNData, CNDataBatch)
        self.TSData = IDSSObj(self, 11, TSData, TSDataBatch)
        self.LineSpacing = IDSSObj(self, 12, LineSpacing, LineSpacingBatch)
        self.LineGeometry = IDSSObj(self, 13, LineGeometry, LineGeometryBatch)
        self.XfmrCode = IDSSObj(self, 14, XfmrCode, XfmrCodeBatch)
        self.Line = IDSSObj(self, 15, Line, LineBatch)
        self.Vsource = IDSSObj(self, 16, Vsource, VsourceBatch)
        self.Isource = IDSSObj(self, 17, Isource, IsourceBatch)
        self.VCCS = IDSSObj(self, 18, VCCS, VCCSBatch)
        self.Load = IDSSObj(self, 19, Load, LoadBatch)
        self.Transformer = IDSSObj(self, 20, Transformer, TransformerBatch)
        self.Capacitor = IDSSObj(self, 22, Capacitor, CapacitorBatch)
        self.Reactor = IDSSObj(self, 23, Reactor, ReactorBatch)
        self.CapControl = IDSSObj(self, 24, CapControl, CapControlBatch)
        self.Fault = IDSSObj(self, 25, Fault, FaultBatch)
        self.Generator = IDSSObj(self, 26, Generator, GeneratorBatch)
        self.GenDispatcher = IDSSObj(self, 27, GenDispatcher, GenDispatcherBatch)
        self.Storage = IDSSObj(self, 28, Storage, StorageBatch)
        self.StorageController = IDSSObj(self, 29, StorageController, StorageControllerBatch)
        self.Relay = IDSSObj(self, 30, Relay, RelayBatch)
        self.Recloser = IDSSObj(self, 31, Recloser, RecloserBatch)
        self.Fuse = IDSSObj(self, 32, Fuse, FuseBatch)
        self.SwtControl = IDSSObj(self, 33, SwtControl, SwtControlBatch)
        self.PVSystem = IDSSObj(self, 34, PVSystem, PVSystemBatch)
        self.UPFC = IDSSObj(self, 35, UPFC, UPFCBatch)
        self.UPFCControl = IDSSObj(self, 36, UPFCControl, UPFCControlBatch)
        self.ESPVLControl = IDSSObj(self, 37, ESPVLControl, ESPVLControlBatch)
        self.IndMach012 = IDSSObj(self, 38, IndMach012, IndMach012Batch)
        self.GICsource = IDSSObj(self, 39, GICsource, GICsourceBatch)
        self.AutoTrans = IDSSObj(self, 40, AutoTrans, AutoTransBatch)
        self.RegControl = IDSSObj(self, 21, RegControl, RegControlBatch)
        self.InvControl = IDSSObj(self, 41, InvControl, InvControlBatch)
        self.ExpControl = IDSSObj(self, 42, ExpControl, ExpControlBatch)
        self.GICLine = IDSSObj(self, 43, GICLine, GICLineBatch)
        self.GICTransformer = IDSSObj(self, 44, GICTransformer, GICTransformerBatch)
        self.VSConverter = IDSSObj(self, 45, VSConverter, VSConverterBatch)
        self.Monitor = IDSSObj(self, 46, Monitor, MonitorBatch)
        self.EnergyMeter = IDSSObj(self, 47, EnergyMeter, EnergyMeterBatch)
        self.Sensor = IDSSObj(self, 48, Sensor, SensorBatch)

__all__ = [
    "IObj",
    "EarthModel",
    "LineType",
    "DimensionUnits",
    "ScanType",
    "SequenceType",
    "Connection",
    "CoreType",
    "PhaseSequence",
    "LoadSolutionModel",
    "RandomType",
    "ControlMode",
    "SolutionMode",
    "SolutionAlgorithm",
    "CircuitModel",
    "AutoAddDeviceType",
    "LoadShapeClass",
    "MonitoredPhase",
]

