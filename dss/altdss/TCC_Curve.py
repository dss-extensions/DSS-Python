# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from typing_extensions import TypedDict, Unpack
from .types import Float64Array, Int32Array
from . import enums
from .DSSObj import IDSSObj, DSSObj
from .Batch import DSSBatch
from .ArrayProxy import BatchInt32ArrayProxy

class TCC_Curve(DSSObj):
    __slots__ = DSSObj._extra_slots
    _cls_name = 'TCC_Curve'
    _cls_idx = 7
    _cls_prop_idx = {
        'npts': 1,
        'c_array': 2,
        't_array': 3,
        'like': 4,
    }


    def _get_NPts(self) -> int:
        """
        Number of points to expect in time-current arrays.

        DSS property name: `NPts`, DSS property index: 1.
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    def _set_NPts(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 1, value, flags)

    NPts = property(_get_NPts, _set_NPts) # type: int

    def _get_C_Array(self) -> Float64Array:
        """
        Array of current (or voltage) values corresponding to time values (see help on T_Array).

        DSS property name: `C_Array`, DSS property index: 2.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 2)

    def _set_C_Array(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(2, value, flags)

    C_Array = property(_get_C_Array, _set_C_Array) # type: Float64Array

    def _get_T_Array(self) -> Float64Array:
        """
        Array of time values in sec. Typical array syntax: 
        t_array = (1, 2, 3, 4, ...)

        Can also substitute a file designation: 
        t_array =  (file=filename)

        The specified file has one value per line.

        DSS property name: `T_Array`, DSS property index: 3.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 3)

    def _set_T_Array(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(3, value, flags)

    T_Array = property(_get_T_Array, _set_T_Array) # type: Float64Array

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 4.
        """
        self._set_string_o(4, value)


class TCC_CurveProperties(TypedDict):
    NPts: int
    C_Array: Float64Array
    T_Array: Float64Array
    Like: AnyStr

class TCC_CurveBatch(DSSBatch):
    _cls_name = 'TCC_Curve'
    _obj_cls = TCC_Curve
    _cls_idx = 7


    def _get_NPts(self) -> BatchInt32ArrayProxy:
        """
        Number of points to expect in time-current arrays.

        DSS property name: `NPts`, DSS property index: 1.
        """
        return BatchInt32ArrayProxy(self, 1)

    def _set_NPts(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(1, value, flags)

    NPts = property(_get_NPts, _set_NPts) # type: BatchInt32ArrayProxy

    def _get_C_Array(self) -> List[Float64Array]:
        """
        Array of current (or voltage) values corresponding to time values (see help on T_Array).

        DSS property name: `C_Array`, DSS property index: 2.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 2)
            for x in self._unpack()
        ]

    def _set_C_Array(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(2, value, flags)

    C_Array = property(_get_C_Array, _set_C_Array) # type: List[Float64Array]

    def _get_T_Array(self) -> List[Float64Array]:
        """
        Array of time values in sec. Typical array syntax: 
        t_array = (1, 2, 3, 4, ...)

        Can also substitute a file designation: 
        t_array =  (file=filename)

        The specified file has one value per line.

        DSS property name: `T_Array`, DSS property index: 3.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 3)
            for x in self._unpack()
        ]

    def _set_T_Array(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(3, value, flags)

    T_Array = property(_get_T_Array, _set_T_Array) # type: List[Float64Array]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 4.
        """
        self._set_batch_string(4, value, flags)

class TCC_CurveBatchProperties(TypedDict):
    NPts: Union[int, Int32Array]
    C_Array: Float64Array
    T_Array: Float64Array
    Like: AnyStr

class ITCC_Curve(IDSSObj, TCC_CurveBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, TCC_Curve, TCC_CurveBatch)
        TCC_CurveBatch.__init__(self, self._api_util, sync_cls_idx=TCC_Curve._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> TCC_Curve:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[TCC_CurveProperties]) -> TCC_Curve:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[TCC_CurveBatchProperties]) -> TCC_CurveBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
