'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class IRelays(Base):
    __slots__ = []

    @property
    def AllNames(self):
        '''(read-only) Array of strings containing names of all Relay elements'''
        return self._get_string_array(self._lib.Relays_Get_AllNames)

    @property
    def Count(self):
        '''(read-only) Number of Relays in circuit'''
        return self._lib.Relays_Get_Count()

    def __len__(self):
        return self._lib.Relays_Get_Count()

    @property
    def First(self):
        '''(read-only) Set First Relay active. If none, returns 0.'''
        return self._lib.Relays_Get_First()

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
    def Name(self):
        '''
        (read) Get name of active relay.
        (write) Set Relay active by name
        '''
        return self._get_string(self._lib.Relays_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Relays_Set_Name(Value)
        self.CheckForError()

    @property
    def Next(self):
        '''(read-only) Advance to next Relay object. Returns 0 when no more relays.'''
        return self._lib.Relays_Get_Next()

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

    @property
    def idx(self):
        '''
        (read) Get/Set active Relay by index into the Relay list. 1..Count
        (write) Get/Set Relay active by index into relay list. 1..Count
        '''
        return self._lib.Relays_Get_idx()

    @idx.setter
    def idx(self, Value):
        self._lib.Relays_Set_idx(Value)
        self.CheckForError()

    def __iter__(self):
        idx = self.First
        while idx != 0:
            yield self
            idx = self.Next

