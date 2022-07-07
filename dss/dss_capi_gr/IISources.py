'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira
Copyright (c) 2018-2022 DSS Extensions contributors
'''
from .._cffi_api_util import Iterable

class IISources(Iterable):
    __slots__ = []

    _columns = [
        'Name',
        'idx',
        'Amps',
        'AngleDeg',
        'Frequency',
    ]

    @property
    def Amps(self):
        '''Magnitude of the ISource in amps'''
        return self.CheckForError(self._lib.ISources_Get_Amps())

    @Amps.setter
    def Amps(self, Value):
        self.CheckForError(self._lib.ISources_Set_Amps(Value))
 
    @property
    def AngleDeg(self):
        '''Phase angle for ISource, degrees'''
        return self.CheckForError(self._lib.ISources_Get_AngleDeg())

    @AngleDeg.setter
    def AngleDeg(self, Value):
        self.CheckForError(self._lib.ISources_Set_AngleDeg(Value))
 
    @property
    def Frequency(self):
        '''The present frequency of the ISource, Hz'''
        return self.CheckForError(self._lib.ISources_Get_Frequency())

    @Frequency.setter
    def Frequency(self, Value):
        self.CheckForError(self._lib.ISources_Set_Frequency(Value))
 