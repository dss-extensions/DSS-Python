'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2023 Paulo Meira

Copyright (c) 2018-2023 DSS-Extensions contributors
'''
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
        '''Close all phases of the fuse.'''
        self.CheckForError(self._lib.Fuses_Close())

    def IsBlown(self) -> bool:
        '''Current state of the fuses. TRUE if any fuse on any phase is blown. Else FALSE.'''
        return self.CheckForError(self._lib.Fuses_IsBlown()) != 0

    def Open(self):
        '''Manual opening of all phases of the fuse.'''
        self.CheckForError(self._lib.Fuses_Open())

    def Reset(self):
        '''Reset fuse to normal state.'''
        self.CheckForError(self._lib.Fuses_Reset())

    @property
    def Delay(self) -> float:
        '''
        A fixed delay time in seconds added to the fuse blowing time determined by the TCC curve. Default is 0.
        This represents a fuse clear or other delay.
        '''
        return self.CheckForError(self._lib.Fuses_Get_Delay())

    @Delay.setter
    def Delay(self, Value: float):
        self.CheckForError(self._lib.Fuses_Set_Delay(Value))

    @property
    def MonitoredObj(self) -> str:
        '''Full name of the circuit element to which the fuse is connected.'''
        return self._get_string(self.CheckForError(self._lib.Fuses_Get_MonitoredObj()))

    @MonitoredObj.setter
    def MonitoredObj(self, Value: AnyStr):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Fuses_Set_MonitoredObj(Value))

    @property
    def MonitoredTerm(self) -> int:
        '''Terminal number to which the fuse is connected.'''
        return self.CheckForError(self._lib.Fuses_Get_MonitoredTerm())

    @MonitoredTerm.setter
    def MonitoredTerm(self, Value: int):
        self.CheckForError(self._lib.Fuses_Set_MonitoredTerm(Value))

    @property
    def NumPhases(self) -> int:
        '''Number of phases, this fuse. '''
        return self.CheckForError(self._lib.Fuses_Get_NumPhases())

    @property
    def RatedCurrent(self) -> float:
        '''
        Multiplier or actual amps for the TCCcurve object. Defaults to 1.0. 
        Multiply current values of TCC curve by this to get actual amps.
        '''
        return self.CheckForError(self._lib.Fuses_Get_RatedCurrent())

    @RatedCurrent.setter
    def RatedCurrent(self, Value: float):
        self.CheckForError(self._lib.Fuses_Set_RatedCurrent(Value))

    @property
    def SwitchedObj(self) -> str:
        '''
        Full name of the circuit element switch that the fuse controls. 
        Defaults to the MonitoredObj.
        '''
        return self._get_string(self.CheckForError(self._lib.Fuses_Get_SwitchedObj()))

    @SwitchedObj.setter
    def SwitchedObj(self, Value: AnyStr):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Fuses_Set_SwitchedObj(Value))

    @property
    def SwitchedTerm(self) -> int:
        '''
        Number of the terminal of the controlled element containing the switch controlled by the fuse.
        '''
        return self.CheckForError(self._lib.Fuses_Get_SwitchedTerm())

    @SwitchedTerm.setter
    def SwitchedTerm(self, Value: int):
        self.CheckForError(self._lib.Fuses_Set_SwitchedTerm(Value))

    @property
    def TCCcurve(self) -> str:
        '''Name of the TCCcurve object that determines fuse blowing.'''
        return self._get_string(self.CheckForError(self._lib.Fuses_Get_TCCcurve()))

    @TCCcurve.setter
    def TCCcurve(self, Value: AnyStr):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Fuses_Set_TCCcurve(Value))

    @property
    def State(self) -> List[str]:
        '''Array of strings indicating the state of each phase of the fuse.'''
        return self.CheckForError(self._get_string_array(self._lib.Fuses_Get_State))

    @State.setter
    def State(self, Value: List[AnyStr]):
        self.CheckForError(self._set_string_array(self._lib.Fuses_Set_State, Value))

    @property
    def NormalState(self) -> List[str]:
        '''Array of strings indicating the normal state of each phase of the fuse.'''
        return self.CheckForError(self._get_string_array(self._lib.Fuses_Get_NormalState))

    @NormalState.setter
    def NormalState(self, Value: List[AnyStr]):
        self.CheckForError(self._set_string_array(self._lib.Fuses_Set_NormalState, Value))
