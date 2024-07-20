# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2024 Paulo Meira
# Copyright (c) 2024 DSS-Extensions contributors
from ._cffi_api_util import Iterable
from ._types import Float64Array
from typing import List, Union, AnyStr
from .enums import StorageStates

class IWindGens(Iterable):
    '''WindGen objects'''
    
    __slots__ = []
    _is_circuit_element = True

    _columns = [
        'Name',
        'idx',
        'RegisterNames',
        'RegisterValues',
        'Ag',
        'Bus1',
        'Class',
        'Cp',
        'daily',
        'duty',
        'IsDelta',
        'kV',
        'kVA',
        'kvar',
        'kW',
        'Lamda',
        'N_WTG',
        'NPoles',
        'pd',
        'PF',
        'Phases',
        'PSS',
        'QFlag',
        'QMode',
        'QSS',
        'Rad',
        'RThev',
        'VCutIn',
        'VCutOut',
        'Vss',
        'WindSpeed',
        'XThev',
        'Yearly',
    ]

    @property
    def RegisterNames(self) -> List[str]:
        '''
        Array of Storage energy meter register names
        
        See also the enum `GeneratorRegisters`.
        '''
        return self._lib.WindGens_Get_RegisterNames()

    @property
    def RegisterValues(self) -> Float64Array:
        '''Array of values in Storage registers.'''
        return self._lib.WindGens_Get_RegisterValues_GR()

    @property
    def kV(self) -> float:
        '''
        Nominal rated (1.0 per unit) voltage for the active WindGen, in kV.
        '''
        return self._lib.WindGens_Get_kV()

    @kV.setter
    def kV(self, Value: float) -> None:
        self._lib.WindGens_Set_kV(Value)

    @property
    def kvar(self) -> float:
        '''
        Base kvar for the active WindGen.
        '''
        return self._lib.WindGens_Get_kvar()

    @kvar.setter
    def kvar(self, Value: float) -> None:
        self._lib.WindGens_Set_kvar(Value)

    @property
    def kW(self) -> float:
        '''
        Total base kW for the active WindGen.
        '''
        return self._lib.WindGens_Get_kW()

    @kW.setter
    def kW(self, Value: float) -> None:
        self._lib.WindGens_Set_kW(Value)

    @property
    def PF(self) -> float:
        '''
        WindGen power factor. Power factor (pos. = producing vars).
        '''
        return self._lib.WindGens_Get_PF()

    @PF.setter
    def PF(self, Value: float) -> None:
        self._lib.WindGens_Set_PF(Value)

    @property
    def kVA(self) -> float:
        '''
        KVA rating of the electrical machine in the WindGen.
        '''
        return self._lib.WindGens_Get_kVA()

    @kVA.setter
    def kVA(self, Value: float) -> None:
        self._lib.WindGens_Set_kVA(Value)

    @property
    def Ag(self) -> float:
        '''
        Gearbox ratio
        '''
        return self._lib.WindGens_Get_Ag()

    @Ag.setter
    def Ag(self, Value: float) -> None:
        self._lib.WindGens_Set_Ag(Value)

    @property
    def Cp(self) -> float:
        '''
        Turbine performance coefficient.
        '''
        return self._lib.WindGens_Get_Cp()

    @Cp.setter
    def Cp(self, Value: float) -> None:
        self._lib.WindGens_Set_Cp(Value)

    @property
    def Lamda(self) -> float:
        '''
        Tip speed ratio
        '''
        return self._lib.WindGens_Get_Lamda()

    @Lamda.setter
    def Lamda(self, Value: float) -> None:
        self._lib.WindGens_Set_Lamda(Value)

    @property
    def N_WTG(self) -> int:
        '''
        Number of WTG in aggregation
        '''
        return self._lib.WindGens_Get_N_WTG()

    @N_WTG.setter
    def N_WTG(self, Value: int) -> None:
        self._lib.WindGens_Set_N_WTG(Value)

    @property
    def NPoles(self) -> int:
        '''
        Number of pole pairs of the induction generator
        '''
        return self._lib.WindGens_Get_NPoles()

    @NPoles.setter
    def NPoles(self, Value: int) -> None:
        self._lib.WindGens_Set_NPoles(Value)

    @property
    def pd(self) -> float:
        '''
        Air density in kg/m3
        '''
        return self._lib.WindGens_Get_pd()

    @pd.setter
    def pd(self, Value: float) -> None:
        self._lib.WindGens_Set_pd(Value)

    @property
    def PSS(self) -> float:
        '''
        Steady state output real power.
        '''
        return self._lib.WindGens_Get_PSS()

    @PSS.setter
    def PSS(self, Value: float) -> None:
        self._lib.WindGens_Set_PSS(Value)

    @property
    def QFlag(self) -> int:
        '''
        Non-zero values enable reactive power and voltage control in the dynamic model.
        '''
        return self._lib.WindGens_Get_QFlag()

    @QFlag.setter
    def QFlag(self, Value: int) -> None:
        self._lib.WindGens_Set_QFlag(Value)

    @property
    def QMode(self) -> int:
        '''
        Q control mode (0:Q, 1:PF, 2:VV).
        '''
        return self._lib.WindGens_Get_QMode()

    @QMode.setter
    def QMode(self, Value: int) -> None:
        self._lib.WindGens_Set_QMode(Value)

    @property
    def QSS(self) -> float:
        '''
        Steady state output reactive power.
        '''
        return self._lib.WindGens_Get_QSS()

    @QSS.setter
    def QSS(self, Value: float) -> None:
        self._lib.WindGens_Set_QSS(Value)

    @property
    def Rad(self) -> float:
        '''
        Rotor radius in meters
        '''
        return self._lib.WindGens_Get_Rad()

    @Rad.setter
    def Rad(self, Value: float) -> None:
        self._lib.WindGens_Set_Rad(Value)

    @property
    def RThev(self) -> float:
        '''
        Per unit Thevenin equivalent resistance (R).
        '''
        return self._lib.WindGens_Get_RThev()

    @RThev.setter
    def RThev(self, Value: float) -> None:
        self._lib.WindGens_Set_RThev(Value)

    @property
    def VCutIn(self) -> float:
        '''
        Cut-in speed for the wind generator
        '''
        return self._lib.WindGens_Get_VCutIn()

    @VCutIn.setter
    def VCutIn(self, Value: float) -> None:
        self._lib.WindGens_Set_VCutIn(Value)

    @property
    def VCutOut(self) -> float:
        '''
        Cut-out speed for the wind generator
        '''
        return self._lib.WindGens_Get_VCutOut()

    @VCutOut.setter
    def VCutOut(self, Value: float) -> None:
        self._lib.WindGens_Set_VCutOut(Value)

    @property
    def Vss(self) -> float:
        '''
        Steady state voltage magnitude.
        '''
        return self._lib.WindGens_Get_Vss()

    @Vss.setter
    def Vss(self, Value: float) -> None:
        self._lib.WindGens_Set_Vss(Value)

    @property
    def WindSpeed(self) -> float:
        '''
        Wind speed in m/s
        '''
        return self._lib.WindGens_Get_WindSpeed()

    @WindSpeed.setter
    def WindSpeed(self, Value: float) -> None:
        self._lib.WindGens_Set_WindSpeed(Value)

    @property
    def XThev(self) -> float:
        '''
        Per unit Thevenin equivalent reactance (X).
        '''
        return self._lib.WindGens_Get_XThev()

    @XThev.setter
    def XThev(self, Value: float) -> None:
        self._lib.WindGens_Set_XThev(Value)

    @property
    def Phases(self) -> int:
        '''
        Number of phases

        (API Extension)
        '''
        return self._lib.WindGens_Get_Phases()

    @Phases.setter
    def Phases(self, Value: int) -> None:
        '''
        Number of phases

        (API Extension)
        '''
        self._lib.WindGens_Set_Phases(Value)

    @property
    def daily(self) -> str:
        '''
        Name of the loadshape for daily wind speed

        (API Extension)
        '''
        return self._lib.WindGens_Get_daily()

    @daily.setter
    def daily(self, Value: AnyStr) -> None:
        self._lib.WindGens_Set_daily(Value)

    @property
    def duty(self) -> str:
        '''
        Name of the loadshape for a duty cycle simulation.

        (API Extension)
        '''
        return self._lib.WindGens_Get_duty()

    @duty.setter
    def duty(self, Value: AnyStr) -> None:
        self._lib.WindGens_Set_duty(Value)

    @property
    def Yearly(self) -> str:
        '''
        Name of yearly loadshape

        (API Extension)
        '''
        return self._lib.WindGens_Get_Yearly()

    @Yearly.setter
    def Yearly(self, Value: AnyStr) -> None:
        self._lib.WindGens_Set_Yearly(Value)

    @property
    def IsDelta(self) -> bool:
        '''
        WindGen connection. True/1 if delta connection, False/0 if wye.

        (API Extension)
        '''
        return self._lib.WindGens_Get_IsDelta()

    @IsDelta.setter
    def IsDelta(self, Value: bool) -> None:
        self._lib.WindGens_Set_IsDelta(Value)

    @property
    def Class(self) -> int:
        '''
        An arbitrary integer number representing the class of WindGen so that WindGen values may be segregated by class.

        (API Extension)
        '''
        return self._lib.WindGens_Get_Class_()

    @Class.setter
    def Class(self, Value: int) -> None:
        self._lib.WindGens_Set_Class_(Value)

    @property
    def Bus1(self) -> str:
        '''
        Bus to which the WindGen is connected. May include specific node specification.

        (API Extension)
        '''
        return self._lib.WindGens_Get_Bus1()

    @Bus1.setter
    def Bus1(self, Value: AnyStr):
        self._lib.WindGens_Set_Bus1(Value)
