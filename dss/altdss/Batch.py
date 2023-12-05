import numpy as np
from typing import Union, List, AnyStr, Optional
from dss.enums import DSSJSONFlags
from .enums import SetterFlags
from .common import Base, LIST_LIKE, InvalidatedObject
from .types import Float64Array, Int32Array
from .DSSObj import DSSObj
from .ArrayProxy import BatchFloat64ArrayProxy, BatchInt32ArrayProxy

class BatchCommon:
    @property
    def Name(self) -> List[str]:
        res = [
            self._ffi.string(self._lib.Obj_GetName(ptr)).decode(self._api_util.codec)
            for ptr in self._unpack()
        ]
        self._check_for_error()
        return res

    def FullName(self) -> List[str]:
        '''Returns the full name (including object type) for all objects in this batch'''

        res = [
            f'{DSSObj._idx_to_cls[self._lib.Obj_GetClassIdx(ptr)]._cls_name}.' + self._ffi.string(self._lib.Obj_GetName(ptr)).decode()
            for ptr in self._unpack()
        ]
        self._check_for_error()
        return res

    def _get_batch_float_func(self, funcname):
        func = self._ffi.addressof(self._api_util.lib_unpatched, funcname)
        res = self._get_float64_array(self._lib.Batch_GetFloat64FromFunc, *self._get_ptr_cnt(), func)
        self._check_for_error()
        return res

    def _get_batch_float64_int32_func(self, funcname, funcArg: int):
        func = self._ffi.addressof(self._api_util.lib_unpatched, funcname)
        res = self._get_float64_array(self._lib.Batch_GetFloat64FromFunc2, *self._get_ptr_cnt(), func, funcArg)
        self._check_for_error()
        return res

    def _get_batch_int32_func(self, funcname):
        func = self._ffi.addressof(self._api_util.lib_unpatched, funcname)
        res = self._get_int32_array(self._lib.Batch_GetInt32FromFunc, *self._get_ptr_cnt(), func)
        self._check_for_error()
        return res

    def _unpack(self):
        return self._ffi.unpack(*self._get_ptr_cnt())

    def _dispose_batch(self, batch_ptr):
        if batch_ptr != self._ffi.NULL:
            self._lib.Batch_Dispose(batch_ptr)

    def _invalidate_ptr(self):
        self._pointer = InvalidatedObject

    def _wrap_ptr(self, ptrptr, countptr):
        if ptrptr != self._ffi.NULL:
            self._pointer = self._ffi.gc(ptrptr[0], self._dispose_batch)
        else:
            self._pointer = self._ffi.NULL

        self._count = countptr[0] if countptr != self._ffi.NULL else 0

    def __eq__(self, other):
        return self is other

    def __len__(self):
        if self._sync_cls_idx:
            return self._lib.Obj_GetCount(self._api_util.ctx, self._sync_cls_idx)

        _, cnt = self._get_ptr_cnt()
        if cnt is None or cnt == self._ffi.NULL:
            return 0

        return cnt
    
    def __call__(self):
        if self._obj_cls is None:
            res = []
            for other_ptr in self._unpack():
                cls_idx = self._lib.Obj_GetClassIdx(other_ptr)
                pycls = DSSObj._idx_to_cls[cls_idx]
                res.append(pycls(self._api_util, other_ptr))
        else:
            res = [
                self._obj_cls(self._api_util, other_ptr)
                for other_ptr in self._unpack()
            ]

        return res

    def to_list(self):
        return self()

    def to_json(self, options: Union[int, DSSJSONFlags] = 0):
        '''
        Returns the data (as a list) of the elements in a batch as a JSON-encoded string.

        The `options` parameter contains bit-flags to toggle specific features.
        See `Obj_ToJSON` (C-API) for more, or `DSSObj.to_json` in Python.

        Additionally, the `ExcludeDisabled` flag can be used to excluded disabled elements from the output.
        '''
        s = self._ffi.gc(self._lib.Batch_ToJSON(*self._get_ptr_cnt(), options), self._lib.DSS_Dispose_String)
        self._check_for_error()
        if s == self._ffi.NULL:
            return '[]'
        
        return self._ffi.string(s).decode(self._api_util.codec)


