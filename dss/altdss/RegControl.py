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
from .AutoTrans import AutoTrans
from .Transformer import Transformer as TransformerObj

class RegControl(DSSObj, CircuitElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots
    _cls_name = 'RegControl'
    _cls_idx = 21
    _cls_prop_idx = {
        'transformer': 1,
        'winding': 2,
        'vreg': 3,
        'band': 4,
        'ptratio': 5,
        'ctprim': 6,
        'r': 7,
        'x': 8,
        'bus': 9,
        'delay': 10,
        'reversible': 11,
        'revvreg': 12,
        'revband': 13,
        'revr': 14,
        'revx': 15,
        'tapdelay': 16,
        'debugtrace': 17,
        'maxtapchange': 18,
        'inversetime': 19,
        'tapwinding': 20,
        'vlimit': 21,
        'ptphase': 22,
        'revthreshold': 23,
        'revdelay': 24,
        'revneutral': 25,
        'eventlog': 26,
        'remoteptratio': 27,
        'tapnum': 28,
        'reset': 29,
        'ldc_z': 30,
        'rev_z': 31,
        'cogen': 32,
        'basefreq': 33,
        'enabled': 34,
        'like': 35,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)

    def _get_Transformer_str(self) -> str:
        """
        Name of Transformer or AutoTrans element to which the RegControl is connected. Do not specify the full object name; "Transformer" or "AutoTrans" is assumed for the object class.  Example:

        Transformer=Xfmr1

        DSS property name: `Transformer`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    def _set_Transformer_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(1, value, flags)

    Transformer_str = property(_get_Transformer_str, _set_Transformer_str) # type: str

    def _get_Transformer(self) -> Union[TransformerObj, AutoTrans]:
        """
        Name of Transformer or AutoTrans element to which the RegControl is connected. Do not specify the full object name; "Transformer" or "AutoTrans" is assumed for the object class.  Example:

        Transformer=Xfmr1

        DSS property name: `Transformer`, DSS property index: 1.
        """
        return self._get_obj(1, None)

    def _set_Transformer(self, value: Union[AnyStr, TransformerObj, AutoTrans], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(1, value, flags)
            return

        self._set_string_o(1, value, flags)

    Transformer = property(_get_Transformer, _set_Transformer) # type: TransformerObj, AutoTrans

    def _get_Winding(self) -> int:
        """
        Number of the winding of the transformer element that the RegControl is monitoring. 1 or 2, typically.  Side Effect: Sets TAPWINDING property to the same winding.

        DSS property name: `Winding`, DSS property index: 2.
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    def _set_Winding(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 2, value, flags)

    Winding = property(_get_Winding, _set_Winding) # type: int

    def _get_VReg(self) -> float:
        """
        Voltage regulator setting, in VOLTS, for the winding being controlled.  Multiplying this value times the ptratio should yield the voltage across the WINDING of the controlled transformer. Default is 120.0

        DSS property name: `VReg`, DSS property index: 3.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    def _set_VReg(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 3, value, flags)

    VReg = property(_get_VReg, _set_VReg) # type: float

    def _get_Band(self) -> float:
        """
        Bandwidth in VOLTS for the controlled bus (see help for ptratio property).  Default is 3.0

        DSS property name: `Band`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    def _set_Band(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 4, value, flags)

    Band = property(_get_Band, _set_Band) # type: float

    def _get_PTRatio(self) -> float:
        """
        Ratio of the PT that converts the controlled winding voltage to the regulator control voltage. Default is 60.  If the winding is Wye, the line-to-neutral voltage is used.  Else, the line-to-line voltage is used. SIDE EFFECT: Also sets RemotePTRatio property.

        DSS property name: `PTRatio`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    def _set_PTRatio(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 5, value, flags)

    PTRatio = property(_get_PTRatio, _set_PTRatio) # type: float

    def _get_CTPrim(self) -> float:
        """
        Rating, in Amperes, of the primary CT rating for which the line amps convert to control rated amps.The typical default secondary ampere rating is 0.2 Amps (check with manufacturer specs). Current at which the LDC voltages match the R and X settings.

        DSS property name: `CTPrim`, DSS property index: 6.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    def _set_CTPrim(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 6, value, flags)

    CTPrim = property(_get_CTPrim, _set_CTPrim) # type: float

    def _get_R(self) -> float:
        """
        R setting on the line drop compensator in the regulator, expressed in VOLTS.

        DSS property name: `R`, DSS property index: 7.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    def _set_R(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 7, value, flags)

    R = property(_get_R, _set_R) # type: float

    def _get_X(self) -> float:
        """
        X setting on the line drop compensator in the regulator, expressed in VOLTS.

        DSS property name: `X`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    def _set_X(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 8, value, flags)

    X = property(_get_X, _set_X) # type: float

    def _get_Bus(self) -> str:
        """
        Name of a bus (busname.nodename) in the system to use as the controlled bus instead of the bus to which the transformer winding is connected or the R and X line drop compensator settings.  Do not specify this value if you wish to use the line drop compensator settings.  Default is null string. Assumes the base voltage for this bus is the same as the transformer winding base specified above. Note: This bus (1-phase) WILL BE CREATED by the regulator control upon SOLVE if not defined by some other device. You can specify the node of the bus you wish to sample (defaults to 1). If specified, the RegControl is redefined as a 1-phase device since only one voltage is used.

        DSS property name: `Bus`, DSS property index: 9.
        """
        return self._get_prop_string(9)

    def _set_Bus(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(9, value, flags)

    Bus = property(_get_Bus, _set_Bus) # type: str

    def _get_Delay(self) -> float:
        """
        Time delay, in seconds, from when the voltage goes out of band to when the tap changing begins. This is used to determine which regulator control will act first. Default is 15.  You may specify any floating point number to achieve a model of whatever condition is necessary.

        DSS property name: `Delay`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    def _set_Delay(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 10, value, flags)

    Delay = property(_get_Delay, _set_Delay) # type: float

    def _get_Reversible(self) -> bool:
        """
        {Yes |No*} Indicates whether or not the regulator can be switched to regulate in the reverse direction. Default is No.Typically applies only to line regulators and not to LTC on a substation transformer.

        DSS property name: `Reversible`, DSS property index: 11.
        """
        return self._lib.Obj_GetInt32(self._ptr, 11) != 0

    def _set_Reversible(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 11, value, flags)

    Reversible = property(_get_Reversible, _set_Reversible) # type: bool

    def _get_RevVReg(self) -> float:
        """
        Voltage setting in volts for operation in the reverse direction.

        DSS property name: `RevVReg`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    def _set_RevVReg(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 12, value, flags)

    RevVReg = property(_get_RevVReg, _set_RevVReg) # type: float

    def _get_RevBand(self) -> float:
        """
        Bandwidth for operating in the reverse direction.

        DSS property name: `RevBand`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    def _set_RevBand(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 13, value, flags)

    RevBand = property(_get_RevBand, _set_RevBand) # type: float

    def _get_RevR(self) -> float:
        """
        R line drop compensator setting for reverse direction.

        DSS property name: `RevR`, DSS property index: 14.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    def _set_RevR(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 14, value, flags)

    RevR = property(_get_RevR, _set_RevR) # type: float

    def _get_RevX(self) -> float:
        """
        X line drop compensator setting for reverse direction.

        DSS property name: `RevX`, DSS property index: 15.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    def _set_RevX(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 15, value, flags)

    RevX = property(_get_RevX, _set_RevX) # type: float

    def _get_TapDelay(self) -> float:
        """
        Delay in sec between tap changes. Default is 2. This is how long it takes between changes after the first change.

        DSS property name: `TapDelay`, DSS property index: 16.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    def _set_TapDelay(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 16, value, flags)

    TapDelay = property(_get_TapDelay, _set_TapDelay) # type: float

    def _get_DebugTrace(self) -> bool:
        """
        {Yes | No* }  Default is no.  Turn this on to capture the progress of the regulator model for each control iteration.  Creates a separate file for each RegControl named "REG_name.csv".

        DSS property name: `DebugTrace`, DSS property index: 17.
        """
        return self._lib.Obj_GetInt32(self._ptr, 17) != 0

    def _set_DebugTrace(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 17, value, flags)

    DebugTrace = property(_get_DebugTrace, _set_DebugTrace) # type: bool

    def _get_MaxTapChange(self) -> int:
        """
        Maximum allowable tap change per control iteration in STATIC control mode.  Default is 16. 

        Set this to 1 to better approximate actual control action. 

        Set this to 0 to fix the tap in the current position.

        DSS property name: `MaxTapChange`, DSS property index: 18.
        """
        return self._lib.Obj_GetInt32(self._ptr, 18)

    def _set_MaxTapChange(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 18, value, flags)

    MaxTapChange = property(_get_MaxTapChange, _set_MaxTapChange) # type: int

    def _get_InverseTime(self) -> bool:
        """
        {Yes | No* } Default is no.  The time delay is adjusted inversely proportional to the amount the voltage is outside the band down to 10%.

        DSS property name: `InverseTime`, DSS property index: 19.
        """
        return self._lib.Obj_GetInt32(self._ptr, 19) != 0

    def _set_InverseTime(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 19, value, flags)

    InverseTime = property(_get_InverseTime, _set_InverseTime) # type: bool

    def _get_TapWinding(self) -> int:
        """
        Winding containing the actual taps, if different than the WINDING property. Defaults to the same winding as specified by the WINDING property.

        DSS property name: `TapWinding`, DSS property index: 20.
        """
        return self._lib.Obj_GetInt32(self._ptr, 20)

    def _set_TapWinding(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 20, value, flags)

    TapWinding = property(_get_TapWinding, _set_TapWinding) # type: int

    def _get_VLimit(self) -> float:
        """
        Voltage Limit for bus to which regulated winding is connected (e.g. first customer). Default is 0.0. Set to a value greater then zero to activate this function.

        DSS property name: `VLimit`, DSS property index: 21.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    def _set_VLimit(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 21, value, flags)

    VLimit = property(_get_VLimit, _set_VLimit) # type: float

    def _get_PTPhase(self) -> Union[enums.RegControlPhaseSelection, int]:
        """
        For multi-phase transformers, the number of the phase being monitored or one of { MAX | MIN} for all phases. Default=1. Must be less than or equal to the number of phases. Ignored for regulated bus.

        DSS property name: `PTPhase`, DSS property index: 22.
        """
        value = self._lib.Obj_GetInt32(self._ptr, 22)
        if value > 0:
            return value

        return enums.RegControlPhaseSelection(value)

    def _set_PTPhase(self, value: Union[AnyStr, int, enums.RegControlPhaseSelection], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(22, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 22, value, flags)

    PTPhase = property(_get_PTPhase, _set_PTPhase) # type: enums.RegControlPhaseSelection

    def _get_PTPhase_str(self) -> str:
        """
        For multi-phase transformers, the number of the phase being monitored or one of { MAX | MIN} for all phases. Default=1. Must be less than or equal to the number of phases. Ignored for regulated bus.

        DSS property name: `PTPhase`, DSS property index: 22.
        """
        return self._get_prop_string(22)

    def _set_PTPhase_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_PTPhase(value, flags)

    PTPhase_str = property(_get_PTPhase_str, _set_PTPhase_str) # type: str

    def _get_RevThreshold(self) -> float:
        """
        kW reverse power threshold for reversing the direction of the regulator. Default is 100.0 kw.

        DSS property name: `RevThreshold`, DSS property index: 23.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    def _set_RevThreshold(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 23, value, flags)

    RevThreshold = property(_get_RevThreshold, _set_RevThreshold) # type: float

    def _get_RevDelay(self) -> float:
        """
        Time Delay in seconds (s) for executing the reversing action once the threshold for reversing has been exceeded. Default is 60 s.

        DSS property name: `RevDelay`, DSS property index: 24.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    def _set_RevDelay(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 24, value, flags)

    RevDelay = property(_get_RevDelay, _set_RevDelay) # type: float

    def _get_RevNeutral(self) -> bool:
        """
        {Yes | No*} Default is no. Set this to Yes if you want the regulator to go to neutral in the reverse direction or in cogen operation.

        DSS property name: `RevNeutral`, DSS property index: 25.
        """
        return self._lib.Obj_GetInt32(self._ptr, 25) != 0

    def _set_RevNeutral(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 25, value, flags)

    RevNeutral = property(_get_RevNeutral, _set_RevNeutral) # type: bool

    def _get_EventLog(self) -> bool:
        """
        {Yes/True | No/False*} Default is NO for regulator control. Log control actions to Eventlog.

        DSS property name: `EventLog`, DSS property index: 26.
        """
        return self._lib.Obj_GetInt32(self._ptr, 26) != 0

    def _set_EventLog(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 26, value, flags)

    EventLog = property(_get_EventLog, _set_EventLog) # type: bool

    def _get_RemotePTRatio(self) -> float:
        """
        When regulating a bus (the Bus= property is set), the PT ratio required to convert actual voltage at the remote bus to control voltage. Is initialized to PTratio property. Set this property after setting PTratio.

        DSS property name: `RemotePTRatio`, DSS property index: 27.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 27)

    def _set_RemotePTRatio(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 27, value, flags)

    RemotePTRatio = property(_get_RemotePTRatio, _set_RemotePTRatio) # type: float

    def _get_TapNum(self) -> int:
        """
        An integer number indicating the tap position that the controlled transformer winding tap position is currently at, or is being set to.  If being set, and the value is outside the range of the transformer min or max tap, then set to the min or max tap position as appropriate. Default is 0

        DSS property name: `TapNum`, DSS property index: 28.
        """
        return self._lib.Obj_GetInt32(self._ptr, 28)

    def _set_TapNum(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 28, value, flags)

    TapNum = property(_get_TapNum, _set_TapNum) # type: int

    def Reset(self, value: bool = True, flags: enums.SetterFlags = 0):
        """
        {Yes | No} If Yes, forces Reset of this RegControl.

        DSS property name: `Reset`, DSS property index: 29.
        """
        self._lib.Obj_SetInt32(self._ptr, 29, value, flags)

    def _get_LDC_Z(self) -> float:
        """
        Z value for Beckwith LDC_Z control option. Volts adjustment at rated control current.

        DSS property name: `LDC_Z`, DSS property index: 30.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 30)

    def _set_LDC_Z(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 30, value, flags)

    LDC_Z = property(_get_LDC_Z, _set_LDC_Z) # type: float

    def _get_Rev_Z(self) -> float:
        """
        Reverse Z value for Beckwith LDC_Z control option.

        DSS property name: `Rev_Z`, DSS property index: 31.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 31)

    def _set_Rev_Z(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 31, value, flags)

    Rev_Z = property(_get_Rev_Z, _set_Rev_Z) # type: float

    def _get_Cogen(self) -> bool:
        """
        {Yes|No*} Default is No. The Cogen feature is activated. Continues looking forward if power reverses, but switches to reverse-mode LDC, vreg and band values.

        DSS property name: `Cogen`, DSS property index: 32.
        """
        return self._lib.Obj_GetInt32(self._ptr, 32) != 0

    def _set_Cogen(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 32, value, flags)

    Cogen = property(_get_Cogen, _set_Cogen) # type: bool

    def _get_BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 33.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 33)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 33, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float

    def _get_Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 34.
        """
        return self._lib.Obj_GetInt32(self._ptr, 34) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 34, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 35.
        """
        self._set_string_o(35, value)


