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

class GICsource(DSSObj, CktElementMixin, PCElementMixin):
    __slots__ = []
    _cls_name = 'GICsource'
    _cls_idx = 40
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
        Voltage magnitude, in volts, of the GIC voltage induced across the associated line. When specified, induced voltage is assumed defined by Voltage and Angle properties. 

        Specify this value

        OR

        EN, EE, lat1, lon1, lat2, lon2. 

        Not both!!  Last one entered will take precedence. Assumed identical in each phase of the Line object.

        DSS property name: `Volts`, DSS property index: 1.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 1)

    @Volts.setter
    def Volts(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 1, value)

    @property
    def Angle(self) -> float:
        """
        Phase angle in degrees of first phase. Default=0.0.  See Voltage property

        DSS property name: `Angle`, DSS property index: 2.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 2)

    @Angle.setter
    def Angle(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 2, value)

    @property
    def Frequency(self) -> float:
        """
        Source frequency.  Defaults to  0.1 Hz. So GICSource=0 at power frequency.

        DSS property name: `Frequency`, DSS property index: 3.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @Frequency.setter
    def Frequency(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def Phases(self) -> int:
        """
        Number of phases.  Defaults to 3. All three phases are assumed in phase (zero sequence)

        DSS property name: `Phases`, DSS property index: 4.
        """
        return self._lib.Obj_GetInt32(self._ptr, 4)

    @Phases.setter
    def Phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 4, value)

    @property
    def EN(self) -> float:
        """
        Northward Electric field (V/km). If specified, Voltage and Angle are computed from EN, EE, lat and lon values.

        DSS property name: `EN`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @EN.setter
    def EN(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def EE(self) -> float:
        """
        Eastward Electric field (V/km).  If specified, Voltage and Angle are computed from EN, EE, lat and lon values.

        DSS property name: `EE`, DSS property index: 6.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    @EE.setter
    def EE(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 6, value)

    @property
    def Lat1(self) -> float:
        """
        Latitude of Bus1 of the line(degrees)

        DSS property name: `Lat1`, DSS property index: 7.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @Lat1.setter
    def Lat1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def Lon1(self) -> float:
        """
        Longitude of Bus1 of the line (degrees)

        DSS property name: `Lon1`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @Lon1.setter
    def Lon1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def Lat2(self) -> float:
        """
        Latitude of Bus2 of the line (degrees)

        DSS property name: `Lat2`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @Lat2.setter
    def Lat2(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def Lon2(self) -> float:
        """
        Longitude of Bus2 of the line (degrees)

        DSS property name: `Lon2`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @Lon2.setter
    def Lon2(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def Spectrum(self) -> str:
        """
        Not used.

        DSS property name: `Spectrum`, DSS property index: 11.
        """
        return self._get_prop_string(11)

    @Spectrum.setter
    def Spectrum(self, value: Union[AnyStr, SpectrumObj]):
        if isinstance(value, DSSObj):
            self._set_obj(11, value)
            return

        self._set_string_o(11, value)

    @property
    def Spectrum_obj(self) -> SpectrumObj:
        """
        Not used.

        DSS property name: `Spectrum`, DSS property index: 11.
        """
        return self._get_obj(11, SpectrumObj)

    @Spectrum_obj.setter
    def Spectrum_obj(self, value: SpectrumObj):
        self._set_obj(11, value)

    @property
    def BaseFreq(self) -> float:
        """
        Not used.

        DSS property name: `BaseFreq`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @BaseFreq.setter
    def BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 13.
        """
        return self._lib.Obj_GetInt32(self._ptr, 13) != 0

    @Enabled.setter
    def Enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 13, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 14.
        """
        self._set_string_o(14, value)


class GICsourceProperties(TypedDict):
    Volts: float
    Angle: float
    Frequency: float
    Phases: int
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

class GICsourceBatch(DSSBatch):
    _cls_name = 'GICsource'
    _obj_cls = GICsource
    _cls_idx = 40


    @property
    def Volts(self) -> BatchFloat64ArrayProxy:
        """
        Voltage magnitude, in volts, of the GIC voltage induced across the associated line. When specified, induced voltage is assumed defined by Voltage and Angle properties. 

        Specify this value

        OR

        EN, EE, lat1, lon1, lat2, lon2. 

        Not both!!  Last one entered will take precedence. Assumed identical in each phase of the Line object.

        DSS property name: `Volts`, DSS property index: 1.
        """
        return BatchFloat64ArrayProxy(self, 1)

    @Volts.setter
    def Volts(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(1, value)

    @property
    def Angle(self) -> BatchFloat64ArrayProxy:
        """
        Phase angle in degrees of first phase. Default=0.0.  See Voltage property

        DSS property name: `Angle`, DSS property index: 2.
        """
        return BatchFloat64ArrayProxy(self, 2)

    @Angle.setter
    def Angle(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(2, value)

    @property
    def Frequency(self) -> BatchFloat64ArrayProxy:
        """
        Source frequency.  Defaults to  0.1 Hz. So GICSource=0 at power frequency.

        DSS property name: `Frequency`, DSS property index: 3.
        """
        return BatchFloat64ArrayProxy(self, 3)

    @Frequency.setter
    def Frequency(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(3, value)

    @property
    def Phases(self) -> BatchInt32ArrayProxy:
        """
        Number of phases.  Defaults to 3. All three phases are assumed in phase (zero sequence)

        DSS property name: `Phases`, DSS property index: 4.
        """
        return BatchInt32ArrayProxy(self, 4)

    @Phases.setter
    def Phases(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(4, value)

    @property
    def EN(self) -> BatchFloat64ArrayProxy:
        """
        Northward Electric field (V/km). If specified, Voltage and Angle are computed from EN, EE, lat and lon values.

        DSS property name: `EN`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    @EN.setter
    def EN(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(5, value)

    @property
    def EE(self) -> BatchFloat64ArrayProxy:
        """
        Eastward Electric field (V/km).  If specified, Voltage and Angle are computed from EN, EE, lat and lon values.

        DSS property name: `EE`, DSS property index: 6.
        """
        return BatchFloat64ArrayProxy(self, 6)

    @EE.setter
    def EE(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(6, value)

    @property
    def Lat1(self) -> BatchFloat64ArrayProxy:
        """
        Latitude of Bus1 of the line(degrees)

        DSS property name: `Lat1`, DSS property index: 7.
        """
        return BatchFloat64ArrayProxy(self, 7)

    @Lat1.setter
    def Lat1(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(7, value)

    @property
    def Lon1(self) -> BatchFloat64ArrayProxy:
        """
        Longitude of Bus1 of the line (degrees)

        DSS property name: `Lon1`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    @Lon1.setter
    def Lon1(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(8, value)

    @property
    def Lat2(self) -> BatchFloat64ArrayProxy:
        """
        Latitude of Bus2 of the line (degrees)

        DSS property name: `Lat2`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    @Lat2.setter
    def Lat2(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(9, value)

    @property
    def Lon2(self) -> BatchFloat64ArrayProxy:
        """
        Longitude of Bus2 of the line (degrees)

        DSS property name: `Lon2`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    @Lon2.setter
    def Lon2(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(10, value)

    @property
    def Spectrum(self) -> List[str]:
        """
        Not used.

        DSS property name: `Spectrum`, DSS property index: 11.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 11)

    @Spectrum.setter
    def Spectrum(self, value: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]]):
        self._set_batch_obj_prop(11, value)

    @property
    def Spectrum_obj(self) -> List[SpectrumObj]:
        """
        Not used.

        DSS property name: `Spectrum`, DSS property index: 11.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 11)

    @Spectrum_obj.setter
    def Spectrum_obj(self, value: SpectrumObj):
        self._set_batch_string(11, value)

    @property
    def BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Not used.

        DSS property name: `BaseFreq`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    @BaseFreq.setter
    def BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(12, value)

    @property
    def Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 13.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 13)
        ]
    @Enabled.setter
    def Enabled(self, value: bool):
        self._set_batch_int32_array(13, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 14.
        """
        self._set_batch_string(14, value)

class GICsourceBatchProperties(TypedDict):
    Volts: Union[float, Float64Array]
    Angle: Union[float, Float64Array]
    Frequency: Union[float, Float64Array]
    Phases: Union[int, Int32Array]
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

class IGICsource(IDSSObj):
    def __init__(self, iobj):
        super().__init__(iobj, GICsource, GICsourceBatch)

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> GICsource:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[GICsourceProperties]) -> GICsource:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[GICsourceBatchProperties]) -> GICsourceBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)