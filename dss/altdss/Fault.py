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

class Fault(DSSObj, CktElementMixin, PDElementMixin):
    __slots__ = CktElementMixin._extra_slots + PDElementMixin._extra_slots
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

    @property
    def Bus1(self) -> str:
        """
        Name of first bus. Examples:

        bus1=busname
        bus1=busname.1.2.3

        Bus2 automatically defaults to busname.0,0,0 unless it was previously defined. 

        DSS property name: `Bus1`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    @Bus1.setter
    def Bus1(self, value: AnyStr):
        self._set_string_o(1, value)

    @property
    def Bus2(self) -> str:
        """
        Name of 2nd bus of the 2-terminal Fault object. Defaults to all phases connected to first bus, node 0, if not specified. (Shunt Wye Connection to ground reference)

        That is, the Fault defaults to a ground fault unless otherwise specified.

        DSS property name: `Bus2`, DSS property index: 2.
        """
        return self._get_prop_string(2)

    @Bus2.setter
    def Bus2(self, value: AnyStr):
        self._set_string_o(2, value)

    @property
    def Phases(self) -> int:
        """
        Number of Phases. Default is 1.

        DSS property name: `Phases`, DSS property index: 3.
        """
        return self._lib.Obj_GetInt32(self._ptr, 3)

    @Phases.setter
    def Phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 3, value)

    @property
    def R(self) -> float:
        """
        Resistance, each phase, ohms. Default is 0.0001. Assumed to be Mean value if gaussian random mode.Max value if uniform mode.  A Fault is actually a series resistance that defaults to a wye connection to ground on the second terminal.  You may reconnect the 2nd terminal to achieve whatever connection.  Use the Gmatrix property to specify an arbitrary conductance matrix.

        DSS property name: `R`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @R.setter
    def R(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def pctStdDev(self) -> float:
        """
        Percent standard deviation in resistance to assume for Monte Carlo fault (MF) solution mode for GAUSSIAN distribution. Default is 0 (no variation from mean).

        DSS property name: `%StdDev`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @pctStdDev.setter
    def pctStdDev(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def GMatrix(self) -> Float64Array:
        """
        Use this to specify a nodal conductance (G) matrix to represent some arbitrary resistance network. Specify in lower triangle form as usual for DSS matrices.

        DSS property name: `GMatrix`, DSS property index: 6.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 6)

    @GMatrix.setter
    def GMatrix(self, value: Float64Array):
        self._set_float64_array_o(6, value)

    @property
    def OnTime(self) -> float:
        """
        Time (sec) at which the fault is established for time varying simulations. Default is 0.0 (on at the beginning of the simulation)

        DSS property name: `OnTime`, DSS property index: 7.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @OnTime.setter
    def OnTime(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def Temporary(self) -> bool:
        """
        {Yes | No} Default is No.  Designate whether the fault is temporary.  For Time-varying simulations, the fault will be removed if the current through the fault drops below the MINAMPS criteria.

        DSS property name: `Temporary`, DSS property index: 8.
        """
        return self._lib.Obj_GetInt32(self._ptr, 8) != 0

    @Temporary.setter
    def Temporary(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 8, value)

    @property
    def MinAmps(self) -> float:
        """
        Minimum amps that can sustain a temporary fault. Default is 5.

        DSS property name: `MinAmps`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @MinAmps.setter
    def MinAmps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def NormAmps(self) -> float:
        """
        Normal rated current.

        DSS property name: `NormAmps`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @NormAmps.setter
    def NormAmps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def EmergAmps(self) -> float:
        """
        Maximum or emerg current.

        DSS property name: `EmergAmps`, DSS property index: 11.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @EmergAmps.setter
    def EmergAmps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def FaultRate(self) -> float:
        """
        Failure rate per year.

        DSS property name: `FaultRate`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @FaultRate.setter
    def FaultRate(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def pctPerm(self) -> float:
        """
        Percent of failures that become permanent.

        DSS property name: `pctPerm`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @pctPerm.setter
    def pctPerm(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def Repair(self) -> float:
        """
        Hours to repair.

        DSS property name: `Repair`, DSS property index: 14.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @Repair.setter
    def Repair(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 15.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @BaseFreq.setter
    def BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 16.
        """
        return self._lib.Obj_GetInt32(self._ptr, 16) != 0

    @Enabled.setter
    def Enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 16, value)

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

