'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2019 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Iterable

class IRelays(Iterable):
    __slots__ = []

    @property
    def MonitoredObj(self):
        '''Full name of object this Relay is monitoring.'''
        return self._get_string(self._lib.Relays_Get_MonitoredObj())

    @MonitoredObj.setter
    def MonitoredObj(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Relays_Set_MonitoredObj(Value)
        self.CheckForError()

    @property
    def MonitoredTerm(self):
        '''Number of terminal of monitored element that this Relay is monitoring.'''
        return self._lib.Relays_Get_MonitoredTerm()

    @MonitoredTerm.setter
    def MonitoredTerm(self, Value):
        self._lib.Relays_Set_MonitoredTerm(Value)
        self.CheckForError()

    @property
    def SwitchedObj(self):
        '''Full name of element that will be switched when relay trips.'''
        return self._get_string(self._lib.Relays_Get_SwitchedObj())

    @SwitchedObj.setter
    def SwitchedObj(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Relays_Set_SwitchedObj(Value)
        self.CheckForError()

    @property
    def SwitchedTerm(self):
        '''Terminal number of the switched object that will be opened when the relay trips.'''
        return self._lib.Relays_Get_SwitchedTerm()

    @SwitchedTerm.setter
    def SwitchedTerm(self, Value):
        self._lib.Relays_Set_SwitchedTerm(Value)
        self.CheckForError()
