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

class GrowthShape(DSSObj):
    __slots__ = []
    _cls_name = 'GrowthShape'
    _cls_idx = 6
    _cls_prop_idx = {
        'npts': 1,
        'year': 2,
        'mult': 3,
        'csvfile': 4,
        'sngfile': 5,
        'dblfile': 6,
        'like': 7,
    }

    def _get_NPts(self) -> int:
        """
        Number of points to expect in subsequent vector.

        DSS property name: `NPts`, DSS property index: 1.
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    def _set_NPts(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    NPts = property(_get_NPts, _set_NPts)

    def _get_Year(self) -> Float64Array:
        """
        Array of year values, or a text file spec, corresponding to the multipliers. Enter only those years where the growth changes. May be any integer sequence -- just so it is consistent. See help on Mult.

        DSS property name: `Year`, DSS property index: 2.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 2)

    def _set_Year(self, value: Float64Array):
        self._set_float64_array_o(2, value)

    Year = property(_get_Year, _set_Year)

    def _get_Mult(self) -> Float64Array:
        """
        Array of growth multiplier values, or a text file spec, corresponding to the year values. Enter the multiplier by which you would multiply the previous year's load to get the present year's.

        Examples:

          Year = [1, 2, 5]   Mult=[1.05, 1.025, 1.02].
          Year= (File=years.txt) Mult= (file=mults.txt).

        Text files contain one value per line.

        DSS property name: `Mult`, DSS property index: 3.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 3)

    def _set_Mult(self, value: Float64Array):
        self._set_float64_array_o(3, value)

    Mult = property(_get_Mult, _set_Mult)

    def _get_CSVFile(self) -> str:
        """
        Switch input of growth curve data to a csv file containing (year, mult) points, one per line.

        DSS property name: `CSVFile`, DSS property index: 4.
        """
        return self._get_prop_string(4)

    def _set_CSVFile(self, value: AnyStr):
        self._set_string_o(4, value)

    CSVFile = property(_get_CSVFile, _set_CSVFile)

    def _get_SngFile(self) -> str:
        """
        Switch input of growth curve data to a binary file of singles containing (year, mult) points, packed one after another.

        DSS property name: `SngFile`, DSS property index: 5.
        """
        return self._get_prop_string(5)

    def _set_SngFile(self, value: AnyStr):
        self._set_string_o(5, value)

    SngFile = property(_get_SngFile, _set_SngFile)

    def _get_DblFile(self) -> str:
        """
        Switch input of growth curve data to a binary file of doubles containing (year, mult) points, packed one after another.

        DSS property name: `DblFile`, DSS property index: 6.
        """
        return self._get_prop_string(6)

    def _set_DblFile(self, value: AnyStr):
        self._set_string_o(6, value)

    DblFile = property(_get_DblFile, _set_DblFile)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 7.
        """
        self._set_string_o(7, value)


class GrowthShapeProperties(TypedDict):
    NPts: int
    Year: Float64Array
    Mult: Float64Array
    CSVFile: AnyStr
    SngFile: AnyStr
    DblFile: AnyStr
    Like: AnyStr

class GrowthShapeBatch(DSSBatch):
    _cls_name = 'GrowthShape'
    _obj_cls = GrowthShape
    _cls_idx = 6


    def _get_NPts(self) -> BatchInt32ArrayProxy:
        """
        Number of points to expect in subsequent vector.

        DSS property name: `NPts`, DSS property index: 1.
        """
        return BatchInt32ArrayProxy(self, 1)

    def _set_NPts(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(1, value)

    NPts = property(_get_NPts, _set_NPts)

    def _get_Year(self) -> List[Float64Array]:
        """
        Array of year values, or a text file spec, corresponding to the multipliers. Enter only those years where the growth changes. May be any integer sequence -- just so it is consistent. See help on Mult.

        DSS property name: `Year`, DSS property index: 2.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 2)
            for x in self._unpack()
        ]

    def _set_Year(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(2, value)

    Year = property(_get_Year, _set_Year)

    def _get_Mult(self) -> List[Float64Array]:
        """
        Array of growth multiplier values, or a text file spec, corresponding to the year values. Enter the multiplier by which you would multiply the previous year's load to get the present year's.

        Examples:

          Year = [1, 2, 5]   Mult=[1.05, 1.025, 1.02].
          Year= (File=years.txt) Mult= (file=mults.txt).

        Text files contain one value per line.

        DSS property name: `Mult`, DSS property index: 3.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 3)
            for x in self._unpack()
        ]

    def _set_Mult(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(3, value)

    Mult = property(_get_Mult, _set_Mult)

    def _get_CSVFile(self) -> List[str]:
        """
        Switch input of growth curve data to a csv file containing (year, mult) points, one per line.

        DSS property name: `CSVFile`, DSS property index: 4.
        """
        return self._get_batch_str_prop(4)

    def _set_CSVFile(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(4, value)

    CSVFile = property(_get_CSVFile, _set_CSVFile)

    def _get_SngFile(self) -> List[str]:
        """
        Switch input of growth curve data to a binary file of singles containing (year, mult) points, packed one after another.

        DSS property name: `SngFile`, DSS property index: 5.
        """
        return self._get_batch_str_prop(5)

    def _set_SngFile(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(5, value)

    SngFile = property(_get_SngFile, _set_SngFile)

    def _get_DblFile(self) -> List[str]:
        """
        Switch input of growth curve data to a binary file of doubles containing (year, mult) points, packed one after another.

        DSS property name: `DblFile`, DSS property index: 6.
        """
        return self._get_batch_str_prop(6)

    def _set_DblFile(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(6, value)

    DblFile = property(_get_DblFile, _set_DblFile)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 7.
        """
        self._set_batch_string(7, value)

class GrowthShapeBatchProperties(TypedDict):
    NPts: Union[int, Int32Array]
    Year: Float64Array
    Mult: Float64Array
    CSVFile: Union[AnyStr, List[AnyStr]]
    SngFile: Union[AnyStr, List[AnyStr]]
    DblFile: Union[AnyStr, List[AnyStr]]
    Like: AnyStr

class IGrowthShape(IDSSObj,GrowthShapeBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, GrowthShape, GrowthShapeBatch)
        GrowthShapeBatch.__init__(self, self._api_util, sync_cls=True)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> GrowthShape:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[GrowthShapeProperties]) -> GrowthShape:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[GrowthShapeBatchProperties]) -> GrowthShapeBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
