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
from .TransformerExtras import TransformerObjMixin
from .XfmrCode import XfmrCode as XfmrCodeObj

class Transformer(DSSObj, CircuitElementMixin, PDElementMixin, TransformerObjMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots + PDElementMixin._extra_slots + TransformerObjMixin._extra_slots
    _cls_name = 'Transformer'
    _cls_idx = 20
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
        'rneut': 10,
        'xneut': 11,
        'buses': 12,
        'conns': 13,
        'kvs': 14,
        'kvas': 15,
        'taps': 16,
        'xhl': 17,
        'xht': 18,
        'xlt': 19,
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
        'xfmrcode': 39,
        'xrconst': 40,
        'x12': 41,
        'x13': 42,
        'x23': 43,
        'leadlag': 44,
        'wdgcurrents': 45,
        'core': 46,
        'rdcohms': 47,
        'seasons': 48,
        'ratings': 49,
        'normamps': 50,
        'emergamps': 51,
        'faultrate': 52,
        'pctperm': 53,
        'repair': 54,
        'basefreq': 55,
        'enabled': 56,
        'like': 57,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)
       PDElementMixin.__init__(self)
       TransformerObjMixin.__init__(self)

    def _get_Phases(self) -> int:
        """
        Number of phases this transformer. Default is 3.

        DSS property name: `Phases`, DSS property index: 1.
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    def _set_Phases(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 1, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: int

    def _get_Windings(self) -> int:
        """
        Number of windings, this transformers. (Also is the number of terminals) Default is 2. This property triggers memory allocation for the Transformer and will cause other properties to revert to default values.

        DSS property name: `Windings`, DSS property index: 2.
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    def _set_Windings(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 2, value, flags)

    Windings = property(_get_Windings, _set_Windings) # type: int

    def _get_pctR(self) -> Float64Array:
        """
        Percent resistance this winding.  (half of total for a 2-winding).

        DSS property name: `%R`, DSS property index: 9.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 9)

    def _set_pctR(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(9, value, flags)

    pctR = property(_get_pctR, _set_pctR) # type: Float64Array

    def _get_RNeut(self) -> Float64Array:
        """
        Default = -1. Neutral resistance of wye (star)-connected winding in actual ohms. If entered as a negative value, the neutral is assumed to be open, or floating. To solidly ground the neutral, connect the neutral conductor to Node 0 in the Bus property spec for this winding. For example: Bus=MyBusName.1.2.3.0, which is generally the default connection.

        DSS property name: `RNeut`, DSS property index: 10.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 10)

    def _set_RNeut(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(10, value, flags)

    RNeut = property(_get_RNeut, _set_RNeut) # type: Float64Array

    def _get_XNeut(self) -> Float64Array:
        """
        Neutral reactance of wye(star)-connected winding in actual ohms.  May be + or -.

        DSS property name: `XNeut`, DSS property index: 11.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 11)

    def _set_XNeut(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(11, value, flags)

    XNeut = property(_get_XNeut, _set_XNeut) # type: Float64Array

    def _get_Buses(self) -> List[str]:
        """
        Use this to specify all the bus connections at once using an array. Example:

        New Transformer.T1 buses="Hibus, lowbus"

        DSS property name: `Buses`, DSS property index: 12.
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 12)

    def _set_Buses(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 12, value_ptr, value_count, flags)
        self._check_for_error()

    Buses = property(_get_Buses, _set_Buses) # type: List[str]

    def _get_Conns(self) -> List[enums.Connection]:
        """
        Use this to specify all the Winding connections at once using an array. Example:

        New Transformer.T1 buses="Hibus, lowbus" ~ conns=(delta, wye)

        DSS property name: `Conns`, DSS property index: 13.
        """
        return [enums.Connection(val) for val in self._get_int32_list(self._lib.Obj_GetInt32Array, self._ptr, 13)]

    def _set_Conns(self, value: Union[List[Union[int, enums.Connection]], List[AnyStr]], flags: enums.SetterFlags = 0):
        if len(value) and not isinstance(value[0], int):
            self._set_string_array_o(13, value, flags)
            return
        self._set_int32_array_o(13, value, flags)

    Conns = property(_get_Conns, _set_Conns) # type: enums.Connection

    def _get_Conns_str(self) -> List[str]:
        """
        Use this to specify all the Winding connections at once using an array. Example:

        New Transformer.T1 buses="Hibus, lowbus" ~ conns=(delta, wye)

        DSS property name: `Conns`, DSS property index: 13.
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 13)

    def _set_Conns_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Conns(value, flags)

    Conns_str = property(_get_Conns_str, _set_Conns_str) # type: List[str]

    def _get_kVs(self) -> Float64Array:
        """
        Use this to specify the kV ratings of all windings at once using an array. Example:

        New Transformer.T1 buses="Hibus, lowbus" 
        ~ conns=(delta, wye)
        ~ kvs=(115, 12.47)

        See kV= property for voltage rules.

        DSS property name: `kVs`, DSS property index: 14.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 14)

    def _set_kVs(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(14, value, flags)

    kVs = property(_get_kVs, _set_kVs) # type: Float64Array

    def _get_kVAs(self) -> Float64Array:
        """
        Use this to specify the kVA ratings of all windings at once using an array.

        DSS property name: `kVAs`, DSS property index: 15.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 15)

    def _set_kVAs(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(15, value, flags)

    kVAs = property(_get_kVAs, _set_kVAs) # type: Float64Array

    def _get_Taps(self) -> Float64Array:
        """
        Use this to specify the p.u. tap of all windings at once using an array.

        DSS property name: `Taps`, DSS property index: 16.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 16)

    def _set_Taps(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(16, value, flags)

    Taps = property(_get_Taps, _set_Taps) # type: Float64Array

    def _get_XHL(self) -> float:
        """
        Use this to specify the percent reactance, H-L (winding 1 to winding 2).  Use for 2- or 3-winding transformers. On the kVA base of winding 1. See also X12.

        DSS property name: `XHL`, DSS property index: 17.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    def _set_XHL(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 17, value, flags)

    XHL = property(_get_XHL, _set_XHL) # type: float

    def _get_XHT(self) -> float:
        """
        Use this to specify the percent reactance, H-T (winding 1 to winding 3).  Use for 3-winding transformers only. On the kVA base of winding 1. See also X13.

        DSS property name: `XHT`, DSS property index: 18.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    def _set_XHT(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 18, value, flags)

    XHT = property(_get_XHT, _set_XHT) # type: float

    def _get_XLT(self) -> float:
        """
        Use this to specify the percent reactance, L-T (winding 2 to winding 3).  Use for 3-winding transformers only. On the kVA base of winding 1.  See also X23.

        DSS property name: `XLT`, DSS property index: 19.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    def _set_XLT(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 19, value, flags)

    XLT = property(_get_XLT, _set_XLT) # type: float

    def _get_XSCArray(self) -> Float64Array:
        """
        Use this to specify the percent reactance between all pairs of windings as an array. All values are on the kVA base of winding 1.  The order of the values is as follows:

        (x12 13 14... 23 24.. 34 ..)  

        There will be n(n-1)/2 values, where n=number of windings.

        DSS property name: `XSCArray`, DSS property index: 20.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 20)

    def _set_XSCArray(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(20, value, flags)

    XSCArray = property(_get_XSCArray, _set_XSCArray) # type: Float64Array

    def _get_Thermal(self) -> float:
        """
        Thermal time constant of the transformer in hours.  Typically about 2.

        DSS property name: `Thermal`, DSS property index: 21.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    def _set_Thermal(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 21, value, flags)

    Thermal = property(_get_Thermal, _set_Thermal) # type: float

    def _get_n(self) -> float:
        """
        n Exponent for thermal properties in IEEE C57.  Typically 0.8.

        DSS property name: `n`, DSS property index: 22.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    def _set_n(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 22, value, flags)

    n = property(_get_n, _set_n) # type: float

    def _get_m(self) -> float:
        """
        m Exponent for thermal properties in IEEE C57.  Typically 0.9 - 1.0

        DSS property name: `m`, DSS property index: 23.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    def _set_m(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 23, value, flags)

    m = property(_get_m, _set_m) # type: float

    def _get_FLRise(self) -> float:
        """
        Temperature rise, deg C, for full load.  Default is 65.

        DSS property name: `FLRise`, DSS property index: 24.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    def _set_FLRise(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 24, value, flags)

    FLRise = property(_get_FLRise, _set_FLRise) # type: float

    def _get_HSRise(self) -> float:
        """
        Hot spot temperature rise, deg C.  Default is 15.

        DSS property name: `HSRise`, DSS property index: 25.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 25)

    def _set_HSRise(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 25, value, flags)

    HSRise = property(_get_HSRise, _set_HSRise) # type: float

    def _get_pctLoadLoss(self) -> float:
        """
        Percent load loss at full load. The %R of the High and Low windings (1 and 2) are adjusted to agree at rated kVA loading.

        DSS property name: `%LoadLoss`, DSS property index: 26.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 26)

    def _set_pctLoadLoss(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 26, value, flags)

    pctLoadLoss = property(_get_pctLoadLoss, _set_pctLoadLoss) # type: float

    def _get_pctNoLoadLoss(self) -> float:
        """
        Percent no load losses at rated excitatation voltage. Default is 0. Converts to a resistance in parallel with the magnetizing impedance in each winding.

        DSS property name: `%NoLoadLoss`, DSS property index: 27.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 27)

    def _set_pctNoLoadLoss(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 27, value, flags)

    pctNoLoadLoss = property(_get_pctNoLoadLoss, _set_pctNoLoadLoss) # type: float

    def _get_NormHkVA(self) -> float:
        """
        Normal maximum kVA rating of H winding (winding 1).  Usually 100% - 110% of maximum nameplate rating, depending on load shape. Defaults to 110% of kVA rating of Winding 1.

        DSS property name: `NormHkVA`, DSS property index: 28.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 28)

    def _set_NormHkVA(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 28, value, flags)

    NormHkVA = property(_get_NormHkVA, _set_NormHkVA) # type: float

    def _get_EmergHkVA(self) -> float:
        """
        Emergency (contingency)  kVA rating of H winding (winding 1).  Usually 140% - 150% of maximum nameplate rating, depending on load shape. Defaults to 150% of kVA rating of Winding 1.

        DSS property name: `EmergHkVA`, DSS property index: 29.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 29)

    def _set_EmergHkVA(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 29, value, flags)

    EmergHkVA = property(_get_EmergHkVA, _set_EmergHkVA) # type: float

    def _get_Sub(self) -> bool:
        """
        ={Yes|No}  Designates whether this transformer is to be considered a substation.Default is No.

        DSS property name: `Sub`, DSS property index: 30.
        """
        return self._lib.Obj_GetInt32(self._ptr, 30) != 0

    def _set_Sub(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 30, value, flags)

    Sub = property(_get_Sub, _set_Sub) # type: bool

    def _get_MaxTap(self) -> Float64Array:
        """
        Max per unit tap for the active winding.  Default is 1.10

        DSS property name: `MaxTap`, DSS property index: 31.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 31)

    def _set_MaxTap(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(31, value, flags)

    MaxTap = property(_get_MaxTap, _set_MaxTap) # type: Float64Array

    def _get_MinTap(self) -> Float64Array:
        """
        Min per unit tap for the active winding.  Default is 0.90

        DSS property name: `MinTap`, DSS property index: 32.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 32)

    def _set_MinTap(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(32, value, flags)

    MinTap = property(_get_MinTap, _set_MinTap) # type: Float64Array

    def _get_NumTaps(self) -> Int32Array:
        """
        Total number of taps between min and max tap.  Default is 32 (16 raise and 16 lower taps about the neutral position). The neutral position is not counted.

        DSS property name: `NumTaps`, DSS property index: 33.
        """
        return self._get_int32_array(self._lib.Obj_GetInt32Array, self._ptr, 33)

    def _set_NumTaps(self, value: Int32Array, flags: enums.SetterFlags = 0):
        self._set_int32_array_o(33, value, flags)

    NumTaps = property(_get_NumTaps, _set_NumTaps) # type: Int32Array

    def _get_SubName(self) -> str:
        """
        Substation Name. Optional. Default is null. If specified, printed on plots

        DSS property name: `SubName`, DSS property index: 34.
        """
        return self._get_prop_string(34)

    def _set_SubName(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(34, value, flags)

    SubName = property(_get_SubName, _set_SubName) # type: str

    def _get_pctIMag(self) -> float:
        """
        Percent magnetizing current. Default=0.0. Magnetizing branch is in parallel with windings in each phase. Also, see "ppm_antifloat".

        DSS property name: `%IMag`, DSS property index: 35.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 35)

    def _set_pctIMag(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 35, value, flags)

    pctIMag = property(_get_pctIMag, _set_pctIMag) # type: float

    def _get_ppm_Antifloat(self) -> float:
        """
        Default=1 ppm.  Parts per million of transformer winding VA rating connected to ground to protect against accidentally floating a winding without a reference. If positive then the effect is adding a very large reactance to ground.  If negative, then a capacitor.

        DSS property name: `ppm_Antifloat`, DSS property index: 36.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 36)

    def _set_ppm_Antifloat(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 36, value, flags)

    ppm_Antifloat = property(_get_ppm_Antifloat, _set_ppm_Antifloat) # type: float

    def _get_pctRs(self) -> Float64Array:
        """
        Use this property to specify all the winding %resistances using an array. Example:

        New Transformer.T1 buses="Hibus, lowbus" ~ %Rs=(0.2  0.3)

        DSS property name: `%Rs`, DSS property index: 37.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 37)

    def _set_pctRs(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(37, value, flags)

    pctRs = property(_get_pctRs, _set_pctRs) # type: Float64Array

    def _get_Bank(self) -> str:
        """
        Name of the bank this transformer is part of, for CIM, MultiSpeak, and other interfaces.

        DSS property name: `Bank`, DSS property index: 38.
        """
        return self._get_prop_string(38)

    def _set_Bank(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(38, value, flags)

    Bank = property(_get_Bank, _set_Bank) # type: str

    def _get_XfmrCode_str(self) -> str:
        """
        Name of a library entry for transformer properties. The named XfmrCode must already be defined.

        DSS property name: `XfmrCode`, DSS property index: 39.
        """
        return self._get_prop_string(39)

    def _set_XfmrCode_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(39, value, flags)

    XfmrCode_str = property(_get_XfmrCode_str, _set_XfmrCode_str) # type: str

    def _get_XfmrCode(self) -> XfmrCodeObj:
        """
        Name of a library entry for transformer properties. The named XfmrCode must already be defined.

        DSS property name: `XfmrCode`, DSS property index: 39.
        """
        return self._get_obj(39, XfmrCodeObj)

    def _set_XfmrCode(self, value: Union[AnyStr, XfmrCodeObj], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(39, value, flags)
            return

        self._set_string_o(39, value, flags)

    XfmrCode = property(_get_XfmrCode, _set_XfmrCode) # type: XfmrCodeObj

    def _get_XRConst(self) -> bool:
        """
        ={Yes|No} Default is NO. Signifies whether or not the X/R is assumed contant for harmonic studies.

        DSS property name: `XRConst`, DSS property index: 40.
        """
        return self._lib.Obj_GetInt32(self._ptr, 40) != 0

    def _set_XRConst(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 40, value, flags)

    XRConst = property(_get_XRConst, _set_XRConst) # type: bool

    def _get_X12(self) -> float:
        """
        Alternative to XHL for specifying the percent reactance from winding 1 to winding 2.  Use for 2- or 3-winding transformers. Percent on the kVA base of winding 1. 

        DSS property name: `X12`, DSS property index: 41.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 41)

    def _set_X12(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 41, value, flags)

    X12 = property(_get_X12, _set_X12) # type: float

    def _get_X13(self) -> float:
        """
        Alternative to XHT for specifying the percent reactance from winding 1 to winding 3.  Use for 3-winding transformers only. Percent on the kVA base of winding 1. 

        DSS property name: `X13`, DSS property index: 42.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 42)

    def _set_X13(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 42, value, flags)

    X13 = property(_get_X13, _set_X13) # type: float

    def _get_X23(self) -> float:
        """
        Alternative to XLT for specifying the percent reactance from winding 2 to winding 3.Use for 3-winding transformers only. Percent on the kVA base of winding 1.  

        DSS property name: `X23`, DSS property index: 43.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 43)

    def _set_X23(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 43, value, flags)

    X23 = property(_get_X23, _set_X23) # type: float

    def _get_LeadLag(self) -> enums.PhaseSequence:
        """
        {Lead | Lag (default) | ANSI (default) | Euro } Designation in mixed Delta-wye connections the relationship between HV to LV winding. Default is ANSI 30 deg lag, e.g., Dy1 of Yd1 vector group. To get typical European Dy11 connection, specify either "lead" or "Euro"

        DSS property name: `LeadLag`, DSS property index: 44.
        """
        return enums.PhaseSequence(self._lib.Obj_GetInt32(self._ptr, 44))

    def _set_LeadLag(self, value: Union[AnyStr, int, enums.PhaseSequence], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(44, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 44, value, flags)

    LeadLag = property(_get_LeadLag, _set_LeadLag) # type: enums.PhaseSequence

    def _get_LeadLag_str(self) -> str:
        """
        {Lead | Lag (default) | ANSI (default) | Euro } Designation in mixed Delta-wye connections the relationship between HV to LV winding. Default is ANSI 30 deg lag, e.g., Dy1 of Yd1 vector group. To get typical European Dy11 connection, specify either "lead" or "Euro"

        DSS property name: `LeadLag`, DSS property index: 44.
        """
        return self._get_prop_string(44)

    def _set_LeadLag_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_LeadLag(value, flags)

    LeadLag_str = property(_get_LeadLag_str, _set_LeadLag_str) # type: str

    def _get_Core(self) -> enums.CoreType:
        """
        {Shell*|5-leg|3-Leg|1-phase|core-1-phase|4-leg} Core Type. Used for GIC analysis

        DSS property name: `Core`, DSS property index: 46.
        """
        return enums.CoreType(self._lib.Obj_GetInt32(self._ptr, 46))

    def _set_Core(self, value: Union[AnyStr, int, enums.CoreType], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(46, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 46, value, flags)

    Core = property(_get_Core, _set_Core) # type: enums.CoreType

    def _get_Core_str(self) -> str:
        """
        {Shell*|5-leg|3-Leg|1-phase|core-1-phase|4-leg} Core Type. Used for GIC analysis

        DSS property name: `Core`, DSS property index: 46.
        """
        return self._get_prop_string(46)

    def _set_Core_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Core(value, flags)

    Core_str = property(_get_Core_str, _set_Core_str) # type: str

    def _get_RDCOhms(self) -> Float64Array:
        """
        Winding dc resistance in OHMS. Useful for GIC analysis. From transformer test report. Defaults to 85% of %R property

        DSS property name: `RDCOhms`, DSS property index: 47.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 47)

    def _set_RDCOhms(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(47, value, flags)

    RDCOhms = property(_get_RDCOhms, _set_RDCOhms) # type: Float64Array

    def _get_Seasons(self) -> int:
        """
        Defines the number of ratings to be defined for the transfomer, to be used only when defining seasonal ratings using the "Ratings" property.

        DSS property name: `Seasons`, DSS property index: 48.
        """
        return self._lib.Obj_GetInt32(self._ptr, 48)

    def _set_Seasons(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 48, value, flags)

    Seasons = property(_get_Seasons, _set_Seasons) # type: int

    def _get_Ratings(self) -> Float64Array:
        """
        An array of ratings to be used when the seasonal ratings flag is True. It can be used to insert
        multiple ratings to change during a QSTS simulation to evaluate different ratings in transformers. Is given in kVA

        DSS property name: `Ratings`, DSS property index: 49.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 49)

    def _set_Ratings(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(49, value, flags)

    Ratings = property(_get_Ratings, _set_Ratings) # type: Float64Array

    def _get_NormAmps(self) -> float:
        """
        Normal rated current.

        DSS property name: `NormAmps`, DSS property index: 50.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 50)

    def _set_NormAmps(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 50, value, flags)

    NormAmps = property(_get_NormAmps, _set_NormAmps) # type: float

    def _get_EmergAmps(self) -> float:
        """
        Maximum or emerg current.

        DSS property name: `EmergAmps`, DSS property index: 51.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 51)

    def _set_EmergAmps(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 51, value, flags)

    EmergAmps = property(_get_EmergAmps, _set_EmergAmps) # type: float

    def _get_FaultRate(self) -> float:
        """
        Failure rate per year.

        DSS property name: `FaultRate`, DSS property index: 52.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 52)

    def _set_FaultRate(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 52, value, flags)

    FaultRate = property(_get_FaultRate, _set_FaultRate) # type: float

    def _get_pctPerm(self) -> float:
        """
        Percent of failures that become permanent.

        DSS property name: `pctPerm`, DSS property index: 53.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 53)

    def _set_pctPerm(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 53, value, flags)

    pctPerm = property(_get_pctPerm, _set_pctPerm) # type: float

    def _get_Repair(self) -> float:
        """
        Hours to repair.

        DSS property name: `Repair`, DSS property index: 54.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 54)

    def _set_Repair(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 54, value, flags)

    Repair = property(_get_Repair, _set_Repair) # type: float

    def _get_BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 55.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 55)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 55, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float

    def _get_Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 56.
        """
        return self._lib.Obj_GetInt32(self._ptr, 56) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 56, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 57.
        """
        self._set_string_o(57, value)


