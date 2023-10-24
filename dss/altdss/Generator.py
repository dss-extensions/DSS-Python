# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from typing_extensions import TypedDict, Unpack
from ._obj_bases import (
    CktElementMixin,
    PCElementMixin,
    ElementHasRegistersMixin,
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
from .DynamicExp import DynamicExp
from .LoadShape import LoadShape
from .Spectrum import Spectrum as SpectrumObj

class Generator(DSSObj, CktElementMixin, PCElementMixin, ElementHasRegistersMixin):
    __slots__ = CktElementMixin._extra_slots + PCElementMixin._extra_slots + ElementHasRegistersMixin._extra_slots
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

    @property
    def Phases(self) -> int:
        """
        Number of Phases, this Generator.  Power is evenly divided among phases.

        DSS property name: `Phases`, DSS property index: 1.
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @Phases.setter
    def Phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def Bus1(self) -> str:
        """
        Bus to which the Generator is connected.  May include specific node specification.

        DSS property name: `Bus1`, DSS property index: 2.
        """
        return self._get_prop_string(2)

    @Bus1.setter
    def Bus1(self, value: AnyStr):
        self._set_string_o(2, value)

    @property
    def kV(self) -> float:
        """
        Nominal rated (1.0 per unit) voltage, kV, for Generator. For 2- and 3-phase Generators, specify phase-phase kV. Otherwise, for phases=1 or phases>3, specify actual kV across each branch of the Generator. If wye (star), specify phase-neutral kV. If delta or phase-phase connected, specify phase-phase kV.

        DSS property name: `kV`, DSS property index: 3.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @kV.setter
    def kV(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def kW(self) -> float:
        """
        Total base kW for the Generator.  A positive value denotes power coming OUT of the element, 
        which is the opposite of a load. This value is modified depending on the dispatch mode. Unaffected by the global load multiplier and growth curves. If you want there to be more generation, you must add more generators or change this value.

        DSS property name: `kW`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @kW.setter
    def kW(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def PF(self) -> float:
        """
        Generator power factor. Default is 0.80. Enter negative for leading powerfactor (when kW and kvar have opposite signs.)
        A positive power factor for a generator signifies that the generator produces vars 
        as is typical for a synchronous generator.  Induction machines would be 
        specified with a negative power factor.

        DSS property name: `PF`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @PF.setter
    def PF(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def kvar(self) -> float:
        """
        Specify the base kvar.  Alternative to specifying the power factor.  Side effect:  the power factor value is altered to agree based on present value of kW.

        DSS property name: `kvar`, DSS property index: 6.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    @kvar.setter
    def kvar(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 6, value)

    @property
    def Model(self) -> enums.GeneratorModel:
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

    @Model.setter
    def Model(self, value: Union[int, enums.GeneratorModel]):
        self._lib.Obj_SetInt32(self._ptr, 7, value)

    @property
    def VMinpu(self) -> float:
        """
        Default = 0.90.  Minimum per unit voltage for which the Model is assumed to apply. Below this value, the load model reverts to a constant impedance model. For model 7, the current is limited to the value computed for constant power at Vminpu.

        DSS property name: `VMinpu`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @VMinpu.setter
    def VMinpu(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def VMaxpu(self) -> float:
        """
        Default = 1.10.  Maximum per unit voltage for which the Model is assumed to apply. Above this value, the load model reverts to a constant impedance model.

        DSS property name: `VMaxpu`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @VMaxpu.setter
    def VMaxpu(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def Yearly_str(self) -> str:
        """
        Dispatch shape to use for yearly simulations.  Must be previously defined as a Loadshape object. If this is not specified, a constant value is assumed (no variation). If the generator is assumed to be ON continuously, specify Status=FIXED, or designate a curve that is 1.0 per unit at all times. Set to NONE to reset to no loadshape. Nominally for 8760 simulations.  If there are fewer points in the designated shape than the number of points in the solution, the curve is repeated.

        DSS property name: `Yearly`, DSS property index: 10.
        """
        return self._get_prop_string(10)

    @Yearly_str.setter
    def Yearly_str(self, value: AnyStr):
        self._set_string_o(10, value)

    @property
    def Yearly(self) -> LoadShape:
        """
        Dispatch shape to use for yearly simulations.  Must be previously defined as a Loadshape object. If this is not specified, a constant value is assumed (no variation). If the generator is assumed to be ON continuously, specify Status=FIXED, or designate a curve that is 1.0 per unit at all times. Set to NONE to reset to no loadshape. Nominally for 8760 simulations.  If there are fewer points in the designated shape than the number of points in the solution, the curve is repeated.

        DSS property name: `Yearly`, DSS property index: 10.
        """
        return self._get_obj(10, LoadShape)

    @Yearly.setter
    def Yearly(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(10, value)
            return

        self._set_string_o(10, value)

    @property
    def Daily_str(self) -> str:
        """
        Dispatch shape to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically.  If generator is assumed to be ON continuously, specify Status=FIXED, or designate a Loadshape object that is 1.0 per unit for all hours. Set to NONE to reset to no loadshape. 

        DSS property name: `Daily`, DSS property index: 11.
        """
        return self._get_prop_string(11)

    @Daily_str.setter
    def Daily_str(self, value: AnyStr):
        self._set_string_o(11, value)

    @property
    def Daily(self) -> LoadShape:
        """
        Dispatch shape to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically.  If generator is assumed to be ON continuously, specify Status=FIXED, or designate a Loadshape object that is 1.0 per unit for all hours. Set to NONE to reset to no loadshape. 

        DSS property name: `Daily`, DSS property index: 11.
        """
        return self._get_obj(11, LoadShape)

    @Daily.setter
    def Daily(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(11, value)
            return

        self._set_string_o(11, value)

    @property
    def Duty_str(self) -> str:
        """
        Load shape to use for duty cycle dispatch simulations such as for wind generation. Must be previously defined as a Loadshape object. Typically would have time intervals less than 1 hr -- perhaps, in seconds. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.

        DSS property name: `Duty`, DSS property index: 12.
        """
        return self._get_prop_string(12)

    @Duty_str.setter
    def Duty_str(self, value: AnyStr):
        self._set_string_o(12, value)

    @property
    def Duty(self) -> LoadShape:
        """
        Load shape to use for duty cycle dispatch simulations such as for wind generation. Must be previously defined as a Loadshape object. Typically would have time intervals less than 1 hr -- perhaps, in seconds. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.

        DSS property name: `Duty`, DSS property index: 12.
        """
        return self._get_obj(12, LoadShape)

    @Duty.setter
    def Duty(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(12, value)
            return

        self._set_string_o(12, value)

    @property
    def DispMode(self) -> enums.GeneratorDispatchMode:
        """
        {Default* | Loadlevel | Price } Default = Default. Dispatch mode. In default mode, gen is either always on or follows dispatch curve as specified. Otherwise, the gen comes on when either the global default load level (Loadshape "default") or the price level exceeds the dispatch value.

        DSS property name: `DispMode`, DSS property index: 13.
        """
        return enums.GeneratorDispatchMode(self._lib.Obj_GetInt32(self._ptr, 13))

    @DispMode.setter
    def DispMode(self, value: Union[AnyStr, int, enums.GeneratorDispatchMode]):
        if not isinstance(value, int):
            self._set_string_o(13, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 13, value)

    @property
    def DispMode_str(self) -> str:
        """
        {Default* | Loadlevel | Price } Default = Default. Dispatch mode. In default mode, gen is either always on or follows dispatch curve as specified. Otherwise, the gen comes on when either the global default load level (Loadshape "default") or the price level exceeds the dispatch value.

        DSS property name: `DispMode`, DSS property index: 13.
        """
        return self._get_prop_string(13)

    @DispMode_str.setter
    def DispMode_str(self, value: AnyStr):
        self.DispMode = value

    @property
    def DispValue(self) -> float:
        """
        Dispatch value. 
        If = 0.0 (default) then Generator follow dispatch curves, if any. 
        If > 0  then Generator is ON only when either the price signal (in Price dispatch mode) exceeds this value or the active circuit load multiplier * "default" loadshape value * the default yearly growth factor exceeds this value.  Then the generator follows dispatch curves (duty, daily, or yearly), if any (see also Status).

        DSS property name: `DispValue`, DSS property index: 14.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @DispValue.setter
    def DispValue(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def Conn(self) -> enums.Connection:
        """
        ={wye|LN|delta|LL}.  Default is wye.

        DSS property name: `Conn`, DSS property index: 15.
        """
        return enums.Connection(self._lib.Obj_GetInt32(self._ptr, 15))

    @Conn.setter
    def Conn(self, value: Union[AnyStr, int, enums.Connection]):
        if not isinstance(value, int):
            self._set_string_o(15, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 15, value)

    @property
    def Conn_str(self) -> str:
        """
        ={wye|LN|delta|LL}.  Default is wye.

        DSS property name: `Conn`, DSS property index: 15.
        """
        return self._get_prop_string(15)

    @Conn_str.setter
    def Conn_str(self, value: AnyStr):
        self.Conn = value

    @property
    def Status(self) -> enums.GeneratorStatus:
        """
        ={Fixed | Variable*}.  If Fixed, then dispatch multipliers do not apply. The generator is alway at full power when it is ON.  Default is Variable  (follows curves).

        DSS property name: `Status`, DSS property index: 16.
        """
        return enums.GeneratorStatus(self._lib.Obj_GetInt32(self._ptr, 16))

    @Status.setter
    def Status(self, value: Union[AnyStr, int, enums.GeneratorStatus]):
        if not isinstance(value, int):
            self._set_string_o(16, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 16, value)

    @property
    def Status_str(self) -> str:
        """
        ={Fixed | Variable*}.  If Fixed, then dispatch multipliers do not apply. The generator is alway at full power when it is ON.  Default is Variable  (follows curves).

        DSS property name: `Status`, DSS property index: 16.
        """
        return self._get_prop_string(16)

    @Status_str.setter
    def Status_str(self, value: AnyStr):
        self.Status = value

    @property
    def Class(self) -> int:
        """
        An arbitrary integer number representing the class of Generator so that Generator values may be segregated by class.

        DSS property name: `Class`, DSS property index: 17.
        """
        return self._lib.Obj_GetInt32(self._ptr, 17)

    @Class.setter
    def Class(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 17, value)

    @property
    def Vpu(self) -> float:
        """
        Per Unit voltage set point for Model = 3  (typical power flow model).  Default is 1.0. 

        DSS property name: `Vpu`, DSS property index: 18.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    @Vpu.setter
    def Vpu(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 18, value)

    @property
    def Maxkvar(self) -> float:
        """
        Maximum kvar limit for Model = 3.  Defaults to twice the specified load kvar.  Always reset this if you change PF or kvar properties.

        DSS property name: `Maxkvar`, DSS property index: 19.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    @Maxkvar.setter
    def Maxkvar(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 19, value)

    @property
    def Minkvar(self) -> float:
        """
        Minimum kvar limit for Model = 3. Enter a negative number if generator can absorb vars. Defaults to negative of Maxkvar.  Always reset this if you change PF or kvar properties.

        DSS property name: `Minkvar`, DSS property index: 20.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    @Minkvar.setter
    def Minkvar(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 20, value)

    @property
    def PVFactor(self) -> float:
        """
        Deceleration factor for P-V generator model (Model=3).  Default is 0.1. If the circuit converges easily, you may want to use a higher number such as 1.0. Use a lower number if solution diverges. Use Debugtrace=yes to create a file that will trace the convergence of a generator model.

        DSS property name: `PVFactor`, DSS property index: 21.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @PVFactor.setter
    def PVFactor(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    @property
    def ForceOn(self) -> bool:
        """
        {Yes | No}  Forces generator ON despite requirements of other dispatch modes. Stays ON until this property is set to NO, or an internal algorithm cancels the forced ON state.

        DSS property name: `ForceOn`, DSS property index: 22.
        """
        return self._lib.Obj_GetInt32(self._ptr, 22) != 0

    @ForceOn.setter
    def ForceOn(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 22, value)

    @property
    def kVA(self) -> float:
        """
        kVA rating of electrical machine. Defaults to 1.2* kW if not specified. Applied to machine or inverter definition for Dynamics mode solutions. 

        DSS property name: `kVA`, DSS property index: 23.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    @kVA.setter
    def kVA(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 23, value)

    @property
    def Xd(self) -> float:
        """
        Per unit synchronous reactance of machine. Presently used only for Thevenin impedance for power flow calcs of user models (model=6). Typically use a value 0.4 to 1.0. Default is 1.0

        DSS property name: `Xd`, DSS property index: 25.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 25)

    @Xd.setter
    def Xd(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 25, value)

    @property
    def Xdp(self) -> float:
        """
        Per unit transient reactance of the machine.  Used for Dynamics mode and Fault studies.  Default is 0.27.For user models, this value is used for the Thevenin/Norton impedance for Dynamics Mode.

        DSS property name: `Xdp`, DSS property index: 26.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 26)

    @Xdp.setter
    def Xdp(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 26, value)

    @property
    def Xdpp(self) -> float:
        """
        Per unit subtransient reactance of the machine.  Used for Harmonics. Default is 0.20.

        DSS property name: `Xdpp`, DSS property index: 27.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 27)

    @Xdpp.setter
    def Xdpp(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 27, value)

    @property
    def H(self) -> float:
        """
        Per unit mass constant of the machine.  MW-sec/MVA.  Default is 1.0.

        DSS property name: `H`, DSS property index: 28.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 28)

    @H.setter
    def H(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 28, value)

    @property
    def D(self) -> float:
        """
        Damping constant.  Usual range is 0 to 4. Default is 1.0.  Adjust to get damping

        DSS property name: `D`, DSS property index: 29.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 29)

    @D.setter
    def D(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 29, value)

    @property
    def UserModel(self) -> str:
        """
        Name of DLL containing user-written model, which computes the terminal currents for Dynamics studies, overriding the default model.  Set to "none" to negate previous setting.

        DSS property name: `UserModel`, DSS property index: 30.
        """
        return self._get_prop_string(30)

    @UserModel.setter
    def UserModel(self, value: AnyStr):
        self._set_string_o(30, value)

    @property
    def UserData(self) -> str:
        """
        String (in quotes or parentheses) that gets passed to user-written model for defining the data required for that model.

        DSS property name: `UserData`, DSS property index: 31.
        """
        return self._get_prop_string(31)

    @UserData.setter
    def UserData(self, value: AnyStr):
        self._set_string_o(31, value)

    @property
    def ShaftModel(self) -> str:
        """
        Name of user-written DLL containing a Shaft model, which models the prime mover and determines the power on the shaft for Dynamics studies. Models additional mass elements other than the single-mass model in the DSS default model. Set to "none" to negate previous setting.

        DSS property name: `ShaftModel`, DSS property index: 32.
        """
        return self._get_prop_string(32)

    @ShaftModel.setter
    def ShaftModel(self, value: AnyStr):
        self._set_string_o(32, value)

    @property
    def ShaftData(self) -> str:
        """
        String (in quotes or parentheses) that gets passed to user-written shaft dynamic model for defining the data for that model.

        DSS property name: `ShaftData`, DSS property index: 33.
        """
        return self._get_prop_string(33)

    @ShaftData.setter
    def ShaftData(self, value: AnyStr):
        self._set_string_o(33, value)

    @property
    def DutyStart(self) -> float:
        """
        Starting time offset [hours] into the duty cycle shape for this generator, defaults to 0

        DSS property name: `DutyStart`, DSS property index: 34.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 34)

    @DutyStart.setter
    def DutyStart(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 34, value)

    @property
    def DebugTrace(self) -> bool:
        """
        {Yes | No }  Default is no.  Turn this on to capture the progress of the generator model for each iteration.  Creates a separate file for each generator named "GEN_name.csv".

        DSS property name: `DebugTrace`, DSS property index: 35.
        """
        return self._lib.Obj_GetInt32(self._ptr, 35) != 0

    @DebugTrace.setter
    def DebugTrace(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 35, value)

    @property
    def Balanced(self) -> bool:
        """
        {Yes | No*} Default is No.  For Model=7, force balanced current only for 3-phase generators. Force zero- and negative-sequence to zero.

        DSS property name: `Balanced`, DSS property index: 36.
        """
        return self._lib.Obj_GetInt32(self._ptr, 36) != 0

    @Balanced.setter
    def Balanced(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 36, value)

    @property
    def XRdp(self) -> float:
        """
        Default is 20. X/R ratio for Xdp property for FaultStudy and Dynamic modes.

        DSS property name: `XRdp`, DSS property index: 37.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 37)

    @XRdp.setter
    def XRdp(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 37, value)

    @property
    def UseFuel(self) -> bool:
        """
        {Yes | *No}. Activates the use of fuel for the operation of the generator. When the fuel level reaches the reserve level, the generator stops until it gets refueled. By default, the generator is connected to a continuous fuel supply, Use this mode to mimic dependency on fuel level for different generation technologies.

        DSS property name: `UseFuel`, DSS property index: 38.
        """
        return self._lib.Obj_GetInt32(self._ptr, 38) != 0

    @UseFuel.setter
    def UseFuel(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 38, value)

    @property
    def FuelkWh(self) -> float:
        """
        {*0}Is the nominal level of fuel for the generator (kWh). It only applies if UseFuel = Yes/True

        DSS property name: `FuelkWh`, DSS property index: 39.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 39)

    @FuelkWh.setter
    def FuelkWh(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 39, value)

    @property
    def pctFuel(self) -> float:
        """
        It is a number between 0 and 100 representing the current amount of fuel available in percentage of FuelkWh. It only applies if UseFuel = Yes/True

        DSS property name: `%Fuel`, DSS property index: 40.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 40)

    @pctFuel.setter
    def pctFuel(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 40, value)

    @property
    def pctReserve(self) -> float:
        """
        It is a number between 0 and 100 representing the reserve level in percentage of FuelkWh. It only applies if UseFuel = Yes/True

        DSS property name: `%Reserve`, DSS property index: 41.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 41)

    @pctReserve.setter
    def pctReserve(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 41, value)

    def Refuel(self, value: bool = True):
        """
        It is a boolean value (Yes/True, No/False) that can be used to manually refuel the generator when needed. It only applies if UseFuel = Yes/True

        DSS property name: `Refuel`, DSS property index: 42.
        """
        self._lib.Obj_SetInt32(self._ptr, 42, value)

    @property
    def DynamicEq_str(self) -> str:
        """
        The name of the dynamic equation (DynamicExp) that will be used for defining the dynamic behavior of the generator. if not defined, the generator dynamics will follow the built-in dynamic equation.

        DSS property name: `DynamicEq`, DSS property index: 43.
        """
        return self._get_prop_string(43)

    @DynamicEq_str.setter
    def DynamicEq_str(self, value: AnyStr):
        self._set_string_o(43, value)

    @property
    def DynamicEq(self) -> DynamicExp:
        """
        The name of the dynamic equation (DynamicExp) that will be used for defining the dynamic behavior of the generator. if not defined, the generator dynamics will follow the built-in dynamic equation.

        DSS property name: `DynamicEq`, DSS property index: 43.
        """
        return self._get_obj(43, DynamicExp)

    @DynamicEq.setter
    def DynamicEq(self, value: Union[AnyStr, DynamicExp]):
        if isinstance(value, DSSObj):
            self._set_obj(43, value)
            return

        self._set_string_o(43, value)

    @property
    def DynOut(self) -> str:
        """
        The name of the variables within the Dynamic equation that will be used to govern the generator dynamics.This generator model requires 2 outputs from the dynamic equation: 

        1. Shaft speed (velocity) relative to synchronous speed.
        2. Shaft, or power, angle (relative to synchronous reference frame).

        The output variables need to be defined in tha strict order.

        DSS property name: `DynOut`, DSS property index: 44.
        """
        return self._get_prop_string(44)

    @DynOut.setter
    def DynOut(self, value: AnyStr):
        self._set_string_o(44, value)

    @property
    def Spectrum_str(self) -> str:
        """
        Name of harmonic voltage or current spectrum for this generator. Voltage behind Xd" for machine - default. Current injection for inverter. Default value is "default", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 45.
        """
        return self._get_prop_string(45)

    @Spectrum_str.setter
    def Spectrum_str(self, value: AnyStr):
        self._set_string_o(45, value)

    @property
    def Spectrum(self) -> SpectrumObj:
        """
        Name of harmonic voltage or current spectrum for this generator. Voltage behind Xd" for machine - default. Current injection for inverter. Default value is "default", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 45.
        """
        return self._get_obj(45, SpectrumObj)

    @Spectrum.setter
    def Spectrum(self, value: Union[AnyStr, SpectrumObj]):
        if isinstance(value, DSSObj):
            self._set_obj(45, value)
            return

        self._set_string_o(45, value)

    @property
    def BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 46.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 46)

    @BaseFreq.setter
    def BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 46, value)

    @property
    def Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 47.
        """
        return self._lib.Obj_GetInt32(self._ptr, 47) != 0

    @Enabled.setter
    def Enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 47, value)

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

