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
from .CircuitElement import CircuitElementBatchMixin, CircuitElementMixin
from .TCC_Curve import TCC_Curve

class Recloser(DSSObj, CircuitElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots
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

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)

    def _get_MonitoredObj_str(self) -> str:
        """
        Full object name of the circuit element, typically a line, transformer, load, or generator, to which the Recloser's PT and/or CT are connected. This is the "monitored" element. There is no default; must be specified.

        DSS property name: `MonitoredObj`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    def _set_MonitoredObj_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(1, value, flags)

    MonitoredObj_str = property(_get_MonitoredObj_str, _set_MonitoredObj_str) # type: str

    def _get_MonitoredObj(self) -> DSSObj:
        """
        Full object name of the circuit element, typically a line, transformer, load, or generator, to which the Recloser's PT and/or CT are connected. This is the "monitored" element. There is no default; must be specified.

        DSS property name: `MonitoredObj`, DSS property index: 1.
        """
        return self._get_obj(1, None)

    def _set_MonitoredObj(self, value: Union[AnyStr, DSSObj], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(1, value, flags)
            return

        self._set_string_o(1, value, flags)

    MonitoredObj = property(_get_MonitoredObj, _set_MonitoredObj) # type: DSSObj

    def _get_MonitoredTerm(self) -> int:
        """
        Number of the terminal of the circuit element to which the Recloser is connected. 1 or 2, typically.  Default is 1.

        DSS property name: `MonitoredTerm`, DSS property index: 2.
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    def _set_MonitoredTerm(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 2, value, flags)

    MonitoredTerm = property(_get_MonitoredTerm, _set_MonitoredTerm) # type: int

    def _get_SwitchedObj_str(self) -> str:
        """
        Name of circuit element switch that the Recloser controls. Specify the full object name.Defaults to the same as the Monitored element. This is the "controlled" element.

        DSS property name: `SwitchedObj`, DSS property index: 3.
        """
        return self._get_prop_string(3)

    def _set_SwitchedObj_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(3, value, flags)

    SwitchedObj_str = property(_get_SwitchedObj_str, _set_SwitchedObj_str) # type: str

    def _get_SwitchedObj(self) -> DSSObj:
        """
        Name of circuit element switch that the Recloser controls. Specify the full object name.Defaults to the same as the Monitored element. This is the "controlled" element.

        DSS property name: `SwitchedObj`, DSS property index: 3.
        """
        return self._get_obj(3, None)

    def _set_SwitchedObj(self, value: Union[AnyStr, DSSObj], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(3, value, flags)
            return

        self._set_string_o(3, value, flags)

    SwitchedObj = property(_get_SwitchedObj, _set_SwitchedObj) # type: DSSObj

    def _get_SwitchedTerm(self) -> int:
        """
        Number of the terminal of the controlled element in which the switch is controlled by the Recloser. 1 or 2, typically.  Default is 1.

        DSS property name: `SwitchedTerm`, DSS property index: 4.
        """
        return self._lib.Obj_GetInt32(self._ptr, 4)

    def _set_SwitchedTerm(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 4, value, flags)

    SwitchedTerm = property(_get_SwitchedTerm, _set_SwitchedTerm) # type: int

    def _get_NumFast(self) -> int:
        """
        Number of Fast (fuse saving) operations.  Default is 1. (See "Shots")

        DSS property name: `NumFast`, DSS property index: 5.
        """
        return self._lib.Obj_GetInt32(self._ptr, 5)

    def _set_NumFast(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 5, value, flags)

    NumFast = property(_get_NumFast, _set_NumFast) # type: int

    def _get_PhaseFast_str(self) -> str:
        """
        Name of the TCC Curve object that determines the Phase Fast trip.  Must have been previously defined as a TCC_Curve object. Default is "A". Multiplying the current values in the curve by the "phasetrip" value gives the actual current.

        DSS property name: `PhaseFast`, DSS property index: 6.
        """
        return self._get_prop_string(6)

    def _set_PhaseFast_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(6, value, flags)

    PhaseFast_str = property(_get_PhaseFast_str, _set_PhaseFast_str) # type: str

    def _get_PhaseFast(self) -> TCC_Curve:
        """
        Name of the TCC Curve object that determines the Phase Fast trip.  Must have been previously defined as a TCC_Curve object. Default is "A". Multiplying the current values in the curve by the "phasetrip" value gives the actual current.

        DSS property name: `PhaseFast`, DSS property index: 6.
        """
        return self._get_obj(6, TCC_Curve)

    def _set_PhaseFast(self, value: Union[AnyStr, TCC_Curve], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(6, value, flags)
            return

        self._set_string_o(6, value, flags)

    PhaseFast = property(_get_PhaseFast, _set_PhaseFast) # type: TCC_Curve

    def _get_PhaseDelayed_str(self) -> str:
        """
        Name of the TCC Curve object that determines the Phase Delayed trip.  Must have been previously defined as a TCC_Curve object. Default is "D".Multiplying the current values in the curve by the "phasetrip" value gives the actual current.

        DSS property name: `PhaseDelayed`, DSS property index: 7.
        """
        return self._get_prop_string(7)

    def _set_PhaseDelayed_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(7, value, flags)

    PhaseDelayed_str = property(_get_PhaseDelayed_str, _set_PhaseDelayed_str) # type: str

    def _get_PhaseDelayed(self) -> TCC_Curve:
        """
        Name of the TCC Curve object that determines the Phase Delayed trip.  Must have been previously defined as a TCC_Curve object. Default is "D".Multiplying the current values in the curve by the "phasetrip" value gives the actual current.

        DSS property name: `PhaseDelayed`, DSS property index: 7.
        """
        return self._get_obj(7, TCC_Curve)

    def _set_PhaseDelayed(self, value: Union[AnyStr, TCC_Curve], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(7, value, flags)
            return

        self._set_string_o(7, value, flags)

    PhaseDelayed = property(_get_PhaseDelayed, _set_PhaseDelayed) # type: TCC_Curve

    def _get_GroundFast_str(self) -> str:
        """
        Name of the TCC Curve object that determines the Ground Fast trip.  Must have been previously defined as a TCC_Curve object. Default is none (ignored). Multiplying the current values in the curve by the "groundtrip" value gives the actual current.

        DSS property name: `GroundFast`, DSS property index: 8.
        """
        return self._get_prop_string(8)

    def _set_GroundFast_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(8, value, flags)

    GroundFast_str = property(_get_GroundFast_str, _set_GroundFast_str) # type: str

    def _get_GroundFast(self) -> TCC_Curve:
        """
        Name of the TCC Curve object that determines the Ground Fast trip.  Must have been previously defined as a TCC_Curve object. Default is none (ignored). Multiplying the current values in the curve by the "groundtrip" value gives the actual current.

        DSS property name: `GroundFast`, DSS property index: 8.
        """
        return self._get_obj(8, TCC_Curve)

    def _set_GroundFast(self, value: Union[AnyStr, TCC_Curve], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(8, value, flags)
            return

        self._set_string_o(8, value, flags)

    GroundFast = property(_get_GroundFast, _set_GroundFast) # type: TCC_Curve

    def _get_GroundDelayed_str(self) -> str:
        """
        Name of the TCC Curve object that determines the Ground Delayed trip.  Must have been previously defined as a TCC_Curve object. Default is none (ignored).Multiplying the current values in the curve by the "groundtrip" value gives the actual current.

        DSS property name: `GroundDelayed`, DSS property index: 9.
        """
        return self._get_prop_string(9)

    def _set_GroundDelayed_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(9, value, flags)

    GroundDelayed_str = property(_get_GroundDelayed_str, _set_GroundDelayed_str) # type: str

    def _get_GroundDelayed(self) -> TCC_Curve:
        """
        Name of the TCC Curve object that determines the Ground Delayed trip.  Must have been previously defined as a TCC_Curve object. Default is none (ignored).Multiplying the current values in the curve by the "groundtrip" value gives the actual current.

        DSS property name: `GroundDelayed`, DSS property index: 9.
        """
        return self._get_obj(9, TCC_Curve)

    def _set_GroundDelayed(self, value: Union[AnyStr, TCC_Curve], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(9, value, flags)
            return

        self._set_string_o(9, value, flags)

    GroundDelayed = property(_get_GroundDelayed, _set_GroundDelayed) # type: TCC_Curve

    def _get_PhaseTrip(self) -> float:
        """
        Multiplier or actual phase amps for the phase TCC curve.  Defaults to 1.0.

        DSS property name: `PhaseTrip`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    def _set_PhaseTrip(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 10, value, flags)

    PhaseTrip = property(_get_PhaseTrip, _set_PhaseTrip) # type: float

    def _get_GroundTrip(self) -> float:
        """
        Multiplier or actual ground amps (3I0) for the ground TCC curve.  Defaults to 1.0.

        DSS property name: `GroundTrip`, DSS property index: 11.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    def _set_GroundTrip(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 11, value, flags)

    GroundTrip = property(_get_GroundTrip, _set_GroundTrip) # type: float

    def _get_PhaseInst(self) -> float:
        """
        Actual amps for instantaneous phase trip which is assumed to happen in 0.01 sec + Delay Time. Default is 0.0, which signifies no inst trip. 

        DSS property name: `PhaseInst`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    def _set_PhaseInst(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 12, value, flags)

    PhaseInst = property(_get_PhaseInst, _set_PhaseInst) # type: float

    def _get_GroundInst(self) -> float:
        """
        Actual amps for instantaneous ground trip which is assumed to happen in 0.01 sec + Delay Time.Default is 0.0, which signifies no inst trip.

        DSS property name: `GroundInst`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    def _set_GroundInst(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 13, value, flags)

    GroundInst = property(_get_GroundInst, _set_GroundInst) # type: float

    def _get_Reset(self) -> float:
        """
        Reset time in sec for Recloser.  Default is 15. 

        DSS property name: `Reset`, DSS property index: 14.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    def _set_Reset(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 14, value, flags)

    Reset = property(_get_Reset, _set_Reset) # type: float

    def _get_Shots(self) -> int:
        """
        Total Number of fast and delayed shots to lockout.  Default is 4. This is one more than the number of reclose intervals.

        DSS property name: `Shots`, DSS property index: 15.
        """
        return self._lib.Obj_GetInt32(self._ptr, 15)

    def _set_Shots(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 15, value, flags)

    Shots = property(_get_Shots, _set_Shots) # type: int

    def _get_RecloseIntervals(self) -> Float64Array:
        """
        Array of reclose intervals.  Default for Recloser is (0.5, 2.0, 2.0) seconds. A locked out Recloser must be closed manually (action=close).

        DSS property name: `RecloseIntervals`, DSS property index: 16.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 16)

    def _set_RecloseIntervals(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(16, value, flags)

    RecloseIntervals = property(_get_RecloseIntervals, _set_RecloseIntervals) # type: Float64Array

    def _get_Delay(self) -> float:
        """
        Fixed delay time (sec) added to Recloser trip time. Default is 0.0. Used to represent breaker time or any other delay.

        DSS property name: `Delay`, DSS property index: 17.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    def _set_Delay(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 17, value, flags)

    Delay = property(_get_Delay, _set_Delay) # type: float

    def _get_TDPhFast(self) -> float:
        """
        Time dial for Phase Fast trip curve. Multiplier on time axis of specified curve. Default=1.0.

        DSS property name: `TDPhFast`, DSS property index: 19.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    def _set_TDPhFast(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 19, value, flags)

    TDPhFast = property(_get_TDPhFast, _set_TDPhFast) # type: float

    def _get_TDGrFast(self) -> float:
        """
        Time dial for Ground Fast trip curve. Multiplier on time axis of specified curve. Default=1.0.

        DSS property name: `TDGrFast`, DSS property index: 20.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    def _set_TDGrFast(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 20, value, flags)

    TDGrFast = property(_get_TDGrFast, _set_TDGrFast) # type: float

    def _get_TDPhDelayed(self) -> float:
        """
        Time dial for Phase Delayed trip curve. Multiplier on time axis of specified curve. Default=1.0.

        DSS property name: `TDPhDelayed`, DSS property index: 21.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    def _set_TDPhDelayed(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 21, value, flags)

    TDPhDelayed = property(_get_TDPhDelayed, _set_TDPhDelayed) # type: float

    def _get_TDGrDelayed(self) -> float:
        """
        Time dial for Ground Delayed trip curve. Multiplier on time axis of specified curve. Default=1.0.

        DSS property name: `TDGrDelayed`, DSS property index: 22.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    def _set_TDGrDelayed(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 22, value, flags)

    TDGrDelayed = property(_get_TDGrDelayed, _set_TDGrDelayed) # type: float

    def _get_Normal(self) -> enums.RecloserState:
        """
        {Open | Closed} Normal state of the recloser. The recloser reverts to this state for reset, change of mode, etc. Defaults to "State" if not specifically declared.

        DSS property name: `Normal`, DSS property index: 23.
        """
        return enums.RecloserState(self._lib.Obj_GetInt32(self._ptr, 23))

    def _set_Normal(self, value: Union[AnyStr, int, enums.RecloserState], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(23, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 23, value, flags)

    Normal = property(_get_Normal, _set_Normal) # type: enums.RecloserState

    def _get_Normal_str(self) -> str:
        """
        {Open | Closed} Normal state of the recloser. The recloser reverts to this state for reset, change of mode, etc. Defaults to "State" if not specifically declared.

        DSS property name: `Normal`, DSS property index: 23.
        """
        return self._get_prop_string(23)

    def _set_Normal_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Normal(value, flags)

    Normal_str = property(_get_Normal_str, _set_Normal_str) # type: str

    def _get_State(self) -> enums.RecloserState:
        """
        {Open | Closed} Actual state of the recloser. Upon setting, immediately forces state of the recloser, overriding the Recloser control. Simulates manual control on recloser. Defaults to Closed. "Open" causes the controlled element to open and lock out. "Closed" causes the controlled element to close and the recloser to reset to its first operation.

        DSS property name: `State`, DSS property index: 24.
        """
        return enums.RecloserState(self._lib.Obj_GetInt32(self._ptr, 24))

    def _set_State(self, value: Union[AnyStr, int, enums.RecloserState], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(24, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 24, value, flags)

    State = property(_get_State, _set_State) # type: enums.RecloserState

    def _get_State_str(self) -> str:
        """
        {Open | Closed} Actual state of the recloser. Upon setting, immediately forces state of the recloser, overriding the Recloser control. Simulates manual control on recloser. Defaults to Closed. "Open" causes the controlled element to open and lock out. "Closed" causes the controlled element to close and the recloser to reset to its first operation.

        DSS property name: `State`, DSS property index: 24.
        """
        return self._get_prop_string(24)

    def _set_State_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_State(value, flags)

    State_str = property(_get_State_str, _set_State_str) # type: str

    def _get_BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 25.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 25)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 25, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float

    def _get_Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 26.
        """
        return self._lib.Obj_GetInt32(self._ptr, 26) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 26, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool

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

class RecloserBatch(DSSBatch, CircuitElementBatchMixin):
    _cls_name = 'Recloser'
    _obj_cls = Recloser
    _cls_idx = 32

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)

    def _get_MonitoredObj_str(self) -> List[str]:
        """
        Full object name of the circuit element, typically a line, transformer, load, or generator, to which the Recloser's PT and/or CT are connected. This is the "monitored" element. There is no default; must be specified.

        DSS property name: `MonitoredObj`, DSS property index: 1.
        """
        return self._get_batch_str_prop(1)

    def _set_MonitoredObj_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(1, value, flags)

    MonitoredObj_str = property(_get_MonitoredObj_str, _set_MonitoredObj_str) # type: List[str]

    def _get_MonitoredObj(self) -> List[DSSObj]:
        """
        Full object name of the circuit element, typically a line, transformer, load, or generator, to which the Recloser's PT and/or CT are connected. This is the "monitored" element. There is no default; must be specified.

        DSS property name: `MonitoredObj`, DSS property index: 1.
        """
        return self._get_batch_obj_prop(1)

    def _set_MonitoredObj(self, value: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(1, value, flags)

    MonitoredObj = property(_get_MonitoredObj, _set_MonitoredObj) # type: List[DSSObj]

    def _get_MonitoredTerm(self) -> BatchInt32ArrayProxy:
        """
        Number of the terminal of the circuit element to which the Recloser is connected. 1 or 2, typically.  Default is 1.

        DSS property name: `MonitoredTerm`, DSS property index: 2.
        """
        return BatchInt32ArrayProxy(self, 2)

    def _set_MonitoredTerm(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(2, value, flags)

    MonitoredTerm = property(_get_MonitoredTerm, _set_MonitoredTerm) # type: BatchInt32ArrayProxy

    def _get_SwitchedObj_str(self) -> List[str]:
        """
        Name of circuit element switch that the Recloser controls. Specify the full object name.Defaults to the same as the Monitored element. This is the "controlled" element.

        DSS property name: `SwitchedObj`, DSS property index: 3.
        """
        return self._get_batch_str_prop(3)

    def _set_SwitchedObj_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(3, value, flags)

    SwitchedObj_str = property(_get_SwitchedObj_str, _set_SwitchedObj_str) # type: List[str]

    def _get_SwitchedObj(self) -> List[DSSObj]:
        """
        Name of circuit element switch that the Recloser controls. Specify the full object name.Defaults to the same as the Monitored element. This is the "controlled" element.

        DSS property name: `SwitchedObj`, DSS property index: 3.
        """
        return self._get_batch_obj_prop(3)

    def _set_SwitchedObj(self, value: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(3, value, flags)

    SwitchedObj = property(_get_SwitchedObj, _set_SwitchedObj) # type: List[DSSObj]

    def _get_SwitchedTerm(self) -> BatchInt32ArrayProxy:
        """
        Number of the terminal of the controlled element in which the switch is controlled by the Recloser. 1 or 2, typically.  Default is 1.

        DSS property name: `SwitchedTerm`, DSS property index: 4.
        """
        return BatchInt32ArrayProxy(self, 4)

    def _set_SwitchedTerm(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(4, value, flags)

    SwitchedTerm = property(_get_SwitchedTerm, _set_SwitchedTerm) # type: BatchInt32ArrayProxy

    def _get_NumFast(self) -> BatchInt32ArrayProxy:
        """
        Number of Fast (fuse saving) operations.  Default is 1. (See "Shots")

        DSS property name: `NumFast`, DSS property index: 5.
        """
        return BatchInt32ArrayProxy(self, 5)

    def _set_NumFast(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(5, value, flags)

    NumFast = property(_get_NumFast, _set_NumFast) # type: BatchInt32ArrayProxy

    def _get_PhaseFast_str(self) -> List[str]:
        """
        Name of the TCC Curve object that determines the Phase Fast trip.  Must have been previously defined as a TCC_Curve object. Default is "A". Multiplying the current values in the curve by the "phasetrip" value gives the actual current.

        DSS property name: `PhaseFast`, DSS property index: 6.
        """
        return self._get_batch_str_prop(6)

    def _set_PhaseFast_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(6, value, flags)

    PhaseFast_str = property(_get_PhaseFast_str, _set_PhaseFast_str) # type: List[str]

    def _get_PhaseFast(self) -> List[TCC_Curve]:
        """
        Name of the TCC Curve object that determines the Phase Fast trip.  Must have been previously defined as a TCC_Curve object. Default is "A". Multiplying the current values in the curve by the "phasetrip" value gives the actual current.

        DSS property name: `PhaseFast`, DSS property index: 6.
        """
        return self._get_batch_obj_prop(6)

    def _set_PhaseFast(self, value: Union[AnyStr, TCC_Curve, List[AnyStr], List[TCC_Curve]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(6, value, flags)

    PhaseFast = property(_get_PhaseFast, _set_PhaseFast) # type: List[TCC_Curve]

    def _get_PhaseDelayed_str(self) -> List[str]:
        """
        Name of the TCC Curve object that determines the Phase Delayed trip.  Must have been previously defined as a TCC_Curve object. Default is "D".Multiplying the current values in the curve by the "phasetrip" value gives the actual current.

        DSS property name: `PhaseDelayed`, DSS property index: 7.
        """
        return self._get_batch_str_prop(7)

    def _set_PhaseDelayed_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(7, value, flags)

    PhaseDelayed_str = property(_get_PhaseDelayed_str, _set_PhaseDelayed_str) # type: List[str]

    def _get_PhaseDelayed(self) -> List[TCC_Curve]:
        """
        Name of the TCC Curve object that determines the Phase Delayed trip.  Must have been previously defined as a TCC_Curve object. Default is "D".Multiplying the current values in the curve by the "phasetrip" value gives the actual current.

        DSS property name: `PhaseDelayed`, DSS property index: 7.
        """
        return self._get_batch_obj_prop(7)

    def _set_PhaseDelayed(self, value: Union[AnyStr, TCC_Curve, List[AnyStr], List[TCC_Curve]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(7, value, flags)

    PhaseDelayed = property(_get_PhaseDelayed, _set_PhaseDelayed) # type: List[TCC_Curve]

    def _get_GroundFast_str(self) -> List[str]:
        """
        Name of the TCC Curve object that determines the Ground Fast trip.  Must have been previously defined as a TCC_Curve object. Default is none (ignored). Multiplying the current values in the curve by the "groundtrip" value gives the actual current.

        DSS property name: `GroundFast`, DSS property index: 8.
        """
        return self._get_batch_str_prop(8)

    def _set_GroundFast_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(8, value, flags)

    GroundFast_str = property(_get_GroundFast_str, _set_GroundFast_str) # type: List[str]

    def _get_GroundFast(self) -> List[TCC_Curve]:
        """
        Name of the TCC Curve object that determines the Ground Fast trip.  Must have been previously defined as a TCC_Curve object. Default is none (ignored). Multiplying the current values in the curve by the "groundtrip" value gives the actual current.

        DSS property name: `GroundFast`, DSS property index: 8.
        """
        return self._get_batch_obj_prop(8)

    def _set_GroundFast(self, value: Union[AnyStr, TCC_Curve, List[AnyStr], List[TCC_Curve]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(8, value, flags)

    GroundFast = property(_get_GroundFast, _set_GroundFast) # type: List[TCC_Curve]

    def _get_GroundDelayed_str(self) -> List[str]:
        """
        Name of the TCC Curve object that determines the Ground Delayed trip.  Must have been previously defined as a TCC_Curve object. Default is none (ignored).Multiplying the current values in the curve by the "groundtrip" value gives the actual current.

        DSS property name: `GroundDelayed`, DSS property index: 9.
        """
        return self._get_batch_str_prop(9)

    def _set_GroundDelayed_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(9, value, flags)

    GroundDelayed_str = property(_get_GroundDelayed_str, _set_GroundDelayed_str) # type: List[str]

    def _get_GroundDelayed(self) -> List[TCC_Curve]:
        """
        Name of the TCC Curve object that determines the Ground Delayed trip.  Must have been previously defined as a TCC_Curve object. Default is none (ignored).Multiplying the current values in the curve by the "groundtrip" value gives the actual current.

        DSS property name: `GroundDelayed`, DSS property index: 9.
        """
        return self._get_batch_obj_prop(9)

    def _set_GroundDelayed(self, value: Union[AnyStr, TCC_Curve, List[AnyStr], List[TCC_Curve]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(9, value, flags)

    GroundDelayed = property(_get_GroundDelayed, _set_GroundDelayed) # type: List[TCC_Curve]

    def _get_PhaseTrip(self) -> BatchFloat64ArrayProxy:
        """
        Multiplier or actual phase amps for the phase TCC curve.  Defaults to 1.0.

        DSS property name: `PhaseTrip`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    def _set_PhaseTrip(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(10, value, flags)

    PhaseTrip = property(_get_PhaseTrip, _set_PhaseTrip) # type: BatchFloat64ArrayProxy

    def _get_GroundTrip(self) -> BatchFloat64ArrayProxy:
        """
        Multiplier or actual ground amps (3I0) for the ground TCC curve.  Defaults to 1.0.

        DSS property name: `GroundTrip`, DSS property index: 11.
        """
        return BatchFloat64ArrayProxy(self, 11)

    def _set_GroundTrip(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(11, value, flags)

    GroundTrip = property(_get_GroundTrip, _set_GroundTrip) # type: BatchFloat64ArrayProxy

    def _get_PhaseInst(self) -> BatchFloat64ArrayProxy:
        """
        Actual amps for instantaneous phase trip which is assumed to happen in 0.01 sec + Delay Time. Default is 0.0, which signifies no inst trip. 

        DSS property name: `PhaseInst`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    def _set_PhaseInst(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(12, value, flags)

    PhaseInst = property(_get_PhaseInst, _set_PhaseInst) # type: BatchFloat64ArrayProxy

    def _get_GroundInst(self) -> BatchFloat64ArrayProxy:
        """
        Actual amps for instantaneous ground trip which is assumed to happen in 0.01 sec + Delay Time.Default is 0.0, which signifies no inst trip.

        DSS property name: `GroundInst`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    def _set_GroundInst(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(13, value, flags)

    GroundInst = property(_get_GroundInst, _set_GroundInst) # type: BatchFloat64ArrayProxy

    def _get_Reset(self) -> BatchFloat64ArrayProxy:
        """
        Reset time in sec for Recloser.  Default is 15. 

        DSS property name: `Reset`, DSS property index: 14.
        """
        return BatchFloat64ArrayProxy(self, 14)

    def _set_Reset(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(14, value, flags)

    Reset = property(_get_Reset, _set_Reset) # type: BatchFloat64ArrayProxy

    def _get_Shots(self) -> BatchInt32ArrayProxy:
        """
        Total Number of fast and delayed shots to lockout.  Default is 4. This is one more than the number of reclose intervals.

        DSS property name: `Shots`, DSS property index: 15.
        """
        return BatchInt32ArrayProxy(self, 15)

    def _set_Shots(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(15, value, flags)

    Shots = property(_get_Shots, _set_Shots) # type: BatchInt32ArrayProxy

    def _get_RecloseIntervals(self) -> List[Float64Array]:
        """
        Array of reclose intervals.  Default for Recloser is (0.5, 2.0, 2.0) seconds. A locked out Recloser must be closed manually (action=close).

        DSS property name: `RecloseIntervals`, DSS property index: 16.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 16)
            for x in self._unpack()
        ]

    def _set_RecloseIntervals(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(16, value, flags)

    RecloseIntervals = property(_get_RecloseIntervals, _set_RecloseIntervals) # type: List[Float64Array]

    def _get_Delay(self) -> BatchFloat64ArrayProxy:
        """
        Fixed delay time (sec) added to Recloser trip time. Default is 0.0. Used to represent breaker time or any other delay.

        DSS property name: `Delay`, DSS property index: 17.
        """
        return BatchFloat64ArrayProxy(self, 17)

    def _set_Delay(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(17, value, flags)

    Delay = property(_get_Delay, _set_Delay) # type: BatchFloat64ArrayProxy

    def _get_TDPhFast(self) -> BatchFloat64ArrayProxy:
        """
        Time dial for Phase Fast trip curve. Multiplier on time axis of specified curve. Default=1.0.

        DSS property name: `TDPhFast`, DSS property index: 19.
        """
        return BatchFloat64ArrayProxy(self, 19)

    def _set_TDPhFast(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(19, value, flags)

    TDPhFast = property(_get_TDPhFast, _set_TDPhFast) # type: BatchFloat64ArrayProxy

    def _get_TDGrFast(self) -> BatchFloat64ArrayProxy:
        """
        Time dial for Ground Fast trip curve. Multiplier on time axis of specified curve. Default=1.0.

        DSS property name: `TDGrFast`, DSS property index: 20.
        """
        return BatchFloat64ArrayProxy(self, 20)

    def _set_TDGrFast(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(20, value, flags)

    TDGrFast = property(_get_TDGrFast, _set_TDGrFast) # type: BatchFloat64ArrayProxy

    def _get_TDPhDelayed(self) -> BatchFloat64ArrayProxy:
        """
        Time dial for Phase Delayed trip curve. Multiplier on time axis of specified curve. Default=1.0.

        DSS property name: `TDPhDelayed`, DSS property index: 21.
        """
        return BatchFloat64ArrayProxy(self, 21)

    def _set_TDPhDelayed(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(21, value, flags)

    TDPhDelayed = property(_get_TDPhDelayed, _set_TDPhDelayed) # type: BatchFloat64ArrayProxy

    def _get_TDGrDelayed(self) -> BatchFloat64ArrayProxy:
        """
        Time dial for Ground Delayed trip curve. Multiplier on time axis of specified curve. Default=1.0.

        DSS property name: `TDGrDelayed`, DSS property index: 22.
        """
        return BatchFloat64ArrayProxy(self, 22)

    def _set_TDGrDelayed(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(22, value, flags)

    TDGrDelayed = property(_get_TDGrDelayed, _set_TDGrDelayed) # type: BatchFloat64ArrayProxy

    def _get_Normal(self) -> BatchInt32ArrayProxy:
        """
        {Open | Closed} Normal state of the recloser. The recloser reverts to this state for reset, change of mode, etc. Defaults to "State" if not specifically declared.

        DSS property name: `Normal`, DSS property index: 23.
        """
        return BatchInt32ArrayProxy(self, 23)

    def _set_Normal(self, value: Union[AnyStr, int, enums.RecloserState, List[AnyStr], List[int], List[enums.RecloserState], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(23, value, flags)
            return

        self._set_batch_int32_array(23, value, flags)

    Normal = property(_get_Normal, _set_Normal) # type: BatchInt32ArrayProxy

    def _get_Normal_str(self) -> List[str]:
        """
        {Open | Closed} Normal state of the recloser. The recloser reverts to this state for reset, change of mode, etc. Defaults to "State" if not specifically declared.

        DSS property name: `Normal`, DSS property index: 23.
        """
        return self._get_batch_str_prop(23)

    def _set_Normal_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Normal(value, flags)

    Normal_str = property(_get_Normal_str, _set_Normal_str) # type: List[str]

    def _get_State(self) -> BatchInt32ArrayProxy:
        """
        {Open | Closed} Actual state of the recloser. Upon setting, immediately forces state of the recloser, overriding the Recloser control. Simulates manual control on recloser. Defaults to Closed. "Open" causes the controlled element to open and lock out. "Closed" causes the controlled element to close and the recloser to reset to its first operation.

        DSS property name: `State`, DSS property index: 24.
        """
        return BatchInt32ArrayProxy(self, 24)

    def _set_State(self, value: Union[AnyStr, int, enums.RecloserState, List[AnyStr], List[int], List[enums.RecloserState], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(24, value, flags)
            return

        self._set_batch_int32_array(24, value, flags)

    State = property(_get_State, _set_State) # type: BatchInt32ArrayProxy

    def _get_State_str(self) -> List[str]:
        """
        {Open | Closed} Actual state of the recloser. Upon setting, immediately forces state of the recloser, overriding the Recloser control. Simulates manual control on recloser. Defaults to Closed. "Open" causes the controlled element to open and lock out. "Closed" causes the controlled element to close and the recloser to reset to its first operation.

        DSS property name: `State`, DSS property index: 24.
        """
        return self._get_batch_str_prop(24)

    def _set_State_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_State(value, flags)

    State_str = property(_get_State_str, _set_State_str) # type: List[str]

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 25.
        """
        return BatchFloat64ArrayProxy(self, 25)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(25, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy

    def _get_Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 26.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(26)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(26, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 27.
        """
        self._set_batch_string(27, value, flags)

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

class IRecloser(IDSSObj, RecloserBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, Recloser, RecloserBatch)
        RecloserBatch.__init__(self, self._api_util, sync_cls_idx=Recloser._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Recloser:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[RecloserProperties]) -> Recloser:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[RecloserBatchProperties]) -> RecloserBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
