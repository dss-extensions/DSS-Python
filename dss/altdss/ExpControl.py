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

class ExpControl(DSSObj, CircuitElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots
    _cls_name = 'ExpControl'
    _cls_idx = 43
    _cls_prop_idx = {
        'pvsystemlist': 1,
        'vreg': 2,
        'slope': 3,
        'vregtau': 4,
        'qbias': 5,
        'vregmin': 6,
        'vregmax': 7,
        'qmaxlead': 8,
        'qmaxlag': 9,
        'eventlog': 10,
        'deltaq_factor': 11,
        'preferq': 12,
        'tresponse': 13,
        'derlist': 14,
        'basefreq': 15,
        'enabled': 16,
        'like': 17,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)

    def _get_PVSystemList(self) -> List[str]:
        """
        Array list of PVSystems to be controlled.

        If not specified, all PVSystems in the circuit are assumed to be controlled by this ExpControl.

        DSS property name: `PVSystemList`, DSS property index: 1.
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 1)

    def _set_PVSystemList(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 1, value_ptr, value_count, flags)
        self._check_for_error()

    PVSystemList = property(_get_PVSystemList, _set_PVSystemList) # type: List[str]

    def _get_VReg(self) -> float:
        """
        Per-unit voltage at which reactive power is zero; defaults to 1.0.

        This may dynamically self-adjust when VregTau > 0, limited by VregMin and VregMax.If input as 0, Vreg will be initialized from a snapshot solution with no inverter Q.The equilibrium point of reactive power is also affected by Qbias

        DSS property name: `VReg`, DSS property index: 2.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 2)

    def _set_VReg(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 2, value, flags)

    VReg = property(_get_VReg, _set_VReg) # type: float

    def _get_Slope(self) -> float:
        """
        Per-unit reactive power injection / per-unit voltage deviation from Vreg; defaults to 50.

        Unlike InvControl, base reactive power is constant at the inverter kva rating.

        DSS property name: `Slope`, DSS property index: 3.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    def _set_Slope(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 3, value, flags)

    Slope = property(_get_Slope, _set_Slope) # type: float

    def _get_VRegTau(self) -> float:
        """
        Time constant for adaptive Vreg. Defaults to 1200 seconds.

        When the control injects or absorbs reactive power due to a voltage deviation from the Q=0 crossing of the volt-var curve, the Q=0 crossing will move toward the actual terminal voltage with this time constant. Over time, the effect is to gradually bring inverter reactive power to zero as the grid voltage changes due to non-solar effects. If zero, then Vreg stays fixed. IEEE1547-2018 requires adjustability from 300s to 5000s

        DSS property name: `VRegTau`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    def _set_VRegTau(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 4, value, flags)

    VRegTau = property(_get_VRegTau, _set_VRegTau) # type: float

    def _get_QBias(self) -> float:
        """
        Equilibrium per-unit reactive power when V=Vreg; defaults to 0.

        Enter > 0 for lagging (capacitive) bias, < 0 for leading (inductive) bias.

        DSS property name: `QBias`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    def _set_QBias(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 5, value, flags)

    QBias = property(_get_QBias, _set_QBias) # type: float

    def _get_VRegMin(self) -> float:
        """
        Lower limit on adaptive Vreg; defaults to 0.95 per-unit

        DSS property name: `VRegMin`, DSS property index: 6.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    def _set_VRegMin(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 6, value, flags)

    VRegMin = property(_get_VRegMin, _set_VRegMin) # type: float

    def _get_VRegMax(self) -> float:
        """
        Upper limit on adaptive Vreg; defaults to 1.05 per-unit

        DSS property name: `VRegMax`, DSS property index: 7.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    def _set_VRegMax(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 7, value, flags)

    VRegMax = property(_get_VRegMax, _set_VRegMax) # type: float

    def _get_QMaxLead(self) -> float:
        """
        Limit on leading (inductive) reactive power injection, in per-unit of base kva; defaults to 0.44.For Category A inverters per P1547/D7, set this value to 0.25.

        Regardless of QmaxLead, the reactive power injection is still limited by dynamic headroom when actual real power output exceeds 0%

        DSS property name: `QMaxLead`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    def _set_QMaxLead(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 8, value, flags)

    QMaxLead = property(_get_QMaxLead, _set_QMaxLead) # type: float

    def _get_QMaxLag(self) -> float:
        """
        Limit on lagging (capacitive) reactive power injection, in per-unit of base kva; defaults to 0.44.

        For Category A inverters per P1547/D7, set this value to 0.25.Regardless of QmaxLag, the reactive power injection is still limited by dynamic headroom when actual real power output exceeds 0%

        DSS property name: `QMaxLag`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    def _set_QMaxLag(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 9, value, flags)

    QMaxLag = property(_get_QMaxLag, _set_QMaxLag) # type: float

    def _get_EventLog(self) -> bool:
        """
        {Yes/True* | No/False} Default is No for ExpControl. Log control actions to Eventlog.

        DSS property name: `EventLog`, DSS property index: 10.
        """
        return self._lib.Obj_GetInt32(self._ptr, 10) != 0

    def _set_EventLog(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 10, value, flags)

    EventLog = property(_get_EventLog, _set_EventLog) # type: bool

    def _get_DeltaQ_Factor(self) -> float:
        """
        Convergence parameter; Defaults to 0.7. 

        Sets the maximum change (in per unit) from the prior var output level to the desired var output level during each control iteration. If numerical instability is noticed in solutions such as var sign changing from one control iteration to the next and voltages oscillating between two values with some separation, this is an indication of numerical instability (use the EventLog to diagnose). If the maximum control iterations are exceeded, and no numerical instability is seen in the EventLog of via monitors, then try increasing the value of this parameter to reduce the number of control iterations needed to achieve the control criteria, and move to the power flow solution.

        DSS property name: `DeltaQ_Factor`, DSS property index: 11.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    def _set_DeltaQ_Factor(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 11, value, flags)

    DeltaQ_Factor = property(_get_DeltaQ_Factor, _set_DeltaQ_Factor) # type: float

    def _get_PreferQ(self) -> bool:
        """
        {Yes/True* | No/False} Default is No for ExpControl.

        Curtails real power output as needed to meet the reactive power requirement. IEEE1547-2018 requires Yes, but the default is No for backward compatibility of OpenDSS models.

        DSS property name: `PreferQ`, DSS property index: 12.
        """
        return self._lib.Obj_GetInt32(self._ptr, 12) != 0

    def _set_PreferQ(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 12, value, flags)

    PreferQ = property(_get_PreferQ, _set_PreferQ) # type: bool

    def _get_TResponse(self) -> float:
        """
        Open-loop response time for changes in Q.

        The value of Q reaches 90% of the target change within Tresponse, which corresponds to a low-pass filter having tau = Tresponse / 2.3026. The behavior is similar to LPFTAU in InvControl, but here the response time is input instead of the time constant. IEEE1547-2018 default is 10s for Category A and 5s for Category B, adjustable from 1s to 90s for both categories. However, the default is 0 for backward compatibility of OpenDSS models.

        DSS property name: `TResponse`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    def _set_TResponse(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 13, value, flags)

    TResponse = property(_get_TResponse, _set_TResponse) # type: float

    def _get_DERList(self) -> List[str]:
        """
        Alternative to PVSystemList for CIM export and import.

        However, storage is not actually implemented yet. Use fully qualified PVSystem names.

        DSS property name: `DERList`, DSS property index: 14.
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 14)

    def _set_DERList(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 14, value_ptr, value_count, flags)
        self._check_for_error()

    DERList = property(_get_DERList, _set_DERList) # type: List[str]

    def _get_BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 15.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 15, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float

    def _get_Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 16.
        """
        return self._lib.Obj_GetInt32(self._ptr, 16) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 16, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 17.
        """
        self._set_string_o(17, value)


