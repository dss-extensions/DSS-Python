# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from typing_extensions import TypedDict, Unpack
from .types import Float64Array, Int32Array
from . import enums
from .DSSObj import IDSSObj, DSSObj
from .Batch import DSSBatch
from .ArrayProxy import BatchFloat64ArrayProxy
from .CircuitElement import CircuitElementBatchMixin, CircuitElementMixin

class UPFCControl(DSSObj, CircuitElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots
    _cls_name = 'UPFCControl'
    _cls_idx = 37
    _cls_prop_idx = {
        'upfclist': 1,
        'basefreq': 2,
        'enabled': 3,
        'like': 4,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)

    def _get_UPFCList(self) -> List[str]:
        """
        The list of all the UPFC devices to be controlled by this controller, If left empty, this control will apply for all UPFCs in the model.

        DSS property name: `UPFCList`, DSS property index: 1.
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 1)

    def _set_UPFCList(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 1, value_ptr, value_count, flags)
        self._check_for_error()

    UPFCList = property(_get_UPFCList, _set_UPFCList) # type: List[str]

    def _get_BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 2.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 2)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 2, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float

    def _get_Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 3.
        """
        return self._lib.Obj_GetInt32(self._ptr, 3) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 3, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool

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

class UPFCControlBatch(DSSBatch, CircuitElementBatchMixin):
    _cls_name = 'UPFCControl'
    _obj_cls = UPFCControl
    _cls_idx = 37

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)

    def _get_UPFCList(self) -> List[List[str]]:
        """
        The list of all the UPFC devices to be controlled by this controller, If left empty, this control will apply for all UPFCs in the model.

        DSS property name: `UPFCList`, DSS property index: 1.
        """
        return self._get_string_ll(1)

    def _set_UPFCList(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._unpack():
            self._lib.Obj_SetStringArray(x, 1, value_ptr, value_count, flags)

        self._check_for_error()

    UPFCList = property(_get_UPFCList, _set_UPFCList) # type: List[List[str]]

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 2.
        """
        return BatchFloat64ArrayProxy(self, 2)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(2, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy

    def _get_Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 3.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(3)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(3, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 4.
        """
        self._set_batch_string(4, value, flags)

class UPFCControlBatchProperties(TypedDict):
    UPFCList: List[AnyStr]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IUPFCControl(IDSSObj, UPFCControlBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, UPFCControl, UPFCControlBatch)
        UPFCControlBatch.__init__(self, self._api_util, sync_cls_idx=UPFCControl._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> UPFCControl:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[UPFCControlProperties]) -> UPFCControl:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[UPFCControlBatchProperties]) -> UPFCControlBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
