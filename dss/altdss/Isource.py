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
from .LoadShape import LoadShape
from .Spectrum import Spectrum as SpectrumObj

class Isource(DSSObj, CktElementMixin, PCElementMixin):
    __slots__ = []
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
    def Amps(self) -> float:
        """
        Magnitude of current source, each phase, in Amps.

        DSS property name: `Amps`, DSS property index: 2.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 2)

    @Amps.setter
    def Amps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 2, value)

    @property
    def Angle(self) -> float:
        """
        Phase angle in degrees of first phase: e.g.,Angle=10.3.
        Phase shift between phases is assumed 120 degrees when number of phases <= 3

        DSS property name: `Angle`, DSS property index: 3.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @Angle.setter
    def Angle(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def Frequency(self) -> float:
        """
        Source frequency.  Defaults to  circuit fundamental frequency.

        DSS property name: `Frequency`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @Frequency.setter
    def Frequency(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def Phases(self) -> int:
        """
        Number of phases.  Defaults to 3. For 3 or less, phase shift is 120 degrees.

        DSS property name: `Phases`, DSS property index: 5.
        """
        return self._lib.Obj_GetInt32(self._ptr, 5)

    @Phases.setter
    def Phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 5, value)

    @property
    def ScanType(self) -> enums.ScanType:
        """
        {pos*| zero | none} Maintain specified sequence for harmonic solution. Default is positive sequence. Otherwise, angle between phases rotates with harmonic.

        DSS property name: `ScanType`, DSS property index: 6.
        """
        return enums.ScanType(self._lib.Obj_GetInt32(self._ptr, 6))

    @ScanType.setter
    def ScanType(self, value: Union[AnyStr, int, enums.ScanType]):
        if not isinstance(value, int):
            self._set_string_o(6, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 6, value)

    @property
    def ScanType_str(self) -> str:
        """
        {pos*| zero | none} Maintain specified sequence for harmonic solution. Default is positive sequence. Otherwise, angle between phases rotates with harmonic.

        DSS property name: `ScanType`, DSS property index: 6.
        """
        return self._get_prop_string(6)

    @ScanType_str.setter
    def ScanType_str(self, value: AnyStr):
        self.ScanType = value

    @property
    def Sequence(self) -> enums.SequenceType:
        """
        {pos*| neg | zero} Set the phase angles for the specified symmetrical component sequence for non-harmonic solution modes. Default is positive sequence. 

        DSS property name: `Sequence`, DSS property index: 7.
        """
        return enums.SequenceType(self._lib.Obj_GetInt32(self._ptr, 7))

    @Sequence.setter
    def Sequence(self, value: Union[AnyStr, int, enums.SequenceType]):
        if not isinstance(value, int):
            self._set_string_o(7, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 7, value)

    @property
    def Sequence_str(self) -> str:
        """
        {pos*| neg | zero} Set the phase angles for the specified symmetrical component sequence for non-harmonic solution modes. Default is positive sequence. 

        DSS property name: `Sequence`, DSS property index: 7.
        """
        return self._get_prop_string(7)

    @Sequence_str.setter
    def Sequence_str(self, value: AnyStr):
        self.Sequence = value

    @property
    def Yearly(self) -> str:
        """
        LOADSHAPE object to use for the per-unit current for YEARLY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual Amp.

        Must be previously defined as a LOADSHAPE object. 

        Is set to the Daily load shape when Daily is defined.  The daily load shape is repeated in this case. Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Yearly`, DSS property index: 8.
        """
        return self._get_prop_string(8)

    @Yearly.setter
    def Yearly(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(8, value)
            return

        self._set_string_o(8, value)

    @property
    def Yearly_obj(self) -> LoadShape:
        """
        LOADSHAPE object to use for the per-unit current for YEARLY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual Amp.

        Must be previously defined as a LOADSHAPE object. 

        Is set to the Daily load shape when Daily is defined.  The daily load shape is repeated in this case. Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Yearly`, DSS property index: 8.
        """
        return self._get_obj(8, LoadShape)

    @Yearly_obj.setter
    def Yearly_obj(self, value: LoadShape):
        self._set_obj(8, value)

    @property
    def Daily(self) -> str:
        """
        LOADSHAPE object to use for the per-unit current for DAILY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual A.

        Must be previously defined as a LOADSHAPE object. 

        Sets Yearly curve if it is not already defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Daily`, DSS property index: 9.
        """
        return self._get_prop_string(9)

    @Daily.setter
    def Daily(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(9, value)
            return

        self._set_string_o(9, value)

    @property
    def Daily_obj(self) -> LoadShape:
        """
        LOADSHAPE object to use for the per-unit current for DAILY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual A.

        Must be previously defined as a LOADSHAPE object. 

        Sets Yearly curve if it is not already defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Daily`, DSS property index: 9.
        """
        return self._get_obj(9, LoadShape)

    @Daily_obj.setter
    def Daily_obj(self, value: LoadShape):
        self._set_obj(9, value)

    @property
    def Duty(self) -> str:
        """
        LOADSHAPE object to use for the per-unit current for DUTYCYCLE-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual A.

        Must be previously defined as a LOADSHAPE object. 

        Defaults to Daily load shape when Daily is defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Duty`, DSS property index: 10.
        """
        return self._get_prop_string(10)

    @Duty.setter
    def Duty(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(10, value)
            return

        self._set_string_o(10, value)

    @property
    def Duty_obj(self) -> LoadShape:
        """
        LOADSHAPE object to use for the per-unit current for DUTYCYCLE-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual A.

        Must be previously defined as a LOADSHAPE object. 

        Defaults to Daily load shape when Daily is defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Duty`, DSS property index: 10.
        """
        return self._get_obj(10, LoadShape)

    @Duty_obj.setter
    def Duty_obj(self, value: LoadShape):
        self._set_obj(10, value)

    @property
    def Bus2(self) -> str:
        """
        Name of bus to which 2nd terminal is connected.
        bus2=busname
        bus2=busname.1.2.3

        Default is Bus1.0.0.0 (grounded-wye connection)

        DSS property name: `Bus2`, DSS property index: 11.
        """
        return self._get_prop_string(11)

    @Bus2.setter
    def Bus2(self, value: AnyStr):
        self._set_string_o(11, value)

    @property
    def Spectrum(self) -> str:
        """
        Harmonic spectrum assumed for this source.  Default is "default".

        DSS property name: `Spectrum`, DSS property index: 12.
        """
        return self._get_prop_string(12)

    @Spectrum.setter
    def Spectrum(self, value: Union[AnyStr, SpectrumObj]):
        if isinstance(value, DSSObj):
            self._set_obj(12, value)
            return

        self._set_string_o(12, value)

    @property
    def Spectrum_obj(self) -> SpectrumObj:
        """
        Harmonic spectrum assumed for this source.  Default is "default".

        DSS property name: `Spectrum`, DSS property index: 12.
        """
        return self._get_obj(12, SpectrumObj)

    @Spectrum_obj.setter
    def Spectrum_obj(self, value: SpectrumObj):
        self._set_obj(12, value)

    @property
    def BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @BaseFreq.setter
    def BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 14.
        """
        return self._lib.Obj_GetInt32(self._ptr, 14) != 0

    @Enabled.setter
    def Enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 14, value)

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

