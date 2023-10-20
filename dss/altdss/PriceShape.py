# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from enum import IntEnum
from typing_extensions import TypedDict, Unpack
import numpy as np
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

class PriceShape(DSSObj, ):
    __slots__ = []
    _cls_name = 'PriceShape'
    _cls_idx = 4
    _cls_prop_idx = {
        'npts': 1,
        'interval': 2,
        'price': 3,
        'hour': 4,
        'mean': 5,
        'stddev': 6,
        'csvfile': 7,
        'sngfile': 8,
        'dblfile': 9,
        'sinterval': 10,
        'minterval': 11,
        'action': 12,
        'like': 13,
    }

    @property
    def NPts(self) -> int:
        """
        Max number of points to expect in price shape vectors. This gets reset to the number of Price values found if less than specified.

        DSS property name: `NPts`, DSS property index: 1.
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @NPts.setter
    def NPts(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def Interval(self) -> float:
        """
        Time interval for fixed interval data, hrs. Default = 1. If Interval = 0 then time data (in hours) may be at irregular intervals and time value must be specified using either the Hour property or input files. Then values are interpolated when Interval=0, but not for fixed interval data.  

        See also "sinterval" and "minterval".

        DSS property name: `Interval`, DSS property index: 2.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 2)

    @Interval.setter
    def Interval(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 2, value)

    @property
    def Price(self) -> Float64Array:
        """
        Array of Price values.  Units should be compatible with the object using the data. You can also use the syntax: 
        Price = (file=filename)     !for text file one value per line
        Price = (dblfile=filename)  !for packed file of doubles
        Price = (sngfile=filename)  !for packed file of singles 

        Note: this property will reset Npts if the  number of values in the files are fewer.

        DSS property name: `Price`, DSS property index: 3.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 3)

    @Price.setter
    def Price(self, value: Float64Array):
        self._set_float64_array_o(3, value)

    @property
    def Hour(self) -> Float64Array:
        """
        Array of hour values. Only necessary to define this property for variable interval data. If the data are fixed interval, do not use this property. You can also use the syntax: 
        hour = (file=filename)     !for text file one value per line
        hour = (dblfile=filename)  !for packed file of doubles
        hour = (sngfile=filename)  !for packed file of singles 

        DSS property name: `Hour`, DSS property index: 4.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 4)

    @Hour.setter
    def Hour(self, value: Float64Array):
        self._set_float64_array_o(4, value)

    @property
    def Mean(self) -> float:
        """
        Mean of the Price curve values.  This is computed on demand the first time a value is needed.  However, you may set it to another value independently. Used for Monte Carlo load simulations.

        DSS property name: `Mean`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @Mean.setter
    def Mean(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def StdDev(self) -> float:
        """
        Standard deviation of the Prices.  This is computed on demand the first time a value is needed.  However, you may set it to another value independently.Is overwritten if you subsequently read in a curve

        Used for Monte Carlo load simulations.

        DSS property name: `StdDev`, DSS property index: 6.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    @StdDev.setter
    def StdDev(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 6, value)

    @property
    def CSVFile(self) -> str:
        """
        Switch input of  Price curve data to a csv file containing (hour, Price) points, or simply (Price) values for fixed time interval data, one per line. NOTE: This action may reset the number of points to a lower value.

        DSS property name: `CSVFile`, DSS property index: 7.
        """
        return self._get_prop_string(7)

    @CSVFile.setter
    def CSVFile(self, value: AnyStr):
        self._set_string_o(7, value)

    @property
    def SngFile(self) -> str:
        """
        Switch input of  Price curve data to a binary file of singles containing (hour, Price) points, or simply (Price) values for fixed time interval data, packed one after another. NOTE: This action may reset the number of points to a lower value.

        DSS property name: `SngFile`, DSS property index: 8.
        """
        return self._get_prop_string(8)

    @SngFile.setter
    def SngFile(self, value: AnyStr):
        self._set_string_o(8, value)

    @property
    def DblFile(self) -> str:
        """
        Switch input of  Price curve data to a binary file of doubles containing (hour, Price) points, or simply (Price) values for fixed time interval data, packed one after another. NOTE: This action may reset the number of points to a lower value.

        DSS property name: `DblFile`, DSS property index: 9.
        """
        return self._get_prop_string(9)

    @DblFile.setter
    def DblFile(self, value: AnyStr):
        self._set_string_o(9, value)

    @property
    def SInterval(self) -> float:
        """
        Specify fixed interval in SECONDS. Alternate way to specify Interval property.

        DSS property name: `SInterval`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @SInterval.setter
    def SInterval(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def MInterval(self) -> float:
        """
        Specify fixed interval in MINUTES. Alternate way to specify Interval property.

        DSS property name: `MInterval`, DSS property index: 11.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @MInterval.setter
    def MInterval(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    def Action(self, value: Union[str, bytes, int, enums.PriceShapeAction]):
        """
        {DblSave | SngSave} After defining Price curve data... Setting action=DblSave or SngSave will cause the present "Price" values to be written to either a packed file of double or single. The filename is the PriceShape name. 

        DSS property name: `Action`, DSS property index: 12.
        """
        if isinstance(value, int):
            self._lib.Obj_SetInt32(self._ptr, 12, value)
            return
    
        self._set_string_o(12, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 13.
        """
        self._set_string_o(13, value)


class PriceShapeProperties(TypedDict):
    NPts: int
    Interval: float
    Price: Float64Array
    Hour: Float64Array
    Mean: float
    StdDev: float
    CSVFile: AnyStr
    SngFile: AnyStr
    DblFile: AnyStr
    SInterval: float
    MInterval: float
    Action: Union[str, bytes, int, enums.PriceShapeAction]
    Like: AnyStr

class PriceShapeBatch(DSSBatch):
    _cls_name = 'PriceShape'
    _obj_cls = PriceShape
    _cls_idx = 4


    @property
    def NPts(self) -> BatchInt32ArrayProxy:
        """
        Max number of points to expect in price shape vectors. This gets reset to the number of Price values found if less than specified.

        DSS property name: `NPts`, DSS property index: 1.
        """
        return BatchInt32ArrayProxy(self, 1)

    @NPts.setter
    def NPts(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(1, value)

    @property
    def Interval(self) -> BatchFloat64ArrayProxy:
        """
        Time interval for fixed interval data, hrs. Default = 1. If Interval = 0 then time data (in hours) may be at irregular intervals and time value must be specified using either the Hour property or input files. Then values are interpolated when Interval=0, but not for fixed interval data.  

        See also "sinterval" and "minterval".

        DSS property name: `Interval`, DSS property index: 2.
        """
        return BatchFloat64ArrayProxy(self, 2)

    @Interval.setter
    def Interval(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(2, value)

    @property
    def Price(self) -> List[Float64Array]:
        """
        Array of Price values.  Units should be compatible with the object using the data. You can also use the syntax: 
        Price = (file=filename)     !for text file one value per line
        Price = (dblfile=filename)  !for packed file of doubles
        Price = (sngfile=filename)  !for packed file of singles 

        Note: this property will reset Npts if the  number of values in the files are fewer.

        DSS property name: `Price`, DSS property index: 3.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 3)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Price.setter
    def Price(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(3, value)

    @property
    def Hour(self) -> List[Float64Array]:
        """
        Array of hour values. Only necessary to define this property for variable interval data. If the data are fixed interval, do not use this property. You can also use the syntax: 
        hour = (file=filename)     !for text file one value per line
        hour = (dblfile=filename)  !for packed file of doubles
        hour = (sngfile=filename)  !for packed file of singles 

        DSS property name: `Hour`, DSS property index: 4.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 4)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Hour.setter
    def Hour(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(4, value)

    @property
    def Mean(self) -> BatchFloat64ArrayProxy:
        """
        Mean of the Price curve values.  This is computed on demand the first time a value is needed.  However, you may set it to another value independently. Used for Monte Carlo load simulations.

        DSS property name: `Mean`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    @Mean.setter
    def Mean(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(5, value)

    @property
    def StdDev(self) -> BatchFloat64ArrayProxy:
        """
        Standard deviation of the Prices.  This is computed on demand the first time a value is needed.  However, you may set it to another value independently.Is overwritten if you subsequently read in a curve

        Used for Monte Carlo load simulations.

        DSS property name: `StdDev`, DSS property index: 6.
        """
        return BatchFloat64ArrayProxy(self, 6)

    @StdDev.setter
    def StdDev(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(6, value)

    @property
    def CSVFile(self) -> List[str]:
        """
        Switch input of  Price curve data to a csv file containing (hour, Price) points, or simply (Price) values for fixed time interval data, one per line. NOTE: This action may reset the number of points to a lower value.

        DSS property name: `CSVFile`, DSS property index: 7.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 7) 

    @CSVFile.setter
    def CSVFile(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(7, value)

    @property
    def SngFile(self) -> List[str]:
        """
        Switch input of  Price curve data to a binary file of singles containing (hour, Price) points, or simply (Price) values for fixed time interval data, packed one after another. NOTE: This action may reset the number of points to a lower value.

        DSS property name: `SngFile`, DSS property index: 8.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 8) 

    @SngFile.setter
    def SngFile(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(8, value)

    @property
    def DblFile(self) -> List[str]:
        """
        Switch input of  Price curve data to a binary file of doubles containing (hour, Price) points, or simply (Price) values for fixed time interval data, packed one after another. NOTE: This action may reset the number of points to a lower value.

        DSS property name: `DblFile`, DSS property index: 9.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 9) 

    @DblFile.setter
    def DblFile(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(9, value)

    @property
    def SInterval(self) -> BatchFloat64ArrayProxy:
        """
        Specify fixed interval in SECONDS. Alternate way to specify Interval property.

        DSS property name: `SInterval`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    @SInterval.setter
    def SInterval(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(10, value)

    @property
    def MInterval(self) -> BatchFloat64ArrayProxy:
        """
        Specify fixed interval in MINUTES. Alternate way to specify Interval property.

        DSS property name: `MInterval`, DSS property index: 11.
        """
        return BatchFloat64ArrayProxy(self, 11)

    @MInterval.setter
    def MInterval(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(11, value)

    def Action(self, value: Union[str, bytes, int, enums.PriceShapeAction]):
        """
        {DblSave | SngSave} After defining Price curve data... Setting action=DblSave or SngSave will cause the present "Price" values to be written to either a packed file of double or single. The filename is the PriceShape name. 

        DSS property name: `Action`, DSS property index: 12.
        """
        if isinstance(value, (bytes, str)) or (isinstance(value, LIST_LIKE) and len(value) > 0 and isinstance(value[0], (bytes, str))):
            self._set_batch_string(12, value)
        else:
            self._set_batch_int32_array(12, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 13.
        """
        self._set_batch_string(13, value)

class PriceShapeBatchProperties(TypedDict):
    NPts: Union[int, Int32Array]
    Interval: Union[float, Float64Array]
    Price: Float64Array
    Hour: Float64Array
    Mean: Union[float, Float64Array]
    StdDev: Union[float, Float64Array]
    CSVFile: Union[AnyStr, List[AnyStr]]
    SngFile: Union[AnyStr, List[AnyStr]]
    DblFile: Union[AnyStr, List[AnyStr]]
    SInterval: Union[float, Float64Array]
    MInterval: Union[float, Float64Array]
    Action: Union[str, bytes, int, enums.PriceShapeAction]
    Like: AnyStr

class IPriceShape(IDSSObj):
    def __init__(self, iobj):
        super().__init__(iobj, PriceShape, PriceShapeBatch)

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> PriceShape:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[PriceShapeProperties]) -> PriceShape:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[PriceShapeBatchProperties]) -> PriceShapeBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
