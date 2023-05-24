'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2023 Paulo Meira

Copyright (c) 2018-2023 DSS-Extensions contributors
'''
from ._cffi_api_util import Iterable

class IISources(Iterable):
    __slots__ = []
    _is_circuit_element = True

    _columns = [
        'Name',
        'idx',
        'Amps',
        'AngleDeg',
        'Frequency',
    ]

    @property
    def Amps(self) -> float:
        '''Magnitude of the ISource in amps'''
        return self.CheckForError(self._lib.ISources_Get_Amps())

    @Amps.setter
    def Amps(self, Value: float):
        self.CheckForError(self._lib.ISources_Set_Amps(Value))
 
    @property
    def AngleDeg(self) -> float:
        '''Phase angle for ISource, degrees'''
        return self.CheckForError(self._lib.ISources_Get_AngleDeg())

    @AngleDeg.setter
    def AngleDeg(self, Value: float):
        self.CheckForError(self._lib.ISources_Set_AngleDeg(Value))
 
    @property
    def Frequency(self) -> float:
        '''The present frequency of the ISource, Hz'''
        return self.CheckForError(self._lib.ISources_Get_Frequency())

    @Frequency.setter
    def Frequency(self, Value: float):
        self.CheckForError(self._lib.ISources_Set_Frequency(Value))
 