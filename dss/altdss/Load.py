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
from .PCElement import PCElementBatchMixin, PCElementMixin
from .CircuitElement import CircuitElementBatchMixin, CircuitElementMixin
from .GrowthShape import GrowthShape
from .LoadShape import LoadShape
from .Spectrum import Spectrum as SpectrumObj

class Load(DSSObj, CircuitElementMixin, PCElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots + PCElementMixin._extra_slots
    _cls_name = 'Load'
    _cls_idx = 19
    _cls_prop_idx = {
        'phases': 1,
        'bus1': 2,
        'kv': 3,
        'kw': 4,
        'pf': 5,
        'model': 6,
        'yearly': 7,
        'daily': 8,
        'duty': 9,
        'growth': 10,
        'conn': 11,
        'kvar': 12,
        'rneut': 13,
        'xneut': 14,
        'status': 15,
        'cls': 16,
        'class': 16,
        'vminpu': 17,
        'vmaxpu': 18,
        'vminnorm': 19,
        'vminemerg': 20,
        'xfkva': 21,
        'allocationfactor': 22,
        'kva': 23,
        'pctmean': 24,
        '%mean': 24,
        'pctstddev': 25,
        '%stddev': 25,
        'cvrwatts': 26,
        'cvrvars': 27,
        'kwh': 28,
        'kwhdays': 29,
        'cfactor': 30,
        'cvrcurve': 31,
        'numcust': 32,
        'zipv': 33,
        'pctseriesrl': 34,
        '%seriesrl': 34,
        'relweight': 35,
        'vlowpu': 36,
        'puxharm': 37,
        'xrharm': 38,
        'spectrum': 39,
        'basefreq': 40,
        'enabled': 41,
        'like': 42,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)
       PCElementMixin.__init__(self)

    def _get_Phases(self) -> int:
        """
        Number of Phases, this load.  Load is evenly divided among phases.

        DSS property name: `Phases`, DSS property index: 1.
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    def _set_Phases(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 1, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: int

    def _get_Bus1(self) -> str:
        """
        Bus to which the load is connected.  May include specific node specification.

        DSS property name: `Bus1`, DSS property index: 2.
        """
        return self._get_prop_string(2)

    def _set_Bus1(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(2, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: str

    def _get_kV(self) -> float:
        """
        Nominal rated (1.0 per unit) voltage, kV, for load. For 2- and 3-phase loads, specify phase-phase kV. Otherwise, specify actual kV across each branch of the load. If wye (star), specify phase-neutral kV. If delta or phase-phase connected, specify phase-phase kV.

        DSS property name: `kV`, DSS property index: 3.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    def _set_kV(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 3, value, flags)

    kV = property(_get_kV, _set_kV) # type: float

    def _get_kW(self) -> float:
        """
        Total base kW for the load.  Normally, you would enter the maximum kW for the load for the first year and allow it to be adjusted by the load shapes, growth shapes, and global load multiplier.

        Legal ways to define base load:
        kW, PF
        kW, kvar
        kVA, PF
        XFKVA * Allocationfactor, PF
        kWh/(kWhdays*24) * Cfactor, PF

        DSS property name: `kW`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    def _set_kW(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 4, value, flags)

    kW = property(_get_kW, _set_kW) # type: float

    def _get_PF(self) -> float:
        """
        Load power factor.  Enter negative for leading powerfactor (when kW and kvar have opposite signs.)

        DSS property name: `PF`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    def _set_PF(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 5, value, flags)

    PF = property(_get_PF, _set_PF) # type: float

    def _get_Model(self) -> enums.LoadModel:
        """
        Integer code for the model to use for load variation with voltage. Valid values are:

        1:Standard constant P+jQ load. (Default)
        2:Constant impedance load. 
        3:Const P, Quadratic Q (like a motor).
        4:Nominal Linear P, Quadratic Q (feeder mix). Use this with CVRfactor.
        5:Constant Current Magnitude
        6:Const P, Fixed Q
        7:Const P, Fixed Impedance Q
        8:ZIPV (7 values)

        For Types 6 and 7, only the P is modified by load multipliers.

        DSS property name: `Model`, DSS property index: 6.
        """
        return enums.LoadModel(self._lib.Obj_GetInt32(self._ptr, 6))

    def _set_Model(self, value: Union[int, enums.LoadModel], flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 6, value, flags)

    Model = property(_get_Model, _set_Model) # type: enums.LoadModel

    def _get_Yearly_str(self) -> str:
        """
        LOADSHAPE object to use for yearly simulations.  Must be previously defined as a Loadshape object. Is set to the Daily load shape  when Daily is defined.  The daily load shape is repeated in this case. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. The default is no variation.

        DSS property name: `Yearly`, DSS property index: 7.
        """
        return self._get_prop_string(7)

    def _set_Yearly_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(7, value, flags)

    Yearly_str = property(_get_Yearly_str, _set_Yearly_str) # type: str

    def _get_Yearly(self) -> LoadShape:
        """
        LOADSHAPE object to use for yearly simulations.  Must be previously defined as a Loadshape object. Is set to the Daily load shape  when Daily is defined.  The daily load shape is repeated in this case. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. The default is no variation.

        DSS property name: `Yearly`, DSS property index: 7.
        """
        return self._get_obj(7, LoadShape)

    def _set_Yearly(self, value: Union[AnyStr, LoadShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(7, value, flags)
            return

        self._set_string_o(7, value, flags)

    Yearly = property(_get_Yearly, _set_Yearly) # type: LoadShape

    def _get_Daily_str(self) -> str:
        """
        LOADSHAPE object to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. Default is no variation (constant) if not defined. Side effect: Sets Yearly load shape if not already defined.

        DSS property name: `Daily`, DSS property index: 8.
        """
        return self._get_prop_string(8)

    def _set_Daily_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(8, value, flags)

    Daily_str = property(_get_Daily_str, _set_Daily_str) # type: str

    def _get_Daily(self) -> LoadShape:
        """
        LOADSHAPE object to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. Default is no variation (constant) if not defined. Side effect: Sets Yearly load shape if not already defined.

        DSS property name: `Daily`, DSS property index: 8.
        """
        return self._get_obj(8, LoadShape)

    def _set_Daily(self, value: Union[AnyStr, LoadShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(8, value, flags)
            return

        self._set_string_o(8, value, flags)

    Daily = property(_get_Daily, _set_Daily) # type: LoadShape

    def _get_Duty_str(self) -> str:
        """
        LOADSHAPE object to use for duty cycle simulations.  Must be previously defined as a Loadshape object.  Typically would have time intervals less than 1 hr. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.Set to NONE to reset to no loadshape. Set Status=Fixed to ignore Loadshape designation.  Defaults to Daily curve If not specified.

        DSS property name: `Duty`, DSS property index: 9.
        """
        return self._get_prop_string(9)

    def _set_Duty_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(9, value, flags)

    Duty_str = property(_get_Duty_str, _set_Duty_str) # type: str

    def _get_Duty(self) -> LoadShape:
        """
        LOADSHAPE object to use for duty cycle simulations.  Must be previously defined as a Loadshape object.  Typically would have time intervals less than 1 hr. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.Set to NONE to reset to no loadshape. Set Status=Fixed to ignore Loadshape designation.  Defaults to Daily curve If not specified.

        DSS property name: `Duty`, DSS property index: 9.
        """
        return self._get_obj(9, LoadShape)

    def _set_Duty(self, value: Union[AnyStr, LoadShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(9, value, flags)
            return

        self._set_string_o(9, value, flags)

    Duty = property(_get_Duty, _set_Duty) # type: LoadShape

    def _get_Growth_str(self) -> str:
        """
        Characteristic  to use for growth factors by years.  Must be previously defined as a Growthshape object. Defaults to circuit default growth factor (see Set Growth command).

        DSS property name: `Growth`, DSS property index: 10.
        """
        return self._get_prop_string(10)

    def _set_Growth_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(10, value, flags)

    Growth_str = property(_get_Growth_str, _set_Growth_str) # type: str

    def _get_Growth(self) -> GrowthShape:
        """
        Characteristic  to use for growth factors by years.  Must be previously defined as a Growthshape object. Defaults to circuit default growth factor (see Set Growth command).

        DSS property name: `Growth`, DSS property index: 10.
        """
        return self._get_obj(10, GrowthShape)

    def _set_Growth(self, value: Union[AnyStr, GrowthShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(10, value, flags)
            return

        self._set_string_o(10, value, flags)

    Growth = property(_get_Growth, _set_Growth) # type: GrowthShape

    def _get_Conn(self) -> enums.Connection:
        """
        ={wye or LN | delta or LL}.  Default is wye.

        DSS property name: `Conn`, DSS property index: 11.
        """
        return enums.Connection(self._lib.Obj_GetInt32(self._ptr, 11))

    def _set_Conn(self, value: Union[AnyStr, int, enums.Connection], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(11, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 11, value, flags)

    Conn = property(_get_Conn, _set_Conn) # type: enums.Connection

    def _get_Conn_str(self) -> str:
        """
        ={wye or LN | delta or LL}.  Default is wye.

        DSS property name: `Conn`, DSS property index: 11.
        """
        return self._get_prop_string(11)

    def _set_Conn_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Conn(value, flags)

    Conn_str = property(_get_Conn_str, _set_Conn_str) # type: str

    def _get_kvar(self) -> float:
        """
        Specify the base kvar for specifying load as kW & kvar.  Assumes kW has been already defined.  Alternative to specifying the power factor.  Side effect:  the power factor and kVA is altered to agree.

        DSS property name: `kvar`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    def _set_kvar(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 12, value, flags)

    kvar = property(_get_kvar, _set_kvar) # type: float

    def _get_RNeut(self) -> float:
        """
        Default is -1. Neutral resistance of wye (star)-connected load in actual ohms. If entered as a negative value, the neutral can be open, or floating, or it can be connected to node 0 (ground), which is the usual default. If >=0 be sure to explicitly specify the node connection for the neutral, or last, conductor. Otherwise, the neutral impedance will be shorted to ground.

        DSS property name: `RNeut`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    def _set_RNeut(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 13, value, flags)

    RNeut = property(_get_RNeut, _set_RNeut) # type: float

    def _get_XNeut(self) -> float:
        """
        Neutral reactance of wye(star)-connected load in actual ohms.  May be + or -.

        DSS property name: `XNeut`, DSS property index: 14.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    def _set_XNeut(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 14, value, flags)

    XNeut = property(_get_XNeut, _set_XNeut) # type: float

    def _get_Status(self) -> enums.LoadStatus:
        """
        ={Variable | Fixed | Exempt}.  Default is variable. If Fixed, no load multipliers apply;  however, growth multipliers do apply.  All multipliers apply to Variable loads.  Exempt loads are not modified by the global load multiplier, such as in load duration curves, etc.  Daily multipliers do apply, so setting this property to Exempt is a good way to represent industrial load that stays the same day-after-day for the period study.

        DSS property name: `Status`, DSS property index: 15.
        """
        return enums.LoadStatus(self._lib.Obj_GetInt32(self._ptr, 15))

    def _set_Status(self, value: Union[AnyStr, int, enums.LoadStatus], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(15, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 15, value, flags)

    Status = property(_get_Status, _set_Status) # type: enums.LoadStatus

    def _get_Status_str(self) -> str:
        """
        ={Variable | Fixed | Exempt}.  Default is variable. If Fixed, no load multipliers apply;  however, growth multipliers do apply.  All multipliers apply to Variable loads.  Exempt loads are not modified by the global load multiplier, such as in load duration curves, etc.  Daily multipliers do apply, so setting this property to Exempt is a good way to represent industrial load that stays the same day-after-day for the period study.

        DSS property name: `Status`, DSS property index: 15.
        """
        return self._get_prop_string(15)

    def _set_Status_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Status(value, flags)

    Status_str = property(_get_Status_str, _set_Status_str) # type: str

    def _get_Class(self) -> int:
        """
        An arbitrary integer number representing the class of load so that load values may be segregated by load value. Default is 1; not used internally.

        DSS property name: `Class`, DSS property index: 16.
        """
        return self._lib.Obj_GetInt32(self._ptr, 16)

    def _set_Class(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 16, value, flags)

    Class = property(_get_Class, _set_Class) # type: int

    def _get_VMinpu(self) -> float:
        """
        Default = 0.95.  Minimum per unit voltage for which the MODEL is assumed to apply. Lower end of normal voltage range.Below this value, the load model reverts to a constant impedance model that matches the model at the transition voltage. See also "Vlowpu" which causes the model to match Model=2 below the transition voltage.

        DSS property name: `VMinpu`, DSS property index: 17.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    def _set_VMinpu(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 17, value, flags)

    VMinpu = property(_get_VMinpu, _set_VMinpu) # type: float

    def _get_VMaxpu(self) -> float:
        """
        Default = 1.05.  Maximum per unit voltage for which the MODEL is assumed to apply. Above this value, the load model reverts to a constant impedance model.

        DSS property name: `VMaxpu`, DSS property index: 18.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    def _set_VMaxpu(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 18, value, flags)

    VMaxpu = property(_get_VMaxpu, _set_VMaxpu) # type: float

    def _get_VMinNorm(self) -> float:
        """
        Minimum per unit voltage for load EEN evaluations, Normal limit.  Default = 0, which defaults to system "vminnorm" property (see Set Command under Executive).  If this property is specified, it ALWAYS overrides the system specification. This allows you to have different criteria for different loads. Set to zero to revert to the default system value.

        DSS property name: `VMinNorm`, DSS property index: 19.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    def _set_VMinNorm(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 19, value, flags)

    VMinNorm = property(_get_VMinNorm, _set_VMinNorm) # type: float

    def _get_VMinEmerg(self) -> float:
        """
        Minimum per unit voltage for load UE evaluations, Emergency limit.  Default = 0, which defaults to system "vminemerg" property (see Set Command under Executive).  If this property is specified, it ALWAYS overrides the system specification. This allows you to have different criteria for different loads. Set to zero to revert to the default system value.

        DSS property name: `VMinEmerg`, DSS property index: 20.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    def _set_VMinEmerg(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 20, value, flags)

    VMinEmerg = property(_get_VMinEmerg, _set_VMinEmerg) # type: float

    def _get_XfkVA(self) -> float:
        """
        Default = 0.0.  Rated kVA of service transformer for allocating loads based on connected kVA at a bus. Side effect:  kW, PF, and kvar are modified. See help on kVA.

        DSS property name: `XfkVA`, DSS property index: 21.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    def _set_XfkVA(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 21, value, flags)

    XfkVA = property(_get_XfkVA, _set_XfkVA) # type: float

    def _get_AllocationFactor(self) -> float:
        """
        Default = 0.5.  Allocation factor for allocating loads based on connected kVA at a bus. Side effect:  kW, PF, and kvar are modified by multiplying this factor times the XFKVA (if > 0).

        DSS property name: `AllocationFactor`, DSS property index: 22.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    def _set_AllocationFactor(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 22, value, flags)

    AllocationFactor = property(_get_AllocationFactor, _set_AllocationFactor) # type: float

    def _get_kVA(self) -> float:
        """
        Specify base Load in kVA (and power factor)

        Legal ways to define base load:
        kW, PF
        kW, kvar
        kVA, PF
        XFKVA * Allocationfactor, PF
        kWh/(kWhdays*24) * Cfactor, PF

        DSS property name: `kVA`, DSS property index: 23.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    def _set_kVA(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 23, value, flags)

    kVA = property(_get_kVA, _set_kVA) # type: float

    def _get_pctMean(self) -> float:
        """
        Percent mean value for load to use for monte carlo studies if no loadshape is assigned to this load. Default is 50.

        DSS property name: `%Mean`, DSS property index: 24.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    def _set_pctMean(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 24, value, flags)

    pctMean = property(_get_pctMean, _set_pctMean) # type: float

    def _get_pctStdDev(self) -> float:
        """
        Percent Std deviation value for load to use for monte carlo studies if no loadshape is assigned to this load. Default is 10.

        DSS property name: `%StdDev`, DSS property index: 25.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 25)

    def _set_pctStdDev(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 25, value, flags)

    pctStdDev = property(_get_pctStdDev, _set_pctStdDev) # type: float

    def _get_CVRWatts(self) -> float:
        """
        Percent reduction in active power (watts) per 1% reduction in voltage from 100% rated. Default=1. 
         Typical values range from 0.4 to 0.8. Applies to Model=4 only.
         Intended to represent conservation voltage reduction or voltage optimization measures.

        DSS property name: `CVRWatts`, DSS property index: 26.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 26)

    def _set_CVRWatts(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 26, value, flags)

    CVRWatts = property(_get_CVRWatts, _set_CVRWatts) # type: float

    def _get_CVRVars(self) -> float:
        """
        Percent reduction in reactive power (vars) per 1% reduction in voltage from 100% rated. Default=2. 
         Typical values range from 2 to 3. Applies to Model=4 only.
         Intended to represent conservation voltage reduction or voltage optimization measures.

        DSS property name: `CVRVars`, DSS property index: 27.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 27)

    def _set_CVRVars(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 27, value, flags)

    CVRVars = property(_get_CVRVars, _set_CVRVars) # type: float

    def _get_kWh(self) -> float:
        """
        kWh billed for this period. Default is 0. See help on kVA and Cfactor and kWhDays.

        DSS property name: `kWh`, DSS property index: 28.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 28)

    def _set_kWh(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 28, value, flags)

    kWh = property(_get_kWh, _set_kWh) # type: float

    def _get_kWhDays(self) -> float:
        """
        Length of kWh billing period in days (24 hr days). Default is 30. Average demand is computed using this value.

        DSS property name: `kWhDays`, DSS property index: 29.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 29)

    def _set_kWhDays(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 29, value, flags)

    kWhDays = property(_get_kWhDays, _set_kWhDays) # type: float

    def _get_CFactor(self) -> float:
        """
        Factor relating average kW to peak kW. Default is 4.0. See kWh and kWhdays. See kVA.

        DSS property name: `CFactor`, DSS property index: 30.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 30)

    def _set_CFactor(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 30, value, flags)

    CFactor = property(_get_CFactor, _set_CFactor) # type: float

    def _get_CVRCurve_str(self) -> str:
        """
        Default is NONE. Curve describing both watt and var factors as a function of time. Refers to a LoadShape object with both Mult and Qmult defined. Define a Loadshape to agree with yearly or daily curve according to the type of analysis being done. If NONE, the CVRwatts and CVRvars factors are used and assumed constant.

        DSS property name: `CVRCurve`, DSS property index: 31.
        """
        return self._get_prop_string(31)

    def _set_CVRCurve_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(31, value, flags)

    CVRCurve_str = property(_get_CVRCurve_str, _set_CVRCurve_str) # type: str

    def _get_CVRCurve(self) -> LoadShape:
        """
        Default is NONE. Curve describing both watt and var factors as a function of time. Refers to a LoadShape object with both Mult and Qmult defined. Define a Loadshape to agree with yearly or daily curve according to the type of analysis being done. If NONE, the CVRwatts and CVRvars factors are used and assumed constant.

        DSS property name: `CVRCurve`, DSS property index: 31.
        """
        return self._get_obj(31, LoadShape)

    def _set_CVRCurve(self, value: Union[AnyStr, LoadShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(31, value, flags)
            return

        self._set_string_o(31, value, flags)

    CVRCurve = property(_get_CVRCurve, _set_CVRCurve) # type: LoadShape

    def _get_NumCust(self) -> int:
        """
        Number of customers, this load. Default is 1.

        DSS property name: `NumCust`, DSS property index: 32.
        """
        return self._lib.Obj_GetInt32(self._ptr, 32)

    def _set_NumCust(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 32, value, flags)

    NumCust = property(_get_NumCust, _set_NumCust) # type: int

    def _get_ZIPV(self) -> Float64Array:
        """
        Array of 7 coefficients:

         First 3 are ZIP weighting factors for real power (should sum to 1)
         Next 3 are ZIP weighting factors for reactive power (should sum to 1)
         Last 1 is cut-off voltage in p.u. of base kV; load is 0 below this cut-off
         No defaults; all coefficients must be specified if using model=8.

        DSS property name: `ZIPV`, DSS property index: 33.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 33)

    def _set_ZIPV(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(33, value, flags)

    ZIPV = property(_get_ZIPV, _set_ZIPV) # type: Float64Array

    def _get_pctSeriesRL(self) -> float:
        """
        Percent of load that is series R-L for Harmonic studies. Default is 50. Remainder is assumed to be parallel R and L. This can have a significant impact on the amount of damping observed in Harmonics solutions.

        DSS property name: `%SeriesRL`, DSS property index: 34.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 34)

    def _set_pctSeriesRL(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 34, value, flags)

    pctSeriesRL = property(_get_pctSeriesRL, _set_pctSeriesRL) # type: float

    def _get_RelWeight(self) -> float:
        """
        Relative weighting factor for reliability calcs. Default = 1. Used to designate high priority loads such as hospitals, etc. 

        Is multiplied by number of customers and load kW during reliability calcs.

        DSS property name: `RelWeight`, DSS property index: 35.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 35)

    def _set_RelWeight(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 35, value, flags)

    RelWeight = property(_get_RelWeight, _set_RelWeight) # type: float

    def _get_VLowpu(self) -> float:
        """
        Default = 0.50.  Per unit voltage at which the model switches to same as constant Z model (model=2). This allows more consistent convergence at very low voltaes due to opening switches or solving for fault situations.

        DSS property name: `VLowpu`, DSS property index: 36.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 36)

    def _set_VLowpu(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 36, value, flags)

    VLowpu = property(_get_VLowpu, _set_VLowpu) # type: float

    def _get_puXHarm(self) -> float:
        """
        Special reactance, pu (based on kVA, kV properties), for the series impedance branch in the load model for HARMONICS analysis. Generally used to represent motor load blocked rotor reactance. If not specified (that is, set =0, the default value), the series branch is computed from the percentage of the nominal load at fundamental frequency specified by the %SERIESRL property. 

        Applies to load model in HARMONICS mode only.

        A typical value would be approximately 0.20 pu based on kVA * %SeriesRL / 100.0.

        DSS property name: `puXHarm`, DSS property index: 37.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 37)

    def _set_puXHarm(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 37, value, flags)

    puXHarm = property(_get_puXHarm, _set_puXHarm) # type: float

    def _get_XRHarm(self) -> float:
        """
        X/R ratio of the special harmonics mode reactance specified by the puXHARM property at fundamental frequency. Default is 6. 

        DSS property name: `XRHarm`, DSS property index: 38.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 38)

    def _set_XRHarm(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 38, value, flags)

    XRHarm = property(_get_XRHarm, _set_XRHarm) # type: float

    def _get_Spectrum_str(self) -> str:
        """
        Name of harmonic current spectrum for this load.  Default is "defaultload", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 39.
        """
        return self._get_prop_string(39)

    def _set_Spectrum_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(39, value, flags)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str) # type: str

    def _get_Spectrum(self) -> SpectrumObj:
        """
        Name of harmonic current spectrum for this load.  Default is "defaultload", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 39.
        """
        return self._get_obj(39, SpectrumObj)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(39, value, flags)
            return

        self._set_string_o(39, value, flags)

    Spectrum = property(_get_Spectrum, _set_Spectrum) # type: SpectrumObj

    def _get_BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 40.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 40)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 40, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float

    def _get_Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 41.
        """
        return self._lib.Obj_GetInt32(self._ptr, 41) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 41, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 42.
        """
        self._set_string_o(42, value)


class LoadProperties(TypedDict):
    Phases: int
    Bus1: AnyStr
    kV: float
    kW: float
    PF: float
    Model: Union[int, enums.LoadModel]
    Yearly: Union[AnyStr, LoadShape]
    Daily: Union[AnyStr, LoadShape]
    Duty: Union[AnyStr, LoadShape]
    Growth: Union[AnyStr, GrowthShape]
    Conn: Union[AnyStr, int, enums.Connection]
    kvar: float
    RNeut: float
    XNeut: float
    Status: Union[AnyStr, int, enums.LoadStatus]
    Class: int
    VMinpu: float
    VMaxpu: float
    VMinNorm: float
    VMinEmerg: float
    XfkVA: float
    AllocationFactor: float
    kVA: float
    pctMean: float
    pctStdDev: float
    CVRWatts: float
    CVRVars: float
    kWh: float
    kWhDays: float
    CFactor: float
    CVRCurve: Union[AnyStr, LoadShape]
    NumCust: int
    ZIPV: Float64Array
    pctSeriesRL: float
    RelWeight: float
    VLowpu: float
    puXHarm: float
    XRHarm: float
    Spectrum: Union[AnyStr, SpectrumObj]
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class LoadBatch(DSSBatch, CircuitElementBatchMixin, PCElementBatchMixin):
    _cls_name = 'Load'
    _obj_cls = Load
    _cls_idx = 19

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)
       PCElementBatchMixin.__init__(self)

    def _get_Phases(self) -> BatchInt32ArrayProxy:
        """
        Number of Phases, this load.  Load is evenly divided among phases.

        DSS property name: `Phases`, DSS property index: 1.
        """
        return BatchInt32ArrayProxy(self, 1)

    def _set_Phases(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(1, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: BatchInt32ArrayProxy

    def _get_Bus1(self) -> List[str]:
        """
        Bus to which the load is connected.  May include specific node specification.

        DSS property name: `Bus1`, DSS property index: 2.
        """
        return self._get_batch_str_prop(2)

    def _set_Bus1(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(2, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: List[str]

    def _get_kV(self) -> BatchFloat64ArrayProxy:
        """
        Nominal rated (1.0 per unit) voltage, kV, for load. For 2- and 3-phase loads, specify phase-phase kV. Otherwise, specify actual kV across each branch of the load. If wye (star), specify phase-neutral kV. If delta or phase-phase connected, specify phase-phase kV.

        DSS property name: `kV`, DSS property index: 3.
        """
        return BatchFloat64ArrayProxy(self, 3)

    def _set_kV(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(3, value, flags)

    kV = property(_get_kV, _set_kV) # type: BatchFloat64ArrayProxy

    def _get_kW(self) -> BatchFloat64ArrayProxy:
        """
        Total base kW for the load.  Normally, you would enter the maximum kW for the load for the first year and allow it to be adjusted by the load shapes, growth shapes, and global load multiplier.

        Legal ways to define base load:
        kW, PF
        kW, kvar
        kVA, PF
        XFKVA * Allocationfactor, PF
        kWh/(kWhdays*24) * Cfactor, PF

        DSS property name: `kW`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    def _set_kW(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(4, value, flags)

    kW = property(_get_kW, _set_kW) # type: BatchFloat64ArrayProxy

    def _get_PF(self) -> BatchFloat64ArrayProxy:
        """
        Load power factor.  Enter negative for leading powerfactor (when kW and kvar have opposite signs.)

        DSS property name: `PF`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    def _set_PF(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(5, value, flags)

    PF = property(_get_PF, _set_PF) # type: BatchFloat64ArrayProxy

    def _get_Model(self) -> BatchInt32ArrayProxy:
        """
        Integer code for the model to use for load variation with voltage. Valid values are:

        1:Standard constant P+jQ load. (Default)
        2:Constant impedance load. 
        3:Const P, Quadratic Q (like a motor).
        4:Nominal Linear P, Quadratic Q (feeder mix). Use this with CVRfactor.
        5:Constant Current Magnitude
        6:Const P, Fixed Q
        7:Const P, Fixed Impedance Q
        8:ZIPV (7 values)

        For Types 6 and 7, only the P is modified by load multipliers.

        DSS property name: `Model`, DSS property index: 6.
        """
        return BatchInt32ArrayProxy(self, 6)

    def _set_Model(self, value: Union[int, enums.LoadModel, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(6, value, flags)

    Model = property(_get_Model, _set_Model) # type: BatchInt32ArrayProxy

    def _get_Yearly_str(self) -> List[str]:
        """
        LOADSHAPE object to use for yearly simulations.  Must be previously defined as a Loadshape object. Is set to the Daily load shape  when Daily is defined.  The daily load shape is repeated in this case. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. The default is no variation.

        DSS property name: `Yearly`, DSS property index: 7.
        """
        return self._get_batch_str_prop(7)

    def _set_Yearly_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(7, value, flags)

    Yearly_str = property(_get_Yearly_str, _set_Yearly_str) # type: List[str]

    def _get_Yearly(self) -> List[LoadShape]:
        """
        LOADSHAPE object to use for yearly simulations.  Must be previously defined as a Loadshape object. Is set to the Daily load shape  when Daily is defined.  The daily load shape is repeated in this case. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. The default is no variation.

        DSS property name: `Yearly`, DSS property index: 7.
        """
        return self._get_batch_obj_prop(7)

    def _set_Yearly(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(7, value, flags)

    Yearly = property(_get_Yearly, _set_Yearly) # type: List[LoadShape]

    def _get_Daily_str(self) -> List[str]:
        """
        LOADSHAPE object to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. Default is no variation (constant) if not defined. Side effect: Sets Yearly load shape if not already defined.

        DSS property name: `Daily`, DSS property index: 8.
        """
        return self._get_batch_str_prop(8)

    def _set_Daily_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(8, value, flags)

    Daily_str = property(_get_Daily_str, _set_Daily_str) # type: List[str]

    def _get_Daily(self) -> List[LoadShape]:
        """
        LOADSHAPE object to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. Default is no variation (constant) if not defined. Side effect: Sets Yearly load shape if not already defined.

        DSS property name: `Daily`, DSS property index: 8.
        """
        return self._get_batch_obj_prop(8)

    def _set_Daily(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(8, value, flags)

    Daily = property(_get_Daily, _set_Daily) # type: List[LoadShape]

    def _get_Duty_str(self) -> List[str]:
        """
        LOADSHAPE object to use for duty cycle simulations.  Must be previously defined as a Loadshape object.  Typically would have time intervals less than 1 hr. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.Set to NONE to reset to no loadshape. Set Status=Fixed to ignore Loadshape designation.  Defaults to Daily curve If not specified.

        DSS property name: `Duty`, DSS property index: 9.
        """
        return self._get_batch_str_prop(9)

    def _set_Duty_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(9, value, flags)

    Duty_str = property(_get_Duty_str, _set_Duty_str) # type: List[str]

    def _get_Duty(self) -> List[LoadShape]:
        """
        LOADSHAPE object to use for duty cycle simulations.  Must be previously defined as a Loadshape object.  Typically would have time intervals less than 1 hr. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.Set to NONE to reset to no loadshape. Set Status=Fixed to ignore Loadshape designation.  Defaults to Daily curve If not specified.

        DSS property name: `Duty`, DSS property index: 9.
        """
        return self._get_batch_obj_prop(9)

    def _set_Duty(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(9, value, flags)

    Duty = property(_get_Duty, _set_Duty) # type: List[LoadShape]

    def _get_Growth_str(self) -> List[str]:
        """
        Characteristic  to use for growth factors by years.  Must be previously defined as a Growthshape object. Defaults to circuit default growth factor (see Set Growth command).

        DSS property name: `Growth`, DSS property index: 10.
        """
        return self._get_batch_str_prop(10)

    def _set_Growth_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(10, value, flags)

    Growth_str = property(_get_Growth_str, _set_Growth_str) # type: List[str]

    def _get_Growth(self) -> List[GrowthShape]:
        """
        Characteristic  to use for growth factors by years.  Must be previously defined as a Growthshape object. Defaults to circuit default growth factor (see Set Growth command).

        DSS property name: `Growth`, DSS property index: 10.
        """
        return self._get_batch_obj_prop(10)

    def _set_Growth(self, value: Union[AnyStr, GrowthShape, List[AnyStr], List[GrowthShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(10, value, flags)

    Growth = property(_get_Growth, _set_Growth) # type: List[GrowthShape]

    def _get_Conn(self) -> BatchInt32ArrayProxy:
        """
        ={wye or LN | delta or LL}.  Default is wye.

        DSS property name: `Conn`, DSS property index: 11.
        """
        return BatchInt32ArrayProxy(self, 11)

    def _set_Conn(self, value: Union[AnyStr, int, enums.Connection, List[AnyStr], List[int], List[enums.Connection], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(11, value, flags)
            return

        self._set_batch_int32_array(11, value, flags)

    Conn = property(_get_Conn, _set_Conn) # type: BatchInt32ArrayProxy

    def _get_Conn_str(self) -> List[str]:
        """
        ={wye or LN | delta or LL}.  Default is wye.

        DSS property name: `Conn`, DSS property index: 11.
        """
        return self._get_batch_str_prop(11)

    def _set_Conn_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Conn(value, flags)

    Conn_str = property(_get_Conn_str, _set_Conn_str) # type: List[str]

    def _get_kvar(self) -> BatchFloat64ArrayProxy:
        """
        Specify the base kvar for specifying load as kW & kvar.  Assumes kW has been already defined.  Alternative to specifying the power factor.  Side effect:  the power factor and kVA is altered to agree.

        DSS property name: `kvar`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    def _set_kvar(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(12, value, flags)

    kvar = property(_get_kvar, _set_kvar) # type: BatchFloat64ArrayProxy

    def _get_RNeut(self) -> BatchFloat64ArrayProxy:
        """
        Default is -1. Neutral resistance of wye (star)-connected load in actual ohms. If entered as a negative value, the neutral can be open, or floating, or it can be connected to node 0 (ground), which is the usual default. If >=0 be sure to explicitly specify the node connection for the neutral, or last, conductor. Otherwise, the neutral impedance will be shorted to ground.

        DSS property name: `RNeut`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    def _set_RNeut(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(13, value, flags)

    RNeut = property(_get_RNeut, _set_RNeut) # type: BatchFloat64ArrayProxy

    def _get_XNeut(self) -> BatchFloat64ArrayProxy:
        """
        Neutral reactance of wye(star)-connected load in actual ohms.  May be + or -.

        DSS property name: `XNeut`, DSS property index: 14.
        """
        return BatchFloat64ArrayProxy(self, 14)

    def _set_XNeut(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(14, value, flags)

    XNeut = property(_get_XNeut, _set_XNeut) # type: BatchFloat64ArrayProxy

    def _get_Status(self) -> BatchInt32ArrayProxy:
        """
        ={Variable | Fixed | Exempt}.  Default is variable. If Fixed, no load multipliers apply;  however, growth multipliers do apply.  All multipliers apply to Variable loads.  Exempt loads are not modified by the global load multiplier, such as in load duration curves, etc.  Daily multipliers do apply, so setting this property to Exempt is a good way to represent industrial load that stays the same day-after-day for the period study.

        DSS property name: `Status`, DSS property index: 15.
        """
        return BatchInt32ArrayProxy(self, 15)

    def _set_Status(self, value: Union[AnyStr, int, enums.LoadStatus, List[AnyStr], List[int], List[enums.LoadStatus], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(15, value, flags)
            return

        self._set_batch_int32_array(15, value, flags)

    Status = property(_get_Status, _set_Status) # type: BatchInt32ArrayProxy

    def _get_Status_str(self) -> List[str]:
        """
        ={Variable | Fixed | Exempt}.  Default is variable. If Fixed, no load multipliers apply;  however, growth multipliers do apply.  All multipliers apply to Variable loads.  Exempt loads are not modified by the global load multiplier, such as in load duration curves, etc.  Daily multipliers do apply, so setting this property to Exempt is a good way to represent industrial load that stays the same day-after-day for the period study.

        DSS property name: `Status`, DSS property index: 15.
        """
        return self._get_batch_str_prop(15)

    def _set_Status_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Status(value, flags)

    Status_str = property(_get_Status_str, _set_Status_str) # type: List[str]

    def _get_Class(self) -> BatchInt32ArrayProxy:
        """
        An arbitrary integer number representing the class of load so that load values may be segregated by load value. Default is 1; not used internally.

        DSS property name: `Class`, DSS property index: 16.
        """
        return BatchInt32ArrayProxy(self, 16)

    def _set_Class(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(16, value, flags)

    Class = property(_get_Class, _set_Class) # type: BatchInt32ArrayProxy

    def _get_VMinpu(self) -> BatchFloat64ArrayProxy:
        """
        Default = 0.95.  Minimum per unit voltage for which the MODEL is assumed to apply. Lower end of normal voltage range.Below this value, the load model reverts to a constant impedance model that matches the model at the transition voltage. See also "Vlowpu" which causes the model to match Model=2 below the transition voltage.

        DSS property name: `VMinpu`, DSS property index: 17.
        """
        return BatchFloat64ArrayProxy(self, 17)

    def _set_VMinpu(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(17, value, flags)

    VMinpu = property(_get_VMinpu, _set_VMinpu) # type: BatchFloat64ArrayProxy

    def _get_VMaxpu(self) -> BatchFloat64ArrayProxy:
        """
        Default = 1.05.  Maximum per unit voltage for which the MODEL is assumed to apply. Above this value, the load model reverts to a constant impedance model.

        DSS property name: `VMaxpu`, DSS property index: 18.
        """
        return BatchFloat64ArrayProxy(self, 18)

    def _set_VMaxpu(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(18, value, flags)

    VMaxpu = property(_get_VMaxpu, _set_VMaxpu) # type: BatchFloat64ArrayProxy

    def _get_VMinNorm(self) -> BatchFloat64ArrayProxy:
        """
        Minimum per unit voltage for load EEN evaluations, Normal limit.  Default = 0, which defaults to system "vminnorm" property (see Set Command under Executive).  If this property is specified, it ALWAYS overrides the system specification. This allows you to have different criteria for different loads. Set to zero to revert to the default system value.

        DSS property name: `VMinNorm`, DSS property index: 19.
        """
        return BatchFloat64ArrayProxy(self, 19)

    def _set_VMinNorm(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(19, value, flags)

    VMinNorm = property(_get_VMinNorm, _set_VMinNorm) # type: BatchFloat64ArrayProxy

    def _get_VMinEmerg(self) -> BatchFloat64ArrayProxy:
        """
        Minimum per unit voltage for load UE evaluations, Emergency limit.  Default = 0, which defaults to system "vminemerg" property (see Set Command under Executive).  If this property is specified, it ALWAYS overrides the system specification. This allows you to have different criteria for different loads. Set to zero to revert to the default system value.

        DSS property name: `VMinEmerg`, DSS property index: 20.
        """
        return BatchFloat64ArrayProxy(self, 20)

    def _set_VMinEmerg(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(20, value, flags)

    VMinEmerg = property(_get_VMinEmerg, _set_VMinEmerg) # type: BatchFloat64ArrayProxy

    def _get_XfkVA(self) -> BatchFloat64ArrayProxy:
        """
        Default = 0.0.  Rated kVA of service transformer for allocating loads based on connected kVA at a bus. Side effect:  kW, PF, and kvar are modified. See help on kVA.

        DSS property name: `XfkVA`, DSS property index: 21.
        """
        return BatchFloat64ArrayProxy(self, 21)

    def _set_XfkVA(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(21, value, flags)

    XfkVA = property(_get_XfkVA, _set_XfkVA) # type: BatchFloat64ArrayProxy

    def _get_AllocationFactor(self) -> BatchFloat64ArrayProxy:
        """
        Default = 0.5.  Allocation factor for allocating loads based on connected kVA at a bus. Side effect:  kW, PF, and kvar are modified by multiplying this factor times the XFKVA (if > 0).

        DSS property name: `AllocationFactor`, DSS property index: 22.
        """
        return BatchFloat64ArrayProxy(self, 22)

    def _set_AllocationFactor(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(22, value, flags)

    AllocationFactor = property(_get_AllocationFactor, _set_AllocationFactor) # type: BatchFloat64ArrayProxy

    def _get_kVA(self) -> BatchFloat64ArrayProxy:
        """
        Specify base Load in kVA (and power factor)

        Legal ways to define base load:
        kW, PF
        kW, kvar
        kVA, PF
        XFKVA * Allocationfactor, PF
        kWh/(kWhdays*24) * Cfactor, PF

        DSS property name: `kVA`, DSS property index: 23.
        """
        return BatchFloat64ArrayProxy(self, 23)

    def _set_kVA(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(23, value, flags)

    kVA = property(_get_kVA, _set_kVA) # type: BatchFloat64ArrayProxy

    def _get_pctMean(self) -> BatchFloat64ArrayProxy:
        """
        Percent mean value for load to use for monte carlo studies if no loadshape is assigned to this load. Default is 50.

        DSS property name: `%Mean`, DSS property index: 24.
        """
        return BatchFloat64ArrayProxy(self, 24)

    def _set_pctMean(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(24, value, flags)

    pctMean = property(_get_pctMean, _set_pctMean) # type: BatchFloat64ArrayProxy

    def _get_pctStdDev(self) -> BatchFloat64ArrayProxy:
        """
        Percent Std deviation value for load to use for monte carlo studies if no loadshape is assigned to this load. Default is 10.

        DSS property name: `%StdDev`, DSS property index: 25.
        """
        return BatchFloat64ArrayProxy(self, 25)

    def _set_pctStdDev(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(25, value, flags)

    pctStdDev = property(_get_pctStdDev, _set_pctStdDev) # type: BatchFloat64ArrayProxy

    def _get_CVRWatts(self) -> BatchFloat64ArrayProxy:
        """
        Percent reduction in active power (watts) per 1% reduction in voltage from 100% rated. Default=1. 
         Typical values range from 0.4 to 0.8. Applies to Model=4 only.
         Intended to represent conservation voltage reduction or voltage optimization measures.

        DSS property name: `CVRWatts`, DSS property index: 26.
        """
        return BatchFloat64ArrayProxy(self, 26)

    def _set_CVRWatts(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(26, value, flags)

    CVRWatts = property(_get_CVRWatts, _set_CVRWatts) # type: BatchFloat64ArrayProxy

    def _get_CVRVars(self) -> BatchFloat64ArrayProxy:
        """
        Percent reduction in reactive power (vars) per 1% reduction in voltage from 100% rated. Default=2. 
         Typical values range from 2 to 3. Applies to Model=4 only.
         Intended to represent conservation voltage reduction or voltage optimization measures.

        DSS property name: `CVRVars`, DSS property index: 27.
        """
        return BatchFloat64ArrayProxy(self, 27)

    def _set_CVRVars(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(27, value, flags)

    CVRVars = property(_get_CVRVars, _set_CVRVars) # type: BatchFloat64ArrayProxy

    def _get_kWh(self) -> BatchFloat64ArrayProxy:
        """
        kWh billed for this period. Default is 0. See help on kVA and Cfactor and kWhDays.

        DSS property name: `kWh`, DSS property index: 28.
        """
        return BatchFloat64ArrayProxy(self, 28)

    def _set_kWh(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(28, value, flags)

    kWh = property(_get_kWh, _set_kWh) # type: BatchFloat64ArrayProxy

    def _get_kWhDays(self) -> BatchFloat64ArrayProxy:
        """
        Length of kWh billing period in days (24 hr days). Default is 30. Average demand is computed using this value.

        DSS property name: `kWhDays`, DSS property index: 29.
        """
        return BatchFloat64ArrayProxy(self, 29)

    def _set_kWhDays(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(29, value, flags)

    kWhDays = property(_get_kWhDays, _set_kWhDays) # type: BatchFloat64ArrayProxy

    def _get_CFactor(self) -> BatchFloat64ArrayProxy:
        """
        Factor relating average kW to peak kW. Default is 4.0. See kWh and kWhdays. See kVA.

        DSS property name: `CFactor`, DSS property index: 30.
        """
        return BatchFloat64ArrayProxy(self, 30)

    def _set_CFactor(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(30, value, flags)

    CFactor = property(_get_CFactor, _set_CFactor) # type: BatchFloat64ArrayProxy

    def _get_CVRCurve_str(self) -> List[str]:
        """
        Default is NONE. Curve describing both watt and var factors as a function of time. Refers to a LoadShape object with both Mult and Qmult defined. Define a Loadshape to agree with yearly or daily curve according to the type of analysis being done. If NONE, the CVRwatts and CVRvars factors are used and assumed constant.

        DSS property name: `CVRCurve`, DSS property index: 31.
        """
        return self._get_batch_str_prop(31)

    def _set_CVRCurve_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(31, value, flags)

    CVRCurve_str = property(_get_CVRCurve_str, _set_CVRCurve_str) # type: List[str]

    def _get_CVRCurve(self) -> List[LoadShape]:
        """
        Default is NONE. Curve describing both watt and var factors as a function of time. Refers to a LoadShape object with both Mult and Qmult defined. Define a Loadshape to agree with yearly or daily curve according to the type of analysis being done. If NONE, the CVRwatts and CVRvars factors are used and assumed constant.

        DSS property name: `CVRCurve`, DSS property index: 31.
        """
        return self._get_batch_obj_prop(31)

    def _set_CVRCurve(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(31, value, flags)

    CVRCurve = property(_get_CVRCurve, _set_CVRCurve) # type: List[LoadShape]

    def _get_NumCust(self) -> BatchInt32ArrayProxy:
        """
        Number of customers, this load. Default is 1.

        DSS property name: `NumCust`, DSS property index: 32.
        """
        return BatchInt32ArrayProxy(self, 32)

    def _set_NumCust(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(32, value, flags)

    NumCust = property(_get_NumCust, _set_NumCust) # type: BatchInt32ArrayProxy

    def _get_ZIPV(self) -> List[Float64Array]:
        """
        Array of 7 coefficients:

         First 3 are ZIP weighting factors for real power (should sum to 1)
         Next 3 are ZIP weighting factors for reactive power (should sum to 1)
         Last 1 is cut-off voltage in p.u. of base kV; load is 0 below this cut-off
         No defaults; all coefficients must be specified if using model=8.

        DSS property name: `ZIPV`, DSS property index: 33.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 33)
            for x in self._unpack()
        ]

    def _set_ZIPV(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(33, value, flags)

    ZIPV = property(_get_ZIPV, _set_ZIPV) # type: List[Float64Array]

    def _get_pctSeriesRL(self) -> BatchFloat64ArrayProxy:
        """
        Percent of load that is series R-L for Harmonic studies. Default is 50. Remainder is assumed to be parallel R and L. This can have a significant impact on the amount of damping observed in Harmonics solutions.

        DSS property name: `%SeriesRL`, DSS property index: 34.
        """
        return BatchFloat64ArrayProxy(self, 34)

    def _set_pctSeriesRL(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(34, value, flags)

    pctSeriesRL = property(_get_pctSeriesRL, _set_pctSeriesRL) # type: BatchFloat64ArrayProxy

    def _get_RelWeight(self) -> BatchFloat64ArrayProxy:
        """
        Relative weighting factor for reliability calcs. Default = 1. Used to designate high priority loads such as hospitals, etc. 

        Is multiplied by number of customers and load kW during reliability calcs.

        DSS property name: `RelWeight`, DSS property index: 35.
        """
        return BatchFloat64ArrayProxy(self, 35)

    def _set_RelWeight(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(35, value, flags)

    RelWeight = property(_get_RelWeight, _set_RelWeight) # type: BatchFloat64ArrayProxy

    def _get_VLowpu(self) -> BatchFloat64ArrayProxy:
        """
        Default = 0.50.  Per unit voltage at which the model switches to same as constant Z model (model=2). This allows more consistent convergence at very low voltaes due to opening switches or solving for fault situations.

        DSS property name: `VLowpu`, DSS property index: 36.
        """
        return BatchFloat64ArrayProxy(self, 36)

    def _set_VLowpu(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(36, value, flags)

    VLowpu = property(_get_VLowpu, _set_VLowpu) # type: BatchFloat64ArrayProxy

    def _get_puXHarm(self) -> BatchFloat64ArrayProxy:
        """
        Special reactance, pu (based on kVA, kV properties), for the series impedance branch in the load model for HARMONICS analysis. Generally used to represent motor load blocked rotor reactance. If not specified (that is, set =0, the default value), the series branch is computed from the percentage of the nominal load at fundamental frequency specified by the %SERIESRL property. 

        Applies to load model in HARMONICS mode only.

        A typical value would be approximately 0.20 pu based on kVA * %SeriesRL / 100.0.

        DSS property name: `puXHarm`, DSS property index: 37.
        """
        return BatchFloat64ArrayProxy(self, 37)

    def _set_puXHarm(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(37, value, flags)

    puXHarm = property(_get_puXHarm, _set_puXHarm) # type: BatchFloat64ArrayProxy

    def _get_XRHarm(self) -> BatchFloat64ArrayProxy:
        """
        X/R ratio of the special harmonics mode reactance specified by the puXHARM property at fundamental frequency. Default is 6. 

        DSS property name: `XRHarm`, DSS property index: 38.
        """
        return BatchFloat64ArrayProxy(self, 38)

    def _set_XRHarm(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(38, value, flags)

    XRHarm = property(_get_XRHarm, _set_XRHarm) # type: BatchFloat64ArrayProxy

    def _get_Spectrum_str(self) -> List[str]:
        """
        Name of harmonic current spectrum for this load.  Default is "defaultload", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 39.
        """
        return self._get_batch_str_prop(39)

    def _set_Spectrum_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(39, value, flags)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str) # type: List[str]

    def _get_Spectrum(self) -> List[SpectrumObj]:
        """
        Name of harmonic current spectrum for this load.  Default is "defaultload", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 39.
        """
        return self._get_batch_obj_prop(39)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(39, value, flags)

    Spectrum = property(_get_Spectrum, _set_Spectrum) # type: List[SpectrumObj]

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 40.
        """
        return BatchFloat64ArrayProxy(self, 40)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(40, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy

    def _get_Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 41.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(41)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(41, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 42.
        """
        self._set_batch_string(42, value, flags)

class LoadBatchProperties(TypedDict):
    Phases: Union[int, Int32Array]
    Bus1: Union[AnyStr, List[AnyStr]]
    kV: Union[float, Float64Array]
    kW: Union[float, Float64Array]
    PF: Union[float, Float64Array]
    Model: Union[int, enums.LoadModel, Int32Array]
    Yearly: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    Daily: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    Duty: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    Growth: Union[AnyStr, GrowthShape, List[AnyStr], List[GrowthShape]]
    Conn: Union[AnyStr, int, enums.Connection, List[AnyStr], List[int], List[enums.Connection], Int32Array]
    kvar: Union[float, Float64Array]
    RNeut: Union[float, Float64Array]
    XNeut: Union[float, Float64Array]
    Status: Union[AnyStr, int, enums.LoadStatus, List[AnyStr], List[int], List[enums.LoadStatus], Int32Array]
    Class: Union[int, Int32Array]
    VMinpu: Union[float, Float64Array]
    VMaxpu: Union[float, Float64Array]
    VMinNorm: Union[float, Float64Array]
    VMinEmerg: Union[float, Float64Array]
    XfkVA: Union[float, Float64Array]
    AllocationFactor: Union[float, Float64Array]
    kVA: Union[float, Float64Array]
    pctMean: Union[float, Float64Array]
    pctStdDev: Union[float, Float64Array]
    CVRWatts: Union[float, Float64Array]
    CVRVars: Union[float, Float64Array]
    kWh: Union[float, Float64Array]
    kWhDays: Union[float, Float64Array]
    CFactor: Union[float, Float64Array]
    CVRCurve: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    NumCust: Union[int, Int32Array]
    ZIPV: Float64Array
    pctSeriesRL: Union[float, Float64Array]
    RelWeight: Union[float, Float64Array]
    VLowpu: Union[float, Float64Array]
    puXHarm: Union[float, Float64Array]
    XRHarm: Union[float, Float64Array]
    Spectrum: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class ILoad(IDSSObj, LoadBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, Load, LoadBatch)
        LoadBatch.__init__(self, self._api_util, sync_cls_idx=Load._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Load:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[LoadProperties]) -> Load:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[LoadBatchProperties]) -> LoadBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
