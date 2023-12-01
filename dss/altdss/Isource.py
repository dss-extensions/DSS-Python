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

class Isource(DSSObj, CircuitElementMixin, PCElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots + PCElementMixin._extra_slots
    _cls_name = 'Isource'
    _cls_idx = 17
    _cls_prop_idx = {
        'bus1': 1,
        'amps': 2,
        'angle': 3,
        'frequency': 4,
        'phases': 5,
        'scantype': 6,
        'sequence': 7,
        'yearly': 8,
        'daily': 9,
        'duty': 10,
        'bus2': 11,
        'spectrum': 12,
        'basefreq': 13,
        'enabled': 14,
        'like': 15,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)
       PCElementMixin.__init__(self)

    def _get_Bus1(self) -> str:
        """
        Name of bus to which source is connected.
        bus1=busname
        bus1=busname.1.2.3

        DSS property name: `Bus1`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    def _set_Bus1(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(1, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: str

    def _get_Amps(self) -> float:
        """
        Magnitude of current source, each phase, in Amps.

        DSS property name: `Amps`, DSS property index: 2.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 2)

    def _set_Amps(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 2, value, flags)

    Amps = property(_get_Amps, _set_Amps) # type: float

    def _get_Angle(self) -> float:
        """
        Phase angle in degrees of first phase: e.g.,Angle=10.3.
        Phase shift between phases is assumed 120 degrees when number of phases <= 3

        DSS property name: `Angle`, DSS property index: 3.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    def _set_Angle(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 3, value, flags)

    Angle = property(_get_Angle, _set_Angle) # type: float

    def _get_Frequency(self) -> float:
        """
        Source frequency.  Defaults to  circuit fundamental frequency.

        DSS property name: `Frequency`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    def _set_Frequency(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 4, value, flags)

    Frequency = property(_get_Frequency, _set_Frequency) # type: float

    def _get_Phases(self) -> int:
        """
        Number of phases.  Defaults to 3. For 3 or less, phase shift is 120 degrees.

        DSS property name: `Phases`, DSS property index: 5.
        """
        return self._lib.Obj_GetInt32(self._ptr, 5)

    def _set_Phases(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 5, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: int

    def _get_ScanType(self) -> enums.ScanType:
        """
        {pos*| zero | none} Maintain specified sequence for harmonic solution. Default is positive sequence. Otherwise, angle between phases rotates with harmonic.

        DSS property name: `ScanType`, DSS property index: 6.
        """
        return enums.ScanType(self._lib.Obj_GetInt32(self._ptr, 6))

    def _set_ScanType(self, value: Union[AnyStr, int, enums.ScanType], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(6, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 6, value, flags)

    ScanType = property(_get_ScanType, _set_ScanType) # type: enums.ScanType

    def _get_ScanType_str(self) -> str:
        """
        {pos*| zero | none} Maintain specified sequence for harmonic solution. Default is positive sequence. Otherwise, angle between phases rotates with harmonic.

        DSS property name: `ScanType`, DSS property index: 6.
        """
        return self._get_prop_string(6)

    def _set_ScanType_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_ScanType(value, flags)

    ScanType_str = property(_get_ScanType_str, _set_ScanType_str) # type: str

    def _get_Sequence(self) -> enums.SequenceType:
        """
        {pos*| neg | zero} Set the phase angles for the specified symmetrical component sequence for non-harmonic solution modes. Default is positive sequence. 

        DSS property name: `Sequence`, DSS property index: 7.
        """
        return enums.SequenceType(self._lib.Obj_GetInt32(self._ptr, 7))

    def _set_Sequence(self, value: Union[AnyStr, int, enums.SequenceType], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(7, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 7, value, flags)

    Sequence = property(_get_Sequence, _set_Sequence) # type: enums.SequenceType

    def _get_Sequence_str(self) -> str:
        """
        {pos*| neg | zero} Set the phase angles for the specified symmetrical component sequence for non-harmonic solution modes. Default is positive sequence. 

        DSS property name: `Sequence`, DSS property index: 7.
        """
        return self._get_prop_string(7)

    def _set_Sequence_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Sequence(value, flags)

    Sequence_str = property(_get_Sequence_str, _set_Sequence_str) # type: str

    def _get_Yearly_str(self) -> str:
        """
        LOADSHAPE object to use for the per-unit current for YEARLY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual Amp.

        Must be previously defined as a LOADSHAPE object. 

        Is set to the Daily load shape when Daily is defined.  The daily load shape is repeated in this case. Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Yearly`, DSS property index: 8.
        """
        return self._get_prop_string(8)

    def _set_Yearly_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(8, value, flags)

    Yearly_str = property(_get_Yearly_str, _set_Yearly_str) # type: str

    def _get_Yearly(self) -> LoadShape:
        """
        LOADSHAPE object to use for the per-unit current for YEARLY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual Amp.

        Must be previously defined as a LOADSHAPE object. 

        Is set to the Daily load shape when Daily is defined.  The daily load shape is repeated in this case. Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Yearly`, DSS property index: 8.
        """
        return self._get_obj(8, LoadShape)

    def _set_Yearly(self, value: Union[AnyStr, LoadShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(8, value, flags)
            return

        self._set_string_o(8, value, flags)

    Yearly = property(_get_Yearly, _set_Yearly) # type: LoadShape

    def _get_Daily_str(self) -> str:
        """
        LOADSHAPE object to use for the per-unit current for DAILY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual A.

        Must be previously defined as a LOADSHAPE object. 

        Sets Yearly curve if it is not already defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Daily`, DSS property index: 9.
        """
        return self._get_prop_string(9)

    def _set_Daily_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(9, value, flags)

    Daily_str = property(_get_Daily_str, _set_Daily_str) # type: str

    def _get_Daily(self) -> LoadShape:
        """
        LOADSHAPE object to use for the per-unit current for DAILY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual A.

        Must be previously defined as a LOADSHAPE object. 

        Sets Yearly curve if it is not already defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Daily`, DSS property index: 9.
        """
        return self._get_obj(9, LoadShape)

    def _set_Daily(self, value: Union[AnyStr, LoadShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(9, value, flags)
            return

        self._set_string_o(9, value, flags)

    Daily = property(_get_Daily, _set_Daily) # type: LoadShape

    def _get_Duty_str(self) -> str:
        """
        LOADSHAPE object to use for the per-unit current for DUTYCYCLE-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual A.

        Must be previously defined as a LOADSHAPE object. 

        Defaults to Daily load shape when Daily is defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Duty`, DSS property index: 10.
        """
        return self._get_prop_string(10)

    def _set_Duty_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(10, value, flags)

    Duty_str = property(_get_Duty_str, _set_Duty_str) # type: str

    def _get_Duty(self) -> LoadShape:
        """
        LOADSHAPE object to use for the per-unit current for DUTYCYCLE-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual A.

        Must be previously defined as a LOADSHAPE object. 

        Defaults to Daily load shape when Daily is defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Duty`, DSS property index: 10.
        """
        return self._get_obj(10, LoadShape)

    def _set_Duty(self, value: Union[AnyStr, LoadShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(10, value, flags)
            return

        self._set_string_o(10, value, flags)

    Duty = property(_get_Duty, _set_Duty) # type: LoadShape

    def _get_Bus2(self) -> str:
        """
        Name of bus to which 2nd terminal is connected.
        bus2=busname
        bus2=busname.1.2.3

        Default is Bus1.0.0.0 (grounded-wye connection)

        DSS property name: `Bus2`, DSS property index: 11.
        """
        return self._get_prop_string(11)

    def _set_Bus2(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(11, value, flags)

    Bus2 = property(_get_Bus2, _set_Bus2) # type: str

    def _get_Spectrum_str(self) -> str:
        """
        Harmonic spectrum assumed for this source.  Default is "default".

        DSS property name: `Spectrum`, DSS property index: 12.
        """
        return self._get_prop_string(12)

    def _set_Spectrum_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(12, value, flags)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str) # type: str

    def _get_Spectrum(self) -> SpectrumObj:
        """
        Harmonic spectrum assumed for this source.  Default is "default".

        DSS property name: `Spectrum`, DSS property index: 12.
        """
        return self._get_obj(12, SpectrumObj)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(12, value, flags)
            return

        self._set_string_o(12, value, flags)

    Spectrum = property(_get_Spectrum, _set_Spectrum) # type: SpectrumObj

    def _get_BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 13, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float

    def _get_Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 14.
        """
        return self._lib.Obj_GetInt32(self._ptr, 14) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 14, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 15.
        """
        self._set_string_o(15, value)


class IsourceProperties(TypedDict):
    Bus1: AnyStr
    Amps: float
    Angle: float
    Frequency: float
    Phases: int
    ScanType: Union[AnyStr, int, enums.ScanType]
    Sequence: Union[AnyStr, int, enums.SequenceType]
    Yearly: Union[AnyStr, LoadShape]
    Daily: Union[AnyStr, LoadShape]
    Duty: Union[AnyStr, LoadShape]
    Bus2: AnyStr
    Spectrum: Union[AnyStr, SpectrumObj]
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class IsourceBatch(DSSBatch, CircuitElementBatchMixin, PCElementBatchMixin):
    _cls_name = 'Isource'
    _obj_cls = Isource
    _cls_idx = 17

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)
       PCElementBatchMixin.__init__(self)

    def _get_Bus1(self) -> List[str]:
        """
        Name of bus to which source is connected.
        bus1=busname
        bus1=busname.1.2.3

        DSS property name: `Bus1`, DSS property index: 1.
        """
        return self._get_batch_str_prop(1)

    def _set_Bus1(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(1, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: List[str]

    def _get_Amps(self) -> BatchFloat64ArrayProxy:
        """
        Magnitude of current source, each phase, in Amps.

        DSS property name: `Amps`, DSS property index: 2.
        """
        return BatchFloat64ArrayProxy(self, 2)

    def _set_Amps(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(2, value, flags)

    Amps = property(_get_Amps, _set_Amps) # type: BatchFloat64ArrayProxy

    def _get_Angle(self) -> BatchFloat64ArrayProxy:
        """
        Phase angle in degrees of first phase: e.g.,Angle=10.3.
        Phase shift between phases is assumed 120 degrees when number of phases <= 3

        DSS property name: `Angle`, DSS property index: 3.
        """
        return BatchFloat64ArrayProxy(self, 3)

    def _set_Angle(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(3, value, flags)

    Angle = property(_get_Angle, _set_Angle) # type: BatchFloat64ArrayProxy

    def _get_Frequency(self) -> BatchFloat64ArrayProxy:
        """
        Source frequency.  Defaults to  circuit fundamental frequency.

        DSS property name: `Frequency`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    def _set_Frequency(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(4, value, flags)

    Frequency = property(_get_Frequency, _set_Frequency) # type: BatchFloat64ArrayProxy

    def _get_Phases(self) -> BatchInt32ArrayProxy:
        """
        Number of phases.  Defaults to 3. For 3 or less, phase shift is 120 degrees.

        DSS property name: `Phases`, DSS property index: 5.
        """
        return BatchInt32ArrayProxy(self, 5)

    def _set_Phases(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(5, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: BatchInt32ArrayProxy

    def _get_ScanType(self) -> BatchInt32ArrayProxy:
        """
        {pos*| zero | none} Maintain specified sequence for harmonic solution. Default is positive sequence. Otherwise, angle between phases rotates with harmonic.

        DSS property name: `ScanType`, DSS property index: 6.
        """
        return BatchInt32ArrayProxy(self, 6)

    def _set_ScanType(self, value: Union[AnyStr, int, enums.ScanType, List[AnyStr], List[int], List[enums.ScanType], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(6, value, flags)
            return

        self._set_batch_int32_array(6, value, flags)

    ScanType = property(_get_ScanType, _set_ScanType) # type: BatchInt32ArrayProxy

    def _get_ScanType_str(self) -> List[str]:
        """
        {pos*| zero | none} Maintain specified sequence for harmonic solution. Default is positive sequence. Otherwise, angle between phases rotates with harmonic.

        DSS property name: `ScanType`, DSS property index: 6.
        """
        return self._get_batch_str_prop(6)

    def _set_ScanType_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_ScanType(value, flags)

    ScanType_str = property(_get_ScanType_str, _set_ScanType_str) # type: List[str]

    def _get_Sequence(self) -> BatchInt32ArrayProxy:
        """
        {pos*| neg | zero} Set the phase angles for the specified symmetrical component sequence for non-harmonic solution modes. Default is positive sequence. 

        DSS property name: `Sequence`, DSS property index: 7.
        """
        return BatchInt32ArrayProxy(self, 7)

    def _set_Sequence(self, value: Union[AnyStr, int, enums.SequenceType, List[AnyStr], List[int], List[enums.SequenceType], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(7, value, flags)
            return

        self._set_batch_int32_array(7, value, flags)

    Sequence = property(_get_Sequence, _set_Sequence) # type: BatchInt32ArrayProxy

    def _get_Sequence_str(self) -> List[str]:
        """
        {pos*| neg | zero} Set the phase angles for the specified symmetrical component sequence for non-harmonic solution modes. Default is positive sequence. 

        DSS property name: `Sequence`, DSS property index: 7.
        """
        return self._get_batch_str_prop(7)

    def _set_Sequence_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Sequence(value, flags)

    Sequence_str = property(_get_Sequence_str, _set_Sequence_str) # type: List[str]

    def _get_Yearly_str(self) -> List[str]:
        """
        LOADSHAPE object to use for the per-unit current for YEARLY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual Amp.

        Must be previously defined as a LOADSHAPE object. 

        Is set to the Daily load shape when Daily is defined.  The daily load shape is repeated in this case. Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Yearly`, DSS property index: 8.
        """
        return self._get_batch_str_prop(8)

    def _set_Yearly_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(8, value, flags)

    Yearly_str = property(_get_Yearly_str, _set_Yearly_str) # type: List[str]

    def _get_Yearly(self) -> List[LoadShape]:
        """
        LOADSHAPE object to use for the per-unit current for YEARLY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual Amp.

        Must be previously defined as a LOADSHAPE object. 

        Is set to the Daily load shape when Daily is defined.  The daily load shape is repeated in this case. Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Yearly`, DSS property index: 8.
        """
        return self._get_batch_obj_prop(8)

    def _set_Yearly(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(8, value, flags)

    Yearly = property(_get_Yearly, _set_Yearly) # type: List[LoadShape]

    def _get_Daily_str(self) -> List[str]:
        """
        LOADSHAPE object to use for the per-unit current for DAILY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual A.

        Must be previously defined as a LOADSHAPE object. 

        Sets Yearly curve if it is not already defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Daily`, DSS property index: 9.
        """
        return self._get_batch_str_prop(9)

    def _set_Daily_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(9, value, flags)

    Daily_str = property(_get_Daily_str, _set_Daily_str) # type: List[str]

    def _get_Daily(self) -> List[LoadShape]:
        """
        LOADSHAPE object to use for the per-unit current for DAILY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual A.

        Must be previously defined as a LOADSHAPE object. 

        Sets Yearly curve if it is not already defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Daily`, DSS property index: 9.
        """
        return self._get_batch_obj_prop(9)

    def _set_Daily(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(9, value, flags)

    Daily = property(_get_Daily, _set_Daily) # type: List[LoadShape]

    def _get_Duty_str(self) -> List[str]:
        """
        LOADSHAPE object to use for the per-unit current for DUTYCYCLE-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual A.

        Must be previously defined as a LOADSHAPE object. 

        Defaults to Daily load shape when Daily is defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Duty`, DSS property index: 10.
        """
        return self._get_batch_str_prop(10)

    def _set_Duty_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(10, value, flags)

    Duty_str = property(_get_Duty_str, _set_Duty_str) # type: List[str]

    def _get_Duty(self) -> List[LoadShape]:
        """
        LOADSHAPE object to use for the per-unit current for DUTYCYCLE-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual A.

        Must be previously defined as a LOADSHAPE object. 

        Defaults to Daily load shape when Daily is defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Duty`, DSS property index: 10.
        """
        return self._get_batch_obj_prop(10)

    def _set_Duty(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(10, value, flags)

    Duty = property(_get_Duty, _set_Duty) # type: List[LoadShape]

    def _get_Bus2(self) -> List[str]:
        """
        Name of bus to which 2nd terminal is connected.
        bus2=busname
        bus2=busname.1.2.3

        Default is Bus1.0.0.0 (grounded-wye connection)

        DSS property name: `Bus2`, DSS property index: 11.
        """
        return self._get_batch_str_prop(11)

    def _set_Bus2(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(11, value, flags)

    Bus2 = property(_get_Bus2, _set_Bus2) # type: List[str]

    def _get_Spectrum_str(self) -> List[str]:
        """
        Harmonic spectrum assumed for this source.  Default is "default".

        DSS property name: `Spectrum`, DSS property index: 12.
        """
        return self._get_batch_str_prop(12)

    def _set_Spectrum_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(12, value, flags)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str) # type: List[str]

    def _get_Spectrum(self) -> List[SpectrumObj]:
        """
        Harmonic spectrum assumed for this source.  Default is "default".

        DSS property name: `Spectrum`, DSS property index: 12.
        """
        return self._get_batch_obj_prop(12)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(12, value, flags)

    Spectrum = property(_get_Spectrum, _set_Spectrum) # type: List[SpectrumObj]

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(13, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy

    def _get_Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 14.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(14)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(14, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 15.
        """
        self._set_batch_string(15, value, flags)

class IsourceBatchProperties(TypedDict):
    Bus1: Union[AnyStr, List[AnyStr]]
    Amps: Union[float, Float64Array]
    Angle: Union[float, Float64Array]
    Frequency: Union[float, Float64Array]
    Phases: Union[int, Int32Array]
    ScanType: Union[AnyStr, int, enums.ScanType, List[AnyStr], List[int], List[enums.ScanType], Int32Array]
    Sequence: Union[AnyStr, int, enums.SequenceType, List[AnyStr], List[int], List[enums.SequenceType], Int32Array]
    Yearly: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    Daily: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    Duty: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    Bus2: Union[AnyStr, List[AnyStr]]
    Spectrum: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IIsource(IDSSObj, IsourceBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, Isource, IsourceBatch)
        IsourceBatch.__init__(self, self._api_util, sync_cls_idx=Isource._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Isource:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[IsourceProperties]) -> Isource:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[IsourceBatchProperties]) -> IsourceBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
