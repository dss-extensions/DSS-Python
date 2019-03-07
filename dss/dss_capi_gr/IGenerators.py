'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2019 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Iterable

class IGenerators(Iterable):
    __slots__ = []

    @property
    def ForcedON(self):
        '''Indicates whether the generator is forced ON regardles of other dispatch criteria.'''
        return self._lib.Generators_Get_ForcedON() != 0

    @ForcedON.setter
    def ForcedON(self, Value):
        self._lib.Generators_Set_ForcedON(Value)
        self.CheckForError()

    @property
    def Model(self):
        '''Generator Model'''
        return self._lib.Generators_Get_Model()

    @Model.setter
    def Model(self, Value):
        self._lib.Generators_Set_Model(Value)
        self.CheckForError()

    @property
    def PF(self):
        '''Power factor (pos. = producing vars). Updates kvar based on present kW value.'''
        return self._lib.Generators_Get_PF()

    @PF.setter
    def PF(self, Value):
        self._lib.Generators_Set_PF(Value)
        self.CheckForError()

    @property
    def Phases(self):
        '''Number of phases'''
        return self._lib.Generators_Get_Phases()

    @Phases.setter
    def Phases(self, Value):
        self._lib.Generators_Set_Phases(Value)
        self.CheckForError()

    @property
    def RegisterNames(self):
        '''(read-only) Array of Names of all generator energy meter registers'''
        return self._get_string_array(self._lib.Generators_Get_RegisterNames)

    @property
    def RegisterValues(self):
        '''(read-only) Array of valus in generator energy meter registers.'''
        self._lib.Generators_Get_RegisterValues_GR()
        return self._get_float64_gr_array()

    @property
    def Vmaxpu(self):
        '''Vmaxpu for generator model'''
        return self._lib.Generators_Get_Vmaxpu()

    @Vmaxpu.setter
    def Vmaxpu(self, Value):
        self._lib.Generators_Set_Vmaxpu(Value)
        self.CheckForError()

    @property
    def Vminpu(self):
        '''Vminpu for Generator model'''
        return self._lib.Generators_Get_Vminpu()

    @Vminpu.setter
    def Vminpu(self, Value):
        self._lib.Generators_Set_Vminpu(Value)
        self.CheckForError()

    @property
    def kV(self):
        '''Voltage base for the active generator, kV'''
        return self._lib.Generators_Get_kV()

    @kV.setter
    def kV(self, Value):
        self._lib.Generators_Set_kV(Value)
        self.CheckForError()

    @property
    def kVArated(self):
        '''kVA rating of the generator'''
        return self._lib.Generators_Get_kVArated()

    @kVArated.setter
    def kVArated(self, Value):
        self._lib.Generators_Set_kVArated(Value)
        self.CheckForError()

    @property
    def kW(self):
        '''kW output for the active generator. kvar is updated for current power factor.'''
        return self._lib.Generators_Get_kW()

    @kW.setter
    def kW(self, Value):
        self._lib.Generators_Set_kW(Value)
        self.CheckForError()

    @property
    def kvar(self):
        '''kvar output for the active generator. Updates power factor based on present kW value.'''
        return self._lib.Generators_Get_kvar()

    @kvar.setter
    def kvar(self, Value):
        self._lib.Generators_Set_kvar(Value)
        self.CheckForError()
