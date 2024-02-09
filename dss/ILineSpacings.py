# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Iterable
from ._types import Float64Array
from typing import Union
from .enums import LineUnits

class ILineSpacings(Iterable):
    '''
    LineSpacing objects
    
    (API Extension)
    '''

    __slots__ = []

    _columns = [
        'Name',
        'idx',
        'Nconds',
        'Phases',
        'Units',
        'Xcoords',
        'Ycoords',
    ]

    @property
    def Phases(self) -> int:
        '''Number of Phases'''
        return self._check_for_error(self._lib.LineSpacings_Get_Phases())

    @Phases.setter
    def Phases(self, Value: int):
        self._check_for_error(self._lib.LineSpacings_Set_Phases(Value))

    @property
    def Nconds(self) -> int:
        return self._check_for_error(self._lib.LineSpacings_Get_Nconds())

    @Nconds.setter
    def Nconds(self, Value: int):
        self._check_for_error(self._lib.LineSpacings_Set_Nconds(Value))

    @property
    def Units(self) -> LineUnits:
        return LineUnits(self._check_for_error(self._lib.LineSpacings_Get_Units()))

    @Units.setter
    def Units(self, Value: Union[int, LineUnits]):
        self._check_for_error(self._lib.LineSpacings_Set_Units(Value))

    @property
    def Xcoords(self) -> Float64Array:
        '''Get/Set the X (horizontal) coordinates of the conductors'''
        self._check_for_error(self._lib.LineSpacings_Get_Xcoords_GR())
        return self._get_float64_gr_array()

    @Xcoords.setter
    def Xcoords(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.LineSpacings_Set_Xcoords(ValuePtr, ValueCount))

    @property
    def Ycoords(self) -> Float64Array:
        '''Get/Set the Y (vertical/height) coordinates of the conductors'''
        self._check_for_error(self._lib.LineSpacings_Get_Ycoords_GR())
        return self._get_float64_gr_array()

    @Ycoords.setter
    def Ycoords(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.LineSpacings_Set_Ycoords(ValuePtr, ValueCount))
