# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from typing_extensions import TypedDict, Unpack
from .types import Float64Array, Int32Array
from . import enums
from .DSSObj import IDSSObj, DSSObj
from .Batch import DSSBatch
from .ArrayProxy import BatchFloat64ArrayProxy, BatchInt32ArrayProxy
from .common import LIST_LIKE
from .LineSpacing import LineSpacing
from .WireData import WireData

class LineGeometry(DSSObj):
    __slots__ = DSSObj._extra_slots
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
        'conductors': 12,
        'cncable': 13,
        'tscable': 14,
        'cncables': 15,
        'tscables': 16,
        'seasons': 17,
        'ratings': 18,
        'linetype': 19,
        'like': 20,
    }


    def _get_NConds(self) -> int:
        """
        Number of conductors in this geometry. Default is 3. Triggers memory allocations. Define first!

        DSS property name: `NConds`, DSS property index: 1.
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    def _set_NConds(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 1, value, flags)

    NConds = property(_get_NConds, _set_NConds) # type: int

    def _get_NPhases(self) -> int:
        """
        Number of phases. Default =3; All other conductors are considered neutrals and might be reduced out.

        DSS property name: `NPhases`, DSS property index: 2.
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    def _set_NPhases(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 2, value, flags)

    NPhases = property(_get_NPhases, _set_NPhases) # type: int

    def _get_Wire_str(self) -> List[str]:
        """
        Code from WireData. MUST BE PREVIOUSLY DEFINED. no default.
        Specifies use of Overhead Line parameter calculation,
        Unless Tape Shield cable previously assigned to phases, and this wire is a neutral.

        DSS property name: `Wire`, DSS property index: 4.
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 4)

    def _set_Wire_str(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        self._set_string_array_o(4, value, flags)

    Wire_str = property(_get_Wire_str, _set_Wire_str) # type: List[str]

    def _get_Wire(self) -> List[WireData]:
        """
        Code from WireData. MUST BE PREVIOUSLY DEFINED. no default.
        Specifies use of Overhead Line parameter calculation,
        Unless Tape Shield cable previously assigned to phases, and this wire is a neutral.

        DSS property name: `Wire`, DSS property index: 4.
        """
        return self._get_obj_array(4, WireData)

    def _set_Wire(self, value: List[Union[AnyStr, WireData]], flags: enums.SetterFlags = 0):
        if value is None or len(value) == 0 or not isinstance(value[0], DSSObj):
            self._set_string_array_o(4, value, flags)
            return

        self._set_obj_array(4, value, flags)

    Wire = property(_get_Wire, _set_Wire) # type: List[WireData]

    def _get_X(self) -> Float64Array:
        """
        x coordinate.

        DSS property name: `X`, DSS property index: 5.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 5)

    def _set_X(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(5, value, flags)

    X = property(_get_X, _set_X) # type: Float64Array

    def _get_H(self) -> Float64Array:
        """
        Height of conductor.

        DSS property name: `H`, DSS property index: 6.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 6)

    def _set_H(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(6, value, flags)

    H = property(_get_H, _set_H) # type: Float64Array

    def _get_Units(self) -> enums.LengthUnit:
        """
        Units for x and h: {mi|kft|km|m|Ft|in|cm } Initial default is "ft", but defaults to last unit defined

        DSS property name: `Units`, DSS property index: 7.
        """
        return enums.LengthUnit(self._lib.Obj_GetInt32(self._ptr, 7))

    def _set_Units(self, value: Union[AnyStr, int, enums.LengthUnit], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(7, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 7, value, flags)

    Units = property(_get_Units, _set_Units) # type: enums.LengthUnit

    def _get_Units_str(self) -> str:
        """
        Units for x and h: {mi|kft|km|m|Ft|in|cm } Initial default is "ft", but defaults to last unit defined

        DSS property name: `Units`, DSS property index: 7.
        """
        return self._get_prop_string(7)

    def _set_Units_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Units(value, flags)

    Units_str = property(_get_Units_str, _set_Units_str) # type: str

    def _get_NormAmps(self) -> float:
        """
        Normal ampacity, amperes for the line. Defaults to first conductor if not specified.

        DSS property name: `NormAmps`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    def _set_NormAmps(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 8, value, flags)

    NormAmps = property(_get_NormAmps, _set_NormAmps) # type: float

    def _get_EmergAmps(self) -> float:
        """
        Emergency ampacity, amperes. Defaults to first conductor if not specified.

        DSS property name: `EmergAmps`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    def _set_EmergAmps(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 9, value, flags)

    EmergAmps = property(_get_EmergAmps, _set_EmergAmps) # type: float

    def _get_Reduce(self) -> bool:
        """
        {Yes | No} Default = no. Reduce to Nphases (Kron Reduction). Reduce out neutrals.

        DSS property name: `Reduce`, DSS property index: 10.
        """
        return self._lib.Obj_GetInt32(self._ptr, 10) != 0

    def _set_Reduce(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 10, value, flags)

    Reduce = property(_get_Reduce, _set_Reduce) # type: bool

    def _get_Spacing_str(self) -> str:
        """
        Reference to a LineSpacing for use in a line constants calculation.
        Alternative to x, h, and units. MUST BE PREVIOUSLY DEFINED.
        Must match "nconds" as previously defined for this geometry.
        Must be used in conjunction with the Wires property.

        DSS property name: `Spacing`, DSS property index: 11.
        """
        return self._get_prop_string(11)

    def _set_Spacing_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(11, value, flags)

    Spacing_str = property(_get_Spacing_str, _set_Spacing_str) # type: str

    def _get_Spacing(self) -> LineSpacing:
        """
        Reference to a LineSpacing for use in a line constants calculation.
        Alternative to x, h, and units. MUST BE PREVIOUSLY DEFINED.
        Must match "nconds" as previously defined for this geometry.
        Must be used in conjunction with the Wires property.

        DSS property name: `Spacing`, DSS property index: 11.
        """
        return self._get_obj(11, LineSpacing)

    def _set_Spacing(self, value: Union[AnyStr, LineSpacing], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(11, value, flags)
            return

        self._set_string_o(11, value, flags)

    Spacing = property(_get_Spacing, _set_Spacing) # type: LineSpacing

    def _get_Seasons(self) -> int:
        """
        Defines the number of ratings to be defined for the wire, to be used only when defining seasonal ratings using the "Ratings" property. Defaults to first conductor if not specified.

        DSS property name: `Seasons`, DSS property index: 17.
        """
        return self._lib.Obj_GetInt32(self._ptr, 17)

    def _set_Seasons(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 17, value, flags)

    Seasons = property(_get_Seasons, _set_Seasons) # type: int

    def _get_Ratings(self) -> Float64Array:
        """
        An array of ratings to be used when the seasonal ratings flag is True. It can be used to insert
        multiple ratings to change during a QSTS simulation to evaluate different ratings in lines.Defaults to first conductor if not specified.

        DSS property name: `Ratings`, DSS property index: 18.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 18)

    def _set_Ratings(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(18, value, flags)

    Ratings = property(_get_Ratings, _set_Ratings) # type: Float64Array

    def _get_LineType(self) -> enums.LineType:
        """
        Code designating the type of line. 
        One of: OH, UG, UG_TS, UG_CN, SWT_LDBRK, SWT_FUSE, SWT_SECT, SWT_REC, SWT_DISC, SWT_BRK, SWT_ELBOW, BUSBAR

        OpenDSS currently does not use this internally. For whatever purpose the user defines. Default is OH.

        DSS property name: `LineType`, DSS property index: 19.
        """
        return enums.LineType(self._lib.Obj_GetInt32(self._ptr, 19))

    def _set_LineType(self, value: Union[AnyStr, int, enums.LineType], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(19, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 19, value, flags)

    LineType = property(_get_LineType, _set_LineType) # type: enums.LineType

    def _get_LineType_str(self) -> str:
        """
        Code designating the type of line. 
        One of: OH, UG, UG_TS, UG_CN, SWT_LDBRK, SWT_FUSE, SWT_SECT, SWT_REC, SWT_DISC, SWT_BRK, SWT_ELBOW, BUSBAR

        OpenDSS currently does not use this internally. For whatever purpose the user defines. Default is OH.

        DSS property name: `LineType`, DSS property index: 19.
        """
        return self._get_prop_string(19)

    def _set_LineType_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_LineType(value, flags)

    LineType_str = property(_get_LineType_str, _set_LineType_str) # type: str

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 20.
        """
        self._set_string_o(20, value)


class LineGeometryProperties(TypedDict):
    NConds: int
    NPhases: int
    Wire: List[Union[AnyStr, WireData]]
    X: Float64Array
    H: Float64Array
    Units: Union[AnyStr, int, enums.LengthUnit]
    NormAmps: float
    EmergAmps: float
    Reduce: bool
    Spacing: Union[AnyStr, LineSpacing]
    Seasons: int
    Ratings: Float64Array
    LineType: Union[AnyStr, int, enums.LineType]
    Like: AnyStr

class LineGeometryBatch(DSSBatch):
    _cls_name = 'LineGeometry'
    _obj_cls = LineGeometry
    _cls_idx = 13


    def _get_NConds(self) -> BatchInt32ArrayProxy:
        """
        Number of conductors in this geometry. Default is 3. Triggers memory allocations. Define first!

        DSS property name: `NConds`, DSS property index: 1.
        """
        return BatchInt32ArrayProxy(self, 1)

    def _set_NConds(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(1, value, flags)

    NConds = property(_get_NConds, _set_NConds) # type: BatchInt32ArrayProxy

    def _get_NPhases(self) -> BatchInt32ArrayProxy:
        """
        Number of phases. Default =3; All other conductors are considered neutrals and might be reduced out.

        DSS property name: `NPhases`, DSS property index: 2.
        """
        return BatchInt32ArrayProxy(self, 2)

    def _set_NPhases(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(2, value, flags)

    NPhases = property(_get_NPhases, _set_NPhases) # type: BatchInt32ArrayProxy

    def _get_Wire_str(self) -> List[List[str]]:
        """
        Code from WireData. MUST BE PREVIOUSLY DEFINED. no default.
        Specifies use of Overhead Line parameter calculation,
        Unless Tape Shield cable previously assigned to phases, and this wire is a neutral.

        DSS property name: `Wire`, DSS property index: 4.
        """
        return self._get_string_ll(4)

    def _set_Wire_str(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        self._set_batch_stringlist_prop(4, value, flags)

    Wire_str = property(_get_Wire_str, _set_Wire_str) # type: List[List[str]]

    def _get_Wire(self) -> List[List[WireData]]:
        """
        Code from WireData. MUST BE PREVIOUSLY DEFINED. no default.
        Specifies use of Overhead Line parameter calculation,
        Unless Tape Shield cable previously assigned to phases, and this wire is a neutral.

        DSS property name: `Wire`, DSS property index: 4.
        """
        return self._get_obj_ll(4, WireData)

    def _set_Wire(self, value: Union[List[AnyStr], List[WireData]], flags: enums.SetterFlags = 0):
        if (not len(value)) or isinstance(value[0], (bytes, str)) or (len(value[0]) and isinstance(value[0][0], (bytes, str))):
            self._set_batch_stringlist_prop(4, value, flags)
            return

        self._set_batch_objlist_prop(4, value, flags)

    Wire = property(_get_Wire, _set_Wire) # type: List[List[WireData]]

    def _get_X(self) -> List[Float64Array]:
        """
        x coordinate.

        DSS property name: `X`, DSS property index: 5.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 5)
            for x in self._unpack()
        ]

    def _set_X(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(5, value, flags)

    X = property(_get_X, _set_X) # type: List[Float64Array]

    def _get_H(self) -> List[Float64Array]:
        """
        Height of conductor.

        DSS property name: `H`, DSS property index: 6.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 6)
            for x in self._unpack()
        ]

    def _set_H(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(6, value, flags)

    H = property(_get_H, _set_H) # type: List[Float64Array]

    def _get_Units(self) -> BatchInt32ArrayProxy:
        """
        Units for x and h: {mi|kft|km|m|Ft|in|cm } Initial default is "ft", but defaults to last unit defined

        DSS property name: `Units`, DSS property index: 7.
        """
        return BatchInt32ArrayProxy(self, 7)

    def _set_Units(self, value: Union[AnyStr, int, enums.LengthUnit, List[AnyStr], List[int], List[enums.LengthUnit], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(7, value, flags)
            return

        self._set_batch_int32_array(7, value, flags)

    Units = property(_get_Units, _set_Units) # type: BatchInt32ArrayProxy

    def _get_Units_str(self) -> List[str]:
        """
        Units for x and h: {mi|kft|km|m|Ft|in|cm } Initial default is "ft", but defaults to last unit defined

        DSS property name: `Units`, DSS property index: 7.
        """
        return self._get_batch_str_prop(7)

    def _set_Units_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Units(value, flags)

    Units_str = property(_get_Units_str, _set_Units_str) # type: List[str]

    def _get_NormAmps(self) -> BatchFloat64ArrayProxy:
        """
        Normal ampacity, amperes for the line. Defaults to first conductor if not specified.

        DSS property name: `NormAmps`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    def _set_NormAmps(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(8, value, flags)

    NormAmps = property(_get_NormAmps, _set_NormAmps) # type: BatchFloat64ArrayProxy

    def _get_EmergAmps(self) -> BatchFloat64ArrayProxy:
        """
        Emergency ampacity, amperes. Defaults to first conductor if not specified.

        DSS property name: `EmergAmps`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    def _set_EmergAmps(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(9, value, flags)

    EmergAmps = property(_get_EmergAmps, _set_EmergAmps) # type: BatchFloat64ArrayProxy

    def _get_Reduce(self) -> List[bool]:
        """
        {Yes | No} Default = no. Reduce to Nphases (Kron Reduction). Reduce out neutrals.

        DSS property name: `Reduce`, DSS property index: 10.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(10)
        ]

    def _set_Reduce(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(10, value, flags)

    Reduce = property(_get_Reduce, _set_Reduce) # type: List[bool]

    def _get_Spacing_str(self) -> List[str]:
        """
        Reference to a LineSpacing for use in a line constants calculation.
        Alternative to x, h, and units. MUST BE PREVIOUSLY DEFINED.
        Must match "nconds" as previously defined for this geometry.
        Must be used in conjunction with the Wires property.

        DSS property name: `Spacing`, DSS property index: 11.
        """
        return self._get_batch_str_prop(11)

    def _set_Spacing_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(11, value, flags)

    Spacing_str = property(_get_Spacing_str, _set_Spacing_str) # type: List[str]

    def _get_Spacing(self) -> List[LineSpacing]:
        """
        Reference to a LineSpacing for use in a line constants calculation.
        Alternative to x, h, and units. MUST BE PREVIOUSLY DEFINED.
        Must match "nconds" as previously defined for this geometry.
        Must be used in conjunction with the Wires property.

        DSS property name: `Spacing`, DSS property index: 11.
        """
        return self._get_batch_obj_prop(11)

    def _set_Spacing(self, value: Union[AnyStr, LineSpacing, List[AnyStr], List[LineSpacing]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(11, value, flags)

    Spacing = property(_get_Spacing, _set_Spacing) # type: List[LineSpacing]

    def _get_Seasons(self) -> BatchInt32ArrayProxy:
        """
        Defines the number of ratings to be defined for the wire, to be used only when defining seasonal ratings using the "Ratings" property. Defaults to first conductor if not specified.

        DSS property name: `Seasons`, DSS property index: 17.
        """
        return BatchInt32ArrayProxy(self, 17)

    def _set_Seasons(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(17, value, flags)

    Seasons = property(_get_Seasons, _set_Seasons) # type: BatchInt32ArrayProxy

    def _get_Ratings(self) -> List[Float64Array]:
        """
        An array of ratings to be used when the seasonal ratings flag is True. It can be used to insert
        multiple ratings to change during a QSTS simulation to evaluate different ratings in lines.Defaults to first conductor if not specified.

        DSS property name: `Ratings`, DSS property index: 18.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 18)
            for x in self._unpack()
        ]

    def _set_Ratings(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(18, value, flags)

    Ratings = property(_get_Ratings, _set_Ratings) # type: List[Float64Array]

    def _get_LineType(self) -> BatchInt32ArrayProxy:
        """
        Code designating the type of line. 
        One of: OH, UG, UG_TS, UG_CN, SWT_LDBRK, SWT_FUSE, SWT_SECT, SWT_REC, SWT_DISC, SWT_BRK, SWT_ELBOW, BUSBAR

        OpenDSS currently does not use this internally. For whatever purpose the user defines. Default is OH.

        DSS property name: `LineType`, DSS property index: 19.
        """
        return BatchInt32ArrayProxy(self, 19)

    def _set_LineType(self, value: Union[AnyStr, int, enums.LineType, List[AnyStr], List[int], List[enums.LineType], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(19, value, flags)
            return

        self._set_batch_int32_array(19, value, flags)

    LineType = property(_get_LineType, _set_LineType) # type: BatchInt32ArrayProxy

    def _get_LineType_str(self) -> List[str]:
        """
        Code designating the type of line. 
        One of: OH, UG, UG_TS, UG_CN, SWT_LDBRK, SWT_FUSE, SWT_SECT, SWT_REC, SWT_DISC, SWT_BRK, SWT_ELBOW, BUSBAR

        OpenDSS currently does not use this internally. For whatever purpose the user defines. Default is OH.

        DSS property name: `LineType`, DSS property index: 19.
        """
        return self._get_batch_str_prop(19)

    def _set_LineType_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_LineType(value, flags)

    LineType_str = property(_get_LineType_str, _set_LineType_str) # type: List[str]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 20.
        """
        self._set_batch_string(20, value, flags)

class LineGeometryBatchProperties(TypedDict):
    NConds: Union[int, Int32Array]
    NPhases: Union[int, Int32Array]
    Wire: Union[List[AnyStr], List[WireData]]
    X: Float64Array
    H: Float64Array
    Units: Union[AnyStr, int, enums.LengthUnit, List[AnyStr], List[int], List[enums.LengthUnit], Int32Array]
    NormAmps: Union[float, Float64Array]
    EmergAmps: Union[float, Float64Array]
    Reduce: bool
    Spacing: Union[AnyStr, LineSpacing, List[AnyStr], List[LineSpacing]]
    Seasons: Union[int, Int32Array]
    Ratings: Float64Array
    LineType: Union[AnyStr, int, enums.LineType, List[AnyStr], List[int], List[enums.LineType], Int32Array]
    Like: AnyStr

class ILineGeometry(IDSSObj, LineGeometryBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, LineGeometry, LineGeometryBatch)
        LineGeometryBatch.__init__(self, self._api_util, sync_cls_idx=LineGeometry._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> LineGeometry:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[LineGeometryProperties]) -> LineGeometry:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[LineGeometryBatchProperties]) -> LineGeometryBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
