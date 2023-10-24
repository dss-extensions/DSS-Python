# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from typing_extensions import TypedDict, Unpack
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

class SwtControl(DSSObj, CktElementMixin):
    __slots__ = CktElementMixin._extra_slots
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

    @property
    def SwitchedObj(self) -> str:
        """
        Name of circuit element switch that the SwtControl operates. Specify the full object class and name.

        DSS property name: `SwitchedObj`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    @SwitchedObj.setter
    def SwitchedObj(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_obj(1, value)
            return

        self._set_string_o(1, value)

    @property
    def SwitchedObj_obj(self) -> DSSObj:
        """
        Name of circuit element switch that the SwtControl operates. Specify the full object class and name.

        DSS property name: `SwitchedObj`, DSS property index: 1.
        """
        return self._get_obj(1, None)

    @SwitchedObj_obj.setter
    def SwitchedObj_obj(self, value: DSSObj):
        self._set_obj(1, value)

    @property
    def SwitchedTerm(self) -> int:
        """
        Terminal number of the controlled element switch. 1 or 2, typically.  Default is 1.

        DSS property name: `SwitchedTerm`, DSS property index: 2.
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @SwitchedTerm.setter
    def SwitchedTerm(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def Lock(self) -> bool:
        """
        {Yes | No} Delayed action. Sends CTRL_LOCK or CTRL_UNLOCK message to control queue. After delay time, controlled switch is locked in its present open / close state or unlocked. Switch will not respond to either manual (Action) or automatic (APIs) control or internal OpenDSS Reset when locked.

        DSS property name: `Lock`, DSS property index: 4.
        """
        return self._lib.Obj_GetInt32(self._ptr, 4) != 0

    @Lock.setter
    def Lock(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 4, value)

    @property
    def Delay(self) -> float:
        """
        Operating time delay (sec) of the switch. Defaults to 120.

        DSS property name: `Delay`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @Delay.setter
    def Delay(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def Normal(self) -> enums.SwtControlState:
        """
        {Open | Closed] Normal state of the switch. If not Locked, the switch reverts to this state for reset, change of mode, etc. Defaults to first Action or State specified if not specifically declared.

        DSS property name: `Normal`, DSS property index: 6.
        """
        return enums.SwtControlState(self._lib.Obj_GetInt32(self._ptr, 6))

    @Normal.setter
    def Normal(self, value: Union[AnyStr, int, enums.SwtControlState]):
        if not isinstance(value, int):
            self._set_string_o(6, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 6, value)

    @property
    def Normal_str(self) -> str:
        """
        {Open | Closed] Normal state of the switch. If not Locked, the switch reverts to this state for reset, change of mode, etc. Defaults to first Action or State specified if not specifically declared.

        DSS property name: `Normal`, DSS property index: 6.
        """
        return self._get_prop_string(6)

    @Normal_str.setter
    def Normal_str(self, value: AnyStr):
        self.Normal = value

    @property
    def State(self) -> enums.SwtControlState:
        """
        {Open | Closed] Present state of the switch. Upon setting, immediately forces state of switch.

        DSS property name: `State`, DSS property index: 7.
        """
        return enums.SwtControlState(self._lib.Obj_GetInt32(self._ptr, 7))

    @State.setter
    def State(self, value: Union[AnyStr, int, enums.SwtControlState]):
        if not isinstance(value, int):
            self._set_string_o(7, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 7, value)

    @property
    def State_str(self) -> str:
        """
        {Open | Closed] Present state of the switch. Upon setting, immediately forces state of switch.

        DSS property name: `State`, DSS property index: 7.
        """
        return self._get_prop_string(7)

    @State_str.setter
    def State_str(self, value: AnyStr):
        self.State = value

    def Reset(self, value: bool = True):
        """
        {Yes | No} If Yes, forces Reset of switch to Normal state and removes Lock independently of any internal reset command for mode change, etc.

        DSS property name: `Reset`, DSS property index: 8.
        """
        self._lib.Obj_SetInt32(self._ptr, 8, value)

    @property
    def BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @BaseFreq.setter
    def BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 10.
        """
        return self._lib.Obj_GetInt32(self._ptr, 10) != 0

    @Enabled.setter
    def Enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 10, value)

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

