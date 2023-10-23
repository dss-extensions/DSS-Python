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
from .LoadShape import LoadShape

class StorageController(DSSObj, CktElementMixin):
    __slots__ = CktElementMixin._extra_slots
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

    @property
    def Element(self) -> str:
        """
        Full object name of the circuit element, typically a line or transformer, which the control is monitoring. There is no default; Must be specified.In "Local" control mode, is the name of the load that will be managed by the storage device, which should be installed at the same bus.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    @Element.setter
    def Element(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_obj(1, value)
            return

        self._set_string_o(1, value)

    @property
    def Element_obj(self) -> DSSObj:
        """
        Full object name of the circuit element, typically a line or transformer, which the control is monitoring. There is no default; Must be specified.In "Local" control mode, is the name of the load that will be managed by the storage device, which should be installed at the same bus.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_obj(1, None)

    @Element_obj.setter
    def Element_obj(self, value: DSSObj):
        self._set_obj(1, value)

    @property
    def Terminal(self) -> int:
        """
        Number of the terminal of the circuit element to which the StorageController control is connected. 1 or 2, typically.  Default is 1. Make sure to select the proper direction on the power for the respective dispatch mode.

        DSS property name: `Terminal`, DSS property index: 2.
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @Terminal.setter
    def Terminal(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def MonPhase(self) -> Union[enums.MonitoredPhase, int]:
        """
        Number of the phase being monitored or one of {AVG | MAX | MIN} for all phases. Default=MAX. Must be less than the number of phases. Used in PeakShave, Follow, Support and I-PeakShave discharging modes and in PeakShaveLow, I-PeakShaveLow charging modes. For modes based on active power measurements, the value used by the control is the monitored one multiplied by the number of phases of the monitored element.

        DSS property name: `MonPhase`, DSS property index: 3.
        """
        value = self._lib.Obj_GetInt32(self._ptr, 3)
        if value > 0:
            return value
    
        return enums.MonitoredPhase(value)

    @MonPhase.setter
    def MonPhase(self, value: Union[AnyStr, int, enums.MonitoredPhase]):
        if not isinstance(value, int):
            self._set_string_o(3, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 3, value)

    @property
    def MonPhase_str(self) -> str:
        """
        Number of the phase being monitored or one of {AVG | MAX | MIN} for all phases. Default=MAX. Must be less than the number of phases. Used in PeakShave, Follow, Support and I-PeakShave discharging modes and in PeakShaveLow, I-PeakShaveLow charging modes. For modes based on active power measurements, the value used by the control is the monitored one multiplied by the number of phases of the monitored element.

        DSS property name: `MonPhase`, DSS property index: 3.
        """
        return self._get_prop_string(3)

    @MonPhase_str.setter
    def MonPhase_str(self, value: AnyStr):
        self.MonPhase = value

    @property
    def kWTarget(self) -> float:
        """
        kW/kamps target for Discharging. The Storage element fleet is dispatched to try to hold the power/current in band at least until the Storage is depleted. The selection of power or current depends on the Discharge mode (PeakShave->kW, I-PeakShave->kamps).

        DSS property name: `kWTarget`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @kWTarget.setter
    def kWTarget(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def kWTargetLow(self) -> float:
        """
        kW/kamps target for Charging. The Storage element fleet is dispatched to try to hold the power/current in band at least until the Storage is fully charged. The selection of power or current depends on the charge mode (PeakShavelow->kW, I-PeakShavelow->kamps).

        DSS property name: `kWTargetLow`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @kWTargetLow.setter
    def kWTargetLow(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def pctkWBand(self) -> float:
        """
        Bandwidth (% of Target kW/kamps) of the dead band around the kW/kamps target value. Default is 2% (+/-1%).No dispatch changes are attempted if the power in the monitored terminal stays within this band.

        DSS property name: `%kWBand`, DSS property index: 6.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    @pctkWBand.setter
    def pctkWBand(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 6, value)

    @property
    def kWBand(self) -> float:
        """
        Alternative way of specifying the bandwidth. (kW/kamps) of the dead band around the kW/kamps target value. Default is 2% of kWTarget (+/-1%).No dispatch changes are attempted if the power in the monitored terminal stays within this band.

        DSS property name: `kWBand`, DSS property index: 7.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @kWBand.setter
    def kWBand(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def pctkWBandLow(self) -> float:
        """
        Bandwidth (% of kWTargetLow) of the dead band around the kW/kamps low target value. Default is 2% (+/-1%).No charging is attempted if the power in the monitored terminal stays within this band.

        DSS property name: `%kWBandLow`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @pctkWBandLow.setter
    def pctkWBandLow(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def kWBandLow(self) -> float:
        """
        Alternative way of specifying the bandwidth. (kW/kamps) of the dead band around the kW/kamps low target value. Default is 2% of kWTargetLow (+/-1%).No charging is attempted if the power in the monitored terminal stays within this band.

        DSS property name: `kWBandLow`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @kWBandLow.setter
    def kWBandLow(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def ElementList(self) -> List[str]:
        """
        Array list of Storage elements to be controlled.  If not specified, all Storage elements in the circuit not presently dispatched by another controller are assumed dispatched by this controller.

        DSS property name: `ElementList`, DSS property index: 10.
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 10)

    @ElementList.setter
    def ElementList(self, value: List[AnyStr]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 10, value_ptr, value_count)
        self._check_for_error()

    @property
    def Weights(self) -> Float64Array:
        """
        Array of proportional weights corresponding to each Storage element in the ElementList. The needed kW or kvar to get back to center band is dispatched to each Storage element according to these weights. Default is to set all weights to 1.0.

        DSS property name: `Weights`, DSS property index: 11.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 11)

    @Weights.setter
    def Weights(self, value: Float64Array):
        self._set_float64_array_o(11, value)

    @property
    def ModeDischarge(self) -> enums.StorageControllerDischargeMode:
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

    @ModeDischarge.setter
    def ModeDischarge(self, value: Union[AnyStr, int, enums.StorageControllerDischargeMode]):
        if not isinstance(value, int):
            self._set_string_o(12, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 12, value)

    @property
    def ModeDischarge_str(self) -> str:
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

    @ModeDischarge_str.setter
    def ModeDischarge_str(self, value: AnyStr):
        self.ModeDischarge = value

    @property
    def ModeCharge(self) -> enums.StorageControllerChargeMode:
        """
        {Loadshape | Time* | PeakShaveLow | I-PeakShaveLow} Mode of operation for the CHARGE FUNCTION of this controller. 

        In Loadshape mode, both charging and discharging precisely follows the per unit loadshape. Storage is charged when the loadshape value is negative. 

        In Time mode, the Storage charging FUNCTION is triggered at the specified %RateCharge at the specified charge trigger time in fractional hours.

        In PeakShaveLow mode, the charging operation will charge the Storage fleet when the power at a monitored element is below a specified KW target (kWTarget_low). The Storage will charge as much power as necessary to keep the power within the deadband around kWTarget_low.

        In I-PeakShaveLow mode, the charging operation will charge the Storage fleet when the current (Amps) at a monitored element is below a specified amps target (kWTarget_low). The Storage will charge as much power as necessary to keep the amps within the deadband around kWTarget_low. When this control mode is active, the property kWTarget_low will be expressed in k-amps and all the other parameters will be adjusted to match the amps (current) control criteria.

        DSS property name: `ModeCharge`, DSS property index: 13.
        """
        return enums.StorageControllerChargeMode(self._lib.Obj_GetInt32(self._ptr, 13))

    @ModeCharge.setter
    def ModeCharge(self, value: Union[AnyStr, int, enums.StorageControllerChargeMode]):
        if not isinstance(value, int):
            self._set_string_o(13, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 13, value)

    @property
    def ModeCharge_str(self) -> str:
        """
        {Loadshape | Time* | PeakShaveLow | I-PeakShaveLow} Mode of operation for the CHARGE FUNCTION of this controller. 

        In Loadshape mode, both charging and discharging precisely follows the per unit loadshape. Storage is charged when the loadshape value is negative. 

        In Time mode, the Storage charging FUNCTION is triggered at the specified %RateCharge at the specified charge trigger time in fractional hours.

        In PeakShaveLow mode, the charging operation will charge the Storage fleet when the power at a monitored element is below a specified KW target (kWTarget_low). The Storage will charge as much power as necessary to keep the power within the deadband around kWTarget_low.

        In I-PeakShaveLow mode, the charging operation will charge the Storage fleet when the current (Amps) at a monitored element is below a specified amps target (kWTarget_low). The Storage will charge as much power as necessary to keep the amps within the deadband around kWTarget_low. When this control mode is active, the property kWTarget_low will be expressed in k-amps and all the other parameters will be adjusted to match the amps (current) control criteria.

        DSS property name: `ModeCharge`, DSS property index: 13.
        """
        return self._get_prop_string(13)

    @ModeCharge_str.setter
    def ModeCharge_str(self, value: AnyStr):
        self.ModeCharge = value

    @property
    def TimeDischargeTrigger(self) -> float:
        """
        Default time of day (hr) for initiating Discharging of the fleet. During Follow or Time mode discharging is triggered at a fixed time each day at this hour. If Follow mode, Storage will be discharged to attempt to hold the load at or below the power level at the time of triggering. In Time mode, the discharge is based on the %RatekW property value. Set this to a negative value to ignore. Default is 12.0 for Follow mode; otherwise it is -1 (ignored). 

        DSS property name: `TimeDischargeTrigger`, DSS property index: 14.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @TimeDischargeTrigger.setter
    def TimeDischargeTrigger(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def TimeChargeTrigger(self) -> float:
        """
        Default time of day (hr) for initiating charging in Time control mode. Set this to a negative value to ignore. Default is 2.0.  (0200).When this value is >0 the Storage fleet is set to charging at this time regardless of other control criteria to make sure Storage is topped off for the next discharge cycle.

        DSS property name: `TimeChargeTrigger`, DSS property index: 15.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @TimeChargeTrigger.setter
    def TimeChargeTrigger(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def pctRatekW(self) -> float:
        """
        Sets the kW discharge rate in % of rated capacity for each element of the fleet. Applies to TIME control mode, SCHEDULE mode, or anytime discharging is triggered by time.

        DSS property name: `%RatekW`, DSS property index: 16.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    @pctRatekW.setter
    def pctRatekW(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 16, value)

    @property
    def pctRateCharge(self) -> float:
        """
        Sets the kW charging rate in % of rated capacity for each element of the fleet. Applies to TIME control mode and anytime charging mode is entered due to a time trigger.

        DSS property name: `%RateCharge`, DSS property index: 17.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    @pctRateCharge.setter
    def pctRateCharge(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 17, value)

    @property
    def pctReserve(self) -> float:
        """
        Use this property to change the % reserve for each Storage element under control of this controller. This might be used, for example, to allow deeper discharges of Storage or in case of emergency operation to use the remainder of the Storage element.

        DSS property name: `%Reserve`, DSS property index: 18.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    @pctReserve.setter
    def pctReserve(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 18, value)

    @property
    def kWhTotal(self) -> float:
        """
        (Read only). Total rated kWh energy Storage capacity of Storage elements controlled by this controller.

        DSS property name: `kWhTotal`, DSS property index: 19.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    @kWhTotal.setter
    def kWhTotal(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 19, value)

    @property
    def kWTotal(self) -> float:
        """
        (Read only). Total rated kW power capacity of Storage elements controlled by this controller.

        DSS property name: `kWTotal`, DSS property index: 20.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    @kWTotal.setter
    def kWTotal(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 20, value)

    @property
    def kWhActual(self) -> float:
        """
        (Read only). Actual kWh stored of all controlled Storage elements. 

        DSS property name: `kWhActual`, DSS property index: 21.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @kWhActual.setter
    def kWhActual(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    @property
    def kWActual(self) -> float:
        """
        (Read only). Actual kW output of all controlled Storage elements. 

        DSS property name: `kWActual`, DSS property index: 22.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    @kWActual.setter
    def kWActual(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 22, value)

    @property
    def kWNeed(self) -> float:
        """
        (Read only). KW needed to meet target.

        DSS property name: `kWNeed`, DSS property index: 23.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    @kWNeed.setter
    def kWNeed(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 23, value)

    @property
    def Yearly(self) -> str:
        """
        Dispatch loadshape object, If any, for Yearly solution Mode.

        DSS property name: `Yearly`, DSS property index: 24.
        """
        return self._get_prop_string(24)

    @Yearly.setter
    def Yearly(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(24, value)
            return

        self._set_string_o(24, value)

    @property
    def Yearly_obj(self) -> LoadShape:
        """
        Dispatch loadshape object, If any, for Yearly solution Mode.

        DSS property name: `Yearly`, DSS property index: 24.
        """
        return self._get_obj(24, LoadShape)

    @Yearly_obj.setter
    def Yearly_obj(self, value: LoadShape):
        self._set_obj(24, value)

    @property
    def Daily(self) -> str:
        """
        Dispatch loadshape object, If any, for Daily solution mode.

        DSS property name: `Daily`, DSS property index: 25.
        """
        return self._get_prop_string(25)

    @Daily.setter
    def Daily(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(25, value)
            return

        self._set_string_o(25, value)

    @property
    def Daily_obj(self) -> LoadShape:
        """
        Dispatch loadshape object, If any, for Daily solution mode.

        DSS property name: `Daily`, DSS property index: 25.
        """
        return self._get_obj(25, LoadShape)

    @Daily_obj.setter
    def Daily_obj(self, value: LoadShape):
        self._set_obj(25, value)

    @property
    def Duty(self) -> str:
        """
        Dispatch loadshape object, If any, for Dutycycle solution mode.

        DSS property name: `Duty`, DSS property index: 26.
        """
        return self._get_prop_string(26)

    @Duty.setter
    def Duty(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(26, value)
            return

        self._set_string_o(26, value)

    @property
    def Duty_obj(self) -> LoadShape:
        """
        Dispatch loadshape object, If any, for Dutycycle solution mode.

        DSS property name: `Duty`, DSS property index: 26.
        """
        return self._get_obj(26, LoadShape)

    @Duty_obj.setter
    def Duty_obj(self, value: LoadShape):
        self._set_obj(26, value)

    @property
    def EventLog(self) -> bool:
        """
        {Yes/True | No/False} Default is No. Log control actions to Eventlog.

        DSS property name: `EventLog`, DSS property index: 27.
        """
        return self._lib.Obj_GetInt32(self._ptr, 27) != 0

    @EventLog.setter
    def EventLog(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 27, value)

    @property
    def InhibitTime(self) -> int:
        """
        Hours (integer) to inhibit Discharging after going into Charge mode. Default is 5.

        DSS property name: `InhibitTime`, DSS property index: 28.
        """
        return self._lib.Obj_GetInt32(self._ptr, 28)

    @InhibitTime.setter
    def InhibitTime(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 28, value)

    @property
    def TUp(self) -> float:
        """
        Duration, hrs, of upramp part for SCHEDULE mode. Default is 0.25.

        DSS property name: `TUp`, DSS property index: 29.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 29)

    @TUp.setter
    def TUp(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 29, value)

    @property
    def TFlat(self) -> float:
        """
        Duration, hrs, of flat part for SCHEDULE mode. Default is 2.0.

        DSS property name: `TFlat`, DSS property index: 30.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 30)

    @TFlat.setter
    def TFlat(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 30, value)

    @property
    def TDn(self) -> float:
        """
        Duration, hrs, of downramp part for SCHEDULE mode. Default is 0.25.

        DSS property name: `TDn`, DSS property index: 31.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 31)

    @TDn.setter
    def TDn(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 31, value)

    @property
    def kWThreshold(self) -> float:
        """
        Threshold, kW, for Follow mode. kW has to be above this value for the Storage element to be dispatched on. Defaults to 75% of the kWTarget value. Must reset this property after setting kWTarget if you want a different value.

        DSS property name: `kWThreshold`, DSS property index: 32.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 32)

    @kWThreshold.setter
    def kWThreshold(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 32, value)

    @property
    def DispFactor(self) -> float:
        """
        Defaults to 1 (disabled). Set to any value between 0 and 1 to enable this parameter.

        Use this parameter to reduce the amount of power requested by the controller in each control iteration. It can be useful when maximum control iterations are exceeded due to numerical instability such as fleet being set to charging and idling in subsequent control iterations (check the Eventlog). 

        DSS property name: `DispFactor`, DSS property index: 33.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 33)

    @DispFactor.setter
    def DispFactor(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 33, value)

    @property
    def ResetLevel(self) -> float:
        """
        The level of charge required for allowing the storage to discharge again after reaching the reserve storage level. After reaching this level, the storage control  will not allow the storage device to discharge, forcing the storage to charge. Once the storage reaches this level, the storage will be able to discharge again. This value is a number between 0.2 and 1

        DSS property name: `ResetLevel`, DSS property index: 34.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 34)

    @ResetLevel.setter
    def ResetLevel(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 34, value)

    @property
    def Seasons(self) -> int:
        """
        With this property the user can specify the number of targets to be used by the controller using the list given at "SeasonTargets"/"SeasonTargetsLow", which can be used to dynamically adjust the storage controller during a QSTS simulation. The default value is 1. This property needs to be defined before defining SeasonTargets/SeasonTargetsLow.

        DSS property name: `Seasons`, DSS property index: 35.
        """
        return self._lib.Obj_GetInt32(self._ptr, 35)

    @Seasons.setter
    def Seasons(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 35, value)

    @property
    def SeasonTargets(self) -> Float64Array:
        """
        An array of doubles specifying the targets to be used during a QSTS simulation. These targets will take effect only if SeasonRating=true. The number of targets cannot exceed the number of seasons defined at the SeasonSignal.The difference between the targets defined at SeasonTargets and SeasonTargetsLow is that SeasonTargets applies to discharging modes, while SeasonTargetsLow applies to charging modes.

        DSS property name: `SeasonTargets`, DSS property index: 36.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 36)

    @SeasonTargets.setter
    def SeasonTargets(self, value: Float64Array):
        self._set_float64_array_o(36, value)

    @property
    def SeasonTargetsLow(self) -> Float64Array:
        """
        An array of doubles specifying the targets to be used during a QSTS simulation. These targets will take effect only if SeasonRating=true. The number of targets cannot exceed the number of seasons defined at the SeasonSignal.The difference between the targets defined at SeasonTargets and SeasonTargetsLow is that SeasonTargets applies to discharging modes, while SeasonTargetsLow applies to charging modes.

        DSS property name: `SeasonTargetsLow`, DSS property index: 37.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 37)

    @SeasonTargetsLow.setter
    def SeasonTargetsLow(self, value: Float64Array):
        self._set_float64_array_o(37, value)

    @property
    def BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 38.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 38)

    @BaseFreq.setter
    def BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 38, value)

    @property
    def Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 39.
        """
        return self._lib.Obj_GetInt32(self._ptr, 39) != 0

    @Enabled.setter
    def Enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 39, value)

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

