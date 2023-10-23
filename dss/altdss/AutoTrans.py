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

class AutoTrans(DSSObj, CktElementMixin, PDElementMixin):
    __slots__ = CktElementMixin._extra_slots + PDElementMixin._extra_slots
    _cls_name = 'AutoTrans'
    _cls_idx = 41
    _cls_prop_idx = {
        'phases': 1,
        'windings': 2,
        'wdg': 3,
        'bus': 4,
        'conn': 5,
        'kv': 6,
        'kva': 7,
        'tap': 8,
        'pctr': 9,
        '%r': 9,
        'rdcohms': 10,
        'core': 11,
        'buses': 12,
        'conns': 13,
        'kvs': 14,
        'kvas': 15,
        'taps': 16,
        'xhx': 17,
        'xht': 18,
        'xxt': 19,
        'xscarray': 20,
        'thermal': 21,
        'n': 22,
        'm': 23,
        'flrise': 24,
        'hsrise': 25,
        'pctloadloss': 26,
        '%loadloss': 26,
        'pctnoloadloss': 27,
        '%noloadloss': 27,
        'normhkva': 28,
        'emerghkva': 29,
        'sub': 30,
        'maxtap': 31,
        'mintap': 32,
        'numtaps': 33,
        'subname': 34,
        'pctimag': 35,
        '%imag': 35,
        'ppm_antifloat': 36,
        'pctrs': 37,
        '%rs': 37,
        'bank': 38,
        'xrconst': 39,
        'leadlag': 40,
        'wdgcurrents': 41,
        'normamps': 42,
        'emergamps': 43,
        'faultrate': 44,
        'pctperm': 45,
        'repair': 46,
        'basefreq': 47,
        'enabled': 48,
        'like': 49,
    }

    @property
    def Phases(self) -> int:
        """
        Number of phases this AutoTrans. Default is 3.

        DSS property name: `Phases`, DSS property index: 1.
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @Phases.setter
    def Phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def Windings(self) -> int:
        """
        Number of windings, this AutoTrans. (Also is the number of terminals) Default is 2. This property triggers memory allocation for the AutoTrans and will cause other properties to revert to default values.

        DSS property name: `Windings`, DSS property index: 2.
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @Windings.setter
    def Windings(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def pctR(self) -> Float64Array:
        """
        Percent ac resistance this winding.  This value is for the power flow model.Is derived from the full load losses in the transformer test report.

        DSS property name: `%R`, DSS property index: 9.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 9)

    @pctR.setter
    def pctR(self, value: Float64Array):
        self._set_float64_array_o(9, value)

    @property
    def RDCOhms(self) -> Float64Array:
        """
        Winding dc resistance in OHMS. Specify this for GIC analysis. From transformer test report (divide by number of phases). Defaults to 85% of %R property (the ac value that includes stray losses).

        DSS property name: `RDCOhms`, DSS property index: 10.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 10)

    @RDCOhms.setter
    def RDCOhms(self, value: Float64Array):
        self._set_float64_array_o(10, value)

    @property
    def Core(self) -> enums.CoreType:
        """
        {Shell*|5-leg|3-Leg|1-phase|core-1-phase|4-leg} Core Type. Used for GIC analysis in auxiliary programs. Not used inside OpenDSS.

        DSS property name: `Core`, DSS property index: 11.
        """
        return enums.CoreType(self._lib.Obj_GetInt32(self._ptr, 11))

    @Core.setter
    def Core(self, value: Union[AnyStr, int, enums.CoreType]):
        if not isinstance(value, int):
            self._set_string_o(11, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 11, value)

    @property
    def Core_str(self) -> str:
        """
        {Shell*|5-leg|3-Leg|1-phase|core-1-phase|4-leg} Core Type. Used for GIC analysis in auxiliary programs. Not used inside OpenDSS.

        DSS property name: `Core`, DSS property index: 11.
        """
        return self._get_prop_string(11)

    @Core_str.setter
    def Core_str(self, value: AnyStr):
        self.Core = value

    @property
    def Buses(self) -> List[str]:
        """
        Use this to specify all the bus connections at once using an array. Example:

        New AutoTrans.T1 buses=[Hbus, Xbus]

        DSS property name: `Buses`, DSS property index: 12.
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 12)

    @Buses.setter
    def Buses(self, value: List[AnyStr]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 12, value_ptr, value_count)
        self._check_for_error()

    @property
    def Conns(self) -> List[enums.AutoTransConnection]:
        """
        Use this to specify all the Winding connections at once using an array. Example:

        New AutoTrans.T1 buses=[Hbus, Xbus] ~ conns=(series, wye)

        DSS property name: `Conns`, DSS property index: 13.
        """
        return [enums.AutoTransConnection(val) for val in self._get_int32_list(self._lib.Obj_GetInt32Array, self._ptr, 13)]

    @Conns.setter
    def Conns(self, value: Union[List[Union[int, enums.AutoTransConnection]], List[AnyStr]]):
        if len(value) and not isinstance(value[0], int):
            self._set_string_array_o(13, value)
            return    
        self._set_int32_array_o(13, value)

    @property
    def Conns_str(self) -> List[str]:
        """
        Use this to specify all the Winding connections at once using an array. Example:

        New AutoTrans.T1 buses=[Hbus, Xbus] ~ conns=(series, wye)

        DSS property name: `Conns`, DSS property index: 13.
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 13)

    @Conns_str.setter
    def Conns_str(self, value: AnyStr):
        self.Conns = value

    @property
    def kVs(self) -> Float64Array:
        """
        Use this to specify the kV ratings of all windings at once using an array. Example:

        New AutoTrans.T1 buses=[Hbus, Xbus] 
        ~ conns=(series, wye)
        ~ kvs=(115, 12.47)

        See kV= property for voltage rules.

        DSS property name: `kVs`, DSS property index: 14.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 14)

    @kVs.setter
    def kVs(self, value: Float64Array):
        self._set_float64_array_o(14, value)

    @property
    def kVAs(self) -> Float64Array:
        """
        Use this to specify the kVA ratings of all windings at once using an array.

        DSS property name: `kVAs`, DSS property index: 15.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 15)

    @kVAs.setter
    def kVAs(self, value: Float64Array):
        self._set_float64_array_o(15, value)

    @property
    def Taps(self) -> Float64Array:
        """
        Use this to specify the p.u. tap of all windings at once using an array.

        DSS property name: `Taps`, DSS property index: 16.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 16)

    @Taps.setter
    def Taps(self, value: Float64Array):
        self._set_float64_array_o(16, value)

    @property
    def XHX(self) -> float:
        """
        Use this to specify the percent reactance, H-L (winding 1 to winding 2).  Use for 2- or 3-winding AutoTranss. On the kVA base of winding 1(H-X). 

        DSS property name: `XHX`, DSS property index: 17.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    @XHX.setter
    def XHX(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 17, value)

    @property
    def XHT(self) -> float:
        """
        Use this to specify the percent reactance, H-T (winding 1 to winding 3).  Use for 3-winding AutoTranss only. On the kVA base of winding 1(H-X). 

        DSS property name: `XHT`, DSS property index: 18.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    @XHT.setter
    def XHT(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 18, value)

    @property
    def XXT(self) -> float:
        """
        Use this to specify the percent reactance, L-T (winding 2 to winding 3).  Use for 3-winding AutoTranss only. On the kVA base of winding 1(H-X).  

        DSS property name: `XXT`, DSS property index: 19.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    @XXT.setter
    def XXT(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 19, value)

    @property
    def XSCArray(self) -> Float64Array:
        """
        Use this to specify the percent reactance between all pairs of windings as an array. All values are on the kVA base of winding 1.  The order of the values is as follows:

        (x12 13 14... 23 24.. 34 ..)  

        There will be n(n-1)/2 values, where n=number of windings.

        DSS property name: `XSCArray`, DSS property index: 20.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 20)

    @XSCArray.setter
    def XSCArray(self, value: Float64Array):
        self._set_float64_array_o(20, value)

    @property
    def Thermal(self) -> float:
        """
        Thermal time constant of the AutoTrans in hours.  Typically about 2.

        DSS property name: `Thermal`, DSS property index: 21.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @Thermal.setter
    def Thermal(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    @property
    def n(self) -> float:
        """
        n Exponent for thermal properties in IEEE C57.  Typically 0.8.

        DSS property name: `n`, DSS property index: 22.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    @n.setter
    def n(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 22, value)

    @property
    def m(self) -> float:
        """
        m Exponent for thermal properties in IEEE C57.  Typically 0.9 - 1.0

        DSS property name: `m`, DSS property index: 23.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    @m.setter
    def m(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 23, value)

    @property
    def FLRise(self) -> float:
        """
        Temperature rise, deg C, for full load.  Default is 65.

        DSS property name: `FLRise`, DSS property index: 24.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    @FLRise.setter
    def FLRise(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 24, value)

    @property
    def HSRise(self) -> float:
        """
        Hot spot temperature rise, deg C.  Default is 15.

        DSS property name: `HSRise`, DSS property index: 25.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 25)

    @HSRise.setter
    def HSRise(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 25, value)

    @property
    def pctLoadLoss(self) -> float:
        """
        Percent load loss at full load. The %R of the High and Low windings (1 and 2) are adjusted to agree at rated kVA loading.

        DSS property name: `%LoadLoss`, DSS property index: 26.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 26)

    @pctLoadLoss.setter
    def pctLoadLoss(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 26, value)

    @property
    def pctNoLoadLoss(self) -> float:
        """
        Percent no load losses at rated excitation voltage. Default is 0. Converts to a resistance in parallel with the magnetizing impedance in each winding.

        DSS property name: `%NoLoadLoss`, DSS property index: 27.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 27)

    @pctNoLoadLoss.setter
    def pctNoLoadLoss(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 27, value)

    @property
    def NormHkVA(self) -> float:
        """
        Normal maximum kVA rating of H winding (winding 1+2).  Usually 100% - 110% of maximum nameplate rating, depending on load shape. Defaults to 110% of kVA rating of Winding 1.

        DSS property name: `NormHkVA`, DSS property index: 28.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 28)

    @NormHkVA.setter
    def NormHkVA(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 28, value)

    @property
    def EmergHkVA(self) -> float:
        """
        Emergency (contingency)  kVA rating of H winding (winding 1+2).  Usually 140% - 150% of maximum nameplate rating, depending on load shape. Defaults to 150% of kVA rating of Winding 1.

        DSS property name: `EmergHkVA`, DSS property index: 29.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 29)

    @EmergHkVA.setter
    def EmergHkVA(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 29, value)

    @property
    def Sub(self) -> bool:
        """
        ={Yes|No}  Designates whether this AutoTrans is to be considered a substation.Default is No.

        DSS property name: `Sub`, DSS property index: 30.
        """
        return self._lib.Obj_GetInt32(self._ptr, 30) != 0

    @Sub.setter
    def Sub(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 30, value)

    @property
    def MaxTap(self) -> Float64Array:
        """
        Max per unit tap for the active winding.  Default is 1.10

        DSS property name: `MaxTap`, DSS property index: 31.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 31)

    @MaxTap.setter
    def MaxTap(self, value: Float64Array):
        self._set_float64_array_o(31, value)

    @property
    def MinTap(self) -> Float64Array:
        """
        Min per unit tap for the active winding.  Default is 0.90

        DSS property name: `MinTap`, DSS property index: 32.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 32)

    @MinTap.setter
    def MinTap(self, value: Float64Array):
        self._set_float64_array_o(32, value)

    @property
    def NumTaps(self) -> Int32Array:
        """
        Total number of taps between min and max tap.  Default is 32 (16 raise and 16 lower taps about the neutral position). The neutral position is not counted.

        DSS property name: `NumTaps`, DSS property index: 33.
        """
        return self._get_int32_array(self._lib.Obj_GetInt32Array, self._ptr, 33)

    @NumTaps.setter
    def NumTaps(self, value: Int32Array):
        self._set_int32_array_o(33, value)

    @property
    def SubName(self) -> str:
        """
        Substation Name. Optional. Default is null. If specified, printed on plots

        DSS property name: `SubName`, DSS property index: 34.
        """
        return self._get_prop_string(34)

    @SubName.setter
    def SubName(self, value: AnyStr):
        self._set_string_o(34, value)

    @property
    def pctIMag(self) -> float:
        """
        Percent magnetizing current. Default=0.0. Magnetizing branch is in parallel with windings in each phase. Also, see "ppm_antifloat".

        DSS property name: `%IMag`, DSS property index: 35.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 35)

    @pctIMag.setter
    def pctIMag(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 35, value)

    @property
    def ppm_Antifloat(self) -> float:
        """
        Default=1 ppm.  Parts per million of AutoTrans winding VA rating connected to ground to protect against accidentally floating a winding without a reference. If positive then the effect is adding a very large reactance to ground.  If negative, then a capacitor.

        DSS property name: `ppm_Antifloat`, DSS property index: 36.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 36)

    @ppm_Antifloat.setter
    def ppm_Antifloat(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 36, value)

    @property
    def pctRs(self) -> Float64Array:
        """
        Use this property to specify all the winding ac %resistances using an array. Example:

        New AutoTrans.T1 buses=[Hibus, lowbus] ~ %Rs=(0.2  0.3)

        DSS property name: `%Rs`, DSS property index: 37.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 37)

    @pctRs.setter
    def pctRs(self, value: Float64Array):
        self._set_float64_array_o(37, value)

    @property
    def Bank(self) -> str:
        """
        Name of the bank this transformer is part of, for CIM, MultiSpeak, and other interfaces.

        DSS property name: `Bank`, DSS property index: 38.
        """
        return self._get_prop_string(38)

    @Bank.setter
    def Bank(self, value: AnyStr):
        self._set_string_o(38, value)

    @property
    def XRConst(self) -> bool:
        """
        ={Yes|No} Default is NO. Signifies whether or not the X/R is assumed constant for harmonic studies.

        DSS property name: `XRConst`, DSS property index: 39.
        """
        return self._lib.Obj_GetInt32(self._ptr, 39) != 0

    @XRConst.setter
    def XRConst(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 39, value)

    @property
    def LeadLag(self) -> enums.PhaseSequence:
        """
        {Lead | Lag (default) | ANSI (default) | Euro } Designation in mixed Delta-wye connections the relationship between HV to LV winding. Default is ANSI 30 deg lag, e.g., Dy1 of Yd1 vector group. To get typical European Dy11 connection, specify either "lead" or "Euro"

        DSS property name: `LeadLag`, DSS property index: 40.
        """
        return enums.PhaseSequence(self._lib.Obj_GetInt32(self._ptr, 40))

    @LeadLag.setter
    def LeadLag(self, value: Union[AnyStr, int, enums.PhaseSequence]):
        if not isinstance(value, int):
            self._set_string_o(40, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 40, value)

    @property
    def LeadLag_str(self) -> str:
        """
        {Lead | Lag (default) | ANSI (default) | Euro } Designation in mixed Delta-wye connections the relationship between HV to LV winding. Default is ANSI 30 deg lag, e.g., Dy1 of Yd1 vector group. To get typical European Dy11 connection, specify either "lead" or "Euro"

        DSS property name: `LeadLag`, DSS property index: 40.
        """
        return self._get_prop_string(40)

    @LeadLag_str.setter
    def LeadLag_str(self, value: AnyStr):
        self.LeadLag = value

    @property
    def NormAmps(self) -> float:
        """
        Normal rated current.

        DSS property name: `NormAmps`, DSS property index: 42.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 42)

    @NormAmps.setter
    def NormAmps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 42, value)

    @property
    def EmergAmps(self) -> float:
        """
        Maximum or emerg current.

        DSS property name: `EmergAmps`, DSS property index: 43.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 43)

    @EmergAmps.setter
    def EmergAmps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 43, value)

    @property
    def FaultRate(self) -> float:
        """
        Failure rate per year.

        DSS property name: `FaultRate`, DSS property index: 44.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 44)

    @FaultRate.setter
    def FaultRate(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 44, value)

    @property
    def pctPerm(self) -> float:
        """
        Percent of failures that become permanent.

        DSS property name: `pctPerm`, DSS property index: 45.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 45)

    @pctPerm.setter
    def pctPerm(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 45, value)

    @property
    def Repair(self) -> float:
        """
        Hours to repair.

        DSS property name: `Repair`, DSS property index: 46.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 46)

    @Repair.setter
    def Repair(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 46, value)

    @property
    def BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 47.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 47)

    @BaseFreq.setter
    def BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 47, value)

    @property
    def Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 48.
        """
        return self._lib.Obj_GetInt32(self._ptr, 48) != 0

    @Enabled.setter
    def Enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 48, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 49.
        """
        self._set_string_o(49, value)


