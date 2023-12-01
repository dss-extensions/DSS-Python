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
from .XYcurve import XYcurve

class Storage(DSSObj, CircuitElementMixin, PCElementMixin, ElementHasRegistersMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots + PCElementMixin._extra_slots + ElementHasRegistersMixin._extra_slots
    _cls_name = 'Storage'
    _cls_idx = 29
    _cls_prop_idx = {
        'phases': 1,
        'bus1': 2,
        'kv': 3,
        'conn': 4,
        'kw': 5,
        'kvar': 6,
        'pf': 7,
        'kva': 8,
        'pctcutin': 9,
        '%cutin': 9,
        'pctcutout': 10,
        '%cutout': 10,
        'effcurve': 11,
        'varfollowinverter': 12,
        'kvarmax': 13,
        'kvarmaxabs': 14,
        'wattpriority': 15,
        'pfpriority': 16,
        'pctpminnovars': 17,
        '%pminnovars': 17,
        'pctpminkvarmax': 18,
        '%pminkvarmax': 18,
        'kwrated': 19,
        'pctkwrated': 20,
        '%kwrated': 20,
        'kwhrated': 21,
        'kwhstored': 22,
        'pctstored': 23,
        '%stored': 23,
        'pctreserve': 24,
        '%reserve': 24,
        'state': 25,
        'pctdischarge': 26,
        '%discharge': 26,
        'pctcharge': 27,
        '%charge': 27,
        'pcteffcharge': 28,
        '%effcharge': 28,
        'pcteffdischarge': 29,
        '%effdischarge': 29,
        'pctidlingkw': 30,
        '%idlingkw': 30,
        'pctidlingkvar': 31,
        '%idlingkvar': 31,
        'pctr': 32,
        '%r': 32,
        'pctx': 33,
        '%x': 33,
        'model': 34,
        'vminpu': 35,
        'vmaxpu': 36,
        'balanced': 37,
        'limitcurrent': 38,
        'yearly': 39,
        'daily': 40,
        'duty': 41,
        'dispmode': 42,
        'dischargetrigger': 43,
        'chargetrigger': 44,
        'timechargetrig': 45,
        'cls': 46,
        'class': 46,
        'dynadll': 47,
        'dynadata': 48,
        'usermodel': 49,
        'userdata': 50,
        'debugtrace': 51,
        'kvdc': 52,
        'kp': 53,
        'pitol': 54,
        'safevoltage': 55,
        'safemode': 56,
        'dynamiceq': 57,
        'dynout': 58,
        'controlmode': 59,
        'amplimit': 60,
        'amplimitgain': 61,
        'spectrum': 62,
        'basefreq': 63,
        'enabled': 64,
        'like': 65,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)
       PCElementMixin.__init__(self)
       ElementHasRegistersMixin.__init__(self)

    def _get_Phases(self) -> int:
        """
        Number of Phases, this Storage element.  Power is evenly divided among phases.

        DSS property name: `Phases`, DSS property index: 1.
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    def _set_Phases(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 1, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: int

    def _get_Bus1(self) -> str:
        """
        Bus to which the Storage element is connected.  May include specific node specification.

        DSS property name: `Bus1`, DSS property index: 2.
        """
        return self._get_prop_string(2)

    def _set_Bus1(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(2, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: str

    def _get_kV(self) -> float:
        """
        Nominal rated (1.0 per unit) voltage, kV, for Storage element. For 2- and 3-phase Storage elements, specify phase-phase kV. Otherwise, specify actual kV across each branch of the Storage element. 

        If wye (star), specify phase-neutral kV. 

        If delta or phase-phase connected, specify phase-phase kV.

        DSS property name: `kV`, DSS property index: 3.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    def _set_kV(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 3, value, flags)

    kV = property(_get_kV, _set_kV) # type: float

    def _get_Conn(self) -> enums.Connection:
        """
        ={wye|LN|delta|LL}.  Default is wye.

        DSS property name: `Conn`, DSS property index: 4.
        """
        return enums.Connection(self._lib.Obj_GetInt32(self._ptr, 4))

    def _set_Conn(self, value: Union[AnyStr, int, enums.Connection], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(4, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 4, value, flags)

    Conn = property(_get_Conn, _set_Conn) # type: enums.Connection

    def _get_Conn_str(self) -> str:
        """
        ={wye|LN|delta|LL}.  Default is wye.

        DSS property name: `Conn`, DSS property index: 4.
        """
        return self._get_prop_string(4)

    def _set_Conn_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Conn(value, flags)

    Conn_str = property(_get_Conn_str, _set_Conn_str) # type: str

    def _get_kW(self) -> float:
        """
        Get/set the requested kW value. Final kW is subjected to the inverter ratings. A positive value denotes power coming OUT of the element, which is the opposite of a Load element. A negative value indicates the Storage element is in Charging state. This value is modified internally depending on the dispatch mode.

        DSS property name: `kW`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    def _set_kW(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 5, value, flags)

    kW = property(_get_kW, _set_kW) # type: float

    def _get_kvar(self) -> float:
        """
        Get/set the requested kvar value. Final kvar is subjected to the inverter ratings. Sets inverter to operate in constant kvar mode.

        DSS property name: `kvar`, DSS property index: 6.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    def _set_kvar(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 6, value, flags)

    kvar = property(_get_kvar, _set_kvar) # type: float

    def _get_PF(self) -> float:
        """
        Get/set the requested PF value. Final PF is subjected to the inverter ratings. Sets inverter to operate in constant PF mode. Nominally, the power factor for discharging (acting as a generator). Default is 1.0. 

        Enter negative for leading power factor (when kW and kvar have opposite signs.)

        A positive power factor signifies kw and kvar at the same direction.

        DSS property name: `PF`, DSS property index: 7.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    def _set_PF(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 7, value, flags)

    PF = property(_get_PF, _set_PF) # type: float

    def _get_kVA(self) -> float:
        """
        Indicates the inverter nameplate capability (in kVA). Used as the base for Dynamics mode and Harmonics mode values.

        DSS property name: `kVA`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    def _set_kVA(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 8, value, flags)

    kVA = property(_get_kVA, _set_kVA) # type: float

    def _get_pctCutIn(self) -> float:
        """
        Cut-in power as a percentage of inverter kVA rating. It is the minimum DC power necessary to turn the inverter ON when it is OFF. Must be greater than or equal to %CutOut. Defaults to 2 for PVSystems and 0 for Storage elements which means that the inverter state will be always ON for this element.

        DSS property name: `%CutIn`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    def _set_pctCutIn(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 9, value, flags)

    pctCutIn = property(_get_pctCutIn, _set_pctCutIn) # type: float

    def _get_pctCutOut(self) -> float:
        """
        Cut-out power as a percentage of inverter kVA rating. It is the minimum DC power necessary to keep the inverter ON. Must be less than or equal to %CutIn. Defaults to 0, which means that, once ON, the inverter state will be always ON for this element.

        DSS property name: `%CutOut`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    def _set_pctCutOut(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 10, value, flags)

    pctCutOut = property(_get_pctCutOut, _set_pctCutOut) # type: float

    def _get_EffCurve_str(self) -> str:
        """
        An XYCurve object, previously defined, that describes the PER UNIT efficiency vs PER UNIT of rated kVA for the inverter. Power at the AC side of the inverter is discounted by the multiplier obtained from this curve.

        DSS property name: `EffCurve`, DSS property index: 11.
        """
        return self._get_prop_string(11)

    def _set_EffCurve_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(11, value, flags)

    EffCurve_str = property(_get_EffCurve_str, _set_EffCurve_str) # type: str

    def _get_EffCurve(self) -> XYcurve:
        """
        An XYCurve object, previously defined, that describes the PER UNIT efficiency vs PER UNIT of rated kVA for the inverter. Power at the AC side of the inverter is discounted by the multiplier obtained from this curve.

        DSS property name: `EffCurve`, DSS property index: 11.
        """
        return self._get_obj(11, XYcurve)

    def _set_EffCurve(self, value: Union[AnyStr, XYcurve], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(11, value, flags)
            return

        self._set_string_o(11, value, flags)

    EffCurve = property(_get_EffCurve, _set_EffCurve) # type: XYcurve

    def _get_VarFollowInverter(self) -> bool:
        """
        Boolean variable (Yes|No) or (True|False). Defaults to False, which indicates that the reactive power generation/absorption does not respect the inverter status.When set to True, the reactive power generation/absorption will cease when the inverter status is off, due to DC kW dropping below %CutOut.  The reactive power generation/absorption will begin again when the DC kW is above %CutIn.  When set to False, the Storage will generate/absorb reactive power regardless of the status of the inverter.

        DSS property name: `VarFollowInverter`, DSS property index: 12.
        """
        return self._lib.Obj_GetInt32(self._ptr, 12) != 0

    def _set_VarFollowInverter(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 12, value, flags)

    VarFollowInverter = property(_get_VarFollowInverter, _set_VarFollowInverter) # type: bool

    def _get_kvarMax(self) -> float:
        """
        Indicates the maximum reactive power GENERATION (un-signed numerical variable in kvar) for the inverter. Defaults to kVA rating of the inverter.

        DSS property name: `kvarMax`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    def _set_kvarMax(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 13, value, flags)

    kvarMax = property(_get_kvarMax, _set_kvarMax) # type: float

    def _get_kvarMaxAbs(self) -> float:
        """
        Indicates the maximum reactive power ABSORPTION (un-signed numerical variable in kvar) for the inverter. Defaults to kvarMax.

        DSS property name: `kvarMaxAbs`, DSS property index: 14.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    def _set_kvarMaxAbs(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 14, value, flags)

    kvarMaxAbs = property(_get_kvarMaxAbs, _set_kvarMaxAbs) # type: float

    def _get_WattPriority(self) -> bool:
        """
        {Yes/No*/True/False} Set inverter to watt priority instead of the default var priority.

        DSS property name: `WattPriority`, DSS property index: 15.
        """
        return self._lib.Obj_GetInt32(self._ptr, 15) != 0

    def _set_WattPriority(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 15, value, flags)

    WattPriority = property(_get_WattPriority, _set_WattPriority) # type: bool

    def _get_PFPriority(self) -> bool:
        """
        If set to true, priority is given to power factor and WattPriority is neglected. It works only if operating in either constant PF or constant kvar modes. Defaults to False.

        DSS property name: `PFPriority`, DSS property index: 16.
        """
        return self._lib.Obj_GetInt32(self._ptr, 16) != 0

    def _set_PFPriority(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 16, value, flags)

    PFPriority = property(_get_PFPriority, _set_PFPriority) # type: bool

    def _get_pctPMinNoVars(self) -> float:
        """
        Minimum active power as percentage of kWrated under which there is no vars production/absorption. Defaults to 0 (disabled).

        DSS property name: `%PMinNoVars`, DSS property index: 17.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    def _set_pctPMinNoVars(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 17, value, flags)

    pctPMinNoVars = property(_get_pctPMinNoVars, _set_pctPMinNoVars) # type: float

    def _get_pctPMinkvarMax(self) -> float:
        """
        Minimum active power as percentage of kWrated that allows the inverter to produce/absorb reactive power up to its maximum reactive power, which can be either kvarMax or kvarMaxAbs, depending on the current operation quadrant. Defaults to 0 (disabled).

        DSS property name: `%PMinkvarMax`, DSS property index: 18.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    def _set_pctPMinkvarMax(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 18, value, flags)

    pctPMinkvarMax = property(_get_pctPMinkvarMax, _set_pctPMinkvarMax) # type: float

    def _get_kWRated(self) -> float:
        """
        kW rating of power output. Base for Loadshapes when DispMode=Follow. Sets kVA property if it has not been specified yet. Defaults to 25.

        DSS property name: `kWRated`, DSS property index: 19.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    def _set_kWRated(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 19, value, flags)

    kWRated = property(_get_kWRated, _set_kWRated) # type: float

    def _get_pctkWRated(self) -> float:
        """
        Upper limit on active power as a percentage of kWrated. Defaults to 100 (disabled).

        DSS property name: `%kWRated`, DSS property index: 20.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    def _set_pctkWRated(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 20, value, flags)

    pctkWRated = property(_get_pctkWRated, _set_pctkWRated) # type: float

    def _get_kWhRated(self) -> float:
        """
        Rated Storage capacity in kWh. Default is 50.

        DSS property name: `kWhRated`, DSS property index: 21.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    def _set_kWhRated(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 21, value, flags)

    kWhRated = property(_get_kWhRated, _set_kWhRated) # type: float

    def _get_kWhStored(self) -> float:
        """
        Present amount of energy stored, kWh. Default is same as kWhrated.

        DSS property name: `kWhStored`, DSS property index: 22.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    def _set_kWhStored(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 22, value, flags)

    kWhStored = property(_get_kWhStored, _set_kWhStored) # type: float

    def _get_pctStored(self) -> float:
        """
        Present amount of energy stored, % of rated kWh. Default is 100.

        DSS property name: `%Stored`, DSS property index: 23.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    def _set_pctStored(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 23, value, flags)

    pctStored = property(_get_pctStored, _set_pctStored) # type: float

    def _get_pctReserve(self) -> float:
        """
        Percentage of rated kWh Storage capacity to be held in reserve for normal operation. Default = 20. 
        This is treated as the minimum energy discharge level unless there is an emergency. For emergency operation set this property lower. Cannot be less than zero.

        DSS property name: `%Reserve`, DSS property index: 24.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    def _set_pctReserve(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 24, value, flags)

    pctReserve = property(_get_pctReserve, _set_pctReserve) # type: float

    def _get_State(self) -> enums.StorageState:
        """
        {IDLING | CHARGING | DISCHARGING}  Get/Set present operational state. In DISCHARGING mode, the Storage element acts as a generator and the kW property is positive. The element continues discharging at the scheduled output power level until the Storage reaches the reserve value. Then the state reverts to IDLING. In the CHARGING state, the Storage element behaves like a Load and the kW property is negative. The element continues to charge until the max Storage kWh is reached and then switches to IDLING state. In IDLING state, the element draws the idling losses plus the associated inverter losses.

        DSS property name: `State`, DSS property index: 25.
        """
        return enums.StorageState(self._lib.Obj_GetInt32(self._ptr, 25))

    def _set_State(self, value: Union[AnyStr, int, enums.StorageState], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(25, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 25, value, flags)

    State = property(_get_State, _set_State) # type: enums.StorageState

    def _get_State_str(self) -> str:
        """
        {IDLING | CHARGING | DISCHARGING}  Get/Set present operational state. In DISCHARGING mode, the Storage element acts as a generator and the kW property is positive. The element continues discharging at the scheduled output power level until the Storage reaches the reserve value. Then the state reverts to IDLING. In the CHARGING state, the Storage element behaves like a Load and the kW property is negative. The element continues to charge until the max Storage kWh is reached and then switches to IDLING state. In IDLING state, the element draws the idling losses plus the associated inverter losses.

        DSS property name: `State`, DSS property index: 25.
        """
        return self._get_prop_string(25)

    def _set_State_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_State(value, flags)

    State_str = property(_get_State_str, _set_State_str) # type: str

    def _get_pctDischarge(self) -> float:
        """
        Discharge rate (output power) in percentage of rated kW. Default = 100.

        DSS property name: `%Discharge`, DSS property index: 26.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 26)

    def _set_pctDischarge(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 26, value, flags)

    pctDischarge = property(_get_pctDischarge, _set_pctDischarge) # type: float

    def _get_pctCharge(self) -> float:
        """
        Charging rate (input power) in percentage of rated kW. Default = 100.

        DSS property name: `%Charge`, DSS property index: 27.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 27)

    def _set_pctCharge(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 27, value, flags)

    pctCharge = property(_get_pctCharge, _set_pctCharge) # type: float

    def _get_pctEffCharge(self) -> float:
        """
        Percentage efficiency for CHARGING the Storage element. Default = 90.

        DSS property name: `%EffCharge`, DSS property index: 28.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 28)

    def _set_pctEffCharge(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 28, value, flags)

    pctEffCharge = property(_get_pctEffCharge, _set_pctEffCharge) # type: float

    def _get_pctEffDischarge(self) -> float:
        """
        Percentage efficiency for DISCHARGING the Storage element. Default = 90.

        DSS property name: `%EffDischarge`, DSS property index: 29.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 29)

    def _set_pctEffDischarge(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 29, value, flags)

    pctEffDischarge = property(_get_pctEffDischarge, _set_pctEffDischarge) # type: float

    def _get_pctIdlingkW(self) -> float:
        """
        Percentage of rated kW consumed by idling losses. Default = 1.

        DSS property name: `%IdlingkW`, DSS property index: 30.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 30)

    def _set_pctIdlingkW(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 30, value, flags)

    pctIdlingkW = property(_get_pctIdlingkW, _set_pctIdlingkW) # type: float

    def _get_pctR(self) -> float:
        """
        Equivalent percentage internal resistance, ohms. Default is 0. Placed in series with internal voltage source for harmonics and dynamics modes. Use a combination of %IdlingkW, %EffCharge and %EffDischarge to account for losses in power flow modes.

        DSS property name: `%R`, DSS property index: 32.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 32)

    def _set_pctR(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 32, value, flags)

    pctR = property(_get_pctR, _set_pctR) # type: float

    def _get_pctX(self) -> float:
        """
        Equivalent percentage internal reactance, ohms. Default is 50%. Placed in series with internal voltage source for harmonics and dynamics modes. (Limits fault current to 2 pu.

        DSS property name: `%X`, DSS property index: 33.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 33)

    def _set_pctX(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 33, value, flags)

    pctX = property(_get_pctX, _set_pctX) # type: float

    def _get_Model(self) -> int:
        """
        Integer code (default=1) for the model to be used for power output variation with voltage. Valid values are:

        1:Storage element injects/absorbs a CONSTANT power.
        2:Storage element is modeled as a CONSTANT IMPEDANCE.
        3:Compute load injection from User-written Model.

        DSS property name: `Model`, DSS property index: 34.
        """
        return self._lib.Obj_GetInt32(self._ptr, 34)

    def _set_Model(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 34, value, flags)

    Model = property(_get_Model, _set_Model) # type: int

    def _get_VMinpu(self) -> float:
        """
        Default = 0.90.  Minimum per unit voltage for which the Model is assumed to apply. Below this value, the load model reverts to a constant impedance model.

        DSS property name: `VMinpu`, DSS property index: 35.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 35)

    def _set_VMinpu(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 35, value, flags)

    VMinpu = property(_get_VMinpu, _set_VMinpu) # type: float

    def _get_VMaxpu(self) -> float:
        """
        Default = 1.10.  Maximum per unit voltage for which the Model is assumed to apply. Above this value, the load model reverts to a constant impedance model.

        DSS property name: `VMaxpu`, DSS property index: 36.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 36)

    def _set_VMaxpu(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 36, value, flags)

    VMaxpu = property(_get_VMaxpu, _set_VMaxpu) # type: float

    def _get_Balanced(self) -> bool:
        """
        {Yes | No*} Default is No. Force balanced current only for 3-phase Storage. Forces zero- and negative-sequence to zero. 

        DSS property name: `Balanced`, DSS property index: 37.
        """
        return self._lib.Obj_GetInt32(self._ptr, 37) != 0

    def _set_Balanced(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 37, value, flags)

    Balanced = property(_get_Balanced, _set_Balanced) # type: bool

    def _get_LimitCurrent(self) -> bool:
        """
        Limits current magnitude to Vminpu value for both 1-phase and 3-phase Storage similar to Generator Model 7. For 3-phase, limits the positive-sequence current but not the negative-sequence.

        DSS property name: `LimitCurrent`, DSS property index: 38.
        """
        return self._lib.Obj_GetInt32(self._ptr, 38) != 0

    def _set_LimitCurrent(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 38, value, flags)

    LimitCurrent = property(_get_LimitCurrent, _set_LimitCurrent) # type: bool

    def _get_Yearly_str(self) -> str:
        """
        Dispatch shape to use for yearly simulations.  Must be previously defined as a Loadshape object. If this is not specified, the Daily dispatch shape, if any, is repeated during Yearly solution modes. In the default dispatch mode, the Storage element uses this loadshape to trigger State changes.

        DSS property name: `Yearly`, DSS property index: 39.
        """
        return self._get_prop_string(39)

    def _set_Yearly_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(39, value, flags)

    Yearly_str = property(_get_Yearly_str, _set_Yearly_str) # type: str

    def _get_Yearly(self) -> LoadShape:
        """
        Dispatch shape to use for yearly simulations.  Must be previously defined as a Loadshape object. If this is not specified, the Daily dispatch shape, if any, is repeated during Yearly solution modes. In the default dispatch mode, the Storage element uses this loadshape to trigger State changes.

        DSS property name: `Yearly`, DSS property index: 39.
        """
        return self._get_obj(39, LoadShape)

    def _set_Yearly(self, value: Union[AnyStr, LoadShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(39, value, flags)
            return

        self._set_string_o(39, value, flags)

    Yearly = property(_get_Yearly, _set_Yearly) # type: LoadShape

    def _get_Daily_str(self) -> str:
        """
        Dispatch shape to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically.  In the default dispatch mode, the Storage element uses this loadshape to trigger State changes.

        DSS property name: `Daily`, DSS property index: 40.
        """
        return self._get_prop_string(40)

    def _set_Daily_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(40, value, flags)

    Daily_str = property(_get_Daily_str, _set_Daily_str) # type: str

    def _get_Daily(self) -> LoadShape:
        """
        Dispatch shape to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically.  In the default dispatch mode, the Storage element uses this loadshape to trigger State changes.

        DSS property name: `Daily`, DSS property index: 40.
        """
        return self._get_obj(40, LoadShape)

    def _set_Daily(self, value: Union[AnyStr, LoadShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(40, value, flags)
            return

        self._set_string_o(40, value, flags)

    Daily = property(_get_Daily, _set_Daily) # type: LoadShape

    def _get_Duty_str(self) -> str:
        """
        Load shape to use for duty cycle dispatch simulations such as for solar ramp rate studies. Must be previously defined as a Loadshape object. 

        Typically would have time intervals of 1-5 seconds. 

        Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.

        DSS property name: `Duty`, DSS property index: 41.
        """
        return self._get_prop_string(41)

    def _set_Duty_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(41, value, flags)

    Duty_str = property(_get_Duty_str, _set_Duty_str) # type: str

    def _get_Duty(self) -> LoadShape:
        """
        Load shape to use for duty cycle dispatch simulations such as for solar ramp rate studies. Must be previously defined as a Loadshape object. 

        Typically would have time intervals of 1-5 seconds. 

        Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.

        DSS property name: `Duty`, DSS property index: 41.
        """
        return self._get_obj(41, LoadShape)

    def _set_Duty(self, value: Union[AnyStr, LoadShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(41, value, flags)
            return

        self._set_string_o(41, value, flags)

    Duty = property(_get_Duty, _set_Duty) # type: LoadShape

    def _get_DispMode(self) -> enums.StorageDispatchMode:
        """
        {DEFAULT | FOLLOW | EXTERNAL | LOADLEVEL | PRICE } Default = "DEFAULT". Dispatch mode. 

        In DEFAULT mode, Storage element state is triggered to discharge or charge at the specified rate by the loadshape curve corresponding to the solution mode. 

        In FOLLOW mode the kW output of the Storage element follows the active loadshape multiplier until Storage is either exhausted or full. The element discharges for positive values and charges for negative values.  The loadshape is based on rated kW. 

        In EXTERNAL mode, Storage element state is controlled by an external Storagecontroller. This mode is automatically set if this Storage element is included in the element list of a StorageController element. 

        For the other two dispatch modes, the Storage element state is controlled by either the global default Loadlevel value or the price level. 

        DSS property name: `DispMode`, DSS property index: 42.
        """
        return enums.StorageDispatchMode(self._lib.Obj_GetInt32(self._ptr, 42))

    def _set_DispMode(self, value: Union[AnyStr, int, enums.StorageDispatchMode], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(42, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 42, value, flags)

    DispMode = property(_get_DispMode, _set_DispMode) # type: enums.StorageDispatchMode

    def _get_DispMode_str(self) -> str:
        """
        {DEFAULT | FOLLOW | EXTERNAL | LOADLEVEL | PRICE } Default = "DEFAULT". Dispatch mode. 

        In DEFAULT mode, Storage element state is triggered to discharge or charge at the specified rate by the loadshape curve corresponding to the solution mode. 

        In FOLLOW mode the kW output of the Storage element follows the active loadshape multiplier until Storage is either exhausted or full. The element discharges for positive values and charges for negative values.  The loadshape is based on rated kW. 

        In EXTERNAL mode, Storage element state is controlled by an external Storagecontroller. This mode is automatically set if this Storage element is included in the element list of a StorageController element. 

        For the other two dispatch modes, the Storage element state is controlled by either the global default Loadlevel value or the price level. 

        DSS property name: `DispMode`, DSS property index: 42.
        """
        return self._get_prop_string(42)

    def _set_DispMode_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_DispMode(value, flags)

    DispMode_str = property(_get_DispMode_str, _set_DispMode_str) # type: str

    def _get_DischargeTrigger(self) -> float:
        """
        Dispatch trigger value for discharging the Storage. 
        If = 0.0 the Storage element state is changed by the State command or by a StorageController object. 
        If <> 0  the Storage element state is set to DISCHARGING when this trigger level is EXCEEDED by either the specified Loadshape curve value or the price signal or global Loadlevel value, depending on dispatch mode. See State property.

        DSS property name: `DischargeTrigger`, DSS property index: 43.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 43)

    def _set_DischargeTrigger(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 43, value, flags)

    DischargeTrigger = property(_get_DischargeTrigger, _set_DischargeTrigger) # type: float

    def _get_ChargeTrigger(self) -> float:
        """
        Dispatch trigger value for charging the Storage. 

        If = 0.0 the Storage element state is changed by the State command or StorageController object.  

        If <> 0  the Storage element state is set to CHARGING when this trigger level is GREATER than either the specified Loadshape curve value or the price signal or global Loadlevel value, depending on dispatch mode. See State property.

        DSS property name: `ChargeTrigger`, DSS property index: 44.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 44)

    def _set_ChargeTrigger(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 44, value, flags)

    ChargeTrigger = property(_get_ChargeTrigger, _set_ChargeTrigger) # type: float

    def _get_TimeChargeTrig(self) -> float:
        """
        Time of day in fractional hours (0230 = 2.5) at which Storage element will automatically go into charge state. Default is 2.0.  Enter a negative time value to disable this feature.

        DSS property name: `TimeChargeTrig`, DSS property index: 45.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 45)

    def _set_TimeChargeTrig(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 45, value, flags)

    TimeChargeTrig = property(_get_TimeChargeTrig, _set_TimeChargeTrig) # type: float

    def _get_Class(self) -> int:
        """
        An arbitrary integer number representing the class of Storage element so that Storage values may be segregated by class.

        DSS property name: `Class`, DSS property index: 46.
        """
        return self._lib.Obj_GetInt32(self._ptr, 46)

    def _set_Class(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 46, value, flags)

    Class = property(_get_Class, _set_Class) # type: int

    def _get_DynaDLL(self) -> str:
        """
        Name of DLL containing user-written dynamics model, which computes the terminal currents for Dynamics-mode simulations, overriding the default model.  Set to "none" to negate previous setting. This DLL has a simpler interface than the UserModel DLL and is only used for Dynamics mode.

        DSS property name: `DynaDLL`, DSS property index: 47.
        """
        return self._get_prop_string(47)

    def _set_DynaDLL(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(47, value, flags)

    DynaDLL = property(_get_DynaDLL, _set_DynaDLL) # type: str

    def _get_DynaData(self) -> str:
        """
        String (in quotes or parentheses if necessary) that gets passed to the user-written dynamics model Edit function for defining the data required for that model.

        DSS property name: `DynaData`, DSS property index: 48.
        """
        return self._get_prop_string(48)

    def _set_DynaData(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(48, value, flags)

    DynaData = property(_get_DynaData, _set_DynaData) # type: str

    def _get_UserModel(self) -> str:
        """
        Name of DLL containing user-written model, which computes the terminal currents for both power flow and dynamics, overriding the default model.  Set to "none" to negate previous setting.

        DSS property name: `UserModel`, DSS property index: 49.
        """
        return self._get_prop_string(49)

    def _set_UserModel(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(49, value, flags)

    UserModel = property(_get_UserModel, _set_UserModel) # type: str

    def _get_UserData(self) -> str:
        """
        String (in quotes or parentheses) that gets passed to user-written model for defining the data required for that model.

        DSS property name: `UserData`, DSS property index: 50.
        """
        return self._get_prop_string(50)

    def _set_UserData(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(50, value, flags)

    UserData = property(_get_UserData, _set_UserData) # type: str

    def _get_DebugTrace(self) -> bool:
        """
        {Yes | No }  Default is no.  Turn this on to capture the progress of the Storage model for each iteration.  Creates a separate file for each Storage element named "Storage_name.csv".

        DSS property name: `DebugTrace`, DSS property index: 51.
        """
        return self._lib.Obj_GetInt32(self._ptr, 51) != 0

    def _set_DebugTrace(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 51, value, flags)

    DebugTrace = property(_get_DebugTrace, _set_DebugTrace) # type: bool

    def _get_kVDC(self) -> float:
        """
        Indicates the rated voltage (kV) at the input of the inverter while the storage is discharging. The value is normally greater or equal to the kV base of the Storage device. It is used for dynamics simulation ONLY.

        DSS property name: `kVDC`, DSS property index: 52.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 52)

    def _set_kVDC(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 52, value, flags)

    kVDC = property(_get_kVDC, _set_kVDC) # type: float

    def _get_Kp(self) -> float:
        """
        It is the proportional gain for the PI controller within the inverter. Use it to modify the controller response in dynamics simulation mode.

        DSS property name: `Kp`, DSS property index: 53.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 53)

    def _set_Kp(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 53, value, flags)

    Kp = property(_get_Kp, _set_Kp) # type: float

    def _get_PITol(self) -> float:
        """
        It is the tolerance (%) for the closed loop controller of the inverter. For dynamics simulation mode.

        DSS property name: `PITol`, DSS property index: 54.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 54)

    def _set_PITol(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 54, value, flags)

    PITol = property(_get_PITol, _set_PITol) # type: float

    def _get_SafeVoltage(self) -> float:
        """
        Indicates the voltage level (%) respect to the base voltage level for which the Inverter will operate. If this threshold is violated, the Inverter will enter safe mode (OFF). For dynamic simulation. By default is 80%.

        DSS property name: `SafeVoltage`, DSS property index: 55.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 55)

    def _set_SafeVoltage(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 55, value, flags)

    SafeVoltage = property(_get_SafeVoltage, _set_SafeVoltage) # type: float

    def _get_SafeMode(self) -> bool:
        """
        (Read only) Indicates whether the inverter entered (Yes) or not (No) into Safe Mode.

        DSS property name: `SafeMode`, DSS property index: 56.
        """
        return self._lib.Obj_GetInt32(self._ptr, 56) != 0

    def _set_SafeMode(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 56, value, flags)

    SafeMode = property(_get_SafeMode, _set_SafeMode) # type: bool

    def _get_DynamicEq_str(self) -> str:
        """
        The name of the dynamic equation (DynamicExp) that will be used for defining the dynamic behavior of the generator. If not defined, the generator dynamics will follow the built-in dynamic equation.

        DSS property name: `DynamicEq`, DSS property index: 57.
        """
        return self._get_prop_string(57)

    def _set_DynamicEq_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(57, value, flags)

    DynamicEq_str = property(_get_DynamicEq_str, _set_DynamicEq_str) # type: str

    def _get_DynamicEq(self) -> DynamicExp:
        """
        The name of the dynamic equation (DynamicExp) that will be used for defining the dynamic behavior of the generator. If not defined, the generator dynamics will follow the built-in dynamic equation.

        DSS property name: `DynamicEq`, DSS property index: 57.
        """
        return self._get_obj(57, DynamicExp)

    def _set_DynamicEq(self, value: Union[AnyStr, DynamicExp], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(57, value, flags)
            return

        self._set_string_o(57, value, flags)

    DynamicEq = property(_get_DynamicEq, _set_DynamicEq) # type: DynamicExp

    def _get_DynOut(self) -> str:
        """
        The name of the variables within the Dynamic equation that will be used to govern the Storage dynamics. This Storage model requires 1 output from the dynamic equation:

            1. Current.

        The output variables need to be defined in the same order.

        DSS property name: `DynOut`, DSS property index: 58.
        """
        return self._get_prop_string(58)

    def _set_DynOut(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(58, value, flags)

    DynOut = property(_get_DynOut, _set_DynOut) # type: str

    def _get_ControlMode(self) -> enums.InverterControlMode:
        """
        Defines the control mode for the inverter. It can be one of {GFM | GFL*}. By default it is GFL (Grid Following Inverter). Use GFM (Grid Forming Inverter) for energizing islanded microgrids, but, if the device is connected to the grid, it is highly recommended to use GFL.

        GFM control mode disables any control action set by the InvControl device.

        DSS property name: `ControlMode`, DSS property index: 59.
        """
        return enums.InverterControlMode(self._lib.Obj_GetInt32(self._ptr, 59))

    def _set_ControlMode(self, value: Union[AnyStr, int, enums.InverterControlMode], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(59, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 59, value, flags)

    ControlMode = property(_get_ControlMode, _set_ControlMode) # type: enums.InverterControlMode

    def _get_ControlMode_str(self) -> str:
        """
        Defines the control mode for the inverter. It can be one of {GFM | GFL*}. By default it is GFL (Grid Following Inverter). Use GFM (Grid Forming Inverter) for energizing islanded microgrids, but, if the device is connected to the grid, it is highly recommended to use GFL.

        GFM control mode disables any control action set by the InvControl device.

        DSS property name: `ControlMode`, DSS property index: 59.
        """
        return self._get_prop_string(59)

    def _set_ControlMode_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_ControlMode(value, flags)

    ControlMode_str = property(_get_ControlMode_str, _set_ControlMode_str) # type: str

    def _get_AmpLimit(self) -> float:
        """
        The current limiter per phase for the IBR when operating in GFM mode. This limit is imposed to prevent the IBR to enter into Safe Mode when reaching the IBR power ratings.
        Once the IBR reaches this value, it remains there without moving into Safe Mode. This value needs to be set lower than the IBR Amps rating.

        DSS property name: `AmpLimit`, DSS property index: 60.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 60)

    def _set_AmpLimit(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 60, value, flags)

    AmpLimit = property(_get_AmpLimit, _set_AmpLimit) # type: float

    def _get_AmpLimitGain(self) -> float:
        """
        Use it for fine tunning the current limiter when active, by default is 0.8, it has to be a value between 0.1 and 1. This value allows users to fine tune the IBRs current limiter to match with the user requirements.

        DSS property name: `AmpLimitGain`, DSS property index: 61.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 61)

    def _set_AmpLimitGain(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 61, value, flags)

    AmpLimitGain = property(_get_AmpLimitGain, _set_AmpLimitGain) # type: float

    def _get_Spectrum_str(self) -> str:
        """
        Name of harmonic voltage or current spectrum for this Storage element. Current injection is assumed for inverter. Default value is "default", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 62.
        """
        return self._get_prop_string(62)

    def _set_Spectrum_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(62, value, flags)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str) # type: str

    def _get_Spectrum(self) -> SpectrumObj:
        """
        Name of harmonic voltage or current spectrum for this Storage element. Current injection is assumed for inverter. Default value is "default", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 62.
        """
        return self._get_obj(62, SpectrumObj)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(62, value, flags)
            return

        self._set_string_o(62, value, flags)

    Spectrum = property(_get_Spectrum, _set_Spectrum) # type: SpectrumObj

    def _get_BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 63.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 63)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 63, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float

    def _get_Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 64.
        """
        return self._lib.Obj_GetInt32(self._ptr, 64) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 64, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 65.
        """
        self._set_string_o(65, value)


class StorageProperties(TypedDict):
    Phases: int
    Bus1: AnyStr
    kV: float
    Conn: Union[AnyStr, int, enums.Connection]
    kW: float
    kvar: float
    PF: float
    kVA: float
    pctCutIn: float
    pctCutOut: float
    EffCurve: Union[AnyStr, XYcurve]
    VarFollowInverter: bool
    kvarMax: float
    kvarMaxAbs: float
    WattPriority: bool
    PFPriority: bool
    pctPMinNoVars: float
    pctPMinkvarMax: float
    kWRated: float
    pctkWRated: float
    kWhRated: float
    kWhStored: float
    pctStored: float
    pctReserve: float
    State: Union[AnyStr, int, enums.StorageState]
    pctDischarge: float
    pctCharge: float
    pctEffCharge: float
    pctEffDischarge: float
    pctIdlingkW: float
    pctR: float
    pctX: float
    Model: int
    VMinpu: float
    VMaxpu: float
    Balanced: bool
    LimitCurrent: bool
    Yearly: Union[AnyStr, LoadShape]
    Daily: Union[AnyStr, LoadShape]
    Duty: Union[AnyStr, LoadShape]
    DispMode: Union[AnyStr, int, enums.StorageDispatchMode]
    DischargeTrigger: float
    ChargeTrigger: float
    TimeChargeTrig: float
    Class: int
    DynaDLL: AnyStr
    DynaData: AnyStr
    UserModel: AnyStr
    UserData: AnyStr
    DebugTrace: bool
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

class StorageBatch(DSSBatch, CircuitElementBatchMixin, PCElementBatchMixin):
    _cls_name = 'Storage'
    _obj_cls = Storage
    _cls_idx = 29

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)
       PCElementBatchMixin.__init__(self)

    def _get_Phases(self) -> BatchInt32ArrayProxy:
        """
        Number of Phases, this Storage element.  Power is evenly divided among phases.

        DSS property name: `Phases`, DSS property index: 1.
        """
        return BatchInt32ArrayProxy(self, 1)

    def _set_Phases(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(1, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: BatchInt32ArrayProxy

    def _get_Bus1(self) -> List[str]:
        """
        Bus to which the Storage element is connected.  May include specific node specification.

        DSS property name: `Bus1`, DSS property index: 2.
        """
        return self._get_batch_str_prop(2)

    def _set_Bus1(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(2, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: List[str]

    def _get_kV(self) -> BatchFloat64ArrayProxy:
        """
        Nominal rated (1.0 per unit) voltage, kV, for Storage element. For 2- and 3-phase Storage elements, specify phase-phase kV. Otherwise, specify actual kV across each branch of the Storage element. 

        If wye (star), specify phase-neutral kV. 

        If delta or phase-phase connected, specify phase-phase kV.

        DSS property name: `kV`, DSS property index: 3.
        """
        return BatchFloat64ArrayProxy(self, 3)

    def _set_kV(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(3, value, flags)

    kV = property(_get_kV, _set_kV) # type: BatchFloat64ArrayProxy

    def _get_Conn(self) -> BatchInt32ArrayProxy:
        """
        ={wye|LN|delta|LL}.  Default is wye.

        DSS property name: `Conn`, DSS property index: 4.
        """
        return BatchInt32ArrayProxy(self, 4)

    def _set_Conn(self, value: Union[AnyStr, int, enums.Connection, List[AnyStr], List[int], List[enums.Connection], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(4, value, flags)
            return

        self._set_batch_int32_array(4, value, flags)

    Conn = property(_get_Conn, _set_Conn) # type: BatchInt32ArrayProxy

    def _get_Conn_str(self) -> List[str]:
        """
        ={wye|LN|delta|LL}.  Default is wye.

        DSS property name: `Conn`, DSS property index: 4.
        """
        return self._get_batch_str_prop(4)

    def _set_Conn_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Conn(value, flags)

    Conn_str = property(_get_Conn_str, _set_Conn_str) # type: List[str]

    def _get_kW(self) -> BatchFloat64ArrayProxy:
        """
        Get/set the requested kW value. Final kW is subjected to the inverter ratings. A positive value denotes power coming OUT of the element, which is the opposite of a Load element. A negative value indicates the Storage element is in Charging state. This value is modified internally depending on the dispatch mode.

        DSS property name: `kW`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    def _set_kW(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(5, value, flags)

    kW = property(_get_kW, _set_kW) # type: BatchFloat64ArrayProxy

    def _get_kvar(self) -> BatchFloat64ArrayProxy:
        """
        Get/set the requested kvar value. Final kvar is subjected to the inverter ratings. Sets inverter to operate in constant kvar mode.

        DSS property name: `kvar`, DSS property index: 6.
        """
        return BatchFloat64ArrayProxy(self, 6)

    def _set_kvar(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(6, value, flags)

    kvar = property(_get_kvar, _set_kvar) # type: BatchFloat64ArrayProxy

    def _get_PF(self) -> BatchFloat64ArrayProxy:
        """
        Get/set the requested PF value. Final PF is subjected to the inverter ratings. Sets inverter to operate in constant PF mode. Nominally, the power factor for discharging (acting as a generator). Default is 1.0. 

        Enter negative for leading power factor (when kW and kvar have opposite signs.)

        A positive power factor signifies kw and kvar at the same direction.

        DSS property name: `PF`, DSS property index: 7.
        """
        return BatchFloat64ArrayProxy(self, 7)

    def _set_PF(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(7, value, flags)

    PF = property(_get_PF, _set_PF) # type: BatchFloat64ArrayProxy

    def _get_kVA(self) -> BatchFloat64ArrayProxy:
        """
        Indicates the inverter nameplate capability (in kVA). Used as the base for Dynamics mode and Harmonics mode values.

        DSS property name: `kVA`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    def _set_kVA(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(8, value, flags)

    kVA = property(_get_kVA, _set_kVA) # type: BatchFloat64ArrayProxy

    def _get_pctCutIn(self) -> BatchFloat64ArrayProxy:
        """
        Cut-in power as a percentage of inverter kVA rating. It is the minimum DC power necessary to turn the inverter ON when it is OFF. Must be greater than or equal to %CutOut. Defaults to 2 for PVSystems and 0 for Storage elements which means that the inverter state will be always ON for this element.

        DSS property name: `%CutIn`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    def _set_pctCutIn(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(9, value, flags)

    pctCutIn = property(_get_pctCutIn, _set_pctCutIn) # type: BatchFloat64ArrayProxy

    def _get_pctCutOut(self) -> BatchFloat64ArrayProxy:
        """
        Cut-out power as a percentage of inverter kVA rating. It is the minimum DC power necessary to keep the inverter ON. Must be less than or equal to %CutIn. Defaults to 0, which means that, once ON, the inverter state will be always ON for this element.

        DSS property name: `%CutOut`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    def _set_pctCutOut(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(10, value, flags)

    pctCutOut = property(_get_pctCutOut, _set_pctCutOut) # type: BatchFloat64ArrayProxy

    def _get_EffCurve_str(self) -> List[str]:
        """
        An XYCurve object, previously defined, that describes the PER UNIT efficiency vs PER UNIT of rated kVA for the inverter. Power at the AC side of the inverter is discounted by the multiplier obtained from this curve.

        DSS property name: `EffCurve`, DSS property index: 11.
        """
        return self._get_batch_str_prop(11)

    def _set_EffCurve_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(11, value, flags)

    EffCurve_str = property(_get_EffCurve_str, _set_EffCurve_str) # type: List[str]

    def _get_EffCurve(self) -> List[XYcurve]:
        """
        An XYCurve object, previously defined, that describes the PER UNIT efficiency vs PER UNIT of rated kVA for the inverter. Power at the AC side of the inverter is discounted by the multiplier obtained from this curve.

        DSS property name: `EffCurve`, DSS property index: 11.
        """
        return self._get_batch_obj_prop(11)

    def _set_EffCurve(self, value: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(11, value, flags)

    EffCurve = property(_get_EffCurve, _set_EffCurve) # type: List[XYcurve]

    def _get_VarFollowInverter(self) -> List[bool]:
        """
        Boolean variable (Yes|No) or (True|False). Defaults to False, which indicates that the reactive power generation/absorption does not respect the inverter status.When set to True, the reactive power generation/absorption will cease when the inverter status is off, due to DC kW dropping below %CutOut.  The reactive power generation/absorption will begin again when the DC kW is above %CutIn.  When set to False, the Storage will generate/absorb reactive power regardless of the status of the inverter.

        DSS property name: `VarFollowInverter`, DSS property index: 12.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(12)
        ]

    def _set_VarFollowInverter(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(12, value, flags)

    VarFollowInverter = property(_get_VarFollowInverter, _set_VarFollowInverter) # type: List[bool]

    def _get_kvarMax(self) -> BatchFloat64ArrayProxy:
        """
        Indicates the maximum reactive power GENERATION (un-signed numerical variable in kvar) for the inverter. Defaults to kVA rating of the inverter.

        DSS property name: `kvarMax`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    def _set_kvarMax(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(13, value, flags)

    kvarMax = property(_get_kvarMax, _set_kvarMax) # type: BatchFloat64ArrayProxy

    def _get_kvarMaxAbs(self) -> BatchFloat64ArrayProxy:
        """
        Indicates the maximum reactive power ABSORPTION (un-signed numerical variable in kvar) for the inverter. Defaults to kvarMax.

        DSS property name: `kvarMaxAbs`, DSS property index: 14.
        """
        return BatchFloat64ArrayProxy(self, 14)

    def _set_kvarMaxAbs(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(14, value, flags)

    kvarMaxAbs = property(_get_kvarMaxAbs, _set_kvarMaxAbs) # type: BatchFloat64ArrayProxy

    def _get_WattPriority(self) -> List[bool]:
        """
        {Yes/No*/True/False} Set inverter to watt priority instead of the default var priority.

        DSS property name: `WattPriority`, DSS property index: 15.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(15)
        ]

    def _set_WattPriority(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(15, value, flags)

    WattPriority = property(_get_WattPriority, _set_WattPriority) # type: List[bool]

    def _get_PFPriority(self) -> List[bool]:
        """
        If set to true, priority is given to power factor and WattPriority is neglected. It works only if operating in either constant PF or constant kvar modes. Defaults to False.

        DSS property name: `PFPriority`, DSS property index: 16.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(16)
        ]

    def _set_PFPriority(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(16, value, flags)

    PFPriority = property(_get_PFPriority, _set_PFPriority) # type: List[bool]

    def _get_pctPMinNoVars(self) -> BatchFloat64ArrayProxy:
        """
        Minimum active power as percentage of kWrated under which there is no vars production/absorption. Defaults to 0 (disabled).

        DSS property name: `%PMinNoVars`, DSS property index: 17.
        """
        return BatchFloat64ArrayProxy(self, 17)

    def _set_pctPMinNoVars(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(17, value, flags)

    pctPMinNoVars = property(_get_pctPMinNoVars, _set_pctPMinNoVars) # type: BatchFloat64ArrayProxy

    def _get_pctPMinkvarMax(self) -> BatchFloat64ArrayProxy:
        """
        Minimum active power as percentage of kWrated that allows the inverter to produce/absorb reactive power up to its maximum reactive power, which can be either kvarMax or kvarMaxAbs, depending on the current operation quadrant. Defaults to 0 (disabled).

        DSS property name: `%PMinkvarMax`, DSS property index: 18.
        """
        return BatchFloat64ArrayProxy(self, 18)

    def _set_pctPMinkvarMax(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(18, value, flags)

    pctPMinkvarMax = property(_get_pctPMinkvarMax, _set_pctPMinkvarMax) # type: BatchFloat64ArrayProxy

    def _get_kWRated(self) -> BatchFloat64ArrayProxy:
        """
        kW rating of power output. Base for Loadshapes when DispMode=Follow. Sets kVA property if it has not been specified yet. Defaults to 25.

        DSS property name: `kWRated`, DSS property index: 19.
        """
        return BatchFloat64ArrayProxy(self, 19)

    def _set_kWRated(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(19, value, flags)

    kWRated = property(_get_kWRated, _set_kWRated) # type: BatchFloat64ArrayProxy

    def _get_pctkWRated(self) -> BatchFloat64ArrayProxy:
        """
        Upper limit on active power as a percentage of kWrated. Defaults to 100 (disabled).

        DSS property name: `%kWRated`, DSS property index: 20.
        """
        return BatchFloat64ArrayProxy(self, 20)

    def _set_pctkWRated(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(20, value, flags)

    pctkWRated = property(_get_pctkWRated, _set_pctkWRated) # type: BatchFloat64ArrayProxy

    def _get_kWhRated(self) -> BatchFloat64ArrayProxy:
        """
        Rated Storage capacity in kWh. Default is 50.

        DSS property name: `kWhRated`, DSS property index: 21.
        """
        return BatchFloat64ArrayProxy(self, 21)

    def _set_kWhRated(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(21, value, flags)

    kWhRated = property(_get_kWhRated, _set_kWhRated) # type: BatchFloat64ArrayProxy

    def _get_kWhStored(self) -> BatchFloat64ArrayProxy:
        """
        Present amount of energy stored, kWh. Default is same as kWhrated.

        DSS property name: `kWhStored`, DSS property index: 22.
        """
        return BatchFloat64ArrayProxy(self, 22)

    def _set_kWhStored(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(22, value, flags)

    kWhStored = property(_get_kWhStored, _set_kWhStored) # type: BatchFloat64ArrayProxy

    def _get_pctStored(self) -> BatchFloat64ArrayProxy:
        """
        Present amount of energy stored, % of rated kWh. Default is 100.

        DSS property name: `%Stored`, DSS property index: 23.
        """
        return BatchFloat64ArrayProxy(self, 23)

    def _set_pctStored(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(23, value, flags)

    pctStored = property(_get_pctStored, _set_pctStored) # type: BatchFloat64ArrayProxy

    def _get_pctReserve(self) -> BatchFloat64ArrayProxy:
        """
        Percentage of rated kWh Storage capacity to be held in reserve for normal operation. Default = 20. 
        This is treated as the minimum energy discharge level unless there is an emergency. For emergency operation set this property lower. Cannot be less than zero.

        DSS property name: `%Reserve`, DSS property index: 24.
        """
        return BatchFloat64ArrayProxy(self, 24)

    def _set_pctReserve(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(24, value, flags)

    pctReserve = property(_get_pctReserve, _set_pctReserve) # type: BatchFloat64ArrayProxy

    def _get_State(self) -> BatchInt32ArrayProxy:
        """
        {IDLING | CHARGING | DISCHARGING}  Get/Set present operational state. In DISCHARGING mode, the Storage element acts as a generator and the kW property is positive. The element continues discharging at the scheduled output power level until the Storage reaches the reserve value. Then the state reverts to IDLING. In the CHARGING state, the Storage element behaves like a Load and the kW property is negative. The element continues to charge until the max Storage kWh is reached and then switches to IDLING state. In IDLING state, the element draws the idling losses plus the associated inverter losses.

        DSS property name: `State`, DSS property index: 25.
        """
        return BatchInt32ArrayProxy(self, 25)

    def _set_State(self, value: Union[AnyStr, int, enums.StorageState, List[AnyStr], List[int], List[enums.StorageState], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(25, value, flags)
            return

        self._set_batch_int32_array(25, value, flags)

    State = property(_get_State, _set_State) # type: BatchInt32ArrayProxy

    def _get_State_str(self) -> List[str]:
        """
        {IDLING | CHARGING | DISCHARGING}  Get/Set present operational state. In DISCHARGING mode, the Storage element acts as a generator and the kW property is positive. The element continues discharging at the scheduled output power level until the Storage reaches the reserve value. Then the state reverts to IDLING. In the CHARGING state, the Storage element behaves like a Load and the kW property is negative. The element continues to charge until the max Storage kWh is reached and then switches to IDLING state. In IDLING state, the element draws the idling losses plus the associated inverter losses.

        DSS property name: `State`, DSS property index: 25.
        """
        return self._get_batch_str_prop(25)

    def _set_State_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_State(value, flags)

    State_str = property(_get_State_str, _set_State_str) # type: List[str]

    def _get_pctDischarge(self) -> BatchFloat64ArrayProxy:
        """
        Discharge rate (output power) in percentage of rated kW. Default = 100.

        DSS property name: `%Discharge`, DSS property index: 26.
        """
        return BatchFloat64ArrayProxy(self, 26)

    def _set_pctDischarge(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(26, value, flags)

    pctDischarge = property(_get_pctDischarge, _set_pctDischarge) # type: BatchFloat64ArrayProxy

    def _get_pctCharge(self) -> BatchFloat64ArrayProxy:
        """
        Charging rate (input power) in percentage of rated kW. Default = 100.

        DSS property name: `%Charge`, DSS property index: 27.
        """
        return BatchFloat64ArrayProxy(self, 27)

    def _set_pctCharge(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(27, value, flags)

    pctCharge = property(_get_pctCharge, _set_pctCharge) # type: BatchFloat64ArrayProxy

    def _get_pctEffCharge(self) -> BatchFloat64ArrayProxy:
        """
        Percentage efficiency for CHARGING the Storage element. Default = 90.

        DSS property name: `%EffCharge`, DSS property index: 28.
        """
        return BatchFloat64ArrayProxy(self, 28)

    def _set_pctEffCharge(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(28, value, flags)

    pctEffCharge = property(_get_pctEffCharge, _set_pctEffCharge) # type: BatchFloat64ArrayProxy

    def _get_pctEffDischarge(self) -> BatchFloat64ArrayProxy:
        """
        Percentage efficiency for DISCHARGING the Storage element. Default = 90.

        DSS property name: `%EffDischarge`, DSS property index: 29.
        """
        return BatchFloat64ArrayProxy(self, 29)

    def _set_pctEffDischarge(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(29, value, flags)

    pctEffDischarge = property(_get_pctEffDischarge, _set_pctEffDischarge) # type: BatchFloat64ArrayProxy

    def _get_pctIdlingkW(self) -> BatchFloat64ArrayProxy:
        """
        Percentage of rated kW consumed by idling losses. Default = 1.

        DSS property name: `%IdlingkW`, DSS property index: 30.
        """
        return BatchFloat64ArrayProxy(self, 30)

    def _set_pctIdlingkW(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(30, value, flags)

    pctIdlingkW = property(_get_pctIdlingkW, _set_pctIdlingkW) # type: BatchFloat64ArrayProxy

    def _get_pctR(self) -> BatchFloat64ArrayProxy:
        """
        Equivalent percentage internal resistance, ohms. Default is 0. Placed in series with internal voltage source for harmonics and dynamics modes. Use a combination of %IdlingkW, %EffCharge and %EffDischarge to account for losses in power flow modes.

        DSS property name: `%R`, DSS property index: 32.
        """
        return BatchFloat64ArrayProxy(self, 32)

    def _set_pctR(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(32, value, flags)

    pctR = property(_get_pctR, _set_pctR) # type: BatchFloat64ArrayProxy

    def _get_pctX(self) -> BatchFloat64ArrayProxy:
        """
        Equivalent percentage internal reactance, ohms. Default is 50%. Placed in series with internal voltage source for harmonics and dynamics modes. (Limits fault current to 2 pu.

        DSS property name: `%X`, DSS property index: 33.
        """
        return BatchFloat64ArrayProxy(self, 33)

    def _set_pctX(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(33, value, flags)

    pctX = property(_get_pctX, _set_pctX) # type: BatchFloat64ArrayProxy

    def _get_Model(self) -> BatchInt32ArrayProxy:
        """
        Integer code (default=1) for the model to be used for power output variation with voltage. Valid values are:

        1:Storage element injects/absorbs a CONSTANT power.
        2:Storage element is modeled as a CONSTANT IMPEDANCE.
        3:Compute load injection from User-written Model.

        DSS property name: `Model`, DSS property index: 34.
        """
        return BatchInt32ArrayProxy(self, 34)

    def _set_Model(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(34, value, flags)

    Model = property(_get_Model, _set_Model) # type: BatchInt32ArrayProxy

    def _get_VMinpu(self) -> BatchFloat64ArrayProxy:
        """
        Default = 0.90.  Minimum per unit voltage for which the Model is assumed to apply. Below this value, the load model reverts to a constant impedance model.

        DSS property name: `VMinpu`, DSS property index: 35.
        """
        return BatchFloat64ArrayProxy(self, 35)

    def _set_VMinpu(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(35, value, flags)

    VMinpu = property(_get_VMinpu, _set_VMinpu) # type: BatchFloat64ArrayProxy

    def _get_VMaxpu(self) -> BatchFloat64ArrayProxy:
        """
        Default = 1.10.  Maximum per unit voltage for which the Model is assumed to apply. Above this value, the load model reverts to a constant impedance model.

        DSS property name: `VMaxpu`, DSS property index: 36.
        """
        return BatchFloat64ArrayProxy(self, 36)

    def _set_VMaxpu(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(36, value, flags)

    VMaxpu = property(_get_VMaxpu, _set_VMaxpu) # type: BatchFloat64ArrayProxy

    def _get_Balanced(self) -> List[bool]:
        """
        {Yes | No*} Default is No. Force balanced current only for 3-phase Storage. Forces zero- and negative-sequence to zero. 

        DSS property name: `Balanced`, DSS property index: 37.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(37)
        ]

    def _set_Balanced(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(37, value, flags)

    Balanced = property(_get_Balanced, _set_Balanced) # type: List[bool]

    def _get_LimitCurrent(self) -> List[bool]:
        """
        Limits current magnitude to Vminpu value for both 1-phase and 3-phase Storage similar to Generator Model 7. For 3-phase, limits the positive-sequence current but not the negative-sequence.

        DSS property name: `LimitCurrent`, DSS property index: 38.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(38)
        ]

    def _set_LimitCurrent(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(38, value, flags)

    LimitCurrent = property(_get_LimitCurrent, _set_LimitCurrent) # type: List[bool]

    def _get_Yearly_str(self) -> List[str]:
        """
        Dispatch shape to use for yearly simulations.  Must be previously defined as a Loadshape object. If this is not specified, the Daily dispatch shape, if any, is repeated during Yearly solution modes. In the default dispatch mode, the Storage element uses this loadshape to trigger State changes.

        DSS property name: `Yearly`, DSS property index: 39.
        """
        return self._get_batch_str_prop(39)

    def _set_Yearly_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(39, value, flags)

    Yearly_str = property(_get_Yearly_str, _set_Yearly_str) # type: List[str]

    def _get_Yearly(self) -> List[LoadShape]:
        """
        Dispatch shape to use for yearly simulations.  Must be previously defined as a Loadshape object. If this is not specified, the Daily dispatch shape, if any, is repeated during Yearly solution modes. In the default dispatch mode, the Storage element uses this loadshape to trigger State changes.

        DSS property name: `Yearly`, DSS property index: 39.
        """
        return self._get_batch_obj_prop(39)

    def _set_Yearly(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(39, value, flags)

    Yearly = property(_get_Yearly, _set_Yearly) # type: List[LoadShape]

    def _get_Daily_str(self) -> List[str]:
        """
        Dispatch shape to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically.  In the default dispatch mode, the Storage element uses this loadshape to trigger State changes.

        DSS property name: `Daily`, DSS property index: 40.
        """
        return self._get_batch_str_prop(40)

    def _set_Daily_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(40, value, flags)

    Daily_str = property(_get_Daily_str, _set_Daily_str) # type: List[str]

    def _get_Daily(self) -> List[LoadShape]:
        """
        Dispatch shape to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically.  In the default dispatch mode, the Storage element uses this loadshape to trigger State changes.

        DSS property name: `Daily`, DSS property index: 40.
        """
        return self._get_batch_obj_prop(40)

    def _set_Daily(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(40, value, flags)

    Daily = property(_get_Daily, _set_Daily) # type: List[LoadShape]

    def _get_Duty_str(self) -> List[str]:
        """
        Load shape to use for duty cycle dispatch simulations such as for solar ramp rate studies. Must be previously defined as a Loadshape object. 

        Typically would have time intervals of 1-5 seconds. 

        Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.

        DSS property name: `Duty`, DSS property index: 41.
        """
        return self._get_batch_str_prop(41)

    def _set_Duty_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(41, value, flags)

    Duty_str = property(_get_Duty_str, _set_Duty_str) # type: List[str]

    def _get_Duty(self) -> List[LoadShape]:
        """
        Load shape to use for duty cycle dispatch simulations such as for solar ramp rate studies. Must be previously defined as a Loadshape object. 

        Typically would have time intervals of 1-5 seconds. 

        Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.

        DSS property name: `Duty`, DSS property index: 41.
        """
        return self._get_batch_obj_prop(41)

    def _set_Duty(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(41, value, flags)

    Duty = property(_get_Duty, _set_Duty) # type: List[LoadShape]

    def _get_DispMode(self) -> BatchInt32ArrayProxy:
        """
        {DEFAULT | FOLLOW | EXTERNAL | LOADLEVEL | PRICE } Default = "DEFAULT". Dispatch mode. 

        In DEFAULT mode, Storage element state is triggered to discharge or charge at the specified rate by the loadshape curve corresponding to the solution mode. 

        In FOLLOW mode the kW output of the Storage element follows the active loadshape multiplier until Storage is either exhausted or full. The element discharges for positive values and charges for negative values.  The loadshape is based on rated kW. 

        In EXTERNAL mode, Storage element state is controlled by an external Storagecontroller. This mode is automatically set if this Storage element is included in the element list of a StorageController element. 

        For the other two dispatch modes, the Storage element state is controlled by either the global default Loadlevel value or the price level. 

        DSS property name: `DispMode`, DSS property index: 42.
        """
        return BatchInt32ArrayProxy(self, 42)

    def _set_DispMode(self, value: Union[AnyStr, int, enums.StorageDispatchMode, List[AnyStr], List[int], List[enums.StorageDispatchMode], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(42, value, flags)
            return

        self._set_batch_int32_array(42, value, flags)

    DispMode = property(_get_DispMode, _set_DispMode) # type: BatchInt32ArrayProxy

    def _get_DispMode_str(self) -> List[str]:
        """
        {DEFAULT | FOLLOW | EXTERNAL | LOADLEVEL | PRICE } Default = "DEFAULT". Dispatch mode. 

        In DEFAULT mode, Storage element state is triggered to discharge or charge at the specified rate by the loadshape curve corresponding to the solution mode. 

        In FOLLOW mode the kW output of the Storage element follows the active loadshape multiplier until Storage is either exhausted or full. The element discharges for positive values and charges for negative values.  The loadshape is based on rated kW. 

        In EXTERNAL mode, Storage element state is controlled by an external Storagecontroller. This mode is automatically set if this Storage element is included in the element list of a StorageController element. 

        For the other two dispatch modes, the Storage element state is controlled by either the global default Loadlevel value or the price level. 

        DSS property name: `DispMode`, DSS property index: 42.
        """
        return self._get_batch_str_prop(42)

    def _set_DispMode_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_DispMode(value, flags)

    DispMode_str = property(_get_DispMode_str, _set_DispMode_str) # type: List[str]

    def _get_DischargeTrigger(self) -> BatchFloat64ArrayProxy:
        """
        Dispatch trigger value for discharging the Storage. 
        If = 0.0 the Storage element state is changed by the State command or by a StorageController object. 
        If <> 0  the Storage element state is set to DISCHARGING when this trigger level is EXCEEDED by either the specified Loadshape curve value or the price signal or global Loadlevel value, depending on dispatch mode. See State property.

        DSS property name: `DischargeTrigger`, DSS property index: 43.
        """
        return BatchFloat64ArrayProxy(self, 43)

    def _set_DischargeTrigger(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(43, value, flags)

    DischargeTrigger = property(_get_DischargeTrigger, _set_DischargeTrigger) # type: BatchFloat64ArrayProxy

    def _get_ChargeTrigger(self) -> BatchFloat64ArrayProxy:
        """
        Dispatch trigger value for charging the Storage. 

        If = 0.0 the Storage element state is changed by the State command or StorageController object.  

        If <> 0  the Storage element state is set to CHARGING when this trigger level is GREATER than either the specified Loadshape curve value or the price signal or global Loadlevel value, depending on dispatch mode. See State property.

        DSS property name: `ChargeTrigger`, DSS property index: 44.
        """
        return BatchFloat64ArrayProxy(self, 44)

    def _set_ChargeTrigger(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(44, value, flags)

    ChargeTrigger = property(_get_ChargeTrigger, _set_ChargeTrigger) # type: BatchFloat64ArrayProxy

    def _get_TimeChargeTrig(self) -> BatchFloat64ArrayProxy:
        """
        Time of day in fractional hours (0230 = 2.5) at which Storage element will automatically go into charge state. Default is 2.0.  Enter a negative time value to disable this feature.

        DSS property name: `TimeChargeTrig`, DSS property index: 45.
        """
        return BatchFloat64ArrayProxy(self, 45)

    def _set_TimeChargeTrig(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(45, value, flags)

    TimeChargeTrig = property(_get_TimeChargeTrig, _set_TimeChargeTrig) # type: BatchFloat64ArrayProxy

    def _get_Class(self) -> BatchInt32ArrayProxy:
        """
        An arbitrary integer number representing the class of Storage element so that Storage values may be segregated by class.

        DSS property name: `Class`, DSS property index: 46.
        """
        return BatchInt32ArrayProxy(self, 46)

    def _set_Class(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(46, value, flags)

    Class = property(_get_Class, _set_Class) # type: BatchInt32ArrayProxy

    def _get_DynaDLL(self) -> List[str]:
        """
        Name of DLL containing user-written dynamics model, which computes the terminal currents for Dynamics-mode simulations, overriding the default model.  Set to "none" to negate previous setting. This DLL has a simpler interface than the UserModel DLL and is only used for Dynamics mode.

        DSS property name: `DynaDLL`, DSS property index: 47.
        """
        return self._get_batch_str_prop(47)

    def _set_DynaDLL(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(47, value, flags)

    DynaDLL = property(_get_DynaDLL, _set_DynaDLL) # type: List[str]

    def _get_DynaData(self) -> List[str]:
        """
        String (in quotes or parentheses if necessary) that gets passed to the user-written dynamics model Edit function for defining the data required for that model.

        DSS property name: `DynaData`, DSS property index: 48.
        """
        return self._get_batch_str_prop(48)

    def _set_DynaData(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(48, value, flags)

    DynaData = property(_get_DynaData, _set_DynaData) # type: List[str]

    def _get_UserModel(self) -> List[str]:
        """
        Name of DLL containing user-written model, which computes the terminal currents for both power flow and dynamics, overriding the default model.  Set to "none" to negate previous setting.

        DSS property name: `UserModel`, DSS property index: 49.
        """
        return self._get_batch_str_prop(49)

    def _set_UserModel(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(49, value, flags)

    UserModel = property(_get_UserModel, _set_UserModel) # type: List[str]

    def _get_UserData(self) -> List[str]:
        """
        String (in quotes or parentheses) that gets passed to user-written model for defining the data required for that model.

        DSS property name: `UserData`, DSS property index: 50.
        """
        return self._get_batch_str_prop(50)

    def _set_UserData(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(50, value, flags)

    UserData = property(_get_UserData, _set_UserData) # type: List[str]

    def _get_DebugTrace(self) -> List[bool]:
        """
        {Yes | No }  Default is no.  Turn this on to capture the progress of the Storage model for each iteration.  Creates a separate file for each Storage element named "Storage_name.csv".

        DSS property name: `DebugTrace`, DSS property index: 51.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(51)
        ]

    def _set_DebugTrace(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(51, value, flags)

    DebugTrace = property(_get_DebugTrace, _set_DebugTrace) # type: List[bool]

    def _get_kVDC(self) -> BatchFloat64ArrayProxy:
        """
        Indicates the rated voltage (kV) at the input of the inverter while the storage is discharging. The value is normally greater or equal to the kV base of the Storage device. It is used for dynamics simulation ONLY.

        DSS property name: `kVDC`, DSS property index: 52.
        """
        return BatchFloat64ArrayProxy(self, 52)

    def _set_kVDC(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(52, value, flags)

    kVDC = property(_get_kVDC, _set_kVDC) # type: BatchFloat64ArrayProxy

    def _get_Kp(self) -> BatchFloat64ArrayProxy:
        """
        It is the proportional gain for the PI controller within the inverter. Use it to modify the controller response in dynamics simulation mode.

        DSS property name: `Kp`, DSS property index: 53.
        """
        return BatchFloat64ArrayProxy(self, 53)

    def _set_Kp(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(53, value, flags)

    Kp = property(_get_Kp, _set_Kp) # type: BatchFloat64ArrayProxy

    def _get_PITol(self) -> BatchFloat64ArrayProxy:
        """
        It is the tolerance (%) for the closed loop controller of the inverter. For dynamics simulation mode.

        DSS property name: `PITol`, DSS property index: 54.
        """
        return BatchFloat64ArrayProxy(self, 54)

    def _set_PITol(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(54, value, flags)

    PITol = property(_get_PITol, _set_PITol) # type: BatchFloat64ArrayProxy

    def _get_SafeVoltage(self) -> BatchFloat64ArrayProxy:
        """
        Indicates the voltage level (%) respect to the base voltage level for which the Inverter will operate. If this threshold is violated, the Inverter will enter safe mode (OFF). For dynamic simulation. By default is 80%.

        DSS property name: `SafeVoltage`, DSS property index: 55.
        """
        return BatchFloat64ArrayProxy(self, 55)

    def _set_SafeVoltage(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(55, value, flags)

    SafeVoltage = property(_get_SafeVoltage, _set_SafeVoltage) # type: BatchFloat64ArrayProxy

    def _get_SafeMode(self) -> List[bool]:
        """
        (Read only) Indicates whether the inverter entered (Yes) or not (No) into Safe Mode.

        DSS property name: `SafeMode`, DSS property index: 56.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(56)
        ]

    def _set_SafeMode(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(56, value, flags)

    SafeMode = property(_get_SafeMode, _set_SafeMode) # type: List[bool]

    def _get_DynamicEq_str(self) -> List[str]:
        """
        The name of the dynamic equation (DynamicExp) that will be used for defining the dynamic behavior of the generator. If not defined, the generator dynamics will follow the built-in dynamic equation.

        DSS property name: `DynamicEq`, DSS property index: 57.
        """
        return self._get_batch_str_prop(57)

    def _set_DynamicEq_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(57, value, flags)

    DynamicEq_str = property(_get_DynamicEq_str, _set_DynamicEq_str) # type: List[str]

    def _get_DynamicEq(self) -> List[DynamicExp]:
        """
        The name of the dynamic equation (DynamicExp) that will be used for defining the dynamic behavior of the generator. If not defined, the generator dynamics will follow the built-in dynamic equation.

        DSS property name: `DynamicEq`, DSS property index: 57.
        """
        return self._get_batch_obj_prop(57)

    def _set_DynamicEq(self, value: Union[AnyStr, DynamicExp, List[AnyStr], List[DynamicExp]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(57, value, flags)

    DynamicEq = property(_get_DynamicEq, _set_DynamicEq) # type: List[DynamicExp]

    def _get_DynOut(self) -> List[str]:
        """
        The name of the variables within the Dynamic equation that will be used to govern the Storage dynamics. This Storage model requires 1 output from the dynamic equation:

            1. Current.

        The output variables need to be defined in the same order.

        DSS property name: `DynOut`, DSS property index: 58.
        """
        return self._get_batch_str_prop(58)

    def _set_DynOut(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(58, value, flags)

    DynOut = property(_get_DynOut, _set_DynOut) # type: List[str]

    def _get_ControlMode(self) -> BatchInt32ArrayProxy:
        """
        Defines the control mode for the inverter. It can be one of {GFM | GFL*}. By default it is GFL (Grid Following Inverter). Use GFM (Grid Forming Inverter) for energizing islanded microgrids, but, if the device is connected to the grid, it is highly recommended to use GFL.

        GFM control mode disables any control action set by the InvControl device.

        DSS property name: `ControlMode`, DSS property index: 59.
        """
        return BatchInt32ArrayProxy(self, 59)

    def _set_ControlMode(self, value: Union[AnyStr, int, enums.InverterControlMode, List[AnyStr], List[int], List[enums.InverterControlMode], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(59, value, flags)
            return

        self._set_batch_int32_array(59, value, flags)

    ControlMode = property(_get_ControlMode, _set_ControlMode) # type: BatchInt32ArrayProxy

    def _get_ControlMode_str(self) -> List[str]:
        """
        Defines the control mode for the inverter. It can be one of {GFM | GFL*}. By default it is GFL (Grid Following Inverter). Use GFM (Grid Forming Inverter) for energizing islanded microgrids, but, if the device is connected to the grid, it is highly recommended to use GFL.

        GFM control mode disables any control action set by the InvControl device.

        DSS property name: `ControlMode`, DSS property index: 59.
        """
        return self._get_batch_str_prop(59)

    def _set_ControlMode_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_ControlMode(value, flags)

    ControlMode_str = property(_get_ControlMode_str, _set_ControlMode_str) # type: List[str]

    def _get_AmpLimit(self) -> BatchFloat64ArrayProxy:
        """
        The current limiter per phase for the IBR when operating in GFM mode. This limit is imposed to prevent the IBR to enter into Safe Mode when reaching the IBR power ratings.
        Once the IBR reaches this value, it remains there without moving into Safe Mode. This value needs to be set lower than the IBR Amps rating.

        DSS property name: `AmpLimit`, DSS property index: 60.
        """
        return BatchFloat64ArrayProxy(self, 60)

    def _set_AmpLimit(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(60, value, flags)

    AmpLimit = property(_get_AmpLimit, _set_AmpLimit) # type: BatchFloat64ArrayProxy

    def _get_AmpLimitGain(self) -> BatchFloat64ArrayProxy:
        """
        Use it for fine tunning the current limiter when active, by default is 0.8, it has to be a value between 0.1 and 1. This value allows users to fine tune the IBRs current limiter to match with the user requirements.

        DSS property name: `AmpLimitGain`, DSS property index: 61.
        """
        return BatchFloat64ArrayProxy(self, 61)

    def _set_AmpLimitGain(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(61, value, flags)

    AmpLimitGain = property(_get_AmpLimitGain, _set_AmpLimitGain) # type: BatchFloat64ArrayProxy

    def _get_Spectrum_str(self) -> List[str]:
        """
        Name of harmonic voltage or current spectrum for this Storage element. Current injection is assumed for inverter. Default value is "default", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 62.
        """
        return self._get_batch_str_prop(62)

    def _set_Spectrum_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(62, value, flags)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str) # type: List[str]

    def _get_Spectrum(self) -> List[SpectrumObj]:
        """
        Name of harmonic voltage or current spectrum for this Storage element. Current injection is assumed for inverter. Default value is "default", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 62.
        """
        return self._get_batch_obj_prop(62)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(62, value, flags)

    Spectrum = property(_get_Spectrum, _set_Spectrum) # type: List[SpectrumObj]

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 63.
        """
        return BatchFloat64ArrayProxy(self, 63)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(63, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy

    def _get_Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 64.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(64)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(64, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 65.
        """
        self._set_batch_string(65, value, flags)

class StorageBatchProperties(TypedDict):
    Phases: Union[int, Int32Array]
    Bus1: Union[AnyStr, List[AnyStr]]
    kV: Union[float, Float64Array]
    Conn: Union[AnyStr, int, enums.Connection, List[AnyStr], List[int], List[enums.Connection], Int32Array]
    kW: Union[float, Float64Array]
    kvar: Union[float, Float64Array]
    PF: Union[float, Float64Array]
    kVA: Union[float, Float64Array]
    pctCutIn: Union[float, Float64Array]
    pctCutOut: Union[float, Float64Array]
    EffCurve: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]
    VarFollowInverter: bool
    kvarMax: Union[float, Float64Array]
    kvarMaxAbs: Union[float, Float64Array]
    WattPriority: bool
    PFPriority: bool
    pctPMinNoVars: Union[float, Float64Array]
    pctPMinkvarMax: Union[float, Float64Array]
    kWRated: Union[float, Float64Array]
    pctkWRated: Union[float, Float64Array]
    kWhRated: Union[float, Float64Array]
    kWhStored: Union[float, Float64Array]
    pctStored: Union[float, Float64Array]
    pctReserve: Union[float, Float64Array]
    State: Union[AnyStr, int, enums.StorageState, List[AnyStr], List[int], List[enums.StorageState], Int32Array]
    pctDischarge: Union[float, Float64Array]
    pctCharge: Union[float, Float64Array]
    pctEffCharge: Union[float, Float64Array]
    pctEffDischarge: Union[float, Float64Array]
    pctIdlingkW: Union[float, Float64Array]
    pctR: Union[float, Float64Array]
    pctX: Union[float, Float64Array]
    Model: Union[int, Int32Array]
    VMinpu: Union[float, Float64Array]
    VMaxpu: Union[float, Float64Array]
    Balanced: bool
    LimitCurrent: bool
    Yearly: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    Daily: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    Duty: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    DispMode: Union[AnyStr, int, enums.StorageDispatchMode, List[AnyStr], List[int], List[enums.StorageDispatchMode], Int32Array]
    DischargeTrigger: Union[float, Float64Array]
    ChargeTrigger: Union[float, Float64Array]
    TimeChargeTrig: Union[float, Float64Array]
    Class: Union[int, Int32Array]
    DynaDLL: Union[AnyStr, List[AnyStr]]
    DynaData: Union[AnyStr, List[AnyStr]]
    UserModel: Union[AnyStr, List[AnyStr]]
    UserData: Union[AnyStr, List[AnyStr]]
    DebugTrace: bool
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

class IStorage(IDSSObj, StorageBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, Storage, StorageBatch)
        StorageBatch.__init__(self, self._api_util, sync_cls_idx=Storage._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Storage:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[StorageProperties]) -> Storage:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[StorageBatchProperties]) -> StorageBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
