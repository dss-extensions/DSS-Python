'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira
Copyright (c) 2018-2022 DSS Extensions contributors
'''
from .._cffi_api_util import Iterable

class IRelays(Iterable):
    __slots__ = []

    _columns = [
        'Name',
        'idx',
        'MonitoredObj',
        'MonitoredTerm',
        'SwitchedObj',
        'SwitchedTerm',
        'State',
        'NormalState'
    ]

    @property
    def MonitoredObj(self):
        '''Full name of object this Relay is monitoring.'''
        return self._get_string(self.CheckForError(self._lib.Relays_Get_MonitoredObj()))

    @MonitoredObj.setter
    def MonitoredObj(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Relays_Set_MonitoredObj(Value))

    @property
    def MonitoredTerm(self):
        '''Number of terminal of monitored element that this Relay is monitoring.'''
        return self.CheckForError(self._lib.Relays_Get_MonitoredTerm())

    @MonitoredTerm.setter
    def MonitoredTerm(self, Value):
        self.CheckForError(self._lib.Relays_Set_MonitoredTerm(Value))

    @property
    def SwitchedObj(self):
        '''Full name of element that will be switched when relay trips.'''
        return self._get_string(self.CheckForError(self._lib.Relays_Get_SwitchedObj()))

    @SwitchedObj.setter
    def SwitchedObj(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Relays_Set_SwitchedObj(Value))

    @property
    def SwitchedTerm(self):
        '''Terminal number of the switched object that will be opened when the relay trips.'''
        return self.CheckForError(self._lib.Relays_Get_SwitchedTerm())

    @SwitchedTerm.setter
    def SwitchedTerm(self, Value):
        self.CheckForError(self._lib.Relays_Set_SwitchedTerm(Value))

    def Open(self):
        '''Open relay's controlled element and lock out the relay.'''
        self.CheckForError(self._lib.Relays_Open())

    def Close(self):
        '''Close the switched object controlled by the relay. Resets relay to first operation.'''
        self.CheckForError(self._lib.Relays_Close())

    def Reset(self):
        '''
        Reset relay to normal state. 
        If open, lock out the relay. 
        If closed, resets relay to first operation.
        '''
        self.CheckForError(self._lib.Relays_Reset())

    @property
    def State(self):
        '''
        Get/Set present state of relay. 
        If set to open, open relay's controlled element and lock out the relay. 
        If set to close, close relay's controlled element and resets relay to first operation.
        '''
        return self.CheckForError(self._lib.Relays_Get_State())

    @State.setter
    def State(self, Value):
        self.CheckForError(self._lib.Relays_Set_State(Value))

    @property
    def NormalState(self):
        '''Normal state of relay.'''
        return self.CheckForError(self._lib.Relays_Get_NormalState())

    @NormalState.setter
    def NormalState(self, Value):
        self.CheckForError(self._lib.Relays_Set_NormalState(Value))