class AutoTransProperties(TypedDict):
    Phases: int
    Windings: int
    pctR: Float64Array
    RDCOhms: Float64Array
    Core: Union[AnyStr, int, enums.CoreType]
    Buses: List[AnyStr]
    Conns: Union[List[Union[int, enums.AutoTransConnection]], List[AnyStr]]
    kVs: Float64Array
    kVAs: Float64Array
    Taps: Float64Array
    XHX: float
    XHT: float
    XXT: float
    XSCArray: Float64Array
    Thermal: float
    n: float
    m: float
    FLRise: float
    HSRise: float
    pctLoadLoss: float
    pctNoLoadLoss: float
    NormHkVA: float
    EmergHkVA: float
    Sub: bool
    MaxTap: Float64Array
    MinTap: Float64Array
    NumTaps: Int32Array
    SubName: AnyStr
    pctIMag: float
    ppm_Antifloat: float
    pctRs: Float64Array
    Bank: AnyStr
    XRConst: bool
    LeadLag: Union[AnyStr, int, enums.PhaseSequence]
    NormAmps: float
    EmergAmps: float
    FaultRate: float
    pctPerm: float
    Repair: float
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class AutoTransBatch(DSSBatch):
    _cls_name = 'AutoTrans'
    _obj_cls = AutoTrans
    _cls_idx = 41


    @property
    def Phases(self) -> BatchInt32ArrayProxy:
        """
        Number of phases this AutoTrans. Default is 3.

        DSS property name: `Phases`, DSS property index: 1.
        """
        return BatchInt32ArrayProxy(self, 1)

    @Phases.setter
    def Phases(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(1, value)

    @property
    def Windings(self) -> BatchInt32ArrayProxy:
        """
        Number of windings, this AutoTrans. (Also is the number of terminals) Default is 2. This property triggers memory allocation for the AutoTrans and will cause other properties to revert to default values.

        DSS property name: `Windings`, DSS property index: 2.
        """
        return BatchInt32ArrayProxy(self, 2)

    @Windings.setter
    def Windings(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(2, value)

    @property
    def pctR(self) -> List[Float64Array]:
        """
        Percent ac resistance this winding.  This value is for the power flow model.Is derived from the full load losses in the transformer test report.

        DSS property name: `%R`, DSS property index: 9.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 9)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @pctR.setter
    def pctR(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(9, value)

    @property
    def RDCOhms(self) -> List[Float64Array]:
        """
        Winding dc resistance in OHMS. Specify this for GIC analysis. From transformer test report (divide by number of phases). Defaults to 85% of %R property (the ac value that includes stray losses).

        DSS property name: `RDCOhms`, DSS property index: 10.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 10)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @RDCOhms.setter
    def RDCOhms(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(10, value)

    @property
    def Core(self) -> BatchInt32ArrayProxy:
        """
        {Shell*|5-leg|3-Leg|1-phase|core-1-phase|4-leg} Core Type. Used for GIC analysis in auxiliary programs. Not used inside OpenDSS.

        DSS property name: `Core`, DSS property index: 11.
        """
        return BatchInt32ArrayProxy(self, 11)

    @Core.setter
    def Core(self, value: Union[AnyStr, int, enums.CoreType, List[AnyStr], List[int], List[enums.CoreType], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(11, value)
            return
    
        self._set_batch_int32_array(11, value)

    @property
    def Core_str(self) -> str:
        """
        {Shell*|5-leg|3-Leg|1-phase|core-1-phase|4-leg} Core Type. Used for GIC analysis in auxiliary programs. Not used inside OpenDSS.

        DSS property name: `Core`, DSS property index: 11.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 11)

    @Core_str.setter
    def Core_str(self, value: AnyStr):
        self.Core = value

    @property
    def Buses(self) -> List[List[str]]:
        """
        Use this to specify all the bus connections at once using an array. Example:

        New AutoTrans.T1 buses=[Hbus, Xbus]

        DSS property name: `Buses`, DSS property index: 12.
        """
        return self._get_string_ll(12)

    @Buses.setter
    def Buses(self, value: List[AnyStr]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._ffi.unpack(self.pointer[0], self.count[0]):
            self._lib.Obj_SetStringArray(x, 12, value_ptr, value_count)
    
        self._check_for_error()

    @property
    def Conns(self) -> List[Int32Array]:
        """
        Use this to specify all the Winding connections at once using an array. Example:

        New AutoTrans.T1 buses=[Hbus, Xbus] ~ conns=(series, wye)

        DSS property name: `Conns`, DSS property index: 13.
        """
        return [
            self._get_int32_array(self._lib.Obj_GetInt32Array, x, 13)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Conns.setter
    def Conns(self, value: Union[List[Union[int, enums.AutoTransConnection]], List[AnyStr]]): #TODO: list of lists
        if len(value) and not isinstance(value[0], int):
            value, value_ptr, value_count = self._prepare_string_array(value)
            for x in self._ffi.unpack(self.pointer[0], self.count[0]):
                self._lib.Obj_SetStringArray(x, 13, value_ptr, value_count)

            self._check_for_error()
            return

        self._set_batch_int32_array(13, value)

    @property
    def Conns_str(self) -> List[List[str]]:
        """
        Use this to specify all the Winding connections at once using an array. Example:

        New AutoTrans.T1 buses=[Hbus, Xbus] ~ conns=(series, wye)

        DSS property name: `Conns`, DSS property index: 13.
        """
        return self._get_string_ll(13)

    @Conns_str.setter
    def Conns_str(self, value: AnyStr):
        self.Conns = value

    @property
    def kVs(self) -> List[Float64Array]:
        """
        Use this to specify the kV ratings of all windings at once using an array. Example:

        New AutoTrans.T1 buses=[Hbus, Xbus] 
        ~ conns=(series, wye)
        ~ kvs=(115, 12.47)

        See kV= property for voltage rules.

        DSS property name: `kVs`, DSS property index: 14.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 14)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @kVs.setter
    def kVs(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(14, value)

    @property
    def kVAs(self) -> List[Float64Array]:
        """
        Use this to specify the kVA ratings of all windings at once using an array.

        DSS property name: `kVAs`, DSS property index: 15.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 15)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @kVAs.setter
    def kVAs(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(15, value)

    @property
    def Taps(self) -> List[Float64Array]:
        """
        Use this to specify the p.u. tap of all windings at once using an array.

        DSS property name: `Taps`, DSS property index: 16.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 16)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Taps.setter
    def Taps(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(16, value)

    @property
    def XHX(self) -> BatchFloat64ArrayProxy:
        """
        Use this to specify the percent reactance, H-L (winding 1 to winding 2).  Use for 2- or 3-winding AutoTranss. On the kVA base of winding 1(H-X). 

        DSS property name: `XHX`, DSS property index: 17.
        """
        return BatchFloat64ArrayProxy(self, 17)

    @XHX.setter
    def XHX(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(17, value)

    @property
    def XHT(self) -> BatchFloat64ArrayProxy:
        """
        Use this to specify the percent reactance, H-T (winding 1 to winding 3).  Use for 3-winding AutoTranss only. On the kVA base of winding 1(H-X). 

        DSS property name: `XHT`, DSS property index: 18.
        """
        return BatchFloat64ArrayProxy(self, 18)

    @XHT.setter
    def XHT(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(18, value)

    @property
    def XXT(self) -> BatchFloat64ArrayProxy:
        """
        Use this to specify the percent reactance, L-T (winding 2 to winding 3).  Use for 3-winding AutoTranss only. On the kVA base of winding 1(H-X).  

        DSS property name: `XXT`, DSS property index: 19.
        """
        return BatchFloat64ArrayProxy(self, 19)

    @XXT.setter
    def XXT(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(19, value)

    @property
    def XSCArray(self) -> List[Float64Array]:
        """
        Use this to specify the percent reactance between all pairs of windings as an array. All values are on the kVA base of winding 1.  The order of the values is as follows:

        (x12 13 14... 23 24.. 34 ..)  

        There will be n(n-1)/2 values, where n=number of windings.

        DSS property name: `XSCArray`, DSS property index: 20.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 20)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @XSCArray.setter
    def XSCArray(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(20, value)

    @property
    def Thermal(self) -> BatchFloat64ArrayProxy:
        """
        Thermal time constant of the AutoTrans in hours.  Typically about 2.

        DSS property name: `Thermal`, DSS property index: 21.
        """
        return BatchFloat64ArrayProxy(self, 21)

    @Thermal.setter
    def Thermal(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(21, value)

    @property
    def n(self) -> BatchFloat64ArrayProxy:
        """
        n Exponent for thermal properties in IEEE C57.  Typically 0.8.

        DSS property name: `n`, DSS property index: 22.
        """
        return BatchFloat64ArrayProxy(self, 22)

    @n.setter
    def n(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(22, value)

    @property
    def m(self) -> BatchFloat64ArrayProxy:
        """
        m Exponent for thermal properties in IEEE C57.  Typically 0.9 - 1.0

        DSS property name: `m`, DSS property index: 23.
        """
        return BatchFloat64ArrayProxy(self, 23)

    @m.setter
    def m(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(23, value)

    @property
    def FLRise(self) -> BatchFloat64ArrayProxy:
        """
        Temperature rise, deg C, for full load.  Default is 65.

        DSS property name: `FLRise`, DSS property index: 24.
        """
        return BatchFloat64ArrayProxy(self, 24)

    @FLRise.setter
    def FLRise(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(24, value)

    @property
    def HSRise(self) -> BatchFloat64ArrayProxy:
        """
        Hot spot temperature rise, deg C.  Default is 15.

        DSS property name: `HSRise`, DSS property index: 25.
        """
        return BatchFloat64ArrayProxy(self, 25)

    @HSRise.setter
    def HSRise(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(25, value)

    @property
    def pctLoadLoss(self) -> BatchFloat64ArrayProxy:
        """
        Percent load loss at full load. The %R of the High and Low windings (1 and 2) are adjusted to agree at rated kVA loading.

        DSS property name: `%LoadLoss`, DSS property index: 26.
        """
        return BatchFloat64ArrayProxy(self, 26)

    @pctLoadLoss.setter
    def pctLoadLoss(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(26, value)

    @property
    def pctNoLoadLoss(self) -> BatchFloat64ArrayProxy:
        """
        Percent no load losses at rated excitation voltage. Default is 0. Converts to a resistance in parallel with the magnetizing impedance in each winding.

        DSS property name: `%NoLoadLoss`, DSS property index: 27.
        """
        return BatchFloat64ArrayProxy(self, 27)

    @pctNoLoadLoss.setter
    def pctNoLoadLoss(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(27, value)

    @property
    def NormHkVA(self) -> BatchFloat64ArrayProxy:
        """
        Normal maximum kVA rating of H winding (winding 1+2).  Usually 100% - 110% of maximum nameplate rating, depending on load shape. Defaults to 110% of kVA rating of Winding 1.

        DSS property name: `NormHkVA`, DSS property index: 28.
        """
        return BatchFloat64ArrayProxy(self, 28)

    @NormHkVA.setter
    def NormHkVA(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(28, value)

    @property
    def EmergHkVA(self) -> BatchFloat64ArrayProxy:
        """
        Emergency (contingency)  kVA rating of H winding (winding 1+2).  Usually 140% - 150% of maximum nameplate rating, depending on load shape. Defaults to 150% of kVA rating of Winding 1.

        DSS property name: `EmergHkVA`, DSS property index: 29.
        """
        return BatchFloat64ArrayProxy(self, 29)

    @EmergHkVA.setter
    def EmergHkVA(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(29, value)

    @property
    def Sub(self) -> List[bool]:
        """
        ={Yes|No}  Designates whether this AutoTrans is to be considered a substation.Default is No.

        DSS property name: `Sub`, DSS property index: 30.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 30)
        ]
    @Sub.setter
    def Sub(self, value: bool):
        self._set_batch_int32_array(30, value)

    @property
    def MaxTap(self) -> List[Float64Array]:
        """
        Max per unit tap for the active winding.  Default is 1.10

        DSS property name: `MaxTap`, DSS property index: 31.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 31)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @MaxTap.setter
    def MaxTap(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(31, value)

    @property
    def MinTap(self) -> List[Float64Array]:
        """
        Min per unit tap for the active winding.  Default is 0.90

        DSS property name: `MinTap`, DSS property index: 32.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 32)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @MinTap.setter
    def MinTap(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(32, value)

    @property
    def NumTaps(self) -> List[Int32Array]:
        """
        Total number of taps between min and max tap.  Default is 32 (16 raise and 16 lower taps about the neutral position). The neutral position is not counted.

        DSS property name: `NumTaps`, DSS property index: 33.
        """
        return [
            self._get_int32_array(self._lib.Obj_GetInt32Array, x, 33)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @NumTaps.setter
    def NumTaps(self, value: Union[Int32Array, List[Int32Array]]):
        self._set_batch_int32_array_prop(33, value)

    @property
    def SubName(self) -> List[str]:
        """
        Substation Name. Optional. Default is null. If specified, printed on plots

        DSS property name: `SubName`, DSS property index: 34.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 34) 

    @SubName.setter
    def SubName(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(34, value)

    @property
    def pctIMag(self) -> BatchFloat64ArrayProxy:
        """
        Percent magnetizing current. Default=0.0. Magnetizing branch is in parallel with windings in each phase. Also, see "ppm_antifloat".

        DSS property name: `%IMag`, DSS property index: 35.
        """
        return BatchFloat64ArrayProxy(self, 35)

    @pctIMag.setter
    def pctIMag(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(35, value)

    @property
    def ppm_Antifloat(self) -> BatchFloat64ArrayProxy:
        """
        Default=1 ppm.  Parts per million of AutoTrans winding VA rating connected to ground to protect against accidentally floating a winding without a reference. If positive then the effect is adding a very large reactance to ground.  If negative, then a capacitor.

        DSS property name: `ppm_Antifloat`, DSS property index: 36.
        """
        return BatchFloat64ArrayProxy(self, 36)

    @ppm_Antifloat.setter
    def ppm_Antifloat(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(36, value)

    @property
    def pctRs(self) -> List[Float64Array]:
        """
        Use this property to specify all the winding ac %resistances using an array. Example:

        New AutoTrans.T1 buses=[Hibus, lowbus] ~ %Rs=(0.2  0.3)

        DSS property name: `%Rs`, DSS property index: 37.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 37)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @pctRs.setter
    def pctRs(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(37, value)

    @property
    def Bank(self) -> List[str]:
        """
        Name of the bank this transformer is part of, for CIM, MultiSpeak, and other interfaces.

        DSS property name: `Bank`, DSS property index: 38.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 38) 

    @Bank.setter
    def Bank(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(38, value)

    @property
    def XRConst(self) -> List[bool]:
        """
        ={Yes|No} Default is NO. Signifies whether or not the X/R is assumed constant for harmonic studies.

        DSS property name: `XRConst`, DSS property index: 39.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 39)
        ]
    @XRConst.setter
    def XRConst(self, value: bool):
        self._set_batch_int32_array(39, value)

    @property
    def LeadLag(self) -> BatchInt32ArrayProxy:
        """
        {Lead | Lag (default) | ANSI (default) | Euro } Designation in mixed Delta-wye connections the relationship between HV to LV winding. Default is ANSI 30 deg lag, e.g., Dy1 of Yd1 vector group. To get typical European Dy11 connection, specify either "lead" or "Euro"

        DSS property name: `LeadLag`, DSS property index: 40.
        """
        return BatchInt32ArrayProxy(self, 40)

    @LeadLag.setter
    def LeadLag(self, value: Union[AnyStr, int, enums.PhaseSequence, List[AnyStr], List[int], List[enums.PhaseSequence], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(40, value)
            return
    
        self._set_batch_int32_array(40, value)

    @property
    def LeadLag_str(self) -> str:
        """
        {Lead | Lag (default) | ANSI (default) | Euro } Designation in mixed Delta-wye connections the relationship between HV to LV winding. Default is ANSI 30 deg lag, e.g., Dy1 of Yd1 vector group. To get typical European Dy11 connection, specify either "lead" or "Euro"

        DSS property name: `LeadLag`, DSS property index: 40.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 40)

    @LeadLag_str.setter
    def LeadLag_str(self, value: AnyStr):
        self.LeadLag = value

    @property
    def NormAmps(self) -> BatchFloat64ArrayProxy:
        """
        Normal rated current.

        DSS property name: `NormAmps`, DSS property index: 42.
        """
        return BatchFloat64ArrayProxy(self, 42)

    @NormAmps.setter
    def NormAmps(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(42, value)

    @property
    def EmergAmps(self) -> BatchFloat64ArrayProxy:
        """
        Maximum or emerg current.

        DSS property name: `EmergAmps`, DSS property index: 43.
        """
        return BatchFloat64ArrayProxy(self, 43)

    @EmergAmps.setter
    def EmergAmps(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(43, value)

    @property
    def FaultRate(self) -> BatchFloat64ArrayProxy:
        """
        Failure rate per year.

        DSS property name: `FaultRate`, DSS property index: 44.
        """
        return BatchFloat64ArrayProxy(self, 44)

    @FaultRate.setter
    def FaultRate(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(44, value)

    @property
    def pctPerm(self) -> BatchFloat64ArrayProxy:
        """
        Percent of failures that become permanent.

        DSS property name: `pctPerm`, DSS property index: 45.
        """
        return BatchFloat64ArrayProxy(self, 45)

    @pctPerm.setter
    def pctPerm(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(45, value)

    @property
    def Repair(self) -> BatchFloat64ArrayProxy:
        """
        Hours to repair.

        DSS property name: `Repair`, DSS property index: 46.
        """
        return BatchFloat64ArrayProxy(self, 46)

    @Repair.setter
    def Repair(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(46, value)

    @property
    def BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 47.
        """
        return BatchFloat64ArrayProxy(self, 47)

    @BaseFreq.setter
    def BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(47, value)

    @property
    def Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 48.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 48)
        ]
    @Enabled.setter
    def Enabled(self, value: bool):
        self._set_batch_int32_array(48, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 49.
        """
        self._set_batch_string(49, value)

class AutoTransBatchProperties(TypedDict):
    Phases: Union[int, Int32Array]
    Windings: Union[int, Int32Array]
    pctR: Float64Array
    RDCOhms: Float64Array
    Core: Union[AnyStr, int, enums.CoreType, List[AnyStr], List[int], List[enums.CoreType], Int32Array]
    Buses: List[AnyStr]
    Conns: Union[List[Union[int, enums.AutoTransConnection]], List[AnyStr]]
    kVs: Float64Array
    kVAs: Float64Array
    Taps: Float64Array
    XHX: Union[float, Float64Array]
    XHT: Union[float, Float64Array]
    XXT: Union[float, Float64Array]
    XSCArray: Float64Array
    Thermal: Union[float, Float64Array]
    n: Union[float, Float64Array]
    m: Union[float, Float64Array]
    FLRise: Union[float, Float64Array]
    HSRise: Union[float, Float64Array]
    pctLoadLoss: Union[float, Float64Array]
    pctNoLoadLoss: Union[float, Float64Array]
    NormHkVA: Union[float, Float64Array]
    EmergHkVA: Union[float, Float64Array]
    Sub: bool
    MaxTap: Float64Array
    MinTap: Float64Array
    NumTaps: Int32Array
    SubName: Union[AnyStr, List[AnyStr]]
    pctIMag: Union[float, Float64Array]
    ppm_Antifloat: Union[float, Float64Array]
    pctRs: Float64Array
    Bank: Union[AnyStr, List[AnyStr]]
    XRConst: bool
    LeadLag: Union[AnyStr, int, enums.PhaseSequence, List[AnyStr], List[int], List[enums.PhaseSequence], Int32Array]
    NormAmps: Union[float, Float64Array]
    EmergAmps: Union[float, Float64Array]
    FaultRate: Union[float, Float64Array]
    pctPerm: Union[float, Float64Array]
    Repair: Union[float, Float64Array]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IAutoTrans(IDSSObj):
    __slots__ = ()

    def __init__(self, iobj):
        super().__init__(iobj, AutoTrans, AutoTransBatch)

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> AutoTrans:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[AutoTransProperties]) -> AutoTrans:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[AutoTransBatchProperties]) -> AutoTransBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
