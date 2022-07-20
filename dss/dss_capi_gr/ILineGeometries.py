'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira
Copyright (c) 2018-2022 DSS Extensions contributors
'''
from .._cffi_api_util import Iterable

class ILineGeometries(Iterable):
    '''Experimental API extension exposing part of the LineGeometry objects'''

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
    def Conductors(self):
        '''(read-only) Array of strings with names of all conductors in the active LineGeometry object'''
        return self.CheckForError(self._get_string_array(self._lib.LineGeometries_Get_Conductors))

    @property
    def EmergAmps(self):
        '''Emergency ampere rating'''
        return self.CheckForError(self._lib.LineGeometries_Get_EmergAmps())

    @EmergAmps.setter
    def EmergAmps(self, Value):
        self.CheckForError(self._lib.LineGeometries_Set_EmergAmps(Value))

    @property
    def NormAmps(self):
        '''Normal ampere rating'''
        return self.CheckForError(self._lib.LineGeometries_Get_NormAmps())

    @NormAmps.setter
    def NormAmps(self, Value):
        self.CheckForError(self._lib.LineGeometries_Set_NormAmps(Value))

    @property
    def RhoEarth(self):
        return self.CheckForError(self._lib.LineGeometries_Get_RhoEarth())

    @RhoEarth.setter
    def RhoEarth(self, Value):
        self.CheckForError(self._lib.LineGeometries_Set_RhoEarth(Value))

    @property
    def Reduce(self):
        return self.CheckForError(self._lib.LineGeometries_Get_Reduce()) != 0

    @Reduce.setter
    def Reduce(self, Value):
        self.CheckForError(self._lib.LineGeometries_Set_Reduce(Value))

    @property
    def Phases(self):
        '''Number of Phases'''
        return self.CheckForError(self._lib.LineGeometries_Get_Phases())

    @Phases.setter
    def Phases(self, Value):
        self.CheckForError(self._lib.LineGeometries_Set_Phases(Value))

    def Rmatrix(self, Frequency, Length, Units):
        '''(read-only) Resistance matrix, ohms'''
        self.CheckForError(self._lib.LineGeometries_Get_Rmatrix_GR(Frequency, Length, Units))
        return self._get_float64_gr_array()

    def Xmatrix(self, Frequency, Length, Units):
        '''(read-only) Reactance matrix, ohms'''
        self.CheckForError(self._lib.LineGeometries_Get_Xmatrix_GR(Frequency, Length, Units))
        return self._get_float64_gr_array()

    def Zmatrix(self, Frequency, Length, Units):
        '''(read-only) Complex impedance matrix, ohms'''
        self.CheckForError(self._lib.LineGeometries_Get_Zmatrix_GR(Frequency, Length, Units))
        return self._get_float64_gr_array()

    def Cmatrix(self, Frequency, Length, Units):
        '''(read-only) Capacitance matrix, nF'''
        self.CheckForError(self._lib.LineGeometries_Get_Cmatrix_GR(Frequency, Length, Units))
        return self._get_float64_gr_array()

    @property
    def Units(self):
        self.CheckForError(self._lib.LineGeometries_Get_Units_GR())
        return self._get_int32_gr_array() #TODO: use enum

    @Units.setter
    def Units(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)
        self.CheckForError(self._lib.LineGeometries_Set_Units(ValuePtr, ValueCount))

    @property
    def Xcoords(self):
        '''Get/Set the X (horizontal) coordinates of the conductors'''
        self.CheckForError(self._lib.LineGeometries_Get_Xcoords_GR())
        return self._get_float64_gr_array()

    @Xcoords.setter
    def Xcoords(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.LineGeometries_Set_Xcoords(ValuePtr, ValueCount))

    @property
    def Ycoords(self):
        '''Get/Set the Y (vertical/height) coordinates of the conductors'''
        self.CheckForError(self._lib.LineGeometries_Get_Ycoords_GR())
        return self._get_float64_gr_array()

    @Ycoords.setter
    def Ycoords(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.LineGeometries_Set_Ycoords(ValuePtr, ValueCount))

    @property
    def Nconds(self):
        '''Number of conductors in this geometry. Default is 3. Triggers memory allocations. Define first!'''
        return self.CheckForError(self._lib.LineGeometries_Get_Nconds())

    @Nconds.setter
    def Nconds(self, Value):
        self.CheckForError(self._lib.LineGeometries_Set_Nconds(Value))