class RegControlProperties(TypedDict):
    Transformer: Union[AnyStr, TransformerObj, AutoTrans]
    Winding: int
    VReg: float
    Band: float
    PTRatio: float
    CTPrim: float
    R: float
    X: float
    Bus: AnyStr
    Delay: float
    Reversible: bool
    RevVReg: float
    RevBand: float
    RevR: float
    RevX: float
    TapDelay: float
    DebugTrace: bool
    MaxTapChange: int
    InverseTime: bool
    TapWinding: int
    VLimit: float
    PTPhase: Union[AnyStr, int, enums.RegControlPhaseSelection]
    RevThreshold: float
    RevDelay: float
    RevNeutral: bool
    EventLog: bool
    RemotePTRatio: float
    TapNum: int
    Reset: bool
    LDC_Z: float
    Rev_Z: float
    Cogen: bool
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class RegControlBatch(DSSBatch, CircuitElementBatchMixin):
    _cls_name = 'RegControl'
    _obj_cls = RegControl
    _cls_idx = 21

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)

    def _get_Transformer_str(self) -> List[str]:
        """
        Name of Transformer or AutoTrans element to which the RegControl is connected. Do not specify the full object name; "Transformer" or "AutoTrans" is assumed for the object class.  Example:

        Transformer=Xfmr1

        DSS property name: `Transformer`, DSS property index: 1.
        """
        return self._get_batch_str_prop(1)

    def _set_Transformer_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(1, value, flags)

    Transformer_str = property(_get_Transformer_str, _set_Transformer_str) # type: List[str]

    def _get_Transformer(self) -> List[Union[TransformerObj, AutoTrans]]:
        """
        Name of Transformer or AutoTrans element to which the RegControl is connected. Do not specify the full object name; "Transformer" or "AutoTrans" is assumed for the object class.  Example:

        Transformer=Xfmr1

        DSS property name: `Transformer`, DSS property index: 1.
        """
        return self._get_batch_obj_prop(1)

    def _set_Transformer(self, value: Union[AnyStr, TransformerObj, AutoTrans, List[AnyStr], List[Union[TransformerObj, AutoTrans]]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(1, value, flags)

    Transformer = property(_get_Transformer, _set_Transformer) # type: List[Union[TransformerObj, AutoTrans]]

    def _get_Winding(self) -> BatchInt32ArrayProxy:
        """
        Number of the winding of the transformer element that the RegControl is monitoring. 1 or 2, typically.  Side Effect: Sets TAPWINDING property to the same winding.

        DSS property name: `Winding`, DSS property index: 2.
        """
        return BatchInt32ArrayProxy(self, 2)

    def _set_Winding(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(2, value, flags)

    Winding = property(_get_Winding, _set_Winding) # type: BatchInt32ArrayProxy

    def _get_VReg(self) -> BatchFloat64ArrayProxy:
        """
        Voltage regulator setting, in VOLTS, for the winding being controlled.  Multiplying this value times the ptratio should yield the voltage across the WINDING of the controlled transformer. Default is 120.0

        DSS property name: `VReg`, DSS property index: 3.
        """
        return BatchFloat64ArrayProxy(self, 3)

    def _set_VReg(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(3, value, flags)

    VReg = property(_get_VReg, _set_VReg) # type: BatchFloat64ArrayProxy

    def _get_Band(self) -> BatchFloat64ArrayProxy:
        """
        Bandwidth in VOLTS for the controlled bus (see help for ptratio property).  Default is 3.0

        DSS property name: `Band`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    def _set_Band(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(4, value, flags)

    Band = property(_get_Band, _set_Band) # type: BatchFloat64ArrayProxy

    def _get_PTRatio(self) -> BatchFloat64ArrayProxy:
        """
        Ratio of the PT that converts the controlled winding voltage to the regulator control voltage. Default is 60.  If the winding is Wye, the line-to-neutral voltage is used.  Else, the line-to-line voltage is used. SIDE EFFECT: Also sets RemotePTRatio property.

        DSS property name: `PTRatio`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    def _set_PTRatio(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(5, value, flags)

    PTRatio = property(_get_PTRatio, _set_PTRatio) # type: BatchFloat64ArrayProxy

    def _get_CTPrim(self) -> BatchFloat64ArrayProxy:
        """
        Rating, in Amperes, of the primary CT rating for which the line amps convert to control rated amps.The typical default secondary ampere rating is 0.2 Amps (check with manufacturer specs). Current at which the LDC voltages match the R and X settings.

        DSS property name: `CTPrim`, DSS property index: 6.
        """
        return BatchFloat64ArrayProxy(self, 6)

    def _set_CTPrim(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(6, value, flags)

    CTPrim = property(_get_CTPrim, _set_CTPrim) # type: BatchFloat64ArrayProxy

    def _get_R(self) -> BatchFloat64ArrayProxy:
        """
        R setting on the line drop compensator in the regulator, expressed in VOLTS.

        DSS property name: `R`, DSS property index: 7.
        """
        return BatchFloat64ArrayProxy(self, 7)

    def _set_R(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(7, value, flags)

    R = property(_get_R, _set_R) # type: BatchFloat64ArrayProxy

    def _get_X(self) -> BatchFloat64ArrayProxy:
        """
        X setting on the line drop compensator in the regulator, expressed in VOLTS.

        DSS property name: `X`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    def _set_X(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(8, value, flags)

    X = property(_get_X, _set_X) # type: BatchFloat64ArrayProxy

    def _get_Bus(self) -> List[str]:
        """
        Name of a bus (busname.nodename) in the system to use as the controlled bus instead of the bus to which the transformer winding is connected or the R and X line drop compensator settings.  Do not specify this value if you wish to use the line drop compensator settings.  Default is null string. Assumes the base voltage for this bus is the same as the transformer winding base specified above. Note: This bus (1-phase) WILL BE CREATED by the regulator control upon SOLVE if not defined by some other device. You can specify the node of the bus you wish to sample (defaults to 1). If specified, the RegControl is redefined as a 1-phase device since only one voltage is used.

        DSS property name: `Bus`, DSS property index: 9.
        """
        return self._get_batch_str_prop(9)

    def _set_Bus(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(9, value, flags)

    Bus = property(_get_Bus, _set_Bus) # type: List[str]

    def _get_Delay(self) -> BatchFloat64ArrayProxy:
        """
        Time delay, in seconds, from when the voltage goes out of band to when the tap changing begins. This is used to determine which regulator control will act first. Default is 15.  You may specify any floating point number to achieve a model of whatever condition is necessary.

        DSS property name: `Delay`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    def _set_Delay(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(10, value, flags)

    Delay = property(_get_Delay, _set_Delay) # type: BatchFloat64ArrayProxy

    def _get_Reversible(self) -> List[bool]:
        """
        {Yes |No*} Indicates whether or not the regulator can be switched to regulate in the reverse direction. Default is No.Typically applies only to line regulators and not to LTC on a substation transformer.

        DSS property name: `Reversible`, DSS property index: 11.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(11)
        ]

    def _set_Reversible(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(11, value, flags)

    Reversible = property(_get_Reversible, _set_Reversible) # type: List[bool]

    def _get_RevVReg(self) -> BatchFloat64ArrayProxy:
        """
        Voltage setting in volts for operation in the reverse direction.

        DSS property name: `RevVReg`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    def _set_RevVReg(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(12, value, flags)

    RevVReg = property(_get_RevVReg, _set_RevVReg) # type: BatchFloat64ArrayProxy

    def _get_RevBand(self) -> BatchFloat64ArrayProxy:
        """
        Bandwidth for operating in the reverse direction.

        DSS property name: `RevBand`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    def _set_RevBand(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(13, value, flags)

    RevBand = property(_get_RevBand, _set_RevBand) # type: BatchFloat64ArrayProxy

    def _get_RevR(self) -> BatchFloat64ArrayProxy:
        """
        R line drop compensator setting for reverse direction.

        DSS property name: `RevR`, DSS property index: 14.
        """
        return BatchFloat64ArrayProxy(self, 14)

    def _set_RevR(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(14, value, flags)

    RevR = property(_get_RevR, _set_RevR) # type: BatchFloat64ArrayProxy

    def _get_RevX(self) -> BatchFloat64ArrayProxy:
        """
        X line drop compensator setting for reverse direction.

        DSS property name: `RevX`, DSS property index: 15.
        """
        return BatchFloat64ArrayProxy(self, 15)

    def _set_RevX(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(15, value, flags)

    RevX = property(_get_RevX, _set_RevX) # type: BatchFloat64ArrayProxy

    def _get_TapDelay(self) -> BatchFloat64ArrayProxy:
        """
        Delay in sec between tap changes. Default is 2. This is how long it takes between changes after the first change.

        DSS property name: `TapDelay`, DSS property index: 16.
        """
        return BatchFloat64ArrayProxy(self, 16)

    def _set_TapDelay(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(16, value, flags)

    TapDelay = property(_get_TapDelay, _set_TapDelay) # type: BatchFloat64ArrayProxy

    def _get_DebugTrace(self) -> List[bool]:
        """
        {Yes | No* }  Default is no.  Turn this on to capture the progress of the regulator model for each control iteration.  Creates a separate file for each RegControl named "REG_name.csv".

        DSS property name: `DebugTrace`, DSS property index: 17.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(17)
        ]

    def _set_DebugTrace(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(17, value, flags)

    DebugTrace = property(_get_DebugTrace, _set_DebugTrace) # type: List[bool]

    def _get_MaxTapChange(self) -> BatchInt32ArrayProxy:
        """
        Maximum allowable tap change per control iteration in STATIC control mode.  Default is 16. 

        Set this to 1 to better approximate actual control action. 

        Set this to 0 to fix the tap in the current position.

        DSS property name: `MaxTapChange`, DSS property index: 18.
        """
        return BatchInt32ArrayProxy(self, 18)

    def _set_MaxTapChange(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(18, value, flags)

    MaxTapChange = property(_get_MaxTapChange, _set_MaxTapChange) # type: BatchInt32ArrayProxy

    def _get_InverseTime(self) -> List[bool]:
        """
        {Yes | No* } Default is no.  The time delay is adjusted inversely proportional to the amount the voltage is outside the band down to 10%.

        DSS property name: `InverseTime`, DSS property index: 19.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(19)
        ]

    def _set_InverseTime(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(19, value, flags)

    InverseTime = property(_get_InverseTime, _set_InverseTime) # type: List[bool]

    def _get_TapWinding(self) -> BatchInt32ArrayProxy:
        """
        Winding containing the actual taps, if different than the WINDING property. Defaults to the same winding as specified by the WINDING property.

        DSS property name: `TapWinding`, DSS property index: 20.
        """
        return BatchInt32ArrayProxy(self, 20)

    def _set_TapWinding(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(20, value, flags)

    TapWinding = property(_get_TapWinding, _set_TapWinding) # type: BatchInt32ArrayProxy

    def _get_VLimit(self) -> BatchFloat64ArrayProxy:
        """
        Voltage Limit for bus to which regulated winding is connected (e.g. first customer). Default is 0.0. Set to a value greater then zero to activate this function.

        DSS property name: `VLimit`, DSS property index: 21.
        """
        return BatchFloat64ArrayProxy(self, 21)

    def _set_VLimit(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(21, value, flags)

    VLimit = property(_get_VLimit, _set_VLimit) # type: BatchFloat64ArrayProxy

    def _get_PTPhase(self) -> BatchInt32ArrayProxy:
        """
        For multi-phase transformers, the number of the phase being monitored or one of { MAX | MIN} for all phases. Default=1. Must be less than or equal to the number of phases. Ignored for regulated bus.

        DSS property name: `PTPhase`, DSS property index: 22.
        """
        return BatchInt32ArrayProxy(self, 22)

    def _set_PTPhase(self, value: Union[AnyStr, int, enums.RegControlPhaseSelection, List[AnyStr], List[int], List[enums.RegControlPhaseSelection], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(22, value, flags)
            return

        self._set_batch_int32_array(22, value, flags)

    PTPhase = property(_get_PTPhase, _set_PTPhase) # type: BatchInt32ArrayProxy

    def _get_PTPhase_str(self) -> List[str]:
        """
        For multi-phase transformers, the number of the phase being monitored or one of { MAX | MIN} for all phases. Default=1. Must be less than or equal to the number of phases. Ignored for regulated bus.

        DSS property name: `PTPhase`, DSS property index: 22.
        """
        return self._get_batch_str_prop(22)

    def _set_PTPhase_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_PTPhase(value, flags)

    PTPhase_str = property(_get_PTPhase_str, _set_PTPhase_str) # type: List[str]

    def _get_RevThreshold(self) -> BatchFloat64ArrayProxy:
        """
        kW reverse power threshold for reversing the direction of the regulator. Default is 100.0 kw.

        DSS property name: `RevThreshold`, DSS property index: 23.
        """
        return BatchFloat64ArrayProxy(self, 23)

    def _set_RevThreshold(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(23, value, flags)

    RevThreshold = property(_get_RevThreshold, _set_RevThreshold) # type: BatchFloat64ArrayProxy

    def _get_RevDelay(self) -> BatchFloat64ArrayProxy:
        """
        Time Delay in seconds (s) for executing the reversing action once the threshold for reversing has been exceeded. Default is 60 s.

        DSS property name: `RevDelay`, DSS property index: 24.
        """
        return BatchFloat64ArrayProxy(self, 24)

    def _set_RevDelay(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(24, value, flags)

    RevDelay = property(_get_RevDelay, _set_RevDelay) # type: BatchFloat64ArrayProxy

    def _get_RevNeutral(self) -> List[bool]:
        """
        {Yes | No*} Default is no. Set this to Yes if you want the regulator to go to neutral in the reverse direction or in cogen operation.

        DSS property name: `RevNeutral`, DSS property index: 25.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(25)
        ]

    def _set_RevNeutral(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(25, value, flags)

    RevNeutral = property(_get_RevNeutral, _set_RevNeutral) # type: List[bool]

    def _get_EventLog(self) -> List[bool]:
        """
        {Yes/True | No/False*} Default is NO for regulator control. Log control actions to Eventlog.

        DSS property name: `EventLog`, DSS property index: 26.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(26)
        ]

    def _set_EventLog(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(26, value, flags)

    EventLog = property(_get_EventLog, _set_EventLog) # type: List[bool]

    def _get_RemotePTRatio(self) -> BatchFloat64ArrayProxy:
        """
        When regulating a bus (the Bus= property is set), the PT ratio required to convert actual voltage at the remote bus to control voltage. Is initialized to PTratio property. Set this property after setting PTratio.

        DSS property name: `RemotePTRatio`, DSS property index: 27.
        """
        return BatchFloat64ArrayProxy(self, 27)

    def _set_RemotePTRatio(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(27, value, flags)

    RemotePTRatio = property(_get_RemotePTRatio, _set_RemotePTRatio) # type: BatchFloat64ArrayProxy

    def _get_TapNum(self) -> BatchInt32ArrayProxy:
        """
        An integer number indicating the tap position that the controlled transformer winding tap position is currently at, or is being set to.  If being set, and the value is outside the range of the transformer min or max tap, then set to the min or max tap position as appropriate. Default is 0

        DSS property name: `TapNum`, DSS property index: 28.
        """
        return BatchInt32ArrayProxy(self, 28)

    def _set_TapNum(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(28, value, flags)

    TapNum = property(_get_TapNum, _set_TapNum) # type: BatchInt32ArrayProxy

    def Reset(self, value: Union[bool, List[bool]] = True, flags: enums.SetterFlags = 0):
        """
        {Yes | No} If Yes, forces Reset of this RegControl.

        DSS property name: `Reset`, DSS property index: 29.
        """
        self._set_batch_int32_array(29, value, flags)

    def _get_LDC_Z(self) -> BatchFloat64ArrayProxy:
        """
        Z value for Beckwith LDC_Z control option. Volts adjustment at rated control current.

        DSS property name: `LDC_Z`, DSS property index: 30.
        """
        return BatchFloat64ArrayProxy(self, 30)

    def _set_LDC_Z(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(30, value, flags)

    LDC_Z = property(_get_LDC_Z, _set_LDC_Z) # type: BatchFloat64ArrayProxy

    def _get_Rev_Z(self) -> BatchFloat64ArrayProxy:
        """
        Reverse Z value for Beckwith LDC_Z control option.

        DSS property name: `Rev_Z`, DSS property index: 31.
        """
        return BatchFloat64ArrayProxy(self, 31)

    def _set_Rev_Z(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(31, value, flags)

    Rev_Z = property(_get_Rev_Z, _set_Rev_Z) # type: BatchFloat64ArrayProxy

    def _get_Cogen(self) -> List[bool]:
        """
        {Yes|No*} Default is No. The Cogen feature is activated. Continues looking forward if power reverses, but switches to reverse-mode LDC, vreg and band values.

        DSS property name: `Cogen`, DSS property index: 32.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(32)
        ]

    def _set_Cogen(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(32, value, flags)

    Cogen = property(_get_Cogen, _set_Cogen) # type: List[bool]

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 33.
        """
        return BatchFloat64ArrayProxy(self, 33)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(33, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy

    def _get_Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 34.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(34)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(34, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 35.
        """
        self._set_batch_string(35, value, flags)

class RegControlBatchProperties(TypedDict):
    Transformer: Union[AnyStr, TransformerObj, AutoTrans, List[AnyStr], List[Union[TransformerObj, AutoTrans]]]
    Winding: Union[int, Int32Array]
    VReg: Union[float, Float64Array]
    Band: Union[float, Float64Array]
    PTRatio: Union[float, Float64Array]
    CTPrim: Union[float, Float64Array]
    R: Union[float, Float64Array]
    X: Union[float, Float64Array]
    Bus: Union[AnyStr, List[AnyStr]]
    Delay: Union[float, Float64Array]
    Reversible: bool
    RevVReg: Union[float, Float64Array]
    RevBand: Union[float, Float64Array]
    RevR: Union[float, Float64Array]
    RevX: Union[float, Float64Array]
    TapDelay: Union[float, Float64Array]
    DebugTrace: bool
    MaxTapChange: Union[int, Int32Array]
    InverseTime: bool
    TapWinding: Union[int, Int32Array]
    VLimit: Union[float, Float64Array]
    PTPhase: Union[AnyStr, int, enums.RegControlPhaseSelection, List[AnyStr], List[int], List[enums.RegControlPhaseSelection], Int32Array]
    RevThreshold: Union[float, Float64Array]
    RevDelay: Union[float, Float64Array]
    RevNeutral: bool
    EventLog: bool
    RemotePTRatio: Union[float, Float64Array]
    TapNum: Union[int, Int32Array]
    Reset: bool
    LDC_Z: Union[float, Float64Array]
    Rev_Z: Union[float, Float64Array]
    Cogen: bool
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IRegControl(IDSSObj, RegControlBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, RegControl, RegControlBatch)
        RegControlBatch.__init__(self, self._api_util, sync_cls_idx=RegControl._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> RegControl:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[RegControlProperties]) -> RegControl:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[RegControlBatchProperties]) -> RegControlBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
