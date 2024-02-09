# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Iterable
from typing import List, AnyStr

class IFuses(Iterable):
    __slots__ = []
    _is_circuit_element = True

    _columns = [
        'Name',
        'idx',
        'NumPhases',
        'MonitoredObj',
        'MonitoredTerm',
        'Delay',
        'IsBlown',
        'TCCcurve',
        'RatedCurrent',
        'SwitchedObj',
        'SwitchedTerm',
        'State',
        'NormalState',
    ]


    def Close(self):
        '''
        Close all phases of the fuse.

        Original COM help: https://opendss.epri.com/Close3.html
        '''
        self._check_for_error(self._lib.Fuses_Close())

    def IsBlown(self) -> bool:
        '''
        Current state of the fuses. TRUE if any fuse on any phase is blown. Else FALSE.

        Original COM help: https://opendss.epri.com/IsBlown.html
        '''
        return self._check_for_error(self._lib.Fuses_IsBlown()) != 0

    def Open(self):
        '''
        Manual opening of all phases of the fuse.

        Original COM help: https://opendss.epri.com/Open2.html
        '''
        self._check_for_error(self._lib.Fuses_Open())

    def Reset(self):
        '''
        Reset fuse to normal state.

        Original COM help: https://opendss.epri.com/Reset7.html
        '''
        self._check_for_error(self._lib.Fuses_Reset())

    @property
    def Delay(self) -> float:
        '''
        A fixed delay time in seconds added to the fuse blowing time determined by the TCC curve. Default is 0.
        This represents a fuse clear or other delay.

        Original COM help: https://opendss.epri.com/Delay1.html
        '''
        return self._check_for_error(self._lib.Fuses_Get_Delay())

    @Delay.setter
    def Delay(self, Value: float):
        self._check_for_error(self._lib.Fuses_Set_Delay(Value))

    @property
    def MonitoredObj(self) -> str:
        '''
        Full name of the circuit element to which the fuse is connected.

        Original COM help: https://opendss.epri.com/MonitoredObj1.html
        '''
        return self._get_string(self._check_for_error(self._lib.Fuses_Get_MonitoredObj()))

    @MonitoredObj.setter
    def MonitoredObj(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Fuses_Set_MonitoredObj(Value))

    @property
    def MonitoredTerm(self) -> int:
        '''
        Terminal number to which the fuse is connected.

        Original COM help: https://opendss.epri.com/MonitoredTerm1.html
        '''
        return self._check_for_error(self._lib.Fuses_Get_MonitoredTerm())

    @MonitoredTerm.setter
    def MonitoredTerm(self, Value: int):
        self._check_for_error(self._lib.Fuses_Set_MonitoredTerm(Value))

    @property
    def NumPhases(self) -> int:
        '''
        Number of phases, this fuse. 

        Original COM help: https://opendss.epri.com/NumPhases1.html
        '''
        return self._check_for_error(self._lib.Fuses_Get_NumPhases())

    @property
    def RatedCurrent(self) -> float:
        '''
        Multiplier or actual amps for the TCCcurve object. Defaults to 1.0. 

        Multiply current values of TCC curve by this to get actual amps.

        Original COM help: https://opendss.epri.com/RatedCurrent.html
        '''
        return self._check_for_error(self._lib.Fuses_Get_RatedCurrent())

    @RatedCurrent.setter
    def RatedCurrent(self, Value: float):
        self._check_for_error(self._lib.Fuses_Set_RatedCurrent(Value))

    @property
    def SwitchedObj(self) -> str:
        '''
        Full name of the circuit element switch that the fuse controls. 
        Defaults to the MonitoredObj.

        Original COM help: https://opendss.epri.com/SwitchedObj.html
        '''
        return self._get_string(self._check_for_error(self._lib.Fuses_Get_SwitchedObj()))

    @SwitchedObj.setter
    def SwitchedObj(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Fuses_Set_SwitchedObj(Value))

    @property
    def SwitchedTerm(self) -> int:
        '''
        Number of the terminal of the controlled element containing the switch controlled by the fuse.

        Original COM help: https://opendss.epri.com/SwitchedTerm.html
        '''
        return self._check_for_error(self._lib.Fuses_Get_SwitchedTerm())

    @SwitchedTerm.setter
    def SwitchedTerm(self, Value: int):
        self._check_for_error(self._lib.Fuses_Set_SwitchedTerm(Value))

    @property
    def TCCcurve(self) -> str:
        '''
        Name of the TCCcurve object that determines fuse blowing.

        Original COM help: https://opendss.epri.com/TCCcurve.html
        '''
        return self._get_string(self._check_for_error(self._lib.Fuses_Get_TCCcurve()))

    @TCCcurve.setter
    def TCCcurve(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Fuses_Set_TCCcurve(Value))

    @property
    def State(self) -> List[str]:
        '''
        Array of strings indicating the state of each phase of the fuse.

        Original COM help: https://opendss.epri.com/State2.html
        '''
        return self._check_for_error(self._get_string_array(self._lib.Fuses_Get_State))

    @State.setter
    def State(self, Value: List[AnyStr]):
        self._check_for_error(self._set_string_array(self._lib.Fuses_Set_State, Value))

    @property
    def NormalState(self) -> List[str]:
        '''
        Array of strings indicating the normal state of each phase of the fuse.

        Original COM help: https://opendss.epri.com/NormalState2.html
        '''
        return self._check_for_error(self._get_string_array(self._lib.Fuses_Get_NormalState))

    @NormalState.setter
    def NormalState(self, Value: List[AnyStr]):
        self._check_for_error(self._set_string_array(self._lib.Fuses_Set_NormalState, Value))
