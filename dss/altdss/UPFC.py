# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from typing_extensions import TypedDict, Unpack
from .types import Float64Array, Int32Array
from . import enums
from .DSSObj import IDSSObj, DSSObj
from .Batch import DSSBatch
from .ArrayProxy import BatchFloat64ArrayProxy, BatchInt32ArrayProxy
from .PCElement import PCElementBatchMixin, PCElementMixin
from .CircuitElement import CircuitElementBatchMixin, CircuitElementMixin

from .AutoTrans import AutoTrans
from .Capacitor import Capacitor
from .Line import Line
from .Reactor import Reactor
from .Transformer import Transformer
PDElement = Union[
    AutoTrans,
    Capacitor,
    Line,
    Reactor,
    Transformer,
]
from .Spectrum import Spectrum as SpectrumObj
from .XYcurve import XYcurve

class UPFC(DSSObj, CircuitElementMixin, PCElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots + PCElementMixin._extra_slots
    _cls_name = 'UPFC'
    _cls_idx = 36
    _cls_prop_idx = {
        'bus1': 1,
        'bus2': 2,
        'refkv': 3,
        'pf': 4,
        'frequency': 5,
        'phases': 6,
        'xs': 7,
        'tol1': 8,
        'mode': 9,
        'vpqmax': 10,
        'losscurve': 11,
        'vhlimit': 12,
        'vllimit': 13,
        'climit': 14,
        'refkv2': 15,
        'kvarlimit': 16,
        'element': 17,
        'spectrum': 18,
        'basefreq': 19,
        'enabled': 20,
        'like': 21,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)
       PCElementMixin.__init__(self)

    def _get_Bus1(self) -> str:
        """
        Name of bus to which the input terminal (1) is connected.
        bus1=busname.1.3
        bus1=busname.1.2.3

        DSS property name: `Bus1`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    def _set_Bus1(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(1, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: str

    def _get_Bus2(self) -> str:
        """
        Name of bus to which the output terminal (2) is connected.
        bus2=busname.1.2
        bus2=busname.1.2.3

        DSS property name: `Bus2`, DSS property index: 2.
        """
        return self._get_prop_string(2)

    def _set_Bus2(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(2, value, flags)

    Bus2 = property(_get_Bus2, _set_Bus2) # type: str

    def _get_RefkV(self) -> float:
        """
        Base Voltage expected at the output of the UPFC

        "refkv=0.24"

        DSS property name: `RefkV`, DSS property index: 3.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    def _set_RefkV(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 3, value, flags)

    RefkV = property(_get_RefkV, _set_RefkV) # type: float

    def _get_PF(self) -> float:
        """
        Power factor target at the input terminal.

        DSS property name: `PF`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    def _set_PF(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 4, value, flags)

    PF = property(_get_PF, _set_PF) # type: float

    def _get_Frequency(self) -> float:
        """
        UPFC working frequency.  Defaults to system default base frequency.

        DSS property name: `Frequency`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    def _set_Frequency(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 5, value, flags)

    Frequency = property(_get_Frequency, _set_Frequency) # type: float

    def _get_Phases(self) -> int:
        """
        Number of phases.  Defaults to 1 phase (2 terminals, 1 conductor per terminal).

        DSS property name: `Phases`, DSS property index: 6.
        """
        return self._lib.Obj_GetInt32(self._ptr, 6)

    def _set_Phases(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 6, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: int

    def _get_Xs(self) -> float:
        """
        Reactance of the series transformer of the UPFC, ohms (default=0.7540 ... 2 mH)

        DSS property name: `Xs`, DSS property index: 7.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    def _set_Xs(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 7, value, flags)

    Xs = property(_get_Xs, _set_Xs) # type: float

    def _get_Tol1(self) -> float:
        """
        Tolerance in pu for the series PI controller
        Tol1=0.02 is the format used to define 2% tolerance (Default=2%)

        DSS property name: `Tol1`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    def _set_Tol1(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 8, value, flags)

    Tol1 = property(_get_Tol1, _set_Tol1) # type: float

    def _get_Mode(self) -> enums.UPFCMode:
        """
        Integer used to define the control mode of the UPFC: 

        0 = Off, 
        1 = Voltage regulator, 
        2 = Phase angle regulator, 
        3 = Dual mode
        4 = It is a control mode where the user can set two different set points to create a secure GAP, these references must be defined in the parameters RefkV and RefkV2. The only restriction when setting these values is that RefkV must be higher than RefkV2. 
        5 = In this mode the user can define the same GAP using two set points as in control mode 4. The only difference between mode 5 and mode 4 is that in mode 5, the UPFC controller performs dual control actions just as in control mode 3

        DSS property name: `Mode`, DSS property index: 9.
        """
        return enums.UPFCMode(self._lib.Obj_GetInt32(self._ptr, 9))

    def _set_Mode(self, value: Union[int, enums.UPFCMode], flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 9, value, flags)

    Mode = property(_get_Mode, _set_Mode) # type: enums.UPFCMode

    def _get_VpqMax(self) -> float:
        """
        Maximum voltage (in volts) delivered by the series voltage source (Default = 24 V)

        DSS property name: `VpqMax`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    def _set_VpqMax(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 10, value, flags)

    VpqMax = property(_get_VpqMax, _set_VpqMax) # type: float

    def _get_LossCurve_str(self) -> str:
        """
        Name of the XYCurve for describing the losses behavior as a function of the voltage at the input of the UPFC

        DSS property name: `LossCurve`, DSS property index: 11.
        """
        return self._get_prop_string(11)

    def _set_LossCurve_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(11, value, flags)

    LossCurve_str = property(_get_LossCurve_str, _set_LossCurve_str) # type: str

    def _get_LossCurve(self) -> XYcurve:
        """
        Name of the XYCurve for describing the losses behavior as a function of the voltage at the input of the UPFC

        DSS property name: `LossCurve`, DSS property index: 11.
        """
        return self._get_obj(11, XYcurve)

    def _set_LossCurve(self, value: Union[AnyStr, XYcurve], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(11, value, flags)
            return

        self._set_string_o(11, value, flags)

    LossCurve = property(_get_LossCurve, _set_LossCurve) # type: XYcurve

    def _get_VHLimit(self) -> float:
        """
        High limit for the voltage at the input of the UPFC, if the voltage is above this value the UPFC turns off. This value is specified in Volts (default 300 V)

        DSS property name: `VHLimit`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    def _set_VHLimit(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 12, value, flags)

    VHLimit = property(_get_VHLimit, _set_VHLimit) # type: float

    def _get_VLLimit(self) -> float:
        """
        low limit for the voltage at the input of the UPFC, if voltage is below this value the UPFC turns off. This value is specified in Volts (default 125 V)

        DSS property name: `VLLimit`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    def _set_VLLimit(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 13, value, flags)

    VLLimit = property(_get_VLLimit, _set_VLLimit) # type: float

    def _get_CLimit(self) -> float:
        """
        Current Limit for the UPFC, if the current passing through the UPFC is higher than this value the UPFC turns off. This value is specified in Amps (Default 265 A)

        DSS property name: `CLimit`, DSS property index: 14.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    def _set_CLimit(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 14, value, flags)

    CLimit = property(_get_CLimit, _set_CLimit) # type: float

    def _get_refkV2(self) -> float:
        """
        Base Voltage expected at the output of the UPFC for control modes 4 and 5.

        This reference must be lower than refkv, see control modes 4 and 5 for details

        DSS property name: `refkV2`, DSS property index: 15.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    def _set_refkV2(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 15, value, flags)

    refkV2 = property(_get_refkV2, _set_refkV2) # type: float

    def _get_kvarLimit(self) -> float:
        """
        Maximum amount of reactive power (kvar) that can be absorbed by the UPFC (Default = 5)

        DSS property name: `kvarLimit`, DSS property index: 16.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    def _set_kvarLimit(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 16, value, flags)

    kvarLimit = property(_get_kvarLimit, _set_kvarLimit) # type: float

    def _get_Element_str(self) -> str:
        """
        The name of the PD element monitored when operating with reactive power compensation. Normally, it should be the PD element immediately upstream the UPFC. The element must be defined including the class, e.g. Line.myline.

        DSS property name: `Element`, DSS property index: 17.
        """
        return self._get_prop_string(17)

    def _set_Element_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(17, value, flags)

    Element_str = property(_get_Element_str, _set_Element_str) # type: str

    def _get_Element(self) -> PDElement:
        """
        The name of the PD element monitored when operating with reactive power compensation. Normally, it should be the PD element immediately upstream the UPFC. The element must be defined including the class, e.g. Line.myline.

        DSS property name: `Element`, DSS property index: 17.
        """
        return self._get_obj(17, PDElement)

    def _set_Element(self, value: Union[AnyStr, PDElement], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(17, value, flags)
            return

        self._set_string_o(17, value, flags)

    Element = property(_get_Element, _set_Element) # type: PDElement

    def _get_Spectrum_str(self) -> str:
        """
        Name of harmonic spectrum for this source.  Default is "defaultUPFC", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 18.
        """
        return self._get_prop_string(18)

    def _set_Spectrum_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(18, value, flags)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str) # type: str

    def _get_Spectrum(self) -> SpectrumObj:
        """
        Name of harmonic spectrum for this source.  Default is "defaultUPFC", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 18.
        """
        return self._get_obj(18, SpectrumObj)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(18, value, flags)
            return

        self._set_string_o(18, value, flags)

    Spectrum = property(_get_Spectrum, _set_Spectrum) # type: SpectrumObj

    def _get_BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 19.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 19, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float

    def _get_Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 20.
        """
        return self._lib.Obj_GetInt32(self._ptr, 20) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 20, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 21.
        """
        self._set_string_o(21, value)


class UPFCProperties(TypedDict):
    Bus1: AnyStr
    Bus2: AnyStr
    RefkV: float
    PF: float
    Frequency: float
    Phases: int
    Xs: float
    Tol1: float
    Mode: Union[int, enums.UPFCMode]
    VpqMax: float
    LossCurve: Union[AnyStr, XYcurve]
    VHLimit: float
    VLLimit: float
    CLimit: float
    refkV2: float
    kvarLimit: float
    Element: Union[AnyStr, PDElement]
    Spectrum: Union[AnyStr, SpectrumObj]
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class UPFCBatch(DSSBatch, CircuitElementBatchMixin, PCElementBatchMixin):
    _cls_name = 'UPFC'
    _obj_cls = UPFC
    _cls_idx = 36

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)
       PCElementBatchMixin.__init__(self)

    def _get_Bus1(self) -> List[str]:
        """
        Name of bus to which the input terminal (1) is connected.
        bus1=busname.1.3
        bus1=busname.1.2.3

        DSS property name: `Bus1`, DSS property index: 1.
        """
        return self._get_batch_str_prop(1)

    def _set_Bus1(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(1, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: List[str]

    def _get_Bus2(self) -> List[str]:
        """
        Name of bus to which the output terminal (2) is connected.
        bus2=busname.1.2
        bus2=busname.1.2.3

        DSS property name: `Bus2`, DSS property index: 2.
        """
        return self._get_batch_str_prop(2)

    def _set_Bus2(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(2, value, flags)

    Bus2 = property(_get_Bus2, _set_Bus2) # type: List[str]

    def _get_RefkV(self) -> BatchFloat64ArrayProxy:
        """
        Base Voltage expected at the output of the UPFC

        "refkv=0.24"

        DSS property name: `RefkV`, DSS property index: 3.
        """
        return BatchFloat64ArrayProxy(self, 3)

    def _set_RefkV(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(3, value, flags)

    RefkV = property(_get_RefkV, _set_RefkV) # type: BatchFloat64ArrayProxy

    def _get_PF(self) -> BatchFloat64ArrayProxy:
        """
        Power factor target at the input terminal.

        DSS property name: `PF`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    def _set_PF(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(4, value, flags)

    PF = property(_get_PF, _set_PF) # type: BatchFloat64ArrayProxy

    def _get_Frequency(self) -> BatchFloat64ArrayProxy:
        """
        UPFC working frequency.  Defaults to system default base frequency.

        DSS property name: `Frequency`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    def _set_Frequency(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(5, value, flags)

    Frequency = property(_get_Frequency, _set_Frequency) # type: BatchFloat64ArrayProxy

    def _get_Phases(self) -> BatchInt32ArrayProxy:
        """
        Number of phases.  Defaults to 1 phase (2 terminals, 1 conductor per terminal).

        DSS property name: `Phases`, DSS property index: 6.
        """
        return BatchInt32ArrayProxy(self, 6)

    def _set_Phases(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(6, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: BatchInt32ArrayProxy

    def _get_Xs(self) -> BatchFloat64ArrayProxy:
        """
        Reactance of the series transformer of the UPFC, ohms (default=0.7540 ... 2 mH)

        DSS property name: `Xs`, DSS property index: 7.
        """
        return BatchFloat64ArrayProxy(self, 7)

    def _set_Xs(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(7, value, flags)

    Xs = property(_get_Xs, _set_Xs) # type: BatchFloat64ArrayProxy

    def _get_Tol1(self) -> BatchFloat64ArrayProxy:
        """
        Tolerance in pu for the series PI controller
        Tol1=0.02 is the format used to define 2% tolerance (Default=2%)

        DSS property name: `Tol1`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    def _set_Tol1(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(8, value, flags)

    Tol1 = property(_get_Tol1, _set_Tol1) # type: BatchFloat64ArrayProxy

    def _get_Mode(self) -> BatchInt32ArrayProxy:
        """
        Integer used to define the control mode of the UPFC: 

        0 = Off, 
        1 = Voltage regulator, 
        2 = Phase angle regulator, 
        3 = Dual mode
        4 = It is a control mode where the user can set two different set points to create a secure GAP, these references must be defined in the parameters RefkV and RefkV2. The only restriction when setting these values is that RefkV must be higher than RefkV2. 
        5 = In this mode the user can define the same GAP using two set points as in control mode 4. The only difference between mode 5 and mode 4 is that in mode 5, the UPFC controller performs dual control actions just as in control mode 3

        DSS property name: `Mode`, DSS property index: 9.
        """
        return BatchInt32ArrayProxy(self, 9)

    def _set_Mode(self, value: Union[int, enums.UPFCMode, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(9, value, flags)

    Mode = property(_get_Mode, _set_Mode) # type: BatchInt32ArrayProxy

    def _get_VpqMax(self) -> BatchFloat64ArrayProxy:
        """
        Maximum voltage (in volts) delivered by the series voltage source (Default = 24 V)

        DSS property name: `VpqMax`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    def _set_VpqMax(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(10, value, flags)

    VpqMax = property(_get_VpqMax, _set_VpqMax) # type: BatchFloat64ArrayProxy

    def _get_LossCurve_str(self) -> List[str]:
        """
        Name of the XYCurve for describing the losses behavior as a function of the voltage at the input of the UPFC

        DSS property name: `LossCurve`, DSS property index: 11.
        """
        return self._get_batch_str_prop(11)

    def _set_LossCurve_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(11, value, flags)

    LossCurve_str = property(_get_LossCurve_str, _set_LossCurve_str) # type: List[str]

    def _get_LossCurve(self) -> List[XYcurve]:
        """
        Name of the XYCurve for describing the losses behavior as a function of the voltage at the input of the UPFC

        DSS property name: `LossCurve`, DSS property index: 11.
        """
        return self._get_batch_obj_prop(11)

    def _set_LossCurve(self, value: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(11, value, flags)

    LossCurve = property(_get_LossCurve, _set_LossCurve) # type: List[XYcurve]

    def _get_VHLimit(self) -> BatchFloat64ArrayProxy:
        """
        High limit for the voltage at the input of the UPFC, if the voltage is above this value the UPFC turns off. This value is specified in Volts (default 300 V)

        DSS property name: `VHLimit`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    def _set_VHLimit(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(12, value, flags)

    VHLimit = property(_get_VHLimit, _set_VHLimit) # type: BatchFloat64ArrayProxy

    def _get_VLLimit(self) -> BatchFloat64ArrayProxy:
        """
        low limit for the voltage at the input of the UPFC, if voltage is below this value the UPFC turns off. This value is specified in Volts (default 125 V)

        DSS property name: `VLLimit`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    def _set_VLLimit(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(13, value, flags)

    VLLimit = property(_get_VLLimit, _set_VLLimit) # type: BatchFloat64ArrayProxy

    def _get_CLimit(self) -> BatchFloat64ArrayProxy:
        """
        Current Limit for the UPFC, if the current passing through the UPFC is higher than this value the UPFC turns off. This value is specified in Amps (Default 265 A)

        DSS property name: `CLimit`, DSS property index: 14.
        """
        return BatchFloat64ArrayProxy(self, 14)

    def _set_CLimit(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(14, value, flags)

    CLimit = property(_get_CLimit, _set_CLimit) # type: BatchFloat64ArrayProxy

    def _get_refkV2(self) -> BatchFloat64ArrayProxy:
        """
        Base Voltage expected at the output of the UPFC for control modes 4 and 5.

        This reference must be lower than refkv, see control modes 4 and 5 for details

        DSS property name: `refkV2`, DSS property index: 15.
        """
        return BatchFloat64ArrayProxy(self, 15)

    def _set_refkV2(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(15, value, flags)

    refkV2 = property(_get_refkV2, _set_refkV2) # type: BatchFloat64ArrayProxy

    def _get_kvarLimit(self) -> BatchFloat64ArrayProxy:
        """
        Maximum amount of reactive power (kvar) that can be absorbed by the UPFC (Default = 5)

        DSS property name: `kvarLimit`, DSS property index: 16.
        """
        return BatchFloat64ArrayProxy(self, 16)

    def _set_kvarLimit(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(16, value, flags)

    kvarLimit = property(_get_kvarLimit, _set_kvarLimit) # type: BatchFloat64ArrayProxy

    def _get_Element_str(self) -> List[str]:
        """
        The name of the PD element monitored when operating with reactive power compensation. Normally, it should be the PD element immediately upstream the UPFC. The element must be defined including the class, e.g. Line.myline.

        DSS property name: `Element`, DSS property index: 17.
        """
        return self._get_batch_str_prop(17)

    def _set_Element_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(17, value, flags)

    Element_str = property(_get_Element_str, _set_Element_str) # type: List[str]

    def _get_Element(self) -> List[PDElement]:
        """
        The name of the PD element monitored when operating with reactive power compensation. Normally, it should be the PD element immediately upstream the UPFC. The element must be defined including the class, e.g. Line.myline.

        DSS property name: `Element`, DSS property index: 17.
        """
        return self._get_batch_obj_prop(17)

    def _set_Element(self, value: Union[AnyStr, PDElement, List[AnyStr], List[PDElement]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(17, value, flags)

    Element = property(_get_Element, _set_Element) # type: List[PDElement]

    def _get_Spectrum_str(self) -> List[str]:
        """
        Name of harmonic spectrum for this source.  Default is "defaultUPFC", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 18.
        """
        return self._get_batch_str_prop(18)

    def _set_Spectrum_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(18, value, flags)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str) # type: List[str]

    def _get_Spectrum(self) -> List[SpectrumObj]:
        """
        Name of harmonic spectrum for this source.  Default is "defaultUPFC", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 18.
        """
        return self._get_batch_obj_prop(18)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(18, value, flags)

    Spectrum = property(_get_Spectrum, _set_Spectrum) # type: List[SpectrumObj]

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 19.
        """
        return BatchFloat64ArrayProxy(self, 19)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(19, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy

    def _get_Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 20.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(20)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(20, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 21.
        """
        self._set_batch_string(21, value, flags)

class UPFCBatchProperties(TypedDict):
    Bus1: Union[AnyStr, List[AnyStr]]
    Bus2: Union[AnyStr, List[AnyStr]]
    RefkV: Union[float, Float64Array]
    PF: Union[float, Float64Array]
    Frequency: Union[float, Float64Array]
    Phases: Union[int, Int32Array]
    Xs: Union[float, Float64Array]
    Tol1: Union[float, Float64Array]
    Mode: Union[int, enums.UPFCMode, Int32Array]
    VpqMax: Union[float, Float64Array]
    LossCurve: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]
    VHLimit: Union[float, Float64Array]
    VLLimit: Union[float, Float64Array]
    CLimit: Union[float, Float64Array]
    refkV2: Union[float, Float64Array]
    kvarLimit: Union[float, Float64Array]
    Element: Union[AnyStr, PDElement, List[AnyStr], List[PDElement]]
    Spectrum: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IUPFC(IDSSObj, UPFCBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, UPFC, UPFCBatch)
        UPFCBatch.__init__(self, self._api_util, sync_cls_idx=UPFC._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> UPFC:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[UPFCProperties]) -> UPFC:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[UPFCBatchProperties]) -> UPFCBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
