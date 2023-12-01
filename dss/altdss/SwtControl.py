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

class SwtControl(DSSObj, CircuitElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots
    _cls_name = 'SwtControl'
    _cls_idx = 34
    _cls_prop_idx = {
        'switchedobj': 1,
        'switchedterm': 2,
        'action': 3,
        'lock': 4,
        'delay': 5,
        'normal': 6,
        'state': 7,
        'reset': 8,
        'basefreq': 9,
        'enabled': 10,
        'like': 11,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)

    def _get_SwitchedObj_str(self) -> str:
        """
        Name of circuit element switch that the SwtControl operates. Specify the full object class and name.

        DSS property name: `SwitchedObj`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    def _set_SwitchedObj_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(1, value, flags)

    SwitchedObj_str = property(_get_SwitchedObj_str, _set_SwitchedObj_str) # type: str

    def _get_SwitchedObj(self) -> DSSObj:
        """
        Name of circuit element switch that the SwtControl operates. Specify the full object class and name.

        DSS property name: `SwitchedObj`, DSS property index: 1.
        """
        return self._get_obj(1, None)

    def _set_SwitchedObj(self, value: Union[AnyStr, DSSObj], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(1, value, flags)
            return

        self._set_string_o(1, value, flags)

    SwitchedObj = property(_get_SwitchedObj, _set_SwitchedObj) # type: DSSObj

    def _get_SwitchedTerm(self) -> int:
        """
        Terminal number of the controlled element switch. 1 or 2, typically.  Default is 1.

        DSS property name: `SwitchedTerm`, DSS property index: 2.
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    def _set_SwitchedTerm(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 2, value, flags)

    SwitchedTerm = property(_get_SwitchedTerm, _set_SwitchedTerm) # type: int

    def _get_Lock(self) -> bool:
        """
        {Yes | No} Delayed action. Sends CTRL_LOCK or CTRL_UNLOCK message to control queue. After delay time, controlled switch is locked in its present open / close state or unlocked. Switch will not respond to either manual (Action) or automatic (APIs) control or internal OpenDSS Reset when locked.

        DSS property name: `Lock`, DSS property index: 4.
        """
        return self._lib.Obj_GetInt32(self._ptr, 4) != 0

    def _set_Lock(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 4, value, flags)

    Lock = property(_get_Lock, _set_Lock) # type: bool

    def _get_Delay(self) -> float:
        """
        Operating time delay (sec) of the switch. Defaults to 120.

        DSS property name: `Delay`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    def _set_Delay(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 5, value, flags)

    Delay = property(_get_Delay, _set_Delay) # type: float

    def _get_Normal(self) -> enums.SwtControlState:
        """
        {Open | Closed] Normal state of the switch. If not Locked, the switch reverts to this state for reset, change of mode, etc. Defaults to first Action or State specified if not specifically declared.

        DSS property name: `Normal`, DSS property index: 6.
        """
        return enums.SwtControlState(self._lib.Obj_GetInt32(self._ptr, 6))

    def _set_Normal(self, value: Union[AnyStr, int, enums.SwtControlState], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(6, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 6, value, flags)

    Normal = property(_get_Normal, _set_Normal) # type: enums.SwtControlState

    def _get_Normal_str(self) -> str:
        """
        {Open | Closed] Normal state of the switch. If not Locked, the switch reverts to this state for reset, change of mode, etc. Defaults to first Action or State specified if not specifically declared.

        DSS property name: `Normal`, DSS property index: 6.
        """
        return self._get_prop_string(6)

    def _set_Normal_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Normal(value, flags)

    Normal_str = property(_get_Normal_str, _set_Normal_str) # type: str

    def _get_State(self) -> enums.SwtControlState:
        """
        {Open | Closed] Present state of the switch. Upon setting, immediately forces state of switch.

        DSS property name: `State`, DSS property index: 7.
        """
        return enums.SwtControlState(self._lib.Obj_GetInt32(self._ptr, 7))

    def _set_State(self, value: Union[AnyStr, int, enums.SwtControlState], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(7, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 7, value, flags)

    State = property(_get_State, _set_State) # type: enums.SwtControlState

    def _get_State_str(self) -> str:
        """
        {Open | Closed] Present state of the switch. Upon setting, immediately forces state of switch.

        DSS property name: `State`, DSS property index: 7.
        """
        return self._get_prop_string(7)

    def _set_State_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_State(value, flags)

    State_str = property(_get_State_str, _set_State_str) # type: str

    def Reset(self, value: bool = True, flags: enums.SetterFlags = 0):
        """
        {Yes | No} If Yes, forces Reset of switch to Normal state and removes Lock independently of any internal reset command for mode change, etc.

        DSS property name: `Reset`, DSS property index: 8.
        """
        self._lib.Obj_SetInt32(self._ptr, 8, value, flags)

    def _get_BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 9, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float

    def _get_Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 10.
        """
        return self._lib.Obj_GetInt32(self._ptr, 10) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 10, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 11.
        """
        self._set_string_o(11, value)


class SwtControlProperties(TypedDict):
    SwitchedObj: Union[AnyStr, DSSObj]
    SwitchedTerm: int
    Lock: bool
    Delay: float
    Normal: Union[AnyStr, int, enums.SwtControlState]
    State: Union[AnyStr, int, enums.SwtControlState]
    Reset: bool
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class SwtControlBatch(DSSBatch, CircuitElementBatchMixin):
    _cls_name = 'SwtControl'
    _obj_cls = SwtControl
    _cls_idx = 34

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)

    def _get_SwitchedObj_str(self) -> List[str]:
        """
        Name of circuit element switch that the SwtControl operates. Specify the full object class and name.

        DSS property name: `SwitchedObj`, DSS property index: 1.
        """
        return self._get_batch_str_prop(1)

    def _set_SwitchedObj_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(1, value, flags)

    SwitchedObj_str = property(_get_SwitchedObj_str, _set_SwitchedObj_str) # type: List[str]

    def _get_SwitchedObj(self) -> List[DSSObj]:
        """
        Name of circuit element switch that the SwtControl operates. Specify the full object class and name.

        DSS property name: `SwitchedObj`, DSS property index: 1.
        """
        return self._get_batch_obj_prop(1)

    def _set_SwitchedObj(self, value: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(1, value, flags)

    SwitchedObj = property(_get_SwitchedObj, _set_SwitchedObj) # type: List[DSSObj]

    def _get_SwitchedTerm(self) -> BatchInt32ArrayProxy:
        """
        Terminal number of the controlled element switch. 1 or 2, typically.  Default is 1.

        DSS property name: `SwitchedTerm`, DSS property index: 2.
        """
        return BatchInt32ArrayProxy(self, 2)

    def _set_SwitchedTerm(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(2, value, flags)

    SwitchedTerm = property(_get_SwitchedTerm, _set_SwitchedTerm) # type: BatchInt32ArrayProxy

    def _get_Lock(self) -> List[bool]:
        """
        {Yes | No} Delayed action. Sends CTRL_LOCK or CTRL_UNLOCK message to control queue. After delay time, controlled switch is locked in its present open / close state or unlocked. Switch will not respond to either manual (Action) or automatic (APIs) control or internal OpenDSS Reset when locked.

        DSS property name: `Lock`, DSS property index: 4.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(4)
        ]

    def _set_Lock(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(4, value, flags)

    Lock = property(_get_Lock, _set_Lock) # type: List[bool]

    def _get_Delay(self) -> BatchFloat64ArrayProxy:
        """
        Operating time delay (sec) of the switch. Defaults to 120.

        DSS property name: `Delay`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    def _set_Delay(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(5, value, flags)

    Delay = property(_get_Delay, _set_Delay) # type: BatchFloat64ArrayProxy

    def _get_Normal(self) -> BatchInt32ArrayProxy:
        """
        {Open | Closed] Normal state of the switch. If not Locked, the switch reverts to this state for reset, change of mode, etc. Defaults to first Action or State specified if not specifically declared.

        DSS property name: `Normal`, DSS property index: 6.
        """
        return BatchInt32ArrayProxy(self, 6)

    def _set_Normal(self, value: Union[AnyStr, int, enums.SwtControlState, List[AnyStr], List[int], List[enums.SwtControlState], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(6, value, flags)
            return

        self._set_batch_int32_array(6, value, flags)

    Normal = property(_get_Normal, _set_Normal) # type: BatchInt32ArrayProxy

    def _get_Normal_str(self) -> List[str]:
        """
        {Open | Closed] Normal state of the switch. If not Locked, the switch reverts to this state for reset, change of mode, etc. Defaults to first Action or State specified if not specifically declared.

        DSS property name: `Normal`, DSS property index: 6.
        """
        return self._get_batch_str_prop(6)

    def _set_Normal_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Normal(value, flags)

    Normal_str = property(_get_Normal_str, _set_Normal_str) # type: List[str]

    def _get_State(self) -> BatchInt32ArrayProxy:
        """
        {Open | Closed] Present state of the switch. Upon setting, immediately forces state of switch.

        DSS property name: `State`, DSS property index: 7.
        """
        return BatchInt32ArrayProxy(self, 7)

    def _set_State(self, value: Union[AnyStr, int, enums.SwtControlState, List[AnyStr], List[int], List[enums.SwtControlState], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(7, value, flags)
            return

        self._set_batch_int32_array(7, value, flags)

    State = property(_get_State, _set_State) # type: BatchInt32ArrayProxy

    def _get_State_str(self) -> List[str]:
        """
        {Open | Closed] Present state of the switch. Upon setting, immediately forces state of switch.

        DSS property name: `State`, DSS property index: 7.
        """
        return self._get_batch_str_prop(7)

    def _set_State_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_State(value, flags)

    State_str = property(_get_State_str, _set_State_str) # type: List[str]

    def Reset(self, value: Union[bool, List[bool]] = True, flags: enums.SetterFlags = 0):
        """
        {Yes | No} If Yes, forces Reset of switch to Normal state and removes Lock independently of any internal reset command for mode change, etc.

        DSS property name: `Reset`, DSS property index: 8.
        """
        self._set_batch_int32_array(8, value, flags)

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(9, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy

    def _get_Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 10.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(10)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(10, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 11.
        """
        self._set_batch_string(11, value, flags)

class SwtControlBatchProperties(TypedDict):
    SwitchedObj: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]]
    SwitchedTerm: Union[int, Int32Array]
    Lock: bool
    Delay: Union[float, Float64Array]
    Normal: Union[AnyStr, int, enums.SwtControlState, List[AnyStr], List[int], List[enums.SwtControlState], Int32Array]
    State: Union[AnyStr, int, enums.SwtControlState, List[AnyStr], List[int], List[enums.SwtControlState], Int32Array]
    Reset: bool
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class ISwtControl(IDSSObj, SwtControlBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, SwtControl, SwtControlBatch)
        SwtControlBatch.__init__(self, self._api_util, sync_cls_idx=SwtControl._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> SwtControl:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[SwtControlProperties]) -> SwtControl:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[SwtControlBatchProperties]) -> SwtControlBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
