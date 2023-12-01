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
from .CircuitElement import CircuitElementBatchMixin, CircuitElementMixin

class ESPVLControl(DSSObj, CircuitElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots
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

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)

    def _get_Element_str(self) -> str:
        """
        Full object name of the circuit element, typically a line or transformer, which the control is monitoring. There is no default; must be specified.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    def _set_Element_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(1, value, flags)

    Element_str = property(_get_Element_str, _set_Element_str) # type: str

    def _get_Element(self) -> DSSObj:
        """
        Full object name of the circuit element, typically a line or transformer, which the control is monitoring. There is no default; must be specified.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_obj(1, None)

    def _set_Element(self, value: Union[AnyStr, DSSObj], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(1, value, flags)
            return

        self._set_string_o(1, value, flags)

    Element = property(_get_Element, _set_Element) # type: DSSObj

    def _get_Terminal(self) -> int:
        """
        Number of the terminal of the circuit element to which the ESPVLControl control is connected. 1 or 2, typically.  Default is 1. Make sure you have the direction on the power matching the sign of kWLimit.

        DSS property name: `Terminal`, DSS property index: 2.
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    def _set_Terminal(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 2, value, flags)

    Terminal = property(_get_Terminal, _set_Terminal) # type: int

    def _get_Type(self) -> enums.ESPVLControlType:
        """
        Type of controller.  1= System Controller; 2= Local controller. 

        DSS property name: `Type`, DSS property index: 3.
        """
        return enums.ESPVLControlType(self._lib.Obj_GetInt32(self._ptr, 3))

    def _set_Type(self, value: Union[AnyStr, int, enums.ESPVLControlType], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(3, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 3, value, flags)

    Type = property(_get_Type, _set_Type) # type: enums.ESPVLControlType

    def _get_Type_str(self) -> str:
        """
        Type of controller.  1= System Controller; 2= Local controller. 

        DSS property name: `Type`, DSS property index: 3.
        """
        return self._get_prop_string(3)

    def _set_Type_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Type(value, flags)

    Type_str = property(_get_Type_str, _set_Type_str) # type: str

    def _get_kWBand(self) -> float:
        """
        Bandwidth (kW) of the dead band around the target limit.No dispatch changes are attempted if the power in the monitored terminal stays within this band.

        DSS property name: `kWBand`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    def _set_kWBand(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 4, value, flags)

    kWBand = property(_get_kWBand, _set_kWBand) # type: float

    def _get_kvarLimit(self) -> float:
        """
        Max kvar to be delivered through the element.  Uses same dead band as kW.

        DSS property name: `kvarLimit`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    def _set_kvarLimit(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 5, value, flags)

    kvarLimit = property(_get_kvarLimit, _set_kvarLimit) # type: float

    def _get_LocalControlList(self) -> List[str]:
        """
        Array list of ESPVLControl local controller objects to be dispatched by System Controller. If not specified, all ESPVLControl devices with type=local in the circuit not attached to another controller are assumed to be part of this controller's fleet.

        DSS property name: `LocalControlList`, DSS property index: 6.
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 6)

    def _set_LocalControlList(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 6, value_ptr, value_count, flags)
        self._check_for_error()

    LocalControlList = property(_get_LocalControlList, _set_LocalControlList) # type: List[str]

    def _get_LocalControlWeights(self) -> Float64Array:
        """
        Array of proportional weights corresponding to each ESPVLControl local controller in the LocalControlList.

        DSS property name: `LocalControlWeights`, DSS property index: 7.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 7)

    def _set_LocalControlWeights(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(7, value, flags)

    LocalControlWeights = property(_get_LocalControlWeights, _set_LocalControlWeights) # type: Float64Array

    def _get_PVSystemList(self) -> List[str]:
        """
        Array list of PVSystem objects to be dispatched by a Local Controller. 

        DSS property name: `PVSystemList`, DSS property index: 8.
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 8)

    def _set_PVSystemList(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 8, value_ptr, value_count, flags)
        self._check_for_error()

    PVSystemList = property(_get_PVSystemList, _set_PVSystemList) # type: List[str]

    def _get_PVSystemWeights(self) -> Float64Array:
        """
        Array of proportional weights corresponding to each PVSystem in the PVSystemList.

        DSS property name: `PVSystemWeights`, DSS property index: 9.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 9)

    def _set_PVSystemWeights(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(9, value, flags)

    PVSystemWeights = property(_get_PVSystemWeights, _set_PVSystemWeights) # type: Float64Array

    def _get_StorageList(self) -> List[str]:
        """
        Array list of Storage objects to be dispatched by Local Controller. 

        DSS property name: `StorageList`, DSS property index: 10.
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 10)

    def _set_StorageList(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 10, value_ptr, value_count, flags)
        self._check_for_error()

    StorageList = property(_get_StorageList, _set_StorageList) # type: List[str]

    def _get_StorageWeights(self) -> Float64Array:
        """
        Array of proportional weights corresponding to each Storage object in the StorageControlList.

        DSS property name: `StorageWeights`, DSS property index: 11.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 11)

    def _set_StorageWeights(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(11, value, flags)

    StorageWeights = property(_get_StorageWeights, _set_StorageWeights) # type: Float64Array

    def _get_BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 12, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float

    def _get_Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 13.
        """
        return self._lib.Obj_GetInt32(self._ptr, 13) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 13, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool

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

