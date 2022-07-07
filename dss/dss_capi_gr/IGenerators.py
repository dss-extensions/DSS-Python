'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira
Copyright (c) 2018-2022 DSS Extensions contributors
'''
from .._cffi_api_util import Iterable

class IGenerators(Iterable):
    __slots__ = []

    _columns = [
        'Name',
        'idx',
        'ForcedON',
        'Model',
        'Phases',
        'PF',
        'kVArated',
        'kV',
        'kW',
        'kvar',
        'Vminpu',
        'Vmaxpu',
        'RegisterNames',
        'RegisterValues',
    ]

    @property
    def ForcedON(self):
        '''Indicates whether the generator is forced ON regardles of other dispatch criteria.'''
        return self.CheckForError(self._lib.Generators_Get_ForcedON()) != 0

    @ForcedON.setter
    def ForcedON(self, Value):
        self.CheckForError(self._lib.Generators_Set_ForcedON(Value))

    @property
    def Model(self):
        '''Generator Model'''
        return self.CheckForError(self._lib.Generators_Get_Model()) #TODO: use enum

    @Model.setter
    def Model(self, Value):
        self.CheckForError(self._lib.Generators_Set_Model(Value))

    @property
    def PF(self):
        '''Power factor (pos. = producing vars). Updates kvar based on present kW value.'''
        return self.CheckForError(self._lib.Generators_Get_PF())

    @PF.setter
    def PF(self, Value):
        self.CheckForError(self._lib.Generators_Set_PF(Value))

    @property
    def Phases(self):
        '''Number of phases'''
        return self.CheckForError(self._lib.Generators_Get_Phases())

    @Phases.setter
    def Phases(self, Value):
        self.CheckForError(self._lib.Generators_Set_Phases(Value))

    @property
    def RegisterNames(self):
        '''(read-only) Array of Names of all generator energy meter registers'''
        return self.CheckForError(self._get_string_array(self._lib.Generators_Get_RegisterNames))

    @property
    def RegisterValues(self):
        '''(read-only) Array of valus in generator energy meter registers.'''
        self.CheckForError(self._lib.Generators_Get_RegisterValues_GR())
        return self._get_float64_gr_array()

    @property
    def Vmaxpu(self):
        '''Vmaxpu for generator model'''
        return self.CheckForError(self._lib.Generators_Get_Vmaxpu())

    @Vmaxpu.setter
    def Vmaxpu(self, Value):
        self.CheckForError(self._lib.Generators_Set_Vmaxpu(Value))

    @property
    def Vminpu(self):
        '''Vminpu for Generator model'''
        return self.CheckForError(self._lib.Generators_Get_Vminpu())

    @Vminpu.setter
    def Vminpu(self, Value):
        self.CheckForError(self._lib.Generators_Set_Vminpu(Value))

    @property
    def kV(self):
        '''Voltage base for the active generator, kV'''
        return self.CheckForError(self._lib.Generators_Get_kV())

    @kV.setter
    def kV(self, Value):
        self.CheckForError(self._lib.Generators_Set_kV(Value))

    @property
    def kVArated(self):
        '''kVA rating of the generator'''
        return self.CheckForError(self._lib.Generators_Get_kVArated())

    @kVArated.setter
    def kVArated(self, Value):
        self.CheckForError(self._lib.Generators_Set_kVArated(Value))

    @property
    def kW(self):
        '''kW output for the active generator. kvar is updated for current power factor.'''
        return self.CheckForError(self._lib.Generators_Get_kW())

    @kW.setter
    def kW(self, Value):
        self.CheckForError(self._lib.Generators_Set_kW(Value))

    @property
    def kvar(self):
        '''kvar output for the active generator. Updates power factor based on present kW value.'''
        return self.CheckForError(self._lib.Generators_Get_kvar())

    @kvar.setter
    def kvar(self, Value):
        self.CheckForError(self._lib.Generators_Set_kvar(Value))