class FaultBatch(DSSBatch):
    _cls_name = 'Fault'
    _obj_cls = Fault
    _cls_idx = 25


    @property
    def Bus1(self) -> List[str]:
        """
        Name of first bus. Examples:

        bus1=busname
        bus1=busname.1.2.3

        Bus2 automatically defaults to busname.0,0,0 unless it was previously defined. 

        DSS property name: `Bus1`, DSS property index: 1.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1) 

    @Bus1.setter
    def Bus1(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(1, value)

    @property
    def Bus2(self) -> List[str]:
        """
        Name of 2nd bus of the 2-terminal Fault object. Defaults to all phases connected to first bus, node 0, if not specified. (Shunt Wye Connection to ground reference)

        That is, the Fault defaults to a ground fault unless otherwise specified.

        DSS property name: `Bus2`, DSS property index: 2.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 2) 

    @Bus2.setter
    def Bus2(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(2, value)

    @property
    def Phases(self) -> BatchInt32ArrayProxy:
        """
        Number of Phases. Default is 1.

        DSS property name: `Phases`, DSS property index: 3.
        """
        return BatchInt32ArrayProxy(self, 3)

    @Phases.setter
    def Phases(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(3, value)

    @property
    def R(self) -> BatchFloat64ArrayProxy:
        """
        Resistance, each phase, ohms. Default is 0.0001. Assumed to be Mean value if gaussian random mode.Max value if uniform mode.  A Fault is actually a series resistance that defaults to a wye connection to ground on the second terminal.  You may reconnect the 2nd terminal to achieve whatever connection.  Use the Gmatrix property to specify an arbitrary conductance matrix.

        DSS property name: `R`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    @R.setter
    def R(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(4, value)

    @property
    def pctStdDev(self) -> BatchFloat64ArrayProxy:
        """
        Percent standard deviation in resistance to assume for Monte Carlo fault (MF) solution mode for GAUSSIAN distribution. Default is 0 (no variation from mean).

        DSS property name: `%StdDev`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    @pctStdDev.setter
    def pctStdDev(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(5, value)

    @property
    def GMatrix(self) -> List[Float64Array]:
        """
        Use this to specify a nodal conductance (G) matrix to represent some arbitrary resistance network. Specify in lower triangle form as usual for DSS matrices.

        DSS property name: `GMatrix`, DSS property index: 6.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 6)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @GMatrix.setter
    def GMatrix(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(6, value)

    @property
    def OnTime(self) -> BatchFloat64ArrayProxy:
        """
        Time (sec) at which the fault is established for time varying simulations. Default is 0.0 (on at the beginning of the simulation)

        DSS property name: `OnTime`, DSS property index: 7.
        """
        return BatchFloat64ArrayProxy(self, 7)

    @OnTime.setter
    def OnTime(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(7, value)

    @property
    def Temporary(self) -> List[bool]:
        """
        {Yes | No} Default is No.  Designate whether the fault is temporary.  For Time-varying simulations, the fault will be removed if the current through the fault drops below the MINAMPS criteria.

        DSS property name: `Temporary`, DSS property index: 8.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 8)
        ]
    @Temporary.setter
    def Temporary(self, value: bool):
        self._set_batch_int32_array(8, value)

    @property
    def MinAmps(self) -> BatchFloat64ArrayProxy:
        """
        Minimum amps that can sustain a temporary fault. Default is 5.

        DSS property name: `MinAmps`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    @MinAmps.setter
    def MinAmps(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(9, value)

    @property
    def NormAmps(self) -> BatchFloat64ArrayProxy:
        """
        Normal rated current.

        DSS property name: `NormAmps`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    @NormAmps.setter
    def NormAmps(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(10, value)

    @property
    def EmergAmps(self) -> BatchFloat64ArrayProxy:
        """
        Maximum or emerg current.

        DSS property name: `EmergAmps`, DSS property index: 11.
        """
        return BatchFloat64ArrayProxy(self, 11)

    @EmergAmps.setter
    def EmergAmps(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(11, value)

    @property
    def FaultRate(self) -> BatchFloat64ArrayProxy:
        """
        Failure rate per year.

        DSS property name: `FaultRate`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    @FaultRate.setter
    def FaultRate(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(12, value)

    @property
    def pctPerm(self) -> BatchFloat64ArrayProxy:
        """
        Percent of failures that become permanent.

        DSS property name: `pctPerm`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    @pctPerm.setter
    def pctPerm(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(13, value)

    @property
    def Repair(self) -> BatchFloat64ArrayProxy:
        """
        Hours to repair.

        DSS property name: `Repair`, DSS property index: 14.
        """
        return BatchFloat64ArrayProxy(self, 14)

    @Repair.setter
    def Repair(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(14, value)

    @property
    def BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 15.
        """
        return BatchFloat64ArrayProxy(self, 15)

    @BaseFreq.setter
    def BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(15, value)

    @property
    def Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 16.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 16)
        ]
    @Enabled.setter
    def Enabled(self, value: bool):
        self._set_batch_int32_array(16, value)

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

class IFault(IDSSObj):
    __slots__ = ()

    def __init__(self, iobj):
        super().__init__(iobj, Fault, FaultBatch)

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Fault:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[FaultProperties]) -> Fault:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[FaultBatchProperties]) -> FaultBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
