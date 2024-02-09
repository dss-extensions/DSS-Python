# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Iterable
from typing import List, Union
from ._types import Float64Array, Int32Array, Float64ArrayOrComplexArray
from .enums import LineUnits

class ILineGeometries(Iterable):
    '''
    LineGeometry objects
    
    (API Extension)
    '''

    __slots__ = []

    _columns = [
        'Name',
        'idx',
        'Nconds',
        'Phases',
        'RhoEarth',
        'Reduce',
        'Units',
        'Conductors',
        'Xcoords',
        'Ycoords',
        'Rmatrix',
        'Xmatrix',
        'Zmatrix',
        'NormAmps',
        'EmergAmps',
    ]
    
    @property
    def Conductors(self) -> List[str]:
        '''Array of strings with names of all conductors in the active LineGeometry object'''
        return self._check_for_error(self._get_string_array(self._lib.LineGeometries_Get_Conductors))

    @property
    def EmergAmps(self) -> float:
        '''Emergency ampere rating'''
        return self._check_for_error(self._lib.LineGeometries_Get_EmergAmps())

    @EmergAmps.setter
    def EmergAmps(self, Value: float):
        self._check_for_error(self._lib.LineGeometries_Set_EmergAmps(Value))

    @property
    def NormAmps(self) -> float:
        '''Normal ampere rating'''
        return self._check_for_error(self._lib.LineGeometries_Get_NormAmps())

    @NormAmps.setter
    def NormAmps(self, Value: float):
        self._check_for_error(self._lib.LineGeometries_Set_NormAmps(Value))

    @property
    def RhoEarth(self) -> float:
        return self._check_for_error(self._lib.LineGeometries_Get_RhoEarth())

    @RhoEarth.setter
    def RhoEarth(self, Value: float):
        self._check_for_error(self._lib.LineGeometries_Set_RhoEarth(Value))

    @property
    def Reduce(self) -> bool:
        return self._check_for_error(self._lib.LineGeometries_Get_Reduce()) != 0

    @Reduce.setter
    def Reduce(self, Value: bool):
        self._check_for_error(self._lib.LineGeometries_Set_Reduce(Value))

    @property
    def Phases(self) -> int:
        '''Number of Phases'''
        return self._check_for_error(self._lib.LineGeometries_Get_Phases())

    @Phases.setter
    def Phases(self, Value: int):
        self._check_for_error(self._lib.LineGeometries_Set_Phases(Value))

    def Rmatrix(self, Frequency: float, Length: float, Units: int) -> Float64Array:
        '''Resistance matrix, ohms'''
        self._check_for_error(self._lib.LineGeometries_Get_Rmatrix_GR(Frequency, Length, Units))
        return self._get_float64_gr_array()

    def Xmatrix(self, Frequency: float, Length: float, Units: int) -> Float64Array:
        '''Reactance matrix, ohms'''
        self._check_for_error(self._lib.LineGeometries_Get_Xmatrix_GR(Frequency, Length, Units))
        return self._get_float64_gr_array()

    def Zmatrix(self, Frequency: float, Length: float, Units: int) -> Float64ArrayOrComplexArray:
        '''Complex impedance matrix, ohms'''
        self._check_for_error(self._lib.LineGeometries_Get_Zmatrix_GR(Frequency, Length, Units))
        return self._get_complex128_gr_array()

    def Cmatrix(self, Frequency: float, Length: float, Units: int) -> Float64Array:
        '''Capacitance matrix, nF'''
        self._check_for_error(self._lib.LineGeometries_Get_Cmatrix_GR(Frequency, Length, Units))
        return self._get_float64_gr_array()

    @property
    def Units(self) -> List[LineUnits]:
        self._check_for_error(self._lib.LineGeometries_Get_Units_GR())
        return [LineUnits(unit) for unit in self._get_int32_gr_array()]

    @Units.setter
    def Units(self, Value: Union[Int32Array, List[LineUnits]]):
        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)
        self._check_for_error(self._lib.LineGeometries_Set_Units(ValuePtr, ValueCount))

    @property
    def Xcoords(self) -> Float64Array:
        '''Get/Set the X (horizontal) coordinates of the conductors'''
        self._check_for_error(self._lib.LineGeometries_Get_Xcoords_GR())
        return self._get_float64_gr_array()

    @Xcoords.setter
    def Xcoords(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.LineGeometries_Set_Xcoords(ValuePtr, ValueCount))

    @property
    def Ycoords(self) -> Float64Array:
        '''Get/Set the Y (vertical/height) coordinates of the conductors'''
        self._check_for_error(self._lib.LineGeometries_Get_Ycoords_GR())
        return self._get_float64_gr_array()

    @Ycoords.setter
    def Ycoords(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.LineGeometries_Set_Ycoords(ValuePtr, ValueCount))

    @property
    def Nconds(self) -> int:
        '''Number of conductors in this geometry. Default is 3. Triggers memory allocations. Define first!'''
        return self._check_for_error(self._lib.LineGeometries_Get_Nconds())

    @Nconds.setter
    def Nconds(self, Value: int):
        self._check_for_error(self._lib.LineGeometries_Set_Nconds(Value))
