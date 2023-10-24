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

class VSConverter(DSSObj, CktElementMixin, PCElementMixin):
    __slots__ = CktElementMixin._extra_slots + PCElementMixin._extra_slots
    _cls_name = 'VSConverter'
    _cls_idx = 46
    _cls_prop_idx = {
        'phases': 1,
        'bus1': 2,
        'kvac': 3,
        'kvdc': 4,
        'kw': 5,
        'ndc': 6,
        'rac': 7,
        'xac': 8,
        'm0': 9,
        'd0': 10,
        'mmin': 11,
        'mmax': 12,
        'iacmax': 13,
        'idcmax': 14,
        'vacref': 15,
        'pacref': 16,
        'qacref': 17,
        'vdcref': 18,
        'vscmode': 19,
        'spectrum': 20,
        'basefreq': 21,
        'enabled': 22,
        'like': 23,
    }

    @property
    def Phases(self) -> int:
        """
        Number of AC plus DC conductors. Default is 4. AC phases numbered before DC conductors.

        DSS property name: `Phases`, DSS property index: 1.
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @Phases.setter
    def Phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def Bus1(self) -> str:
        """
        Name of converter bus, containing both AC and DC conductors. Bus2 is always ground.

        DSS property name: `Bus1`, DSS property index: 2.
        """
        return self._get_prop_string(2)

    @Bus1.setter
    def Bus1(self, value: AnyStr):
        self._set_string_o(2, value)

    @property
    def kVAC(self) -> float:
        """
        Nominal AC line-neutral voltage in kV. Must be specified > 0.

        DSS property name: `kVAC`, DSS property index: 3.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @kVAC.setter
    def kVAC(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def kVDC(self) -> float:
        """
        Nominal DC voltage in kV. Must be specified > 0.

        DSS property name: `kVDC`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @kVDC.setter
    def kVDC(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def kW(self) -> float:
        """
        Nominal converter power in kW. Must be specified > 0.

        DSS property name: `kW`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @kW.setter
    def kW(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def NDC(self) -> int:
        """
        Number of DC conductors. Default is 1. DC conductors numbered after AC phases.

        DSS property name: `NDC`, DSS property index: 6.
        """
        return self._lib.Obj_GetInt32(self._ptr, 6)

    @NDC.setter
    def NDC(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 6, value)

    @property
    def RAC(self) -> float:
        """
        AC resistance (ohms) for the converter transformer, plus any series reactors. Default is 0.
        Must be 0 for Vac control mode.

        DSS property name: `RAC`, DSS property index: 7.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @RAC.setter
    def RAC(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def XAC(self) -> float:
        """
        AC reactance (ohms) for the converter transformer, plus any series reactors. Default is 0.
        Must be 0 for Vac control mode. Must be >0 for PacVac, PacQac or VacVdc control mode.

        DSS property name: `XAC`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @XAC.setter
    def XAC(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def M0(self) -> float:
        """
        Fixed or initial value of the modulation index. Default is 0.5.

        DSS property name: `M0`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @M0.setter
    def M0(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def d0(self) -> float:
        """
        Fixed or initial value of the power angle in degrees. Default is 0.

        DSS property name: `d0`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @d0.setter
    def d0(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def MMin(self) -> float:
        """
        Minimum value of modulation index. Default is 0.1.

        DSS property name: `MMin`, DSS property index: 11.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @MMin.setter
    def MMin(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def MMax(self) -> float:
        """
        Maximum value of modulation index. Default is 0.9.

        DSS property name: `MMax`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @MMax.setter
    def MMax(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def IACMax(self) -> float:
        """
        Maximum value of AC line current, per-unit of nominal. Default is 2.

        DSS property name: `IACMax`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @IACMax.setter
    def IACMax(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def IDCMax(self) -> float:
        """
        Maximum value of DC current, per-unit of nominal. Default is 2.

        DSS property name: `IDCMax`, DSS property index: 14.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @IDCMax.setter
    def IDCMax(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def VACRef(self) -> float:
        """
        Reference AC line-to-neutral voltage, RMS Volts. Default is 0.
        Applies to PacVac and VdcVac control modes, influencing m.

        DSS property name: `VACRef`, DSS property index: 15.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @VACRef.setter
    def VACRef(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def PACRef(self) -> float:
        """
        Reference total AC real power, Watts. Default is 0.
        Applies to PacVac and PacQac control modes, influencing d.

        DSS property name: `PACRef`, DSS property index: 16.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    @PACRef.setter
    def PACRef(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 16, value)

    @property
    def QACRef(self) -> float:
        """
        Reference total AC reactive power, Vars. Default is 0.
        Applies to PacQac and VdcQac control modes, influencing m.

        DSS property name: `QACRef`, DSS property index: 17.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    @QACRef.setter
    def QACRef(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 17, value)

    @property
    def VDCRef(self) -> float:
        """
        Reference DC voltage, Volts. Default is 0.
        Applies to VdcVac control mode, influencing d.

        DSS property name: `VDCRef`, DSS property index: 18.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    @VDCRef.setter
    def VDCRef(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 18, value)

    @property
    def VSCMode(self) -> enums.VSConverterControlMode:
        """
        Control Mode (Fixed|PacVac|PacQac|VdcVac|VdcQac). Default is Fixed.

        DSS property name: `VSCMode`, DSS property index: 19.
        """
        return enums.VSConverterControlMode(self._lib.Obj_GetInt32(self._ptr, 19))

    @VSCMode.setter
    def VSCMode(self, value: Union[AnyStr, int, enums.VSConverterControlMode]):
        if not isinstance(value, int):
            self._set_string_o(19, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 19, value)

    @property
    def VSCMode_str(self) -> str:
        """
        Control Mode (Fixed|PacVac|PacQac|VdcVac|VdcQac). Default is Fixed.

        DSS property name: `VSCMode`, DSS property index: 19.
        """
        return self._get_prop_string(19)

    @VSCMode_str.setter
    def VSCMode_str(self, value: AnyStr):
        self.VSCMode = value

    @property
    def Spectrum_str(self) -> str:
        """
        Name of harmonic spectrum for this device.

        DSS property name: `Spectrum`, DSS property index: 20.
        """
        return self._get_prop_string(20)

    @Spectrum_str.setter
    def Spectrum_str(self, value: AnyStr):
        self._set_string_o(20, value)

    @property
    def Spectrum(self) -> SpectrumObj:
        """
        Name of harmonic spectrum for this device.

        DSS property name: `Spectrum`, DSS property index: 20.
        """
        return self._get_obj(20, SpectrumObj)

    @Spectrum.setter
    def Spectrum(self, value: Union[AnyStr, SpectrumObj]):
        if isinstance(value, DSSObj):
            self._set_obj(20, value)
            return

        self._set_string_o(20, value)

    @property
    def BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 21.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @BaseFreq.setter
    def BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    @property
    def Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 22.
        """
        return self._lib.Obj_GetInt32(self._ptr, 22) != 0

    @Enabled.setter
    def Enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 22, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 23.
        """
        self._set_string_o(23, value)


class VSConverterProperties(TypedDict):
    Phases: int
    Bus1: AnyStr
    kVAC: float
    kVDC: float
    kW: float
    NDC: int
    RAC: float
    XAC: float
    M0: float
    d0: float
    MMin: float
    MMax: float
    IACMax: float
    IDCMax: float
    VACRef: float
    PACRef: float
    QACRef: float
    VDCRef: float
    VSCMode: Union[AnyStr, int, enums.VSConverterControlMode]
    Spectrum: Union[AnyStr, SpectrumObj]
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class VSConverterBatch(DSSBatch):
    _cls_name = 'VSConverter'
    _obj_cls = VSConverter
    _cls_idx = 46


    @property
    def Phases(self) -> BatchInt32ArrayProxy:
        """
        Number of AC plus DC conductors. Default is 4. AC phases numbered before DC conductors.

        DSS property name: `Phases`, DSS property index: 1.
        """
        return BatchInt32ArrayProxy(self, 1)

    @Phases.setter
    def Phases(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(1, value)

    @property
    def Bus1(self) -> List[str]:
        """
        Name of converter bus, containing both AC and DC conductors. Bus2 is always ground.

        DSS property name: `Bus1`, DSS property index: 2.
        """
        return self._get_batch_str_prop(2) 

    @Bus1.setter
    def Bus1(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(2, value)

    @property
    def kVAC(self) -> BatchFloat64ArrayProxy:
        """
        Nominal AC line-neutral voltage in kV. Must be specified > 0.

        DSS property name: `kVAC`, DSS property index: 3.
        """
        return BatchFloat64ArrayProxy(self, 3)

    @kVAC.setter
    def kVAC(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(3, value)

    @property
    def kVDC(self) -> BatchFloat64ArrayProxy:
        """
        Nominal DC voltage in kV. Must be specified > 0.

        DSS property name: `kVDC`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    @kVDC.setter
    def kVDC(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(4, value)

    @property
    def kW(self) -> BatchFloat64ArrayProxy:
        """
        Nominal converter power in kW. Must be specified > 0.

        DSS property name: `kW`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    @kW.setter
    def kW(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(5, value)

    @property
    def NDC(self) -> BatchInt32ArrayProxy:
        """
        Number of DC conductors. Default is 1. DC conductors numbered after AC phases.

        DSS property name: `NDC`, DSS property index: 6.
        """
        return BatchInt32ArrayProxy(self, 6)

    @NDC.setter
    def NDC(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(6, value)

    @property
    def RAC(self) -> BatchFloat64ArrayProxy:
        """
        AC resistance (ohms) for the converter transformer, plus any series reactors. Default is 0.
        Must be 0 for Vac control mode.

        DSS property name: `RAC`, DSS property index: 7.
        """
        return BatchFloat64ArrayProxy(self, 7)

    @RAC.setter
    def RAC(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(7, value)

    @property
    def XAC(self) -> BatchFloat64ArrayProxy:
        """
        AC reactance (ohms) for the converter transformer, plus any series reactors. Default is 0.
        Must be 0 for Vac control mode. Must be >0 for PacVac, PacQac or VacVdc control mode.

        DSS property name: `XAC`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    @XAC.setter
    def XAC(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(8, value)

    @property
    def M0(self) -> BatchFloat64ArrayProxy:
        """
        Fixed or initial value of the modulation index. Default is 0.5.

        DSS property name: `M0`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    @M0.setter
    def M0(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(9, value)

    @property
    def d0(self) -> BatchFloat64ArrayProxy:
        """
        Fixed or initial value of the power angle in degrees. Default is 0.

        DSS property name: `d0`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    @d0.setter
    def d0(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(10, value)

    @property
    def MMin(self) -> BatchFloat64ArrayProxy:
        """
        Minimum value of modulation index. Default is 0.1.

        DSS property name: `MMin`, DSS property index: 11.
        """
        return BatchFloat64ArrayProxy(self, 11)

    @MMin.setter
    def MMin(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(11, value)

    @property
    def MMax(self) -> BatchFloat64ArrayProxy:
        """
        Maximum value of modulation index. Default is 0.9.

        DSS property name: `MMax`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    @MMax.setter
    def MMax(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(12, value)

    @property
    def IACMax(self) -> BatchFloat64ArrayProxy:
        """
        Maximum value of AC line current, per-unit of nominal. Default is 2.

        DSS property name: `IACMax`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    @IACMax.setter
    def IACMax(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(13, value)

    @property
    def IDCMax(self) -> BatchFloat64ArrayProxy:
        """
        Maximum value of DC current, per-unit of nominal. Default is 2.

        DSS property name: `IDCMax`, DSS property index: 14.
        """
        return BatchFloat64ArrayProxy(self, 14)

    @IDCMax.setter
    def IDCMax(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(14, value)

    @property
    def VACRef(self) -> BatchFloat64ArrayProxy:
        """
        Reference AC line-to-neutral voltage, RMS Volts. Default is 0.
        Applies to PacVac and VdcVac control modes, influencing m.

        DSS property name: `VACRef`, DSS property index: 15.
        """
        return BatchFloat64ArrayProxy(self, 15)

    @VACRef.setter
    def VACRef(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(15, value)

    @property
    def PACRef(self) -> BatchFloat64ArrayProxy:
        """
        Reference total AC real power, Watts. Default is 0.
        Applies to PacVac and PacQac control modes, influencing d.

        DSS property name: `PACRef`, DSS property index: 16.
        """
        return BatchFloat64ArrayProxy(self, 16)

    @PACRef.setter
    def PACRef(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(16, value)

    @property
    def QACRef(self) -> BatchFloat64ArrayProxy:
        """
        Reference total AC reactive power, Vars. Default is 0.
        Applies to PacQac and VdcQac control modes, influencing m.

        DSS property name: `QACRef`, DSS property index: 17.
        """
        return BatchFloat64ArrayProxy(self, 17)

    @QACRef.setter
    def QACRef(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(17, value)

    @property
    def VDCRef(self) -> BatchFloat64ArrayProxy:
        """
        Reference DC voltage, Volts. Default is 0.
        Applies to VdcVac control mode, influencing d.

        DSS property name: `VDCRef`, DSS property index: 18.
        """
        return BatchFloat64ArrayProxy(self, 18)

    @VDCRef.setter
    def VDCRef(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(18, value)

    @property
    def VSCMode(self) -> BatchInt32ArrayProxy:
        """
        Control Mode (Fixed|PacVac|PacQac|VdcVac|VdcQac). Default is Fixed.

        DSS property name: `VSCMode`, DSS property index: 19.
        """
        return BatchInt32ArrayProxy(self, 19)

    @VSCMode.setter
    def VSCMode(self, value: Union[AnyStr, int, enums.VSConverterControlMode, List[AnyStr], List[int], List[enums.VSConverterControlMode], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(19, value)
            return
    
        self._set_batch_int32_array(19, value)

    @property
    def VSCMode_str(self) -> str:
        """
        Control Mode (Fixed|PacVac|PacQac|VdcVac|VdcQac). Default is Fixed.

        DSS property name: `VSCMode`, DSS property index: 19.
        """
        return self._get_batch_str_prop(19)

    @VSCMode_str.setter
    def VSCMode_str(self, value: AnyStr):
        self.VSCMode = value

    @property
    def Spectrum_str(self) -> List[str]:
        """
        Name of harmonic spectrum for this device.

        DSS property name: `Spectrum`, DSS property index: 20.
        """
        return self._get_batch_str_prop(20)

    @Spectrum_str.setter
    def Spectrum_str(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(20, value)

    @property
    def Spectrum(self) -> List[SpectrumObj]:
        """
        Name of harmonic spectrum for this device.

        DSS property name: `Spectrum`, DSS property index: 20.
        """
        return self._get_batch_obj_prop(20)

    @Spectrum.setter
    def Spectrum(self, value: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]]):
        self._set_batch_obj_prop(20, value)

    @property
    def BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 21.
        """
        return BatchFloat64ArrayProxy(self, 21)

    @BaseFreq.setter
    def BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(21, value)

    @property
    def Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 22.
        """
        return [v != 0 for v in 
            self._get_batch_int32_prop(22)
        ]
    @Enabled.setter
    def Enabled(self, value: bool):
        self._set_batch_int32_array(22, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 23.
        """
        self._set_batch_string(23, value)

class VSConverterBatchProperties(TypedDict):
    Phases: Union[int, Int32Array]
    Bus1: Union[AnyStr, List[AnyStr]]
    kVAC: Union[float, Float64Array]
    kVDC: Union[float, Float64Array]
    kW: Union[float, Float64Array]
    NDC: Union[int, Int32Array]
    RAC: Union[float, Float64Array]
    XAC: Union[float, Float64Array]
    M0: Union[float, Float64Array]
    d0: Union[float, Float64Array]
    MMin: Union[float, Float64Array]
    MMax: Union[float, Float64Array]
    IACMax: Union[float, Float64Array]
    IDCMax: Union[float, Float64Array]
    VACRef: Union[float, Float64Array]
    PACRef: Union[float, Float64Array]
    QACRef: Union[float, Float64Array]
    VDCRef: Union[float, Float64Array]
    VSCMode: Union[AnyStr, int, enums.VSConverterControlMode, List[AnyStr], List[int], List[enums.VSConverterControlMode], Int32Array]
    Spectrum: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IVSConverter(IDSSObj,VSConverterBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, VSConverter, VSConverterBatch)
        VSConverterBatch.__init__(self, self._api_util, sync_cls=True)
        

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> VSConverter:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[VSConverterProperties]) -> VSConverter:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[VSConverterBatchProperties]) -> VSConverterBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
