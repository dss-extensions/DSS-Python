'''
Object and batch API bases, used internally.

Copyright (c) 2021-2023 Paulo Meira
Copyright (c) 2021-2023 DSS-Extensions contributors
'''
import numpy as np
from typing import Union, List, AnyStr, Optional, Generator
from ._types import Float64Array, Int32Array
from ._cffi_api_util import Base
from .enums import DSSJSONFlags

try:
    import pandas as pd
    LIST_LIKE = (pd.Series, list, tuple)
except ModuleNotFoundError:
    LIST_LIKE = (list, tuple)

# from typing_extensions import Self

# class NotSet:
#     pass

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
        batch._lib.Batch_SetFloat64Array(
            batch.pointer[0],
            batch.count[0],
            self._idx,
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
        batch._lib.Batch_SetFloat64Array(
            batch.pointer[0],
            batch.count[0],
            self._idx,
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
        batch._lib.Batch_SetInt32Array(
            batch.pointer[0],
            batch.count[0],
            self._idx,
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
            self._idx,
            data_ptr
        )
        batch._check_for_error()
        return self

class Edit:
    '''
    Edit is a helper class that makes block-editing DSS properties
    easier. It supports instances for the new Obj and Batch APIs.
    '''

    def __init__(self, obj_or_batch, num_changes=1, needs_begin=True):
        '''
        `num_changes` is required for a few classes to correctly match the official OpenDSS behavior
        and must be the number of properties modified in the current editing block. As of DSS C-API
        v0.13, this is only required for the Monitor class, when the `Action` property is used with 
        the `Process` value.
        '''
        self.needs_begin = needs_begin
        self.obj_or_batch = obj_or_batch
        self.num_changes = num_changes

    def __enter__(self):
        if self.needs_begin:
            self.obj_or_batch.begin_edit()

        return self.obj_or_batch

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.obj_or_batch.end_edit(self.num_changes)


class DSSObj(Base):
    # _properties_by_idx = {
    #     1: ('kV', 'Obj_SetDouble')
    # }
    # _properties_by_name = {
    #     'kV': (1, 'Obj_SetDouble')
    # }
    __slots__ = [
        '_ptr',
        '_ffi',
        '_get_int32_list',
    ]

    def __init__(self, api_util, ptr):
        super().__init__(api_util)
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
        - `SkipDSSClass`: do not add the "DSSClass" property to the JSON objects.

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
        # ffi = self._api_util.ffi
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

    def _set_string_o(self, idx: int, value: AnyStr):
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Obj_SetString(self._ptr, idx, value)
        self._check_for_error()

    def _set_float64_array_o(self, idx: int, value: Float64Array):
        value, value_ptr, value_count = self._prepare_float64_array(value)
        self._lib.Obj_SetFloat64Array(self._ptr, idx, value_ptr, value_count)
        self._check_for_error()

    def _set_int32_array_o(self, idx: int, value: Int32Array):
        value, value_ptr, value_count = self._prepare_int32_array(value)
        self._lib.Obj_SetInt32Array(self._ptr, idx, value_ptr, value_count)
        self._check_for_error()

    def _set_string_array_o(self, idx: int, value: List[AnyStr]):
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
            pycls = DSSObj._idx_to_cls[cls_idx]

        return pycls(self._api_util, other_ptr)

    def _set_obj(self, idx: int, other):
        if other is not None:
            other_ptr = other._ptr
        else:
            other_ptr = self._ffi.NULL

        self._lib.Obj_SetObject(self._ptr, idx, other_ptr)
        self._check_for_error()

    def _get_obj_array(self, idx: int, pycls=None):
        ptr = self._ffi.new('void***')
        cnt = self._ffi.new('int32_t[4]')
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
                pycls = DSSObj._idx_to_cls[cls_idx]
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
        if other is None or (isinstance(other, LIST_LIKE) and len(other) == 0):
            other_ptr = self._ffi.NULL
            other_cnt = 0
        else:
            other_cnt = len(other)
            other_ptr = self.ffi.new('void*[]', other_cnt)
            other_ptr[:] = [o._ptr for o in other]

        self._lib.Obj_SetObjectArray(self._ptr, idx, other_ptr, other_cnt)
        self._check_for_error()

    def begin_edit(self):
        '''
        Marks a DSS object for editing

        In the editing mode, some final side-effects of changing properties are post-poned
        until `_end_edit` is called. This side-effects can be somewhat costly, like updating
        the model parameters or internal matrices.

        If you don't have any performance constraint, you may edit each property individually
        without worrying about using `begin_edit` and `end_edit`. For convenience, those are
        emitted automatically when editing single properties outside an edit block.
        '''
        self._lib.Obj_BeginEdit(self._ptr)
        self._check_for_error()

    def end_edit(self, num_changes: int = 1):
        '''
        Leaves the editing state of a DSS object

        `num_changes` is required for a few classes to correctly match the official OpenDSS behavior
        and must be the number of properties modified in the current editing block. As of DSS C-API
        v0.13, this is only required for the Monitor class, when the `Action` property is used with 
        the `Process` value.
        '''
        self._lib.Obj_EndEdit(self._ptr, num_changes)
        self._check_for_error()

def _get_dispose_batch(lib, ffi):
    def _dispose_batch(ptr):
        if ptr != ffi.NULL and ptr[0] != ffi.NULL:
            lib.Batch_Dispose(ptr[0])

    return _dispose_batch

class DSSBatch(Base):

    #TODO: keep property name for debugging? Or maybe use from the parent object

    def __init__(self, api_util, **kwargs):
        begin_edit = kwargs.pop('begin_edit', None)
        if begin_edit is None:
            begin_edit = True

        if len(kwargs) > 1:
            raise ValueError('Exactly one argument is expected.')

        Base.__init__(self, api_util)
        self._ffi = api_util.ffi
        self.pointer = self._ffi.gc(self._ffi.new('void***'), _get_dispose_batch(self._lib, self._ffi))
        self.count = self._ffi.new('int32_t[4]')

        if len(kwargs) == 0:
            self._lib.Batch_CreateByClass(self.pointer, self.count, self._cls_idx)
            self._check_for_error()
            return

        new_names = kwargs.get('new_names')
        if new_names is not None:
            names, names_ptr, names_count = self._prepare_string_array(new_names)
            self._lib.Batch_CreateFromNew(self.pointer, self.count, self._cls_idx, names_ptr, names_count, begin_edit)
            self._check_for_error()
            return

        new_count = kwargs.get('new_count')
        if new_count is not None:
            self._lib.Batch_CreateFromNew(self.pointer, self.count, self._cls_idx, self._ffi.NULL, new_count, begin_edit)
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

    def begin_edit(self):
        '''
        Marks for editing all DSS objects in the batch

        In the editing mode, some final side-effects of changing properties are post-poned
        until `_end_edit` is called. This side-effects can be somewhat costly, like updating
        the model parameters or internal matrices.

        If you don't have any performance constraint, you may edit each property individually
        without worrying about using `begin_edit` and `end_edit`. For convenience, those are
        emitted automatically when editing single properties outside an edit block.
        '''
        self._lib.Batch_BeginEdit(self.pointer[0], self.count[0])
        self._check_for_error()

    def end_edit(self, num_changes: int = 1):
        '''
        Leaves the editing states of all DSS objects in the batch

        `num_changes` is required for a few classes to correctly match the official OpenDSS behavior
        and must be the number of properties modified in the current editing block. As of DSS C-API
        v0.13, this is only required for the Monitor class, when the `Action` property is used with 
        the `Process` value.
        '''
        self._lib.Batch_EndEdit(self.pointer[0], self.count[0], num_changes)
        self._check_for_error()

    def __eq__(self, other):
        return self is other

    def __len__(self):
        if self.count is None or self.count == self._ffi.NULL:
            return 0

        return self.count[0]

    def __iter__(self):
        for ptr in self._ffi.unpack(self.pointer[0], self.count[0]):
            yield self._obj_cls(self._api_util, ptr)

    def __getitem__(self, idx0) -> DSSObj:
        #TODO: decide if we keep it 0-based or 1-based here
        '''Get element at 0-based index of the batch pointer array'''
        if idx0 >= len(self) or idx0 < 0:
            raise IndexError

        ptr = self.pointer[0][idx0]
        return self._obj_cls(self._api_util, ptr)

    def _set_batch_float64_array(self, idx: int, value: Union[BatchFloat64ArrayProxy, float, List[float], Float64Array]):
        if isinstance(value, (BatchFloat64ArrayProxy, BatchInt32ArrayProxy)):
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
            idx,
            data_ptr
        )


    def _set_batch_int32_array(self, idx: int, value: Union[BatchInt32ArrayProxy, int, List[int], Int32Array]):
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

        data, data_ptr, data_cnt = self._prepare_int32_array(value)
        if data_cnt != self.count[0]:
            raise ValueError("Number of elements must match")

        self._lib.Batch_SetInt32Array(
            self.pointer[0],
            self.count[0],
            idx,
            data_ptr
        )

    def _set_batch_string(self, idx: int, value: Union[AnyStr, List[AnyStr]]):
        if isinstance(value, (bytes, str)):
            if not isinstance(value, bytes):
                value = value.encode(self._api_util.codec)
            self._lib.Batch_SetString(self.pointer[0], self.count[0], idx, value)
            self._check_for_error()
            return

        # Assume it's a list otherwise
        if len(value) != self.count[0]:
            raise ValueError("The number of elements must match the number of elements in the batch.")

        if not len(value):
            value_ptr = self._ffi.NULL
        else:
            value, value_ptr, _ = self._prepare_string_array(value)

        self._lib.Batch_SetStringArray(self.pointer[0], self.count[0], idx, value_ptr)
        self._check_for_error()


    def _set_batch_stringlist_prop(self, idx: int, value: List[AnyStr]):
        '''
        A SINGLE STRING LIST is applied to all objects in the batch for property `idx`
        '''
        if self.count[0] == 0:
            return

        if not len(value):
            value_ptr, value_count = self._ffi.NULL, 0
        else:
            value, value_ptr, value_count = self._prepare_string_array(value)

        for x in self._ffi.unpack(self.pointer[0], self.count[0]):
            self._lib.Obj_SetStringArray(x, idx, value_ptr, value_count)

        self._check_for_error()


    def _set_batch_float64_array_prop(self, idx: int, value: Union[Float64Array, None]):
        '''
        Set values to a FLOAT64 ARRAY property `idx`
        '''
        if self.count[0] == 0:
            return
        
        if isinstance(value, (BatchFloat64ArrayProxy, BatchInt32ArrayProxy)):
            value = value.to_array()
        
        # Assume 2-d values at first
        single_array = False

        # Empty arrays or None
        if not len(value) or value is None:
            value_ptr, value_count = self._ffi.NULL, 0
            single_array = True
        
        # Lists of values, 1-d series, or 1-d array
        elif (isinstance(value, LIST_LIKE) and np.isscalar(value[0])) or (isinstance(value, np.ndarray) and len(value.shape) == 1):
            value, value_ptr, value_count = self._prepare_float64_array(value)
            single_array = True


        if single_array:
            # Apply the same array for all objects in the batch
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetFloat64Array(x, idx, value_ptr, value_count)
        else:
            # Apply one array for each object
            value_2d = value
            for x, value in zip(self._ffi.unpack(self.pointer[0], self.count[0]), value_2d):
                if not len(value) or value is None:
                    value_ptr, value_count = self._ffi.NULL, 0
                else:
                    value, value_ptr, value_count = self._prepare_float64_array(value)

                self._lib.Obj_SetFloat64Array(x, idx, value_ptr, value_count)

        self._check_for_error()


    def _set_batch_int32_array_prop(self, idx: int, value: Union[Int32Array, None]):
        '''
        Set values to an INT32 ARRAY property `idx`
        '''
        if self.count[0] == 0:
            return
        
        if isinstance(value, (BatchFloat64ArrayProxy, BatchInt32ArrayProxy)):
            value = value.to_array()
        
        # Assume 2-d values at first
        single_array = False

        # Empty arrays or None
        if not len(value) or value is None:
            value_ptr, value_count = self._ffi.NULL, 0
            single_array = True
        
        # Lists of values, 1-d series, or 1-d array
        elif (isinstance(value, LIST_LIKE) and np.isscalar(value[0])) or (isinstance(value, np.ndarray) and len(value.shape) == 1):
            value, value_ptr, value_count = self._prepare_int32_array(value)
            single_array = True

        if single_array:
            # Apply the same array for all objects in the batch
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetInt32Array(x, idx, value_ptr, value_count)
        else:
            # Apply one array for each object
            value_2d = value
            for x, value in zip(self._ffi.unpack(self.pointer[0], self.count[0]), value_2d):
                if not len(value) or value is None:
                    value_ptr, value_count = self._ffi.NULL, 0
                else:
                    value, value_ptr, value_count = self._prepare_int32_array(value)

                self._lib.Obj_SetInt32Array(x, idx, value_ptr, value_count)

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


    def _get_obj_ll(self, idx: int, pycls):
        if self.count[0] == 0:
            return []

        obj = self._obj_cls(self._api_util, self.pointer[0])
        res = []
        for ptr in self._ffi.unpack(self.pointer[0], self.count[0]):
            obj._ptr = ptr
            res.append(obj._get_obj_array(idx, pycls))

        return res

    def _set_batch_obj_prop(self, idx: int, other: Optional[Union[DSSObj, List[DSSObj]]]):
        if self.count[0] == 0:
            return

        if other is None or (isinstance(other, LIST_LIKE) and len(other) == 0):
            # Set each object to empty
            self._lib.Batch_SetObject(self.pointer[0], self.count[0], idx, self._ffi.NULL)
            self._check_for_error()
            return

        if other is not None or isinstance(other, (bytes, str)) or (isinstance(other, LIST_LIKE) and len(other) and isinstance(other[0], (bytes, str))):
            self._set_batch_string(idx, other)
            return

        if isinstance(other, DSSObj):
            self._lib.Batch_SetObject(self.pointer[0], self.count[0], idx, other._ptr)
            self._check_for_error()
            return

        # Assume it's a list otherwise
        if len(other) != self.count[0]:
            raise ValueError("The number of elements must match the number of elements in the batch.")

        other_ptr = self._ffi.new('void*[]', len(other))
        other_ptr[:] = [o._ptr if o is not None else self._ffi.NULL for o in other]
        other_cnt = len(other)
        self._lib.Batch_SetObjectArray(self.pointer[0], self.count[0], idx, other_ptr)
        self._check_for_error()


    def _set_batch_objlist_prop(self, idx: int, other: List[DSSObj]):
        if self.count[0] == 0:
            return

        if other is None or (isinstance(other, LIST_LIKE) and len(other) == 0):
            other_ptr = self._ffi.NULL
            other_cnt = 0
        else:
            other_ptr = self._ffi.new('void*[]', len(other))
            other_ptr[:] = [o._ptr if o is not None else self._ffi.NULL for o in other]
            other_cnt = len(other)

        for ptr in self._ffi.unpack(self.pointer[0], self.count[0]):
            self._lib.Obj_SetObjectArray(ptr, idx, other_ptr, other_cnt)

        self._check_for_error()

        # if len(other) != self.count[0]:
        #     raise ValueError("Number of element in the list must match the number of elements in the batch.")
        # obj = self._obj_cls(self._api_util, self.pointer[0])
        # for other_objs, ptr in zip(other, self._ffi.unpack(self.pointer[0], self.count[0])):
        #     # this could be further optimized to reuse the pointers, but it's 
        #     # not usually in the hot path
        #     obj._ptr = ptr
        #     obj._set_obj_array(idx, other_objs)



class IDSSObj(Base):
    def __init__(self, iobj, obj_cls, batch_cls):
        Base.__init__(self, iobj._api_util)
        self._iobj = iobj
        self.cls_idx = obj_cls._cls_idx
        self._obj_cls = obj_cls
        self._batch_cls = batch_cls
        DSSObj._idx_to_cls[self.cls_idx] = obj_cls

    def batch(self, **kwargs):
        '''
        Creates a new batch handler of (existing) objects
        '''
        return self._batch_cls(self._api_util, **kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, count: Optional[int] = None, begin_edit=True):
        '''
        Creates a new batch handler of new objects, with the specified names, 
        or "count" elements with a randomized prefix.
        '''
        if names is not None:
            if count is not None:
                raise ValueError("Provide either names or count, not both")

            return self._batch_cls(self._api_util, new_names=names, begin_edit=begin_edit)

        if count is not None:
            return self._batch_cls(self._api_util, new_count=count, begin_edit=begin_edit)

        raise ValueError("Provide either names or count to create a new batch")


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
