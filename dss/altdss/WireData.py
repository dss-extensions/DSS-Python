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

class WireData(DSSObj):
    __slots__ = DSSObj._extra_slots
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


    def _get_RDC(self) -> float:
        """
        dc Resistance, ohms per unit length (see Runits). Defaults to Rac/1.02 if not specified.

        DSS property name: `RDC`, DSS property index: 1.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 1)

    def _set_RDC(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 1, value, flags)

    RDC = property(_get_RDC, _set_RDC) # type: float

    def _get_RAC(self) -> float:
        """
        Resistance at 60 Hz per unit length. Defaults to 1.02*Rdc if not specified.

        DSS property name: `RAC`, DSS property index: 2.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 2)

    def _set_RAC(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 2, value, flags)

    RAC = property(_get_RAC, _set_RAC) # type: float

    def _get_RUnits(self) -> enums.LengthUnit:
        """
        Length units for resistance: ohms per {mi|kft|km|m|Ft|in|cm|mm} Default=none.

        DSS property name: `RUnits`, DSS property index: 3.
        """
        return enums.LengthUnit(self._lib.Obj_GetInt32(self._ptr, 3))

    def _set_RUnits(self, value: Union[AnyStr, int, enums.LengthUnit], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(3, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 3, value, flags)

    RUnits = property(_get_RUnits, _set_RUnits) # type: enums.LengthUnit

    def _get_RUnits_str(self) -> str:
        """
        Length units for resistance: ohms per {mi|kft|km|m|Ft|in|cm|mm} Default=none.

        DSS property name: `RUnits`, DSS property index: 3.
        """
        return self._get_prop_string(3)

    def _set_RUnits_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_RUnits(value, flags)

    RUnits_str = property(_get_RUnits_str, _set_RUnits_str) # type: str

    def _get_GMRAC(self) -> float:
        """
        GMR at 60 Hz. Defaults to .7788*radius if not specified.

        DSS property name: `GMRAC`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    def _set_GMRAC(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 4, value, flags)

    GMRAC = property(_get_GMRAC, _set_GMRAC) # type: float

    def _get_GMRUnits(self) -> enums.LengthUnit:
        """
        Units for GMR: {mi|kft|km|m|Ft|in|cm|mm} Default=none.

        DSS property name: `GMRUnits`, DSS property index: 5.
        """
        return enums.LengthUnit(self._lib.Obj_GetInt32(self._ptr, 5))

    def _set_GMRUnits(self, value: Union[AnyStr, int, enums.LengthUnit], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(5, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 5, value, flags)

    GMRUnits = property(_get_GMRUnits, _set_GMRUnits) # type: enums.LengthUnit

    def _get_GMRUnits_str(self) -> str:
        """
        Units for GMR: {mi|kft|km|m|Ft|in|cm|mm} Default=none.

        DSS property name: `GMRUnits`, DSS property index: 5.
        """
        return self._get_prop_string(5)

    def _set_GMRUnits_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_GMRUnits(value, flags)

    GMRUnits_str = property(_get_GMRUnits_str, _set_GMRUnits_str) # type: str

    def _get_Radius(self) -> float:
        """
        Outside radius of conductor. Defaults to GMR/0.7788 if not specified.

        DSS property name: `Radius`, DSS property index: 6.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    def _set_Radius(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 6, value, flags)

    Radius = property(_get_Radius, _set_Radius) # type: float

    def _get_RadUnits(self) -> enums.LengthUnit:
        """
        Units for outside radius: {mi|kft|km|m|Ft|in|cm|mm} Default=none.

        DSS property name: `RadUnits`, DSS property index: 7.
        """
        return enums.LengthUnit(self._lib.Obj_GetInt32(self._ptr, 7))

    def _set_RadUnits(self, value: Union[AnyStr, int, enums.LengthUnit], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(7, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 7, value, flags)

    RadUnits = property(_get_RadUnits, _set_RadUnits) # type: enums.LengthUnit

    def _get_RadUnits_str(self) -> str:
        """
        Units for outside radius: {mi|kft|km|m|Ft|in|cm|mm} Default=none.

        DSS property name: `RadUnits`, DSS property index: 7.
        """
        return self._get_prop_string(7)

    def _set_RadUnits_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_RadUnits(value, flags)

    RadUnits_str = property(_get_RadUnits_str, _set_RadUnits_str) # type: str

    def _get_NormAmps(self) -> float:
        """
        Normal ampacity, amperes. Defaults to Emergency amps/1.5 if not specified.

        DSS property name: `NormAmps`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    def _set_NormAmps(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 8, value, flags)

    NormAmps = property(_get_NormAmps, _set_NormAmps) # type: float

    def _get_EmergAmps(self) -> float:
        """
        Emergency ampacity, amperes. Defaults to 1.5 * Normal Amps if not specified.

        DSS property name: `EmergAmps`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    def _set_EmergAmps(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 9, value, flags)

    EmergAmps = property(_get_EmergAmps, _set_EmergAmps) # type: float

    def _get_Diam(self) -> float:
        """
        Diameter; Alternative method for entering radius.

        DSS property name: `Diam`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    def _set_Diam(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 10, value, flags)

    Diam = property(_get_Diam, _set_Diam) # type: float

    def _get_Seasons(self) -> int:
        """
        Defines the number of ratings to be defined for the wire, to be used only when defining seasonal ratings using the "Ratings" property.

        DSS property name: `Seasons`, DSS property index: 11.
        """
        return self._lib.Obj_GetInt32(self._ptr, 11)

    def _set_Seasons(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 11, value, flags)

    Seasons = property(_get_Seasons, _set_Seasons) # type: int

    def _get_Ratings(self) -> Float64Array:
        """
        An array of ratings to be used when the seasonal ratings flag is True. It can be used to insert
        multiple ratings to change during a QSTS simulation to evaluate different ratings in lines.

        DSS property name: `Ratings`, DSS property index: 12.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 12)

    def _set_Ratings(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(12, value, flags)

    Ratings = property(_get_Ratings, _set_Ratings) # type: Float64Array

    def _get_CapRadius(self) -> float:
        """
        Equivalent conductor radius for capacitance calcs. Specify this for bundled conductors. Defaults to same value as radius. Define Diam or Radius property first.

        DSS property name: `CapRadius`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    def _set_CapRadius(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 13, value, flags)

    CapRadius = property(_get_CapRadius, _set_CapRadius) # type: float

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 14.
        """
        self._set_string_o(14, value)


class WireDataProperties(TypedDict):
    RDC: float
    RAC: float
    RUnits: Union[AnyStr, int, enums.LengthUnit]
    GMRAC: float
    GMRUnits: Union[AnyStr, int, enums.LengthUnit]
    Radius: float
    RadUnits: Union[AnyStr, int, enums.LengthUnit]
    NormAmps: float
    EmergAmps: float
    Diam: float
    Seasons: int
    Ratings: Float64Array
    CapRadius: float
    Like: AnyStr

class WireDataBatch(DSSBatch):
    _cls_name = 'WireData'
    _obj_cls = WireData
    _cls_idx = 9


    def _get_RDC(self) -> BatchFloat64ArrayProxy:
        """
        dc Resistance, ohms per unit length (see Runits). Defaults to Rac/1.02 if not specified.

        DSS property name: `RDC`, DSS property index: 1.
        """
        return BatchFloat64ArrayProxy(self, 1)

    def _set_RDC(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(1, value, flags)

    RDC = property(_get_RDC, _set_RDC) # type: BatchFloat64ArrayProxy

    def _get_RAC(self) -> BatchFloat64ArrayProxy:
        """
        Resistance at 60 Hz per unit length. Defaults to 1.02*Rdc if not specified.

        DSS property name: `RAC`, DSS property index: 2.
        """
        return BatchFloat64ArrayProxy(self, 2)

    def _set_RAC(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(2, value, flags)

    RAC = property(_get_RAC, _set_RAC) # type: BatchFloat64ArrayProxy

    def _get_RUnits(self) -> BatchInt32ArrayProxy:
        """
        Length units for resistance: ohms per {mi|kft|km|m|Ft|in|cm|mm} Default=none.

        DSS property name: `RUnits`, DSS property index: 3.
        """
        return BatchInt32ArrayProxy(self, 3)

    def _set_RUnits(self, value: Union[AnyStr, int, enums.LengthUnit, List[AnyStr], List[int], List[enums.LengthUnit], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(3, value, flags)
            return

        self._set_batch_int32_array(3, value, flags)

    RUnits = property(_get_RUnits, _set_RUnits) # type: BatchInt32ArrayProxy

    def _get_RUnits_str(self) -> List[str]:
        """
        Length units for resistance: ohms per {mi|kft|km|m|Ft|in|cm|mm} Default=none.

        DSS property name: `RUnits`, DSS property index: 3.
        """
        return self._get_batch_str_prop(3)

    def _set_RUnits_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_RUnits(value, flags)

    RUnits_str = property(_get_RUnits_str, _set_RUnits_str) # type: List[str]

    def _get_GMRAC(self) -> BatchFloat64ArrayProxy:
        """
        GMR at 60 Hz. Defaults to .7788*radius if not specified.

        DSS property name: `GMRAC`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    def _set_GMRAC(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(4, value, flags)

    GMRAC = property(_get_GMRAC, _set_GMRAC) # type: BatchFloat64ArrayProxy

    def _get_GMRUnits(self) -> BatchInt32ArrayProxy:
        """
        Units for GMR: {mi|kft|km|m|Ft|in|cm|mm} Default=none.

        DSS property name: `GMRUnits`, DSS property index: 5.
        """
        return BatchInt32ArrayProxy(self, 5)

    def _set_GMRUnits(self, value: Union[AnyStr, int, enums.LengthUnit, List[AnyStr], List[int], List[enums.LengthUnit], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(5, value, flags)
            return

        self._set_batch_int32_array(5, value, flags)

    GMRUnits = property(_get_GMRUnits, _set_GMRUnits) # type: BatchInt32ArrayProxy

    def _get_GMRUnits_str(self) -> List[str]:
        """
        Units for GMR: {mi|kft|km|m|Ft|in|cm|mm} Default=none.

        DSS property name: `GMRUnits`, DSS property index: 5.
        """
        return self._get_batch_str_prop(5)

    def _set_GMRUnits_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_GMRUnits(value, flags)

    GMRUnits_str = property(_get_GMRUnits_str, _set_GMRUnits_str) # type: List[str]

    def _get_Radius(self) -> BatchFloat64ArrayProxy:
        """
        Outside radius of conductor. Defaults to GMR/0.7788 if not specified.

        DSS property name: `Radius`, DSS property index: 6.
        """
        return BatchFloat64ArrayProxy(self, 6)

    def _set_Radius(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(6, value, flags)

    Radius = property(_get_Radius, _set_Radius) # type: BatchFloat64ArrayProxy

    def _get_RadUnits(self) -> BatchInt32ArrayProxy:
        """
        Units for outside radius: {mi|kft|km|m|Ft|in|cm|mm} Default=none.

        DSS property name: `RadUnits`, DSS property index: 7.
        """
        return BatchInt32ArrayProxy(self, 7)

    def _set_RadUnits(self, value: Union[AnyStr, int, enums.LengthUnit, List[AnyStr], List[int], List[enums.LengthUnit], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(7, value, flags)
            return

        self._set_batch_int32_array(7, value, flags)

    RadUnits = property(_get_RadUnits, _set_RadUnits) # type: BatchInt32ArrayProxy

    def _get_RadUnits_str(self) -> List[str]:
        """
        Units for outside radius: {mi|kft|km|m|Ft|in|cm|mm} Default=none.

        DSS property name: `RadUnits`, DSS property index: 7.
        """
        return self._get_batch_str_prop(7)

    def _set_RadUnits_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_RadUnits(value, flags)

    RadUnits_str = property(_get_RadUnits_str, _set_RadUnits_str) # type: List[str]

    def _get_NormAmps(self) -> BatchFloat64ArrayProxy:
        """
        Normal ampacity, amperes. Defaults to Emergency amps/1.5 if not specified.

        DSS property name: `NormAmps`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    def _set_NormAmps(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(8, value, flags)

    NormAmps = property(_get_NormAmps, _set_NormAmps) # type: BatchFloat64ArrayProxy

    def _get_EmergAmps(self) -> BatchFloat64ArrayProxy:
        """
        Emergency ampacity, amperes. Defaults to 1.5 * Normal Amps if not specified.

        DSS property name: `EmergAmps`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    def _set_EmergAmps(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(9, value, flags)

    EmergAmps = property(_get_EmergAmps, _set_EmergAmps) # type: BatchFloat64ArrayProxy

    def _get_Diam(self) -> BatchFloat64ArrayProxy:
        """
        Diameter; Alternative method for entering radius.

        DSS property name: `Diam`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    def _set_Diam(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(10, value, flags)

    Diam = property(_get_Diam, _set_Diam) # type: BatchFloat64ArrayProxy

    def _get_Seasons(self) -> BatchInt32ArrayProxy:
        """
        Defines the number of ratings to be defined for the wire, to be used only when defining seasonal ratings using the "Ratings" property.

        DSS property name: `Seasons`, DSS property index: 11.
        """
        return BatchInt32ArrayProxy(self, 11)

    def _set_Seasons(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(11, value, flags)

    Seasons = property(_get_Seasons, _set_Seasons) # type: BatchInt32ArrayProxy

    def _get_Ratings(self) -> List[Float64Array]:
        """
        An array of ratings to be used when the seasonal ratings flag is True. It can be used to insert
        multiple ratings to change during a QSTS simulation to evaluate different ratings in lines.

        DSS property name: `Ratings`, DSS property index: 12.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 12)
            for x in self._unpack()
        ]

    def _set_Ratings(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(12, value, flags)

    Ratings = property(_get_Ratings, _set_Ratings) # type: List[Float64Array]

    def _get_CapRadius(self) -> BatchFloat64ArrayProxy:
        """
        Equivalent conductor radius for capacitance calcs. Specify this for bundled conductors. Defaults to same value as radius. Define Diam or Radius property first.

        DSS property name: `CapRadius`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    def _set_CapRadius(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(13, value, flags)

    CapRadius = property(_get_CapRadius, _set_CapRadius) # type: BatchFloat64ArrayProxy

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 14.
        """
        self._set_batch_string(14, value, flags)

class WireDataBatchProperties(TypedDict):
    RDC: Union[float, Float64Array]
    RAC: Union[float, Float64Array]
    RUnits: Union[AnyStr, int, enums.LengthUnit, List[AnyStr], List[int], List[enums.LengthUnit], Int32Array]
    GMRAC: Union[float, Float64Array]
    GMRUnits: Union[AnyStr, int, enums.LengthUnit, List[AnyStr], List[int], List[enums.LengthUnit], Int32Array]
    Radius: Union[float, Float64Array]
    RadUnits: Union[AnyStr, int, enums.LengthUnit, List[AnyStr], List[int], List[enums.LengthUnit], Int32Array]
    NormAmps: Union[float, Float64Array]
    EmergAmps: Union[float, Float64Array]
    Diam: Union[float, Float64Array]
    Seasons: Union[int, Int32Array]
    Ratings: Float64Array
    CapRadius: Union[float, Float64Array]
    Like: AnyStr

class IWireData(IDSSObj, WireDataBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, WireData, WireDataBatch)
        WireDataBatch.__init__(self, self._api_util, sync_cls_idx=WireData._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> WireData:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[WireDataProperties]) -> WireData:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[WireDataBatchProperties]) -> WireDataBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
