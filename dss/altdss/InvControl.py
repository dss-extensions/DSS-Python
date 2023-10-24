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
from .XYcurve import XYcurve

class InvControl(DSSObj, CktElementMixin):
    __slots__ = CktElementMixin._extra_slots
    _cls_name = 'InvControl'
    _cls_idx = 42
    _cls_prop_idx = {
        'derlist': 1,
        'mode': 2,
        'combimode': 3,
        'vvc_curve1': 4,
        'hysteresis_offset': 5,
        'voltage_curvex_ref': 6,
        'avgwindowlen': 7,
        'voltwatt_curve': 8,
        'dbvmin': 9,
        'dbvmax': 10,
        'argralowv': 11,
        'argrahiv': 12,
        'dynreacavgwindowlen': 13,
        'deltaq_factor': 14,
        'voltagechangetolerance': 15,
        'varchangetolerance': 16,
        'voltwattyaxis': 17,
        'rateofchangemode': 18,
        'lpftau': 19,
        'risefalllimit': 20,
        'deltap_factor': 21,
        'eventlog': 22,
        'refreactivepower': 23,
        'activepchangetolerance': 24,
        'monvoltagecalc': 25,
        'monbus': 26,
        'monbusesvbase': 27,
        'voltwattch_curve': 28,
        'wattpf_curve': 29,
        'wattvar_curve': 30,
        'vv_refreactivepower': 31,
        'pvsystemlist': 32,
        'vsetpoint': 33,
        'controlmodel': 34,
        'basefreq': 35,
        'enabled': 36,
        'like': 37,
    }

    @property
    def DERList(self) -> List[str]:
        """
        Array list of PVSystem and/or Storage elements to be controlled. If not specified, all PVSystem and Storage in the circuit are assumed to be controlled by this control. 

        No capability of hierarchical control between two controls for a single element is implemented at this time.

        DSS property name: `DERList`, DSS property index: 1.
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 1)

    @DERList.setter
    def DERList(self, value: List[AnyStr]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 1, value_ptr, value_count)
        self._check_for_error()

    @property
    def Mode(self) -> enums.InvControlControlMode:
        """
        Smart inverter function in which the InvControl will control the PC elements specified in DERList, according to the options below:

        Must be one of: {VOLTVAR | VOLTWATT | DYNAMICREACCURR | WATTPF | WATTVAR | GFM} 
        if the user desires to use modes simultaneously, then set the CombiMode property. Setting the Mode to any valid value disables combination mode.

        In volt-var mode. This mode attempts to CONTROL the vars, according to one or two volt-var curves, depending on the monitored voltages, present active power output, and the capabilities of the PVSystem/Storage. 

        In volt-watt mode. This mode attempts to LIMIT the watts, according to one defined volt-watt curve, depending on the monitored voltages and the capabilities of the PVSystem/Storage. 

        In dynamic reactive current mode. This mode attempts to increasingly counter deviations by CONTROLLING vars, depending on the monitored voltages, present active power output, and the capabilities of the of the PVSystem/Storage.

        In watt-pf mode. This mode attempts to CONTROL the vars, according to a watt-pf curve, depending on the present active power output, and the capabilities of the PVSystem/Storage. 

        In watt-var mode. This mode attempts to CONTROL the vars, according to a watt-var curve, depending on the present active power output, and the capabilities of the PVSystem/Storage. 

        In GFM mode this control will trigger the GFM control routine for the DERs within the DERList. The GFM actiosn will only take place if the pointed DERs are in GFM mode. The controller parameters are locally setup at the DER.


        NO DEFAULT

        DSS property name: `Mode`, DSS property index: 2.
        """
        return enums.InvControlControlMode(self._lib.Obj_GetInt32(self._ptr, 2))

    @Mode.setter
    def Mode(self, value: Union[AnyStr, int, enums.InvControlControlMode]):
        if not isinstance(value, int):
            self._set_string_o(2, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def Mode_str(self) -> str:
        """
        Smart inverter function in which the InvControl will control the PC elements specified in DERList, according to the options below:

        Must be one of: {VOLTVAR | VOLTWATT | DYNAMICREACCURR | WATTPF | WATTVAR | GFM} 
        if the user desires to use modes simultaneously, then set the CombiMode property. Setting the Mode to any valid value disables combination mode.

        In volt-var mode. This mode attempts to CONTROL the vars, according to one or two volt-var curves, depending on the monitored voltages, present active power output, and the capabilities of the PVSystem/Storage. 

        In volt-watt mode. This mode attempts to LIMIT the watts, according to one defined volt-watt curve, depending on the monitored voltages and the capabilities of the PVSystem/Storage. 

        In dynamic reactive current mode. This mode attempts to increasingly counter deviations by CONTROLLING vars, depending on the monitored voltages, present active power output, and the capabilities of the of the PVSystem/Storage.

        In watt-pf mode. This mode attempts to CONTROL the vars, according to a watt-pf curve, depending on the present active power output, and the capabilities of the PVSystem/Storage. 

        In watt-var mode. This mode attempts to CONTROL the vars, according to a watt-var curve, depending on the present active power output, and the capabilities of the PVSystem/Storage. 

        In GFM mode this control will trigger the GFM control routine for the DERs within the DERList. The GFM actiosn will only take place if the pointed DERs are in GFM mode. The controller parameters are locally setup at the DER.


        NO DEFAULT

        DSS property name: `Mode`, DSS property index: 2.
        """
        return self._get_prop_string(2)

    @Mode_str.setter
    def Mode_str(self, value: AnyStr):
        self.Mode = value

    @property
    def CombiMode(self) -> enums.InvControlCombiMode:
        """
        Combination of smart inverter functions in which the InvControl will control the PC elements in DERList, according to the options below: 

        Must be a combination of the following: {VV_VW | VV_DRC}. Default is to not set this property, in which case the single control mode in Mode is active.  

        In combined VV_VW mode, both volt-var and volt-watt control modes are active simultaneously.  See help individually for volt-var mode and volt-watt mode in Mode property.
        Note that the PVSystem/Storage will attempt to achieve both the volt-watt and volt-var set-points based on the capabilities of the inverter in the PVSystem/Storage (kVA rating, etc), any limits set on maximum active power,

        In combined VV_DRC, both the volt-var and the dynamic reactive current modes are simultaneously active.

        DSS property name: `CombiMode`, DSS property index: 3.
        """
        return enums.InvControlCombiMode(self._lib.Obj_GetInt32(self._ptr, 3))

    @CombiMode.setter
    def CombiMode(self, value: Union[AnyStr, int, enums.InvControlCombiMode]):
        if not isinstance(value, int):
            self._set_string_o(3, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 3, value)

    @property
    def CombiMode_str(self) -> str:
        """
        Combination of smart inverter functions in which the InvControl will control the PC elements in DERList, according to the options below: 

        Must be a combination of the following: {VV_VW | VV_DRC}. Default is to not set this property, in which case the single control mode in Mode is active.  

        In combined VV_VW mode, both volt-var and volt-watt control modes are active simultaneously.  See help individually for volt-var mode and volt-watt mode in Mode property.
        Note that the PVSystem/Storage will attempt to achieve both the volt-watt and volt-var set-points based on the capabilities of the inverter in the PVSystem/Storage (kVA rating, etc), any limits set on maximum active power,

        In combined VV_DRC, both the volt-var and the dynamic reactive current modes are simultaneously active.

        DSS property name: `CombiMode`, DSS property index: 3.
        """
        return self._get_prop_string(3)

    @CombiMode_str.setter
    def CombiMode_str(self, value: AnyStr):
        self.CombiMode = value

    @property
    def VVC_Curve1(self) -> str:
        """
        Required for VOLTVAR mode. 

        Name of the XYCurve object containing the volt-var curve. The positive values of the y-axis of the volt-var curve represent values in pu of the provided base reactive power. The negative values of the y-axis are values in pu of the absorbed base reactive power. 
        Provided and absorbed base reactive power values are defined in the RefReactivePower property

        Units for the x-axis are per-unit voltage, which may be in per unit of the rated voltage for the PVSystem/Storage, or may be in per unit of the average voltage at the terminals over a user-defined number of prior solutions. 

        DSS property name: `VVC_Curve1`, DSS property index: 4.
        """
        return self._get_prop_string(4)

    @VVC_Curve1.setter
    def VVC_Curve1(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(4, value)
            return

        self._set_string_o(4, value)

    @property
    def VVC_Curve1_obj(self) -> XYcurve:
        """
        Required for VOLTVAR mode. 

        Name of the XYCurve object containing the volt-var curve. The positive values of the y-axis of the volt-var curve represent values in pu of the provided base reactive power. The negative values of the y-axis are values in pu of the absorbed base reactive power. 
        Provided and absorbed base reactive power values are defined in the RefReactivePower property

        Units for the x-axis are per-unit voltage, which may be in per unit of the rated voltage for the PVSystem/Storage, or may be in per unit of the average voltage at the terminals over a user-defined number of prior solutions. 

        DSS property name: `VVC_Curve1`, DSS property index: 4.
        """
        return self._get_obj(4, XYcurve)

    @VVC_Curve1_obj.setter
    def VVC_Curve1_obj(self, value: XYcurve):
        self._set_obj(4, value)

    @property
    def Hysteresis_Offset(self) -> float:
        """
        Required for VOLTVAR mode, and defaults to 0. 

        for the times when the terminal voltage is decreasing, this is the off-set in per-unit voltage of a curve whose shape is the same as vvc_curve. It is offset by a certain negative value of per-unit voltage, which is defined by the base quantity for the x-axis of the volt-var curve (see help for voltage_curvex_ref)

        if the PVSystem/Storage terminal voltage has been increasing, and has not changed directions, utilize vvc_curve1 for the volt-var response. 

        if the PVSystem/Storage terminal voltage has been increasing and changes directions and begins to decrease, then move from utilizing vvc_curve1 to a volt-var curve of the same shape, but offset by a certain per-unit voltage value. 

        Maintain the same per-unit available var output level (unless head-room has changed due to change in active power or kva rating of PVSystem/Storage).  Per-unit var values remain the same for this internally constructed second curve (hysteresis curve). 

        if the terminal voltage has been decreasing and changes directions and begins to increase , then move from utilizing the offset curve, back to the vvc_curve1 for volt-var response, but stay at the same per-unit available vars output level.

        DSS property name: `Hysteresis_Offset`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @Hysteresis_Offset.setter
    def Hysteresis_Offset(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def Voltage_CurveX_Ref(self) -> enums.InvControlVoltageCurveXRef:
        """
        Required for VOLTVAR and VOLTWATT modes, and defaults to rated.  Possible values are: {rated|avg|ravg}.  

        Defines whether the x-axis values (voltage in per unit) for vvc_curve1 and the volt-watt curve corresponds to:

        rated. The rated voltage for the PVSystem/Storage object (1.0 in the volt-var curve equals rated voltage).

        avg. The average terminal voltage recorded over a certain number of prior power-flow solutions.
        with the avg setting, 1.0 per unit on the x-axis of the volt-var curve(s) corresponds to the average voltage.
        from a certain number of prior intervals.  See avgwindowlen parameter.

        ravg. Same as avg, with the exception that the avgerage terminal voltage is divided by the rated voltage.

        DSS property name: `Voltage_CurveX_Ref`, DSS property index: 6.
        """
        return enums.InvControlVoltageCurveXRef(self._lib.Obj_GetInt32(self._ptr, 6))

    @Voltage_CurveX_Ref.setter
    def Voltage_CurveX_Ref(self, value: Union[AnyStr, int, enums.InvControlVoltageCurveXRef]):
        if not isinstance(value, int):
            self._set_string_o(6, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 6, value)

    @property
    def Voltage_CurveX_Ref_str(self) -> str:
        """
        Required for VOLTVAR and VOLTWATT modes, and defaults to rated.  Possible values are: {rated|avg|ravg}.  

        Defines whether the x-axis values (voltage in per unit) for vvc_curve1 and the volt-watt curve corresponds to:

        rated. The rated voltage for the PVSystem/Storage object (1.0 in the volt-var curve equals rated voltage).

        avg. The average terminal voltage recorded over a certain number of prior power-flow solutions.
        with the avg setting, 1.0 per unit on the x-axis of the volt-var curve(s) corresponds to the average voltage.
        from a certain number of prior intervals.  See avgwindowlen parameter.

        ravg. Same as avg, with the exception that the avgerage terminal voltage is divided by the rated voltage.

        DSS property name: `Voltage_CurveX_Ref`, DSS property index: 6.
        """
        return self._get_prop_string(6)

    @Voltage_CurveX_Ref_str.setter
    def Voltage_CurveX_Ref_str(self, value: AnyStr):
        self.Voltage_CurveX_Ref = value

    @property
    def AvgWindowLen(self) -> int:
        """
        Required for VOLTVAR mode and VOLTWATT mode, and defaults to 0 seconds (0s). 

        Sets the length of the averaging window over which the average PVSystem/Storage terminal voltage is calculated. 

        Units are indicated by appending s, m, or h to the integer value. 

        The averaging window will calculate the average PVSystem/Storage terminal voltage over the specified period of time, up to and including the last power flow solution. 

        Note, if the solution stepsize is larger than the window length, then the voltage will be assumed to have been constant over the time-frame specified by the window length.

        DSS property name: `AvgWindowLen`, DSS property index: 7.
        """
        return self._lib.Obj_GetInt32(self._ptr, 7)

    @AvgWindowLen.setter
    def AvgWindowLen(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 7, value)

    @property
    def VoltWatt_Curve(self) -> str:
        """
        Required for VOLTWATT mode. 

        Name of the XYCurve object containing the volt-watt curve. 

        Units for the x-axis are per-unit voltage, which may be in per unit of the rated voltage for the PVSystem/Storage, or may be in per unit of the average voltage at the terminals over a user-defined number of prior solutions. 

        Units for the y-axis are either in one of the options described in the VoltwattYAxis property. 

        DSS property name: `VoltWatt_Curve`, DSS property index: 8.
        """
        return self._get_prop_string(8)

    @VoltWatt_Curve.setter
    def VoltWatt_Curve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(8, value)
            return

        self._set_string_o(8, value)

    @property
    def VoltWatt_Curve_obj(self) -> XYcurve:
        """
        Required for VOLTWATT mode. 

        Name of the XYCurve object containing the volt-watt curve. 

        Units for the x-axis are per-unit voltage, which may be in per unit of the rated voltage for the PVSystem/Storage, or may be in per unit of the average voltage at the terminals over a user-defined number of prior solutions. 

        Units for the y-axis are either in one of the options described in the VoltwattYAxis property. 

        DSS property name: `VoltWatt_Curve`, DSS property index: 8.
        """
        return self._get_obj(8, XYcurve)

    @VoltWatt_Curve_obj.setter
    def VoltWatt_Curve_obj(self, value: XYcurve):
        self._set_obj(8, value)

    @property
    def DbVMin(self) -> float:
        """
        Required for the dynamic reactive current mode (DYNAMICREACCURR), and defaults to 0.95 per-unit voltage (referenced to the PVSystem/Storage object rated voltage or a windowed average value). 

        This parameter is the minimum voltage that defines the voltage dead-band within which no reactive power is allowed to be generated. 

        DSS property name: `DbVMin`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @DbVMin.setter
    def DbVMin(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def DbVMax(self) -> float:
        """
        Required for the dynamic reactive current mode (DYNAMICREACCURR), and defaults to 1.05 per-unit voltage (referenced to the PVSystem object rated voltage or a windowed average value). 

        This parameter is the maximum voltage that defines the voltage dead-band within which no reactive power is allowed to be generated. 

        DSS property name: `DbVMax`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @DbVMax.setter
    def DbVMax(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def ArGraLowV(self) -> float:
        """
        Required for the dynamic reactive current mode (DYNAMICREACCURR), and defaults to 0.1  

        This is a gradient, expressed in unit-less terms of %/%, to establish the ratio by which percentage capacitive reactive power production is increased as the  percent delta-voltage decreases below DbVMin. 

        Percent delta-voltage is defined as the present PVSystem/Storage terminal voltage minus the moving average voltage, expressed as a percentage of the rated voltage for the PVSystem/Storage object. 

        Note, the moving average voltage for the dynamic reactive current mode is different than the moving average voltage for the volt-watt and volt-var modes.

        DSS property name: `ArGraLowV`, DSS property index: 11.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @ArGraLowV.setter
    def ArGraLowV(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def ArGraHiV(self) -> float:
        """
        Required for the dynamic reactive current mode (DYNAMICREACCURR), and defaults to 0.1  

        This is a gradient, expressed in unit-less terms of %/%, to establish the ratio by which percentage inductive reactive power production is increased as the  percent delta-voltage decreases above DbVMax. 

        Percent delta-voltage is defined as the present PVSystem/Storage terminal voltage minus the moving average voltage, expressed as a percentage of the rated voltage for the PVSystem/Storage object. 

        Note, the moving average voltage for the dynamic reactive current mode is different than the mmoving average voltage for the volt-watt and volt-var modes.

        DSS property name: `ArGraHiV`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @ArGraHiV.setter
    def ArGraHiV(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def DynReacAvgWindowLen(self) -> int:
        """
        Required for the dynamic reactive current mode (DYNAMICREACCURR), and defaults to 1 seconds (1s). do not use a value smaller than 1.0 

        Sets the length of the averaging window over which the average PVSystem/Storage terminal voltage is calculated for the dynamic reactive current mode. 

        Units are indicated by appending s, m, or h to the integer value. 

        Typically this will be a shorter averaging window than the volt-var and volt-watt averaging window.

        The averaging window will calculate the average PVSystem/Storage terminal voltage over the specified period of time, up to and including the last power flow solution.  Note, if the solution stepsize is larger than the window length, then the voltage will be assumed to have been constant over the time-frame specified by the window length.

        DSS property name: `DynReacAvgWindowLen`, DSS property index: 13.
        """
        return self._lib.Obj_GetInt32(self._ptr, 13)

    @DynReacAvgWindowLen.setter
    def DynReacAvgWindowLen(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 13, value)

    @property
    def DeltaQ_Factor(self) -> float:
        """
        Required for the VOLTVAR and DYNAMICREACCURR modes.  Defaults to -1.0. 

        Defining -1.0, OpenDSS takes care internally of delta_Q itself. It tries to improve convergence as well as speed up process

        Sets the maximum change (in per unit) from the prior var output level to the desired var output level during each control iteration. 


        if numerical instability is noticed in solutions such as var sign changing from one control iteration to the next and voltages oscillating between two values with some separation, this is an indication of numerical instability (use the EventLog to diagnose). 

        if the maximum control iterations are exceeded, and no numerical instability is seen in the EventLog of via monitors, then try increasing the value of this parameter to reduce the number of control iterations needed to achieve the control criteria, and move to the power flow solution. 

        When operating the controller using exponential control model (see CtrlModel), this parameter represents the sampling time gain of the controller, which is used for accelrating the controller response in terms of control iterations required.

        DSS property name: `DeltaQ_Factor`, DSS property index: 14.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @DeltaQ_Factor.setter
    def DeltaQ_Factor(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def VoltageChangeTolerance(self) -> float:
        """
        Defaults to 0.0001 per-unit voltage.  This parameter should only be modified by advanced users of the InvControl.  

        Tolerance in pu of the control loop convergence associated to the monitored voltage in pu. This value is compared with the difference of the monitored voltage in pu of the current and previous control iterations of the control loop

        This voltage tolerance value plus the var/watt tolerance value (VarChangeTolerance/ActivePChangeTolerance) determine, together, when to stop control iterations by the InvControl. 

        If an InvControl is controlling more than one PVSystem/Storage, each PVSystem/Storage has this quantity calculated independently, and so an individual PVSystem/Storage may reach the tolerance within different numbers of control iterations.

        DSS property name: `VoltageChangeTolerance`, DSS property index: 15.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @VoltageChangeTolerance.setter
    def VoltageChangeTolerance(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def VarChangeTolerance(self) -> float:
        """
        Required for VOLTVAR and DYNAMICREACCURR modes.  Defaults to 0.025 per unit of the base provided or absorbed reactive power described in the RefReactivePower property This parameter should only be modified by advanced users of the InvControl. 

        Tolerance in pu of the convergence of the control loop associated with reactive power. For the same control iteration, this value is compared to the difference, as an absolute value (without sign), between the desired reactive power value in pu and the output reactive power in pu of the controlled element.

        This reactive power tolerance value plus the voltage tolerance value (VoltageChangeTolerance) determine, together, when to stop control iterations by the InvControl.  

        If an InvControl is controlling more than one PVSystem/Storage, each PVSystem/Storage has this quantity calculated independently, and so an individual PVSystem/Storage may reach the tolerance within different numbers of control iterations.

        DSS property name: `VarChangeTolerance`, DSS property index: 16.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    @VarChangeTolerance.setter
    def VarChangeTolerance(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 16, value)

    @property
    def VoltWattYAxis(self) -> enums.InvControlVoltWattYAxis:
        """
        Required for VOLTWATT mode.  Must be one of: {PMPPPU* | PAVAILABLEPU| PCTPMPPPU | KVARATINGPU}.  The default is PMPPPU.  

        Units for the y-axis of the volt-watt curve while in volt-watt mode. 

        When set to PMPPPU. The y-axis corresponds to the value in pu of Pmpp property of the PVSystem. 

        When set to PAVAILABLEPU. The y-axis corresponds to the value in pu of the available active power of the PVSystem. 

        When set to PCTPMPPPU. The y-axis corresponds to the value in pu of the power Pmpp multiplied by 1/100 of the %Pmpp property of the PVSystem.

        When set to KVARATINGPU. The y-axis corresponds to the value in pu of the kVA property of the PVSystem.

        DSS property name: `VoltWattYAxis`, DSS property index: 17.
        """
        return enums.InvControlVoltWattYAxis(self._lib.Obj_GetInt32(self._ptr, 17))

    @VoltWattYAxis.setter
    def VoltWattYAxis(self, value: Union[AnyStr, int, enums.InvControlVoltWattYAxis]):
        if not isinstance(value, int):
            self._set_string_o(17, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 17, value)

    @property
    def VoltWattYAxis_str(self) -> str:
        """
        Required for VOLTWATT mode.  Must be one of: {PMPPPU* | PAVAILABLEPU| PCTPMPPPU | KVARATINGPU}.  The default is PMPPPU.  

        Units for the y-axis of the volt-watt curve while in volt-watt mode. 

        When set to PMPPPU. The y-axis corresponds to the value in pu of Pmpp property of the PVSystem. 

        When set to PAVAILABLEPU. The y-axis corresponds to the value in pu of the available active power of the PVSystem. 

        When set to PCTPMPPPU. The y-axis corresponds to the value in pu of the power Pmpp multiplied by 1/100 of the %Pmpp property of the PVSystem.

        When set to KVARATINGPU. The y-axis corresponds to the value in pu of the kVA property of the PVSystem.

        DSS property name: `VoltWattYAxis`, DSS property index: 17.
        """
        return self._get_prop_string(17)

    @VoltWattYAxis_str.setter
    def VoltWattYAxis_str(self, value: AnyStr):
        self.VoltWattYAxis = value

    @property
    def RateOfChangeMode(self) -> enums.InvControlRateOfChangeMode:
        """
        Required for VOLTWATT and VOLTVAR mode.  Must be one of: {INACTIVE* | LPF | RISEFALL }.  The default is INACTIVE.  

        Auxiliary option that aims to limit the changes of the desired reactive power and the active power limit between time steps, the alternatives are listed below: 

        INACTIVE. It indicates there is no limit on rate of change imposed for either active or reactive power output. 

        LPF. A low-pass RC filter is applied to the desired reactive power and/or the active power limit to determine the output power as a function of a time constant defined in the LPFTau property. 

        RISEFALL. A rise and fall limit in the change of active and/or reactive power expressed in terms of pu power per second, defined in the RiseFallLimit, is applied to the desired reactive power and/or the active power limit. 

        DSS property name: `RateOfChangeMode`, DSS property index: 18.
        """
        return enums.InvControlRateOfChangeMode(self._lib.Obj_GetInt32(self._ptr, 18))

    @RateOfChangeMode.setter
    def RateOfChangeMode(self, value: Union[AnyStr, int, enums.InvControlRateOfChangeMode]):
        if not isinstance(value, int):
            self._set_string_o(18, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 18, value)

    @property
    def RateOfChangeMode_str(self) -> str:
        """
        Required for VOLTWATT and VOLTVAR mode.  Must be one of: {INACTIVE* | LPF | RISEFALL }.  The default is INACTIVE.  

        Auxiliary option that aims to limit the changes of the desired reactive power and the active power limit between time steps, the alternatives are listed below: 

        INACTIVE. It indicates there is no limit on rate of change imposed for either active or reactive power output. 

        LPF. A low-pass RC filter is applied to the desired reactive power and/or the active power limit to determine the output power as a function of a time constant defined in the LPFTau property. 

        RISEFALL. A rise and fall limit in the change of active and/or reactive power expressed in terms of pu power per second, defined in the RiseFallLimit, is applied to the desired reactive power and/or the active power limit. 

        DSS property name: `RateOfChangeMode`, DSS property index: 18.
        """
        return self._get_prop_string(18)

    @RateOfChangeMode_str.setter
    def RateOfChangeMode_str(self, value: AnyStr):
        self.RateOfChangeMode = value

    @property
    def LPFTau(self) -> float:
        """
        Not required. Defaults to 0 seconds. 

        Filter time constant of the LPF option of the RateofChangeMode property. The time constant will cause the low-pass filter to achieve 95% of the target value in 3 time constants.

        DSS property name: `LPFTau`, DSS property index: 19.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    @LPFTau.setter
    def LPFTau(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 19, value)

    @property
    def RiseFallLimit(self) -> float:
        """
        Not required.  Defaults to no limit (-1). Must be -1 (no limit) or a positive value.  

        Limit in power in pu per second used by the RISEFALL option of the RateofChangeMode property.The base value for this ramp is defined in the RefReactivePower property and/or in VoltwattYAxis.

        DSS property name: `RiseFallLimit`, DSS property index: 20.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    @RiseFallLimit.setter
    def RiseFallLimit(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 20, value)

    @property
    def DeltaP_Factor(self) -> float:
        """
        Required for the VOLTWATT modes.  Defaults to -1.0. 

        Defining -1.0, OpenDSS takes care internally of delta_P itself. It tries to improve convergence as well as speed up process

        Defining between 0.05 and 1.0, it sets the maximum change (in unit of the y-axis) from the prior active power output level to the desired active power output level during each control iteration. 


        If numerical instability is noticed in solutions such as active power changing substantially from one control iteration to the next and/or voltages oscillating between two values with some separation, this is an indication of numerical instability (use the EventLog to diagnose). 

        If the maximum control iterations are exceeded, and no numerical instability is seen in the EventLog of via monitors, then try increasing the value of this parameter to reduce the number of control iterations needed to achieve the control criteria, and move to the power flow solution.

        DSS property name: `DeltaP_Factor`, DSS property index: 21.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @DeltaP_Factor.setter
    def DeltaP_Factor(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    @property
    def EventLog(self) -> bool:
        """
        {Yes/True | No/False*} Default is NO for InvControl. Log control actions to Eventlog.

        DSS property name: `EventLog`, DSS property index: 22.
        """
        return self._lib.Obj_GetInt32(self._ptr, 22) != 0

    @EventLog.setter
    def EventLog(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 22, value)

    @property
    def RefReactivePower(self) -> enums.InvControlReactivePowerReference:
        """
        Required for any mode that has VOLTVAR, DYNAMICREACCURR and WATTVAR. Defaults to VARAVAL.

        Defines the base reactive power for both the provided and absorbed reactive power, according to one of the following options: 

        VARAVAL. The base values for the provided and absorbed reactive power are equal to the available reactive power.

        VARMAX: The base values of the provided and absorbed reactive power are equal to the value defined in the kvarMax and kvarMaxAbs properties, respectively.

        DSS property name: `RefReactivePower`, DSS property index: 23.
        """
        return enums.InvControlReactivePowerReference(self._lib.Obj_GetInt32(self._ptr, 23))

    @RefReactivePower.setter
    def RefReactivePower(self, value: Union[AnyStr, int, enums.InvControlReactivePowerReference]):
        if not isinstance(value, int):
            self._set_string_o(23, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 23, value)

    @property
    def RefReactivePower_str(self) -> str:
        """
        Required for any mode that has VOLTVAR, DYNAMICREACCURR and WATTVAR. Defaults to VARAVAL.

        Defines the base reactive power for both the provided and absorbed reactive power, according to one of the following options: 

        VARAVAL. The base values for the provided and absorbed reactive power are equal to the available reactive power.

        VARMAX: The base values of the provided and absorbed reactive power are equal to the value defined in the kvarMax and kvarMaxAbs properties, respectively.

        DSS property name: `RefReactivePower`, DSS property index: 23.
        """
        return self._get_prop_string(23)

    @RefReactivePower_str.setter
    def RefReactivePower_str(self, value: AnyStr):
        self.RefReactivePower = value

    @property
    def ActivePChangeTolerance(self) -> float:
        """
        Required for VOLTWATT. Default is 0.01

        Tolerance in pu of the convergence of the control loop associated with active power. For the same control iteration, this value is compared to the difference between the active power limit in pu resulted from the convergence process and the one resulted from the volt-watt function.

        This reactive power tolerance value plus the voltage tolerance value (VoltageChangeTolerance) determine, together, when to stop control iterations by the InvControl.  

        If an InvControl is controlling more than one PVSystem/Storage, each PVSystem/Storage has this quantity calculated independently, and so an individual PVSystem/Storage may reach the tolerance within different numbers of control iterations.

        DSS property name: `ActivePChangeTolerance`, DSS property index: 24.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    @ActivePChangeTolerance.setter
    def ActivePChangeTolerance(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 24, value)

    @property
    def MonVoltageCalc(self) -> Union[enums.MonitoredPhase, int]:
        """
        Number of the phase being monitored or one of {AVG | MAX | MIN} for all phases. Default=AVG. 

        DSS property name: `MonVoltageCalc`, DSS property index: 25.
        """
        value = self._lib.Obj_GetInt32(self._ptr, 25)
        if value > 0:
            return value
    
        return enums.MonitoredPhase(value)

    @MonVoltageCalc.setter
    def MonVoltageCalc(self, value: Union[AnyStr, int, enums.MonitoredPhase]):
        if not isinstance(value, int):
            self._set_string_o(25, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 25, value)

    @property
    def MonVoltageCalc_str(self) -> str:
        """
        Number of the phase being monitored or one of {AVG | MAX | MIN} for all phases. Default=AVG. 

        DSS property name: `MonVoltageCalc`, DSS property index: 25.
        """
        return self._get_prop_string(25)

    @MonVoltageCalc_str.setter
    def MonVoltageCalc_str(self, value: AnyStr):
        self.MonVoltageCalc = value

    @property
    def MonBus(self) -> List[str]:
        """
        Name of monitored bus used by the voltage-dependent control modes. Default is bus of the controlled PVSystem/Storage or Storage.

        DSS property name: `MonBus`, DSS property index: 26.
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 26)

    @MonBus.setter
    def MonBus(self, value: List[AnyStr]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 26, value_ptr, value_count)
        self._check_for_error()

    @property
    def MonBusesVBase(self) -> Float64Array:
        """
        Array list of rated voltages of the buses and their nodes presented in the monBus property. This list may have different line-to-line and/or line-to-ground voltages.

        DSS property name: `MonBusesVBase`, DSS property index: 27.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 27)

    @MonBusesVBase.setter
    def MonBusesVBase(self, value: Float64Array):
        self._set_float64_array_o(27, value)

    @property
    def VoltWattCH_Curve(self) -> str:
        """
        Required for VOLTWATT mode for Storage element in CHARGING state. 

        The name of an XYCurve object that describes the variation in active power output (in per unit of maximum active power output for the Storage). 

        Units for the x-axis are per-unit voltage, which may be in per unit of the rated voltage for the Storage, or may be in per unit of the average voltage at the terminals over a user-defined number of prior solutions. 

        Units for the y-axis are either in: (1) per unit of maximum active power output capability of the Storage, or (2) maximum available active power output capability (defined by the parameter: VoltwattYAxis), corresponding to the terminal voltage (x-axis value in per unit). 

        No default -- must be specified for VOLTWATT mode for Storage element in CHARGING state.

        DSS property name: `VoltWattCH_Curve`, DSS property index: 28.
        """
        return self._get_prop_string(28)

    @VoltWattCH_Curve.setter
    def VoltWattCH_Curve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(28, value)
            return

        self._set_string_o(28, value)

    @property
    def VoltWattCH_Curve_obj(self) -> XYcurve:
        """
        Required for VOLTWATT mode for Storage element in CHARGING state. 

        The name of an XYCurve object that describes the variation in active power output (in per unit of maximum active power output for the Storage). 

        Units for the x-axis are per-unit voltage, which may be in per unit of the rated voltage for the Storage, or may be in per unit of the average voltage at the terminals over a user-defined number of prior solutions. 

        Units for the y-axis are either in: (1) per unit of maximum active power output capability of the Storage, or (2) maximum available active power output capability (defined by the parameter: VoltwattYAxis), corresponding to the terminal voltage (x-axis value in per unit). 

        No default -- must be specified for VOLTWATT mode for Storage element in CHARGING state.

        DSS property name: `VoltWattCH_Curve`, DSS property index: 28.
        """
        return self._get_obj(28, XYcurve)

    @VoltWattCH_Curve_obj.setter
    def VoltWattCH_Curve_obj(self, value: XYcurve):
        self._set_obj(28, value)

    @property
    def WattPF_Curve(self) -> str:
        """
        Required for WATTPF mode.

        Name of the XYCurve object containing the watt-pf curve.
        The positive values of the y-axis are positive power factor values. The negative values of the the y-axis are negative power factor values. When positive, the output reactive power has the same direction of the output active power, and when negative, it has the opposite direction.
        Units for the x-axis are per-unit output active power, and the base active power is the Pmpp for PVSystem and kWrated for Storage.

        The y-axis represents the power factor and the reference is power factor equal to 0. 

        For example, if the user wants to define the following XY coordinates: (0, 0.9); (0.2, 0.9); (0.5, -0.9); (1, -0.9).
        Try to plot them considering the y-axis reference equal to unity power factor.

        The user needs to translate this curve into a plot in which the y-axis reference is equal to 0 power factor.It means that two new XY coordinates need to be included, in this case they are: (0.35, 1); (0.35, -1).
        Try to plot them considering the y-axis reference equal to 0 power factor.
        The discontinuity in 0.35pu is not a problem since var is zero for either power factor equal to 1 or -1.

        DSS property name: `WattPF_Curve`, DSS property index: 29.
        """
        return self._get_prop_string(29)

    @WattPF_Curve.setter
    def WattPF_Curve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(29, value)
            return

        self._set_string_o(29, value)

    @property
    def WattPF_Curve_obj(self) -> XYcurve:
        """
        Required for WATTPF mode.

        Name of the XYCurve object containing the watt-pf curve.
        The positive values of the y-axis are positive power factor values. The negative values of the the y-axis are negative power factor values. When positive, the output reactive power has the same direction of the output active power, and when negative, it has the opposite direction.
        Units for the x-axis are per-unit output active power, and the base active power is the Pmpp for PVSystem and kWrated for Storage.

        The y-axis represents the power factor and the reference is power factor equal to 0. 

        For example, if the user wants to define the following XY coordinates: (0, 0.9); (0.2, 0.9); (0.5, -0.9); (1, -0.9).
        Try to plot them considering the y-axis reference equal to unity power factor.

        The user needs to translate this curve into a plot in which the y-axis reference is equal to 0 power factor.It means that two new XY coordinates need to be included, in this case they are: (0.35, 1); (0.35, -1).
        Try to plot them considering the y-axis reference equal to 0 power factor.
        The discontinuity in 0.35pu is not a problem since var is zero for either power factor equal to 1 or -1.

        DSS property name: `WattPF_Curve`, DSS property index: 29.
        """
        return self._get_obj(29, XYcurve)

    @WattPF_Curve_obj.setter
    def WattPF_Curve_obj(self, value: XYcurve):
        self._set_obj(29, value)

    @property
    def WattVar_Curve(self) -> str:
        """
        Required for WATTVAR mode. 

        Name of the XYCurve object containing the watt-var curve. The positive values of the y-axis of the watt-var curve represent values in pu of the provided base reactive power. The negative values of the y-axis are values in pu of the absorbed base reactive power. 
        Provided and absorbed base reactive power values are defined in the RefReactivePower property.

        Units for the x-axis are per-unit output active power, and the base active power is the Pmpp for PVSystem and kWrated for Storage.

        DSS property name: `WattVar_Curve`, DSS property index: 30.
        """
        return self._get_prop_string(30)

    @WattVar_Curve.setter
    def WattVar_Curve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(30, value)
            return

        self._set_string_o(30, value)

    @property
    def WattVar_Curve_obj(self) -> XYcurve:
        """
        Required for WATTVAR mode. 

        Name of the XYCurve object containing the watt-var curve. The positive values of the y-axis of the watt-var curve represent values in pu of the provided base reactive power. The negative values of the y-axis are values in pu of the absorbed base reactive power. 
        Provided and absorbed base reactive power values are defined in the RefReactivePower property.

        Units for the x-axis are per-unit output active power, and the base active power is the Pmpp for PVSystem and kWrated for Storage.

        DSS property name: `WattVar_Curve`, DSS property index: 30.
        """
        return self._get_obj(30, XYcurve)

    @WattVar_Curve_obj.setter
    def WattVar_Curve_obj(self, value: XYcurve):
        self._set_obj(30, value)

    @property
    def VSetPoint(self) -> float:
        """
        Required for Active Voltage Regulation (AVR).

        DSS property name: `VSetPoint`, DSS property index: 33.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 33)

    @VSetPoint.setter
    def VSetPoint(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 33, value)

    @property
    def ControlModel(self) -> enums.InvControlControlModel:
        """
        Integer defining the method for moving across the control curve. It can be one of the following:

        0 = Linear mode (default)
        1 = Exponential

        Use this property for better tunning your controller and improve the controller response in terms of control iterations needed to reach the target.
        This property alters the meaning of deltaQ_factor and deltaP_factor properties according to its value (Check help). The method can also be combined with the controller tolerance for improving performance.

        DSS property name: `ControlModel`, DSS property index: 34.
        """
        return enums.InvControlControlModel(self._lib.Obj_GetInt32(self._ptr, 34))

    @ControlModel.setter
    def ControlModel(self, value: Union[int, enums.InvControlControlModel]):
        self._lib.Obj_SetInt32(self._ptr, 34, value)

    @property
    def BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 35.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 35)

    @BaseFreq.setter
    def BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 35, value)

    @property
    def Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 36.
        """
        return self._lib.Obj_GetInt32(self._ptr, 36) != 0

    @Enabled.setter
    def Enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 36, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 37.
        """
        self._set_string_o(37, value)


class InvControlProperties(TypedDict):
    DERList: List[AnyStr]
    Mode: Union[AnyStr, int, enums.InvControlControlMode]
    CombiMode: Union[AnyStr, int, enums.InvControlCombiMode]
    VVC_Curve1: Union[AnyStr, XYcurve]
    Hysteresis_Offset: float
    Voltage_CurveX_Ref: Union[AnyStr, int, enums.InvControlVoltageCurveXRef]
    AvgWindowLen: int
    VoltWatt_Curve: Union[AnyStr, XYcurve]
    DbVMin: float
    DbVMax: float
    ArGraLowV: float
    ArGraHiV: float
    DynReacAvgWindowLen: int
    DeltaQ_Factor: float
    VoltageChangeTolerance: float
    VarChangeTolerance: float
    VoltWattYAxis: Union[AnyStr, int, enums.InvControlVoltWattYAxis]
    RateOfChangeMode: Union[AnyStr, int, enums.InvControlRateOfChangeMode]
    LPFTau: float
    RiseFallLimit: float
    DeltaP_Factor: float
    EventLog: bool
    RefReactivePower: Union[AnyStr, int, enums.InvControlReactivePowerReference]
    ActivePChangeTolerance: float
    MonVoltageCalc: Union[AnyStr, int, enums.MonitoredPhase]
    MonBus: List[AnyStr]
    MonBusesVBase: Float64Array
    VoltWattCH_Curve: Union[AnyStr, XYcurve]
    WattPF_Curve: Union[AnyStr, XYcurve]
    WattVar_Curve: Union[AnyStr, XYcurve]
    VSetPoint: float
    ControlModel: Union[int, enums.InvControlControlModel]
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class InvControlBatch(DSSBatch):
    _cls_name = 'InvControl'
    _obj_cls = InvControl
    _cls_idx = 42


    @property
    def DERList(self) -> List[List[str]]:
        """
        Array list of PVSystem and/or Storage elements to be controlled. If not specified, all PVSystem and Storage in the circuit are assumed to be controlled by this control. 

        No capability of hierarchical control between two controls for a single element is implemented at this time.

        DSS property name: `DERList`, DSS property index: 1.
        """
        return self._get_string_ll(1)

    @DERList.setter
    def DERList(self, value: List[AnyStr]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._unpack():
            self._lib.Obj_SetStringArray(x, 1, value_ptr, value_count)
    
        self._check_for_error()

    @property
    def Mode(self) -> BatchInt32ArrayProxy:
        """
        Smart inverter function in which the InvControl will control the PC elements specified in DERList, according to the options below:

        Must be one of: {VOLTVAR | VOLTWATT | DYNAMICREACCURR | WATTPF | WATTVAR | GFM} 
        if the user desires to use modes simultaneously, then set the CombiMode property. Setting the Mode to any valid value disables combination mode.

        In volt-var mode. This mode attempts to CONTROL the vars, according to one or two volt-var curves, depending on the monitored voltages, present active power output, and the capabilities of the PVSystem/Storage. 

        In volt-watt mode. This mode attempts to LIMIT the watts, according to one defined volt-watt curve, depending on the monitored voltages and the capabilities of the PVSystem/Storage. 

        In dynamic reactive current mode. This mode attempts to increasingly counter deviations by CONTROLLING vars, depending on the monitored voltages, present active power output, and the capabilities of the of the PVSystem/Storage.

        In watt-pf mode. This mode attempts to CONTROL the vars, according to a watt-pf curve, depending on the present active power output, and the capabilities of the PVSystem/Storage. 

        In watt-var mode. This mode attempts to CONTROL the vars, according to a watt-var curve, depending on the present active power output, and the capabilities of the PVSystem/Storage. 

        In GFM mode this control will trigger the GFM control routine for the DERs within the DERList. The GFM actiosn will only take place if the pointed DERs are in GFM mode. The controller parameters are locally setup at the DER.


        NO DEFAULT

        DSS property name: `Mode`, DSS property index: 2.
        """
        return BatchInt32ArrayProxy(self, 2)

    @Mode.setter
    def Mode(self, value: Union[AnyStr, int, enums.InvControlControlMode, List[AnyStr], List[int], List[enums.InvControlControlMode], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(2, value)
            return
    
        self._set_batch_int32_array(2, value)

    @property
    def Mode_str(self) -> str:
        """
        Smart inverter function in which the InvControl will control the PC elements specified in DERList, according to the options below:

        Must be one of: {VOLTVAR | VOLTWATT | DYNAMICREACCURR | WATTPF | WATTVAR | GFM} 
        if the user desires to use modes simultaneously, then set the CombiMode property. Setting the Mode to any valid value disables combination mode.

        In volt-var mode. This mode attempts to CONTROL the vars, according to one or two volt-var curves, depending on the monitored voltages, present active power output, and the capabilities of the PVSystem/Storage. 

        In volt-watt mode. This mode attempts to LIMIT the watts, according to one defined volt-watt curve, depending on the monitored voltages and the capabilities of the PVSystem/Storage. 

        In dynamic reactive current mode. This mode attempts to increasingly counter deviations by CONTROLLING vars, depending on the monitored voltages, present active power output, and the capabilities of the of the PVSystem/Storage.

        In watt-pf mode. This mode attempts to CONTROL the vars, according to a watt-pf curve, depending on the present active power output, and the capabilities of the PVSystem/Storage. 

        In watt-var mode. This mode attempts to CONTROL the vars, according to a watt-var curve, depending on the present active power output, and the capabilities of the PVSystem/Storage. 

        In GFM mode this control will trigger the GFM control routine for the DERs within the DERList. The GFM actiosn will only take place if the pointed DERs are in GFM mode. The controller parameters are locally setup at the DER.


        NO DEFAULT

        DSS property name: `Mode`, DSS property index: 2.
        """
        return self._get_batch_str_prop(2)

    @Mode_str.setter
    def Mode_str(self, value: AnyStr):
        self.Mode = value

    @property
    def CombiMode(self) -> BatchInt32ArrayProxy:
        """
        Combination of smart inverter functions in which the InvControl will control the PC elements in DERList, according to the options below: 

        Must be a combination of the following: {VV_VW | VV_DRC}. Default is to not set this property, in which case the single control mode in Mode is active.  

        In combined VV_VW mode, both volt-var and volt-watt control modes are active simultaneously.  See help individually for volt-var mode and volt-watt mode in Mode property.
        Note that the PVSystem/Storage will attempt to achieve both the volt-watt and volt-var set-points based on the capabilities of the inverter in the PVSystem/Storage (kVA rating, etc), any limits set on maximum active power,

        In combined VV_DRC, both the volt-var and the dynamic reactive current modes are simultaneously active.

        DSS property name: `CombiMode`, DSS property index: 3.
        """
        return BatchInt32ArrayProxy(self, 3)

    @CombiMode.setter
    def CombiMode(self, value: Union[AnyStr, int, enums.InvControlCombiMode, List[AnyStr], List[int], List[enums.InvControlCombiMode], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(3, value)
            return
    
        self._set_batch_int32_array(3, value)

    @property
    def CombiMode_str(self) -> str:
        """
        Combination of smart inverter functions in which the InvControl will control the PC elements in DERList, according to the options below: 

        Must be a combination of the following: {VV_VW | VV_DRC}. Default is to not set this property, in which case the single control mode in Mode is active.  

        In combined VV_VW mode, both volt-var and volt-watt control modes are active simultaneously.  See help individually for volt-var mode and volt-watt mode in Mode property.
        Note that the PVSystem/Storage will attempt to achieve both the volt-watt and volt-var set-points based on the capabilities of the inverter in the PVSystem/Storage (kVA rating, etc), any limits set on maximum active power,

        In combined VV_DRC, both the volt-var and the dynamic reactive current modes are simultaneously active.

        DSS property name: `CombiMode`, DSS property index: 3.
        """
        return self._get_batch_str_prop(3)

    @CombiMode_str.setter
    def CombiMode_str(self, value: AnyStr):
        self.CombiMode = value

    @property
    def VVC_Curve1(self) -> List[str]:
        """
        Required for VOLTVAR mode. 

        Name of the XYCurve object containing the volt-var curve. The positive values of the y-axis of the volt-var curve represent values in pu of the provided base reactive power. The negative values of the y-axis are values in pu of the absorbed base reactive power. 
        Provided and absorbed base reactive power values are defined in the RefReactivePower property

        Units for the x-axis are per-unit voltage, which may be in per unit of the rated voltage for the PVSystem/Storage, or may be in per unit of the average voltage at the terminals over a user-defined number of prior solutions. 

        DSS property name: `VVC_Curve1`, DSS property index: 4.
        """
        return self._get_batch_str_prop(4)

    @VVC_Curve1.setter
    def VVC_Curve1(self, value: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]):
        self._set_batch_obj_prop(4, value)

    @property
    def VVC_Curve1_obj(self) -> List[XYcurve]:
        """
        Required for VOLTVAR mode. 

        Name of the XYCurve object containing the volt-var curve. The positive values of the y-axis of the volt-var curve represent values in pu of the provided base reactive power. The negative values of the y-axis are values in pu of the absorbed base reactive power. 
        Provided and absorbed base reactive power values are defined in the RefReactivePower property

        Units for the x-axis are per-unit voltage, which may be in per unit of the rated voltage for the PVSystem/Storage, or may be in per unit of the average voltage at the terminals over a user-defined number of prior solutions. 

        DSS property name: `VVC_Curve1`, DSS property index: 4.
        """
        return self._get_batch_obj_prop(4)

    @VVC_Curve1_obj.setter
    def VVC_Curve1_obj(self, value: XYcurve):
        self._set_batch_string(4, value)

    @property
    def Hysteresis_Offset(self) -> BatchFloat64ArrayProxy:
        """
        Required for VOLTVAR mode, and defaults to 0. 

        for the times when the terminal voltage is decreasing, this is the off-set in per-unit voltage of a curve whose shape is the same as vvc_curve. It is offset by a certain negative value of per-unit voltage, which is defined by the base quantity for the x-axis of the volt-var curve (see help for voltage_curvex_ref)

        if the PVSystem/Storage terminal voltage has been increasing, and has not changed directions, utilize vvc_curve1 for the volt-var response. 

        if the PVSystem/Storage terminal voltage has been increasing and changes directions and begins to decrease, then move from utilizing vvc_curve1 to a volt-var curve of the same shape, but offset by a certain per-unit voltage value. 

        Maintain the same per-unit available var output level (unless head-room has changed due to change in active power or kva rating of PVSystem/Storage).  Per-unit var values remain the same for this internally constructed second curve (hysteresis curve). 

        if the terminal voltage has been decreasing and changes directions and begins to increase , then move from utilizing the offset curve, back to the vvc_curve1 for volt-var response, but stay at the same per-unit available vars output level.

        DSS property name: `Hysteresis_Offset`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    @Hysteresis_Offset.setter
    def Hysteresis_Offset(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(5, value)

    @property
    def Voltage_CurveX_Ref(self) -> BatchInt32ArrayProxy:
        """
        Required for VOLTVAR and VOLTWATT modes, and defaults to rated.  Possible values are: {rated|avg|ravg}.  

        Defines whether the x-axis values (voltage in per unit) for vvc_curve1 and the volt-watt curve corresponds to:

        rated. The rated voltage for the PVSystem/Storage object (1.0 in the volt-var curve equals rated voltage).

        avg. The average terminal voltage recorded over a certain number of prior power-flow solutions.
        with the avg setting, 1.0 per unit on the x-axis of the volt-var curve(s) corresponds to the average voltage.
        from a certain number of prior intervals.  See avgwindowlen parameter.

        ravg. Same as avg, with the exception that the avgerage terminal voltage is divided by the rated voltage.

        DSS property name: `Voltage_CurveX_Ref`, DSS property index: 6.
        """
        return BatchInt32ArrayProxy(self, 6)

    @Voltage_CurveX_Ref.setter
    def Voltage_CurveX_Ref(self, value: Union[AnyStr, int, enums.InvControlVoltageCurveXRef, List[AnyStr], List[int], List[enums.InvControlVoltageCurveXRef], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(6, value)
            return
    
        self._set_batch_int32_array(6, value)

    @property
    def Voltage_CurveX_Ref_str(self) -> str:
        """
        Required for VOLTVAR and VOLTWATT modes, and defaults to rated.  Possible values are: {rated|avg|ravg}.  

        Defines whether the x-axis values (voltage in per unit) for vvc_curve1 and the volt-watt curve corresponds to:

        rated. The rated voltage for the PVSystem/Storage object (1.0 in the volt-var curve equals rated voltage).

        avg. The average terminal voltage recorded over a certain number of prior power-flow solutions.
        with the avg setting, 1.0 per unit on the x-axis of the volt-var curve(s) corresponds to the average voltage.
        from a certain number of prior intervals.  See avgwindowlen parameter.

        ravg. Same as avg, with the exception that the avgerage terminal voltage is divided by the rated voltage.

        DSS property name: `Voltage_CurveX_Ref`, DSS property index: 6.
        """
        return self._get_batch_str_prop(6)

    @Voltage_CurveX_Ref_str.setter
    def Voltage_CurveX_Ref_str(self, value: AnyStr):
        self.Voltage_CurveX_Ref = value

    @property
    def AvgWindowLen(self) -> BatchInt32ArrayProxy:
        """
        Required for VOLTVAR mode and VOLTWATT mode, and defaults to 0 seconds (0s). 

        Sets the length of the averaging window over which the average PVSystem/Storage terminal voltage is calculated. 

        Units are indicated by appending s, m, or h to the integer value. 

        The averaging window will calculate the average PVSystem/Storage terminal voltage over the specified period of time, up to and including the last power flow solution. 

        Note, if the solution stepsize is larger than the window length, then the voltage will be assumed to have been constant over the time-frame specified by the window length.

        DSS property name: `AvgWindowLen`, DSS property index: 7.
        """
        return BatchInt32ArrayProxy(self, 7)

    @AvgWindowLen.setter
    def AvgWindowLen(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(7, value)

    @property
    def VoltWatt_Curve(self) -> List[str]:
        """
        Required for VOLTWATT mode. 

        Name of the XYCurve object containing the volt-watt curve. 

        Units for the x-axis are per-unit voltage, which may be in per unit of the rated voltage for the PVSystem/Storage, or may be in per unit of the average voltage at the terminals over a user-defined number of prior solutions. 

        Units for the y-axis are either in one of the options described in the VoltwattYAxis property. 

        DSS property name: `VoltWatt_Curve`, DSS property index: 8.
        """
        return self._get_batch_str_prop(8)

    @VoltWatt_Curve.setter
    def VoltWatt_Curve(self, value: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]):
        self._set_batch_obj_prop(8, value)

    @property
    def VoltWatt_Curve_obj(self) -> List[XYcurve]:
        """
        Required for VOLTWATT mode. 

        Name of the XYCurve object containing the volt-watt curve. 

        Units for the x-axis are per-unit voltage, which may be in per unit of the rated voltage for the PVSystem/Storage, or may be in per unit of the average voltage at the terminals over a user-defined number of prior solutions. 

        Units for the y-axis are either in one of the options described in the VoltwattYAxis property. 

        DSS property name: `VoltWatt_Curve`, DSS property index: 8.
        """
        return self._get_batch_obj_prop(8)

    @VoltWatt_Curve_obj.setter
    def VoltWatt_Curve_obj(self, value: XYcurve):
        self._set_batch_string(8, value)

    @property
    def DbVMin(self) -> BatchFloat64ArrayProxy:
        """
        Required for the dynamic reactive current mode (DYNAMICREACCURR), and defaults to 0.95 per-unit voltage (referenced to the PVSystem/Storage object rated voltage or a windowed average value). 

        This parameter is the minimum voltage that defines the voltage dead-band within which no reactive power is allowed to be generated. 

        DSS property name: `DbVMin`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    @DbVMin.setter
    def DbVMin(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(9, value)

    @property
    def DbVMax(self) -> BatchFloat64ArrayProxy:
        """
        Required for the dynamic reactive current mode (DYNAMICREACCURR), and defaults to 1.05 per-unit voltage (referenced to the PVSystem object rated voltage or a windowed average value). 

        This parameter is the maximum voltage that defines the voltage dead-band within which no reactive power is allowed to be generated. 

        DSS property name: `DbVMax`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    @DbVMax.setter
    def DbVMax(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(10, value)

    @property
    def ArGraLowV(self) -> BatchFloat64ArrayProxy:
        """
        Required for the dynamic reactive current mode (DYNAMICREACCURR), and defaults to 0.1  

        This is a gradient, expressed in unit-less terms of %/%, to establish the ratio by which percentage capacitive reactive power production is increased as the  percent delta-voltage decreases below DbVMin. 

        Percent delta-voltage is defined as the present PVSystem/Storage terminal voltage minus the moving average voltage, expressed as a percentage of the rated voltage for the PVSystem/Storage object. 

        Note, the moving average voltage for the dynamic reactive current mode is different than the moving average voltage for the volt-watt and volt-var modes.

        DSS property name: `ArGraLowV`, DSS property index: 11.
        """
        return BatchFloat64ArrayProxy(self, 11)

    @ArGraLowV.setter
    def ArGraLowV(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(11, value)

    @property
    def ArGraHiV(self) -> BatchFloat64ArrayProxy:
        """
        Required for the dynamic reactive current mode (DYNAMICREACCURR), and defaults to 0.1  

        This is a gradient, expressed in unit-less terms of %/%, to establish the ratio by which percentage inductive reactive power production is increased as the  percent delta-voltage decreases above DbVMax. 

        Percent delta-voltage is defined as the present PVSystem/Storage terminal voltage minus the moving average voltage, expressed as a percentage of the rated voltage for the PVSystem/Storage object. 

        Note, the moving average voltage for the dynamic reactive current mode is different than the mmoving average voltage for the volt-watt and volt-var modes.

        DSS property name: `ArGraHiV`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    @ArGraHiV.setter
    def ArGraHiV(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(12, value)

    @property
    def DynReacAvgWindowLen(self) -> BatchInt32ArrayProxy:
        """
        Required for the dynamic reactive current mode (DYNAMICREACCURR), and defaults to 1 seconds (1s). do not use a value smaller than 1.0 

        Sets the length of the averaging window over which the average PVSystem/Storage terminal voltage is calculated for the dynamic reactive current mode. 

        Units are indicated by appending s, m, or h to the integer value. 

        Typically this will be a shorter averaging window than the volt-var and volt-watt averaging window.

        The averaging window will calculate the average PVSystem/Storage terminal voltage over the specified period of time, up to and including the last power flow solution.  Note, if the solution stepsize is larger than the window length, then the voltage will be assumed to have been constant over the time-frame specified by the window length.

        DSS property name: `DynReacAvgWindowLen`, DSS property index: 13.
        """
        return BatchInt32ArrayProxy(self, 13)

    @DynReacAvgWindowLen.setter
    def DynReacAvgWindowLen(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(13, value)

    @property
    def DeltaQ_Factor(self) -> BatchFloat64ArrayProxy:
        """
        Required for the VOLTVAR and DYNAMICREACCURR modes.  Defaults to -1.0. 

        Defining -1.0, OpenDSS takes care internally of delta_Q itself. It tries to improve convergence as well as speed up process

        Sets the maximum change (in per unit) from the prior var output level to the desired var output level during each control iteration. 


        if numerical instability is noticed in solutions such as var sign changing from one control iteration to the next and voltages oscillating between two values with some separation, this is an indication of numerical instability (use the EventLog to diagnose). 

        if the maximum control iterations are exceeded, and no numerical instability is seen in the EventLog of via monitors, then try increasing the value of this parameter to reduce the number of control iterations needed to achieve the control criteria, and move to the power flow solution. 

        When operating the controller using exponential control model (see CtrlModel), this parameter represents the sampling time gain of the controller, which is used for accelrating the controller response in terms of control iterations required.

        DSS property name: `DeltaQ_Factor`, DSS property index: 14.
        """
        return BatchFloat64ArrayProxy(self, 14)

    @DeltaQ_Factor.setter
    def DeltaQ_Factor(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(14, value)

    @property
    def VoltageChangeTolerance(self) -> BatchFloat64ArrayProxy:
        """
        Defaults to 0.0001 per-unit voltage.  This parameter should only be modified by advanced users of the InvControl.  

        Tolerance in pu of the control loop convergence associated to the monitored voltage in pu. This value is compared with the difference of the monitored voltage in pu of the current and previous control iterations of the control loop

        This voltage tolerance value plus the var/watt tolerance value (VarChangeTolerance/ActivePChangeTolerance) determine, together, when to stop control iterations by the InvControl. 

        If an InvControl is controlling more than one PVSystem/Storage, each PVSystem/Storage has this quantity calculated independently, and so an individual PVSystem/Storage may reach the tolerance within different numbers of control iterations.

        DSS property name: `VoltageChangeTolerance`, DSS property index: 15.
        """
        return BatchFloat64ArrayProxy(self, 15)

    @VoltageChangeTolerance.setter
    def VoltageChangeTolerance(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(15, value)

    @property
    def VarChangeTolerance(self) -> BatchFloat64ArrayProxy:
        """
        Required for VOLTVAR and DYNAMICREACCURR modes.  Defaults to 0.025 per unit of the base provided or absorbed reactive power described in the RefReactivePower property This parameter should only be modified by advanced users of the InvControl. 

        Tolerance in pu of the convergence of the control loop associated with reactive power. For the same control iteration, this value is compared to the difference, as an absolute value (without sign), between the desired reactive power value in pu and the output reactive power in pu of the controlled element.

        This reactive power tolerance value plus the voltage tolerance value (VoltageChangeTolerance) determine, together, when to stop control iterations by the InvControl.  

        If an InvControl is controlling more than one PVSystem/Storage, each PVSystem/Storage has this quantity calculated independently, and so an individual PVSystem/Storage may reach the tolerance within different numbers of control iterations.

        DSS property name: `VarChangeTolerance`, DSS property index: 16.
        """
        return BatchFloat64ArrayProxy(self, 16)

    @VarChangeTolerance.setter
    def VarChangeTolerance(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(16, value)

    @property
    def VoltWattYAxis(self) -> BatchInt32ArrayProxy:
        """
        Required for VOLTWATT mode.  Must be one of: {PMPPPU* | PAVAILABLEPU| PCTPMPPPU | KVARATINGPU}.  The default is PMPPPU.  

        Units for the y-axis of the volt-watt curve while in volt-watt mode. 

        When set to PMPPPU. The y-axis corresponds to the value in pu of Pmpp property of the PVSystem. 

        When set to PAVAILABLEPU. The y-axis corresponds to the value in pu of the available active power of the PVSystem. 

        When set to PCTPMPPPU. The y-axis corresponds to the value in pu of the power Pmpp multiplied by 1/100 of the %Pmpp property of the PVSystem.

        When set to KVARATINGPU. The y-axis corresponds to the value in pu of the kVA property of the PVSystem.

        DSS property name: `VoltWattYAxis`, DSS property index: 17.
        """
        return BatchInt32ArrayProxy(self, 17)

    @VoltWattYAxis.setter
    def VoltWattYAxis(self, value: Union[AnyStr, int, enums.InvControlVoltWattYAxis, List[AnyStr], List[int], List[enums.InvControlVoltWattYAxis], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(17, value)
            return
    
        self._set_batch_int32_array(17, value)

    @property
    def VoltWattYAxis_str(self) -> str:
        """
        Required for VOLTWATT mode.  Must be one of: {PMPPPU* | PAVAILABLEPU| PCTPMPPPU | KVARATINGPU}.  The default is PMPPPU.  

        Units for the y-axis of the volt-watt curve while in volt-watt mode. 

        When set to PMPPPU. The y-axis corresponds to the value in pu of Pmpp property of the PVSystem. 

        When set to PAVAILABLEPU. The y-axis corresponds to the value in pu of the available active power of the PVSystem. 

        When set to PCTPMPPPU. The y-axis corresponds to the value in pu of the power Pmpp multiplied by 1/100 of the %Pmpp property of the PVSystem.

        When set to KVARATINGPU. The y-axis corresponds to the value in pu of the kVA property of the PVSystem.

        DSS property name: `VoltWattYAxis`, DSS property index: 17.
        """
        return self._get_batch_str_prop(17)

    @VoltWattYAxis_str.setter
    def VoltWattYAxis_str(self, value: AnyStr):
        self.VoltWattYAxis = value

    @property
    def RateOfChangeMode(self) -> BatchInt32ArrayProxy:
        """
        Required for VOLTWATT and VOLTVAR mode.  Must be one of: {INACTIVE* | LPF | RISEFALL }.  The default is INACTIVE.  

        Auxiliary option that aims to limit the changes of the desired reactive power and the active power limit between time steps, the alternatives are listed below: 

        INACTIVE. It indicates there is no limit on rate of change imposed for either active or reactive power output. 

        LPF. A low-pass RC filter is applied to the desired reactive power and/or the active power limit to determine the output power as a function of a time constant defined in the LPFTau property. 

        RISEFALL. A rise and fall limit in the change of active and/or reactive power expressed in terms of pu power per second, defined in the RiseFallLimit, is applied to the desired reactive power and/or the active power limit. 

        DSS property name: `RateOfChangeMode`, DSS property index: 18.
        """
        return BatchInt32ArrayProxy(self, 18)

    @RateOfChangeMode.setter
    def RateOfChangeMode(self, value: Union[AnyStr, int, enums.InvControlRateOfChangeMode, List[AnyStr], List[int], List[enums.InvControlRateOfChangeMode], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(18, value)
            return
    
        self._set_batch_int32_array(18, value)

    @property
    def RateOfChangeMode_str(self) -> str:
        """
        Required for VOLTWATT and VOLTVAR mode.  Must be one of: {INACTIVE* | LPF | RISEFALL }.  The default is INACTIVE.  

        Auxiliary option that aims to limit the changes of the desired reactive power and the active power limit between time steps, the alternatives are listed below: 

        INACTIVE. It indicates there is no limit on rate of change imposed for either active or reactive power output. 

        LPF. A low-pass RC filter is applied to the desired reactive power and/or the active power limit to determine the output power as a function of a time constant defined in the LPFTau property. 

        RISEFALL. A rise and fall limit in the change of active and/or reactive power expressed in terms of pu power per second, defined in the RiseFallLimit, is applied to the desired reactive power and/or the active power limit. 

        DSS property name: `RateOfChangeMode`, DSS property index: 18.
        """
        return self._get_batch_str_prop(18)

    @RateOfChangeMode_str.setter
    def RateOfChangeMode_str(self, value: AnyStr):
        self.RateOfChangeMode = value

    @property
    def LPFTau(self) -> BatchFloat64ArrayProxy:
        """
        Not required. Defaults to 0 seconds. 

        Filter time constant of the LPF option of the RateofChangeMode property. The time constant will cause the low-pass filter to achieve 95% of the target value in 3 time constants.

        DSS property name: `LPFTau`, DSS property index: 19.
        """
        return BatchFloat64ArrayProxy(self, 19)

    @LPFTau.setter
    def LPFTau(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(19, value)

    @property
    def RiseFallLimit(self) -> BatchFloat64ArrayProxy:
        """
        Not required.  Defaults to no limit (-1). Must be -1 (no limit) or a positive value.  

        Limit in power in pu per second used by the RISEFALL option of the RateofChangeMode property.The base value for this ramp is defined in the RefReactivePower property and/or in VoltwattYAxis.

        DSS property name: `RiseFallLimit`, DSS property index: 20.
        """
        return BatchFloat64ArrayProxy(self, 20)

    @RiseFallLimit.setter
    def RiseFallLimit(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(20, value)

    @property
    def DeltaP_Factor(self) -> BatchFloat64ArrayProxy:
        """
        Required for the VOLTWATT modes.  Defaults to -1.0. 

        Defining -1.0, OpenDSS takes care internally of delta_P itself. It tries to improve convergence as well as speed up process

        Defining between 0.05 and 1.0, it sets the maximum change (in unit of the y-axis) from the prior active power output level to the desired active power output level during each control iteration. 


        If numerical instability is noticed in solutions such as active power changing substantially from one control iteration to the next and/or voltages oscillating between two values with some separation, this is an indication of numerical instability (use the EventLog to diagnose). 

        If the maximum control iterations are exceeded, and no numerical instability is seen in the EventLog of via monitors, then try increasing the value of this parameter to reduce the number of control iterations needed to achieve the control criteria, and move to the power flow solution.

        DSS property name: `DeltaP_Factor`, DSS property index: 21.
        """
        return BatchFloat64ArrayProxy(self, 21)

    @DeltaP_Factor.setter
    def DeltaP_Factor(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(21, value)

    @property
    def EventLog(self) -> List[bool]:
        """
        {Yes/True | No/False*} Default is NO for InvControl. Log control actions to Eventlog.

        DSS property name: `EventLog`, DSS property index: 22.
        """
        return [v != 0 for v in 
            self._get_batch_int32_prop(22)
        ]
    @EventLog.setter
    def EventLog(self, value: bool):
        self._set_batch_int32_array(22, value)

    @property
    def RefReactivePower(self) -> BatchInt32ArrayProxy:
        """
        Required for any mode that has VOLTVAR, DYNAMICREACCURR and WATTVAR. Defaults to VARAVAL.

        Defines the base reactive power for both the provided and absorbed reactive power, according to one of the following options: 

        VARAVAL. The base values for the provided and absorbed reactive power are equal to the available reactive power.

        VARMAX: The base values of the provided and absorbed reactive power are equal to the value defined in the kvarMax and kvarMaxAbs properties, respectively.

        DSS property name: `RefReactivePower`, DSS property index: 23.
        """
        return BatchInt32ArrayProxy(self, 23)

    @RefReactivePower.setter
    def RefReactivePower(self, value: Union[AnyStr, int, enums.InvControlReactivePowerReference, List[AnyStr], List[int], List[enums.InvControlReactivePowerReference], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(23, value)
            return
    
        self._set_batch_int32_array(23, value)

    @property
    def RefReactivePower_str(self) -> str:
        """
        Required for any mode that has VOLTVAR, DYNAMICREACCURR and WATTVAR. Defaults to VARAVAL.

        Defines the base reactive power for both the provided and absorbed reactive power, according to one of the following options: 

        VARAVAL. The base values for the provided and absorbed reactive power are equal to the available reactive power.

        VARMAX: The base values of the provided and absorbed reactive power are equal to the value defined in the kvarMax and kvarMaxAbs properties, respectively.

        DSS property name: `RefReactivePower`, DSS property index: 23.
        """
        return self._get_batch_str_prop(23)

    @RefReactivePower_str.setter
    def RefReactivePower_str(self, value: AnyStr):
        self.RefReactivePower = value

    @property
    def ActivePChangeTolerance(self) -> BatchFloat64ArrayProxy:
        """
        Required for VOLTWATT. Default is 0.01

        Tolerance in pu of the convergence of the control loop associated with active power. For the same control iteration, this value is compared to the difference between the active power limit in pu resulted from the convergence process and the one resulted from the volt-watt function.

        This reactive power tolerance value plus the voltage tolerance value (VoltageChangeTolerance) determine, together, when to stop control iterations by the InvControl.  

        If an InvControl is controlling more than one PVSystem/Storage, each PVSystem/Storage has this quantity calculated independently, and so an individual PVSystem/Storage may reach the tolerance within different numbers of control iterations.

        DSS property name: `ActivePChangeTolerance`, DSS property index: 24.
        """
        return BatchFloat64ArrayProxy(self, 24)

    @ActivePChangeTolerance.setter
    def ActivePChangeTolerance(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(24, value)

    @property
    def MonVoltageCalc(self) -> BatchInt32ArrayProxy:
        """
        Number of the phase being monitored or one of {AVG | MAX | MIN} for all phases. Default=AVG. 

        DSS property name: `MonVoltageCalc`, DSS property index: 25.
        """
        return BatchInt32ArrayProxy(self, 25)

    @MonVoltageCalc.setter
    def MonVoltageCalc(self, value: Union[AnyStr, int, enums.MonitoredPhase, List[AnyStr], List[int], List[enums.MonitoredPhase], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(25, value)
            return
    
        self._set_batch_int32_array(25, value)

    @property
    def MonVoltageCalc_str(self) -> str:
        """
        Number of the phase being monitored or one of {AVG | MAX | MIN} for all phases. Default=AVG. 

        DSS property name: `MonVoltageCalc`, DSS property index: 25.
        """
        return self._get_batch_str_prop(25)

    @MonVoltageCalc_str.setter
    def MonVoltageCalc_str(self, value: AnyStr):
        self.MonVoltageCalc = value

    @property
    def MonBus(self) -> List[List[str]]:
        """
        Name of monitored bus used by the voltage-dependent control modes. Default is bus of the controlled PVSystem/Storage or Storage.

        DSS property name: `MonBus`, DSS property index: 26.
        """
        return self._get_string_ll(26)

    @MonBus.setter
    def MonBus(self, value: List[AnyStr]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._unpack():
            self._lib.Obj_SetStringArray(x, 26, value_ptr, value_count)
    
        self._check_for_error()

    @property
    def MonBusesVBase(self) -> List[Float64Array]:
        """
        Array list of rated voltages of the buses and their nodes presented in the monBus property. This list may have different line-to-line and/or line-to-ground voltages.

        DSS property name: `MonBusesVBase`, DSS property index: 27.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 27)
            for x in self._unpack()
        ]

    @MonBusesVBase.setter
    def MonBusesVBase(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(27, value)

    @property
    def VoltWattCH_Curve(self) -> List[str]:
        """
        Required for VOLTWATT mode for Storage element in CHARGING state. 

        The name of an XYCurve object that describes the variation in active power output (in per unit of maximum active power output for the Storage). 

        Units for the x-axis are per-unit voltage, which may be in per unit of the rated voltage for the Storage, or may be in per unit of the average voltage at the terminals over a user-defined number of prior solutions. 

        Units for the y-axis are either in: (1) per unit of maximum active power output capability of the Storage, or (2) maximum available active power output capability (defined by the parameter: VoltwattYAxis), corresponding to the terminal voltage (x-axis value in per unit). 

        No default -- must be specified for VOLTWATT mode for Storage element in CHARGING state.

        DSS property name: `VoltWattCH_Curve`, DSS property index: 28.
        """
        return self._get_batch_str_prop(28)

    @VoltWattCH_Curve.setter
    def VoltWattCH_Curve(self, value: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]):
        self._set_batch_obj_prop(28, value)

    @property
    def VoltWattCH_Curve_obj(self) -> List[XYcurve]:
        """
        Required for VOLTWATT mode for Storage element in CHARGING state. 

        The name of an XYCurve object that describes the variation in active power output (in per unit of maximum active power output for the Storage). 

        Units for the x-axis are per-unit voltage, which may be in per unit of the rated voltage for the Storage, or may be in per unit of the average voltage at the terminals over a user-defined number of prior solutions. 

        Units for the y-axis are either in: (1) per unit of maximum active power output capability of the Storage, or (2) maximum available active power output capability (defined by the parameter: VoltwattYAxis), corresponding to the terminal voltage (x-axis value in per unit). 

        No default -- must be specified for VOLTWATT mode for Storage element in CHARGING state.

        DSS property name: `VoltWattCH_Curve`, DSS property index: 28.
        """
        return self._get_batch_obj_prop(28)

    @VoltWattCH_Curve_obj.setter
    def VoltWattCH_Curve_obj(self, value: XYcurve):
        self._set_batch_string(28, value)

    @property
    def WattPF_Curve(self) -> List[str]:
        """
        Required for WATTPF mode.

        Name of the XYCurve object containing the watt-pf curve.
        The positive values of the y-axis are positive power factor values. The negative values of the the y-axis are negative power factor values. When positive, the output reactive power has the same direction of the output active power, and when negative, it has the opposite direction.
        Units for the x-axis are per-unit output active power, and the base active power is the Pmpp for PVSystem and kWrated for Storage.

        The y-axis represents the power factor and the reference is power factor equal to 0. 

        For example, if the user wants to define the following XY coordinates: (0, 0.9); (0.2, 0.9); (0.5, -0.9); (1, -0.9).
        Try to plot them considering the y-axis reference equal to unity power factor.

        The user needs to translate this curve into a plot in which the y-axis reference is equal to 0 power factor.It means that two new XY coordinates need to be included, in this case they are: (0.35, 1); (0.35, -1).
        Try to plot them considering the y-axis reference equal to 0 power factor.
        The discontinuity in 0.35pu is not a problem since var is zero for either power factor equal to 1 or -1.

        DSS property name: `WattPF_Curve`, DSS property index: 29.
        """
        return self._get_batch_str_prop(29)

    @WattPF_Curve.setter
    def WattPF_Curve(self, value: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]):
        self._set_batch_obj_prop(29, value)

    @property
    def WattPF_Curve_obj(self) -> List[XYcurve]:
        """
        Required for WATTPF mode.

        Name of the XYCurve object containing the watt-pf curve.
        The positive values of the y-axis are positive power factor values. The negative values of the the y-axis are negative power factor values. When positive, the output reactive power has the same direction of the output active power, and when negative, it has the opposite direction.
        Units for the x-axis are per-unit output active power, and the base active power is the Pmpp for PVSystem and kWrated for Storage.

        The y-axis represents the power factor and the reference is power factor equal to 0. 

        For example, if the user wants to define the following XY coordinates: (0, 0.9); (0.2, 0.9); (0.5, -0.9); (1, -0.9).
        Try to plot them considering the y-axis reference equal to unity power factor.

        The user needs to translate this curve into a plot in which the y-axis reference is equal to 0 power factor.It means that two new XY coordinates need to be included, in this case they are: (0.35, 1); (0.35, -1).
        Try to plot them considering the y-axis reference equal to 0 power factor.
        The discontinuity in 0.35pu is not a problem since var is zero for either power factor equal to 1 or -1.

        DSS property name: `WattPF_Curve`, DSS property index: 29.
        """
        return self._get_batch_obj_prop(29)

    @WattPF_Curve_obj.setter
    def WattPF_Curve_obj(self, value: XYcurve):
        self._set_batch_string(29, value)

    @property
    def WattVar_Curve(self) -> List[str]:
        """
        Required for WATTVAR mode. 

        Name of the XYCurve object containing the watt-var curve. The positive values of the y-axis of the watt-var curve represent values in pu of the provided base reactive power. The negative values of the y-axis are values in pu of the absorbed base reactive power. 
        Provided and absorbed base reactive power values are defined in the RefReactivePower property.

        Units for the x-axis are per-unit output active power, and the base active power is the Pmpp for PVSystem and kWrated for Storage.

        DSS property name: `WattVar_Curve`, DSS property index: 30.
        """
        return self._get_batch_str_prop(30)

    @WattVar_Curve.setter
    def WattVar_Curve(self, value: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]):
        self._set_batch_obj_prop(30, value)

    @property
    def WattVar_Curve_obj(self) -> List[XYcurve]:
        """
        Required for WATTVAR mode. 

        Name of the XYCurve object containing the watt-var curve. The positive values of the y-axis of the watt-var curve represent values in pu of the provided base reactive power. The negative values of the y-axis are values in pu of the absorbed base reactive power. 
        Provided and absorbed base reactive power values are defined in the RefReactivePower property.

        Units for the x-axis are per-unit output active power, and the base active power is the Pmpp for PVSystem and kWrated for Storage.

        DSS property name: `WattVar_Curve`, DSS property index: 30.
        """
        return self._get_batch_obj_prop(30)

    @WattVar_Curve_obj.setter
    def WattVar_Curve_obj(self, value: XYcurve):
        self._set_batch_string(30, value)

    @property
    def VSetPoint(self) -> BatchFloat64ArrayProxy:
        """
        Required for Active Voltage Regulation (AVR).

        DSS property name: `VSetPoint`, DSS property index: 33.
        """
        return BatchFloat64ArrayProxy(self, 33)

    @VSetPoint.setter
    def VSetPoint(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(33, value)

    @property
    def ControlModel(self) -> BatchInt32ArrayProxy:
        """
        Integer defining the method for moving across the control curve. It can be one of the following:

        0 = Linear mode (default)
        1 = Exponential

        Use this property for better tunning your controller and improve the controller response in terms of control iterations needed to reach the target.
        This property alters the meaning of deltaQ_factor and deltaP_factor properties according to its value (Check help). The method can also be combined with the controller tolerance for improving performance.

        DSS property name: `ControlModel`, DSS property index: 34.
        """
        return BatchInt32ArrayProxy(self, 34)

    @ControlModel.setter
    def ControlModel(self, value: Union[int, enums.InvControlControlModel, Int32Array]):
        self._set_batch_int32_array(34, value)

    @property
    def BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 35.
        """
        return BatchFloat64ArrayProxy(self, 35)

    @BaseFreq.setter
    def BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(35, value)

    @property
    def Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 36.
        """
        return [v != 0 for v in 
            self._get_batch_int32_prop(36)
        ]
    @Enabled.setter
    def Enabled(self, value: bool):
        self._set_batch_int32_array(36, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 37.
        """
        self._set_batch_string(37, value)

class InvControlBatchProperties(TypedDict):
    DERList: List[AnyStr]
    Mode: Union[AnyStr, int, enums.InvControlControlMode, List[AnyStr], List[int], List[enums.InvControlControlMode], Int32Array]
    CombiMode: Union[AnyStr, int, enums.InvControlCombiMode, List[AnyStr], List[int], List[enums.InvControlCombiMode], Int32Array]
    VVC_Curve1: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]
    Hysteresis_Offset: Union[float, Float64Array]
    Voltage_CurveX_Ref: Union[AnyStr, int, enums.InvControlVoltageCurveXRef, List[AnyStr], List[int], List[enums.InvControlVoltageCurveXRef], Int32Array]
    AvgWindowLen: Union[int, Int32Array]
    VoltWatt_Curve: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]
    DbVMin: Union[float, Float64Array]
    DbVMax: Union[float, Float64Array]
    ArGraLowV: Union[float, Float64Array]
    ArGraHiV: Union[float, Float64Array]
    DynReacAvgWindowLen: Union[int, Int32Array]
    DeltaQ_Factor: Union[float, Float64Array]
    VoltageChangeTolerance: Union[float, Float64Array]
    VarChangeTolerance: Union[float, Float64Array]
    VoltWattYAxis: Union[AnyStr, int, enums.InvControlVoltWattYAxis, List[AnyStr], List[int], List[enums.InvControlVoltWattYAxis], Int32Array]
    RateOfChangeMode: Union[AnyStr, int, enums.InvControlRateOfChangeMode, List[AnyStr], List[int], List[enums.InvControlRateOfChangeMode], Int32Array]
    LPFTau: Union[float, Float64Array]
    RiseFallLimit: Union[float, Float64Array]
    DeltaP_Factor: Union[float, Float64Array]
    EventLog: bool
    RefReactivePower: Union[AnyStr, int, enums.InvControlReactivePowerReference, List[AnyStr], List[int], List[enums.InvControlReactivePowerReference], Int32Array]
    ActivePChangeTolerance: Union[float, Float64Array]
    MonVoltageCalc: Union[AnyStr, int, enums.MonitoredPhase, List[AnyStr], List[int], List[enums.MonitoredPhase], Int32Array]
    MonBus: List[AnyStr]
    MonBusesVBase: Float64Array
    VoltWattCH_Curve: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]
    WattPF_Curve: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]
    WattVar_Curve: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]
    VSetPoint: Union[float, Float64Array]
    ControlModel: Union[int, enums.InvControlControlModel, Int32Array]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IInvControl(IDSSObj,InvControlBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, InvControl, InvControlBatch)
        InvControlBatch.__init__(self, self._api_util, sync_cls=True)
        

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> InvControl:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[InvControlProperties]) -> InvControl:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[InvControlBatchProperties]) -> InvControlBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
