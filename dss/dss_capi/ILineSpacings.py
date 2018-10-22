'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class ILineSpacings(Base):
    '''Experimental API extension exposing part of the LineSpacing objects'''

    __slots__ = []

    @property
    def AllNames(self):
        '''(read-only) Array of strings with names of all devices'''
        return self.get_string_array(self.lib.LineSpacings_Get_AllNames)

    @property
    def Conductors(self):
        '''(read-only) Array of strings with names of all conductors in the active LineSpacing object'''
        return self.get_string_array(self.lib.LineSpacings_Get_Conductors)

    @property
    def Count(self):
        '''(read-only) Number of LineSpacings'''
        return self.lib.LineSpacings_Get_Count()

    @property
    def First(self):
        return self.lib.LineSpacings_Get_First()

    @property
    def Next(self):
        return self.lib.LineSpacings_Get_Next()

    @property
    def Name(self):
        '''Name of active LineSpacing'''
        return self.get_string(self.lib.LineSpacings_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.LineSpacings_Set_Name(Value)

    def __len__(self):
        return self.lib.LineSpacings_Get_Count()

    @property
    def Phases(self):
        '''Number of Phases'''
        return self.lib.LineSpacings_Get_Phases()

    @Phases.setter
    def Phases(self, Value):
        self.lib.LineSpacings_Set_Phases(Value)

    @property
    def Nconds(self):
        return self.lib.LineSpacings_Get_Nconds()

    @Nconds.setter
    def Nconds(self, Value):
        self.lib.LineSpacings_Set_Nconds(Value)

    @property
    def Units(self):
        return self.lib.LineSpacings_Get_Units()

    @Units.setter
    def Units(self, Value):
        self.lib.LineSpacings_Set_Units(Value)

    @property
    def Xcoords(self):
        '''Get/Set the X (horizontal) coordinates of the conductors'''
        self.lib.LineSpacings_Get_Xcoords_GR()
        return self.get_float64_gr_array()

    @Xcoords.setter
    def Xcoords(self, Value):
        Value, ValuePtr, ValueCount = self.prepare_float64_array(Value)
        self.lib.LineSpacings_Set_Xcoords(ValuePtr, ValueCount)

    @property
    def Ycoords(self):
        '''Get/Set the Y (vertical/height) coordinates of the conductors'''
        self.lib.LineSpacings_Get_Ycoords_GR()
        return self.get_float64_gr_array()

    @Ycoords.setter
    def Ycoords(self, Value):
        Value, ValuePtr, ValueCount = self.prepare_float64_array(Value)
        self.lib.LineSpacings_Set_Ycoords(ValuePtr, ValueCount)

    def __iter__(self):
        idx = self.First
        while idx != 0:
            yield self
            idx = self.Next
