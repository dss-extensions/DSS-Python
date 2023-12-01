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
from .PDElement import PDElementBatchMixin, PDElementMixin
from .CircuitElement import CircuitElementBatchMixin, CircuitElementMixin
from .XYcurve import XYcurve

class GICTransformer(DSSObj, CircuitElementMixin, PDElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots + PDElementMixin._extra_slots
    _cls_name = 'GICTransformer'
    _cls_idx = 45
    _cls_prop_idx = {
        'bush': 1,
        'busnh': 2,
        'busx': 3,
        'busnx': 4,
        'phases': 5,
        'type': 6,
        'r1': 7,
        'r2': 8,
        'kvll1': 9,
        'kvll2': 10,
        'mva': 11,
        'varcurve': 12,
        'pctr1': 13,
        '%r1': 13,
        'pctr2': 14,
        '%r2': 14,
        'k': 15,
        'normamps': 16,
        'emergamps': 17,
        'faultrate': 18,
        'pctperm': 19,
        'repair': 20,
        'basefreq': 21,
        'enabled': 22,
        'like': 23,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)
       PDElementMixin.__init__(self)

    def _get_BusH(self) -> str:
        """
        Name of High-side(H) bus. Examples:
        BusH=busname
        BusH=busname.1.2.3

        DSS property name: `BusH`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    def _set_BusH(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(1, value, flags)

    BusH = property(_get_BusH, _set_BusH) # type: str

    def _get_BusNH(self) -> str:
        """
        Name of Neutral bus for H, or first, winding. Defaults to all phases connected to H-side bus, node 0, if not specified and transformer type is either GSU or YY. (Shunt Wye Connection to ground reference)For Auto, this is automatically set to the X bus.

        DSS property name: `BusNH`, DSS property index: 2.
        """
        return self._get_prop_string(2)

    def _set_BusNH(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(2, value, flags)

    BusNH = property(_get_BusNH, _set_BusNH) # type: str

    def _get_BusX(self) -> str:
        """
        Name of Low-side(X) bus, if type=Auto or YY. 

        DSS property name: `BusX`, DSS property index: 3.
        """
        return self._get_prop_string(3)

    def _set_BusX(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(3, value, flags)

    BusX = property(_get_BusX, _set_BusX) # type: str

    def _get_BusNX(self) -> str:
        """
        Name of Neutral bus for X, or Second, winding. Defaults to all phases connected to X-side bus, node 0, if not specified. (Shunt Wye Connection to ground reference)

        DSS property name: `BusNX`, DSS property index: 4.
        """
        return self._get_prop_string(4)

    def _set_BusNX(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(4, value, flags)

    BusNX = property(_get_BusNX, _set_BusNX) # type: str

    def _get_Phases(self) -> int:
        """
        Number of Phases. Default is 3.

        DSS property name: `Phases`, DSS property index: 5.
        """
        return self._lib.Obj_GetInt32(self._ptr, 5)

    def _set_Phases(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 5, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: int

    def _get_Type(self) -> enums.GICTransformerType:
        """
        Type of transformer: {GSU* | Auto | YY}. Default is GSU.

        DSS property name: `Type`, DSS property index: 6.
        """
        return enums.GICTransformerType(self._lib.Obj_GetInt32(self._ptr, 6))

    def _set_Type(self, value: Union[AnyStr, int, enums.GICTransformerType], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(6, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 6, value, flags)

    Type = property(_get_Type, _set_Type) # type: enums.GICTransformerType

    def _get_Type_str(self) -> str:
        """
        Type of transformer: {GSU* | Auto | YY}. Default is GSU.

        DSS property name: `Type`, DSS property index: 6.
        """
        return self._get_prop_string(6)

    def _set_Type_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Type(value, flags)

    Type_str = property(_get_Type_str, _set_Type_str) # type: str

    def _get_R1(self) -> float:
        """
        Resistance, each phase, ohms for H winding, (Series winding, if Auto). Default is 0.0001. If 

        DSS property name: `R1`, DSS property index: 7.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    def _set_R1(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 7, value, flags)

    R1 = property(_get_R1, _set_R1) # type: float

    def _get_R2(self) -> float:
        """
        Resistance, each phase, ohms for X winding, (Common winding, if Auto). Default is 0.0001. 

        DSS property name: `R2`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    def _set_R2(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 8, value, flags)

    R2 = property(_get_R2, _set_R2) # type: float

    def _get_kVLL1(self) -> float:
        """
        Optional. kV LL rating for H winding (winding 1). Default is 500. Required if you are going to export vars for power flow analysis or enter winding resistances in percent.

        DSS property name: `kVLL1`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    def _set_kVLL1(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 9, value, flags)

    kVLL1 = property(_get_kVLL1, _set_kVLL1) # type: float

    def _get_kVLL2(self) -> float:
        """
        Optional. kV LL rating for X winding (winding 2). Default is 138. Required if you are going to export vars for power flow analysis or enter winding resistances in percent..

        DSS property name: `kVLL2`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    def _set_kVLL2(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 10, value, flags)

    kVLL2 = property(_get_kVLL2, _set_kVLL2) # type: float

    def _get_MVA(self) -> float:
        """
        Optional. MVA Rating assumed Transformer. Default is 100. Used for computing vars due to GIC and winding resistances if kV and MVA ratings are specified.

        DSS property name: `MVA`, DSS property index: 11.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    def _set_MVA(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 11, value, flags)

    MVA = property(_get_MVA, _set_MVA) # type: float

    def _get_VarCurve_str(self) -> str:
        """
        Optional. XYCurve object name. Curve is expected as TOTAL pu vars vs pu GIC amps/phase. Vars are in pu of the MVA property. No Default value. Required only if you are going to export vars for power flow analysis. See K property.

        DSS property name: `VarCurve`, DSS property index: 12.
        """
        return self._get_prop_string(12)

    def _set_VarCurve_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(12, value, flags)

    VarCurve_str = property(_get_VarCurve_str, _set_VarCurve_str) # type: str

    def _get_VarCurve(self) -> XYcurve:
        """
        Optional. XYCurve object name. Curve is expected as TOTAL pu vars vs pu GIC amps/phase. Vars are in pu of the MVA property. No Default value. Required only if you are going to export vars for power flow analysis. See K property.

        DSS property name: `VarCurve`, DSS property index: 12.
        """
        return self._get_obj(12, XYcurve)

    def _set_VarCurve(self, value: Union[AnyStr, XYcurve], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(12, value, flags)
            return

        self._set_string_o(12, value, flags)

    VarCurve = property(_get_VarCurve, _set_VarCurve) # type: XYcurve

    def _get_pctR1(self) -> float:
        """
        Optional. Percent Resistance, each phase, for H winding (1), (Series winding, if Auto). Default is 0.2. 

        Alternative way to enter R1 value. It is the actual resistances in ohmns that matter. MVA and kV should be specified.

        DSS property name: `%R1`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    def _set_pctR1(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 13, value, flags)

    pctR1 = property(_get_pctR1, _set_pctR1) # type: float

    def _get_pctR2(self) -> float:
        """
        Optional. Percent Resistance, each phase, for X winding (2), (Common winding, if Auto). Default is 0.2. 

        Alternative way to enter R2 value. It is the actual resistances in ohms that matter. MVA and kV should be specified.

        DSS property name: `%R2`, DSS property index: 14.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    def _set_pctR2(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 14, value, flags)

    pctR2 = property(_get_pctR2, _set_pctR2) # type: float

    def _get_K(self) -> float:
        """
        Mvar K factor. Default way to convert GIC Amps in H winding (winding 1) to Mvar. Default is 2.2. Commonly-used simple multiplier for estimating Mvar losses for power flow analysis. 

        Mvar = K * kvLL * GIC per phase / 1000 

        Mutually exclusive with using the VarCurve property and pu curves.If you specify this (default), VarCurve is ignored.

        DSS property name: `K`, DSS property index: 15.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    def _set_K(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 15, value, flags)

    K = property(_get_K, _set_K) # type: float

    def _get_NormAmps(self) -> float:
        """
        Normal rated current.

        DSS property name: `NormAmps`, DSS property index: 16.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    def _set_NormAmps(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 16, value, flags)

    NormAmps = property(_get_NormAmps, _set_NormAmps) # type: float

    def _get_EmergAmps(self) -> float:
        """
        Maximum or emerg current.

        DSS property name: `EmergAmps`, DSS property index: 17.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    def _set_EmergAmps(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 17, value, flags)

    EmergAmps = property(_get_EmergAmps, _set_EmergAmps) # type: float

    def _get_FaultRate(self) -> float:
        """
        Failure rate per year.

        DSS property name: `FaultRate`, DSS property index: 18.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    def _set_FaultRate(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 18, value, flags)

    FaultRate = property(_get_FaultRate, _set_FaultRate) # type: float

    def _get_pctPerm(self) -> float:
        """
        Percent of failures that become permanent.

        DSS property name: `pctPerm`, DSS property index: 19.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    def _set_pctPerm(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 19, value, flags)

    pctPerm = property(_get_pctPerm, _set_pctPerm) # type: float

    def _get_Repair(self) -> float:
        """
        Hours to repair.

        DSS property name: `Repair`, DSS property index: 20.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    def _set_Repair(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 20, value, flags)

    Repair = property(_get_Repair, _set_Repair) # type: float

    def _get_BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 21.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 21, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float

    def _get_Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 22.
        """
        return self._lib.Obj_GetInt32(self._ptr, 22) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 22, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 23.
        """
        self._set_string_o(23, value)


class GICTransformerProperties(TypedDict):
    BusH: AnyStr
    BusNH: AnyStr
    BusX: AnyStr
    BusNX: AnyStr
    Phases: int
    Type: Union[AnyStr, int, enums.GICTransformerType]
    R1: float
    R2: float
    kVLL1: float
    kVLL2: float
    MVA: float
    VarCurve: Union[AnyStr, XYcurve]
    pctR1: float
    pctR2: float
    K: float
    NormAmps: float
    EmergAmps: float
    FaultRate: float
    pctPerm: float
    Repair: float
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class GICTransformerBatch(DSSBatch, CircuitElementBatchMixin, PDElementBatchMixin):
    _cls_name = 'GICTransformer'
    _obj_cls = GICTransformer
    _cls_idx = 45

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)
       PDElementBatchMixin.__init__(self)

    def _get_BusH(self) -> List[str]:
        """
        Name of High-side(H) bus. Examples:
        BusH=busname
        BusH=busname.1.2.3

        DSS property name: `BusH`, DSS property index: 1.
        """
        return self._get_batch_str_prop(1)

    def _set_BusH(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(1, value, flags)

    BusH = property(_get_BusH, _set_BusH) # type: List[str]

    def _get_BusNH(self) -> List[str]:
        """
        Name of Neutral bus for H, or first, winding. Defaults to all phases connected to H-side bus, node 0, if not specified and transformer type is either GSU or YY. (Shunt Wye Connection to ground reference)For Auto, this is automatically set to the X bus.

        DSS property name: `BusNH`, DSS property index: 2.
        """
        return self._get_batch_str_prop(2)

    def _set_BusNH(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(2, value, flags)

    BusNH = property(_get_BusNH, _set_BusNH) # type: List[str]

    def _get_BusX(self) -> List[str]:
        """
        Name of Low-side(X) bus, if type=Auto or YY. 

        DSS property name: `BusX`, DSS property index: 3.
        """
        return self._get_batch_str_prop(3)

    def _set_BusX(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(3, value, flags)

    BusX = property(_get_BusX, _set_BusX) # type: List[str]

    def _get_BusNX(self) -> List[str]:
        """
        Name of Neutral bus for X, or Second, winding. Defaults to all phases connected to X-side bus, node 0, if not specified. (Shunt Wye Connection to ground reference)

        DSS property name: `BusNX`, DSS property index: 4.
        """
        return self._get_batch_str_prop(4)

    def _set_BusNX(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(4, value, flags)

    BusNX = property(_get_BusNX, _set_BusNX) # type: List[str]

    def _get_Phases(self) -> BatchInt32ArrayProxy:
        """
        Number of Phases. Default is 3.

        DSS property name: `Phases`, DSS property index: 5.
        """
        return BatchInt32ArrayProxy(self, 5)

    def _set_Phases(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(5, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: BatchInt32ArrayProxy

    def _get_Type(self) -> BatchInt32ArrayProxy:
        """
        Type of transformer: {GSU* | Auto | YY}. Default is GSU.

        DSS property name: `Type`, DSS property index: 6.
        """
        return BatchInt32ArrayProxy(self, 6)

    def _set_Type(self, value: Union[AnyStr, int, enums.GICTransformerType, List[AnyStr], List[int], List[enums.GICTransformerType], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(6, value, flags)
            return

        self._set_batch_int32_array(6, value, flags)

    Type = property(_get_Type, _set_Type) # type: BatchInt32ArrayProxy

    def _get_Type_str(self) -> List[str]:
        """
        Type of transformer: {GSU* | Auto | YY}. Default is GSU.

        DSS property name: `Type`, DSS property index: 6.
        """
        return self._get_batch_str_prop(6)

    def _set_Type_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Type(value, flags)

    Type_str = property(_get_Type_str, _set_Type_str) # type: List[str]

    def _get_R1(self) -> BatchFloat64ArrayProxy:
        """
        Resistance, each phase, ohms for H winding, (Series winding, if Auto). Default is 0.0001. If 

        DSS property name: `R1`, DSS property index: 7.
        """
        return BatchFloat64ArrayProxy(self, 7)

    def _set_R1(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(7, value, flags)

    R1 = property(_get_R1, _set_R1) # type: BatchFloat64ArrayProxy

    def _get_R2(self) -> BatchFloat64ArrayProxy:
        """
        Resistance, each phase, ohms for X winding, (Common winding, if Auto). Default is 0.0001. 

        DSS property name: `R2`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    def _set_R2(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(8, value, flags)

    R2 = property(_get_R2, _set_R2) # type: BatchFloat64ArrayProxy

    def _get_kVLL1(self) -> BatchFloat64ArrayProxy:
        """
        Optional. kV LL rating for H winding (winding 1). Default is 500. Required if you are going to export vars for power flow analysis or enter winding resistances in percent.

        DSS property name: `kVLL1`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    def _set_kVLL1(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(9, value, flags)

    kVLL1 = property(_get_kVLL1, _set_kVLL1) # type: BatchFloat64ArrayProxy

    def _get_kVLL2(self) -> BatchFloat64ArrayProxy:
        """
        Optional. kV LL rating for X winding (winding 2). Default is 138. Required if you are going to export vars for power flow analysis or enter winding resistances in percent..

        DSS property name: `kVLL2`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    def _set_kVLL2(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(10, value, flags)

    kVLL2 = property(_get_kVLL2, _set_kVLL2) # type: BatchFloat64ArrayProxy

    def _get_MVA(self) -> BatchFloat64ArrayProxy:
        """
        Optional. MVA Rating assumed Transformer. Default is 100. Used for computing vars due to GIC and winding resistances if kV and MVA ratings are specified.

        DSS property name: `MVA`, DSS property index: 11.
        """
        return BatchFloat64ArrayProxy(self, 11)

    def _set_MVA(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(11, value, flags)

    MVA = property(_get_MVA, _set_MVA) # type: BatchFloat64ArrayProxy

    def _get_VarCurve_str(self) -> List[str]:
        """
        Optional. XYCurve object name. Curve is expected as TOTAL pu vars vs pu GIC amps/phase. Vars are in pu of the MVA property. No Default value. Required only if you are going to export vars for power flow analysis. See K property.

        DSS property name: `VarCurve`, DSS property index: 12.
        """
        return self._get_batch_str_prop(12)

    def _set_VarCurve_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(12, value, flags)

    VarCurve_str = property(_get_VarCurve_str, _set_VarCurve_str) # type: List[str]

    def _get_VarCurve(self) -> List[XYcurve]:
        """
        Optional. XYCurve object name. Curve is expected as TOTAL pu vars vs pu GIC amps/phase. Vars are in pu of the MVA property. No Default value. Required only if you are going to export vars for power flow analysis. See K property.

        DSS property name: `VarCurve`, DSS property index: 12.
        """
        return self._get_batch_obj_prop(12)

    def _set_VarCurve(self, value: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(12, value, flags)

    VarCurve = property(_get_VarCurve, _set_VarCurve) # type: List[XYcurve]

    def _get_pctR1(self) -> BatchFloat64ArrayProxy:
        """
        Optional. Percent Resistance, each phase, for H winding (1), (Series winding, if Auto). Default is 0.2. 

        Alternative way to enter R1 value. It is the actual resistances in ohmns that matter. MVA and kV should be specified.

        DSS property name: `%R1`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    def _set_pctR1(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(13, value, flags)

    pctR1 = property(_get_pctR1, _set_pctR1) # type: BatchFloat64ArrayProxy

    def _get_pctR2(self) -> BatchFloat64ArrayProxy:
        """
        Optional. Percent Resistance, each phase, for X winding (2), (Common winding, if Auto). Default is 0.2. 

        Alternative way to enter R2 value. It is the actual resistances in ohms that matter. MVA and kV should be specified.

        DSS property name: `%R2`, DSS property index: 14.
        """
        return BatchFloat64ArrayProxy(self, 14)

    def _set_pctR2(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(14, value, flags)

    pctR2 = property(_get_pctR2, _set_pctR2) # type: BatchFloat64ArrayProxy

    def _get_K(self) -> BatchFloat64ArrayProxy:
        """
        Mvar K factor. Default way to convert GIC Amps in H winding (winding 1) to Mvar. Default is 2.2. Commonly-used simple multiplier for estimating Mvar losses for power flow analysis. 

        Mvar = K * kvLL * GIC per phase / 1000 

        Mutually exclusive with using the VarCurve property and pu curves.If you specify this (default), VarCurve is ignored.

        DSS property name: `K`, DSS property index: 15.
        """
        return BatchFloat64ArrayProxy(self, 15)

    def _set_K(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(15, value, flags)

    K = property(_get_K, _set_K) # type: BatchFloat64ArrayProxy

    def _get_NormAmps(self) -> BatchFloat64ArrayProxy:
        """
        Normal rated current.

        DSS property name: `NormAmps`, DSS property index: 16.
        """
        return BatchFloat64ArrayProxy(self, 16)

    def _set_NormAmps(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(16, value, flags)

    NormAmps = property(_get_NormAmps, _set_NormAmps) # type: BatchFloat64ArrayProxy

    def _get_EmergAmps(self) -> BatchFloat64ArrayProxy:
        """
        Maximum or emerg current.

        DSS property name: `EmergAmps`, DSS property index: 17.
        """
        return BatchFloat64ArrayProxy(self, 17)

    def _set_EmergAmps(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(17, value, flags)

    EmergAmps = property(_get_EmergAmps, _set_EmergAmps) # type: BatchFloat64ArrayProxy

    def _get_FaultRate(self) -> BatchFloat64ArrayProxy:
        """
        Failure rate per year.

        DSS property name: `FaultRate`, DSS property index: 18.
        """
        return BatchFloat64ArrayProxy(self, 18)

    def _set_FaultRate(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(18, value, flags)

    FaultRate = property(_get_FaultRate, _set_FaultRate) # type: BatchFloat64ArrayProxy

    def _get_pctPerm(self) -> BatchFloat64ArrayProxy:
        """
        Percent of failures that become permanent.

        DSS property name: `pctPerm`, DSS property index: 19.
        """
        return BatchFloat64ArrayProxy(self, 19)

    def _set_pctPerm(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(19, value, flags)

    pctPerm = property(_get_pctPerm, _set_pctPerm) # type: BatchFloat64ArrayProxy

    def _get_Repair(self) -> BatchFloat64ArrayProxy:
        """
        Hours to repair.

        DSS property name: `Repair`, DSS property index: 20.
        """
        return BatchFloat64ArrayProxy(self, 20)

    def _set_Repair(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(20, value, flags)

    Repair = property(_get_Repair, _set_Repair) # type: BatchFloat64ArrayProxy

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 21.
        """
        return BatchFloat64ArrayProxy(self, 21)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(21, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy

    def _get_Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 22.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(22)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(22, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 23.
        """
        self._set_batch_string(23, value, flags)

class GICTransformerBatchProperties(TypedDict):
    BusH: Union[AnyStr, List[AnyStr]]
    BusNH: Union[AnyStr, List[AnyStr]]
    BusX: Union[AnyStr, List[AnyStr]]
    BusNX: Union[AnyStr, List[AnyStr]]
    Phases: Union[int, Int32Array]
    Type: Union[AnyStr, int, enums.GICTransformerType, List[AnyStr], List[int], List[enums.GICTransformerType], Int32Array]
    R1: Union[float, Float64Array]
    R2: Union[float, Float64Array]
    kVLL1: Union[float, Float64Array]
    kVLL2: Union[float, Float64Array]
    MVA: Union[float, Float64Array]
    VarCurve: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]
    pctR1: Union[float, Float64Array]
    pctR2: Union[float, Float64Array]
    K: Union[float, Float64Array]
    NormAmps: Union[float, Float64Array]
    EmergAmps: Union[float, Float64Array]
    FaultRate: Union[float, Float64Array]
    pctPerm: Union[float, Float64Array]
    Repair: Union[float, Float64Array]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IGICTransformer(IDSSObj, GICTransformerBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, GICTransformer, GICTransformerBatch)
        GICTransformerBatch.__init__(self, self._api_util, sync_cls_idx=GICTransformer._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> GICTransformer:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[GICTransformerProperties]) -> GICTransformer:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[GICTransformerBatchProperties]) -> GICTransformerBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
