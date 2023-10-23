# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from typing_extensions import TypedDict, Unpack
from ._obj_bases import (
    BatchFloat64ArrayProxy,
    BatchInt32ArrayProxy,
    DSSObj,
    DSSBatch,
    IDSSObj,
    LIST_LIKE,
    # NotSet,
)
from .._types import Float64Array, Int32Array
from .._cffi_api_util import Base
from . import enums

class WireData(DSSObj):
    __slots__ = []
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
    def RDC(self) -> float:
        """
        dc Resistance, ohms per unit length (see Runits). Defaults to Rac/1.02 if not specified.

        DSS property name: `RDC`, DSS property index: 1.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 1)

    @RDC.setter
    def RDC(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 1, value)

    @property
    def RAC(self) -> float:
        """
        Resistance at 60 Hz per unit length. Defaults to 1.02*Rdc if not specified.

        DSS property name: `RAC`, DSS property index: 2.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 2)

    @RAC.setter
    def RAC(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 2, value)

    @property
    def RUnits(self) -> enums.LengthUnit:
        """
        Length units for resistance: ohms per {mi|kft|km|m|Ft|in|cm|mm} Default=none.

        DSS property name: `RUnits`, DSS property index: 3.
        """
        return enums.LengthUnit(self._lib.Obj_GetInt32(self._ptr, 3))

    @RUnits.setter
    def RUnits(self, value: Union[AnyStr, int, enums.LengthUnit]):
        if not isinstance(value, int):
            self._set_string_o(3, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 3, value)

    @property
    def RUnits_str(self) -> str:
        """
        Length units for resistance: ohms per {mi|kft|km|m|Ft|in|cm|mm} Default=none.

        DSS property name: `RUnits`, DSS property index: 3.
        """
        return self._get_prop_string(3)

    @RUnits_str.setter
    def RUnits_str(self, value: AnyStr):
        self.RUnits = value

    @property
    def GMRAC(self) -> float:
        """
        GMR at 60 Hz. Defaults to .7788*radius if not specified.

        DSS property name: `GMRAC`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @GMRAC.setter
    def GMRAC(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def GMRUnits(self) -> enums.LengthUnit:
        """
        Units for GMR: {mi|kft|km|m|Ft|in|cm|mm} Default=none.

        DSS property name: `GMRUnits`, DSS property index: 5.
        """
        return enums.LengthUnit(self._lib.Obj_GetInt32(self._ptr, 5))

    @GMRUnits.setter
    def GMRUnits(self, value: Union[AnyStr, int, enums.LengthUnit]):
        if not isinstance(value, int):
            self._set_string_o(5, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 5, value)

    @property
    def GMRUnits_str(self) -> str:
        """
        Units for GMR: {mi|kft|km|m|Ft|in|cm|mm} Default=none.

        DSS property name: `GMRUnits`, DSS property index: 5.
        """
        return self._get_prop_string(5)

    @GMRUnits_str.setter
    def GMRUnits_str(self, value: AnyStr):
        self.GMRUnits = value

    @property
    def Radius(self) -> float:
        """
        Outside radius of conductor. Defaults to GMR/0.7788 if not specified.

        DSS property name: `Radius`, DSS property index: 6.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    @Radius.setter
    def Radius(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 6, value)

    @property
    def RadUnits(self) -> enums.LengthUnit:
        """
        Units for outside radius: {mi|kft|km|m|Ft|in|cm|mm} Default=none.

        DSS property name: `RadUnits`, DSS property index: 7.
        """
        return enums.LengthUnit(self._lib.Obj_GetInt32(self._ptr, 7))

    @RadUnits.setter
    def RadUnits(self, value: Union[AnyStr, int, enums.LengthUnit]):
        if not isinstance(value, int):
            self._set_string_o(7, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 7, value)

    @property
    def RadUnits_str(self) -> str:
        """
        Units for outside radius: {mi|kft|km|m|Ft|in|cm|mm} Default=none.

        DSS property name: `RadUnits`, DSS property index: 7.
        """
        return self._get_prop_string(7)

    @RadUnits_str.setter
    def RadUnits_str(self, value: AnyStr):
        self.RadUnits = value

    @property
    def NormAmps(self) -> float:
        """
        Normal ampacity, amperes. Defaults to Emergency amps/1.5 if not specified.

        DSS property name: `NormAmps`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @NormAmps.setter
    def NormAmps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def EmergAmps(self) -> float:
        """
        Emergency ampacity, amperes. Defaults to 1.5 * Normal Amps if not specified.

        DSS property name: `EmergAmps`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @EmergAmps.setter
    def EmergAmps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def Diam(self) -> float:
        """
        Diameter; Alternative method for entering radius.

        DSS property name: `Diam`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @Diam.setter
    def Diam(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def Seasons(self) -> int:
        """
        Defines the number of ratings to be defined for the wire, to be used only when defining seasonal ratings using the "Ratings" property.

        DSS property name: `Seasons`, DSS property index: 11.
        """
        return self._lib.Obj_GetInt32(self._ptr, 11)

    @Seasons.setter
    def Seasons(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 11, value)

    @property
    def Ratings(self) -> Float64Array:
        """
        An array of ratings to be used when the seasonal ratings flag is True. It can be used to insert
        multiple ratings to change during a QSTS simulation to evaluate different ratings in lines.

        DSS property name: `Ratings`, DSS property index: 12.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 12)

    @Ratings.setter
    def Ratings(self, value: Float64Array):
        self._set_float64_array_o(12, value)

    @property
    def CapRadius(self) -> float:
        """
        Equivalent conductor radius for capacitance calcs. Specify this for bundled conductors. Defaults to same value as radius. Define Diam or Radius property first.

        DSS property name: `CapRadius`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @CapRadius.setter
    def CapRadius(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

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


    @property
    def RDC(self) -> BatchFloat64ArrayProxy:
        """
        dc Resistance, ohms per unit length (see Runits). Defaults to Rac/1.02 if not specified.

        DSS property name: `RDC`, DSS property index: 1.
        """
        return BatchFloat64ArrayProxy(self, 1)

    @RDC.setter
    def RDC(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(1, value)

    @property
    def RAC(self) -> BatchFloat64ArrayProxy:
        """
        Resistance at 60 Hz per unit length. Defaults to 1.02*Rdc if not specified.

        DSS property name: `RAC`, DSS property index: 2.
        """
        return BatchFloat64ArrayProxy(self, 2)

    @RAC.setter
    def RAC(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(2, value)

    @property
    def RUnits(self) -> BatchInt32ArrayProxy:
        """
        Length units for resistance: ohms per {mi|kft|km|m|Ft|in|cm|mm} Default=none.

        DSS property name: `RUnits`, DSS property index: 3.
        """
        return BatchInt32ArrayProxy(self, 3)

    @RUnits.setter
    def RUnits(self, value: Union[AnyStr, int, enums.LengthUnit, List[AnyStr], List[int], List[enums.LengthUnit], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(3, value)
            return
    
        self._set_batch_int32_array(3, value)

    @property
    def RUnits_str(self) -> str:
        """
        Length units for resistance: ohms per {mi|kft|km|m|Ft|in|cm|mm} Default=none.

        DSS property name: `RUnits`, DSS property index: 3.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 3)

    @RUnits_str.setter
    def RUnits_str(self, value: AnyStr):
        self.RUnits = value

    @property
    def GMRAC(self) -> BatchFloat64ArrayProxy:
        """
        GMR at 60 Hz. Defaults to .7788*radius if not specified.

        DSS property name: `GMRAC`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    @GMRAC.setter
    def GMRAC(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(4, value)

    @property
    def GMRUnits(self) -> BatchInt32ArrayProxy:
        """
        Units for GMR: {mi|kft|km|m|Ft|in|cm|mm} Default=none.

        DSS property name: `GMRUnits`, DSS property index: 5.
        """
        return BatchInt32ArrayProxy(self, 5)

    @GMRUnits.setter
    def GMRUnits(self, value: Union[AnyStr, int, enums.LengthUnit, List[AnyStr], List[int], List[enums.LengthUnit], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(5, value)
            return
    
        self._set_batch_int32_array(5, value)

    @property
    def GMRUnits_str(self) -> str:
        """
        Units for GMR: {mi|kft|km|m|Ft|in|cm|mm} Default=none.

        DSS property name: `GMRUnits`, DSS property index: 5.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 5)

    @GMRUnits_str.setter
    def GMRUnits_str(self, value: AnyStr):
        self.GMRUnits = value

    @property
    def Radius(self) -> BatchFloat64ArrayProxy:
        """
        Outside radius of conductor. Defaults to GMR/0.7788 if not specified.

        DSS property name: `Radius`, DSS property index: 6.
        """
        return BatchFloat64ArrayProxy(self, 6)

    @Radius.setter
    def Radius(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(6, value)

    @property
    def RadUnits(self) -> BatchInt32ArrayProxy:
        """
        Units for outside radius: {mi|kft|km|m|Ft|in|cm|mm} Default=none.

        DSS property name: `RadUnits`, DSS property index: 7.
        """
        return BatchInt32ArrayProxy(self, 7)

    @RadUnits.setter
    def RadUnits(self, value: Union[AnyStr, int, enums.LengthUnit, List[AnyStr], List[int], List[enums.LengthUnit], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(7, value)
            return
    
        self._set_batch_int32_array(7, value)

    @property
    def RadUnits_str(self) -> str:
        """
        Units for outside radius: {mi|kft|km|m|Ft|in|cm|mm} Default=none.

        DSS property name: `RadUnits`, DSS property index: 7.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 7)

    @RadUnits_str.setter
    def RadUnits_str(self, value: AnyStr):
        self.RadUnits = value

    @property
    def NormAmps(self) -> BatchFloat64ArrayProxy:
        """
        Normal ampacity, amperes. Defaults to Emergency amps/1.5 if not specified.

        DSS property name: `NormAmps`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    @NormAmps.setter
    def NormAmps(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(8, value)

    @property
    def EmergAmps(self) -> BatchFloat64ArrayProxy:
        """
        Emergency ampacity, amperes. Defaults to 1.5 * Normal Amps if not specified.

        DSS property name: `EmergAmps`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    @EmergAmps.setter
    def EmergAmps(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(9, value)

    @property
    def Diam(self) -> BatchFloat64ArrayProxy:
        """
        Diameter; Alternative method for entering radius.

        DSS property name: `Diam`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    @Diam.setter
    def Diam(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(10, value)

    @property
    def Seasons(self) -> BatchInt32ArrayProxy:
        """
        Defines the number of ratings to be defined for the wire, to be used only when defining seasonal ratings using the "Ratings" property.

        DSS property name: `Seasons`, DSS property index: 11.
        """
        return BatchInt32ArrayProxy(self, 11)

    @Seasons.setter
    def Seasons(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(11, value)

    @property
    def Ratings(self) -> List[Float64Array]:
        """
        An array of ratings to be used when the seasonal ratings flag is True. It can be used to insert
        multiple ratings to change during a QSTS simulation to evaluate different ratings in lines.

        DSS property name: `Ratings`, DSS property index: 12.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 12)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Ratings.setter
    def Ratings(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(12, value)

    @property
    def CapRadius(self) -> BatchFloat64ArrayProxy:
        """
        Equivalent conductor radius for capacitance calcs. Specify this for bundled conductors. Defaults to same value as radius. Define Diam or Radius property first.

        DSS property name: `CapRadius`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    @CapRadius.setter
    def CapRadius(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(13, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 14.
        """
        self._set_batch_string(14, value)

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

class IWireData(IDSSObj):
    __slots__ = ()

    def __init__(self, iobj):
        super().__init__(iobj, WireData, WireDataBatch)

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> WireData:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[WireDataProperties]) -> WireData:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[WireDataBatchProperties]) -> WireDataBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
