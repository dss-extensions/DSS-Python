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

class Sensor(DSSObj, CircuitElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots
    _cls_name = 'Sensor'
    _cls_idx = 49
    _cls_prop_idx = {
        'element': 1,
        'terminal': 2,
        'kvbase': 3,
        'clear': 4,
        'kvs': 5,
        'currents': 6,
        'kws': 7,
        'kvars': 8,
        'conn': 9,
        'deltadirection': 10,
        'pcterror': 11,
        '%error': 11,
        'weight': 12,
        'basefreq': 13,
        'enabled': 14,
        'like': 15,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)

    def _get_Element_str(self) -> str:
        """
        Name (Full Object name) of element to which the Sensor is connected.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    def _set_Element_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(1, value, flags)

    Element_str = property(_get_Element_str, _set_Element_str) # type: str

    def _get_Element(self) -> DSSObj:
        """
        Name (Full Object name) of element to which the Sensor is connected.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_obj(1, None)

    def _set_Element(self, value: Union[AnyStr, DSSObj], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(1, value, flags)
            return

        self._set_string_o(1, value, flags)

    Element = property(_get_Element, _set_Element) # type: DSSObj

    def _get_Terminal(self) -> int:
        """
        Number of the terminal of the circuit element to which the Sensor is connected. 1 or 2, typically. Default is 1.

        DSS property name: `Terminal`, DSS property index: 2.
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    def _set_Terminal(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 2, value, flags)

    Terminal = property(_get_Terminal, _set_Terminal) # type: int

    def _get_kVBase(self) -> float:
        """
        Voltage base for the sensor, in kV. If connected to a 2- or 3-phase terminal, 
        specify L-L voltage. For 1-phase devices specify L-N or actual 1-phase voltage. Like many other DSS devices, default is 12.47kV.

        DSS property name: `kVBase`, DSS property index: 3.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    def _set_kVBase(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 3, value, flags)

    kVBase = property(_get_kVBase, _set_kVBase) # type: float

    def Clear(self, value: bool = True, flags: enums.SetterFlags = 0):
        """
        { Yes | No }. Clear=Yes clears sensor values. Should be issued before putting in a new set of measurements.

        DSS property name: `Clear`, DSS property index: 4.
        """
        self._lib.Obj_SetInt32(self._ptr, 4, value, flags)

    def _get_kVs(self) -> Float64Array:
        """
        Array of Voltages (kV) measured by the voltage sensor. For Delta-connected sensors, Line-Line voltages are expected. For Wye, Line-Neutral are expected.

        DSS property name: `kVs`, DSS property index: 5.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 5)

    def _set_kVs(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(5, value, flags)

    kVs = property(_get_kVs, _set_kVs) # type: Float64Array

    def _get_Currents(self) -> Float64Array:
        """
        Array of Currents (amps) measured by the current sensor. Specify this or power quantities; not both.

        DSS property name: `Currents`, DSS property index: 6.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 6)

    def _set_Currents(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(6, value, flags)

    Currents = property(_get_Currents, _set_Currents) # type: Float64Array

    def _get_kWs(self) -> Float64Array:
        """
        Array of Active power (kW) measurements at the sensor. Is converted into Currents along with q=[...]
        Will override any currents=[...] specification.

        DSS property name: `kWs`, DSS property index: 7.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 7)

    def _set_kWs(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(7, value, flags)

    kWs = property(_get_kWs, _set_kWs) # type: Float64Array

    def _get_kvars(self) -> Float64Array:
        """
        Array of Reactive power (kvar) measurements at the sensor. Is converted into Currents along with p=[...]

        DSS property name: `kvars`, DSS property index: 8.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 8)

    def _set_kvars(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(8, value, flags)

    kvars = property(_get_kvars, _set_kvars) # type: Float64Array

    def _get_Conn(self) -> enums.Connection:
        """
        Voltage sensor Connection: { wye | delta | LN | LL }.  Default is wye. Applies to voltage measurement only. 
        Currents are always assumed to be line currents.
        If wye or LN, voltage is assumed measured line-neutral; otherwise, line-line.

        DSS property name: `Conn`, DSS property index: 9.
        """
        return enums.Connection(self._lib.Obj_GetInt32(self._ptr, 9))

    def _set_Conn(self, value: Union[AnyStr, int, enums.Connection], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(9, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 9, value, flags)

    Conn = property(_get_Conn, _set_Conn) # type: enums.Connection

    def _get_Conn_str(self) -> str:
        """
        Voltage sensor Connection: { wye | delta | LN | LL }.  Default is wye. Applies to voltage measurement only. 
        Currents are always assumed to be line currents.
        If wye or LN, voltage is assumed measured line-neutral; otherwise, line-line.

        DSS property name: `Conn`, DSS property index: 9.
        """
        return self._get_prop_string(9)

    def _set_Conn_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Conn(value, flags)

    Conn_str = property(_get_Conn_str, _set_Conn_str) # type: str

    def _get_DeltaDirection(self) -> int:
        """
        {1 or -1}  Default is 1:  1-2, 2-3, 3-1.  For reverse rotation, enter -1. Any positive or negative entry will suffice.

        DSS property name: `DeltaDirection`, DSS property index: 10.
        """
        return self._lib.Obj_GetInt32(self._ptr, 10)

    def _set_DeltaDirection(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 10, value, flags)

    DeltaDirection = property(_get_DeltaDirection, _set_DeltaDirection) # type: int

    def _get_pctError(self) -> float:
        """
        Assumed percent error in the measurement. Default is 1.

        DSS property name: `%Error`, DSS property index: 11.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    def _set_pctError(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 11, value, flags)

    pctError = property(_get_pctError, _set_pctError) # type: float

    def _get_Weight(self) -> float:
        """
        Weighting factor: Default is 1.

        DSS property name: `Weight`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    def _set_Weight(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 12, value, flags)

    Weight = property(_get_Weight, _set_Weight) # type: float

    def _get_BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 13, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float

    def _get_Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 14.
        """
        return self._lib.Obj_GetInt32(self._ptr, 14) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 14, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 15.
        """
        self._set_string_o(15, value)


class SensorProperties(TypedDict):
    Element: Union[AnyStr, DSSObj]
    Terminal: int
    kVBase: float
    Clear: bool
    kVs: Float64Array
    Currents: Float64Array
    kWs: Float64Array
    kvars: Float64Array
    Conn: Union[AnyStr, int, enums.Connection]
    DeltaDirection: int
    pctError: float
    Weight: float
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class SensorBatch(DSSBatch, CircuitElementBatchMixin):
    _cls_name = 'Sensor'
    _obj_cls = Sensor
    _cls_idx = 49

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)

    def _get_Element_str(self) -> List[str]:
        """
        Name (Full Object name) of element to which the Sensor is connected.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_batch_str_prop(1)

    def _set_Element_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(1, value, flags)

    Element_str = property(_get_Element_str, _set_Element_str) # type: List[str]

    def _get_Element(self) -> List[DSSObj]:
        """
        Name (Full Object name) of element to which the Sensor is connected.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_batch_obj_prop(1)

    def _set_Element(self, value: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(1, value, flags)

    Element = property(_get_Element, _set_Element) # type: List[DSSObj]

    def _get_Terminal(self) -> BatchInt32ArrayProxy:
        """
        Number of the terminal of the circuit element to which the Sensor is connected. 1 or 2, typically. Default is 1.

        DSS property name: `Terminal`, DSS property index: 2.
        """
        return BatchInt32ArrayProxy(self, 2)

    def _set_Terminal(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(2, value, flags)

    Terminal = property(_get_Terminal, _set_Terminal) # type: BatchInt32ArrayProxy

    def _get_kVBase(self) -> BatchFloat64ArrayProxy:
        """
        Voltage base for the sensor, in kV. If connected to a 2- or 3-phase terminal, 
        specify L-L voltage. For 1-phase devices specify L-N or actual 1-phase voltage. Like many other DSS devices, default is 12.47kV.

        DSS property name: `kVBase`, DSS property index: 3.
        """
        return BatchFloat64ArrayProxy(self, 3)

    def _set_kVBase(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(3, value, flags)

    kVBase = property(_get_kVBase, _set_kVBase) # type: BatchFloat64ArrayProxy

    def Clear(self, value: Union[bool, List[bool]] = True, flags: enums.SetterFlags = 0):
        """
        { Yes | No }. Clear=Yes clears sensor values. Should be issued before putting in a new set of measurements.

        DSS property name: `Clear`, DSS property index: 4.
        """
        self._set_batch_int32_array(4, value, flags)

    def _get_kVs(self) -> List[Float64Array]:
        """
        Array of Voltages (kV) measured by the voltage sensor. For Delta-connected sensors, Line-Line voltages are expected. For Wye, Line-Neutral are expected.

        DSS property name: `kVs`, DSS property index: 5.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 5)
            for x in self._unpack()
        ]

    def _set_kVs(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(5, value, flags)

    kVs = property(_get_kVs, _set_kVs) # type: List[Float64Array]

    def _get_Currents(self) -> List[Float64Array]:
        """
        Array of Currents (amps) measured by the current sensor. Specify this or power quantities; not both.

        DSS property name: `Currents`, DSS property index: 6.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 6)
            for x in self._unpack()
        ]

    def _set_Currents(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(6, value, flags)

    Currents = property(_get_Currents, _set_Currents) # type: List[Float64Array]

    def _get_kWs(self) -> List[Float64Array]:
        """
        Array of Active power (kW) measurements at the sensor. Is converted into Currents along with q=[...]
        Will override any currents=[...] specification.

        DSS property name: `kWs`, DSS property index: 7.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 7)
            for x in self._unpack()
        ]

    def _set_kWs(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(7, value, flags)

    kWs = property(_get_kWs, _set_kWs) # type: List[Float64Array]

    def _get_kvars(self) -> List[Float64Array]:
        """
        Array of Reactive power (kvar) measurements at the sensor. Is converted into Currents along with p=[...]

        DSS property name: `kvars`, DSS property index: 8.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 8)
            for x in self._unpack()
        ]

    def _set_kvars(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(8, value, flags)

    kvars = property(_get_kvars, _set_kvars) # type: List[Float64Array]

    def _get_Conn(self) -> BatchInt32ArrayProxy:
        """
        Voltage sensor Connection: { wye | delta | LN | LL }.  Default is wye. Applies to voltage measurement only. 
        Currents are always assumed to be line currents.
        If wye or LN, voltage is assumed measured line-neutral; otherwise, line-line.

        DSS property name: `Conn`, DSS property index: 9.
        """
        return BatchInt32ArrayProxy(self, 9)

    def _set_Conn(self, value: Union[AnyStr, int, enums.Connection, List[AnyStr], List[int], List[enums.Connection], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(9, value, flags)
            return

        self._set_batch_int32_array(9, value, flags)

    Conn = property(_get_Conn, _set_Conn) # type: BatchInt32ArrayProxy

    def _get_Conn_str(self) -> List[str]:
        """
        Voltage sensor Connection: { wye | delta | LN | LL }.  Default is wye. Applies to voltage measurement only. 
        Currents are always assumed to be line currents.
        If wye or LN, voltage is assumed measured line-neutral; otherwise, line-line.

        DSS property name: `Conn`, DSS property index: 9.
        """
        return self._get_batch_str_prop(9)

    def _set_Conn_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Conn(value, flags)

    Conn_str = property(_get_Conn_str, _set_Conn_str) # type: List[str]

    def _get_DeltaDirection(self) -> BatchInt32ArrayProxy:
        """
        {1 or -1}  Default is 1:  1-2, 2-3, 3-1.  For reverse rotation, enter -1. Any positive or negative entry will suffice.

        DSS property name: `DeltaDirection`, DSS property index: 10.
        """
        return BatchInt32ArrayProxy(self, 10)

    def _set_DeltaDirection(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(10, value, flags)

    DeltaDirection = property(_get_DeltaDirection, _set_DeltaDirection) # type: BatchInt32ArrayProxy

    def _get_pctError(self) -> BatchFloat64ArrayProxy:
        """
        Assumed percent error in the measurement. Default is 1.

        DSS property name: `%Error`, DSS property index: 11.
        """
        return BatchFloat64ArrayProxy(self, 11)

    def _set_pctError(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(11, value, flags)

    pctError = property(_get_pctError, _set_pctError) # type: BatchFloat64ArrayProxy

    def _get_Weight(self) -> BatchFloat64ArrayProxy:
        """
        Weighting factor: Default is 1.

        DSS property name: `Weight`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    def _set_Weight(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(12, value, flags)

    Weight = property(_get_Weight, _set_Weight) # type: BatchFloat64ArrayProxy

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(13, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy

    def _get_Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 14.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(14)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(14, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 15.
        """
        self._set_batch_string(15, value, flags)

class SensorBatchProperties(TypedDict):
    Element: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]]
    Terminal: Union[int, Int32Array]
    kVBase: Union[float, Float64Array]
    Clear: bool
    kVs: Float64Array
    Currents: Float64Array
    kWs: Float64Array
    kvars: Float64Array
    Conn: Union[AnyStr, int, enums.Connection, List[AnyStr], List[int], List[enums.Connection], Int32Array]
    DeltaDirection: Union[int, Int32Array]
    pctError: Union[float, Float64Array]
    Weight: Union[float, Float64Array]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

#TODO: warn that begin_edit=False with extra params will be ignored?

class ISensor(IDSSObj, SensorBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, Sensor, SensorBatch)
        SensorBatch.__init__(self, self._api_util, sync_cls_idx=Sensor._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Sensor:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[SensorProperties]) -> Sensor:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[SensorBatchProperties]) -> SensorBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
