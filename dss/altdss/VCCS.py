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

    def _get_Bus1(self) -> str:
        """
        Name of bus to which source is connected.
        bus1=busname
        bus1=busname.1.2.3

        DSS property name: `Bus1`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    def _set_Bus1(self, value: AnyStr):
        self._set_string_o(1, value)

    Bus1 = property(_get_Bus1, _set_Bus1)

    def _get_Phases(self) -> int:
        """
        Number of phases.  Defaults to 1.

        DSS property name: `Phases`, DSS property index: 2.
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    def _set_Phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    Phases = property(_get_Phases, _set_Phases)

    def _get_PRated(self) -> float:
        """
        Total rated power, in Watts.

        DSS property name: `PRated`, DSS property index: 3.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    def _set_PRated(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    PRated = property(_get_PRated, _set_PRated)

    def _get_VRated(self) -> float:
        """
        Rated line-to-line voltage, in Volts

        DSS property name: `VRated`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    def _set_VRated(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    VRated = property(_get_VRated, _set_VRated)

    def _get_Ppct(self) -> float:
        """
        Steady-state operating output, in percent of rated.

        DSS property name: `Ppct`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    def _set_Ppct(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    Ppct = property(_get_Ppct, _set_Ppct)

    def _get_BP1_str(self) -> str:
        """
        XYCurve defining the input piece-wise linear block.

        DSS property name: `BP1`, DSS property index: 6.
        """
        return self._get_prop_string(6)

    def _set_BP1_str(self, value: AnyStr):
        self._set_string_o(6, value)

    BP1_str = property(_get_BP1_str, _set_BP1_str)

    def _get_BP1(self) -> XYcurve:
        """
        XYCurve defining the input piece-wise linear block.

        DSS property name: `BP1`, DSS property index: 6.
        """
        return self._get_obj(6, XYcurve)

    def _set_BP1(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(6, value)
            return

        self._set_string_o(6, value)

    BP1 = property(_get_BP1, _set_BP1)

    def _get_BP2_str(self) -> str:
        """
        XYCurve defining the output piece-wise linear block.

        DSS property name: `BP2`, DSS property index: 7.
        """
        return self._get_prop_string(7)

    def _set_BP2_str(self, value: AnyStr):
        self._set_string_o(7, value)

    BP2_str = property(_get_BP2_str, _set_BP2_str)

    def _get_BP2(self) -> XYcurve:
        """
        XYCurve defining the output piece-wise linear block.

        DSS property name: `BP2`, DSS property index: 7.
        """
        return self._get_obj(7, XYcurve)

    def _set_BP2(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(7, value)
            return

        self._set_string_o(7, value)

    BP2 = property(_get_BP2, _set_BP2)

    def _get_Filter_str(self) -> str:
        """
        XYCurve defining the digital filter coefficients (x numerator, y denominator).

        DSS property name: `Filter`, DSS property index: 8.
        """
        return self._get_prop_string(8)

    def _set_Filter_str(self, value: AnyStr):
        self._set_string_o(8, value)

    Filter_str = property(_get_Filter_str, _set_Filter_str)

    def _get_Filter(self) -> XYcurve:
        """
        XYCurve defining the digital filter coefficients (x numerator, y denominator).

        DSS property name: `Filter`, DSS property index: 8.
        """
        return self._get_obj(8, XYcurve)

    def _set_Filter(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(8, value)
            return

        self._set_string_o(8, value)

    Filter = property(_get_Filter, _set_Filter)

    def _get_FSample(self) -> float:
        """
        Sample frequency [Hz} for the digital filter.

        DSS property name: `FSample`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    def _set_FSample(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    FSample = property(_get_FSample, _set_FSample)

    def _get_RMSMode(self) -> bool:
        """
        True if only Hz is used to represent a phase-locked loop (PLL), ignoring the BP1, BP2 and time-domain transformations. Default is no.

        DSS property name: `RMSMode`, DSS property index: 10.
        """
        return self._lib.Obj_GetInt32(self._ptr, 10) != 0

    def _set_RMSMode(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 10, value)

    RMSMode = property(_get_RMSMode, _set_RMSMode)

    def _get_IMaxpu(self) -> float:
        """
        Maximum output current in per-unit of rated; defaults to 1.1

        DSS property name: `IMaxpu`, DSS property index: 11.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    def _set_IMaxpu(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    IMaxpu = property(_get_IMaxpu, _set_IMaxpu)

    def _get_VRMSTau(self) -> float:
        """
        Time constant in sensing Vrms for the PLL; defaults to 0.0015

        DSS property name: `VRMSTau`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    def _set_VRMSTau(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    VRMSTau = property(_get_VRMSTau, _set_VRMSTau)

    def _get_IRMSTau(self) -> float:
        """
        Time constant in producing Irms from the PLL; defaults to 0.0015

        DSS property name: `IRMSTau`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    def _set_IRMSTau(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    IRMSTau = property(_get_IRMSTau, _set_IRMSTau)

    def _get_Spectrum_str(self) -> str:
        """
        Harmonic spectrum assumed for this source.  Default is "default".

        DSS property name: `Spectrum`, DSS property index: 14.
        """
        return self._get_prop_string(14)

    def _set_Spectrum_str(self, value: AnyStr):
        self._set_string_o(14, value)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str)

    def _get_Spectrum(self) -> SpectrumObj:
        """
        Harmonic spectrum assumed for this source.  Default is "default".

        DSS property name: `Spectrum`, DSS property index: 14.
        """
        return self._get_obj(14, SpectrumObj)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj]):
        if isinstance(value, DSSObj):
            self._set_obj(14, value)
            return

        self._set_string_o(14, value)

    Spectrum = property(_get_Spectrum, _set_Spectrum)

    def _get_BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 15.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    def _set_BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq)

    def _get_Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 16.
        """
        return self._lib.Obj_GetInt32(self._ptr, 16) != 0

    def _set_Enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 16, value)

    Enabled = property(_get_Enabled, _set_Enabled)

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


    def _get_Bus1(self) -> List[str]:
        """
        Name of bus to which source is connected.
        bus1=busname
        bus1=busname.1.2.3

        DSS property name: `Bus1`, DSS property index: 1.
        """
        return self._get_batch_str_prop(1)

    def _set_Bus1(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(1, value)

    Bus1 = property(_get_Bus1, _set_Bus1)

    def _get_Phases(self) -> BatchInt32ArrayProxy:
        """
        Number of phases.  Defaults to 1.

        DSS property name: `Phases`, DSS property index: 2.
        """
        return BatchInt32ArrayProxy(self, 2)

    def _set_Phases(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(2, value)

    Phases = property(_get_Phases, _set_Phases)

    def _get_PRated(self) -> BatchFloat64ArrayProxy:
        """
        Total rated power, in Watts.

        DSS property name: `PRated`, DSS property index: 3.
        """
        return BatchFloat64ArrayProxy(self, 3)

    def _set_PRated(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(3, value)

    PRated = property(_get_PRated, _set_PRated)

    def _get_VRated(self) -> BatchFloat64ArrayProxy:
        """
        Rated line-to-line voltage, in Volts

        DSS property name: `VRated`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    def _set_VRated(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(4, value)

    VRated = property(_get_VRated, _set_VRated)

    def _get_Ppct(self) -> BatchFloat64ArrayProxy:
        """
        Steady-state operating output, in percent of rated.

        DSS property name: `Ppct`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    def _set_Ppct(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(5, value)

    Ppct = property(_get_Ppct, _set_Ppct)

    def _get_BP1_str(self) -> List[str]:
        """
        XYCurve defining the input piece-wise linear block.

        DSS property name: `BP1`, DSS property index: 6.
        """
        return self._get_batch_str_prop(6)

    def _set_BP1_str(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(6, value)

    BP1_str = property(_get_BP1_str, _set_BP1_str)

    def _get_BP1(self) -> List[XYcurve]:
        """
        XYCurve defining the input piece-wise linear block.

        DSS property name: `BP1`, DSS property index: 6.
        """
        return self._get_batch_obj_prop(6)

    def _set_BP1(self, value: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]):
        self._set_batch_obj_prop(6, value)

    BP1 = property(_get_BP1, _set_BP1)

    def _get_BP2_str(self) -> List[str]:
        """
        XYCurve defining the output piece-wise linear block.

        DSS property name: `BP2`, DSS property index: 7.
        """
        return self._get_batch_str_prop(7)

    def _set_BP2_str(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(7, value)

    BP2_str = property(_get_BP2_str, _set_BP2_str)

    def _get_BP2(self) -> List[XYcurve]:
        """
        XYCurve defining the output piece-wise linear block.

        DSS property name: `BP2`, DSS property index: 7.
        """
        return self._get_batch_obj_prop(7)

    def _set_BP2(self, value: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]):
        self._set_batch_obj_prop(7, value)

    BP2 = property(_get_BP2, _set_BP2)

    def _get_Filter_str(self) -> List[str]:
        """
        XYCurve defining the digital filter coefficients (x numerator, y denominator).

        DSS property name: `Filter`, DSS property index: 8.
        """
        return self._get_batch_str_prop(8)

    def _set_Filter_str(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(8, value)

    Filter_str = property(_get_Filter_str, _set_Filter_str)

    def _get_Filter(self) -> List[XYcurve]:
        """
        XYCurve defining the digital filter coefficients (x numerator, y denominator).

        DSS property name: `Filter`, DSS property index: 8.
        """
        return self._get_batch_obj_prop(8)

    def _set_Filter(self, value: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]):
        self._set_batch_obj_prop(8, value)

    Filter = property(_get_Filter, _set_Filter)

    def _get_FSample(self) -> BatchFloat64ArrayProxy:
        """
        Sample frequency [Hz} for the digital filter.

        DSS property name: `FSample`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    def _set_FSample(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(9, value)

    FSample = property(_get_FSample, _set_FSample)

    def _get_RMSMode(self) -> List[bool]:
        """
        True if only Hz is used to represent a phase-locked loop (PLL), ignoring the BP1, BP2 and time-domain transformations. Default is no.

        DSS property name: `RMSMode`, DSS property index: 10.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(10)
        ]

    def _set_RMSMode(self, value: bool):
        self._set_batch_int32_array(10, value)

    RMSMode = property(_get_RMSMode, _set_RMSMode)

    def _get_IMaxpu(self) -> BatchFloat64ArrayProxy:
        """
        Maximum output current in per-unit of rated; defaults to 1.1

        DSS property name: `IMaxpu`, DSS property index: 11.
        """
        return BatchFloat64ArrayProxy(self, 11)

    def _set_IMaxpu(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(11, value)

    IMaxpu = property(_get_IMaxpu, _set_IMaxpu)

    def _get_VRMSTau(self) -> BatchFloat64ArrayProxy:
        """
        Time constant in sensing Vrms for the PLL; defaults to 0.0015

        DSS property name: `VRMSTau`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    def _set_VRMSTau(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(12, value)

    VRMSTau = property(_get_VRMSTau, _set_VRMSTau)

    def _get_IRMSTau(self) -> BatchFloat64ArrayProxy:
        """
        Time constant in producing Irms from the PLL; defaults to 0.0015

        DSS property name: `IRMSTau`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    def _set_IRMSTau(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(13, value)

    IRMSTau = property(_get_IRMSTau, _set_IRMSTau)

    def _get_Spectrum_str(self) -> List[str]:
        """
        Harmonic spectrum assumed for this source.  Default is "default".

        DSS property name: `Spectrum`, DSS property index: 14.
        """
        return self._get_batch_str_prop(14)

    def _set_Spectrum_str(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(14, value)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str)

    def _get_Spectrum(self) -> List[SpectrumObj]:
        """
        Harmonic spectrum assumed for this source.  Default is "default".

        DSS property name: `Spectrum`, DSS property index: 14.
        """
        return self._get_batch_obj_prop(14)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]]):
        self._set_batch_obj_prop(14, value)

    Spectrum = property(_get_Spectrum, _set_Spectrum)

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 15.
        """
        return BatchFloat64ArrayProxy(self, 15)

    def _set_BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(15, value)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq)

    def _get_Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 16.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(16)
        ]

    def _set_Enabled(self, value: bool):
        self._set_batch_int32_array(16, value)

    Enabled = property(_get_Enabled, _set_Enabled)

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
