'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira
Copyright (c) 2018-2022 DSS Extensions contributors
'''
from .._cffi_api_util import Iterable

class ILineSpacings(Iterable):
    '''Experimental API extension exposing part of the LineSpacing objects'''

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
    def Phases(self):
        '''Number of Phases'''
        return self.CheckForError(self._lib.LineSpacings_Get_Phases())

    @Phases.setter
    def Phases(self, Value):
        self.CheckForError(self._lib.LineSpacings_Set_Phases(Value))

    @property
    def Nconds(self):
        return self.CheckForError(self._lib.LineSpacings_Get_Nconds())

    @Nconds.setter
    def Nconds(self, Value):
        self.CheckForError(self._lib.LineSpacings_Set_Nconds(Value))

    @property
    def Units(self):
        return self.CheckForError(self._lib.LineSpacings_Get_Units()) #TODO: use enum

    @Units.setter
    def Units(self, Value):
        self.CheckForError(self._lib.LineSpacings_Set_Units(Value))

    @property
    def Xcoords(self):
        '''Get/Set the X (horizontal) coordinates of the conductors'''
        self.CheckForError(self._lib.LineSpacings_Get_Xcoords_GR())
        return self._get_float64_gr_array()

    @Xcoords.setter
    def Xcoords(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.LineSpacings_Set_Xcoords(ValuePtr, ValueCount))

    @property
    def Ycoords(self):
        '''Get/Set the Y (vertical/height) coordinates of the conductors'''
        self.CheckForError(self._lib.LineSpacings_Get_Ycoords_GR())
        return self._get_float64_gr_array()

    @Ycoords.setter
    def Ycoords(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.LineSpacings_Set_Ycoords(ValuePtr, ValueCount))
