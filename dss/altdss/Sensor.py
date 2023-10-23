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

class Sensor(DSSObj, CktElementMixin):
    __slots__ = CktElementMixin._extra_slots
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

    @property
    def Element(self) -> str:
        """
        Name (Full Object name) of element to which the Sensor is connected.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    @Element.setter
    def Element(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_obj(1, value)
            return

        self._set_string_o(1, value)

    @property
    def Element_obj(self) -> DSSObj:
        """
        Name (Full Object name) of element to which the Sensor is connected.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_obj(1, None)

    @Element_obj.setter
    def Element_obj(self, value: DSSObj):
        self._set_obj(1, value)

    @property
    def Terminal(self) -> int:
        """
        Number of the terminal of the circuit element to which the Sensor is connected. 1 or 2, typically. Default is 1.

        DSS property name: `Terminal`, DSS property index: 2.
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @Terminal.setter
    def Terminal(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    @property
    def kVBase(self) -> float:
        """
        Voltage base for the sensor, in kV. If connected to a 2- or 3-phase terminal, 
        specify L-L voltage. For 1-phase devices specify L-N or actual 1-phase voltage. Like many other DSS devices, default is 12.47kV.

        DSS property name: `kVBase`, DSS property index: 3.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @kVBase.setter
    def kVBase(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    def Clear(self, value: bool = True):
        """
        { Yes | No }. Clear=Yes clears sensor values. Should be issued before putting in a new set of measurements.

        DSS property name: `Clear`, DSS property index: 4.
        """
        self._lib.Obj_SetInt32(self._ptr, 4, value)

    @property
    def kVs(self) -> Float64Array:
        """
        Array of Voltages (kV) measured by the voltage sensor. For Delta-connected sensors, Line-Line voltages are expected. For Wye, Line-Neutral are expected.

        DSS property name: `kVs`, DSS property index: 5.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 5)

    @kVs.setter
    def kVs(self, value: Float64Array):
        self._set_float64_array_o(5, value)

    @property
    def Currents(self) -> Float64Array:
        """
        Array of Currents (amps) measured by the current sensor. Specify this or power quantities; not both.

        DSS property name: `Currents`, DSS property index: 6.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 6)

    @Currents.setter
    def Currents(self, value: Float64Array):
        self._set_float64_array_o(6, value)

    @property
    def kWs(self) -> Float64Array:
        """
        Array of Active power (kW) measurements at the sensor. Is converted into Currents along with q=[...]
        Will override any currents=[...] specification.

        DSS property name: `kWs`, DSS property index: 7.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 7)

    @kWs.setter
    def kWs(self, value: Float64Array):
        self._set_float64_array_o(7, value)

    @property
    def kvars(self) -> Float64Array:
        """
        Array of Reactive power (kvar) measurements at the sensor. Is converted into Currents along with p=[...]

        DSS property name: `kvars`, DSS property index: 8.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 8)

    @kvars.setter
    def kvars(self, value: Float64Array):
        self._set_float64_array_o(8, value)

    @property
    def Conn(self) -> enums.Connection:
        """
        Voltage sensor Connection: { wye | delta | LN | LL }.  Default is wye. Applies to voltage measurement only. 
        Currents are always assumed to be line currents.
        If wye or LN, voltage is assumed measured line-neutral; otherwise, line-line.

        DSS property name: `Conn`, DSS property index: 9.
        """
        return enums.Connection(self._lib.Obj_GetInt32(self._ptr, 9))

    @Conn.setter
    def Conn(self, value: Union[AnyStr, int, enums.Connection]):
        if not isinstance(value, int):
            self._set_string_o(9, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 9, value)

    @property
    def Conn_str(self) -> str:
        """
        Voltage sensor Connection: { wye | delta | LN | LL }.  Default is wye. Applies to voltage measurement only. 
        Currents are always assumed to be line currents.
        If wye or LN, voltage is assumed measured line-neutral; otherwise, line-line.

        DSS property name: `Conn`, DSS property index: 9.
        """
        return self._get_prop_string(9)

    @Conn_str.setter
    def Conn_str(self, value: AnyStr):
        self.Conn = value

    @property
    def DeltaDirection(self) -> int:
        """
        {1 or -1}  Default is 1:  1-2, 2-3, 3-1.  For reverse rotation, enter -1. Any positive or negative entry will suffice.

        DSS property name: `DeltaDirection`, DSS property index: 10.
        """
        return self._lib.Obj_GetInt32(self._ptr, 10)

    @DeltaDirection.setter
    def DeltaDirection(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 10, value)

    @property
    def pctError(self) -> float:
        """
        Assumed percent error in the measurement. Default is 1.

        DSS property name: `%Error`, DSS property index: 11.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @pctError.setter
    def pctError(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def Weight(self) -> float:
        """
        Weighting factor: Default is 1.

        DSS property name: `Weight`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @Weight.setter
    def Weight(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @BaseFreq.setter
    def BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 14.
        """
        return self._lib.Obj_GetInt32(self._ptr, 14) != 0

    @Enabled.setter
    def Enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 14, value)

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

class SensorBatch(DSSBatch):
    _cls_name = 'Sensor'
    _obj_cls = Sensor
    _cls_idx = 49


    @property
    def Element(self) -> List[str]:
        """
        Name (Full Object name) of element to which the Sensor is connected.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @Element.setter
    def Element(self, value: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]]):
        self._set_batch_obj_prop(1, value)

    @property
    def Element_obj(self) -> List[DSSObj]:
        """
        Name (Full Object name) of element to which the Sensor is connected.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 1)

    @Element_obj.setter
    def Element_obj(self, value: DSSObj):
        self._set_batch_string(1, value)

    @property
    def Terminal(self) -> BatchInt32ArrayProxy:
        """
        Number of the terminal of the circuit element to which the Sensor is connected. 1 or 2, typically. Default is 1.

        DSS property name: `Terminal`, DSS property index: 2.
        """
        return BatchInt32ArrayProxy(self, 2)

    @Terminal.setter
    def Terminal(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(2, value)

    @property
    def kVBase(self) -> BatchFloat64ArrayProxy:
        """
        Voltage base for the sensor, in kV. If connected to a 2- or 3-phase terminal, 
        specify L-L voltage. For 1-phase devices specify L-N or actual 1-phase voltage. Like many other DSS devices, default is 12.47kV.

        DSS property name: `kVBase`, DSS property index: 3.
        """
        return BatchFloat64ArrayProxy(self, 3)

    @kVBase.setter
    def kVBase(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(3, value)

    def Clear(self, value: Union[bool, List[bool]] = True):
        """
        { Yes | No }. Clear=Yes clears sensor values. Should be issued before putting in a new set of measurements.

        DSS property name: `Clear`, DSS property index: 4.
        """
        self._set_batch_int32_array(4, value)

    @property
    def kVs(self) -> List[Float64Array]:
        """
        Array of Voltages (kV) measured by the voltage sensor. For Delta-connected sensors, Line-Line voltages are expected. For Wye, Line-Neutral are expected.

        DSS property name: `kVs`, DSS property index: 5.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 5)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @kVs.setter
    def kVs(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(5, value)

    @property
    def Currents(self) -> List[Float64Array]:
        """
        Array of Currents (amps) measured by the current sensor. Specify this or power quantities; not both.

        DSS property name: `Currents`, DSS property index: 6.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 6)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Currents.setter
    def Currents(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(6, value)

    @property
    def kWs(self) -> List[Float64Array]:
        """
        Array of Active power (kW) measurements at the sensor. Is converted into Currents along with q=[...]
        Will override any currents=[...] specification.

        DSS property name: `kWs`, DSS property index: 7.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 7)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @kWs.setter
    def kWs(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(7, value)

    @property
    def kvars(self) -> List[Float64Array]:
        """
        Array of Reactive power (kvar) measurements at the sensor. Is converted into Currents along with p=[...]

        DSS property name: `kvars`, DSS property index: 8.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 8)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @kvars.setter
    def kvars(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(8, value)

    @property
    def Conn(self) -> BatchInt32ArrayProxy:
        """
        Voltage sensor Connection: { wye | delta | LN | LL }.  Default is wye. Applies to voltage measurement only. 
        Currents are always assumed to be line currents.
        If wye or LN, voltage is assumed measured line-neutral; otherwise, line-line.

        DSS property name: `Conn`, DSS property index: 9.
        """
        return BatchInt32ArrayProxy(self, 9)

    @Conn.setter
    def Conn(self, value: Union[AnyStr, int, enums.Connection, List[AnyStr], List[int], List[enums.Connection], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(9, value)
            return
    
        self._set_batch_int32_array(9, value)

    @property
    def Conn_str(self) -> str:
        """
        Voltage sensor Connection: { wye | delta | LN | LL }.  Default is wye. Applies to voltage measurement only. 
        Currents are always assumed to be line currents.
        If wye or LN, voltage is assumed measured line-neutral; otherwise, line-line.

        DSS property name: `Conn`, DSS property index: 9.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 9)

    @Conn_str.setter
    def Conn_str(self, value: AnyStr):
        self.Conn = value

    @property
    def DeltaDirection(self) -> BatchInt32ArrayProxy:
        """
        {1 or -1}  Default is 1:  1-2, 2-3, 3-1.  For reverse rotation, enter -1. Any positive or negative entry will suffice.

        DSS property name: `DeltaDirection`, DSS property index: 10.
        """
        return BatchInt32ArrayProxy(self, 10)

    @DeltaDirection.setter
    def DeltaDirection(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(10, value)

    @property
    def pctError(self) -> BatchFloat64ArrayProxy:
        """
        Assumed percent error in the measurement. Default is 1.

        DSS property name: `%Error`, DSS property index: 11.
        """
        return BatchFloat64ArrayProxy(self, 11)

    @pctError.setter
    def pctError(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(11, value)

    @property
    def Weight(self) -> BatchFloat64ArrayProxy:
        """
        Weighting factor: Default is 1.

        DSS property name: `Weight`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    @Weight.setter
    def Weight(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(12, value)

    @property
    def BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    @BaseFreq.setter
    def BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(13, value)

    @property
    def Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 14.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 14)
        ]
    @Enabled.setter
    def Enabled(self, value: bool):
        self._set_batch_int32_array(14, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 15.
        """
        self._set_batch_string(15, value)

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

class ISensor(IDSSObj):
    __slots__ = ()

    def __init__(self, iobj):
        super().__init__(iobj, Sensor, SensorBatch)

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Sensor:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[SensorProperties]) -> Sensor:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[SensorBatchProperties]) -> SensorBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
