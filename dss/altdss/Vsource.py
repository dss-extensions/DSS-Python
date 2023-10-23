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
from .LoadShape import LoadShape

class Vsource(DSSObj, CktElementMixin, PCElementMixin):
    __slots__ = CktElementMixin._extra_slots + PCElementMixin._extra_slots
    _cls_name = 'Vsource'
    _cls_idx = 16
    _cls_prop_idx = {
        'bus1': 1,
        'basekv': 2,
        'pu': 3,
        'angle': 4,
        'frequency': 5,
        'phases': 6,
        'mvasc3': 7,
        'mvasc1': 8,
        'x1r1': 9,
        'x0r0': 10,
        'isc3': 11,
        'isc1': 12,
        'r1': 13,
        'x1': 14,
        'r0': 15,
        'x0': 16,
        'scantype': 17,
        'sequence': 18,
        'bus2': 19,
        'z1': 20,
        'z0': 21,
        'z2': 22,
        'puz1': 23,
        'puz0': 24,
        'puz2': 25,
        'basemva': 26,
        'yearly': 27,
        'daily': 28,
        'duty': 29,
        'model': 30,
        'puzideal': 31,
        'spectrum': 32,
        'basefreq': 33,
        'enabled': 34,
        'like': 35,
    }

    @property
    def Bus1(self) -> str:
        """
        Name of bus to which the main terminal (1) is connected.
        bus1=busname
        bus1=busname.1.2.3

        The VSOURCE object is a two-terminal voltage source (thevenin equivalent). Bus2 defaults to Bus1 with all phases connected to ground (node 0) unless previously specified. This is a Yg connection. If you want something different, define the Bus2 property explicitly.

        DSS property name: `Bus1`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    @Bus1.setter
    def Bus1(self, value: AnyStr):
        self._set_string_o(1, value)

    @property
    def BasekV(self) -> float:
        """
        Base Source kV, usually phase-phase (L-L) unless you are making a positive-sequence model or 1-phase modelin which case, it will be phase-neutral (L-N) kV.

        DSS property name: `BasekV`, DSS property index: 2.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 2)

    @BasekV.setter
    def BasekV(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 2, value)

    @property
    def pu(self) -> float:
        """
        Per unit of the base voltage that the source is actually operating at.
        "pu=1.05"

        DSS property name: `pu`, DSS property index: 3.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @pu.setter
    def pu(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def Angle(self) -> float:
        """
        Phase angle in degrees of first phase: e.g.,Angle=10.3

        DSS property name: `Angle`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @Angle.setter
    def Angle(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def Frequency(self) -> float:
        """
        Source frequency.  Defaults to system default base frequency.

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
    def MVASC3(self) -> float:
        """
        MVA Short circuit, 3-phase fault. Default = 2000. Z1 is determined by squaring the base kv and dividing by this value. For single-phase source, this value is not used.

        DSS property name: `MVASC3`, DSS property index: 7.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @MVASC3.setter
    def MVASC3(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def MVASC1(self) -> float:
        """
        MVA Short Circuit, 1-phase fault. Default = 2100. The "single-phase impedance", Zs, is determined by squaring the base kV and dividing by this value. Then Z0 is determined by Z0 = 3Zs - 2Z1.  For 1-phase sources, Zs is used directly. Use X0R0 to define X/R ratio for 1-phase source.

        DSS property name: `MVASC1`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @MVASC1.setter
    def MVASC1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def X1R1(self) -> float:
        """
        Positive-sequence  X/R ratio. Default = 4.

        DSS property name: `X1R1`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @X1R1.setter
    def X1R1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def X0R0(self) -> float:
        """
        Zero-sequence X/R ratio.Default = 3.

        DSS property name: `X0R0`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @X0R0.setter
    def X0R0(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def Isc3(self) -> float:
        """
        Alternate method of defining the source impedance. 
        3-phase short circuit current, amps.  Default is 10000.

        DSS property name: `Isc3`, DSS property index: 11.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @Isc3.setter
    def Isc3(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def Isc1(self) -> float:
        """
        Alternate method of defining the source impedance. 
        single-phase short circuit current, amps.  Default is 10500.

        DSS property name: `Isc1`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @Isc1.setter
    def Isc1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def R1(self) -> float:
        """
        Alternate method of defining the source impedance. 
        Positive-sequence resistance, ohms.  Default is 1.65.

        DSS property name: `R1`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @R1.setter
    def R1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def X1(self) -> float:
        """
        Alternate method of defining the source impedance. 
        Positive-sequence reactance, ohms.  Default is 6.6.

        DSS property name: `X1`, DSS property index: 14.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @X1.setter
    def X1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def R0(self) -> float:
        """
        Alternate method of defining the source impedance. 
        Zero-sequence resistance, ohms.  Default is 1.9.

        DSS property name: `R0`, DSS property index: 15.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @R0.setter
    def R0(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def X0(self) -> float:
        """
        Alternate method of defining the source impedance. 
        Zero-sequence reactance, ohms.  Default is 5.7.

        DSS property name: `X0`, DSS property index: 16.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    @X0.setter
    def X0(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 16, value)

    @property
    def ScanType(self) -> enums.ScanType:
        """
        {pos*| zero | none} Maintain specified sequence for harmonic solution. Default is positive sequence. Otherwise, angle between phases rotates with harmonic.

        DSS property name: `ScanType`, DSS property index: 17.
        """
        return enums.ScanType(self._lib.Obj_GetInt32(self._ptr, 17))

    @ScanType.setter
    def ScanType(self, value: Union[AnyStr, int, enums.ScanType]):
        if not isinstance(value, int):
            self._set_string_o(17, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 17, value)

    @property
    def ScanType_str(self) -> str:
        """
        {pos*| zero | none} Maintain specified sequence for harmonic solution. Default is positive sequence. Otherwise, angle between phases rotates with harmonic.

        DSS property name: `ScanType`, DSS property index: 17.
        """
        return self._get_prop_string(17)

    @ScanType_str.setter
    def ScanType_str(self, value: AnyStr):
        self.ScanType = value

    @property
    def Sequence(self) -> enums.SequenceType:
        """
        {pos*| neg | zero} Set the phase angles for the specified symmetrical component sequence for non-harmonic solution modes. Default is positive sequence. 

        DSS property name: `Sequence`, DSS property index: 18.
        """
        return enums.SequenceType(self._lib.Obj_GetInt32(self._ptr, 18))

    @Sequence.setter
    def Sequence(self, value: Union[AnyStr, int, enums.SequenceType]):
        if not isinstance(value, int):
            self._set_string_o(18, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 18, value)

    @property
    def Sequence_str(self) -> str:
        """
        {pos*| neg | zero} Set the phase angles for the specified symmetrical component sequence for non-harmonic solution modes. Default is positive sequence. 

        DSS property name: `Sequence`, DSS property index: 18.
        """
        return self._get_prop_string(18)

    @Sequence_str.setter
    def Sequence_str(self, value: AnyStr):
        self.Sequence = value

    @property
    def Bus2(self) -> str:
        """
        Name of bus to which 2nd terminal is connected.
        bus2=busname
        bus2=busname.1.2.3

        Default is Bus1.0.0.0 (grounded wye connection)

        DSS property name: `Bus2`, DSS property index: 19.
        """
        return self._get_prop_string(19)

    @Bus2.setter
    def Bus2(self, value: AnyStr):
        self._set_string_o(19, value)

    @property
    def Z2(self) -> complex:
        """
        Negative-sequence equivalent source impedance, ohms, as a 2-element array representing a complex number. Example: 

        Z2=[1, 2]  ! represents 1 + j2 

        Used to define the impedance matrix of the VSOURCE if Z1 is also specified. 

        Note: Z2 defaults to Z1 if it is not specifically defined. If Z2 is not equal to Z1, the impedance matrix is asymmetrical.

        DSS property name: `Z2`, DSS property index: 22.
        """
        return self._get_complex(22)

    @Z2.setter
    def Z2(self, value: complex):
        self._set_complex(22, value)

    @property
    def puZ1(self) -> complex:
        """
        2-element array: e.g., [1  2]. An alternate way to specify Z1. See Z1 property. Per-unit positive-sequence impedance on base of Vsource BasekV and BaseMVA.

        DSS property name: `puZ1`, DSS property index: 23.
        """
        return self._get_complex(23)

    @puZ1.setter
    def puZ1(self, value: complex):
        self._set_complex(23, value)

    @property
    def puZ0(self) -> complex:
        """
        2-element array: e.g., [1  2]. An alternate way to specify Z0. See Z0 property. Per-unit zero-sequence impedance on base of Vsource BasekV and BaseMVA.

        DSS property name: `puZ0`, DSS property index: 24.
        """
        return self._get_complex(24)

    @puZ0.setter
    def puZ0(self, value: complex):
        self._set_complex(24, value)

    @property
    def puZ2(self) -> complex:
        """
        2-element array: e.g., [1  2]. An alternate way to specify Z2. See Z2 property. Per-unit negative-sequence impedance on base of Vsource BasekV and BaseMVA.

        DSS property name: `puZ2`, DSS property index: 25.
        """
        return self._get_complex(25)

    @puZ2.setter
    def puZ2(self, value: complex):
        self._set_complex(25, value)

    @property
    def BaseMVA(self) -> float:
        """
        Default value is 100. Base used to convert values specified with puZ1, puZ0, and puZ2 properties to ohms on kV base specified by BasekV property.

        DSS property name: `BaseMVA`, DSS property index: 26.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 26)

    @BaseMVA.setter
    def BaseMVA(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 26, value)

    @property
    def Yearly(self) -> str:
        """
        LOADSHAPE object to use for the per-unit voltage for YEARLY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual L-N kV.

        Must be previously defined as a LOADSHAPE object. 

        Is set to the Daily load shape when Daily is defined.  The daily load shape is repeated in this case. Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Yearly`, DSS property index: 27.
        """
        return self._get_prop_string(27)

    @Yearly.setter
    def Yearly(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(27, value)
            return

        self._set_string_o(27, value)

    @property
    def Yearly_obj(self) -> LoadShape:
        """
        LOADSHAPE object to use for the per-unit voltage for YEARLY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual L-N kV.

        Must be previously defined as a LOADSHAPE object. 

        Is set to the Daily load shape when Daily is defined.  The daily load shape is repeated in this case. Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Yearly`, DSS property index: 27.
        """
        return self._get_obj(27, LoadShape)

    @Yearly_obj.setter
    def Yearly_obj(self, value: LoadShape):
        self._set_obj(27, value)

    @property
    def Daily(self) -> str:
        """
        LOADSHAPE object to use for the per-unit voltage for DAILY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual L-N kV.

        Must be previously defined as a LOADSHAPE object. 

        Sets Yearly curve if it is not already defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Daily`, DSS property index: 28.
        """
        return self._get_prop_string(28)

    @Daily.setter
    def Daily(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(28, value)
            return

        self._set_string_o(28, value)

    @property
    def Daily_obj(self) -> LoadShape:
        """
        LOADSHAPE object to use for the per-unit voltage for DAILY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual L-N kV.

        Must be previously defined as a LOADSHAPE object. 

        Sets Yearly curve if it is not already defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Daily`, DSS property index: 28.
        """
        return self._get_obj(28, LoadShape)

    @Daily_obj.setter
    def Daily_obj(self, value: LoadShape):
        self._set_obj(28, value)

    @property
    def Duty(self) -> str:
        """
        LOADSHAPE object to use for the per-unit voltage for DUTYCYCLE-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual L-N kV.

        Must be previously defined as a LOADSHAPE object. 

        Defaults to Daily load shape when Daily is defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Duty`, DSS property index: 29.
        """
        return self._get_prop_string(29)

    @Duty.setter
    def Duty(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(29, value)
            return

        self._set_string_o(29, value)

    @property
    def Duty_obj(self) -> LoadShape:
        """
        LOADSHAPE object to use for the per-unit voltage for DUTYCYCLE-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual L-N kV.

        Must be previously defined as a LOADSHAPE object. 

        Defaults to Daily load shape when Daily is defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Duty`, DSS property index: 29.
        """
        return self._get_obj(29, LoadShape)

    @Duty_obj.setter
    def Duty_obj(self, value: LoadShape):
        self._set_obj(29, value)

    @property
    def Model(self) -> enums.VSourceModel:
        """
        {Thevenin* | Ideal}  Specifies whether the Vsource is to be considered a Thevenin short circuit model or a quasi-ideal voltage source. If Thevenin, the Vsource uses the impedances defined for all calculations. If "Ideal", the model uses a small impedance on the diagonal of the impedance matrix for the fundamental base frequency power flow only. Then switches to actual Thevenin model for other frequencies. 

        DSS property name: `Model`, DSS property index: 30.
        """
        return enums.VSourceModel(self._lib.Obj_GetInt32(self._ptr, 30))

    @Model.setter
    def Model(self, value: Union[AnyStr, int, enums.VSourceModel]):
        if not isinstance(value, int):
            self._set_string_o(30, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 30, value)

    @property
    def Model_str(self) -> str:
        """
        {Thevenin* | Ideal}  Specifies whether the Vsource is to be considered a Thevenin short circuit model or a quasi-ideal voltage source. If Thevenin, the Vsource uses the impedances defined for all calculations. If "Ideal", the model uses a small impedance on the diagonal of the impedance matrix for the fundamental base frequency power flow only. Then switches to actual Thevenin model for other frequencies. 

        DSS property name: `Model`, DSS property index: 30.
        """
        return self._get_prop_string(30)

    @Model_str.setter
    def Model_str(self, value: AnyStr):
        self.Model = value

    @property
    def puZIdeal(self) -> complex:
        """
        2-element array: e.g., [1  2]. The pu impedance to use for the quasi-ideal voltage source model. Should be a very small impedances. Default is [1e-6, 0.001]. Per-unit impedance on base of Vsource BasekV and BaseMVA. If too small, solution may not work. Be sure to check the voltage values and powers.

        DSS property name: `puZIdeal`, DSS property index: 31.
        """
        return self._get_complex(31)

    @puZIdeal.setter
    def puZIdeal(self, value: complex):
        self._set_complex(31, value)

    @property
    def Spectrum(self) -> str:
        """
        Name of harmonic spectrum for this source.  Default is "defaultvsource", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 32.
        """
        return self._get_prop_string(32)

    @Spectrum.setter
    def Spectrum(self, value: Union[AnyStr, SpectrumObj]):
        if isinstance(value, DSSObj):
            self._set_obj(32, value)
            return

        self._set_string_o(32, value)

    @property
    def Spectrum_obj(self) -> SpectrumObj:
        """
        Name of harmonic spectrum for this source.  Default is "defaultvsource", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 32.
        """
        return self._get_obj(32, SpectrumObj)

    @Spectrum_obj.setter
    def Spectrum_obj(self, value: SpectrumObj):
        self._set_obj(32, value)

    @property
    def BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 33.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 33)

    @BaseFreq.setter
    def BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 33, value)

    @property
    def Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 34.
        """
        return self._lib.Obj_GetInt32(self._ptr, 34) != 0

    @Enabled.setter
    def Enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 34, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 35.
        """
        self._set_string_o(35, value)


class VsourceProperties(TypedDict):
    Bus1: AnyStr
    BasekV: float
    pu: float
    Angle: float
    Frequency: float
    Phases: int
    MVASC3: float
    MVASC1: float
    X1R1: float
    X0R0: float
    Isc3: float
    Isc1: float
    R1: float
    X1: float
    R0: float
    X0: float
    ScanType: Union[AnyStr, int, enums.ScanType]
    Sequence: Union[AnyStr, int, enums.SequenceType]
    Bus2: AnyStr
    Z2: complex
    puZ1: complex
    puZ0: complex
    puZ2: complex
    BaseMVA: float
    Yearly: Union[AnyStr, LoadShape]
    Daily: Union[AnyStr, LoadShape]
    Duty: Union[AnyStr, LoadShape]
    Model: Union[AnyStr, int, enums.VSourceModel]
    puZIdeal: complex
    Spectrum: Union[AnyStr, SpectrumObj]
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class VsourceBatch(DSSBatch):
    _cls_name = 'Vsource'
    _obj_cls = Vsource
    _cls_idx = 16


    @property
    def Bus1(self) -> List[str]:
        """
        Name of bus to which the main terminal (1) is connected.
        bus1=busname
        bus1=busname.1.2.3

        The VSOURCE object is a two-terminal voltage source (thevenin equivalent). Bus2 defaults to Bus1 with all phases connected to ground (node 0) unless previously specified. This is a Yg connection. If you want something different, define the Bus2 property explicitly.

        DSS property name: `Bus1`, DSS property index: 1.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1) 

    @Bus1.setter
    def Bus1(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(1, value)

    @property
    def BasekV(self) -> BatchFloat64ArrayProxy:
        """
        Base Source kV, usually phase-phase (L-L) unless you are making a positive-sequence model or 1-phase modelin which case, it will be phase-neutral (L-N) kV.

        DSS property name: `BasekV`, DSS property index: 2.
        """
        return BatchFloat64ArrayProxy(self, 2)

    @BasekV.setter
    def BasekV(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(2, value)

    @property
    def pu(self) -> BatchFloat64ArrayProxy:
        """
        Per unit of the base voltage that the source is actually operating at.
        "pu=1.05"

        DSS property name: `pu`, DSS property index: 3.
        """
        return BatchFloat64ArrayProxy(self, 3)

    @pu.setter
    def pu(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(3, value)

    @property
    def Angle(self) -> BatchFloat64ArrayProxy:
        """
        Phase angle in degrees of first phase: e.g.,Angle=10.3

        DSS property name: `Angle`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    @Angle.setter
    def Angle(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(4, value)

    @property
    def Frequency(self) -> BatchFloat64ArrayProxy:
        """
        Source frequency.  Defaults to system default base frequency.

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
    def MVASC3(self) -> BatchFloat64ArrayProxy:
        """
        MVA Short circuit, 3-phase fault. Default = 2000. Z1 is determined by squaring the base kv and dividing by this value. For single-phase source, this value is not used.

        DSS property name: `MVASC3`, DSS property index: 7.
        """
        return BatchFloat64ArrayProxy(self, 7)

    @MVASC3.setter
    def MVASC3(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(7, value)

    @property
    def MVASC1(self) -> BatchFloat64ArrayProxy:
        """
        MVA Short Circuit, 1-phase fault. Default = 2100. The "single-phase impedance", Zs, is determined by squaring the base kV and dividing by this value. Then Z0 is determined by Z0 = 3Zs - 2Z1.  For 1-phase sources, Zs is used directly. Use X0R0 to define X/R ratio for 1-phase source.

        DSS property name: `MVASC1`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    @MVASC1.setter
    def MVASC1(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(8, value)

    @property
    def X1R1(self) -> BatchFloat64ArrayProxy:
        """
        Positive-sequence  X/R ratio. Default = 4.

        DSS property name: `X1R1`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    @X1R1.setter
    def X1R1(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(9, value)

    @property
    def X0R0(self) -> BatchFloat64ArrayProxy:
        """
        Zero-sequence X/R ratio.Default = 3.

        DSS property name: `X0R0`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    @X0R0.setter
    def X0R0(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(10, value)

    @property
    def Isc3(self) -> BatchFloat64ArrayProxy:
        """
        Alternate method of defining the source impedance. 
        3-phase short circuit current, amps.  Default is 10000.

        DSS property name: `Isc3`, DSS property index: 11.
        """
        return BatchFloat64ArrayProxy(self, 11)

    @Isc3.setter
    def Isc3(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(11, value)

    @property
    def Isc1(self) -> BatchFloat64ArrayProxy:
        """
        Alternate method of defining the source impedance. 
        single-phase short circuit current, amps.  Default is 10500.

        DSS property name: `Isc1`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    @Isc1.setter
    def Isc1(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(12, value)

    @property
    def R1(self) -> BatchFloat64ArrayProxy:
        """
        Alternate method of defining the source impedance. 
        Positive-sequence resistance, ohms.  Default is 1.65.

        DSS property name: `R1`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    @R1.setter
    def R1(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(13, value)

    @property
    def X1(self) -> BatchFloat64ArrayProxy:
        """
        Alternate method of defining the source impedance. 
        Positive-sequence reactance, ohms.  Default is 6.6.

        DSS property name: `X1`, DSS property index: 14.
        """
        return BatchFloat64ArrayProxy(self, 14)

    @X1.setter
    def X1(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(14, value)

    @property
    def R0(self) -> BatchFloat64ArrayProxy:
        """
        Alternate method of defining the source impedance. 
        Zero-sequence resistance, ohms.  Default is 1.9.

        DSS property name: `R0`, DSS property index: 15.
        """
        return BatchFloat64ArrayProxy(self, 15)

    @R0.setter
    def R0(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(15, value)

    @property
    def X0(self) -> BatchFloat64ArrayProxy:
        """
        Alternate method of defining the source impedance. 
        Zero-sequence reactance, ohms.  Default is 5.7.

        DSS property name: `X0`, DSS property index: 16.
        """
        return BatchFloat64ArrayProxy(self, 16)

    @X0.setter
    def X0(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(16, value)

    @property
    def ScanType(self) -> BatchInt32ArrayProxy:
        """
        {pos*| zero | none} Maintain specified sequence for harmonic solution. Default is positive sequence. Otherwise, angle between phases rotates with harmonic.

        DSS property name: `ScanType`, DSS property index: 17.
        """
        return BatchInt32ArrayProxy(self, 17)

    @ScanType.setter
    def ScanType(self, value: Union[AnyStr, int, enums.ScanType, List[AnyStr], List[int], List[enums.ScanType], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(17, value)
            return
    
        self._set_batch_int32_array(17, value)

    @property
    def ScanType_str(self) -> str:
        """
        {pos*| zero | none} Maintain specified sequence for harmonic solution. Default is positive sequence. Otherwise, angle between phases rotates with harmonic.

        DSS property name: `ScanType`, DSS property index: 17.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 17)

    @ScanType_str.setter
    def ScanType_str(self, value: AnyStr):
        self.ScanType = value

    @property
    def Sequence(self) -> BatchInt32ArrayProxy:
        """
        {pos*| neg | zero} Set the phase angles for the specified symmetrical component sequence for non-harmonic solution modes. Default is positive sequence. 

        DSS property name: `Sequence`, DSS property index: 18.
        """
        return BatchInt32ArrayProxy(self, 18)

    @Sequence.setter
    def Sequence(self, value: Union[AnyStr, int, enums.SequenceType, List[AnyStr], List[int], List[enums.SequenceType], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(18, value)
            return
    
        self._set_batch_int32_array(18, value)

    @property
    def Sequence_str(self) -> str:
        """
        {pos*| neg | zero} Set the phase angles for the specified symmetrical component sequence for non-harmonic solution modes. Default is positive sequence. 

        DSS property name: `Sequence`, DSS property index: 18.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 18)

    @Sequence_str.setter
    def Sequence_str(self, value: AnyStr):
        self.Sequence = value

    @property
    def Bus2(self) -> List[str]:
        """
        Name of bus to which 2nd terminal is connected.
        bus2=busname
        bus2=busname.1.2.3

        Default is Bus1.0.0.0 (grounded wye connection)

        DSS property name: `Bus2`, DSS property index: 19.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 19) 

    @Bus2.setter
    def Bus2(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(19, value)

    @property
    def Z2(self) -> List[complex]:
        """
        Negative-sequence equivalent source impedance, ohms, as a 2-element array representing a complex number. Example: 

        Z2=[1, 2]  ! represents 1 + j2 

        Used to define the impedance matrix of the VSOURCE if Z1 is also specified. 

        Note: Z2 defaults to Z1 if it is not specifically defined. If Z2 is not equal to Z1, the impedance matrix is asymmetrical.

        DSS property name: `Z2`, DSS property index: 22.
        """
        return [   
            self._get_float64_array(
                self._lib.Obj_GetFloat64Array, 
                x,
                22,
            ).view(dtype=complex)[0]
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Z2.setter
    def Z2(self, value: Union[complex, List[complex]]):
        if isinstance(value, complex):
            value, value_ptr, value_count = self._prepare_float64_array([value.real, value.imag])
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetFloat64Array(x, 22, value_ptr, value_count)
            return

        values = value
        if len(values) != self.count[0]:
            raise ValueError('Number of elements provided must match the number of objects in the batch.')

        value, value_ptr, value_count = self._prepare_float64_array([0, 0])
        for v, x in zip(values, self._ffi.unpack(self.pointer[0], self.count[0])):
            value[0] = v.real
            value[1] = v.imag
            self._lib.Obj_SetFloat64Array(x, 22, value_ptr, value_count)

    @property
    def puZ1(self) -> List[complex]:
        """
        2-element array: e.g., [1  2]. An alternate way to specify Z1. See Z1 property. Per-unit positive-sequence impedance on base of Vsource BasekV and BaseMVA.

        DSS property name: `puZ1`, DSS property index: 23.
        """
        return [   
            self._get_float64_array(
                self._lib.Obj_GetFloat64Array, 
                x,
                23,
            ).view(dtype=complex)[0]
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @puZ1.setter
    def puZ1(self, value: Union[complex, List[complex]]):
        if isinstance(value, complex):
            value, value_ptr, value_count = self._prepare_float64_array([value.real, value.imag])
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetFloat64Array(x, 23, value_ptr, value_count)
            return

        values = value
        if len(values) != self.count[0]:
            raise ValueError('Number of elements provided must match the number of objects in the batch.')

        value, value_ptr, value_count = self._prepare_float64_array([0, 0])
        for v, x in zip(values, self._ffi.unpack(self.pointer[0], self.count[0])):
            value[0] = v.real
            value[1] = v.imag
            self._lib.Obj_SetFloat64Array(x, 23, value_ptr, value_count)

    @property
    def puZ0(self) -> List[complex]:
        """
        2-element array: e.g., [1  2]. An alternate way to specify Z0. See Z0 property. Per-unit zero-sequence impedance on base of Vsource BasekV and BaseMVA.

        DSS property name: `puZ0`, DSS property index: 24.
        """
        return [   
            self._get_float64_array(
                self._lib.Obj_GetFloat64Array, 
                x,
                24,
            ).view(dtype=complex)[0]
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @puZ0.setter
    def puZ0(self, value: Union[complex, List[complex]]):
        if isinstance(value, complex):
            value, value_ptr, value_count = self._prepare_float64_array([value.real, value.imag])
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetFloat64Array(x, 24, value_ptr, value_count)
            return

        values = value
        if len(values) != self.count[0]:
            raise ValueError('Number of elements provided must match the number of objects in the batch.')

        value, value_ptr, value_count = self._prepare_float64_array([0, 0])
        for v, x in zip(values, self._ffi.unpack(self.pointer[0], self.count[0])):
            value[0] = v.real
            value[1] = v.imag
            self._lib.Obj_SetFloat64Array(x, 24, value_ptr, value_count)

    @property
    def puZ2(self) -> List[complex]:
        """
        2-element array: e.g., [1  2]. An alternate way to specify Z2. See Z2 property. Per-unit negative-sequence impedance on base of Vsource BasekV and BaseMVA.

        DSS property name: `puZ2`, DSS property index: 25.
        """
        return [   
            self._get_float64_array(
                self._lib.Obj_GetFloat64Array, 
                x,
                25,
            ).view(dtype=complex)[0]
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @puZ2.setter
    def puZ2(self, value: Union[complex, List[complex]]):
        if isinstance(value, complex):
            value, value_ptr, value_count = self._prepare_float64_array([value.real, value.imag])
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetFloat64Array(x, 25, value_ptr, value_count)
            return

        values = value
        if len(values) != self.count[0]:
            raise ValueError('Number of elements provided must match the number of objects in the batch.')

        value, value_ptr, value_count = self._prepare_float64_array([0, 0])
        for v, x in zip(values, self._ffi.unpack(self.pointer[0], self.count[0])):
            value[0] = v.real
            value[1] = v.imag
            self._lib.Obj_SetFloat64Array(x, 25, value_ptr, value_count)

    @property
    def BaseMVA(self) -> BatchFloat64ArrayProxy:
        """
        Default value is 100. Base used to convert values specified with puZ1, puZ0, and puZ2 properties to ohms on kV base specified by BasekV property.

        DSS property name: `BaseMVA`, DSS property index: 26.
        """
        return BatchFloat64ArrayProxy(self, 26)

    @BaseMVA.setter
    def BaseMVA(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(26, value)

    @property
    def Yearly(self) -> List[str]:
        """
        LOADSHAPE object to use for the per-unit voltage for YEARLY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual L-N kV.

        Must be previously defined as a LOADSHAPE object. 

        Is set to the Daily load shape when Daily is defined.  The daily load shape is repeated in this case. Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Yearly`, DSS property index: 27.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 27)

    @Yearly.setter
    def Yearly(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]):
        self._set_batch_obj_prop(27, value)

    @property
    def Yearly_obj(self) -> List[LoadShape]:
        """
        LOADSHAPE object to use for the per-unit voltage for YEARLY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual L-N kV.

        Must be previously defined as a LOADSHAPE object. 

        Is set to the Daily load shape when Daily is defined.  The daily load shape is repeated in this case. Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Yearly`, DSS property index: 27.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 27)

    @Yearly_obj.setter
    def Yearly_obj(self, value: LoadShape):
        self._set_batch_string(27, value)

    @property
    def Daily(self) -> List[str]:
        """
        LOADSHAPE object to use for the per-unit voltage for DAILY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual L-N kV.

        Must be previously defined as a LOADSHAPE object. 

        Sets Yearly curve if it is not already defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Daily`, DSS property index: 28.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 28)

    @Daily.setter
    def Daily(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]):
        self._set_batch_obj_prop(28, value)

    @property
    def Daily_obj(self) -> List[LoadShape]:
        """
        LOADSHAPE object to use for the per-unit voltage for DAILY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual L-N kV.

        Must be previously defined as a LOADSHAPE object. 

        Sets Yearly curve if it is not already defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Daily`, DSS property index: 28.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 28)

    @Daily_obj.setter
    def Daily_obj(self, value: LoadShape):
        self._set_batch_string(28, value)

    @property
    def Duty(self) -> List[str]:
        """
        LOADSHAPE object to use for the per-unit voltage for DUTYCYCLE-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual L-N kV.

        Must be previously defined as a LOADSHAPE object. 

        Defaults to Daily load shape when Daily is defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Duty`, DSS property index: 29.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 29)

    @Duty.setter
    def Duty(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]):
        self._set_batch_obj_prop(29, value)

    @property
    def Duty_obj(self) -> List[LoadShape]:
        """
        LOADSHAPE object to use for the per-unit voltage for DUTYCYCLE-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual L-N kV.

        Must be previously defined as a LOADSHAPE object. 

        Defaults to Daily load shape when Daily is defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Duty`, DSS property index: 29.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 29)

    @Duty_obj.setter
    def Duty_obj(self, value: LoadShape):
        self._set_batch_string(29, value)

    @property
    def Model(self) -> BatchInt32ArrayProxy:
        """
        {Thevenin* | Ideal}  Specifies whether the Vsource is to be considered a Thevenin short circuit model or a quasi-ideal voltage source. If Thevenin, the Vsource uses the impedances defined for all calculations. If "Ideal", the model uses a small impedance on the diagonal of the impedance matrix for the fundamental base frequency power flow only. Then switches to actual Thevenin model for other frequencies. 

        DSS property name: `Model`, DSS property index: 30.
        """
        return BatchInt32ArrayProxy(self, 30)

    @Model.setter
    def Model(self, value: Union[AnyStr, int, enums.VSourceModel, List[AnyStr], List[int], List[enums.VSourceModel], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(30, value)
            return
    
        self._set_batch_int32_array(30, value)

    @property
    def Model_str(self) -> str:
        """
        {Thevenin* | Ideal}  Specifies whether the Vsource is to be considered a Thevenin short circuit model or a quasi-ideal voltage source. If Thevenin, the Vsource uses the impedances defined for all calculations. If "Ideal", the model uses a small impedance on the diagonal of the impedance matrix for the fundamental base frequency power flow only. Then switches to actual Thevenin model for other frequencies. 

        DSS property name: `Model`, DSS property index: 30.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 30)

    @Model_str.setter
    def Model_str(self, value: AnyStr):
        self.Model = value

    @property
    def puZIdeal(self) -> List[complex]:
        """
        2-element array: e.g., [1  2]. The pu impedance to use for the quasi-ideal voltage source model. Should be a very small impedances. Default is [1e-6, 0.001]. Per-unit impedance on base of Vsource BasekV and BaseMVA. If too small, solution may not work. Be sure to check the voltage values and powers.

        DSS property name: `puZIdeal`, DSS property index: 31.
        """
        return [   
            self._get_float64_array(
                self._lib.Obj_GetFloat64Array, 
                x,
                31,
            ).view(dtype=complex)[0]
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @puZIdeal.setter
    def puZIdeal(self, value: Union[complex, List[complex]]):
        if isinstance(value, complex):
            value, value_ptr, value_count = self._prepare_float64_array([value.real, value.imag])
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetFloat64Array(x, 31, value_ptr, value_count)
            return

        values = value
        if len(values) != self.count[0]:
            raise ValueError('Number of elements provided must match the number of objects in the batch.')

        value, value_ptr, value_count = self._prepare_float64_array([0, 0])
        for v, x in zip(values, self._ffi.unpack(self.pointer[0], self.count[0])):
            value[0] = v.real
            value[1] = v.imag
            self._lib.Obj_SetFloat64Array(x, 31, value_ptr, value_count)

    @property
    def Spectrum(self) -> List[str]:
        """
        Name of harmonic spectrum for this source.  Default is "defaultvsource", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 32.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 32)

    @Spectrum.setter
    def Spectrum(self, value: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]]):
        self._set_batch_obj_prop(32, value)

    @property
    def Spectrum_obj(self) -> List[SpectrumObj]:
        """
        Name of harmonic spectrum for this source.  Default is "defaultvsource", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 32.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 32)

    @Spectrum_obj.setter
    def Spectrum_obj(self, value: SpectrumObj):
        self._set_batch_string(32, value)

    @property
    def BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 33.
        """
        return BatchFloat64ArrayProxy(self, 33)

    @BaseFreq.setter
    def BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(33, value)

    @property
    def Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 34.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 34)
        ]
    @Enabled.setter
    def Enabled(self, value: bool):
        self._set_batch_int32_array(34, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 35.
        """
        self._set_batch_string(35, value)

class VsourceBatchProperties(TypedDict):
    Bus1: Union[AnyStr, List[AnyStr]]
    BasekV: Union[float, Float64Array]
    pu: Union[float, Float64Array]
    Angle: Union[float, Float64Array]
    Frequency: Union[float, Float64Array]
    Phases: Union[int, Int32Array]
    MVASC3: Union[float, Float64Array]
    MVASC1: Union[float, Float64Array]
    X1R1: Union[float, Float64Array]
    X0R0: Union[float, Float64Array]
    Isc3: Union[float, Float64Array]
    Isc1: Union[float, Float64Array]
    R1: Union[float, Float64Array]
    X1: Union[float, Float64Array]
    R0: Union[float, Float64Array]
    X0: Union[float, Float64Array]
    ScanType: Union[AnyStr, int, enums.ScanType, List[AnyStr], List[int], List[enums.ScanType], Int32Array]
    Sequence: Union[AnyStr, int, enums.SequenceType, List[AnyStr], List[int], List[enums.SequenceType], Int32Array]
    Bus2: Union[AnyStr, List[AnyStr]]
    Z2: Union[complex, List[complex]]
    puZ1: Union[complex, List[complex]]
    puZ0: Union[complex, List[complex]]
    puZ2: Union[complex, List[complex]]
    BaseMVA: Union[float, Float64Array]
    Yearly: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    Daily: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    Duty: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    Model: Union[AnyStr, int, enums.VSourceModel, List[AnyStr], List[int], List[enums.VSourceModel], Int32Array]
    puZIdeal: Union[complex, List[complex]]
    Spectrum: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IVsource(IDSSObj):
    __slots__ = ()

    def __init__(self, iobj):
        super().__init__(iobj, Vsource, VsourceBatch)

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Vsource:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[VsourceProperties]) -> Vsource:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[VsourceBatchProperties]) -> VsourceBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
