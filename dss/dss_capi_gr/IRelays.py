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
