# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from typing_extensions import TypedDict, Unpack
from ._obj_bases import (
    BatchFloat64ArrayProxy,
    BatchInt32ArrayProxy,
    DSSObj,
    DSSBatch,
    IDSSObj,
    LIST_LIKE,
    # NotSet,
)
from .._types import Float64Array, Int32Array
from .._cffi_api_util import Base
from . import enums

class XYcurve(DSSObj):
    __slots__ = []
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

    @property
    def NPts(self) -> int:
        """
        Max number of points to expect in curve. This could get reset to the actual number of points defined if less than specified.

        DSS property name: `NPts`, DSS property index: 1.
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @NPts.setter
    def NPts(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def YArray(self) -> Float64Array:
        """
        Alternate way to enter Y values. Enter an array of Y values corresponding to the X values.  You can also use the syntax: 
        Yarray = (file=filename)     !for text file one value per line
        Yarray = (dblfile=filename)  !for packed file of doubles
        Yarray = (sngfile=filename)  !for packed file of singles 

        Note: this property will reset Npts to a smaller value if the  number of values in the files are fewer.

        DSS property name: `YArray`, DSS property index: 3.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 3)

    @YArray.setter
    def YArray(self, value: Float64Array):
        self._set_float64_array_o(3, value)

    @property
    def XArray(self) -> Float64Array:
        """
        Alternate way to enter X values. Enter an array of X values corresponding to the Y values.  You can also use the syntax: 
        Xarray = (file=filename)     !for text file one value per line
        Xarray = (dblfile=filename)  !for packed file of doubles
        Xarray = (sngfile=filename)  !for packed file of singles 

        Note: this property will reset Npts to a smaller value if the  number of values in the files are fewer.

        DSS property name: `XArray`, DSS property index: 4.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 4)

    @XArray.setter
    def XArray(self, value: Float64Array):
        self._set_float64_array_o(4, value)

    @property
    def CSVFile(self) -> str:
        """
        Switch input of  X-Y curve data to a CSV file containing X, Y points one per line. NOTE: This action may reset the number of points to a lower value.

        DSS property name: `CSVFile`, DSS property index: 5.
        """
        return self._get_prop_string(5)

    @CSVFile.setter
    def CSVFile(self, value: AnyStr):
        self._set_string_o(5, value)

    @property
    def SngFile(self) -> str:
        """
        Switch input of  X-Y curve data to a binary file of SINGLES containing X, Y points packed one after another. NOTE: This action may reset the number of points to a lower value.

        DSS property name: `SngFile`, DSS property index: 6.
        """
        return self._get_prop_string(6)

    @SngFile.setter
    def SngFile(self, value: AnyStr):
        self._set_string_o(6, value)

    @property
    def DblFile(self) -> str:
        """
        Switch input of  X-Y  curve data to a binary file of DOUBLES containing X, Y points packed one after another. NOTE: This action may reset the number of points to a lower value.

        DSS property name: `DblFile`, DSS property index: 7.
        """
        return self._get_prop_string(7)

    @DblFile.setter
    def DblFile(self, value: AnyStr):
        self._set_string_o(7, value)

    @property
    def X(self) -> float:
        """
        Enter a value and then retrieve the interpolated Y value from the Y property. On input shifted then scaled to original curve. Scaled then shifted on output.

        DSS property name: `X`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @X.setter
    def X(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def Y(self) -> float:
        """
        Enter a value and then retrieve the interpolated X value from the X property. On input shifted then scaled to original curve. Scaled then shifted on output.

        DSS property name: `Y`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @Y.setter
    def Y(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def XShift(self) -> float:
        """
        Shift X property values (in/out) by this amount of offset. Default = 0. Does not change original definition of arrays.

        DSS property name: `XShift`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @XShift.setter
    def XShift(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def YShift(self) -> float:
        """
        Shift Y property values (in/out) by this amount of offset. Default = 0. Does not change original definition of arrays.

        DSS property name: `YShift`, DSS property index: 11.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @YShift.setter
    def YShift(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def XScale(self) -> float:
        """
        Scale X property values (in/out) by this factor. Default = 1.0. Does not change original definition of arrays.

        DSS property name: `XScale`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @XScale.setter
    def XScale(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def YScale(self) -> float:
        """
        Scale Y property values (in/out) by this factor. Default = 1.0. Does not change original definition of arrays.

        DSS property name: `YScale`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @YScale.setter
    def YScale(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

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


    @property
    def NPts(self) -> BatchInt32ArrayProxy:
        """
        Max number of points to expect in curve. This could get reset to the actual number of points defined if less than specified.

        DSS property name: `NPts`, DSS property index: 1.
        """
        return BatchInt32ArrayProxy(self, 1)

    @NPts.setter
    def NPts(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(1, value)

    @property
    def YArray(self) -> List[Float64Array]:
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
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @YArray.setter
    def YArray(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(3, value)

    @property
    def XArray(self) -> List[Float64Array]:
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
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @XArray.setter
    def XArray(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(4, value)

    @property
    def CSVFile(self) -> List[str]:
        """
        Switch input of  X-Y curve data to a CSV file containing X, Y points one per line. NOTE: This action may reset the number of points to a lower value.

        DSS property name: `CSVFile`, DSS property index: 5.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 5) 

    @CSVFile.setter
    def CSVFile(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(5, value)

    @property
    def SngFile(self) -> List[str]:
        """
        Switch input of  X-Y curve data to a binary file of SINGLES containing X, Y points packed one after another. NOTE: This action may reset the number of points to a lower value.

        DSS property name: `SngFile`, DSS property index: 6.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 6) 

    @SngFile.setter
    def SngFile(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(6, value)

    @property
    def DblFile(self) -> List[str]:
        """
        Switch input of  X-Y  curve data to a binary file of DOUBLES containing X, Y points packed one after another. NOTE: This action may reset the number of points to a lower value.

        DSS property name: `DblFile`, DSS property index: 7.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 7) 

    @DblFile.setter
    def DblFile(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(7, value)

    @property
    def X(self) -> BatchFloat64ArrayProxy:
        """
        Enter a value and then retrieve the interpolated Y value from the Y property. On input shifted then scaled to original curve. Scaled then shifted on output.

        DSS property name: `X`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    @X.setter
    def X(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(8, value)

    @property
    def Y(self) -> BatchFloat64ArrayProxy:
        """
        Enter a value and then retrieve the interpolated X value from the X property. On input shifted then scaled to original curve. Scaled then shifted on output.

        DSS property name: `Y`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    @Y.setter
    def Y(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(9, value)

    @property
    def XShift(self) -> BatchFloat64ArrayProxy:
        """
        Shift X property values (in/out) by this amount of offset. Default = 0. Does not change original definition of arrays.

        DSS property name: `XShift`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    @XShift.setter
    def XShift(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(10, value)

    @property
    def YShift(self) -> BatchFloat64ArrayProxy:
        """
        Shift Y property values (in/out) by this amount of offset. Default = 0. Does not change original definition of arrays.

        DSS property name: `YShift`, DSS property index: 11.
        """
        return BatchFloat64ArrayProxy(self, 11)

    @YShift.setter
    def YShift(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(11, value)

    @property
    def XScale(self) -> BatchFloat64ArrayProxy:
        """
        Scale X property values (in/out) by this factor. Default = 1.0. Does not change original definition of arrays.

        DSS property name: `XScale`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    @XScale.setter
    def XScale(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(12, value)

    @property
    def YScale(self) -> BatchFloat64ArrayProxy:
        """
        Scale Y property values (in/out) by this factor. Default = 1.0. Does not change original definition of arrays.

        DSS property name: `YScale`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    @YScale.setter
    def YScale(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(13, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 14.
        """
        self._set_batch_string(14, value)

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

class IXYcurve(IDSSObj):
    __slots__ = ()

    def __init__(self, iobj):
        super().__init__(iobj, XYcurve, XYcurveBatch)

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> XYcurve:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[XYcurveProperties]) -> XYcurve:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[XYcurveBatchProperties]) -> XYcurveBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
