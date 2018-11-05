'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class ILoadShapes(Base):
    __slots__ = []

    def New(self, Name):
        if type(Name) is not bytes:
            Name = Name.encode(self._api_util.codec)

        return self._lib.LoadShapes_New(Name)

    def Normalize(self):
        self._lib.LoadShapes_Normalize()

    @property
    def AllNames(self):
        '''(read-only) Array of strings containing names of all Loadshape objects currently defined.'''
        return self._get_string_array(self._lib.LoadShapes_Get_AllNames)

    @property
    def Count(self):
        '''(read-only) Number of Loadshape objects currently defined in Loadshape collection'''
        return self._lib.LoadShapes_Get_Count()

    def __len__(self):
        return self._lib.LoadShapes_Get_Count()

    @property
    def First(self):
        '''(read-only) Set the first loadshape active and return integer index of the loadshape. Returns 0 if none.'''
        return self._lib.LoadShapes_Get_First()

    @property
    def HrInterval(self):
        '''Fixed interval time value, hours.'''
        return self._lib.LoadShapes_Get_HrInterval()

    @HrInterval.setter
    def HrInterval(self, Value):
        self._lib.LoadShapes_Set_HrInterval(Value)
        self.CheckForError()

    @property
    def MinInterval(self):
        '''Fixed Interval time value, in minutes'''
        return self._lib.LoadShapes_Get_MinInterval()

    @MinInterval.setter
    def MinInterval(self, Value):
        self._lib.LoadShapes_Set_MinInterval(Value)
        self.CheckForError()

    @property
    def Name(self):
        '''
        (read) Get the Name of the active Loadshape
        (write) Set the active Loadshape by name
        '''
        return self._get_string(self._lib.LoadShapes_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.LoadShapes_Set_Name(Value)
        self.CheckForError()

    @property
    def Next(self):
        '''(read-only) Advance active Loadshape to the next on in the collection. Returns 0 if no more loadshapes.'''
        return self._lib.LoadShapes_Get_Next()

    @property
    def Npts(self):
        '''
        (read) Get Number of points in active Loadshape.
        (write) Set number of points to allocate for active Loadshape.
        '''
        return self._lib.LoadShapes_Get_Npts()

    @Npts.setter
    def Npts(self, Value):
        self._lib.LoadShapes_Set_Npts(Value)
        self.CheckForError()

    @property
    def PBase(self):
        return self._lib.LoadShapes_Get_PBase()

    @PBase.setter
    def PBase(self, Value):
        self._lib.LoadShapes_Set_PBase(Value)
        self.CheckForError()

    Pbase = PBase

    @property
    def Pmult(self):
        '''
        (read) Array of Doubles for the P multiplier in the Loadshape.
        (write) Array of doubles containing the P array for the Loadshape.
        '''
        return self._get_float64_array(self._lib.LoadShapes_Get_Pmult)

    @Pmult.setter
    def Pmult(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.LoadShapes_Set_Pmult(ValuePtr, ValueCount)
        self.CheckForError()

    @property
    def QBase(self):
        '''Base for normalizing Q curve. If left at zero, the peak value is used.'''
        return self._lib.LoadShapes_Get_Qbase()

    @QBase.setter
    def QBase(self, Value):
        self._lib.LoadShapes_Set_Qbase(Value)
        self.CheckForError()

    Qbase = QBase

    @property
    def Qmult(self):
        '''Array of doubles containing the Q multipliers.'''
        return self._get_float64_array(self._lib.LoadShapes_Get_Qmult)

    @Qmult.setter
    def Qmult(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.LoadShapes_Set_Qmult(ValuePtr, ValueCount)
        self.CheckForError()

    @property
    def TimeArray(self):
        '''Time array in hours correscponding to P and Q multipliers when the Interval=0.'''
        return self._get_float64_array(self._lib.LoadShapes_Get_TimeArray)

    @TimeArray.setter
    def TimeArray(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.LoadShapes_Set_TimeArray(ValuePtr, ValueCount)
        self.CheckForError()

    @property
    def UseActual(self):
        '''T/F flag to let Loads know to use the actual value in the curve rather than use the value as a multiplier.'''
        return self._lib.LoadShapes_Get_UseActual() != 0

    @UseActual.setter
    def UseActual(self, Value):
        self._lib.LoadShapes_Set_UseActual(Value)
        self.CheckForError()

    @property
    def sInterval(self):
        return self._lib.LoadShapes_Get_sInterval()

    @sInterval.setter
    def sInterval(self, Value):
        self._lib.LoadShapes_Set_Sinterval(Value)
        self.CheckForError()

    Sinterval = sInterval

    def __iter__(self):
        idx = self.First
        while idx != 0:
            yield self
            idx = self.Next

