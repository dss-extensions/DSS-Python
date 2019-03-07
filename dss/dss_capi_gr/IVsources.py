'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2019 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Iterable

class IVsources(Iterable):
    '''Experimental API extension exposing part of the WireData objects'''

    __slots__ = []

    @property
    def AngleDeg(self):
        '''
        (read) Phase angle of first phase in degrees
        (write) phase angle in degrees
        '''
        return self._lib.Vsources_Get_AngleDeg()

    @AngleDeg.setter
    def AngleDeg(self, Value):
        self._lib.Vsources_Set_AngleDeg(Value)
        self.CheckForError()

    @property
    def BasekV(self):
        '''Source voltage in kV'''
        return self._lib.Vsources_Get_BasekV()

    @BasekV.setter
    def BasekV(self, Value):
        self._lib.Vsources_Set_BasekV(Value)
        self.CheckForError()

    @property
    def Frequency(self):
        '''Source frequency in Hz'''
        return self._lib.Vsources_Get_Frequency()

    @Frequency.setter
    def Frequency(self, Value):
        self._lib.Vsources_Set_Frequency(Value)
        self.CheckForError()

    @property
    def Phases(self):
        '''Number of phases'''
        return self._lib.Vsources_Get_Phases()

    @Phases.setter
    def Phases(self, Value):
        self._lib.Vsources_Set_Phases(Value)
        self.CheckForError()

    @property
    def pu(self):
        '''
        (read) Source pu voltage.
        (write) Per-unit value of source voltage based on kV
        '''
        return self._lib.Vsources_Get_pu()

    @pu.setter
    def pu(self, Value):
        self._lib.Vsources_Set_pu(Value)
        self.CheckForError()