class SwtControlBatch(DSSBatch):
    _cls_name = 'SwtControl'
    _obj_cls = SwtControl
    _cls_idx = 34


    @property
    def SwitchedObj(self) -> List[str]:
        """
        Name of circuit element switch that the SwtControl operates. Specify the full object class and name.

        DSS property name: `SwitchedObj`, DSS property index: 1.
        """
        return self._get_batch_str_prop(1)

    @SwitchedObj.setter
    def SwitchedObj(self, value: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]]):
        self._set_batch_obj_prop(1, value)

    @property
    def SwitchedObj_obj(self) -> List[DSSObj]:
        """
        Name of circuit element switch that the SwtControl operates. Specify the full object class and name.

        DSS property name: `SwitchedObj`, DSS property index: 1.
        """
        return self._get_batch_obj_prop(1)

    @SwitchedObj_obj.setter
    def SwitchedObj_obj(self, value: DSSObj):
        self._set_batch_string(1, value)

    @property
    def SwitchedTerm(self) -> BatchInt32ArrayProxy:
        """
        Terminal number of the controlled element switch. 1 or 2, typically.  Default is 1.

        DSS property name: `SwitchedTerm`, DSS property index: 2.
        """
        return BatchInt32ArrayProxy(self, 2)

    @SwitchedTerm.setter
    def SwitchedTerm(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(2, value)

    @property
    def Lock(self) -> List[bool]:
        """
        {Yes | No} Delayed action. Sends CTRL_LOCK or CTRL_UNLOCK message to control queue. After delay time, controlled switch is locked in its present open / close state or unlocked. Switch will not respond to either manual (Action) or automatic (APIs) control or internal OpenDSS Reset when locked.

        DSS property name: `Lock`, DSS property index: 4.
        """
        return [v != 0 for v in 
            self._get_batch_int32_prop(4)
        ]
    @Lock.setter
    def Lock(self, value: bool):
        self._set_batch_int32_array(4, value)

    @property
    def Delay(self) -> BatchFloat64ArrayProxy:
        """
        Operating time delay (sec) of the switch. Defaults to 120.

        DSS property name: `Delay`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    @Delay.setter
    def Delay(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(5, value)

    @property
    def Normal(self) -> BatchInt32ArrayProxy:
        """
        {Open | Closed] Normal state of the switch. If not Locked, the switch reverts to this state for reset, change of mode, etc. Defaults to first Action or State specified if not specifically declared.

        DSS property name: `Normal`, DSS property index: 6.
        """
        return BatchInt32ArrayProxy(self, 6)

    @Normal.setter
    def Normal(self, value: Union[AnyStr, int, enums.SwtControlState, List[AnyStr], List[int], List[enums.SwtControlState], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(6, value)
            return
    
        self._set_batch_int32_array(6, value)

    @property
    def Normal_str(self) -> str:
        """
        {Open | Closed] Normal state of the switch. If not Locked, the switch reverts to this state for reset, change of mode, etc. Defaults to first Action or State specified if not specifically declared.

        DSS property name: `Normal`, DSS property index: 6.
        """
        return self._get_batch_str_prop(6)

    @Normal_str.setter
    def Normal_str(self, value: AnyStr):
        self.Normal = value

    @property
    def State(self) -> BatchInt32ArrayProxy:
        """
        {Open | Closed] Present state of the switch. Upon setting, immediately forces state of switch.

        DSS property name: `State`, DSS property index: 7.
        """
        return BatchInt32ArrayProxy(self, 7)

    @State.setter
    def State(self, value: Union[AnyStr, int, enums.SwtControlState, List[AnyStr], List[int], List[enums.SwtControlState], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(7, value)
            return
    
        self._set_batch_int32_array(7, value)

    @property
    def State_str(self) -> str:
        """
        {Open | Closed] Present state of the switch. Upon setting, immediately forces state of switch.

        DSS property name: `State`, DSS property index: 7.
        """
        return self._get_batch_str_prop(7)

    @State_str.setter
    def State_str(self, value: AnyStr):
        self.State = value

    def Reset(self, value: Union[bool, List[bool]] = True):
        """
        {Yes | No} If Yes, forces Reset of switch to Normal state and removes Lock independently of any internal reset command for mode change, etc.

        DSS property name: `Reset`, DSS property index: 8.
        """
        self._set_batch_int32_array(8, value)

    @property
    def BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    @BaseFreq.setter
    def BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(9, value)

    @property
    def Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 10.
        """
        return [v != 0 for v in 
            self._get_batch_int32_prop(10)
        ]
    @Enabled.setter
    def Enabled(self, value: bool):
        self._set_batch_int32_array(10, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 11.
        """
        self._set_batch_string(11, value)

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

class ISwtControl(IDSSObj,SwtControlBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, SwtControl, SwtControlBatch)
        SwtControlBatch.__init__(self, self._api_util, sync_cls=True)
        

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> SwtControl:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[SwtControlProperties]) -> SwtControl:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[SwtControlBatchProperties]) -> SwtControlBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
