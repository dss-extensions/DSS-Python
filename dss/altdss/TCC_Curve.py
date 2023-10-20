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

class TCC_Curve(DSSObj, ):
    __slots__ = []
    _cls_name = 'TCC_Curve'
    _cls_idx = 7
    _cls_prop_idx = {
        'npts': 1,
        'c_array': 2,
        't_array': 3,
        'like': 4,
    }

    @property
    def NPts(self) -> int:
        """
        Number of points to expect in time-current arrays.

        DSS property name: `NPts`, DSS property index: 1.
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @NPts.setter
    def NPts(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def C_Array(self) -> Float64Array:
        """
        Array of current (or voltage) values corresponding to time values (see help on T_Array).

        DSS property name: `C_Array`, DSS property index: 2.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 2)

    @C_Array.setter
    def C_Array(self, value: Float64Array):
        self._set_float64_array_o(2, value)

    @property
    def T_Array(self) -> Float64Array:
        """
        Array of time values in sec. Typical array syntax: 
        t_array = (1, 2, 3, 4, ...)

        Can also substitute a file designation: 
        t_array =  (file=filename)

        The specified file has one value per line.

        DSS property name: `T_Array`, DSS property index: 3.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 3)

    @T_Array.setter
    def T_Array(self, value: Float64Array):
        self._set_float64_array_o(3, value)

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


    @property
    def NPts(self) -> BatchInt32ArrayProxy:
        """
        Number of points to expect in time-current arrays.

        DSS property name: `NPts`, DSS property index: 1.
        """
        return BatchInt32ArrayProxy(self, 1)

    @NPts.setter
    def NPts(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(1, value)

    @property
    def C_Array(self) -> List[Float64Array]:
        """
        Array of current (or voltage) values corresponding to time values (see help on T_Array).

        DSS property name: `C_Array`, DSS property index: 2.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 2)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @C_Array.setter
    def C_Array(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(2, value)

    @property
    def T_Array(self) -> List[Float64Array]:
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
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @T_Array.setter
    def T_Array(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(3, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 4.
        """
        self._set_batch_string(4, value)

class TCC_CurveBatchProperties(TypedDict):
    NPts: Union[int, Int32Array]
    C_Array: Float64Array
    T_Array: Float64Array
    Like: AnyStr

class ITCC_Curve(IDSSObj):
    def __init__(self, iobj):
        super().__init__(iobj, TCC_Curve, TCC_CurveBatch)

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> TCC_Curve:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[TCC_CurveProperties]) -> TCC_Curve:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[TCC_CurveBatchProperties]) -> TCC_CurveBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
