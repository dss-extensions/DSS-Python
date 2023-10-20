# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from enum import IntEnum
from typing_extensions import TypedDict, Unpack
import numpy as np
from ._obj_bases import (
    CktElementMixin,
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

class UPFCControl(DSSObj, CktElementMixin):
    __slots__ = []
    _cls_name = 'UPFCControl'
    _cls_idx = 37
    _cls_prop_idx = {
        'upfclist': 1,
        'basefreq': 2,
        'enabled': 3,
        'like': 4,
    }

    @property
    def UPFCList(self) -> List[str]:
        """
        The list of all the UPFC devices to be controlled by this controller, If left empty, this control will apply for all UPFCs in the model.

        DSS property name: `UPFCList`, DSS property index: 1.
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 1)

    @UPFCList.setter
    def UPFCList(self, value: List[AnyStr]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 1, value_ptr, value_count)
        self._check_for_error()

    @property
    def BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 2.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 2)

    @BaseFreq.setter
    def BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 2, value)

    @property
    def Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 3.
        """
        return self._lib.Obj_GetInt32(self._ptr, 3) != 0

    @Enabled.setter
    def Enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 3, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 4.
        """
        self._set_string_o(4, value)


class UPFCControlProperties(TypedDict):
    UPFCList: List[AnyStr]
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class UPFCControlBatch(DSSBatch):
    _cls_name = 'UPFCControl'
    _obj_cls = UPFCControl
    _cls_idx = 37


    @property
    def UPFCList(self) -> List[List[str]]:
        """
        The list of all the UPFC devices to be controlled by this controller, If left empty, this control will apply for all UPFCs in the model.

        DSS property name: `UPFCList`, DSS property index: 1.
        """
        return self._get_string_ll(1)

    @UPFCList.setter
    def UPFCList(self, value: List[AnyStr]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._ffi.unpack(self.pointer[0], self.count[0]):
            self._lib.Obj_SetStringArray(x, 1, value_ptr, value_count)
    
        self._check_for_error()

    @property
    def BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 2.
        """
        return BatchFloat64ArrayProxy(self, 2)

    @BaseFreq.setter
    def BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(2, value)

    @property
    def Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 3.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 3)
        ]
    @Enabled.setter
    def Enabled(self, value: bool):
        self._set_batch_int32_array(3, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 4.
        """
        self._set_batch_string(4, value)

class UPFCControlBatchProperties(TypedDict):
    UPFCList: List[AnyStr]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IUPFCControl(IDSSObj):
    def __init__(self, iobj):
        super().__init__(iobj, UPFCControl, UPFCControlBatch)

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> UPFCControl:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[UPFCControlProperties]) -> UPFCControl:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[UPFCControlBatchProperties]) -> UPFCControlBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
