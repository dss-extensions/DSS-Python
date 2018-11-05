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
        return self._get_string_array(self._lib.LineGeometries_Get_AllNames)

    @property
    def Conductors(self):
        '''(read-only) Array of strings with names of all conductors in the active LineGeometry object'''
        return self._get_string_array(self._lib.LineGeometries_Get_Conductors)

    @property
    def Count(self):
        '''(read-only) Number of LineGeometries'''
        return self._lib.LineGeometries_Get_Count()

    @property
    def First(self):
        return self._lib.LineGeometries_Get_First()

    @property
    def Next(self):
        return self._lib.LineGeometries_Get_Next()

    @property
    def Name(self):
        '''Name of active LineGeometry'''
        return self._get_string(self._lib.LineGeometries_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.LineGeometries_Set_Name(Value)
        self.CheckForError()

    def __len__(self):
        return self._lib.LineGeometries_Get_Count()

    @property
    def EmergAmps(self):
        '''Emergency ampere rating'''
        return self._lib.LineGeometries_Get_EmergAmps()

    @EmergAmps.setter
    def EmergAmps(self, Value):
        self._lib.LineGeometries_Set_EmergAmps(Value)
        self.CheckForError()

    @property
    def NormAmps(self):
        '''Normal Ampere rating'''
        return self._lib.LineGeometries_Get_NormAmps()

    @NormAmps.setter
    def NormAmps(self, Value):
        self._lib.LineGeometries_Set_NormAmps(Value)
        self.CheckForError()

    @property
    def RhoEarth(self):
        return self._lib.LineGeometries_Get_RhoEarth()

    @RhoEarth.setter
    def RhoEarth(self, Value):
        self._lib.LineGeometries_Set_RhoEarth(Value)
        self.CheckForError()

    @property
    def Reduce(self):
        return self._lib.LineGeometries_Get_Reduce() != 0

    @Reduce.setter
    def Reduce(self, Value):
        self._lib.LineGeometries_Set_Reduce(Value)
        self.CheckForError()

    @property
    def Phases(self):
        '''Number of Phases'''
        return self._lib.LineGeometries_Get_Phases()

    @Phases.setter
    def Phases(self, Value):
        self._lib.LineGeometries_Set_Phases(Value)
        self.CheckForError()

    def Rmatrix(self, Frequency, Length, Units):
        '''(read-only) Resistance matrix, ohms'''
        self._lib.LineGeometries_Get_Rmatrix_GR(Frequency, Length, Units)
        return self._get_float64_gr_array()

    def Xmatrix(self, Frequency, Length, Units):
        '''(read-only) Reactance matrix, ohms'''
        self._lib.LineGeometries_Get_Xmatrix_GR(Frequency, Length, Units)
        return self._get_float64_gr_array()

    def Zmatrix(self, Frequency, Length, Units):
        '''(read-only) Complex impedance matrix, ohms'''
        self._lib.LineGeometries_Get_Zmatrix_GR(Frequency, Length, Units)
        return self._get_float64_gr_array()

    def Cmatrix(self, Frequency, Length, Units):
        '''(read-only) Capacitance matrix, nF'''
        self._lib.LineGeometries_Get_Cmatrix_GR(Frequency, Length, Units)
        return self._get_float64_gr_array()

    @property
    def Units(self):
        self._lib.LineGeometries_Get_Units_GR()
        return self._get_int32_gr_array()

    @Units.setter
    def Units(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)
        self._lib.LineGeometries_Set_Units(ValuePtr, ValueCount)
        self.CheckForError()

    @property
    def Xcoords(self):
        '''Get/Set the X (horizontal) coordinates of the conductors'''
        self._lib.LineGeometries_Get_Xcoords_GR()
        return self._get_float64_gr_array()

    @Xcoords.setter
    def Xcoords(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.LineGeometries_Set_Xcoords(ValuePtr, ValueCount)
        self.CheckForError()

    @property
    def Ycoords(self):
        '''Get/Set the Y (vertical/height) coordinates of the conductors'''
        self._lib.LineGeometries_Get_Ycoords_GR()
        return self._get_float64_gr_array()

    @Ycoords.setter
    def Ycoords(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.LineGeometries_Set_Ycoords(ValuePtr, ValueCount)
        self.CheckForError()

    def __iter__(self):
        idx = self.First
        while idx != 0:
            yield self
            idx = self.Next

