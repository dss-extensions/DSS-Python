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

class ESPVLControl(DSSObj, CktElementMixin):
    __slots__ = []
    _cls_name = 'ESPVLControl'
    _cls_idx = 38
    _cls_prop_idx = {
        'element': 1,
        'terminal': 2,
        'type': 3,
        'kwband': 4,
        'kvarlimit': 5,
        'localcontrollist': 6,
        'localcontrolweights': 7,
        'pvsystemlist': 8,
        'pvsystemweights': 9,
        'storagelist': 10,
        'storageweights': 11,
        'basefreq': 12,
        'enabled': 13,
        'like': 14,
    }

    @property
    def Element(self) -> str:
        """
        Full object name of the circuit element, typically a line or transformer, which the control is monitoring. There is no default; must be specified.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    @Element.setter
    def Element(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_obj(1, value)
            return

        self._set_string_o(1, value)

    @property
    def Element_obj(self) -> DSSObj:
        """
        Full object name of the circuit element, typically a line or transformer, which the control is monitoring. There is no default; must be specified.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_obj(1, None)

    @Element_obj.setter
    def Element_obj(self, value: DSSObj):
        self._set_obj(1, value)

    @property
    def Terminal(self) -> int:
        """
        Number of the terminal of the circuit element to which the ESPVLControl control is connected. 1 or 2, typically.  Default is 1. Make sure you have the direction on the power matching the sign of kWLimit.

        DSS property name: `Terminal`, DSS property index: 2.
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @Terminal.setter
    def Terminal(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def Type(self) -> enums.ESPVLControlType:
        """
        Type of controller.  1= System Controller; 2= Local controller. 

        DSS property name: `Type`, DSS property index: 3.
        """
        return enums.ESPVLControlType(self._lib.Obj_GetInt32(self._ptr, 3))

    @Type.setter
    def Type(self, value: Union[AnyStr, int, enums.ESPVLControlType]):
        if not isinstance(value, int):
            self._set_string_o(3, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 3, value)

    @property
    def Type_str(self) -> str:
        """
        Type of controller.  1= System Controller; 2= Local controller. 

        DSS property name: `Type`, DSS property index: 3.
        """
        return self._get_prop_string(3)

    @Type_str.setter
    def Type_str(self, value: AnyStr):
        self.Type = value

    @property
    def kWBand(self) -> float:
        """
        Bandwidth (kW) of the dead band around the target limit.No dispatch changes are attempted if the power in the monitored terminal stays within this band.

        DSS property name: `kWBand`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @kWBand.setter
    def kWBand(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def kvarLimit(self) -> float:
        """
        Max kvar to be delivered through the element.  Uses same dead band as kW.

        DSS property name: `kvarLimit`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @kvarLimit.setter
    def kvarLimit(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def LocalControlList(self) -> List[str]:
        """
        Array list of ESPVLControl local controller objects to be dispatched by System Controller. If not specified, all ESPVLControl devices with type=local in the circuit not attached to another controller are assumed to be part of this controller's fleet.

        DSS property name: `LocalControlList`, DSS property index: 6.
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 6)

    @LocalControlList.setter
    def LocalControlList(self, value: List[AnyStr]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 6, value_ptr, value_count)
        self._check_for_error()

    @property
    def LocalControlWeights(self) -> Float64Array:
        """
        Array of proportional weights corresponding to each ESPVLControl local controller in the LocalControlList.

        DSS property name: `LocalControlWeights`, DSS property index: 7.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 7)

    @LocalControlWeights.setter
    def LocalControlWeights(self, value: Float64Array):
        self._set_float64_array_o(7, value)

    @property
    def PVSystemList(self) -> List[str]:
        """
        Array list of PVSystem objects to be dispatched by a Local Controller. 

        DSS property name: `PVSystemList`, DSS property index: 8.
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 8)

    @PVSystemList.setter
    def PVSystemList(self, value: List[AnyStr]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 8, value_ptr, value_count)
        self._check_for_error()

    @property
    def PVSystemWeights(self) -> Float64Array:
        """
        Array of proportional weights corresponding to each PVSystem in the PVSystemList.

        DSS property name: `PVSystemWeights`, DSS property index: 9.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 9)

    @PVSystemWeights.setter
    def PVSystemWeights(self, value: Float64Array):
        self._set_float64_array_o(9, value)

    @property
    def StorageList(self) -> List[str]:
        """
        Array list of Storage objects to be dispatched by Local Controller. 

        DSS property name: `StorageList`, DSS property index: 10.
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 10)

    @StorageList.setter
    def StorageList(self, value: List[AnyStr]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 10, value_ptr, value_count)
        self._check_for_error()

    @property
    def StorageWeights(self) -> Float64Array:
        """
        Array of proportional weights corresponding to each Storage object in the StorageControlList.

        DSS property name: `StorageWeights`, DSS property index: 11.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 11)

    @StorageWeights.setter
    def StorageWeights(self, value: Float64Array):
        self._set_float64_array_o(11, value)

    @property
    def BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @BaseFreq.setter
    def BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 13.
        """
        return self._lib.Obj_GetInt32(self._ptr, 13) != 0

    @Enabled.setter
    def Enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 13, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 14.
        """
        self._set_string_o(14, value)


class ESPVLControlProperties(TypedDict):
    Element: Union[AnyStr, DSSObj]
    Terminal: int
    Type: Union[AnyStr, int, enums.ESPVLControlType]
    kWBand: float
    kvarLimit: float
    LocalControlList: List[AnyStr]
    LocalControlWeights: Float64Array
    PVSystemList: List[AnyStr]
    PVSystemWeights: Float64Array
    StorageList: List[AnyStr]
    StorageWeights: Float64Array
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class ESPVLControlBatch(DSSBatch):
    _cls_name = 'ESPVLControl'
    _obj_cls = ESPVLControl
    _cls_idx = 38


    @property
    def Element(self) -> List[str]:
        """
        Full object name of the circuit element, typically a line or transformer, which the control is monitoring. There is no default; must be specified.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @Element.setter
    def Element(self, value: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]]):
        self._set_batch_obj_prop(1, value)

    @property
    def Element_obj(self) -> List[DSSObj]:
        """
        Full object name of the circuit element, typically a line or transformer, which the control is monitoring. There is no default; must be specified.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 1)

    @Element_obj.setter
    def Element_obj(self, value: DSSObj):
        self._set_batch_string(1, value)

    @property
    def Terminal(self) -> BatchInt32ArrayProxy:
        """
        Number of the terminal of the circuit element to which the ESPVLControl control is connected. 1 or 2, typically.  Default is 1. Make sure you have the direction on the power matching the sign of kWLimit.

        DSS property name: `Terminal`, DSS property index: 2.
        """
        return BatchInt32ArrayProxy(self, 2)

    @Terminal.setter
    def Terminal(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(2, value)

    @property
    def Type(self) -> BatchInt32ArrayProxy:
        """
        Type of controller.  1= System Controller; 2= Local controller. 

        DSS property name: `Type`, DSS property index: 3.
        """
        return BatchInt32ArrayProxy(self, 3)

    @Type.setter
    def Type(self, value: Union[AnyStr, int, enums.ESPVLControlType, List[AnyStr], List[int], List[enums.ESPVLControlType], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(3, value)
            return
    
        self._set_batch_int32_array(3, value)

    @property
    def Type_str(self) -> str:
        """
        Type of controller.  1= System Controller; 2= Local controller. 

        DSS property name: `Type`, DSS property index: 3.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 3)

    @Type_str.setter
    def Type_str(self, value: AnyStr):
        self.Type = value

    @property
    def kWBand(self) -> BatchFloat64ArrayProxy:
        """
        Bandwidth (kW) of the dead band around the target limit.No dispatch changes are attempted if the power in the monitored terminal stays within this band.

        DSS property name: `kWBand`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    @kWBand.setter
    def kWBand(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(4, value)

    @property
    def kvarLimit(self) -> BatchFloat64ArrayProxy:
        """
        Max kvar to be delivered through the element.  Uses same dead band as kW.

        DSS property name: `kvarLimit`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    @kvarLimit.setter
    def kvarLimit(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(5, value)

    @property
    def LocalControlList(self) -> List[List[str]]:
        """
        Array list of ESPVLControl local controller objects to be dispatched by System Controller. If not specified, all ESPVLControl devices with type=local in the circuit not attached to another controller are assumed to be part of this controller's fleet.

        DSS property name: `LocalControlList`, DSS property index: 6.
        """
        return self._get_string_ll(6)

    @LocalControlList.setter
    def LocalControlList(self, value: List[AnyStr]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._ffi.unpack(self.pointer[0], self.count[0]):
            self._lib.Obj_SetStringArray(x, 6, value_ptr, value_count)
    
        self._check_for_error()

    @property
    def LocalControlWeights(self) -> List[Float64Array]:
        """
        Array of proportional weights corresponding to each ESPVLControl local controller in the LocalControlList.

        DSS property name: `LocalControlWeights`, DSS property index: 7.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 7)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @LocalControlWeights.setter
    def LocalControlWeights(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(7, value)

    @property
    def PVSystemList(self) -> List[List[str]]:
        """
        Array list of PVSystem objects to be dispatched by a Local Controller. 

        DSS property name: `PVSystemList`, DSS property index: 8.
        """
        return self._get_string_ll(8)

    @PVSystemList.setter
    def PVSystemList(self, value: List[AnyStr]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._ffi.unpack(self.pointer[0], self.count[0]):
            self._lib.Obj_SetStringArray(x, 8, value_ptr, value_count)
    
        self._check_for_error()

    @property
    def PVSystemWeights(self) -> List[Float64Array]:
        """
        Array of proportional weights corresponding to each PVSystem in the PVSystemList.

        DSS property name: `PVSystemWeights`, DSS property index: 9.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 9)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @PVSystemWeights.setter
    def PVSystemWeights(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(9, value)

    @property
    def StorageList(self) -> List[List[str]]:
        """
        Array list of Storage objects to be dispatched by Local Controller. 

        DSS property name: `StorageList`, DSS property index: 10.
        """
        return self._get_string_ll(10)

    @StorageList.setter
    def StorageList(self, value: List[AnyStr]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._ffi.unpack(self.pointer[0], self.count[0]):
            self._lib.Obj_SetStringArray(x, 10, value_ptr, value_count)
    
        self._check_for_error()

    @property
    def StorageWeights(self) -> List[Float64Array]:
        """
        Array of proportional weights corresponding to each Storage object in the StorageControlList.

        DSS property name: `StorageWeights`, DSS property index: 11.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 11)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @StorageWeights.setter
    def StorageWeights(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(11, value)

    @property
    def BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    @BaseFreq.setter
    def BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(12, value)

    @property
    def Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 13.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 13)
        ]
    @Enabled.setter
    def Enabled(self, value: bool):
        self._set_batch_int32_array(13, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 14.
        """
        self._set_batch_string(14, value)

class ESPVLControlBatchProperties(TypedDict):
    Element: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]]
    Terminal: Union[int, Int32Array]
    Type: Union[AnyStr, int, enums.ESPVLControlType, List[AnyStr], List[int], List[enums.ESPVLControlType], Int32Array]
    kWBand: Union[float, Float64Array]
    kvarLimit: Union[float, Float64Array]
    LocalControlList: List[AnyStr]
    LocalControlWeights: Float64Array
    PVSystemList: List[AnyStr]
    PVSystemWeights: Float64Array
    StorageList: List[AnyStr]
    StorageWeights: Float64Array
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IESPVLControl(IDSSObj):
    def __init__(self, iobj):
        super().__init__(iobj, ESPVLControl, ESPVLControlBatch)

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> ESPVLControl:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[ESPVLControlProperties]) -> ESPVLControl:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[ESPVLControlBatchProperties]) -> ESPVLControlBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
