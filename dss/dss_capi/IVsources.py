'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class IVsources(Base):
    __slots__ = []

    @property
    def AllNames(self):
        '''(read-only) Names of all Vsource objects in the circuit'''
        return self.get_string_array(self.lib.Vsources_Get_AllNames)

    @property
    def AngleDeg(self):
        '''
        (read) Phase angle of first phase in degrees
        (write) phase angle in degrees
        '''
        return self.lib.Vsources_Get_AngleDeg()

    @AngleDeg.setter
    def AngleDeg(self, Value):
        self.lib.Vsources_Set_AngleDeg(Value)

    @property
    def BasekV(self):
        '''Source voltage in kV'''
        return self.lib.Vsources_Get_BasekV()

    @BasekV.setter
    def BasekV(self, Value):
        self.lib.Vsources_Set_BasekV(Value)

    @property
    def Count(self):
        '''(read-only) Number of Vsource Object'''
        return self.lib.Vsources_Get_Count()

    def __len__(self):
        return self.lib.Vsources_Get_Count()

    @property
    def First(self):
        '''(read-only) Sets the first VSOURCE to be active; Returns 0 if none'''
        return self.lib.Vsources_Get_First()

    @property
    def Frequency(self):
        '''Source frequency in Hz'''
        return self.lib.Vsources_Get_Frequency()

    @Frequency.setter
    def Frequency(self, Value):
        self.lib.Vsources_Set_Frequency(Value)

    @property
    def Name(self):
        '''
        (read) Get Active VSOURCE name
        (write) Set Active VSOURCE by Name
        '''
        return self.get_string(self.lib.Vsources_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.Vsources_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Sets the next VSOURCE object to be active; returns zero if no more'''
        return self.lib.Vsources_Get_Next()

    @property
    def Phases(self):
        '''Number of phases'''
        return self.lib.Vsources_Get_Phases()

    @Phases.setter
    def Phases(self, Value):
        self.lib.Vsources_Set_Phases(Value)

    @property
    def pu(self):
        '''
        (read) Source pu voltage.
        (write) Per-unit value of source voltage based on kV
        '''
        return self.lib.Vsources_Get_pu()

    @pu.setter
    def pu(self, Value):
        self.lib.Vsources_Set_pu(Value)

    def __iter__(self):
        idx = self.First
        while idx != 0:
            yield self
            idx = self.Next