class DSSBatch(Base, BatchCommon):
    #TODO: keep property name for debugging? Or maybe use from the parent object
    def __init__(self, api_util, **kwargs):
        begin_edit = kwargs.pop('begin_edit', None)
        if begin_edit is None:
            begin_edit = True

        if len(kwargs) > 1:
            raise ValueError('Exactly one argument is expected.')

        self._sync_cls_idx = kwargs.get('sync_cls_idx', False)

        if not self._sync_cls_idx:
            Base.__init__(self, api_util)

        self._ffi = api_util.ffi
        self._ptrptr = ptrptr = self._ffi.new('void***')
        self._countptr = countptr = self._ffi.new('int32_t[4]')

        if len(kwargs) == 0 or (len(kwargs) == 1 and self._sync_cls_idx):
            if not self._sync_cls_idx:
                self._lib.Batch_CreateByClass(ptrptr, countptr, self._cls_idx)
                self._wrap_ptr(ptrptr, countptr)
                # No need to track this kind of batch since it's dynamic
            else:
                self._pointer = self._lib.Obj_GetListPointer(self._api_util.ctx, self._cls_idx)                
                self._count = self._lib.Obj_GetCount(self._api_util.ctx, self._cls_idx)
                api_util.track_batch(self)

            self._check_for_error()
            return

        api_util.track_batch(self)
        from_func = kwargs.get('from_func')
        if from_func is not None:
            func, *func_args = from_func
            func(ptrptr, countptr, *func_args)
            self._wrap_ptr(ptrptr, countptr)
            self._check_for_error()
            return

        new_names = kwargs.get('new_names')
        if new_names is not None:
            names, names_ptr, names_count = self._prepare_string_array(new_names)
            self._lib.Batch_CreateFromNew(ptrptr, countptr, self._cls_idx, names_ptr, names_count, begin_edit)
            self._wrap_ptr(ptrptr, countptr)
            self._check_for_error()
            return

        new_count = kwargs.get('new_count')
        if new_count is not None:
            self._lib.Batch_CreateFromNew(ptrptr, countptr, self._cls_idx, self._ffi.NULL, new_count, begin_edit)
            self._wrap_ptr(ptrptr, countptr)
            self._check_for_error()
            return

        regexp = kwargs.get('re')
        if regexp is not None:
            if not isinstance(regexp, bytes):
                regexp = regexp.encode(self._api_util.codec)

            self._lib.Batch_CreateByRegExp(ptrptr, countptr, self._cls_idx, regexp)
            self._wrap_ptr(ptrptr, countptr)
            self._check_for_error()
            return

        idx = kwargs.get('idx')
        if regexp is not None:
            idx, idx_ptr, idx_cnt = self._prepare_int32_array(idx)
            self._lib.Batch_CreateByIndex(ptrptr, countptr, self._cls_idx, idx_ptr, idx_cnt)
            self._wrap_ptr(ptrptr, countptr)
            self._check_for_error()
            return

        (prop_name, intval), = kwargs.items()
        prop_idx = self._obj_cls._cls_prop_idx.get(prop_name.lower())
        if prop_idx is None:
            raise ValueError('Invalid property name "{}"'.format(prop_name))
        self._lib.Batch_CreateByInt32Property(ptrptr, countptr, self._cls_idx, prop_idx, intval)
        self._wrap_ptr(ptrptr, countptr)
        self._check_for_error()

    def begin_edit(self) -> None:
        '''
        Marks for editing all DSS objects in the batch

        In the editing mode, some final side-effects of changing properties are post-poned
        until `_end_edit` is called. This side-effects can be somewhat costly, like updating
        the model parameters or internal matrices.

        If you don't have any performance constraint, you may edit each property individually
        without worrying about using `begin_edit` and `end_edit`. For convenience, those are
        emitted automatically when editing single properties outside an edit block.
        '''
        self._lib.Batch_BeginEdit(*self._get_ptr_cnt())
        self._check_for_error()

    def end_edit(self, num_changes: int = 1) -> None:
        '''
        Leaves the editing states of all DSS objects in the batch

        `num_changes` is required for a few classes to correctly match the official OpenDSS behavior
        and must be the number of properties modified in the current editing block. As of DSS C-API
        v0.13, this is only required for the Monitor class, when the `Action` property is used with 
        the `Process` value.
        '''
        self._lib.Batch_EndEdit(*self._get_ptr_cnt(), num_changes)
        self._check_for_error()

    def _get_ptr_cnt(self):
        if self._sync_cls_idx:
            self._pointer = self._lib.Obj_GetListPointer(self._api_util.ctx, self._sync_cls_idx)
            self._count = self._lib.Obj_GetCount(self._api_util.ctx, self._sync_cls_idx)

        return (self._pointer, self._count)

    def __iter__(self):
        for ptr in self._unpack():
            yield self._obj_cls(self._api_util, ptr)

    def __getitem__(self, idx0) -> DSSObj:
        #TODO: decide if we keep it 0-based or 1-based here
        '''Get element at 0-based index of the batch pointer array'''
        if idx0 >= len(self) or idx0 < 0:
            raise IndexError

        _pointer, _count = self._get_ptr_cnt()
        ptr = _pointer[idx0]
        return self._obj_cls(self._api_util, ptr)

    def _set_batch_float64_array(self, idx: int, value: Union[BatchFloat64ArrayProxy, float, List[float], Float64Array], flags: SetterFlags = 0):
        if isinstance(value, (BatchFloat64ArrayProxy, BatchInt32ArrayProxy)):
            if self is value._batch and value._idx == idx:
                # ignore if we're setting to property to itself
                return

            value = value.to_array()

        ptr_cnt = self._get_ptr_cnt()
        if np.isscalar(value):
            self._lib.Batch_Float64(
                *ptr_cnt,
                idx,
                self._lib.BatchOperation_Set,
                value,
                flags
            )
            return

        data, data_ptr, data_cnt = self._prepare_float64_array(value)
        if data_cnt != len(self):
            raise ValueError("Number of elements must match")

        self._lib.Batch_SetFloat64Array(
            *ptr_cnt,
            idx,
            data_ptr,
            flags
        )


    def _set_batch_int32_array(self, idx: int, value: Union[BatchInt32ArrayProxy, int, List[int], Int32Array], flags: SetterFlags = 0):
        if isinstance(value, BatchInt32ArrayProxy):
            if self is value._batch and value._idx == idx:
                # ignore if we're setting to property to itself
                return

            value = value.to_array()

        ptr_cnt = self._get_ptr_cnt()
        if np.isscalar(value):
            self._lib.Batch_Int32(
                *ptr_cnt,
                idx,
                self._lib.BatchOperation_Set,
                value,
                flags
            )
            return

        data, data_ptr, data_cnt = self._prepare_int32_array(value)
        if data_cnt != len(self):
            raise ValueError("Number of elements must match")

        self._lib.Batch_SetInt32Array(
            *ptr_cnt,
            idx,
            data_ptr,
            flags
        )

    def _set_batch_string(self, idx: int, value: Union[AnyStr, List[AnyStr]], flags: SetterFlags = 0):
        if isinstance(value, (bytes, str)):
            if not isinstance(value, bytes):
                value = value.encode(self._api_util.codec)
            self._lib.Batch_SetString(*self._get_ptr_cnt(), idx, value, flags)
            self._check_for_error()
            return

        # Assume it's a list otherwise
        if len(value) != len(self):
            raise ValueError("The number of elements must match the number of elements in the batch.")

        if not len(value):
            value_ptr = self._ffi.NULL
        else:
            value, value_ptr, _ = self._prepare_string_array(value)

        self._lib.Batch_SetStringArray(*self._get_ptr_cnt(), idx, value_ptr, flags)
        self._check_for_error()

    def _get_batch_float_prop(self, index):
        return self._get_float64_array(self._lib.Batch_GetFloat64, *self._get_ptr_cnt(), index)

    def _get_batch_int32_prop(self, index):
        return self._get_int32_array(self._lib.Batch_GetInt32, *self._get_ptr_cnt(), index)

    def _get_batch_str_prop(self, index):
        return self._get_string_array(self._lib.Batch_GetString, *self._get_ptr_cnt(), index)

    def _get_batch_obj_prop(self, index, pycls=None):
        ptr = self._ffi.new('void***')
        cnt = self._ffi.new('int32_t[4]')
        self._lib.Batch_GetObject(ptr, cnt, *self._get_ptr_cnt(), index)
        if not cnt[0]:
            self._lib.DSS_Dispose_PPointer(ptr)
            self._check_for_error()
            return []

        # wrap the results with Python classes
        NULL = self._ffi.NULL
        if pycls is None:
            res = []
            for other_ptr in self._ffi.unpack(ptr[0], cnt[0]):
                if other_ptr == NULL:
                    res.append(None)
                    continue
    
                cls_idx = self._lib.Obj_GetClassIdx(other_ptr)
                pycls = DSSObj._idx_to_cls[cls_idx]
                res.append(pycls(self._api_util, other_ptr))
        else:
            res = [
                pycls(self._api_util, other_ptr) if other_ptr != NULL else None
                for other_ptr in self._ffi.unpack(ptr[0], cnt[0])
            ]

        self._lib.DSS_Dispose_PPointer(ptr)
        self._check_for_error()
        return res

    def _set_batch_stringlist_prop(self, idx: int, value: List[AnyStr], flags: SetterFlags = 0):
        '''
        A SINGLE STRING LIST is applied to all objects in the batch for property `idx`
        '''
        if len(self) == 0:
            return

        if not len(value):
            value_ptr, value_count = self._ffi.NULL, 0
        else:
            value, value_ptr, value_count = self._prepare_string_array(value)

        for x in self._unpack():
            self._lib.Obj_SetStringArray(x, idx, value_ptr, value_count, flags)

        self._check_for_error()


    def _set_batch_float64_array_prop(self, idx: int, value: Union[Float64Array, None], flags: SetterFlags = 0):
        '''
        Set values to a FLOAT64 ARRAY property `idx`
        '''
        if len(self) == 0:
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
            for x in self._unpack():
                self._lib.Obj_SetFloat64Array(x, idx, value_ptr, value_count)
        else:
            # Apply one array for each object
            value_2d = value
            for x, value in zip(self._unpack(), value_2d):
                if not len(value) or value is None:
                    value_ptr, value_count = self._ffi.NULL, 0
                else:
                    value, value_ptr, value_count = self._prepare_float64_array(value)

                self._lib.Obj_SetFloat64Array(x, idx, value_ptr, value_count, flags)

        self._check_for_error()


    def _set_batch_int32_array_prop(self, idx: int, value: Union[Int32Array, None], flags: SetterFlags = 0):
        '''
        Set values to an INT32 ARRAY property `idx`
        '''
        if len(self) == 0:
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
            for x in self._unpack():
                self._lib.Obj_SetInt32Array(x, idx, value_ptr, value_count, flags)
        else:
            # Apply one array for each object
            value_2d = value
            for x, value in zip(self._unpack(), value_2d):
                if not len(value) or value is None:
                    value_ptr, value_count = self._ffi.NULL, 0
                else:
                    value, value_ptr, value_count = self._prepare_int32_array(value)

                self._lib.Obj_SetInt32Array(x, idx, value_ptr, value_count, flags)

        self._check_for_error()


    def _get_string_ll(self, idx: int):
        return [
            self._get_string_array(self._lib.Obj_GetStringArray, x, idx)
            for x in self._unpack()
        ]
    
    def _get_string(self, str_ptr) -> str:
        self._check_for_error()
        return self._ffi.string(str_ptr).decode(self._api_util.codec)

    def _get_obj_ll(self, idx: int, pycls):
        if len(self) == 0:
            return []

        _pointer, _ = self._get_ptr_cnt()
        obj = self._obj_cls(self._api_util, _pointer[0])
        res = []
        for ptr in self._unpack():
            obj._ptr = ptr
            res.append(obj._get_obj_array(idx, pycls))

        return res

    def _set_batch_obj_prop(self, idx: int, other: Optional[Union[DSSObj, List[DSSObj]]], flags: SetterFlags = 0):
        if len(self) == 0:
            return

        if other is None or (isinstance(other, LIST_LIKE) and len(other) == 0):
            # Set each object to empty
            self._lib.Batch_SetObject(*self._get_ptr_cnt(), idx, self._ffi.NULL, flags)
            self._check_for_error()
            return

        if other is not None or isinstance(other, (bytes, str)) or (isinstance(other, LIST_LIKE) and len(other) and isinstance(other[0], (bytes, str))):
            self._set_batch_string(idx, other, flags)
            return

        if isinstance(other, DSSObj):
            self._lib.Batch_SetObject(*self._get_ptr_cnt(), idx, other._ptr, flags)
            self._check_for_error()
            return

        # Assume it's a list otherwise
        if len(other) != len(self):
            raise ValueError("The number of elements must match the number of elements in the batch.")

        other_ptr = self._ffi.new('void*[]', len(other))
        other_ptr[:] = [o._ptr if o is not None else self._ffi.NULL for o in other]
        other_cnt = len(other)
        self._lib.Batch_SetObjectArray(*self._get_ptr_cnt(), idx, other_ptr, flags)
        self._check_for_error()


    def _set_batch_objlist_prop(self, idx: int, other: List[DSSObj], flags: SetterFlags = 0):
        if len(self) == 0:
            return

        if other is None or (isinstance(other, LIST_LIKE) and len(other) == 0):
            other_ptr = self._ffi.NULL
            other_cnt = 0
        else:
            other_ptr = self._ffi.new('void*[]', len(other))
            other_ptr[:] = [o._ptr if o is not None else self._ffi.NULL for o in other]
            other_cnt = len(other)

        for ptr in self._unpack():
            self._lib.Obj_SetObjectArray(ptr, idx, other_ptr, other_cnt, flags)

        self._check_for_error()

        # if len(other) != len(self):
        #     raise ValueError("Number of element in the list must match the number of elements in the batch.")
        # obj = self._obj_cls(self._api_util, self._pointer[0])
        # for other_objs, ptr in zip(other, self._unpack()):
        #     # this could be further optimized to reuse the pointers, but it's 
        #     # not usually in the hot path
        #     obj._ptr = ptr
        #     obj._set_obj_array(idx, other_objs)


