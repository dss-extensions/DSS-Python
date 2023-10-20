# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from enum import IntEnum
from typing_extensions import TypedDict, Unpack
import numpy as np
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
from .XYcurve import XYcurve

class Storage(DSSObj, CktElementMixin, PCElementMixin, ElementHasRegistersMixin):
    __slots__ = []
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

    @property
    def Phases(self) -> int:
        """
        Number of Phases, this Storage element.  Power is evenly divided among phases.

        DSS property name: `Phases`, DSS property index: 1.
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @Phases.setter
    def Phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def Bus1(self) -> str:
        """
        Bus to which the Storage element is connected.  May include specific node specification.

        DSS property name: `Bus1`, DSS property index: 2.
        """
        return self._get_prop_string(2)

    @Bus1.setter
    def Bus1(self, value: AnyStr):
        self._set_string_o(2, value)

    @property
    def kV(self) -> float:
        """
        Nominal rated (1.0 per unit) voltage, kV, for Storage element. For 2- and 3-phase Storage elements, specify phase-phase kV. Otherwise, specify actual kV across each branch of the Storage element. 

        If wye (star), specify phase-neutral kV. 

        If delta or phase-phase connected, specify phase-phase kV.

        DSS property name: `kV`, DSS property index: 3.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @kV.setter
    def kV(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def Conn(self) -> enums.Connection:
        """
        ={wye|LN|delta|LL}.  Default is wye.

        DSS property name: `Conn`, DSS property index: 4.
        """
        return enums.Connection(self._lib.Obj_GetInt32(self._ptr, 4))

    @Conn.setter
    def Conn(self, value: Union[AnyStr, int, enums.Connection]):
        if not isinstance(value, int):
            self._set_string_o(4, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 4, value)

    @property
    def Conn_str(self) -> str:
        """
        ={wye|LN|delta|LL}.  Default is wye.

        DSS property name: `Conn`, DSS property index: 4.
        """
        return self._get_prop_string(4)

    @Conn_str.setter
    def Conn_str(self, value: AnyStr):
        self.Conn = value

    @property
    def kW(self) -> float:
        """
        Get/set the requested kW value. Final kW is subjected to the inverter ratings. A positive value denotes power coming OUT of the element, which is the opposite of a Load element. A negative value indicates the Storage element is in Charging state. This value is modified internally depending on the dispatch mode.

        DSS property name: `kW`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @kW.setter
    def kW(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def kvar(self) -> float:
        """
        Get/set the requested kvar value. Final kvar is subjected to the inverter ratings. Sets inverter to operate in constant kvar mode.

        DSS property name: `kvar`, DSS property index: 6.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    @kvar.setter
    def kvar(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 6, value)

    @property
    def PF(self) -> float:
        """
        Get/set the requested PF value. Final PF is subjected to the inverter ratings. Sets inverter to operate in constant PF mode. Nominally, the power factor for discharging (acting as a generator). Default is 1.0. 

        Enter negative for leading power factor (when kW and kvar have opposite signs.)

        A positive power factor signifies kw and kvar at the same direction.

        DSS property name: `PF`, DSS property index: 7.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @PF.setter
    def PF(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def kVA(self) -> float:
        """
        Indicates the inverter nameplate capability (in kVA). Used as the base for Dynamics mode and Harmonics mode values.

        DSS property name: `kVA`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @kVA.setter
    def kVA(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def pctCutIn(self) -> float:
        """
        Cut-in power as a percentage of inverter kVA rating. It is the minimum DC power necessary to turn the inverter ON when it is OFF. Must be greater than or equal to %CutOut. Defaults to 2 for PVSystems and 0 for Storage elements which means that the inverter state will be always ON for this element.

        DSS property name: `%CutIn`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @pctCutIn.setter
    def pctCutIn(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def pctCutOut(self) -> float:
        """
        Cut-out power as a percentage of inverter kVA rating. It is the minimum DC power necessary to keep the inverter ON. Must be less than or equal to %CutIn. Defaults to 0, which means that, once ON, the inverter state will be always ON for this element.

        DSS property name: `%CutOut`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @pctCutOut.setter
    def pctCutOut(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def EffCurve(self) -> str:
        """
        An XYCurve object, previously defined, that describes the PER UNIT efficiency vs PER UNIT of rated kVA for the inverter. Power at the AC side of the inverter is discounted by the multiplier obtained from this curve.

        DSS property name: `EffCurve`, DSS property index: 11.
        """
        return self._get_prop_string(11)

    @EffCurve.setter
    def EffCurve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(11, value)
            return

        self._set_string_o(11, value)

    @property
    def EffCurve_obj(self) -> XYcurve:
        """
        An XYCurve object, previously defined, that describes the PER UNIT efficiency vs PER UNIT of rated kVA for the inverter. Power at the AC side of the inverter is discounted by the multiplier obtained from this curve.

        DSS property name: `EffCurve`, DSS property index: 11.
        """
        return self._get_obj(11, XYcurve)

    @EffCurve_obj.setter
    def EffCurve_obj(self, value: XYcurve):
        self._set_obj(11, value)

    @property
    def VarFollowInverter(self) -> bool:
        """
        Boolean variable (Yes|No) or (True|False). Defaults to False, which indicates that the reactive power generation/absorption does not respect the inverter status.When set to True, the reactive power generation/absorption will cease when the inverter status is off, due to DC kW dropping below %CutOut.  The reactive power generation/absorption will begin again when the DC kW is above %CutIn.  When set to False, the Storage will generate/absorb reactive power regardless of the status of the inverter.

        DSS property name: `VarFollowInverter`, DSS property index: 12.
        """
        return self._lib.Obj_GetInt32(self._ptr, 12) != 0

    @VarFollowInverter.setter
    def VarFollowInverter(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 12, value)

    @property
    def kvarMax(self) -> float:
        """
        Indicates the maximum reactive power GENERATION (un-signed numerical variable in kvar) for the inverter. Defaults to kVA rating of the inverter.

        DSS property name: `kvarMax`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @kvarMax.setter
    def kvarMax(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def kvarMaxAbs(self) -> float:
        """
        Indicates the maximum reactive power ABSORPTION (un-signed numerical variable in kvar) for the inverter. Defaults to kvarMax.

        DSS property name: `kvarMaxAbs`, DSS property index: 14.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @kvarMaxAbs.setter
    def kvarMaxAbs(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def WattPriority(self) -> bool:
        """
        {Yes/No*/True/False} Set inverter to watt priority instead of the default var priority.

        DSS property name: `WattPriority`, DSS property index: 15.
        """
        return self._lib.Obj_GetInt32(self._ptr, 15) != 0

    @WattPriority.setter
    def WattPriority(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 15, value)

    @property
    def PFPriority(self) -> bool:
        """
        If set to true, priority is given to power factor and WattPriority is neglected. It works only if operating in either constant PF or constant kvar modes. Defaults to False.

        DSS property name: `PFPriority`, DSS property index: 16.
        """
        return self._lib.Obj_GetInt32(self._ptr, 16) != 0

    @PFPriority.setter
    def PFPriority(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 16, value)

    @property
    def pctPMinNoVars(self) -> float:
        """
        Minimum active power as percentage of kWrated under which there is no vars production/absorption. Defaults to 0 (disabled).

        DSS property name: `%PMinNoVars`, DSS property index: 17.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    @pctPMinNoVars.setter
    def pctPMinNoVars(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 17, value)

    @property
    def pctPMinkvarMax(self) -> float:
        """
        Minimum active power as percentage of kWrated that allows the inverter to produce/absorb reactive power up to its maximum reactive power, which can be either kvarMax or kvarMaxAbs, depending on the current operation quadrant. Defaults to 0 (disabled).

        DSS property name: `%PMinkvarMax`, DSS property index: 18.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    @pctPMinkvarMax.setter
    def pctPMinkvarMax(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 18, value)

    @property
    def kWRated(self) -> float:
        """
        kW rating of power output. Base for Loadshapes when DispMode=Follow. Sets kVA property if it has not been specified yet. Defaults to 25.

        DSS property name: `kWRated`, DSS property index: 19.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    @kWRated.setter
    def kWRated(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 19, value)

    @property
    def pctkWRated(self) -> float:
        """
        Upper limit on active power as a percentage of kWrated. Defaults to 100 (disabled).

        DSS property name: `%kWRated`, DSS property index: 20.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    @pctkWRated.setter
    def pctkWRated(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 20, value)

    @property
    def kWhRated(self) -> float:
        """
        Rated Storage capacity in kWh. Default is 50.

        DSS property name: `kWhRated`, DSS property index: 21.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @kWhRated.setter
    def kWhRated(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    @property
    def kWhStored(self) -> float:
        """
        Present amount of energy stored, kWh. Default is same as kWhrated.

        DSS property name: `kWhStored`, DSS property index: 22.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    @kWhStored.setter
    def kWhStored(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 22, value)

    @property
    def pctStored(self) -> float:
        """
        Present amount of energy stored, % of rated kWh. Default is 100.

        DSS property name: `%Stored`, DSS property index: 23.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    @pctStored.setter
    def pctStored(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 23, value)

    @property
    def pctReserve(self) -> float:
        """
        Percentage of rated kWh Storage capacity to be held in reserve for normal operation. Default = 20. 
        This is treated as the minimum energy discharge level unless there is an emergency. For emergency operation set this property lower. Cannot be less than zero.

        DSS property name: `%Reserve`, DSS property index: 24.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    @pctReserve.setter
    def pctReserve(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 24, value)

    @property
    def State(self) -> enums.StorageState:
        """
        {IDLING | CHARGING | DISCHARGING}  Get/Set present operational state. In DISCHARGING mode, the Storage element acts as a generator and the kW property is positive. The element continues discharging at the scheduled output power level until the Storage reaches the reserve value. Then the state reverts to IDLING. In the CHARGING state, the Storage element behaves like a Load and the kW property is negative. The element continues to charge until the max Storage kWh is reached and then switches to IDLING state. In IDLING state, the element draws the idling losses plus the associated inverter losses.

        DSS property name: `State`, DSS property index: 25.
        """
        return enums.StorageState(self._lib.Obj_GetInt32(self._ptr, 25))

    @State.setter
    def State(self, value: Union[AnyStr, int, enums.StorageState]):
        if not isinstance(value, int):
            self._set_string_o(25, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 25, value)

    @property
    def State_str(self) -> str:
        """
        {IDLING | CHARGING | DISCHARGING}  Get/Set present operational state. In DISCHARGING mode, the Storage element acts as a generator and the kW property is positive. The element continues discharging at the scheduled output power level until the Storage reaches the reserve value. Then the state reverts to IDLING. In the CHARGING state, the Storage element behaves like a Load and the kW property is negative. The element continues to charge until the max Storage kWh is reached and then switches to IDLING state. In IDLING state, the element draws the idling losses plus the associated inverter losses.

        DSS property name: `State`, DSS property index: 25.
        """
        return self._get_prop_string(25)

    @State_str.setter
    def State_str(self, value: AnyStr):
        self.State = value

    @property
    def pctDischarge(self) -> float:
        """
        Discharge rate (output power) in percentage of rated kW. Default = 100.

        DSS property name: `%Discharge`, DSS property index: 26.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 26)

    @pctDischarge.setter
    def pctDischarge(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 26, value)

    @property
    def pctCharge(self) -> float:
        """
        Charging rate (input power) in percentage of rated kW. Default = 100.

        DSS property name: `%Charge`, DSS property index: 27.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 27)

    @pctCharge.setter
    def pctCharge(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 27, value)

    @property
    def pctEffCharge(self) -> float:
        """
        Percentage efficiency for CHARGING the Storage element. Default = 90.

        DSS property name: `%EffCharge`, DSS property index: 28.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 28)

    @pctEffCharge.setter
    def pctEffCharge(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 28, value)

    @property
    def pctEffDischarge(self) -> float:
        """
        Percentage efficiency for DISCHARGING the Storage element. Default = 90.

        DSS property name: `%EffDischarge`, DSS property index: 29.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 29)

    @pctEffDischarge.setter
    def pctEffDischarge(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 29, value)

    @property
    def pctIdlingkW(self) -> float:
        """
        Percentage of rated kW consumed by idling losses. Default = 1.

        DSS property name: `%IdlingkW`, DSS property index: 30.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 30)

    @pctIdlingkW.setter
    def pctIdlingkW(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 30, value)

    @property
    def pctR(self) -> float:
        """
        Equivalent percentage internal resistance, ohms. Default is 0. Placed in series with internal voltage source for harmonics and dynamics modes. Use a combination of %IdlingkW, %EffCharge and %EffDischarge to account for losses in power flow modes.

        DSS property name: `%R`, DSS property index: 32.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 32)

    @pctR.setter
    def pctR(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 32, value)

    @property
    def pctX(self) -> float:
        """
        Equivalent percentage internal reactance, ohms. Default is 50%. Placed in series with internal voltage source for harmonics and dynamics modes. (Limits fault current to 2 pu.

        DSS property name: `%X`, DSS property index: 33.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 33)

    @pctX.setter
    def pctX(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 33, value)

    @property
    def Model(self) -> int:
        """
        Integer code (default=1) for the model to be used for power output variation with voltage. Valid values are:

        1:Storage element injects/absorbs a CONSTANT power.
        2:Storage element is modeled as a CONSTANT IMPEDANCE.
        3:Compute load injection from User-written Model.

        DSS property name: `Model`, DSS property index: 34.
        """
        return self._lib.Obj_GetInt32(self._ptr, 34)

    @Model.setter
    def Model(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 34, value)

    @property
    def VMinpu(self) -> float:
        """
        Default = 0.90.  Minimum per unit voltage for which the Model is assumed to apply. Below this value, the load model reverts to a constant impedance model.

        DSS property name: `VMinpu`, DSS property index: 35.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 35)

    @VMinpu.setter
    def VMinpu(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 35, value)

    @property
    def VMaxpu(self) -> float:
        """
        Default = 1.10.  Maximum per unit voltage for which the Model is assumed to apply. Above this value, the load model reverts to a constant impedance model.

        DSS property name: `VMaxpu`, DSS property index: 36.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 36)

    @VMaxpu.setter
    def VMaxpu(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 36, value)

    @property
    def Balanced(self) -> bool:
        """
        {Yes | No*} Default is No. Force balanced current only for 3-phase Storage. Forces zero- and negative-sequence to zero. 

        DSS property name: `Balanced`, DSS property index: 37.
        """
        return self._lib.Obj_GetInt32(self._ptr, 37) != 0

    @Balanced.setter
    def Balanced(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 37, value)

    @property
    def LimitCurrent(self) -> bool:
        """
        Limits current magnitude to Vminpu value for both 1-phase and 3-phase Storage similar to Generator Model 7. For 3-phase, limits the positive-sequence current but not the negative-sequence.

        DSS property name: `LimitCurrent`, DSS property index: 38.
        """
        return self._lib.Obj_GetInt32(self._ptr, 38) != 0

    @LimitCurrent.setter
    def LimitCurrent(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 38, value)

    @property
    def Yearly(self) -> str:
        """
        Dispatch shape to use for yearly simulations.  Must be previously defined as a Loadshape object. If this is not specified, the Daily dispatch shape, if any, is repeated during Yearly solution modes. In the default dispatch mode, the Storage element uses this loadshape to trigger State changes.

        DSS property name: `Yearly`, DSS property index: 39.
        """
        return self._get_prop_string(39)

    @Yearly.setter
    def Yearly(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(39, value)
            return

        self._set_string_o(39, value)

    @property
    def Yearly_obj(self) -> LoadShape:
        """
        Dispatch shape to use for yearly simulations.  Must be previously defined as a Loadshape object. If this is not specified, the Daily dispatch shape, if any, is repeated during Yearly solution modes. In the default dispatch mode, the Storage element uses this loadshape to trigger State changes.

        DSS property name: `Yearly`, DSS property index: 39.
        """
        return self._get_obj(39, LoadShape)

    @Yearly_obj.setter
    def Yearly_obj(self, value: LoadShape):
        self._set_obj(39, value)

    @property
    def Daily(self) -> str:
        """
        Dispatch shape to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically.  In the default dispatch mode, the Storage element uses this loadshape to trigger State changes.

        DSS property name: `Daily`, DSS property index: 40.
        """
        return self._get_prop_string(40)

    @Daily.setter
    def Daily(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(40, value)
            return

        self._set_string_o(40, value)

    @property
    def Daily_obj(self) -> LoadShape:
        """
        Dispatch shape to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically.  In the default dispatch mode, the Storage element uses this loadshape to trigger State changes.

        DSS property name: `Daily`, DSS property index: 40.
        """
        return self._get_obj(40, LoadShape)

    @Daily_obj.setter
    def Daily_obj(self, value: LoadShape):
        self._set_obj(40, value)

    @property
    def Duty(self) -> str:
        """
        Load shape to use for duty cycle dispatch simulations such as for solar ramp rate studies. Must be previously defined as a Loadshape object. 

        Typically would have time intervals of 1-5 seconds. 

        Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.

        DSS property name: `Duty`, DSS property index: 41.
        """
        return self._get_prop_string(41)

    @Duty.setter
    def Duty(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(41, value)
            return

        self._set_string_o(41, value)

    @property
    def Duty_obj(self) -> LoadShape:
        """
        Load shape to use for duty cycle dispatch simulations such as for solar ramp rate studies. Must be previously defined as a Loadshape object. 

        Typically would have time intervals of 1-5 seconds. 

        Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.

        DSS property name: `Duty`, DSS property index: 41.
        """
        return self._get_obj(41, LoadShape)

    @Duty_obj.setter
    def Duty_obj(self, value: LoadShape):
        self._set_obj(41, value)

    @property
    def DispMode(self) -> enums.StorageDispatchMode:
        """
        {DEFAULT | FOLLOW | EXTERNAL | LOADLEVEL | PRICE } Default = "DEFAULT". Dispatch mode. 

        In DEFAULT mode, Storage element state is triggered to discharge or charge at the specified rate by the loadshape curve corresponding to the solution mode. 

        In FOLLOW mode the kW output of the Storage element follows the active loadshape multiplier until Storage is either exhausted or full. The element discharges for positive values and charges for negative values.  The loadshape is based on rated kW. 

        In EXTERNAL mode, Storage element state is controlled by an external Storagecontroller. This mode is automatically set if this Storage element is included in the element list of a StorageController element. 

        For the other two dispatch modes, the Storage element state is controlled by either the global default Loadlevel value or the price level. 

        DSS property name: `DispMode`, DSS property index: 42.
        """
        return enums.StorageDispatchMode(self._lib.Obj_GetInt32(self._ptr, 42))

    @DispMode.setter
    def DispMode(self, value: Union[AnyStr, int, enums.StorageDispatchMode]):
        if not isinstance(value, int):
            self._set_string_o(42, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 42, value)

    @property
    def DispMode_str(self) -> str:
        """
        {DEFAULT | FOLLOW | EXTERNAL | LOADLEVEL | PRICE } Default = "DEFAULT". Dispatch mode. 

        In DEFAULT mode, Storage element state is triggered to discharge or charge at the specified rate by the loadshape curve corresponding to the solution mode. 

        In FOLLOW mode the kW output of the Storage element follows the active loadshape multiplier until Storage is either exhausted or full. The element discharges for positive values and charges for negative values.  The loadshape is based on rated kW. 

        In EXTERNAL mode, Storage element state is controlled by an external Storagecontroller. This mode is automatically set if this Storage element is included in the element list of a StorageController element. 

        For the other two dispatch modes, the Storage element state is controlled by either the global default Loadlevel value or the price level. 

        DSS property name: `DispMode`, DSS property index: 42.
        """
        return self._get_prop_string(42)

    @DispMode_str.setter
    def DispMode_str(self, value: AnyStr):
        self.DispMode = value

    @property
    def DischargeTrigger(self) -> float:
        """
        Dispatch trigger value for discharging the Storage. 
        If = 0.0 the Storage element state is changed by the State command or by a StorageController object. 
        If <> 0  the Storage element state is set to DISCHARGING when this trigger level is EXCEEDED by either the specified Loadshape curve value or the price signal or global Loadlevel value, depending on dispatch mode. See State property.

        DSS property name: `DischargeTrigger`, DSS property index: 43.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 43)

    @DischargeTrigger.setter
    def DischargeTrigger(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 43, value)

    @property
    def ChargeTrigger(self) -> float:
        """
        Dispatch trigger value for charging the Storage. 

        If = 0.0 the Storage element state is changed by the State command or StorageController object.  

        If <> 0  the Storage element state is set to CHARGING when this trigger level is GREATER than either the specified Loadshape curve value or the price signal or global Loadlevel value, depending on dispatch mode. See State property.

        DSS property name: `ChargeTrigger`, DSS property index: 44.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 44)

    @ChargeTrigger.setter
    def ChargeTrigger(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 44, value)

    @property
    def TimeChargeTrig(self) -> float:
        """
        Time of day in fractional hours (0230 = 2.5) at which Storage element will automatically go into charge state. Default is 2.0.  Enter a negative time value to disable this feature.

        DSS property name: `TimeChargeTrig`, DSS property index: 45.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 45)

    @TimeChargeTrig.setter
    def TimeChargeTrig(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 45, value)

    @property
    def Class(self) -> int:
        """
        An arbitrary integer number representing the class of Storage element so that Storage values may be segregated by class.

        DSS property name: `Class`, DSS property index: 46.
        """
        return self._lib.Obj_GetInt32(self._ptr, 46)

    @Class.setter
    def Class(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 46, value)

    @property
    def DynaDLL(self) -> str:
        """
        Name of DLL containing user-written dynamics model, which computes the terminal currents for Dynamics-mode simulations, overriding the default model.  Set to "none" to negate previous setting. This DLL has a simpler interface than the UserModel DLL and is only used for Dynamics mode.

        DSS property name: `DynaDLL`, DSS property index: 47.
        """
        return self._get_prop_string(47)

    @DynaDLL.setter
    def DynaDLL(self, value: AnyStr):
        self._set_string_o(47, value)

    @property
    def DynaData(self) -> str:
        """
        String (in quotes or parentheses if necessary) that gets passed to the user-written dynamics model Edit function for defining the data required for that model.

        DSS property name: `DynaData`, DSS property index: 48.
        """
        return self._get_prop_string(48)

    @DynaData.setter
    def DynaData(self, value: AnyStr):
        self._set_string_o(48, value)

    @property
    def UserModel(self) -> str:
        """
        Name of DLL containing user-written model, which computes the terminal currents for both power flow and dynamics, overriding the default model.  Set to "none" to negate previous setting.

        DSS property name: `UserModel`, DSS property index: 49.
        """
        return self._get_prop_string(49)

    @UserModel.setter
    def UserModel(self, value: AnyStr):
        self._set_string_o(49, value)

    @property
    def UserData(self) -> str:
        """
        String (in quotes or parentheses) that gets passed to user-written model for defining the data required for that model.

        DSS property name: `UserData`, DSS property index: 50.
        """
        return self._get_prop_string(50)

    @UserData.setter
    def UserData(self, value: AnyStr):
        self._set_string_o(50, value)

    @property
    def DebugTrace(self) -> bool:
        """
        {Yes | No }  Default is no.  Turn this on to capture the progress of the Storage model for each iteration.  Creates a separate file for each Storage element named "Storage_name.csv".

        DSS property name: `DebugTrace`, DSS property index: 51.
        """
        return self._lib.Obj_GetInt32(self._ptr, 51) != 0

    @DebugTrace.setter
    def DebugTrace(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 51, value)

    @property
    def kVDC(self) -> float:
        """
        Indicates the rated voltage (kV) at the input of the inverter while the storage is discharging. The value is normally greater or equal to the kV base of the Storage device. It is used for dynamics simulation ONLY.

        DSS property name: `kVDC`, DSS property index: 52.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 52)

    @kVDC.setter
    def kVDC(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 52, value)

    @property
    def Kp(self) -> float:
        """
        It is the proportional gain for the PI controller within the inverter. Use it to modify the controller response in dynamics simulation mode.

        DSS property name: `Kp`, DSS property index: 53.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 53)

    @Kp.setter
    def Kp(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 53, value)

    @property
    def PITol(self) -> float:
        """
        It is the tolerance (%) for the closed loop controller of the inverter. For dynamics simulation mode.

        DSS property name: `PITol`, DSS property index: 54.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 54)

    @PITol.setter
    def PITol(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 54, value)

    @property
    def SafeVoltage(self) -> float:
        """
        Indicates the voltage level (%) respect to the base voltage level for which the Inverter will operate. If this threshold is violated, the Inverter will enter safe mode (OFF). For dynamic simulation. By default is 80%.

        DSS property name: `SafeVoltage`, DSS property index: 55.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 55)

    @SafeVoltage.setter
    def SafeVoltage(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 55, value)

    @property
    def SafeMode(self) -> bool:
        """
        (Read only) Indicates whether the inverter entered (Yes) or not (No) into Safe Mode.

        DSS property name: `SafeMode`, DSS property index: 56.
        """
        return self._lib.Obj_GetInt32(self._ptr, 56) != 0

    @SafeMode.setter
    def SafeMode(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 56, value)

    @property
    def DynamicEq(self) -> str:
        """
        The name of the dynamic equation (DynamicExp) that will be used for defining the dynamic behavior of the generator. If not defined, the generator dynamics will follow the built-in dynamic equation.

        DSS property name: `DynamicEq`, DSS property index: 57.
        """
        return self._get_prop_string(57)

    @DynamicEq.setter
    def DynamicEq(self, value: Union[AnyStr, DynamicExp]):
        if isinstance(value, DSSObj):
            self._set_obj(57, value)
            return

        self._set_string_o(57, value)

    @property
    def DynamicEq_obj(self) -> DynamicExp:
        """
        The name of the dynamic equation (DynamicExp) that will be used for defining the dynamic behavior of the generator. If not defined, the generator dynamics will follow the built-in dynamic equation.

        DSS property name: `DynamicEq`, DSS property index: 57.
        """
        return self._get_obj(57, DynamicExp)

    @DynamicEq_obj.setter
    def DynamicEq_obj(self, value: DynamicExp):
        self._set_obj(57, value)

    @property
    def DynOut(self) -> str:
        """
        The name of the variables within the Dynamic equation that will be used to govern the Storage dynamics. This Storage model requires 1 output from the dynamic equation:

            1. Current.

        The output variables need to be defined in the same order.

        DSS property name: `DynOut`, DSS property index: 58.
        """
        return self._get_prop_string(58)

    @DynOut.setter
    def DynOut(self, value: AnyStr):
        self._set_string_o(58, value)

    @property
    def ControlMode(self) -> enums.InverterControlMode:
        """
        Defines the control mode for the inverter. It can be one of {GFM | GFL*}. By default it is GFL (Grid Following Inverter). Use GFM (Grid Forming Inverter) for energizing islanded microgrids, but, if the device is connected to the grid, it is highly recommended to use GFL.

        GFM control mode disables any control action set by the InvControl device.

        DSS property name: `ControlMode`, DSS property index: 59.
        """
        return enums.InverterControlMode(self._lib.Obj_GetInt32(self._ptr, 59))

    @ControlMode.setter
    def ControlMode(self, value: Union[AnyStr, int, enums.InverterControlMode]):
        if not isinstance(value, int):
            self._set_string_o(59, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 59, value)

    @property
    def ControlMode_str(self) -> str:
        """
        Defines the control mode for the inverter. It can be one of {GFM | GFL*}. By default it is GFL (Grid Following Inverter). Use GFM (Grid Forming Inverter) for energizing islanded microgrids, but, if the device is connected to the grid, it is highly recommended to use GFL.

        GFM control mode disables any control action set by the InvControl device.

        DSS property name: `ControlMode`, DSS property index: 59.
        """
        return self._get_prop_string(59)

    @ControlMode_str.setter
    def ControlMode_str(self, value: AnyStr):
        self.ControlMode = value

    @property
    def AmpLimit(self) -> float:
        """
        The current limiter per phase for the IBR when operating in GFM mode. This limit is imposed to prevent the IBR to enter into Safe Mode when reaching the IBR power ratings.
        Once the IBR reaches this value, it remains there without moving into Safe Mode. This value needs to be set lower than the IBR Amps rating.

        DSS property name: `AmpLimit`, DSS property index: 60.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 60)

    @AmpLimit.setter
    def AmpLimit(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 60, value)

    @property
    def AmpLimitGain(self) -> float:
        """
        Use it for fine tunning the current limiter when active, by default is 0.8, it has to be a value between 0.1 and 1. This value allows users to fine tune the IBRs current limiter to match with the user requirements.

        DSS property name: `AmpLimitGain`, DSS property index: 61.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 61)

    @AmpLimitGain.setter
    def AmpLimitGain(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 61, value)

    @property
    def Spectrum(self) -> str:
        """
        Name of harmonic voltage or current spectrum for this Storage element. Current injection is assumed for inverter. Default value is "default", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 62.
        """
        return self._get_prop_string(62)

    @Spectrum.setter
    def Spectrum(self, value: Union[AnyStr, SpectrumObj]):
        if isinstance(value, DSSObj):
            self._set_obj(62, value)
            return

        self._set_string_o(62, value)

    @property
    def Spectrum_obj(self) -> SpectrumObj:
        """
        Name of harmonic voltage or current spectrum for this Storage element. Current injection is assumed for inverter. Default value is "default", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 62.
        """
        return self._get_obj(62, SpectrumObj)

    @Spectrum_obj.setter
    def Spectrum_obj(self, value: SpectrumObj):
        self._set_obj(62, value)

    @property
    def BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 63.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 63)

    @BaseFreq.setter
    def BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 63, value)

    @property
    def Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 64.
        """
        return self._lib.Obj_GetInt32(self._ptr, 64) != 0

    @Enabled.setter
    def Enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 64, value)

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

class StorageBatch(DSSBatch):
    _cls_name = 'Storage'
    _obj_cls = Storage
    _cls_idx = 29


    @property
    def Phases(self) -> BatchInt32ArrayProxy:
        """
        Number of Phases, this Storage element.  Power is evenly divided among phases.

        DSS property name: `Phases`, DSS property index: 1.
        """
        return BatchInt32ArrayProxy(self, 1)

    @Phases.setter
    def Phases(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(1, value)

    @property
    def Bus1(self) -> List[str]:
        """
        Bus to which the Storage element is connected.  May include specific node specification.

        DSS property name: `Bus1`, DSS property index: 2.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 2) 

    @Bus1.setter
    def Bus1(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(2, value)

    @property
    def kV(self) -> BatchFloat64ArrayProxy:
        """
        Nominal rated (1.0 per unit) voltage, kV, for Storage element. For 2- and 3-phase Storage elements, specify phase-phase kV. Otherwise, specify actual kV across each branch of the Storage element. 

        If wye (star), specify phase-neutral kV. 

        If delta or phase-phase connected, specify phase-phase kV.

        DSS property name: `kV`, DSS property index: 3.
        """
        return BatchFloat64ArrayProxy(self, 3)

    @kV.setter
    def kV(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(3, value)

    @property
    def Conn(self) -> BatchInt32ArrayProxy:
        """
        ={wye|LN|delta|LL}.  Default is wye.

        DSS property name: `Conn`, DSS property index: 4.
        """
        return BatchInt32ArrayProxy(self, 4)

    @Conn.setter
    def Conn(self, value: Union[AnyStr, int, enums.Connection, List[AnyStr], List[int], List[enums.Connection], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(4, value)
            return
    
        self._set_batch_int32_array(4, value)

    @property
    def Conn_str(self) -> str:
        """
        ={wye|LN|delta|LL}.  Default is wye.

        DSS property name: `Conn`, DSS property index: 4.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 4)

    @Conn_str.setter
    def Conn_str(self, value: AnyStr):
        self.Conn = value

    @property
    def kW(self) -> BatchFloat64ArrayProxy:
        """
        Get/set the requested kW value. Final kW is subjected to the inverter ratings. A positive value denotes power coming OUT of the element, which is the opposite of a Load element. A negative value indicates the Storage element is in Charging state. This value is modified internally depending on the dispatch mode.

        DSS property name: `kW`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    @kW.setter
    def kW(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(5, value)

    @property
    def kvar(self) -> BatchFloat64ArrayProxy:
        """
        Get/set the requested kvar value. Final kvar is subjected to the inverter ratings. Sets inverter to operate in constant kvar mode.

        DSS property name: `kvar`, DSS property index: 6.
        """
        return BatchFloat64ArrayProxy(self, 6)

    @kvar.setter
    def kvar(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(6, value)

    @property
    def PF(self) -> BatchFloat64ArrayProxy:
        """
        Get/set the requested PF value. Final PF is subjected to the inverter ratings. Sets inverter to operate in constant PF mode. Nominally, the power factor for discharging (acting as a generator). Default is 1.0. 

        Enter negative for leading power factor (when kW and kvar have opposite signs.)

        A positive power factor signifies kw and kvar at the same direction.

        DSS property name: `PF`, DSS property index: 7.
        """
        return BatchFloat64ArrayProxy(self, 7)

    @PF.setter
    def PF(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(7, value)

    @property
    def kVA(self) -> BatchFloat64ArrayProxy:
        """
        Indicates the inverter nameplate capability (in kVA). Used as the base for Dynamics mode and Harmonics mode values.

        DSS property name: `kVA`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    @kVA.setter
    def kVA(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(8, value)

    @property
    def pctCutIn(self) -> BatchFloat64ArrayProxy:
        """
        Cut-in power as a percentage of inverter kVA rating. It is the minimum DC power necessary to turn the inverter ON when it is OFF. Must be greater than or equal to %CutOut. Defaults to 2 for PVSystems and 0 for Storage elements which means that the inverter state will be always ON for this element.

        DSS property name: `%CutIn`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    @pctCutIn.setter
    def pctCutIn(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(9, value)

    @property
    def pctCutOut(self) -> BatchFloat64ArrayProxy:
        """
        Cut-out power as a percentage of inverter kVA rating. It is the minimum DC power necessary to keep the inverter ON. Must be less than or equal to %CutIn. Defaults to 0, which means that, once ON, the inverter state will be always ON for this element.

        DSS property name: `%CutOut`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    @pctCutOut.setter
    def pctCutOut(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(10, value)

    @property
    def EffCurve(self) -> List[str]:
        """
        An XYCurve object, previously defined, that describes the PER UNIT efficiency vs PER UNIT of rated kVA for the inverter. Power at the AC side of the inverter is discounted by the multiplier obtained from this curve.

        DSS property name: `EffCurve`, DSS property index: 11.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 11)

    @EffCurve.setter
    def EffCurve(self, value: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]):
        self._set_batch_obj_prop(11, value)

    @property
    def EffCurve_obj(self) -> List[XYcurve]:
        """
        An XYCurve object, previously defined, that describes the PER UNIT efficiency vs PER UNIT of rated kVA for the inverter. Power at the AC side of the inverter is discounted by the multiplier obtained from this curve.

        DSS property name: `EffCurve`, DSS property index: 11.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 11)

    @EffCurve_obj.setter
    def EffCurve_obj(self, value: XYcurve):
        self._set_batch_string(11, value)

    @property
    def VarFollowInverter(self) -> List[bool]:
        """
        Boolean variable (Yes|No) or (True|False). Defaults to False, which indicates that the reactive power generation/absorption does not respect the inverter status.When set to True, the reactive power generation/absorption will cease when the inverter status is off, due to DC kW dropping below %CutOut.  The reactive power generation/absorption will begin again when the DC kW is above %CutIn.  When set to False, the Storage will generate/absorb reactive power regardless of the status of the inverter.

        DSS property name: `VarFollowInverter`, DSS property index: 12.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 12)
        ]
    @VarFollowInverter.setter
    def VarFollowInverter(self, value: bool):
        self._set_batch_int32_array(12, value)

    @property
    def kvarMax(self) -> BatchFloat64ArrayProxy:
        """
        Indicates the maximum reactive power GENERATION (un-signed numerical variable in kvar) for the inverter. Defaults to kVA rating of the inverter.

        DSS property name: `kvarMax`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    @kvarMax.setter
    def kvarMax(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(13, value)

    @property
    def kvarMaxAbs(self) -> BatchFloat64ArrayProxy:
        """
        Indicates the maximum reactive power ABSORPTION (un-signed numerical variable in kvar) for the inverter. Defaults to kvarMax.

        DSS property name: `kvarMaxAbs`, DSS property index: 14.
        """
        return BatchFloat64ArrayProxy(self, 14)

    @kvarMaxAbs.setter
    def kvarMaxAbs(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(14, value)

    @property
    def WattPriority(self) -> List[bool]:
        """
        {Yes/No*/True/False} Set inverter to watt priority instead of the default var priority.

        DSS property name: `WattPriority`, DSS property index: 15.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 15)
        ]
    @WattPriority.setter
    def WattPriority(self, value: bool):
        self._set_batch_int32_array(15, value)

    @property
    def PFPriority(self) -> List[bool]:
        """
        If set to true, priority is given to power factor and WattPriority is neglected. It works only if operating in either constant PF or constant kvar modes. Defaults to False.

        DSS property name: `PFPriority`, DSS property index: 16.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 16)
        ]
    @PFPriority.setter
    def PFPriority(self, value: bool):
        self._set_batch_int32_array(16, value)

    @property
    def pctPMinNoVars(self) -> BatchFloat64ArrayProxy:
        """
        Minimum active power as percentage of kWrated under which there is no vars production/absorption. Defaults to 0 (disabled).

        DSS property name: `%PMinNoVars`, DSS property index: 17.
        """
        return BatchFloat64ArrayProxy(self, 17)

    @pctPMinNoVars.setter
    def pctPMinNoVars(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(17, value)

    @property
    def pctPMinkvarMax(self) -> BatchFloat64ArrayProxy:
        """
        Minimum active power as percentage of kWrated that allows the inverter to produce/absorb reactive power up to its maximum reactive power, which can be either kvarMax or kvarMaxAbs, depending on the current operation quadrant. Defaults to 0 (disabled).

        DSS property name: `%PMinkvarMax`, DSS property index: 18.
        """
        return BatchFloat64ArrayProxy(self, 18)

    @pctPMinkvarMax.setter
    def pctPMinkvarMax(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(18, value)

    @property
    def kWRated(self) -> BatchFloat64ArrayProxy:
        """
        kW rating of power output. Base for Loadshapes when DispMode=Follow. Sets kVA property if it has not been specified yet. Defaults to 25.

        DSS property name: `kWRated`, DSS property index: 19.
        """
        return BatchFloat64ArrayProxy(self, 19)

    @kWRated.setter
    def kWRated(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(19, value)

    @property
    def pctkWRated(self) -> BatchFloat64ArrayProxy:
        """
        Upper limit on active power as a percentage of kWrated. Defaults to 100 (disabled).

        DSS property name: `%kWRated`, DSS property index: 20.
        """
        return BatchFloat64ArrayProxy(self, 20)

    @pctkWRated.setter
    def pctkWRated(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(20, value)

    @property
    def kWhRated(self) -> BatchFloat64ArrayProxy:
        """
        Rated Storage capacity in kWh. Default is 50.

        DSS property name: `kWhRated`, DSS property index: 21.
        """
        return BatchFloat64ArrayProxy(self, 21)

    @kWhRated.setter
    def kWhRated(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(21, value)

    @property
    def kWhStored(self) -> BatchFloat64ArrayProxy:
        """
        Present amount of energy stored, kWh. Default is same as kWhrated.

        DSS property name: `kWhStored`, DSS property index: 22.
        """
        return BatchFloat64ArrayProxy(self, 22)

    @kWhStored.setter
    def kWhStored(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(22, value)

    @property
    def pctStored(self) -> BatchFloat64ArrayProxy:
        """
        Present amount of energy stored, % of rated kWh. Default is 100.

        DSS property name: `%Stored`, DSS property index: 23.
        """
        return BatchFloat64ArrayProxy(self, 23)

    @pctStored.setter
    def pctStored(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(23, value)

    @property
    def pctReserve(self) -> BatchFloat64ArrayProxy:
        """
        Percentage of rated kWh Storage capacity to be held in reserve for normal operation. Default = 20. 
        This is treated as the minimum energy discharge level unless there is an emergency. For emergency operation set this property lower. Cannot be less than zero.

        DSS property name: `%Reserve`, DSS property index: 24.
        """
        return BatchFloat64ArrayProxy(self, 24)

    @pctReserve.setter
    def pctReserve(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(24, value)

    @property
    def State(self) -> BatchInt32ArrayProxy:
        """
        {IDLING | CHARGING | DISCHARGING}  Get/Set present operational state. In DISCHARGING mode, the Storage element acts as a generator and the kW property is positive. The element continues discharging at the scheduled output power level until the Storage reaches the reserve value. Then the state reverts to IDLING. In the CHARGING state, the Storage element behaves like a Load and the kW property is negative. The element continues to charge until the max Storage kWh is reached and then switches to IDLING state. In IDLING state, the element draws the idling losses plus the associated inverter losses.

        DSS property name: `State`, DSS property index: 25.
        """
        return BatchInt32ArrayProxy(self, 25)

    @State.setter
    def State(self, value: Union[AnyStr, int, enums.StorageState, List[AnyStr], List[int], List[enums.StorageState], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(25, value)
            return
    
        self._set_batch_int32_array(25, value)

    @property
    def State_str(self) -> str:
        """
        {IDLING | CHARGING | DISCHARGING}  Get/Set present operational state. In DISCHARGING mode, the Storage element acts as a generator and the kW property is positive. The element continues discharging at the scheduled output power level until the Storage reaches the reserve value. Then the state reverts to IDLING. In the CHARGING state, the Storage element behaves like a Load and the kW property is negative. The element continues to charge until the max Storage kWh is reached and then switches to IDLING state. In IDLING state, the element draws the idling losses plus the associated inverter losses.

        DSS property name: `State`, DSS property index: 25.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 25)

    @State_str.setter
    def State_str(self, value: AnyStr):
        self.State = value

    @property
    def pctDischarge(self) -> BatchFloat64ArrayProxy:
        """
        Discharge rate (output power) in percentage of rated kW. Default = 100.

        DSS property name: `%Discharge`, DSS property index: 26.
        """
        return BatchFloat64ArrayProxy(self, 26)

    @pctDischarge.setter
    def pctDischarge(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(26, value)

    @property
    def pctCharge(self) -> BatchFloat64ArrayProxy:
        """
        Charging rate (input power) in percentage of rated kW. Default = 100.

        DSS property name: `%Charge`, DSS property index: 27.
        """
        return BatchFloat64ArrayProxy(self, 27)

    @pctCharge.setter
    def pctCharge(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(27, value)

    @property
    def pctEffCharge(self) -> BatchFloat64ArrayProxy:
        """
        Percentage efficiency for CHARGING the Storage element. Default = 90.

        DSS property name: `%EffCharge`, DSS property index: 28.
        """
        return BatchFloat64ArrayProxy(self, 28)

    @pctEffCharge.setter
    def pctEffCharge(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(28, value)

    @property
    def pctEffDischarge(self) -> BatchFloat64ArrayProxy:
        """
        Percentage efficiency for DISCHARGING the Storage element. Default = 90.

        DSS property name: `%EffDischarge`, DSS property index: 29.
        """
        return BatchFloat64ArrayProxy(self, 29)

    @pctEffDischarge.setter
    def pctEffDischarge(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(29, value)

    @property
    def pctIdlingkW(self) -> BatchFloat64ArrayProxy:
        """
        Percentage of rated kW consumed by idling losses. Default = 1.

        DSS property name: `%IdlingkW`, DSS property index: 30.
        """
        return BatchFloat64ArrayProxy(self, 30)

    @pctIdlingkW.setter
    def pctIdlingkW(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(30, value)

    @property
    def pctR(self) -> BatchFloat64ArrayProxy:
        """
        Equivalent percentage internal resistance, ohms. Default is 0. Placed in series with internal voltage source for harmonics and dynamics modes. Use a combination of %IdlingkW, %EffCharge and %EffDischarge to account for losses in power flow modes.

        DSS property name: `%R`, DSS property index: 32.
        """
        return BatchFloat64ArrayProxy(self, 32)

    @pctR.setter
    def pctR(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(32, value)

    @property
    def pctX(self) -> BatchFloat64ArrayProxy:
        """
        Equivalent percentage internal reactance, ohms. Default is 50%. Placed in series with internal voltage source for harmonics and dynamics modes. (Limits fault current to 2 pu.

        DSS property name: `%X`, DSS property index: 33.
        """
        return BatchFloat64ArrayProxy(self, 33)

    @pctX.setter
    def pctX(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(33, value)

    @property
    def Model(self) -> BatchInt32ArrayProxy:
        """
        Integer code (default=1) for the model to be used for power output variation with voltage. Valid values are:

        1:Storage element injects/absorbs a CONSTANT power.
        2:Storage element is modeled as a CONSTANT IMPEDANCE.
        3:Compute load injection from User-written Model.

        DSS property name: `Model`, DSS property index: 34.
        """
        return BatchInt32ArrayProxy(self, 34)

    @Model.setter
    def Model(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(34, value)

    @property
    def VMinpu(self) -> BatchFloat64ArrayProxy:
        """
        Default = 0.90.  Minimum per unit voltage for which the Model is assumed to apply. Below this value, the load model reverts to a constant impedance model.

        DSS property name: `VMinpu`, DSS property index: 35.
        """
        return BatchFloat64ArrayProxy(self, 35)

    @VMinpu.setter
    def VMinpu(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(35, value)

    @property
    def VMaxpu(self) -> BatchFloat64ArrayProxy:
        """
        Default = 1.10.  Maximum per unit voltage for which the Model is assumed to apply. Above this value, the load model reverts to a constant impedance model.

        DSS property name: `VMaxpu`, DSS property index: 36.
        """
        return BatchFloat64ArrayProxy(self, 36)

    @VMaxpu.setter
    def VMaxpu(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(36, value)

    @property
    def Balanced(self) -> List[bool]:
        """
        {Yes | No*} Default is No. Force balanced current only for 3-phase Storage. Forces zero- and negative-sequence to zero. 

        DSS property name: `Balanced`, DSS property index: 37.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 37)
        ]
    @Balanced.setter
    def Balanced(self, value: bool):
        self._set_batch_int32_array(37, value)

    @property
    def LimitCurrent(self) -> List[bool]:
        """
        Limits current magnitude to Vminpu value for both 1-phase and 3-phase Storage similar to Generator Model 7. For 3-phase, limits the positive-sequence current but not the negative-sequence.

        DSS property name: `LimitCurrent`, DSS property index: 38.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 38)
        ]
    @LimitCurrent.setter
    def LimitCurrent(self, value: bool):
        self._set_batch_int32_array(38, value)

    @property
    def Yearly(self) -> List[str]:
        """
        Dispatch shape to use for yearly simulations.  Must be previously defined as a Loadshape object. If this is not specified, the Daily dispatch shape, if any, is repeated during Yearly solution modes. In the default dispatch mode, the Storage element uses this loadshape to trigger State changes.

        DSS property name: `Yearly`, DSS property index: 39.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 39)

    @Yearly.setter
    def Yearly(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]):
        self._set_batch_obj_prop(39, value)

    @property
    def Yearly_obj(self) -> List[LoadShape]:
        """
        Dispatch shape to use for yearly simulations.  Must be previously defined as a Loadshape object. If this is not specified, the Daily dispatch shape, if any, is repeated during Yearly solution modes. In the default dispatch mode, the Storage element uses this loadshape to trigger State changes.

        DSS property name: `Yearly`, DSS property index: 39.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 39)

    @Yearly_obj.setter
    def Yearly_obj(self, value: LoadShape):
        self._set_batch_string(39, value)

    @property
    def Daily(self) -> List[str]:
        """
        Dispatch shape to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically.  In the default dispatch mode, the Storage element uses this loadshape to trigger State changes.

        DSS property name: `Daily`, DSS property index: 40.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 40)

    @Daily.setter
    def Daily(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]):
        self._set_batch_obj_prop(40, value)

    @property
    def Daily_obj(self) -> List[LoadShape]:
        """
        Dispatch shape to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically.  In the default dispatch mode, the Storage element uses this loadshape to trigger State changes.

        DSS property name: `Daily`, DSS property index: 40.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 40)

    @Daily_obj.setter
    def Daily_obj(self, value: LoadShape):
        self._set_batch_string(40, value)

    @property
    def Duty(self) -> List[str]:
        """
        Load shape to use for duty cycle dispatch simulations such as for solar ramp rate studies. Must be previously defined as a Loadshape object. 

        Typically would have time intervals of 1-5 seconds. 

        Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.

        DSS property name: `Duty`, DSS property index: 41.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 41)

    @Duty.setter
    def Duty(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]):
        self._set_batch_obj_prop(41, value)

    @property
    def Duty_obj(self) -> List[LoadShape]:
        """
        Load shape to use for duty cycle dispatch simulations such as for solar ramp rate studies. Must be previously defined as a Loadshape object. 

        Typically would have time intervals of 1-5 seconds. 

        Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.

        DSS property name: `Duty`, DSS property index: 41.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 41)

    @Duty_obj.setter
    def Duty_obj(self, value: LoadShape):
        self._set_batch_string(41, value)

    @property
    def DispMode(self) -> BatchInt32ArrayProxy:
        """
        {DEFAULT | FOLLOW | EXTERNAL | LOADLEVEL | PRICE } Default = "DEFAULT". Dispatch mode. 

        In DEFAULT mode, Storage element state is triggered to discharge or charge at the specified rate by the loadshape curve corresponding to the solution mode. 

        In FOLLOW mode the kW output of the Storage element follows the active loadshape multiplier until Storage is either exhausted or full. The element discharges for positive values and charges for negative values.  The loadshape is based on rated kW. 

        In EXTERNAL mode, Storage element state is controlled by an external Storagecontroller. This mode is automatically set if this Storage element is included in the element list of a StorageController element. 

        For the other two dispatch modes, the Storage element state is controlled by either the global default Loadlevel value or the price level. 

        DSS property name: `DispMode`, DSS property index: 42.
        """
        return BatchInt32ArrayProxy(self, 42)

    @DispMode.setter
    def DispMode(self, value: Union[AnyStr, int, enums.StorageDispatchMode, List[AnyStr], List[int], List[enums.StorageDispatchMode], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(42, value)
            return
    
        self._set_batch_int32_array(42, value)

    @property
    def DispMode_str(self) -> str:
        """
        {DEFAULT | FOLLOW | EXTERNAL | LOADLEVEL | PRICE } Default = "DEFAULT". Dispatch mode. 

        In DEFAULT mode, Storage element state is triggered to discharge or charge at the specified rate by the loadshape curve corresponding to the solution mode. 

        In FOLLOW mode the kW output of the Storage element follows the active loadshape multiplier until Storage is either exhausted or full. The element discharges for positive values and charges for negative values.  The loadshape is based on rated kW. 

        In EXTERNAL mode, Storage element state is controlled by an external Storagecontroller. This mode is automatically set if this Storage element is included in the element list of a StorageController element. 

        For the other two dispatch modes, the Storage element state is controlled by either the global default Loadlevel value or the price level. 

        DSS property name: `DispMode`, DSS property index: 42.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 42)

    @DispMode_str.setter
    def DispMode_str(self, value: AnyStr):
        self.DispMode = value

    @property
    def DischargeTrigger(self) -> BatchFloat64ArrayProxy:
        """
        Dispatch trigger value for discharging the Storage. 
        If = 0.0 the Storage element state is changed by the State command or by a StorageController object. 
        If <> 0  the Storage element state is set to DISCHARGING when this trigger level is EXCEEDED by either the specified Loadshape curve value or the price signal or global Loadlevel value, depending on dispatch mode. See State property.

        DSS property name: `DischargeTrigger`, DSS property index: 43.
        """
        return BatchFloat64ArrayProxy(self, 43)

    @DischargeTrigger.setter
    def DischargeTrigger(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(43, value)

    @property
    def ChargeTrigger(self) -> BatchFloat64ArrayProxy:
        """
        Dispatch trigger value for charging the Storage. 

        If = 0.0 the Storage element state is changed by the State command or StorageController object.  

        If <> 0  the Storage element state is set to CHARGING when this trigger level is GREATER than either the specified Loadshape curve value or the price signal or global Loadlevel value, depending on dispatch mode. See State property.

        DSS property name: `ChargeTrigger`, DSS property index: 44.
        """
        return BatchFloat64ArrayProxy(self, 44)

    @ChargeTrigger.setter
    def ChargeTrigger(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(44, value)

    @property
    def TimeChargeTrig(self) -> BatchFloat64ArrayProxy:
        """
        Time of day in fractional hours (0230 = 2.5) at which Storage element will automatically go into charge state. Default is 2.0.  Enter a negative time value to disable this feature.

        DSS property name: `TimeChargeTrig`, DSS property index: 45.
        """
        return BatchFloat64ArrayProxy(self, 45)

    @TimeChargeTrig.setter
    def TimeChargeTrig(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(45, value)

    @property
    def Class(self) -> BatchInt32ArrayProxy:
        """
        An arbitrary integer number representing the class of Storage element so that Storage values may be segregated by class.

        DSS property name: `Class`, DSS property index: 46.
        """
        return BatchInt32ArrayProxy(self, 46)

    @Class.setter
    def Class(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(46, value)

    @property
    def DynaDLL(self) -> List[str]:
        """
        Name of DLL containing user-written dynamics model, which computes the terminal currents for Dynamics-mode simulations, overriding the default model.  Set to "none" to negate previous setting. This DLL has a simpler interface than the UserModel DLL and is only used for Dynamics mode.

        DSS property name: `DynaDLL`, DSS property index: 47.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 47) 

    @DynaDLL.setter
    def DynaDLL(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(47, value)

    @property
    def DynaData(self) -> List[str]:
        """
        String (in quotes or parentheses if necessary) that gets passed to the user-written dynamics model Edit function for defining the data required for that model.

        DSS property name: `DynaData`, DSS property index: 48.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 48) 

    @DynaData.setter
    def DynaData(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(48, value)

    @property
    def UserModel(self) -> List[str]:
        """
        Name of DLL containing user-written model, which computes the terminal currents for both power flow and dynamics, overriding the default model.  Set to "none" to negate previous setting.

        DSS property name: `UserModel`, DSS property index: 49.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 49) 

    @UserModel.setter
    def UserModel(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(49, value)

    @property
    def UserData(self) -> List[str]:
        """
        String (in quotes or parentheses) that gets passed to user-written model for defining the data required for that model.

        DSS property name: `UserData`, DSS property index: 50.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 50) 

    @UserData.setter
    def UserData(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(50, value)

    @property
    def DebugTrace(self) -> List[bool]:
        """
        {Yes | No }  Default is no.  Turn this on to capture the progress of the Storage model for each iteration.  Creates a separate file for each Storage element named "Storage_name.csv".

        DSS property name: `DebugTrace`, DSS property index: 51.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 51)
        ]
    @DebugTrace.setter
    def DebugTrace(self, value: bool):
        self._set_batch_int32_array(51, value)

    @property
    def kVDC(self) -> BatchFloat64ArrayProxy:
        """
        Indicates the rated voltage (kV) at the input of the inverter while the storage is discharging. The value is normally greater or equal to the kV base of the Storage device. It is used for dynamics simulation ONLY.

        DSS property name: `kVDC`, DSS property index: 52.
        """
        return BatchFloat64ArrayProxy(self, 52)

    @kVDC.setter
    def kVDC(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(52, value)

    @property
    def Kp(self) -> BatchFloat64ArrayProxy:
        """
        It is the proportional gain for the PI controller within the inverter. Use it to modify the controller response in dynamics simulation mode.

        DSS property name: `Kp`, DSS property index: 53.
        """
        return BatchFloat64ArrayProxy(self, 53)

    @Kp.setter
    def Kp(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(53, value)

    @property
    def PITol(self) -> BatchFloat64ArrayProxy:
        """
        It is the tolerance (%) for the closed loop controller of the inverter. For dynamics simulation mode.

        DSS property name: `PITol`, DSS property index: 54.
        """
        return BatchFloat64ArrayProxy(self, 54)

    @PITol.setter
    def PITol(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(54, value)

    @property
    def SafeVoltage(self) -> BatchFloat64ArrayProxy:
        """
        Indicates the voltage level (%) respect to the base voltage level for which the Inverter will operate. If this threshold is violated, the Inverter will enter safe mode (OFF). For dynamic simulation. By default is 80%.

        DSS property name: `SafeVoltage`, DSS property index: 55.
        """
        return BatchFloat64ArrayProxy(self, 55)

    @SafeVoltage.setter
    def SafeVoltage(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(55, value)

    @property
    def SafeMode(self) -> List[bool]:
        """
        (Read only) Indicates whether the inverter entered (Yes) or not (No) into Safe Mode.

        DSS property name: `SafeMode`, DSS property index: 56.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 56)
        ]
    @SafeMode.setter
    def SafeMode(self, value: bool):
        self._set_batch_int32_array(56, value)

    @property
    def DynamicEq(self) -> List[str]:
        """
        The name of the dynamic equation (DynamicExp) that will be used for defining the dynamic behavior of the generator. If not defined, the generator dynamics will follow the built-in dynamic equation.

        DSS property name: `DynamicEq`, DSS property index: 57.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 57)

    @DynamicEq.setter
    def DynamicEq(self, value: Union[AnyStr, DynamicExp, List[AnyStr], List[DynamicExp]]):
        self._set_batch_obj_prop(57, value)

    @property
    def DynamicEq_obj(self) -> List[DynamicExp]:
        """
        The name of the dynamic equation (DynamicExp) that will be used for defining the dynamic behavior of the generator. If not defined, the generator dynamics will follow the built-in dynamic equation.

        DSS property name: `DynamicEq`, DSS property index: 57.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 57)

    @DynamicEq_obj.setter
    def DynamicEq_obj(self, value: DynamicExp):
        self._set_batch_string(57, value)

    @property
    def DynOut(self) -> List[str]:
        """
        The name of the variables within the Dynamic equation that will be used to govern the Storage dynamics. This Storage model requires 1 output from the dynamic equation:

            1. Current.

        The output variables need to be defined in the same order.

        DSS property name: `DynOut`, DSS property index: 58.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 58) 

    @DynOut.setter
    def DynOut(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(58, value)

    @property
    def ControlMode(self) -> BatchInt32ArrayProxy:
        """
        Defines the control mode for the inverter. It can be one of {GFM | GFL*}. By default it is GFL (Grid Following Inverter). Use GFM (Grid Forming Inverter) for energizing islanded microgrids, but, if the device is connected to the grid, it is highly recommended to use GFL.

        GFM control mode disables any control action set by the InvControl device.

        DSS property name: `ControlMode`, DSS property index: 59.
        """
        return BatchInt32ArrayProxy(self, 59)

    @ControlMode.setter
    def ControlMode(self, value: Union[AnyStr, int, enums.InverterControlMode, List[AnyStr], List[int], List[enums.InverterControlMode], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(59, value)
            return
    
        self._set_batch_int32_array(59, value)

    @property
    def ControlMode_str(self) -> str:
        """
        Defines the control mode for the inverter. It can be one of {GFM | GFL*}. By default it is GFL (Grid Following Inverter). Use GFM (Grid Forming Inverter) for energizing islanded microgrids, but, if the device is connected to the grid, it is highly recommended to use GFL.

        GFM control mode disables any control action set by the InvControl device.

        DSS property name: `ControlMode`, DSS property index: 59.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 59)

    @ControlMode_str.setter
    def ControlMode_str(self, value: AnyStr):
        self.ControlMode = value

    @property
    def AmpLimit(self) -> BatchFloat64ArrayProxy:
        """
        The current limiter per phase for the IBR when operating in GFM mode. This limit is imposed to prevent the IBR to enter into Safe Mode when reaching the IBR power ratings.
        Once the IBR reaches this value, it remains there without moving into Safe Mode. This value needs to be set lower than the IBR Amps rating.

        DSS property name: `AmpLimit`, DSS property index: 60.
        """
        return BatchFloat64ArrayProxy(self, 60)

    @AmpLimit.setter
    def AmpLimit(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(60, value)

    @property
    def AmpLimitGain(self) -> BatchFloat64ArrayProxy:
        """
        Use it for fine tunning the current limiter when active, by default is 0.8, it has to be a value between 0.1 and 1. This value allows users to fine tune the IBRs current limiter to match with the user requirements.

        DSS property name: `AmpLimitGain`, DSS property index: 61.
        """
        return BatchFloat64ArrayProxy(self, 61)

    @AmpLimitGain.setter
    def AmpLimitGain(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(61, value)

    @property
    def Spectrum(self) -> List[str]:
        """
        Name of harmonic voltage or current spectrum for this Storage element. Current injection is assumed for inverter. Default value is "default", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 62.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 62)

    @Spectrum.setter
    def Spectrum(self, value: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]]):
        self._set_batch_obj_prop(62, value)

    @property
    def Spectrum_obj(self) -> List[SpectrumObj]:
        """
        Name of harmonic voltage or current spectrum for this Storage element. Current injection is assumed for inverter. Default value is "default", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 62.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 62)

    @Spectrum_obj.setter
    def Spectrum_obj(self, value: SpectrumObj):
        self._set_batch_string(62, value)

    @property
    def BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 63.
        """
        return BatchFloat64ArrayProxy(self, 63)

    @BaseFreq.setter
    def BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(63, value)

    @property
    def Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 64.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 64)
        ]
    @Enabled.setter
    def Enabled(self, value: bool):
        self._set_batch_int32_array(64, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 65.
        """
        self._set_batch_string(65, value)

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

class IStorage(IDSSObj):
    def __init__(self, iobj):
        super().__init__(iobj, Storage, StorageBatch)

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Storage:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[StorageProperties]) -> Storage:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[StorageBatchProperties]) -> StorageBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
