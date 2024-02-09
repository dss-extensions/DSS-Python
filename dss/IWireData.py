# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Iterable
from typing import Union
from .enums import LineUnits

class IWireData(Iterable):
    '''
    WireData objects
    
    (API Extension)
    '''

    __slots__ = []

    _columns = [
        'Name',
        'idx',
        'NormAmps',
        'EmergAmps',
        'Rdc',
        'Rac',
        'ResistanceUnits',
        'GMRac',
        'GMRUnits',
        'Radius',
        'Diameter',
        'RadiusUnits',
        'CapRadius',
    ]

    @property
    def EmergAmps(self) -> float:
        '''Emergency ampere rating'''
        return self._check_for_error(self._lib.WireData_Get_EmergAmps())

    @EmergAmps.setter
    def EmergAmps(self, Value: float):
        self._check_for_error(self._lib.WireData_Set_EmergAmps(Value))

    @property
    def NormAmps(self) -> float:
        '''Normal Ampere rating'''
        return self._check_for_error(self._lib.WireData_Get_NormAmps())

    @NormAmps.setter
    def NormAmps(self, Value: float):
        self._check_for_error(self._lib.WireData_Set_NormAmps(Value))

    @property
    def Rdc(self) -> float:
        return self._check_for_error(self._lib.WireData_Get_Rdc())

    @Rdc.setter
    def Rdc(self, Value: float):
        self._check_for_error(self._lib.WireData_Set_Rdc(Value))

    @property
    def Rac(self) -> float:
        return self._check_for_error(self._lib.WireData_Get_Rac())

    @Rac.setter
    def Rac(self, Value: float):
        self._check_for_error(self._lib.WireData_Set_Rac(Value))

    @property
    def GMRac(self) -> float:
        return self._check_for_error(self._lib.WireData_Get_GMRac())

    @GMRac.setter
    def GMRac(self, Value: float):
        self._check_for_error(self._lib.WireData_Set_GMRac(Value))

    @property
    def GMRUnits(self) -> LineUnits:
        return LineUnits(self._check_for_error(self._lib.WireData_Get_GMRUnits()))

    @GMRUnits.setter
    def GMRUnits(self, Value: Union[int, LineUnits]):
        self._check_for_error(self._lib.WireData_Set_GMRUnits(Value))

    @property
    def Radius(self) -> float:
        return self._check_for_error(self._lib.WireData_Get_Radius())

    @Radius.setter
    def Radius(self, Value: float):
        self._check_for_error(self._lib.WireData_Set_Radius(Value))

    @property
    def RadiusUnits(self) -> int:
        return self._check_for_error(self._lib.WireData_Get_RadiusUnits())

    @RadiusUnits.setter
    def RadiusUnits(self, Value: int):
        self._check_for_error(self._lib.WireData_Set_RadiusUnits(Value))

    @property
    def ResistanceUnits(self) -> LineUnits:
        return LineUnits(self._check_for_error(self._lib.WireData_Get_ResistanceUnits()))

    @ResistanceUnits.setter
    def ResistanceUnits(self, Value: Union[int, LineUnits]):
        self._check_for_error(self._lib.WireData_Set_ResistanceUnits(Value))

    @property
    def Diameter(self) -> float:
        return self._check_for_error(self._lib.WireData_Get_Diameter())

    @Diameter.setter
    def Diameter(self, Value: float):
        self._check_for_error(self._lib.WireData_Set_Diameter(Value))

    @property
    def CapRadius(self) -> float:
        '''Equivalent conductor radius for capacitance calcs. Specify this for bundled conductors. Defaults to same value as radius.'''
        return self._check_for_error(self._lib.WireData_Get_CapRadius())

    @CapRadius.setter
    def CapRadius(self, Value: float):
        self._check_for_error(self._lib.WireData_Set_CapRadius(Value))
