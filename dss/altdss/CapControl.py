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
from .Capacitor import Capacitor as CapacitorObj
from .LoadShape import LoadShape

class CapControl(DSSObj, CircuitElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots
    _cls_name = 'CapControl'
    _cls_idx = 24
    _cls_prop_idx = {
        'element': 1,
        'terminal': 2,
        'capacitor': 3,
        'type': 4,
        'ptratio': 5,
        'ctratio': 6,
        'onsetting': 7,
        'offsetting': 8,
        'delay': 9,
        'voltoverride': 10,
        'vmax': 11,
        'vmin': 12,
        'delayoff': 13,
        'deadtime': 14,
        'ctphase': 15,
        'ptphase': 16,
        'vbus': 17,
        'eventlog': 18,
        'usermodel': 19,
        'userdata': 20,
        'pctminkvar': 21,
        'reset': 22,
        'controlsignal': 23,
        'basefreq': 24,
        'enabled': 25,
        'like': 26,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)

    def _get_Element_str(self) -> str:
        """
        Full object name of the circuit element, typically a line or transformer, to which the capacitor control's PT and/or CT are connected.There is no default; must be specified.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    def _set_Element_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(1, value, flags)

    Element_str = property(_get_Element_str, _set_Element_str) # type: str

    def _get_Element(self) -> DSSObj:
        """
        Full object name of the circuit element, typically a line or transformer, to which the capacitor control's PT and/or CT are connected.There is no default; must be specified.

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
        Number of the terminal of the circuit element to which the CapControl is connected. 1 or 2, typically.  Default is 1.

        DSS property name: `Terminal`, DSS property index: 2.
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    def _set_Terminal(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 2, value, flags)

    Terminal = property(_get_Terminal, _set_Terminal) # type: int

    def _get_Capacitor_str(self) -> str:
        """
        Name of Capacitor element which the CapControl controls. No Default; Must be specified.Do not specify the full object name; "Capacitor" is assumed for the object class.  Example:

        Capacitor=cap1

        DSS property name: `Capacitor`, DSS property index: 3.
        """
        return self._get_prop_string(3)

    def _set_Capacitor_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(3, value, flags)

    Capacitor_str = property(_get_Capacitor_str, _set_Capacitor_str) # type: str

    def _get_Capacitor(self) -> CapacitorObj:
        """
        Name of Capacitor element which the CapControl controls. No Default; Must be specified.Do not specify the full object name; "Capacitor" is assumed for the object class.  Example:

        Capacitor=cap1

        DSS property name: `Capacitor`, DSS property index: 3.
        """
        return self._get_obj(3, CapacitorObj)

    def _set_Capacitor(self, value: Union[AnyStr, CapacitorObj], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(3, value, flags)
            return

        self._set_string_o(3, value, flags)

    Capacitor = property(_get_Capacitor, _set_Capacitor) # type: CapacitorObj

    def _get_Type(self) -> enums.CapControlType:
        """
        {Current | Voltage | kvar | PF | Time | Follow} Control type.  Specify the ONsetting and OFFsetting appropriately with the type of control. (See help for ONsetting)

        DSS property name: `Type`, DSS property index: 4.
        """
        return enums.CapControlType(self._lib.Obj_GetInt32(self._ptr, 4))

    def _set_Type(self, value: Union[AnyStr, int, enums.CapControlType], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(4, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 4, value, flags)

    Type = property(_get_Type, _set_Type) # type: enums.CapControlType

    def _get_Type_str(self) -> str:
        """
        {Current | Voltage | kvar | PF | Time | Follow} Control type.  Specify the ONsetting and OFFsetting appropriately with the type of control. (See help for ONsetting)

        DSS property name: `Type`, DSS property index: 4.
        """
        return self._get_prop_string(4)

    def _set_Type_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Type(value, flags)

    Type_str = property(_get_Type_str, _set_Type_str) # type: str

    def _get_PTRatio(self) -> float:
        """
        Ratio of the PT that converts the monitored voltage to the control voltage. Default is 60.  If the capacitor is Wye, the 1st phase line-to-neutral voltage is monitored.  Else, the line-to-line voltage (1st - 2nd phase) is monitored.

        DSS property name: `PTRatio`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    def _set_PTRatio(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 5, value, flags)

    PTRatio = property(_get_PTRatio, _set_PTRatio) # type: float

    def _get_CTRatio(self) -> float:
        """
        Ratio of the CT from line amps to control ampere setting for current and kvar control types. 

        DSS property name: `CTRatio`, DSS property index: 6.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    def _set_CTRatio(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 6, value, flags)

    CTRatio = property(_get_CTRatio, _set_CTRatio) # type: float

    def _get_OnSetting(self) -> float:
        """
        Value at which the control arms to switch the capacitor ON (or ratchet up a step).  

        Type of Control:

        Current: Line Amps / CTratio
        Voltage: Line-Neutral (or Line-Line for delta) Volts / PTratio
        kvar:    Total kvar, all phases (3-phase for pos seq model). This is directional. 
        PF:      Power Factor, Total power in monitored terminal. Negative for Leading. 
        Time:    Hrs from Midnight as a floating point number (decimal). 7:30am would be entered as 7.5.
        Follow:  Follows a loadshape (ControlSignal) to determine when to turn ON/OFF the capacitor. If the value is different than 0 the capacitor will connect to the grid, otherwise, it will be disconnected.

        DSS property name: `OnSetting`, DSS property index: 7.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    def _set_OnSetting(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 7, value, flags)

    OnSetting = property(_get_OnSetting, _set_OnSetting) # type: float

    def _get_OffSetting(self) -> float:
        """
        Value at which the control arms to switch the capacitor OFF. (See help for ONsetting)For Time control, is OK to have Off time the next day ( < On time)

        DSS property name: `OffSetting`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    def _set_OffSetting(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 8, value, flags)

    OffSetting = property(_get_OffSetting, _set_OffSetting) # type: float

    def _get_Delay(self) -> float:
        """
        Time delay, in seconds, from when the control is armed before it sends out the switching command to turn ON.  The control may reset before the action actually occurs. This is used to determine which capacity control will act first. Default is 15.  You may specify any floating point number to achieve a model of whatever condition is necessary.

        DSS property name: `Delay`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    def _set_Delay(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 9, value, flags)

    Delay = property(_get_Delay, _set_Delay) # type: float

    def _get_VoltOverride(self) -> bool:
        """
        {Yes | No}  Default is No.  Switch to indicate whether VOLTAGE OVERRIDE is to be considered. Vmax and Vmin must be set to reasonable values if this property is Yes.

        DSS property name: `VoltOverride`, DSS property index: 10.
        """
        return self._lib.Obj_GetInt32(self._ptr, 10) != 0

    def _set_VoltOverride(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 10, value, flags)

    VoltOverride = property(_get_VoltOverride, _set_VoltOverride) # type: bool

    def _get_VMax(self) -> float:
        """
        Maximum voltage, in volts.  If the voltage across the capacitor divided by the PTRATIO is greater than this voltage, the capacitor will switch OFF regardless of other control settings. Default is 126 (goes with a PT ratio of 60 for 12.47 kV system).

        DSS property name: `VMax`, DSS property index: 11.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    def _set_VMax(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 11, value, flags)

    VMax = property(_get_VMax, _set_VMax) # type: float

    def _get_VMin(self) -> float:
        """
        Minimum voltage, in volts.  If the voltage across the capacitor divided by the PTRATIO is less than this voltage, the capacitor will switch ON regardless of other control settings. Default is 115 (goes with a PT ratio of 60 for 12.47 kV system).

        DSS property name: `VMin`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    def _set_VMin(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 12, value, flags)

    VMin = property(_get_VMin, _set_VMin) # type: float

    def _get_DelayOff(self) -> float:
        """
        Time delay, in seconds, for control to turn OFF when present state is ON. Default is 15.

        DSS property name: `DelayOff`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    def _set_DelayOff(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 13, value, flags)

    DelayOff = property(_get_DelayOff, _set_DelayOff) # type: float

    def _get_DeadTime(self) -> float:
        """
        Dead time after capacitor is turned OFF before it can be turned back ON. Default is 300 sec.

        DSS property name: `DeadTime`, DSS property index: 14.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    def _set_DeadTime(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 14, value, flags)

    DeadTime = property(_get_DeadTime, _set_DeadTime) # type: float

    def _get_CTPhase(self) -> Union[enums.MonitoredPhase, int]:
        """
        Number of the phase being monitored for CURRENT control or one of {AVG | MAX | MIN} for all phases. Default=1. If delta or L-L connection, enter the first or the two phases being monitored [1-2, 2-3, 3-1]. Must be less than the number of phases. Does not apply to kvar control which uses all phases by default.

        DSS property name: `CTPhase`, DSS property index: 15.
        """
        value = self._lib.Obj_GetInt32(self._ptr, 15)
        if value > 0:
            return value

        return enums.MonitoredPhase(value)

    def _set_CTPhase(self, value: Union[AnyStr, int, enums.MonitoredPhase], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(15, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 15, value, flags)

    CTPhase = property(_get_CTPhase, _set_CTPhase) # type: enums.MonitoredPhase

    def _get_CTPhase_str(self) -> str:
        """
        Number of the phase being monitored for CURRENT control or one of {AVG | MAX | MIN} for all phases. Default=1. If delta or L-L connection, enter the first or the two phases being monitored [1-2, 2-3, 3-1]. Must be less than the number of phases. Does not apply to kvar control which uses all phases by default.

        DSS property name: `CTPhase`, DSS property index: 15.
        """
        return self._get_prop_string(15)

    def _set_CTPhase_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_CTPhase(value, flags)

    CTPhase_str = property(_get_CTPhase_str, _set_CTPhase_str) # type: str

    def _get_PTPhase(self) -> Union[enums.MonitoredPhase, int]:
        """
        Number of the phase being monitored for VOLTAGE control or one of {AVG | MAX | MIN} for all phases. Default=1. If delta or L-L connection, enter the first or the two phases being monitored [1-2, 2-3, 3-1]. Must be less than the number of phases. Does not apply to kvar control which uses all phases by default.

        DSS property name: `PTPhase`, DSS property index: 16.
        """
        value = self._lib.Obj_GetInt32(self._ptr, 16)
        if value > 0:
            return value

        return enums.MonitoredPhase(value)

    def _set_PTPhase(self, value: Union[AnyStr, int, enums.MonitoredPhase], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(16, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 16, value, flags)

    PTPhase = property(_get_PTPhase, _set_PTPhase) # type: enums.MonitoredPhase

    def _get_PTPhase_str(self) -> str:
        """
        Number of the phase being monitored for VOLTAGE control or one of {AVG | MAX | MIN} for all phases. Default=1. If delta or L-L connection, enter the first or the two phases being monitored [1-2, 2-3, 3-1]. Must be less than the number of phases. Does not apply to kvar control which uses all phases by default.

        DSS property name: `PTPhase`, DSS property index: 16.
        """
        return self._get_prop_string(16)

    def _set_PTPhase_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_PTPhase(value, flags)

    PTPhase_str = property(_get_PTPhase_str, _set_PTPhase_str) # type: str

    def _get_VBus(self) -> str:
        """
        Name of bus to use for voltage override function. Default is bus at monitored terminal. Sometimes it is useful to monitor a bus in another location to emulate various DMS control algorithms.

        DSS property name: `VBus`, DSS property index: 17.
        """
        return self._get_prop_string(17)

    def _set_VBus(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(17, value, flags)

    VBus = property(_get_VBus, _set_VBus) # type: str

    def _get_EventLog(self) -> bool:
        """
        {Yes/True | No/False*} Default is NO for CapControl. Log control actions to Eventlog.

        DSS property name: `EventLog`, DSS property index: 18.
        """
        return self._lib.Obj_GetInt32(self._ptr, 18) != 0

    def _set_EventLog(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 18, value, flags)

    EventLog = property(_get_EventLog, _set_EventLog) # type: bool

    def _get_UserModel(self) -> str:
        """
        Name of DLL containing user-written CapControl model, overriding the default model.  Set to "none" to negate previous setting. 

        DSS property name: `UserModel`, DSS property index: 19.
        """
        return self._get_prop_string(19)

    def _set_UserModel(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(19, value, flags)

    UserModel = property(_get_UserModel, _set_UserModel) # type: str

    def _get_UserData(self) -> str:
        """
        String (in quotes or parentheses if necessary) that gets passed to the user-written CapControl model Edit function for defining the data required for that model. 

        DSS property name: `UserData`, DSS property index: 20.
        """
        return self._get_prop_string(20)

    def _set_UserData(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(20, value, flags)

    UserData = property(_get_UserData, _set_UserData) # type: str

    def _get_pctMinkvar(self) -> float:
        """
        For PF control option, min percent of total bank kvar at which control will close capacitor switch. Default = 50.

        DSS property name: `pctMinkvar`, DSS property index: 21.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    def _set_pctMinkvar(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 21, value, flags)

    pctMinkvar = property(_get_pctMinkvar, _set_pctMinkvar) # type: float

    def Reset(self, value: bool = True, flags: enums.SetterFlags = 0):
        """
        {Yes | No} If Yes, forces Reset of this CapControl.

        DSS property name: `Reset`, DSS property index: 22.
        """
        self._lib.Obj_SetInt32(self._ptr, 22, value, flags)

    def _get_ControlSignal_str(self) -> str:
        """
        Load shape used for controlling the connection/disconnection of the capacitor to the grid, when the load shape is DIFFERENT than ZERO (0) the capacitor will be ON and connected to the grid. Otherwise, if the load shape value is EQUAL to ZERO (0) the capacitor bank will be OFF and disconnected from the grid.

        DSS property name: `ControlSignal`, DSS property index: 23.
        """
        return self._get_prop_string(23)

    def _set_ControlSignal_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(23, value, flags)

    ControlSignal_str = property(_get_ControlSignal_str, _set_ControlSignal_str) # type: str

    def _get_ControlSignal(self) -> LoadShape:
        """
        Load shape used for controlling the connection/disconnection of the capacitor to the grid, when the load shape is DIFFERENT than ZERO (0) the capacitor will be ON and connected to the grid. Otherwise, if the load shape value is EQUAL to ZERO (0) the capacitor bank will be OFF and disconnected from the grid.

        DSS property name: `ControlSignal`, DSS property index: 23.
        """
        return self._get_obj(23, LoadShape)

    def _set_ControlSignal(self, value: Union[AnyStr, LoadShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(23, value, flags)
            return

        self._set_string_o(23, value, flags)

    ControlSignal = property(_get_ControlSignal, _set_ControlSignal) # type: LoadShape

    def _get_BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 24.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 24, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float

    def _get_Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 25.
        """
        return self._lib.Obj_GetInt32(self._ptr, 25) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 25, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 26.
        """
        self._set_string_o(26, value)


class CapControlProperties(TypedDict):
    Element: Union[AnyStr, DSSObj]
    Terminal: int
    Capacitor: Union[AnyStr, CapacitorObj]
    Type: Union[AnyStr, int, enums.CapControlType]
    PTRatio: float
    CTRatio: float
    OnSetting: float
    OffSetting: float
    Delay: float
    VoltOverride: bool
    VMax: float
    VMin: float
    DelayOff: float
    DeadTime: float
    CTPhase: Union[AnyStr, int, enums.MonitoredPhase]
    PTPhase: Union[AnyStr, int, enums.MonitoredPhase]
    VBus: AnyStr
    EventLog: bool
    UserModel: AnyStr
    UserData: AnyStr
    pctMinkvar: float
    Reset: bool
    ControlSignal: Union[AnyStr, LoadShape]
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class CapControlBatch(DSSBatch, CircuitElementBatchMixin):
    _cls_name = 'CapControl'
    _obj_cls = CapControl
    _cls_idx = 24

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)

    def _get_Element_str(self) -> List[str]:
        """
        Full object name of the circuit element, typically a line or transformer, to which the capacitor control's PT and/or CT are connected.There is no default; must be specified.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_batch_str_prop(1)

    def _set_Element_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(1, value, flags)

    Element_str = property(_get_Element_str, _set_Element_str) # type: List[str]

    def _get_Element(self) -> List[DSSObj]:
        """
        Full object name of the circuit element, typically a line or transformer, to which the capacitor control's PT and/or CT are connected.There is no default; must be specified.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_batch_obj_prop(1)

    def _set_Element(self, value: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(1, value, flags)

    Element = property(_get_Element, _set_Element) # type: List[DSSObj]

    def _get_Terminal(self) -> BatchInt32ArrayProxy:
        """
        Number of the terminal of the circuit element to which the CapControl is connected. 1 or 2, typically.  Default is 1.

        DSS property name: `Terminal`, DSS property index: 2.
        """
        return BatchInt32ArrayProxy(self, 2)

    def _set_Terminal(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(2, value, flags)

    Terminal = property(_get_Terminal, _set_Terminal) # type: BatchInt32ArrayProxy

    def _get_Capacitor_str(self) -> List[str]:
        """
        Name of Capacitor element which the CapControl controls. No Default; Must be specified.Do not specify the full object name; "Capacitor" is assumed for the object class.  Example:

        Capacitor=cap1

        DSS property name: `Capacitor`, DSS property index: 3.
        """
        return self._get_batch_str_prop(3)

    def _set_Capacitor_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(3, value, flags)

    Capacitor_str = property(_get_Capacitor_str, _set_Capacitor_str) # type: List[str]

    def _get_Capacitor(self) -> List[CapacitorObj]:
        """
        Name of Capacitor element which the CapControl controls. No Default; Must be specified.Do not specify the full object name; "Capacitor" is assumed for the object class.  Example:

        Capacitor=cap1

        DSS property name: `Capacitor`, DSS property index: 3.
        """
        return self._get_batch_obj_prop(3)

    def _set_Capacitor(self, value: Union[AnyStr, CapacitorObj, List[AnyStr], List[CapacitorObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(3, value, flags)

    Capacitor = property(_get_Capacitor, _set_Capacitor) # type: List[CapacitorObj]

    def _get_Type(self) -> BatchInt32ArrayProxy:
        """
        {Current | Voltage | kvar | PF | Time | Follow} Control type.  Specify the ONsetting and OFFsetting appropriately with the type of control. (See help for ONsetting)

        DSS property name: `Type`, DSS property index: 4.
        """
        return BatchInt32ArrayProxy(self, 4)

    def _set_Type(self, value: Union[AnyStr, int, enums.CapControlType, List[AnyStr], List[int], List[enums.CapControlType], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(4, value, flags)
            return

        self._set_batch_int32_array(4, value, flags)

    Type = property(_get_Type, _set_Type) # type: BatchInt32ArrayProxy

    def _get_Type_str(self) -> List[str]:
        """
        {Current | Voltage | kvar | PF | Time | Follow} Control type.  Specify the ONsetting and OFFsetting appropriately with the type of control. (See help for ONsetting)

        DSS property name: `Type`, DSS property index: 4.
        """
        return self._get_batch_str_prop(4)

    def _set_Type_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Type(value, flags)

    Type_str = property(_get_Type_str, _set_Type_str) # type: List[str]

    def _get_PTRatio(self) -> BatchFloat64ArrayProxy:
        """
        Ratio of the PT that converts the monitored voltage to the control voltage. Default is 60.  If the capacitor is Wye, the 1st phase line-to-neutral voltage is monitored.  Else, the line-to-line voltage (1st - 2nd phase) is monitored.

        DSS property name: `PTRatio`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    def _set_PTRatio(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(5, value, flags)

    PTRatio = property(_get_PTRatio, _set_PTRatio) # type: BatchFloat64ArrayProxy

    def _get_CTRatio(self) -> BatchFloat64ArrayProxy:
        """
        Ratio of the CT from line amps to control ampere setting for current and kvar control types. 

        DSS property name: `CTRatio`, DSS property index: 6.
        """
        return BatchFloat64ArrayProxy(self, 6)

    def _set_CTRatio(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(6, value, flags)

    CTRatio = property(_get_CTRatio, _set_CTRatio) # type: BatchFloat64ArrayProxy

    def _get_OnSetting(self) -> BatchFloat64ArrayProxy:
        """
        Value at which the control arms to switch the capacitor ON (or ratchet up a step).  

        Type of Control:

        Current: Line Amps / CTratio
        Voltage: Line-Neutral (or Line-Line for delta) Volts / PTratio
        kvar:    Total kvar, all phases (3-phase for pos seq model). This is directional. 
        PF:      Power Factor, Total power in monitored terminal. Negative for Leading. 
        Time:    Hrs from Midnight as a floating point number (decimal). 7:30am would be entered as 7.5.
        Follow:  Follows a loadshape (ControlSignal) to determine when to turn ON/OFF the capacitor. If the value is different than 0 the capacitor will connect to the grid, otherwise, it will be disconnected.

        DSS property name: `OnSetting`, DSS property index: 7.
        """
        return BatchFloat64ArrayProxy(self, 7)

    def _set_OnSetting(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(7, value, flags)

    OnSetting = property(_get_OnSetting, _set_OnSetting) # type: BatchFloat64ArrayProxy

    def _get_OffSetting(self) -> BatchFloat64ArrayProxy:
        """
        Value at which the control arms to switch the capacitor OFF. (See help for ONsetting)For Time control, is OK to have Off time the next day ( < On time)

        DSS property name: `OffSetting`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    def _set_OffSetting(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(8, value, flags)

    OffSetting = property(_get_OffSetting, _set_OffSetting) # type: BatchFloat64ArrayProxy

    def _get_Delay(self) -> BatchFloat64ArrayProxy:
        """
        Time delay, in seconds, from when the control is armed before it sends out the switching command to turn ON.  The control may reset before the action actually occurs. This is used to determine which capacity control will act first. Default is 15.  You may specify any floating point number to achieve a model of whatever condition is necessary.

        DSS property name: `Delay`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    def _set_Delay(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(9, value, flags)

    Delay = property(_get_Delay, _set_Delay) # type: BatchFloat64ArrayProxy

    def _get_VoltOverride(self) -> List[bool]:
        """
        {Yes | No}  Default is No.  Switch to indicate whether VOLTAGE OVERRIDE is to be considered. Vmax and Vmin must be set to reasonable values if this property is Yes.

        DSS property name: `VoltOverride`, DSS property index: 10.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(10)
        ]

    def _set_VoltOverride(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(10, value, flags)

    VoltOverride = property(_get_VoltOverride, _set_VoltOverride) # type: List[bool]

    def _get_VMax(self) -> BatchFloat64ArrayProxy:
        """
        Maximum voltage, in volts.  If the voltage across the capacitor divided by the PTRATIO is greater than this voltage, the capacitor will switch OFF regardless of other control settings. Default is 126 (goes with a PT ratio of 60 for 12.47 kV system).

        DSS property name: `VMax`, DSS property index: 11.
        """
        return BatchFloat64ArrayProxy(self, 11)

    def _set_VMax(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(11, value, flags)

    VMax = property(_get_VMax, _set_VMax) # type: BatchFloat64ArrayProxy

    def _get_VMin(self) -> BatchFloat64ArrayProxy:
        """
        Minimum voltage, in volts.  If the voltage across the capacitor divided by the PTRATIO is less than this voltage, the capacitor will switch ON regardless of other control settings. Default is 115 (goes with a PT ratio of 60 for 12.47 kV system).

        DSS property name: `VMin`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    def _set_VMin(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(12, value, flags)

    VMin = property(_get_VMin, _set_VMin) # type: BatchFloat64ArrayProxy

    def _get_DelayOff(self) -> BatchFloat64ArrayProxy:
        """
        Time delay, in seconds, for control to turn OFF when present state is ON. Default is 15.

        DSS property name: `DelayOff`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    def _set_DelayOff(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(13, value, flags)

    DelayOff = property(_get_DelayOff, _set_DelayOff) # type: BatchFloat64ArrayProxy

    def _get_DeadTime(self) -> BatchFloat64ArrayProxy:
        """
        Dead time after capacitor is turned OFF before it can be turned back ON. Default is 300 sec.

        DSS property name: `DeadTime`, DSS property index: 14.
        """
        return BatchFloat64ArrayProxy(self, 14)

    def _set_DeadTime(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(14, value, flags)

    DeadTime = property(_get_DeadTime, _set_DeadTime) # type: BatchFloat64ArrayProxy

    def _get_CTPhase(self) -> BatchInt32ArrayProxy:
        """
        Number of the phase being monitored for CURRENT control or one of {AVG | MAX | MIN} for all phases. Default=1. If delta or L-L connection, enter the first or the two phases being monitored [1-2, 2-3, 3-1]. Must be less than the number of phases. Does not apply to kvar control which uses all phases by default.

        DSS property name: `CTPhase`, DSS property index: 15.
        """
        return BatchInt32ArrayProxy(self, 15)

    def _set_CTPhase(self, value: Union[AnyStr, int, enums.MonitoredPhase, List[AnyStr], List[int], List[enums.MonitoredPhase], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(15, value, flags)
            return

        self._set_batch_int32_array(15, value, flags)

    CTPhase = property(_get_CTPhase, _set_CTPhase) # type: BatchInt32ArrayProxy

    def _get_CTPhase_str(self) -> List[str]:
        """
        Number of the phase being monitored for CURRENT control or one of {AVG | MAX | MIN} for all phases. Default=1. If delta or L-L connection, enter the first or the two phases being monitored [1-2, 2-3, 3-1]. Must be less than the number of phases. Does not apply to kvar control which uses all phases by default.

        DSS property name: `CTPhase`, DSS property index: 15.
        """
        return self._get_batch_str_prop(15)

    def _set_CTPhase_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_CTPhase(value, flags)

    CTPhase_str = property(_get_CTPhase_str, _set_CTPhase_str) # type: List[str]

    def _get_PTPhase(self) -> BatchInt32ArrayProxy:
        """
        Number of the phase being monitored for VOLTAGE control or one of {AVG | MAX | MIN} for all phases. Default=1. If delta or L-L connection, enter the first or the two phases being monitored [1-2, 2-3, 3-1]. Must be less than the number of phases. Does not apply to kvar control which uses all phases by default.

        DSS property name: `PTPhase`, DSS property index: 16.
        """
        return BatchInt32ArrayProxy(self, 16)

    def _set_PTPhase(self, value: Union[AnyStr, int, enums.MonitoredPhase, List[AnyStr], List[int], List[enums.MonitoredPhase], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(16, value, flags)
            return

        self._set_batch_int32_array(16, value, flags)

    PTPhase = property(_get_PTPhase, _set_PTPhase) # type: BatchInt32ArrayProxy

    def _get_PTPhase_str(self) -> List[str]:
        """
        Number of the phase being monitored for VOLTAGE control or one of {AVG | MAX | MIN} for all phases. Default=1. If delta or L-L connection, enter the first or the two phases being monitored [1-2, 2-3, 3-1]. Must be less than the number of phases. Does not apply to kvar control which uses all phases by default.

        DSS property name: `PTPhase`, DSS property index: 16.
        """
        return self._get_batch_str_prop(16)

    def _set_PTPhase_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_PTPhase(value, flags)

    PTPhase_str = property(_get_PTPhase_str, _set_PTPhase_str) # type: List[str]

    def _get_VBus(self) -> List[str]:
        """
        Name of bus to use for voltage override function. Default is bus at monitored terminal. Sometimes it is useful to monitor a bus in another location to emulate various DMS control algorithms.

        DSS property name: `VBus`, DSS property index: 17.
        """
        return self._get_batch_str_prop(17)

    def _set_VBus(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(17, value, flags)

    VBus = property(_get_VBus, _set_VBus) # type: List[str]

    def _get_EventLog(self) -> List[bool]:
        """
        {Yes/True | No/False*} Default is NO for CapControl. Log control actions to Eventlog.

        DSS property name: `EventLog`, DSS property index: 18.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(18)
        ]

    def _set_EventLog(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(18, value, flags)

    EventLog = property(_get_EventLog, _set_EventLog) # type: List[bool]

    def _get_UserModel(self) -> List[str]:
        """
        Name of DLL containing user-written CapControl model, overriding the default model.  Set to "none" to negate previous setting. 

        DSS property name: `UserModel`, DSS property index: 19.
        """
        return self._get_batch_str_prop(19)

    def _set_UserModel(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(19, value, flags)

    UserModel = property(_get_UserModel, _set_UserModel) # type: List[str]

    def _get_UserData(self) -> List[str]:
        """
        String (in quotes or parentheses if necessary) that gets passed to the user-written CapControl model Edit function for defining the data required for that model. 

        DSS property name: `UserData`, DSS property index: 20.
        """
        return self._get_batch_str_prop(20)

    def _set_UserData(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(20, value, flags)

    UserData = property(_get_UserData, _set_UserData) # type: List[str]

    def _get_pctMinkvar(self) -> BatchFloat64ArrayProxy:
        """
        For PF control option, min percent of total bank kvar at which control will close capacitor switch. Default = 50.

        DSS property name: `pctMinkvar`, DSS property index: 21.
        """
        return BatchFloat64ArrayProxy(self, 21)

    def _set_pctMinkvar(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(21, value, flags)

    pctMinkvar = property(_get_pctMinkvar, _set_pctMinkvar) # type: BatchFloat64ArrayProxy

    def Reset(self, value: Union[bool, List[bool]] = True, flags: enums.SetterFlags = 0):
        """
        {Yes | No} If Yes, forces Reset of this CapControl.

        DSS property name: `Reset`, DSS property index: 22.
        """
        self._set_batch_int32_array(22, value, flags)

    def _get_ControlSignal_str(self) -> List[str]:
        """
        Load shape used for controlling the connection/disconnection of the capacitor to the grid, when the load shape is DIFFERENT than ZERO (0) the capacitor will be ON and connected to the grid. Otherwise, if the load shape value is EQUAL to ZERO (0) the capacitor bank will be OFF and disconnected from the grid.

        DSS property name: `ControlSignal`, DSS property index: 23.
        """
        return self._get_batch_str_prop(23)

    def _set_ControlSignal_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(23, value, flags)

    ControlSignal_str = property(_get_ControlSignal_str, _set_ControlSignal_str) # type: List[str]

    def _get_ControlSignal(self) -> List[LoadShape]:
        """
        Load shape used for controlling the connection/disconnection of the capacitor to the grid, when the load shape is DIFFERENT than ZERO (0) the capacitor will be ON and connected to the grid. Otherwise, if the load shape value is EQUAL to ZERO (0) the capacitor bank will be OFF and disconnected from the grid.

        DSS property name: `ControlSignal`, DSS property index: 23.
        """
        return self._get_batch_obj_prop(23)

    def _set_ControlSignal(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(23, value, flags)

    ControlSignal = property(_get_ControlSignal, _set_ControlSignal) # type: List[LoadShape]

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 24.
        """
        return BatchFloat64ArrayProxy(self, 24)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(24, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy

    def _get_Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 25.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(25)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(25, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 26.
        """
        self._set_batch_string(26, value, flags)

class CapControlBatchProperties(TypedDict):
    Element: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]]
    Terminal: Union[int, Int32Array]
    Capacitor: Union[AnyStr, CapacitorObj, List[AnyStr], List[CapacitorObj]]
    Type: Union[AnyStr, int, enums.CapControlType, List[AnyStr], List[int], List[enums.CapControlType], Int32Array]
    PTRatio: Union[float, Float64Array]
    CTRatio: Union[float, Float64Array]
    OnSetting: Union[float, Float64Array]
    OffSetting: Union[float, Float64Array]
    Delay: Union[float, Float64Array]
    VoltOverride: bool
    VMax: Union[float, Float64Array]
    VMin: Union[float, Float64Array]
    DelayOff: Union[float, Float64Array]
    DeadTime: Union[float, Float64Array]
    CTPhase: Union[AnyStr, int, enums.MonitoredPhase, List[AnyStr], List[int], List[enums.MonitoredPhase], Int32Array]
    PTPhase: Union[AnyStr, int, enums.MonitoredPhase, List[AnyStr], List[int], List[enums.MonitoredPhase], Int32Array]
    VBus: Union[AnyStr, List[AnyStr]]
    EventLog: bool
    UserModel: Union[AnyStr, List[AnyStr]]
    UserData: Union[AnyStr, List[AnyStr]]
    pctMinkvar: Union[float, Float64Array]
    Reset: bool
    ControlSignal: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class ICapControl(IDSSObj, CapControlBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, CapControl, CapControlBatch)
        CapControlBatch.__init__(self, self._api_util, sync_cls_idx=CapControl._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> CapControl:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[CapControlProperties]) -> CapControl:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[CapControlBatchProperties]) -> CapControlBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
