'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class IGenerators(Base):
    __slots__ = []

    @property
    def AllNames(self):
        '''(read-only) Array of names of all Generator objects.'''
        return self.get_string_array(self.lib.Generators_Get_AllNames)

    @property
    def Count(self):
        '''(read-only) Number of Generator Objects in Active Circuit'''
        return self.lib.Generators_Get_Count()

    def __len__(self):
        return self.lib.Generators_Get_Count()

    @property
    def First(self):
        '''(read-only) Sets first Generator to be active.  Returns 0 if none.'''
        return self.lib.Generators_Get_First()

    @property
    def ForcedON(self):
        '''Indicates whether the generator is forced ON regardles of other dispatch criteria.'''
        return self.lib.Generators_Get_ForcedON() != 0

    @ForcedON.setter
    def ForcedON(self, Value):
        self.lib.Generators_Set_ForcedON(Value)

    @property
    def Model(self):
        '''Generator Model'''
        return self.lib.Generators_Get_Model()

    @Model.setter
    def Model(self, Value):
        self.lib.Generators_Set_Model(Value)

    @property
    def Name(self):
        '''Sets a generator active by name.'''
        return self.get_string(self.lib.Generators_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.Generators_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Sets next Generator to be active.  Returns 0 if no more.'''
        return self.lib.Generators_Get_Next()

    @property
    def PF(self):
        '''Power factor (pos. = producing vars). Updates kvar based on present kW value.'''
        return self.lib.Generators_Get_PF()

    @PF.setter
    def PF(self, Value):
        self.lib.Generators_Set_PF(Value)

    @property
    def Phases(self):
        '''Number of phases'''
        return self.lib.Generators_Get_Phases()

    @Phases.setter
    def Phases(self, Value):
        self.lib.Generators_Set_Phases(Value)

    @property
    def RegisterNames(self):
        '''(read-only) Array of Names of all generator energy meter registers'''
        return self.get_string_array(self.lib.Generators_Get_RegisterNames)

    @property
    def RegisterValues(self):
        '''(read-only) Array of valus in generator energy meter registers.'''
        self.lib.Generators_Get_RegisterValues_GR()
        return self.get_float64_gr_array()

    @property
    def Vmaxpu(self):
        '''Vmaxpu for generator model'''
        return self.lib.Generators_Get_Vmaxpu()

    @Vmaxpu.setter
    def Vmaxpu(self, Value):
        self.lib.Generators_Set_Vmaxpu(Value)

    @property
    def Vminpu(self):
        '''Vminpu for Generator model'''
        return self.lib.Generators_Get_Vminpu()

    @Vminpu.setter
    def Vminpu(self, Value):
        self.lib.Generators_Set_Vminpu(Value)

    @property
    def idx(self):
        '''Get/Set active Generator by index into generators list.  1..Count'''
        return self.lib.Generators_Get_idx()

    @idx.setter
    def idx(self, Value):
        self.lib.Generators_Set_idx(Value)

    @property
    def kV(self):
        '''Voltage base for the active generator, kV'''
        return self.lib.Generators_Get_kV()

    @kV.setter
    def kV(self, Value):
        self.lib.Generators_Set_kV(Value)

    @property
    def kVArated(self):
        '''kVA rating of the generator'''
        return self.lib.Generators_Get_kVArated()

    @kVArated.setter
    def kVArated(self, Value):
        self.lib.Generators_Set_kVArated(Value)

    @property
    def kW(self):
        '''kW output for the active generator. kvar is updated for current power factor.'''
        return self.lib.Generators_Get_kW()

    @kW.setter
    def kW(self, Value):
        self.lib.Generators_Set_kW(Value)

    @property
    def kvar(self):
        '''kvar output for the active generator. Updates power factor based on present kW value.'''
        return self.lib.Generators_Get_kvar()

    @kvar.setter
    def kvar(self, Value):
        self.lib.Generators_Set_kvar(Value)

    def __iter__(self):
        idx = self.First
        while idx != 0:
            yield self
            idx = self.Next