class TransformerProperties(TypedDict):
    Phases: int
    Windings: int
    pctR: Float64Array
    RNeut: Float64Array
    XNeut: Float64Array
    Buses: List[AnyStr]
    Conns: Union[List[Union[int, enums.Connection]], List[AnyStr]]
    kVs: Float64Array
    kVAs: Float64Array
    Taps: Float64Array
    XHL: float
    XHT: float
    XLT: float
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
    XfmrCode: Union[AnyStr, XfmrCodeObj]
    XRConst: bool
    X12: float
    X13: float
    X23: float
    LeadLag: Union[AnyStr, int, enums.PhaseSequence]
    Core: Union[AnyStr, int, enums.CoreType]
    RDCOhms: Float64Array
    Seasons: int
    Ratings: Float64Array
    NormAmps: float
    EmergAmps: float
    FaultRate: float
    pctPerm: float
    Repair: float
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class TransformerBatch(DSSBatch, CircuitElementBatchMixin, PDElementBatchMixin):
    _cls_name = 'Transformer'
    _obj_cls = Transformer
    _cls_idx = 20

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)
       PDElementBatchMixin.__init__(self)

    def _get_Phases(self) -> BatchInt32ArrayProxy:
        """
        Number of phases this transformer. Default is 3.

        DSS property name: `Phases`, DSS property index: 1.
        """
        return BatchInt32ArrayProxy(self, 1)

    def _set_Phases(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(1, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: BatchInt32ArrayProxy

    def _get_Windings(self) -> BatchInt32ArrayProxy:
        """
        Number of windings, this transformers. (Also is the number of terminals) Default is 2. This property triggers memory allocation for the Transformer and will cause other properties to revert to default values.

        DSS property name: `Windings`, DSS property index: 2.
        """
        return BatchInt32ArrayProxy(self, 2)

    def _set_Windings(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(2, value, flags)

    Windings = property(_get_Windings, _set_Windings) # type: BatchInt32ArrayProxy

    def _get_pctR(self) -> List[Float64Array]:
        """
        Percent resistance this winding.  (half of total for a 2-winding).

        DSS property name: `%R`, DSS property index: 9.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 9)
            for x in self._unpack()
        ]

    def _set_pctR(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(9, value, flags)

    pctR = property(_get_pctR, _set_pctR) # type: List[Float64Array]

    def _get_RNeut(self) -> List[Float64Array]:
        """
        Default = -1. Neutral resistance of wye (star)-connected winding in actual ohms. If entered as a negative value, the neutral is assumed to be open, or floating. To solidly ground the neutral, connect the neutral conductor to Node 0 in the Bus property spec for this winding. For example: Bus=MyBusName.1.2.3.0, which is generally the default connection.

        DSS property name: `RNeut`, DSS property index: 10.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 10)
            for x in self._unpack()
        ]

    def _set_RNeut(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(10, value, flags)

    RNeut = property(_get_RNeut, _set_RNeut) # type: List[Float64Array]

    def _get_XNeut(self) -> List[Float64Array]:
        """
        Neutral reactance of wye(star)-connected winding in actual ohms.  May be + or -.

        DSS property name: `XNeut`, DSS property index: 11.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 11)
            for x in self._unpack()
        ]

    def _set_XNeut(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(11, value, flags)

    XNeut = property(_get_XNeut, _set_XNeut) # type: List[Float64Array]

    def _get_Buses(self) -> List[List[str]]:
        """
        Use this to specify all the bus connections at once using an array. Example:

        New Transformer.T1 buses="Hibus, lowbus"

        DSS property name: `Buses`, DSS property index: 12.
        """
        return self._get_string_ll(12)

    def _set_Buses(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._unpack():
            self._lib.Obj_SetStringArray(x, 12, value_ptr, value_count, flags)

        self._check_for_error()

    Buses = property(_get_Buses, _set_Buses) # type: List[List[str]]

    def _get_Conns(self) -> List[Int32Array]:
        """
        Use this to specify all the Winding connections at once using an array. Example:

        New Transformer.T1 buses="Hibus, lowbus" ~ conns=(delta, wye)

        DSS property name: `Conns`, DSS property index: 13.
        """
        return [
            self._get_int32_array(self._lib.Obj_GetInt32Array, x, 13)
            for x in self._unpack()
        ]

    def _set_Conns(self, value: Union[List[Union[int, enums.Connection]], List[AnyStr]], flags: enums.SetterFlags = 0): #TODO: list of lists
        if len(value) and not isinstance(value[0], int):
            value, value_ptr, value_count = self._prepare_string_array(value)
            for x in self._unpack():
                self._lib.Obj_SetStringArray(x, 13, value_ptr, value_count, flags)

            self._check_for_error()
            return

        self._set_batch_int32_array(13, value, flags)

    Conns = property(_get_Conns, _set_Conns) # type: List[Int32Array]

    def _get_Conns_str(self) -> List[List[str]]:
        """
        Use this to specify all the Winding connections at once using an array. Example:

        New Transformer.T1 buses="Hibus, lowbus" ~ conns=(delta, wye)

        DSS property name: `Conns`, DSS property index: 13.
        """
        return self._get_string_ll(13)

    def _set_Conns_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Conns(value, flags)

    Conns_str = property(_get_Conns_str, _set_Conns_str) # type: List[List[str]]

    def _get_kVs(self) -> List[Float64Array]:
        """
        Use this to specify the kV ratings of all windings at once using an array. Example:

        New Transformer.T1 buses="Hibus, lowbus" 
        ~ conns=(delta, wye)
        ~ kvs=(115, 12.47)

        See kV= property for voltage rules.

        DSS property name: `kVs`, DSS property index: 14.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 14)
            for x in self._unpack()
        ]

    def _set_kVs(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(14, value, flags)

    kVs = property(_get_kVs, _set_kVs) # type: List[Float64Array]

    def _get_kVAs(self) -> List[Float64Array]:
        """
        Use this to specify the kVA ratings of all windings at once using an array.

        DSS property name: `kVAs`, DSS property index: 15.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 15)
            for x in self._unpack()
        ]

    def _set_kVAs(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(15, value, flags)

    kVAs = property(_get_kVAs, _set_kVAs) # type: List[Float64Array]

    def _get_Taps(self) -> List[Float64Array]:
        """
        Use this to specify the p.u. tap of all windings at once using an array.

        DSS property name: `Taps`, DSS property index: 16.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 16)
            for x in self._unpack()
        ]

    def _set_Taps(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(16, value, flags)

    Taps = property(_get_Taps, _set_Taps) # type: List[Float64Array]

    def _get_XHL(self) -> BatchFloat64ArrayProxy:
        """
        Use this to specify the percent reactance, H-L (winding 1 to winding 2).  Use for 2- or 3-winding transformers. On the kVA base of winding 1. See also X12.

        DSS property name: `XHL`, DSS property index: 17.
        """
        return BatchFloat64ArrayProxy(self, 17)

    def _set_XHL(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(17, value, flags)

    XHL = property(_get_XHL, _set_XHL) # type: BatchFloat64ArrayProxy

    def _get_XHT(self) -> BatchFloat64ArrayProxy:
        """
        Use this to specify the percent reactance, H-T (winding 1 to winding 3).  Use for 3-winding transformers only. On the kVA base of winding 1. See also X13.

        DSS property name: `XHT`, DSS property index: 18.
        """
        return BatchFloat64ArrayProxy(self, 18)

    def _set_XHT(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(18, value, flags)

    XHT = property(_get_XHT, _set_XHT) # type: BatchFloat64ArrayProxy

    def _get_XLT(self) -> BatchFloat64ArrayProxy:
        """
        Use this to specify the percent reactance, L-T (winding 2 to winding 3).  Use for 3-winding transformers only. On the kVA base of winding 1.  See also X23.

        DSS property name: `XLT`, DSS property index: 19.
        """
        return BatchFloat64ArrayProxy(self, 19)

    def _set_XLT(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(19, value, flags)

    XLT = property(_get_XLT, _set_XLT) # type: BatchFloat64ArrayProxy

    def _get_XSCArray(self) -> List[Float64Array]:
        """
        Use this to specify the percent reactance between all pairs of windings as an array. All values are on the kVA base of winding 1.  The order of the values is as follows:

        (x12 13 14... 23 24.. 34 ..)  

        There will be n(n-1)/2 values, where n=number of windings.

        DSS property name: `XSCArray`, DSS property index: 20.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 20)
            for x in self._unpack()
        ]

    def _set_XSCArray(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(20, value, flags)

    XSCArray = property(_get_XSCArray, _set_XSCArray) # type: List[Float64Array]

    def _get_Thermal(self) -> BatchFloat64ArrayProxy:
        """
        Thermal time constant of the transformer in hours.  Typically about 2.

        DSS property name: `Thermal`, DSS property index: 21.
        """
        return BatchFloat64ArrayProxy(self, 21)

    def _set_Thermal(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(21, value, flags)

    Thermal = property(_get_Thermal, _set_Thermal) # type: BatchFloat64ArrayProxy

    def _get_n(self) -> BatchFloat64ArrayProxy:
        """
        n Exponent for thermal properties in IEEE C57.  Typically 0.8.

        DSS property name: `n`, DSS property index: 22.
        """
        return BatchFloat64ArrayProxy(self, 22)

    def _set_n(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(22, value, flags)

    n = property(_get_n, _set_n) # type: BatchFloat64ArrayProxy

    def _get_m(self) -> BatchFloat64ArrayProxy:
        """
        m Exponent for thermal properties in IEEE C57.  Typically 0.9 - 1.0

        DSS property name: `m`, DSS property index: 23.
        """
        return BatchFloat64ArrayProxy(self, 23)

    def _set_m(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(23, value, flags)

    m = property(_get_m, _set_m) # type: BatchFloat64ArrayProxy

    def _get_FLRise(self) -> BatchFloat64ArrayProxy:
        """
        Temperature rise, deg C, for full load.  Default is 65.

        DSS property name: `FLRise`, DSS property index: 24.
        """
        return BatchFloat64ArrayProxy(self, 24)

    def _set_FLRise(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(24, value, flags)

    FLRise = property(_get_FLRise, _set_FLRise) # type: BatchFloat64ArrayProxy

    def _get_HSRise(self) -> BatchFloat64ArrayProxy:
        """
        Hot spot temperature rise, deg C.  Default is 15.

        DSS property name: `HSRise`, DSS property index: 25.
        """
        return BatchFloat64ArrayProxy(self, 25)

    def _set_HSRise(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(25, value, flags)

    HSRise = property(_get_HSRise, _set_HSRise) # type: BatchFloat64ArrayProxy

    def _get_pctLoadLoss(self) -> BatchFloat64ArrayProxy:
        """
        Percent load loss at full load. The %R of the High and Low windings (1 and 2) are adjusted to agree at rated kVA loading.

        DSS property name: `%LoadLoss`, DSS property index: 26.
        """
        return BatchFloat64ArrayProxy(self, 26)

    def _set_pctLoadLoss(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(26, value, flags)

    pctLoadLoss = property(_get_pctLoadLoss, _set_pctLoadLoss) # type: BatchFloat64ArrayProxy

    def _get_pctNoLoadLoss(self) -> BatchFloat64ArrayProxy:
        """
        Percent no load losses at rated excitatation voltage. Default is 0. Converts to a resistance in parallel with the magnetizing impedance in each winding.

        DSS property name: `%NoLoadLoss`, DSS property index: 27.
        """
        return BatchFloat64ArrayProxy(self, 27)

    def _set_pctNoLoadLoss(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(27, value, flags)

    pctNoLoadLoss = property(_get_pctNoLoadLoss, _set_pctNoLoadLoss) # type: BatchFloat64ArrayProxy

    def _get_NormHkVA(self) -> BatchFloat64ArrayProxy:
        """
        Normal maximum kVA rating of H winding (winding 1).  Usually 100% - 110% of maximum nameplate rating, depending on load shape. Defaults to 110% of kVA rating of Winding 1.

        DSS property name: `NormHkVA`, DSS property index: 28.
        """
        return BatchFloat64ArrayProxy(self, 28)

    def _set_NormHkVA(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(28, value, flags)

    NormHkVA = property(_get_NormHkVA, _set_NormHkVA) # type: BatchFloat64ArrayProxy

    def _get_EmergHkVA(self) -> BatchFloat64ArrayProxy:
        """
        Emergency (contingency)  kVA rating of H winding (winding 1).  Usually 140% - 150% of maximum nameplate rating, depending on load shape. Defaults to 150% of kVA rating of Winding 1.

        DSS property name: `EmergHkVA`, DSS property index: 29.
        """
        return BatchFloat64ArrayProxy(self, 29)

    def _set_EmergHkVA(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(29, value, flags)

    EmergHkVA = property(_get_EmergHkVA, _set_EmergHkVA) # type: BatchFloat64ArrayProxy

    def _get_Sub(self) -> List[bool]:
        """
        ={Yes|No}  Designates whether this transformer is to be considered a substation.Default is No.

        DSS property name: `Sub`, DSS property index: 30.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(30)
        ]

    def _set_Sub(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(30, value, flags)

    Sub = property(_get_Sub, _set_Sub) # type: List[bool]

    def _get_MaxTap(self) -> List[Float64Array]:
        """
        Max per unit tap for the active winding.  Default is 1.10

        DSS property name: `MaxTap`, DSS property index: 31.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 31)
            for x in self._unpack()
        ]

    def _set_MaxTap(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(31, value, flags)

    MaxTap = property(_get_MaxTap, _set_MaxTap) # type: List[Float64Array]

    def _get_MinTap(self) -> List[Float64Array]:
        """
        Min per unit tap for the active winding.  Default is 0.90

        DSS property name: `MinTap`, DSS property index: 32.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 32)
            for x in self._unpack()
        ]

    def _set_MinTap(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(32, value, flags)

    MinTap = property(_get_MinTap, _set_MinTap) # type: List[Float64Array]

    def _get_NumTaps(self) -> List[Int32Array]:
        """
        Total number of taps between min and max tap.  Default is 32 (16 raise and 16 lower taps about the neutral position). The neutral position is not counted.

        DSS property name: `NumTaps`, DSS property index: 33.
        """
        return [
            self._get_int32_array(self._lib.Obj_GetInt32Array, x, 33)
            for x in self._unpack()
        ]

    def _set_NumTaps(self, value: Union[Int32Array, List[Int32Array]], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array_prop(33, value, flags)

    NumTaps = property(_get_NumTaps, _set_NumTaps) # type: List[Int32Array]

    def _get_SubName(self) -> List[str]:
        """
        Substation Name. Optional. Default is null. If specified, printed on plots

        DSS property name: `SubName`, DSS property index: 34.
        """
        return self._get_batch_str_prop(34)

    def _set_SubName(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(34, value, flags)

    SubName = property(_get_SubName, _set_SubName) # type: List[str]

    def _get_pctIMag(self) -> BatchFloat64ArrayProxy:
        """
        Percent magnetizing current. Default=0.0. Magnetizing branch is in parallel with windings in each phase. Also, see "ppm_antifloat".

        DSS property name: `%IMag`, DSS property index: 35.
        """
        return BatchFloat64ArrayProxy(self, 35)

    def _set_pctIMag(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(35, value, flags)

    pctIMag = property(_get_pctIMag, _set_pctIMag) # type: BatchFloat64ArrayProxy

    def _get_ppm_Antifloat(self) -> BatchFloat64ArrayProxy:
        """
        Default=1 ppm.  Parts per million of transformer winding VA rating connected to ground to protect against accidentally floating a winding without a reference. If positive then the effect is adding a very large reactance to ground.  If negative, then a capacitor.

        DSS property name: `ppm_Antifloat`, DSS property index: 36.
        """
        return BatchFloat64ArrayProxy(self, 36)

    def _set_ppm_Antifloat(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(36, value, flags)

    ppm_Antifloat = property(_get_ppm_Antifloat, _set_ppm_Antifloat) # type: BatchFloat64ArrayProxy

    def _get_pctRs(self) -> List[Float64Array]:
        """
        Use this property to specify all the winding %resistances using an array. Example:

        New Transformer.T1 buses="Hibus, lowbus" ~ %Rs=(0.2  0.3)

        DSS property name: `%Rs`, DSS property index: 37.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 37)
            for x in self._unpack()
        ]

    def _set_pctRs(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(37, value, flags)

    pctRs = property(_get_pctRs, _set_pctRs) # type: List[Float64Array]

    def _get_Bank(self) -> List[str]:
        """
        Name of the bank this transformer is part of, for CIM, MultiSpeak, and other interfaces.

        DSS property name: `Bank`, DSS property index: 38.
        """
        return self._get_batch_str_prop(38)

    def _set_Bank(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(38, value, flags)

    Bank = property(_get_Bank, _set_Bank) # type: List[str]

    def _get_XfmrCode_str(self) -> List[str]:
        """
        Name of a library entry for transformer properties. The named XfmrCode must already be defined.

        DSS property name: `XfmrCode`, DSS property index: 39.
        """
        return self._get_batch_str_prop(39)

    def _set_XfmrCode_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(39, value, flags)

    XfmrCode_str = property(_get_XfmrCode_str, _set_XfmrCode_str) # type: List[str]

    def _get_XfmrCode(self) -> List[XfmrCodeObj]:
        """
        Name of a library entry for transformer properties. The named XfmrCode must already be defined.

        DSS property name: `XfmrCode`, DSS property index: 39.
        """
        return self._get_batch_obj_prop(39)

    def _set_XfmrCode(self, value: Union[AnyStr, XfmrCodeObj, List[AnyStr], List[XfmrCodeObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(39, value, flags)

    XfmrCode = property(_get_XfmrCode, _set_XfmrCode) # type: List[XfmrCodeObj]

    def _get_XRConst(self) -> List[bool]:
        """
        ={Yes|No} Default is NO. Signifies whether or not the X/R is assumed contant for harmonic studies.

        DSS property name: `XRConst`, DSS property index: 40.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(40)
        ]

    def _set_XRConst(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(40, value, flags)

    XRConst = property(_get_XRConst, _set_XRConst) # type: List[bool]

    def _get_X12(self) -> BatchFloat64ArrayProxy:
        """
        Alternative to XHL for specifying the percent reactance from winding 1 to winding 2.  Use for 2- or 3-winding transformers. Percent on the kVA base of winding 1. 

        DSS property name: `X12`, DSS property index: 41.
        """
        return BatchFloat64ArrayProxy(self, 41)

    def _set_X12(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(41, value, flags)

    X12 = property(_get_X12, _set_X12) # type: BatchFloat64ArrayProxy

    def _get_X13(self) -> BatchFloat64ArrayProxy:
        """
        Alternative to XHT for specifying the percent reactance from winding 1 to winding 3.  Use for 3-winding transformers only. Percent on the kVA base of winding 1. 

        DSS property name: `X13`, DSS property index: 42.
        """
        return BatchFloat64ArrayProxy(self, 42)

    def _set_X13(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(42, value, flags)

    X13 = property(_get_X13, _set_X13) # type: BatchFloat64ArrayProxy

    def _get_X23(self) -> BatchFloat64ArrayProxy:
        """
        Alternative to XLT for specifying the percent reactance from winding 2 to winding 3.Use for 3-winding transformers only. Percent on the kVA base of winding 1.  

        DSS property name: `X23`, DSS property index: 43.
        """
        return BatchFloat64ArrayProxy(self, 43)

    def _set_X23(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(43, value, flags)

    X23 = property(_get_X23, _set_X23) # type: BatchFloat64ArrayProxy

    def _get_LeadLag(self) -> BatchInt32ArrayProxy:
        """
        {Lead | Lag (default) | ANSI (default) | Euro } Designation in mixed Delta-wye connections the relationship between HV to LV winding. Default is ANSI 30 deg lag, e.g., Dy1 of Yd1 vector group. To get typical European Dy11 connection, specify either "lead" or "Euro"

        DSS property name: `LeadLag`, DSS property index: 44.
        """
        return BatchInt32ArrayProxy(self, 44)

    def _set_LeadLag(self, value: Union[AnyStr, int, enums.PhaseSequence, List[AnyStr], List[int], List[enums.PhaseSequence], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(44, value, flags)
            return

        self._set_batch_int32_array(44, value, flags)

    LeadLag = property(_get_LeadLag, _set_LeadLag) # type: BatchInt32ArrayProxy

    def _get_LeadLag_str(self) -> List[str]:
        """
        {Lead | Lag (default) | ANSI (default) | Euro } Designation in mixed Delta-wye connections the relationship between HV to LV winding. Default is ANSI 30 deg lag, e.g., Dy1 of Yd1 vector group. To get typical European Dy11 connection, specify either "lead" or "Euro"

        DSS property name: `LeadLag`, DSS property index: 44.
        """
        return self._get_batch_str_prop(44)

    def _set_LeadLag_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_LeadLag(value, flags)

    LeadLag_str = property(_get_LeadLag_str, _set_LeadLag_str) # type: List[str]

    def _get_Core(self) -> BatchInt32ArrayProxy:
        """
        {Shell*|5-leg|3-Leg|1-phase|core-1-phase|4-leg} Core Type. Used for GIC analysis

        DSS property name: `Core`, DSS property index: 46.
        """
        return BatchInt32ArrayProxy(self, 46)

    def _set_Core(self, value: Union[AnyStr, int, enums.CoreType, List[AnyStr], List[int], List[enums.CoreType], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(46, value, flags)
            return

        self._set_batch_int32_array(46, value, flags)

    Core = property(_get_Core, _set_Core) # type: BatchInt32ArrayProxy

    def _get_Core_str(self) -> List[str]:
        """
        {Shell*|5-leg|3-Leg|1-phase|core-1-phase|4-leg} Core Type. Used for GIC analysis

        DSS property name: `Core`, DSS property index: 46.
        """
        return self._get_batch_str_prop(46)

    def _set_Core_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Core(value, flags)

    Core_str = property(_get_Core_str, _set_Core_str) # type: List[str]

    def _get_RDCOhms(self) -> List[Float64Array]:
        """
        Winding dc resistance in OHMS. Useful for GIC analysis. From transformer test report. Defaults to 85% of %R property

        DSS property name: `RDCOhms`, DSS property index: 47.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 47)
            for x in self._unpack()
        ]

    def _set_RDCOhms(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(47, value, flags)

    RDCOhms = property(_get_RDCOhms, _set_RDCOhms) # type: List[Float64Array]

    def _get_Seasons(self) -> BatchInt32ArrayProxy:
        """
        Defines the number of ratings to be defined for the transfomer, to be used only when defining seasonal ratings using the "Ratings" property.

        DSS property name: `Seasons`, DSS property index: 48.
        """
        return BatchInt32ArrayProxy(self, 48)

    def _set_Seasons(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(48, value, flags)

    Seasons = property(_get_Seasons, _set_Seasons) # type: BatchInt32ArrayProxy

    def _get_Ratings(self) -> List[Float64Array]:
        """
        An array of ratings to be used when the seasonal ratings flag is True. It can be used to insert
        multiple ratings to change during a QSTS simulation to evaluate different ratings in transformers. Is given in kVA

        DSS property name: `Ratings`, DSS property index: 49.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 49)
            for x in self._unpack()
        ]

    def _set_Ratings(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(49, value, flags)

    Ratings = property(_get_Ratings, _set_Ratings) # type: List[Float64Array]

    def _get_NormAmps(self) -> BatchFloat64ArrayProxy:
        """
        Normal rated current.

        DSS property name: `NormAmps`, DSS property index: 50.
        """
        return BatchFloat64ArrayProxy(self, 50)

    def _set_NormAmps(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(50, value, flags)

    NormAmps = property(_get_NormAmps, _set_NormAmps) # type: BatchFloat64ArrayProxy

    def _get_EmergAmps(self) -> BatchFloat64ArrayProxy:
        """
        Maximum or emerg current.

        DSS property name: `EmergAmps`, DSS property index: 51.
        """
        return BatchFloat64ArrayProxy(self, 51)

    def _set_EmergAmps(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(51, value, flags)

    EmergAmps = property(_get_EmergAmps, _set_EmergAmps) # type: BatchFloat64ArrayProxy

    def _get_FaultRate(self) -> BatchFloat64ArrayProxy:
        """
        Failure rate per year.

        DSS property name: `FaultRate`, DSS property index: 52.
        """
        return BatchFloat64ArrayProxy(self, 52)

    def _set_FaultRate(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(52, value, flags)

    FaultRate = property(_get_FaultRate, _set_FaultRate) # type: BatchFloat64ArrayProxy

    def _get_pctPerm(self) -> BatchFloat64ArrayProxy:
        """
        Percent of failures that become permanent.

        DSS property name: `pctPerm`, DSS property index: 53.
        """
        return BatchFloat64ArrayProxy(self, 53)

    def _set_pctPerm(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(53, value, flags)

    pctPerm = property(_get_pctPerm, _set_pctPerm) # type: BatchFloat64ArrayProxy

    def _get_Repair(self) -> BatchFloat64ArrayProxy:
        """
        Hours to repair.

        DSS property name: `Repair`, DSS property index: 54.
        """
        return BatchFloat64ArrayProxy(self, 54)

    def _set_Repair(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(54, value, flags)

    Repair = property(_get_Repair, _set_Repair) # type: BatchFloat64ArrayProxy

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 55.
        """
        return BatchFloat64ArrayProxy(self, 55)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(55, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy

    def _get_Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 56.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(56)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(56, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 57.
        """
        self._set_batch_string(57, value, flags)

class TransformerBatchProperties(TypedDict):
    Phases: Union[int, Int32Array]
    Windings: Union[int, Int32Array]
    pctR: Float64Array
    RNeut: Float64Array
    XNeut: Float64Array
    Buses: List[AnyStr]
    Conns: Union[List[Union[int, enums.Connection]], List[AnyStr]]
    kVs: Float64Array
    kVAs: Float64Array
    Taps: Float64Array
    XHL: Union[float, Float64Array]
    XHT: Union[float, Float64Array]
    XLT: Union[float, Float64Array]
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
    XfmrCode: Union[AnyStr, XfmrCodeObj, List[AnyStr], List[XfmrCodeObj]]
    XRConst: bool
    X12: Union[float, Float64Array]
    X13: Union[float, Float64Array]
    X23: Union[float, Float64Array]
    LeadLag: Union[AnyStr, int, enums.PhaseSequence, List[AnyStr], List[int], List[enums.PhaseSequence], Int32Array]
    Core: Union[AnyStr, int, enums.CoreType, List[AnyStr], List[int], List[enums.CoreType], Int32Array]
    RDCOhms: Float64Array
    Seasons: Union[int, Int32Array]
    Ratings: Float64Array
    NormAmps: Union[float, Float64Array]
    EmergAmps: Union[float, Float64Array]
    FaultRate: Union[float, Float64Array]
    pctPerm: Union[float, Float64Array]
    Repair: Union[float, Float64Array]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class ITransformer(IDSSObj, TransformerBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, Transformer, TransformerBatch)
        TransformerBatch.__init__(self, self._api_util, sync_cls_idx=Transformer._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Transformer:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[TransformerProperties]) -> Transformer:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[TransformerBatchProperties]) -> TransformerBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
