'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2022 Paulo Meira
Copyright (c) 2022 DSS Extensions contributors
'''
from .._cffi_api_util import Iterable

class IStorages(Iterable):
    '''Storage objects'''
    
    __slots__ = []

    _columns = [
        'Name',
        'idx',
        'RegisterNames',
        'RegisterValues',
        'puSOC',
        'State',
    ]


    @property
    def puSOC(self):
        '''Per unit state of charge'''
        return self.CheckForError(self._lib.Storages_Get_puSOC())

    @puSOC.setter
    def puSOC(self, Value):
        self.CheckForError(self._lib.Storages_Set_puSOC(Value))

    @property
    def State(self):
        '''
        Get/set state: 0=Idling; 1=Discharging; -1=Charging;

        Related enumeration: StorageStates
        '''
        return self.CheckForError(self._lib.Storages_Get_State())

    @State.setter
    def State(self, Value):
        self.CheckForError(self._lib.Storages_Set_State(Value))

    @property
    def RegisterNames(self):
        '''Array of Names of all Storage energy meter registers'''
        return self.CheckForError(self._get_string_array(self._lib.Storages_Get_RegisterNames))

    @property
    def RegisterValues(self):
        '''Array of values in Storage registers.'''
        self.CheckForError(self._lib.Storages_Get_RegisterValues_GR())
        return self._get_float64_gr_array()

