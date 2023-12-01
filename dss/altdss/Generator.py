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

class Generator(DSSObj, CircuitElementMixin, PCElementMixin, ElementHasRegistersMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots + PCElementMixin._extra_slots + ElementHasRegistersMixin._extra_slots
    _cls_name = 'Generator'
    _cls_idx = 27
    _cls_prop_idx = {
        'phases': 1,
        'bus1': 2,
        'kv': 3,
        'kw': 4,
        'pf': 5,
        'kvar': 6,
        'model': 7,
        'vminpu': 8,
        'vmaxpu': 9,
        'yearly': 10,
        'daily': 11,
        'duty': 12,
        'dispmode': 13,
        'dispvalue': 14,
        'conn': 15,
        'status': 16,
        'cls': 17,
        'class': 17,
        'vpu': 18,
        'maxkvar': 19,
        'minkvar': 20,
        'pvfactor': 21,
        'forceon': 22,
        'kva': 23,
        'mva': 24,
        'xd': 25,
        'xdp': 26,
        'xdpp': 27,
        'h': 28,
        'd': 29,
        'usermodel': 30,
        'userdata': 31,
        'shaftmodel': 32,
        'shaftdata': 33,
        'dutystart': 34,
        'debugtrace': 35,
        'balanced': 36,
        'xrdp': 37,
        'usefuel': 38,
        'fuelkwh': 39,
        'pctfuel': 40,
        '%fuel': 40,
        'pctreserve': 41,
        '%reserve': 41,
        'refuel': 42,
        'dynamiceq': 43,
        'dynout': 44,
        'spectrum': 45,
        'basefreq': 46,
        'enabled': 47,
        'like': 48,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)
       PCElementMixin.__init__(self)
       ElementHasRegistersMixin.__init__(self)

    def _get_Phases(self) -> int:
        """
        Number of Phases, this Generator.  Power is evenly divided among phases.

        DSS property name: `Phases`, DSS property index: 1.
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    def _set_Phases(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 1, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: int

    def _get_Bus1(self) -> str:
        """
        Bus to which the Generator is connected.  May include specific node specification.

        DSS property name: `Bus1`, DSS property index: 2.
        """
        return self._get_prop_string(2)

    def _set_Bus1(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(2, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: str

    def _get_kV(self) -> float:
        """
        Nominal rated (1.0 per unit) voltage, kV, for Generator. For 2- and 3-phase Generators, specify phase-phase kV. Otherwise, for phases=1 or phases>3, specify actual kV across each branch of the Generator. If wye (star), specify phase-neutral kV. If delta or phase-phase connected, specify phase-phase kV.

        DSS property name: `kV`, DSS property index: 3.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    def _set_kV(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 3, value, flags)

    kV = property(_get_kV, _set_kV) # type: float

    def _get_kW(self) -> float:
        """
        Total base kW for the Generator.  A positive value denotes power coming OUT of the element, 
        which is the opposite of a load. This value is modified depending on the dispatch mode. Unaffected by the global load multiplier and growth curves. If you want there to be more generation, you must add more generators or change this value.

        DSS property name: `kW`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    def _set_kW(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 4, value, flags)

    kW = property(_get_kW, _set_kW) # type: float

    def _get_PF(self) -> float:
        """
        Generator power factor. Default is 0.80. Enter negative for leading powerfactor (when kW and kvar have opposite signs.)
        A positive power factor for a generator signifies that the generator produces vars 
        as is typical for a synchronous generator.  Induction machines would be 
        specified with a negative power factor.

        DSS property name: `PF`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    def _set_PF(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 5, value, flags)

    PF = property(_get_PF, _set_PF) # type: float

    def _get_kvar(self) -> float:
        """
        Specify the base kvar.  Alternative to specifying the power factor.  Side effect:  the power factor value is altered to agree based on present value of kW.

        DSS property name: `kvar`, DSS property index: 6.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    def _set_kvar(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 6, value, flags)

    kvar = property(_get_kvar, _set_kvar) # type: float

    def _get_Model(self) -> enums.GeneratorModel:
        """
        Integer code for the model to use for generation variation with voltage. Valid values are:

        1:Generator injects a constant kW at specified power factor.
        2:Generator is modeled as a constant admittance.
        3:Const kW, constant kV.  Somewhat like a conventional transmission power flow P-V generator.
        4:Const kW, Fixed Q (Q never varies)
        5:Const kW, Fixed Q(as a constant reactance)
        6:Compute load injection from User-written Model.(see usage of Xd, Xdp)
        7:Constant kW, kvar, but current-limited below Vminpu. Approximates a simple inverter. See also Balanced.

        DSS property name: `Model`, DSS property index: 7.
        """
        return enums.GeneratorModel(self._lib.Obj_GetInt32(self._ptr, 7))

    def _set_Model(self, value: Union[int, enums.GeneratorModel], flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 7, value, flags)

    Model = property(_get_Model, _set_Model) # type: enums.GeneratorModel

    def _get_VMinpu(self) -> float:
        """
        Default = 0.90.  Minimum per unit voltage for which the Model is assumed to apply. Below this value, the load model reverts to a constant impedance model. For model 7, the current is limited to the value computed for constant power at Vminpu.

        DSS property name: `VMinpu`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    def _set_VMinpu(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 8, value, flags)

    VMinpu = property(_get_VMinpu, _set_VMinpu) # type: float

    def _get_VMaxpu(self) -> float:
        """
        Default = 1.10.  Maximum per unit voltage for which the Model is assumed to apply. Above this value, the load model reverts to a constant impedance model.

        DSS property name: `VMaxpu`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    def _set_VMaxpu(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 9, value, flags)

    VMaxpu = property(_get_VMaxpu, _set_VMaxpu) # type: float

    def _get_Yearly_str(self) -> str:
        """
        Dispatch shape to use for yearly simulations.  Must be previously defined as a Loadshape object. If this is not specified, a constant value is assumed (no variation). If the generator is assumed to be ON continuously, specify Status=FIXED, or designate a curve that is 1.0 per unit at all times. Set to NONE to reset to no loadshape. Nominally for 8760 simulations.  If there are fewer points in the designated shape than the number of points in the solution, the curve is repeated.

        DSS property name: `Yearly`, DSS property index: 10.
        """
        return self._get_prop_string(10)

    def _set_Yearly_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(10, value, flags)

    Yearly_str = property(_get_Yearly_str, _set_Yearly_str) # type: str

    def _get_Yearly(self) -> LoadShape:
        """
        Dispatch shape to use for yearly simulations.  Must be previously defined as a Loadshape object. If this is not specified, a constant value is assumed (no variation). If the generator is assumed to be ON continuously, specify Status=FIXED, or designate a curve that is 1.0 per unit at all times. Set to NONE to reset to no loadshape. Nominally for 8760 simulations.  If there are fewer points in the designated shape than the number of points in the solution, the curve is repeated.

        DSS property name: `Yearly`, DSS property index: 10.
        """
        return self._get_obj(10, LoadShape)

    def _set_Yearly(self, value: Union[AnyStr, LoadShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(10, value, flags)
            return

        self._set_string_o(10, value, flags)

    Yearly = property(_get_Yearly, _set_Yearly) # type: LoadShape

    def _get_Daily_str(self) -> str:
        """
        Dispatch shape to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically.  If generator is assumed to be ON continuously, specify Status=FIXED, or designate a Loadshape object that is 1.0 per unit for all hours. Set to NONE to reset to no loadshape. 

        DSS property name: `Daily`, DSS property index: 11.
        """
        return self._get_prop_string(11)

    def _set_Daily_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(11, value, flags)

    Daily_str = property(_get_Daily_str, _set_Daily_str) # type: str

    def _get_Daily(self) -> LoadShape:
        """
        Dispatch shape to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically.  If generator is assumed to be ON continuously, specify Status=FIXED, or designate a Loadshape object that is 1.0 per unit for all hours. Set to NONE to reset to no loadshape. 

        DSS property name: `Daily`, DSS property index: 11.
        """
        return self._get_obj(11, LoadShape)

    def _set_Daily(self, value: Union[AnyStr, LoadShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(11, value, flags)
            return

        self._set_string_o(11, value, flags)

    Daily = property(_get_Daily, _set_Daily) # type: LoadShape

    def _get_Duty_str(self) -> str:
        """
        Load shape to use for duty cycle dispatch simulations such as for wind generation. Must be previously defined as a Loadshape object. Typically would have time intervals less than 1 hr -- perhaps, in seconds. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.

        DSS property name: `Duty`, DSS property index: 12.
        """
        return self._get_prop_string(12)

    def _set_Duty_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(12, value, flags)

    Duty_str = property(_get_Duty_str, _set_Duty_str) # type: str

    def _get_Duty(self) -> LoadShape:
        """
        Load shape to use for duty cycle dispatch simulations such as for wind generation. Must be previously defined as a Loadshape object. Typically would have time intervals less than 1 hr -- perhaps, in seconds. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.

        DSS property name: `Duty`, DSS property index: 12.
        """
        return self._get_obj(12, LoadShape)

    def _set_Duty(self, value: Union[AnyStr, LoadShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(12, value, flags)
            return

        self._set_string_o(12, value, flags)

    Duty = property(_get_Duty, _set_Duty) # type: LoadShape

    def _get_DispMode(self) -> enums.GeneratorDispatchMode:
        """
        {Default* | Loadlevel | Price } Default = Default. Dispatch mode. In default mode, gen is either always on or follows dispatch curve as specified. Otherwise, the gen comes on when either the global default load level (Loadshape "default") or the price level exceeds the dispatch value.

        DSS property name: `DispMode`, DSS property index: 13.
        """
        return enums.GeneratorDispatchMode(self._lib.Obj_GetInt32(self._ptr, 13))

    def _set_DispMode(self, value: Union[AnyStr, int, enums.GeneratorDispatchMode], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(13, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 13, value, flags)

    DispMode = property(_get_DispMode, _set_DispMode) # type: enums.GeneratorDispatchMode

    def _get_DispMode_str(self) -> str:
        """
        {Default* | Loadlevel | Price } Default = Default. Dispatch mode. In default mode, gen is either always on or follows dispatch curve as specified. Otherwise, the gen comes on when either the global default load level (Loadshape "default") or the price level exceeds the dispatch value.

        DSS property name: `DispMode`, DSS property index: 13.
        """
        return self._get_prop_string(13)

    def _set_DispMode_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_DispMode(value, flags)

    DispMode_str = property(_get_DispMode_str, _set_DispMode_str) # type: str

    def _get_DispValue(self) -> float:
        """
        Dispatch value. 
        If = 0.0 (default) then Generator follow dispatch curves, if any. 
        If > 0  then Generator is ON only when either the price signal (in Price dispatch mode) exceeds this value or the active circuit load multiplier * "default" loadshape value * the default yearly growth factor exceeds this value.  Then the generator follows dispatch curves (duty, daily, or yearly), if any (see also Status).

        DSS property name: `DispValue`, DSS property index: 14.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    def _set_DispValue(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 14, value, flags)

    DispValue = property(_get_DispValue, _set_DispValue) # type: float

    def _get_Conn(self) -> enums.Connection:
        """
        ={wye|LN|delta|LL}.  Default is wye.

        DSS property name: `Conn`, DSS property index: 15.
        """
        return enums.Connection(self._lib.Obj_GetInt32(self._ptr, 15))

    def _set_Conn(self, value: Union[AnyStr, int, enums.Connection], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(15, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 15, value, flags)

    Conn = property(_get_Conn, _set_Conn) # type: enums.Connection

    def _get_Conn_str(self) -> str:
        """
        ={wye|LN|delta|LL}.  Default is wye.

        DSS property name: `Conn`, DSS property index: 15.
        """
        return self._get_prop_string(15)

    def _set_Conn_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Conn(value, flags)

    Conn_str = property(_get_Conn_str, _set_Conn_str) # type: str

    def _get_Status(self) -> enums.GeneratorStatus:
        """
        ={Fixed | Variable*}.  If Fixed, then dispatch multipliers do not apply. The generator is alway at full power when it is ON.  Default is Variable  (follows curves).

        DSS property name: `Status`, DSS property index: 16.
        """
        return enums.GeneratorStatus(self._lib.Obj_GetInt32(self._ptr, 16))

    def _set_Status(self, value: Union[AnyStr, int, enums.GeneratorStatus], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(16, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 16, value, flags)

    Status = property(_get_Status, _set_Status) # type: enums.GeneratorStatus

    def _get_Status_str(self) -> str:
        """
        ={Fixed | Variable*}.  If Fixed, then dispatch multipliers do not apply. The generator is alway at full power when it is ON.  Default is Variable  (follows curves).

        DSS property name: `Status`, DSS property index: 16.
        """
        return self._get_prop_string(16)

    def _set_Status_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Status(value, flags)

    Status_str = property(_get_Status_str, _set_Status_str) # type: str

    def _get_Class(self) -> int:
        """
        An arbitrary integer number representing the class of Generator so that Generator values may be segregated by class.

        DSS property name: `Class`, DSS property index: 17.
        """
        return self._lib.Obj_GetInt32(self._ptr, 17)

    def _set_Class(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 17, value, flags)

    Class = property(_get_Class, _set_Class) # type: int

    def _get_Vpu(self) -> float:
        """
        Per Unit voltage set point for Model = 3  (typical power flow model).  Default is 1.0. 

        DSS property name: `Vpu`, DSS property index: 18.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    def _set_Vpu(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 18, value, flags)

    Vpu = property(_get_Vpu, _set_Vpu) # type: float

    def _get_Maxkvar(self) -> float:
        """
        Maximum kvar limit for Model = 3.  Defaults to twice the specified load kvar.  Always reset this if you change PF or kvar properties.

        DSS property name: `Maxkvar`, DSS property index: 19.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    def _set_Maxkvar(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 19, value, flags)

    Maxkvar = property(_get_Maxkvar, _set_Maxkvar) # type: float

    def _get_Minkvar(self) -> float:
        """
        Minimum kvar limit for Model = 3. Enter a negative number if generator can absorb vars. Defaults to negative of Maxkvar.  Always reset this if you change PF or kvar properties.

        DSS property name: `Minkvar`, DSS property index: 20.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    def _set_Minkvar(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 20, value, flags)

    Minkvar = property(_get_Minkvar, _set_Minkvar) # type: float

    def _get_PVFactor(self) -> float:
        """
        Deceleration factor for P-V generator model (Model=3).  Default is 0.1. If the circuit converges easily, you may want to use a higher number such as 1.0. Use a lower number if solution diverges. Use Debugtrace=yes to create a file that will trace the convergence of a generator model.

        DSS property name: `PVFactor`, DSS property index: 21.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    def _set_PVFactor(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 21, value, flags)

    PVFactor = property(_get_PVFactor, _set_PVFactor) # type: float

    def _get_ForceOn(self) -> bool:
        """
        {Yes | No}  Forces generator ON despite requirements of other dispatch modes. Stays ON until this property is set to NO, or an internal algorithm cancels the forced ON state.

        DSS property name: `ForceOn`, DSS property index: 22.
        """
        return self._lib.Obj_GetInt32(self._ptr, 22) != 0

    def _set_ForceOn(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 22, value, flags)

    ForceOn = property(_get_ForceOn, _set_ForceOn) # type: bool

    def _get_kVA(self) -> float:
        """
        kVA rating of electrical machine. Defaults to 1.2* kW if not specified. Applied to machine or inverter definition for Dynamics mode solutions. 

        DSS property name: `kVA`, DSS property index: 23.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    def _set_kVA(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 23, value, flags)

    kVA = property(_get_kVA, _set_kVA) # type: float

    def _get_Xd(self) -> float:
        """
        Per unit synchronous reactance of machine. Presently used only for Thevenin impedance for power flow calcs of user models (model=6). Typically use a value 0.4 to 1.0. Default is 1.0

        DSS property name: `Xd`, DSS property index: 25.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 25)

    def _set_Xd(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 25, value, flags)

    Xd = property(_get_Xd, _set_Xd) # type: float

    def _get_Xdp(self) -> float:
        """
        Per unit transient reactance of the machine.  Used for Dynamics mode and Fault studies.  Default is 0.27.For user models, this value is used for the Thevenin/Norton impedance for Dynamics Mode.

        DSS property name: `Xdp`, DSS property index: 26.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 26)

    def _set_Xdp(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 26, value, flags)

    Xdp = property(_get_Xdp, _set_Xdp) # type: float

    def _get_Xdpp(self) -> float:
        """
        Per unit subtransient reactance of the machine.  Used for Harmonics. Default is 0.20.

        DSS property name: `Xdpp`, DSS property index: 27.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 27)

    def _set_Xdpp(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 27, value, flags)

    Xdpp = property(_get_Xdpp, _set_Xdpp) # type: float

    def _get_H(self) -> float:
        """
        Per unit mass constant of the machine.  MW-sec/MVA.  Default is 1.0.

        DSS property name: `H`, DSS property index: 28.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 28)

    def _set_H(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 28, value, flags)

    H = property(_get_H, _set_H) # type: float

    def _get_D(self) -> float:
        """
        Damping constant.  Usual range is 0 to 4. Default is 1.0.  Adjust to get damping

        DSS property name: `D`, DSS property index: 29.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 29)

    def _set_D(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 29, value, flags)

    D = property(_get_D, _set_D) # type: float

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

    def _get_ShaftModel(self) -> str:
        """
        Name of user-written DLL containing a Shaft model, which models the prime mover and determines the power on the shaft for Dynamics studies. Models additional mass elements other than the single-mass model in the DSS default model. Set to "none" to negate previous setting.

        DSS property name: `ShaftModel`, DSS property index: 32.
        """
        return self._get_prop_string(32)

    def _set_ShaftModel(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(32, value, flags)

    ShaftModel = property(_get_ShaftModel, _set_ShaftModel) # type: str

    def _get_ShaftData(self) -> str:
        """
        String (in quotes or parentheses) that gets passed to user-written shaft dynamic model for defining the data for that model.

        DSS property name: `ShaftData`, DSS property index: 33.
        """
        return self._get_prop_string(33)

    def _set_ShaftData(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(33, value, flags)

    ShaftData = property(_get_ShaftData, _set_ShaftData) # type: str

    def _get_DutyStart(self) -> float:
        """
        Starting time offset [hours] into the duty cycle shape for this generator, defaults to 0

        DSS property name: `DutyStart`, DSS property index: 34.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 34)

    def _set_DutyStart(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 34, value, flags)

    DutyStart = property(_get_DutyStart, _set_DutyStart) # type: float

    def _get_DebugTrace(self) -> bool:
        """
        {Yes | No }  Default is no.  Turn this on to capture the progress of the generator model for each iteration.  Creates a separate file for each generator named "GEN_name.csv".

        DSS property name: `DebugTrace`, DSS property index: 35.
        """
        return self._lib.Obj_GetInt32(self._ptr, 35) != 0

    def _set_DebugTrace(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 35, value, flags)

    DebugTrace = property(_get_DebugTrace, _set_DebugTrace) # type: bool

    def _get_Balanced(self) -> bool:
        """
        {Yes | No*} Default is No.  For Model=7, force balanced current only for 3-phase generators. Force zero- and negative-sequence to zero.

        DSS property name: `Balanced`, DSS property index: 36.
        """
        return self._lib.Obj_GetInt32(self._ptr, 36) != 0

    def _set_Balanced(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 36, value, flags)

    Balanced = property(_get_Balanced, _set_Balanced) # type: bool

    def _get_XRdp(self) -> float:
        """
        Default is 20. X/R ratio for Xdp property for FaultStudy and Dynamic modes.

        DSS property name: `XRdp`, DSS property index: 37.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 37)

    def _set_XRdp(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 37, value, flags)

    XRdp = property(_get_XRdp, _set_XRdp) # type: float

    def _get_UseFuel(self) -> bool:
        """
        {Yes | *No}. Activates the use of fuel for the operation of the generator. When the fuel level reaches the reserve level, the generator stops until it gets refueled. By default, the generator is connected to a continuous fuel supply, Use this mode to mimic dependency on fuel level for different generation technologies.

        DSS property name: `UseFuel`, DSS property index: 38.
        """
        return self._lib.Obj_GetInt32(self._ptr, 38) != 0

    def _set_UseFuel(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 38, value, flags)

    UseFuel = property(_get_UseFuel, _set_UseFuel) # type: bool

    def _get_FuelkWh(self) -> float:
        """
        {*0}Is the nominal level of fuel for the generator (kWh). It only applies if UseFuel = Yes/True

        DSS property name: `FuelkWh`, DSS property index: 39.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 39)

    def _set_FuelkWh(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 39, value, flags)

    FuelkWh = property(_get_FuelkWh, _set_FuelkWh) # type: float

    def _get_pctFuel(self) -> float:
        """
        It is a number between 0 and 100 representing the current amount of fuel available in percentage of FuelkWh. It only applies if UseFuel = Yes/True

        DSS property name: `%Fuel`, DSS property index: 40.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 40)

    def _set_pctFuel(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 40, value, flags)

    pctFuel = property(_get_pctFuel, _set_pctFuel) # type: float

    def _get_pctReserve(self) -> float:
        """
        It is a number between 0 and 100 representing the reserve level in percentage of FuelkWh. It only applies if UseFuel = Yes/True

        DSS property name: `%Reserve`, DSS property index: 41.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 41)

    def _set_pctReserve(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 41, value, flags)

    pctReserve = property(_get_pctReserve, _set_pctReserve) # type: float

    def Refuel(self, value: bool = True, flags: enums.SetterFlags = 0):
        """
        It is a boolean value (Yes/True, No/False) that can be used to manually refuel the generator when needed. It only applies if UseFuel = Yes/True

        DSS property name: `Refuel`, DSS property index: 42.
        """
        self._lib.Obj_SetInt32(self._ptr, 42, value, flags)

    def _get_DynamicEq_str(self) -> str:
        """
        The name of the dynamic equation (DynamicExp) that will be used for defining the dynamic behavior of the generator. if not defined, the generator dynamics will follow the built-in dynamic equation.

        DSS property name: `DynamicEq`, DSS property index: 43.
        """
        return self._get_prop_string(43)

    def _set_DynamicEq_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(43, value, flags)

    DynamicEq_str = property(_get_DynamicEq_str, _set_DynamicEq_str) # type: str

    def _get_DynamicEq(self) -> DynamicExp:
        """
        The name of the dynamic equation (DynamicExp) that will be used for defining the dynamic behavior of the generator. if not defined, the generator dynamics will follow the built-in dynamic equation.

        DSS property name: `DynamicEq`, DSS property index: 43.
        """
        return self._get_obj(43, DynamicExp)

    def _set_DynamicEq(self, value: Union[AnyStr, DynamicExp], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(43, value, flags)
            return

        self._set_string_o(43, value, flags)

    DynamicEq = property(_get_DynamicEq, _set_DynamicEq) # type: DynamicExp

    def _get_DynOut(self) -> str:
        """
        The name of the variables within the Dynamic equation that will be used to govern the generator dynamics.This generator model requires 2 outputs from the dynamic equation: 

        1. Shaft speed (velocity) relative to synchronous speed.
        2. Shaft, or power, angle (relative to synchronous reference frame).

        The output variables need to be defined in tha strict order.

        DSS property name: `DynOut`, DSS property index: 44.
        """
        return self._get_prop_string(44)

    def _set_DynOut(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(44, value, flags)

    DynOut = property(_get_DynOut, _set_DynOut) # type: str

    def _get_Spectrum_str(self) -> str:
        """
        Name of harmonic voltage or current spectrum for this generator. Voltage behind Xd" for machine - default. Current injection for inverter. Default value is "default", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 45.
        """
        return self._get_prop_string(45)

    def _set_Spectrum_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(45, value, flags)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str) # type: str

    def _get_Spectrum(self) -> SpectrumObj:
        """
        Name of harmonic voltage or current spectrum for this generator. Voltage behind Xd" for machine - default. Current injection for inverter. Default value is "default", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 45.
        """
        return self._get_obj(45, SpectrumObj)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(45, value, flags)
            return

        self._set_string_o(45, value, flags)

    Spectrum = property(_get_Spectrum, _set_Spectrum) # type: SpectrumObj

    def _get_BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 46.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 46)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 46, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float

    def _get_Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 47.
        """
        return self._lib.Obj_GetInt32(self._ptr, 47) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 47, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 48.
        """
        self._set_string_o(48, value)


class GeneratorProperties(TypedDict):
    Phases: int
    Bus1: AnyStr
    kV: float
    kW: float
    PF: float
    kvar: float
    Model: Union[int, enums.GeneratorModel]
    VMinpu: float
    VMaxpu: float
    Yearly: Union[AnyStr, LoadShape]
    Daily: Union[AnyStr, LoadShape]
    Duty: Union[AnyStr, LoadShape]
    DispMode: Union[AnyStr, int, enums.GeneratorDispatchMode]
    DispValue: float
    Conn: Union[AnyStr, int, enums.Connection]
    Status: Union[AnyStr, int, enums.GeneratorStatus]
    Class: int
    Vpu: float
    Maxkvar: float
    Minkvar: float
    PVFactor: float
    ForceOn: bool
    kVA: float
    Xd: float
    Xdp: float
    Xdpp: float
    H: float
    D: float
    UserModel: AnyStr
    UserData: AnyStr
    ShaftModel: AnyStr
    ShaftData: AnyStr
    DutyStart: float
    DebugTrace: bool
    Balanced: bool
    XRdp: float
    UseFuel: bool
    FuelkWh: float
    pctFuel: float
    pctReserve: float
    Refuel: bool
    DynamicEq: Union[AnyStr, DynamicExp]
    DynOut: AnyStr
    Spectrum: Union[AnyStr, SpectrumObj]
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class GeneratorBatch(DSSBatch, CircuitElementBatchMixin, PCElementBatchMixin):
    _cls_name = 'Generator'
    _obj_cls = Generator
    _cls_idx = 27

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)
       PCElementBatchMixin.__init__(self)

    def _get_Phases(self) -> BatchInt32ArrayProxy:
        """
        Number of Phases, this Generator.  Power is evenly divided among phases.

        DSS property name: `Phases`, DSS property index: 1.
        """
        return BatchInt32ArrayProxy(self, 1)

    def _set_Phases(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(1, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: BatchInt32ArrayProxy

    def _get_Bus1(self) -> List[str]:
        """
        Bus to which the Generator is connected.  May include specific node specification.

        DSS property name: `Bus1`, DSS property index: 2.
        """
        return self._get_batch_str_prop(2)

    def _set_Bus1(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(2, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: List[str]

    def _get_kV(self) -> BatchFloat64ArrayProxy:
        """
        Nominal rated (1.0 per unit) voltage, kV, for Generator. For 2- and 3-phase Generators, specify phase-phase kV. Otherwise, for phases=1 or phases>3, specify actual kV across each branch of the Generator. If wye (star), specify phase-neutral kV. If delta or phase-phase connected, specify phase-phase kV.

        DSS property name: `kV`, DSS property index: 3.
        """
        return BatchFloat64ArrayProxy(self, 3)

    def _set_kV(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(3, value, flags)

    kV = property(_get_kV, _set_kV) # type: BatchFloat64ArrayProxy

    def _get_kW(self) -> BatchFloat64ArrayProxy:
        """
        Total base kW for the Generator.  A positive value denotes power coming OUT of the element, 
        which is the opposite of a load. This value is modified depending on the dispatch mode. Unaffected by the global load multiplier and growth curves. If you want there to be more generation, you must add more generators or change this value.

        DSS property name: `kW`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    def _set_kW(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(4, value, flags)

    kW = property(_get_kW, _set_kW) # type: BatchFloat64ArrayProxy

    def _get_PF(self) -> BatchFloat64ArrayProxy:
        """
        Generator power factor. Default is 0.80. Enter negative for leading powerfactor (when kW and kvar have opposite signs.)
        A positive power factor for a generator signifies that the generator produces vars 
        as is typical for a synchronous generator.  Induction machines would be 
        specified with a negative power factor.

        DSS property name: `PF`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    def _set_PF(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(5, value, flags)

    PF = property(_get_PF, _set_PF) # type: BatchFloat64ArrayProxy

    def _get_kvar(self) -> BatchFloat64ArrayProxy:
        """
        Specify the base kvar.  Alternative to specifying the power factor.  Side effect:  the power factor value is altered to agree based on present value of kW.

        DSS property name: `kvar`, DSS property index: 6.
        """
        return BatchFloat64ArrayProxy(self, 6)

    def _set_kvar(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(6, value, flags)

    kvar = property(_get_kvar, _set_kvar) # type: BatchFloat64ArrayProxy

    def _get_Model(self) -> BatchInt32ArrayProxy:
        """
        Integer code for the model to use for generation variation with voltage. Valid values are:

        1:Generator injects a constant kW at specified power factor.
        2:Generator is modeled as a constant admittance.
        3:Const kW, constant kV.  Somewhat like a conventional transmission power flow P-V generator.
        4:Const kW, Fixed Q (Q never varies)
        5:Const kW, Fixed Q(as a constant reactance)
        6:Compute load injection from User-written Model.(see usage of Xd, Xdp)
        7:Constant kW, kvar, but current-limited below Vminpu. Approximates a simple inverter. See also Balanced.

        DSS property name: `Model`, DSS property index: 7.
        """
        return BatchInt32ArrayProxy(self, 7)

    def _set_Model(self, value: Union[int, enums.GeneratorModel, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(7, value, flags)

    Model = property(_get_Model, _set_Model) # type: BatchInt32ArrayProxy

    def _get_VMinpu(self) -> BatchFloat64ArrayProxy:
        """
        Default = 0.90.  Minimum per unit voltage for which the Model is assumed to apply. Below this value, the load model reverts to a constant impedance model. For model 7, the current is limited to the value computed for constant power at Vminpu.

        DSS property name: `VMinpu`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    def _set_VMinpu(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(8, value, flags)

    VMinpu = property(_get_VMinpu, _set_VMinpu) # type: BatchFloat64ArrayProxy

    def _get_VMaxpu(self) -> BatchFloat64ArrayProxy:
        """
        Default = 1.10.  Maximum per unit voltage for which the Model is assumed to apply. Above this value, the load model reverts to a constant impedance model.

        DSS property name: `VMaxpu`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    def _set_VMaxpu(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(9, value, flags)

    VMaxpu = property(_get_VMaxpu, _set_VMaxpu) # type: BatchFloat64ArrayProxy

    def _get_Yearly_str(self) -> List[str]:
        """
        Dispatch shape to use for yearly simulations.  Must be previously defined as a Loadshape object. If this is not specified, a constant value is assumed (no variation). If the generator is assumed to be ON continuously, specify Status=FIXED, or designate a curve that is 1.0 per unit at all times. Set to NONE to reset to no loadshape. Nominally for 8760 simulations.  If there are fewer points in the designated shape than the number of points in the solution, the curve is repeated.

        DSS property name: `Yearly`, DSS property index: 10.
        """
        return self._get_batch_str_prop(10)

    def _set_Yearly_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(10, value, flags)

    Yearly_str = property(_get_Yearly_str, _set_Yearly_str) # type: List[str]

    def _get_Yearly(self) -> List[LoadShape]:
        """
        Dispatch shape to use for yearly simulations.  Must be previously defined as a Loadshape object. If this is not specified, a constant value is assumed (no variation). If the generator is assumed to be ON continuously, specify Status=FIXED, or designate a curve that is 1.0 per unit at all times. Set to NONE to reset to no loadshape. Nominally for 8760 simulations.  If there are fewer points in the designated shape than the number of points in the solution, the curve is repeated.

        DSS property name: `Yearly`, DSS property index: 10.
        """
        return self._get_batch_obj_prop(10)

    def _set_Yearly(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(10, value, flags)

    Yearly = property(_get_Yearly, _set_Yearly) # type: List[LoadShape]

    def _get_Daily_str(self) -> List[str]:
        """
        Dispatch shape to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically.  If generator is assumed to be ON continuously, specify Status=FIXED, or designate a Loadshape object that is 1.0 per unit for all hours. Set to NONE to reset to no loadshape. 

        DSS property name: `Daily`, DSS property index: 11.
        """
        return self._get_batch_str_prop(11)

    def _set_Daily_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(11, value, flags)

    Daily_str = property(_get_Daily_str, _set_Daily_str) # type: List[str]

    def _get_Daily(self) -> List[LoadShape]:
        """
        Dispatch shape to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically.  If generator is assumed to be ON continuously, specify Status=FIXED, or designate a Loadshape object that is 1.0 per unit for all hours. Set to NONE to reset to no loadshape. 

        DSS property name: `Daily`, DSS property index: 11.
        """
        return self._get_batch_obj_prop(11)

    def _set_Daily(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(11, value, flags)

    Daily = property(_get_Daily, _set_Daily) # type: List[LoadShape]

    def _get_Duty_str(self) -> List[str]:
        """
        Load shape to use for duty cycle dispatch simulations such as for wind generation. Must be previously defined as a Loadshape object. Typically would have time intervals less than 1 hr -- perhaps, in seconds. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.

        DSS property name: `Duty`, DSS property index: 12.
        """
        return self._get_batch_str_prop(12)

    def _set_Duty_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(12, value, flags)

    Duty_str = property(_get_Duty_str, _set_Duty_str) # type: List[str]

    def _get_Duty(self) -> List[LoadShape]:
        """
        Load shape to use for duty cycle dispatch simulations such as for wind generation. Must be previously defined as a Loadshape object. Typically would have time intervals less than 1 hr -- perhaps, in seconds. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.

        DSS property name: `Duty`, DSS property index: 12.
        """
        return self._get_batch_obj_prop(12)

    def _set_Duty(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(12, value, flags)

    Duty = property(_get_Duty, _set_Duty) # type: List[LoadShape]

    def _get_DispMode(self) -> BatchInt32ArrayProxy:
        """
        {Default* | Loadlevel | Price } Default = Default. Dispatch mode. In default mode, gen is either always on or follows dispatch curve as specified. Otherwise, the gen comes on when either the global default load level (Loadshape "default") or the price level exceeds the dispatch value.

        DSS property name: `DispMode`, DSS property index: 13.
        """
        return BatchInt32ArrayProxy(self, 13)

    def _set_DispMode(self, value: Union[AnyStr, int, enums.GeneratorDispatchMode, List[AnyStr], List[int], List[enums.GeneratorDispatchMode], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(13, value, flags)
            return

        self._set_batch_int32_array(13, value, flags)

    DispMode = property(_get_DispMode, _set_DispMode) # type: BatchInt32ArrayProxy

    def _get_DispMode_str(self) -> List[str]:
        """
        {Default* | Loadlevel | Price } Default = Default. Dispatch mode. In default mode, gen is either always on or follows dispatch curve as specified. Otherwise, the gen comes on when either the global default load level (Loadshape "default") or the price level exceeds the dispatch value.

        DSS property name: `DispMode`, DSS property index: 13.
        """
        return self._get_batch_str_prop(13)

    def _set_DispMode_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_DispMode(value, flags)

    DispMode_str = property(_get_DispMode_str, _set_DispMode_str) # type: List[str]

    def _get_DispValue(self) -> BatchFloat64ArrayProxy:
        """
        Dispatch value. 
        If = 0.0 (default) then Generator follow dispatch curves, if any. 
        If > 0  then Generator is ON only when either the price signal (in Price dispatch mode) exceeds this value or the active circuit load multiplier * "default" loadshape value * the default yearly growth factor exceeds this value.  Then the generator follows dispatch curves (duty, daily, or yearly), if any (see also Status).

        DSS property name: `DispValue`, DSS property index: 14.
        """
        return BatchFloat64ArrayProxy(self, 14)

    def _set_DispValue(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(14, value, flags)

    DispValue = property(_get_DispValue, _set_DispValue) # type: BatchFloat64ArrayProxy

    def _get_Conn(self) -> BatchInt32ArrayProxy:
        """
        ={wye|LN|delta|LL}.  Default is wye.

        DSS property name: `Conn`, DSS property index: 15.
        """
        return BatchInt32ArrayProxy(self, 15)

    def _set_Conn(self, value: Union[AnyStr, int, enums.Connection, List[AnyStr], List[int], List[enums.Connection], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(15, value, flags)
            return

        self._set_batch_int32_array(15, value, flags)

    Conn = property(_get_Conn, _set_Conn) # type: BatchInt32ArrayProxy

    def _get_Conn_str(self) -> List[str]:
        """
        ={wye|LN|delta|LL}.  Default is wye.

        DSS property name: `Conn`, DSS property index: 15.
        """
        return self._get_batch_str_prop(15)

    def _set_Conn_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Conn(value, flags)

    Conn_str = property(_get_Conn_str, _set_Conn_str) # type: List[str]

    def _get_Status(self) -> BatchInt32ArrayProxy:
        """
        ={Fixed | Variable*}.  If Fixed, then dispatch multipliers do not apply. The generator is alway at full power when it is ON.  Default is Variable  (follows curves).

        DSS property name: `Status`, DSS property index: 16.
        """
        return BatchInt32ArrayProxy(self, 16)

    def _set_Status(self, value: Union[AnyStr, int, enums.GeneratorStatus, List[AnyStr], List[int], List[enums.GeneratorStatus], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(16, value, flags)
            return

        self._set_batch_int32_array(16, value, flags)

    Status = property(_get_Status, _set_Status) # type: BatchInt32ArrayProxy

    def _get_Status_str(self) -> List[str]:
        """
        ={Fixed | Variable*}.  If Fixed, then dispatch multipliers do not apply. The generator is alway at full power when it is ON.  Default is Variable  (follows curves).

        DSS property name: `Status`, DSS property index: 16.
        """
        return self._get_batch_str_prop(16)

    def _set_Status_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Status(value, flags)

    Status_str = property(_get_Status_str, _set_Status_str) # type: List[str]

    def _get_Class(self) -> BatchInt32ArrayProxy:
        """
        An arbitrary integer number representing the class of Generator so that Generator values may be segregated by class.

        DSS property name: `Class`, DSS property index: 17.
        """
        return BatchInt32ArrayProxy(self, 17)

    def _set_Class(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(17, value, flags)

    Class = property(_get_Class, _set_Class) # type: BatchInt32ArrayProxy

    def _get_Vpu(self) -> BatchFloat64ArrayProxy:
        """
        Per Unit voltage set point for Model = 3  (typical power flow model).  Default is 1.0. 

        DSS property name: `Vpu`, DSS property index: 18.
        """
        return BatchFloat64ArrayProxy(self, 18)

    def _set_Vpu(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(18, value, flags)

    Vpu = property(_get_Vpu, _set_Vpu) # type: BatchFloat64ArrayProxy

    def _get_Maxkvar(self) -> BatchFloat64ArrayProxy:
        """
        Maximum kvar limit for Model = 3.  Defaults to twice the specified load kvar.  Always reset this if you change PF or kvar properties.

        DSS property name: `Maxkvar`, DSS property index: 19.
        """
        return BatchFloat64ArrayProxy(self, 19)

    def _set_Maxkvar(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(19, value, flags)

    Maxkvar = property(_get_Maxkvar, _set_Maxkvar) # type: BatchFloat64ArrayProxy

    def _get_Minkvar(self) -> BatchFloat64ArrayProxy:
        """
        Minimum kvar limit for Model = 3. Enter a negative number if generator can absorb vars. Defaults to negative of Maxkvar.  Always reset this if you change PF or kvar properties.

        DSS property name: `Minkvar`, DSS property index: 20.
        """
        return BatchFloat64ArrayProxy(self, 20)

    def _set_Minkvar(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(20, value, flags)

    Minkvar = property(_get_Minkvar, _set_Minkvar) # type: BatchFloat64ArrayProxy

    def _get_PVFactor(self) -> BatchFloat64ArrayProxy:
        """
        Deceleration factor for P-V generator model (Model=3).  Default is 0.1. If the circuit converges easily, you may want to use a higher number such as 1.0. Use a lower number if solution diverges. Use Debugtrace=yes to create a file that will trace the convergence of a generator model.

        DSS property name: `PVFactor`, DSS property index: 21.
        """
        return BatchFloat64ArrayProxy(self, 21)

    def _set_PVFactor(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(21, value, flags)

    PVFactor = property(_get_PVFactor, _set_PVFactor) # type: BatchFloat64ArrayProxy

    def _get_ForceOn(self) -> List[bool]:
        """
        {Yes | No}  Forces generator ON despite requirements of other dispatch modes. Stays ON until this property is set to NO, or an internal algorithm cancels the forced ON state.

        DSS property name: `ForceOn`, DSS property index: 22.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(22)
        ]

    def _set_ForceOn(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(22, value, flags)

    ForceOn = property(_get_ForceOn, _set_ForceOn) # type: List[bool]

    def _get_kVA(self) -> BatchFloat64ArrayProxy:
        """
        kVA rating of electrical machine. Defaults to 1.2* kW if not specified. Applied to machine or inverter definition for Dynamics mode solutions. 

        DSS property name: `kVA`, DSS property index: 23.
        """
        return BatchFloat64ArrayProxy(self, 23)

    def _set_kVA(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(23, value, flags)

    kVA = property(_get_kVA, _set_kVA) # type: BatchFloat64ArrayProxy

    def _get_Xd(self) -> BatchFloat64ArrayProxy:
        """
        Per unit synchronous reactance of machine. Presently used only for Thevenin impedance for power flow calcs of user models (model=6). Typically use a value 0.4 to 1.0. Default is 1.0

        DSS property name: `Xd`, DSS property index: 25.
        """
        return BatchFloat64ArrayProxy(self, 25)

    def _set_Xd(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(25, value, flags)

    Xd = property(_get_Xd, _set_Xd) # type: BatchFloat64ArrayProxy

    def _get_Xdp(self) -> BatchFloat64ArrayProxy:
        """
        Per unit transient reactance of the machine.  Used for Dynamics mode and Fault studies.  Default is 0.27.For user models, this value is used for the Thevenin/Norton impedance for Dynamics Mode.

        DSS property name: `Xdp`, DSS property index: 26.
        """
        return BatchFloat64ArrayProxy(self, 26)

    def _set_Xdp(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(26, value, flags)

    Xdp = property(_get_Xdp, _set_Xdp) # type: BatchFloat64ArrayProxy

    def _get_Xdpp(self) -> BatchFloat64ArrayProxy:
        """
        Per unit subtransient reactance of the machine.  Used for Harmonics. Default is 0.20.

        DSS property name: `Xdpp`, DSS property index: 27.
        """
        return BatchFloat64ArrayProxy(self, 27)

    def _set_Xdpp(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(27, value, flags)

    Xdpp = property(_get_Xdpp, _set_Xdpp) # type: BatchFloat64ArrayProxy

    def _get_H(self) -> BatchFloat64ArrayProxy:
        """
        Per unit mass constant of the machine.  MW-sec/MVA.  Default is 1.0.

        DSS property name: `H`, DSS property index: 28.
        """
        return BatchFloat64ArrayProxy(self, 28)

    def _set_H(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(28, value, flags)

    H = property(_get_H, _set_H) # type: BatchFloat64ArrayProxy

    def _get_D(self) -> BatchFloat64ArrayProxy:
        """
        Damping constant.  Usual range is 0 to 4. Default is 1.0.  Adjust to get damping

        DSS property name: `D`, DSS property index: 29.
        """
        return BatchFloat64ArrayProxy(self, 29)

    def _set_D(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(29, value, flags)

    D = property(_get_D, _set_D) # type: BatchFloat64ArrayProxy

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

    def _get_ShaftModel(self) -> List[str]:
        """
        Name of user-written DLL containing a Shaft model, which models the prime mover and determines the power on the shaft for Dynamics studies. Models additional mass elements other than the single-mass model in the DSS default model. Set to "none" to negate previous setting.

        DSS property name: `ShaftModel`, DSS property index: 32.
        """
        return self._get_batch_str_prop(32)

    def _set_ShaftModel(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(32, value, flags)

    ShaftModel = property(_get_ShaftModel, _set_ShaftModel) # type: List[str]

    def _get_ShaftData(self) -> List[str]:
        """
        String (in quotes or parentheses) that gets passed to user-written shaft dynamic model for defining the data for that model.

        DSS property name: `ShaftData`, DSS property index: 33.
        """
        return self._get_batch_str_prop(33)

    def _set_ShaftData(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(33, value, flags)

    ShaftData = property(_get_ShaftData, _set_ShaftData) # type: List[str]

    def _get_DutyStart(self) -> BatchFloat64ArrayProxy:
        """
        Starting time offset [hours] into the duty cycle shape for this generator, defaults to 0

        DSS property name: `DutyStart`, DSS property index: 34.
        """
        return BatchFloat64ArrayProxy(self, 34)

    def _set_DutyStart(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(34, value, flags)

    DutyStart = property(_get_DutyStart, _set_DutyStart) # type: BatchFloat64ArrayProxy

    def _get_DebugTrace(self) -> List[bool]:
        """
        {Yes | No }  Default is no.  Turn this on to capture the progress of the generator model for each iteration.  Creates a separate file for each generator named "GEN_name.csv".

        DSS property name: `DebugTrace`, DSS property index: 35.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(35)
        ]

    def _set_DebugTrace(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(35, value, flags)

    DebugTrace = property(_get_DebugTrace, _set_DebugTrace) # type: List[bool]

    def _get_Balanced(self) -> List[bool]:
        """
        {Yes | No*} Default is No.  For Model=7, force balanced current only for 3-phase generators. Force zero- and negative-sequence to zero.

        DSS property name: `Balanced`, DSS property index: 36.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(36)
        ]

    def _set_Balanced(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(36, value, flags)

    Balanced = property(_get_Balanced, _set_Balanced) # type: List[bool]

    def _get_XRdp(self) -> BatchFloat64ArrayProxy:
        """
        Default is 20. X/R ratio for Xdp property for FaultStudy and Dynamic modes.

        DSS property name: `XRdp`, DSS property index: 37.
        """
        return BatchFloat64ArrayProxy(self, 37)

    def _set_XRdp(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(37, value, flags)

    XRdp = property(_get_XRdp, _set_XRdp) # type: BatchFloat64ArrayProxy

    def _get_UseFuel(self) -> List[bool]:
        """
        {Yes | *No}. Activates the use of fuel for the operation of the generator. When the fuel level reaches the reserve level, the generator stops until it gets refueled. By default, the generator is connected to a continuous fuel supply, Use this mode to mimic dependency on fuel level for different generation technologies.

        DSS property name: `UseFuel`, DSS property index: 38.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(38)
        ]

    def _set_UseFuel(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(38, value, flags)

    UseFuel = property(_get_UseFuel, _set_UseFuel) # type: List[bool]

    def _get_FuelkWh(self) -> BatchFloat64ArrayProxy:
        """
        {*0}Is the nominal level of fuel for the generator (kWh). It only applies if UseFuel = Yes/True

        DSS property name: `FuelkWh`, DSS property index: 39.
        """
        return BatchFloat64ArrayProxy(self, 39)

    def _set_FuelkWh(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(39, value, flags)

    FuelkWh = property(_get_FuelkWh, _set_FuelkWh) # type: BatchFloat64ArrayProxy

    def _get_pctFuel(self) -> BatchFloat64ArrayProxy:
        """
        It is a number between 0 and 100 representing the current amount of fuel available in percentage of FuelkWh. It only applies if UseFuel = Yes/True

        DSS property name: `%Fuel`, DSS property index: 40.
        """
        return BatchFloat64ArrayProxy(self, 40)

    def _set_pctFuel(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(40, value, flags)

    pctFuel = property(_get_pctFuel, _set_pctFuel) # type: BatchFloat64ArrayProxy

    def _get_pctReserve(self) -> BatchFloat64ArrayProxy:
        """
        It is a number between 0 and 100 representing the reserve level in percentage of FuelkWh. It only applies if UseFuel = Yes/True

        DSS property name: `%Reserve`, DSS property index: 41.
        """
        return BatchFloat64ArrayProxy(self, 41)

    def _set_pctReserve(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(41, value, flags)

    pctReserve = property(_get_pctReserve, _set_pctReserve) # type: BatchFloat64ArrayProxy

    def Refuel(self, value: Union[bool, List[bool]] = True, flags: enums.SetterFlags = 0):
        """
        It is a boolean value (Yes/True, No/False) that can be used to manually refuel the generator when needed. It only applies if UseFuel = Yes/True

        DSS property name: `Refuel`, DSS property index: 42.
        """
        self._set_batch_int32_array(42, value, flags)

    def _get_DynamicEq_str(self) -> List[str]:
        """
        The name of the dynamic equation (DynamicExp) that will be used for defining the dynamic behavior of the generator. if not defined, the generator dynamics will follow the built-in dynamic equation.

        DSS property name: `DynamicEq`, DSS property index: 43.
        """
        return self._get_batch_str_prop(43)

    def _set_DynamicEq_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(43, value, flags)

    DynamicEq_str = property(_get_DynamicEq_str, _set_DynamicEq_str) # type: List[str]

    def _get_DynamicEq(self) -> List[DynamicExp]:
        """
        The name of the dynamic equation (DynamicExp) that will be used for defining the dynamic behavior of the generator. if not defined, the generator dynamics will follow the built-in dynamic equation.

        DSS property name: `DynamicEq`, DSS property index: 43.
        """
        return self._get_batch_obj_prop(43)

    def _set_DynamicEq(self, value: Union[AnyStr, DynamicExp, List[AnyStr], List[DynamicExp]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(43, value, flags)

    DynamicEq = property(_get_DynamicEq, _set_DynamicEq) # type: List[DynamicExp]

    def _get_DynOut(self) -> List[str]:
        """
        The name of the variables within the Dynamic equation that will be used to govern the generator dynamics.This generator model requires 2 outputs from the dynamic equation: 

        1. Shaft speed (velocity) relative to synchronous speed.
        2. Shaft, or power, angle (relative to synchronous reference frame).

        The output variables need to be defined in tha strict order.

        DSS property name: `DynOut`, DSS property index: 44.
        """
        return self._get_batch_str_prop(44)

    def _set_DynOut(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(44, value, flags)

    DynOut = property(_get_DynOut, _set_DynOut) # type: List[str]

    def _get_Spectrum_str(self) -> List[str]:
        """
        Name of harmonic voltage or current spectrum for this generator. Voltage behind Xd" for machine - default. Current injection for inverter. Default value is "default", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 45.
        """
        return self._get_batch_str_prop(45)

    def _set_Spectrum_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(45, value, flags)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str) # type: List[str]

    def _get_Spectrum(self) -> List[SpectrumObj]:
        """
        Name of harmonic voltage or current spectrum for this generator. Voltage behind Xd" for machine - default. Current injection for inverter. Default value is "default", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 45.
        """
        return self._get_batch_obj_prop(45)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(45, value, flags)

    Spectrum = property(_get_Spectrum, _set_Spectrum) # type: List[SpectrumObj]

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 46.
        """
        return BatchFloat64ArrayProxy(self, 46)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(46, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy

    def _get_Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 47.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(47)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(47, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 48.
        """
        self._set_batch_string(48, value, flags)

class GeneratorBatchProperties(TypedDict):
    Phases: Union[int, Int32Array]
    Bus1: Union[AnyStr, List[AnyStr]]
    kV: Union[float, Float64Array]
    kW: Union[float, Float64Array]
    PF: Union[float, Float64Array]
    kvar: Union[float, Float64Array]
    Model: Union[int, enums.GeneratorModel, Int32Array]
    VMinpu: Union[float, Float64Array]
    VMaxpu: Union[float, Float64Array]
    Yearly: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    Daily: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    Duty: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    DispMode: Union[AnyStr, int, enums.GeneratorDispatchMode, List[AnyStr], List[int], List[enums.GeneratorDispatchMode], Int32Array]
    DispValue: Union[float, Float64Array]
    Conn: Union[AnyStr, int, enums.Connection, List[AnyStr], List[int], List[enums.Connection], Int32Array]
    Status: Union[AnyStr, int, enums.GeneratorStatus, List[AnyStr], List[int], List[enums.GeneratorStatus], Int32Array]
    Class: Union[int, Int32Array]
    Vpu: Union[float, Float64Array]
    Maxkvar: Union[float, Float64Array]
    Minkvar: Union[float, Float64Array]
    PVFactor: Union[float, Float64Array]
    ForceOn: bool
    kVA: Union[float, Float64Array]
    Xd: Union[float, Float64Array]
    Xdp: Union[float, Float64Array]
    Xdpp: Union[float, Float64Array]
    H: Union[float, Float64Array]
    D: Union[float, Float64Array]
    UserModel: Union[AnyStr, List[AnyStr]]
    UserData: Union[AnyStr, List[AnyStr]]
    ShaftModel: Union[AnyStr, List[AnyStr]]
    ShaftData: Union[AnyStr, List[AnyStr]]
    DutyStart: Union[float, Float64Array]
    DebugTrace: bool
    Balanced: bool
    XRdp: Union[float, Float64Array]
    UseFuel: bool
    FuelkWh: Union[float, Float64Array]
    pctFuel: Union[float, Float64Array]
    pctReserve: Union[float, Float64Array]
    Refuel: bool
    DynamicEq: Union[AnyStr, DynamicExp, List[AnyStr], List[DynamicExp]]
    DynOut: Union[AnyStr, List[AnyStr]]
    Spectrum: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IGenerator(IDSSObj, GeneratorBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, Generator, GeneratorBatch)
        GeneratorBatch.__init__(self, self._api_util, sync_cls_idx=Generator._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Generator:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[GeneratorProperties]) -> Generator:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[GeneratorBatchProperties]) -> GeneratorBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
