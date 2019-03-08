'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2019 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Iterable

class IISources(Iterable):
    __slots__ = []

    @property
    def Amps(self):
        '''Magnitude of the ISource in amps'''
        return self._lib.ISources_Get_Amps()

    @Amps.setter
    def Amps(self, Value):
        self._lib.ISources_Set_Amps(Value)
        self.CheckForError()

    @property
    def AngleDeg(self):
        '''Phase angle for ISource, degrees'''
        return self._lib.ISources_Get_AngleDeg()

    @AngleDeg.setter
    def AngleDeg(self, Value):
        self._lib.ISources_Set_AngleDeg(Value)
        self.CheckForError()

    @property
    def Frequency(self):
        '''The present frequency of the ISource, Hz'''
        return self._lib.ISources_Get_Frequency()

    @Frequency.setter
    def Frequency(self, Value):
        self._lib.ISources_Set_Frequency(Value)
        self.CheckForError()
