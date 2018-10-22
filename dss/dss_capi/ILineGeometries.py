'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class ILineGeometries(Base):
    '''Experimental API extension exposing part of the LineGeometry objects'''

    __slots__ = []

    @property
    def AllNames(self):
        '''(read-only) Array of strings with names of all devices'''
        return self.get_string_array(self.lib.LineGeometries_Get_AllNames)

    @property
    def Conductors(self):
        '''(read-only) Array of strings with names of all conductors in the active LineGeometry object'''
        return self.get_string_array(self.lib.LineGeometries_Get_Conductors)

    @property
    def Count(self):
        '''(read-only) Number of LineGeometries'''
        return self.lib.LineGeometries_Get_Count()

    @property
    def First(self):
        return self.lib.LineGeometries_Get_First()

    @property
    def Next(self):
        return self.lib.LineGeometries_Get_Next()

    @property
    def Name(self):
        '''Name of active LineGeometry'''
        return self.get_string(self.lib.LineGeometries_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.LineGeometries_Set_Name(Value)

    def __len__(self):
        return self.lib.LineGeometries_Get_Count()

    @property
    def EmergAmps(self):
        '''Emergency ampere rating'''
        return self.lib.LineGeometries_Get_EmergAmps()

    @EmergAmps.setter
    def EmergAmps(self, Value):
        self.lib.LineGeometries_Set_EmergAmps(Value)

    @property
    def NormAmps(self):
        '''Normal Ampere rating'''
        return self.lib.LineGeometries_Get_NormAmps()

    @NormAmps.setter
    def NormAmps(self, Value):
        self.lib.LineGeometries_Set_NormAmps(Value)

    @property
    def RhoEarth(self):
        return self.lib.LineGeometries_Get_RhoEarth()

    @RhoEarth.setter
    def RhoEarth(self, Value):
        self.lib.LineGeometries_Set_RhoEarth(Value)

    @property
    def Reduce(self):
        return self.lib.LineGeometries_Get_Reduce() != 0

    @Reduce.setter
    def Reduce(self, Value):
        self.lib.LineGeometries_Set_Reduce(Value)

    @property
    def Phases(self):
        '''Number of Phases'''
        return self.lib.LineGeometries_Get_Phases()

    @Phases.setter
    def Phases(self, Value):
        self.lib.LineGeometries_Set_Phases(Value)

    def Rmatrix(self, Frequency, Length, Units):
        '''(read-only) Resistance matrix, ohms'''
        self.lib.LineGeometries_Get_Rmatrix_GR(Frequency, Length, Units)
        return self.get_float64_gr_array()

    def Xmatrix(self, Frequency, Length, Units):
        '''(read-only) Reactance matrix, ohms'''
        self.lib.LineGeometries_Get_Xmatrix_GR(Frequency, Length, Units)
        return self.get_float64_gr_array()

    def Zmatrix(self, Frequency, Length, Units):
        '''(read-only) Complex impedance matrix, ohms'''
        self.lib.LineGeometries_Get_Zmatrix_GR(Frequency, Length, Units)
        return self.get_float64_gr_array()

    def Cmatrix(self, Frequency, Length, Units):
        '''(read-only) Capacitance matrix, nF'''
        self.lib.LineGeometries_Get_Cmatrix_GR(Frequency, Length, Units)
        return self.get_float64_gr_array()

    @property
    def Units(self):
        self.lib.LineGeometries_Get_Units_GR()
        return self.get_int32_gr_array()

    @Units.setter
    def Units(self, Value):
        Value, ValuePtr, ValueCount = self.prepare_int32_array(Value)
        self.lib.LineGeometries_Set_Units(ValuePtr, ValueCount)

    @property
    def Xcoords(self):
        '''Get/Set the X (horizontal) coordinates of the conductors'''
        self.lib.LineGeometries_Get_Xcoords_GR()
        return self.get_float64_gr_array()

    @Xcoords.setter
    def Xcoords(self, Value):
        Value, ValuePtr, ValueCount = self.prepare_float64_array(Value)
        self.lib.LineGeometries_Set_Xcoords(ValuePtr, ValueCount)

    @property
    def Ycoords(self):
        '''Get/Set the Y (vertical/height) coordinates of the conductors'''
        self.lib.LineGeometries_Get_Ycoords_GR()
        return self.get_float64_gr_array()

    @Ycoords.setter
    def Ycoords(self, Value):
        Value, ValuePtr, ValueCount = self.prepare_float64_array(Value)
        self.lib.LineGeometries_Set_Ycoords(ValuePtr, ValueCount)

    def __iter__(self):
        idx = self.First
        while idx != 0:
            yield self
            idx = self.Next

