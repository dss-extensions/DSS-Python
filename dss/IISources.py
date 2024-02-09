# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
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
        '''
        Magnitude of the ISource in amps

        Original COM help: https://opendss.epri.com/Amps.html
        '''
        return self._check_for_error(self._lib.ISources_Get_Amps())

    @Amps.setter
    def Amps(self, Value: float):
        self._check_for_error(self._lib.ISources_Set_Amps(Value))
 
    @property
    def AngleDeg(self) -> float:
        '''
        Phase angle for ISource, degrees

        Original COM help: https://opendss.epri.com/AngleDeg.html
        '''
        return self._check_for_error(self._lib.ISources_Get_AngleDeg())

    @AngleDeg.setter
    def AngleDeg(self, Value: float):
        self._check_for_error(self._lib.ISources_Set_AngleDeg(Value))
 
    @property
    def Frequency(self) -> float:
        '''
        The present frequency of the ISource, Hz

        Original COM help: https://opendss.epri.com/Frequency.html
        '''
        return self._check_for_error(self._lib.ISources_Get_Frequency())

    @Frequency.setter
    def Frequency(self, Value: float):
        self._check_for_error(self._lib.ISources_Set_Frequency(Value))
 