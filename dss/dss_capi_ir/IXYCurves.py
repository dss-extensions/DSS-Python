'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class IXYCurves(Base):
    __slots__ = []

    @property
    def Count(self):
        '''(read-only) Number of XYCurve Objects'''
        return self._lib.XYCurves_Get_Count()

    def __len__(self):
        return self._lib.XYCurves_Get_Count()

    @property
    def First(self):
        '''(read-only) Sets first XYcurve object active; returns 0 if none.'''
        return self._lib.XYCurves_Get_First()

    @property
    def Name(self):
        '''
        (read) Name of active XYCurve Object
        (write) Get Name of active XYCurve Object
        '''
        return self._get_string(self._lib.XYCurves_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.XYCurves_Set_Name(Value)
        self.CheckForError()

    @property
    def Next(self):
        '''(read-only) Advances to next XYCurve object; returns 0 if no more objects of this class'''
        return self._lib.XYCurves_Get_Next()

    @property
    def Npts(self):
        '''Get/Set Number of points in X-Y curve'''
        return self._lib.XYCurves_Get_Npts()

    @Npts.setter
    def Npts(self, Value):
        self._lib.XYCurves_Set_Npts(Value)
        self.CheckForError()

    @property
    def Xarray(self):
        '''Get/Set X values as a Array of doubles. Set Npts to max number expected if setting'''
        return self._get_float64_array(self._lib.XYCurves_Get_Xarray)

    @Xarray.setter
    def Xarray(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.XYCurves_Set_Xarray(ValuePtr, ValueCount)
        self.CheckForError()

    @property
    def Xscale(self):
        '''Factor to scale X values from original curve'''
        return self._lib.XYCurves_Get_Xscale()

    @Xscale.setter
    def Xscale(self, Value):
        self._lib.XYCurves_Set_Xscale(Value)
        self.CheckForError()

    @property
    def Xshift(self):
        '''Amount to shift X value from original curve'''
        return self._lib.XYCurves_Get_Xshift()

    @Xshift.setter
    def Xshift(self, Value):
        self._lib.XYCurves_Set_Xshift(Value)
        self.CheckForError()

    @property
    def Yarray(self):
        '''Get/Set Y values in curve; Set Npts to max number expected if setting'''
        return self._get_float64_array(self._lib.XYCurves_Get_Yarray)

    @Yarray.setter
    def Yarray(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.XYCurves_Set_Yarray(ValuePtr, ValueCount)
        self.CheckForError()

    @property
    def Yscale(self):
        '''
        (read) Factor to scale Y values from original curve
        (write) Amount to scale Y values from original curve. Represents a curve shift.
        '''
        return self._lib.XYCurves_Get_Yscale()

    @Yscale.setter
    def Yscale(self, Value):
        self._lib.XYCurves_Set_Yscale(Value)
        self.CheckForError()

    @property
    def Yshift(self):
        '''amount to shift Y valiue from original curve'''
        return self._lib.XYCurves_Get_Yshift()

    @Yshift.setter
    def Yshift(self, Value):
        self._lib.XYCurves_Set_Yshift(Value)
        self.CheckForError()

    @property
    def x(self):
        '''Set X value or get interpolated value after setting Y'''
        return self._lib.XYCurves_Get_x()

    @x.setter
    def x(self, Value):
        self._lib.XYCurves_Set_x(Value)
        self.CheckForError()

    @property
    def y(self):
        '''
        (read) Y value for present X or set this value then get corresponding X
        (write) Set Y value or get interpolated Y value after setting X
        '''
        return self._lib.XYCurves_Get_y()

    @y.setter
    def y(self, Value):
        self._lib.XYCurves_Set_y(Value)
        self.CheckForError()

    def __iter__(self):
        idx = self.First
        while idx != 0:
            yield self
            idx = self.Next

