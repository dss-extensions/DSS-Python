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
from .TCC_Curve import TCC_Curve

class Fuse(DSSObj, CktElementMixin):
    __slots__ = CktElementMixin._extra_slots
    _cls_name = 'Fuse'
    _cls_idx = 33
    _cls_prop_idx = {
        'monitoredobj': 1,
        'monitoredterm': 2,
        'switchedobj': 3,
        'switchedterm': 4,
        'fusecurve': 5,
        'ratedcurrent': 6,
        'delay': 7,
        'action': 8,
        'normal': 9,
        'state': 10,
        'basefreq': 11,
        'enabled': 12,
        'like': 13,
    }

    @property
    def MonitoredObj(self) -> str:
        """
        Full object name of the circuit element, typically a line, transformer, load, or generator, to which the Fuse is connected. This is the "monitored" element. There is no default; must be specified.

        DSS property name: `MonitoredObj`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    @MonitoredObj.setter
    def MonitoredObj(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_obj(1, value)
            return

        self._set_string_o(1, value)

    @property
    def MonitoredObj_obj(self) -> DSSObj:
        """
        Full object name of the circuit element, typically a line, transformer, load, or generator, to which the Fuse is connected. This is the "monitored" element. There is no default; must be specified.

        DSS property name: `MonitoredObj`, DSS property index: 1.
        """
        return self._get_obj(1, None)

    @MonitoredObj_obj.setter
    def MonitoredObj_obj(self, value: DSSObj):
        self._set_obj(1, value)

    @property
    def MonitoredTerm(self) -> int:
        """
        Number of the terminal of the circuit element to which the Fuse is connected. 1 or 2, typically.  Default is 1.

        DSS property name: `MonitoredTerm`, DSS property index: 2.
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @MonitoredTerm.setter
    def MonitoredTerm(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def SwitchedObj(self) -> str:
        """
        Name of circuit element switch that the Fuse controls. Specify the full object name.Defaults to the same as the Monitored element. This is the "controlled" element.

        DSS property name: `SwitchedObj`, DSS property index: 3.
        """
        return self._get_prop_string(3)

    @SwitchedObj.setter
    def SwitchedObj(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_obj(3, value)
            return

        self._set_string_o(3, value)

    @property
    def SwitchedObj_obj(self) -> DSSObj:
        """
        Name of circuit element switch that the Fuse controls. Specify the full object name.Defaults to the same as the Monitored element. This is the "controlled" element.

        DSS property name: `SwitchedObj`, DSS property index: 3.
        """
        return self._get_obj(3, None)

    @SwitchedObj_obj.setter
    def SwitchedObj_obj(self, value: DSSObj):
        self._set_obj(3, value)

    @property
    def SwitchedTerm(self) -> int:
        """
        Number of the terminal of the controlled element in which the switch is controlled by the Fuse. 1 or 2, typically.  Default is 1.  Assumes all phases of the element have a fuse of this type.

        DSS property name: `SwitchedTerm`, DSS property index: 4.
        """
        return self._lib.Obj_GetInt32(self._ptr, 4)

    @SwitchedTerm.setter
    def SwitchedTerm(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 4, value)

    @property
    def FuseCurve(self) -> str:
        """
        Name of the TCC Curve object that determines the fuse blowing.  Must have been previously defined as a TCC_Curve object. Default is "Tlink". Multiplying the current values in the curve by the "RatedCurrent" value gives the actual current.

        DSS property name: `FuseCurve`, DSS property index: 5.
        """
        return self._get_prop_string(5)

    @FuseCurve.setter
    def FuseCurve(self, value: Union[AnyStr, TCC_Curve]):
        if isinstance(value, DSSObj):
            self._set_obj(5, value)
            return

        self._set_string_o(5, value)

    @property
    def FuseCurve_obj(self) -> TCC_Curve:
        """
        Name of the TCC Curve object that determines the fuse blowing.  Must have been previously defined as a TCC_Curve object. Default is "Tlink". Multiplying the current values in the curve by the "RatedCurrent" value gives the actual current.

        DSS property name: `FuseCurve`, DSS property index: 5.
        """
        return self._get_obj(5, TCC_Curve)

    @FuseCurve_obj.setter
    def FuseCurve_obj(self, value: TCC_Curve):
        self._set_obj(5, value)

    @property
    def RatedCurrent(self) -> float:
        """
        Multiplier or actual phase amps for the phase TCC curve.  Defaults to 1.0.

        DSS property name: `RatedCurrent`, DSS property index: 6.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    @RatedCurrent.setter
    def RatedCurrent(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 6, value)

    @property
    def Delay(self) -> float:
        """
        Fixed delay time (sec) added to Fuse blowing time determined from the TCC curve. Default is 0.0. Used to represent fuse clearing time or any other delay.

        DSS property name: `Delay`, DSS property index: 7.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @Delay.setter
    def Delay(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    def Action(self, value: Union[AnyStr, int, enums.FuseAction]):
        """
        DEPRECATED. See "State" property.

        DSS property name: `Action`, DSS property index: 8.
        """
        if isinstance(value, int):
            self._lib.Obj_SetInt32(self._ptr, 8, value)
            return
    
        self._set_string_o(8, value)

    def close(self):
        '''Shortcut to Action(FuseAction.close)'''
        self._lib.Obj_SetInt32(self._ptr, 8, enums.FuseAction.close)

    def open(self):
        '''Shortcut to Action(FuseAction.open)'''
        self._lib.Obj_SetInt32(self._ptr, 8, enums.FuseAction.open)

    @property
    def Normal(self) -> List[enums.FuseState]:
        """
        ARRAY of strings {Open | Closed} representing the Normal state of the fuse in each phase of the controlled element. The fuse reverts to this state for reset, change of mode, etc. Defaults to "State" if not specifically declared.

        DSS property name: `Normal`, DSS property index: 9.
        """
        return [enums.FuseState(val) for val in self._get_int32_list(self._lib.Obj_GetInt32Array, self._ptr, 9)]

    @Normal.setter
    def Normal(self, value: Union[List[Union[int, enums.FuseState]], List[AnyStr]]):
        if len(value) and not isinstance(value[0], int):
            self._set_string_array_o(9, value)
            return    
        self._set_int32_array_o(9, value)

    @property
    def Normal_str(self) -> List[str]:
        """
        ARRAY of strings {Open | Closed} representing the Normal state of the fuse in each phase of the controlled element. The fuse reverts to this state for reset, change of mode, etc. Defaults to "State" if not specifically declared.

        DSS property name: `Normal`, DSS property index: 9.
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 9)

    @Normal_str.setter
    def Normal_str(self, value: AnyStr):
        self.Normal = value

    @property
    def State(self) -> List[enums.FuseState]:
        """
        ARRAY of strings {Open | Closed} representing the Actual state of the fuse in each phase of the controlled element. Upon setting, immediately forces state of fuse(s). Simulates manual control on Fuse. Defaults to Closed for all phases.

        DSS property name: `State`, DSS property index: 10.
        """
        return [enums.FuseState(val) for val in self._get_int32_list(self._lib.Obj_GetInt32Array, self._ptr, 10)]

    @State.setter
    def State(self, value: Union[List[Union[int, enums.FuseState]], List[AnyStr]]):
        if len(value) and not isinstance(value[0], int):
            self._set_string_array_o(10, value)
            return    
        self._set_int32_array_o(10, value)

    @property
    def State_str(self) -> List[str]:
        """
        ARRAY of strings {Open | Closed} representing the Actual state of the fuse in each phase of the controlled element. Upon setting, immediately forces state of fuse(s). Simulates manual control on Fuse. Defaults to Closed for all phases.

        DSS property name: `State`, DSS property index: 10.
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 10)

    @State_str.setter
    def State_str(self, value: AnyStr):
        self.State = value

    @property
    def BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 11.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @BaseFreq.setter
    def BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 12.
        """
        return self._lib.Obj_GetInt32(self._ptr, 12) != 0

    @Enabled.setter
    def Enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 12, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 13.
        """
        self._set_string_o(13, value)


class FuseProperties(TypedDict):
    MonitoredObj: Union[AnyStr, DSSObj]
    MonitoredTerm: int
    SwitchedObj: Union[AnyStr, DSSObj]
    SwitchedTerm: int
    FuseCurve: Union[AnyStr, TCC_Curve]
    RatedCurrent: float
    Delay: float
    Action: Union[AnyStr, int, enums.FuseAction]
    Normal: Union[List[Union[int, enums.FuseState]], List[AnyStr]]
    State: Union[List[Union[int, enums.FuseState]], List[AnyStr]]
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class FuseBatch(DSSBatch):
    _cls_name = 'Fuse'
    _obj_cls = Fuse
    _cls_idx = 33


    @property
    def MonitoredObj(self) -> List[str]:
        """
        Full object name of the circuit element, typically a line, transformer, load, or generator, to which the Fuse is connected. This is the "monitored" element. There is no default; must be specified.

        DSS property name: `MonitoredObj`, DSS property index: 1.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @MonitoredObj.setter
    def MonitoredObj(self, value: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]]):
        self._set_batch_obj_prop(1, value)

    @property
    def MonitoredObj_obj(self) -> List[DSSObj]:
        """
        Full object name of the circuit element, typically a line, transformer, load, or generator, to which the Fuse is connected. This is the "monitored" element. There is no default; must be specified.

        DSS property name: `MonitoredObj`, DSS property index: 1.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 1)

    @MonitoredObj_obj.setter
    def MonitoredObj_obj(self, value: DSSObj):
        self._set_batch_string(1, value)

    @property
    def MonitoredTerm(self) -> BatchInt32ArrayProxy:
        """
        Number of the terminal of the circuit element to which the Fuse is connected. 1 or 2, typically.  Default is 1.

        DSS property name: `MonitoredTerm`, DSS property index: 2.
        """
        return BatchInt32ArrayProxy(self, 2)

    @MonitoredTerm.setter
    def MonitoredTerm(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(2, value)

    @property
    def SwitchedObj(self) -> List[str]:
        """
        Name of circuit element switch that the Fuse controls. Specify the full object name.Defaults to the same as the Monitored element. This is the "controlled" element.

        DSS property name: `SwitchedObj`, DSS property index: 3.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 3)

    @SwitchedObj.setter
    def SwitchedObj(self, value: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]]):
        self._set_batch_obj_prop(3, value)

    @property
    def SwitchedObj_obj(self) -> List[DSSObj]:
        """
        Name of circuit element switch that the Fuse controls. Specify the full object name.Defaults to the same as the Monitored element. This is the "controlled" element.

        DSS property name: `SwitchedObj`, DSS property index: 3.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 3)

    @SwitchedObj_obj.setter
    def SwitchedObj_obj(self, value: DSSObj):
        self._set_batch_string(3, value)

    @property
    def SwitchedTerm(self) -> BatchInt32ArrayProxy:
        """
        Number of the terminal of the controlled element in which the switch is controlled by the Fuse. 1 or 2, typically.  Default is 1.  Assumes all phases of the element have a fuse of this type.

        DSS property name: `SwitchedTerm`, DSS property index: 4.
        """
        return BatchInt32ArrayProxy(self, 4)

    @SwitchedTerm.setter
    def SwitchedTerm(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(4, value)

    @property
    def FuseCurve(self) -> List[str]:
        """
        Name of the TCC Curve object that determines the fuse blowing.  Must have been previously defined as a TCC_Curve object. Default is "Tlink". Multiplying the current values in the curve by the "RatedCurrent" value gives the actual current.

        DSS property name: `FuseCurve`, DSS property index: 5.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 5)

    @FuseCurve.setter
    def FuseCurve(self, value: Union[AnyStr, TCC_Curve, List[AnyStr], List[TCC_Curve]]):
        self._set_batch_obj_prop(5, value)

    @property
    def FuseCurve_obj(self) -> List[TCC_Curve]:
        """
        Name of the TCC Curve object that determines the fuse blowing.  Must have been previously defined as a TCC_Curve object. Default is "Tlink". Multiplying the current values in the curve by the "RatedCurrent" value gives the actual current.

        DSS property name: `FuseCurve`, DSS property index: 5.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 5)

    @FuseCurve_obj.setter
    def FuseCurve_obj(self, value: TCC_Curve):
        self._set_batch_string(5, value)

    @property
    def RatedCurrent(self) -> BatchFloat64ArrayProxy:
        """
        Multiplier or actual phase amps for the phase TCC curve.  Defaults to 1.0.

        DSS property name: `RatedCurrent`, DSS property index: 6.
        """
        return BatchFloat64ArrayProxy(self, 6)

    @RatedCurrent.setter
    def RatedCurrent(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(6, value)

    @property
    def Delay(self) -> BatchFloat64ArrayProxy:
        """
        Fixed delay time (sec) added to Fuse blowing time determined from the TCC curve. Default is 0.0. Used to represent fuse clearing time or any other delay.

        DSS property name: `Delay`, DSS property index: 7.
        """
        return BatchFloat64ArrayProxy(self, 7)

    @Delay.setter
    def Delay(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(7, value)

    def Action(self, value: Union[AnyStr, int, enums.FuseAction]):
        """
        DEPRECATED. See "State" property.

        DSS property name: `Action`, DSS property index: 8.
        """
        if isinstance(value, (bytes, str)) or (isinstance(value, LIST_LIKE) and len(value) > 0 and isinstance(value[0], (bytes, str))):
            self._set_batch_string(8, value)
        else:
            self._set_batch_int32_array(8, value)

    def close(self):
        '''Shortcut to Action(FuseAction.close)'''
        self._set_batch_int32_array(8, enums.FuseAction.close)

    def open(self):
        '''Shortcut to Action(FuseAction.open)'''
        self._set_batch_int32_array(8, enums.FuseAction.open)

    @property
    def Normal(self) -> List[Int32Array]:
        """
        ARRAY of strings {Open | Closed} representing the Normal state of the fuse in each phase of the controlled element. The fuse reverts to this state for reset, change of mode, etc. Defaults to "State" if not specifically declared.

        DSS property name: `Normal`, DSS property index: 9.
        """
        return [
            self._get_int32_array(self._lib.Obj_GetInt32Array, x, 9)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Normal.setter
    def Normal(self, value: Union[List[Union[int, enums.FuseState]], List[AnyStr]]): #TODO: list of lists
        if len(value) and not isinstance(value[0], int):
            value, value_ptr, value_count = self._prepare_string_array(value)
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetStringArray(x, 9, value_ptr, value_count)

            self._check_for_error()
            return

        self._set_batch_int32_array(9, value)

    @property
    def Normal_str(self) -> List[List[str]]:
        """
        ARRAY of strings {Open | Closed} representing the Normal state of the fuse in each phase of the controlled element. The fuse reverts to this state for reset, change of mode, etc. Defaults to "State" if not specifically declared.

        DSS property name: `Normal`, DSS property index: 9.
        """
        return self._get_string_ll(9)

    @Normal_str.setter
    def Normal_str(self, value: AnyStr):
        self.Normal = value

    @property
    def State(self) -> List[Int32Array]:
        """
        ARRAY of strings {Open | Closed} representing the Actual state of the fuse in each phase of the controlled element. Upon setting, immediately forces state of fuse(s). Simulates manual control on Fuse. Defaults to Closed for all phases.

        DSS property name: `State`, DSS property index: 10.
        """
        return [
            self._get_int32_array(self._lib.Obj_GetInt32Array, x, 10)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @State.setter
    def State(self, value: Union[List[Union[int, enums.FuseState]], List[AnyStr]]): #TODO: list of lists
        if len(value) and not isinstance(value[0], int):
            value, value_ptr, value_count = self._prepare_string_array(value)
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetStringArray(x, 10, value_ptr, value_count)

            self._check_for_error()
            return

        self._set_batch_int32_array(10, value)

    @property
    def State_str(self) -> List[List[str]]:
        """
        ARRAY of strings {Open | Closed} representing the Actual state of the fuse in each phase of the controlled element. Upon setting, immediately forces state of fuse(s). Simulates manual control on Fuse. Defaults to Closed for all phases.

        DSS property name: `State`, DSS property index: 10.
        """
        return self._get_string_ll(10)

    @State_str.setter
    def State_str(self, value: AnyStr):
        self.State = value

    @property
    def BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 11.
        """
        return BatchFloat64ArrayProxy(self, 11)

    @BaseFreq.setter
    def BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(11, value)

    @property
    def Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 12.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 12)
        ]
    @Enabled.setter
    def Enabled(self, value: bool):
        self._set_batch_int32_array(12, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 13.
        """
        self._set_batch_string(13, value)

class FuseBatchProperties(TypedDict):
    MonitoredObj: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]]
    MonitoredTerm: Union[int, Int32Array]
    SwitchedObj: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]]
    SwitchedTerm: Union[int, Int32Array]
    FuseCurve: Union[AnyStr, TCC_Curve, List[AnyStr], List[TCC_Curve]]
    RatedCurrent: Union[float, Float64Array]
    Delay: Union[float, Float64Array]
    Action: Union[AnyStr, int, enums.FuseAction]
    Normal: Union[List[Union[int, enums.FuseState]], List[AnyStr]]
    State: Union[List[Union[int, enums.FuseState]], List[AnyStr]]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IFuse(IDSSObj):
    __slots__ = ()

    def __init__(self, iobj):
        super().__init__(iobj, Fuse, FuseBatch)

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Fuse:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[FuseProperties]) -> Fuse:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[FuseBatchProperties]) -> FuseBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
