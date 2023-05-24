'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira

Copyright (c) 2018-2022 DSS-Extensions contributors
'''
from ._cffi_api_util import Iterable
from ._types import Float64Array

class IXYCurves(Iterable):
    __slots__ = []

    _columns = [
        'Name',
        'idx',
        'Npts',
        'Xarray',
        'Xscale',
        'Xshift',
        'Yarray',
        'Yscale',
        'Yshift',
        'x',
        'y',
    ]

    @property
    def Npts(self) -> int:
        '''Get/Set Number of points in X-Y curve'''
        return self.CheckForError(self._lib.XYCurves_Get_Npts())

    @Npts.setter
    def Npts(self, Value: int):
        self.CheckForError(self._lib.XYCurves_Set_Npts(Value))

    @property
    def Xarray(self) -> Float64Array:
        '''Get/set X values as a Array of doubles. Set Npts to max number expected if setting'''
        self.CheckForError(self._lib.XYCurves_Get_Xarray_GR())
        return self._get_float64_gr_array()

    @Xarray.setter
    def Xarray(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.XYCurves_Set_Xarray(ValuePtr, ValueCount))

    @property
    def Xscale(self) -> float:
        '''Factor to scale X values from original curve'''
        return self.CheckForError(self._lib.XYCurves_Get_Xscale())

    @Xscale.setter
    def Xscale(self, Value: float):
        self.CheckForError(self._lib.XYCurves_Set_Xscale(Value))

    @property
    def Xshift(self) -> float:
        '''Amount to shift X value from original curve'''
        return self.CheckForError(self._lib.XYCurves_Get_Xshift())

    @Xshift.setter
    def Xshift(self, Value: float):
        self.CheckForError(self._lib.XYCurves_Set_Xshift(Value))

    @property
    def Yarray(self) -> Float64Array:
        '''Get/Set Y values in curve; Set Npts to max number expected if setting'''
        self.CheckForError(self._lib.XYCurves_Get_Yarray_GR())
        return self._get_float64_gr_array()

    @Yarray.setter
    def Yarray(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.XYCurves_Set_Yarray(ValuePtr, ValueCount))

    @property
    def Yscale(self) -> float:
        '''Factor to scale Y values from original curve'''
        return self.CheckForError(self._lib.XYCurves_Get_Yscale())

    @Yscale.setter
    def Yscale(self, Value: float):
        self.CheckForError(self._lib.XYCurves_Set_Yscale(Value))

    @property
    def Yshift(self) -> float:
        '''Amount to shift Y value from original curve'''
        return self.CheckForError(self._lib.XYCurves_Get_Yshift())

    @Yshift.setter
    def Yshift(self, Value: float):
        self.CheckForError(self._lib.XYCurves_Set_Yshift(Value))

    @property
    def x(self) -> float:
        '''Set X value or get interpolated value after setting Y'''
        return self.CheckForError(self._lib.XYCurves_Get_x())

    @x.setter
    def x(self, Value: float):
        self.CheckForError(self._lib.XYCurves_Set_x(Value))

    @property
    def y(self) -> float:
        '''Set Y value or get interpolated Y value after setting X'''
        return self.CheckForError(self._lib.XYCurves_Get_y())

    @y.setter
    def y(self, Value: float):
        self.CheckForError(self._lib.XYCurves_Set_y(Value))