class ESPVLControlBatch(DSSBatch, CircuitElementBatchMixin):
    _cls_name = 'ESPVLControl'
    _obj_cls = ESPVLControl
    _cls_idx = 38

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)

    def _get_Element_str(self) -> List[str]:
        """
        Full object name of the circuit element, typically a line or transformer, which the control is monitoring. There is no default; must be specified.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_batch_str_prop(1)

    def _set_Element_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(1, value, flags)

    Element_str = property(_get_Element_str, _set_Element_str) # type: List[str]

    def _get_Element(self) -> List[DSSObj]:
        """
        Full object name of the circuit element, typically a line or transformer, which the control is monitoring. There is no default; must be specified.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_batch_obj_prop(1)

    def _set_Element(self, value: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(1, value, flags)

    Element = property(_get_Element, _set_Element) # type: List[DSSObj]

    def _get_Terminal(self) -> BatchInt32ArrayProxy:
        """
        Number of the terminal of the circuit element to which the ESPVLControl control is connected. 1 or 2, typically.  Default is 1. Make sure you have the direction on the power matching the sign of kWLimit.

        DSS property name: `Terminal`, DSS property index: 2.
        """
        return BatchInt32ArrayProxy(self, 2)

    def _set_Terminal(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(2, value, flags)

    Terminal = property(_get_Terminal, _set_Terminal) # type: BatchInt32ArrayProxy

    def _get_Type(self) -> BatchInt32ArrayProxy:
        """
        Type of controller.  1= System Controller; 2= Local controller. 

        DSS property name: `Type`, DSS property index: 3.
        """
        return BatchInt32ArrayProxy(self, 3)

    def _set_Type(self, value: Union[AnyStr, int, enums.ESPVLControlType, List[AnyStr], List[int], List[enums.ESPVLControlType], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(3, value, flags)
            return

        self._set_batch_int32_array(3, value, flags)

    Type = property(_get_Type, _set_Type) # type: BatchInt32ArrayProxy

    def _get_Type_str(self) -> List[str]:
        """
        Type of controller.  1= System Controller; 2= Local controller. 

        DSS property name: `Type`, DSS property index: 3.
        """
        return self._get_batch_str_prop(3)

    def _set_Type_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Type(value, flags)

    Type_str = property(_get_Type_str, _set_Type_str) # type: List[str]

    def _get_kWBand(self) -> BatchFloat64ArrayProxy:
        """
        Bandwidth (kW) of the dead band around the target limit.No dispatch changes are attempted if the power in the monitored terminal stays within this band.

        DSS property name: `kWBand`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    def _set_kWBand(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(4, value, flags)

    kWBand = property(_get_kWBand, _set_kWBand) # type: BatchFloat64ArrayProxy

    def _get_kvarLimit(self) -> BatchFloat64ArrayProxy:
        """
        Max kvar to be delivered through the element.  Uses same dead band as kW.

        DSS property name: `kvarLimit`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    def _set_kvarLimit(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(5, value, flags)

    kvarLimit = property(_get_kvarLimit, _set_kvarLimit) # type: BatchFloat64ArrayProxy

    def _get_LocalControlList(self) -> List[List[str]]:
        """
        Array list of ESPVLControl local controller objects to be dispatched by System Controller. If not specified, all ESPVLControl devices with type=local in the circuit not attached to another controller are assumed to be part of this controller's fleet.

        DSS property name: `LocalControlList`, DSS property index: 6.
        """
        return self._get_string_ll(6)

    def _set_LocalControlList(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._unpack():
            self._lib.Obj_SetStringArray(x, 6, value_ptr, value_count, flags)

        self._check_for_error()

    LocalControlList = property(_get_LocalControlList, _set_LocalControlList) # type: List[List[str]]

    def _get_LocalControlWeights(self) -> List[Float64Array]:
        """
        Array of proportional weights corresponding to each ESPVLControl local controller in the LocalControlList.

        DSS property name: `LocalControlWeights`, DSS property index: 7.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 7)
            for x in self._unpack()
        ]

    def _set_LocalControlWeights(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(7, value, flags)

    LocalControlWeights = property(_get_LocalControlWeights, _set_LocalControlWeights) # type: List[Float64Array]

    def _get_PVSystemList(self) -> List[List[str]]:
        """
        Array list of PVSystem objects to be dispatched by a Local Controller. 

        DSS property name: `PVSystemList`, DSS property index: 8.
        """
        return self._get_string_ll(8)

    def _set_PVSystemList(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._unpack():
            self._lib.Obj_SetStringArray(x, 8, value_ptr, value_count, flags)

        self._check_for_error()

    PVSystemList = property(_get_PVSystemList, _set_PVSystemList) # type: List[List[str]]

    def _get_PVSystemWeights(self) -> List[Float64Array]:
        """
        Array of proportional weights corresponding to each PVSystem in the PVSystemList.

        DSS property name: `PVSystemWeights`, DSS property index: 9.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 9)
            for x in self._unpack()
        ]

    def _set_PVSystemWeights(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(9, value, flags)

    PVSystemWeights = property(_get_PVSystemWeights, _set_PVSystemWeights) # type: List[Float64Array]

    def _get_StorageList(self) -> List[List[str]]:
        """
        Array list of Storage objects to be dispatched by Local Controller. 

        DSS property name: `StorageList`, DSS property index: 10.
        """
        return self._get_string_ll(10)

    def _set_StorageList(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._unpack():
            self._lib.Obj_SetStringArray(x, 10, value_ptr, value_count, flags)

        self._check_for_error()

    StorageList = property(_get_StorageList, _set_StorageList) # type: List[List[str]]

    def _get_StorageWeights(self) -> List[Float64Array]:
        """
        Array of proportional weights corresponding to each Storage object in the StorageControlList.

        DSS property name: `StorageWeights`, DSS property index: 11.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 11)
            for x in self._unpack()
        ]

    def _set_StorageWeights(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(11, value, flags)

    StorageWeights = property(_get_StorageWeights, _set_StorageWeights) # type: List[Float64Array]

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(12, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy

    def _get_Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 13.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(13)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(13, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 14.
        """
        self._set_batch_string(14, value, flags)

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

class IESPVLControl(IDSSObj, ESPVLControlBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, ESPVLControl, ESPVLControlBatch)
        ESPVLControlBatch.__init__(self, self._api_util, sync_cls_idx=ESPVLControl._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> ESPVLControl:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[ESPVLControlProperties]) -> ESPVLControl:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[ESPVLControlBatchProperties]) -> ESPVLControlBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
