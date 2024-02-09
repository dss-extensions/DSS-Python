# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2023-2024 Paulo Meira
# Copyright (c) 2023-2024 DSS-Extensions contributors
from ._cffi_api_util import Iterable

class IGICSources(Iterable):
    __slots__ = []
    _is_circuit_element = True

    _columns = [
        'Name',
        'idx',
        'Phases',
        'Bus1',
        'Bus2',
        'EN',
        'EE',
        'Lat1',
        'Lat2',
        'Lon1',
        'Lon2',
        'Volts',
    ]

    @property
    def Bus1(self) -> str:
        '''First bus name of GICSource (Created name)'''
        return self._get_string(self._check_for_error(self._lib.GICSources_Get_Bus1()))

    @property
    def Bus2(self) -> str:
        '''Second bus name'''
        return self._get_string(self._check_for_error(self._lib.GICSources_Get_Bus2()))

    @property
    def Phases(self) -> int:
        '''Number of Phases, this GICSource element.'''
        return self._check_for_error(self._lib.GICSources_Get_Phases())

    @Phases.setter
    def Phases(self, Value: int):
        self._check_for_error(self._lib.GICSources_Set_Phases(Value))

    @property
    def EN(self) -> float:
        '''Northward E Field V/km'''
        return self._check_for_error(self._lib.GICSources_Get_EN())

    @EN.setter
    def EN(self, Value: float):
        self._check_for_error(self._lib.GICSources_Set_EN(Value))

    @property
    def EE(self) -> float:
        '''Eastward E Field, V/km'''
        return self._check_for_error(self._lib.GICSources_Get_EE())

    @EE.setter
    def EE(self, Value: float):
        self._check_for_error(self._lib.GICSources_Set_EE(Value))

    @property
    def Lat1(self) -> float:
        '''Latitude of Bus1 (degrees)'''
        return self._check_for_error(self._lib.GICSources_Get_Lat1())

    @Lat1.setter
    def Lat1(self, Value: float):
        self._check_for_error(self._lib.GICSources_Set_Lat1(Value))

    @property
    def Lat2(self) -> float:
        '''Latitude of Bus2 (degrees)'''
        return self._check_for_error(self._lib.GICSources_Get_Lat2())

    @Lat2.setter
    def Lat2(self, Value: float):
        self._check_for_error(self._lib.GICSources_Set_Lat2(Value))

    @property
    def Lon1(self) -> float:
        '''Longitude of Bus1 (Degrees)'''
        return self._check_for_error(self._lib.GICSources_Get_Lon1())

    @Lon1.setter
    def Lon1(self, Value: float):
        self._check_for_error(self._lib.GICSources_Set_Lon1(Value))

    @property
    def Lon2(self) -> float:
        '''Longitude of Bus2 (Degrees)'''
        return self._check_for_error(self._lib.GICSources_Get_Lon2())

    @Lon2.setter
    def Lon2(self, Value: float):
        self._check_for_error(self._lib.GICSources_Set_Lon2(Value))

    @property
    def Volts(self) -> float:
        '''Specify dc voltage directly'''
        return self._check_for_error(self._lib.GICSources_Get_Volts())

    @Volts.setter
    def Volts(self, Value: float):
        self._check_for_error(self._lib.GICSources_Set_Volts(Value))
