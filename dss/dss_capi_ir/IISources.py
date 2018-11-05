'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class IISources(Base):
    __slots__ = []

    @property
    def AllNames(self):
        '''(read-only) Array of strings containing names of all ISOURCE elements.'''
        return self._get_string_array(self._lib.ISources_Get_AllNames)

    @property
    def Amps(self):
        '''Magnitude of the ISOURCE in amps'''
        return self._lib.ISources_Get_Amps()

    @Amps.setter
    def Amps(self, Value):
        self._lib.ISources_Set_Amps(Value)
        self.CheckForError()

    @property
    def AngleDeg(self):
        '''Phase angle for ISOURCE, degrees'''
        return self._lib.ISources_Get_AngleDeg()

    @AngleDeg.setter
    def AngleDeg(self, Value):
        self._lib.ISources_Set_AngleDeg(Value)
        self.CheckForError()

    @property
    def Count(self):
        '''(read-only) Count: Number of ISOURCE elements.'''
        return self._lib.ISources_Get_Count()

    def __len__(self):
        return self._lib.ISources_Get_Count()

    @property
    def First(self):
        '''(read-only) Set the First ISOURCE to be active; returns Zero if none.'''
        return self._lib.ISources_Get_First()

    @property
    def Frequency(self):
        '''The present frequency of the ISOURCE, Hz'''
        return self._lib.ISources_Get_Frequency()

    @Frequency.setter
    def Frequency(self, Value):
        self._lib.ISources_Set_Frequency(Value)
        self.CheckForError()

    @property
    def Name(self):
        '''
        (read) Get name of active ISOURCE
        (write) Set Active ISOURCE by name
        '''
        return self._get_string(self._lib.ISources_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.ISources_Set_Name(Value)
        self.CheckForError()

    @property
    def Next(self):
        '''(read-only) Sets the next ISOURCE element to be the active one. Returns Zero if no more.'''
        return self._lib.ISources_Get_Next()

    def __iter__(self):
        idx = self.First
        while idx != 0:
            yield self
            idx = self.Next
