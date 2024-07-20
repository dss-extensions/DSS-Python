# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2023-2024 Paulo Meira
# Copyright (c) 2023-2024 DSS-Extensions contributors
from ._cffi_api_util import Iterable
from ._types import Float64Array
from typing import List, Union
from .enums import StorageStates

class IStorages(Iterable):
    '''Storage objects'''
    
    __slots__ = []
    _is_circuit_element = True

    _columns = [
        'Name',
        'idx',
        'RegisterNames',
        'RegisterValues',
        'puSOC',
        'State',
        'AmpLimit',
        'AmpLimitGain',
        'ChargeTrigger',
        'ControlMode',
        'DischargeTrigger',
        'EffCharge',
        'EffDischarge',
        'Kp',
        'kV',
        'kVA',
        'kvar',
        'kVDC',
        'kW',
        'kWhRated',
        'kWRated',
        'LimitCurrent',
        'PF',
        'PITol',
        'SafeMode',
        'SafeVoltage',
        'TimeChargeTrig',
        'VarFollowInverter',
    ]


    @property
    def puSOC(self) -> float:
        '''Per unit state of charge'''
        return self._lib.Storages_Get_puSOC()

    @puSOC.setter
    def puSOC(self, Value: float):
        self._lib.Storages_Set_puSOC(Value)

    @property
    def State(self) -> StorageStates:
        '''
        Get/set state: 0=Idling; 1=Discharging; -1=Charging;
        '''
        return StorageStates(self._lib.Storages_Get_State())

    @State.setter
    def State(self, Value: Union[int, StorageStates]):
        self._lib.Storages_Set_State(Value)

    @property
    def RegisterNames(self) -> List[str]:
        '''
        Array of Storage energy meter register names
        
        See also the enum `GeneratorRegisters`.
        '''
        return self._lib.Storages_Get_RegisterNames()

    @property
    def RegisterValues(self) -> Float64Array:
        '''Array of values in Storage registers.'''
        return self._lib.Storages_Get_RegisterValues_GR()

    @property
    def AmpLimit(self) -> float:
        '''
        Current limit per phase for the IBR when operating in GFM mode.
        '''
        return self._lib.Storages_Get_AmpLimit()

    @AmpLimit.setter
    def AmpLimit(self, Value: float) -> None:
        self._lib.Storages_Set_AmpLimit(Value)

    @property
    def AmpLimitGain(self) -> float:
        '''
        Use it for fine tuning the current limiter when active.
        '''
        return self._lib.Storages_Get_AmpLimitGain()

    @AmpLimitGain.setter
    def AmpLimitGain(self, Value: float) -> None:
        self._lib.Storages_Set_AmpLimitGain(Value)

    @property
    def ChargeTrigger(self) -> float:
        '''
        Dispatch trigger value for charging the Storage.
        '''
        return self._lib.Storages_Get_ChargeTrigger()

    @ChargeTrigger.setter
    def ChargeTrigger(self, Value: float) -> None:
        self._lib.Storages_Set_ChargeTrigger(Value)

    @property
    def ControlMode(self) -> int:
        '''
        Control mode for the inverter. It can be one of {GFM = 1 | GFL* = 0}.
        '''
        return self._lib.Storages_Get_ControlMode()

    @ControlMode.setter
    def ControlMode(self, Value: int) -> None:
        self._lib.Storages_Set_ControlMode(Value)

    @property
    def DischargeTrigger(self) -> float:
        '''
        Dispatch trigger value for discharging the Storage.
        '''
        return self._lib.Storages_Get_DischargeTrigger()

    @DischargeTrigger.setter
    def DischargeTrigger(self, Value: float) -> None:
        self._lib.Storages_Set_DischargeTrigger(Value)

    @property
    def EffCharge(self) -> float:
        '''
        Percentage efficiency for CHARGING the Storage element.
        '''
        return self._lib.Storages_Get_EffCharge()

    @EffCharge.setter
    def EffCharge(self, Value: float) -> None:
        self._lib.Storages_Set_EffCharge(Value)

    @property
    def EffDischarge(self) -> float:
        '''
        Percentage efficiency for DISCHARGING the Storage element.
        '''
        return self._lib.Storages_Get_EffDischarge()

    @EffDischarge.setter
    def EffDischarge(self, Value: float) -> None:
        self._lib.Storages_Set_EffDischarge(Value)

    @property
    def Kp(self) -> float:
        '''
        Proportional gain for the PI controller within the inverter.
        Use it to modify the controller response in dynamics simulation mode.
        '''
        return self._lib.Storages_Get_Kp()

    @Kp.setter
    def Kp(self, Value: float) -> None:
        self._lib.Storages_Set_Kp(Value)

    @property
    def kV(self) -> float:
        '''
        Nominal rated (1.0 per unit) voltage, kV, for Storage element.
        '''
        return self._lib.Storages_Get_kV()

    @kV.setter
    def kV(self, Value: float) -> None:
        self._lib.Storages_Set_kV(Value)

    @property
    def kVA(self) -> float:
        '''
        Inverter nameplate capability (in kVA). Used as the base for Dynamics mode and Harmonics mode values.
        '''
        return self._lib.Storages_Get_kVA()

    @kVA.setter
    def kVA(self, Value: float) -> None:
        self._lib.Storages_Set_kVA(Value)

    @property
    def kvar(self) -> float:
        '''
        Get/set the requested kvar value. Final kvar is subjected to the inverter ratings. Sets inverter to operate in constant kvar mode.
        '''
        return self._lib.Storages_Get_kvar()

    @kvar.setter
    def kvar(self, Value: float) -> None:
        self._lib.Storages_Set_kvar(Value)

    @property
    def kVDC(self) -> float:
        '''
        Rated voltage (kV) at the input of the inverter while the storage is discharging
        '''
        return self._lib.Storages_Get_kVDC()

    @kVDC.setter
    def kVDC(self, Value: float) -> None:
        self._lib.Storages_Set_kVDC(Value)

    @property
    def kW(self) -> float:
        '''
        Get/set the requested kW value. Final kW is subjected to the inverter ratings.
        '''
        return self._lib.Storages_Get_kW()

    @kW.setter
    def kW(self, Value: float) -> None:
        self._lib.Storages_Set_kW(Value)

    @property
    def kWhRated(self) -> float:
        '''
        Rated Storage capacity in kWh.
        '''
        return self._lib.Storages_Get_kWhRated()

    @kWhRated.setter
    def kWhRated(self, Value: float) -> None:
        self._lib.Storages_Set_kWhRated(Value)

    @property
    def kWRated(self) -> float:
        '''
        kW rating of power output. Base for Loadshapes when DispMode=Follow. Sets kVA property if it has not been specified yet.
        '''
        return self._lib.Storages_Get_kWRated()

    @kWRated.setter
    def kWRated(self, Value: float) -> None:
        self._lib.Storages_Set_kWRated(Value)

    @property
    def LimitCurrent(self) -> bool:
        '''
        Limits current magnitude to Vminpu value for both 1-phase and 3-phase Storage similar to Generator Model 7.
        For 3-phase, limits the positive-sequence current but not the negative-sequence."
        '''
        return self._lib.Storages_Get_LimitCurrent()

    @LimitCurrent.setter
    def LimitCurrent(self, Value: bool) -> None:
        self._lib.Storages_Set_LimitCurrent(Value)

    @property
    def PF(self) -> float:
        '''
        Get/set the requested PF value.
        '''
        return self._lib.Storages_Get_PF()

    @PF.setter
    def PF(self, Value: float) -> None:
        self._lib.Storages_Set_PF(Value)

    @property
    def PITol(self) -> float:
        '''
        Tolerance (%) for the closed loop controller of the inverter
        '''
        return self._lib.Storages_Get_PITol()

    @PITol.setter
    def PITol(self, Value: float) -> None:
        self._lib.Storages_Set_PITol(Value)

    @property
    def SafeMode(self) -> int:
        '''
        (Read only) Indicates whether the inverter entered (Yes) or not (No) into Safe Mode.
        '''
        return self._lib.Storages_Get_SafeMode()

    @property
    def SafeVoltage(self) -> float:
        '''
        Indicates the voltage level (%) respect to the base voltage level for which the Inverter will operate.
        '''
        return self._lib.Storages_Get_SafeVoltage()

    @SafeVoltage.setter
    def SafeVoltage(self, Value: float) -> None:
        self._lib.Storages_Set_SafeVoltage(Value)

    @property
    def TimeChargeTrig(self) -> float:
        '''
        Time of day in fractional hours (0230 = 2.5) at which Storage element will automatically go into charge state.
        '''
        return self._lib.Storages_Get_TimeChargeTrig()

    @TimeChargeTrig.setter
    def TimeChargeTrig(self, Value: float) -> None:
        self._lib.Storages_Set_TimeChargeTrig(Value)

    @property
    def VarFollowInverter(self) -> int:
        '''
        Indicates if the reactive power generation/absorption does not respect the inverter status
        '''
        return self._lib.Storages_Get_VarFollowInverter()

    @VarFollowInverter.setter
    def VarFollowInverter(self, Value: int) -> None:
        self._lib.Storages_Set_VarFollowInverter(Value)


