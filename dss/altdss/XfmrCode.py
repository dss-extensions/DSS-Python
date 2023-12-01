# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from typing_extensions import TypedDict, Unpack
from .types import Float64Array, Int32Array
from . import enums
from .DSSObj import IDSSObj, DSSObj
from .Batch import DSSBatch
from .ArrayProxy import BatchFloat64ArrayProxy, BatchInt32ArrayProxy

class XfmrCode(DSSObj):
    __slots__ = DSSObj._extra_slots
    _cls_name = 'XfmrCode'
    _cls_idx = 14
    _cls_prop_idx = {
        'phases': 1,
        'windings': 2,
        'wdg': 3,
        'conn': 4,
        'kv': 5,
        'kva': 6,
        'tap': 7,
        'pctr': 8,
        '%r': 8,
        'rneut': 9,
        'xneut': 10,
        'conns': 11,
        'kvs': 12,
        'kvas': 13,
        'taps': 14,
        'xhl': 15,
        'xht': 16,
        'xlt': 17,
        'xscarray': 18,
        'thermal': 19,
        'n': 20,
        'm': 21,
        'flrise': 22,
        'hsrise': 23,
        'pctloadloss': 24,
        '%loadloss': 24,
        'pctnoloadloss': 25,
        '%noloadloss': 25,
        'normhkva': 26,
        'emerghkva': 27,
        'maxtap': 28,
        'mintap': 29,
        'numtaps': 30,
        'pctimag': 31,
        '%imag': 31,
        'ppm_antifloat': 32,
        'pctrs': 33,
        '%rs': 33,
        'x12': 34,
        'x13': 35,
        'x23': 36,
        'rdcohms': 37,
        'seasons': 38,
        'ratings': 39,
        'like': 40,
    }


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

        DSS property name: `%R`, DSS property index: 8.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 8)

    def _set_pctR(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(8, value, flags)

    pctR = property(_get_pctR, _set_pctR) # type: Float64Array

    def _get_RNeut(self) -> Float64Array:
        """
        Default = -1. Neutral resistance of wye (star)-connected winding in actual ohms.If entered as a negative value, the neutral is assumed to be open, or floating.

        DSS property name: `RNeut`, DSS property index: 9.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 9)

    def _set_RNeut(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(9, value, flags)

    RNeut = property(_get_RNeut, _set_RNeut) # type: Float64Array

    def _get_XNeut(self) -> Float64Array:
        """
        Neutral reactance of wye(star)-connected winding in actual ohms.  May be + or -.

        DSS property name: `XNeut`, DSS property index: 10.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 10)

    def _set_XNeut(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(10, value, flags)

    XNeut = property(_get_XNeut, _set_XNeut) # type: Float64Array

    def _get_Conns(self) -> List[enums.Connection]:
        """
        Use this to specify all the Winding connections at once using an array. Example:

        New Transformer.T1 buses="Hibus, lowbus"
        ~ conns=(delta, wye)

        DSS property name: `Conns`, DSS property index: 11.
        """
        return [enums.Connection(val) for val in self._get_int32_list(self._lib.Obj_GetInt32Array, self._ptr, 11)]

    def _set_Conns(self, value: Union[List[Union[int, enums.Connection]], List[AnyStr]], flags: enums.SetterFlags = 0):
        if len(value) and not isinstance(value[0], int):
            self._set_string_array_o(11, value, flags)
            return
        self._set_int32_array_o(11, value, flags)

    Conns = property(_get_Conns, _set_Conns) # type: enums.Connection

    def _get_Conns_str(self) -> List[str]:
        """
        Use this to specify all the Winding connections at once using an array. Example:

        New Transformer.T1 buses="Hibus, lowbus"
        ~ conns=(delta, wye)

        DSS property name: `Conns`, DSS property index: 11.
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 11)

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

        DSS property name: `kVs`, DSS property index: 12.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 12)

    def _set_kVs(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(12, value, flags)

    kVs = property(_get_kVs, _set_kVs) # type: Float64Array

    def _get_kVAs(self) -> Float64Array:
        """
        Use this to specify the kVA ratings of all windings at once using an array.

        DSS property name: `kVAs`, DSS property index: 13.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 13)

    def _set_kVAs(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(13, value, flags)

    kVAs = property(_get_kVAs, _set_kVAs) # type: Float64Array

    def _get_Taps(self) -> Float64Array:
        """
        Use this to specify the normal p.u. tap of all windings at once using an array.

        DSS property name: `Taps`, DSS property index: 14.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 14)

    def _set_Taps(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(14, value, flags)

    Taps = property(_get_Taps, _set_Taps) # type: Float64Array

    def _get_XHL(self) -> float:
        """
        Use this to specify the percent reactance, H-L (winding 1 to winding 2).  Use for 2- or 3-winding transformers. On the kva base of winding 1.

        DSS property name: `XHL`, DSS property index: 15.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    def _set_XHL(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 15, value, flags)

    XHL = property(_get_XHL, _set_XHL) # type: float

    def _get_XHT(self) -> float:
        """
        Use this to specify the percent reactance, H-T (winding 1 to winding 3).  Use for 3-winding transformers only. On the kVA base of winding 1.

        DSS property name: `XHT`, DSS property index: 16.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    def _set_XHT(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 16, value, flags)

    XHT = property(_get_XHT, _set_XHT) # type: float

    def _get_XLT(self) -> float:
        """
        Use this to specify the percent reactance, L-T (winding 2 to winding 3).  Use for 3-winding transformers only. On the kVA base of winding 1.

        DSS property name: `XLT`, DSS property index: 17.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    def _set_XLT(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 17, value, flags)

    XLT = property(_get_XLT, _set_XLT) # type: float

    def _get_XSCArray(self) -> Float64Array:
        """
        Use this to specify the percent reactance between all pairs of windings as an array. All values are on the kVA base of winding 1.  The order of the values is as follows:

        (x12 13 14... 23 24.. 34 ..)  

        There will be n(n-1)/2 values, where n=number of windings.

        DSS property name: `XSCArray`, DSS property index: 18.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 18)

    def _set_XSCArray(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(18, value, flags)

    XSCArray = property(_get_XSCArray, _set_XSCArray) # type: Float64Array

    def _get_Thermal(self) -> float:
        """
        Thermal time constant of the transformer in hours.  Typically about 2.

        DSS property name: `Thermal`, DSS property index: 19.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    def _set_Thermal(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 19, value, flags)

    Thermal = property(_get_Thermal, _set_Thermal) # type: float

    def _get_n(self) -> float:
        """
        n Exponent for thermal properties in IEEE C57.  Typically 0.8.

        DSS property name: `n`, DSS property index: 20.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    def _set_n(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 20, value, flags)

    n = property(_get_n, _set_n) # type: float

    def _get_m(self) -> float:
        """
        m Exponent for thermal properties in IEEE C57.  Typically 0.9 - 1.0

        DSS property name: `m`, DSS property index: 21.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    def _set_m(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 21, value, flags)

    m = property(_get_m, _set_m) # type: float

    def _get_FLRise(self) -> float:
        """
        Temperature rise, deg C, for full load.  Default is 65.

        DSS property name: `FLRise`, DSS property index: 22.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    def _set_FLRise(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 22, value, flags)

    FLRise = property(_get_FLRise, _set_FLRise) # type: float

    def _get_HSRise(self) -> float:
        """
        Hot spot temperature rise, deg C.  Default is 15.

        DSS property name: `HSRise`, DSS property index: 23.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    def _set_HSRise(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 23, value, flags)

    HSRise = property(_get_HSRise, _set_HSRise) # type: float

    def _get_pctLoadLoss(self) -> float:
        """
        Percent load loss at full load. The %R of the High and Low windings (1 and 2) are adjusted to agree at rated kVA loading.

        DSS property name: `%LoadLoss`, DSS property index: 24.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    def _set_pctLoadLoss(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 24, value, flags)

    pctLoadLoss = property(_get_pctLoadLoss, _set_pctLoadLoss) # type: float

    def _get_pctNoLoadLoss(self) -> float:
        """
        Percent no load losses at rated excitation voltage. Default is 0. Converts to a resistance in parallel with the magnetizing impedance in each winding.

        DSS property name: `%NoLoadLoss`, DSS property index: 25.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 25)

    def _set_pctNoLoadLoss(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 25, value, flags)

    pctNoLoadLoss = property(_get_pctNoLoadLoss, _set_pctNoLoadLoss) # type: float

    def _get_NormHkVA(self) -> float:
        """
        Normal maximum kVA rating of H winding (winding 1).  Usually 100% - 110% of maximum nameplate rating, depending on load shape. Defaults to 110% of kVA rating of Winding 1.

        DSS property name: `NormHkVA`, DSS property index: 26.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 26)

    def _set_NormHkVA(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 26, value, flags)

    NormHkVA = property(_get_NormHkVA, _set_NormHkVA) # type: float

    def _get_EmergHkVA(self) -> float:
        """
        Emergency (contingency)  kVA rating of H winding (winding 1).  Usually 140% - 150% of maximum nameplate rating, depending on load shape. Defaults to 150% of kVA rating of Winding 1.

        DSS property name: `EmergHkVA`, DSS property index: 27.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 27)

    def _set_EmergHkVA(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 27, value, flags)

    EmergHkVA = property(_get_EmergHkVA, _set_EmergHkVA) # type: float

    def _get_MaxTap(self) -> Float64Array:
        """
        Max per unit tap for the active winding.  Default is 1.10

        DSS property name: `MaxTap`, DSS property index: 28.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 28)

    def _set_MaxTap(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(28, value, flags)

    MaxTap = property(_get_MaxTap, _set_MaxTap) # type: Float64Array

    def _get_MinTap(self) -> Float64Array:
        """
        Min per unit tap for the active winding.  Default is 0.90

        DSS property name: `MinTap`, DSS property index: 29.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 29)

    def _set_MinTap(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(29, value, flags)

    MinTap = property(_get_MinTap, _set_MinTap) # type: Float64Array

    def _get_NumTaps(self) -> Int32Array:
        """
        Total number of taps between min and max tap.  Default is 32.

        DSS property name: `NumTaps`, DSS property index: 30.
        """
        return self._get_int32_array(self._lib.Obj_GetInt32Array, self._ptr, 30)

    def _set_NumTaps(self, value: Int32Array, flags: enums.SetterFlags = 0):
        self._set_int32_array_o(30, value, flags)

    NumTaps = property(_get_NumTaps, _set_NumTaps) # type: Int32Array

    def _get_pctIMag(self) -> float:
        """
        Percent magnetizing current. Default=0.0. Magnetizing branch is in parallel with windings in each phase. Also, see "ppm_antifloat".

        DSS property name: `%IMag`, DSS property index: 31.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 31)

    def _set_pctIMag(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 31, value, flags)

    pctIMag = property(_get_pctIMag, _set_pctIMag) # type: float

    def _get_ppm_Antifloat(self) -> float:
        """
        Default=1 ppm.  Parts per million of transformer winding VA rating connected to ground to protect against accidentally floating a winding without a reference. If positive then the effect is adding a very large reactance to ground.  If negative, then a capacitor.

        DSS property name: `ppm_Antifloat`, DSS property index: 32.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 32)

    def _set_ppm_Antifloat(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 32, value, flags)

    ppm_Antifloat = property(_get_ppm_Antifloat, _set_ppm_Antifloat) # type: float

    def _get_pctRs(self) -> Float64Array:
        """
        Use this property to specify all the winding %resistances using an array. Example:

        New Transformer.T1 buses="Hibus, lowbus" ~ %Rs=(0.2  0.3)

        DSS property name: `%Rs`, DSS property index: 33.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 33)

    def _set_pctRs(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(33, value, flags)

    pctRs = property(_get_pctRs, _set_pctRs) # type: Float64Array

    def _get_X12(self) -> float:
        """
        Alternative to XHL for specifying the percent reactance from winding 1 to winding 2.  Use for 2- or 3-winding transformers. Percent on the kVA base of winding 1. 

        DSS property name: `X12`, DSS property index: 34.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 34)

    def _set_X12(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 34, value, flags)

    X12 = property(_get_X12, _set_X12) # type: float

    def _get_X13(self) -> float:
        """
        Alternative to XHT for specifying the percent reactance from winding 1 to winding 3.  Use for 3-winding transformers only. Percent on the kVA base of winding 1. 

        DSS property name: `X13`, DSS property index: 35.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 35)

    def _set_X13(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 35, value, flags)

    X13 = property(_get_X13, _set_X13) # type: float

    def _get_X23(self) -> float:
        """
        Alternative to XLT for specifying the percent reactance from winding 2 to winding 3.Use for 3-winding transformers only. Percent on the kVA base of winding 1.  

        DSS property name: `X23`, DSS property index: 36.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 36)

    def _set_X23(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 36, value, flags)

    X23 = property(_get_X23, _set_X23) # type: float

    def _get_RDCOhms(self) -> Float64Array:
        """
        Winding dc resistance in OHMS. Useful for GIC analysis. From transformer test report. Defaults to 85% of %R property

        DSS property name: `RDCOhms`, DSS property index: 37.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 37)

    def _set_RDCOhms(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(37, value, flags)

    RDCOhms = property(_get_RDCOhms, _set_RDCOhms) # type: Float64Array

    def _get_Seasons(self) -> int:
        """
        Defines the number of ratings to be defined for the transfomer, to be used only when defining seasonal ratings using the "Ratings" property.

        DSS property name: `Seasons`, DSS property index: 38.
        """
        return self._lib.Obj_GetInt32(self._ptr, 38)

    def _set_Seasons(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 38, value, flags)

    Seasons = property(_get_Seasons, _set_Seasons) # type: int

    def _get_Ratings(self) -> Float64Array:
        """
        An array of ratings to be used when the seasonal ratings flag is True. It can be used to insert
        multiple ratings to change during a QSTS simulation to evaluate different ratings in transformers.

        DSS property name: `Ratings`, DSS property index: 39.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 39)

    def _set_Ratings(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(39, value, flags)

    Ratings = property(_get_Ratings, _set_Ratings) # type: Float64Array

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 40.
        """
        self._set_string_o(40, value)


class XfmrCodeProperties(TypedDict):
    Phases: int
    Windings: int
    pctR: Float64Array
    RNeut: Float64Array
    XNeut: Float64Array
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
    MaxTap: Float64Array
    MinTap: Float64Array
    NumTaps: Int32Array
    pctIMag: float
    ppm_Antifloat: float
    pctRs: Float64Array
    X12: float
    X13: float
    X23: float
    RDCOhms: Float64Array
    Seasons: int
    Ratings: Float64Array
    Like: AnyStr

class XfmrCodeBatch(DSSBatch):
    _cls_name = 'XfmrCode'
    _obj_cls = XfmrCode
    _cls_idx = 14


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

        DSS property name: `%R`, DSS property index: 8.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 8)
            for x in self._unpack()
        ]

    def _set_pctR(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(8, value, flags)

    pctR = property(_get_pctR, _set_pctR) # type: List[Float64Array]

    def _get_RNeut(self) -> List[Float64Array]:
        """
        Default = -1. Neutral resistance of wye (star)-connected winding in actual ohms.If entered as a negative value, the neutral is assumed to be open, or floating.

        DSS property name: `RNeut`, DSS property index: 9.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 9)
            for x in self._unpack()
        ]

    def _set_RNeut(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(9, value, flags)

    RNeut = property(_get_RNeut, _set_RNeut) # type: List[Float64Array]

    def _get_XNeut(self) -> List[Float64Array]:
        """
        Neutral reactance of wye(star)-connected winding in actual ohms.  May be + or -.

        DSS property name: `XNeut`, DSS property index: 10.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 10)
            for x in self._unpack()
        ]

    def _set_XNeut(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(10, value, flags)

    XNeut = property(_get_XNeut, _set_XNeut) # type: List[Float64Array]

    def _get_Conns(self) -> List[Int32Array]:
        """
        Use this to specify all the Winding connections at once using an array. Example:

        New Transformer.T1 buses="Hibus, lowbus"
        ~ conns=(delta, wye)

        DSS property name: `Conns`, DSS property index: 11.
        """
        return [
            self._get_int32_array(self._lib.Obj_GetInt32Array, x, 11)
            for x in self._unpack()
        ]

    def _set_Conns(self, value: Union[List[Union[int, enums.Connection]], List[AnyStr]], flags: enums.SetterFlags = 0): #TODO: list of lists
        if len(value) and not isinstance(value[0], int):
            value, value_ptr, value_count = self._prepare_string_array(value)
            for x in self._unpack():
                self._lib.Obj_SetStringArray(x, 11, value_ptr, value_count, flags)

            self._check_for_error()
            return

        self._set_batch_int32_array(11, value, flags)

    Conns = property(_get_Conns, _set_Conns) # type: List[Int32Array]

    def _get_Conns_str(self) -> List[List[str]]:
        """
        Use this to specify all the Winding connections at once using an array. Example:

        New Transformer.T1 buses="Hibus, lowbus"
        ~ conns=(delta, wye)

        DSS property name: `Conns`, DSS property index: 11.
        """
        return self._get_string_ll(11)

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

        DSS property name: `kVs`, DSS property index: 12.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 12)
            for x in self._unpack()
        ]

    def _set_kVs(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(12, value, flags)

    kVs = property(_get_kVs, _set_kVs) # type: List[Float64Array]

    def _get_kVAs(self) -> List[Float64Array]:
        """
        Use this to specify the kVA ratings of all windings at once using an array.

        DSS property name: `kVAs`, DSS property index: 13.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 13)
            for x in self._unpack()
        ]

    def _set_kVAs(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(13, value, flags)

    kVAs = property(_get_kVAs, _set_kVAs) # type: List[Float64Array]

    def _get_Taps(self) -> List[Float64Array]:
        """
        Use this to specify the normal p.u. tap of all windings at once using an array.

        DSS property name: `Taps`, DSS property index: 14.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 14)
            for x in self._unpack()
        ]

    def _set_Taps(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(14, value, flags)

    Taps = property(_get_Taps, _set_Taps) # type: List[Float64Array]

    def _get_XHL(self) -> BatchFloat64ArrayProxy:
        """
        Use this to specify the percent reactance, H-L (winding 1 to winding 2).  Use for 2- or 3-winding transformers. On the kva base of winding 1.

        DSS property name: `XHL`, DSS property index: 15.
        """
        return BatchFloat64ArrayProxy(self, 15)

    def _set_XHL(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(15, value, flags)

    XHL = property(_get_XHL, _set_XHL) # type: BatchFloat64ArrayProxy

    def _get_XHT(self) -> BatchFloat64ArrayProxy:
        """
        Use this to specify the percent reactance, H-T (winding 1 to winding 3).  Use for 3-winding transformers only. On the kVA base of winding 1.

        DSS property name: `XHT`, DSS property index: 16.
        """
        return BatchFloat64ArrayProxy(self, 16)

    def _set_XHT(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(16, value, flags)

    XHT = property(_get_XHT, _set_XHT) # type: BatchFloat64ArrayProxy

    def _get_XLT(self) -> BatchFloat64ArrayProxy:
        """
        Use this to specify the percent reactance, L-T (winding 2 to winding 3).  Use for 3-winding transformers only. On the kVA base of winding 1.

        DSS property name: `XLT`, DSS property index: 17.
        """
        return BatchFloat64ArrayProxy(self, 17)

    def _set_XLT(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(17, value, flags)

    XLT = property(_get_XLT, _set_XLT) # type: BatchFloat64ArrayProxy

    def _get_XSCArray(self) -> List[Float64Array]:
        """
        Use this to specify the percent reactance between all pairs of windings as an array. All values are on the kVA base of winding 1.  The order of the values is as follows:

        (x12 13 14... 23 24.. 34 ..)  

        There will be n(n-1)/2 values, where n=number of windings.

        DSS property name: `XSCArray`, DSS property index: 18.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 18)
            for x in self._unpack()
        ]

    def _set_XSCArray(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(18, value, flags)

    XSCArray = property(_get_XSCArray, _set_XSCArray) # type: List[Float64Array]

    def _get_Thermal(self) -> BatchFloat64ArrayProxy:
        """
        Thermal time constant of the transformer in hours.  Typically about 2.

        DSS property name: `Thermal`, DSS property index: 19.
        """
        return BatchFloat64ArrayProxy(self, 19)

    def _set_Thermal(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(19, value, flags)

    Thermal = property(_get_Thermal, _set_Thermal) # type: BatchFloat64ArrayProxy

    def _get_n(self) -> BatchFloat64ArrayProxy:
        """
        n Exponent for thermal properties in IEEE C57.  Typically 0.8.

        DSS property name: `n`, DSS property index: 20.
        """
        return BatchFloat64ArrayProxy(self, 20)

    def _set_n(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(20, value, flags)

    n = property(_get_n, _set_n) # type: BatchFloat64ArrayProxy

    def _get_m(self) -> BatchFloat64ArrayProxy:
        """
        m Exponent for thermal properties in IEEE C57.  Typically 0.9 - 1.0

        DSS property name: `m`, DSS property index: 21.
        """
        return BatchFloat64ArrayProxy(self, 21)

    def _set_m(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(21, value, flags)

    m = property(_get_m, _set_m) # type: BatchFloat64ArrayProxy

    def _get_FLRise(self) -> BatchFloat64ArrayProxy:
        """
        Temperature rise, deg C, for full load.  Default is 65.

        DSS property name: `FLRise`, DSS property index: 22.
        """
        return BatchFloat64ArrayProxy(self, 22)

    def _set_FLRise(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(22, value, flags)

    FLRise = property(_get_FLRise, _set_FLRise) # type: BatchFloat64ArrayProxy

    def _get_HSRise(self) -> BatchFloat64ArrayProxy:
        """
        Hot spot temperature rise, deg C.  Default is 15.

        DSS property name: `HSRise`, DSS property index: 23.
        """
        return BatchFloat64ArrayProxy(self, 23)

    def _set_HSRise(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(23, value, flags)

    HSRise = property(_get_HSRise, _set_HSRise) # type: BatchFloat64ArrayProxy

    def _get_pctLoadLoss(self) -> BatchFloat64ArrayProxy:
        """
        Percent load loss at full load. The %R of the High and Low windings (1 and 2) are adjusted to agree at rated kVA loading.

        DSS property name: `%LoadLoss`, DSS property index: 24.
        """
        return BatchFloat64ArrayProxy(self, 24)

    def _set_pctLoadLoss(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(24, value, flags)

    pctLoadLoss = property(_get_pctLoadLoss, _set_pctLoadLoss) # type: BatchFloat64ArrayProxy

    def _get_pctNoLoadLoss(self) -> BatchFloat64ArrayProxy:
        """
        Percent no load losses at rated excitation voltage. Default is 0. Converts to a resistance in parallel with the magnetizing impedance in each winding.

        DSS property name: `%NoLoadLoss`, DSS property index: 25.
        """
        return BatchFloat64ArrayProxy(self, 25)

    def _set_pctNoLoadLoss(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(25, value, flags)

    pctNoLoadLoss = property(_get_pctNoLoadLoss, _set_pctNoLoadLoss) # type: BatchFloat64ArrayProxy

    def _get_NormHkVA(self) -> BatchFloat64ArrayProxy:
        """
        Normal maximum kVA rating of H winding (winding 1).  Usually 100% - 110% of maximum nameplate rating, depending on load shape. Defaults to 110% of kVA rating of Winding 1.

        DSS property name: `NormHkVA`, DSS property index: 26.
        """
        return BatchFloat64ArrayProxy(self, 26)

    def _set_NormHkVA(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(26, value, flags)

    NormHkVA = property(_get_NormHkVA, _set_NormHkVA) # type: BatchFloat64ArrayProxy

    def _get_EmergHkVA(self) -> BatchFloat64ArrayProxy:
        """
        Emergency (contingency)  kVA rating of H winding (winding 1).  Usually 140% - 150% of maximum nameplate rating, depending on load shape. Defaults to 150% of kVA rating of Winding 1.

        DSS property name: `EmergHkVA`, DSS property index: 27.
        """
        return BatchFloat64ArrayProxy(self, 27)

    def _set_EmergHkVA(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(27, value, flags)

    EmergHkVA = property(_get_EmergHkVA, _set_EmergHkVA) # type: BatchFloat64ArrayProxy

    def _get_MaxTap(self) -> List[Float64Array]:
        """
        Max per unit tap for the active winding.  Default is 1.10

        DSS property name: `MaxTap`, DSS property index: 28.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 28)
            for x in self._unpack()
        ]

    def _set_MaxTap(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(28, value, flags)

    MaxTap = property(_get_MaxTap, _set_MaxTap) # type: List[Float64Array]

    def _get_MinTap(self) -> List[Float64Array]:
        """
        Min per unit tap for the active winding.  Default is 0.90

        DSS property name: `MinTap`, DSS property index: 29.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 29)
            for x in self._unpack()
        ]

    def _set_MinTap(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(29, value, flags)

    MinTap = property(_get_MinTap, _set_MinTap) # type: List[Float64Array]

    def _get_NumTaps(self) -> List[Int32Array]:
        """
        Total number of taps between min and max tap.  Default is 32.

        DSS property name: `NumTaps`, DSS property index: 30.
        """
        return [
            self._get_int32_array(self._lib.Obj_GetInt32Array, x, 30)
            for x in self._unpack()
        ]

    def _set_NumTaps(self, value: Union[Int32Array, List[Int32Array]], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array_prop(30, value, flags)

    NumTaps = property(_get_NumTaps, _set_NumTaps) # type: List[Int32Array]

    def _get_pctIMag(self) -> BatchFloat64ArrayProxy:
        """
        Percent magnetizing current. Default=0.0. Magnetizing branch is in parallel with windings in each phase. Also, see "ppm_antifloat".

        DSS property name: `%IMag`, DSS property index: 31.
        """
        return BatchFloat64ArrayProxy(self, 31)

    def _set_pctIMag(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(31, value, flags)

    pctIMag = property(_get_pctIMag, _set_pctIMag) # type: BatchFloat64ArrayProxy

    def _get_ppm_Antifloat(self) -> BatchFloat64ArrayProxy:
        """
        Default=1 ppm.  Parts per million of transformer winding VA rating connected to ground to protect against accidentally floating a winding without a reference. If positive then the effect is adding a very large reactance to ground.  If negative, then a capacitor.

        DSS property name: `ppm_Antifloat`, DSS property index: 32.
        """
        return BatchFloat64ArrayProxy(self, 32)

    def _set_ppm_Antifloat(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(32, value, flags)

    ppm_Antifloat = property(_get_ppm_Antifloat, _set_ppm_Antifloat) # type: BatchFloat64ArrayProxy

    def _get_pctRs(self) -> List[Float64Array]:
        """
        Use this property to specify all the winding %resistances using an array. Example:

        New Transformer.T1 buses="Hibus, lowbus" ~ %Rs=(0.2  0.3)

        DSS property name: `%Rs`, DSS property index: 33.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 33)
            for x in self._unpack()
        ]

    def _set_pctRs(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(33, value, flags)

    pctRs = property(_get_pctRs, _set_pctRs) # type: List[Float64Array]

    def _get_X12(self) -> BatchFloat64ArrayProxy:
        """
        Alternative to XHL for specifying the percent reactance from winding 1 to winding 2.  Use for 2- or 3-winding transformers. Percent on the kVA base of winding 1. 

        DSS property name: `X12`, DSS property index: 34.
        """
        return BatchFloat64ArrayProxy(self, 34)

    def _set_X12(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(34, value, flags)

    X12 = property(_get_X12, _set_X12) # type: BatchFloat64ArrayProxy

    def _get_X13(self) -> BatchFloat64ArrayProxy:
        """
        Alternative to XHT for specifying the percent reactance from winding 1 to winding 3.  Use for 3-winding transformers only. Percent on the kVA base of winding 1. 

        DSS property name: `X13`, DSS property index: 35.
        """
        return BatchFloat64ArrayProxy(self, 35)

    def _set_X13(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(35, value, flags)

    X13 = property(_get_X13, _set_X13) # type: BatchFloat64ArrayProxy

    def _get_X23(self) -> BatchFloat64ArrayProxy:
        """
        Alternative to XLT for specifying the percent reactance from winding 2 to winding 3.Use for 3-winding transformers only. Percent on the kVA base of winding 1.  

        DSS property name: `X23`, DSS property index: 36.
        """
        return BatchFloat64ArrayProxy(self, 36)

    def _set_X23(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(36, value, flags)

    X23 = property(_get_X23, _set_X23) # type: BatchFloat64ArrayProxy

    def _get_RDCOhms(self) -> List[Float64Array]:
        """
        Winding dc resistance in OHMS. Useful for GIC analysis. From transformer test report. Defaults to 85% of %R property

        DSS property name: `RDCOhms`, DSS property index: 37.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 37)
            for x in self._unpack()
        ]

    def _set_RDCOhms(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(37, value, flags)

    RDCOhms = property(_get_RDCOhms, _set_RDCOhms) # type: List[Float64Array]

    def _get_Seasons(self) -> BatchInt32ArrayProxy:
        """
        Defines the number of ratings to be defined for the transfomer, to be used only when defining seasonal ratings using the "Ratings" property.

        DSS property name: `Seasons`, DSS property index: 38.
        """
        return BatchInt32ArrayProxy(self, 38)

    def _set_Seasons(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(38, value, flags)

    Seasons = property(_get_Seasons, _set_Seasons) # type: BatchInt32ArrayProxy

    def _get_Ratings(self) -> List[Float64Array]:
        """
        An array of ratings to be used when the seasonal ratings flag is True. It can be used to insert
        multiple ratings to change during a QSTS simulation to evaluate different ratings in transformers.

        DSS property name: `Ratings`, DSS property index: 39.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 39)
            for x in self._unpack()
        ]

    def _set_Ratings(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(39, value, flags)

    Ratings = property(_get_Ratings, _set_Ratings) # type: List[Float64Array]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 40.
        """
        self._set_batch_string(40, value, flags)

class XfmrCodeBatchProperties(TypedDict):
    Phases: Union[int, Int32Array]
    Windings: Union[int, Int32Array]
    pctR: Float64Array
    RNeut: Float64Array
    XNeut: Float64Array
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
    MaxTap: Float64Array
    MinTap: Float64Array
    NumTaps: Int32Array
    pctIMag: Union[float, Float64Array]
    ppm_Antifloat: Union[float, Float64Array]
    pctRs: Float64Array
    X12: Union[float, Float64Array]
    X13: Union[float, Float64Array]
    X23: Union[float, Float64Array]
    RDCOhms: Float64Array
    Seasons: Union[int, Int32Array]
    Ratings: Float64Array
    Like: AnyStr

class IXfmrCode(IDSSObj, XfmrCodeBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, XfmrCode, XfmrCodeBatch)
        XfmrCodeBatch.__init__(self, self._api_util, sync_cls_idx=XfmrCode._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> XfmrCode:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[XfmrCodeProperties]) -> XfmrCode:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[XfmrCodeBatchProperties]) -> XfmrCodeBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
