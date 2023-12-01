# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from typing_extensions import TypedDict, Unpack
from .types import Float64Array, Int32Array
from . import enums
from .DSSObj import IDSSObj, DSSObj
from .Batch import DSSBatch
from .ArrayProxy import BatchInt32ArrayProxy
from .common import LIST_LIKE

class LineSpacing(DSSObj):
    __slots__ = DSSObj._extra_slots
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


    def _get_NConds(self) -> int:
        """
        Number of wires in this geometry. Default is 3. Triggers memory allocations. Define first!

        DSS property name: `NConds`, DSS property index: 1.
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    def _set_NConds(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 1, value, flags)

    NConds = property(_get_NConds, _set_NConds) # type: int

    def _get_NPhases(self) -> int:
        """
        Number of retained phase conductors. If less than the number of wires, list the retained phase coordinates first.

        DSS property name: `NPhases`, DSS property index: 2.
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    def _set_NPhases(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 2, value, flags)

    NPhases = property(_get_NPhases, _set_NPhases) # type: int

    def _get_X(self) -> Float64Array:
        """
        Array of wire X coordinates.

        DSS property name: `X`, DSS property index: 3.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 3)

    def _set_X(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(3, value, flags)

    X = property(_get_X, _set_X) # type: Float64Array

    def _get_H(self) -> Float64Array:
        """
        Array of wire Heights.

        DSS property name: `H`, DSS property index: 4.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 4)

    def _set_H(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(4, value, flags)

    H = property(_get_H, _set_H) # type: Float64Array

    def _get_Units(self) -> enums.LengthUnit:
        """
        Units for x and h: {mi|kft|km|m|Ft|in|cm } Initial default is "ft", but defaults to last unit defined

        DSS property name: `Units`, DSS property index: 5.
        """
        return enums.LengthUnit(self._lib.Obj_GetInt32(self._ptr, 5))

    def _set_Units(self, value: Union[AnyStr, int, enums.LengthUnit], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(5, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 5, value, flags)

    Units = property(_get_Units, _set_Units) # type: enums.LengthUnit

    def _get_Units_str(self) -> str:
        """
        Units for x and h: {mi|kft|km|m|Ft|in|cm } Initial default is "ft", but defaults to last unit defined

        DSS property name: `Units`, DSS property index: 5.
        """
        return self._get_prop_string(5)

    def _set_Units_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Units(value, flags)

    Units_str = property(_get_Units_str, _set_Units_str) # type: str

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 6.
        """
        self._set_string_o(6, value)


class LineSpacingProperties(TypedDict):
    NConds: int
    NPhases: int
    X: Float64Array
    H: Float64Array
    Units: Union[AnyStr, int, enums.LengthUnit]
    Like: AnyStr

class LineSpacingBatch(DSSBatch):
    _cls_name = 'LineSpacing'
    _obj_cls = LineSpacing
    _cls_idx = 12


    def _get_NConds(self) -> BatchInt32ArrayProxy:
        """
        Number of wires in this geometry. Default is 3. Triggers memory allocations. Define first!

        DSS property name: `NConds`, DSS property index: 1.
        """
        return BatchInt32ArrayProxy(self, 1)

    def _set_NConds(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(1, value, flags)

    NConds = property(_get_NConds, _set_NConds) # type: BatchInt32ArrayProxy

    def _get_NPhases(self) -> BatchInt32ArrayProxy:
        """
        Number of retained phase conductors. If less than the number of wires, list the retained phase coordinates first.

        DSS property name: `NPhases`, DSS property index: 2.
        """
        return BatchInt32ArrayProxy(self, 2)

    def _set_NPhases(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(2, value, flags)

    NPhases = property(_get_NPhases, _set_NPhases) # type: BatchInt32ArrayProxy

    def _get_X(self) -> List[Float64Array]:
        """
        Array of wire X coordinates.

        DSS property name: `X`, DSS property index: 3.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 3)
            for x in self._unpack()
        ]

    def _set_X(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(3, value, flags)

    X = property(_get_X, _set_X) # type: List[Float64Array]

    def _get_H(self) -> List[Float64Array]:
        """
        Array of wire Heights.

        DSS property name: `H`, DSS property index: 4.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 4)
            for x in self._unpack()
        ]

    def _set_H(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(4, value, flags)

    H = property(_get_H, _set_H) # type: List[Float64Array]

    def _get_Units(self) -> BatchInt32ArrayProxy:
        """
        Units for x and h: {mi|kft|km|m|Ft|in|cm } Initial default is "ft", but defaults to last unit defined

        DSS property name: `Units`, DSS property index: 5.
        """
        return BatchInt32ArrayProxy(self, 5)

    def _set_Units(self, value: Union[AnyStr, int, enums.LengthUnit, List[AnyStr], List[int], List[enums.LengthUnit], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(5, value, flags)
            return

        self._set_batch_int32_array(5, value, flags)

    Units = property(_get_Units, _set_Units) # type: BatchInt32ArrayProxy

    def _get_Units_str(self) -> List[str]:
        """
        Units for x and h: {mi|kft|km|m|Ft|in|cm } Initial default is "ft", but defaults to last unit defined

        DSS property name: `Units`, DSS property index: 5.
        """
        return self._get_batch_str_prop(5)

    def _set_Units_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Units(value, flags)

    Units_str = property(_get_Units_str, _set_Units_str) # type: List[str]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 6.
        """
        self._set_batch_string(6, value, flags)

class LineSpacingBatchProperties(TypedDict):
    NConds: Union[int, Int32Array]
    NPhases: Union[int, Int32Array]
    X: Float64Array
    H: Float64Array
    Units: Union[AnyStr, int, enums.LengthUnit, List[AnyStr], List[int], List[enums.LengthUnit], Int32Array]
    Like: AnyStr

class ILineSpacing(IDSSObj, LineSpacingBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, LineSpacing, LineSpacingBatch)
        LineSpacingBatch.__init__(self, self._api_util, sync_cls_idx=LineSpacing._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> LineSpacing:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[LineSpacingProperties]) -> LineSpacing:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[LineSpacingBatchProperties]) -> LineSpacingBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
