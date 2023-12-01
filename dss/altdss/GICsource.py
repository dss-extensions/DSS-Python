# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from typing_extensions import TypedDict, Unpack
from .types import Float64Array, Int32Array
from . import enums
from .DSSObj import IDSSObj, DSSObj
from .Batch import DSSBatch
from .ArrayProxy import BatchFloat64ArrayProxy, BatchInt32ArrayProxy
from .PCElement import PCElementBatchMixin, PCElementMixin
from .CircuitElement import CircuitElementBatchMixin, CircuitElementMixin
from .Spectrum import Spectrum as SpectrumObj

class GICsource(DSSObj, CircuitElementMixin, PCElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots + PCElementMixin._extra_slots
    _cls_name = 'GICsource'
    _cls_idx = 40
    _cls_prop_idx = {
        'volts': 1,
        'angle': 2,
        'frequency': 3,
        'phases': 4,
        'en': 5,
        'ee': 6,
        'lat1': 7,
        'lon1': 8,
        'lat2': 9,
        'lon2': 10,
        'spectrum': 11,
        'basefreq': 12,
        'enabled': 13,
        'like': 14,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)
       PCElementMixin.__init__(self)

    def _get_Volts(self) -> float:
        """
        Voltage magnitude, in volts, of the GIC voltage induced across the associated line. When specified, induced voltage is assumed defined by Voltage and Angle properties. 

        Specify this value

        OR

        EN, EE, lat1, lon1, lat2, lon2. 

        Not both!!  Last one entered will take precedence. Assumed identical in each phase of the Line object.

        DSS property name: `Volts`, DSS property index: 1.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 1)

    def _set_Volts(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 1, value, flags)

    Volts = property(_get_Volts, _set_Volts) # type: float

    def _get_Angle(self) -> float:
        """
        Phase angle in degrees of first phase. Default=0.0.  See Voltage property

        DSS property name: `Angle`, DSS property index: 2.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 2)

    def _set_Angle(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 2, value, flags)

    Angle = property(_get_Angle, _set_Angle) # type: float

    def _get_Frequency(self) -> float:
        """
        Source frequency.  Defaults to  0.1 Hz. So GICSource=0 at power frequency.

        DSS property name: `Frequency`, DSS property index: 3.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    def _set_Frequency(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 3, value, flags)

    Frequency = property(_get_Frequency, _set_Frequency) # type: float

    def _get_Phases(self) -> int:
        """
        Number of phases.  Defaults to 3. All three phases are assumed in phase (zero sequence)

        DSS property name: `Phases`, DSS property index: 4.
        """
        return self._lib.Obj_GetInt32(self._ptr, 4)

    def _set_Phases(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 4, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: int

    def _get_EN(self) -> float:
        """
        Northward Electric field (V/km). If specified, Voltage and Angle are computed from EN, EE, lat and lon values.

        DSS property name: `EN`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    def _set_EN(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 5, value, flags)

    EN = property(_get_EN, _set_EN) # type: float

    def _get_EE(self) -> float:
        """
        Eastward Electric field (V/km).  If specified, Voltage and Angle are computed from EN, EE, lat and lon values.

        DSS property name: `EE`, DSS property index: 6.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    def _set_EE(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 6, value, flags)

    EE = property(_get_EE, _set_EE) # type: float

    def _get_Lat1(self) -> float:
        """
        Latitude of Bus1 of the line(degrees)

        DSS property name: `Lat1`, DSS property index: 7.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    def _set_Lat1(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 7, value, flags)

    Lat1 = property(_get_Lat1, _set_Lat1) # type: float

    def _get_Lon1(self) -> float:
        """
        Longitude of Bus1 of the line (degrees)

        DSS property name: `Lon1`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    def _set_Lon1(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 8, value, flags)

    Lon1 = property(_get_Lon1, _set_Lon1) # type: float

    def _get_Lat2(self) -> float:
        """
        Latitude of Bus2 of the line (degrees)

        DSS property name: `Lat2`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    def _set_Lat2(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 9, value, flags)

    Lat2 = property(_get_Lat2, _set_Lat2) # type: float

    def _get_Lon2(self) -> float:
        """
        Longitude of Bus2 of the line (degrees)

        DSS property name: `Lon2`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    def _set_Lon2(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 10, value, flags)

    Lon2 = property(_get_Lon2, _set_Lon2) # type: float

    def _get_Spectrum_str(self) -> str:
        """
        Not used.

        DSS property name: `Spectrum`, DSS property index: 11.
        """
        return self._get_prop_string(11)

    def _set_Spectrum_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(11, value, flags)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str) # type: str

    def _get_Spectrum(self) -> SpectrumObj:
        """
        Not used.

        DSS property name: `Spectrum`, DSS property index: 11.
        """
        return self._get_obj(11, SpectrumObj)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(11, value, flags)
            return

        self._set_string_o(11, value, flags)

    Spectrum = property(_get_Spectrum, _set_Spectrum) # type: SpectrumObj

    def _get_BaseFreq(self) -> float:
        """
        Not used.

        DSS property name: `BaseFreq`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 12, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float

    def _get_Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 13.
        """
        return self._lib.Obj_GetInt32(self._ptr, 13) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 13, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 14.
        """
        self._set_string_o(14, value)


