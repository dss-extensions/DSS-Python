# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2023-2024 Paulo Meira
# Copyright (c) 2023-2024 DSS-Extensions contributors
from ._cffi_api_util import Iterable
from ._types import Float64Array
from typing import List, Union
from .enums import StorageStates

class IStorages(Iterable):
    '''Storage objects'''
    
    __slots__ = []
    _is_circuit_element = True

    _columns = [
        'Name',
        'idx',
        'RegisterNames',
        'RegisterValues',
        'puSOC',
        'State',
    ]


    @property
    def puSOC(self) -> float:
        '''Per unit state of charge'''
        return self._check_for_error(self._lib.Storages_Get_puSOC())

    @puSOC.setter
    def puSOC(self, Value: float):
        self._check_for_error(self._lib.Storages_Set_puSOC(Value))

    @property
    def State(self) -> StorageStates:
        '''
        Get/set state: 0=Idling; 1=Discharging; -1=Charging;
        '''
        return StorageStates(self._check_for_error(self._lib.Storages_Get_State()))

    @State.setter
    def State(self, Value: Union[int, StorageStates]):
        self._check_for_error(self._lib.Storages_Set_State(Value))

    @property
    def RegisterNames(self) -> List[str]:
        '''
        Array of Storage energy meter register names
        
        See also the enum `GeneratorRegisters`.
        '''
        return self._check_for_error(self._get_string_array(self._lib.Storages_Get_RegisterNames))

    @property
    def RegisterValues(self) -> Float64Array:
        '''Array of values in Storage registers.'''
        self._check_for_error(self._lib.Storages_Get_RegisterValues_GR())
        return self._get_float64_gr_array()

