# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from typing_extensions import TypedDict, Unpack
from ._obj_bases import (
    CircuitElementMixin,
    PDElementMixin,
    CircuitElementBatchMixin,
    PDElementBatchMixin,
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

class Fault(DSSObj, CircuitElementMixin, PDElementMixin):
    __slots__ = CircuitElementMixin._extra_slots + PDElementMixin._extra_slots
    _cls_name = 'Fault'
    _cls_idx = 25
    _cls_prop_idx = {
        'bus1': 1,
        'bus2': 2,
        'phases': 3,
        'r': 4,
        'pctstddev': 5,
        '%stddev': 5,
        'gmatrix': 6,
        'ontime': 7,
        'temporary': 8,
        'minamps': 9,
        'normamps': 10,
        'emergamps': 11,
        'faultrate': 12,
        'pctperm': 13,
        'repair': 14,
        'basefreq': 15,
        'enabled': 16,
        'like': 17,
    }

    def _get_Bus1(self) -> str:
        """
        Name of first bus. Examples:

        bus1=busname
        bus1=busname.1.2.3

        Bus2 automatically defaults to busname.0,0,0 unless it was previously defined. 

        DSS property name: `Bus1`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    def _set_Bus1(self, value: AnyStr):
        self._set_string_o(1, value)

    Bus1 = property(_get_Bus1, _set_Bus1)

    def _get_Bus2(self) -> str:
        """
        Name of 2nd bus of the 2-terminal Fault object. Defaults to all phases connected to first bus, node 0, if not specified. (Shunt Wye Connection to ground reference)

        That is, the Fault defaults to a ground fault unless otherwise specified.

        DSS property name: `Bus2`, DSS property index: 2.
        """
        return self._get_prop_string(2)

    def _set_Bus2(self, value: AnyStr):
        self._set_string_o(2, value)

    Bus2 = property(_get_Bus2, _set_Bus2)

    def _get_Phases(self) -> int:
        """
        Number of Phases. Default is 1.

        DSS property name: `Phases`, DSS property index: 3.
        """
        return self._lib.Obj_GetInt32(self._ptr, 3)

    def _set_Phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 3, value)

    Phases = property(_get_Phases, _set_Phases)

    def _get_R(self) -> float:
        """
        Resistance, each phase, ohms. Default is 0.0001. Assumed to be Mean value if gaussian random mode.Max value if uniform mode.  A Fault is actually a series resistance that defaults to a wye connection to ground on the second terminal.  You may reconnect the 2nd terminal to achieve whatever connection.  Use the Gmatrix property to specify an arbitrary conductance matrix.

        DSS property name: `R`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    def _set_R(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    R = property(_get_R, _set_R)

    def _get_pctStdDev(self) -> float:
        """
        Percent standard deviation in resistance to assume for Monte Carlo fault (MF) solution mode for GAUSSIAN distribution. Default is 0 (no variation from mean).

        DSS property name: `%StdDev`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    def _set_pctStdDev(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    pctStdDev = property(_get_pctStdDev, _set_pctStdDev)

    def _get_GMatrix(self) -> Float64Array:
        """
        Use this to specify a nodal conductance (G) matrix to represent some arbitrary resistance network. Specify in lower triangle form as usual for DSS matrices.

        DSS property name: `GMatrix`, DSS property index: 6.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 6)

    def _set_GMatrix(self, value: Float64Array):
        self._set_float64_array_o(6, value)

    GMatrix = property(_get_GMatrix, _set_GMatrix)

    def _get_OnTime(self) -> float:
        """
        Time (sec) at which the fault is established for time varying simulations. Default is 0.0 (on at the beginning of the simulation)

        DSS property name: `OnTime`, DSS property index: 7.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    def _set_OnTime(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    OnTime = property(_get_OnTime, _set_OnTime)

    def _get_Temporary(self) -> bool:
        """
        {Yes | No} Default is No.  Designate whether the fault is temporary.  For Time-varying simulations, the fault will be removed if the current through the fault drops below the MINAMPS criteria.

        DSS property name: `Temporary`, DSS property index: 8.
        """
        return self._lib.Obj_GetInt32(self._ptr, 8) != 0

    def _set_Temporary(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 8, value)

    Temporary = property(_get_Temporary, _set_Temporary)

    def _get_MinAmps(self) -> float:
        """
        Minimum amps that can sustain a temporary fault. Default is 5.

        DSS property name: `MinAmps`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    def _set_MinAmps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    MinAmps = property(_get_MinAmps, _set_MinAmps)

    def _get_NormAmps(self) -> float:
        """
        Normal rated current.

        DSS property name: `NormAmps`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    def _set_NormAmps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    NormAmps = property(_get_NormAmps, _set_NormAmps)

    def _get_EmergAmps(self) -> float:
        """
        Maximum or emerg current.

        DSS property name: `EmergAmps`, DSS property index: 11.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    def _set_EmergAmps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    EmergAmps = property(_get_EmergAmps, _set_EmergAmps)

    def _get_FaultRate(self) -> float:
        """
        Failure rate per year.

        DSS property name: `FaultRate`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    def _set_FaultRate(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    FaultRate = property(_get_FaultRate, _set_FaultRate)

    def _get_pctPerm(self) -> float:
        """
        Percent of failures that become permanent.

        DSS property name: `pctPerm`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    def _set_pctPerm(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    pctPerm = property(_get_pctPerm, _set_pctPerm)

    def _get_Repair(self) -> float:
        """
        Hours to repair.

        DSS property name: `Repair`, DSS property index: 14.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    def _set_Repair(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    Repair = property(_get_Repair, _set_Repair)

    def _get_BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 15.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    def _set_BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq)

    def _get_Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 16.
        """
        return self._lib.Obj_GetInt32(self._ptr, 16) != 0

    def _set_Enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 16, value)

    Enabled = property(_get_Enabled, _set_Enabled)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 17.
        """
        self._set_string_o(17, value)


class FaultProperties(TypedDict):
    Bus1: AnyStr
    Bus2: AnyStr
    Phases: int
    R: float
    pctStdDev: float
    GMatrix: Float64Array
    OnTime: float
    Temporary: bool
    MinAmps: float
    NormAmps: float
    EmergAmps: float
    FaultRate: float
    pctPerm: float
    Repair: float
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class FaultBatch(DSSBatch, CircuitElementBatchMixin, PDElementBatchMixin):
    _cls_name = 'Fault'
    _obj_cls = Fault
    _cls_idx = 25


    def _get_Bus1(self) -> List[str]:
        """
        Name of first bus. Examples:

        bus1=busname
        bus1=busname.1.2.3

        Bus2 automatically defaults to busname.0,0,0 unless it was previously defined. 

        DSS property name: `Bus1`, DSS property index: 1.
        """
        return self._get_batch_str_prop(1)

    def _set_Bus1(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(1, value)

    Bus1 = property(_get_Bus1, _set_Bus1)

    def _get_Bus2(self) -> List[str]:
        """
        Name of 2nd bus of the 2-terminal Fault object. Defaults to all phases connected to first bus, node 0, if not specified. (Shunt Wye Connection to ground reference)

        That is, the Fault defaults to a ground fault unless otherwise specified.

        DSS property name: `Bus2`, DSS property index: 2.
        """
        return self._get_batch_str_prop(2)

    def _set_Bus2(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(2, value)

    Bus2 = property(_get_Bus2, _set_Bus2)

    def _get_Phases(self) -> BatchInt32ArrayProxy:
        """
        Number of Phases. Default is 1.

        DSS property name: `Phases`, DSS property index: 3.
        """
        return BatchInt32ArrayProxy(self, 3)

    def _set_Phases(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(3, value)

    Phases = property(_get_Phases, _set_Phases)

    def _get_R(self) -> BatchFloat64ArrayProxy:
        """
        Resistance, each phase, ohms. Default is 0.0001. Assumed to be Mean value if gaussian random mode.Max value if uniform mode.  A Fault is actually a series resistance that defaults to a wye connection to ground on the second terminal.  You may reconnect the 2nd terminal to achieve whatever connection.  Use the Gmatrix property to specify an arbitrary conductance matrix.

        DSS property name: `R`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    def _set_R(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(4, value)

    R = property(_get_R, _set_R)

    def _get_pctStdDev(self) -> BatchFloat64ArrayProxy:
        """
        Percent standard deviation in resistance to assume for Monte Carlo fault (MF) solution mode for GAUSSIAN distribution. Default is 0 (no variation from mean).

        DSS property name: `%StdDev`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    def _set_pctStdDev(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(5, value)

    pctStdDev = property(_get_pctStdDev, _set_pctStdDev)

    def _get_GMatrix(self) -> List[Float64Array]:
        """
        Use this to specify a nodal conductance (G) matrix to represent some arbitrary resistance network. Specify in lower triangle form as usual for DSS matrices.

        DSS property name: `GMatrix`, DSS property index: 6.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 6)
            for x in self._unpack()
        ]

    def _set_GMatrix(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(6, value)

    GMatrix = property(_get_GMatrix, _set_GMatrix)

    def _get_OnTime(self) -> BatchFloat64ArrayProxy:
        """
        Time (sec) at which the fault is established for time varying simulations. Default is 0.0 (on at the beginning of the simulation)

        DSS property name: `OnTime`, DSS property index: 7.
        """
        return BatchFloat64ArrayProxy(self, 7)

    def _set_OnTime(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(7, value)

    OnTime = property(_get_OnTime, _set_OnTime)

    def _get_Temporary(self) -> List[bool]:
        """
        {Yes | No} Default is No.  Designate whether the fault is temporary.  For Time-varying simulations, the fault will be removed if the current through the fault drops below the MINAMPS criteria.

        DSS property name: `Temporary`, DSS property index: 8.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(8)
        ]

    def _set_Temporary(self, value: bool):
        self._set_batch_int32_array(8, value)

    Temporary = property(_get_Temporary, _set_Temporary)

    def _get_MinAmps(self) -> BatchFloat64ArrayProxy:
        """
        Minimum amps that can sustain a temporary fault. Default is 5.

        DSS property name: `MinAmps`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    def _set_MinAmps(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(9, value)

    MinAmps = property(_get_MinAmps, _set_MinAmps)

    def _get_NormAmps(self) -> BatchFloat64ArrayProxy:
        """
        Normal rated current.

        DSS property name: `NormAmps`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    def _set_NormAmps(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(10, value)

    NormAmps = property(_get_NormAmps, _set_NormAmps)

    def _get_EmergAmps(self) -> BatchFloat64ArrayProxy:
        """
        Maximum or emerg current.

        DSS property name: `EmergAmps`, DSS property index: 11.
        """
        return BatchFloat64ArrayProxy(self, 11)

    def _set_EmergAmps(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(11, value)

    EmergAmps = property(_get_EmergAmps, _set_EmergAmps)

    def _get_FaultRate(self) -> BatchFloat64ArrayProxy:
        """
        Failure rate per year.

        DSS property name: `FaultRate`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    def _set_FaultRate(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(12, value)

    FaultRate = property(_get_FaultRate, _set_FaultRate)

    def _get_pctPerm(self) -> BatchFloat64ArrayProxy:
        """
        Percent of failures that become permanent.

        DSS property name: `pctPerm`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    def _set_pctPerm(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(13, value)

    pctPerm = property(_get_pctPerm, _set_pctPerm)

    def _get_Repair(self) -> BatchFloat64ArrayProxy:
        """
        Hours to repair.

        DSS property name: `Repair`, DSS property index: 14.
        """
        return BatchFloat64ArrayProxy(self, 14)

    def _set_Repair(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(14, value)

    Repair = property(_get_Repair, _set_Repair)

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 15.
        """
        return BatchFloat64ArrayProxy(self, 15)

    def _set_BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(15, value)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq)

    def _get_Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 16.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(16)
        ]

    def _set_Enabled(self, value: bool):
        self._set_batch_int32_array(16, value)

    Enabled = property(_get_Enabled, _set_Enabled)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 17.
        """
        self._set_batch_string(17, value)

class FaultBatchProperties(TypedDict):
    Bus1: Union[AnyStr, List[AnyStr]]
    Bus2: Union[AnyStr, List[AnyStr]]
    Phases: Union[int, Int32Array]
    R: Union[float, Float64Array]
    pctStdDev: Union[float, Float64Array]
    GMatrix: Float64Array
    OnTime: Union[float, Float64Array]
    Temporary: bool
    MinAmps: Union[float, Float64Array]
    NormAmps: Union[float, Float64Array]
    EmergAmps: Union[float, Float64Array]
    FaultRate: Union[float, Float64Array]
    pctPerm: Union[float, Float64Array]
    Repair: Union[float, Float64Array]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IFault(IDSSObj, FaultBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, Fault, FaultBatch)
        FaultBatch.__init__(self, self._api_util, sync_cls=True)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Fault:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[FaultProperties]) -> Fault:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[FaultBatchProperties]) -> FaultBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
