'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2019 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Iterable

class ILineSpacings(Iterable):
    '''Experimental API extension exposing part of the LineSpacing objects'''

    __slots__ = []

    @property
    def Phases(self):
        '''Number of Phases'''
        return self._lib.LineSpacings_Get_Phases()

    @Phases.setter
    def Phases(self, Value):
        self._lib.LineSpacings_Set_Phases(Value)
        self.CheckForError()

    @property
    def Nconds(self):
        return self._lib.LineSpacings_Get_Nconds()

    @Nconds.setter
    def Nconds(self, Value):
        self._lib.LineSpacings_Set_Nconds(Value)
        self.CheckForError()

    @property
    def Units(self):
        return self._lib.LineSpacings_Get_Units()

    @Units.setter
    def Units(self, Value):
        self._lib.LineSpacings_Set_Units(Value)
        self.CheckForError()

    @property
    def Xcoords(self):
        '''Get/Set the X (horizontal) coordinates of the conductors'''
        return self._get_float64_array(self._lib.LineSpacings_Get_Xcoords)

    @Xcoords.setter
    def Xcoords(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.LineSpacings_Set_Xcoords(ValuePtr, ValueCount)
        self.CheckForError()

    @property
    def Ycoords(self):
        '''Get/Set the Y (vertical/height) coordinates of the conductors'''
        return self._get_float64_array(self._lib.LineSpacings_Get_Ycoords)

    @Ycoords.setter
    def Ycoords(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.LineSpacings_Set_Ycoords(ValuePtr, ValueCount)
        self.CheckForError()
