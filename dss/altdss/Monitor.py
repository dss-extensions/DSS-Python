# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from typing_extensions import TypedDict, Unpack
from ._obj_bases import (
    CktElementMixin,
    MonitorObjMixin,
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

class Monitor(DSSObj, CktElementMixin, MonitorObjMixin):
    __slots__ = CktElementMixin._extra_slots + MonitorObjMixin._extra_slots
    _cls_name = 'Monitor'
    _cls_idx = 47
    _cls_prop_idx = {
        'element': 1,
        'terminal': 2,
        'mode': 3,
        'action': 4,
        'residual': 5,
        'vipolar': 6,
        'ppolar': 7,
        'basefreq': 8,
        'enabled': 9,
        'like': 10,
    }

    @property
    def Element(self) -> str:
        """
        Name (Full Object name) of element to which the monitor is connected.

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
        Name (Full Object name) of element to which the monitor is connected.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_obj(1, None)

    @Element_obj.setter
    def Element_obj(self, value: DSSObj):
        self._set_obj(1, value)

    @property
    def Terminal(self) -> int:
        """
        Number of the terminal of the circuit element to which the monitor is connected. 1 or 2, typically. For monitoring states, attach monitor to terminal 1.

        DSS property name: `Terminal`, DSS property index: 2.
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @Terminal.setter
    def Terminal(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def Mode(self) -> int:
        """
        Bitmask integer designating the values the monitor is to capture: 
        0 = Voltages and currents at designated terminal
        1 = Powers at designated terminal
        2 = Tap Position (Transformer Device only)
        3 = State Variables (PCElements only)
        4 = Flicker level and severity index (Pst) for voltages. No adders apply.
            Flicker level at simulation time step, Pst at 10-minute time step.
        5 = Solution variables (Iterations, etc).
        Normally, these would be actual phasor quantities from solution.
        6 = Capacitor Switching (Capacitors only)
        7 = Storage state vars (Storage device only)
        8 = All winding currents (Transformer device only)
        9 = Losses, watts and var (of monitored device)
        10 = All Winding voltages (Transformer device only)
        Normally, these would be actual phasor quantities from solution.
        11 = All terminal node voltages and line currents of monitored device
        12 = All terminal node voltages LL and line currents of monitored device
        Combine mode with adders below to achieve other results for terminal quantities:
        +16 = Sequence quantities
        +32 = Magnitude only
        +64 = Positive sequence only or avg of all phases

        Mix adder to obtain desired results. For example:
        Mode=112 will save positive sequence voltage and current magnitudes only
        Mode=48 will save all sequence voltages and currents, but magnitude only.

        DSS property name: `Mode`, DSS property index: 3.
        """
        return self._lib.Obj_GetInt32(self._ptr, 3)

    @Mode.setter
    def Mode(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 3, value)

    def Action(self, value: Union[AnyStr, int, enums.MonitorAction]):
        """
        {Clear | Save | Take | Process}
        (C)lears or (S)aves current buffer.
        (T)ake action takes a sample.
        (P)rocesses the data taken so far (e.g. Pst for mode 4).

        Note that monitors are automatically reset (cleared) when the Set Mode= command is issued. Otherwise, the user must explicitly reset all monitors (reset monitors command) or individual monitors with the Clear action.

        DSS property name: `Action`, DSS property index: 4.
        """
        if isinstance(value, int):
            self._lib.Obj_SetInt32(self._ptr, 4, value)
            return
    
        self._set_string_o(4, value)

    def Clear(self):
        '''Shortcut to Action(MonitorAction.Clear)'''
        self._lib.Obj_SetInt32(self._ptr, 4, enums.MonitorAction.Clear)

    def Save(self):
        '''Shortcut to Action(MonitorAction.Save)'''
        self._lib.Obj_SetInt32(self._ptr, 4, enums.MonitorAction.Save)

    def TakeSample(self):
        '''Shortcut to Action(MonitorAction.TakeSample)'''
        self._lib.Obj_SetInt32(self._ptr, 4, enums.MonitorAction.TakeSample)

    def Process(self):
        '''Shortcut to Action(MonitorAction.Process)'''
        self._lib.Obj_SetInt32(self._ptr, 4, enums.MonitorAction.Process)

    def Reset(self):
        '''Shortcut to Action(MonitorAction.Reset)'''
        self._lib.Obj_SetInt32(self._ptr, 4, enums.MonitorAction.Reset)

    @property
    def Residual(self) -> bool:
        """
        {Yes/True | No/False} Default = No.  Include Residual cbannel (sum of all phases) for voltage and current. Does not apply to sequence quantity modes or power modes.

        DSS property name: `Residual`, DSS property index: 5.
        """
        return self._lib.Obj_GetInt32(self._ptr, 5) != 0

    @Residual.setter
    def Residual(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 5, value)

    @property
    def VIPolar(self) -> bool:
        """
        {Yes/True | No/False} Default = YES. Report voltage and current in polar form (Mag/Angle). (default)  Otherwise, it will be real and imaginary.

        DSS property name: `VIPolar`, DSS property index: 6.
        """
        return self._lib.Obj_GetInt32(self._ptr, 6) != 0

    @VIPolar.setter
    def VIPolar(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 6, value)

    @property
    def PPolar(self) -> bool:
        """
        {Yes/True | No/False} Default = YES. Report power in Apparent power, S, in polar form (Mag/Angle).(default)  Otherwise, is P and Q

        DSS property name: `PPolar`, DSS property index: 7.
        """
        return self._lib.Obj_GetInt32(self._ptr, 7) != 0

    @PPolar.setter
    def PPolar(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 7, value)

    @property
    def BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @BaseFreq.setter
    def BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 9.
        """
        return self._lib.Obj_GetInt32(self._ptr, 9) != 0

    @Enabled.setter
    def Enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 9, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 10.
        """
        self._set_string_o(10, value)


class MonitorProperties(TypedDict):
    Element: Union[AnyStr, DSSObj]
    Terminal: int
    Mode: int
    Action: Union[AnyStr, int, enums.MonitorAction]
    Residual: bool
    VIPolar: bool
    PPolar: bool
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class MonitorBatch(DSSBatch):
    _cls_name = 'Monitor'
    _obj_cls = Monitor
    _cls_idx = 47


    @property
    def Element(self) -> List[str]:
        """
        Name (Full Object name) of element to which the monitor is connected.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @Element.setter
    def Element(self, value: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]]):
        self._set_batch_obj_prop(1, value)

    @property
    def Element_obj(self) -> List[DSSObj]:
        """
        Name (Full Object name) of element to which the monitor is connected.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 1)

    @Element_obj.setter
    def Element_obj(self, value: DSSObj):
        self._set_batch_string(1, value)

    @property
    def Terminal(self) -> BatchInt32ArrayProxy:
        """
        Number of the terminal of the circuit element to which the monitor is connected. 1 or 2, typically. For monitoring states, attach monitor to terminal 1.

        DSS property name: `Terminal`, DSS property index: 2.
        """
        return BatchInt32ArrayProxy(self, 2)

    @Terminal.setter
    def Terminal(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(2, value)

    @property
    def Mode(self) -> BatchInt32ArrayProxy:
        """
        Bitmask integer designating the values the monitor is to capture: 
        0 = Voltages and currents at designated terminal
        1 = Powers at designated terminal
        2 = Tap Position (Transformer Device only)
        3 = State Variables (PCElements only)
        4 = Flicker level and severity index (Pst) for voltages. No adders apply.
            Flicker level at simulation time step, Pst at 10-minute time step.
        5 = Solution variables (Iterations, etc).
        Normally, these would be actual phasor quantities from solution.
        6 = Capacitor Switching (Capacitors only)
        7 = Storage state vars (Storage device only)
        8 = All winding currents (Transformer device only)
        9 = Losses, watts and var (of monitored device)
        10 = All Winding voltages (Transformer device only)
        Normally, these would be actual phasor quantities from solution.
        11 = All terminal node voltages and line currents of monitored device
        12 = All terminal node voltages LL and line currents of monitored device
        Combine mode with adders below to achieve other results for terminal quantities:
        +16 = Sequence quantities
        +32 = Magnitude only
        +64 = Positive sequence only or avg of all phases

        Mix adder to obtain desired results. For example:
        Mode=112 will save positive sequence voltage and current magnitudes only
        Mode=48 will save all sequence voltages and currents, but magnitude only.

        DSS property name: `Mode`, DSS property index: 3.
        """
        return BatchInt32ArrayProxy(self, 3)

    @Mode.setter
    def Mode(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(3, value)

    def Action(self, value: Union[AnyStr, int, enums.MonitorAction]):
        """
        {Clear | Save | Take | Process}
        (C)lears or (S)aves current buffer.
        (T)ake action takes a sample.
        (P)rocesses the data taken so far (e.g. Pst for mode 4).

        Note that monitors are automatically reset (cleared) when the Set Mode= command is issued. Otherwise, the user must explicitly reset all monitors (reset monitors command) or individual monitors with the Clear action.

        DSS property name: `Action`, DSS property index: 4.
        """
        if isinstance(value, (bytes, str)) or (isinstance(value, LIST_LIKE) and len(value) > 0 and isinstance(value[0], (bytes, str))):
            self._set_batch_string(4, value)
        else:
            self._set_batch_int32_array(4, value)

    def Clear(self):
        '''Shortcut to Action(MonitorAction.Clear)'''
        self._set_batch_int32_array(4, enums.MonitorAction.Clear)

    def Save(self):
        '''Shortcut to Action(MonitorAction.Save)'''
        self._set_batch_int32_array(4, enums.MonitorAction.Save)

    def TakeSample(self):
        '''Shortcut to Action(MonitorAction.TakeSample)'''
        self._set_batch_int32_array(4, enums.MonitorAction.TakeSample)

    def Process(self):
        '''Shortcut to Action(MonitorAction.Process)'''
        self._set_batch_int32_array(4, enums.MonitorAction.Process)

    def Reset(self):
        '''Shortcut to Action(MonitorAction.Reset)'''
        self._set_batch_int32_array(4, enums.MonitorAction.Reset)

    @property
    def Residual(self) -> List[bool]:
        """
        {Yes/True | No/False} Default = No.  Include Residual cbannel (sum of all phases) for voltage and current. Does not apply to sequence quantity modes or power modes.

        DSS property name: `Residual`, DSS property index: 5.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 5)
        ]
    @Residual.setter
    def Residual(self, value: bool):
        self._set_batch_int32_array(5, value)

    @property
    def VIPolar(self) -> List[bool]:
        """
        {Yes/True | No/False} Default = YES. Report voltage and current in polar form (Mag/Angle). (default)  Otherwise, it will be real and imaginary.

        DSS property name: `VIPolar`, DSS property index: 6.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 6)
        ]
    @VIPolar.setter
    def VIPolar(self, value: bool):
        self._set_batch_int32_array(6, value)

    @property
    def PPolar(self) -> List[bool]:
        """
        {Yes/True | No/False} Default = YES. Report power in Apparent power, S, in polar form (Mag/Angle).(default)  Otherwise, is P and Q

        DSS property name: `PPolar`, DSS property index: 7.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 7)
        ]
    @PPolar.setter
    def PPolar(self, value: bool):
        self._set_batch_int32_array(7, value)

    @property
    def BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    @BaseFreq.setter
    def BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(8, value)

    @property
    def Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 9.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 9)
        ]
    @Enabled.setter
    def Enabled(self, value: bool):
        self._set_batch_int32_array(9, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 10.
        """
        self._set_batch_string(10, value)

class MonitorBatchProperties(TypedDict):
    Element: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]]
    Terminal: Union[int, Int32Array]
    Mode: Union[int, Int32Array]
    Action: Union[AnyStr, int, enums.MonitorAction]
    Residual: bool
    VIPolar: bool
    PPolar: bool
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IMonitor(IDSSObj):
    __slots__ = ()

    def __init__(self, iobj):
        super().__init__(iobj, Monitor, MonitorBatch)

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Monitor:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[MonitorProperties]) -> Monitor:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[MonitorBatchProperties]) -> MonitorBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
