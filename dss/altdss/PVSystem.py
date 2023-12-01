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
from .PCElement import PCElementBatchMixin, ElementHasRegistersMixin, PCElementMixin
from .CircuitElement import CircuitElementBatchMixin, CircuitElementMixin
from .DynamicExp import DynamicExp
from .LoadShape import LoadShape
from .Spectrum import Spectrum as SpectrumObj
from .TShape import TShape
from .XYcurve import XYcurve

class PVSystem(DSSObj, CircuitElementMixin, PCElementMixin, ElementHasRegistersMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots + PCElementMixin._extra_slots + ElementHasRegistersMixin._extra_slots
    _cls_name = 'PVSystem'
    _cls_idx = 35
    _cls_prop_idx = {
        'phases': 1,
        'bus1': 2,
        'kv': 3,
        'irradiance': 4,
        'pmpp': 5,
        'pctpmpp': 6,
        '%pmpp': 6,
        'temperature': 7,
        'pf': 8,
        'conn': 9,
        'kvar': 10,
        'kva': 11,
        'pctcutin': 12,
        '%cutin': 12,
        'pctcutout': 13,
        '%cutout': 13,
        'effcurve': 14,
        'ptcurve': 15,
        'p-tcurve': 15,
        'pctr': 16,
        '%r': 16,
        'pctx': 17,
        '%x': 17,
        'model': 18,
        'vminpu': 19,
        'vmaxpu': 20,
        'balanced': 21,
        'limitcurrent': 22,
        'yearly': 23,
        'daily': 24,
        'duty': 25,
        'tyearly': 26,
        'tdaily': 27,
        'tduty': 28,
        'cls': 29,
        'class': 29,
        'usermodel': 30,
        'userdata': 31,
        'debugtrace': 32,
        'varfollowinverter': 33,
        'dutystart': 34,
        'wattpriority': 35,
        'pfpriority': 36,
        'pctpminnovars': 37,
        '%pminnovars': 37,
        'pctpminkvarmax': 38,
        '%pminkvarmax': 38,
        'kvarmax': 39,
        'kvarmaxabs': 40,
        'kvdc': 41,
        'kp': 42,
        'pitol': 43,
        'safevoltage': 44,
        'safemode': 45,
        'dynamiceq': 46,
        'dynout': 47,
        'controlmode': 48,
        'amplimit': 49,
        'amplimitgain': 50,
        'spectrum': 51,
        'basefreq': 52,
        'enabled': 53,
        'like': 54,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)
       PCElementMixin.__init__(self)
       ElementHasRegistersMixin.__init__(self)

    def _get_Phases(self) -> int:
        """
        Number of Phases, this PVSystem element.  Power is evenly divided among phases.

        DSS property name: `Phases`, DSS property index: 1.
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    def _set_Phases(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 1, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: int

    def _get_Bus1(self) -> str:
        """
        Bus to which the PVSystem element is connected.  May include specific node specification.

        DSS property name: `Bus1`, DSS property index: 2.
        """
        return self._get_prop_string(2)

    def _set_Bus1(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(2, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: str

    def _get_kV(self) -> float:
        """
        Nominal rated (1.0 per unit) voltage, kV, for PVSystem element. For 2- and 3-phase PVSystem elements, specify phase-phase kV. Otherwise, specify actual kV across each branch of the PVSystem element. If 1-phase wye (star or LN), specify phase-neutral kV. If 1-phase delta or phase-phase connected, specify phase-phase kV.

        DSS property name: `kV`, DSS property index: 3.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    def _set_kV(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 3, value, flags)

    kV = property(_get_kV, _set_kV) # type: float

    def _get_Irradiance(self) -> float:
        """
        Get/set the present irradiance value in kW/sq-m. Used as base value for shape multipliers. Generally entered as peak value for the time period of interest and the yearly, daily, and duty load shape objects are defined as per unit multipliers (just like Loads/Generators).

        DSS property name: `Irradiance`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    def _set_Irradiance(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 4, value, flags)

    Irradiance = property(_get_Irradiance, _set_Irradiance) # type: float

    def _get_Pmpp(self) -> float:
        """
        Get/set the rated max power of the PV array for 1.0 kW/sq-m irradiance and a user-selected array temperature. The P-TCurve should be defined relative to the selected array temperature.

        DSS property name: `Pmpp`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    def _set_Pmpp(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 5, value, flags)

    Pmpp = property(_get_Pmpp, _set_Pmpp) # type: float

    def _get_pctPmpp(self) -> float:
        """
        Upper limit on active power as a percentage of Pmpp.

        DSS property name: `%Pmpp`, DSS property index: 6.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    def _set_pctPmpp(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 6, value, flags)

    pctPmpp = property(_get_pctPmpp, _set_pctPmpp) # type: float

    def _get_Temperature(self) -> float:
        """
        Get/set the present Temperature. Used as fixed value corresponding to PTCurve property. A multiplier is obtained from the Pmpp-Temp curve and applied to the nominal Pmpp from the irradiance to determine the net array output.

        DSS property name: `Temperature`, DSS property index: 7.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    def _set_Temperature(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 7, value, flags)

    Temperature = property(_get_Temperature, _set_Temperature) # type: float

    def _get_PF(self) -> float:
        """
        Nominally, the power factor for the output power. Default is 1.0. Setting this property will cause the inverter to operate in constant power factor mode.Enter negative when kW and kvar have opposite signs.
        A positive power factor signifies that the PVSystem element produces vars 
        as is typical for a generator.  

        DSS property name: `PF`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    def _set_PF(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 8, value, flags)

    PF = property(_get_PF, _set_PF) # type: float

    def _get_Conn(self) -> enums.Connection:
        """
        ={wye|LN|delta|LL}.  Default is wye.

        DSS property name: `Conn`, DSS property index: 9.
        """
        return enums.Connection(self._lib.Obj_GetInt32(self._ptr, 9))

    def _set_Conn(self, value: Union[AnyStr, int, enums.Connection], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(9, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 9, value, flags)

    Conn = property(_get_Conn, _set_Conn) # type: enums.Connection

    def _get_Conn_str(self) -> str:
        """
        ={wye|LN|delta|LL}.  Default is wye.

        DSS property name: `Conn`, DSS property index: 9.
        """
        return self._get_prop_string(9)

    def _set_Conn_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Conn(value, flags)

    Conn_str = property(_get_Conn_str, _set_Conn_str) # type: str

    def _get_kvar(self) -> float:
        """
        Get/set the present kvar value.  Setting this property forces the inverter to operate in constant kvar mode.

        DSS property name: `kvar`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    def _set_kvar(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 10, value, flags)

    kvar = property(_get_kvar, _set_kvar) # type: float

    def _get_kVA(self) -> float:
        """
        kVA rating of inverter. Used as the base for Dynamics mode and Harmonics mode values.

        DSS property name: `kVA`, DSS property index: 11.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    def _set_kVA(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 11, value, flags)

    kVA = property(_get_kVA, _set_kVA) # type: float

    def _get_pctCutIn(self) -> float:
        """
        % cut-in power -- % of kVA rating of inverter. When the inverter is OFF, the power from the array must be greater than this for the inverter to turn on.

        DSS property name: `%CutIn`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    def _set_pctCutIn(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 12, value, flags)

    pctCutIn = property(_get_pctCutIn, _set_pctCutIn) # type: float

    def _get_pctCutOut(self) -> float:
        """
        % cut-out power -- % of kVA rating of inverter. When the inverter is ON, the inverter turns OFF when the power from the array drops below this value.

        DSS property name: `%CutOut`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    def _set_pctCutOut(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 13, value, flags)

    pctCutOut = property(_get_pctCutOut, _set_pctCutOut) # type: float

    def _get_EffCurve_str(self) -> str:
        """
        An XYCurve object, previously defined, that describes the PER UNIT efficiency vs PER UNIT of rated kVA for the inverter. Inverter output power is discounted by the multiplier obtained from this curve.

        DSS property name: `EffCurve`, DSS property index: 14.
        """
        return self._get_prop_string(14)

    def _set_EffCurve_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(14, value, flags)

    EffCurve_str = property(_get_EffCurve_str, _set_EffCurve_str) # type: str

    def _get_EffCurve(self) -> XYcurve:
        """
        An XYCurve object, previously defined, that describes the PER UNIT efficiency vs PER UNIT of rated kVA for the inverter. Inverter output power is discounted by the multiplier obtained from this curve.

        DSS property name: `EffCurve`, DSS property index: 14.
        """
        return self._get_obj(14, XYcurve)

    def _set_EffCurve(self, value: Union[AnyStr, XYcurve], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(14, value, flags)
            return

        self._set_string_o(14, value, flags)

    EffCurve = property(_get_EffCurve, _set_EffCurve) # type: XYcurve

    def _get_PTCurve_str(self) -> str:
        """
        An XYCurve object, previously defined, that describes the PV array PER UNIT Pmpp vs Temperature curve. Temperature units must agree with the Temperature property and the Temperature shapes used for simulations. The Pmpp values are specified in per unit of the Pmpp value for 1 kW/sq-m irradiance. The value for the temperature at which Pmpp is defined should be 1.0. The net array power is determined by the irradiance * Pmpp * f(Temperature)

        DSS property name: `P-TCurve`, DSS property index: 15.
        """
        return self._get_prop_string(15)

    def _set_PTCurve_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(15, value, flags)

    PTCurve_str = property(_get_PTCurve_str, _set_PTCurve_str) # type: str

    def _get_PTCurve(self) -> XYcurve:
        """
        An XYCurve object, previously defined, that describes the PV array PER UNIT Pmpp vs Temperature curve. Temperature units must agree with the Temperature property and the Temperature shapes used for simulations. The Pmpp values are specified in per unit of the Pmpp value for 1 kW/sq-m irradiance. The value for the temperature at which Pmpp is defined should be 1.0. The net array power is determined by the irradiance * Pmpp * f(Temperature)

        DSS property name: `P-TCurve`, DSS property index: 15.
        """
        return self._get_obj(15, XYcurve)

    def _set_PTCurve(self, value: Union[AnyStr, XYcurve], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(15, value, flags)
            return

        self._set_string_o(15, value, flags)

    PTCurve = property(_get_PTCurve, _set_PTCurve) # type: XYcurve

    def _get_pctR(self) -> float:
        """
        Equivalent percent internal resistance, ohms. Default is 50%. Placed in series with internal voltage source for harmonics and dynamics modes. (Limits fault current to about 2 pu if not current limited -- see LimitCurrent) 

        DSS property name: `%R`, DSS property index: 16.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    def _set_pctR(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 16, value, flags)

    pctR = property(_get_pctR, _set_pctR) # type: float

    def _get_pctX(self) -> float:
        """
        Equivalent percent internal reactance, ohms. Default is 0%. Placed in series with internal voltage source for harmonics and dynamics modes. 

        DSS property name: `%X`, DSS property index: 17.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    def _set_pctX(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 17, value, flags)

    pctX = property(_get_pctX, _set_pctX) # type: float

    def _get_Model(self) -> enums.PVSystemModel:
        """
        Integer code (default=1) for the model to use for power output variation with voltage. Valid values are:

        1:PVSystem element injects a CONSTANT kW at specified power factor.
        2:PVSystem element is modeled as a CONSTANT ADMITTANCE.
        3:Compute load injection from User-written Model.

        DSS property name: `Model`, DSS property index: 18.
        """
        return enums.PVSystemModel(self._lib.Obj_GetInt32(self._ptr, 18))

    def _set_Model(self, value: Union[int, enums.PVSystemModel], flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 18, value, flags)

    Model = property(_get_Model, _set_Model) # type: enums.PVSystemModel

    def _get_VMinpu(self) -> float:
        """
        Default = 0.90.  Minimum per unit voltage for which the Model is assumed to apply. Below this value, the load model reverts to a constant impedance model except for Dynamics model. In Dynamics mode, the current magnitude is limited to the value the power flow would compute for this voltage.

        DSS property name: `VMinpu`, DSS property index: 19.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    def _set_VMinpu(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 19, value, flags)

    VMinpu = property(_get_VMinpu, _set_VMinpu) # type: float

    def _get_VMaxpu(self) -> float:
        """
        Default = 1.10.  Maximum per unit voltage for which the Model is assumed to apply. Above this value, the load model reverts to a constant impedance model.

        DSS property name: `VMaxpu`, DSS property index: 20.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    def _set_VMaxpu(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 20, value, flags)

    VMaxpu = property(_get_VMaxpu, _set_VMaxpu) # type: float

    def _get_Balanced(self) -> bool:
        """
        {Yes | No*} Default is No.  Force balanced current only for 3-phase PVSystems. Forces zero- and negative-sequence to zero. 

        DSS property name: `Balanced`, DSS property index: 21.
        """
        return self._lib.Obj_GetInt32(self._ptr, 21) != 0

    def _set_Balanced(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 21, value, flags)

    Balanced = property(_get_Balanced, _set_Balanced) # type: bool

    def _get_LimitCurrent(self) -> bool:
        """
        Limits current magnitude to Vminpu value for both 1-phase and 3-phase PVSystems similar to Generator Model 7. For 3-phase, limits the positive-sequence current but not the negative-sequence.

        DSS property name: `LimitCurrent`, DSS property index: 22.
        """
        return self._lib.Obj_GetInt32(self._ptr, 22) != 0

    def _set_LimitCurrent(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 22, value, flags)

    LimitCurrent = property(_get_LimitCurrent, _set_LimitCurrent) # type: bool

    def _get_Yearly_str(self) -> str:
        """
        Dispatch shape to use for yearly simulations.  Must be previously defined as a Loadshape object. If this is not specified, the Daily dispatch shape, if any, is repeated during Yearly solution modes. In the default dispatch mode, the PVSystem element uses this loadshape to trigger State changes.

        DSS property name: `Yearly`, DSS property index: 23.
        """
        return self._get_prop_string(23)

    def _set_Yearly_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(23, value, flags)

    Yearly_str = property(_get_Yearly_str, _set_Yearly_str) # type: str

    def _get_Yearly(self) -> LoadShape:
        """
        Dispatch shape to use for yearly simulations.  Must be previously defined as a Loadshape object. If this is not specified, the Daily dispatch shape, if any, is repeated during Yearly solution modes. In the default dispatch mode, the PVSystem element uses this loadshape to trigger State changes.

        DSS property name: `Yearly`, DSS property index: 23.
        """
        return self._get_obj(23, LoadShape)

    def _set_Yearly(self, value: Union[AnyStr, LoadShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(23, value, flags)
            return

        self._set_string_o(23, value, flags)

    Yearly = property(_get_Yearly, _set_Yearly) # type: LoadShape

    def _get_Daily_str(self) -> str:
        """
        Dispatch shape to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically.  In the default dispatch mode, the PVSystem element uses this loadshape to trigger State changes.

        DSS property name: `Daily`, DSS property index: 24.
        """
        return self._get_prop_string(24)

    def _set_Daily_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(24, value, flags)

    Daily_str = property(_get_Daily_str, _set_Daily_str) # type: str

    def _get_Daily(self) -> LoadShape:
        """
        Dispatch shape to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically.  In the default dispatch mode, the PVSystem element uses this loadshape to trigger State changes.

        DSS property name: `Daily`, DSS property index: 24.
        """
        return self._get_obj(24, LoadShape)

    def _set_Daily(self, value: Union[AnyStr, LoadShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(24, value, flags)
            return

        self._set_string_o(24, value, flags)

    Daily = property(_get_Daily, _set_Daily) # type: LoadShape

    def _get_Duty_str(self) -> str:
        """
        Load shape to use for duty cycle dispatch simulations such as for solar ramp rate studies. Must be previously defined as a Loadshape object. Typically would have time intervals of 1-5 seconds. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.

        DSS property name: `Duty`, DSS property index: 25.
        """
        return self._get_prop_string(25)

    def _set_Duty_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(25, value, flags)

    Duty_str = property(_get_Duty_str, _set_Duty_str) # type: str

    def _get_Duty(self) -> LoadShape:
        """
        Load shape to use for duty cycle dispatch simulations such as for solar ramp rate studies. Must be previously defined as a Loadshape object. Typically would have time intervals of 1-5 seconds. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.

        DSS property name: `Duty`, DSS property index: 25.
        """
        return self._get_obj(25, LoadShape)

    def _set_Duty(self, value: Union[AnyStr, LoadShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(25, value, flags)
            return

        self._set_string_o(25, value, flags)

    Duty = property(_get_Duty, _set_Duty) # type: LoadShape

    def _get_TYearly_str(self) -> str:
        """
        Temperature shape to use for yearly simulations.  Must be previously defined as a TShape object. If this is not specified, the Daily dispatch shape, if any, is repeated during Yearly solution modes. The PVSystem element uses this TShape to determine the Pmpp from the Pmpp vs T curve. Units must agree with the Pmpp vs T curve.

        DSS property name: `TYearly`, DSS property index: 26.
        """
        return self._get_prop_string(26)

    def _set_TYearly_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(26, value, flags)

    TYearly_str = property(_get_TYearly_str, _set_TYearly_str) # type: str

    def _get_TYearly(self) -> TShape:
        """
        Temperature shape to use for yearly simulations.  Must be previously defined as a TShape object. If this is not specified, the Daily dispatch shape, if any, is repeated during Yearly solution modes. The PVSystem element uses this TShape to determine the Pmpp from the Pmpp vs T curve. Units must agree with the Pmpp vs T curve.

        DSS property name: `TYearly`, DSS property index: 26.
        """
        return self._get_obj(26, TShape)

    def _set_TYearly(self, value: Union[AnyStr, TShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(26, value, flags)
            return

        self._set_string_o(26, value, flags)

    TYearly = property(_get_TYearly, _set_TYearly) # type: TShape

    def _get_TDaily_str(self) -> str:
        """
        Temperature shape to use for daily simulations.  Must be previously defined as a TShape object of 24 hrs, typically.  The PVSystem element uses this TShape to determine the Pmpp from the Pmpp vs T curve. Units must agree with the Pmpp vs T curve.

        DSS property name: `TDaily`, DSS property index: 27.
        """
        return self._get_prop_string(27)

    def _set_TDaily_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(27, value, flags)

    TDaily_str = property(_get_TDaily_str, _set_TDaily_str) # type: str

    def _get_TDaily(self) -> TShape:
        """
        Temperature shape to use for daily simulations.  Must be previously defined as a TShape object of 24 hrs, typically.  The PVSystem element uses this TShape to determine the Pmpp from the Pmpp vs T curve. Units must agree with the Pmpp vs T curve.

        DSS property name: `TDaily`, DSS property index: 27.
        """
        return self._get_obj(27, TShape)

    def _set_TDaily(self, value: Union[AnyStr, TShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(27, value, flags)
            return

        self._set_string_o(27, value, flags)

    TDaily = property(_get_TDaily, _set_TDaily) # type: TShape

    def _get_TDuty_str(self) -> str:
        """
        Temperature shape to use for duty cycle dispatch simulations such as for solar ramp rate studies. Must be previously defined as a TShape object. Typically would have time intervals of 1-5 seconds. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat. The PVSystem model uses this TShape to determine the Pmpp from the Pmpp vs T curve. Units must agree with the Pmpp vs T curve.

        DSS property name: `TDuty`, DSS property index: 28.
        """
        return self._get_prop_string(28)

    def _set_TDuty_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(28, value, flags)

    TDuty_str = property(_get_TDuty_str, _set_TDuty_str) # type: str

    def _get_TDuty(self) -> TShape:
        """
        Temperature shape to use for duty cycle dispatch simulations such as for solar ramp rate studies. Must be previously defined as a TShape object. Typically would have time intervals of 1-5 seconds. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat. The PVSystem model uses this TShape to determine the Pmpp from the Pmpp vs T curve. Units must agree with the Pmpp vs T curve.

        DSS property name: `TDuty`, DSS property index: 28.
        """
        return self._get_obj(28, TShape)

    def _set_TDuty(self, value: Union[AnyStr, TShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(28, value, flags)
            return

        self._set_string_o(28, value, flags)

    TDuty = property(_get_TDuty, _set_TDuty) # type: TShape

    def _get_Class(self) -> int:
        """
        An arbitrary integer number representing the class of PVSystem element so that PVSystem values may be segregated by class.

        DSS property name: `Class`, DSS property index: 29.
        """
        return self._lib.Obj_GetInt32(self._ptr, 29)

    def _set_Class(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 29, value, flags)

    Class = property(_get_Class, _set_Class) # type: int

    def _get_UserModel(self) -> str:
        """
        Name of DLL containing user-written model, which computes the terminal currents for Dynamics studies, overriding the default model.  Set to "none" to negate previous setting.

        DSS property name: `UserModel`, DSS property index: 30.
        """
        return self._get_prop_string(30)

    def _set_UserModel(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(30, value, flags)

    UserModel = property(_get_UserModel, _set_UserModel) # type: str

    def _get_UserData(self) -> str:
        """
        String (in quotes or parentheses) that gets passed to user-written model for defining the data required for that model.

        DSS property name: `UserData`, DSS property index: 31.
        """
        return self._get_prop_string(31)

    def _set_UserData(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(31, value, flags)

    UserData = property(_get_UserData, _set_UserData) # type: str

    def _get_DebugTrace(self) -> bool:
        """
        {Yes | No }  Default is no.  Turn this on to capture the progress of the PVSystem model for each iteration.  Creates a separate file for each PVSystem element named "PVSystem_name.csv".

        DSS property name: `DebugTrace`, DSS property index: 32.
        """
        return self._lib.Obj_GetInt32(self._ptr, 32) != 0

    def _set_DebugTrace(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 32, value, flags)

    DebugTrace = property(_get_DebugTrace, _set_DebugTrace) # type: bool

    def _get_VarFollowInverter(self) -> bool:
        """
        Boolean variable (Yes|No) or (True|False). Defaults to False which indicates that the reactive power generation/absorption does not respect the inverter status.When set to True, the PVSystem reactive power generation/absorption will cease when the inverter status is off, due to panel kW dropping below %Cutout.  The reactive power generation/absorption will begin again when the panel kW is above %Cutin.  When set to False, the PVSystem will generate/absorb reactive power regardless of the status of the inverter.

        DSS property name: `VarFollowInverter`, DSS property index: 33.
        """
        return self._lib.Obj_GetInt32(self._ptr, 33) != 0

    def _set_VarFollowInverter(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 33, value, flags)

    VarFollowInverter = property(_get_VarFollowInverter, _set_VarFollowInverter) # type: bool

    def _get_DutyStart(self) -> float:
        """
        Starting time offset [hours] into the duty cycle shape for this PVSystem, defaults to 0

        DSS property name: `DutyStart`, DSS property index: 34.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 34)

    def _set_DutyStart(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 34, value, flags)

    DutyStart = property(_get_DutyStart, _set_DutyStart) # type: float

    def _get_WattPriority(self) -> bool:
        """
        {Yes/No*/True/False} Set inverter to watt priority instead of the default var priority

        DSS property name: `WattPriority`, DSS property index: 35.
        """
        return self._lib.Obj_GetInt32(self._ptr, 35) != 0

    def _set_WattPriority(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 35, value, flags)

    WattPriority = property(_get_WattPriority, _set_WattPriority) # type: bool

    def _get_PFPriority(self) -> bool:
        """
        {Yes/No*/True/False} Set inverter to operate with PF priority when in constant PF mode. If "Yes", value assigned to "WattPriority" is neglected. If controlled by an InvControl with either Volt-Var or DRC or both functions activated, PF priority is neglected and "WattPriority" is considered. Default = No.

        DSS property name: `PFPriority`, DSS property index: 36.
        """
        return self._lib.Obj_GetInt32(self._ptr, 36) != 0

    def _set_PFPriority(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 36, value, flags)

    PFPriority = property(_get_PFPriority, _set_PFPriority) # type: bool

    def _get_pctPMinNoVars(self) -> float:
        """
        Minimum active power as percentage of Pmpp under which there is no vars production/absorption.

        DSS property name: `%PMinNoVars`, DSS property index: 37.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 37)

    def _set_pctPMinNoVars(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 37, value, flags)

    pctPMinNoVars = property(_get_pctPMinNoVars, _set_pctPMinNoVars) # type: float

    def _get_pctPMinkvarMax(self) -> float:
        """
        Minimum active power as percentage of Pmpp that allows the inverter to produce/absorb reactive power up to its kvarMax or kvarMaxAbs.

        DSS property name: `%PMinkvarMax`, DSS property index: 38.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 38)

    def _set_pctPMinkvarMax(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 38, value, flags)

    pctPMinkvarMax = property(_get_pctPMinkvarMax, _set_pctPMinkvarMax) # type: float

    def _get_kvarMax(self) -> float:
        """
        Indicates the maximum reactive power GENERATION (un-signed numerical variable in kvar) for the inverter (as an un-signed value). Defaults to kVA rating of the inverter.

        DSS property name: `kvarMax`, DSS property index: 39.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 39)

    def _set_kvarMax(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 39, value, flags)

    kvarMax = property(_get_kvarMax, _set_kvarMax) # type: float

    def _get_kvarMaxAbs(self) -> float:
        """
        Indicates the maximum reactive power ABSORPTION (un-signed numerical variable in kvar) for the inverter (as an un-signed value). Defaults to kVA rating of the inverter.

        DSS property name: `kvarMaxAbs`, DSS property index: 40.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 40)

    def _set_kvarMaxAbs(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 40, value, flags)

    kvarMaxAbs = property(_get_kvarMaxAbs, _set_kvarMaxAbs) # type: float

    def _get_kVDC(self) -> float:
        """
        Indicates the rated voltage (kV) at the input of the inverter at the peak of PV energy production. The value is normally greater or equal to the kV base of the PV system. It is used for dynamics simulation ONLY.

        DSS property name: `kVDC`, DSS property index: 41.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 41)

    def _set_kVDC(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 41, value, flags)

    kVDC = property(_get_kVDC, _set_kVDC) # type: float

    def _get_Kp(self) -> float:
        """
        It is the proportional gain for the PI controller within the inverter. Use it to modify the controller response in dynamics simulation mode.

        DSS property name: `Kp`, DSS property index: 42.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 42)

    def _set_Kp(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 42, value, flags)

    Kp = property(_get_Kp, _set_Kp) # type: float

    def _get_PITol(self) -> float:
        """
        It is the tolerance (%) for the closed loop controller of the inverter. For dynamics simulation mode.

        DSS property name: `PITol`, DSS property index: 43.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 43)

    def _set_PITol(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 43, value, flags)

    PITol = property(_get_PITol, _set_PITol) # type: float

    def _get_SafeVoltage(self) -> float:
        """
        Indicates the voltage level (%) respect to the base voltage level for which the Inverter will operate. If this threshold is violated, the Inverter will enter safe mode (OFF). For dynamic simulation. By default is 80%

        DSS property name: `SafeVoltage`, DSS property index: 44.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 44)

    def _set_SafeVoltage(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 44, value, flags)

    SafeVoltage = property(_get_SafeVoltage, _set_SafeVoltage) # type: float

    def _get_SafeMode(self) -> bool:
        """
        (Read only) Indicates whether the inverter entered (Yes) or not (No) into Safe Mode.

        DSS property name: `SafeMode`, DSS property index: 45.
        """
        return self._lib.Obj_GetInt32(self._ptr, 45) != 0

    def _set_SafeMode(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 45, value, flags)

    SafeMode = property(_get_SafeMode, _set_SafeMode) # type: bool

    def _get_DynamicEq_str(self) -> str:
        """
        The name of the dynamic equation (DynamicExp) that will be used for defining the dynamic behavior of the generator. If not defined, the generator dynamics will follow the built-in dynamic equation.

        DSS property name: `DynamicEq`, DSS property index: 46.
        """
        return self._get_prop_string(46)

    def _set_DynamicEq_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(46, value, flags)

    DynamicEq_str = property(_get_DynamicEq_str, _set_DynamicEq_str) # type: str

    def _get_DynamicEq(self) -> DynamicExp:
        """
        The name of the dynamic equation (DynamicExp) that will be used for defining the dynamic behavior of the generator. If not defined, the generator dynamics will follow the built-in dynamic equation.

        DSS property name: `DynamicEq`, DSS property index: 46.
        """
        return self._get_obj(46, DynamicExp)

    def _set_DynamicEq(self, value: Union[AnyStr, DynamicExp], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(46, value, flags)
            return

        self._set_string_o(46, value, flags)

    DynamicEq = property(_get_DynamicEq, _set_DynamicEq) # type: DynamicExp

    def _get_DynOut(self) -> str:
        """
        The name of the variables within the Dynamic equation that will be used to govern the PVSystem dynamics. This PVsystem model requires 1 output from the dynamic equation:

            1. Current.

        The output variables need to be defined in the same order.

        DSS property name: `DynOut`, DSS property index: 47.
        """
        return self._get_prop_string(47)

    def _set_DynOut(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(47, value, flags)

    DynOut = property(_get_DynOut, _set_DynOut) # type: str

    def _get_ControlMode(self) -> enums.InverterControlMode:
        """
        Defines the control mode for the inverter. It can be one of {GFM | GFL*}. By default it is GFL (Grid Following Inverter). Use GFM (Grid Forming Inverter) for energizing islanded microgrids, but, if the device is connected to the grid, it is highly recommended to use GFL.

        GFM control mode disables any control action set by the InvControl device.

        DSS property name: `ControlMode`, DSS property index: 48.
        """
        return enums.InverterControlMode(self._lib.Obj_GetInt32(self._ptr, 48))

    def _set_ControlMode(self, value: Union[AnyStr, int, enums.InverterControlMode], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(48, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 48, value, flags)

    ControlMode = property(_get_ControlMode, _set_ControlMode) # type: enums.InverterControlMode

    def _get_ControlMode_str(self) -> str:
        """
        Defines the control mode for the inverter. It can be one of {GFM | GFL*}. By default it is GFL (Grid Following Inverter). Use GFM (Grid Forming Inverter) for energizing islanded microgrids, but, if the device is connected to the grid, it is highly recommended to use GFL.

        GFM control mode disables any control action set by the InvControl device.

        DSS property name: `ControlMode`, DSS property index: 48.
        """
        return self._get_prop_string(48)

    def _set_ControlMode_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_ControlMode(value, flags)

    ControlMode_str = property(_get_ControlMode_str, _set_ControlMode_str) # type: str

    def _get_AmpLimit(self) -> float:
        """
        The current limiter per phase for the IBR when operating in GFM mode. This limit is imposed to prevent the IBR to enter into Safe Mode when reaching the IBR power ratings.
        Once the IBR reaches this value, it remains there without moving into Safe Mode. This value needs to be set lower than the IBR Amps rating.

        DSS property name: `AmpLimit`, DSS property index: 49.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 49)

    def _set_AmpLimit(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 49, value, flags)

    AmpLimit = property(_get_AmpLimit, _set_AmpLimit) # type: float

    def _get_AmpLimitGain(self) -> float:
        """
        Use it for fine tunning the current limiter when active, by default is 0.8, it has to be a value between 0.1 and 1. This value allows users to fine tune the IBRs current limiter to match with the user requirements.

        DSS property name: `AmpLimitGain`, DSS property index: 50.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 50)

    def _set_AmpLimitGain(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 50, value, flags)

    AmpLimitGain = property(_get_AmpLimitGain, _set_AmpLimitGain) # type: float

    def _get_Spectrum_str(self) -> str:
        """
        Name of harmonic voltage or current spectrum for this PVSystem element. A harmonic voltage source is assumed for the inverter. Default value is "default", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 51.
        """
        return self._get_prop_string(51)

    def _set_Spectrum_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(51, value, flags)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str) # type: str

    def _get_Spectrum(self) -> SpectrumObj:
        """
        Name of harmonic voltage or current spectrum for this PVSystem element. A harmonic voltage source is assumed for the inverter. Default value is "default", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 51.
        """
        return self._get_obj(51, SpectrumObj)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(51, value, flags)
            return

        self._set_string_o(51, value, flags)

    Spectrum = property(_get_Spectrum, _set_Spectrum) # type: SpectrumObj

    def _get_BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 52.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 52)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 52, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float

    def _get_Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 53.
        """
        return self._lib.Obj_GetInt32(self._ptr, 53) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 53, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 54.
        """
        self._set_string_o(54, value)


