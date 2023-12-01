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

class Relay(DSSObj, CircuitElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots
    _cls_name = 'Relay'
    _cls_idx = 31
    _cls_prop_idx = {
        'monitoredobj': 1,
        'monitoredterm': 2,
        'switchedobj': 3,
        'switchedterm': 4,
        'type': 5,
        'phasecurve': 6,
        'groundcurve': 7,
        'phasetrip': 8,
        'groundtrip': 9,
        'tdphase': 10,
        'tdground': 11,
        'phaseinst': 12,
        'groundinst': 13,
        'reset': 14,
        'shots': 15,
        'recloseintervals': 16,
        'delay': 17,
        'overvoltcurve': 18,
        'undervoltcurve': 19,
        'kvbase': 20,
        'pctpickup47': 21,
        '47%pickup': 21,
        'f47pctpickup': 21,
        'baseamps46': 22,
        '46baseamps': 22,
        'f46baseamps': 22,
        'pctpickup46': 23,
        '46%pickup': 23,
        'f46pctpickup': 23,
        'isqt46': 24,
        '46isqt': 24,
        'f46isqt': 24,
        'variable': 25,
        'overtrip': 26,
        'undertrip': 27,
        'breakertime': 28,
        'action': 29,
        'z1mag': 30,
        'z1ang': 31,
        'z0mag': 32,
        'z0ang': 33,
        'mphase': 34,
        'mground': 35,
        'eventlog': 36,
        'debugtrace': 37,
        'distreverse': 38,
        'normal': 39,
        'state': 40,
        'doc_tiltanglelow': 41,
        'doc_tiltanglehigh': 42,
        'doc_tripsettinglow': 43,
        'doc_tripsettinghigh': 44,
        'doc_tripsettingmag': 45,
        'doc_delayinner': 46,
        'doc_phasecurveinner': 47,
        'doc_phasetripinner': 48,
        'doc_tdphaseinner': 49,
        'doc_p1blocking': 50,
        'basefreq': 51,
        'enabled': 52,
        'like': 53,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)

    def _get_MonitoredObj_str(self) -> str:
        """
        Full object name of the circuit element, typically a line, transformer, load, or generator, to which the relay's PT and/or CT are connected. This is the "monitored" element. There is no default; must be specified.

        DSS property name: `MonitoredObj`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    def _set_MonitoredObj_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(1, value, flags)

    MonitoredObj_str = property(_get_MonitoredObj_str, _set_MonitoredObj_str) # type: str

    def _get_MonitoredObj(self) -> DSSObj:
        """
        Full object name of the circuit element, typically a line, transformer, load, or generator, to which the relay's PT and/or CT are connected. This is the "monitored" element. There is no default; must be specified.

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
        Number of the terminal of the circuit element to which the Relay is connected. 1 or 2, typically.  Default is 1.

        DSS property name: `MonitoredTerm`, DSS property index: 2.
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    def _set_MonitoredTerm(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 2, value, flags)

    MonitoredTerm = property(_get_MonitoredTerm, _set_MonitoredTerm) # type: int

    def _get_SwitchedObj_str(self) -> str:
        """
        Name of circuit element switch that the Relay controls. Specify the full object name.Defaults to the same as the Monitored element. This is the "controlled" element.

        DSS property name: `SwitchedObj`, DSS property index: 3.
        """
        return self._get_prop_string(3)

    def _set_SwitchedObj_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(3, value, flags)

    SwitchedObj_str = property(_get_SwitchedObj_str, _set_SwitchedObj_str) # type: str

    def _get_SwitchedObj(self) -> DSSObj:
        """
        Name of circuit element switch that the Relay controls. Specify the full object name.Defaults to the same as the Monitored element. This is the "controlled" element.

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
        Number of the terminal of the controlled element in which the switch is controlled by the Relay. 1 or 2, typically.  Default is 1.

        DSS property name: `SwitchedTerm`, DSS property index: 4.
        """
        return self._lib.Obj_GetInt32(self._ptr, 4)

    def _set_SwitchedTerm(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 4, value, flags)

    SwitchedTerm = property(_get_SwitchedTerm, _set_SwitchedTerm) # type: int

    def _get_Type(self) -> enums.RelayType:
        """
        One of a legal relay type:
          Current
          Voltage
          Reversepower
          46 (neg seq current)
          47 (neg seq voltage)
          Generic (generic over/under relay)
          Distance
          TD21
          DOC (directional overcurrent)

        Default is overcurrent relay (Current) Specify the curve and pickup settings appropriate for each type. Generic relays monitor PC Element Control variables and trip on out of over/under range in definite time.

        DSS property name: `Type`, DSS property index: 5.
        """
        return enums.RelayType(self._lib.Obj_GetInt32(self._ptr, 5))

    def _set_Type(self, value: Union[AnyStr, int, enums.RelayType], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(5, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 5, value, flags)

    Type = property(_get_Type, _set_Type) # type: enums.RelayType

    def _get_Type_str(self) -> str:
        """
        One of a legal relay type:
          Current
          Voltage
          Reversepower
          46 (neg seq current)
          47 (neg seq voltage)
          Generic (generic over/under relay)
          Distance
          TD21
          DOC (directional overcurrent)

        Default is overcurrent relay (Current) Specify the curve and pickup settings appropriate for each type. Generic relays monitor PC Element Control variables and trip on out of over/under range in definite time.

        DSS property name: `Type`, DSS property index: 5.
        """
        return self._get_prop_string(5)

    def _set_Type_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Type(value, flags)

    Type_str = property(_get_Type_str, _set_Type_str) # type: str

    def _get_PhaseCurve_str(self) -> str:
        """
        Name of the TCC Curve object that determines the phase trip.  Must have been previously defined as a TCC_Curve object. Default is none (ignored). For overcurrent relay, multiplying the current values in the curve by the "phasetrip" value gives the actual current.

        DSS property name: `PhaseCurve`, DSS property index: 6.
        """
        return self._get_prop_string(6)

    def _set_PhaseCurve_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(6, value, flags)

    PhaseCurve_str = property(_get_PhaseCurve_str, _set_PhaseCurve_str) # type: str

    def _get_PhaseCurve(self) -> TCC_Curve:
        """
        Name of the TCC Curve object that determines the phase trip.  Must have been previously defined as a TCC_Curve object. Default is none (ignored). For overcurrent relay, multiplying the current values in the curve by the "phasetrip" value gives the actual current.

        DSS property name: `PhaseCurve`, DSS property index: 6.
        """
        return self._get_obj(6, TCC_Curve)

    def _set_PhaseCurve(self, value: Union[AnyStr, TCC_Curve], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(6, value, flags)
            return

        self._set_string_o(6, value, flags)

    PhaseCurve = property(_get_PhaseCurve, _set_PhaseCurve) # type: TCC_Curve

    def _get_GroundCurve_str(self) -> str:
        """
        Name of the TCC Curve object that determines the ground trip.  Must have been previously defined as a TCC_Curve object. Default is none (ignored).For overcurrent relay, multiplying the current values in the curve by the "groundtrip" valuw gives the actual current.

        DSS property name: `GroundCurve`, DSS property index: 7.
        """
        return self._get_prop_string(7)

    def _set_GroundCurve_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(7, value, flags)

    GroundCurve_str = property(_get_GroundCurve_str, _set_GroundCurve_str) # type: str

    def _get_GroundCurve(self) -> TCC_Curve:
        """
        Name of the TCC Curve object that determines the ground trip.  Must have been previously defined as a TCC_Curve object. Default is none (ignored).For overcurrent relay, multiplying the current values in the curve by the "groundtrip" valuw gives the actual current.

        DSS property name: `GroundCurve`, DSS property index: 7.
        """
        return self._get_obj(7, TCC_Curve)

    def _set_GroundCurve(self, value: Union[AnyStr, TCC_Curve], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(7, value, flags)
            return

        self._set_string_o(7, value, flags)

    GroundCurve = property(_get_GroundCurve, _set_GroundCurve) # type: TCC_Curve

    def _get_PhaseTrip(self) -> float:
        """
        Multiplier or actual phase amps for the phase TCC curve.  Defaults to 1.0.

        DSS property name: `PhaseTrip`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    def _set_PhaseTrip(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 8, value, flags)

    PhaseTrip = property(_get_PhaseTrip, _set_PhaseTrip) # type: float

    def _get_GroundTrip(self) -> float:
        """
        Multiplier or actual ground amps (3I0) for the ground TCC curve.  Defaults to 1.0.

        DSS property name: `GroundTrip`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    def _set_GroundTrip(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 9, value, flags)

    GroundTrip = property(_get_GroundTrip, _set_GroundTrip) # type: float

    def _get_TDPhase(self) -> float:
        """
        Time dial for Phase trip curve. Multiplier on time axis of specified curve. Default=1.0.

        DSS property name: `TDPhase`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    def _set_TDPhase(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 10, value, flags)

    TDPhase = property(_get_TDPhase, _set_TDPhase) # type: float

    def _get_TDGround(self) -> float:
        """
        Time dial for Ground trip curve. Multiplier on time axis of specified curve. Default=1.0.

        DSS property name: `TDGround`, DSS property index: 11.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    def _set_TDGround(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 11, value, flags)

    TDGround = property(_get_TDGround, _set_TDGround) # type: float

    def _get_PhaseInst(self) -> float:
        """
        Actual  amps (Current relay) or kW (reverse power relay) for instantaneous phase trip which is assumed to happen in 0.01 sec + Delay Time. Default is 0.0, which signifies no inst trip. Use this value for specifying the Reverse Power threshold (kW) for reverse power relays.

        DSS property name: `PhaseInst`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    def _set_PhaseInst(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 12, value, flags)

    PhaseInst = property(_get_PhaseInst, _set_PhaseInst) # type: float

    def _get_GroundInst(self) -> float:
        """
        Actual  amps for instantaneous ground trip which is assumed to happen in 0.01 sec + Delay Time.Default is 0.0, which signifies no inst trip.

        DSS property name: `GroundInst`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    def _set_GroundInst(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 13, value, flags)

    GroundInst = property(_get_GroundInst, _set_GroundInst) # type: float

    def _get_Reset(self) -> float:
        """
        Reset time in sec for relay.  Default is 15. If this much time passes between the last pickup event, and the relay has not locked out, the operation counter resets.

        DSS property name: `Reset`, DSS property index: 14.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    def _set_Reset(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 14, value, flags)

    Reset = property(_get_Reset, _set_Reset) # type: float

    def _get_Shots(self) -> int:
        """
        Number of shots to lockout.  Default is 4. This is one more than the number of reclose intervals.

        DSS property name: `Shots`, DSS property index: 15.
        """
        return self._lib.Obj_GetInt32(self._ptr, 15)

    def _set_Shots(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 15, value, flags)

    Shots = property(_get_Shots, _set_Shots) # type: int

    def _get_RecloseIntervals(self) -> Float64Array:
        """
        Array of reclose intervals. If none, specify "NONE". Default for overcurrent relay is (0.5, 2.0, 2.0) seconds. Default for a voltage relay is (5.0). In a voltage relay, this is  seconds after restoration of voltage that the reclose occurs. Reverse power relay is one shot to lockout, so this is ignored.  A locked out relay must be closed manually (set action=close).

        DSS property name: `RecloseIntervals`, DSS property index: 16.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 16)

    def _set_RecloseIntervals(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(16, value, flags)

    RecloseIntervals = property(_get_RecloseIntervals, _set_RecloseIntervals) # type: Float64Array

    def _get_Delay(self) -> float:
        """
        Trip time delay (sec) for DEFINITE TIME relays. Default is 0.0 for current, voltage and DOC relays. If >0 then this value is used instead of curves. Used by Generic, RevPower, 46 and 47 relays. Defaults to 0.1 s for these relays.

        DSS property name: `Delay`, DSS property index: 17.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    def _set_Delay(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 17, value, flags)

    Delay = property(_get_Delay, _set_Delay) # type: float

    def _get_OvervoltCurve_str(self) -> str:
        """
        TCC Curve object to use for overvoltage relay.  Curve is assumed to be defined with per unit voltage values. Voltage base should be defined for the relay. Default is none (ignored).

        DSS property name: `OvervoltCurve`, DSS property index: 18.
        """
        return self._get_prop_string(18)

    def _set_OvervoltCurve_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(18, value, flags)

    OvervoltCurve_str = property(_get_OvervoltCurve_str, _set_OvervoltCurve_str) # type: str

    def _get_OvervoltCurve(self) -> TCC_Curve:
        """
        TCC Curve object to use for overvoltage relay.  Curve is assumed to be defined with per unit voltage values. Voltage base should be defined for the relay. Default is none (ignored).

        DSS property name: `OvervoltCurve`, DSS property index: 18.
        """
        return self._get_obj(18, TCC_Curve)

    def _set_OvervoltCurve(self, value: Union[AnyStr, TCC_Curve], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(18, value, flags)
            return

        self._set_string_o(18, value, flags)

    OvervoltCurve = property(_get_OvervoltCurve, _set_OvervoltCurve) # type: TCC_Curve

    def _get_UndervoltCurve_str(self) -> str:
        """
        TCC Curve object to use for undervoltage relay.  Curve is assumed to be defined with per unit voltage values. Voltage base should be defined for the relay. Default is none (ignored).

        DSS property name: `UndervoltCurve`, DSS property index: 19.
        """
        return self._get_prop_string(19)

    def _set_UndervoltCurve_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(19, value, flags)

    UndervoltCurve_str = property(_get_UndervoltCurve_str, _set_UndervoltCurve_str) # type: str

    def _get_UndervoltCurve(self) -> TCC_Curve:
        """
        TCC Curve object to use for undervoltage relay.  Curve is assumed to be defined with per unit voltage values. Voltage base should be defined for the relay. Default is none (ignored).

        DSS property name: `UndervoltCurve`, DSS property index: 19.
        """
        return self._get_obj(19, TCC_Curve)

    def _set_UndervoltCurve(self, value: Union[AnyStr, TCC_Curve], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(19, value, flags)
            return

        self._set_string_o(19, value, flags)

    UndervoltCurve = property(_get_UndervoltCurve, _set_UndervoltCurve) # type: TCC_Curve

    def _get_kVBase(self) -> float:
        """
        Voltage base (kV) for the relay. Specify line-line for 3 phase devices); line-neutral for 1-phase devices.  Relay assumes the number of phases of the monitored element.  Default is 0.0, which results in assuming the voltage values in the "TCC" curve are specified in actual line-to-neutral volts.

        DSS property name: `kVBase`, DSS property index: 20.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    def _set_kVBase(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 20, value, flags)

    kVBase = property(_get_kVBase, _set_kVBase) # type: float

    def _get_F47pctPickup(self) -> float:
        """
        Percent voltage pickup for 47 relay (Neg seq voltage). Default is 2. Specify also base voltage (kvbase) and delay time value.   

        DSS property name: `47%Pickup`, DSS property index: 21.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    def _set_F47pctPickup(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 21, value, flags)

    F47pctPickup = property(_get_F47pctPickup, _set_F47pctPickup) # type: float

    def _get_F46BaseAmps(self) -> float:
        """
        Base current, Amps, for 46 relay (neg seq current).  Used for establishing pickup and per unit I-squared-t.

        DSS property name: `46BaseAmps`, DSS property index: 22.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    def _set_F46BaseAmps(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 22, value, flags)

    F46BaseAmps = property(_get_F46BaseAmps, _set_F46BaseAmps) # type: float

    def _get_F46pctPickup(self) -> float:
        """
        Percent pickup current for 46 relay (neg seq current).  Default is 20.0.   When current exceeds this value * BaseAmps, I-squared-t calc starts.

        DSS property name: `46%Pickup`, DSS property index: 23.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    def _set_F46pctPickup(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 23, value, flags)

    F46pctPickup = property(_get_F46pctPickup, _set_F46pctPickup) # type: float

    def _get_F46isqt(self) -> float:
        """
        Negative Sequence I-squared-t trip value for 46 relay (neg seq current).  Default is 1 (trips in 1 sec for 1 per unit neg seq current).  Should be 1 to 99.

        DSS property name: `46isqt`, DSS property index: 24.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    def _set_F46isqt(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 24, value, flags)

    F46isqt = property(_get_F46isqt, _set_F46isqt) # type: float

    def _get_Variable(self) -> str:
        """
        Name of variable in PC Elements being monitored.  Only applies to Generic relay.

        DSS property name: `Variable`, DSS property index: 25.
        """
        return self._get_prop_string(25)

    def _set_Variable(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(25, value, flags)

    Variable = property(_get_Variable, _set_Variable) # type: str

    def _get_Overtrip(self) -> float:
        """
        Trip setting (high value) for Generic relay variable.  Relay trips in definite time if value of variable exceeds this value.

        DSS property name: `Overtrip`, DSS property index: 26.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 26)

    def _set_Overtrip(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 26, value, flags)

    Overtrip = property(_get_Overtrip, _set_Overtrip) # type: float

    def _get_Undertrip(self) -> float:
        """
        Trip setting (low value) for Generic relay variable.  Relay trips in definite time if value of variable is less than this value.

        DSS property name: `Undertrip`, DSS property index: 27.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 27)

    def _set_Undertrip(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 27, value, flags)

    Undertrip = property(_get_Undertrip, _set_Undertrip) # type: float

    def _get_BreakerTime(self) -> float:
        """
        Fixed delay time (sec) added to relay time. Default is 0.0. Designed to represent breaker time or some other delay after a trip decision is made.Use Delay property for setting a fixed trip time delay.Added to trip time of current and voltage relays. Could use in combination with inst trip value to obtain a definite time overcurrent relay.

        DSS property name: `BreakerTime`, DSS property index: 28.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 28)

    def _set_BreakerTime(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 28, value, flags)

    BreakerTime = property(_get_BreakerTime, _set_BreakerTime) # type: float

    def _get_Action(self) -> enums.RelayAction:
        """
        DEPRECATED. See "State" property

        DSS property name: `Action`, DSS property index: 29.
        """
        return enums.RelayAction(self._lib.Obj_GetInt32(self._ptr, 29))

    def _set_Action(self, value: Union[AnyStr, int, enums.RelayAction], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(29, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 29, value, flags)

    Action = property(_get_Action, _set_Action) # type: enums.RelayAction

    def _get_Action_str(self) -> str:
        """
        DEPRECATED. See "State" property

        DSS property name: `Action`, DSS property index: 29.
        """
        return self._get_prop_string(29)

    def _set_Action_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Action(value, flags)

    Action_str = property(_get_Action_str, _set_Action_str) # type: str

    def _get_Z1Mag(self) -> float:
        """
        Positive sequence reach impedance in primary ohms for Distance and TD21 functions. Default=0.7

        DSS property name: `Z1Mag`, DSS property index: 30.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 30)

    def _set_Z1Mag(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 30, value, flags)

    Z1Mag = property(_get_Z1Mag, _set_Z1Mag) # type: float

    def _get_Z1Ang(self) -> float:
        """
        Positive sequence reach impedance angle in degrees for Distance and TD21 functions. Default=64.0

        DSS property name: `Z1Ang`, DSS property index: 31.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 31)

    def _set_Z1Ang(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 31, value, flags)

    Z1Ang = property(_get_Z1Ang, _set_Z1Ang) # type: float

    def _get_Z0Mag(self) -> float:
        """
        Zero sequence reach impedance in primary ohms for Distance and TD21 functions. Default=2.1

        DSS property name: `Z0Mag`, DSS property index: 32.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 32)

    def _set_Z0Mag(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 32, value, flags)

    Z0Mag = property(_get_Z0Mag, _set_Z0Mag) # type: float

    def _get_Z0Ang(self) -> float:
        """
        Zero sequence reach impedance angle in degrees for Distance and TD21 functions. Default=68.0

        DSS property name: `Z0Ang`, DSS property index: 33.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 33)

    def _set_Z0Ang(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 33, value, flags)

    Z0Ang = property(_get_Z0Ang, _set_Z0Ang) # type: float

    def _get_MPhase(self) -> float:
        """
        Phase reach multiplier in per-unit for Distance and TD21 functions. Default=0.7

        DSS property name: `MPhase`, DSS property index: 34.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 34)

    def _set_MPhase(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 34, value, flags)

    MPhase = property(_get_MPhase, _set_MPhase) # type: float

    def _get_MGround(self) -> float:
        """
        Ground reach multiplier in per-unit for Distance and TD21 functions. Default=0.7

        DSS property name: `MGround`, DSS property index: 35.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 35)

    def _set_MGround(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 35, value, flags)

    MGround = property(_get_MGround, _set_MGround) # type: float

    def _get_EventLog(self) -> bool:
        """
        {Yes/True | No/False* } Default is No for Relay. Write trips, reclose and reset events to EventLog.

        DSS property name: `EventLog`, DSS property index: 36.
        """
        return self._lib.Obj_GetInt32(self._ptr, 36) != 0

    def _set_EventLog(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 36, value, flags)

    EventLog = property(_get_EventLog, _set_EventLog) # type: bool

    def _get_DebugTrace(self) -> bool:
        """
        {Yes/True* | No/False* } Default is No for Relay. Write extra details to Eventlog.

        DSS property name: `DebugTrace`, DSS property index: 37.
        """
        return self._lib.Obj_GetInt32(self._ptr, 37) != 0

    def _set_DebugTrace(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 37, value, flags)

    DebugTrace = property(_get_DebugTrace, _set_DebugTrace) # type: bool

    def _get_DistReverse(self) -> bool:
        """
        {Yes/True* | No/False} Default is No; reverse direction for distance and td21 types.

        DSS property name: `DistReverse`, DSS property index: 38.
        """
        return self._lib.Obj_GetInt32(self._ptr, 38) != 0

    def _set_DistReverse(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 38, value, flags)

    DistReverse = property(_get_DistReverse, _set_DistReverse) # type: bool

    def _get_Normal(self) -> enums.RelayState:
        """
        {Open | Closed} Normal state of the relay. The relay reverts to this state for reset, change of mode, etc. Defaults to "State" if not specifically declared.

        DSS property name: `Normal`, DSS property index: 39.
        """
        return enums.RelayState(self._lib.Obj_GetInt32(self._ptr, 39))

    def _set_Normal(self, value: Union[AnyStr, int, enums.RelayState], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(39, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 39, value, flags)

    Normal = property(_get_Normal, _set_Normal) # type: enums.RelayState

    def _get_Normal_str(self) -> str:
        """
        {Open | Closed} Normal state of the relay. The relay reverts to this state for reset, change of mode, etc. Defaults to "State" if not specifically declared.

        DSS property name: `Normal`, DSS property index: 39.
        """
        return self._get_prop_string(39)

    def _set_Normal_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Normal(value, flags)

    Normal_str = property(_get_Normal_str, _set_Normal_str) # type: str

    def _get_State(self) -> enums.RelayState:
        """
        {Open | Closed} Actual state of the relay. Upon setting, immediately forces state of the relay, overriding the Relay control. Simulates manual control on relay. Defaults to Closed. "Open" causes the controlled element to open and lock out. "Closed" causes the controlled element to close and the relay to reset to its first operation.

        DSS property name: `State`, DSS property index: 40.
        """
        return enums.RelayState(self._lib.Obj_GetInt32(self._ptr, 40))

    def _set_State(self, value: Union[AnyStr, int, enums.RelayState], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(40, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 40, value, flags)

    State = property(_get_State, _set_State) # type: enums.RelayState

    def _get_State_str(self) -> str:
        """
        {Open | Closed} Actual state of the relay. Upon setting, immediately forces state of the relay, overriding the Relay control. Simulates manual control on relay. Defaults to Closed. "Open" causes the controlled element to open and lock out. "Closed" causes the controlled element to close and the relay to reset to its first operation.

        DSS property name: `State`, DSS property index: 40.
        """
        return self._get_prop_string(40)

    def _set_State_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_State(value, flags)

    State_str = property(_get_State_str, _set_State_str) # type: str

    def _get_DOC_TiltAngleLow(self) -> float:
        """
        Tilt angle for low-current trip line. Default is 90.

        DSS property name: `DOC_TiltAngleLow`, DSS property index: 41.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 41)

    def _set_DOC_TiltAngleLow(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 41, value, flags)

    DOC_TiltAngleLow = property(_get_DOC_TiltAngleLow, _set_DOC_TiltAngleLow) # type: float

    def _get_DOC_TiltAngleHigh(self) -> float:
        """
        Tilt angle for high-current trip line. Default is 90.

        DSS property name: `DOC_TiltAngleHigh`, DSS property index: 42.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 42)

    def _set_DOC_TiltAngleHigh(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 42, value, flags)

    DOC_TiltAngleHigh = property(_get_DOC_TiltAngleHigh, _set_DOC_TiltAngleHigh) # type: float

    def _get_DOC_TripSettingLow(self) -> float:
        """
        Resistive trip setting for low-current line. Default is 0.

        DSS property name: `DOC_TripSettingLow`, DSS property index: 43.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 43)

    def _set_DOC_TripSettingLow(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 43, value, flags)

    DOC_TripSettingLow = property(_get_DOC_TripSettingLow, _set_DOC_TripSettingLow) # type: float

    def _get_DOC_TripSettingHigh(self) -> float:
        """
        Resistive trip setting for high-current line.  Default is -1 (deactivated). To activate, set a positive value. Must be greater than "DOC_TripSettingLow".

        DSS property name: `DOC_TripSettingHigh`, DSS property index: 44.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 44)

    def _set_DOC_TripSettingHigh(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 44, value, flags)

    DOC_TripSettingHigh = property(_get_DOC_TripSettingHigh, _set_DOC_TripSettingHigh) # type: float

    def _get_DOC_TripSettingMag(self) -> float:
        """
        Trip setting for current magnitude (defines a circle in the relay characteristics). Default is -1 (deactivated). To activate, set a positive value.

        DSS property name: `DOC_TripSettingMag`, DSS property index: 45.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 45)

    def _set_DOC_TripSettingMag(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 45, value, flags)

    DOC_TripSettingMag = property(_get_DOC_TripSettingMag, _set_DOC_TripSettingMag) # type: float

    def _get_DOC_DelayInner(self) -> float:
        """
        Trip time delay (sec) for operation in inner region for DOC relay, defined when "DOC_TripSettingMag" or "DOC_TripSettingHigh" are activate. Default is -1.0 (deactivated), meaning that the relay characteristic is insensitive in the inner region (no trip). Set to 0 for instantaneous trip and >0 for a definite time delay. If "DOC_PhaseCurveInner" is specified, time delay from curve is utilized instead.

        DSS property name: `DOC_DelayInner`, DSS property index: 46.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 46)

    def _set_DOC_DelayInner(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 46, value, flags)

    DOC_DelayInner = property(_get_DOC_DelayInner, _set_DOC_DelayInner) # type: float

    def _get_DOC_PhaseCurveInner_str(self) -> str:
        """
        Name of the TCC Curve object that determines the phase trip for operation in inner region for DOC relay. Must have been previously defined as a TCC_Curve object. Default is none (ignored). Multiplying the current values in the curve by the "DOC_PhaseTripInner" value gives the actual current.

        DSS property name: `DOC_PhaseCurveInner`, DSS property index: 47.
        """
        return self._get_prop_string(47)

    def _set_DOC_PhaseCurveInner_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(47, value, flags)

    DOC_PhaseCurveInner_str = property(_get_DOC_PhaseCurveInner_str, _set_DOC_PhaseCurveInner_str) # type: str

    def _get_DOC_PhaseCurveInner(self) -> TCC_Curve:
        """
        Name of the TCC Curve object that determines the phase trip for operation in inner region for DOC relay. Must have been previously defined as a TCC_Curve object. Default is none (ignored). Multiplying the current values in the curve by the "DOC_PhaseTripInner" value gives the actual current.

        DSS property name: `DOC_PhaseCurveInner`, DSS property index: 47.
        """
        return self._get_obj(47, TCC_Curve)

    def _set_DOC_PhaseCurveInner(self, value: Union[AnyStr, TCC_Curve], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(47, value, flags)
            return

        self._set_string_o(47, value, flags)

    DOC_PhaseCurveInner = property(_get_DOC_PhaseCurveInner, _set_DOC_PhaseCurveInner) # type: TCC_Curve

    def _get_DOC_PhaseTripInner(self) -> float:
        """
        Multiplier for the "DOC_PhaseCurveInner" TCC curve.  Defaults to 1.0.

        DSS property name: `DOC_PhaseTripInner`, DSS property index: 48.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 48)

    def _set_DOC_PhaseTripInner(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 48, value, flags)

    DOC_PhaseTripInner = property(_get_DOC_PhaseTripInner, _set_DOC_PhaseTripInner) # type: float

    def _get_DOC_TDPhaseInner(self) -> float:
        """
        Time dial for "DOC_PhaseCurveInner" TCC curve. Multiplier on time axis of specified curve. Default=1.0.

        DSS property name: `DOC_TDPhaseInner`, DSS property index: 49.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 49)

    def _set_DOC_TDPhaseInner(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 49, value, flags)

    DOC_TDPhaseInner = property(_get_DOC_TDPhaseInner, _set_DOC_TDPhaseInner) # type: float

    def _get_DOC_P1Blocking(self) -> bool:
        """
        {Yes/True* | No/False} Blocking element that impedes relay from tripping if balanced net three-phase active power is in the forward direction (i.e., flowing into the monitored terminal). For a delayed trip, if at any given time the reverse power flow condition stops, the tripping is reset. Default=True.

        DSS property name: `DOC_P1Blocking`, DSS property index: 50.
        """
        return self._lib.Obj_GetInt32(self._ptr, 50) != 0

    def _set_DOC_P1Blocking(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 50, value, flags)

    DOC_P1Blocking = property(_get_DOC_P1Blocking, _set_DOC_P1Blocking) # type: bool

    def _get_BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 51.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 51)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 51, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float

    def _get_Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 52.
        """
        return self._lib.Obj_GetInt32(self._ptr, 52) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 52, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 53.
        """
        self._set_string_o(53, value)


class RelayProperties(TypedDict):
    MonitoredObj: Union[AnyStr, DSSObj]
    MonitoredTerm: int
    SwitchedObj: Union[AnyStr, DSSObj]
    SwitchedTerm: int
    Type: Union[AnyStr, int, enums.RelayType]
    PhaseCurve: Union[AnyStr, TCC_Curve]
    GroundCurve: Union[AnyStr, TCC_Curve]
    PhaseTrip: float
    GroundTrip: float
    TDPhase: float
    TDGround: float
    PhaseInst: float
    GroundInst: float
    Reset: float
    Shots: int
    RecloseIntervals: Float64Array
    Delay: float
    OvervoltCurve: Union[AnyStr, TCC_Curve]
    UndervoltCurve: Union[AnyStr, TCC_Curve]
    kVBase: float
    F47pctPickup: float
    F46BaseAmps: float
    F46pctPickup: float
    F46isqt: float
    Variable: AnyStr
    Overtrip: float
    Undertrip: float
    BreakerTime: float
    Action: Union[AnyStr, int, enums.RelayAction]
    Z1Mag: float
    Z1Ang: float
    Z0Mag: float
    Z0Ang: float
    MPhase: float
    MGround: float
    EventLog: bool
    DebugTrace: bool
    DistReverse: bool
    Normal: Union[AnyStr, int, enums.RelayState]
    State: Union[AnyStr, int, enums.RelayState]
    DOC_TiltAngleLow: float
    DOC_TiltAngleHigh: float
    DOC_TripSettingLow: float
    DOC_TripSettingHigh: float
    DOC_TripSettingMag: float
    DOC_DelayInner: float
    DOC_PhaseCurveInner: Union[AnyStr, TCC_Curve]
    DOC_PhaseTripInner: float
    DOC_TDPhaseInner: float
    DOC_P1Blocking: bool
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class RelayBatch(DSSBatch, CircuitElementBatchMixin):
    _cls_name = 'Relay'
    _obj_cls = Relay
    _cls_idx = 31

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)

    def _get_MonitoredObj_str(self) -> List[str]:
        """
        Full object name of the circuit element, typically a line, transformer, load, or generator, to which the relay's PT and/or CT are connected. This is the "monitored" element. There is no default; must be specified.

        DSS property name: `MonitoredObj`, DSS property index: 1.
        """
        return self._get_batch_str_prop(1)

    def _set_MonitoredObj_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(1, value, flags)

    MonitoredObj_str = property(_get_MonitoredObj_str, _set_MonitoredObj_str) # type: List[str]

    def _get_MonitoredObj(self) -> List[DSSObj]:
        """
        Full object name of the circuit element, typically a line, transformer, load, or generator, to which the relay's PT and/or CT are connected. This is the "monitored" element. There is no default; must be specified.

        DSS property name: `MonitoredObj`, DSS property index: 1.
        """
        return self._get_batch_obj_prop(1)

    def _set_MonitoredObj(self, value: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(1, value, flags)

    MonitoredObj = property(_get_MonitoredObj, _set_MonitoredObj) # type: List[DSSObj]

    def _get_MonitoredTerm(self) -> BatchInt32ArrayProxy:
        """
        Number of the terminal of the circuit element to which the Relay is connected. 1 or 2, typically.  Default is 1.

        DSS property name: `MonitoredTerm`, DSS property index: 2.
        """
        return BatchInt32ArrayProxy(self, 2)

    def _set_MonitoredTerm(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(2, value, flags)

    MonitoredTerm = property(_get_MonitoredTerm, _set_MonitoredTerm) # type: BatchInt32ArrayProxy

    def _get_SwitchedObj_str(self) -> List[str]:
        """
        Name of circuit element switch that the Relay controls. Specify the full object name.Defaults to the same as the Monitored element. This is the "controlled" element.

        DSS property name: `SwitchedObj`, DSS property index: 3.
        """
        return self._get_batch_str_prop(3)

    def _set_SwitchedObj_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(3, value, flags)

    SwitchedObj_str = property(_get_SwitchedObj_str, _set_SwitchedObj_str) # type: List[str]

    def _get_SwitchedObj(self) -> List[DSSObj]:
        """
        Name of circuit element switch that the Relay controls. Specify the full object name.Defaults to the same as the Monitored element. This is the "controlled" element.

        DSS property name: `SwitchedObj`, DSS property index: 3.
        """
        return self._get_batch_obj_prop(3)

    def _set_SwitchedObj(self, value: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(3, value, flags)

    SwitchedObj = property(_get_SwitchedObj, _set_SwitchedObj) # type: List[DSSObj]

    def _get_SwitchedTerm(self) -> BatchInt32ArrayProxy:
        """
        Number of the terminal of the controlled element in which the switch is controlled by the Relay. 1 or 2, typically.  Default is 1.

        DSS property name: `SwitchedTerm`, DSS property index: 4.
        """
        return BatchInt32ArrayProxy(self, 4)

    def _set_SwitchedTerm(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(4, value, flags)

    SwitchedTerm = property(_get_SwitchedTerm, _set_SwitchedTerm) # type: BatchInt32ArrayProxy

    def _get_Type(self) -> BatchInt32ArrayProxy:
        """
        One of a legal relay type:
          Current
          Voltage
          Reversepower
          46 (neg seq current)
          47 (neg seq voltage)
          Generic (generic over/under relay)
          Distance
          TD21
          DOC (directional overcurrent)

        Default is overcurrent relay (Current) Specify the curve and pickup settings appropriate for each type. Generic relays monitor PC Element Control variables and trip on out of over/under range in definite time.

        DSS property name: `Type`, DSS property index: 5.
        """
        return BatchInt32ArrayProxy(self, 5)

    def _set_Type(self, value: Union[AnyStr, int, enums.RelayType, List[AnyStr], List[int], List[enums.RelayType], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(5, value, flags)
            return

        self._set_batch_int32_array(5, value, flags)

    Type = property(_get_Type, _set_Type) # type: BatchInt32ArrayProxy

    def _get_Type_str(self) -> List[str]:
        """
        One of a legal relay type:
          Current
          Voltage
          Reversepower
          46 (neg seq current)
          47 (neg seq voltage)
          Generic (generic over/under relay)
          Distance
          TD21
          DOC (directional overcurrent)

        Default is overcurrent relay (Current) Specify the curve and pickup settings appropriate for each type. Generic relays monitor PC Element Control variables and trip on out of over/under range in definite time.

        DSS property name: `Type`, DSS property index: 5.
        """
        return self._get_batch_str_prop(5)

    def _set_Type_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Type(value, flags)

    Type_str = property(_get_Type_str, _set_Type_str) # type: List[str]

    def _get_PhaseCurve_str(self) -> List[str]:
        """
        Name of the TCC Curve object that determines the phase trip.  Must have been previously defined as a TCC_Curve object. Default is none (ignored). For overcurrent relay, multiplying the current values in the curve by the "phasetrip" value gives the actual current.

        DSS property name: `PhaseCurve`, DSS property index: 6.
        """
        return self._get_batch_str_prop(6)

    def _set_PhaseCurve_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(6, value, flags)

    PhaseCurve_str = property(_get_PhaseCurve_str, _set_PhaseCurve_str) # type: List[str]

    def _get_PhaseCurve(self) -> List[TCC_Curve]:
        """
        Name of the TCC Curve object that determines the phase trip.  Must have been previously defined as a TCC_Curve object. Default is none (ignored). For overcurrent relay, multiplying the current values in the curve by the "phasetrip" value gives the actual current.

        DSS property name: `PhaseCurve`, DSS property index: 6.
        """
        return self._get_batch_obj_prop(6)

    def _set_PhaseCurve(self, value: Union[AnyStr, TCC_Curve, List[AnyStr], List[TCC_Curve]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(6, value, flags)

    PhaseCurve = property(_get_PhaseCurve, _set_PhaseCurve) # type: List[TCC_Curve]

    def _get_GroundCurve_str(self) -> List[str]:
        """
        Name of the TCC Curve object that determines the ground trip.  Must have been previously defined as a TCC_Curve object. Default is none (ignored).For overcurrent relay, multiplying the current values in the curve by the "groundtrip" valuw gives the actual current.

        DSS property name: `GroundCurve`, DSS property index: 7.
        """
        return self._get_batch_str_prop(7)

    def _set_GroundCurve_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(7, value, flags)

    GroundCurve_str = property(_get_GroundCurve_str, _set_GroundCurve_str) # type: List[str]

    def _get_GroundCurve(self) -> List[TCC_Curve]:
        """
        Name of the TCC Curve object that determines the ground trip.  Must have been previously defined as a TCC_Curve object. Default is none (ignored).For overcurrent relay, multiplying the current values in the curve by the "groundtrip" valuw gives the actual current.

        DSS property name: `GroundCurve`, DSS property index: 7.
        """
        return self._get_batch_obj_prop(7)

    def _set_GroundCurve(self, value: Union[AnyStr, TCC_Curve, List[AnyStr], List[TCC_Curve]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(7, value, flags)

    GroundCurve = property(_get_GroundCurve, _set_GroundCurve) # type: List[TCC_Curve]

    def _get_PhaseTrip(self) -> BatchFloat64ArrayProxy:
        """
        Multiplier or actual phase amps for the phase TCC curve.  Defaults to 1.0.

        DSS property name: `PhaseTrip`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    def _set_PhaseTrip(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(8, value, flags)

    PhaseTrip = property(_get_PhaseTrip, _set_PhaseTrip) # type: BatchFloat64ArrayProxy

    def _get_GroundTrip(self) -> BatchFloat64ArrayProxy:
        """
        Multiplier or actual ground amps (3I0) for the ground TCC curve.  Defaults to 1.0.

        DSS property name: `GroundTrip`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    def _set_GroundTrip(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(9, value, flags)

    GroundTrip = property(_get_GroundTrip, _set_GroundTrip) # type: BatchFloat64ArrayProxy

    def _get_TDPhase(self) -> BatchFloat64ArrayProxy:
        """
        Time dial for Phase trip curve. Multiplier on time axis of specified curve. Default=1.0.

        DSS property name: `TDPhase`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    def _set_TDPhase(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(10, value, flags)

    TDPhase = property(_get_TDPhase, _set_TDPhase) # type: BatchFloat64ArrayProxy

    def _get_TDGround(self) -> BatchFloat64ArrayProxy:
        """
        Time dial for Ground trip curve. Multiplier on time axis of specified curve. Default=1.0.

        DSS property name: `TDGround`, DSS property index: 11.
        """
        return BatchFloat64ArrayProxy(self, 11)

    def _set_TDGround(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(11, value, flags)

    TDGround = property(_get_TDGround, _set_TDGround) # type: BatchFloat64ArrayProxy

    def _get_PhaseInst(self) -> BatchFloat64ArrayProxy:
        """
        Actual  amps (Current relay) or kW (reverse power relay) for instantaneous phase trip which is assumed to happen in 0.01 sec + Delay Time. Default is 0.0, which signifies no inst trip. Use this value for specifying the Reverse Power threshold (kW) for reverse power relays.

        DSS property name: `PhaseInst`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    def _set_PhaseInst(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(12, value, flags)

    PhaseInst = property(_get_PhaseInst, _set_PhaseInst) # type: BatchFloat64ArrayProxy

    def _get_GroundInst(self) -> BatchFloat64ArrayProxy:
        """
        Actual  amps for instantaneous ground trip which is assumed to happen in 0.01 sec + Delay Time.Default is 0.0, which signifies no inst trip.

        DSS property name: `GroundInst`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    def _set_GroundInst(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(13, value, flags)

    GroundInst = property(_get_GroundInst, _set_GroundInst) # type: BatchFloat64ArrayProxy

    def _get_Reset(self) -> BatchFloat64ArrayProxy:
        """
        Reset time in sec for relay.  Default is 15. If this much time passes between the last pickup event, and the relay has not locked out, the operation counter resets.

        DSS property name: `Reset`, DSS property index: 14.
        """
        return BatchFloat64ArrayProxy(self, 14)

    def _set_Reset(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(14, value, flags)

    Reset = property(_get_Reset, _set_Reset) # type: BatchFloat64ArrayProxy

    def _get_Shots(self) -> BatchInt32ArrayProxy:
        """
        Number of shots to lockout.  Default is 4. This is one more than the number of reclose intervals.

        DSS property name: `Shots`, DSS property index: 15.
        """
        return BatchInt32ArrayProxy(self, 15)

    def _set_Shots(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(15, value, flags)

    Shots = property(_get_Shots, _set_Shots) # type: BatchInt32ArrayProxy

    def _get_RecloseIntervals(self) -> List[Float64Array]:
        """
        Array of reclose intervals. If none, specify "NONE". Default for overcurrent relay is (0.5, 2.0, 2.0) seconds. Default for a voltage relay is (5.0). In a voltage relay, this is  seconds after restoration of voltage that the reclose occurs. Reverse power relay is one shot to lockout, so this is ignored.  A locked out relay must be closed manually (set action=close).

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
        Trip time delay (sec) for DEFINITE TIME relays. Default is 0.0 for current, voltage and DOC relays. If >0 then this value is used instead of curves. Used by Generic, RevPower, 46 and 47 relays. Defaults to 0.1 s for these relays.

        DSS property name: `Delay`, DSS property index: 17.
        """
        return BatchFloat64ArrayProxy(self, 17)

    def _set_Delay(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(17, value, flags)

    Delay = property(_get_Delay, _set_Delay) # type: BatchFloat64ArrayProxy

    def _get_OvervoltCurve_str(self) -> List[str]:
        """
        TCC Curve object to use for overvoltage relay.  Curve is assumed to be defined with per unit voltage values. Voltage base should be defined for the relay. Default is none (ignored).

        DSS property name: `OvervoltCurve`, DSS property index: 18.
        """
        return self._get_batch_str_prop(18)

    def _set_OvervoltCurve_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(18, value, flags)

    OvervoltCurve_str = property(_get_OvervoltCurve_str, _set_OvervoltCurve_str) # type: List[str]

    def _get_OvervoltCurve(self) -> List[TCC_Curve]:
        """
        TCC Curve object to use for overvoltage relay.  Curve is assumed to be defined with per unit voltage values. Voltage base should be defined for the relay. Default is none (ignored).

        DSS property name: `OvervoltCurve`, DSS property index: 18.
        """
        return self._get_batch_obj_prop(18)

    def _set_OvervoltCurve(self, value: Union[AnyStr, TCC_Curve, List[AnyStr], List[TCC_Curve]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(18, value, flags)

    OvervoltCurve = property(_get_OvervoltCurve, _set_OvervoltCurve) # type: List[TCC_Curve]

    def _get_UndervoltCurve_str(self) -> List[str]:
        """
        TCC Curve object to use for undervoltage relay.  Curve is assumed to be defined with per unit voltage values. Voltage base should be defined for the relay. Default is none (ignored).

        DSS property name: `UndervoltCurve`, DSS property index: 19.
        """
        return self._get_batch_str_prop(19)

    def _set_UndervoltCurve_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(19, value, flags)

    UndervoltCurve_str = property(_get_UndervoltCurve_str, _set_UndervoltCurve_str) # type: List[str]

    def _get_UndervoltCurve(self) -> List[TCC_Curve]:
        """
        TCC Curve object to use for undervoltage relay.  Curve is assumed to be defined with per unit voltage values. Voltage base should be defined for the relay. Default is none (ignored).

        DSS property name: `UndervoltCurve`, DSS property index: 19.
        """
        return self._get_batch_obj_prop(19)

    def _set_UndervoltCurve(self, value: Union[AnyStr, TCC_Curve, List[AnyStr], List[TCC_Curve]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(19, value, flags)

    UndervoltCurve = property(_get_UndervoltCurve, _set_UndervoltCurve) # type: List[TCC_Curve]

    def _get_kVBase(self) -> BatchFloat64ArrayProxy:
        """
        Voltage base (kV) for the relay. Specify line-line for 3 phase devices); line-neutral for 1-phase devices.  Relay assumes the number of phases of the monitored element.  Default is 0.0, which results in assuming the voltage values in the "TCC" curve are specified in actual line-to-neutral volts.

        DSS property name: `kVBase`, DSS property index: 20.
        """
        return BatchFloat64ArrayProxy(self, 20)

    def _set_kVBase(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(20, value, flags)

    kVBase = property(_get_kVBase, _set_kVBase) # type: BatchFloat64ArrayProxy

    def _get_F47pctPickup(self) -> BatchFloat64ArrayProxy:
        """
        Percent voltage pickup for 47 relay (Neg seq voltage). Default is 2. Specify also base voltage (kvbase) and delay time value.   

        DSS property name: `47%Pickup`, DSS property index: 21.
        """
        return BatchFloat64ArrayProxy(self, 21)

    def _set_F47pctPickup(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(21, value, flags)

    F47pctPickup = property(_get_F47pctPickup, _set_F47pctPickup) # type: BatchFloat64ArrayProxy

    def _get_F46BaseAmps(self) -> BatchFloat64ArrayProxy:
        """
        Base current, Amps, for 46 relay (neg seq current).  Used for establishing pickup and per unit I-squared-t.

        DSS property name: `46BaseAmps`, DSS property index: 22.
        """
        return BatchFloat64ArrayProxy(self, 22)

    def _set_F46BaseAmps(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(22, value, flags)

    F46BaseAmps = property(_get_F46BaseAmps, _set_F46BaseAmps) # type: BatchFloat64ArrayProxy

    def _get_F46pctPickup(self) -> BatchFloat64ArrayProxy:
        """
        Percent pickup current for 46 relay (neg seq current).  Default is 20.0.   When current exceeds this value * BaseAmps, I-squared-t calc starts.

        DSS property name: `46%Pickup`, DSS property index: 23.
        """
        return BatchFloat64ArrayProxy(self, 23)

    def _set_F46pctPickup(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(23, value, flags)

    F46pctPickup = property(_get_F46pctPickup, _set_F46pctPickup) # type: BatchFloat64ArrayProxy

    def _get_F46isqt(self) -> BatchFloat64ArrayProxy:
        """
        Negative Sequence I-squared-t trip value for 46 relay (neg seq current).  Default is 1 (trips in 1 sec for 1 per unit neg seq current).  Should be 1 to 99.

        DSS property name: `46isqt`, DSS property index: 24.
        """
        return BatchFloat64ArrayProxy(self, 24)

    def _set_F46isqt(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(24, value, flags)

    F46isqt = property(_get_F46isqt, _set_F46isqt) # type: BatchFloat64ArrayProxy

    def _get_Variable(self) -> List[str]:
        """
        Name of variable in PC Elements being monitored.  Only applies to Generic relay.

        DSS property name: `Variable`, DSS property index: 25.
        """
        return self._get_batch_str_prop(25)

    def _set_Variable(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(25, value, flags)

    Variable = property(_get_Variable, _set_Variable) # type: List[str]

    def _get_Overtrip(self) -> BatchFloat64ArrayProxy:
        """
        Trip setting (high value) for Generic relay variable.  Relay trips in definite time if value of variable exceeds this value.

        DSS property name: `Overtrip`, DSS property index: 26.
        """
        return BatchFloat64ArrayProxy(self, 26)

    def _set_Overtrip(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(26, value, flags)

    Overtrip = property(_get_Overtrip, _set_Overtrip) # type: BatchFloat64ArrayProxy

    def _get_Undertrip(self) -> BatchFloat64ArrayProxy:
        """
        Trip setting (low value) for Generic relay variable.  Relay trips in definite time if value of variable is less than this value.

        DSS property name: `Undertrip`, DSS property index: 27.
        """
        return BatchFloat64ArrayProxy(self, 27)

    def _set_Undertrip(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(27, value, flags)

    Undertrip = property(_get_Undertrip, _set_Undertrip) # type: BatchFloat64ArrayProxy

    def _get_BreakerTime(self) -> BatchFloat64ArrayProxy:
        """
        Fixed delay time (sec) added to relay time. Default is 0.0. Designed to represent breaker time or some other delay after a trip decision is made.Use Delay property for setting a fixed trip time delay.Added to trip time of current and voltage relays. Could use in combination with inst trip value to obtain a definite time overcurrent relay.

        DSS property name: `BreakerTime`, DSS property index: 28.
        """
        return BatchFloat64ArrayProxy(self, 28)

    def _set_BreakerTime(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(28, value, flags)

    BreakerTime = property(_get_BreakerTime, _set_BreakerTime) # type: BatchFloat64ArrayProxy

    def _get_Action(self) -> BatchInt32ArrayProxy:
        """
        DEPRECATED. See "State" property

        DSS property name: `Action`, DSS property index: 29.
        """
        return BatchInt32ArrayProxy(self, 29)

    def _set_Action(self, value: Union[AnyStr, int, enums.RelayAction, List[AnyStr], List[int], List[enums.RelayAction], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(29, value, flags)
            return

        self._set_batch_int32_array(29, value, flags)

    Action = property(_get_Action, _set_Action) # type: BatchInt32ArrayProxy

    def _get_Action_str(self) -> List[str]:
        """
        DEPRECATED. See "State" property

        DSS property name: `Action`, DSS property index: 29.
        """
        return self._get_batch_str_prop(29)

    def _set_Action_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Action(value, flags)

    Action_str = property(_get_Action_str, _set_Action_str) # type: List[str]

    def _get_Z1Mag(self) -> BatchFloat64ArrayProxy:
        """
        Positive sequence reach impedance in primary ohms for Distance and TD21 functions. Default=0.7

        DSS property name: `Z1Mag`, DSS property index: 30.
        """
        return BatchFloat64ArrayProxy(self, 30)

    def _set_Z1Mag(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(30, value, flags)

    Z1Mag = property(_get_Z1Mag, _set_Z1Mag) # type: BatchFloat64ArrayProxy

    def _get_Z1Ang(self) -> BatchFloat64ArrayProxy:
        """
        Positive sequence reach impedance angle in degrees for Distance and TD21 functions. Default=64.0

        DSS property name: `Z1Ang`, DSS property index: 31.
        """
        return BatchFloat64ArrayProxy(self, 31)

    def _set_Z1Ang(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(31, value, flags)

    Z1Ang = property(_get_Z1Ang, _set_Z1Ang) # type: BatchFloat64ArrayProxy

    def _get_Z0Mag(self) -> BatchFloat64ArrayProxy:
        """
        Zero sequence reach impedance in primary ohms for Distance and TD21 functions. Default=2.1

        DSS property name: `Z0Mag`, DSS property index: 32.
        """
        return BatchFloat64ArrayProxy(self, 32)

    def _set_Z0Mag(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(32, value, flags)

    Z0Mag = property(_get_Z0Mag, _set_Z0Mag) # type: BatchFloat64ArrayProxy

    def _get_Z0Ang(self) -> BatchFloat64ArrayProxy:
        """
        Zero sequence reach impedance angle in degrees for Distance and TD21 functions. Default=68.0

        DSS property name: `Z0Ang`, DSS property index: 33.
        """
        return BatchFloat64ArrayProxy(self, 33)

    def _set_Z0Ang(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(33, value, flags)

    Z0Ang = property(_get_Z0Ang, _set_Z0Ang) # type: BatchFloat64ArrayProxy

    def _get_MPhase(self) -> BatchFloat64ArrayProxy:
        """
        Phase reach multiplier in per-unit for Distance and TD21 functions. Default=0.7

        DSS property name: `MPhase`, DSS property index: 34.
        """
        return BatchFloat64ArrayProxy(self, 34)

    def _set_MPhase(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(34, value, flags)

    MPhase = property(_get_MPhase, _set_MPhase) # type: BatchFloat64ArrayProxy

    def _get_MGround(self) -> BatchFloat64ArrayProxy:
        """
        Ground reach multiplier in per-unit for Distance and TD21 functions. Default=0.7

        DSS property name: `MGround`, DSS property index: 35.
        """
        return BatchFloat64ArrayProxy(self, 35)

    def _set_MGround(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(35, value, flags)

    MGround = property(_get_MGround, _set_MGround) # type: BatchFloat64ArrayProxy

    def _get_EventLog(self) -> List[bool]:
        """
        {Yes/True | No/False* } Default is No for Relay. Write trips, reclose and reset events to EventLog.

        DSS property name: `EventLog`, DSS property index: 36.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(36)
        ]

    def _set_EventLog(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(36, value, flags)

    EventLog = property(_get_EventLog, _set_EventLog) # type: List[bool]

    def _get_DebugTrace(self) -> List[bool]:
        """
        {Yes/True* | No/False* } Default is No for Relay. Write extra details to Eventlog.

        DSS property name: `DebugTrace`, DSS property index: 37.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(37)
        ]

    def _set_DebugTrace(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(37, value, flags)

    DebugTrace = property(_get_DebugTrace, _set_DebugTrace) # type: List[bool]

    def _get_DistReverse(self) -> List[bool]:
        """
        {Yes/True* | No/False} Default is No; reverse direction for distance and td21 types.

        DSS property name: `DistReverse`, DSS property index: 38.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(38)
        ]

    def _set_DistReverse(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(38, value, flags)

    DistReverse = property(_get_DistReverse, _set_DistReverse) # type: List[bool]

    def _get_Normal(self) -> BatchInt32ArrayProxy:
        """
        {Open | Closed} Normal state of the relay. The relay reverts to this state for reset, change of mode, etc. Defaults to "State" if not specifically declared.

        DSS property name: `Normal`, DSS property index: 39.
        """
        return BatchInt32ArrayProxy(self, 39)

    def _set_Normal(self, value: Union[AnyStr, int, enums.RelayState, List[AnyStr], List[int], List[enums.RelayState], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(39, value, flags)
            return

        self._set_batch_int32_array(39, value, flags)

    Normal = property(_get_Normal, _set_Normal) # type: BatchInt32ArrayProxy

    def _get_Normal_str(self) -> List[str]:
        """
        {Open | Closed} Normal state of the relay. The relay reverts to this state for reset, change of mode, etc. Defaults to "State" if not specifically declared.

        DSS property name: `Normal`, DSS property index: 39.
        """
        return self._get_batch_str_prop(39)

    def _set_Normal_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Normal(value, flags)

    Normal_str = property(_get_Normal_str, _set_Normal_str) # type: List[str]

    def _get_State(self) -> BatchInt32ArrayProxy:
        """
        {Open | Closed} Actual state of the relay. Upon setting, immediately forces state of the relay, overriding the Relay control. Simulates manual control on relay. Defaults to Closed. "Open" causes the controlled element to open and lock out. "Closed" causes the controlled element to close and the relay to reset to its first operation.

        DSS property name: `State`, DSS property index: 40.
        """
        return BatchInt32ArrayProxy(self, 40)

    def _set_State(self, value: Union[AnyStr, int, enums.RelayState, List[AnyStr], List[int], List[enums.RelayState], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(40, value, flags)
            return

        self._set_batch_int32_array(40, value, flags)

    State = property(_get_State, _set_State) # type: BatchInt32ArrayProxy

    def _get_State_str(self) -> List[str]:
        """
        {Open | Closed} Actual state of the relay. Upon setting, immediately forces state of the relay, overriding the Relay control. Simulates manual control on relay. Defaults to Closed. "Open" causes the controlled element to open and lock out. "Closed" causes the controlled element to close and the relay to reset to its first operation.

        DSS property name: `State`, DSS property index: 40.
        """
        return self._get_batch_str_prop(40)

    def _set_State_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_State(value, flags)

    State_str = property(_get_State_str, _set_State_str) # type: List[str]

    def _get_DOC_TiltAngleLow(self) -> BatchFloat64ArrayProxy:
        """
        Tilt angle for low-current trip line. Default is 90.

        DSS property name: `DOC_TiltAngleLow`, DSS property index: 41.
        """
        return BatchFloat64ArrayProxy(self, 41)

    def _set_DOC_TiltAngleLow(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(41, value, flags)

    DOC_TiltAngleLow = property(_get_DOC_TiltAngleLow, _set_DOC_TiltAngleLow) # type: BatchFloat64ArrayProxy

    def _get_DOC_TiltAngleHigh(self) -> BatchFloat64ArrayProxy:
        """
        Tilt angle for high-current trip line. Default is 90.

        DSS property name: `DOC_TiltAngleHigh`, DSS property index: 42.
        """
        return BatchFloat64ArrayProxy(self, 42)

    def _set_DOC_TiltAngleHigh(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(42, value, flags)

    DOC_TiltAngleHigh = property(_get_DOC_TiltAngleHigh, _set_DOC_TiltAngleHigh) # type: BatchFloat64ArrayProxy

    def _get_DOC_TripSettingLow(self) -> BatchFloat64ArrayProxy:
        """
        Resistive trip setting for low-current line. Default is 0.

        DSS property name: `DOC_TripSettingLow`, DSS property index: 43.
        """
        return BatchFloat64ArrayProxy(self, 43)

    def _set_DOC_TripSettingLow(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(43, value, flags)

    DOC_TripSettingLow = property(_get_DOC_TripSettingLow, _set_DOC_TripSettingLow) # type: BatchFloat64ArrayProxy

    def _get_DOC_TripSettingHigh(self) -> BatchFloat64ArrayProxy:
        """
        Resistive trip setting for high-current line.  Default is -1 (deactivated). To activate, set a positive value. Must be greater than "DOC_TripSettingLow".

        DSS property name: `DOC_TripSettingHigh`, DSS property index: 44.
        """
        return BatchFloat64ArrayProxy(self, 44)

    def _set_DOC_TripSettingHigh(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(44, value, flags)

    DOC_TripSettingHigh = property(_get_DOC_TripSettingHigh, _set_DOC_TripSettingHigh) # type: BatchFloat64ArrayProxy

    def _get_DOC_TripSettingMag(self) -> BatchFloat64ArrayProxy:
        """
        Trip setting for current magnitude (defines a circle in the relay characteristics). Default is -1 (deactivated). To activate, set a positive value.

        DSS property name: `DOC_TripSettingMag`, DSS property index: 45.
        """
        return BatchFloat64ArrayProxy(self, 45)

    def _set_DOC_TripSettingMag(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(45, value, flags)

    DOC_TripSettingMag = property(_get_DOC_TripSettingMag, _set_DOC_TripSettingMag) # type: BatchFloat64ArrayProxy

    def _get_DOC_DelayInner(self) -> BatchFloat64ArrayProxy:
        """
        Trip time delay (sec) for operation in inner region for DOC relay, defined when "DOC_TripSettingMag" or "DOC_TripSettingHigh" are activate. Default is -1.0 (deactivated), meaning that the relay characteristic is insensitive in the inner region (no trip). Set to 0 for instantaneous trip and >0 for a definite time delay. If "DOC_PhaseCurveInner" is specified, time delay from curve is utilized instead.

        DSS property name: `DOC_DelayInner`, DSS property index: 46.
        """
        return BatchFloat64ArrayProxy(self, 46)

    def _set_DOC_DelayInner(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(46, value, flags)

    DOC_DelayInner = property(_get_DOC_DelayInner, _set_DOC_DelayInner) # type: BatchFloat64ArrayProxy

    def _get_DOC_PhaseCurveInner_str(self) -> List[str]:
        """
        Name of the TCC Curve object that determines the phase trip for operation in inner region for DOC relay. Must have been previously defined as a TCC_Curve object. Default is none (ignored). Multiplying the current values in the curve by the "DOC_PhaseTripInner" value gives the actual current.

        DSS property name: `DOC_PhaseCurveInner`, DSS property index: 47.
        """
        return self._get_batch_str_prop(47)

    def _set_DOC_PhaseCurveInner_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(47, value, flags)

    DOC_PhaseCurveInner_str = property(_get_DOC_PhaseCurveInner_str, _set_DOC_PhaseCurveInner_str) # type: List[str]

    def _get_DOC_PhaseCurveInner(self) -> List[TCC_Curve]:
        """
        Name of the TCC Curve object that determines the phase trip for operation in inner region for DOC relay. Must have been previously defined as a TCC_Curve object. Default is none (ignored). Multiplying the current values in the curve by the "DOC_PhaseTripInner" value gives the actual current.

        DSS property name: `DOC_PhaseCurveInner`, DSS property index: 47.
        """
        return self._get_batch_obj_prop(47)

    def _set_DOC_PhaseCurveInner(self, value: Union[AnyStr, TCC_Curve, List[AnyStr], List[TCC_Curve]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(47, value, flags)

    DOC_PhaseCurveInner = property(_get_DOC_PhaseCurveInner, _set_DOC_PhaseCurveInner) # type: List[TCC_Curve]

    def _get_DOC_PhaseTripInner(self) -> BatchFloat64ArrayProxy:
        """
        Multiplier for the "DOC_PhaseCurveInner" TCC curve.  Defaults to 1.0.

        DSS property name: `DOC_PhaseTripInner`, DSS property index: 48.
        """
        return BatchFloat64ArrayProxy(self, 48)

    def _set_DOC_PhaseTripInner(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(48, value, flags)

    DOC_PhaseTripInner = property(_get_DOC_PhaseTripInner, _set_DOC_PhaseTripInner) # type: BatchFloat64ArrayProxy

    def _get_DOC_TDPhaseInner(self) -> BatchFloat64ArrayProxy:
        """
        Time dial for "DOC_PhaseCurveInner" TCC curve. Multiplier on time axis of specified curve. Default=1.0.

        DSS property name: `DOC_TDPhaseInner`, DSS property index: 49.
        """
        return BatchFloat64ArrayProxy(self, 49)

    def _set_DOC_TDPhaseInner(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(49, value, flags)

    DOC_TDPhaseInner = property(_get_DOC_TDPhaseInner, _set_DOC_TDPhaseInner) # type: BatchFloat64ArrayProxy

    def _get_DOC_P1Blocking(self) -> List[bool]:
        """
        {Yes/True* | No/False} Blocking element that impedes relay from tripping if balanced net three-phase active power is in the forward direction (i.e., flowing into the monitored terminal). For a delayed trip, if at any given time the reverse power flow condition stops, the tripping is reset. Default=True.

        DSS property name: `DOC_P1Blocking`, DSS property index: 50.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(50)
        ]

    def _set_DOC_P1Blocking(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(50, value, flags)

    DOC_P1Blocking = property(_get_DOC_P1Blocking, _set_DOC_P1Blocking) # type: List[bool]

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 51.
        """
        return BatchFloat64ArrayProxy(self, 51)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(51, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy

    def _get_Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 52.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(52)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(52, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 53.
        """
        self._set_batch_string(53, value, flags)

class RelayBatchProperties(TypedDict):
    MonitoredObj: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]]
    MonitoredTerm: Union[int, Int32Array]
    SwitchedObj: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]]
    SwitchedTerm: Union[int, Int32Array]
    Type: Union[AnyStr, int, enums.RelayType, List[AnyStr], List[int], List[enums.RelayType], Int32Array]
    PhaseCurve: Union[AnyStr, TCC_Curve, List[AnyStr], List[TCC_Curve]]
    GroundCurve: Union[AnyStr, TCC_Curve, List[AnyStr], List[TCC_Curve]]
    PhaseTrip: Union[float, Float64Array]
    GroundTrip: Union[float, Float64Array]
    TDPhase: Union[float, Float64Array]
    TDGround: Union[float, Float64Array]
    PhaseInst: Union[float, Float64Array]
    GroundInst: Union[float, Float64Array]
    Reset: Union[float, Float64Array]
    Shots: Union[int, Int32Array]
    RecloseIntervals: Float64Array
    Delay: Union[float, Float64Array]
    OvervoltCurve: Union[AnyStr, TCC_Curve, List[AnyStr], List[TCC_Curve]]
    UndervoltCurve: Union[AnyStr, TCC_Curve, List[AnyStr], List[TCC_Curve]]
    kVBase: Union[float, Float64Array]
    F47pctPickup: Union[float, Float64Array]
    F46BaseAmps: Union[float, Float64Array]
    F46pctPickup: Union[float, Float64Array]
    F46isqt: Union[float, Float64Array]
    Variable: Union[AnyStr, List[AnyStr]]
    Overtrip: Union[float, Float64Array]
    Undertrip: Union[float, Float64Array]
    BreakerTime: Union[float, Float64Array]
    Action: Union[AnyStr, int, enums.RelayAction, List[AnyStr], List[int], List[enums.RelayAction], Int32Array]
    Z1Mag: Union[float, Float64Array]
    Z1Ang: Union[float, Float64Array]
    Z0Mag: Union[float, Float64Array]
    Z0Ang: Union[float, Float64Array]
    MPhase: Union[float, Float64Array]
    MGround: Union[float, Float64Array]
    EventLog: bool
    DebugTrace: bool
    DistReverse: bool
    Normal: Union[AnyStr, int, enums.RelayState, List[AnyStr], List[int], List[enums.RelayState], Int32Array]
    State: Union[AnyStr, int, enums.RelayState, List[AnyStr], List[int], List[enums.RelayState], Int32Array]
    DOC_TiltAngleLow: Union[float, Float64Array]
    DOC_TiltAngleHigh: Union[float, Float64Array]
    DOC_TripSettingLow: Union[float, Float64Array]
    DOC_TripSettingHigh: Union[float, Float64Array]
    DOC_TripSettingMag: Union[float, Float64Array]
    DOC_DelayInner: Union[float, Float64Array]
    DOC_PhaseCurveInner: Union[AnyStr, TCC_Curve, List[AnyStr], List[TCC_Curve]]
    DOC_PhaseTripInner: Union[float, Float64Array]
    DOC_TDPhaseInner: Union[float, Float64Array]
    DOC_P1Blocking: bool
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IRelay(IDSSObj, RelayBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, Relay, RelayBatch)
        RelayBatch.__init__(self, self._api_util, sync_cls_idx=Relay._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Relay:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[RelayProperties]) -> Relay:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[RelayBatchProperties]) -> RelayBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