class ExpControlProperties(TypedDict):
    PVSystemList: List[AnyStr]
    VReg: float
    Slope: float
    VRegTau: float
    QBias: float
    VRegMin: float
    VRegMax: float
    QMaxLead: float
    QMaxLag: float
    EventLog: bool
    DeltaQ_Factor: float
    PreferQ: bool
    TResponse: float
    DERList: List[AnyStr]
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class ExpControlBatch(DSSBatch, CircuitElementBatchMixin):
    _cls_name = 'ExpControl'
    _obj_cls = ExpControl
    _cls_idx = 43

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)

    def _get_PVSystemList(self) -> List[List[str]]:
        """
        Array list of PVSystems to be controlled.

        If not specified, all PVSystems in the circuit are assumed to be controlled by this ExpControl.

        DSS property name: `PVSystemList`, DSS property index: 1.
        """
        return self._get_string_ll(1)

    def _set_PVSystemList(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._unpack():
            self._lib.Obj_SetStringArray(x, 1, value_ptr, value_count, flags)

        self._check_for_error()

    PVSystemList = property(_get_PVSystemList, _set_PVSystemList) # type: List[List[str]]

    def _get_VReg(self) -> BatchFloat64ArrayProxy:
        """
        Per-unit voltage at which reactive power is zero; defaults to 1.0.

        This may dynamically self-adjust when VregTau > 0, limited by VregMin and VregMax.If input as 0, Vreg will be initialized from a snapshot solution with no inverter Q.The equilibrium point of reactive power is also affected by Qbias

        DSS property name: `VReg`, DSS property index: 2.
        """
        return BatchFloat64ArrayProxy(self, 2)

    def _set_VReg(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(2, value, flags)

    VReg = property(_get_VReg, _set_VReg) # type: BatchFloat64ArrayProxy

    def _get_Slope(self) -> BatchFloat64ArrayProxy:
        """
        Per-unit reactive power injection / per-unit voltage deviation from Vreg; defaults to 50.

        Unlike InvControl, base reactive power is constant at the inverter kva rating.

        DSS property name: `Slope`, DSS property index: 3.
        """
        return BatchFloat64ArrayProxy(self, 3)

    def _set_Slope(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(3, value, flags)

    Slope = property(_get_Slope, _set_Slope) # type: BatchFloat64ArrayProxy

    def _get_VRegTau(self) -> BatchFloat64ArrayProxy:
        """
        Time constant for adaptive Vreg. Defaults to 1200 seconds.

        When the control injects or absorbs reactive power due to a voltage deviation from the Q=0 crossing of the volt-var curve, the Q=0 crossing will move toward the actual terminal voltage with this time constant. Over time, the effect is to gradually bring inverter reactive power to zero as the grid voltage changes due to non-solar effects. If zero, then Vreg stays fixed. IEEE1547-2018 requires adjustability from 300s to 5000s

        DSS property name: `VRegTau`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    def _set_VRegTau(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(4, value, flags)

    VRegTau = property(_get_VRegTau, _set_VRegTau) # type: BatchFloat64ArrayProxy

    def _get_QBias(self) -> BatchFloat64ArrayProxy:
        """
        Equilibrium per-unit reactive power when V=Vreg; defaults to 0.

        Enter > 0 for lagging (capacitive) bias, < 0 for leading (inductive) bias.

        DSS property name: `QBias`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    def _set_QBias(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(5, value, flags)

    QBias = property(_get_QBias, _set_QBias) # type: BatchFloat64ArrayProxy

    def _get_VRegMin(self) -> BatchFloat64ArrayProxy:
        """
        Lower limit on adaptive Vreg; defaults to 0.95 per-unit

        DSS property name: `VRegMin`, DSS property index: 6.
        """
        return BatchFloat64ArrayProxy(self, 6)

    def _set_VRegMin(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(6, value, flags)

    VRegMin = property(_get_VRegMin, _set_VRegMin) # type: BatchFloat64ArrayProxy

    def _get_VRegMax(self) -> BatchFloat64ArrayProxy:
        """
        Upper limit on adaptive Vreg; defaults to 1.05 per-unit

        DSS property name: `VRegMax`, DSS property index: 7.
        """
        return BatchFloat64ArrayProxy(self, 7)

    def _set_VRegMax(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(7, value, flags)

    VRegMax = property(_get_VRegMax, _set_VRegMax) # type: BatchFloat64ArrayProxy

    def _get_QMaxLead(self) -> BatchFloat64ArrayProxy:
        """
        Limit on leading (inductive) reactive power injection, in per-unit of base kva; defaults to 0.44.For Category A inverters per P1547/D7, set this value to 0.25.

        Regardless of QmaxLead, the reactive power injection is still limited by dynamic headroom when actual real power output exceeds 0%

        DSS property name: `QMaxLead`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    def _set_QMaxLead(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(8, value, flags)

    QMaxLead = property(_get_QMaxLead, _set_QMaxLead) # type: BatchFloat64ArrayProxy

    def _get_QMaxLag(self) -> BatchFloat64ArrayProxy:
        """
        Limit on lagging (capacitive) reactive power injection, in per-unit of base kva; defaults to 0.44.

        For Category A inverters per P1547/D7, set this value to 0.25.Regardless of QmaxLag, the reactive power injection is still limited by dynamic headroom when actual real power output exceeds 0%

        DSS property name: `QMaxLag`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    def _set_QMaxLag(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(9, value, flags)

    QMaxLag = property(_get_QMaxLag, _set_QMaxLag) # type: BatchFloat64ArrayProxy

    def _get_EventLog(self) -> List[bool]:
        """
        {Yes/True* | No/False} Default is No for ExpControl. Log control actions to Eventlog.

        DSS property name: `EventLog`, DSS property index: 10.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(10)
        ]

    def _set_EventLog(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(10, value, flags)

    EventLog = property(_get_EventLog, _set_EventLog) # type: List[bool]

    def _get_DeltaQ_Factor(self) -> BatchFloat64ArrayProxy:
        """
        Convergence parameter; Defaults to 0.7. 

        Sets the maximum change (in per unit) from the prior var output level to the desired var output level during each control iteration. If numerical instability is noticed in solutions such as var sign changing from one control iteration to the next and voltages oscillating between two values with some separation, this is an indication of numerical instability (use the EventLog to diagnose). If the maximum control iterations are exceeded, and no numerical instability is seen in the EventLog of via monitors, then try increasing the value of this parameter to reduce the number of control iterations needed to achieve the control criteria, and move to the power flow solution.

        DSS property name: `DeltaQ_Factor`, DSS property index: 11.
        """
        return BatchFloat64ArrayProxy(self, 11)

    def _set_DeltaQ_Factor(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(11, value, flags)

    DeltaQ_Factor = property(_get_DeltaQ_Factor, _set_DeltaQ_Factor) # type: BatchFloat64ArrayProxy

    def _get_PreferQ(self) -> List[bool]:
        """
        {Yes/True* | No/False} Default is No for ExpControl.

        Curtails real power output as needed to meet the reactive power requirement. IEEE1547-2018 requires Yes, but the default is No for backward compatibility of OpenDSS models.

        DSS property name: `PreferQ`, DSS property index: 12.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(12)
        ]

    def _set_PreferQ(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(12, value, flags)

    PreferQ = property(_get_PreferQ, _set_PreferQ) # type: List[bool]

    def _get_TResponse(self) -> BatchFloat64ArrayProxy:
        """
        Open-loop response time for changes in Q.

        The value of Q reaches 90% of the target change within Tresponse, which corresponds to a low-pass filter having tau = Tresponse / 2.3026. The behavior is similar to LPFTAU in InvControl, but here the response time is input instead of the time constant. IEEE1547-2018 default is 10s for Category A and 5s for Category B, adjustable from 1s to 90s for both categories. However, the default is 0 for backward compatibility of OpenDSS models.

        DSS property name: `TResponse`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    def _set_TResponse(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(13, value, flags)

    TResponse = property(_get_TResponse, _set_TResponse) # type: BatchFloat64ArrayProxy

    def _get_DERList(self) -> List[List[str]]:
        """
        Alternative to PVSystemList for CIM export and import.

        However, storage is not actually implemented yet. Use fully qualified PVSystem names.

        DSS property name: `DERList`, DSS property index: 14.
        """
        return self._get_string_ll(14)

    def _set_DERList(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._unpack():
            self._lib.Obj_SetStringArray(x, 14, value_ptr, value_count, flags)

        self._check_for_error()

    DERList = property(_get_DERList, _set_DERList) # type: List[List[str]]

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 15.
        """
        return BatchFloat64ArrayProxy(self, 15)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(15, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy

    def _get_Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 16.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(16)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(16, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 17.
        """
        self._set_batch_string(17, value, flags)

class ExpControlBatchProperties(TypedDict):
    PVSystemList: List[AnyStr]
    VReg: Union[float, Float64Array]
    Slope: Union[float, Float64Array]
    VRegTau: Union[float, Float64Array]
    QBias: Union[float, Float64Array]
    VRegMin: Union[float, Float64Array]
    VRegMax: Union[float, Float64Array]
    QMaxLead: Union[float, Float64Array]
    QMaxLag: Union[float, Float64Array]
    EventLog: bool
    DeltaQ_Factor: Union[float, Float64Array]
    PreferQ: bool
    TResponse: Union[float, Float64Array]
    DERList: List[AnyStr]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IExpControl(IDSSObj, ExpControlBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, ExpControl, ExpControlBatch)
        ExpControlBatch.__init__(self, self._api_util, sync_cls_idx=ExpControl._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> ExpControl:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[ExpControlProperties]) -> ExpControl:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[ExpControlBatchProperties]) -> ExpControlBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
