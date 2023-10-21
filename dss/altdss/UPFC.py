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
from .XYcurve import XYcurve

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

class UPFC(DSSObj, CktElementMixin, PCElementMixin):
    __slots__ = []
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

    @property
    def Bus1(self) -> str:
        """
        Name of bus to which the input terminal (1) is connected.
        bus1=busname.1.3
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
        Name of bus to which the output terminal (2) is connected.
        bus2=busname.1.2
        bus2=busname.1.2.3

        DSS property name: `Bus2`, DSS property index: 2.
        """
        return self._get_prop_string(2)

    @Bus2.setter
    def Bus2(self, value: AnyStr):
        self._set_string_o(2, value)

    @property
    def RefkV(self) -> float:
        """
        Base Voltage expected at the output of the UPFC

        "refkv=0.24"

        DSS property name: `RefkV`, DSS property index: 3.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @RefkV.setter
    def RefkV(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def PF(self) -> float:
        """
        Power factor target at the input terminal.

        DSS property name: `PF`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @PF.setter
    def PF(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def Frequency(self) -> float:
        """
        UPFC working frequency.  Defaults to system default base frequency.

        DSS property name: `Frequency`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @Frequency.setter
    def Frequency(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def Phases(self) -> int:
        """
        Number of phases.  Defaults to 1 phase (2 terminals, 1 conductor per terminal).

        DSS property name: `Phases`, DSS property index: 6.
        """
        return self._lib.Obj_GetInt32(self._ptr, 6)

    @Phases.setter
    def Phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 6, value)

    @property
    def Xs(self) -> float:
        """
        Reactance of the series transformer of the UPFC, ohms (default=0.7540 ... 2 mH)

        DSS property name: `Xs`, DSS property index: 7.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @Xs.setter
    def Xs(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def Tol1(self) -> float:
        """
        Tolerance in pu for the series PI controller
        Tol1=0.02 is the format used to define 2% tolerance (Default=2%)

        DSS property name: `Tol1`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @Tol1.setter
    def Tol1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def Mode(self) -> enums.UPFCMode:
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

    @Mode.setter
    def Mode(self, value: Union[int, enums.UPFCMode]):
        self._lib.Obj_SetInt32(self._ptr, 9, value)

    @property
    def VpqMax(self) -> float:
        """
        Maximum voltage (in volts) delivered by the series voltage source (Default = 24 V)

        DSS property name: `VpqMax`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @VpqMax.setter
    def VpqMax(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def LossCurve(self) -> str:
        """
        Name of the XYCurve for describing the losses behavior as a function of the voltage at the input of the UPFC

        DSS property name: `LossCurve`, DSS property index: 11.
        """
        return self._get_prop_string(11)

    @LossCurve.setter
    def LossCurve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(11, value)
            return

        self._set_string_o(11, value)

    @property
    def LossCurve_obj(self) -> XYcurve:
        """
        Name of the XYCurve for describing the losses behavior as a function of the voltage at the input of the UPFC

        DSS property name: `LossCurve`, DSS property index: 11.
        """
        return self._get_obj(11, XYcurve)

    @LossCurve_obj.setter
    def LossCurve_obj(self, value: XYcurve):
        self._set_obj(11, value)

    @property
    def VHLimit(self) -> float:
        """
        High limit for the voltage at the input of the UPFC, if the voltage is above this value the UPFC turns off. This value is specified in Volts (default 300 V)

        DSS property name: `VHLimit`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @VHLimit.setter
    def VHLimit(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def VLLimit(self) -> float:
        """
        low limit for the voltage at the input of the UPFC, if voltage is below this value the UPFC turns off. This value is specified in Volts (default 125 V)

        DSS property name: `VLLimit`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @VLLimit.setter
    def VLLimit(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def CLimit(self) -> float:
        """
        Current Limit for the UPFC, if the current passing through the UPFC is higher than this value the UPFC turns off. This value is specified in Amps (Default 265 A)

        DSS property name: `CLimit`, DSS property index: 14.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @CLimit.setter
    def CLimit(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def refkV2(self) -> float:
        """
        Base Voltage expected at the output of the UPFC for control modes 4 and 5.

        This reference must be lower than refkv, see control modes 4 and 5 for details

        DSS property name: `refkV2`, DSS property index: 15.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @refkV2.setter
    def refkV2(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def kvarLimit(self) -> float:
        """
        Maximum amount of reactive power (kvar) that can be absorbed by the UPFC (Default = 5)

        DSS property name: `kvarLimit`, DSS property index: 16.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    @kvarLimit.setter
    def kvarLimit(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 16, value)

    @property
    def Element(self) -> str:
        """
        The name of the PD element monitored when operating with reactive power compensation. Normally, it should be the PD element immediately upstream the UPFC. The element must be defined including the class, e.g. Line.myline.

        DSS property name: `Element`, DSS property index: 17.
        """
        return self._get_prop_string(17)

    @Element.setter
    def Element(self, value: Union[AnyStr, PDElement]):
        if isinstance(value, DSSObj):
            self._set_obj(17, value)
            return

        self._set_string_o(17, value)

    @property
    def Element_obj(self) -> PDElement:
        """
        The name of the PD element monitored when operating with reactive power compensation. Normally, it should be the PD element immediately upstream the UPFC. The element must be defined including the class, e.g. Line.myline.

        DSS property name: `Element`, DSS property index: 17.
        """
        return self._get_obj(17, PDElement)

    @Element_obj.setter
    def Element_obj(self, value: PDElement):
        self._set_obj(17, value)

    @property
    def Spectrum(self) -> str:
        """
        Name of harmonic spectrum for this source.  Default is "defaultUPFC", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 18.
        """
        return self._get_prop_string(18)

    @Spectrum.setter
    def Spectrum(self, value: Union[AnyStr, SpectrumObj]):
        if isinstance(value, DSSObj):
            self._set_obj(18, value)
            return

        self._set_string_o(18, value)

    @property
    def Spectrum_obj(self) -> SpectrumObj:
        """
        Name of harmonic spectrum for this source.  Default is "defaultUPFC", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 18.
        """
        return self._get_obj(18, SpectrumObj)

    @Spectrum_obj.setter
    def Spectrum_obj(self, value: SpectrumObj):
        self._set_obj(18, value)

    @property
    def BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 19.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    @BaseFreq.setter
    def BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 19, value)

    @property
    def Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 20.
        """
        return self._lib.Obj_GetInt32(self._ptr, 20) != 0

    @Enabled.setter
    def Enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 20, value)

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

class UPFCBatch(DSSBatch):
    _cls_name = 'UPFC'
    _obj_cls = UPFC
    _cls_idx = 36


    @property
    def Bus1(self) -> List[str]:
        """
        Name of bus to which the input terminal (1) is connected.
        bus1=busname.1.3
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
        Name of bus to which the output terminal (2) is connected.
        bus2=busname.1.2
        bus2=busname.1.2.3

        DSS property name: `Bus2`, DSS property index: 2.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 2) 

    @Bus2.setter
    def Bus2(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(2, value)

    @property
    def RefkV(self) -> BatchFloat64ArrayProxy:
        """
        Base Voltage expected at the output of the UPFC

        "refkv=0.24"

        DSS property name: `RefkV`, DSS property index: 3.
        """
        return BatchFloat64ArrayProxy(self, 3)

    @RefkV.setter
    def RefkV(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(3, value)

    @property
    def PF(self) -> BatchFloat64ArrayProxy:
        """
        Power factor target at the input terminal.

        DSS property name: `PF`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    @PF.setter
    def PF(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(4, value)

    @property
    def Frequency(self) -> BatchFloat64ArrayProxy:
        """
        UPFC working frequency.  Defaults to system default base frequency.

        DSS property name: `Frequency`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    @Frequency.setter
    def Frequency(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(5, value)

    @property
    def Phases(self) -> BatchInt32ArrayProxy:
        """
        Number of phases.  Defaults to 1 phase (2 terminals, 1 conductor per terminal).

        DSS property name: `Phases`, DSS property index: 6.
        """
        return BatchInt32ArrayProxy(self, 6)

    @Phases.setter
    def Phases(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(6, value)

    @property
    def Xs(self) -> BatchFloat64ArrayProxy:
        """
        Reactance of the series transformer of the UPFC, ohms (default=0.7540 ... 2 mH)

        DSS property name: `Xs`, DSS property index: 7.
        """
        return BatchFloat64ArrayProxy(self, 7)

    @Xs.setter
    def Xs(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(7, value)

    @property
    def Tol1(self) -> BatchFloat64ArrayProxy:
        """
        Tolerance in pu for the series PI controller
        Tol1=0.02 is the format used to define 2% tolerance (Default=2%)

        DSS property name: `Tol1`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    @Tol1.setter
    def Tol1(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(8, value)

    @property
    def Mode(self) -> BatchInt32ArrayProxy:
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

    @Mode.setter
    def Mode(self, value: Union[int, enums.UPFCMode, Int32Array]):
        self._set_batch_int32_array(9, value)

    @property
    def VpqMax(self) -> BatchFloat64ArrayProxy:
        """
        Maximum voltage (in volts) delivered by the series voltage source (Default = 24 V)

        DSS property name: `VpqMax`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    @VpqMax.setter
    def VpqMax(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(10, value)

    @property
    def LossCurve(self) -> List[str]:
        """
        Name of the XYCurve for describing the losses behavior as a function of the voltage at the input of the UPFC

        DSS property name: `LossCurve`, DSS property index: 11.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 11)

    @LossCurve.setter
    def LossCurve(self, value: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]):
        self._set_batch_obj_prop(11, value)

    @property
    def LossCurve_obj(self) -> List[XYcurve]:
        """
        Name of the XYCurve for describing the losses behavior as a function of the voltage at the input of the UPFC

        DSS property name: `LossCurve`, DSS property index: 11.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 11)

    @LossCurve_obj.setter
    def LossCurve_obj(self, value: XYcurve):
        self._set_batch_string(11, value)

    @property
    def VHLimit(self) -> BatchFloat64ArrayProxy:
        """
        High limit for the voltage at the input of the UPFC, if the voltage is above this value the UPFC turns off. This value is specified in Volts (default 300 V)

        DSS property name: `VHLimit`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    @VHLimit.setter
    def VHLimit(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(12, value)

    @property
    def VLLimit(self) -> BatchFloat64ArrayProxy:
        """
        low limit for the voltage at the input of the UPFC, if voltage is below this value the UPFC turns off. This value is specified in Volts (default 125 V)

        DSS property name: `VLLimit`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    @VLLimit.setter
    def VLLimit(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(13, value)

    @property
    def CLimit(self) -> BatchFloat64ArrayProxy:
        """
        Current Limit for the UPFC, if the current passing through the UPFC is higher than this value the UPFC turns off. This value is specified in Amps (Default 265 A)

        DSS property name: `CLimit`, DSS property index: 14.
        """
        return BatchFloat64ArrayProxy(self, 14)

    @CLimit.setter
    def CLimit(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(14, value)

    @property
    def refkV2(self) -> BatchFloat64ArrayProxy:
        """
        Base Voltage expected at the output of the UPFC for control modes 4 and 5.

        This reference must be lower than refkv, see control modes 4 and 5 for details

        DSS property name: `refkV2`, DSS property index: 15.
        """
        return BatchFloat64ArrayProxy(self, 15)

    @refkV2.setter
    def refkV2(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(15, value)

    @property
    def kvarLimit(self) -> BatchFloat64ArrayProxy:
        """
        Maximum amount of reactive power (kvar) that can be absorbed by the UPFC (Default = 5)

        DSS property name: `kvarLimit`, DSS property index: 16.
        """
        return BatchFloat64ArrayProxy(self, 16)

    @kvarLimit.setter
    def kvarLimit(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(16, value)

    @property
    def Element(self) -> List[str]:
        """
        The name of the PD element monitored when operating with reactive power compensation. Normally, it should be the PD element immediately upstream the UPFC. The element must be defined including the class, e.g. Line.myline.

        DSS property name: `Element`, DSS property index: 17.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 17)

    @Element.setter
    def Element(self, value: Union[AnyStr, PDElement, List[AnyStr], List[PDElement]]):
        self._set_batch_obj_prop(17, value)

    @property
    def Element_obj(self) -> List[PDElement]:
        """
        The name of the PD element monitored when operating with reactive power compensation. Normally, it should be the PD element immediately upstream the UPFC. The element must be defined including the class, e.g. Line.myline.

        DSS property name: `Element`, DSS property index: 17.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 17)

    @Element_obj.setter
    def Element_obj(self, value: PDElement):
        self._set_batch_string(17, value)

    @property
    def Spectrum(self) -> List[str]:
        """
        Name of harmonic spectrum for this source.  Default is "defaultUPFC", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 18.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 18)

    @Spectrum.setter
    def Spectrum(self, value: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]]):
        self._set_batch_obj_prop(18, value)

    @property
    def Spectrum_obj(self) -> List[SpectrumObj]:
        """
        Name of harmonic spectrum for this source.  Default is "defaultUPFC", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 18.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 18)

    @Spectrum_obj.setter
    def Spectrum_obj(self, value: SpectrumObj):
        self._set_batch_string(18, value)

    @property
    def BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 19.
        """
        return BatchFloat64ArrayProxy(self, 19)

    @BaseFreq.setter
    def BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(19, value)

    @property
    def Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 20.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 20)
        ]
    @Enabled.setter
    def Enabled(self, value: bool):
        self._set_batch_int32_array(20, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 21.
        """
        self._set_batch_string(21, value)

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

class IUPFC(IDSSObj):
    def __init__(self, iobj):
        super().__init__(iobj, UPFC, UPFCBatch)

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> UPFC:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[UPFCProperties]) -> UPFC:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[UPFCBatchProperties]) -> UPFCBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)