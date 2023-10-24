# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from typing_extensions import TypedDict, Unpack
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
from .XYcurve import XYcurve

class VCCS(DSSObj, CktElementMixin, PCElementMixin):
    __slots__ = CktElementMixin._extra_slots + PCElementMixin._extra_slots
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
    def Bus1(self) -> str:
        """
        Name of bus to which source is connected.
        bus1=busname
        bus1=busname.1.2.3

        DSS property name: `Bus1`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    @Bus1.setter
    def Bus1(self, value: AnyStr):
        self._set_string_o(1, value)

    @property
    def Phases(self) -> int:
        """
        Number of phases.  Defaults to 1.

        DSS property name: `Phases`, DSS property index: 2.
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @Phases.setter
    def Phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def PRated(self) -> float:
        """
        Total rated power, in Watts.

        DSS property name: `PRated`, DSS property index: 3.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @PRated.setter
    def PRated(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def VRated(self) -> float:
        """
        Rated line-to-line voltage, in Volts

        DSS property name: `VRated`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @VRated.setter
    def VRated(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def Ppct(self) -> float:
        """
        Steady-state operating output, in percent of rated.

        DSS property name: `Ppct`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @Ppct.setter
    def Ppct(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def BP1_str(self) -> str:
        """
        XYCurve defining the input piece-wise linear block.

        DSS property name: `BP1`, DSS property index: 6.
        """
        return self._get_prop_string(6)

    @BP1_str.setter
    def BP1_str(self, value: AnyStr):
        self._set_string_o(6, value)

    @property
    def BP1(self) -> XYcurve:
        """
        XYCurve defining the input piece-wise linear block.

        DSS property name: `BP1`, DSS property index: 6.
        """
        return self._get_obj(6, XYcurve)

    @BP1.setter
    def BP1(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(6, value)
            return

        self._set_string_o(6, value)

    @property
    def BP2_str(self) -> str:
        """
        XYCurve defining the output piece-wise linear block.

        DSS property name: `BP2`, DSS property index: 7.
        """
        return self._get_prop_string(7)

    @BP2_str.setter
    def BP2_str(self, value: AnyStr):
        self._set_string_o(7, value)

    @property
    def BP2(self) -> XYcurve:
        """
        XYCurve defining the output piece-wise linear block.

        DSS property name: `BP2`, DSS property index: 7.
        """
        return self._get_obj(7, XYcurve)

    @BP2.setter
    def BP2(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(7, value)
            return

        self._set_string_o(7, value)

    @property
    def Filter_str(self) -> str:
        """
        XYCurve defining the digital filter coefficients (x numerator, y denominator).

        DSS property name: `Filter`, DSS property index: 8.
        """
        return self._get_prop_string(8)

    @Filter_str.setter
    def Filter_str(self, value: AnyStr):
        self._set_string_o(8, value)

    @property
    def Filter(self) -> XYcurve:
        """
        XYCurve defining the digital filter coefficients (x numerator, y denominator).

        DSS property name: `Filter`, DSS property index: 8.
        """
        return self._get_obj(8, XYcurve)

    @Filter.setter
    def Filter(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(8, value)
            return

        self._set_string_o(8, value)

    @property
    def FSample(self) -> float:
        """
        Sample frequency [Hz} for the digital filter.

        DSS property name: `FSample`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @FSample.setter
    def FSample(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def RMSMode(self) -> bool:
        """
        True if only Hz is used to represent a phase-locked loop (PLL), ignoring the BP1, BP2 and time-domain transformations. Default is no.

        DSS property name: `RMSMode`, DSS property index: 10.
        """
        return self._lib.Obj_GetInt32(self._ptr, 10) != 0

    @RMSMode.setter
    def RMSMode(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 10, value)

    @property
    def IMaxpu(self) -> float:
        """
        Maximum output current in per-unit of rated; defaults to 1.1

        DSS property name: `IMaxpu`, DSS property index: 11.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @IMaxpu.setter
    def IMaxpu(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def VRMSTau(self) -> float:
        """
        Time constant in sensing Vrms for the PLL; defaults to 0.0015

        DSS property name: `VRMSTau`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @VRMSTau.setter
    def VRMSTau(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def IRMSTau(self) -> float:
        """
        Time constant in producing Irms from the PLL; defaults to 0.0015

        DSS property name: `IRMSTau`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @IRMSTau.setter
    def IRMSTau(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def Spectrum_str(self) -> str:
        """
        Harmonic spectrum assumed for this source.  Default is "default".

        DSS property name: `Spectrum`, DSS property index: 14.
        """
        return self._get_prop_string(14)

    @Spectrum_str.setter
    def Spectrum_str(self, value: AnyStr):
        self._set_string_o(14, value)

    @property
    def Spectrum(self) -> SpectrumObj:
        """
        Harmonic spectrum assumed for this source.  Default is "default".

        DSS property name: `Spectrum`, DSS property index: 14.
        """
        return self._get_obj(14, SpectrumObj)

    @Spectrum.setter
    def Spectrum(self, value: Union[AnyStr, SpectrumObj]):
        if isinstance(value, DSSObj):
            self._set_obj(14, value)
            return

        self._set_string_o(14, value)

    @property
    def BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 15.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @BaseFreq.setter
    def BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 16.
        """
        return self._lib.Obj_GetInt32(self._ptr, 16) != 0

    @Enabled.setter
    def Enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 16, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 17.
        """
        self._set_string_o(17, value)


class VCCSProperties(TypedDict):
    Bus1: AnyStr
    Phases: int
    PRated: float
    VRated: float
    Ppct: float
    BP1: Union[AnyStr, XYcurve]
    BP2: Union[AnyStr, XYcurve]
    Filter: Union[AnyStr, XYcurve]
    FSample: float
    RMSMode: bool
    IMaxpu: float
    VRMSTau: float
    IRMSTau: float
    Spectrum: Union[AnyStr, SpectrumObj]
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class VCCSBatch(DSSBatch):
    _cls_name = 'VCCS'
    _obj_cls = VCCS
    _cls_idx = 18


    @property
    def Bus1(self) -> List[str]:
        """
        Name of bus to which source is connected.
        bus1=busname
        bus1=busname.1.2.3

        DSS property name: `Bus1`, DSS property index: 1.
        """
        return self._get_batch_str_prop(1) 

    @Bus1.setter
    def Bus1(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(1, value)

    @property
    def Phases(self) -> BatchInt32ArrayProxy:
        """
        Number of phases.  Defaults to 1.

        DSS property name: `Phases`, DSS property index: 2.
        """
        return BatchInt32ArrayProxy(self, 2)

    @Phases.setter
    def Phases(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(2, value)

    @property
    def PRated(self) -> BatchFloat64ArrayProxy:
        """
        Total rated power, in Watts.

        DSS property name: `PRated`, DSS property index: 3.
        """
        return BatchFloat64ArrayProxy(self, 3)

    @PRated.setter
    def PRated(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(3, value)

    @property
    def VRated(self) -> BatchFloat64ArrayProxy:
        """
        Rated line-to-line voltage, in Volts

        DSS property name: `VRated`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    @VRated.setter
    def VRated(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(4, value)

    @property
    def Ppct(self) -> BatchFloat64ArrayProxy:
        """
        Steady-state operating output, in percent of rated.

        DSS property name: `Ppct`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    @Ppct.setter
    def Ppct(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(5, value)

    @property
    def BP1_str(self) -> List[str]:
        """
        XYCurve defining the input piece-wise linear block.

        DSS property name: `BP1`, DSS property index: 6.
        """
        return self._get_batch_str_prop(6)

    @BP1_str.setter
    def BP1_str(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(6, value)

    @property
    def BP1(self) -> List[XYcurve]:
        """
        XYCurve defining the input piece-wise linear block.

        DSS property name: `BP1`, DSS property index: 6.
        """
        return self._get_batch_obj_prop(6)

    @BP1.setter
    def BP1(self, value: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]):
        self._set_batch_obj_prop(6, value)

    @property
    def BP2_str(self) -> List[str]:
        """
        XYCurve defining the output piece-wise linear block.

        DSS property name: `BP2`, DSS property index: 7.
        """
        return self._get_batch_str_prop(7)

    @BP2_str.setter
    def BP2_str(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(7, value)

    @property
    def BP2(self) -> List[XYcurve]:
        """
        XYCurve defining the output piece-wise linear block.

        DSS property name: `BP2`, DSS property index: 7.
        """
        return self._get_batch_obj_prop(7)

    @BP2.setter
    def BP2(self, value: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]):
        self._set_batch_obj_prop(7, value)

    @property
    def Filter_str(self) -> List[str]:
        """
        XYCurve defining the digital filter coefficients (x numerator, y denominator).

        DSS property name: `Filter`, DSS property index: 8.
        """
        return self._get_batch_str_prop(8)

    @Filter_str.setter
    def Filter_str(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(8, value)

    @property
    def Filter(self) -> List[XYcurve]:
        """
        XYCurve defining the digital filter coefficients (x numerator, y denominator).

        DSS property name: `Filter`, DSS property index: 8.
        """
        return self._get_batch_obj_prop(8)

    @Filter.setter
    def Filter(self, value: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]):
        self._set_batch_obj_prop(8, value)

    @property
    def FSample(self) -> BatchFloat64ArrayProxy:
        """
        Sample frequency [Hz} for the digital filter.

        DSS property name: `FSample`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    @FSample.setter
    def FSample(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(9, value)

    @property
    def RMSMode(self) -> List[bool]:
        """
        True if only Hz is used to represent a phase-locked loop (PLL), ignoring the BP1, BP2 and time-domain transformations. Default is no.

        DSS property name: `RMSMode`, DSS property index: 10.
        """
        return [v != 0 for v in 
            self._get_batch_int32_prop(10)
        ]
    @RMSMode.setter
    def RMSMode(self, value: bool):
        self._set_batch_int32_array(10, value)

    @property
    def IMaxpu(self) -> BatchFloat64ArrayProxy:
        """
        Maximum output current in per-unit of rated; defaults to 1.1

        DSS property name: `IMaxpu`, DSS property index: 11.
        """
        return BatchFloat64ArrayProxy(self, 11)

    @IMaxpu.setter
    def IMaxpu(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(11, value)

    @property
    def VRMSTau(self) -> BatchFloat64ArrayProxy:
        """
        Time constant in sensing Vrms for the PLL; defaults to 0.0015

        DSS property name: `VRMSTau`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    @VRMSTau.setter
    def VRMSTau(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(12, value)

    @property
    def IRMSTau(self) -> BatchFloat64ArrayProxy:
        """
        Time constant in producing Irms from the PLL; defaults to 0.0015

        DSS property name: `IRMSTau`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    @IRMSTau.setter
    def IRMSTau(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(13, value)

    @property
    def Spectrum_str(self) -> List[str]:
        """
        Harmonic spectrum assumed for this source.  Default is "default".

        DSS property name: `Spectrum`, DSS property index: 14.
        """
        return self._get_batch_str_prop(14)

    @Spectrum_str.setter
    def Spectrum_str(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(14, value)

    @property
    def Spectrum(self) -> List[SpectrumObj]:
        """
        Harmonic spectrum assumed for this source.  Default is "default".

        DSS property name: `Spectrum`, DSS property index: 14.
        """
        return self._get_batch_obj_prop(14)

    @Spectrum.setter
    def Spectrum(self, value: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]]):
        self._set_batch_obj_prop(14, value)

    @property
    def BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 15.
        """
        return BatchFloat64ArrayProxy(self, 15)

    @BaseFreq.setter
    def BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(15, value)

    @property
    def Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 16.
        """
        return [v != 0 for v in 
            self._get_batch_int32_prop(16)
        ]
    @Enabled.setter
    def Enabled(self, value: bool):
        self._set_batch_int32_array(16, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 17.
        """
        self._set_batch_string(17, value)

class VCCSBatchProperties(TypedDict):
    Bus1: Union[AnyStr, List[AnyStr]]
    Phases: Union[int, Int32Array]
    PRated: Union[float, Float64Array]
    VRated: Union[float, Float64Array]
    Ppct: Union[float, Float64Array]
    BP1: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]
    BP2: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]
    Filter: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]
    FSample: Union[float, Float64Array]
    RMSMode: bool
    IMaxpu: Union[float, Float64Array]
    VRMSTau: Union[float, Float64Array]
    IRMSTau: Union[float, Float64Array]
    Spectrum: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IVCCS(IDSSObj,VCCSBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, VCCS, VCCSBatch)
        VCCSBatch.__init__(self, self._api_util, sync_cls=True)
        

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> VCCS:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[VCCSProperties]) -> VCCS:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[VCCSBatchProperties]) -> VCCSBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
