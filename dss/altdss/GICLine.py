# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from enum import IntEnum
from typing_extensions import TypedDict, Unpack
import numpy as np
from ._obj_bases import (
    CktElementMixin,
    PCElementMixin,
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
from .Spectrum import Spectrum as SpectrumObj

class GICLine(DSSObj, CktElementMixin, PCElementMixin):
    __slots__ = []
    _cls_name = 'GICLine'
    _cls_idx = 44
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
    def Bus1(self) -> str:
        """
        Name of bus to which the main terminal (1) is connected.
        bus1=busname
        bus1=busname.1.2.3

        DSS property name: `Bus1`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    @Bus1.setter
    def Bus1(self, value: AnyStr):
        self._set_string_o(1, value)

    @property
    def Bus2(self) -> str:
        """
        Name of bus to which 2nd terminal is connected.
        bus2=busname
        bus2=busname.1.2.3

        No Default; must be specified.

        DSS property name: `Bus2`, DSS property index: 2.
        """
        return self._get_prop_string(2)

    @Bus2.setter
    def Bus2(self, value: AnyStr):
        self._set_string_o(2, value)

    @property
    def Volts(self) -> float:
        """
        Voltage magnitude, in volts, of the GIC voltage induced across this line. When specified, voltage source is assumed defined by Voltage and Angle properties. 

        Specify this value

        OR

        EN, EE, lat1, lon1, lat2, lon2. 

        Not both!!  Last one entered will take precedence. Assumed identical in each phase of the Line object.

        DSS property name: `Volts`, DSS property index: 3.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @Volts.setter
    def Volts(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def Angle(self) -> float:
        """
        Phase angle in degrees of first phase. Default=0.0.  See Voltage property

        DSS property name: `Angle`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @Angle.setter
    def Angle(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def Frequency(self) -> float:
        """
        Source frequency.  Defaults to 0.1 Hz.

        DSS property name: `Frequency`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @Frequency.setter
    def Frequency(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def Phases(self) -> int:
        """
        Number of phases.  Defaults to 3.

        DSS property name: `Phases`, DSS property index: 6.
        """
        return self._lib.Obj_GetInt32(self._ptr, 6)

    @Phases.setter
    def Phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 6, value)

    @property
    def R(self) -> float:
        """
        Resistance of line, ohms of impedance in series with GIC voltage source. 

        DSS property name: `R`, DSS property index: 7.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @R.setter
    def R(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def X(self) -> float:
        """
        Reactance at base frequency, ohms. Default = 0.0. This value is generally not important for GIC studies but may be used if desired.

        DSS property name: `X`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @X.setter
    def X(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def C(self) -> float:
        """
        Value of line blocking capacitance in microfarads. Default = 0.0, implying that there is no line blocking capacitor.

        DSS property name: `C`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @C.setter
    def C(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def EN(self) -> float:
        """
        Northward Electric field (V/km). If specified, Voltage and Angle are computed from EN, EE, lat and lon values.

        DSS property name: `EN`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @EN.setter
    def EN(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def EE(self) -> float:
        """
        Eastward Electric field (V/km).  If specified, Voltage and Angle are computed from EN, EE, lat and lon values.

        DSS property name: `EE`, DSS property index: 11.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @EE.setter
    def EE(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def Lat1(self) -> float:
        """
        Latitude of Bus1 (degrees)

        DSS property name: `Lat1`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @Lat1.setter
    def Lat1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def Lon1(self) -> float:
        """
        Longitude of Bus1 (degrees)

        DSS property name: `Lon1`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @Lon1.setter
    def Lon1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def Lat2(self) -> float:
        """
        Latitude of Bus2 (degrees)

        DSS property name: `Lat2`, DSS property index: 14.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @Lat2.setter
    def Lat2(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def Lon2(self) -> float:
        """
        Longitude of Bus2 (degrees)

        DSS property name: `Lon2`, DSS property index: 15.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @Lon2.setter
    def Lon2(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def Spectrum(self) -> str:
        """
        Inherited Property for all PCElements. Name of harmonic spectrum for this source.  Default is "defaultvsource", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 16.
        """
        return self._get_prop_string(16)

    @Spectrum.setter
    def Spectrum(self, value: Union[AnyStr, SpectrumObj]):
        if isinstance(value, DSSObj):
            self._set_obj(16, value)
            return

        self._set_string_o(16, value)

    @property
    def Spectrum_obj(self) -> SpectrumObj:
        """
        Inherited Property for all PCElements. Name of harmonic spectrum for this source.  Default is "defaultvsource", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 16.
        """
        return self._get_obj(16, SpectrumObj)

    @Spectrum_obj.setter
    def Spectrum_obj(self, value: SpectrumObj):
        self._set_obj(16, value)

    @property
    def BaseFreq(self) -> float:
        """
        Inherited Property for all PCElements. Base frequency for specification of reactance value.

        DSS property name: `BaseFreq`, DSS property index: 17.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    @BaseFreq.setter
    def BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 17, value)

    @property
    def Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 18.
        """
        return self._lib.Obj_GetInt32(self._ptr, 18) != 0

    @Enabled.setter
    def Enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 18, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 19.
        """
        self._set_string_o(19, value)


class GICLineProperties(TypedDict):
    Bus1: AnyStr
    Bus2: AnyStr
    Volts: float
    Angle: float
    Frequency: float
    Phases: int
    R: float
    X: float
    C: float
    EN: float
    EE: float
    Lat1: float
    Lon1: float
    Lat2: float
    Lon2: float
    Spectrum: Union[AnyStr, SpectrumObj]
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class GICLineBatch(DSSBatch):
    _cls_name = 'GICLine'
    _obj_cls = GICLine
    _cls_idx = 44


    @property
    def Bus1(self) -> List[str]:
        """
        Name of bus to which the main terminal (1) is connected.
        bus1=busname
        bus1=busname.1.2.3

        DSS property name: `Bus1`, DSS property index: 1.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1) 

    @Bus1.setter
    def Bus1(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(1, value)

    @property
    def Bus2(self) -> List[str]:
        """
        Name of bus to which 2nd terminal is connected.
        bus2=busname
        bus2=busname.1.2.3

        No Default; must be specified.

        DSS property name: `Bus2`, DSS property index: 2.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 2) 

    @Bus2.setter
    def Bus2(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(2, value)

    @property
    def Volts(self) -> BatchFloat64ArrayProxy:
        """
        Voltage magnitude, in volts, of the GIC voltage induced across this line. When specified, voltage source is assumed defined by Voltage and Angle properties. 

        Specify this value

        OR

        EN, EE, lat1, lon1, lat2, lon2. 

        Not both!!  Last one entered will take precedence. Assumed identical in each phase of the Line object.

        DSS property name: `Volts`, DSS property index: 3.
        """
        return BatchFloat64ArrayProxy(self, 3)

    @Volts.setter
    def Volts(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(3, value)

    @property
    def Angle(self) -> BatchFloat64ArrayProxy:
        """
        Phase angle in degrees of first phase. Default=0.0.  See Voltage property

        DSS property name: `Angle`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    @Angle.setter
    def Angle(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(4, value)

    @property
    def Frequency(self) -> BatchFloat64ArrayProxy:
        """
        Source frequency.  Defaults to 0.1 Hz.

        DSS property name: `Frequency`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    @Frequency.setter
    def Frequency(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(5, value)

    @property
    def Phases(self) -> BatchInt32ArrayProxy:
        """
        Number of phases.  Defaults to 3.

        DSS property name: `Phases`, DSS property index: 6.
        """
        return BatchInt32ArrayProxy(self, 6)

    @Phases.setter
    def Phases(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(6, value)

    @property
    def R(self) -> BatchFloat64ArrayProxy:
        """
        Resistance of line, ohms of impedance in series with GIC voltage source. 

        DSS property name: `R`, DSS property index: 7.
        """
        return BatchFloat64ArrayProxy(self, 7)

    @R.setter
    def R(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(7, value)

    @property
    def X(self) -> BatchFloat64ArrayProxy:
        """
        Reactance at base frequency, ohms. Default = 0.0. This value is generally not important for GIC studies but may be used if desired.

        DSS property name: `X`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    @X.setter
    def X(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(8, value)

    @property
    def C(self) -> BatchFloat64ArrayProxy:
        """
        Value of line blocking capacitance in microfarads. Default = 0.0, implying that there is no line blocking capacitor.

        DSS property name: `C`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    @C.setter
    def C(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(9, value)

    @property
    def EN(self) -> BatchFloat64ArrayProxy:
        """
        Northward Electric field (V/km). If specified, Voltage and Angle are computed from EN, EE, lat and lon values.

        DSS property name: `EN`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    @EN.setter
    def EN(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(10, value)

    @property
    def EE(self) -> BatchFloat64ArrayProxy:
        """
        Eastward Electric field (V/km).  If specified, Voltage and Angle are computed from EN, EE, lat and lon values.

        DSS property name: `EE`, DSS property index: 11.
        """
        return BatchFloat64ArrayProxy(self, 11)

    @EE.setter
    def EE(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(11, value)

    @property
    def Lat1(self) -> BatchFloat64ArrayProxy:
        """
        Latitude of Bus1 (degrees)

        DSS property name: `Lat1`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    @Lat1.setter
    def Lat1(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(12, value)

    @property
    def Lon1(self) -> BatchFloat64ArrayProxy:
        """
        Longitude of Bus1 (degrees)

        DSS property name: `Lon1`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    @Lon1.setter
    def Lon1(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(13, value)

    @property
    def Lat2(self) -> BatchFloat64ArrayProxy:
        """
        Latitude of Bus2 (degrees)

        DSS property name: `Lat2`, DSS property index: 14.
        """
        return BatchFloat64ArrayProxy(self, 14)

    @Lat2.setter
    def Lat2(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(14, value)

    @property
    def Lon2(self) -> BatchFloat64ArrayProxy:
        """
        Longitude of Bus2 (degrees)

        DSS property name: `Lon2`, DSS property index: 15.
        """
        return BatchFloat64ArrayProxy(self, 15)

    @Lon2.setter
    def Lon2(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(15, value)

    @property
    def Spectrum(self) -> List[str]:
        """
        Inherited Property for all PCElements. Name of harmonic spectrum for this source.  Default is "defaultvsource", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 16.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 16)

    @Spectrum.setter
    def Spectrum(self, value: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]]):
        self._set_batch_obj_prop(16, value)

    @property
    def Spectrum_obj(self) -> List[SpectrumObj]:
        """
        Inherited Property for all PCElements. Name of harmonic spectrum for this source.  Default is "defaultvsource", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 16.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 16)

    @Spectrum_obj.setter
    def Spectrum_obj(self, value: SpectrumObj):
        self._set_batch_string(16, value)

    @property
    def BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Inherited Property for all PCElements. Base frequency for specification of reactance value.

        DSS property name: `BaseFreq`, DSS property index: 17.
        """
        return BatchFloat64ArrayProxy(self, 17)

    @BaseFreq.setter
    def BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(17, value)

    @property
    def Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 18.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 18)
        ]
    @Enabled.setter
    def Enabled(self, value: bool):
        self._set_batch_int32_array(18, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 19.
        """
        self._set_batch_string(19, value)

class GICLineBatchProperties(TypedDict):
    Bus1: Union[AnyStr, List[AnyStr]]
    Bus2: Union[AnyStr, List[AnyStr]]
    Volts: Union[float, Float64Array]
    Angle: Union[float, Float64Array]
    Frequency: Union[float, Float64Array]
    Phases: Union[int, Int32Array]
    R: Union[float, Float64Array]
    X: Union[float, Float64Array]
    C: Union[float, Float64Array]
    EN: Union[float, Float64Array]
    EE: Union[float, Float64Array]
    Lat1: Union[float, Float64Array]
    Lon1: Union[float, Float64Array]
    Lat2: Union[float, Float64Array]
    Lon2: Union[float, Float64Array]
    Spectrum: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IGICLine(IDSSObj):
    def __init__(self, iobj):
        super().__init__(iobj, GICLine, GICLineBatch)

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> GICLine:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[GICLineProperties]) -> GICLine:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[GICLineBatchProperties]) -> GICLineBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
