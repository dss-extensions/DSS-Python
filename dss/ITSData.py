# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Iterable

class ITSData(Iterable):
    '''
    TSData objects
    
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
        'GMRac',
        'GMRUnits',
        'Radius',
        'RadiusUnits',
        'ResistanceUnits',
        'Diameter',
        'TapeLayer',
        'TapeLap',
        'DiaShield',
        'DiaCable',
        'DiaIns',
        'InsLayer',
        'EpsR',
    ]

    @property
    def EmergAmps(self) -> float:
        '''Emergency ampere rating'''
        return self._check_for_error(self._lib.TSData_Get_EmergAmps())

    @EmergAmps.setter
    def EmergAmps(self, Value: float):
        self._check_for_error(self._lib.TSData_Set_EmergAmps(Value))

    @property
    def NormAmps(self) -> float:
        '''Normal Ampere rating'''
        return self._check_for_error(self._lib.TSData_Get_NormAmps())

    @NormAmps.setter
    def NormAmps(self, Value: float):
        self._check_for_error(self._lib.TSData_Set_NormAmps(Value))

    @property
    def Rdc(self) -> float:
        return self._check_for_error(self._lib.TSData_Get_Rdc())

    @Rdc.setter
    def Rdc(self, Value: float):
        self._check_for_error(self._lib.TSData_Set_Rdc(Value))

    @property
    def Rac(self) -> float:
        return self._check_for_error(self._lib.TSData_Get_Rac())

    @Rac.setter
    def Rac(self, Value: float):
        self._check_for_error(self._lib.TSData_Set_Rac(Value))

    @property
    def GMRac(self) -> float:
        return self._check_for_error(self._lib.TSData_Get_GMRac())

    @GMRac.setter
    def GMRac(self, Value: float):
        self._check_for_error(self._lib.TSData_Set_GMRac(Value))

    @property
    def GMRUnits(self) -> int:
        return self._check_for_error(self._lib.TSData_Get_GMRUnits())

    @GMRUnits.setter
    def GMRUnits(self, Value: int):
        self._check_for_error(self._lib.TSData_Set_GMRUnits(Value))

    @property
    def Radius(self) -> float:
        return self._check_for_error(self._lib.TSData_Get_Radius())

    @Radius.setter
    def Radius(self, Value: float):
        self._check_for_error(self._lib.TSData_Set_Radius(Value))

    @property
    def RadiusUnits(self) -> int:
        return self._check_for_error(self._lib.TSData_Get_RadiusUnits())

    @RadiusUnits.setter
    def RadiusUnits(self, Value: int):
        self._check_for_error(self._lib.TSData_Set_RadiusUnits(Value))

    @property
    def ResistanceUnits(self) -> int:
        return self._check_for_error(self._lib.TSData_Get_ResistanceUnits())

    @ResistanceUnits.setter
    def ResistanceUnits(self, Value: int):
        self._check_for_error(self._lib.TSData_Set_ResistanceUnits(Value))

    @property
    def Diameter(self) -> float:
        return self._check_for_error(self._lib.TSData_Get_Diameter())

    @Diameter.setter
    def Diameter(self, Value: float):
        self._check_for_error(self._lib.TSData_Set_Diameter(Value))

    @property
    def EpsR(self) -> float:
        return self._check_for_error(self._lib.TSData_Get_EpsR())

    @EpsR.setter
    def EpsR(self, Value: float):
        self._check_for_error(self._lib.TSData_Set_EpsR(Value))

    @property
    def InsLayer(self) -> float:
        return self._check_for_error(self._lib.TSData_Get_InsLayer())

    @InsLayer.setter
    def InsLayer(self, Value: float):
        self._check_for_error(self._lib.TSData_Set_InsLayer(Value))

    @property
    def DiaIns(self) -> float:
        return self._check_for_error(self._lib.TSData_Get_DiaIns())

    @DiaIns.setter
    def DiaIns(self, Value: float):
        self._check_for_error(self._lib.TSData_Set_DiaIns(Value))

    @property
    def DiaCable(self) -> float:
        return self._check_for_error(self._lib.TSData_Get_DiaCable())

    @DiaCable.setter
    def DiaCable(self, Value: float):
        self._check_for_error(self._lib.TSData_Set_DiaCable(Value))

    @property
    def DiaShield(self) -> float:
        return self._check_for_error(self._lib.TSData_Get_DiaShield())

    @DiaShield.setter
    def DiaShield(self, Value: float):
        self._check_for_error(self._lib.TSData_Set_DiaShield(Value))

    @property
    def TapeLayer(self) -> float:
        return self._check_for_error(self._lib.TSData_Get_TapeLayer())

    @TapeLayer.setter
    def TapeLayer(self, Value: float):
        self._check_for_error(self._lib.TSData_Set_TapeLayer(Value))

    @property
    def TapeLap(self) -> float:
        return self._check_for_error(self._lib.TSData_Get_TapeLap())

    @TapeLap.setter
    def TapeLap(self, Value: float):
        self._check_for_error(self._lib.TSData_Set_TapeLap(Value))
