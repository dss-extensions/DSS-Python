# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from typing_extensions import TypedDict, Unpack
from ._obj_bases import (
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

class XfmrCode(DSSObj):
    __slots__ = []
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

    @property
    def Phases(self) -> int:
        """
        Number of phases this transformer. Default is 3.

        DSS property name: `Phases`, DSS property index: 1.
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @Phases.setter
    def Phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def Windings(self) -> int:
        """
        Number of windings, this transformers. (Also is the number of terminals) Default is 2. This property triggers memory allocation for the Transformer and will cause other properties to revert to default values.

        DSS property name: `Windings`, DSS property index: 2.
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @Windings.setter
    def Windings(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def pctR(self) -> Float64Array:
        """
        Percent resistance this winding.  (half of total for a 2-winding).

        DSS property name: `%R`, DSS property index: 8.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 8)

    @pctR.setter
    def pctR(self, value: Float64Array):
        self._set_float64_array_o(8, value)

    @property
    def RNeut(self) -> Float64Array:
        """
        Default = -1. Neutral resistance of wye (star)-connected winding in actual ohms.If entered as a negative value, the neutral is assumed to be open, or floating.

        DSS property name: `RNeut`, DSS property index: 9.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 9)

    @RNeut.setter
    def RNeut(self, value: Float64Array):
        self._set_float64_array_o(9, value)

    @property
    def XNeut(self) -> Float64Array:
        """
        Neutral reactance of wye(star)-connected winding in actual ohms.  May be + or -.

        DSS property name: `XNeut`, DSS property index: 10.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 10)

    @XNeut.setter
    def XNeut(self, value: Float64Array):
        self._set_float64_array_o(10, value)

    @property
    def Conns(self) -> List[enums.Connection]:
        """
        Use this to specify all the Winding connections at once using an array. Example:

        New Transformer.T1 buses="Hibus, lowbus"
        ~ conns=(delta, wye)

        DSS property name: `Conns`, DSS property index: 11.
        """
        return [enums.Connection(val) for val in self._get_int32_list(self._lib.Obj_GetInt32Array, self._ptr, 11)]

    @Conns.setter
    def Conns(self, value: Union[List[Union[int, enums.Connection]], List[AnyStr]]):
        if len(value) and not isinstance(value[0], int):
            self._set_string_array_o(11, value)
            return    
        self._set_int32_array_o(11, value)

    @property
    def Conns_str(self) -> List[str]:
        """
        Use this to specify all the Winding connections at once using an array. Example:

        New Transformer.T1 buses="Hibus, lowbus"
        ~ conns=(delta, wye)

        DSS property name: `Conns`, DSS property index: 11.
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 11)

    @Conns_str.setter
    def Conns_str(self, value: AnyStr):
        self.Conns = value

    @property
    def kVs(self) -> Float64Array:
        """
        Use this to specify the kV ratings of all windings at once using an array. Example:

        New Transformer.T1 buses="Hibus, lowbus" 
        ~ conns=(delta, wye)
        ~ kvs=(115, 12.47)

        See kV= property for voltage rules.

        DSS property name: `kVs`, DSS property index: 12.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 12)

    @kVs.setter
    def kVs(self, value: Float64Array):
        self._set_float64_array_o(12, value)

    @property
    def kVAs(self) -> Float64Array:
        """
        Use this to specify the kVA ratings of all windings at once using an array.

        DSS property name: `kVAs`, DSS property index: 13.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 13)

    @kVAs.setter
    def kVAs(self, value: Float64Array):
        self._set_float64_array_o(13, value)

    @property
    def Taps(self) -> Float64Array:
        """
        Use this to specify the normal p.u. tap of all windings at once using an array.

        DSS property name: `Taps`, DSS property index: 14.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 14)

    @Taps.setter
    def Taps(self, value: Float64Array):
        self._set_float64_array_o(14, value)

    @property
    def XHL(self) -> float:
        """
        Use this to specify the percent reactance, H-L (winding 1 to winding 2).  Use for 2- or 3-winding transformers. On the kva base of winding 1.

        DSS property name: `XHL`, DSS property index: 15.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @XHL.setter
    def XHL(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def XHT(self) -> float:
        """
        Use this to specify the percent reactance, H-T (winding 1 to winding 3).  Use for 3-winding transformers only. On the kVA base of winding 1.

        DSS property name: `XHT`, DSS property index: 16.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    @XHT.setter
    def XHT(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 16, value)

    @property
    def XLT(self) -> float:
        """
        Use this to specify the percent reactance, L-T (winding 2 to winding 3).  Use for 3-winding transformers only. On the kVA base of winding 1.

        DSS property name: `XLT`, DSS property index: 17.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    @XLT.setter
    def XLT(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 17, value)

    @property
    def XSCArray(self) -> Float64Array:
        """
        Use this to specify the percent reactance between all pairs of windings as an array. All values are on the kVA base of winding 1.  The order of the values is as follows:

        (x12 13 14... 23 24.. 34 ..)  

        There will be n(n-1)/2 values, where n=number of windings.

        DSS property name: `XSCArray`, DSS property index: 18.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 18)

    @XSCArray.setter
    def XSCArray(self, value: Float64Array):
        self._set_float64_array_o(18, value)

    @property
    def Thermal(self) -> float:
        """
        Thermal time constant of the transformer in hours.  Typically about 2.

        DSS property name: `Thermal`, DSS property index: 19.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    @Thermal.setter
    def Thermal(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 19, value)

    @property
    def n(self) -> float:
        """
        n Exponent for thermal properties in IEEE C57.  Typically 0.8.

        DSS property name: `n`, DSS property index: 20.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    @n.setter
    def n(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 20, value)

    @property
    def m(self) -> float:
        """
        m Exponent for thermal properties in IEEE C57.  Typically 0.9 - 1.0

        DSS property name: `m`, DSS property index: 21.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @m.setter
    def m(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    @property
    def FLRise(self) -> float:
        """
        Temperature rise, deg C, for full load.  Default is 65.

        DSS property name: `FLRise`, DSS property index: 22.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    @FLRise.setter
    def FLRise(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 22, value)

    @property
    def HSRise(self) -> float:
        """
        Hot spot temperature rise, deg C.  Default is 15.

        DSS property name: `HSRise`, DSS property index: 23.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    @HSRise.setter
    def HSRise(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 23, value)

    @property
    def pctLoadLoss(self) -> float:
        """
        Percent load loss at full load. The %R of the High and Low windings (1 and 2) are adjusted to agree at rated kVA loading.

        DSS property name: `%LoadLoss`, DSS property index: 24.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    @pctLoadLoss.setter
    def pctLoadLoss(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 24, value)

    @property
    def pctNoLoadLoss(self) -> float:
        """
        Percent no load losses at rated excitation voltage. Default is 0. Converts to a resistance in parallel with the magnetizing impedance in each winding.

        DSS property name: `%NoLoadLoss`, DSS property index: 25.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 25)

    @pctNoLoadLoss.setter
    def pctNoLoadLoss(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 25, value)

    @property
    def NormHkVA(self) -> float:
        """
        Normal maximum kVA rating of H winding (winding 1).  Usually 100% - 110% of maximum nameplate rating, depending on load shape. Defaults to 110% of kVA rating of Winding 1.

        DSS property name: `NormHkVA`, DSS property index: 26.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 26)

    @NormHkVA.setter
    def NormHkVA(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 26, value)

    @property
    def EmergHkVA(self) -> float:
        """
        Emergency (contingency)  kVA rating of H winding (winding 1).  Usually 140% - 150% of maximum nameplate rating, depending on load shape. Defaults to 150% of kVA rating of Winding 1.

        DSS property name: `EmergHkVA`, DSS property index: 27.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 27)

    @EmergHkVA.setter
    def EmergHkVA(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 27, value)

    @property
    def MaxTap(self) -> Float64Array:
        """
        Max per unit tap for the active winding.  Default is 1.10

        DSS property name: `MaxTap`, DSS property index: 28.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 28)

    @MaxTap.setter
    def MaxTap(self, value: Float64Array):
        self._set_float64_array_o(28, value)

    @property
    def MinTap(self) -> Float64Array:
        """
        Min per unit tap for the active winding.  Default is 0.90

        DSS property name: `MinTap`, DSS property index: 29.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 29)

    @MinTap.setter
    def MinTap(self, value: Float64Array):
        self._set_float64_array_o(29, value)

    @property
    def NumTaps(self) -> Int32Array:
        """
        Total number of taps between min and max tap.  Default is 32.

        DSS property name: `NumTaps`, DSS property index: 30.
        """
        return self._get_int32_array(self._lib.Obj_GetInt32Array, self._ptr, 30)

    @NumTaps.setter
    def NumTaps(self, value: Int32Array):
        self._set_int32_array_o(30, value)

    @property
    def pctIMag(self) -> float:
        """
        Percent magnetizing current. Default=0.0. Magnetizing branch is in parallel with windings in each phase. Also, see "ppm_antifloat".

        DSS property name: `%IMag`, DSS property index: 31.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 31)

    @pctIMag.setter
    def pctIMag(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 31, value)

    @property
    def ppm_Antifloat(self) -> float:
        """
        Default=1 ppm.  Parts per million of transformer winding VA rating connected to ground to protect against accidentally floating a winding without a reference. If positive then the effect is adding a very large reactance to ground.  If negative, then a capacitor.

        DSS property name: `ppm_Antifloat`, DSS property index: 32.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 32)

    @ppm_Antifloat.setter
    def ppm_Antifloat(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 32, value)

    @property
    def pctRs(self) -> Float64Array:
        """
        Use this property to specify all the winding %resistances using an array. Example:

        New Transformer.T1 buses="Hibus, lowbus" ~ %Rs=(0.2  0.3)

        DSS property name: `%Rs`, DSS property index: 33.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 33)

    @pctRs.setter
    def pctRs(self, value: Float64Array):
        self._set_float64_array_o(33, value)

    @property
    def X12(self) -> float:
        """
        Alternative to XHL for specifying the percent reactance from winding 1 to winding 2.  Use for 2- or 3-winding transformers. Percent on the kVA base of winding 1. 

        DSS property name: `X12`, DSS property index: 34.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 34)

    @X12.setter
    def X12(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 34, value)

    @property
    def X13(self) -> float:
        """
        Alternative to XHT for specifying the percent reactance from winding 1 to winding 3.  Use for 3-winding transformers only. Percent on the kVA base of winding 1. 

        DSS property name: `X13`, DSS property index: 35.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 35)

    @X13.setter
    def X13(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 35, value)

    @property
    def X23(self) -> float:
        """
        Alternative to XLT for specifying the percent reactance from winding 2 to winding 3.Use for 3-winding transformers only. Percent on the kVA base of winding 1.  

        DSS property name: `X23`, DSS property index: 36.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 36)

    @X23.setter
    def X23(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 36, value)

    @property
    def RDCOhms(self) -> Float64Array:
        """
        Winding dc resistance in OHMS. Useful for GIC analysis. From transformer test report. Defaults to 85% of %R property

        DSS property name: `RDCOhms`, DSS property index: 37.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 37)

    @RDCOhms.setter
    def RDCOhms(self, value: Float64Array):
        self._set_float64_array_o(37, value)

    @property
    def Seasons(self) -> int:
        """
        Defines the number of ratings to be defined for the transfomer, to be used only when defining seasonal ratings using the "Ratings" property.

        DSS property name: `Seasons`, DSS property index: 38.
        """
        return self._lib.Obj_GetInt32(self._ptr, 38)

    @Seasons.setter
    def Seasons(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 38, value)

    @property
    def Ratings(self) -> Float64Array:
        """
        An array of ratings to be used when the seasonal ratings flag is True. It can be used to insert
        multiple ratings to change during a QSTS simulation to evaluate different ratings in transformers.

        DSS property name: `Ratings`, DSS property index: 39.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 39)

    @Ratings.setter
    def Ratings(self, value: Float64Array):
        self._set_float64_array_o(39, value)

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


    @property
    def Phases(self) -> BatchInt32ArrayProxy:
        """
        Number of phases this transformer. Default is 3.

        DSS property name: `Phases`, DSS property index: 1.
        """
        return BatchInt32ArrayProxy(self, 1)

    @Phases.setter
    def Phases(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(1, value)

    @property
    def Windings(self) -> BatchInt32ArrayProxy:
        """
        Number of windings, this transformers. (Also is the number of terminals) Default is 2. This property triggers memory allocation for the Transformer and will cause other properties to revert to default values.

        DSS property name: `Windings`, DSS property index: 2.
        """
        return BatchInt32ArrayProxy(self, 2)

    @Windings.setter
    def Windings(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(2, value)

    @property
    def pctR(self) -> List[Float64Array]:
        """
        Percent resistance this winding.  (half of total for a 2-winding).

        DSS property name: `%R`, DSS property index: 8.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 8)
            for x in self._unpack()
        ]

    @pctR.setter
    def pctR(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(8, value)

    @property
    def RNeut(self) -> List[Float64Array]:
        """
        Default = -1. Neutral resistance of wye (star)-connected winding in actual ohms.If entered as a negative value, the neutral is assumed to be open, or floating.

        DSS property name: `RNeut`, DSS property index: 9.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 9)
            for x in self._unpack()
        ]

    @RNeut.setter
    def RNeut(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(9, value)

    @property
    def XNeut(self) -> List[Float64Array]:
        """
        Neutral reactance of wye(star)-connected winding in actual ohms.  May be + or -.

        DSS property name: `XNeut`, DSS property index: 10.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 10)
            for x in self._unpack()
        ]

    @XNeut.setter
    def XNeut(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(10, value)

    @property
    def Conns(self) -> List[Int32Array]:
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

    @Conns.setter
    def Conns(self, value: Union[List[Union[int, enums.Connection]], List[AnyStr]]): #TODO: list of lists
        if len(value) and not isinstance(value[0], int):
            value, value_ptr, value_count = self._prepare_string_array(value)
            for x in self._unpack():
                self._lib.Obj_SetStringArray(x, 11, value_ptr, value_count)

            self._check_for_error()
            return

        self._set_batch_int32_array(11, value)

    @property
    def Conns_str(self) -> List[List[str]]:
        """
        Use this to specify all the Winding connections at once using an array. Example:

        New Transformer.T1 buses="Hibus, lowbus"
        ~ conns=(delta, wye)

        DSS property name: `Conns`, DSS property index: 11.
        """
        return self._get_string_ll(11)

    @Conns_str.setter
    def Conns_str(self, value: AnyStr):
        self.Conns = value

    @property
    def kVs(self) -> List[Float64Array]:
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

    @kVs.setter
    def kVs(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(12, value)

    @property
    def kVAs(self) -> List[Float64Array]:
        """
        Use this to specify the kVA ratings of all windings at once using an array.

        DSS property name: `kVAs`, DSS property index: 13.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 13)
            for x in self._unpack()
        ]

    @kVAs.setter
    def kVAs(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(13, value)

    @property
    def Taps(self) -> List[Float64Array]:
        """
        Use this to specify the normal p.u. tap of all windings at once using an array.

        DSS property name: `Taps`, DSS property index: 14.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 14)
            for x in self._unpack()
        ]

    @Taps.setter
    def Taps(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(14, value)

    @property
    def XHL(self) -> BatchFloat64ArrayProxy:
        """
        Use this to specify the percent reactance, H-L (winding 1 to winding 2).  Use for 2- or 3-winding transformers. On the kva base of winding 1.

        DSS property name: `XHL`, DSS property index: 15.
        """
        return BatchFloat64ArrayProxy(self, 15)

    @XHL.setter
    def XHL(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(15, value)

    @property
    def XHT(self) -> BatchFloat64ArrayProxy:
        """
        Use this to specify the percent reactance, H-T (winding 1 to winding 3).  Use for 3-winding transformers only. On the kVA base of winding 1.

        DSS property name: `XHT`, DSS property index: 16.
        """
        return BatchFloat64ArrayProxy(self, 16)

    @XHT.setter
    def XHT(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(16, value)

    @property
    def XLT(self) -> BatchFloat64ArrayProxy:
        """
        Use this to specify the percent reactance, L-T (winding 2 to winding 3).  Use for 3-winding transformers only. On the kVA base of winding 1.

        DSS property name: `XLT`, DSS property index: 17.
        """
        return BatchFloat64ArrayProxy(self, 17)

    @XLT.setter
    def XLT(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(17, value)

    @property
    def XSCArray(self) -> List[Float64Array]:
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

    @XSCArray.setter
    def XSCArray(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(18, value)

    @property
    def Thermal(self) -> BatchFloat64ArrayProxy:
        """
        Thermal time constant of the transformer in hours.  Typically about 2.

        DSS property name: `Thermal`, DSS property index: 19.
        """
        return BatchFloat64ArrayProxy(self, 19)

    @Thermal.setter
    def Thermal(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(19, value)

    @property
    def n(self) -> BatchFloat64ArrayProxy:
        """
        n Exponent for thermal properties in IEEE C57.  Typically 0.8.

        DSS property name: `n`, DSS property index: 20.
        """
        return BatchFloat64ArrayProxy(self, 20)

    @n.setter
    def n(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(20, value)

    @property
    def m(self) -> BatchFloat64ArrayProxy:
        """
        m Exponent for thermal properties in IEEE C57.  Typically 0.9 - 1.0

        DSS property name: `m`, DSS property index: 21.
        """
        return BatchFloat64ArrayProxy(self, 21)

    @m.setter
    def m(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(21, value)

    @property
    def FLRise(self) -> BatchFloat64ArrayProxy:
        """
        Temperature rise, deg C, for full load.  Default is 65.

        DSS property name: `FLRise`, DSS property index: 22.
        """
        return BatchFloat64ArrayProxy(self, 22)

    @FLRise.setter
    def FLRise(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(22, value)

    @property
    def HSRise(self) -> BatchFloat64ArrayProxy:
        """
        Hot spot temperature rise, deg C.  Default is 15.

        DSS property name: `HSRise`, DSS property index: 23.
        """
        return BatchFloat64ArrayProxy(self, 23)

    @HSRise.setter
    def HSRise(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(23, value)

    @property
    def pctLoadLoss(self) -> BatchFloat64ArrayProxy:
        """
        Percent load loss at full load. The %R of the High and Low windings (1 and 2) are adjusted to agree at rated kVA loading.

        DSS property name: `%LoadLoss`, DSS property index: 24.
        """
        return BatchFloat64ArrayProxy(self, 24)

    @pctLoadLoss.setter
    def pctLoadLoss(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(24, value)

    @property
    def pctNoLoadLoss(self) -> BatchFloat64ArrayProxy:
        """
        Percent no load losses at rated excitation voltage. Default is 0. Converts to a resistance in parallel with the magnetizing impedance in each winding.

        DSS property name: `%NoLoadLoss`, DSS property index: 25.
        """
        return BatchFloat64ArrayProxy(self, 25)

    @pctNoLoadLoss.setter
    def pctNoLoadLoss(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(25, value)

    @property
    def NormHkVA(self) -> BatchFloat64ArrayProxy:
        """
        Normal maximum kVA rating of H winding (winding 1).  Usually 100% - 110% of maximum nameplate rating, depending on load shape. Defaults to 110% of kVA rating of Winding 1.

        DSS property name: `NormHkVA`, DSS property index: 26.
        """
        return BatchFloat64ArrayProxy(self, 26)

    @NormHkVA.setter
    def NormHkVA(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(26, value)

    @property
    def EmergHkVA(self) -> BatchFloat64ArrayProxy:
        """
        Emergency (contingency)  kVA rating of H winding (winding 1).  Usually 140% - 150% of maximum nameplate rating, depending on load shape. Defaults to 150% of kVA rating of Winding 1.

        DSS property name: `EmergHkVA`, DSS property index: 27.
        """
        return BatchFloat64ArrayProxy(self, 27)

    @EmergHkVA.setter
    def EmergHkVA(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(27, value)

    @property
    def MaxTap(self) -> List[Float64Array]:
        """
        Max per unit tap for the active winding.  Default is 1.10

        DSS property name: `MaxTap`, DSS property index: 28.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 28)
            for x in self._unpack()
        ]

    @MaxTap.setter
    def MaxTap(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(28, value)

    @property
    def MinTap(self) -> List[Float64Array]:
        """
        Min per unit tap for the active winding.  Default is 0.90

        DSS property name: `MinTap`, DSS property index: 29.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 29)
            for x in self._unpack()
        ]

    @MinTap.setter
    def MinTap(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(29, value)

    @property
    def NumTaps(self) -> List[Int32Array]:
        """
        Total number of taps between min and max tap.  Default is 32.

        DSS property name: `NumTaps`, DSS property index: 30.
        """
        return [
            self._get_int32_array(self._lib.Obj_GetInt32Array, x, 30)
            for x in self._unpack()
        ]

    @NumTaps.setter
    def NumTaps(self, value: Union[Int32Array, List[Int32Array]]):
        self._set_batch_int32_array_prop(30, value)

    @property
    def pctIMag(self) -> BatchFloat64ArrayProxy:
        """
        Percent magnetizing current. Default=0.0. Magnetizing branch is in parallel with windings in each phase. Also, see "ppm_antifloat".

        DSS property name: `%IMag`, DSS property index: 31.
        """
        return BatchFloat64ArrayProxy(self, 31)

    @pctIMag.setter
    def pctIMag(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(31, value)

    @property
    def ppm_Antifloat(self) -> BatchFloat64ArrayProxy:
        """
        Default=1 ppm.  Parts per million of transformer winding VA rating connected to ground to protect against accidentally floating a winding without a reference. If positive then the effect is adding a very large reactance to ground.  If negative, then a capacitor.

        DSS property name: `ppm_Antifloat`, DSS property index: 32.
        """
        return BatchFloat64ArrayProxy(self, 32)

    @ppm_Antifloat.setter
    def ppm_Antifloat(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(32, value)

    @property
    def pctRs(self) -> List[Float64Array]:
        """
        Use this property to specify all the winding %resistances using an array. Example:

        New Transformer.T1 buses="Hibus, lowbus" ~ %Rs=(0.2  0.3)

        DSS property name: `%Rs`, DSS property index: 33.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 33)
            for x in self._unpack()
        ]

    @pctRs.setter
    def pctRs(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(33, value)

    @property
    def X12(self) -> BatchFloat64ArrayProxy:
        """
        Alternative to XHL for specifying the percent reactance from winding 1 to winding 2.  Use for 2- or 3-winding transformers. Percent on the kVA base of winding 1. 

        DSS property name: `X12`, DSS property index: 34.
        """
        return BatchFloat64ArrayProxy(self, 34)

    @X12.setter
    def X12(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(34, value)

    @property
    def X13(self) -> BatchFloat64ArrayProxy:
        """
        Alternative to XHT for specifying the percent reactance from winding 1 to winding 3.  Use for 3-winding transformers only. Percent on the kVA base of winding 1. 

        DSS property name: `X13`, DSS property index: 35.
        """
        return BatchFloat64ArrayProxy(self, 35)

    @X13.setter
    def X13(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(35, value)

    @property
    def X23(self) -> BatchFloat64ArrayProxy:
        """
        Alternative to XLT for specifying the percent reactance from winding 2 to winding 3.Use for 3-winding transformers only. Percent on the kVA base of winding 1.  

        DSS property name: `X23`, DSS property index: 36.
        """
        return BatchFloat64ArrayProxy(self, 36)

    @X23.setter
    def X23(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(36, value)

    @property
    def RDCOhms(self) -> List[Float64Array]:
        """
        Winding dc resistance in OHMS. Useful for GIC analysis. From transformer test report. Defaults to 85% of %R property

        DSS property name: `RDCOhms`, DSS property index: 37.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 37)
            for x in self._unpack()
        ]

    @RDCOhms.setter
    def RDCOhms(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(37, value)

    @property
    def Seasons(self) -> BatchInt32ArrayProxy:
        """
        Defines the number of ratings to be defined for the transfomer, to be used only when defining seasonal ratings using the "Ratings" property.

        DSS property name: `Seasons`, DSS property index: 38.
        """
        return BatchInt32ArrayProxy(self, 38)

    @Seasons.setter
    def Seasons(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(38, value)

    @property
    def Ratings(self) -> List[Float64Array]:
        """
        An array of ratings to be used when the seasonal ratings flag is True. It can be used to insert
        multiple ratings to change during a QSTS simulation to evaluate different ratings in transformers.

        DSS property name: `Ratings`, DSS property index: 39.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 39)
            for x in self._unpack()
        ]

    @Ratings.setter
    def Ratings(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(39, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 40.
        """
        self._set_batch_string(40, value)

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

class IXfmrCode(IDSSObj,XfmrCodeBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, XfmrCode, XfmrCodeBatch)
        XfmrCodeBatch.__init__(self, self._api_util, sync_cls=True)
        

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> XfmrCode:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[XfmrCodeProperties]) -> XfmrCode:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[XfmrCodeBatchProperties]) -> XfmrCodeBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