class NonUniformBatch(Base, BatchCommon):
    '''
    A batch of non-uniform objects.

    Currently, provides:
    - iteration through individual objects
    - access as a list of objects, either through a call statement or `to_list()` function.
    - all basic names as a list of strings
    - all full names (including DSS object type) as a list of strings
    '''

    __slots__ = (
        '_func',
        '_parent_ptr',
        '_ptr',
        '_cnt',
        '_obj_cls',
        '_ffi',
        '_copy_safe',
        '__weakref__',
    )

    def _invalidate_ptr(self):
        self._ptr = InvalidatedObject

    def __init__(self, func, parent, pycls=None, copy_safe=False, sync_cls_idx=None):
        Base.__init__(self, parent._api_util)
        BatchCommon.__init__(self)
        self._ffi = self._api_util.ffi
        self._func = func
        self._parent_ptr = parent._ptr
        self._obj_cls = pycls
        self._ptr = None
        self._cnt = None
        self._copy_safe = copy_safe
        if self._copy_safe:
            self._api_util.track_batch(self)

        if func is None:
            self._sync_cls_idx = sync_cls_idx
        else:
            self._sync_cls_idx = None

    def _dispose_batch(self, batch_ptr):
        if batch_ptr != self._ffi.NULL and batch_ptr[0] != self._ffi.NULL:
            self._lib.Batch_Dispose(batch_ptr[0])

    def _get_ptr_cnt(self):
        if self._sync_cls_idx:
            self._pointer = self._lib.Obj_GetListPointer(self._api_util.ctx, self._sync_cls_idx)
            self._count = self._lib.Obj_GetCount(self._api_util.ctx, self._sync_cls_idx)
            return (self._pointer, self._count)

        if self._copy_safe and self._cnt is not None:
            return (self._ptr[0], self._cnt[0])

        self._ptr = self._ffi.gc(self._ffi.new('void***'), self._dispose_batch)
        self._cnt = self._ffi.new('int32_t[4]')
        self._func(self._ptr, self._cnt, self._parent_ptr)
        return (self._ptr[0], self._cnt[0])

    def __iter__(self):
        ptr, cnt = self._get_ptr_cnt()
        if self._obj_cls is None:
            for idx in range(cnt):
                other_ptr = ptr[idx]
                cls_idx = self._lib.Obj_GetClassIdx(other_ptr)
                pycls = DSSObj._idx_to_cls[cls_idx]
                yield pycls(self._api_util, other_ptr)

            return

        for idx in range(cnt[0]):
            yield self._obj_cls(self._api_util, ptr[idx])


__all__ = ('DSSBatch', 'NonUniformBatch', )
