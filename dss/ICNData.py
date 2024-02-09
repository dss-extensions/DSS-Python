# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Iterable
from typing import Union
from .enums import LineUnits

class ICNData(Iterable):
    '''
    CNData objects
    
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
        'EpsR',
        'InsLayer',
        'DiaIns',
        'DiaCable',
        'DiaStrand',
        'RStrand',
        'k',
    ]

    @property
    def EmergAmps(self) -> float:
        '''Emergency ampere rating'''
        return self._check_for_error(self._lib.CNData_Get_EmergAmps())

    @EmergAmps.setter
    def EmergAmps(self, Value: float):
        self._check_for_error(self._lib.CNData_Set_EmergAmps(Value))

    @property
    def NormAmps(self) -> float:
        '''Normal Ampere rating'''
        return self._check_for_error(self._lib.CNData_Get_NormAmps())

    @NormAmps.setter
    def NormAmps(self, Value: float):
        self._check_for_error(self._lib.CNData_Set_NormAmps(Value))

    @property
    def Rdc(self) -> float:
        return self._check_for_error(self._lib.CNData_Get_Rdc())

    @Rdc.setter
    def Rdc(self, Value: float):
        self._check_for_error(self._lib.CNData_Set_Rdc(Value))

    @property
    def Rac(self) -> float:
        return self._check_for_error(self._lib.CNData_Get_Rac())

    @Rac.setter
    def Rac(self, Value: float):
        self._check_for_error(self._lib.CNData_Set_Rac(Value))

    @property
    def GMRac(self) -> float:
        return self._check_for_error(self._lib.CNData_Get_GMRac())

    @GMRac.setter
    def GMRac(self, Value: float):
        self._check_for_error(self._lib.CNData_Set_GMRac(Value))

    @property
    def GMRUnits(self) -> LineUnits:
        return LineUnits(self._check_for_error(self._lib.CNData_Get_GMRUnits()))

    @GMRUnits.setter
    def GMRUnits(self, Value: int):
        self._check_for_error(self._lib.CNData_Set_GMRUnits(Value))

    @property
    def Radius(self) -> float:
        return self._check_for_error(self._lib.CNData_Get_Radius())

    @Radius.setter
    def Radius(self, Value: float):
        self._check_for_error(self._lib.CNData_Set_Radius(Value))

    @property
    def RadiusUnits(self) -> LineUnits:
        return LineUnits(self._check_for_error(self._lib.CNData_Get_RadiusUnits()))

    @RadiusUnits.setter
    def RadiusUnits(self, Value: Union[int, LineUnits]):
        self._check_for_error(self._lib.CNData_Set_RadiusUnits(Value))

    @property
    def ResistanceUnits(self) -> LineUnits:
        return LineUnits(self._check_for_error(self._lib.CNData_Get_ResistanceUnits()))

    @ResistanceUnits.setter
    def ResistanceUnits(self, Value: Union[int, LineUnits]):
        self._check_for_error(self._lib.CNData_Set_ResistanceUnits(Value))

    @property
    def Diameter(self) -> float:
        return self._check_for_error(self._lib.CNData_Get_Diameter())

    @Diameter.setter
    def Diameter(self, Value: float):
        self._check_for_error(self._lib.CNData_Set_Diameter(Value))

    @property
    def EpsR(self) -> float:
        return self._check_for_error(self._lib.CNData_Get_EpsR())

    @EpsR.setter
    def EpsR(self, Value: float):
        self._check_for_error(self._lib.CNData_Set_EpsR(Value))

    @property
    def InsLayer(self) -> float:
        return self._check_for_error(self._lib.CNData_Get_InsLayer())

    @InsLayer.setter
    def InsLayer(self, Value: float):
        self._check_for_error(self._lib.CNData_Set_InsLayer(Value))

    @property
    def DiaIns(self) -> float:
        return self._check_for_error(self._lib.CNData_Get_DiaIns())

    @DiaIns.setter
    def DiaIns(self, Value: float):
        self._check_for_error(self._lib.CNData_Set_DiaIns(Value))

    @property
    def DiaCable(self) -> float:
        return self._check_for_error(self._lib.CNData_Get_DiaCable())

    @DiaCable.setter
    def DiaCable(self, Value: float):
        self._check_for_error(self._lib.CNData_Set_DiaCable(Value))

    @property
    def k(self) -> int:
        return self._check_for_error(self._lib.CNData_Get_k())

    @k.setter
    def k(self, Value: int):
        self._check_for_error(self._lib.CNData_Set_k(Value))

    @property
    def DiaStrand(self) -> float:
        return self._check_for_error(self._lib.CNData_Get_DiaStrand())

    @DiaStrand.setter
    def DiaStrand(self, Value: float):
        self._check_for_error(self._lib.CNData_Set_DiaStrand(Value))

    @property
    def GmrStrand(self) -> float:
        return self._check_for_error(self._lib.CNData_Get_GmrStrand())

    @GmrStrand.setter
    def GmrStrand(self, Value: float):
        self._check_for_error(self._lib.CNData_Set_GmrStrand(Value))

    @property
    def RStrand(self) -> float:
        return self._check_for_error(self._lib.CNData_Get_RStrand())

    @RStrand.setter
    def RStrand(self, Value: float):
        self._check_for_error(self._lib.CNData_Set_RStrand(Value))