class StorageControllerBatch(DSSBatch):
    _cls_name = 'StorageController'
    _obj_cls = StorageController
    _cls_idx = 30


    @property
    def Element(self) -> List[str]:
        """
        Full object name of the circuit element, typically a line or transformer, which the control is monitoring. There is no default; Must be specified.In "Local" control mode, is the name of the load that will be managed by the storage device, which should be installed at the same bus.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @Element.setter
    def Element(self, value: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]]):
        self._set_batch_obj_prop(1, value)

    @property
    def Element_obj(self) -> List[DSSObj]:
        """
        Full object name of the circuit element, typically a line or transformer, which the control is monitoring. There is no default; Must be specified.In "Local" control mode, is the name of the load that will be managed by the storage device, which should be installed at the same bus.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 1)

    @Element_obj.setter
    def Element_obj(self, value: DSSObj):
        self._set_batch_string(1, value)

    @property
    def Terminal(self) -> BatchInt32ArrayProxy:
        """
        Number of the terminal of the circuit element to which the StorageController control is connected. 1 or 2, typically.  Default is 1. Make sure to select the proper direction on the power for the respective dispatch mode.

        DSS property name: `Terminal`, DSS property index: 2.
        """
        return BatchInt32ArrayProxy(self, 2)

    @Terminal.setter
    def Terminal(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(2, value)

    @property
    def MonPhase(self) -> BatchInt32ArrayProxy:
        """
        Number of the phase being monitored or one of {AVG | MAX | MIN} for all phases. Default=MAX. Must be less than the number of phases. Used in PeakShave, Follow, Support and I-PeakShave discharging modes and in PeakShaveLow, I-PeakShaveLow charging modes. For modes based on active power measurements, the value used by the control is the monitored one multiplied by the number of phases of the monitored element.

        DSS property name: `MonPhase`, DSS property index: 3.
        """
        return BatchInt32ArrayProxy(self, 3)

    @MonPhase.setter
    def MonPhase(self, value: Union[AnyStr, int, enums.MonitoredPhase, List[AnyStr], List[int], List[enums.MonitoredPhase], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(3, value)
            return
    
        self._set_batch_int32_array(3, value)

    @property
    def MonPhase_str(self) -> str:
        """
        Number of the phase being monitored or one of {AVG | MAX | MIN} for all phases. Default=MAX. Must be less than the number of phases. Used in PeakShave, Follow, Support and I-PeakShave discharging modes and in PeakShaveLow, I-PeakShaveLow charging modes. For modes based on active power measurements, the value used by the control is the monitored one multiplied by the number of phases of the monitored element.

        DSS property name: `MonPhase`, DSS property index: 3.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 3)

    @MonPhase_str.setter
    def MonPhase_str(self, value: AnyStr):
        self.MonPhase = value

    @property
    def kWTarget(self) -> BatchFloat64ArrayProxy:
        """
        kW/kamps target for Discharging. The Storage element fleet is dispatched to try to hold the power/current in band at least until the Storage is depleted. The selection of power or current depends on the Discharge mode (PeakShave->kW, I-PeakShave->kamps).

        DSS property name: `kWTarget`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    @kWTarget.setter
    def kWTarget(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(4, value)

    @property
    def kWTargetLow(self) -> BatchFloat64ArrayProxy:
        """
        kW/kamps target for Charging. The Storage element fleet is dispatched to try to hold the power/current in band at least until the Storage is fully charged. The selection of power or current depends on the charge mode (PeakShavelow->kW, I-PeakShavelow->kamps).

        DSS property name: `kWTargetLow`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    @kWTargetLow.setter
    def kWTargetLow(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(5, value)

    @property
    def pctkWBand(self) -> BatchFloat64ArrayProxy:
        """
        Bandwidth (% of Target kW/kamps) of the dead band around the kW/kamps target value. Default is 2% (+/-1%).No dispatch changes are attempted if the power in the monitored terminal stays within this band.

        DSS property name: `%kWBand`, DSS property index: 6.
        """
        return BatchFloat64ArrayProxy(self, 6)

    @pctkWBand.setter
    def pctkWBand(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(6, value)

    @property
    def kWBand(self) -> BatchFloat64ArrayProxy:
        """
        Alternative way of specifying the bandwidth. (kW/kamps) of the dead band around the kW/kamps target value. Default is 2% of kWTarget (+/-1%).No dispatch changes are attempted if the power in the monitored terminal stays within this band.

        DSS property name: `kWBand`, DSS property index: 7.
        """
        return BatchFloat64ArrayProxy(self, 7)

    @kWBand.setter
    def kWBand(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(7, value)

    @property
    def pctkWBandLow(self) -> BatchFloat64ArrayProxy:
        """
        Bandwidth (% of kWTargetLow) of the dead band around the kW/kamps low target value. Default is 2% (+/-1%).No charging is attempted if the power in the monitored terminal stays within this band.

        DSS property name: `%kWBandLow`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    @pctkWBandLow.setter
    def pctkWBandLow(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(8, value)

    @property
    def kWBandLow(self) -> BatchFloat64ArrayProxy:
        """
        Alternative way of specifying the bandwidth. (kW/kamps) of the dead band around the kW/kamps low target value. Default is 2% of kWTargetLow (+/-1%).No charging is attempted if the power in the monitored terminal stays within this band.

        DSS property name: `kWBandLow`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    @kWBandLow.setter
    def kWBandLow(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(9, value)

    @property
    def ElementList(self) -> List[List[str]]:
        """
        Array list of Storage elements to be controlled.  If not specified, all Storage elements in the circuit not presently dispatched by another controller are assumed dispatched by this controller.

        DSS property name: `ElementList`, DSS property index: 10.
        """
        return self._get_string_ll(10)

    @ElementList.setter
    def ElementList(self, value: List[AnyStr]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._ffi.unpack(self.pointer[0], self.count[0]):
            self._lib.Obj_SetStringArray(x, 10, value_ptr, value_count)
    
        self._check_for_error()

    @property
    def Weights(self) -> List[Float64Array]:
        """
        Array of proportional weights corresponding to each Storage element in the ElementList. The needed kW or kvar to get back to center band is dispatched to each Storage element according to these weights. Default is to set all weights to 1.0.

        DSS property name: `Weights`, DSS property index: 11.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 11)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Weights.setter
    def Weights(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(11, value)

    @property
    def ModeDischarge(self) -> BatchInt32ArrayProxy:
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

    @ModeDischarge.setter
    def ModeDischarge(self, value: Union[AnyStr, int, enums.StorageControllerDischargeMode, List[AnyStr], List[int], List[enums.StorageControllerDischargeMode], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(12, value)
            return
    
        self._set_batch_int32_array(12, value)

    @property
    def ModeDischarge_str(self) -> str:
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
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 12)

    @ModeDischarge_str.setter
    def ModeDischarge_str(self, value: AnyStr):
        self.ModeDischarge = value

    @property
    def ModeCharge(self) -> BatchInt32ArrayProxy:
        """
        {Loadshape | Time* | PeakShaveLow | I-PeakShaveLow} Mode of operation for the CHARGE FUNCTION of this controller. 

        In Loadshape mode, both charging and discharging precisely follows the per unit loadshape. Storage is charged when the loadshape value is negative. 

        In Time mode, the Storage charging FUNCTION is triggered at the specified %RateCharge at the specified charge trigger time in fractional hours.

        In PeakShaveLow mode, the charging operation will charge the Storage fleet when the power at a monitored element is below a specified KW target (kWTarget_low). The Storage will charge as much power as necessary to keep the power within the deadband around kWTarget_low.

        In I-PeakShaveLow mode, the charging operation will charge the Storage fleet when the current (Amps) at a monitored element is below a specified amps target (kWTarget_low). The Storage will charge as much power as necessary to keep the amps within the deadband around kWTarget_low. When this control mode is active, the property kWTarget_low will be expressed in k-amps and all the other parameters will be adjusted to match the amps (current) control criteria.

        DSS property name: `ModeCharge`, DSS property index: 13.
        """
        return BatchInt32ArrayProxy(self, 13)

    @ModeCharge.setter
    def ModeCharge(self, value: Union[AnyStr, int, enums.StorageControllerChargeMode, List[AnyStr], List[int], List[enums.StorageControllerChargeMode], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(13, value)
            return
    
        self._set_batch_int32_array(13, value)

    @property
    def ModeCharge_str(self) -> str:
        """
        {Loadshape | Time* | PeakShaveLow | I-PeakShaveLow} Mode of operation for the CHARGE FUNCTION of this controller. 

        In Loadshape mode, both charging and discharging precisely follows the per unit loadshape. Storage is charged when the loadshape value is negative. 

        In Time mode, the Storage charging FUNCTION is triggered at the specified %RateCharge at the specified charge trigger time in fractional hours.

        In PeakShaveLow mode, the charging operation will charge the Storage fleet when the power at a monitored element is below a specified KW target (kWTarget_low). The Storage will charge as much power as necessary to keep the power within the deadband around kWTarget_low.

        In I-PeakShaveLow mode, the charging operation will charge the Storage fleet when the current (Amps) at a monitored element is below a specified amps target (kWTarget_low). The Storage will charge as much power as necessary to keep the amps within the deadband around kWTarget_low. When this control mode is active, the property kWTarget_low will be expressed in k-amps and all the other parameters will be adjusted to match the amps (current) control criteria.

        DSS property name: `ModeCharge`, DSS property index: 13.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 13)

    @ModeCharge_str.setter
    def ModeCharge_str(self, value: AnyStr):
        self.ModeCharge = value

    @property
    def TimeDischargeTrigger(self) -> BatchFloat64ArrayProxy:
        """
        Default time of day (hr) for initiating Discharging of the fleet. During Follow or Time mode discharging is triggered at a fixed time each day at this hour. If Follow mode, Storage will be discharged to attempt to hold the load at or below the power level at the time of triggering. In Time mode, the discharge is based on the %RatekW property value. Set this to a negative value to ignore. Default is 12.0 for Follow mode; otherwise it is -1 (ignored). 

        DSS property name: `TimeDischargeTrigger`, DSS property index: 14.
        """
        return BatchFloat64ArrayProxy(self, 14)

    @TimeDischargeTrigger.setter
    def TimeDischargeTrigger(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(14, value)

    @property
    def TimeChargeTrigger(self) -> BatchFloat64ArrayProxy:
        """
        Default time of day (hr) for initiating charging in Time control mode. Set this to a negative value to ignore. Default is 2.0.  (0200).When this value is >0 the Storage fleet is set to charging at this time regardless of other control criteria to make sure Storage is topped off for the next discharge cycle.

        DSS property name: `TimeChargeTrigger`, DSS property index: 15.
        """
        return BatchFloat64ArrayProxy(self, 15)

    @TimeChargeTrigger.setter
    def TimeChargeTrigger(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(15, value)

    @property
    def pctRatekW(self) -> BatchFloat64ArrayProxy:
        """
        Sets the kW discharge rate in % of rated capacity for each element of the fleet. Applies to TIME control mode, SCHEDULE mode, or anytime discharging is triggered by time.

        DSS property name: `%RatekW`, DSS property index: 16.
        """
        return BatchFloat64ArrayProxy(self, 16)

    @pctRatekW.setter
    def pctRatekW(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(16, value)

    @property
    def pctRateCharge(self) -> BatchFloat64ArrayProxy:
        """
        Sets the kW charging rate in % of rated capacity for each element of the fleet. Applies to TIME control mode and anytime charging mode is entered due to a time trigger.

        DSS property name: `%RateCharge`, DSS property index: 17.
        """
        return BatchFloat64ArrayProxy(self, 17)

    @pctRateCharge.setter
    def pctRateCharge(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(17, value)

    @property
    def pctReserve(self) -> BatchFloat64ArrayProxy:
        """
        Use this property to change the % reserve for each Storage element under control of this controller. This might be used, for example, to allow deeper discharges of Storage or in case of emergency operation to use the remainder of the Storage element.

        DSS property name: `%Reserve`, DSS property index: 18.
        """
        return BatchFloat64ArrayProxy(self, 18)

    @pctReserve.setter
    def pctReserve(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(18, value)

    @property
    def kWhTotal(self) -> BatchFloat64ArrayProxy:
        """
        (Read only). Total rated kWh energy Storage capacity of Storage elements controlled by this controller.

        DSS property name: `kWhTotal`, DSS property index: 19.
        """
        return BatchFloat64ArrayProxy(self, 19)

    @kWhTotal.setter
    def kWhTotal(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(19, value)

    @property
    def kWTotal(self) -> BatchFloat64ArrayProxy:
        """
        (Read only). Total rated kW power capacity of Storage elements controlled by this controller.

        DSS property name: `kWTotal`, DSS property index: 20.
        """
        return BatchFloat64ArrayProxy(self, 20)

    @kWTotal.setter
    def kWTotal(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(20, value)

    @property
    def kWhActual(self) -> BatchFloat64ArrayProxy:
        """
        (Read only). Actual kWh stored of all controlled Storage elements. 

        DSS property name: `kWhActual`, DSS property index: 21.
        """
        return BatchFloat64ArrayProxy(self, 21)

    @kWhActual.setter
    def kWhActual(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(21, value)

    @property
    def kWActual(self) -> BatchFloat64ArrayProxy:
        """
        (Read only). Actual kW output of all controlled Storage elements. 

        DSS property name: `kWActual`, DSS property index: 22.
        """
        return BatchFloat64ArrayProxy(self, 22)

    @kWActual.setter
    def kWActual(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(22, value)

    @property
    def kWNeed(self) -> BatchFloat64ArrayProxy:
        """
        (Read only). KW needed to meet target.

        DSS property name: `kWNeed`, DSS property index: 23.
        """
        return BatchFloat64ArrayProxy(self, 23)

    @kWNeed.setter
    def kWNeed(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(23, value)

    @property
    def Yearly(self) -> List[str]:
        """
        Dispatch loadshape object, If any, for Yearly solution Mode.

        DSS property name: `Yearly`, DSS property index: 24.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 24)

    @Yearly.setter
    def Yearly(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]):
        self._set_batch_obj_prop(24, value)

    @property
    def Yearly_obj(self) -> List[LoadShape]:
        """
        Dispatch loadshape object, If any, for Yearly solution Mode.

        DSS property name: `Yearly`, DSS property index: 24.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 24)

    @Yearly_obj.setter
    def Yearly_obj(self, value: LoadShape):
        self._set_batch_string(24, value)

    @property
    def Daily(self) -> List[str]:
        """
        Dispatch loadshape object, If any, for Daily solution mode.

        DSS property name: `Daily`, DSS property index: 25.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 25)

    @Daily.setter
    def Daily(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]):
        self._set_batch_obj_prop(25, value)

    @property
    def Daily_obj(self) -> List[LoadShape]:
        """
        Dispatch loadshape object, If any, for Daily solution mode.

        DSS property name: `Daily`, DSS property index: 25.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 25)

    @Daily_obj.setter
    def Daily_obj(self, value: LoadShape):
        self._set_batch_string(25, value)

    @property
    def Duty(self) -> List[str]:
        """
        Dispatch loadshape object, If any, for Dutycycle solution mode.

        DSS property name: `Duty`, DSS property index: 26.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 26)

    @Duty.setter
    def Duty(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]):
        self._set_batch_obj_prop(26, value)

    @property
    def Duty_obj(self) -> List[LoadShape]:
        """
        Dispatch loadshape object, If any, for Dutycycle solution mode.

        DSS property name: `Duty`, DSS property index: 26.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 26)

    @Duty_obj.setter
    def Duty_obj(self, value: LoadShape):
        self._set_batch_string(26, value)

    @property
    def EventLog(self) -> List[bool]:
        """
        {Yes/True | No/False} Default is No. Log control actions to Eventlog.

        DSS property name: `EventLog`, DSS property index: 27.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 27)
        ]
    @EventLog.setter
    def EventLog(self, value: bool):
        self._set_batch_int32_array(27, value)

    @property
    def InhibitTime(self) -> BatchInt32ArrayProxy:
        """
        Hours (integer) to inhibit Discharging after going into Charge mode. Default is 5.

        DSS property name: `InhibitTime`, DSS property index: 28.
        """
        return BatchInt32ArrayProxy(self, 28)

    @InhibitTime.setter
    def InhibitTime(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(28, value)

    @property
    def TUp(self) -> BatchFloat64ArrayProxy:
        """
        Duration, hrs, of upramp part for SCHEDULE mode. Default is 0.25.

        DSS property name: `TUp`, DSS property index: 29.
        """
        return BatchFloat64ArrayProxy(self, 29)

    @TUp.setter
    def TUp(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(29, value)

    @property
    def TFlat(self) -> BatchFloat64ArrayProxy:
        """
        Duration, hrs, of flat part for SCHEDULE mode. Default is 2.0.

        DSS property name: `TFlat`, DSS property index: 30.
        """
        return BatchFloat64ArrayProxy(self, 30)

    @TFlat.setter
    def TFlat(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(30, value)

    @property
    def TDn(self) -> BatchFloat64ArrayProxy:
        """
        Duration, hrs, of downramp part for SCHEDULE mode. Default is 0.25.

        DSS property name: `TDn`, DSS property index: 31.
        """
        return BatchFloat64ArrayProxy(self, 31)

    @TDn.setter
    def TDn(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(31, value)

    @property
    def kWThreshold(self) -> BatchFloat64ArrayProxy:
        """
        Threshold, kW, for Follow mode. kW has to be above this value for the Storage element to be dispatched on. Defaults to 75% of the kWTarget value. Must reset this property after setting kWTarget if you want a different value.

        DSS property name: `kWThreshold`, DSS property index: 32.
        """
        return BatchFloat64ArrayProxy(self, 32)

    @kWThreshold.setter
    def kWThreshold(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(32, value)

    @property
    def DispFactor(self) -> BatchFloat64ArrayProxy:
        """
        Defaults to 1 (disabled). Set to any value between 0 and 1 to enable this parameter.

        Use this parameter to reduce the amount of power requested by the controller in each control iteration. It can be useful when maximum control iterations are exceeded due to numerical instability such as fleet being set to charging and idling in subsequent control iterations (check the Eventlog). 

        DSS property name: `DispFactor`, DSS property index: 33.
        """
        return BatchFloat64ArrayProxy(self, 33)

    @DispFactor.setter
    def DispFactor(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(33, value)

    @property
    def ResetLevel(self) -> BatchFloat64ArrayProxy:
        """
        The level of charge required for allowing the storage to discharge again after reaching the reserve storage level. After reaching this level, the storage control  will not allow the storage device to discharge, forcing the storage to charge. Once the storage reaches this level, the storage will be able to discharge again. This value is a number between 0.2 and 1

        DSS property name: `ResetLevel`, DSS property index: 34.
        """
        return BatchFloat64ArrayProxy(self, 34)

    @ResetLevel.setter
    def ResetLevel(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(34, value)

    @property
    def Seasons(self) -> BatchInt32ArrayProxy:
        """
        With this property the user can specify the number of targets to be used by the controller using the list given at "SeasonTargets"/"SeasonTargetsLow", which can be used to dynamically adjust the storage controller during a QSTS simulation. The default value is 1. This property needs to be defined before defining SeasonTargets/SeasonTargetsLow.

        DSS property name: `Seasons`, DSS property index: 35.
        """
        return BatchInt32ArrayProxy(self, 35)

    @Seasons.setter
    def Seasons(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(35, value)

    @property
    def SeasonTargets(self) -> List[Float64Array]:
        """
        An array of doubles specifying the targets to be used during a QSTS simulation. These targets will take effect only if SeasonRating=true. The number of targets cannot exceed the number of seasons defined at the SeasonSignal.The difference between the targets defined at SeasonTargets and SeasonTargetsLow is that SeasonTargets applies to discharging modes, while SeasonTargetsLow applies to charging modes.

        DSS property name: `SeasonTargets`, DSS property index: 36.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 36)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @SeasonTargets.setter
    def SeasonTargets(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(36, value)

    @property
    def SeasonTargetsLow(self) -> List[Float64Array]:
        """
        An array of doubles specifying the targets to be used during a QSTS simulation. These targets will take effect only if SeasonRating=true. The number of targets cannot exceed the number of seasons defined at the SeasonSignal.The difference between the targets defined at SeasonTargets and SeasonTargetsLow is that SeasonTargets applies to discharging modes, while SeasonTargetsLow applies to charging modes.

        DSS property name: `SeasonTargetsLow`, DSS property index: 37.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 37)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @SeasonTargetsLow.setter
    def SeasonTargetsLow(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(37, value)

    @property
    def BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 38.
        """
        return BatchFloat64ArrayProxy(self, 38)

    @BaseFreq.setter
    def BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(38, value)

    @property
    def Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 39.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 39)
        ]
    @Enabled.setter
    def Enabled(self, value: bool):
        self._set_batch_int32_array(39, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 40.
        """
        self._set_batch_string(40, value)

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

class IStorageController(IDSSObj):
    __slots__ = ()

    def __init__(self, iobj):
        super().__init__(iobj, StorageController, StorageControllerBatch)

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> StorageController:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[StorageControllerProperties]) -> StorageController:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[StorageControllerBatchProperties]) -> StorageControllerBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
