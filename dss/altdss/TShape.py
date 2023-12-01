# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from typing_extensions import TypedDict, Unpack
from .types import Float64Array, Int32Array
from . import enums
from .DSSObj import IDSSObj, DSSObj
from .Batch import DSSBatch
from .ArrayProxy import BatchFloat64ArrayProxy, BatchInt32ArrayProxy
from .common import LIST_LIKE

class TShape(DSSObj):
    __slots__ = DSSObj._extra_slots
    _cls_name = 'TShape'
    _cls_idx = 3
    _cls_prop_idx = {
        'npts': 1,
        'interval': 2,
        'temp': 3,
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


    def _get_NPts(self) -> int:
        """
        Max number of points to expect in temperature shape vectors. This gets reset to the number of Temperature values found if less than specified.

        DSS property name: `NPts`, DSS property index: 1.
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    def _set_NPts(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 1, value, flags)

    NPts = property(_get_NPts, _set_NPts) # type: int

    def _get_Interval(self) -> float:
        """
        Time interval for fixed interval data, hrs. Default = 1. If Interval = 0 then time data (in hours) may be at irregular intervals and time value must be specified using either the Hour property or input files. Then values are interpolated when Interval=0, but not for fixed interval data.  

        See also "sinterval" and "minterval".

        DSS property name: `Interval`, DSS property index: 2.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 2)

    def _set_Interval(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 2, value, flags)

    Interval = property(_get_Interval, _set_Interval) # type: float

    def _get_Temp(self) -> Float64Array:
        """
        Array of temperature values.  Units should be compatible with the object using the data. You can also use the syntax: 
        Temp = (file=filename)     !for text file one value per line
        Temp = (dblfile=filename)  !for packed file of doubles
        Temp = (sngfile=filename)  !for packed file of singles 

        Note: this property will reset Npts if the  number of values in the files are fewer.

        DSS property name: `Temp`, DSS property index: 3.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 3)

    def _set_Temp(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(3, value, flags)

    Temp = property(_get_Temp, _set_Temp) # type: Float64Array

    def _get_Hour(self) -> Float64Array:
        """
        Array of hour values. Only necessary to define this property for variable interval data. If the data are fixed interval, do not use this property. You can also use the syntax: 
        hour = (file=filename)     !for text file one value per line
        hour = (dblfile=filename)  !for packed file of doubles
        hour = (sngfile=filename)  !for packed file of singles 

        DSS property name: `Hour`, DSS property index: 4.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 4)

    def _set_Hour(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(4, value, flags)

    Hour = property(_get_Hour, _set_Hour) # type: Float64Array

    def _get_Mean(self) -> float:
        """
        Mean of the temperature curve values.  This is computed on demand the first time a value is needed.  However, you may set it to another value independently. Used for Monte Carlo load simulations.

        DSS property name: `Mean`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    def _set_Mean(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 5, value, flags)

    Mean = property(_get_Mean, _set_Mean) # type: float

    def _get_StdDev(self) -> float:
        """
        Standard deviation of the temperatures.  This is computed on demand the first time a value is needed.  However, you may set it to another value independently.Is overwritten if you subsequently read in a curve

        Used for Monte Carlo load simulations.

        DSS property name: `StdDev`, DSS property index: 6.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    def _set_StdDev(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 6, value, flags)

    StdDev = property(_get_StdDev, _set_StdDev) # type: float

    def _get_CSVFile(self) -> str:
        """
        Switch input of  temperature curve data to a csv file containing (hour, Temp) points, or simply (Temp) values for fixed time interval data, one per line. NOTE: This action may reset the number of points to a lower value.

        DSS property name: `CSVFile`, DSS property index: 7.
        """
        return self._get_prop_string(7)

    def _set_CSVFile(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(7, value, flags)

    CSVFile = property(_get_CSVFile, _set_CSVFile) # type: str

    def _get_SngFile(self) -> str:
        """
        Switch input of  temperature curve data to a binary file of singles containing (hour, Temp) points, or simply (Temp) values for fixed time interval data, packed one after another. NOTE: This action may reset the number of points to a lower value.

        DSS property name: `SngFile`, DSS property index: 8.
        """
        return self._get_prop_string(8)

    def _set_SngFile(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(8, value, flags)

    SngFile = property(_get_SngFile, _set_SngFile) # type: str

    def _get_DblFile(self) -> str:
        """
        Switch input of  temperature curve data to a binary file of doubles containing (hour, Temp) points, or simply (Temp) values for fixed time interval data, packed one after another. NOTE: This action may reset the number of points to a lower value.

        DSS property name: `DblFile`, DSS property index: 9.
        """
        return self._get_prop_string(9)

    def _set_DblFile(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(9, value, flags)

    DblFile = property(_get_DblFile, _set_DblFile) # type: str

    def _get_SInterval(self) -> float:
        """
        Specify fixed interval in SECONDS. Alternate way to specify Interval property.

        DSS property name: `SInterval`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    def _set_SInterval(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 10, value, flags)

    SInterval = property(_get_SInterval, _set_SInterval) # type: float

    def _get_MInterval(self) -> float:
        """
        Specify fixed interval in MINUTES. Alternate way to specify Interval property.

        DSS property name: `MInterval`, DSS property index: 11.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    def _set_MInterval(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 11, value, flags)

    MInterval = property(_get_MInterval, _set_MInterval) # type: float

    def Action(self, value: Union[AnyStr, int, enums.TShapeAction], flags: enums.SetterFlags = 0):
        """
        {DblSave | SngSave} After defining temperature curve data... Setting action=DblSave or SngSave will cause the present "Temp" values to be written to either a packed file of double or single. The filename is the Tshape name. 

        DSS property name: `Action`, DSS property index: 12.
        """
        if isinstance(value, int):
            self._lib.Obj_SetInt32(self._ptr, 12, value, flags)
            return

        self._set_string_o(12, value)

    def DblSave(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(TShapeAction.DblSave)'''
        self._lib.Obj_SetInt32(self._ptr, 12, enums.TShapeAction.DblSave, flags)

    def SngSave(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(TShapeAction.SngSave)'''
        self._lib.Obj_SetInt32(self._ptr, 12, enums.TShapeAction.SngSave, flags)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 13.
        """
        self._set_string_o(13, value)


class TShapeProperties(TypedDict):
    NPts: int
    Interval: float
    Temp: Float64Array
    Hour: Float64Array
    Mean: float
    StdDev: float
    CSVFile: AnyStr
    SngFile: AnyStr
    DblFile: AnyStr
    SInterval: float
    MInterval: float
    Action: Union[AnyStr, int, enums.TShapeAction]
    Like: AnyStr

class TShapeBatch(DSSBatch):
    _cls_name = 'TShape'
    _obj_cls = TShape
    _cls_idx = 3


    def _get_NPts(self) -> BatchInt32ArrayProxy:
        """
        Max number of points to expect in temperature shape vectors. This gets reset to the number of Temperature values found if less than specified.

        DSS property name: `NPts`, DSS property index: 1.
        """
        return BatchInt32ArrayProxy(self, 1)

    def _set_NPts(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(1, value, flags)

    NPts = property(_get_NPts, _set_NPts) # type: BatchInt32ArrayProxy

    def _get_Interval(self) -> BatchFloat64ArrayProxy:
        """
        Time interval for fixed interval data, hrs. Default = 1. If Interval = 0 then time data (in hours) may be at irregular intervals and time value must be specified using either the Hour property or input files. Then values are interpolated when Interval=0, but not for fixed interval data.  

        See also "sinterval" and "minterval".

        DSS property name: `Interval`, DSS property index: 2.
        """
        return BatchFloat64ArrayProxy(self, 2)

    def _set_Interval(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(2, value, flags)

    Interval = property(_get_Interval, _set_Interval) # type: BatchFloat64ArrayProxy

    def _get_Temp(self) -> List[Float64Array]:
        """
        Array of temperature values.  Units should be compatible with the object using the data. You can also use the syntax: 
        Temp = (file=filename)     !for text file one value per line
        Temp = (dblfile=filename)  !for packed file of doubles
        Temp = (sngfile=filename)  !for packed file of singles 

        Note: this property will reset Npts if the  number of values in the files are fewer.

        DSS property name: `Temp`, DSS property index: 3.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 3)
            for x in self._unpack()
        ]

    def _set_Temp(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(3, value, flags)

    Temp = property(_get_Temp, _set_Temp) # type: List[Float64Array]

    def _get_Hour(self) -> List[Float64Array]:
        """
        Array of hour values. Only necessary to define this property for variable interval data. If the data are fixed interval, do not use this property. You can also use the syntax: 
        hour = (file=filename)     !for text file one value per line
        hour = (dblfile=filename)  !for packed file of doubles
        hour = (sngfile=filename)  !for packed file of singles 

        DSS property name: `Hour`, DSS property index: 4.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 4)
            for x in self._unpack()
        ]

    def _set_Hour(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(4, value, flags)

    Hour = property(_get_Hour, _set_Hour) # type: List[Float64Array]

    def _get_Mean(self) -> BatchFloat64ArrayProxy:
        """
        Mean of the temperature curve values.  This is computed on demand the first time a value is needed.  However, you may set it to another value independently. Used for Monte Carlo load simulations.

        DSS property name: `Mean`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    def _set_Mean(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(5, value, flags)

    Mean = property(_get_Mean, _set_Mean) # type: BatchFloat64ArrayProxy

    def _get_StdDev(self) -> BatchFloat64ArrayProxy:
        """
        Standard deviation of the temperatures.  This is computed on demand the first time a value is needed.  However, you may set it to another value independently.Is overwritten if you subsequently read in a curve

        Used for Monte Carlo load simulations.

        DSS property name: `StdDev`, DSS property index: 6.
        """
        return BatchFloat64ArrayProxy(self, 6)

    def _set_StdDev(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(6, value, flags)

    StdDev = property(_get_StdDev, _set_StdDev) # type: BatchFloat64ArrayProxy

    def _get_CSVFile(self) -> List[str]:
        """
        Switch input of  temperature curve data to a csv file containing (hour, Temp) points, or simply (Temp) values for fixed time interval data, one per line. NOTE: This action may reset the number of points to a lower value.

        DSS property name: `CSVFile`, DSS property index: 7.
        """
        return self._get_batch_str_prop(7)

    def _set_CSVFile(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(7, value, flags)

    CSVFile = property(_get_CSVFile, _set_CSVFile) # type: List[str]

    def _get_SngFile(self) -> List[str]:
        """
        Switch input of  temperature curve data to a binary file of singles containing (hour, Temp) points, or simply (Temp) values for fixed time interval data, packed one after another. NOTE: This action may reset the number of points to a lower value.

        DSS property name: `SngFile`, DSS property index: 8.
        """
        return self._get_batch_str_prop(8)

    def _set_SngFile(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(8, value, flags)

    SngFile = property(_get_SngFile, _set_SngFile) # type: List[str]

    def _get_DblFile(self) -> List[str]:
        """
        Switch input of  temperature curve data to a binary file of doubles containing (hour, Temp) points, or simply (Temp) values for fixed time interval data, packed one after another. NOTE: This action may reset the number of points to a lower value.

        DSS property name: `DblFile`, DSS property index: 9.
        """
        return self._get_batch_str_prop(9)

    def _set_DblFile(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(9, value, flags)

    DblFile = property(_get_DblFile, _set_DblFile) # type: List[str]

    def _get_SInterval(self) -> BatchFloat64ArrayProxy:
        """
        Specify fixed interval in SECONDS. Alternate way to specify Interval property.

        DSS property name: `SInterval`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    def _set_SInterval(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(10, value, flags)

    SInterval = property(_get_SInterval, _set_SInterval) # type: BatchFloat64ArrayProxy

    def _get_MInterval(self) -> BatchFloat64ArrayProxy:
        """
        Specify fixed interval in MINUTES. Alternate way to specify Interval property.

        DSS property name: `MInterval`, DSS property index: 11.
        """
        return BatchFloat64ArrayProxy(self, 11)

    def _set_MInterval(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(11, value, flags)

    MInterval = property(_get_MInterval, _set_MInterval) # type: BatchFloat64ArrayProxy

    def Action(self, value: Union[AnyStr, int, enums.TShapeAction], flags: enums.SetterFlags = 0):
        """
        {DblSave | SngSave} After defining temperature curve data... Setting action=DblSave or SngSave will cause the present "Temp" values to be written to either a packed file of double or single. The filename is the Tshape name. 

        DSS property name: `Action`, DSS property index: 12.
        """
        if isinstance(value, (bytes, str)) or (isinstance(value, LIST_LIKE) and len(value) > 0 and isinstance(value[0], (bytes, str))):
            self._set_batch_string(12, value, flags)
        else:
            self._set_batch_int32_array(12, value, flags)

    def DblSave(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(TShapeAction.DblSave)'''
        self._set_batch_int32_array(12, enums.TShapeAction.DblSave, flags)

    def SngSave(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(TShapeAction.SngSave)'''
        self._set_batch_int32_array(12, enums.TShapeAction.SngSave, flags)

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 13.
        """
        self._set_batch_string(13, value, flags)

class TShapeBatchProperties(TypedDict):
    NPts: Union[int, Int32Array]
    Interval: Union[float, Float64Array]
    Temp: Float64Array
    Hour: Float64Array
    Mean: Union[float, Float64Array]
    StdDev: Union[float, Float64Array]
    CSVFile: Union[AnyStr, List[AnyStr]]
    SngFile: Union[AnyStr, List[AnyStr]]
    DblFile: Union[AnyStr, List[AnyStr]]
    SInterval: Union[float, Float64Array]
    MInterval: Union[float, Float64Array]
    Action: Union[AnyStr, int, enums.TShapeAction]
    Like: AnyStr

class ITShape(IDSSObj, TShapeBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, TShape, TShapeBatch)
        TShapeBatch.__init__(self, self._api_util, sync_cls_idx=TShape._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> TShape:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[TShapeProperties]) -> TShape:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[TShapeBatchProperties]) -> TShapeBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
