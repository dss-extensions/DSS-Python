'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira
Copyright (c) 2018-2022 DSS Extensions contributors
'''
from .._cffi_api_util import Iterable

class IVsources(Iterable):
    __slots__ = []

    _columns = [
        'Name',
        'idx',
        'Phases',
        'BasekV',
        'AngleDeg',
        'Frequency',
        'pu',
    ]

    @property
    def AngleDeg(self):
        '''Phase angle of first phase in degrees'''
        return self.CheckForError(self._lib.Vsources_Get_AngleDeg())

    @AngleDeg.setter
    def AngleDeg(self, Value):
        self.CheckForError(self._lib.Vsources_Set_AngleDeg(Value))

    @property
    def BasekV(self):
        '''Source voltage in kV'''
        return self.CheckForError(self._lib.Vsources_Get_BasekV())

    @BasekV.setter
    def BasekV(self, Value):
        self.CheckForError(self._lib.Vsources_Set_BasekV(Value))

    @property
    def Frequency(self):
        '''Source frequency in Hz'''
        return self.CheckForError(self._lib.Vsources_Get_Frequency())

    @Frequency.setter
    def Frequency(self, Value):
        self.CheckForError(self._lib.Vsources_Set_Frequency(Value))

    @property
    def Phases(self):
        '''Number of phases'''
        return self.CheckForError(self._lib.Vsources_Get_Phases())

    @Phases.setter
    def Phases(self, Value):
        self.CheckForError(self._lib.Vsources_Set_Phases(Value))

    @property
    def pu(self):
        '''Per-unit value of source voltage'''
        return self.CheckForError(self._lib.Vsources_Get_pu())

    @pu.setter
    def pu(self, Value):
        self.CheckForError(self._lib.Vsources_Set_pu(Value))
