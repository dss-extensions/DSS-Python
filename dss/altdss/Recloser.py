# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from typing_extensions import TypedDict, Unpack
from ._obj_bases import (
    CktElementMixin,
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
from .TCC_Curve import TCC_Curve

class Recloser(DSSObj, CktElementMixin):
    __slots__ = CktElementMixin._extra_slots
    _cls_name = 'Recloser'
    _cls_idx = 32
    _cls_prop_idx = {
        'monitoredobj': 1,
        'monitoredterm': 2,
        'switchedobj': 3,
        'switchedterm': 4,
        'numfast': 5,
        'phasefast': 6,
        'phasedelayed': 7,
        'groundfast': 8,
        'grounddelayed': 9,
        'phasetrip': 10,
        'groundtrip': 11,
        'phaseinst': 12,
        'groundinst': 13,
        'reset': 14,
        'shots': 15,
        'recloseintervals': 16,
        'delay': 17,
        'action': 18,
        'tdphfast': 19,
        'tdgrfast': 20,
        'tdphdelayed': 21,
        'tdgrdelayed': 22,
        'normal': 23,
        'state': 24,
        'basefreq': 25,
        'enabled': 26,
        'like': 27,
    }

    @property
    def MonitoredObj(self) -> str:
        """
        Full object name of the circuit element, typically a line, transformer, load, or generator, to which the Recloser's PT and/or CT are connected. This is the "monitored" element. There is no default; must be specified.

        DSS property name: `MonitoredObj`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    @MonitoredObj.setter
    def MonitoredObj(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_obj(1, value)
            return

        self._set_string_o(1, value)

    @property
    def MonitoredObj_obj(self) -> DSSObj:
        """
        Full object name of the circuit element, typically a line, transformer, load, or generator, to which the Recloser's PT and/or CT are connected. This is the "monitored" element. There is no default; must be specified.

        DSS property name: `MonitoredObj`, DSS property index: 1.
        """
        return self._get_obj(1, None)

    @MonitoredObj_obj.setter
    def MonitoredObj_obj(self, value: DSSObj):
        self._set_obj(1, value)

    @property
    def MonitoredTerm(self) -> int:
        """
        Number of the terminal of the circuit element to which the Recloser is connected. 1 or 2, typically.  Default is 1.

        DSS property name: `MonitoredTerm`, DSS property index: 2.
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @MonitoredTerm.setter
    def MonitoredTerm(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def SwitchedObj(self) -> str:
        """
        Name of circuit element switch that the Recloser controls. Specify the full object name.Defaults to the same as the Monitored element. This is the "controlled" element.

        DSS property name: `SwitchedObj`, DSS property index: 3.
        """
        return self._get_prop_string(3)

    @SwitchedObj.setter
    def SwitchedObj(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_obj(3, value)
            return

        self._set_string_o(3, value)

    @property
    def SwitchedObj_obj(self) -> DSSObj:
        """
        Name of circuit element switch that the Recloser controls. Specify the full object name.Defaults to the same as the Monitored element. This is the "controlled" element.

        DSS property name: `SwitchedObj`, DSS property index: 3.
        """
        return self._get_obj(3, None)

    @SwitchedObj_obj.setter
    def SwitchedObj_obj(self, value: DSSObj):
        self._set_obj(3, value)

    @property
    def SwitchedTerm(self) -> int:
        """
        Number of the terminal of the controlled element in which the switch is controlled by the Recloser. 1 or 2, typically.  Default is 1.

        DSS property name: `SwitchedTerm`, DSS property index: 4.
        """
        return self._lib.Obj_GetInt32(self._ptr, 4)

    @SwitchedTerm.setter
    def SwitchedTerm(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 4, value)

    @property
    def NumFast(self) -> int:
        """
        Number of Fast (fuse saving) operations.  Default is 1. (See "Shots")

        DSS property name: `NumFast`, DSS property index: 5.
        """
        return self._lib.Obj_GetInt32(self._ptr, 5)

    @NumFast.setter
    def NumFast(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 5, value)

    @property
    def PhaseFast(self) -> str:
        """
        Name of the TCC Curve object that determines the Phase Fast trip.  Must have been previously defined as a TCC_Curve object. Default is "A". Multiplying the current values in the curve by the "phasetrip" value gives the actual current.

        DSS property name: `PhaseFast`, DSS property index: 6.
        """
        return self._get_prop_string(6)

    @PhaseFast.setter
    def PhaseFast(self, value: Union[AnyStr, TCC_Curve]):
        if isinstance(value, DSSObj):
            self._set_obj(6, value)
            return

        self._set_string_o(6, value)

    @property
    def PhaseFast_obj(self) -> TCC_Curve:
        """
        Name of the TCC Curve object that determines the Phase Fast trip.  Must have been previously defined as a TCC_Curve object. Default is "A". Multiplying the current values in the curve by the "phasetrip" value gives the actual current.

        DSS property name: `PhaseFast`, DSS property index: 6.
        """
        return self._get_obj(6, TCC_Curve)

    @PhaseFast_obj.setter
    def PhaseFast_obj(self, value: TCC_Curve):
        self._set_obj(6, value)

    @property
    def PhaseDelayed(self) -> str:
        """
        Name of the TCC Curve object that determines the Phase Delayed trip.  Must have been previously defined as a TCC_Curve object. Default is "D".Multiplying the current values in the curve by the "phasetrip" value gives the actual current.

        DSS property name: `PhaseDelayed`, DSS property index: 7.
        """
        return self._get_prop_string(7)

    @PhaseDelayed.setter
    def PhaseDelayed(self, value: Union[AnyStr, TCC_Curve]):
        if isinstance(value, DSSObj):
            self._set_obj(7, value)
            return

        self._set_string_o(7, value)

    @property
    def PhaseDelayed_obj(self) -> TCC_Curve:
        """
        Name of the TCC Curve object that determines the Phase Delayed trip.  Must have been previously defined as a TCC_Curve object. Default is "D".Multiplying the current values in the curve by the "phasetrip" value gives the actual current.

        DSS property name: `PhaseDelayed`, DSS property index: 7.
        """
        return self._get_obj(7, TCC_Curve)

    @PhaseDelayed_obj.setter
    def PhaseDelayed_obj(self, value: TCC_Curve):
        self._set_obj(7, value)

    @property
    def GroundFast(self) -> str:
        """
        Name of the TCC Curve object that determines the Ground Fast trip.  Must have been previously defined as a TCC_Curve object. Default is none (ignored). Multiplying the current values in the curve by the "groundtrip" value gives the actual current.

        DSS property name: `GroundFast`, DSS property index: 8.
        """
        return self._get_prop_string(8)

    @GroundFast.setter
    def GroundFast(self, value: Union[AnyStr, TCC_Curve]):
        if isinstance(value, DSSObj):
            self._set_obj(8, value)
            return

        self._set_string_o(8, value)

    @property
    def GroundFast_obj(self) -> TCC_Curve:
        """
        Name of the TCC Curve object that determines the Ground Fast trip.  Must have been previously defined as a TCC_Curve object. Default is none (ignored). Multiplying the current values in the curve by the "groundtrip" value gives the actual current.

        DSS property name: `GroundFast`, DSS property index: 8.
        """
        return self._get_obj(8, TCC_Curve)

    @GroundFast_obj.setter
    def GroundFast_obj(self, value: TCC_Curve):
        self._set_obj(8, value)

    @property
    def GroundDelayed(self) -> str:
        """
        Name of the TCC Curve object that determines the Ground Delayed trip.  Must have been previously defined as a TCC_Curve object. Default is none (ignored).Multiplying the current values in the curve by the "groundtrip" value gives the actual current.

        DSS property name: `GroundDelayed`, DSS property index: 9.
        """
        return self._get_prop_string(9)

    @GroundDelayed.setter
    def GroundDelayed(self, value: Union[AnyStr, TCC_Curve]):
        if isinstance(value, DSSObj):
            self._set_obj(9, value)
            return

        self._set_string_o(9, value)

    @property
    def GroundDelayed_obj(self) -> TCC_Curve:
        """
        Name of the TCC Curve object that determines the Ground Delayed trip.  Must have been previously defined as a TCC_Curve object. Default is none (ignored).Multiplying the current values in the curve by the "groundtrip" value gives the actual current.

        DSS property name: `GroundDelayed`, DSS property index: 9.
        """
        return self._get_obj(9, TCC_Curve)

    @GroundDelayed_obj.setter
    def GroundDelayed_obj(self, value: TCC_Curve):
        self._set_obj(9, value)

    @property
    def PhaseTrip(self) -> float:
        """
        Multiplier or actual phase amps for the phase TCC curve.  Defaults to 1.0.

        DSS property name: `PhaseTrip`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @PhaseTrip.setter
    def PhaseTrip(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def GroundTrip(self) -> float:
        """
        Multiplier or actual ground amps (3I0) for the ground TCC curve.  Defaults to 1.0.

        DSS property name: `GroundTrip`, DSS property index: 11.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @GroundTrip.setter
    def GroundTrip(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def PhaseInst(self) -> float:
        """
        Actual amps for instantaneous phase trip which is assumed to happen in 0.01 sec + Delay Time. Default is 0.0, which signifies no inst trip. 

        DSS property name: `PhaseInst`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @PhaseInst.setter
    def PhaseInst(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def GroundInst(self) -> float:
        """
        Actual amps for instantaneous ground trip which is assumed to happen in 0.01 sec + Delay Time.Default is 0.0, which signifies no inst trip.

        DSS property name: `GroundInst`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @GroundInst.setter
    def GroundInst(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def Reset(self) -> float:
        """
        Reset time in sec for Recloser.  Default is 15. 

        DSS property name: `Reset`, DSS property index: 14.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @Reset.setter
    def Reset(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def Shots(self) -> int:
        """
        Total Number of fast and delayed shots to lockout.  Default is 4. This is one more than the number of reclose intervals.

        DSS property name: `Shots`, DSS property index: 15.
        """
        return self._lib.Obj_GetInt32(self._ptr, 15)

    @Shots.setter
    def Shots(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 15, value)

    @property
    def RecloseIntervals(self) -> Float64Array:
        """
        Array of reclose intervals.  Default for Recloser is (0.5, 2.0, 2.0) seconds. A locked out Recloser must be closed manually (action=close).

        DSS property name: `RecloseIntervals`, DSS property index: 16.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 16)

    @RecloseIntervals.setter
    def RecloseIntervals(self, value: Float64Array):
        self._set_float64_array_o(16, value)

    @property
    def Delay(self) -> float:
        """
        Fixed delay time (sec) added to Recloser trip time. Default is 0.0. Used to represent breaker time or any other delay.

        DSS property name: `Delay`, DSS property index: 17.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    @Delay.setter
    def Delay(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 17, value)

    @property
    def TDPhFast(self) -> float:
        """
        Time dial for Phase Fast trip curve. Multiplier on time axis of specified curve. Default=1.0.

        DSS property name: `TDPhFast`, DSS property index: 19.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    @TDPhFast.setter
    def TDPhFast(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 19, value)

    @property
    def TDGrFast(self) -> float:
        """
        Time dial for Ground Fast trip curve. Multiplier on time axis of specified curve. Default=1.0.

        DSS property name: `TDGrFast`, DSS property index: 20.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    @TDGrFast.setter
    def TDGrFast(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 20, value)

    @property
    def TDPhDelayed(self) -> float:
        """
        Time dial for Phase Delayed trip curve. Multiplier on time axis of specified curve. Default=1.0.

        DSS property name: `TDPhDelayed`, DSS property index: 21.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @TDPhDelayed.setter
    def TDPhDelayed(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    @property
    def TDGrDelayed(self) -> float:
        """
        Time dial for Ground Delayed trip curve. Multiplier on time axis of specified curve. Default=1.0.

        DSS property name: `TDGrDelayed`, DSS property index: 22.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    @TDGrDelayed.setter
    def TDGrDelayed(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 22, value)

    @property
    def Normal(self) -> enums.RecloserState:
        """
        {Open | Closed} Normal state of the recloser. The recloser reverts to this state for reset, change of mode, etc. Defaults to "State" if not specifically declared.

        DSS property name: `Normal`, DSS property index: 23.
        """
        return enums.RecloserState(self._lib.Obj_GetInt32(self._ptr, 23))

    @Normal.setter
    def Normal(self, value: Union[AnyStr, int, enums.RecloserState]):
        if not isinstance(value, int):
            self._set_string_o(23, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 23, value)

    @property
    def Normal_str(self) -> str:
        """
        {Open | Closed} Normal state of the recloser. The recloser reverts to this state for reset, change of mode, etc. Defaults to "State" if not specifically declared.

        DSS property name: `Normal`, DSS property index: 23.
        """
        return self._get_prop_string(23)

    @Normal_str.setter
    def Normal_str(self, value: AnyStr):
        self.Normal = value

    @property
    def State(self) -> enums.RecloserState:
        """
        {Open | Closed} Actual state of the recloser. Upon setting, immediately forces state of the recloser, overriding the Recloser control. Simulates manual control on recloser. Defaults to Closed. "Open" causes the controlled element to open and lock out. "Closed" causes the controlled element to close and the recloser to reset to its first operation.

        DSS property name: `State`, DSS property index: 24.
        """
        return enums.RecloserState(self._lib.Obj_GetInt32(self._ptr, 24))

    @State.setter
    def State(self, value: Union[AnyStr, int, enums.RecloserState]):
        if not isinstance(value, int):
            self._set_string_o(24, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 24, value)

    @property
    def State_str(self) -> str:
        """
        {Open | Closed} Actual state of the recloser. Upon setting, immediately forces state of the recloser, overriding the Recloser control. Simulates manual control on recloser. Defaults to Closed. "Open" causes the controlled element to open and lock out. "Closed" causes the controlled element to close and the recloser to reset to its first operation.

        DSS property name: `State`, DSS property index: 24.
        """
        return self._get_prop_string(24)

    @State_str.setter
    def State_str(self, value: AnyStr):
        self.State = value

    @property
    def BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 25.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 25)

    @BaseFreq.setter
    def BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 25, value)

    @property
    def Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 26.
        """
        return self._lib.Obj_GetInt32(self._ptr, 26) != 0

    @Enabled.setter
    def Enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 26, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 27.
        """
        self._set_string_o(27, value)


class RecloserProperties(TypedDict):
    MonitoredObj: Union[AnyStr, DSSObj]
    MonitoredTerm: int
    SwitchedObj: Union[AnyStr, DSSObj]
    SwitchedTerm: int
    NumFast: int
    PhaseFast: Union[AnyStr, TCC_Curve]
    PhaseDelayed: Union[AnyStr, TCC_Curve]
    GroundFast: Union[AnyStr, TCC_Curve]
    GroundDelayed: Union[AnyStr, TCC_Curve]
    PhaseTrip: float
    GroundTrip: float
    PhaseInst: float
    GroundInst: float
    Reset: float
    Shots: int
    RecloseIntervals: Float64Array
    Delay: float
    TDPhFast: float
    TDGrFast: float
    TDPhDelayed: float
    TDGrDelayed: float
    Normal: Union[AnyStr, int, enums.RecloserState]
    State: Union[AnyStr, int, enums.RecloserState]
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class RecloserBatch(DSSBatch):
    _cls_name = 'Recloser'
    _obj_cls = Recloser
    _cls_idx = 32


    @property
    def MonitoredObj(self) -> List[str]:
        """
        Full object name of the circuit element, typically a line, transformer, load, or generator, to which the Recloser's PT and/or CT are connected. This is the "monitored" element. There is no default; must be specified.

        DSS property name: `MonitoredObj`, DSS property index: 1.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @MonitoredObj.setter
    def MonitoredObj(self, value: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]]):
        self._set_batch_obj_prop(1, value)

    @property
    def MonitoredObj_obj(self) -> List[DSSObj]:
        """
        Full object name of the circuit element, typically a line, transformer, load, or generator, to which the Recloser's PT and/or CT are connected. This is the "monitored" element. There is no default; must be specified.

        DSS property name: `MonitoredObj`, DSS property index: 1.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 1)

    @MonitoredObj_obj.setter
    def MonitoredObj_obj(self, value: DSSObj):
        self._set_batch_string(1, value)

    @property
    def MonitoredTerm(self) -> BatchInt32ArrayProxy:
        """
        Number of the terminal of the circuit element to which the Recloser is connected. 1 or 2, typically.  Default is 1.

        DSS property name: `MonitoredTerm`, DSS property index: 2.
        """
        return BatchInt32ArrayProxy(self, 2)

    @MonitoredTerm.setter
    def MonitoredTerm(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(2, value)

    @property
    def SwitchedObj(self) -> List[str]:
        """
        Name of circuit element switch that the Recloser controls. Specify the full object name.Defaults to the same as the Monitored element. This is the "controlled" element.

        DSS property name: `SwitchedObj`, DSS property index: 3.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 3)

    @SwitchedObj.setter
    def SwitchedObj(self, value: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]]):
        self._set_batch_obj_prop(3, value)

    @property
    def SwitchedObj_obj(self) -> List[DSSObj]:
        """
        Name of circuit element switch that the Recloser controls. Specify the full object name.Defaults to the same as the Monitored element. This is the "controlled" element.

        DSS property name: `SwitchedObj`, DSS property index: 3.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 3)

    @SwitchedObj_obj.setter
    def SwitchedObj_obj(self, value: DSSObj):
        self._set_batch_string(3, value)

    @property
    def SwitchedTerm(self) -> BatchInt32ArrayProxy:
        """
        Number of the terminal of the controlled element in which the switch is controlled by the Recloser. 1 or 2, typically.  Default is 1.

        DSS property name: `SwitchedTerm`, DSS property index: 4.
        """
        return BatchInt32ArrayProxy(self, 4)

    @SwitchedTerm.setter
    def SwitchedTerm(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(4, value)

    @property
    def NumFast(self) -> BatchInt32ArrayProxy:
        """
        Number of Fast (fuse saving) operations.  Default is 1. (See "Shots")

        DSS property name: `NumFast`, DSS property index: 5.
        """
        return BatchInt32ArrayProxy(self, 5)

    @NumFast.setter
    def NumFast(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(5, value)

    @property
    def PhaseFast(self) -> List[str]:
        """
        Name of the TCC Curve object that determines the Phase Fast trip.  Must have been previously defined as a TCC_Curve object. Default is "A". Multiplying the current values in the curve by the "phasetrip" value gives the actual current.

        DSS property name: `PhaseFast`, DSS property index: 6.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 6)

    @PhaseFast.setter
    def PhaseFast(self, value: Union[AnyStr, TCC_Curve, List[AnyStr], List[TCC_Curve]]):
        self._set_batch_obj_prop(6, value)

    @property
    def PhaseFast_obj(self) -> List[TCC_Curve]:
        """
        Name of the TCC Curve object that determines the Phase Fast trip.  Must have been previously defined as a TCC_Curve object. Default is "A". Multiplying the current values in the curve by the "phasetrip" value gives the actual current.

        DSS property name: `PhaseFast`, DSS property index: 6.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 6)

    @PhaseFast_obj.setter
    def PhaseFast_obj(self, value: TCC_Curve):
        self._set_batch_string(6, value)

    @property
    def PhaseDelayed(self) -> List[str]:
        """
        Name of the TCC Curve object that determines the Phase Delayed trip.  Must have been previously defined as a TCC_Curve object. Default is "D".Multiplying the current values in the curve by the "phasetrip" value gives the actual current.

        DSS property name: `PhaseDelayed`, DSS property index: 7.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 7)

    @PhaseDelayed.setter
    def PhaseDelayed(self, value: Union[AnyStr, TCC_Curve, List[AnyStr], List[TCC_Curve]]):
        self._set_batch_obj_prop(7, value)

    @property
    def PhaseDelayed_obj(self) -> List[TCC_Curve]:
        """
        Name of the TCC Curve object that determines the Phase Delayed trip.  Must have been previously defined as a TCC_Curve object. Default is "D".Multiplying the current values in the curve by the "phasetrip" value gives the actual current.

        DSS property name: `PhaseDelayed`, DSS property index: 7.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 7)

    @PhaseDelayed_obj.setter
    def PhaseDelayed_obj(self, value: TCC_Curve):
        self._set_batch_string(7, value)

    @property
    def GroundFast(self) -> List[str]:
        """
        Name of the TCC Curve object that determines the Ground Fast trip.  Must have been previously defined as a TCC_Curve object. Default is none (ignored). Multiplying the current values in the curve by the "groundtrip" value gives the actual current.

        DSS property name: `GroundFast`, DSS property index: 8.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 8)

    @GroundFast.setter
    def GroundFast(self, value: Union[AnyStr, TCC_Curve, List[AnyStr], List[TCC_Curve]]):
        self._set_batch_obj_prop(8, value)

    @property
    def GroundFast_obj(self) -> List[TCC_Curve]:
        """
        Name of the TCC Curve object that determines the Ground Fast trip.  Must have been previously defined as a TCC_Curve object. Default is none (ignored). Multiplying the current values in the curve by the "groundtrip" value gives the actual current.

        DSS property name: `GroundFast`, DSS property index: 8.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 8)

    @GroundFast_obj.setter
    def GroundFast_obj(self, value: TCC_Curve):
        self._set_batch_string(8, value)

    @property
    def GroundDelayed(self) -> List[str]:
        """
        Name of the TCC Curve object that determines the Ground Delayed trip.  Must have been previously defined as a TCC_Curve object. Default is none (ignored).Multiplying the current values in the curve by the "groundtrip" value gives the actual current.

        DSS property name: `GroundDelayed`, DSS property index: 9.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 9)

    @GroundDelayed.setter
    def GroundDelayed(self, value: Union[AnyStr, TCC_Curve, List[AnyStr], List[TCC_Curve]]):
        self._set_batch_obj_prop(9, value)

    @property
    def GroundDelayed_obj(self) -> List[TCC_Curve]:
        """
        Name of the TCC Curve object that determines the Ground Delayed trip.  Must have been previously defined as a TCC_Curve object. Default is none (ignored).Multiplying the current values in the curve by the "groundtrip" value gives the actual current.

        DSS property name: `GroundDelayed`, DSS property index: 9.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 9)

    @GroundDelayed_obj.setter
    def GroundDelayed_obj(self, value: TCC_Curve):
        self._set_batch_string(9, value)

    @property
    def PhaseTrip(self) -> BatchFloat64ArrayProxy:
        """
        Multiplier or actual phase amps for the phase TCC curve.  Defaults to 1.0.

        DSS property name: `PhaseTrip`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    @PhaseTrip.setter
    def PhaseTrip(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(10, value)

    @property
    def GroundTrip(self) -> BatchFloat64ArrayProxy:
        """
        Multiplier or actual ground amps (3I0) for the ground TCC curve.  Defaults to 1.0.

        DSS property name: `GroundTrip`, DSS property index: 11.
        """
        return BatchFloat64ArrayProxy(self, 11)

    @GroundTrip.setter
    def GroundTrip(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(11, value)

    @property
    def PhaseInst(self) -> BatchFloat64ArrayProxy:
        """
        Actual amps for instantaneous phase trip which is assumed to happen in 0.01 sec + Delay Time. Default is 0.0, which signifies no inst trip. 

        DSS property name: `PhaseInst`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    @PhaseInst.setter
    def PhaseInst(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(12, value)

    @property
    def GroundInst(self) -> BatchFloat64ArrayProxy:
        """
        Actual amps for instantaneous ground trip which is assumed to happen in 0.01 sec + Delay Time.Default is 0.0, which signifies no inst trip.

        DSS property name: `GroundInst`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    @GroundInst.setter
    def GroundInst(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(13, value)

    @property
    def Reset(self) -> BatchFloat64ArrayProxy:
        """
        Reset time in sec for Recloser.  Default is 15. 

        DSS property name: `Reset`, DSS property index: 14.
        """
        return BatchFloat64ArrayProxy(self, 14)

    @Reset.setter
    def Reset(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(14, value)

    @property
    def Shots(self) -> BatchInt32ArrayProxy:
        """
        Total Number of fast and delayed shots to lockout.  Default is 4. This is one more than the number of reclose intervals.

        DSS property name: `Shots`, DSS property index: 15.
        """
        return BatchInt32ArrayProxy(self, 15)

    @Shots.setter
    def Shots(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(15, value)

    @property
    def RecloseIntervals(self) -> List[Float64Array]:
        """
        Array of reclose intervals.  Default for Recloser is (0.5, 2.0, 2.0) seconds. A locked out Recloser must be closed manually (action=close).

        DSS property name: `RecloseIntervals`, DSS property index: 16.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 16)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @RecloseIntervals.setter
    def RecloseIntervals(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(16, value)

    @property
    def Delay(self) -> BatchFloat64ArrayProxy:
        """
        Fixed delay time (sec) added to Recloser trip time. Default is 0.0. Used to represent breaker time or any other delay.

        DSS property name: `Delay`, DSS property index: 17.
        """
        return BatchFloat64ArrayProxy(self, 17)

    @Delay.setter
    def Delay(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(17, value)

    @property
    def TDPhFast(self) -> BatchFloat64ArrayProxy:
        """
        Time dial for Phase Fast trip curve. Multiplier on time axis of specified curve. Default=1.0.

        DSS property name: `TDPhFast`, DSS property index: 19.
        """
        return BatchFloat64ArrayProxy(self, 19)

    @TDPhFast.setter
    def TDPhFast(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(19, value)

    @property
    def TDGrFast(self) -> BatchFloat64ArrayProxy:
        """
        Time dial for Ground Fast trip curve. Multiplier on time axis of specified curve. Default=1.0.

        DSS property name: `TDGrFast`, DSS property index: 20.
        """
        return BatchFloat64ArrayProxy(self, 20)

    @TDGrFast.setter
    def TDGrFast(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(20, value)

    @property
    def TDPhDelayed(self) -> BatchFloat64ArrayProxy:
        """
        Time dial for Phase Delayed trip curve. Multiplier on time axis of specified curve. Default=1.0.

        DSS property name: `TDPhDelayed`, DSS property index: 21.
        """
        return BatchFloat64ArrayProxy(self, 21)

    @TDPhDelayed.setter
    def TDPhDelayed(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(21, value)

    @property
    def TDGrDelayed(self) -> BatchFloat64ArrayProxy:
        """
        Time dial for Ground Delayed trip curve. Multiplier on time axis of specified curve. Default=1.0.

        DSS property name: `TDGrDelayed`, DSS property index: 22.
        """
        return BatchFloat64ArrayProxy(self, 22)

    @TDGrDelayed.setter
    def TDGrDelayed(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(22, value)

    @property
    def Normal(self) -> BatchInt32ArrayProxy:
        """
        {Open | Closed} Normal state of the recloser. The recloser reverts to this state for reset, change of mode, etc. Defaults to "State" if not specifically declared.

        DSS property name: `Normal`, DSS property index: 23.
        """
        return BatchInt32ArrayProxy(self, 23)

    @Normal.setter
    def Normal(self, value: Union[AnyStr, int, enums.RecloserState, List[AnyStr], List[int], List[enums.RecloserState], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(23, value)
            return
    
        self._set_batch_int32_array(23, value)

    @property
    def Normal_str(self) -> str:
        """
        {Open | Closed} Normal state of the recloser. The recloser reverts to this state for reset, change of mode, etc. Defaults to "State" if not specifically declared.

        DSS property name: `Normal`, DSS property index: 23.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 23)

    @Normal_str.setter
    def Normal_str(self, value: AnyStr):
        self.Normal = value

    @property
    def State(self) -> BatchInt32ArrayProxy:
        """
        {Open | Closed} Actual state of the recloser. Upon setting, immediately forces state of the recloser, overriding the Recloser control. Simulates manual control on recloser. Defaults to Closed. "Open" causes the controlled element to open and lock out. "Closed" causes the controlled element to close and the recloser to reset to its first operation.

        DSS property name: `State`, DSS property index: 24.
        """
        return BatchInt32ArrayProxy(self, 24)

    @State.setter
    def State(self, value: Union[AnyStr, int, enums.RecloserState, List[AnyStr], List[int], List[enums.RecloserState], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(24, value)
            return
    
        self._set_batch_int32_array(24, value)

    @property
    def State_str(self) -> str:
        """
        {Open | Closed} Actual state of the recloser. Upon setting, immediately forces state of the recloser, overriding the Recloser control. Simulates manual control on recloser. Defaults to Closed. "Open" causes the controlled element to open and lock out. "Closed" causes the controlled element to close and the recloser to reset to its first operation.

        DSS property name: `State`, DSS property index: 24.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 24)

    @State_str.setter
    def State_str(self, value: AnyStr):
        self.State = value

    @property
    def BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 25.
        """
        return BatchFloat64ArrayProxy(self, 25)

    @BaseFreq.setter
    def BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(25, value)

    @property
    def Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 26.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 26)
        ]
    @Enabled.setter
    def Enabled(self, value: bool):
        self._set_batch_int32_array(26, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 27.
        """
        self._set_batch_string(27, value)

class RecloserBatchProperties(TypedDict):
    MonitoredObj: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]]
    MonitoredTerm: Union[int, Int32Array]
    SwitchedObj: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]]
    SwitchedTerm: Union[int, Int32Array]
    NumFast: Union[int, Int32Array]
    PhaseFast: Union[AnyStr, TCC_Curve, List[AnyStr], List[TCC_Curve]]
    PhaseDelayed: Union[AnyStr, TCC_Curve, List[AnyStr], List[TCC_Curve]]
    GroundFast: Union[AnyStr, TCC_Curve, List[AnyStr], List[TCC_Curve]]
    GroundDelayed: Union[AnyStr, TCC_Curve, List[AnyStr], List[TCC_Curve]]
    PhaseTrip: Union[float, Float64Array]
    GroundTrip: Union[float, Float64Array]
    PhaseInst: Union[float, Float64Array]
    GroundInst: Union[float, Float64Array]
    Reset: Union[float, Float64Array]
    Shots: Union[int, Int32Array]
    RecloseIntervals: Float64Array
    Delay: Union[float, Float64Array]
    TDPhFast: Union[float, Float64Array]
    TDGrFast: Union[float, Float64Array]
    TDPhDelayed: Union[float, Float64Array]
    TDGrDelayed: Union[float, Float64Array]
    Normal: Union[AnyStr, int, enums.RecloserState, List[AnyStr], List[int], List[enums.RecloserState], Int32Array]
    State: Union[AnyStr, int, enums.RecloserState, List[AnyStr], List[int], List[enums.RecloserState], Int32Array]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IRecloser(IDSSObj):
    __slots__ = ()

    def __init__(self, iobj):
        super().__init__(iobj, Recloser, RecloserBatch)

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Recloser:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[RecloserProperties]) -> Recloser:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[RecloserBatchProperties]) -> RecloserBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
