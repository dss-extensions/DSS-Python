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

class Capacitor(DSSObj, CircuitElementMixin, PDElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots + PDElementMixin._extra_slots
    _cls_name = 'Capacitor'
    _cls_idx = 22
    _cls_prop_idx = {
        'bus1': 1,
        'bus2': 2,
        'phases': 3,
        'kvar': 4,
        'kv': 5,
        'conn': 6,
        'cmatrix': 7,
        'cuf': 8,
        'r': 9,
        'xl': 10,
        'harm': 11,
        'numsteps': 12,
        'states': 13,
        'normamps': 14,
        'emergamps': 15,
        'faultrate': 16,
        'pctperm': 17,
        'repair': 18,
        'basefreq': 19,
        'enabled': 20,
        'like': 21,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)
       PDElementMixin.__init__(self)

    def _get_Bus1(self) -> str:
        """
        Name of first bus of 2-terminal capacitor. Examples:
        bus1=busname
        bus1=busname.1.2.3

        If only one bus specified, Bus2 will default to this bus, Node 0, and the capacitor will be a Yg shunt bank.

        DSS property name: `Bus1`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    def _set_Bus1(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(1, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: str

    def _get_Bus2(self) -> str:
        """
        Name of 2nd bus. Defaults to all phases connected to first bus, node 0, (Shunt Wye Connection) except when Bus2 explicitly specified. 

        Not necessary to specify for delta (LL) connection.

        DSS property name: `Bus2`, DSS property index: 2.
        """
        return self._get_prop_string(2)

    def _set_Bus2(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(2, value, flags)

    Bus2 = property(_get_Bus2, _set_Bus2) # type: str

    def _get_Phases(self) -> int:
        """
        Number of phases.

        DSS property name: `Phases`, DSS property index: 3.
        """
        return self._lib.Obj_GetInt32(self._ptr, 3)

    def _set_Phases(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 3, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: int

    def _get_kvar(self) -> Float64Array:
        """
        Total kvar, if one step, or ARRAY of kvar ratings for each step.  Evenly divided among phases. See rules for NUMSTEPS.

        DSS property name: `kvar`, DSS property index: 4.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 4)

    def _set_kvar(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(4, value, flags)

    kvar = property(_get_kvar, _set_kvar) # type: Float64Array

    def _get_kV(self) -> float:
        """
        For 2, 3-phase, kV phase-phase. Otherwise specify actual can rating.

        DSS property name: `kV`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    def _set_kV(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 5, value, flags)

    kV = property(_get_kV, _set_kV) # type: float

    def _get_Conn(self) -> enums.Connection:
        """
        ={wye | delta |LN |LL}  Default is wye, which is equivalent to LN

        DSS property name: `Conn`, DSS property index: 6.
        """
        return enums.Connection(self._lib.Obj_GetInt32(self._ptr, 6))

    def _set_Conn(self, value: Union[AnyStr, int, enums.Connection], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(6, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 6, value, flags)

    Conn = property(_get_Conn, _set_Conn) # type: enums.Connection

    def _get_Conn_str(self) -> str:
        """
        ={wye | delta |LN |LL}  Default is wye, which is equivalent to LN

        DSS property name: `Conn`, DSS property index: 6.
        """
        return self._get_prop_string(6)

    def _set_Conn_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Conn(value, flags)

    Conn_str = property(_get_Conn_str, _set_Conn_str) # type: str

    def _get_CMatrix(self) -> Float64Array:
        """
        Nodal cap. matrix, lower triangle, microfarads, of the following form:

        cmatrix="c11 | -c21 c22 | -c31 -c32 c33"

        All steps are assumed the same if this property is used.

        DSS property name: `CMatrix`, DSS property index: 7.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 7)

    def _set_CMatrix(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(7, value, flags)

    CMatrix = property(_get_CMatrix, _set_CMatrix) # type: Float64Array

    def _get_Cuf(self) -> Float64Array:
        """
        ARRAY of Capacitance, each phase, for each step, microfarads.
        See Rules for NumSteps.

        DSS property name: `Cuf`, DSS property index: 8.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 8)

    def _set_Cuf(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(8, value, flags)

    Cuf = property(_get_Cuf, _set_Cuf) # type: Float64Array

    def _get_R(self) -> Float64Array:
        """
        ARRAY of series resistance in each phase (line), ohms. Default is 0.0

        DSS property name: `R`, DSS property index: 9.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 9)

    def _set_R(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(9, value, flags)

    R = property(_get_R, _set_R) # type: Float64Array

    def _get_XL(self) -> Float64Array:
        """
        ARRAY of series inductive reactance(s) in each phase (line) for filter, ohms at base frequency. Use this OR "h" property to define filter. Default is 0.0.

        DSS property name: `XL`, DSS property index: 10.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 10)

    def _set_XL(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(10, value, flags)

    XL = property(_get_XL, _set_XL) # type: Float64Array

    def _get_Harm(self) -> Float64Array:
        """
        ARRAY of harmonics to which each step is tuned. Zero is interpreted as meaning zero reactance (no filter). Default is zero.

        DSS property name: `Harm`, DSS property index: 11.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 11)

    def _set_Harm(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(11, value, flags)

    Harm = property(_get_Harm, _set_Harm) # type: Float64Array

    def _get_NumSteps(self) -> int:
        """
        Number of steps in this capacitor bank. Default = 1. Forces reallocation of the capacitance, reactor, and states array.  Rules: If this property was previously =1, the value in the kvar property is divided equally among the steps. The kvar property does not need to be reset if that is accurate.  If the Cuf or Cmatrix property was used previously, all steps are set to the value of the first step. The states property is set to all steps on. All filter steps are set to the same harmonic. If this property was previously >1, the arrays are reallocated, but no values are altered. You must SUBSEQUENTLY assign all array properties.

        DSS property name: `NumSteps`, DSS property index: 12.
        """
        return self._lib.Obj_GetInt32(self._ptr, 12)

    def _set_NumSteps(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 12, value, flags)

    NumSteps = property(_get_NumSteps, _set_NumSteps) # type: int

    def _get_States(self) -> Int32Array:
        """
        ARRAY of integers {1|0} states representing the state of each step (on|off). Defaults to 1 when reallocated (on). Capcontrol will modify this array as it turns steps on or off.

        DSS property name: `States`, DSS property index: 13.
        """
        return self._get_int32_array(self._lib.Obj_GetInt32Array, self._ptr, 13)

    def _set_States(self, value: Int32Array, flags: enums.SetterFlags = 0):
        self._set_int32_array_o(13, value, flags)

    States = property(_get_States, _set_States) # type: Int32Array

    def _get_NormAmps(self) -> float:
        """
        Normal rated current. Defaults to 180% of per-phase rated current.

        DSS property name: `NormAmps`, DSS property index: 14.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    def _set_NormAmps(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 14, value, flags)

    NormAmps = property(_get_NormAmps, _set_NormAmps) # type: float

    def _get_EmergAmps(self) -> float:
        """
        Maximum or emerg current. Defaults to 180% of per-phase rated current.

        DSS property name: `EmergAmps`, DSS property index: 15.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    def _set_EmergAmps(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 15, value, flags)

    EmergAmps = property(_get_EmergAmps, _set_EmergAmps) # type: float

    def _get_FaultRate(self) -> float:
        """
        Failure rate per year.

        DSS property name: `FaultRate`, DSS property index: 16.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    def _set_FaultRate(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 16, value, flags)

    FaultRate = property(_get_FaultRate, _set_FaultRate) # type: float

    def _get_pctPerm(self) -> float:
        """
        Percent of failures that become permanent.

        DSS property name: `pctPerm`, DSS property index: 17.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    def _set_pctPerm(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 17, value, flags)

    pctPerm = property(_get_pctPerm, _set_pctPerm) # type: float

    def _get_Repair(self) -> float:
        """
        Hours to repair.

        DSS property name: `Repair`, DSS property index: 18.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    def _set_Repair(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 18, value, flags)

    Repair = property(_get_Repair, _set_Repair) # type: float

    def _get_BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 19.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 19, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float

    def _get_Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 20.
        """
        return self._lib.Obj_GetInt32(self._ptr, 20) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 20, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 21.
        """
        self._set_string_o(21, value)


class CapacitorProperties(TypedDict):
    Bus1: AnyStr
    Bus2: AnyStr
    Phases: int
    kvar: Float64Array
    kV: float
    Conn: Union[AnyStr, int, enums.Connection]
    CMatrix: Float64Array
    Cuf: Float64Array
    R: Float64Array
    XL: Float64Array
    Harm: Float64Array
    NumSteps: int
    States: Int32Array
    NormAmps: float
    EmergAmps: float
    FaultRate: float
    pctPerm: float
    Repair: float
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class CapacitorBatch(DSSBatch, CircuitElementBatchMixin, PDElementBatchMixin):
    _cls_name = 'Capacitor'
    _obj_cls = Capacitor
    _cls_idx = 22

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)
       PDElementBatchMixin.__init__(self)

    def _get_Bus1(self) -> List[str]:
        """
        Name of first bus of 2-terminal capacitor. Examples:
        bus1=busname
        bus1=busname.1.2.3

        If only one bus specified, Bus2 will default to this bus, Node 0, and the capacitor will be a Yg shunt bank.

        DSS property name: `Bus1`, DSS property index: 1.
        """
        return self._get_batch_str_prop(1)

    def _set_Bus1(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(1, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: List[str]

    def _get_Bus2(self) -> List[str]:
        """
        Name of 2nd bus. Defaults to all phases connected to first bus, node 0, (Shunt Wye Connection) except when Bus2 explicitly specified. 

        Not necessary to specify for delta (LL) connection.

        DSS property name: `Bus2`, DSS property index: 2.
        """
        return self._get_batch_str_prop(2)

    def _set_Bus2(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(2, value, flags)

    Bus2 = property(_get_Bus2, _set_Bus2) # type: List[str]

    def _get_Phases(self) -> BatchInt32ArrayProxy:
        """
        Number of phases.

        DSS property name: `Phases`, DSS property index: 3.
        """
        return BatchInt32ArrayProxy(self, 3)

    def _set_Phases(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(3, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: BatchInt32ArrayProxy

    def _get_kvar(self) -> List[Float64Array]:
        """
        Total kvar, if one step, or ARRAY of kvar ratings for each step.  Evenly divided among phases. See rules for NUMSTEPS.

        DSS property name: `kvar`, DSS property index: 4.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 4)
            for x in self._unpack()
        ]

    def _set_kvar(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(4, value, flags)

    kvar = property(_get_kvar, _set_kvar) # type: List[Float64Array]

    def _get_kV(self) -> BatchFloat64ArrayProxy:
        """
        For 2, 3-phase, kV phase-phase. Otherwise specify actual can rating.

        DSS property name: `kV`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    def _set_kV(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(5, value, flags)

    kV = property(_get_kV, _set_kV) # type: BatchFloat64ArrayProxy

    def _get_Conn(self) -> BatchInt32ArrayProxy:
        """
        ={wye | delta |LN |LL}  Default is wye, which is equivalent to LN

        DSS property name: `Conn`, DSS property index: 6.
        """
        return BatchInt32ArrayProxy(self, 6)

    def _set_Conn(self, value: Union[AnyStr, int, enums.Connection, List[AnyStr], List[int], List[enums.Connection], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(6, value, flags)
            return

        self._set_batch_int32_array(6, value, flags)

    Conn = property(_get_Conn, _set_Conn) # type: BatchInt32ArrayProxy

    def _get_Conn_str(self) -> List[str]:
        """
        ={wye | delta |LN |LL}  Default is wye, which is equivalent to LN

        DSS property name: `Conn`, DSS property index: 6.
        """
        return self._get_batch_str_prop(6)

    def _set_Conn_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Conn(value, flags)

    Conn_str = property(_get_Conn_str, _set_Conn_str) # type: List[str]

    def _get_CMatrix(self) -> List[Float64Array]:
        """
        Nodal cap. matrix, lower triangle, microfarads, of the following form:

        cmatrix="c11 | -c21 c22 | -c31 -c32 c33"

        All steps are assumed the same if this property is used.

        DSS property name: `CMatrix`, DSS property index: 7.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 7)
            for x in self._unpack()
        ]

    def _set_CMatrix(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(7, value, flags)

    CMatrix = property(_get_CMatrix, _set_CMatrix) # type: List[Float64Array]

    def _get_Cuf(self) -> List[Float64Array]:
        """
        ARRAY of Capacitance, each phase, for each step, microfarads.
        See Rules for NumSteps.

        DSS property name: `Cuf`, DSS property index: 8.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 8)
            for x in self._unpack()
        ]

    def _set_Cuf(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(8, value, flags)

    Cuf = property(_get_Cuf, _set_Cuf) # type: List[Float64Array]

    def _get_R(self) -> List[Float64Array]:
        """
        ARRAY of series resistance in each phase (line), ohms. Default is 0.0

        DSS property name: `R`, DSS property index: 9.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 9)
            for x in self._unpack()
        ]

    def _set_R(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(9, value, flags)

    R = property(_get_R, _set_R) # type: List[Float64Array]

    def _get_XL(self) -> List[Float64Array]:
        """
        ARRAY of series inductive reactance(s) in each phase (line) for filter, ohms at base frequency. Use this OR "h" property to define filter. Default is 0.0.

        DSS property name: `XL`, DSS property index: 10.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 10)
            for x in self._unpack()
        ]

    def _set_XL(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(10, value, flags)

    XL = property(_get_XL, _set_XL) # type: List[Float64Array]

    def _get_Harm(self) -> List[Float64Array]:
        """
        ARRAY of harmonics to which each step is tuned. Zero is interpreted as meaning zero reactance (no filter). Default is zero.

        DSS property name: `Harm`, DSS property index: 11.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 11)
            for x in self._unpack()
        ]

    def _set_Harm(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(11, value, flags)

    Harm = property(_get_Harm, _set_Harm) # type: List[Float64Array]

    def _get_NumSteps(self) -> BatchInt32ArrayProxy:
        """
        Number of steps in this capacitor bank. Default = 1. Forces reallocation of the capacitance, reactor, and states array.  Rules: If this property was previously =1, the value in the kvar property is divided equally among the steps. The kvar property does not need to be reset if that is accurate.  If the Cuf or Cmatrix property was used previously, all steps are set to the value of the first step. The states property is set to all steps on. All filter steps are set to the same harmonic. If this property was previously >1, the arrays are reallocated, but no values are altered. You must SUBSEQUENTLY assign all array properties.

        DSS property name: `NumSteps`, DSS property index: 12.
        """
        return BatchInt32ArrayProxy(self, 12)

    def _set_NumSteps(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(12, value, flags)

    NumSteps = property(_get_NumSteps, _set_NumSteps) # type: BatchInt32ArrayProxy

    def _get_States(self) -> List[Int32Array]:
        """
        ARRAY of integers {1|0} states representing the state of each step (on|off). Defaults to 1 when reallocated (on). Capcontrol will modify this array as it turns steps on or off.

        DSS property name: `States`, DSS property index: 13.
        """
        return [
            self._get_int32_array(self._lib.Obj_GetInt32Array, x, 13)
            for x in self._unpack()
        ]

    def _set_States(self, value: Union[Int32Array, List[Int32Array]], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array_prop(13, value, flags)

    States = property(_get_States, _set_States) # type: List[Int32Array]

    def _get_NormAmps(self) -> BatchFloat64ArrayProxy:
        """
        Normal rated current. Defaults to 180% of per-phase rated current.

        DSS property name: `NormAmps`, DSS property index: 14.
        """
        return BatchFloat64ArrayProxy(self, 14)

    def _set_NormAmps(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(14, value, flags)

    NormAmps = property(_get_NormAmps, _set_NormAmps) # type: BatchFloat64ArrayProxy

    def _get_EmergAmps(self) -> BatchFloat64ArrayProxy:
        """
        Maximum or emerg current. Defaults to 180% of per-phase rated current.

        DSS property name: `EmergAmps`, DSS property index: 15.
        """
        return BatchFloat64ArrayProxy(self, 15)

    def _set_EmergAmps(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(15, value, flags)

    EmergAmps = property(_get_EmergAmps, _set_EmergAmps) # type: BatchFloat64ArrayProxy

    def _get_FaultRate(self) -> BatchFloat64ArrayProxy:
        """
        Failure rate per year.

        DSS property name: `FaultRate`, DSS property index: 16.
        """
        return BatchFloat64ArrayProxy(self, 16)

    def _set_FaultRate(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(16, value, flags)

    FaultRate = property(_get_FaultRate, _set_FaultRate) # type: BatchFloat64ArrayProxy

    def _get_pctPerm(self) -> BatchFloat64ArrayProxy:
        """
        Percent of failures that become permanent.

        DSS property name: `pctPerm`, DSS property index: 17.
        """
        return BatchFloat64ArrayProxy(self, 17)

    def _set_pctPerm(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(17, value, flags)

    pctPerm = property(_get_pctPerm, _set_pctPerm) # type: BatchFloat64ArrayProxy

    def _get_Repair(self) -> BatchFloat64ArrayProxy:
        """
        Hours to repair.

        DSS property name: `Repair`, DSS property index: 18.
        """
        return BatchFloat64ArrayProxy(self, 18)

    def _set_Repair(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(18, value, flags)

    Repair = property(_get_Repair, _set_Repair) # type: BatchFloat64ArrayProxy

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 19.
        """
        return BatchFloat64ArrayProxy(self, 19)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(19, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy

    def _get_Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 20.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(20)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(20, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 21.
        """
        self._set_batch_string(21, value, flags)

class CapacitorBatchProperties(TypedDict):
    Bus1: Union[AnyStr, List[AnyStr]]
    Bus2: Union[AnyStr, List[AnyStr]]
    Phases: Union[int, Int32Array]
    kvar: Float64Array
    kV: Union[float, Float64Array]
    Conn: Union[AnyStr, int, enums.Connection, List[AnyStr], List[int], List[enums.Connection], Int32Array]
    CMatrix: Float64Array
    Cuf: Float64Array
    R: Float64Array
    XL: Float64Array
    Harm: Float64Array
    NumSteps: Union[int, Int32Array]
    States: Int32Array
    NormAmps: Union[float, Float64Array]
    EmergAmps: Union[float, Float64Array]
    FaultRate: Union[float, Float64Array]
    pctPerm: Union[float, Float64Array]
    Repair: Union[float, Float64Array]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class ICapacitor(IDSSObj, CapacitorBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, Capacitor, CapacitorBatch)
        CapacitorBatch.__init__(self, self._api_util, sync_cls_idx=Capacitor._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Capacitor:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[CapacitorProperties]) -> Capacitor:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[CapacitorBatchProperties]) -> CapacitorBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
