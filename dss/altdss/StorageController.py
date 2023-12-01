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
from .LoadShape import LoadShape

class StorageController(DSSObj, CircuitElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots
    _cls_name = 'StorageController'
    _cls_idx = 30
    _cls_prop_idx = {
        'element': 1,
        'terminal': 2,
        'monphase': 3,
        'kwtarget': 4,
        'kwtargetlow': 5,
        'pctkwband': 6,
        '%kwband': 6,
        'kwband': 7,
        'pctkwbandlow': 8,
        '%kwbandlow': 8,
        'kwbandlow': 9,
        'elementlist': 10,
        'weights': 11,
        'modedischarge': 12,
        'modecharge': 13,
        'timedischargetrigger': 14,
        'timechargetrigger': 15,
        'pctratekw': 16,
        '%ratekw': 16,
        'pctratecharge': 17,
        '%ratecharge': 17,
        'pctreserve': 18,
        '%reserve': 18,
        'kwhtotal': 19,
        'kwtotal': 20,
        'kwhactual': 21,
        'kwactual': 22,
        'kwneed': 23,
        'yearly': 24,
        'daily': 25,
        'duty': 26,
        'eventlog': 27,
        'inhibittime': 28,
        'tup': 29,
        'tflat': 30,
        'tdn': 31,
        'kwthreshold': 32,
        'dispfactor': 33,
        'resetlevel': 34,
        'seasons': 35,
        'seasontargets': 36,
        'seasontargetslow': 37,
        'basefreq': 38,
        'enabled': 39,
        'like': 40,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)

    def _get_Element_str(self) -> str:
        """
        Full object name of the circuit element, typically a line or transformer, which the control is monitoring. There is no default; Must be specified.In "Local" control mode, is the name of the load that will be managed by the storage device, which should be installed at the same bus.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    def _set_Element_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(1, value, flags)

    Element_str = property(_get_Element_str, _set_Element_str) # type: str

    def _get_Element(self) -> DSSObj:
        """
        Full object name of the circuit element, typically a line or transformer, which the control is monitoring. There is no default; Must be specified.In "Local" control mode, is the name of the load that will be managed by the storage device, which should be installed at the same bus.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_obj(1, None)

    def _set_Element(self, value: Union[AnyStr, DSSObj], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(1, value, flags)
            return

        self._set_string_o(1, value, flags)

    Element = property(_get_Element, _set_Element) # type: DSSObj

    def _get_Terminal(self) -> int:
        """
        Number of the terminal of the circuit element to which the StorageController control is connected. 1 or 2, typically.  Default is 1. Make sure to select the proper direction on the power for the respective dispatch mode.

        DSS property name: `Terminal`, DSS property index: 2.
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    def _set_Terminal(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 2, value, flags)

    Terminal = property(_get_Terminal, _set_Terminal) # type: int

    def _get_MonPhase(self) -> Union[enums.MonitoredPhase, int]:
        """
        Number of the phase being monitored or one of {AVG | MAX | MIN} for all phases. Default=MAX. Must be less than the number of phases. Used in PeakShave, Follow, Support and I-PeakShave discharging modes and in PeakShaveLow, I-PeakShaveLow charging modes. For modes based on active power measurements, the value used by the control is the monitored one multiplied by the number of phases of the monitored element.

        DSS property name: `MonPhase`, DSS property index: 3.
        """
        value = self._lib.Obj_GetInt32(self._ptr, 3)
        if value > 0:
            return value

        return enums.MonitoredPhase(value)

    def _set_MonPhase(self, value: Union[AnyStr, int, enums.MonitoredPhase], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(3, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 3, value, flags)

    MonPhase = property(_get_MonPhase, _set_MonPhase) # type: enums.MonitoredPhase

    def _get_MonPhase_str(self) -> str:
        """
        Number of the phase being monitored or one of {AVG | MAX | MIN} for all phases. Default=MAX. Must be less than the number of phases. Used in PeakShave, Follow, Support and I-PeakShave discharging modes and in PeakShaveLow, I-PeakShaveLow charging modes. For modes based on active power measurements, the value used by the control is the monitored one multiplied by the number of phases of the monitored element.

        DSS property name: `MonPhase`, DSS property index: 3.
        """
        return self._get_prop_string(3)

    def _set_MonPhase_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_MonPhase(value, flags)

    MonPhase_str = property(_get_MonPhase_str, _set_MonPhase_str) # type: str

    def _get_kWTarget(self) -> float:
        """
        kW/kamps target for Discharging. The Storage element fleet is dispatched to try to hold the power/current in band at least until the Storage is depleted. The selection of power or current depends on the Discharge mode (PeakShave->kW, I-PeakShave->kamps).

        DSS property name: `kWTarget`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    def _set_kWTarget(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 4, value, flags)

    kWTarget = property(_get_kWTarget, _set_kWTarget) # type: float

    def _get_kWTargetLow(self) -> float:
        """
        kW/kamps target for Charging. The Storage element fleet is dispatched to try to hold the power/current in band at least until the Storage is fully charged. The selection of power or current depends on the charge mode (PeakShavelow->kW, I-PeakShavelow->kamps).

        DSS property name: `kWTargetLow`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    def _set_kWTargetLow(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 5, value, flags)

    kWTargetLow = property(_get_kWTargetLow, _set_kWTargetLow) # type: float

    def _get_pctkWBand(self) -> float:
        """
        Bandwidth (% of Target kW/kamps) of the dead band around the kW/kamps target value. Default is 2% (+/-1%).No dispatch changes are attempted if the power in the monitored terminal stays within this band.

        DSS property name: `%kWBand`, DSS property index: 6.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    def _set_pctkWBand(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 6, value, flags)

    pctkWBand = property(_get_pctkWBand, _set_pctkWBand) # type: float

    def _get_kWBand(self) -> float:
        """
        Alternative way of specifying the bandwidth. (kW/kamps) of the dead band around the kW/kamps target value. Default is 2% of kWTarget (+/-1%).No dispatch changes are attempted if the power in the monitored terminal stays within this band.

        DSS property name: `kWBand`, DSS property index: 7.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    def _set_kWBand(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 7, value, flags)

    kWBand = property(_get_kWBand, _set_kWBand) # type: float

    def _get_pctkWBandLow(self) -> float:
        """
        Bandwidth (% of kWTargetLow) of the dead band around the kW/kamps low target value. Default is 2% (+/-1%).No charging is attempted if the power in the monitored terminal stays within this band.

        DSS property name: `%kWBandLow`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    def _set_pctkWBandLow(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 8, value, flags)

    pctkWBandLow = property(_get_pctkWBandLow, _set_pctkWBandLow) # type: float

    def _get_kWBandLow(self) -> float:
        """
        Alternative way of specifying the bandwidth. (kW/kamps) of the dead band around the kW/kamps low target value. Default is 2% of kWTargetLow (+/-1%).No charging is attempted if the power in the monitored terminal stays within this band.

        DSS property name: `kWBandLow`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    def _set_kWBandLow(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 9, value, flags)

    kWBandLow = property(_get_kWBandLow, _set_kWBandLow) # type: float

    def _get_ElementList(self) -> List[str]:
        """
        Array list of Storage elements to be controlled.  If not specified, all Storage elements in the circuit not presently dispatched by another controller are assumed dispatched by this controller.

        DSS property name: `ElementList`, DSS property index: 10.
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 10)

    def _set_ElementList(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 10, value_ptr, value_count, flags)
        self._check_for_error()

    ElementList = property(_get_ElementList, _set_ElementList) # type: List[str]

    def _get_Weights(self) -> Float64Array:
        """
        Array of proportional weights corresponding to each Storage element in the ElementList. The needed kW or kvar to get back to center band is dispatched to each Storage element according to these weights. Default is to set all weights to 1.0.

        DSS property name: `Weights`, DSS property index: 11.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 11)

    def _set_Weights(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(11, value, flags)

    Weights = property(_get_Weights, _set_Weights) # type: Float64Array

    def _get_ModeDischarge(self) -> enums.StorageControllerDischargeMode:
        """
        {PeakShave* | Follow | Support | Loadshape | Time | Schedule | I-PeakShave} Mode of operation for the DISCHARGE FUNCTION of this controller. 

        In PeakShave mode (Default), the control attempts to discharge Storage to keep power in the monitored element below the kWTarget. 

        In Follow mode, the control is triggered by time and resets the kWTarget value to the present monitored element power. It then attempts to discharge Storage to keep power in the monitored element below the new kWTarget. See TimeDischargeTrigger.

        In Support mode, the control operates oppositely of PeakShave mode: Storage is discharged to keep kW power output up near the target. 

        In Loadshape mode, both charging and discharging precisely follows the per unit loadshape. Storage is discharged when the loadshape value is positive. 

        In Time mode, the Storage discharge is turned on at the specified %RatekW at the specified discharge trigger time in fractional hours.

        In Schedule mode, the Tup, TFlat, and Tdn properties specify the up ramp duration, flat duration, and down ramp duration for the schedule. The schedule start time is set by TimeDischargeTrigger and the rate of discharge for the flat part is determined by %RatekW.

        In I-PeakShave mode, the control attempts to discharge Storage to keep current in the monitored element below the target given in k-amps (thousands of amps), when this control mode is active, the property kWTarget will be expressed in k-amps. 

        DSS property name: `ModeDischarge`, DSS property index: 12.
        """
        return enums.StorageControllerDischargeMode(self._lib.Obj_GetInt32(self._ptr, 12))

    def _set_ModeDischarge(self, value: Union[AnyStr, int, enums.StorageControllerDischargeMode], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(12, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 12, value, flags)

    ModeDischarge = property(_get_ModeDischarge, _set_ModeDischarge) # type: enums.StorageControllerDischargeMode

    def _get_ModeDischarge_str(self) -> str:
        """
        {PeakShave* | Follow | Support | Loadshape | Time | Schedule | I-PeakShave} Mode of operation for the DISCHARGE FUNCTION of this controller. 

        In PeakShave mode (Default), the control attempts to discharge Storage to keep power in the monitored element below the kWTarget. 

        In Follow mode, the control is triggered by time and resets the kWTarget value to the present monitored element power. It then attempts to discharge Storage to keep power in the monitored element below the new kWTarget. See TimeDischargeTrigger.

        In Support mode, the control operates oppositely of PeakShave mode: Storage is discharged to keep kW power output up near the target. 

        In Loadshape mode, both charging and discharging precisely follows the per unit loadshape. Storage is discharged when the loadshape value is positive. 

        In Time mode, the Storage discharge is turned on at the specified %RatekW at the specified discharge trigger time in fractional hours.

        In Schedule mode, the Tup, TFlat, and Tdn properties specify the up ramp duration, flat duration, and down ramp duration for the schedule. The schedule start time is set by TimeDischargeTrigger and the rate of discharge for the flat part is determined by %RatekW.

        In I-PeakShave mode, the control attempts to discharge Storage to keep current in the monitored element below the target given in k-amps (thousands of amps), when this control mode is active, the property kWTarget will be expressed in k-amps. 

        DSS property name: `ModeDischarge`, DSS property index: 12.
        """
        return self._get_prop_string(12)

    def _set_ModeDischarge_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_ModeDischarge(value, flags)

    ModeDischarge_str = property(_get_ModeDischarge_str, _set_ModeDischarge_str) # type: str

    def _get_ModeCharge(self) -> enums.StorageControllerChargeMode:
        """
        {Loadshape | Time* | PeakShaveLow | I-PeakShaveLow} Mode of operation for the CHARGE FUNCTION of this controller. 

        In Loadshape mode, both charging and discharging precisely follows the per unit loadshape. Storage is charged when the loadshape value is negative. 

        In Time mode, the Storage charging FUNCTION is triggered at the specified %RateCharge at the specified charge trigger time in fractional hours.

        In PeakShaveLow mode, the charging operation will charge the Storage fleet when the power at a monitored element is below a specified KW target (kWTarget_low). The Storage will charge as much power as necessary to keep the power within the deadband around kWTarget_low.

        In I-PeakShaveLow mode, the charging operation will charge the Storage fleet when the current (Amps) at a monitored element is below a specified amps target (kWTarget_low). The Storage will charge as much power as necessary to keep the amps within the deadband around kWTarget_low. When this control mode is active, the property kWTarget_low will be expressed in k-amps and all the other parameters will be adjusted to match the amps (current) control criteria.

        DSS property name: `ModeCharge`, DSS property index: 13.
        """
        return enums.StorageControllerChargeMode(self._lib.Obj_GetInt32(self._ptr, 13))

    def _set_ModeCharge(self, value: Union[AnyStr, int, enums.StorageControllerChargeMode], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(13, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 13, value, flags)

    ModeCharge = property(_get_ModeCharge, _set_ModeCharge) # type: enums.StorageControllerChargeMode

    def _get_ModeCharge_str(self) -> str:
        """
        {Loadshape | Time* | PeakShaveLow | I-PeakShaveLow} Mode of operation for the CHARGE FUNCTION of this controller. 

        In Loadshape mode, both charging and discharging precisely follows the per unit loadshape. Storage is charged when the loadshape value is negative. 

        In Time mode, the Storage charging FUNCTION is triggered at the specified %RateCharge at the specified charge trigger time in fractional hours.

        In PeakShaveLow mode, the charging operation will charge the Storage fleet when the power at a monitored element is below a specified KW target (kWTarget_low). The Storage will charge as much power as necessary to keep the power within the deadband around kWTarget_low.

        In I-PeakShaveLow mode, the charging operation will charge the Storage fleet when the current (Amps) at a monitored element is below a specified amps target (kWTarget_low). The Storage will charge as much power as necessary to keep the amps within the deadband around kWTarget_low. When this control mode is active, the property kWTarget_low will be expressed in k-amps and all the other parameters will be adjusted to match the amps (current) control criteria.

        DSS property name: `ModeCharge`, DSS property index: 13.
        """
        return self._get_prop_string(13)

    def _set_ModeCharge_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_ModeCharge(value, flags)

    ModeCharge_str = property(_get_ModeCharge_str, _set_ModeCharge_str) # type: str

    def _get_TimeDischargeTrigger(self) -> float:
        """
        Default time of day (hr) for initiating Discharging of the fleet. During Follow or Time mode discharging is triggered at a fixed time each day at this hour. If Follow mode, Storage will be discharged to attempt to hold the load at or below the power level at the time of triggering. In Time mode, the discharge is based on the %RatekW property value. Set this to a negative value to ignore. Default is 12.0 for Follow mode; otherwise it is -1 (ignored). 

        DSS property name: `TimeDischargeTrigger`, DSS property index: 14.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    def _set_TimeDischargeTrigger(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 14, value, flags)

    TimeDischargeTrigger = property(_get_TimeDischargeTrigger, _set_TimeDischargeTrigger) # type: float

    def _get_TimeChargeTrigger(self) -> float:
        """
        Default time of day (hr) for initiating charging in Time control mode. Set this to a negative value to ignore. Default is 2.0.  (0200).When this value is >0 the Storage fleet is set to charging at this time regardless of other control criteria to make sure Storage is topped off for the next discharge cycle.

        DSS property name: `TimeChargeTrigger`, DSS property index: 15.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    def _set_TimeChargeTrigger(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 15, value, flags)

    TimeChargeTrigger = property(_get_TimeChargeTrigger, _set_TimeChargeTrigger) # type: float

    def _get_pctRatekW(self) -> float:
        """
        Sets the kW discharge rate in % of rated capacity for each element of the fleet. Applies to TIME control mode, SCHEDULE mode, or anytime discharging is triggered by time.

        DSS property name: `%RatekW`, DSS property index: 16.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    def _set_pctRatekW(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 16, value, flags)

    pctRatekW = property(_get_pctRatekW, _set_pctRatekW) # type: float

    def _get_pctRateCharge(self) -> float:
        """
        Sets the kW charging rate in % of rated capacity for each element of the fleet. Applies to TIME control mode and anytime charging mode is entered due to a time trigger.

        DSS property name: `%RateCharge`, DSS property index: 17.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    def _set_pctRateCharge(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 17, value, flags)

    pctRateCharge = property(_get_pctRateCharge, _set_pctRateCharge) # type: float

    def _get_pctReserve(self) -> float:
        """
        Use this property to change the % reserve for each Storage element under control of this controller. This might be used, for example, to allow deeper discharges of Storage or in case of emergency operation to use the remainder of the Storage element.

        DSS property name: `%Reserve`, DSS property index: 18.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    def _set_pctReserve(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 18, value, flags)

    pctReserve = property(_get_pctReserve, _set_pctReserve) # type: float

    def _get_kWhTotal(self) -> float:
        """
        (Read only). Total rated kWh energy Storage capacity of Storage elements controlled by this controller.

        DSS property name: `kWhTotal`, DSS property index: 19.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    def _set_kWhTotal(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 19, value, flags)

    kWhTotal = property(_get_kWhTotal, _set_kWhTotal) # type: float

    def _get_kWTotal(self) -> float:
        """
        (Read only). Total rated kW power capacity of Storage elements controlled by this controller.

        DSS property name: `kWTotal`, DSS property index: 20.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    def _set_kWTotal(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 20, value, flags)

    kWTotal = property(_get_kWTotal, _set_kWTotal) # type: float

    def _get_kWhActual(self) -> float:
        """
        (Read only). Actual kWh stored of all controlled Storage elements. 

        DSS property name: `kWhActual`, DSS property index: 21.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    def _set_kWhActual(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 21, value, flags)

    kWhActual = property(_get_kWhActual, _set_kWhActual) # type: float

    def _get_kWActual(self) -> float:
        """
        (Read only). Actual kW output of all controlled Storage elements. 

        DSS property name: `kWActual`, DSS property index: 22.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    def _set_kWActual(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 22, value, flags)

    kWActual = property(_get_kWActual, _set_kWActual) # type: float

    def _get_kWNeed(self) -> float:
        """
        (Read only). KW needed to meet target.

        DSS property name: `kWNeed`, DSS property index: 23.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    def _set_kWNeed(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 23, value, flags)

    kWNeed = property(_get_kWNeed, _set_kWNeed) # type: float

    def _get_Yearly_str(self) -> str:
        """
        Dispatch loadshape object, If any, for Yearly solution Mode.

        DSS property name: `Yearly`, DSS property index: 24.
        """
        return self._get_prop_string(24)

    def _set_Yearly_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(24, value, flags)

    Yearly_str = property(_get_Yearly_str, _set_Yearly_str) # type: str

    def _get_Yearly(self) -> LoadShape:
        """
        Dispatch loadshape object, If any, for Yearly solution Mode.

        DSS property name: `Yearly`, DSS property index: 24.
        """
        return self._get_obj(24, LoadShape)

    def _set_Yearly(self, value: Union[AnyStr, LoadShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(24, value, flags)
            return

        self._set_string_o(24, value, flags)

    Yearly = property(_get_Yearly, _set_Yearly) # type: LoadShape

    def _get_Daily_str(self) -> str:
        """
        Dispatch loadshape object, If any, for Daily solution mode.

        DSS property name: `Daily`, DSS property index: 25.
        """
        return self._get_prop_string(25)

    def _set_Daily_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(25, value, flags)

    Daily_str = property(_get_Daily_str, _set_Daily_str) # type: str

    def _get_Daily(self) -> LoadShape:
        """
        Dispatch loadshape object, If any, for Daily solution mode.

        DSS property name: `Daily`, DSS property index: 25.
        """
        return self._get_obj(25, LoadShape)

    def _set_Daily(self, value: Union[AnyStr, LoadShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(25, value, flags)
            return

        self._set_string_o(25, value, flags)

    Daily = property(_get_Daily, _set_Daily) # type: LoadShape

    def _get_Duty_str(self) -> str:
        """
        Dispatch loadshape object, If any, for Dutycycle solution mode.

        DSS property name: `Duty`, DSS property index: 26.
        """
        return self._get_prop_string(26)

    def _set_Duty_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(26, value, flags)

    Duty_str = property(_get_Duty_str, _set_Duty_str) # type: str

    def _get_Duty(self) -> LoadShape:
        """
        Dispatch loadshape object, If any, for Dutycycle solution mode.

        DSS property name: `Duty`, DSS property index: 26.
        """
        return self._get_obj(26, LoadShape)

    def _set_Duty(self, value: Union[AnyStr, LoadShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(26, value, flags)
            return

        self._set_string_o(26, value, flags)

    Duty = property(_get_Duty, _set_Duty) # type: LoadShape

    def _get_EventLog(self) -> bool:
        """
        {Yes/True | No/False} Default is No. Log control actions to Eventlog.

        DSS property name: `EventLog`, DSS property index: 27.
        """
        return self._lib.Obj_GetInt32(self._ptr, 27) != 0

    def _set_EventLog(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 27, value, flags)

    EventLog = property(_get_EventLog, _set_EventLog) # type: bool

    def _get_InhibitTime(self) -> int:
        """
        Hours (integer) to inhibit Discharging after going into Charge mode. Default is 5.

        DSS property name: `InhibitTime`, DSS property index: 28.
        """
        return self._lib.Obj_GetInt32(self._ptr, 28)

    def _set_InhibitTime(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 28, value, flags)

    InhibitTime = property(_get_InhibitTime, _set_InhibitTime) # type: int

    def _get_TUp(self) -> float:
        """
        Duration, hrs, of upramp part for SCHEDULE mode. Default is 0.25.

        DSS property name: `TUp`, DSS property index: 29.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 29)

    def _set_TUp(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 29, value, flags)

    TUp = property(_get_TUp, _set_TUp) # type: float

    def _get_TFlat(self) -> float:
        """
        Duration, hrs, of flat part for SCHEDULE mode. Default is 2.0.

        DSS property name: `TFlat`, DSS property index: 30.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 30)

    def _set_TFlat(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 30, value, flags)

    TFlat = property(_get_TFlat, _set_TFlat) # type: float

    def _get_TDn(self) -> float:
        """
        Duration, hrs, of downramp part for SCHEDULE mode. Default is 0.25.

        DSS property name: `TDn`, DSS property index: 31.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 31)

    def _set_TDn(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 31, value, flags)

    TDn = property(_get_TDn, _set_TDn) # type: float

    def _get_kWThreshold(self) -> float:
        """
        Threshold, kW, for Follow mode. kW has to be above this value for the Storage element to be dispatched on. Defaults to 75% of the kWTarget value. Must reset this property after setting kWTarget if you want a different value.

        DSS property name: `kWThreshold`, DSS property index: 32.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 32)

    def _set_kWThreshold(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 32, value, flags)

    kWThreshold = property(_get_kWThreshold, _set_kWThreshold) # type: float

    def _get_DispFactor(self) -> float:
        """
        Defaults to 1 (disabled). Set to any value between 0 and 1 to enable this parameter.

        Use this parameter to reduce the amount of power requested by the controller in each control iteration. It can be useful when maximum control iterations are exceeded due to numerical instability such as fleet being set to charging and idling in subsequent control iterations (check the Eventlog). 

        DSS property name: `DispFactor`, DSS property index: 33.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 33)

    def _set_DispFactor(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 33, value, flags)

    DispFactor = property(_get_DispFactor, _set_DispFactor) # type: float

    def _get_ResetLevel(self) -> float:
        """
        The level of charge required for allowing the storage to discharge again after reaching the reserve storage level. After reaching this level, the storage control  will not allow the storage device to discharge, forcing the storage to charge. Once the storage reaches this level, the storage will be able to discharge again. This value is a number between 0.2 and 1

        DSS property name: `ResetLevel`, DSS property index: 34.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 34)

    def _set_ResetLevel(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 34, value, flags)

    ResetLevel = property(_get_ResetLevel, _set_ResetLevel) # type: float

    def _get_Seasons(self) -> int:
        """
        With this property the user can specify the number of targets to be used by the controller using the list given at "SeasonTargets"/"SeasonTargetsLow", which can be used to dynamically adjust the storage controller during a QSTS simulation. The default value is 1. This property needs to be defined before defining SeasonTargets/SeasonTargetsLow.

        DSS property name: `Seasons`, DSS property index: 35.
        """
        return self._lib.Obj_GetInt32(self._ptr, 35)

    def _set_Seasons(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 35, value, flags)

    Seasons = property(_get_Seasons, _set_Seasons) # type: int

    def _get_SeasonTargets(self) -> Float64Array:
        """
        An array of doubles specifying the targets to be used during a QSTS simulation. These targets will take effect only if SeasonRating=true. The number of targets cannot exceed the number of seasons defined at the SeasonSignal.The difference between the targets defined at SeasonTargets and SeasonTargetsLow is that SeasonTargets applies to discharging modes, while SeasonTargetsLow applies to charging modes.

        DSS property name: `SeasonTargets`, DSS property index: 36.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 36)

    def _set_SeasonTargets(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(36, value, flags)

    SeasonTargets = property(_get_SeasonTargets, _set_SeasonTargets) # type: Float64Array

    def _get_SeasonTargetsLow(self) -> Float64Array:
        """
        An array of doubles specifying the targets to be used during a QSTS simulation. These targets will take effect only if SeasonRating=true. The number of targets cannot exceed the number of seasons defined at the SeasonSignal.The difference between the targets defined at SeasonTargets and SeasonTargetsLow is that SeasonTargets applies to discharging modes, while SeasonTargetsLow applies to charging modes.

        DSS property name: `SeasonTargetsLow`, DSS property index: 37.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 37)

    def _set_SeasonTargetsLow(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(37, value, flags)

    SeasonTargetsLow = property(_get_SeasonTargetsLow, _set_SeasonTargetsLow) # type: Float64Array

    def _get_BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 38.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 38)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 38, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float

    def _get_Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 39.
        """
        return self._lib.Obj_GetInt32(self._ptr, 39) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 39, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 40.
        """
        self._set_string_o(40, value)


class StorageControllerProperties(TypedDict):
    Element: Union[AnyStr, DSSObj]
    Terminal: int
    MonPhase: Union[AnyStr, int, enums.MonitoredPhase]
    kWTarget: float
    kWTargetLow: float
    pctkWBand: float
    kWBand: float
    pctkWBandLow: float
    kWBandLow: float
    ElementList: List[AnyStr]
    Weights: Float64Array
    ModeDischarge: Union[AnyStr, int, enums.StorageControllerDischargeMode]
    ModeCharge: Union[AnyStr, int, enums.StorageControllerChargeMode]
    TimeDischargeTrigger: float
    TimeChargeTrigger: float
    pctRatekW: float
    pctRateCharge: float
    pctReserve: float
    kWhTotal: float
    kWTotal: float
    kWhActual: float
    kWActual: float
    kWNeed: float
    Yearly: Union[AnyStr, LoadShape]
    Daily: Union[AnyStr, LoadShape]
    Duty: Union[AnyStr, LoadShape]
    EventLog: bool
    InhibitTime: int
    TUp: float
    TFlat: float
    TDn: float
    kWThreshold: float
    DispFactor: float
    ResetLevel: float
    Seasons: int
    SeasonTargets: Float64Array
    SeasonTargetsLow: Float64Array
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class StorageControllerBatch(DSSBatch, CircuitElementBatchMixin):
    _cls_name = 'StorageController'
    _obj_cls = StorageController
    _cls_idx = 30

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)

    def _get_Element_str(self) -> List[str]:
        """
        Full object name of the circuit element, typically a line or transformer, which the control is monitoring. There is no default; Must be specified.In "Local" control mode, is the name of the load that will be managed by the storage device, which should be installed at the same bus.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_batch_str_prop(1)

    def _set_Element_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(1, value, flags)

    Element_str = property(_get_Element_str, _set_Element_str) # type: List[str]

    def _get_Element(self) -> List[DSSObj]:
        """
        Full object name of the circuit element, typically a line or transformer, which the control is monitoring. There is no default; Must be specified.In "Local" control mode, is the name of the load that will be managed by the storage device, which should be installed at the same bus.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_batch_obj_prop(1)

    def _set_Element(self, value: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(1, value, flags)

    Element = property(_get_Element, _set_Element) # type: List[DSSObj]

    def _get_Terminal(self) -> BatchInt32ArrayProxy:
        """
        Number of the terminal of the circuit element to which the StorageController control is connected. 1 or 2, typically.  Default is 1. Make sure to select the proper direction on the power for the respective dispatch mode.

        DSS property name: `Terminal`, DSS property index: 2.
        """
        return BatchInt32ArrayProxy(self, 2)

    def _set_Terminal(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(2, value, flags)

    Terminal = property(_get_Terminal, _set_Terminal) # type: BatchInt32ArrayProxy

    def _get_MonPhase(self) -> BatchInt32ArrayProxy:
        """
        Number of the phase being monitored or one of {AVG | MAX | MIN} for all phases. Default=MAX. Must be less than the number of phases. Used in PeakShave, Follow, Support and I-PeakShave discharging modes and in PeakShaveLow, I-PeakShaveLow charging modes. For modes based on active power measurements, the value used by the control is the monitored one multiplied by the number of phases of the monitored element.

        DSS property name: `MonPhase`, DSS property index: 3.
        """
        return BatchInt32ArrayProxy(self, 3)

    def _set_MonPhase(self, value: Union[AnyStr, int, enums.MonitoredPhase, List[AnyStr], List[int], List[enums.MonitoredPhase], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(3, value, flags)
            return

        self._set_batch_int32_array(3, value, flags)

    MonPhase = property(_get_MonPhase, _set_MonPhase) # type: BatchInt32ArrayProxy

    def _get_MonPhase_str(self) -> List[str]:
        """
        Number of the phase being monitored or one of {AVG | MAX | MIN} for all phases. Default=MAX. Must be less than the number of phases. Used in PeakShave, Follow, Support and I-PeakShave discharging modes and in PeakShaveLow, I-PeakShaveLow charging modes. For modes based on active power measurements, the value used by the control is the monitored one multiplied by the number of phases of the monitored element.

        DSS property name: `MonPhase`, DSS property index: 3.
        """
        return self._get_batch_str_prop(3)

    def _set_MonPhase_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_MonPhase(value, flags)

    MonPhase_str = property(_get_MonPhase_str, _set_MonPhase_str) # type: List[str]

    def _get_kWTarget(self) -> BatchFloat64ArrayProxy:
        """
        kW/kamps target for Discharging. The Storage element fleet is dispatched to try to hold the power/current in band at least until the Storage is depleted. The selection of power or current depends on the Discharge mode (PeakShave->kW, I-PeakShave->kamps).

        DSS property name: `kWTarget`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    def _set_kWTarget(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(4, value, flags)

    kWTarget = property(_get_kWTarget, _set_kWTarget) # type: BatchFloat64ArrayProxy

    def _get_kWTargetLow(self) -> BatchFloat64ArrayProxy:
        """
        kW/kamps target for Charging. The Storage element fleet is dispatched to try to hold the power/current in band at least until the Storage is fully charged. The selection of power or current depends on the charge mode (PeakShavelow->kW, I-PeakShavelow->kamps).

        DSS property name: `kWTargetLow`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    def _set_kWTargetLow(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(5, value, flags)

    kWTargetLow = property(_get_kWTargetLow, _set_kWTargetLow) # type: BatchFloat64ArrayProxy

    def _get_pctkWBand(self) -> BatchFloat64ArrayProxy:
        """
        Bandwidth (% of Target kW/kamps) of the dead band around the kW/kamps target value. Default is 2% (+/-1%).No dispatch changes are attempted if the power in the monitored terminal stays within this band.

        DSS property name: `%kWBand`, DSS property index: 6.
        """
        return BatchFloat64ArrayProxy(self, 6)

    def _set_pctkWBand(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(6, value, flags)

    pctkWBand = property(_get_pctkWBand, _set_pctkWBand) # type: BatchFloat64ArrayProxy

    def _get_kWBand(self) -> BatchFloat64ArrayProxy:
        """
        Alternative way of specifying the bandwidth. (kW/kamps) of the dead band around the kW/kamps target value. Default is 2% of kWTarget (+/-1%).No dispatch changes are attempted if the power in the monitored terminal stays within this band.

        DSS property name: `kWBand`, DSS property index: 7.
        """
        return BatchFloat64ArrayProxy(self, 7)

    def _set_kWBand(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(7, value, flags)

    kWBand = property(_get_kWBand, _set_kWBand) # type: BatchFloat64ArrayProxy

    def _get_pctkWBandLow(self) -> BatchFloat64ArrayProxy:
        """
        Bandwidth (% of kWTargetLow) of the dead band around the kW/kamps low target value. Default is 2% (+/-1%).No charging is attempted if the power in the monitored terminal stays within this band.

        DSS property name: `%kWBandLow`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    def _set_pctkWBandLow(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(8, value, flags)

    pctkWBandLow = property(_get_pctkWBandLow, _set_pctkWBandLow) # type: BatchFloat64ArrayProxy

    def _get_kWBandLow(self) -> BatchFloat64ArrayProxy:
        """
        Alternative way of specifying the bandwidth. (kW/kamps) of the dead band around the kW/kamps low target value. Default is 2% of kWTargetLow (+/-1%).No charging is attempted if the power in the monitored terminal stays within this band.

        DSS property name: `kWBandLow`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    def _set_kWBandLow(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(9, value, flags)

    kWBandLow = property(_get_kWBandLow, _set_kWBandLow) # type: BatchFloat64ArrayProxy

    def _get_ElementList(self) -> List[List[str]]:
        """
        Array list of Storage elements to be controlled.  If not specified, all Storage elements in the circuit not presently dispatched by another controller are assumed dispatched by this controller.

        DSS property name: `ElementList`, DSS property index: 10.
        """
        return self._get_string_ll(10)

    def _set_ElementList(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._unpack():
            self._lib.Obj_SetStringArray(x, 10, value_ptr, value_count, flags)

        self._check_for_error()

    ElementList = property(_get_ElementList, _set_ElementList) # type: List[List[str]]

    def _get_Weights(self) -> List[Float64Array]:
        """
        Array of proportional weights corresponding to each Storage element in the ElementList. The needed kW or kvar to get back to center band is dispatched to each Storage element according to these weights. Default is to set all weights to 1.0.

        DSS property name: `Weights`, DSS property index: 11.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 11)
            for x in self._unpack()
        ]

    def _set_Weights(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(11, value, flags)

    Weights = property(_get_Weights, _set_Weights) # type: List[Float64Array]

    def _get_ModeDischarge(self) -> BatchInt32ArrayProxy:
        """
        {PeakShave* | Follow | Support | Loadshape | Time | Schedule | I-PeakShave} Mode of operation for the DISCHARGE FUNCTION of this controller. 

        In PeakShave mode (Default), the control attempts to discharge Storage to keep power in the monitored element below the kWTarget. 

        In Follow mode, the control is triggered by time and resets the kWTarget value to the present monitored element power. It then attempts to discharge Storage to keep power in the monitored element below the new kWTarget. See TimeDischargeTrigger.

        In Support mode, the control operates oppositely of PeakShave mode: Storage is discharged to keep kW power output up near the target. 

        In Loadshape mode, both charging and discharging precisely follows the per unit loadshape. Storage is discharged when the loadshape value is positive. 

        In Time mode, the Storage discharge is turned on at the specified %RatekW at the specified discharge trigger time in fractional hours.

        In Schedule mode, the Tup, TFlat, and Tdn properties specify the up ramp duration, flat duration, and down ramp duration for the schedule. The schedule start time is set by TimeDischargeTrigger and the rate of discharge for the flat part is determined by %RatekW.

        In I-PeakShave mode, the control attempts to discharge Storage to keep current in the monitored element below the target given in k-amps (thousands of amps), when this control mode is active, the property kWTarget will be expressed in k-amps. 

        DSS property name: `ModeDischarge`, DSS property index: 12.
        """
        return BatchInt32ArrayProxy(self, 12)

    def _set_ModeDischarge(self, value: Union[AnyStr, int, enums.StorageControllerDischargeMode, List[AnyStr], List[int], List[enums.StorageControllerDischargeMode], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(12, value, flags)
            return

        self._set_batch_int32_array(12, value, flags)

    ModeDischarge = property(_get_ModeDischarge, _set_ModeDischarge) # type: BatchInt32ArrayProxy

    def _get_ModeDischarge_str(self) -> List[str]:
        """
        {PeakShave* | Follow | Support | Loadshape | Time | Schedule | I-PeakShave} Mode of operation for the DISCHARGE FUNCTION of this controller. 

        In PeakShave mode (Default), the control attempts to discharge Storage to keep power in the monitored element below the kWTarget. 

        In Follow mode, the control is triggered by time and resets the kWTarget value to the present monitored element power. It then attempts to discharge Storage to keep power in the monitored element below the new kWTarget. See TimeDischargeTrigger.

        In Support mode, the control operates oppositely of PeakShave mode: Storage is discharged to keep kW power output up near the target. 

        In Loadshape mode, both charging and discharging precisely follows the per unit loadshape. Storage is discharged when the loadshape value is positive. 

        In Time mode, the Storage discharge is turned on at the specified %RatekW at the specified discharge trigger time in fractional hours.

        In Schedule mode, the Tup, TFlat, and Tdn properties specify the up ramp duration, flat duration, and down ramp duration for the schedule. The schedule start time is set by TimeDischargeTrigger and the rate of discharge for the flat part is determined by %RatekW.

        In I-PeakShave mode, the control attempts to discharge Storage to keep current in the monitored element below the target given in k-amps (thousands of amps), when this control mode is active, the property kWTarget will be expressed in k-amps. 

        DSS property name: `ModeDischarge`, DSS property index: 12.
        """
        return self._get_batch_str_prop(12)

    def _set_ModeDischarge_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_ModeDischarge(value, flags)

    ModeDischarge_str = property(_get_ModeDischarge_str, _set_ModeDischarge_str) # type: List[str]

    def _get_ModeCharge(self) -> BatchInt32ArrayProxy:
        """
        {Loadshape | Time* | PeakShaveLow | I-PeakShaveLow} Mode of operation for the CHARGE FUNCTION of this controller. 

        In Loadshape mode, both charging and discharging precisely follows the per unit loadshape. Storage is charged when the loadshape value is negative. 

        In Time mode, the Storage charging FUNCTION is triggered at the specified %RateCharge at the specified charge trigger time in fractional hours.

        In PeakShaveLow mode, the charging operation will charge the Storage fleet when the power at a monitored element is below a specified KW target (kWTarget_low). The Storage will charge as much power as necessary to keep the power within the deadband around kWTarget_low.

        In I-PeakShaveLow mode, the charging operation will charge the Storage fleet when the current (Amps) at a monitored element is below a specified amps target (kWTarget_low). The Storage will charge as much power as necessary to keep the amps within the deadband around kWTarget_low. When this control mode is active, the property kWTarget_low will be expressed in k-amps and all the other parameters will be adjusted to match the amps (current) control criteria.

        DSS property name: `ModeCharge`, DSS property index: 13.
        """
        return BatchInt32ArrayProxy(self, 13)

    def _set_ModeCharge(self, value: Union[AnyStr, int, enums.StorageControllerChargeMode, List[AnyStr], List[int], List[enums.StorageControllerChargeMode], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(13, value, flags)
            return

        self._set_batch_int32_array(13, value, flags)

    ModeCharge = property(_get_ModeCharge, _set_ModeCharge) # type: BatchInt32ArrayProxy

    def _get_ModeCharge_str(self) -> List[str]:
        """
        {Loadshape | Time* | PeakShaveLow | I-PeakShaveLow} Mode of operation for the CHARGE FUNCTION of this controller. 

        In Loadshape mode, both charging and discharging precisely follows the per unit loadshape. Storage is charged when the loadshape value is negative. 

        In Time mode, the Storage charging FUNCTION is triggered at the specified %RateCharge at the specified charge trigger time in fractional hours.

        In PeakShaveLow mode, the charging operation will charge the Storage fleet when the power at a monitored element is below a specified KW target (kWTarget_low). The Storage will charge as much power as necessary to keep the power within the deadband around kWTarget_low.

        In I-PeakShaveLow mode, the charging operation will charge the Storage fleet when the current (Amps) at a monitored element is below a specified amps target (kWTarget_low). The Storage will charge as much power as necessary to keep the amps within the deadband around kWTarget_low. When this control mode is active, the property kWTarget_low will be expressed in k-amps and all the other parameters will be adjusted to match the amps (current) control criteria.

        DSS property name: `ModeCharge`, DSS property index: 13.
        """
        return self._get_batch_str_prop(13)

    def _set_ModeCharge_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_ModeCharge(value, flags)

    ModeCharge_str = property(_get_ModeCharge_str, _set_ModeCharge_str) # type: List[str]

    def _get_TimeDischargeTrigger(self) -> BatchFloat64ArrayProxy:
        """
        Default time of day (hr) for initiating Discharging of the fleet. During Follow or Time mode discharging is triggered at a fixed time each day at this hour. If Follow mode, Storage will be discharged to attempt to hold the load at or below the power level at the time of triggering. In Time mode, the discharge is based on the %RatekW property value. Set this to a negative value to ignore. Default is 12.0 for Follow mode; otherwise it is -1 (ignored). 

        DSS property name: `TimeDischargeTrigger`, DSS property index: 14.
        """
        return BatchFloat64ArrayProxy(self, 14)

    def _set_TimeDischargeTrigger(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(14, value, flags)

    TimeDischargeTrigger = property(_get_TimeDischargeTrigger, _set_TimeDischargeTrigger) # type: BatchFloat64ArrayProxy

    def _get_TimeChargeTrigger(self) -> BatchFloat64ArrayProxy:
        """
        Default time of day (hr) for initiating charging in Time control mode. Set this to a negative value to ignore. Default is 2.0.  (0200).When this value is >0 the Storage fleet is set to charging at this time regardless of other control criteria to make sure Storage is topped off for the next discharge cycle.

        DSS property name: `TimeChargeTrigger`, DSS property index: 15.
        """
        return BatchFloat64ArrayProxy(self, 15)

    def _set_TimeChargeTrigger(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(15, value, flags)

    TimeChargeTrigger = property(_get_TimeChargeTrigger, _set_TimeChargeTrigger) # type: BatchFloat64ArrayProxy

    def _get_pctRatekW(self) -> BatchFloat64ArrayProxy:
        """
        Sets the kW discharge rate in % of rated capacity for each element of the fleet. Applies to TIME control mode, SCHEDULE mode, or anytime discharging is triggered by time.

        DSS property name: `%RatekW`, DSS property index: 16.
        """
        return BatchFloat64ArrayProxy(self, 16)

    def _set_pctRatekW(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(16, value, flags)

    pctRatekW = property(_get_pctRatekW, _set_pctRatekW) # type: BatchFloat64ArrayProxy

    def _get_pctRateCharge(self) -> BatchFloat64ArrayProxy:
        """
        Sets the kW charging rate in % of rated capacity for each element of the fleet. Applies to TIME control mode and anytime charging mode is entered due to a time trigger.

        DSS property name: `%RateCharge`, DSS property index: 17.
        """
        return BatchFloat64ArrayProxy(self, 17)

    def _set_pctRateCharge(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(17, value, flags)

    pctRateCharge = property(_get_pctRateCharge, _set_pctRateCharge) # type: BatchFloat64ArrayProxy

    def _get_pctReserve(self) -> BatchFloat64ArrayProxy:
        """
        Use this property to change the % reserve for each Storage element under control of this controller. This might be used, for example, to allow deeper discharges of Storage or in case of emergency operation to use the remainder of the Storage element.

        DSS property name: `%Reserve`, DSS property index: 18.
        """
        return BatchFloat64ArrayProxy(self, 18)

    def _set_pctReserve(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(18, value, flags)

    pctReserve = property(_get_pctReserve, _set_pctReserve) # type: BatchFloat64ArrayProxy

    def _get_kWhTotal(self) -> BatchFloat64ArrayProxy:
        """
        (Read only). Total rated kWh energy Storage capacity of Storage elements controlled by this controller.

        DSS property name: `kWhTotal`, DSS property index: 19.
        """
        return BatchFloat64ArrayProxy(self, 19)

    def _set_kWhTotal(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(19, value, flags)

    kWhTotal = property(_get_kWhTotal, _set_kWhTotal) # type: BatchFloat64ArrayProxy

    def _get_kWTotal(self) -> BatchFloat64ArrayProxy:
        """
        (Read only). Total rated kW power capacity of Storage elements controlled by this controller.

        DSS property name: `kWTotal`, DSS property index: 20.
        """
        return BatchFloat64ArrayProxy(self, 20)

    def _set_kWTotal(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(20, value, flags)

    kWTotal = property(_get_kWTotal, _set_kWTotal) # type: BatchFloat64ArrayProxy

    def _get_kWhActual(self) -> BatchFloat64ArrayProxy:
        """
        (Read only). Actual kWh stored of all controlled Storage elements. 

        DSS property name: `kWhActual`, DSS property index: 21.
        """
        return BatchFloat64ArrayProxy(self, 21)

    def _set_kWhActual(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(21, value, flags)

    kWhActual = property(_get_kWhActual, _set_kWhActual) # type: BatchFloat64ArrayProxy

    def _get_kWActual(self) -> BatchFloat64ArrayProxy:
        """
        (Read only). Actual kW output of all controlled Storage elements. 

        DSS property name: `kWActual`, DSS property index: 22.
        """
        return BatchFloat64ArrayProxy(self, 22)

    def _set_kWActual(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(22, value, flags)

    kWActual = property(_get_kWActual, _set_kWActual) # type: BatchFloat64ArrayProxy

    def _get_kWNeed(self) -> BatchFloat64ArrayProxy:
        """
        (Read only). KW needed to meet target.

        DSS property name: `kWNeed`, DSS property index: 23.
        """
        return BatchFloat64ArrayProxy(self, 23)

    def _set_kWNeed(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(23, value, flags)

    kWNeed = property(_get_kWNeed, _set_kWNeed) # type: BatchFloat64ArrayProxy

    def _get_Yearly_str(self) -> List[str]:
        """
        Dispatch loadshape object, If any, for Yearly solution Mode.

        DSS property name: `Yearly`, DSS property index: 24.
        """
        return self._get_batch_str_prop(24)

    def _set_Yearly_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(24, value, flags)

    Yearly_str = property(_get_Yearly_str, _set_Yearly_str) # type: List[str]

    def _get_Yearly(self) -> List[LoadShape]:
        """
        Dispatch loadshape object, If any, for Yearly solution Mode.

        DSS property name: `Yearly`, DSS property index: 24.
        """
        return self._get_batch_obj_prop(24)

    def _set_Yearly(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(24, value, flags)

    Yearly = property(_get_Yearly, _set_Yearly) # type: List[LoadShape]

    def _get_Daily_str(self) -> List[str]:
        """
        Dispatch loadshape object, If any, for Daily solution mode.

        DSS property name: `Daily`, DSS property index: 25.
        """
        return self._get_batch_str_prop(25)

    def _set_Daily_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(25, value, flags)

    Daily_str = property(_get_Daily_str, _set_Daily_str) # type: List[str]

    def _get_Daily(self) -> List[LoadShape]:
        """
        Dispatch loadshape object, If any, for Daily solution mode.

        DSS property name: `Daily`, DSS property index: 25.
        """
        return self._get_batch_obj_prop(25)

    def _set_Daily(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(25, value, flags)

    Daily = property(_get_Daily, _set_Daily) # type: List[LoadShape]

    def _get_Duty_str(self) -> List[str]:
        """
        Dispatch loadshape object, If any, for Dutycycle solution mode.

        DSS property name: `Duty`, DSS property index: 26.
        """
        return self._get_batch_str_prop(26)

    def _set_Duty_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(26, value, flags)

    Duty_str = property(_get_Duty_str, _set_Duty_str) # type: List[str]

    def _get_Duty(self) -> List[LoadShape]:
        """
        Dispatch loadshape object, If any, for Dutycycle solution mode.

        DSS property name: `Duty`, DSS property index: 26.
        """
        return self._get_batch_obj_prop(26)

    def _set_Duty(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(26, value, flags)

    Duty = property(_get_Duty, _set_Duty) # type: List[LoadShape]

    def _get_EventLog(self) -> List[bool]:
        """
        {Yes/True | No/False} Default is No. Log control actions to Eventlog.

        DSS property name: `EventLog`, DSS property index: 27.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(27)
        ]

    def _set_EventLog(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(27, value, flags)

    EventLog = property(_get_EventLog, _set_EventLog) # type: List[bool]

    def _get_InhibitTime(self) -> BatchInt32ArrayProxy:
        """
        Hours (integer) to inhibit Discharging after going into Charge mode. Default is 5.

        DSS property name: `InhibitTime`, DSS property index: 28.
        """
        return BatchInt32ArrayProxy(self, 28)

    def _set_InhibitTime(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(28, value, flags)

    InhibitTime = property(_get_InhibitTime, _set_InhibitTime) # type: BatchInt32ArrayProxy

    def _get_TUp(self) -> BatchFloat64ArrayProxy:
        """
        Duration, hrs, of upramp part for SCHEDULE mode. Default is 0.25.

        DSS property name: `TUp`, DSS property index: 29.
        """
        return BatchFloat64ArrayProxy(self, 29)

    def _set_TUp(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(29, value, flags)

    TUp = property(_get_TUp, _set_TUp) # type: BatchFloat64ArrayProxy

    def _get_TFlat(self) -> BatchFloat64ArrayProxy:
        """
        Duration, hrs, of flat part for SCHEDULE mode. Default is 2.0.

        DSS property name: `TFlat`, DSS property index: 30.
        """
        return BatchFloat64ArrayProxy(self, 30)

    def _set_TFlat(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(30, value, flags)

    TFlat = property(_get_TFlat, _set_TFlat) # type: BatchFloat64ArrayProxy

    def _get_TDn(self) -> BatchFloat64ArrayProxy:
        """
        Duration, hrs, of downramp part for SCHEDULE mode. Default is 0.25.

        DSS property name: `TDn`, DSS property index: 31.
        """
        return BatchFloat64ArrayProxy(self, 31)

    def _set_TDn(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(31, value, flags)

    TDn = property(_get_TDn, _set_TDn) # type: BatchFloat64ArrayProxy

    def _get_kWThreshold(self) -> BatchFloat64ArrayProxy:
        """
        Threshold, kW, for Follow mode. kW has to be above this value for the Storage element to be dispatched on. Defaults to 75% of the kWTarget value. Must reset this property after setting kWTarget if you want a different value.

        DSS property name: `kWThreshold`, DSS property index: 32.
        """
        return BatchFloat64ArrayProxy(self, 32)

    def _set_kWThreshold(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(32, value, flags)

    kWThreshold = property(_get_kWThreshold, _set_kWThreshold) # type: BatchFloat64ArrayProxy

    def _get_DispFactor(self) -> BatchFloat64ArrayProxy:
        """
        Defaults to 1 (disabled). Set to any value between 0 and 1 to enable this parameter.

        Use this parameter to reduce the amount of power requested by the controller in each control iteration. It can be useful when maximum control iterations are exceeded due to numerical instability such as fleet being set to charging and idling in subsequent control iterations (check the Eventlog). 

        DSS property name: `DispFactor`, DSS property index: 33.
        """
        return BatchFloat64ArrayProxy(self, 33)

    def _set_DispFactor(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(33, value, flags)

    DispFactor = property(_get_DispFactor, _set_DispFactor) # type: BatchFloat64ArrayProxy

    def _get_ResetLevel(self) -> BatchFloat64ArrayProxy:
        """
        The level of charge required for allowing the storage to discharge again after reaching the reserve storage level. After reaching this level, the storage control  will not allow the storage device to discharge, forcing the storage to charge. Once the storage reaches this level, the storage will be able to discharge again. This value is a number between 0.2 and 1

        DSS property name: `ResetLevel`, DSS property index: 34.
        """
        return BatchFloat64ArrayProxy(self, 34)

    def _set_ResetLevel(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(34, value, flags)

    ResetLevel = property(_get_ResetLevel, _set_ResetLevel) # type: BatchFloat64ArrayProxy

    def _get_Seasons(self) -> BatchInt32ArrayProxy:
        """
        With this property the user can specify the number of targets to be used by the controller using the list given at "SeasonTargets"/"SeasonTargetsLow", which can be used to dynamically adjust the storage controller during a QSTS simulation. The default value is 1. This property needs to be defined before defining SeasonTargets/SeasonTargetsLow.

        DSS property name: `Seasons`, DSS property index: 35.
        """
        return BatchInt32ArrayProxy(self, 35)

    def _set_Seasons(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(35, value, flags)

    Seasons = property(_get_Seasons, _set_Seasons) # type: BatchInt32ArrayProxy

    def _get_SeasonTargets(self) -> List[Float64Array]:
        """
        An array of doubles specifying the targets to be used during a QSTS simulation. These targets will take effect only if SeasonRating=true. The number of targets cannot exceed the number of seasons defined at the SeasonSignal.The difference between the targets defined at SeasonTargets and SeasonTargetsLow is that SeasonTargets applies to discharging modes, while SeasonTargetsLow applies to charging modes.

        DSS property name: `SeasonTargets`, DSS property index: 36.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 36)
            for x in self._unpack()
        ]

    def _set_SeasonTargets(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(36, value, flags)

    SeasonTargets = property(_get_SeasonTargets, _set_SeasonTargets) # type: List[Float64Array]

    def _get_SeasonTargetsLow(self) -> List[Float64Array]:
        """
        An array of doubles specifying the targets to be used during a QSTS simulation. These targets will take effect only if SeasonRating=true. The number of targets cannot exceed the number of seasons defined at the SeasonSignal.The difference between the targets defined at SeasonTargets and SeasonTargetsLow is that SeasonTargets applies to discharging modes, while SeasonTargetsLow applies to charging modes.

        DSS property name: `SeasonTargetsLow`, DSS property index: 37.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 37)
            for x in self._unpack()
        ]

    def _set_SeasonTargetsLow(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(37, value, flags)

    SeasonTargetsLow = property(_get_SeasonTargetsLow, _set_SeasonTargetsLow) # type: List[Float64Array]

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 38.
        """
        return BatchFloat64ArrayProxy(self, 38)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(38, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy

    def _get_Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 39.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(39)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(39, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 40.
        """
        self._set_batch_string(40, value, flags)

class StorageControllerBatchProperties(TypedDict):
    Element: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]]
    Terminal: Union[int, Int32Array]
    MonPhase: Union[AnyStr, int, enums.MonitoredPhase, List[AnyStr], List[int], List[enums.MonitoredPhase], Int32Array]
    kWTarget: Union[float, Float64Array]
    kWTargetLow: Union[float, Float64Array]
    pctkWBand: Union[float, Float64Array]
    kWBand: Union[float, Float64Array]
    pctkWBandLow: Union[float, Float64Array]
    kWBandLow: Union[float, Float64Array]
    ElementList: List[AnyStr]
    Weights: Float64Array
    ModeDischarge: Union[AnyStr, int, enums.StorageControllerDischargeMode, List[AnyStr], List[int], List[enums.StorageControllerDischargeMode], Int32Array]
    ModeCharge: Union[AnyStr, int, enums.StorageControllerChargeMode, List[AnyStr], List[int], List[enums.StorageControllerChargeMode], Int32Array]
    TimeDischargeTrigger: Union[float, Float64Array]
    TimeChargeTrigger: Union[float, Float64Array]
    pctRatekW: Union[float, Float64Array]
    pctRateCharge: Union[float, Float64Array]
    pctReserve: Union[float, Float64Array]
    kWhTotal: Union[float, Float64Array]
    kWTotal: Union[float, Float64Array]
    kWhActual: Union[float, Float64Array]
    kWActual: Union[float, Float64Array]
    kWNeed: Union[float, Float64Array]
    Yearly: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    Daily: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    Duty: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    EventLog: bool
    InhibitTime: Union[int, Int32Array]
    TUp: Union[float, Float64Array]
    TFlat: Union[float, Float64Array]
    TDn: Union[float, Float64Array]
    kWThreshold: Union[float, Float64Array]
    DispFactor: Union[float, Float64Array]
    ResetLevel: Union[float, Float64Array]
    Seasons: Union[int, Int32Array]
    SeasonTargets: Float64Array
    SeasonTargetsLow: Float64Array
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IStorageController(IDSSObj, StorageControllerBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, StorageController, StorageControllerBatch)
        StorageControllerBatch.__init__(self, self._api_util, sync_cls_idx=StorageController._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> StorageController:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[StorageControllerProperties]) -> StorageController:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[StorageControllerBatchProperties]) -> StorageControllerBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
