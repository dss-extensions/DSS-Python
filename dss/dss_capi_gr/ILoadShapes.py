'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2019 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Iterable

class ILoadShapes(Iterable):
    __slots__ = []

    def New(self, Name):
        if type(Name) is not bytes:
            Name = Name.encode(self._api_util.codec)

        return self._lib.LoadShapes_New(Name)

    def Normalize(self):
        self._lib.LoadShapes_Normalize()

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
        '''Array of doubles for the P multiplier in the Loadshape.'''
        self._lib.LoadShapes_Get_Pmult_GR()
        return self._get_float64_gr_array()

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
        self._lib.LoadShapes_Get_Qmult_GR()
        return self._get_float64_gr_array()

    @Qmult.setter
    def Qmult(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.LoadShapes_Set_Qmult(ValuePtr, ValueCount)
        self.CheckForError()

    @property
    def TimeArray(self):
        '''Time array in hours correscponding to P and Q multipliers when the Interval=0.'''
        self._lib.LoadShapes_Get_TimeArray_GR()
        return self._get_float64_gr_array()

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
