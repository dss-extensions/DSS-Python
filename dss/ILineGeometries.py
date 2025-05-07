# A compatibility layer for DSS C-API that mimics EPRI's OpenDSS COM interface.
# Copyright (c) 2016-2025 Paulo Meira
# Copyright (c) 2018-2025 DSS-Extensions contributors
from ._cffi_api_util import Iterable
from typing import List, Union
from ._types import Float64Array, Float64Matrix, Int32Array, ComplexMatrix 
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
        return self._lib.LineGeometries_Get_Conductors()

    @property
    def EmergAmps(self) -> float:
        '''Emergency ampere rating'''
        return self._lib.LineGeometries_Get_EmergAmps()

    @EmergAmps.setter
    def EmergAmps(self, Value: float):
        self._lib.LineGeometries_Set_EmergAmps(Value)

    @property
    def NormAmps(self) -> float:
        '''Normal ampere rating'''
        return self._lib.LineGeometries_Get_NormAmps()

    @NormAmps.setter
    def NormAmps(self, Value: float):
        self._lib.LineGeometries_Set_NormAmps(Value)

    @property
    def RhoEarth(self) -> float:
        return self._lib.LineGeometries_Get_RhoEarth()

    @RhoEarth.setter
    def RhoEarth(self, Value: float):
        self._lib.LineGeometries_Set_RhoEarth(Value)

    @property
    def Reduce(self) -> bool:
        return self._lib.LineGeometries_Get_Reduce()

    @Reduce.setter
    def Reduce(self, Value: bool):
        self._lib.LineGeometries_Set_Reduce(Value)

    @property
    def Phases(self) -> int:
        '''Number of Phases'''
        return self._lib.LineGeometries_Get_Phases()

    @Phases.setter
    def Phases(self, Value: int):
        self._lib.LineGeometries_Set_Phases(Value)

    def Rmatrix(self, Frequency: float, Length: float, Units: int) -> Float64Matrix:
        '''Resistance matrix, ohms'''
        return self._lib.LineGeometries_Get_Rmatrix_GR(Frequency, Length, Units)

    def Xmatrix(self, Frequency: float, Length: float, Units: int) -> Float64Matrix:
        '''Reactance matrix, ohms'''
        return self._lib.LineGeometries_Get_Xmatrix_GR(Frequency, Length, Units)

    def Zmatrix(self, Frequency: float, Length: float, Units: int) -> ComplexMatrix:
        '''Complex impedance matrix, ohms'''
        return self._lib.LineGeometries_Get_Zmatrix_GR(Frequency, Length, Units)

    def Cmatrix(self, Frequency: float, Length: float, Units: int) -> Float64Array:
        '''Capacitance matrix, nF'''
        return self._lib.LineGeometries_Get_Cmatrix_GR(Frequency, Length, Units)

    @property
    def Units(self) -> List[LineUnits]:
        return [LineUnits(unit) for unit in self._lib.LineGeometries_Get_Units_GR()]

    @Units.setter
    def Units(self, Value: Union[Int32Array, List[LineUnits]]):
        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)
        self._lib.LineGeometries_Set_Units(ValuePtr, ValueCount)

    @property
    def Xcoords(self) -> Float64Array:
        '''Get/Set the X (horizontal) coordinates of the conductors'''
        return self._lib.LineGeometries_Get_Xcoords_GR()

    @Xcoords.setter
    def Xcoords(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.LineGeometries_Set_Xcoords(ValuePtr, ValueCount)

    @property
    def Ycoords(self) -> Float64Array:
        '''Get/Set the Y (vertical/height) coordinates of the conductors'''
        return self._lib.LineGeometries_Get_Ycoords_GR()

    @Ycoords.setter
    def Ycoords(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.LineGeometries_Set_Ycoords(ValuePtr, ValueCount)

    @property
    def Nconds(self) -> int:
        '''Number of conductors in this geometry. Default is 3. Triggers memory allocations. Define first!'''
        return self._lib.LineGeometries_Get_Nconds()

    @Nconds.setter
    def Nconds(self, Value: int):
        self._lib.LineGeometries_Set_Nconds(Value)