class GeneratorBatch(DSSBatch):
    _cls_name = 'Generator'
    _obj_cls = Generator
    _cls_idx = 27


    @property
    def Phases(self) -> BatchInt32ArrayProxy:
        """
        Number of Phases, this Generator.  Power is evenly divided among phases.

        DSS property name: `Phases`, DSS property index: 1.
        """
        return BatchInt32ArrayProxy(self, 1)

    @Phases.setter
    def Phases(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(1, value)

    @property
    def Bus1(self) -> List[str]:
        """
        Bus to which the Generator is connected.  May include specific node specification.

        DSS property name: `Bus1`, DSS property index: 2.
        """
        return self._get_batch_str_prop(2) 

    @Bus1.setter
    def Bus1(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(2, value)

    @property
    def kV(self) -> BatchFloat64ArrayProxy:
        """
        Nominal rated (1.0 per unit) voltage, kV, for Generator. For 2- and 3-phase Generators, specify phase-phase kV. Otherwise, for phases=1 or phases>3, specify actual kV across each branch of the Generator. If wye (star), specify phase-neutral kV. If delta or phase-phase connected, specify phase-phase kV.

        DSS property name: `kV`, DSS property index: 3.
        """
        return BatchFloat64ArrayProxy(self, 3)

    @kV.setter
    def kV(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(3, value)

    @property
    def kW(self) -> BatchFloat64ArrayProxy:
        """
        Total base kW for the Generator.  A positive value denotes power coming OUT of the element, 
        which is the opposite of a load. This value is modified depending on the dispatch mode. Unaffected by the global load multiplier and growth curves. If you want there to be more generation, you must add more generators or change this value.

        DSS property name: `kW`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    @kW.setter
    def kW(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(4, value)

    @property
    def PF(self) -> BatchFloat64ArrayProxy:
        """
        Generator power factor. Default is 0.80. Enter negative for leading powerfactor (when kW and kvar have opposite signs.)
        A positive power factor for a generator signifies that the generator produces vars 
        as is typical for a synchronous generator.  Induction machines would be 
        specified with a negative power factor.

        DSS property name: `PF`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    @PF.setter
    def PF(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(5, value)

    @property
    def kvar(self) -> BatchFloat64ArrayProxy:
        """
        Specify the base kvar.  Alternative to specifying the power factor.  Side effect:  the power factor value is altered to agree based on present value of kW.

        DSS property name: `kvar`, DSS property index: 6.
        """
        return BatchFloat64ArrayProxy(self, 6)

    @kvar.setter
    def kvar(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(6, value)

    @property
    def Model(self) -> BatchInt32ArrayProxy:
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

    @Model.setter
    def Model(self, value: Union[int, enums.GeneratorModel, Int32Array]):
        self._set_batch_int32_array(7, value)

    @property
    def VMinpu(self) -> BatchFloat64ArrayProxy:
        """
        Default = 0.90.  Minimum per unit voltage for which the Model is assumed to apply. Below this value, the load model reverts to a constant impedance model. For model 7, the current is limited to the value computed for constant power at Vminpu.

        DSS property name: `VMinpu`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    @VMinpu.setter
    def VMinpu(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(8, value)

    @property
    def VMaxpu(self) -> BatchFloat64ArrayProxy:
        """
        Default = 1.10.  Maximum per unit voltage for which the Model is assumed to apply. Above this value, the load model reverts to a constant impedance model.

        DSS property name: `VMaxpu`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    @VMaxpu.setter
    def VMaxpu(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(9, value)

    @property
    def Yearly_str(self) -> List[str]:
        """
        Dispatch shape to use for yearly simulations.  Must be previously defined as a Loadshape object. If this is not specified, a constant value is assumed (no variation). If the generator is assumed to be ON continuously, specify Status=FIXED, or designate a curve that is 1.0 per unit at all times. Set to NONE to reset to no loadshape. Nominally for 8760 simulations.  If there are fewer points in the designated shape than the number of points in the solution, the curve is repeated.

        DSS property name: `Yearly`, DSS property index: 10.
        """
        return self._get_batch_str_prop(10)

    @Yearly_str.setter
    def Yearly_str(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(10, value)

    @property
    def Yearly(self) -> List[LoadShape]:
        """
        Dispatch shape to use for yearly simulations.  Must be previously defined as a Loadshape object. If this is not specified, a constant value is assumed (no variation). If the generator is assumed to be ON continuously, specify Status=FIXED, or designate a curve that is 1.0 per unit at all times. Set to NONE to reset to no loadshape. Nominally for 8760 simulations.  If there are fewer points in the designated shape than the number of points in the solution, the curve is repeated.

        DSS property name: `Yearly`, DSS property index: 10.
        """
        return self._get_batch_obj_prop(10)

    @Yearly.setter
    def Yearly(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]):
        self._set_batch_obj_prop(10, value)

    @property
    def Daily_str(self) -> List[str]:
        """
        Dispatch shape to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically.  If generator is assumed to be ON continuously, specify Status=FIXED, or designate a Loadshape object that is 1.0 per unit for all hours. Set to NONE to reset to no loadshape. 

        DSS property name: `Daily`, DSS property index: 11.
        """
        return self._get_batch_str_prop(11)

    @Daily_str.setter
    def Daily_str(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(11, value)

    @property
    def Daily(self) -> List[LoadShape]:
        """
        Dispatch shape to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically.  If generator is assumed to be ON continuously, specify Status=FIXED, or designate a Loadshape object that is 1.0 per unit for all hours. Set to NONE to reset to no loadshape. 

        DSS property name: `Daily`, DSS property index: 11.
        """
        return self._get_batch_obj_prop(11)

    @Daily.setter
    def Daily(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]):
        self._set_batch_obj_prop(11, value)

    @property
    def Duty_str(self) -> List[str]:
        """
        Load shape to use for duty cycle dispatch simulations such as for wind generation. Must be previously defined as a Loadshape object. Typically would have time intervals less than 1 hr -- perhaps, in seconds. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.

        DSS property name: `Duty`, DSS property index: 12.
        """
        return self._get_batch_str_prop(12)

    @Duty_str.setter
    def Duty_str(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(12, value)

    @property
    def Duty(self) -> List[LoadShape]:
        """
        Load shape to use for duty cycle dispatch simulations such as for wind generation. Must be previously defined as a Loadshape object. Typically would have time intervals less than 1 hr -- perhaps, in seconds. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.

        DSS property name: `Duty`, DSS property index: 12.
        """
        return self._get_batch_obj_prop(12)

    @Duty.setter
    def Duty(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]):
        self._set_batch_obj_prop(12, value)

    @property
    def DispMode(self) -> BatchInt32ArrayProxy:
        """
        {Default* | Loadlevel | Price } Default = Default. Dispatch mode. In default mode, gen is either always on or follows dispatch curve as specified. Otherwise, the gen comes on when either the global default load level (Loadshape "default") or the price level exceeds the dispatch value.

        DSS property name: `DispMode`, DSS property index: 13.
        """
        return BatchInt32ArrayProxy(self, 13)

    @DispMode.setter
    def DispMode(self, value: Union[AnyStr, int, enums.GeneratorDispatchMode, List[AnyStr], List[int], List[enums.GeneratorDispatchMode], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(13, value)
            return
    
        self._set_batch_int32_array(13, value)

    @property
    def DispMode_str(self) -> str:
        """
        {Default* | Loadlevel | Price } Default = Default. Dispatch mode. In default mode, gen is either always on or follows dispatch curve as specified. Otherwise, the gen comes on when either the global default load level (Loadshape "default") or the price level exceeds the dispatch value.

        DSS property name: `DispMode`, DSS property index: 13.
        """
        return self._get_batch_str_prop(13)

    @DispMode_str.setter
    def DispMode_str(self, value: AnyStr):
        self.DispMode = value

    @property
    def DispValue(self) -> BatchFloat64ArrayProxy:
        """
        Dispatch value. 
        If = 0.0 (default) then Generator follow dispatch curves, if any. 
        If > 0  then Generator is ON only when either the price signal (in Price dispatch mode) exceeds this value or the active circuit load multiplier * "default" loadshape value * the default yearly growth factor exceeds this value.  Then the generator follows dispatch curves (duty, daily, or yearly), if any (see also Status).

        DSS property name: `DispValue`, DSS property index: 14.
        """
        return BatchFloat64ArrayProxy(self, 14)

    @DispValue.setter
    def DispValue(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(14, value)

    @property
    def Conn(self) -> BatchInt32ArrayProxy:
        """
        ={wye|LN|delta|LL}.  Default is wye.

        DSS property name: `Conn`, DSS property index: 15.
        """
        return BatchInt32ArrayProxy(self, 15)

    @Conn.setter
    def Conn(self, value: Union[AnyStr, int, enums.Connection, List[AnyStr], List[int], List[enums.Connection], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(15, value)
            return
    
        self._set_batch_int32_array(15, value)

    @property
    def Conn_str(self) -> str:
        """
        ={wye|LN|delta|LL}.  Default is wye.

        DSS property name: `Conn`, DSS property index: 15.
        """
        return self._get_batch_str_prop(15)

    @Conn_str.setter
    def Conn_str(self, value: AnyStr):
        self.Conn = value

    @property
    def Status(self) -> BatchInt32ArrayProxy:
        """
        ={Fixed | Variable*}.  If Fixed, then dispatch multipliers do not apply. The generator is alway at full power when it is ON.  Default is Variable  (follows curves).

        DSS property name: `Status`, DSS property index: 16.
        """
        return BatchInt32ArrayProxy(self, 16)

    @Status.setter
    def Status(self, value: Union[AnyStr, int, enums.GeneratorStatus, List[AnyStr], List[int], List[enums.GeneratorStatus], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(16, value)
            return
    
        self._set_batch_int32_array(16, value)

    @property
    def Status_str(self) -> str:
        """
        ={Fixed | Variable*}.  If Fixed, then dispatch multipliers do not apply. The generator is alway at full power when it is ON.  Default is Variable  (follows curves).

        DSS property name: `Status`, DSS property index: 16.
        """
        return self._get_batch_str_prop(16)

    @Status_str.setter
    def Status_str(self, value: AnyStr):
        self.Status = value

    @property
    def Class(self) -> BatchInt32ArrayProxy:
        """
        An arbitrary integer number representing the class of Generator so that Generator values may be segregated by class.

        DSS property name: `Class`, DSS property index: 17.
        """
        return BatchInt32ArrayProxy(self, 17)

    @Class.setter
    def Class(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(17, value)

    @property
    def Vpu(self) -> BatchFloat64ArrayProxy:
        """
        Per Unit voltage set point for Model = 3  (typical power flow model).  Default is 1.0. 

        DSS property name: `Vpu`, DSS property index: 18.
        """
        return BatchFloat64ArrayProxy(self, 18)

    @Vpu.setter
    def Vpu(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(18, value)

    @property
    def Maxkvar(self) -> BatchFloat64ArrayProxy:
        """
        Maximum kvar limit for Model = 3.  Defaults to twice the specified load kvar.  Always reset this if you change PF or kvar properties.

        DSS property name: `Maxkvar`, DSS property index: 19.
        """
        return BatchFloat64ArrayProxy(self, 19)

    @Maxkvar.setter
    def Maxkvar(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(19, value)

    @property
    def Minkvar(self) -> BatchFloat64ArrayProxy:
        """
        Minimum kvar limit for Model = 3. Enter a negative number if generator can absorb vars. Defaults to negative of Maxkvar.  Always reset this if you change PF or kvar properties.

        DSS property name: `Minkvar`, DSS property index: 20.
        """
        return BatchFloat64ArrayProxy(self, 20)

    @Minkvar.setter
    def Minkvar(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(20, value)

    @property
    def PVFactor(self) -> BatchFloat64ArrayProxy:
        """
        Deceleration factor for P-V generator model (Model=3).  Default is 0.1. If the circuit converges easily, you may want to use a higher number such as 1.0. Use a lower number if solution diverges. Use Debugtrace=yes to create a file that will trace the convergence of a generator model.

        DSS property name: `PVFactor`, DSS property index: 21.
        """
        return BatchFloat64ArrayProxy(self, 21)

    @PVFactor.setter
    def PVFactor(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(21, value)

    @property
    def ForceOn(self) -> List[bool]:
        """
        {Yes | No}  Forces generator ON despite requirements of other dispatch modes. Stays ON until this property is set to NO, or an internal algorithm cancels the forced ON state.

        DSS property name: `ForceOn`, DSS property index: 22.
        """
        return [v != 0 for v in 
            self._get_batch_int32_prop(22)
        ]
    @ForceOn.setter
    def ForceOn(self, value: bool):
        self._set_batch_int32_array(22, value)

    @property
    def kVA(self) -> BatchFloat64ArrayProxy:
        """
        kVA rating of electrical machine. Defaults to 1.2* kW if not specified. Applied to machine or inverter definition for Dynamics mode solutions. 

        DSS property name: `kVA`, DSS property index: 23.
        """
        return BatchFloat64ArrayProxy(self, 23)

    @kVA.setter
    def kVA(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(23, value)

    @property
    def Xd(self) -> BatchFloat64ArrayProxy:
        """
        Per unit synchronous reactance of machine. Presently used only for Thevenin impedance for power flow calcs of user models (model=6). Typically use a value 0.4 to 1.0. Default is 1.0

        DSS property name: `Xd`, DSS property index: 25.
        """
        return BatchFloat64ArrayProxy(self, 25)

    @Xd.setter
    def Xd(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(25, value)

    @property
    def Xdp(self) -> BatchFloat64ArrayProxy:
        """
        Per unit transient reactance of the machine.  Used for Dynamics mode and Fault studies.  Default is 0.27.For user models, this value is used for the Thevenin/Norton impedance for Dynamics Mode.

        DSS property name: `Xdp`, DSS property index: 26.
        """
        return BatchFloat64ArrayProxy(self, 26)

    @Xdp.setter
    def Xdp(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(26, value)

    @property
    def Xdpp(self) -> BatchFloat64ArrayProxy:
        """
        Per unit subtransient reactance of the machine.  Used for Harmonics. Default is 0.20.

        DSS property name: `Xdpp`, DSS property index: 27.
        """
        return BatchFloat64ArrayProxy(self, 27)

    @Xdpp.setter
    def Xdpp(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(27, value)

    @property
    def H(self) -> BatchFloat64ArrayProxy:
        """
        Per unit mass constant of the machine.  MW-sec/MVA.  Default is 1.0.

        DSS property name: `H`, DSS property index: 28.
        """
        return BatchFloat64ArrayProxy(self, 28)

    @H.setter
    def H(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(28, value)

    @property
    def D(self) -> BatchFloat64ArrayProxy:
        """
        Damping constant.  Usual range is 0 to 4. Default is 1.0.  Adjust to get damping

        DSS property name: `D`, DSS property index: 29.
        """
        return BatchFloat64ArrayProxy(self, 29)

    @D.setter
    def D(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(29, value)

    @property
    def UserModel(self) -> List[str]:
        """
        Name of DLL containing user-written model, which computes the terminal currents for Dynamics studies, overriding the default model.  Set to "none" to negate previous setting.

        DSS property name: `UserModel`, DSS property index: 30.
        """
        return self._get_batch_str_prop(30) 

    @UserModel.setter
    def UserModel(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(30, value)

    @property
    def UserData(self) -> List[str]:
        """
        String (in quotes or parentheses) that gets passed to user-written model for defining the data required for that model.

        DSS property name: `UserData`, DSS property index: 31.
        """
        return self._get_batch_str_prop(31) 

    @UserData.setter
    def UserData(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(31, value)

    @property
    def ShaftModel(self) -> List[str]:
        """
        Name of user-written DLL containing a Shaft model, which models the prime mover and determines the power on the shaft for Dynamics studies. Models additional mass elements other than the single-mass model in the DSS default model. Set to "none" to negate previous setting.

        DSS property name: `ShaftModel`, DSS property index: 32.
        """
        return self._get_batch_str_prop(32) 

    @ShaftModel.setter
    def ShaftModel(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(32, value)

    @property
    def ShaftData(self) -> List[str]:
        """
        String (in quotes or parentheses) that gets passed to user-written shaft dynamic model for defining the data for that model.

        DSS property name: `ShaftData`, DSS property index: 33.
        """
        return self._get_batch_str_prop(33) 

    @ShaftData.setter
    def ShaftData(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(33, value)

    @property
    def DutyStart(self) -> BatchFloat64ArrayProxy:
        """
        Starting time offset [hours] into the duty cycle shape for this generator, defaults to 0

        DSS property name: `DutyStart`, DSS property index: 34.
        """
        return BatchFloat64ArrayProxy(self, 34)

    @DutyStart.setter
    def DutyStart(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(34, value)

    @property
    def DebugTrace(self) -> List[bool]:
        """
        {Yes | No }  Default is no.  Turn this on to capture the progress of the generator model for each iteration.  Creates a separate file for each generator named "GEN_name.csv".

        DSS property name: `DebugTrace`, DSS property index: 35.
        """
        return [v != 0 for v in 
            self._get_batch_int32_prop(35)
        ]
    @DebugTrace.setter
    def DebugTrace(self, value: bool):
        self._set_batch_int32_array(35, value)

    @property
    def Balanced(self) -> List[bool]:
        """
        {Yes | No*} Default is No.  For Model=7, force balanced current only for 3-phase generators. Force zero- and negative-sequence to zero.

        DSS property name: `Balanced`, DSS property index: 36.
        """
        return [v != 0 for v in 
            self._get_batch_int32_prop(36)
        ]
    @Balanced.setter
    def Balanced(self, value: bool):
        self._set_batch_int32_array(36, value)

    @property
    def XRdp(self) -> BatchFloat64ArrayProxy:
        """
        Default is 20. X/R ratio for Xdp property for FaultStudy and Dynamic modes.

        DSS property name: `XRdp`, DSS property index: 37.
        """
        return BatchFloat64ArrayProxy(self, 37)

    @XRdp.setter
    def XRdp(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(37, value)

    @property
    def UseFuel(self) -> List[bool]:
        """
        {Yes | *No}. Activates the use of fuel for the operation of the generator. When the fuel level reaches the reserve level, the generator stops until it gets refueled. By default, the generator is connected to a continuous fuel supply, Use this mode to mimic dependency on fuel level for different generation technologies.

        DSS property name: `UseFuel`, DSS property index: 38.
        """
        return [v != 0 for v in 
            self._get_batch_int32_prop(38)
        ]
    @UseFuel.setter
    def UseFuel(self, value: bool):
        self._set_batch_int32_array(38, value)

    @property
    def FuelkWh(self) -> BatchFloat64ArrayProxy:
        """
        {*0}Is the nominal level of fuel for the generator (kWh). It only applies if UseFuel = Yes/True

        DSS property name: `FuelkWh`, DSS property index: 39.
        """
        return BatchFloat64ArrayProxy(self, 39)

    @FuelkWh.setter
    def FuelkWh(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(39, value)

    @property
    def pctFuel(self) -> BatchFloat64ArrayProxy:
        """
        It is a number between 0 and 100 representing the current amount of fuel available in percentage of FuelkWh. It only applies if UseFuel = Yes/True

        DSS property name: `%Fuel`, DSS property index: 40.
        """
        return BatchFloat64ArrayProxy(self, 40)

    @pctFuel.setter
    def pctFuel(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(40, value)

    @property
    def pctReserve(self) -> BatchFloat64ArrayProxy:
        """
        It is a number between 0 and 100 representing the reserve level in percentage of FuelkWh. It only applies if UseFuel = Yes/True

        DSS property name: `%Reserve`, DSS property index: 41.
        """
        return BatchFloat64ArrayProxy(self, 41)

    @pctReserve.setter
    def pctReserve(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(41, value)

    def Refuel(self, value: Union[bool, List[bool]] = True):
        """
        It is a boolean value (Yes/True, No/False) that can be used to manually refuel the generator when needed. It only applies if UseFuel = Yes/True

        DSS property name: `Refuel`, DSS property index: 42.
        """
        self._set_batch_int32_array(42, value)

    @property
    def DynamicEq_str(self) -> List[str]:
        """
        The name of the dynamic equation (DynamicExp) that will be used for defining the dynamic behavior of the generator. if not defined, the generator dynamics will follow the built-in dynamic equation.

        DSS property name: `DynamicEq`, DSS property index: 43.
        """
        return self._get_batch_str_prop(43)

    @DynamicEq_str.setter
    def DynamicEq_str(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(43, value)

    @property
    def DynamicEq(self) -> List[DynamicExp]:
        """
        The name of the dynamic equation (DynamicExp) that will be used for defining the dynamic behavior of the generator. if not defined, the generator dynamics will follow the built-in dynamic equation.

        DSS property name: `DynamicEq`, DSS property index: 43.
        """
        return self._get_batch_obj_prop(43)

    @DynamicEq.setter
    def DynamicEq(self, value: Union[AnyStr, DynamicExp, List[AnyStr], List[DynamicExp]]):
        self._set_batch_obj_prop(43, value)

    @property
    def DynOut(self) -> List[str]:
        """
        The name of the variables within the Dynamic equation that will be used to govern the generator dynamics.This generator model requires 2 outputs from the dynamic equation: 

        1. Shaft speed (velocity) relative to synchronous speed.
        2. Shaft, or power, angle (relative to synchronous reference frame).

        The output variables need to be defined in tha strict order.

        DSS property name: `DynOut`, DSS property index: 44.
        """
        return self._get_batch_str_prop(44) 

    @DynOut.setter
    def DynOut(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(44, value)

    @property
    def Spectrum_str(self) -> List[str]:
        """
        Name of harmonic voltage or current spectrum for this generator. Voltage behind Xd" for machine - default. Current injection for inverter. Default value is "default", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 45.
        """
        return self._get_batch_str_prop(45)

    @Spectrum_str.setter
    def Spectrum_str(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(45, value)

    @property
    def Spectrum(self) -> List[SpectrumObj]:
        """
        Name of harmonic voltage or current spectrum for this generator. Voltage behind Xd" for machine - default. Current injection for inverter. Default value is "default", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 45.
        """
        return self._get_batch_obj_prop(45)

    @Spectrum.setter
    def Spectrum(self, value: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]]):
        self._set_batch_obj_prop(45, value)

    @property
    def BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 46.
        """
        return BatchFloat64ArrayProxy(self, 46)

    @BaseFreq.setter
    def BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(46, value)

    @property
    def Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 47.
        """
        return [v != 0 for v in 
            self._get_batch_int32_prop(47)
        ]
    @Enabled.setter
    def Enabled(self, value: bool):
        self._set_batch_int32_array(47, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 48.
        """
        self._set_batch_string(48, value)

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

class IGenerator(IDSSObj,GeneratorBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, Generator, GeneratorBatch)
        GeneratorBatch.__init__(self, self._api_util, sync_cls=True)
        

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Generator:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[GeneratorProperties]) -> Generator:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[GeneratorBatchProperties]) -> GeneratorBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