class PVSystemProperties(TypedDict):
    Phases: int
    Bus1: AnyStr
    kV: float
    Irradiance: float
    Pmpp: float
    pctPmpp: float
    Temperature: float
    PF: float
    Conn: Union[AnyStr, int, enums.Connection]
    kvar: float
    kVA: float
    pctCutIn: float
    pctCutOut: float
    EffCurve: Union[AnyStr, XYcurve]
    PTCurve: Union[AnyStr, XYcurve]
    pctR: float
    pctX: float
    Model: Union[int, enums.PVSystemModel]
    VMinpu: float
    VMaxpu: float
    Balanced: bool
    LimitCurrent: bool
    Yearly: Union[AnyStr, LoadShape]
    Daily: Union[AnyStr, LoadShape]
    Duty: Union[AnyStr, LoadShape]
    TYearly: Union[AnyStr, TShape]
    TDaily: Union[AnyStr, TShape]
    TDuty: Union[AnyStr, TShape]
    Class: int
    UserModel: AnyStr
    UserData: AnyStr
    DebugTrace: bool
    VarFollowInverter: bool
    DutyStart: float
    WattPriority: bool
    PFPriority: bool
    pctPMinNoVars: float
    pctPMinkvarMax: float
    kvarMax: float
    kvarMaxAbs: float
    kVDC: float
    Kp: float
    PITol: float
    SafeVoltage: float
    SafeMode: bool
    DynamicEq: Union[AnyStr, DynamicExp]
    DynOut: AnyStr
    ControlMode: Union[AnyStr, int, enums.InverterControlMode]
    AmpLimit: float
    AmpLimitGain: float
    Spectrum: Union[AnyStr, SpectrumObj]
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class PVSystemBatch(DSSBatch, CircuitElementBatchMixin, PCElementBatchMixin):
    _cls_name = 'PVSystem'
    _obj_cls = PVSystem
    _cls_idx = 35

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)
       PCElementBatchMixin.__init__(self)

    def _get_Phases(self) -> BatchInt32ArrayProxy:
        """
        Number of Phases, this PVSystem element.  Power is evenly divided among phases.

        DSS property name: `Phases`, DSS property index: 1.
        """
        return BatchInt32ArrayProxy(self, 1)

    def _set_Phases(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(1, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: BatchInt32ArrayProxy

    def _get_Bus1(self) -> List[str]:
        """
        Bus to which the PVSystem element is connected.  May include specific node specification.

        DSS property name: `Bus1`, DSS property index: 2.
        """
        return self._get_batch_str_prop(2)

    def _set_Bus1(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(2, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: List[str]

    def _get_kV(self) -> BatchFloat64ArrayProxy:
        """
        Nominal rated (1.0 per unit) voltage, kV, for PVSystem element. For 2- and 3-phase PVSystem elements, specify phase-phase kV. Otherwise, specify actual kV across each branch of the PVSystem element. If 1-phase wye (star or LN), specify phase-neutral kV. If 1-phase delta or phase-phase connected, specify phase-phase kV.

        DSS property name: `kV`, DSS property index: 3.
        """
        return BatchFloat64ArrayProxy(self, 3)

    def _set_kV(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(3, value, flags)

    kV = property(_get_kV, _set_kV) # type: BatchFloat64ArrayProxy

    def _get_Irradiance(self) -> BatchFloat64ArrayProxy:
        """
        Get/set the present irradiance value in kW/sq-m. Used as base value for shape multipliers. Generally entered as peak value for the time period of interest and the yearly, daily, and duty load shape objects are defined as per unit multipliers (just like Loads/Generators).

        DSS property name: `Irradiance`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    def _set_Irradiance(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(4, value, flags)

    Irradiance = property(_get_Irradiance, _set_Irradiance) # type: BatchFloat64ArrayProxy

    def _get_Pmpp(self) -> BatchFloat64ArrayProxy:
        """
        Get/set the rated max power of the PV array for 1.0 kW/sq-m irradiance and a user-selected array temperature. The P-TCurve should be defined relative to the selected array temperature.

        DSS property name: `Pmpp`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    def _set_Pmpp(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(5, value, flags)

    Pmpp = property(_get_Pmpp, _set_Pmpp) # type: BatchFloat64ArrayProxy

    def _get_pctPmpp(self) -> BatchFloat64ArrayProxy:
        """
        Upper limit on active power as a percentage of Pmpp.

        DSS property name: `%Pmpp`, DSS property index: 6.
        """
        return BatchFloat64ArrayProxy(self, 6)

    def _set_pctPmpp(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(6, value, flags)

    pctPmpp = property(_get_pctPmpp, _set_pctPmpp) # type: BatchFloat64ArrayProxy

    def _get_Temperature(self) -> BatchFloat64ArrayProxy:
        """
        Get/set the present Temperature. Used as fixed value corresponding to PTCurve property. A multiplier is obtained from the Pmpp-Temp curve and applied to the nominal Pmpp from the irradiance to determine the net array output.

        DSS property name: `Temperature`, DSS property index: 7.
        """
        return BatchFloat64ArrayProxy(self, 7)

    def _set_Temperature(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(7, value, flags)

    Temperature = property(_get_Temperature, _set_Temperature) # type: BatchFloat64ArrayProxy

    def _get_PF(self) -> BatchFloat64ArrayProxy:
        """
        Nominally, the power factor for the output power. Default is 1.0. Setting this property will cause the inverter to operate in constant power factor mode.Enter negative when kW and kvar have opposite signs.
        A positive power factor signifies that the PVSystem element produces vars 
        as is typical for a generator.  

        DSS property name: `PF`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    def _set_PF(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(8, value, flags)

    PF = property(_get_PF, _set_PF) # type: BatchFloat64ArrayProxy

    def _get_Conn(self) -> BatchInt32ArrayProxy:
        """
        ={wye|LN|delta|LL}.  Default is wye.

        DSS property name: `Conn`, DSS property index: 9.
        """
        return BatchInt32ArrayProxy(self, 9)

    def _set_Conn(self, value: Union[AnyStr, int, enums.Connection, List[AnyStr], List[int], List[enums.Connection], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(9, value, flags)
            return

        self._set_batch_int32_array(9, value, flags)

    Conn = property(_get_Conn, _set_Conn) # type: BatchInt32ArrayProxy

    def _get_Conn_str(self) -> List[str]:
        """
        ={wye|LN|delta|LL}.  Default is wye.

        DSS property name: `Conn`, DSS property index: 9.
        """
        return self._get_batch_str_prop(9)

    def _set_Conn_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Conn(value, flags)

    Conn_str = property(_get_Conn_str, _set_Conn_str) # type: List[str]

    def _get_kvar(self) -> BatchFloat64ArrayProxy:
        """
        Get/set the present kvar value.  Setting this property forces the inverter to operate in constant kvar mode.

        DSS property name: `kvar`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    def _set_kvar(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(10, value, flags)

    kvar = property(_get_kvar, _set_kvar) # type: BatchFloat64ArrayProxy

    def _get_kVA(self) -> BatchFloat64ArrayProxy:
        """
        kVA rating of inverter. Used as the base for Dynamics mode and Harmonics mode values.

        DSS property name: `kVA`, DSS property index: 11.
        """
        return BatchFloat64ArrayProxy(self, 11)

    def _set_kVA(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(11, value, flags)

    kVA = property(_get_kVA, _set_kVA) # type: BatchFloat64ArrayProxy

    def _get_pctCutIn(self) -> BatchFloat64ArrayProxy:
        """
        % cut-in power -- % of kVA rating of inverter. When the inverter is OFF, the power from the array must be greater than this for the inverter to turn on.

        DSS property name: `%CutIn`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    def _set_pctCutIn(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(12, value, flags)

    pctCutIn = property(_get_pctCutIn, _set_pctCutIn) # type: BatchFloat64ArrayProxy

    def _get_pctCutOut(self) -> BatchFloat64ArrayProxy:
        """
        % cut-out power -- % of kVA rating of inverter. When the inverter is ON, the inverter turns OFF when the power from the array drops below this value.

        DSS property name: `%CutOut`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    def _set_pctCutOut(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(13, value, flags)

    pctCutOut = property(_get_pctCutOut, _set_pctCutOut) # type: BatchFloat64ArrayProxy

    def _get_EffCurve_str(self) -> List[str]:
        """
        An XYCurve object, previously defined, that describes the PER UNIT efficiency vs PER UNIT of rated kVA for the inverter. Inverter output power is discounted by the multiplier obtained from this curve.

        DSS property name: `EffCurve`, DSS property index: 14.
        """
        return self._get_batch_str_prop(14)

    def _set_EffCurve_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(14, value, flags)

    EffCurve_str = property(_get_EffCurve_str, _set_EffCurve_str) # type: List[str]

    def _get_EffCurve(self) -> List[XYcurve]:
        """
        An XYCurve object, previously defined, that describes the PER UNIT efficiency vs PER UNIT of rated kVA for the inverter. Inverter output power is discounted by the multiplier obtained from this curve.

        DSS property name: `EffCurve`, DSS property index: 14.
        """
        return self._get_batch_obj_prop(14)

    def _set_EffCurve(self, value: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(14, value, flags)

    EffCurve = property(_get_EffCurve, _set_EffCurve) # type: List[XYcurve]

    def _get_PTCurve_str(self) -> List[str]:
        """
        An XYCurve object, previously defined, that describes the PV array PER UNIT Pmpp vs Temperature curve. Temperature units must agree with the Temperature property and the Temperature shapes used for simulations. The Pmpp values are specified in per unit of the Pmpp value for 1 kW/sq-m irradiance. The value for the temperature at which Pmpp is defined should be 1.0. The net array power is determined by the irradiance * Pmpp * f(Temperature)

        DSS property name: `P-TCurve`, DSS property index: 15.
        """
        return self._get_batch_str_prop(15)

    def _set_PTCurve_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(15, value, flags)

    PTCurve_str = property(_get_PTCurve_str, _set_PTCurve_str) # type: List[str]

    def _get_PTCurve(self) -> List[XYcurve]:
        """
        An XYCurve object, previously defined, that describes the PV array PER UNIT Pmpp vs Temperature curve. Temperature units must agree with the Temperature property and the Temperature shapes used for simulations. The Pmpp values are specified in per unit of the Pmpp value for 1 kW/sq-m irradiance. The value for the temperature at which Pmpp is defined should be 1.0. The net array power is determined by the irradiance * Pmpp * f(Temperature)

        DSS property name: `P-TCurve`, DSS property index: 15.
        """
        return self._get_batch_obj_prop(15)

    def _set_PTCurve(self, value: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(15, value, flags)

    PTCurve = property(_get_PTCurve, _set_PTCurve) # type: List[XYcurve]

    def _get_pctR(self) -> BatchFloat64ArrayProxy:
        """
        Equivalent percent internal resistance, ohms. Default is 50%. Placed in series with internal voltage source for harmonics and dynamics modes. (Limits fault current to about 2 pu if not current limited -- see LimitCurrent) 

        DSS property name: `%R`, DSS property index: 16.
        """
        return BatchFloat64ArrayProxy(self, 16)

    def _set_pctR(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(16, value, flags)

    pctR = property(_get_pctR, _set_pctR) # type: BatchFloat64ArrayProxy

    def _get_pctX(self) -> BatchFloat64ArrayProxy:
        """
        Equivalent percent internal reactance, ohms. Default is 0%. Placed in series with internal voltage source for harmonics and dynamics modes. 

        DSS property name: `%X`, DSS property index: 17.
        """
        return BatchFloat64ArrayProxy(self, 17)

    def _set_pctX(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(17, value, flags)

    pctX = property(_get_pctX, _set_pctX) # type: BatchFloat64ArrayProxy

    def _get_Model(self) -> BatchInt32ArrayProxy:
        """
        Integer code (default=1) for the model to use for power output variation with voltage. Valid values are:

        1:PVSystem element injects a CONSTANT kW at specified power factor.
        2:PVSystem element is modeled as a CONSTANT ADMITTANCE.
        3:Compute load injection from User-written Model.

        DSS property name: `Model`, DSS property index: 18.
        """
        return BatchInt32ArrayProxy(self, 18)

    def _set_Model(self, value: Union[int, enums.PVSystemModel, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(18, value, flags)

    Model = property(_get_Model, _set_Model) # type: BatchInt32ArrayProxy

    def _get_VMinpu(self) -> BatchFloat64ArrayProxy:
        """
        Default = 0.90.  Minimum per unit voltage for which the Model is assumed to apply. Below this value, the load model reverts to a constant impedance model except for Dynamics model. In Dynamics mode, the current magnitude is limited to the value the power flow would compute for this voltage.

        DSS property name: `VMinpu`, DSS property index: 19.
        """
        return BatchFloat64ArrayProxy(self, 19)

    def _set_VMinpu(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(19, value, flags)

    VMinpu = property(_get_VMinpu, _set_VMinpu) # type: BatchFloat64ArrayProxy

    def _get_VMaxpu(self) -> BatchFloat64ArrayProxy:
        """
        Default = 1.10.  Maximum per unit voltage for which the Model is assumed to apply. Above this value, the load model reverts to a constant impedance model.

        DSS property name: `VMaxpu`, DSS property index: 20.
        """
        return BatchFloat64ArrayProxy(self, 20)

    def _set_VMaxpu(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(20, value, flags)

    VMaxpu = property(_get_VMaxpu, _set_VMaxpu) # type: BatchFloat64ArrayProxy

    def _get_Balanced(self) -> List[bool]:
        """
        {Yes | No*} Default is No.  Force balanced current only for 3-phase PVSystems. Forces zero- and negative-sequence to zero. 

        DSS property name: `Balanced`, DSS property index: 21.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(21)
        ]

    def _set_Balanced(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(21, value, flags)

    Balanced = property(_get_Balanced, _set_Balanced) # type: List[bool]

    def _get_LimitCurrent(self) -> List[bool]:
        """
        Limits current magnitude to Vminpu value for both 1-phase and 3-phase PVSystems similar to Generator Model 7. For 3-phase, limits the positive-sequence current but not the negative-sequence.

        DSS property name: `LimitCurrent`, DSS property index: 22.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(22)
        ]

    def _set_LimitCurrent(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(22, value, flags)

    LimitCurrent = property(_get_LimitCurrent, _set_LimitCurrent) # type: List[bool]

    def _get_Yearly_str(self) -> List[str]:
        """
        Dispatch shape to use for yearly simulations.  Must be previously defined as a Loadshape object. If this is not specified, the Daily dispatch shape, if any, is repeated during Yearly solution modes. In the default dispatch mode, the PVSystem element uses this loadshape to trigger State changes.

        DSS property name: `Yearly`, DSS property index: 23.
        """
        return self._get_batch_str_prop(23)

    def _set_Yearly_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(23, value, flags)

    Yearly_str = property(_get_Yearly_str, _set_Yearly_str) # type: List[str]

    def _get_Yearly(self) -> List[LoadShape]:
        """
        Dispatch shape to use for yearly simulations.  Must be previously defined as a Loadshape object. If this is not specified, the Daily dispatch shape, if any, is repeated during Yearly solution modes. In the default dispatch mode, the PVSystem element uses this loadshape to trigger State changes.

        DSS property name: `Yearly`, DSS property index: 23.
        """
        return self._get_batch_obj_prop(23)

    def _set_Yearly(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(23, value, flags)

    Yearly = property(_get_Yearly, _set_Yearly) # type: List[LoadShape]

    def _get_Daily_str(self) -> List[str]:
        """
        Dispatch shape to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically.  In the default dispatch mode, the PVSystem element uses this loadshape to trigger State changes.

        DSS property name: `Daily`, DSS property index: 24.
        """
        return self._get_batch_str_prop(24)

    def _set_Daily_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(24, value, flags)

    Daily_str = property(_get_Daily_str, _set_Daily_str) # type: List[str]

    def _get_Daily(self) -> List[LoadShape]:
        """
        Dispatch shape to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically.  In the default dispatch mode, the PVSystem element uses this loadshape to trigger State changes.

        DSS property name: `Daily`, DSS property index: 24.
        """
        return self._get_batch_obj_prop(24)

    def _set_Daily(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(24, value, flags)

    Daily = property(_get_Daily, _set_Daily) # type: List[LoadShape]

    def _get_Duty_str(self) -> List[str]:
        """
        Load shape to use for duty cycle dispatch simulations such as for solar ramp rate studies. Must be previously defined as a Loadshape object. Typically would have time intervals of 1-5 seconds. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.

        DSS property name: `Duty`, DSS property index: 25.
        """
        return self._get_batch_str_prop(25)

    def _set_Duty_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(25, value, flags)

    Duty_str = property(_get_Duty_str, _set_Duty_str) # type: List[str]

    def _get_Duty(self) -> List[LoadShape]:
        """
        Load shape to use for duty cycle dispatch simulations such as for solar ramp rate studies. Must be previously defined as a Loadshape object. Typically would have time intervals of 1-5 seconds. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.

        DSS property name: `Duty`, DSS property index: 25.
        """
        return self._get_batch_obj_prop(25)

    def _set_Duty(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(25, value, flags)

    Duty = property(_get_Duty, _set_Duty) # type: List[LoadShape]

    def _get_TYearly_str(self) -> List[str]:
        """
        Temperature shape to use for yearly simulations.  Must be previously defined as a TShape object. If this is not specified, the Daily dispatch shape, if any, is repeated during Yearly solution modes. The PVSystem element uses this TShape to determine the Pmpp from the Pmpp vs T curve. Units must agree with the Pmpp vs T curve.

        DSS property name: `TYearly`, DSS property index: 26.
        """
        return self._get_batch_str_prop(26)

    def _set_TYearly_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(26, value, flags)

    TYearly_str = property(_get_TYearly_str, _set_TYearly_str) # type: List[str]

    def _get_TYearly(self) -> List[TShape]:
        """
        Temperature shape to use for yearly simulations.  Must be previously defined as a TShape object. If this is not specified, the Daily dispatch shape, if any, is repeated during Yearly solution modes. The PVSystem element uses this TShape to determine the Pmpp from the Pmpp vs T curve. Units must agree with the Pmpp vs T curve.

        DSS property name: `TYearly`, DSS property index: 26.
        """
        return self._get_batch_obj_prop(26)

    def _set_TYearly(self, value: Union[AnyStr, TShape, List[AnyStr], List[TShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(26, value, flags)

    TYearly = property(_get_TYearly, _set_TYearly) # type: List[TShape]

    def _get_TDaily_str(self) -> List[str]:
        """
        Temperature shape to use for daily simulations.  Must be previously defined as a TShape object of 24 hrs, typically.  The PVSystem element uses this TShape to determine the Pmpp from the Pmpp vs T curve. Units must agree with the Pmpp vs T curve.

        DSS property name: `TDaily`, DSS property index: 27.
        """
        return self._get_batch_str_prop(27)

    def _set_TDaily_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(27, value, flags)

    TDaily_str = property(_get_TDaily_str, _set_TDaily_str) # type: List[str]

    def _get_TDaily(self) -> List[TShape]:
        """
        Temperature shape to use for daily simulations.  Must be previously defined as a TShape object of 24 hrs, typically.  The PVSystem element uses this TShape to determine the Pmpp from the Pmpp vs T curve. Units must agree with the Pmpp vs T curve.

        DSS property name: `TDaily`, DSS property index: 27.
        """
        return self._get_batch_obj_prop(27)

    def _set_TDaily(self, value: Union[AnyStr, TShape, List[AnyStr], List[TShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(27, value, flags)

    TDaily = property(_get_TDaily, _set_TDaily) # type: List[TShape]

    def _get_TDuty_str(self) -> List[str]:
        """
        Temperature shape to use for duty cycle dispatch simulations such as for solar ramp rate studies. Must be previously defined as a TShape object. Typically would have time intervals of 1-5 seconds. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat. The PVSystem model uses this TShape to determine the Pmpp from the Pmpp vs T curve. Units must agree with the Pmpp vs T curve.

        DSS property name: `TDuty`, DSS property index: 28.
        """
        return self._get_batch_str_prop(28)

    def _set_TDuty_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(28, value, flags)

    TDuty_str = property(_get_TDuty_str, _set_TDuty_str) # type: List[str]

    def _get_TDuty(self) -> List[TShape]:
        """
        Temperature shape to use for duty cycle dispatch simulations such as for solar ramp rate studies. Must be previously defined as a TShape object. Typically would have time intervals of 1-5 seconds. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat. The PVSystem model uses this TShape to determine the Pmpp from the Pmpp vs T curve. Units must agree with the Pmpp vs T curve.

        DSS property name: `TDuty`, DSS property index: 28.
        """
        return self._get_batch_obj_prop(28)

    def _set_TDuty(self, value: Union[AnyStr, TShape, List[AnyStr], List[TShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(28, value, flags)

    TDuty = property(_get_TDuty, _set_TDuty) # type: List[TShape]

    def _get_Class(self) -> BatchInt32ArrayProxy:
        """
        An arbitrary integer number representing the class of PVSystem element so that PVSystem values may be segregated by class.

        DSS property name: `Class`, DSS property index: 29.
        """
        return BatchInt32ArrayProxy(self, 29)

    def _set_Class(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(29, value, flags)

    Class = property(_get_Class, _set_Class) # type: BatchInt32ArrayProxy

    def _get_UserModel(self) -> List[str]:
        """
        Name of DLL containing user-written model, which computes the terminal currents for Dynamics studies, overriding the default model.  Set to "none" to negate previous setting.

        DSS property name: `UserModel`, DSS property index: 30.
        """
        return self._get_batch_str_prop(30)

    def _set_UserModel(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(30, value, flags)

    UserModel = property(_get_UserModel, _set_UserModel) # type: List[str]

    def _get_UserData(self) -> List[str]:
        """
        String (in quotes or parentheses) that gets passed to user-written model for defining the data required for that model.

        DSS property name: `UserData`, DSS property index: 31.
        """
        return self._get_batch_str_prop(31)

    def _set_UserData(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(31, value, flags)

    UserData = property(_get_UserData, _set_UserData) # type: List[str]

    def _get_DebugTrace(self) -> List[bool]:
        """
        {Yes | No }  Default is no.  Turn this on to capture the progress of the PVSystem model for each iteration.  Creates a separate file for each PVSystem element named "PVSystem_name.csv".

        DSS property name: `DebugTrace`, DSS property index: 32.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(32)
        ]

    def _set_DebugTrace(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(32, value, flags)

    DebugTrace = property(_get_DebugTrace, _set_DebugTrace) # type: List[bool]

    def _get_VarFollowInverter(self) -> List[bool]:
        """
        Boolean variable (Yes|No) or (True|False). Defaults to False which indicates that the reactive power generation/absorption does not respect the inverter status.When set to True, the PVSystem reactive power generation/absorption will cease when the inverter status is off, due to panel kW dropping below %Cutout.  The reactive power generation/absorption will begin again when the panel kW is above %Cutin.  When set to False, the PVSystem will generate/absorb reactive power regardless of the status of the inverter.

        DSS property name: `VarFollowInverter`, DSS property index: 33.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(33)
        ]

    def _set_VarFollowInverter(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(33, value, flags)

    VarFollowInverter = property(_get_VarFollowInverter, _set_VarFollowInverter) # type: List[bool]

    def _get_DutyStart(self) -> BatchFloat64ArrayProxy:
        """
        Starting time offset [hours] into the duty cycle shape for this PVSystem, defaults to 0

        DSS property name: `DutyStart`, DSS property index: 34.
        """
        return BatchFloat64ArrayProxy(self, 34)

    def _set_DutyStart(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(34, value, flags)

    DutyStart = property(_get_DutyStart, _set_DutyStart) # type: BatchFloat64ArrayProxy

    def _get_WattPriority(self) -> List[bool]:
        """
        {Yes/No*/True/False} Set inverter to watt priority instead of the default var priority

        DSS property name: `WattPriority`, DSS property index: 35.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(35)
        ]

    def _set_WattPriority(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(35, value, flags)

    WattPriority = property(_get_WattPriority, _set_WattPriority) # type: List[bool]

    def _get_PFPriority(self) -> List[bool]:
        """
        {Yes/No*/True/False} Set inverter to operate with PF priority when in constant PF mode. If "Yes", value assigned to "WattPriority" is neglected. If controlled by an InvControl with either Volt-Var or DRC or both functions activated, PF priority is neglected and "WattPriority" is considered. Default = No.

        DSS property name: `PFPriority`, DSS property index: 36.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(36)
        ]

    def _set_PFPriority(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(36, value, flags)

    PFPriority = property(_get_PFPriority, _set_PFPriority) # type: List[bool]

    def _get_pctPMinNoVars(self) -> BatchFloat64ArrayProxy:
        """
        Minimum active power as percentage of Pmpp under which there is no vars production/absorption.

        DSS property name: `%PMinNoVars`, DSS property index: 37.
        """
        return BatchFloat64ArrayProxy(self, 37)

    def _set_pctPMinNoVars(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(37, value, flags)

    pctPMinNoVars = property(_get_pctPMinNoVars, _set_pctPMinNoVars) # type: BatchFloat64ArrayProxy

    def _get_pctPMinkvarMax(self) -> BatchFloat64ArrayProxy:
        """
        Minimum active power as percentage of Pmpp that allows the inverter to produce/absorb reactive power up to its kvarMax or kvarMaxAbs.

        DSS property name: `%PMinkvarMax`, DSS property index: 38.
        """
        return BatchFloat64ArrayProxy(self, 38)

    def _set_pctPMinkvarMax(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(38, value, flags)

    pctPMinkvarMax = property(_get_pctPMinkvarMax, _set_pctPMinkvarMax) # type: BatchFloat64ArrayProxy

    def _get_kvarMax(self) -> BatchFloat64ArrayProxy:
        """
        Indicates the maximum reactive power GENERATION (un-signed numerical variable in kvar) for the inverter (as an un-signed value). Defaults to kVA rating of the inverter.

        DSS property name: `kvarMax`, DSS property index: 39.
        """
        return BatchFloat64ArrayProxy(self, 39)

    def _set_kvarMax(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(39, value, flags)

    kvarMax = property(_get_kvarMax, _set_kvarMax) # type: BatchFloat64ArrayProxy

    def _get_kvarMaxAbs(self) -> BatchFloat64ArrayProxy:
        """
        Indicates the maximum reactive power ABSORPTION (un-signed numerical variable in kvar) for the inverter (as an un-signed value). Defaults to kVA rating of the inverter.

        DSS property name: `kvarMaxAbs`, DSS property index: 40.
        """
        return BatchFloat64ArrayProxy(self, 40)

    def _set_kvarMaxAbs(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(40, value, flags)

    kvarMaxAbs = property(_get_kvarMaxAbs, _set_kvarMaxAbs) # type: BatchFloat64ArrayProxy

    def _get_kVDC(self) -> BatchFloat64ArrayProxy:
        """
        Indicates the rated voltage (kV) at the input of the inverter at the peak of PV energy production. The value is normally greater or equal to the kV base of the PV system. It is used for dynamics simulation ONLY.

        DSS property name: `kVDC`, DSS property index: 41.
        """
        return BatchFloat64ArrayProxy(self, 41)

    def _set_kVDC(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(41, value, flags)

    kVDC = property(_get_kVDC, _set_kVDC) # type: BatchFloat64ArrayProxy

    def _get_Kp(self) -> BatchFloat64ArrayProxy:
        """
        It is the proportional gain for the PI controller within the inverter. Use it to modify the controller response in dynamics simulation mode.

        DSS property name: `Kp`, DSS property index: 42.
        """
        return BatchFloat64ArrayProxy(self, 42)

    def _set_Kp(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(42, value, flags)

    Kp = property(_get_Kp, _set_Kp) # type: BatchFloat64ArrayProxy

    def _get_PITol(self) -> BatchFloat64ArrayProxy:
        """
        It is the tolerance (%) for the closed loop controller of the inverter. For dynamics simulation mode.

        DSS property name: `PITol`, DSS property index: 43.
        """
        return BatchFloat64ArrayProxy(self, 43)

    def _set_PITol(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(43, value, flags)

    PITol = property(_get_PITol, _set_PITol) # type: BatchFloat64ArrayProxy

    def _get_SafeVoltage(self) -> BatchFloat64ArrayProxy:
        """
        Indicates the voltage level (%) respect to the base voltage level for which the Inverter will operate. If this threshold is violated, the Inverter will enter safe mode (OFF). For dynamic simulation. By default is 80%

        DSS property name: `SafeVoltage`, DSS property index: 44.
        """
        return BatchFloat64ArrayProxy(self, 44)

    def _set_SafeVoltage(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(44, value, flags)

    SafeVoltage = property(_get_SafeVoltage, _set_SafeVoltage) # type: BatchFloat64ArrayProxy

    def _get_SafeMode(self) -> List[bool]:
        """
        (Read only) Indicates whether the inverter entered (Yes) or not (No) into Safe Mode.

        DSS property name: `SafeMode`, DSS property index: 45.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(45)
        ]

    def _set_SafeMode(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(45, value, flags)

    SafeMode = property(_get_SafeMode, _set_SafeMode) # type: List[bool]

    def _get_DynamicEq_str(self) -> List[str]:
        """
        The name of the dynamic equation (DynamicExp) that will be used for defining the dynamic behavior of the generator. If not defined, the generator dynamics will follow the built-in dynamic equation.

        DSS property name: `DynamicEq`, DSS property index: 46.
        """
        return self._get_batch_str_prop(46)

    def _set_DynamicEq_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(46, value, flags)

    DynamicEq_str = property(_get_DynamicEq_str, _set_DynamicEq_str) # type: List[str]

    def _get_DynamicEq(self) -> List[DynamicExp]:
        """
        The name of the dynamic equation (DynamicExp) that will be used for defining the dynamic behavior of the generator. If not defined, the generator dynamics will follow the built-in dynamic equation.

        DSS property name: `DynamicEq`, DSS property index: 46.
        """
        return self._get_batch_obj_prop(46)

    def _set_DynamicEq(self, value: Union[AnyStr, DynamicExp, List[AnyStr], List[DynamicExp]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(46, value, flags)

    DynamicEq = property(_get_DynamicEq, _set_DynamicEq) # type: List[DynamicExp]

    def _get_DynOut(self) -> List[str]:
        """
        The name of the variables within the Dynamic equation that will be used to govern the PVSystem dynamics. This PVsystem model requires 1 output from the dynamic equation:

            1. Current.

        The output variables need to be defined in the same order.

        DSS property name: `DynOut`, DSS property index: 47.
        """
        return self._get_batch_str_prop(47)

    def _set_DynOut(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(47, value, flags)

    DynOut = property(_get_DynOut, _set_DynOut) # type: List[str]

    def _get_ControlMode(self) -> BatchInt32ArrayProxy:
        """
        Defines the control mode for the inverter. It can be one of {GFM | GFL*}. By default it is GFL (Grid Following Inverter). Use GFM (Grid Forming Inverter) for energizing islanded microgrids, but, if the device is connected to the grid, it is highly recommended to use GFL.

        GFM control mode disables any control action set by the InvControl device.

        DSS property name: `ControlMode`, DSS property index: 48.
        """
        return BatchInt32ArrayProxy(self, 48)

    def _set_ControlMode(self, value: Union[AnyStr, int, enums.InverterControlMode, List[AnyStr], List[int], List[enums.InverterControlMode], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(48, value, flags)
            return

        self._set_batch_int32_array(48, value, flags)

    ControlMode = property(_get_ControlMode, _set_ControlMode) # type: BatchInt32ArrayProxy

    def _get_ControlMode_str(self) -> List[str]:
        """
        Defines the control mode for the inverter. It can be one of {GFM | GFL*}. By default it is GFL (Grid Following Inverter). Use GFM (Grid Forming Inverter) for energizing islanded microgrids, but, if the device is connected to the grid, it is highly recommended to use GFL.

        GFM control mode disables any control action set by the InvControl device.

        DSS property name: `ControlMode`, DSS property index: 48.
        """
        return self._get_batch_str_prop(48)

    def _set_ControlMode_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_ControlMode(value, flags)

    ControlMode_str = property(_get_ControlMode_str, _set_ControlMode_str) # type: List[str]

    def _get_AmpLimit(self) -> BatchFloat64ArrayProxy:
        """
        The current limiter per phase for the IBR when operating in GFM mode. This limit is imposed to prevent the IBR to enter into Safe Mode when reaching the IBR power ratings.
        Once the IBR reaches this value, it remains there without moving into Safe Mode. This value needs to be set lower than the IBR Amps rating.

        DSS property name: `AmpLimit`, DSS property index: 49.
        """
        return BatchFloat64ArrayProxy(self, 49)

    def _set_AmpLimit(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(49, value, flags)

    AmpLimit = property(_get_AmpLimit, _set_AmpLimit) # type: BatchFloat64ArrayProxy

    def _get_AmpLimitGain(self) -> BatchFloat64ArrayProxy:
        """
        Use it for fine tunning the current limiter when active, by default is 0.8, it has to be a value between 0.1 and 1. This value allows users to fine tune the IBRs current limiter to match with the user requirements.

        DSS property name: `AmpLimitGain`, DSS property index: 50.
        """
        return BatchFloat64ArrayProxy(self, 50)

    def _set_AmpLimitGain(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(50, value, flags)

    AmpLimitGain = property(_get_AmpLimitGain, _set_AmpLimitGain) # type: BatchFloat64ArrayProxy

    def _get_Spectrum_str(self) -> List[str]:
        """
        Name of harmonic voltage or current spectrum for this PVSystem element. A harmonic voltage source is assumed for the inverter. Default value is "default", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 51.
        """
        return self._get_batch_str_prop(51)

    def _set_Spectrum_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(51, value, flags)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str) # type: List[str]

    def _get_Spectrum(self) -> List[SpectrumObj]:
        """
        Name of harmonic voltage or current spectrum for this PVSystem element. A harmonic voltage source is assumed for the inverter. Default value is "default", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 51.
        """
        return self._get_batch_obj_prop(51)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(51, value, flags)

    Spectrum = property(_get_Spectrum, _set_Spectrum) # type: List[SpectrumObj]

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 52.
        """
        return BatchFloat64ArrayProxy(self, 52)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(52, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy

    def _get_Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 53.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(53)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(53, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 54.
        """
        self._set_batch_string(54, value, flags)

class PVSystemBatchProperties(TypedDict):
    Phases: Union[int, Int32Array]
    Bus1: Union[AnyStr, List[AnyStr]]
    kV: Union[float, Float64Array]
    Irradiance: Union[float, Float64Array]
    Pmpp: Union[float, Float64Array]
    pctPmpp: Union[float, Float64Array]
    Temperature: Union[float, Float64Array]
    PF: Union[float, Float64Array]
    Conn: Union[AnyStr, int, enums.Connection, List[AnyStr], List[int], List[enums.Connection], Int32Array]
    kvar: Union[float, Float64Array]
    kVA: Union[float, Float64Array]
    pctCutIn: Union[float, Float64Array]
    pctCutOut: Union[float, Float64Array]
    EffCurve: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]
    PTCurve: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]
    pctR: Union[float, Float64Array]
    pctX: Union[float, Float64Array]
    Model: Union[int, enums.PVSystemModel, Int32Array]
    VMinpu: Union[float, Float64Array]
    VMaxpu: Union[float, Float64Array]
    Balanced: bool
    LimitCurrent: bool
    Yearly: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    Daily: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    Duty: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    TYearly: Union[AnyStr, TShape, List[AnyStr], List[TShape]]
    TDaily: Union[AnyStr, TShape, List[AnyStr], List[TShape]]
    TDuty: Union[AnyStr, TShape, List[AnyStr], List[TShape]]
    Class: Union[int, Int32Array]
    UserModel: Union[AnyStr, List[AnyStr]]
    UserData: Union[AnyStr, List[AnyStr]]
    DebugTrace: bool
    VarFollowInverter: bool
    DutyStart: Union[float, Float64Array]
    WattPriority: bool
    PFPriority: bool
    pctPMinNoVars: Union[float, Float64Array]
    pctPMinkvarMax: Union[float, Float64Array]
    kvarMax: Union[float, Float64Array]
    kvarMaxAbs: Union[float, Float64Array]
    kVDC: Union[float, Float64Array]
    Kp: Union[float, Float64Array]
    PITol: Union[float, Float64Array]
    SafeVoltage: Union[float, Float64Array]
    SafeMode: bool
    DynamicEq: Union[AnyStr, DynamicExp, List[AnyStr], List[DynamicExp]]
    DynOut: Union[AnyStr, List[AnyStr]]
    ControlMode: Union[AnyStr, int, enums.InverterControlMode, List[AnyStr], List[int], List[enums.InverterControlMode], Int32Array]
    AmpLimit: Union[float, Float64Array]
    AmpLimitGain: Union[float, Float64Array]
    Spectrum: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IPVSystem(IDSSObj, PVSystemBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, PVSystem, PVSystemBatch)
        PVSystemBatch.__init__(self, self._api_util, sync_cls_idx=PVSystem._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> PVSystem:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[PVSystemProperties]) -> PVSystem:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[PVSystemBatchProperties]) -> PVSystemBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
