# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from typing_extensions import TypedDict, Unpack
from .types import Float64Array, Int32Array
from . import enums
from .DSSObj import IDSSObj, DSSObj
from .Batch import DSSBatch
from .ArrayProxy import BatchFloat64ArrayProxy, BatchInt32ArrayProxy

class XYcurve(DSSObj):
    __slots__ = DSSObj._extra_slots
    _cls_name = 'XYcurve'
    _cls_idx = 5
    _cls_prop_idx = {
        'npts': 1,
        'points': 2,
        'yarray': 3,
        'xarray': 4,
        'csvfile': 5,
        'sngfile': 6,
        'dblfile': 7,
        'x': 8,
        'y': 9,
        'xshift': 10,
        'yshift': 11,
        'xscale': 12,
        'yscale': 13,
        'like': 14,
    }


    def _get_NPts(self) -> int:
        """
        Max number of points to expect in curve. This could get reset to the actual number of points defined if less than specified.

        DSS property name: `NPts`, DSS property index: 1.
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    def _set_NPts(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 1, value, flags)

    NPts = property(_get_NPts, _set_NPts) # type: int

    def _get_YArray(self) -> Float64Array:
        """
        Alternate way to enter Y values. Enter an array of Y values corresponding to the X values.  You can also use the syntax: 
        Yarray = (file=filename)     !for text file one value per line
        Yarray = (dblfile=filename)  !for packed file of doubles
        Yarray = (sngfile=filename)  !for packed file of singles 

        Note: this property will reset Npts to a smaller value if the  number of values in the files are fewer.

        DSS property name: `YArray`, DSS property index: 3.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 3)

    def _set_YArray(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(3, value, flags)

    YArray = property(_get_YArray, _set_YArray) # type: Float64Array

    def _get_XArray(self) -> Float64Array:
        """
        Alternate way to enter X values. Enter an array of X values corresponding to the Y values.  You can also use the syntax: 
        Xarray = (file=filename)     !for text file one value per line
        Xarray = (dblfile=filename)  !for packed file of doubles
        Xarray = (sngfile=filename)  !for packed file of singles 

        Note: this property will reset Npts to a smaller value if the  number of values in the files are fewer.

        DSS property name: `XArray`, DSS property index: 4.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 4)

    def _set_XArray(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(4, value, flags)

    XArray = property(_get_XArray, _set_XArray) # type: Float64Array

    def _get_CSVFile(self) -> str:
        """
        Switch input of  X-Y curve data to a CSV file containing X, Y points one per line. NOTE: This action may reset the number of points to a lower value.

        DSS property name: `CSVFile`, DSS property index: 5.
        """
        return self._get_prop_string(5)

    def _set_CSVFile(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(5, value, flags)

    CSVFile = property(_get_CSVFile, _set_CSVFile) # type: str

    def _get_SngFile(self) -> str:
        """
        Switch input of  X-Y curve data to a binary file of SINGLES containing X, Y points packed one after another. NOTE: This action may reset the number of points to a lower value.

        DSS property name: `SngFile`, DSS property index: 6.
        """
        return self._get_prop_string(6)

    def _set_SngFile(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(6, value, flags)

    SngFile = property(_get_SngFile, _set_SngFile) # type: str

    def _get_DblFile(self) -> str:
        """
        Switch input of  X-Y  curve data to a binary file of DOUBLES containing X, Y points packed one after another. NOTE: This action may reset the number of points to a lower value.

        DSS property name: `DblFile`, DSS property index: 7.
        """
        return self._get_prop_string(7)

    def _set_DblFile(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(7, value, flags)

    DblFile = property(_get_DblFile, _set_DblFile) # type: str

    def _get_X(self) -> float:
        """
        Enter a value and then retrieve the interpolated Y value from the Y property. On input shifted then scaled to original curve. Scaled then shifted on output.

        DSS property name: `X`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    def _set_X(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 8, value, flags)

    X = property(_get_X, _set_X) # type: float

    def _get_Y(self) -> float:
        """
        Enter a value and then retrieve the interpolated X value from the X property. On input shifted then scaled to original curve. Scaled then shifted on output.

        DSS property name: `Y`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    def _set_Y(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 9, value, flags)

    Y = property(_get_Y, _set_Y) # type: float

    def _get_XShift(self) -> float:
        """
        Shift X property values (in/out) by this amount of offset. Default = 0. Does not change original definition of arrays.

        DSS property name: `XShift`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    def _set_XShift(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 10, value, flags)

    XShift = property(_get_XShift, _set_XShift) # type: float

    def _get_YShift(self) -> float:
        """
        Shift Y property values (in/out) by this amount of offset. Default = 0. Does not change original definition of arrays.

        DSS property name: `YShift`, DSS property index: 11.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    def _set_YShift(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 11, value, flags)

    YShift = property(_get_YShift, _set_YShift) # type: float

    def _get_XScale(self) -> float:
        """
        Scale X property values (in/out) by this factor. Default = 1.0. Does not change original definition of arrays.

        DSS property name: `XScale`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    def _set_XScale(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 12, value, flags)

    XScale = property(_get_XScale, _set_XScale) # type: float

    def _get_YScale(self) -> float:
        """
        Scale Y property values (in/out) by this factor. Default = 1.0. Does not change original definition of arrays.

        DSS property name: `YScale`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    def _set_YScale(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 13, value, flags)

    YScale = property(_get_YScale, _set_YScale) # type: float

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 14.
        """
        self._set_string_o(14, value)


class XYcurveProperties(TypedDict):
    NPts: int
    YArray: Float64Array
    XArray: Float64Array
    CSVFile: AnyStr
    SngFile: AnyStr
    DblFile: AnyStr
    X: float
    Y: float
    XShift: float
    YShift: float
    XScale: float
    YScale: float
    Like: AnyStr

class XYcurveBatch(DSSBatch):
    _cls_name = 'XYcurve'
    _obj_cls = XYcurve
    _cls_idx = 5


    def _get_NPts(self) -> BatchInt32ArrayProxy:
        """
        Max number of points to expect in curve. This could get reset to the actual number of points defined if less than specified.

        DSS property name: `NPts`, DSS property index: 1.
        """
        return BatchInt32ArrayProxy(self, 1)

    def _set_NPts(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(1, value, flags)

    NPts = property(_get_NPts, _set_NPts) # type: BatchInt32ArrayProxy

    def _get_YArray(self) -> List[Float64Array]:
        """
        Alternate way to enter Y values. Enter an array of Y values corresponding to the X values.  You can also use the syntax: 
        Yarray = (file=filename)     !for text file one value per line
        Yarray = (dblfile=filename)  !for packed file of doubles
        Yarray = (sngfile=filename)  !for packed file of singles 

        Note: this property will reset Npts to a smaller value if the  number of values in the files are fewer.

        DSS property name: `YArray`, DSS property index: 3.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 3)
            for x in self._unpack()
        ]

    def _set_YArray(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(3, value, flags)

    YArray = property(_get_YArray, _set_YArray) # type: List[Float64Array]

    def _get_XArray(self) -> List[Float64Array]:
        """
        Alternate way to enter X values. Enter an array of X values corresponding to the Y values.  You can also use the syntax: 
        Xarray = (file=filename)     !for text file one value per line
        Xarray = (dblfile=filename)  !for packed file of doubles
        Xarray = (sngfile=filename)  !for packed file of singles 

        Note: this property will reset Npts to a smaller value if the  number of values in the files are fewer.

        DSS property name: `XArray`, DSS property index: 4.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 4)
            for x in self._unpack()
        ]

    def _set_XArray(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(4, value, flags)

    XArray = property(_get_XArray, _set_XArray) # type: List[Float64Array]

    def _get_CSVFile(self) -> List[str]:
        """
        Switch input of  X-Y curve data to a CSV file containing X, Y points one per line. NOTE: This action may reset the number of points to a lower value.

        DSS property name: `CSVFile`, DSS property index: 5.
        """
        return self._get_batch_str_prop(5)

    def _set_CSVFile(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(5, value, flags)

    CSVFile = property(_get_CSVFile, _set_CSVFile) # type: List[str]

    def _get_SngFile(self) -> List[str]:
        """
        Switch input of  X-Y curve data to a binary file of SINGLES containing X, Y points packed one after another. NOTE: This action may reset the number of points to a lower value.

        DSS property name: `SngFile`, DSS property index: 6.
        """
        return self._get_batch_str_prop(6)

    def _set_SngFile(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(6, value, flags)

    SngFile = property(_get_SngFile, _set_SngFile) # type: List[str]

    def _get_DblFile(self) -> List[str]:
        """
        Switch input of  X-Y  curve data to a binary file of DOUBLES containing X, Y points packed one after another. NOTE: This action may reset the number of points to a lower value.

        DSS property name: `DblFile`, DSS property index: 7.
        """
        return self._get_batch_str_prop(7)

    def _set_DblFile(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(7, value, flags)

    DblFile = property(_get_DblFile, _set_DblFile) # type: List[str]

    def _get_X(self) -> BatchFloat64ArrayProxy:
        """
        Enter a value and then retrieve the interpolated Y value from the Y property. On input shifted then scaled to original curve. Scaled then shifted on output.

        DSS property name: `X`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    def _set_X(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(8, value, flags)

    X = property(_get_X, _set_X) # type: BatchFloat64ArrayProxy

    def _get_Y(self) -> BatchFloat64ArrayProxy:
        """
        Enter a value and then retrieve the interpolated X value from the X property. On input shifted then scaled to original curve. Scaled then shifted on output.

        DSS property name: `Y`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    def _set_Y(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(9, value, flags)

    Y = property(_get_Y, _set_Y) # type: BatchFloat64ArrayProxy

    def _get_XShift(self) -> BatchFloat64ArrayProxy:
        """
        Shift X property values (in/out) by this amount of offset. Default = 0. Does not change original definition of arrays.

        DSS property name: `XShift`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    def _set_XShift(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(10, value, flags)

    XShift = property(_get_XShift, _set_XShift) # type: BatchFloat64ArrayProxy

    def _get_YShift(self) -> BatchFloat64ArrayProxy:
        """
        Shift Y property values (in/out) by this amount of offset. Default = 0. Does not change original definition of arrays.

        DSS property name: `YShift`, DSS property index: 11.
        """
        return BatchFloat64ArrayProxy(self, 11)

    def _set_YShift(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(11, value, flags)

    YShift = property(_get_YShift, _set_YShift) # type: BatchFloat64ArrayProxy

    def _get_XScale(self) -> BatchFloat64ArrayProxy:
        """
        Scale X property values (in/out) by this factor. Default = 1.0. Does not change original definition of arrays.

        DSS property name: `XScale`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    def _set_XScale(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(12, value, flags)

    XScale = property(_get_XScale, _set_XScale) # type: BatchFloat64ArrayProxy

    def _get_YScale(self) -> BatchFloat64ArrayProxy:
        """
        Scale Y property values (in/out) by this factor. Default = 1.0. Does not change original definition of arrays.

        DSS property name: `YScale`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    def _set_YScale(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(13, value, flags)

    YScale = property(_get_YScale, _set_YScale) # type: BatchFloat64ArrayProxy

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 14.
        """
        self._set_batch_string(14, value, flags)

class XYcurveBatchProperties(TypedDict):
    NPts: Union[int, Int32Array]
    YArray: Float64Array
    XArray: Float64Array
    CSVFile: Union[AnyStr, List[AnyStr]]
    SngFile: Union[AnyStr, List[AnyStr]]
    DblFile: Union[AnyStr, List[AnyStr]]
    X: Union[float, Float64Array]
    Y: Union[float, Float64Array]
    XShift: Union[float, Float64Array]
    YShift: Union[float, Float64Array]
    XScale: Union[float, Float64Array]
    YScale: Union[float, Float64Array]
    Like: AnyStr

class IXYcurve(IDSSObj, XYcurveBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, XYcurve, XYcurveBatch)
        XYcurveBatch.__init__(self, self._api_util, sync_cls_idx=XYcurve._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> XYcurve:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[XYcurveProperties]) -> XYcurve:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[XYcurveBatchProperties]) -> XYcurveBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
