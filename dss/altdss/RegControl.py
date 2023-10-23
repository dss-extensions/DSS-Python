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
from .AutoTrans import AutoTrans
from .Transformer import Transformer as TransformerObj

class RegControl(DSSObj, CktElementMixin):
    __slots__ = CktElementMixin._extra_slots
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

    @property
    def Transformer(self) -> str:
        """
        Name of Transformer or AutoTrans element to which the RegControl is connected. Do not specify the full object name; "Transformer" or "AutoTrans" is assumed for the object class.  Example:

        Transformer=Xfmr1

        DSS property name: `Transformer`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    @Transformer.setter
    def Transformer(self, value: Union[AnyStr, TransformerObj, AutoTrans]):
        if isinstance(value, DSSObj):
            self._set_obj(1, value)
            return

        self._set_string_o(1, value)

    @property
    def Transformer_obj(self) -> Union[TransformerObj, AutoTrans]:
        """
        Name of Transformer or AutoTrans element to which the RegControl is connected. Do not specify the full object name; "Transformer" or "AutoTrans" is assumed for the object class.  Example:

        Transformer=Xfmr1

        DSS property name: `Transformer`, DSS property index: 1.
        """
        return self._get_obj(1, None)

    @Transformer_obj.setter
    def Transformer_obj(self, value: Union[TransformerObj, AutoTrans]):
        self._set_obj(1, value)

    @property
    def Winding(self) -> int:
        """
        Number of the winding of the transformer element that the RegControl is monitoring. 1 or 2, typically.  Side Effect: Sets TAPWINDING property to the same winding.

        DSS property name: `Winding`, DSS property index: 2.
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @Winding.setter
    def Winding(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def VReg(self) -> float:
        """
        Voltage regulator setting, in VOLTS, for the winding being controlled.  Multiplying this value times the ptratio should yield the voltage across the WINDING of the controlled transformer. Default is 120.0

        DSS property name: `VReg`, DSS property index: 3.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @VReg.setter
    def VReg(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def Band(self) -> float:
        """
        Bandwidth in VOLTS for the controlled bus (see help for ptratio property).  Default is 3.0

        DSS property name: `Band`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @Band.setter
    def Band(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def PTRatio(self) -> float:
        """
        Ratio of the PT that converts the controlled winding voltage to the regulator control voltage. Default is 60.  If the winding is Wye, the line-to-neutral voltage is used.  Else, the line-to-line voltage is used. SIDE EFFECT: Also sets RemotePTRatio property.

        DSS property name: `PTRatio`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @PTRatio.setter
    def PTRatio(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def CTPrim(self) -> float:
        """
        Rating, in Amperes, of the primary CT rating for which the line amps convert to control rated amps.The typical default secondary ampere rating is 0.2 Amps (check with manufacturer specs). Current at which the LDC voltages match the R and X settings.

        DSS property name: `CTPrim`, DSS property index: 6.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    @CTPrim.setter
    def CTPrim(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 6, value)

    @property
    def R(self) -> float:
        """
        R setting on the line drop compensator in the regulator, expressed in VOLTS.

        DSS property name: `R`, DSS property index: 7.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @R.setter
    def R(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def X(self) -> float:
        """
        X setting on the line drop compensator in the regulator, expressed in VOLTS.

        DSS property name: `X`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @X.setter
    def X(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def Bus(self) -> str:
        """
        Name of a bus (busname.nodename) in the system to use as the controlled bus instead of the bus to which the transformer winding is connected or the R and X line drop compensator settings.  Do not specify this value if you wish to use the line drop compensator settings.  Default is null string. Assumes the base voltage for this bus is the same as the transformer winding base specified above. Note: This bus (1-phase) WILL BE CREATED by the regulator control upon SOLVE if not defined by some other device. You can specify the node of the bus you wish to sample (defaults to 1). If specified, the RegControl is redefined as a 1-phase device since only one voltage is used.

        DSS property name: `Bus`, DSS property index: 9.
        """
        return self._get_prop_string(9)

    @Bus.setter
    def Bus(self, value: AnyStr):
        self._set_string_o(9, value)

    @property
    def Delay(self) -> float:
        """
        Time delay, in seconds, from when the voltage goes out of band to when the tap changing begins. This is used to determine which regulator control will act first. Default is 15.  You may specify any floating point number to achieve a model of whatever condition is necessary.

        DSS property name: `Delay`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @Delay.setter
    def Delay(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def Reversible(self) -> bool:
        """
        {Yes |No*} Indicates whether or not the regulator can be switched to regulate in the reverse direction. Default is No.Typically applies only to line regulators and not to LTC on a substation transformer.

        DSS property name: `Reversible`, DSS property index: 11.
        """
        return self._lib.Obj_GetInt32(self._ptr, 11) != 0

    @Reversible.setter
    def Reversible(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 11, value)

    @property
    def RevVReg(self) -> float:
        """
        Voltage setting in volts for operation in the reverse direction.

        DSS property name: `RevVReg`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @RevVReg.setter
    def RevVReg(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def RevBand(self) -> float:
        """
        Bandwidth for operating in the reverse direction.

        DSS property name: `RevBand`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @RevBand.setter
    def RevBand(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def RevR(self) -> float:
        """
        R line drop compensator setting for reverse direction.

        DSS property name: `RevR`, DSS property index: 14.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @RevR.setter
    def RevR(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def RevX(self) -> float:
        """
        X line drop compensator setting for reverse direction.

        DSS property name: `RevX`, DSS property index: 15.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @RevX.setter
    def RevX(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def TapDelay(self) -> float:
        """
        Delay in sec between tap changes. Default is 2. This is how long it takes between changes after the first change.

        DSS property name: `TapDelay`, DSS property index: 16.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    @TapDelay.setter
    def TapDelay(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 16, value)

    @property
    def DebugTrace(self) -> bool:
        """
        {Yes | No* }  Default is no.  Turn this on to capture the progress of the regulator model for each control iteration.  Creates a separate file for each RegControl named "REG_name.csv".

        DSS property name: `DebugTrace`, DSS property index: 17.
        """
        return self._lib.Obj_GetInt32(self._ptr, 17) != 0

    @DebugTrace.setter
    def DebugTrace(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 17, value)

    @property
    def MaxTapChange(self) -> int:
        """
        Maximum allowable tap change per control iteration in STATIC control mode.  Default is 16. 

        Set this to 1 to better approximate actual control action. 

        Set this to 0 to fix the tap in the current position.

        DSS property name: `MaxTapChange`, DSS property index: 18.
        """
        return self._lib.Obj_GetInt32(self._ptr, 18)

    @MaxTapChange.setter
    def MaxTapChange(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 18, value)

    @property
    def InverseTime(self) -> bool:
        """
        {Yes | No* } Default is no.  The time delay is adjusted inversely proportional to the amount the voltage is outside the band down to 10%.

        DSS property name: `InverseTime`, DSS property index: 19.
        """
        return self._lib.Obj_GetInt32(self._ptr, 19) != 0

    @InverseTime.setter
    def InverseTime(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 19, value)

    @property
    def TapWinding(self) -> int:
        """
        Winding containing the actual taps, if different than the WINDING property. Defaults to the same winding as specified by the WINDING property.

        DSS property name: `TapWinding`, DSS property index: 20.
        """
        return self._lib.Obj_GetInt32(self._ptr, 20)

    @TapWinding.setter
    def TapWinding(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 20, value)

    @property
    def VLimit(self) -> float:
        """
        Voltage Limit for bus to which regulated winding is connected (e.g. first customer). Default is 0.0. Set to a value greater then zero to activate this function.

        DSS property name: `VLimit`, DSS property index: 21.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @VLimit.setter
    def VLimit(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    @property
    def PTPhase(self) -> Union[enums.RegControlPhaseSelection, int]:
        """
        For multi-phase transformers, the number of the phase being monitored or one of { MAX | MIN} for all phases. Default=1. Must be less than or equal to the number of phases. Ignored for regulated bus.

        DSS property name: `PTPhase`, DSS property index: 22.
        """
        value = self._lib.Obj_GetInt32(self._ptr, 22)
        if value > 0:
            return value
    
        return enums.RegControlPhaseSelection(value)

    @PTPhase.setter
    def PTPhase(self, value: Union[AnyStr, int, enums.RegControlPhaseSelection]):
        if not isinstance(value, int):
            self._set_string_o(22, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 22, value)

    @property
    def PTPhase_str(self) -> str:
        """
        For multi-phase transformers, the number of the phase being monitored or one of { MAX | MIN} for all phases. Default=1. Must be less than or equal to the number of phases. Ignored for regulated bus.

        DSS property name: `PTPhase`, DSS property index: 22.
        """
        return self._get_prop_string(22)

    @PTPhase_str.setter
    def PTPhase_str(self, value: AnyStr):
        self.PTPhase = value

    @property
    def RevThreshold(self) -> float:
        """
        kW reverse power threshold for reversing the direction of the regulator. Default is 100.0 kw.

        DSS property name: `RevThreshold`, DSS property index: 23.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    @RevThreshold.setter
    def RevThreshold(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 23, value)

    @property
    def RevDelay(self) -> float:
        """
        Time Delay in seconds (s) for executing the reversing action once the threshold for reversing has been exceeded. Default is 60 s.

        DSS property name: `RevDelay`, DSS property index: 24.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    @RevDelay.setter
    def RevDelay(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 24, value)

    @property
    def RevNeutral(self) -> bool:
        """
        {Yes | No*} Default is no. Set this to Yes if you want the regulator to go to neutral in the reverse direction or in cogen operation.

        DSS property name: `RevNeutral`, DSS property index: 25.
        """
        return self._lib.Obj_GetInt32(self._ptr, 25) != 0

    @RevNeutral.setter
    def RevNeutral(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 25, value)

    @property
    def EventLog(self) -> bool:
        """
        {Yes/True | No/False*} Default is NO for regulator control. Log control actions to Eventlog.

        DSS property name: `EventLog`, DSS property index: 26.
        """
        return self._lib.Obj_GetInt32(self._ptr, 26) != 0

    @EventLog.setter
    def EventLog(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 26, value)

    @property
    def RemotePTRatio(self) -> float:
        """
        When regulating a bus (the Bus= property is set), the PT ratio required to convert actual voltage at the remote bus to control voltage. Is initialized to PTratio property. Set this property after setting PTratio.

        DSS property name: `RemotePTRatio`, DSS property index: 27.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 27)

    @RemotePTRatio.setter
    def RemotePTRatio(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 27, value)

    @property
    def TapNum(self) -> int:
        """
        An integer number indicating the tap position that the controlled transformer winding tap position is currently at, or is being set to.  If being set, and the value is outside the range of the transformer min or max tap, then set to the min or max tap position as appropriate. Default is 0

        DSS property name: `TapNum`, DSS property index: 28.
        """
        return self._lib.Obj_GetInt32(self._ptr, 28)

    @TapNum.setter
    def TapNum(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 28, value)

    def Reset(self, value: bool = True):
        """
        {Yes | No} If Yes, forces Reset of this RegControl.

        DSS property name: `Reset`, DSS property index: 29.
        """
        self._lib.Obj_SetInt32(self._ptr, 29, value)

    @property
    def LDC_Z(self) -> float:
        """
        Z value for Beckwith LDC_Z control option. Volts adjustment at rated control current.

        DSS property name: `LDC_Z`, DSS property index: 30.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 30)

    @LDC_Z.setter
    def LDC_Z(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 30, value)

    @property
    def Rev_Z(self) -> float:
        """
        Reverse Z value for Beckwith LDC_Z control option.

        DSS property name: `Rev_Z`, DSS property index: 31.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 31)

    @Rev_Z.setter
    def Rev_Z(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 31, value)

    @property
    def Cogen(self) -> bool:
        """
        {Yes|No*} Default is No. The Cogen feature is activated. Continues looking forward if power reverses, but switches to reverse-mode LDC, vreg and band values.

        DSS property name: `Cogen`, DSS property index: 32.
        """
        return self._lib.Obj_GetInt32(self._ptr, 32) != 0

    @Cogen.setter
    def Cogen(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 32, value)

    @property
    def BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 33.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 33)

    @BaseFreq.setter
    def BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 33, value)

    @property
    def Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 34.
        """
        return self._lib.Obj_GetInt32(self._ptr, 34) != 0

    @Enabled.setter
    def Enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 34, value)

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

class RegControlBatch(DSSBatch):
    _cls_name = 'RegControl'
    _obj_cls = RegControl
    _cls_idx = 21


    @property
    def Transformer(self) -> List[str]:
        """
        Name of Transformer or AutoTrans element to which the RegControl is connected. Do not specify the full object name; "Transformer" or "AutoTrans" is assumed for the object class.  Example:

        Transformer=Xfmr1

        DSS property name: `Transformer`, DSS property index: 1.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @Transformer.setter
    def Transformer(self, value: Union[AnyStr, TransformerObj, AutoTrans, List[AnyStr], List[Union[TransformerObj, AutoTrans]]]):
        self._set_batch_obj_prop(1, value)

    @property
    def Transformer_obj(self) -> List[Union[TransformerObj, AutoTrans]]:
        """
        Name of Transformer or AutoTrans element to which the RegControl is connected. Do not specify the full object name; "Transformer" or "AutoTrans" is assumed for the object class.  Example:

        Transformer=Xfmr1

        DSS property name: `Transformer`, DSS property index: 1.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 1)

    @Transformer_obj.setter
    def Transformer_obj(self, value: Union[TransformerObj, AutoTrans]):
        self._set_batch_string(1, value)

    @property
    def Winding(self) -> BatchInt32ArrayProxy:
        """
        Number of the winding of the transformer element that the RegControl is monitoring. 1 or 2, typically.  Side Effect: Sets TAPWINDING property to the same winding.

        DSS property name: `Winding`, DSS property index: 2.
        """
        return BatchInt32ArrayProxy(self, 2)

    @Winding.setter
    def Winding(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(2, value)

    @property
    def VReg(self) -> BatchFloat64ArrayProxy:
        """
        Voltage regulator setting, in VOLTS, for the winding being controlled.  Multiplying this value times the ptratio should yield the voltage across the WINDING of the controlled transformer. Default is 120.0

        DSS property name: `VReg`, DSS property index: 3.
        """
        return BatchFloat64ArrayProxy(self, 3)

    @VReg.setter
    def VReg(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(3, value)

    @property
    def Band(self) -> BatchFloat64ArrayProxy:
        """
        Bandwidth in VOLTS for the controlled bus (see help for ptratio property).  Default is 3.0

        DSS property name: `Band`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    @Band.setter
    def Band(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(4, value)

    @property
    def PTRatio(self) -> BatchFloat64ArrayProxy:
        """
        Ratio of the PT that converts the controlled winding voltage to the regulator control voltage. Default is 60.  If the winding is Wye, the line-to-neutral voltage is used.  Else, the line-to-line voltage is used. SIDE EFFECT: Also sets RemotePTRatio property.

        DSS property name: `PTRatio`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    @PTRatio.setter
    def PTRatio(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(5, value)

    @property
    def CTPrim(self) -> BatchFloat64ArrayProxy:
        """
        Rating, in Amperes, of the primary CT rating for which the line amps convert to control rated amps.The typical default secondary ampere rating is 0.2 Amps (check with manufacturer specs). Current at which the LDC voltages match the R and X settings.

        DSS property name: `CTPrim`, DSS property index: 6.
        """
        return BatchFloat64ArrayProxy(self, 6)

    @CTPrim.setter
    def CTPrim(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(6, value)

    @property
    def R(self) -> BatchFloat64ArrayProxy:
        """
        R setting on the line drop compensator in the regulator, expressed in VOLTS.

        DSS property name: `R`, DSS property index: 7.
        """
        return BatchFloat64ArrayProxy(self, 7)

    @R.setter
    def R(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(7, value)

    @property
    def X(self) -> BatchFloat64ArrayProxy:
        """
        X setting on the line drop compensator in the regulator, expressed in VOLTS.

        DSS property name: `X`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    @X.setter
    def X(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(8, value)

    @property
    def Bus(self) -> List[str]:
        """
        Name of a bus (busname.nodename) in the system to use as the controlled bus instead of the bus to which the transformer winding is connected or the R and X line drop compensator settings.  Do not specify this value if you wish to use the line drop compensator settings.  Default is null string. Assumes the base voltage for this bus is the same as the transformer winding base specified above. Note: This bus (1-phase) WILL BE CREATED by the regulator control upon SOLVE if not defined by some other device. You can specify the node of the bus you wish to sample (defaults to 1). If specified, the RegControl is redefined as a 1-phase device since only one voltage is used.

        DSS property name: `Bus`, DSS property index: 9.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 9) 

    @Bus.setter
    def Bus(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(9, value)

    @property
    def Delay(self) -> BatchFloat64ArrayProxy:
        """
        Time delay, in seconds, from when the voltage goes out of band to when the tap changing begins. This is used to determine which regulator control will act first. Default is 15.  You may specify any floating point number to achieve a model of whatever condition is necessary.

        DSS property name: `Delay`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    @Delay.setter
    def Delay(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(10, value)

    @property
    def Reversible(self) -> List[bool]:
        """
        {Yes |No*} Indicates whether or not the regulator can be switched to regulate in the reverse direction. Default is No.Typically applies only to line regulators and not to LTC on a substation transformer.

        DSS property name: `Reversible`, DSS property index: 11.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 11)
        ]
    @Reversible.setter
    def Reversible(self, value: bool):
        self._set_batch_int32_array(11, value)

    @property
    def RevVReg(self) -> BatchFloat64ArrayProxy:
        """
        Voltage setting in volts for operation in the reverse direction.

        DSS property name: `RevVReg`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    @RevVReg.setter
    def RevVReg(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(12, value)

    @property
    def RevBand(self) -> BatchFloat64ArrayProxy:
        """
        Bandwidth for operating in the reverse direction.

        DSS property name: `RevBand`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    @RevBand.setter
    def RevBand(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(13, value)

    @property
    def RevR(self) -> BatchFloat64ArrayProxy:
        """
        R line drop compensator setting for reverse direction.

        DSS property name: `RevR`, DSS property index: 14.
        """
        return BatchFloat64ArrayProxy(self, 14)

    @RevR.setter
    def RevR(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(14, value)

    @property
    def RevX(self) -> BatchFloat64ArrayProxy:
        """
        X line drop compensator setting for reverse direction.

        DSS property name: `RevX`, DSS property index: 15.
        """
        return BatchFloat64ArrayProxy(self, 15)

    @RevX.setter
    def RevX(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(15, value)

    @property
    def TapDelay(self) -> BatchFloat64ArrayProxy:
        """
        Delay in sec between tap changes. Default is 2. This is how long it takes between changes after the first change.

        DSS property name: `TapDelay`, DSS property index: 16.
        """
        return BatchFloat64ArrayProxy(self, 16)

    @TapDelay.setter
    def TapDelay(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(16, value)

    @property
    def DebugTrace(self) -> List[bool]:
        """
        {Yes | No* }  Default is no.  Turn this on to capture the progress of the regulator model for each control iteration.  Creates a separate file for each RegControl named "REG_name.csv".

        DSS property name: `DebugTrace`, DSS property index: 17.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 17)
        ]
    @DebugTrace.setter
    def DebugTrace(self, value: bool):
        self._set_batch_int32_array(17, value)

    @property
    def MaxTapChange(self) -> BatchInt32ArrayProxy:
        """
        Maximum allowable tap change per control iteration in STATIC control mode.  Default is 16. 

        Set this to 1 to better approximate actual control action. 

        Set this to 0 to fix the tap in the current position.

        DSS property name: `MaxTapChange`, DSS property index: 18.
        """
        return BatchInt32ArrayProxy(self, 18)

    @MaxTapChange.setter
    def MaxTapChange(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(18, value)

    @property
    def InverseTime(self) -> List[bool]:
        """
        {Yes | No* } Default is no.  The time delay is adjusted inversely proportional to the amount the voltage is outside the band down to 10%.

        DSS property name: `InverseTime`, DSS property index: 19.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 19)
        ]
    @InverseTime.setter
    def InverseTime(self, value: bool):
        self._set_batch_int32_array(19, value)

    @property
    def TapWinding(self) -> BatchInt32ArrayProxy:
        """
        Winding containing the actual taps, if different than the WINDING property. Defaults to the same winding as specified by the WINDING property.

        DSS property name: `TapWinding`, DSS property index: 20.
        """
        return BatchInt32ArrayProxy(self, 20)

    @TapWinding.setter
    def TapWinding(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(20, value)

    @property
    def VLimit(self) -> BatchFloat64ArrayProxy:
        """
        Voltage Limit for bus to which regulated winding is connected (e.g. first customer). Default is 0.0. Set to a value greater then zero to activate this function.

        DSS property name: `VLimit`, DSS property index: 21.
        """
        return BatchFloat64ArrayProxy(self, 21)

    @VLimit.setter
    def VLimit(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(21, value)

    @property
    def PTPhase(self) -> BatchInt32ArrayProxy:
        """
        For multi-phase transformers, the number of the phase being monitored or one of { MAX | MIN} for all phases. Default=1. Must be less than or equal to the number of phases. Ignored for regulated bus.

        DSS property name: `PTPhase`, DSS property index: 22.
        """
        return BatchInt32ArrayProxy(self, 22)

    @PTPhase.setter
    def PTPhase(self, value: Union[AnyStr, int, enums.RegControlPhaseSelection, List[AnyStr], List[int], List[enums.RegControlPhaseSelection], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(22, value)
            return
    
        self._set_batch_int32_array(22, value)

    @property
    def PTPhase_str(self) -> str:
        """
        For multi-phase transformers, the number of the phase being monitored or one of { MAX | MIN} for all phases. Default=1. Must be less than or equal to the number of phases. Ignored for regulated bus.

        DSS property name: `PTPhase`, DSS property index: 22.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 22)

    @PTPhase_str.setter
    def PTPhase_str(self, value: AnyStr):
        self.PTPhase = value

    @property
    def RevThreshold(self) -> BatchFloat64ArrayProxy:
        """
        kW reverse power threshold for reversing the direction of the regulator. Default is 100.0 kw.

        DSS property name: `RevThreshold`, DSS property index: 23.
        """
        return BatchFloat64ArrayProxy(self, 23)

    @RevThreshold.setter
    def RevThreshold(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(23, value)

    @property
    def RevDelay(self) -> BatchFloat64ArrayProxy:
        """
        Time Delay in seconds (s) for executing the reversing action once the threshold for reversing has been exceeded. Default is 60 s.

        DSS property name: `RevDelay`, DSS property index: 24.
        """
        return BatchFloat64ArrayProxy(self, 24)

    @RevDelay.setter
    def RevDelay(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(24, value)

    @property
    def RevNeutral(self) -> List[bool]:
        """
        {Yes | No*} Default is no. Set this to Yes if you want the regulator to go to neutral in the reverse direction or in cogen operation.

        DSS property name: `RevNeutral`, DSS property index: 25.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 25)
        ]
    @RevNeutral.setter
    def RevNeutral(self, value: bool):
        self._set_batch_int32_array(25, value)

    @property
    def EventLog(self) -> List[bool]:
        """
        {Yes/True | No/False*} Default is NO for regulator control. Log control actions to Eventlog.

        DSS property name: `EventLog`, DSS property index: 26.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 26)
        ]
    @EventLog.setter
    def EventLog(self, value: bool):
        self._set_batch_int32_array(26, value)

    @property
    def RemotePTRatio(self) -> BatchFloat64ArrayProxy:
        """
        When regulating a bus (the Bus= property is set), the PT ratio required to convert actual voltage at the remote bus to control voltage. Is initialized to PTratio property. Set this property after setting PTratio.

        DSS property name: `RemotePTRatio`, DSS property index: 27.
        """
        return BatchFloat64ArrayProxy(self, 27)

    @RemotePTRatio.setter
    def RemotePTRatio(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(27, value)

    @property
    def TapNum(self) -> BatchInt32ArrayProxy:
        """
        An integer number indicating the tap position that the controlled transformer winding tap position is currently at, or is being set to.  If being set, and the value is outside the range of the transformer min or max tap, then set to the min or max tap position as appropriate. Default is 0

        DSS property name: `TapNum`, DSS property index: 28.
        """
        return BatchInt32ArrayProxy(self, 28)

    @TapNum.setter
    def TapNum(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(28, value)

    def Reset(self, value: Union[bool, List[bool]] = True):
        """
        {Yes | No} If Yes, forces Reset of this RegControl.

        DSS property name: `Reset`, DSS property index: 29.
        """
        self._set_batch_int32_array(29, value)

    @property
    def LDC_Z(self) -> BatchFloat64ArrayProxy:
        """
        Z value for Beckwith LDC_Z control option. Volts adjustment at rated control current.

        DSS property name: `LDC_Z`, DSS property index: 30.
        """
        return BatchFloat64ArrayProxy(self, 30)

    @LDC_Z.setter
    def LDC_Z(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(30, value)

    @property
    def Rev_Z(self) -> BatchFloat64ArrayProxy:
        """
        Reverse Z value for Beckwith LDC_Z control option.

        DSS property name: `Rev_Z`, DSS property index: 31.
        """
        return BatchFloat64ArrayProxy(self, 31)

    @Rev_Z.setter
    def Rev_Z(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(31, value)

    @property
    def Cogen(self) -> List[bool]:
        """
        {Yes|No*} Default is No. The Cogen feature is activated. Continues looking forward if power reverses, but switches to reverse-mode LDC, vreg and band values.

        DSS property name: `Cogen`, DSS property index: 32.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 32)
        ]
    @Cogen.setter
    def Cogen(self, value: bool):
        self._set_batch_int32_array(32, value)

    @property
    def BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 33.
        """
        return BatchFloat64ArrayProxy(self, 33)

    @BaseFreq.setter
    def BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(33, value)

    @property
    def Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 34.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 34)
        ]
    @Enabled.setter
    def Enabled(self, value: bool):
        self._set_batch_int32_array(34, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 35.
        """
        self._set_batch_string(35, value)

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

class IRegControl(IDSSObj):
    __slots__ = ()

    def __init__(self, iobj):
        super().__init__(iobj, RegControl, RegControlBatch)

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> RegControl:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[RegControlProperties]) -> RegControl:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[RegControlBatchProperties]) -> RegControlBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
