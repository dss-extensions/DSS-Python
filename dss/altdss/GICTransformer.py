# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from typing_extensions import TypedDict, Unpack
from ._obj_bases import (
    CktElementMixin,
    PDElementMixin,
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
from .XYcurve import XYcurve

class GICTransformer(DSSObj, CktElementMixin, PDElementMixin):
    __slots__ = CktElementMixin._extra_slots + PDElementMixin._extra_slots
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

    @property
    def BusH(self) -> str:
        """
        Name of High-side(H) bus. Examples:
        BusH=busname
        BusH=busname.1.2.3

        DSS property name: `BusH`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    @BusH.setter
    def BusH(self, value: AnyStr):
        self._set_string_o(1, value)

    @property
    def BusNH(self) -> str:
        """
        Name of Neutral bus for H, or first, winding. Defaults to all phases connected to H-side bus, node 0, if not specified and transformer type is either GSU or YY. (Shunt Wye Connection to ground reference)For Auto, this is automatically set to the X bus.

        DSS property name: `BusNH`, DSS property index: 2.
        """
        return self._get_prop_string(2)

    @BusNH.setter
    def BusNH(self, value: AnyStr):
        self._set_string_o(2, value)

    @property
    def BusX(self) -> str:
        """
        Name of Low-side(X) bus, if type=Auto or YY. 

        DSS property name: `BusX`, DSS property index: 3.
        """
        return self._get_prop_string(3)

    @BusX.setter
    def BusX(self, value: AnyStr):
        self._set_string_o(3, value)

    @property
    def BusNX(self) -> str:
        """
        Name of Neutral bus for X, or Second, winding. Defaults to all phases connected to X-side bus, node 0, if not specified. (Shunt Wye Connection to ground reference)

        DSS property name: `BusNX`, DSS property index: 4.
        """
        return self._get_prop_string(4)

    @BusNX.setter
    def BusNX(self, value: AnyStr):
        self._set_string_o(4, value)

    @property
    def Phases(self) -> int:
        """
        Number of Phases. Default is 3.

        DSS property name: `Phases`, DSS property index: 5.
        """
        return self._lib.Obj_GetInt32(self._ptr, 5)

    @Phases.setter
    def Phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 5, value)

    @property
    def Type(self) -> enums.GICTransformerType:
        """
        Type of transformer: {GSU* | Auto | YY}. Default is GSU.

        DSS property name: `Type`, DSS property index: 6.
        """
        return enums.GICTransformerType(self._lib.Obj_GetInt32(self._ptr, 6))

    @Type.setter
    def Type(self, value: Union[AnyStr, int, enums.GICTransformerType]):
        if not isinstance(value, int):
            self._set_string_o(6, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 6, value)

    @property
    def Type_str(self) -> str:
        """
        Type of transformer: {GSU* | Auto | YY}. Default is GSU.

        DSS property name: `Type`, DSS property index: 6.
        """
        return self._get_prop_string(6)

    @Type_str.setter
    def Type_str(self, value: AnyStr):
        self.Type = value

    @property
    def R1(self) -> float:
        """
        Resistance, each phase, ohms for H winding, (Series winding, if Auto). Default is 0.0001. If 

        DSS property name: `R1`, DSS property index: 7.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @R1.setter
    def R1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def R2(self) -> float:
        """
        Resistance, each phase, ohms for X winding, (Common winding, if Auto). Default is 0.0001. 

        DSS property name: `R2`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @R2.setter
    def R2(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def kVLL1(self) -> float:
        """
        Optional. kV LL rating for H winding (winding 1). Default is 500. Required if you are going to export vars for power flow analysis or enter winding resistances in percent.

        DSS property name: `kVLL1`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @kVLL1.setter
    def kVLL1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def kVLL2(self) -> float:
        """
        Optional. kV LL rating for X winding (winding 2). Default is 138. Required if you are going to export vars for power flow analysis or enter winding resistances in percent..

        DSS property name: `kVLL2`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @kVLL2.setter
    def kVLL2(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def MVA(self) -> float:
        """
        Optional. MVA Rating assumed Transformer. Default is 100. Used for computing vars due to GIC and winding resistances if kV and MVA ratings are specified.

        DSS property name: `MVA`, DSS property index: 11.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @MVA.setter
    def MVA(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def VarCurve(self) -> str:
        """
        Optional. XYCurve object name. Curve is expected as TOTAL pu vars vs pu GIC amps/phase. Vars are in pu of the MVA property. No Default value. Required only if you are going to export vars for power flow analysis. See K property.

        DSS property name: `VarCurve`, DSS property index: 12.
        """
        return self._get_prop_string(12)

    @VarCurve.setter
    def VarCurve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(12, value)
            return

        self._set_string_o(12, value)

    @property
    def VarCurve_obj(self) -> XYcurve:
        """
        Optional. XYCurve object name. Curve is expected as TOTAL pu vars vs pu GIC amps/phase. Vars are in pu of the MVA property. No Default value. Required only if you are going to export vars for power flow analysis. See K property.

        DSS property name: `VarCurve`, DSS property index: 12.
        """
        return self._get_obj(12, XYcurve)

    @VarCurve_obj.setter
    def VarCurve_obj(self, value: XYcurve):
        self._set_obj(12, value)

    @property
    def pctR1(self) -> float:
        """
        Optional. Percent Resistance, each phase, for H winding (1), (Series winding, if Auto). Default is 0.2. 

        Alternative way to enter R1 value. It is the actual resistances in ohmns that matter. MVA and kV should be specified.

        DSS property name: `%R1`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @pctR1.setter
    def pctR1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def pctR2(self) -> float:
        """
        Optional. Percent Resistance, each phase, for X winding (2), (Common winding, if Auto). Default is 0.2. 

        Alternative way to enter R2 value. It is the actual resistances in ohms that matter. MVA and kV should be specified.

        DSS property name: `%R2`, DSS property index: 14.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @pctR2.setter
    def pctR2(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def K(self) -> float:
        """
        Mvar K factor. Default way to convert GIC Amps in H winding (winding 1) to Mvar. Default is 2.2. Commonly-used simple multiplier for estimating Mvar losses for power flow analysis. 

        Mvar = K * kvLL * GIC per phase / 1000 

        Mutually exclusive with using the VarCurve property and pu curves.If you specify this (default), VarCurve is ignored.

        DSS property name: `K`, DSS property index: 15.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @K.setter
    def K(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def NormAmps(self) -> float:
        """
        Normal rated current.

        DSS property name: `NormAmps`, DSS property index: 16.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    @NormAmps.setter
    def NormAmps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 16, value)

    @property
    def EmergAmps(self) -> float:
        """
        Maximum or emerg current.

        DSS property name: `EmergAmps`, DSS property index: 17.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    @EmergAmps.setter
    def EmergAmps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 17, value)

    @property
    def FaultRate(self) -> float:
        """
        Failure rate per year.

        DSS property name: `FaultRate`, DSS property index: 18.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    @FaultRate.setter
    def FaultRate(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 18, value)

    @property
    def pctPerm(self) -> float:
        """
        Percent of failures that become permanent.

        DSS property name: `pctPerm`, DSS property index: 19.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    @pctPerm.setter
    def pctPerm(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 19, value)

    @property
    def Repair(self) -> float:
        """
        Hours to repair.

        DSS property name: `Repair`, DSS property index: 20.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    @Repair.setter
    def Repair(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 20, value)

    @property
    def BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 21.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @BaseFreq.setter
    def BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    @property
    def Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 22.
        """
        return self._lib.Obj_GetInt32(self._ptr, 22) != 0

    @Enabled.setter
    def Enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 22, value)

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

class GICTransformerBatch(DSSBatch):
    _cls_name = 'GICTransformer'
    _obj_cls = GICTransformer
    _cls_idx = 45


    @property
    def BusH(self) -> List[str]:
        """
        Name of High-side(H) bus. Examples:
        BusH=busname
        BusH=busname.1.2.3

        DSS property name: `BusH`, DSS property index: 1.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1) 

    @BusH.setter
    def BusH(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(1, value)

    @property
    def BusNH(self) -> List[str]:
        """
        Name of Neutral bus for H, or first, winding. Defaults to all phases connected to H-side bus, node 0, if not specified and transformer type is either GSU or YY. (Shunt Wye Connection to ground reference)For Auto, this is automatically set to the X bus.

        DSS property name: `BusNH`, DSS property index: 2.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 2) 

    @BusNH.setter
    def BusNH(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(2, value)

    @property
    def BusX(self) -> List[str]:
        """
        Name of Low-side(X) bus, if type=Auto or YY. 

        DSS property name: `BusX`, DSS property index: 3.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 3) 

    @BusX.setter
    def BusX(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(3, value)

    @property
    def BusNX(self) -> List[str]:
        """
        Name of Neutral bus for X, or Second, winding. Defaults to all phases connected to X-side bus, node 0, if not specified. (Shunt Wye Connection to ground reference)

        DSS property name: `BusNX`, DSS property index: 4.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 4) 

    @BusNX.setter
    def BusNX(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(4, value)

    @property
    def Phases(self) -> BatchInt32ArrayProxy:
        """
        Number of Phases. Default is 3.

        DSS property name: `Phases`, DSS property index: 5.
        """
        return BatchInt32ArrayProxy(self, 5)

    @Phases.setter
    def Phases(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(5, value)

    @property
    def Type(self) -> BatchInt32ArrayProxy:
        """
        Type of transformer: {GSU* | Auto | YY}. Default is GSU.

        DSS property name: `Type`, DSS property index: 6.
        """
        return BatchInt32ArrayProxy(self, 6)

    @Type.setter
    def Type(self, value: Union[AnyStr, int, enums.GICTransformerType, List[AnyStr], List[int], List[enums.GICTransformerType], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(6, value)
            return
    
        self._set_batch_int32_array(6, value)

    @property
    def Type_str(self) -> str:
        """
        Type of transformer: {GSU* | Auto | YY}. Default is GSU.

        DSS property name: `Type`, DSS property index: 6.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 6)

    @Type_str.setter
    def Type_str(self, value: AnyStr):
        self.Type = value

    @property
    def R1(self) -> BatchFloat64ArrayProxy:
        """
        Resistance, each phase, ohms for H winding, (Series winding, if Auto). Default is 0.0001. If 

        DSS property name: `R1`, DSS property index: 7.
        """
        return BatchFloat64ArrayProxy(self, 7)

    @R1.setter
    def R1(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(7, value)

    @property
    def R2(self) -> BatchFloat64ArrayProxy:
        """
        Resistance, each phase, ohms for X winding, (Common winding, if Auto). Default is 0.0001. 

        DSS property name: `R2`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    @R2.setter
    def R2(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(8, value)

    @property
    def kVLL1(self) -> BatchFloat64ArrayProxy:
        """
        Optional. kV LL rating for H winding (winding 1). Default is 500. Required if you are going to export vars for power flow analysis or enter winding resistances in percent.

        DSS property name: `kVLL1`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    @kVLL1.setter
    def kVLL1(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(9, value)

    @property
    def kVLL2(self) -> BatchFloat64ArrayProxy:
        """
        Optional. kV LL rating for X winding (winding 2). Default is 138. Required if you are going to export vars for power flow analysis or enter winding resistances in percent..

        DSS property name: `kVLL2`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    @kVLL2.setter
    def kVLL2(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(10, value)

    @property
    def MVA(self) -> BatchFloat64ArrayProxy:
        """
        Optional. MVA Rating assumed Transformer. Default is 100. Used for computing vars due to GIC and winding resistances if kV and MVA ratings are specified.

        DSS property name: `MVA`, DSS property index: 11.
        """
        return BatchFloat64ArrayProxy(self, 11)

    @MVA.setter
    def MVA(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(11, value)

    @property
    def VarCurve(self) -> List[str]:
        """
        Optional. XYCurve object name. Curve is expected as TOTAL pu vars vs pu GIC amps/phase. Vars are in pu of the MVA property. No Default value. Required only if you are going to export vars for power flow analysis. See K property.

        DSS property name: `VarCurve`, DSS property index: 12.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 12)

    @VarCurve.setter
    def VarCurve(self, value: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]):
        self._set_batch_obj_prop(12, value)

    @property
    def VarCurve_obj(self) -> List[XYcurve]:
        """
        Optional. XYCurve object name. Curve is expected as TOTAL pu vars vs pu GIC amps/phase. Vars are in pu of the MVA property. No Default value. Required only if you are going to export vars for power flow analysis. See K property.

        DSS property name: `VarCurve`, DSS property index: 12.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 12)

    @VarCurve_obj.setter
    def VarCurve_obj(self, value: XYcurve):
        self._set_batch_string(12, value)

    @property
    def pctR1(self) -> BatchFloat64ArrayProxy:
        """
        Optional. Percent Resistance, each phase, for H winding (1), (Series winding, if Auto). Default is 0.2. 

        Alternative way to enter R1 value. It is the actual resistances in ohmns that matter. MVA and kV should be specified.

        DSS property name: `%R1`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    @pctR1.setter
    def pctR1(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(13, value)

    @property
    def pctR2(self) -> BatchFloat64ArrayProxy:
        """
        Optional. Percent Resistance, each phase, for X winding (2), (Common winding, if Auto). Default is 0.2. 

        Alternative way to enter R2 value. It is the actual resistances in ohms that matter. MVA and kV should be specified.

        DSS property name: `%R2`, DSS property index: 14.
        """
        return BatchFloat64ArrayProxy(self, 14)

    @pctR2.setter
    def pctR2(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(14, value)

    @property
    def K(self) -> BatchFloat64ArrayProxy:
        """
        Mvar K factor. Default way to convert GIC Amps in H winding (winding 1) to Mvar. Default is 2.2. Commonly-used simple multiplier for estimating Mvar losses for power flow analysis. 

        Mvar = K * kvLL * GIC per phase / 1000 

        Mutually exclusive with using the VarCurve property and pu curves.If you specify this (default), VarCurve is ignored.

        DSS property name: `K`, DSS property index: 15.
        """
        return BatchFloat64ArrayProxy(self, 15)

    @K.setter
    def K(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(15, value)

    @property
    def NormAmps(self) -> BatchFloat64ArrayProxy:
        """
        Normal rated current.

        DSS property name: `NormAmps`, DSS property index: 16.
        """
        return BatchFloat64ArrayProxy(self, 16)

    @NormAmps.setter
    def NormAmps(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(16, value)

    @property
    def EmergAmps(self) -> BatchFloat64ArrayProxy:
        """
        Maximum or emerg current.

        DSS property name: `EmergAmps`, DSS property index: 17.
        """
        return BatchFloat64ArrayProxy(self, 17)

    @EmergAmps.setter
    def EmergAmps(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(17, value)

    @property
    def FaultRate(self) -> BatchFloat64ArrayProxy:
        """
        Failure rate per year.

        DSS property name: `FaultRate`, DSS property index: 18.
        """
        return BatchFloat64ArrayProxy(self, 18)

    @FaultRate.setter
    def FaultRate(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(18, value)

    @property
    def pctPerm(self) -> BatchFloat64ArrayProxy:
        """
        Percent of failures that become permanent.

        DSS property name: `pctPerm`, DSS property index: 19.
        """
        return BatchFloat64ArrayProxy(self, 19)

    @pctPerm.setter
    def pctPerm(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(19, value)

    @property
    def Repair(self) -> BatchFloat64ArrayProxy:
        """
        Hours to repair.

        DSS property name: `Repair`, DSS property index: 20.
        """
        return BatchFloat64ArrayProxy(self, 20)

    @Repair.setter
    def Repair(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(20, value)

    @property
    def BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 21.
        """
        return BatchFloat64ArrayProxy(self, 21)

    @BaseFreq.setter
    def BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(21, value)

    @property
    def Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 22.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 22)
        ]
    @Enabled.setter
    def Enabled(self, value: bool):
        self._set_batch_int32_array(22, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 23.
        """
        self._set_batch_string(23, value)

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

class IGICTransformer(IDSSObj):
    __slots__ = ()

    def __init__(self, iobj):
        super().__init__(iobj, GICTransformer, GICTransformerBatch)

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> GICTransformer:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[GICTransformerProperties]) -> GICTransformer:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[GICTransformerBatchProperties]) -> GICTransformerBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