class IsourceBatch(DSSBatch):
    _cls_name = 'Isource'
    _obj_cls = Isource
    _cls_idx = 17


    @property
    def Bus1(self) -> List[str]:
        """
        Name of bus to which source is connected.
        bus1=busname
        bus1=busname.1.2.3

        DSS property name: `Bus1`, DSS property index: 1.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1) 

    @Bus1.setter
    def Bus1(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(1, value)

    @property
    def Amps(self) -> BatchFloat64ArrayProxy:
        """
        Magnitude of current source, each phase, in Amps.

        DSS property name: `Amps`, DSS property index: 2.
        """
        return BatchFloat64ArrayProxy(self, 2)

    @Amps.setter
    def Amps(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(2, value)

    @property
    def Angle(self) -> BatchFloat64ArrayProxy:
        """
        Phase angle in degrees of first phase: e.g.,Angle=10.3.
        Phase shift between phases is assumed 120 degrees when number of phases <= 3

        DSS property name: `Angle`, DSS property index: 3.
        """
        return BatchFloat64ArrayProxy(self, 3)

    @Angle.setter
    def Angle(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(3, value)

    @property
    def Frequency(self) -> BatchFloat64ArrayProxy:
        """
        Source frequency.  Defaults to  circuit fundamental frequency.

        DSS property name: `Frequency`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    @Frequency.setter
    def Frequency(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(4, value)

    @property
    def Phases(self) -> BatchInt32ArrayProxy:
        """
        Number of phases.  Defaults to 3. For 3 or less, phase shift is 120 degrees.

        DSS property name: `Phases`, DSS property index: 5.
        """
        return BatchInt32ArrayProxy(self, 5)

    @Phases.setter
    def Phases(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(5, value)

    @property
    def ScanType(self) -> BatchInt32ArrayProxy:
        """
        {pos*| zero | none} Maintain specified sequence for harmonic solution. Default is positive sequence. Otherwise, angle between phases rotates with harmonic.

        DSS property name: `ScanType`, DSS property index: 6.
        """
        return BatchInt32ArrayProxy(self, 6)

    @ScanType.setter
    def ScanType(self, value: Union[AnyStr, int, enums.ScanType, List[AnyStr], List[int], List[enums.ScanType], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(6, value)
            return
    
        self._set_batch_int32_array(6, value)

    @property
    def ScanType_str(self) -> str:
        """
        {pos*| zero | none} Maintain specified sequence for harmonic solution. Default is positive sequence. Otherwise, angle between phases rotates with harmonic.

        DSS property name: `ScanType`, DSS property index: 6.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 6)

    @ScanType_str.setter
    def ScanType_str(self, value: AnyStr):
        self.ScanType = value

    @property
    def Sequence(self) -> BatchInt32ArrayProxy:
        """
        {pos*| neg | zero} Set the phase angles for the specified symmetrical component sequence for non-harmonic solution modes. Default is positive sequence. 

        DSS property name: `Sequence`, DSS property index: 7.
        """
        return BatchInt32ArrayProxy(self, 7)

    @Sequence.setter
    def Sequence(self, value: Union[AnyStr, int, enums.SequenceType, List[AnyStr], List[int], List[enums.SequenceType], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(7, value)
            return
    
        self._set_batch_int32_array(7, value)

    @property
    def Sequence_str(self) -> str:
        """
        {pos*| neg | zero} Set the phase angles for the specified symmetrical component sequence for non-harmonic solution modes. Default is positive sequence. 

        DSS property name: `Sequence`, DSS property index: 7.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 7)

    @Sequence_str.setter
    def Sequence_str(self, value: AnyStr):
        self.Sequence = value

    @property
    def Yearly(self) -> List[str]:
        """
        LOADSHAPE object to use for the per-unit current for YEARLY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual Amp.

        Must be previously defined as a LOADSHAPE object. 

        Is set to the Daily load shape when Daily is defined.  The daily load shape is repeated in this case. Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Yearly`, DSS property index: 8.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 8)

    @Yearly.setter
    def Yearly(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]):
        self._set_batch_obj_prop(8, value)

    @property
    def Yearly_obj(self) -> List[LoadShape]:
        """
        LOADSHAPE object to use for the per-unit current for YEARLY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual Amp.

        Must be previously defined as a LOADSHAPE object. 

        Is set to the Daily load shape when Daily is defined.  The daily load shape is repeated in this case. Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Yearly`, DSS property index: 8.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 8)

    @Yearly_obj.setter
    def Yearly_obj(self, value: LoadShape):
        self._set_batch_string(8, value)

    @property
    def Daily(self) -> List[str]:
        """
        LOADSHAPE object to use for the per-unit current for DAILY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual A.

        Must be previously defined as a LOADSHAPE object. 

        Sets Yearly curve if it is not already defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Daily`, DSS property index: 9.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 9)

    @Daily.setter
    def Daily(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]):
        self._set_batch_obj_prop(9, value)

    @property
    def Daily_obj(self) -> List[LoadShape]:
        """
        LOADSHAPE object to use for the per-unit current for DAILY-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual A.

        Must be previously defined as a LOADSHAPE object. 

        Sets Yearly curve if it is not already defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Daily`, DSS property index: 9.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 9)

    @Daily_obj.setter
    def Daily_obj(self, value: LoadShape):
        self._set_batch_string(9, value)

    @property
    def Duty(self) -> List[str]:
        """
        LOADSHAPE object to use for the per-unit current for DUTYCYCLE-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual A.

        Must be previously defined as a LOADSHAPE object. 

        Defaults to Daily load shape when Daily is defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Duty`, DSS property index: 10.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 10)

    @Duty.setter
    def Duty(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]):
        self._set_batch_obj_prop(10, value)

    @property
    def Duty_obj(self) -> List[LoadShape]:
        """
        LOADSHAPE object to use for the per-unit current for DUTYCYCLE-mode simulations. Set the Mult property of the LOADSHAPE to the pu curve. Qmult is not used. If UseActual=Yes then the Mult curve should be actual A.

        Must be previously defined as a LOADSHAPE object. 

        Defaults to Daily load shape when Daily is defined.   Set to NONE to reset to no loadshape for Yearly mode. The default is no variation.

        DSS property name: `Duty`, DSS property index: 10.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 10)

    @Duty_obj.setter
    def Duty_obj(self, value: LoadShape):
        self._set_batch_string(10, value)

    @property
    def Bus2(self) -> List[str]:
        """
        Name of bus to which 2nd terminal is connected.
        bus2=busname
        bus2=busname.1.2.3

        Default is Bus1.0.0.0 (grounded-wye connection)

        DSS property name: `Bus2`, DSS property index: 11.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 11) 

    @Bus2.setter
    def Bus2(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(11, value)

    @property
    def Spectrum(self) -> List[str]:
        """
        Harmonic spectrum assumed for this source.  Default is "default".

        DSS property name: `Spectrum`, DSS property index: 12.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 12)

    @Spectrum.setter
    def Spectrum(self, value: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]]):
        self._set_batch_obj_prop(12, value)

    @property
    def Spectrum_obj(self) -> List[SpectrumObj]:
        """
        Harmonic spectrum assumed for this source.  Default is "default".

        DSS property name: `Spectrum`, DSS property index: 12.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 12)

    @Spectrum_obj.setter
    def Spectrum_obj(self, value: SpectrumObj):
        self._set_batch_string(12, value)

    @property
    def BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    @BaseFreq.setter
    def BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(13, value)

    @property
    def Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 14.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 14)
        ]
    @Enabled.setter
    def Enabled(self, value: bool):
        self._set_batch_int32_array(14, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 15.
        """
        self._set_batch_string(15, value)

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

class IIsource(IDSSObj):
    def __init__(self, iobj):
        super().__init__(iobj, Isource, IsourceBatch)

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Isource:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[IsourceProperties]) -> Isource:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[IsourceBatchProperties]) -> IsourceBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
