import numpy as np
from dss.enums import DSSJSONFlags
from .enums import SetterFlags
from .common import Base, LIST_LIKE, InvalidatedObject
from .types import Float64Array, Int32Array
from typing import Union, List, AnyStr, Optional

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
        '__weakref__',
    ]
    _extra_slots = []

    def __init__(self, api_util, ptr):
        Base.__init__(self, api_util)
        self._ptr = ptr
        self._ffi = api_util.ffi
        self._get_int32_list = api_util.get_int32_array2
        api_util.track_obj(self)

    def _invalidate_ptr(self):
        self._ptr = InvalidatedObject

    def __hash__(self):
        return self._ptr.__hash__()

    def __eq__(self, other):
        return self._ptr == getattr(other, '_ptr')

    def __ne__(self, other):
        return self._ptr != getattr(other, '_ptr')

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
        s = self._ffi.gc(self._lib.Obj_ToJSON(self._ptr, options), self._lib.DSS_Dispose_String)
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

        return f'<{self._cls_name}.{self.Name}>'# {" ".join(vals)}'

    @property
    def Name(self) -> str:
        s = self._lib.Obj_GetName(self._ptr)
        self._check_for_error()
        return self._ffi.string(s).decode(self._api_util.codec)

    def FullName(self) -> str:
        return f'{self._cls_name}.{self.Name}'

    def _get_complex(self, idx: int) -> complex:
        return self._get_float64_array(
            self._lib.Obj_GetFloat64Array,
            self._ptr,
            idx
        ).view(complex)[0]

    def _set_complex(self, idx: int, value: complex, flags: SetterFlags = 0):
        data = np.array([complex(value)])
        data, data_ptr, cnt_ptr = self._prepare_float64_array(data.view(dtype=np.float64))
        self._lib.Obj_SetFloat64Array(self._ptr, idx, data_ptr, cnt_ptr, flags)
        self._check_for_error()

    def _get_prop_string(self, idx: int) -> str:
        s = self._lib.Obj_GetString(self._ptr, idx)
        return self._decode_and_free_string(s)

    def _set_string_o(self, idx: int, value: AnyStr, flags: SetterFlags = 0):
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Obj_SetString(self._ptr, idx, value, flags)
        self._check_for_error()

    def _set_float64_array_o(self, idx: int, value: Float64Array, flags: SetterFlags = 0):
        value, value_ptr, value_count = self._prepare_float64_array(value)
        self._lib.Obj_SetFloat64Array(self._ptr, idx, value_ptr, value_count, flags)
        self._check_for_error()

    def _set_int32_array_o(self, idx: int, value: Int32Array, flags: SetterFlags = 0):
        value, value_ptr, value_count = self._prepare_int32_array(value)
        self._lib.Obj_SetInt32Array(self._ptr, idx, value_ptr, value_count, flags)
        self._check_for_error()

    def _set_string_array_o(self, idx: int, value: List[AnyStr], flags: SetterFlags = 0):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, idx, value_ptr, value_count, flags)
        self._check_for_error()

    def _get_obj_from_ptr(self, other_ptr, pycls=None):
        self._check_for_error()
        if other_ptr == self._ffi.NULL:
            return None

        if pycls is None:
            cls_idx = self._lib.Obj_GetClassIdx(other_ptr)
            pycls = DSSObj._idx_to_cls[cls_idx]

        return pycls(self._api_util, other_ptr)

    def _get_obj(self, idx: int, pycls):
        other_ptr = self._lib.Obj_GetObject(self._ptr, idx)
        self._check_for_error()
        if other_ptr == self._ffi.NULL:
            return None

        if pycls is None:
            cls_idx = self._lib.Obj_GetClassIdx(other_ptr)
            pycls = DSSObj._idx_to_cls[cls_idx]

        return pycls(self._api_util, other_ptr)

    def _set_obj(self, idx: int, other, flags: SetterFlags = 0):
        if other is not None:
            other_ptr = other._ptr
        else:
            other_ptr = self._ffi.NULL

        self._lib.Obj_SetObject(self._ptr, idx, other_ptr, flags)
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

    def _get_obj_array_func(self, func, *args, pycls=None):
        ptr = self._ffi.new('void***')
        cnt = self._ffi.new('int32_t[4]')
        func(self._ptr, ptr, cnt, *args)
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


    def _set_obj_array(self, idx: int, other, flags: SetterFlags = 0):
        if other is None or (isinstance(other, LIST_LIKE) and len(other) == 0):
            other_ptr = self._ffi.NULL
            other_cnt = 0
        else:
            other_cnt = len(other)
            other_ptr = self.ffi.new('void*[]', other_cnt)
            other_ptr[:] = [o._ptr for o in other]

        self._lib.Obj_SetObjectArray(self._ptr, idx, other_ptr, other_cnt, flags)
        self._check_for_error()

    def begin_edit(self) -> None:
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

    def end_edit(self, num_changes: int = 1) -> None:
        '''
        Leaves the editing state of a DSS object

        `num_changes` is required for a few classes to correctly match the official OpenDSS behavior
        and must be the number of properties modified in the current editing block. As of DSS C-API
        v0.13, this is only required for the Monitor class, when the `Action` property is used with 
        the `Process` value.
        '''
        self._lib.Obj_EndEdit(self._ptr, num_changes)
        self._check_for_error()


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

    def _batch_new_aux(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, props=None):
        '''
        Aux. function used by the descendant classes (which provide typing info) to create the batches.
        '''
        if df is not None:
            columns = list(df.columns)
            if names is None:
                if 'name' in df.columns:
                    names = df['name'].astype(str)
                    columns.remove('name')
                elif 'names' in df.columns:
                    names = df['names'].astype(str)
                    columns.remove('names')

            batch = IDSSObj.batch_new(self, names=names, begin_edit=True)
            try:
                for k in columns:
                    setattr(batch, k, df[k])
            finally:
                batch.end_edit()

            return batch

        if props:
            # Allow using name instead of names if passing kwargs for pre-filling
            if names is None and count is None and 'name' in props:
                names = props.pop('name')

            batch = IDSSObj.batch_new(self, names=names, count=count, begin_edit=True)
            try:
                for k, v in props.items():
                    setattr(batch, k, v)
            finally:
                batch.end_edit()

            return batch

        return IDSSObj.batch_new(self, names, count, begin_edit)


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


    def _new(self, name: AnyStr, begin_edit=True, activate=False, props=None):
        '''
        Aux. function used by the descendant classes (which provide typing info) to create the objects.
        '''
        if props:
            obj = IDSSObj.new(self, name, True, activate)
            try:
                for k, v in props.items():
                    setattr(obj, k, v)
            finally:
                obj.end_edit()

            return obj

        return IDSSObj.new(self, name, begin_edit, activate)
        

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

    def __contains__(self, name: str) -> bool:
        lib = self._lib
        if type(name) is not bytes:
            name = name.encode(self._api_util.codec)

        return (lib.Obj_GetHandleByName(self._api_util.ctx, self.cls_idx, name) != self._api_util.ffi.NULL)
