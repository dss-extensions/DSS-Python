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
from .PCElement import PCElementBatchMixin, PCElementMixin
from .CircuitElement import CircuitElementBatchMixin, CircuitElementMixin
from .LoadShape import LoadShape
from .Spectrum import Spectrum as SpectrumObj

class Vsource(DSSObj, CircuitElementMixin, PCElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots + PCElementMixin._extra_slots
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

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)
       PCElementMixin.__init__(self)

    def _get_Bus1(self) -> str:
        """
        Name of bus to which the main terminal (1) is connected.
        bus1=busname
        bus1=busname.1.2.3

        The VSOURCE object is a two-terminal voltage source (thevenin equivalent). Bus2 defaults to Bus1 with all phases connected to ground (node 0) unless previously specified. This is a Yg connection. If you want something different, define the Bus2 property explicitly.

        DSS property name: `Bus1`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    def _set_Bus1(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(1, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: str

    def _get_BasekV(self) -> float:
        """
        Base Source kV, usually phase-phase (L-L) unless you are making a positive-sequence model or 1-phase modelin which case, it will be phase-neutral (L-N) kV.

        DSS property name: `BasekV`, DSS property index: 2.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 2)

    def _set_BasekV(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 2, value, flags)

    BasekV = property(_get_BasekV, _set_BasekV) # type: float

    def _get_pu(self) -> float:
        """
        Per unit of the base voltage that the source is actually operating at.
        "pu=1.05"

        DSS property name: `pu`, DSS property index: 3.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    def _set_pu(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 3, value, flags)

    pu = property(_get_pu, _set_pu) # type: float

    def _get_Angle(self) -> float:
        """
        Phase angle in degrees of first phase: e.g.,Angle=10.3

        DSS property name: `Angle`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    def _set_Angle(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 4, value, flags)

    Angle = property(_get_Angle, _set_Angle) # type: float

    def _get_Frequency(self) -> float:
        """
        Source frequency.  Defaults to system default base frequency.

        DSS property name: `Frequency`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    def _set_Frequency(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 5, value, flags)

    Frequency = property(_get_Frequency, _set_Frequency) # type: float

    def _get_Phases(self) -> int:
        """
        Number of phases.  Defaults to 3.

        DSS property name: `Phases`, DSS property index: 6.
        """
        return self._lib.Obj_GetInt32(self._ptr, 6)

    def _set_Phases(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 6, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: int

    def _get_MVASC3(self) -> float:
        """
        MVA Short circuit, 3-phase fault. Default = 2000. Z1 is determined by squaring the base kv and dividing by this value. For single-phase source, this value is not used.

        DSS property name: `MVASC3`, DSS property index: 7.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    def _set_MVASC3(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 7, value, flags)

    MVASC3 = property(_get_MVASC3, _set_MVASC3) # type: float

    def _get_MVASC1(self) -> float:
        """
        MVA Short Circuit, 1-phase fault. Default = 2100. The "single-phase impedance", Zs, is determined by squaring the base kV and dividing by this value. Then Z0 is determined by Z0 = 3Zs - 2Z1.  For 1-phase sources, Zs is used directly. Use X0R0 to define X/R ratio for 1-phase source.

        DSS property name: `MVASC1`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    def _set_MVASC1(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 8, value, flags)

    MVASC1 = property(_get_MVASC1, _set_MVASC1) # type: float

    def _get_X1R1(self) -> float:
        """
        Positive-sequence  X/R ratio. Default = 4.

        DSS property name: `X1R1`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    def _set_X1R1(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 9, value, flags)

    X1R1 = property(_get_X1R1, _set_X1R1) # type: float

    def _get_X0R0(self) -> float:
        """
        Zero-sequence X/R ratio.Default = 3.

        DSS property name: `X0R0`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    def _set_X0R0(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 10, value, flags)

    X0R0 = property(_get_X0R0, _set_X0R0) # type: float

    def _get_Isc3(self) -> float:
        """
        Alternate method of defining the source impedance. 
        3-phase short circuit current, amps.  Default is 10000.

        DSS property name: `Isc3`, DSS property index: 11.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    def _set_Isc3(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 11, value, flags)

    Isc3 = property(_get_Isc3, _set_Isc3) # type: float

    def _get_Isc1(self) -> float:
        """
        Alternate method of defining the source impedance. 
        single-phase short circuit current, amps.  Default is 10500.

        DSS property name: `Isc1`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    def _set_Isc1(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 12, value, flags)

    Isc1 = property(_get_Isc1, _set_Isc1) # type: float

    def _get_R1(self) -> float:
        """
        Alternate method of defining the source impedance. 
        Positive-sequence resistance, ohms.  Default is 1.65.

        DSS property name: `R1`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    def _set_R1(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 13, value, flags)

    R1 = property(_get_R1, _set_R1) # type: float

    def _get_X1(self) -> float:
        """
        Alternate method of defining the source impedance. 
        Positive-sequence reactance, ohms.  Default is 6.6.

        DSS property name: `X1`, DSS property index: 14.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    def _set_X1(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 14, value, flags)

    X1 = property(_get_X1, _set_X1) # type: float

    def _get_R0(self) -> float:
        """
        Alternate method of defining the source impedance. 
        Zero-sequence resistance, ohms.  Default is 1.9.

        DSS property name: `R0`, DSS property index: 15.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    def _set_R0(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 15, value, flags)

    R0 = property(_get_R0, _set_R0) # type: float

    def _get_X0(self) -> float:
        """
        Alternate method of defining the source impedance. 
        Zero-sequence reactance, ohms.  Default is 5.7.

        DSS property name: `X0`, DSS property index: 16.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    def _set_X0(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 16, value, flags)

    X0 = property(_get_X0, _set_X0) # type: float

    def _get_ScanType(self) -> enums.ScanType:
        """
        {pos*| zero | none} Maintain specified sequence for harmonic solution. Default is positive sequence. Otherwise, angle between phases rotates with harmonic.

        DSS property name: `ScanType`, DSS property index: 17.
        """
        return enums.ScanType(self._lib.Obj_GetInt32(self._ptr, 17))

    def _set_ScanType(self, value: Union[AnyStr, int, enums.ScanType], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(17, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 17, value, flags)

    ScanType = property(_get_ScanType, _set_ScanType) # type: enums.ScanType

    def _get_ScanType_str(self) -> str:
        """
        {pos*| zero | none} Maintain specified sequence for harmonic solution. Default is positive sequence. Otherwise, angle between phases rotates with harmonic.

        DSS property name: `ScanType`, DSS property index: 17.
        """
        return self._get_prop_string(17)

    def _set_ScanType_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_ScanType(value, flags)

    ScanType_str = property(_get_ScanType_str, _set_ScanType_str) # type: str

    def _get_Sequence(self) -> enums.SequenceType:
        """
        {pos*| neg | zero} Set the phase angles for the specified symmetrical component sequence for non-harmonic solution modes. Default is positive sequence. 

        DSS property name: `Sequence`, DSS property index: 18.
        """
        return enums.SequenceType(self._lib.Obj_GetInt32(self._ptr, 18))

    def _set_Sequence(self, value: Union[AnyStr, int, enums.SequenceType], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(18, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 18, value, flags)

    Sequence = property(_get_Sequence, _set_Sequence) # type: enums.SequenceType

    def _get_Sequence_str(self) -> str:
        """
        {pos*| neg | zero} Set the phase angles for the specified symmetrical component sequence for non-harmonic solution modes. Default is positive sequence. 

        DSS property name: `Sequence`, DSS property index: 18.
        """
        return self._get_prop_string(18)

    def _set_Sequence_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Sequence(value, flags)

    Sequence_str = property(_get_Sequence_str, _set_Sequence_str) # type: str

    def _get_Bus2(self) -> str:
        """
        Name of bus to which 2nd terminal is connected.
        bus2=busname
        bus2=busname.1.2.3

        Default is Bus1.0.0.0 (grounded wye connection)

        DSS property name: `Bus2`, DSS property index: 19.
        """
        return self._get_prop_string(19)

    def _set_Bus2(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(19, value, flags)

    Bus2 = property(_get_Bus2, _set_Bus2) # type: str

    def _get_Z2(self) -> complex:
        """
        Negative-sequence equivalent source impedance, ohms, as a 2-element array representing a complex number. Example: 

        Z2=[1, 2]  ! represents 1 + j2 

        Used to define the impedance matrix of the VSOURCE if Z1 is also specified. 

        Note: Z2 defaults to Z1 if it is not specifically defined. If Z2 is not equal to Z1, the impedance matrix is asymmetrical.

        DSS property name: `Z2`, DSS property index: 22.
        """
        return self._get_complex(22)

    def _set_Z2(self, value: complex, flags: enums.SetterFlags = 0):
        self._set_complex(22, value, flags)

    Z2 = property(_get_Z2, _set_Z2) # type: complex

    def _get_puZ1(self) -> complex:
        """
        2-element array: e.g., [1  2]. An alternate way to specify Z1. See Z1 property. Per-unit positive-sequence impedance on base of Vsource BasekV and BaseMVA.

        DSS property name: `puZ1`, DSS property index: 23.
        """
        return self._get_complex(23)

    def _set_puZ1(self, value: complex, flags: enums.SetterFlags = 0):
        self._set_complex(23, value, flags)

    puZ1 = property(_get_puZ1, _set_puZ1) # type: complex

    def _get_puZ0(self) -> complex:
        """
        2-element array: e.g., [1  2]. An alternate way to specify Z0. See Z0 property. Per-unit zero-sequence impedance on base of Vsource BasekV and BaseMVA.

        DSS property name: `puZ0`, DSS property index: 24.
        """
        return self._get_complex(24)

    def _set_puZ0(self, value: complex, flags: enums.SetterFlags = 0):
        self._set_complex(24, value, flags)

    puZ0 = property(_get_puZ0, _set_puZ0) # type: complex

    def _get_puZ2(self) -> complex:
        """
        2-element array: e.g., [1  2]. An alternate way to specify Z2. See Z2 property. Per-unit negative-sequence impedance on base of Vsource BasekV and BaseMVA.

        DSS property name: `puZ2`, DSS property index: 25.
        """
        return self._get_complex(25)

    def _set_puZ2(self, value: complex, flags: enums.SetterFlags = 0):
        self._set_complex(25, value, flags)

    puZ2 = property(_get_puZ2, _set_puZ2) # type: complex

    def _get_BaseMVA(self) -> float:
        """
        Default value is 100. Base used to convert values specified with puZ1, puZ0, and puZ2 properties to ohms on kV base specified by BasekV property.

        DSS property name: `BaseMVA`, DSS property index: 26.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 26)

    def _set_BaseMVA(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 26, value, flags)

    BaseMVA = property(_get_BaseMVA, _set_BaseMVA) # type: float

    def _get_Yearly_str(self) -> str:
        """
        LOADSHAPE object to use for the per-unit voltage for YEARLY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual L-N kV.

        Must be previously defined as a LOADSHAPE object. 

        Is set to the Daily load shape when Daily is defined.  The daily load shape is repeated in this case. Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Yearly`, DSS property index: 27.
        """
        return self._get_prop_string(27)

    def _set_Yearly_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(27, value, flags)

    Yearly_str = property(_get_Yearly_str, _set_Yearly_str) # type: str

    def _get_Yearly(self) -> LoadShape:
        """
        LOADSHAPE object to use for the per-unit voltage for YEARLY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual L-N kV.

        Must be previously defined as a LOADSHAPE object. 

        Is set to the Daily load shape when Daily is defined.  The daily load shape is repeated in this case. Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Yearly`, DSS property index: 27.
        """
        return self._get_obj(27, LoadShape)

    def _set_Yearly(self, value: Union[AnyStr, LoadShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(27, value, flags)
            return

        self._set_string_o(27, value, flags)

    Yearly = property(_get_Yearly, _set_Yearly) # type: LoadShape

    def _get_Daily_str(self) -> str:
        """
        LOADSHAPE object to use for the per-unit voltage for DAILY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual L-N kV.

        Must be previously defined as a LOADSHAPE object. 

        Sets Yearly curve if it is not already defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Daily`, DSS property index: 28.
        """
        return self._get_prop_string(28)

    def _set_Daily_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(28, value, flags)

    Daily_str = property(_get_Daily_str, _set_Daily_str) # type: str

    def _get_Daily(self) -> LoadShape:
        """
        LOADSHAPE object to use for the per-unit voltage for DAILY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual L-N kV.

        Must be previously defined as a LOADSHAPE object. 

        Sets Yearly curve if it is not already defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Daily`, DSS property index: 28.
        """
        return self._get_obj(28, LoadShape)

    def _set_Daily(self, value: Union[AnyStr, LoadShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(28, value, flags)
            return

        self._set_string_o(28, value, flags)

    Daily = property(_get_Daily, _set_Daily) # type: LoadShape

    def _get_Duty_str(self) -> str:
        """
        LOADSHAPE object to use for the per-unit voltage for DUTYCYCLE-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual L-N kV.

        Must be previously defined as a LOADSHAPE object. 

        Defaults to Daily load shape when Daily is defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Duty`, DSS property index: 29.
        """
        return self._get_prop_string(29)

    def _set_Duty_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(29, value, flags)

    Duty_str = property(_get_Duty_str, _set_Duty_str) # type: str

    def _get_Duty(self) -> LoadShape:
        """
        LOADSHAPE object to use for the per-unit voltage for DUTYCYCLE-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual L-N kV.

        Must be previously defined as a LOADSHAPE object. 

        Defaults to Daily load shape when Daily is defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Duty`, DSS property index: 29.
        """
        return self._get_obj(29, LoadShape)

    def _set_Duty(self, value: Union[AnyStr, LoadShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(29, value, flags)
            return

        self._set_string_o(29, value, flags)

    Duty = property(_get_Duty, _set_Duty) # type: LoadShape

    def _get_Model(self) -> enums.VSourceModel:
        """
        {Thevenin* | Ideal}  Specifies whether the Vsource is to be considered a Thevenin short circuit model or a quasi-ideal voltage source. If Thevenin, the Vsource uses the impedances defined for all calculations. If "Ideal", the model uses a small impedance on the diagonal of the impedance matrix for the fundamental base frequency power flow only. Then switches to actual Thevenin model for other frequencies. 

        DSS property name: `Model`, DSS property index: 30.
        """
        return enums.VSourceModel(self._lib.Obj_GetInt32(self._ptr, 30))

    def _set_Model(self, value: Union[AnyStr, int, enums.VSourceModel], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(30, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 30, value, flags)

    Model = property(_get_Model, _set_Model) # type: enums.VSourceModel

    def _get_Model_str(self) -> str:
        """
        {Thevenin* | Ideal}  Specifies whether the Vsource is to be considered a Thevenin short circuit model or a quasi-ideal voltage source. If Thevenin, the Vsource uses the impedances defined for all calculations. If "Ideal", the model uses a small impedance on the diagonal of the impedance matrix for the fundamental base frequency power flow only. Then switches to actual Thevenin model for other frequencies. 

        DSS property name: `Model`, DSS property index: 30.
        """
        return self._get_prop_string(30)

    def _set_Model_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Model(value, flags)

    Model_str = property(_get_Model_str, _set_Model_str) # type: str

    def _get_puZIdeal(self) -> complex:
        """
        2-element array: e.g., [1  2]. The pu impedance to use for the quasi-ideal voltage source model. Should be a very small impedances. Default is [1e-6, 0.001]. Per-unit impedance on base of Vsource BasekV and BaseMVA. If too small, solution may not work. Be sure to check the voltage values and powers.

        DSS property name: `puZIdeal`, DSS property index: 31.
        """
        return self._get_complex(31)

    def _set_puZIdeal(self, value: complex, flags: enums.SetterFlags = 0):
        self._set_complex(31, value, flags)

    puZIdeal = property(_get_puZIdeal, _set_puZIdeal) # type: complex

    def _get_Spectrum_str(self) -> str:
        """
        Name of harmonic spectrum for this source.  Default is "defaultvsource", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 32.
        """
        return self._get_prop_string(32)

    def _set_Spectrum_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(32, value, flags)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str) # type: str

    def _get_Spectrum(self) -> SpectrumObj:
        """
        Name of harmonic spectrum for this source.  Default is "defaultvsource", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 32.
        """
        return self._get_obj(32, SpectrumObj)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(32, value, flags)
            return

        self._set_string_o(32, value, flags)

    Spectrum = property(_get_Spectrum, _set_Spectrum) # type: SpectrumObj

    def _get_BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 33.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 33)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 33, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float

    def _get_Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 34.
        """
        return self._lib.Obj_GetInt32(self._ptr, 34) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 34, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool

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

class VsourceBatch(DSSBatch, CircuitElementBatchMixin, PCElementBatchMixin):
    _cls_name = 'Vsource'
    _obj_cls = Vsource
    _cls_idx = 16

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)
       PCElementBatchMixin.__init__(self)

    def _get_Bus1(self) -> List[str]:
        """
        Name of bus to which the main terminal (1) is connected.
        bus1=busname
        bus1=busname.1.2.3

        The VSOURCE object is a two-terminal voltage source (thevenin equivalent). Bus2 defaults to Bus1 with all phases connected to ground (node 0) unless previously specified. This is a Yg connection. If you want something different, define the Bus2 property explicitly.

        DSS property name: `Bus1`, DSS property index: 1.
        """
        return self._get_batch_str_prop(1)

    def _set_Bus1(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(1, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: List[str]

    def _get_BasekV(self) -> BatchFloat64ArrayProxy:
        """
        Base Source kV, usually phase-phase (L-L) unless you are making a positive-sequence model or 1-phase modelin which case, it will be phase-neutral (L-N) kV.

        DSS property name: `BasekV`, DSS property index: 2.
        """
        return BatchFloat64ArrayProxy(self, 2)

    def _set_BasekV(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(2, value, flags)

    BasekV = property(_get_BasekV, _set_BasekV) # type: BatchFloat64ArrayProxy

    def _get_pu(self) -> BatchFloat64ArrayProxy:
        """
        Per unit of the base voltage that the source is actually operating at.
        "pu=1.05"

        DSS property name: `pu`, DSS property index: 3.
        """
        return BatchFloat64ArrayProxy(self, 3)

    def _set_pu(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(3, value, flags)

    pu = property(_get_pu, _set_pu) # type: BatchFloat64ArrayProxy

    def _get_Angle(self) -> BatchFloat64ArrayProxy:
        """
        Phase angle in degrees of first phase: e.g.,Angle=10.3

        DSS property name: `Angle`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    def _set_Angle(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(4, value, flags)

    Angle = property(_get_Angle, _set_Angle) # type: BatchFloat64ArrayProxy

    def _get_Frequency(self) -> BatchFloat64ArrayProxy:
        """
        Source frequency.  Defaults to system default base frequency.

        DSS property name: `Frequency`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    def _set_Frequency(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(5, value, flags)

    Frequency = property(_get_Frequency, _set_Frequency) # type: BatchFloat64ArrayProxy

    def _get_Phases(self) -> BatchInt32ArrayProxy:
        """
        Number of phases.  Defaults to 3.

        DSS property name: `Phases`, DSS property index: 6.
        """
        return BatchInt32ArrayProxy(self, 6)

    def _set_Phases(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(6, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: BatchInt32ArrayProxy

    def _get_MVASC3(self) -> BatchFloat64ArrayProxy:
        """
        MVA Short circuit, 3-phase fault. Default = 2000. Z1 is determined by squaring the base kv and dividing by this value. For single-phase source, this value is not used.

        DSS property name: `MVASC3`, DSS property index: 7.
        """
        return BatchFloat64ArrayProxy(self, 7)

    def _set_MVASC3(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(7, value, flags)

    MVASC3 = property(_get_MVASC3, _set_MVASC3) # type: BatchFloat64ArrayProxy

    def _get_MVASC1(self) -> BatchFloat64ArrayProxy:
        """
        MVA Short Circuit, 1-phase fault. Default = 2100. The "single-phase impedance", Zs, is determined by squaring the base kV and dividing by this value. Then Z0 is determined by Z0 = 3Zs - 2Z1.  For 1-phase sources, Zs is used directly. Use X0R0 to define X/R ratio for 1-phase source.

        DSS property name: `MVASC1`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    def _set_MVASC1(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(8, value, flags)

    MVASC1 = property(_get_MVASC1, _set_MVASC1) # type: BatchFloat64ArrayProxy

    def _get_X1R1(self) -> BatchFloat64ArrayProxy:
        """
        Positive-sequence  X/R ratio. Default = 4.

        DSS property name: `X1R1`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    def _set_X1R1(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(9, value, flags)

    X1R1 = property(_get_X1R1, _set_X1R1) # type: BatchFloat64ArrayProxy

    def _get_X0R0(self) -> BatchFloat64ArrayProxy:
        """
        Zero-sequence X/R ratio.Default = 3.

        DSS property name: `X0R0`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    def _set_X0R0(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(10, value, flags)

    X0R0 = property(_get_X0R0, _set_X0R0) # type: BatchFloat64ArrayProxy

    def _get_Isc3(self) -> BatchFloat64ArrayProxy:
        """
        Alternate method of defining the source impedance. 
        3-phase short circuit current, amps.  Default is 10000.

        DSS property name: `Isc3`, DSS property index: 11.
        """
        return BatchFloat64ArrayProxy(self, 11)

    def _set_Isc3(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(11, value, flags)

    Isc3 = property(_get_Isc3, _set_Isc3) # type: BatchFloat64ArrayProxy

    def _get_Isc1(self) -> BatchFloat64ArrayProxy:
        """
        Alternate method of defining the source impedance. 
        single-phase short circuit current, amps.  Default is 10500.

        DSS property name: `Isc1`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    def _set_Isc1(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(12, value, flags)

    Isc1 = property(_get_Isc1, _set_Isc1) # type: BatchFloat64ArrayProxy

    def _get_R1(self) -> BatchFloat64ArrayProxy:
        """
        Alternate method of defining the source impedance. 
        Positive-sequence resistance, ohms.  Default is 1.65.

        DSS property name: `R1`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    def _set_R1(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(13, value, flags)

    R1 = property(_get_R1, _set_R1) # type: BatchFloat64ArrayProxy

    def _get_X1(self) -> BatchFloat64ArrayProxy:
        """
        Alternate method of defining the source impedance. 
        Positive-sequence reactance, ohms.  Default is 6.6.

        DSS property name: `X1`, DSS property index: 14.
        """
        return BatchFloat64ArrayProxy(self, 14)

    def _set_X1(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(14, value, flags)

    X1 = property(_get_X1, _set_X1) # type: BatchFloat64ArrayProxy

    def _get_R0(self) -> BatchFloat64ArrayProxy:
        """
        Alternate method of defining the source impedance. 
        Zero-sequence resistance, ohms.  Default is 1.9.

        DSS property name: `R0`, DSS property index: 15.
        """
        return BatchFloat64ArrayProxy(self, 15)

    def _set_R0(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(15, value, flags)

    R0 = property(_get_R0, _set_R0) # type: BatchFloat64ArrayProxy

    def _get_X0(self) -> BatchFloat64ArrayProxy:
        """
        Alternate method of defining the source impedance. 
        Zero-sequence reactance, ohms.  Default is 5.7.

        DSS property name: `X0`, DSS property index: 16.
        """
        return BatchFloat64ArrayProxy(self, 16)

    def _set_X0(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(16, value, flags)

    X0 = property(_get_X0, _set_X0) # type: BatchFloat64ArrayProxy

    def _get_ScanType(self) -> BatchInt32ArrayProxy:
        """
        {pos*| zero | none} Maintain specified sequence for harmonic solution. Default is positive sequence. Otherwise, angle between phases rotates with harmonic.

        DSS property name: `ScanType`, DSS property index: 17.
        """
        return BatchInt32ArrayProxy(self, 17)

    def _set_ScanType(self, value: Union[AnyStr, int, enums.ScanType, List[AnyStr], List[int], List[enums.ScanType], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(17, value, flags)
            return

        self._set_batch_int32_array(17, value, flags)

    ScanType = property(_get_ScanType, _set_ScanType) # type: BatchInt32ArrayProxy

    def _get_ScanType_str(self) -> List[str]:
        """
        {pos*| zero | none} Maintain specified sequence for harmonic solution. Default is positive sequence. Otherwise, angle between phases rotates with harmonic.

        DSS property name: `ScanType`, DSS property index: 17.
        """
        return self._get_batch_str_prop(17)

    def _set_ScanType_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_ScanType(value, flags)

    ScanType_str = property(_get_ScanType_str, _set_ScanType_str) # type: List[str]

    def _get_Sequence(self) -> BatchInt32ArrayProxy:
        """
        {pos*| neg | zero} Set the phase angles for the specified symmetrical component sequence for non-harmonic solution modes. Default is positive sequence. 

        DSS property name: `Sequence`, DSS property index: 18.
        """
        return BatchInt32ArrayProxy(self, 18)

    def _set_Sequence(self, value: Union[AnyStr, int, enums.SequenceType, List[AnyStr], List[int], List[enums.SequenceType], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(18, value, flags)
            return

        self._set_batch_int32_array(18, value, flags)

    Sequence = property(_get_Sequence, _set_Sequence) # type: BatchInt32ArrayProxy

    def _get_Sequence_str(self) -> List[str]:
        """
        {pos*| neg | zero} Set the phase angles for the specified symmetrical component sequence for non-harmonic solution modes. Default is positive sequence. 

        DSS property name: `Sequence`, DSS property index: 18.
        """
        return self._get_batch_str_prop(18)

    def _set_Sequence_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Sequence(value, flags)

    Sequence_str = property(_get_Sequence_str, _set_Sequence_str) # type: List[str]

    def _get_Bus2(self) -> List[str]:
        """
        Name of bus to which 2nd terminal is connected.
        bus2=busname
        bus2=busname.1.2.3

        Default is Bus1.0.0.0 (grounded wye connection)

        DSS property name: `Bus2`, DSS property index: 19.
        """
        return self._get_batch_str_prop(19)

    def _set_Bus2(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(19, value, flags)

    Bus2 = property(_get_Bus2, _set_Bus2) # type: List[str]

    def _get_Z2(self) -> List[complex]:
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
            for x in self._unpack()
        ]

    def _set_Z2(self, value: Union[complex, List[complex]], flags: enums.SetterFlags = 0):
        if isinstance(value, complex):
            value, value_ptr, value_count = self._prepare_float64_array([value.real, value.imag])
            for x in self._unpack():
                self._lib.Obj_SetFloat64Array(x, 22, value_ptr, value_count, flags)
            return

        values = value
        if len(values) != len(self):
            raise ValueError('Number of elements provided must match the number of objects in the batch.')

        value, value_ptr, value_count = self._prepare_float64_array([0, 0])
        for v, x in zip(values, self._unpack()):
            value[0] = v.real
            value[1] = v.imag
            self._lib.Obj_SetFloat64Array(x, 22, value_ptr, value_count, flags)

    Z2 = property(_get_Z2, _set_Z2) # type: List[complex]

    def _get_puZ1(self) -> List[complex]:
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
            for x in self._unpack()
        ]

    def _set_puZ1(self, value: Union[complex, List[complex]], flags: enums.SetterFlags = 0):
        if isinstance(value, complex):
            value, value_ptr, value_count = self._prepare_float64_array([value.real, value.imag])
            for x in self._unpack():
                self._lib.Obj_SetFloat64Array(x, 23, value_ptr, value_count, flags)
            return

        values = value
        if len(values) != len(self):
            raise ValueError('Number of elements provided must match the number of objects in the batch.')

        value, value_ptr, value_count = self._prepare_float64_array([0, 0])
        for v, x in zip(values, self._unpack()):
            value[0] = v.real
            value[1] = v.imag
            self._lib.Obj_SetFloat64Array(x, 23, value_ptr, value_count, flags)

    puZ1 = property(_get_puZ1, _set_puZ1) # type: List[complex]

    def _get_puZ0(self) -> List[complex]:
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
            for x in self._unpack()
        ]

    def _set_puZ0(self, value: Union[complex, List[complex]], flags: enums.SetterFlags = 0):
        if isinstance(value, complex):
            value, value_ptr, value_count = self._prepare_float64_array([value.real, value.imag])
            for x in self._unpack():
                self._lib.Obj_SetFloat64Array(x, 24, value_ptr, value_count, flags)
            return

        values = value
        if len(values) != len(self):
            raise ValueError('Number of elements provided must match the number of objects in the batch.')

        value, value_ptr, value_count = self._prepare_float64_array([0, 0])
        for v, x in zip(values, self._unpack()):
            value[0] = v.real
            value[1] = v.imag
            self._lib.Obj_SetFloat64Array(x, 24, value_ptr, value_count, flags)

    puZ0 = property(_get_puZ0, _set_puZ0) # type: List[complex]

    def _get_puZ2(self) -> List[complex]:
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
            for x in self._unpack()
        ]

    def _set_puZ2(self, value: Union[complex, List[complex]], flags: enums.SetterFlags = 0):
        if isinstance(value, complex):
            value, value_ptr, value_count = self._prepare_float64_array([value.real, value.imag])
            for x in self._unpack():
                self._lib.Obj_SetFloat64Array(x, 25, value_ptr, value_count, flags)
            return

        values = value
        if len(values) != len(self):
            raise ValueError('Number of elements provided must match the number of objects in the batch.')

        value, value_ptr, value_count = self._prepare_float64_array([0, 0])
        for v, x in zip(values, self._unpack()):
            value[0] = v.real
            value[1] = v.imag
            self._lib.Obj_SetFloat64Array(x, 25, value_ptr, value_count, flags)

    puZ2 = property(_get_puZ2, _set_puZ2) # type: List[complex]

    def _get_BaseMVA(self) -> BatchFloat64ArrayProxy:
        """
        Default value is 100. Base used to convert values specified with puZ1, puZ0, and puZ2 properties to ohms on kV base specified by BasekV property.

        DSS property name: `BaseMVA`, DSS property index: 26.
        """
        return BatchFloat64ArrayProxy(self, 26)

    def _set_BaseMVA(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(26, value, flags)

    BaseMVA = property(_get_BaseMVA, _set_BaseMVA) # type: BatchFloat64ArrayProxy

    def _get_Yearly_str(self) -> List[str]:
        """
        LOADSHAPE object to use for the per-unit voltage for YEARLY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual L-N kV.

        Must be previously defined as a LOADSHAPE object. 

        Is set to the Daily load shape when Daily is defined.  The daily load shape is repeated in this case. Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Yearly`, DSS property index: 27.
        """
        return self._get_batch_str_prop(27)

    def _set_Yearly_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(27, value, flags)

    Yearly_str = property(_get_Yearly_str, _set_Yearly_str) # type: List[str]

    def _get_Yearly(self) -> List[LoadShape]:
        """
        LOADSHAPE object to use for the per-unit voltage for YEARLY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual L-N kV.

        Must be previously defined as a LOADSHAPE object. 

        Is set to the Daily load shape when Daily is defined.  The daily load shape is repeated in this case. Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Yearly`, DSS property index: 27.
        """
        return self._get_batch_obj_prop(27)

    def _set_Yearly(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(27, value, flags)

    Yearly = property(_get_Yearly, _set_Yearly) # type: List[LoadShape]

    def _get_Daily_str(self) -> List[str]:
        """
        LOADSHAPE object to use for the per-unit voltage for DAILY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual L-N kV.

        Must be previously defined as a LOADSHAPE object. 

        Sets Yearly curve if it is not already defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Daily`, DSS property index: 28.
        """
        return self._get_batch_str_prop(28)

    def _set_Daily_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(28, value, flags)

    Daily_str = property(_get_Daily_str, _set_Daily_str) # type: List[str]

    def _get_Daily(self) -> List[LoadShape]:
        """
        LOADSHAPE object to use for the per-unit voltage for DAILY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual L-N kV.

        Must be previously defined as a LOADSHAPE object. 

        Sets Yearly curve if it is not already defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Daily`, DSS property index: 28.
        """
        return self._get_batch_obj_prop(28)

    def _set_Daily(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(28, value, flags)

    Daily = property(_get_Daily, _set_Daily) # type: List[LoadShape]

    def _get_Duty_str(self) -> List[str]:
        """
        LOADSHAPE object to use for the per-unit voltage for DUTYCYCLE-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual L-N kV.

        Must be previously defined as a LOADSHAPE object. 

        Defaults to Daily load shape when Daily is defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Duty`, DSS property index: 29.
        """
        return self._get_batch_str_prop(29)

    def _set_Duty_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(29, value, flags)

    Duty_str = property(_get_Duty_str, _set_Duty_str) # type: List[str]

    def _get_Duty(self) -> List[LoadShape]:
        """
        LOADSHAPE object to use for the per-unit voltage for DUTYCYCLE-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual L-N kV.

        Must be previously defined as a LOADSHAPE object. 

        Defaults to Daily load shape when Daily is defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Duty`, DSS property index: 29.
        """
        return self._get_batch_obj_prop(29)

    def _set_Duty(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(29, value, flags)

    Duty = property(_get_Duty, _set_Duty) # type: List[LoadShape]

    def _get_Model(self) -> BatchInt32ArrayProxy:
        """
        {Thevenin* | Ideal}  Specifies whether the Vsource is to be considered a Thevenin short circuit model or a quasi-ideal voltage source. If Thevenin, the Vsource uses the impedances defined for all calculations. If "Ideal", the model uses a small impedance on the diagonal of the impedance matrix for the fundamental base frequency power flow only. Then switches to actual Thevenin model for other frequencies. 

        DSS property name: `Model`, DSS property index: 30.
        """
        return BatchInt32ArrayProxy(self, 30)

    def _set_Model(self, value: Union[AnyStr, int, enums.VSourceModel, List[AnyStr], List[int], List[enums.VSourceModel], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(30, value, flags)
            return

        self._set_batch_int32_array(30, value, flags)

    Model = property(_get_Model, _set_Model) # type: BatchInt32ArrayProxy

    def _get_Model_str(self) -> List[str]:
        """
        {Thevenin* | Ideal}  Specifies whether the Vsource is to be considered a Thevenin short circuit model or a quasi-ideal voltage source. If Thevenin, the Vsource uses the impedances defined for all calculations. If "Ideal", the model uses a small impedance on the diagonal of the impedance matrix for the fundamental base frequency power flow only. Then switches to actual Thevenin model for other frequencies. 

        DSS property name: `Model`, DSS property index: 30.
        """
        return self._get_batch_str_prop(30)

    def _set_Model_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Model(value, flags)

    Model_str = property(_get_Model_str, _set_Model_str) # type: List[str]

    def _get_puZIdeal(self) -> List[complex]:
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
            for x in self._unpack()
        ]

    def _set_puZIdeal(self, value: Union[complex, List[complex]], flags: enums.SetterFlags = 0):
        if isinstance(value, complex):
            value, value_ptr, value_count = self._prepare_float64_array([value.real, value.imag])
            for x in self._unpack():
                self._lib.Obj_SetFloat64Array(x, 31, value_ptr, value_count, flags)
            return

        values = value
        if len(values) != len(self):
            raise ValueError('Number of elements provided must match the number of objects in the batch.')

        value, value_ptr, value_count = self._prepare_float64_array([0, 0])
        for v, x in zip(values, self._unpack()):
            value[0] = v.real
            value[1] = v.imag
            self._lib.Obj_SetFloat64Array(x, 31, value_ptr, value_count, flags)

    puZIdeal = property(_get_puZIdeal, _set_puZIdeal) # type: List[complex]

    def _get_Spectrum_str(self) -> List[str]:
        """
        Name of harmonic spectrum for this source.  Default is "defaultvsource", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 32.
        """
        return self._get_batch_str_prop(32)

    def _set_Spectrum_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(32, value, flags)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str) # type: List[str]

    def _get_Spectrum(self) -> List[SpectrumObj]:
        """
        Name of harmonic spectrum for this source.  Default is "defaultvsource", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 32.
        """
        return self._get_batch_obj_prop(32)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(32, value, flags)

    Spectrum = property(_get_Spectrum, _set_Spectrum) # type: List[SpectrumObj]

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 33.
        """
        return BatchFloat64ArrayProxy(self, 33)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(33, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy

    def _get_Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 34.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(34)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(34, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 35.
        """
        self._set_batch_string(35, value, flags)

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

class IVsource(IDSSObj, VsourceBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, Vsource, VsourceBatch)
        VsourceBatch.__init__(self, self._api_util, sync_cls_idx=Vsource._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Vsource:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[VsourceProperties]) -> Vsource:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[VsourceBatchProperties]) -> VsourceBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