class GICsourceProperties(TypedDict):
    Volts: float
    Angle: float
    Frequency: float
    Phases: int
    EN: float
    EE: float
    Lat1: float
    Lon1: float
    Lat2: float
    Lon2: float
    Spectrum: Union[AnyStr, SpectrumObj]
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class GICsourceBatch(DSSBatch, CircuitElementBatchMixin, PCElementBatchMixin):
    _cls_name = 'GICsource'
    _obj_cls = GICsource
    _cls_idx = 40

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)
       PCElementBatchMixin.__init__(self)

    def _get_Volts(self) -> BatchFloat64ArrayProxy:
        """
        Voltage magnitude, in volts, of the GIC voltage induced across the associated line. When specified, induced voltage is assumed defined by Voltage and Angle properties. 

        Specify this value

        OR

        EN, EE, lat1, lon1, lat2, lon2. 

        Not both!!  Last one entered will take precedence. Assumed identical in each phase of the Line object.

        DSS property name: `Volts`, DSS property index: 1.
        """
        return BatchFloat64ArrayProxy(self, 1)

    def _set_Volts(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(1, value, flags)

    Volts = property(_get_Volts, _set_Volts) # type: BatchFloat64ArrayProxy

    def _get_Angle(self) -> BatchFloat64ArrayProxy:
        """
        Phase angle in degrees of first phase. Default=0.0.  See Voltage property

        DSS property name: `Angle`, DSS property index: 2.
        """
        return BatchFloat64ArrayProxy(self, 2)

    def _set_Angle(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(2, value, flags)

    Angle = property(_get_Angle, _set_Angle) # type: BatchFloat64ArrayProxy

    def _get_Frequency(self) -> BatchFloat64ArrayProxy:
        """
        Source frequency.  Defaults to  0.1 Hz. So GICSource=0 at power frequency.

        DSS property name: `Frequency`, DSS property index: 3.
        """
        return BatchFloat64ArrayProxy(self, 3)

    def _set_Frequency(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(3, value, flags)

    Frequency = property(_get_Frequency, _set_Frequency) # type: BatchFloat64ArrayProxy

    def _get_Phases(self) -> BatchInt32ArrayProxy:
        """
        Number of phases.  Defaults to 3. All three phases are assumed in phase (zero sequence)

        DSS property name: `Phases`, DSS property index: 4.
        """
        return BatchInt32ArrayProxy(self, 4)

    def _set_Phases(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(4, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: BatchInt32ArrayProxy

    def _get_EN(self) -> BatchFloat64ArrayProxy:
        """
        Northward Electric field (V/km). If specified, Voltage and Angle are computed from EN, EE, lat and lon values.

        DSS property name: `EN`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    def _set_EN(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(5, value, flags)

    EN = property(_get_EN, _set_EN) # type: BatchFloat64ArrayProxy

    def _get_EE(self) -> BatchFloat64ArrayProxy:
        """
        Eastward Electric field (V/km).  If specified, Voltage and Angle are computed from EN, EE, lat and lon values.

        DSS property name: `EE`, DSS property index: 6.
        """
        return BatchFloat64ArrayProxy(self, 6)

    def _set_EE(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(6, value, flags)

    EE = property(_get_EE, _set_EE) # type: BatchFloat64ArrayProxy

    def _get_Lat1(self) -> BatchFloat64ArrayProxy:
        """
        Latitude of Bus1 of the line(degrees)

        DSS property name: `Lat1`, DSS property index: 7.
        """
        return BatchFloat64ArrayProxy(self, 7)

    def _set_Lat1(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(7, value, flags)

    Lat1 = property(_get_Lat1, _set_Lat1) # type: BatchFloat64ArrayProxy

    def _get_Lon1(self) -> BatchFloat64ArrayProxy:
        """
        Longitude of Bus1 of the line (degrees)

        DSS property name: `Lon1`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    def _set_Lon1(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(8, value, flags)

    Lon1 = property(_get_Lon1, _set_Lon1) # type: BatchFloat64ArrayProxy

    def _get_Lat2(self) -> BatchFloat64ArrayProxy:
        """
        Latitude of Bus2 of the line (degrees)

        DSS property name: `Lat2`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    def _set_Lat2(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(9, value, flags)

    Lat2 = property(_get_Lat2, _set_Lat2) # type: BatchFloat64ArrayProxy

    def _get_Lon2(self) -> BatchFloat64ArrayProxy:
        """
        Longitude of Bus2 of the line (degrees)

        DSS property name: `Lon2`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    def _set_Lon2(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(10, value, flags)

    Lon2 = property(_get_Lon2, _set_Lon2) # type: BatchFloat64ArrayProxy

    def _get_Spectrum_str(self) -> List[str]:
        """
        Not used.

        DSS property name: `Spectrum`, DSS property index: 11.
        """
        return self._get_batch_str_prop(11)

    def _set_Spectrum_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(11, value, flags)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str) # type: List[str]

    def _get_Spectrum(self) -> List[SpectrumObj]:
        """
        Not used.

        DSS property name: `Spectrum`, DSS property index: 11.
        """
        return self._get_batch_obj_prop(11)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(11, value, flags)

    Spectrum = property(_get_Spectrum, _set_Spectrum) # type: List[SpectrumObj]

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Not used.

        DSS property name: `BaseFreq`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(12, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy

    def _get_Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 13.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(13)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(13, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 14.
        """
        self._set_batch_string(14, value, flags)

class GICsourceBatchProperties(TypedDict):
    Volts: Union[float, Float64Array]
    Angle: Union[float, Float64Array]
    Frequency: Union[float, Float64Array]
    Phases: Union[int, Int32Array]
    EN: Union[float, Float64Array]
    EE: Union[float, Float64Array]
    Lat1: Union[float, Float64Array]
    Lon1: Union[float, Float64Array]
    Lat2: Union[float, Float64Array]
    Lon2: Union[float, Float64Array]
    Spectrum: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IGICsource(IDSSObj, GICsourceBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, GICsource, GICsourceBatch)
        GICsourceBatch.__init__(self, self._api_util, sync_cls_idx=GICsource._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> GICsource:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[GICsourceProperties]) -> GICsource:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[GICsourceBatchProperties]) -> GICsourceBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
