# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from enum import IntEnum
from typing_extensions import TypedDict, Unpack
import numpy as np
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

class Capacitor(DSSObj, CktElementMixin, PDElementMixin):
    __slots__ = []
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

    @property
    def Bus1(self) -> str:
        """
        Name of first bus of 2-terminal capacitor. Examples:
        bus1=busname
        bus1=busname.1.2.3

        If only one bus specified, Bus2 will default to this bus, Node 0, and the capacitor will be a Yg shunt bank.

        DSS property name: `Bus1`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    @Bus1.setter
    def Bus1(self, value: AnyStr):
        self._set_string_o(1, value)

    @property
    def Bus2(self) -> str:
        """
        Name of 2nd bus. Defaults to all phases connected to first bus, node 0, (Shunt Wye Connection) except when Bus2 explicitly specified. 

        Not necessary to specify for delta (LL) connection.

        DSS property name: `Bus2`, DSS property index: 2.
        """
        return self._get_prop_string(2)

    @Bus2.setter
    def Bus2(self, value: AnyStr):
        self._set_string_o(2, value)

    @property
    def Phases(self) -> int:
        """
        Number of phases.

        DSS property name: `Phases`, DSS property index: 3.
        """
        return self._lib.Obj_GetInt32(self._ptr, 3)

    @Phases.setter
    def Phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 3, value)

    @property
    def kvar(self) -> Float64Array:
        """
        Total kvar, if one step, or ARRAY of kvar ratings for each step.  Evenly divided among phases. See rules for NUMSTEPS.

        DSS property name: `kvar`, DSS property index: 4.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 4)

    @kvar.setter
    def kvar(self, value: Float64Array):
        self._set_float64_array_o(4, value)

    @property
    def kV(self) -> float:
        """
        For 2, 3-phase, kV phase-phase. Otherwise specify actual can rating.

        DSS property name: `kV`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @kV.setter
    def kV(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def Conn(self) -> enums.Connection:
        """
        ={wye | delta |LN |LL}  Default is wye, which is equivalent to LN

        DSS property name: `Conn`, DSS property index: 6.
        """
        return enums.Connection(self._lib.Obj_GetInt32(self._ptr, 6))

    @Conn.setter
    def Conn(self, value: Union[AnyStr, int, enums.Connection]):
        if not isinstance(value, int):
            self._set_string_o(6, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 6, value)

    @property
    def Conn_str(self) -> str:
        """
        ={wye | delta |LN |LL}  Default is wye, which is equivalent to LN

        DSS property name: `Conn`, DSS property index: 6.
        """
        return self._get_prop_string(6)

    @Conn_str.setter
    def Conn_str(self, value: AnyStr):
        self.Conn = value

    @property
    def CMatrix(self) -> Float64Array:
        """
        Nodal cap. matrix, lower triangle, microfarads, of the following form:

        cmatrix="c11 | -c21 c22 | -c31 -c32 c33"

        All steps are assumed the same if this property is used.

        DSS property name: `CMatrix`, DSS property index: 7.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 7)

    @CMatrix.setter
    def CMatrix(self, value: Float64Array):
        self._set_float64_array_o(7, value)

    @property
    def Cuf(self) -> Float64Array:
        """
        ARRAY of Capacitance, each phase, for each step, microfarads.
        See Rules for NumSteps.

        DSS property name: `Cuf`, DSS property index: 8.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 8)

    @Cuf.setter
    def Cuf(self, value: Float64Array):
        self._set_float64_array_o(8, value)

    @property
    def R(self) -> Float64Array:
        """
        ARRAY of series resistance in each phase (line), ohms. Default is 0.0

        DSS property name: `R`, DSS property index: 9.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 9)

    @R.setter
    def R(self, value: Float64Array):
        self._set_float64_array_o(9, value)

    @property
    def XL(self) -> Float64Array:
        """
        ARRAY of series inductive reactance(s) in each phase (line) for filter, ohms at base frequency. Use this OR "h" property to define filter. Default is 0.0.

        DSS property name: `XL`, DSS property index: 10.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 10)

    @XL.setter
    def XL(self, value: Float64Array):
        self._set_float64_array_o(10, value)

    @property
    def Harm(self) -> Float64Array:
        """
        ARRAY of harmonics to which each step is tuned. Zero is interpreted as meaning zero reactance (no filter). Default is zero.

        DSS property name: `Harm`, DSS property index: 11.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 11)

    @Harm.setter
    def Harm(self, value: Float64Array):
        self._set_float64_array_o(11, value)

    @property
    def NumSteps(self) -> int:
        """
        Number of steps in this capacitor bank. Default = 1. Forces reallocation of the capacitance, reactor, and states array.  Rules: If this property was previously =1, the value in the kvar property is divided equally among the steps. The kvar property does not need to be reset if that is accurate.  If the Cuf or Cmatrix property was used previously, all steps are set to the value of the first step. The states property is set to all steps on. All filter steps are set to the same harmonic. If this property was previously >1, the arrays are reallocated, but no values are altered. You must SUBSEQUENTLY assign all array properties.

        DSS property name: `NumSteps`, DSS property index: 12.
        """
        return self._lib.Obj_GetInt32(self._ptr, 12)

    @NumSteps.setter
    def NumSteps(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 12, value)

    @property
    def States(self) -> Int32Array:
        """
        ARRAY of integers {1|0} states representing the state of each step (on|off). Defaults to 1 when reallocated (on). Capcontrol will modify this array as it turns steps on or off.

        DSS property name: `States`, DSS property index: 13.
        """
        return self._get_int32_array(self._lib.Obj_GetInt32Array, self._ptr, 13)

    @States.setter
    def States(self, value: Int32Array):
        self._set_int32_array_o(13, value)

    @property
    def NormAmps(self) -> float:
        """
        Normal rated current. Defaults to 180% of per-phase rated current.

        DSS property name: `NormAmps`, DSS property index: 14.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @NormAmps.setter
    def NormAmps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def EmergAmps(self) -> float:
        """
        Maximum or emerg current. Defaults to 180% of per-phase rated current.

        DSS property name: `EmergAmps`, DSS property index: 15.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @EmergAmps.setter
    def EmergAmps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def FaultRate(self) -> float:
        """
        Failure rate per year.

        DSS property name: `FaultRate`, DSS property index: 16.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    @FaultRate.setter
    def FaultRate(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 16, value)

    @property
    def pctPerm(self) -> float:
        """
        Percent of failures that become permanent.

        DSS property name: `pctPerm`, DSS property index: 17.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    @pctPerm.setter
    def pctPerm(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 17, value)

    @property
    def Repair(self) -> float:
        """
        Hours to repair.

        DSS property name: `Repair`, DSS property index: 18.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    @Repair.setter
    def Repair(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 18, value)

    @property
    def BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 19.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    @BaseFreq.setter
    def BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 19, value)

    @property
    def Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 20.
        """
        return self._lib.Obj_GetInt32(self._ptr, 20) != 0

    @Enabled.setter
    def Enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 20, value)

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

class CapacitorBatch(DSSBatch):
    _cls_name = 'Capacitor'
    _obj_cls = Capacitor
    _cls_idx = 22


    @property
    def Bus1(self) -> List[str]:
        """
        Name of first bus of 2-terminal capacitor. Examples:
        bus1=busname
        bus1=busname.1.2.3

        If only one bus specified, Bus2 will default to this bus, Node 0, and the capacitor will be a Yg shunt bank.

        DSS property name: `Bus1`, DSS property index: 1.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1) 

    @Bus1.setter
    def Bus1(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(1, value)

    @property
    def Bus2(self) -> List[str]:
        """
        Name of 2nd bus. Defaults to all phases connected to first bus, node 0, (Shunt Wye Connection) except when Bus2 explicitly specified. 

        Not necessary to specify for delta (LL) connection.

        DSS property name: `Bus2`, DSS property index: 2.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 2) 

    @Bus2.setter
    def Bus2(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(2, value)

    @property
    def Phases(self) -> BatchInt32ArrayProxy:
        """
        Number of phases.

        DSS property name: `Phases`, DSS property index: 3.
        """
        return BatchInt32ArrayProxy(self, 3)

    @Phases.setter
    def Phases(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(3, value)

    @property
    def kvar(self) -> List[Float64Array]:
        """
        Total kvar, if one step, or ARRAY of kvar ratings for each step.  Evenly divided among phases. See rules for NUMSTEPS.

        DSS property name: `kvar`, DSS property index: 4.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 4)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @kvar.setter
    def kvar(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(4, value)

    @property
    def kV(self) -> BatchFloat64ArrayProxy:
        """
        For 2, 3-phase, kV phase-phase. Otherwise specify actual can rating.

        DSS property name: `kV`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    @kV.setter
    def kV(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(5, value)

    @property
    def Conn(self) -> BatchInt32ArrayProxy:
        """
        ={wye | delta |LN |LL}  Default is wye, which is equivalent to LN

        DSS property name: `Conn`, DSS property index: 6.
        """
        return BatchInt32ArrayProxy(self, 6)

    @Conn.setter
    def Conn(self, value: Union[AnyStr, int, enums.Connection, List[AnyStr], List[int], List[enums.Connection], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(6, value)
            return
    
        self._set_batch_int32_array(6, value)

    @property
    def Conn_str(self) -> str:
        """
        ={wye | delta |LN |LL}  Default is wye, which is equivalent to LN

        DSS property name: `Conn`, DSS property index: 6.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 6)

    @Conn_str.setter
    def Conn_str(self, value: AnyStr):
        self.Conn = value

    @property
    def CMatrix(self) -> List[Float64Array]:
        """
        Nodal cap. matrix, lower triangle, microfarads, of the following form:

        cmatrix="c11 | -c21 c22 | -c31 -c32 c33"

        All steps are assumed the same if this property is used.

        DSS property name: `CMatrix`, DSS property index: 7.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 7)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @CMatrix.setter
    def CMatrix(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(7, value)

    @property
    def Cuf(self) -> List[Float64Array]:
        """
        ARRAY of Capacitance, each phase, for each step, microfarads.
        See Rules for NumSteps.

        DSS property name: `Cuf`, DSS property index: 8.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 8)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Cuf.setter
    def Cuf(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(8, value)

    @property
    def R(self) -> List[Float64Array]:
        """
        ARRAY of series resistance in each phase (line), ohms. Default is 0.0

        DSS property name: `R`, DSS property index: 9.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 9)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @R.setter
    def R(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(9, value)

    @property
    def XL(self) -> List[Float64Array]:
        """
        ARRAY of series inductive reactance(s) in each phase (line) for filter, ohms at base frequency. Use this OR "h" property to define filter. Default is 0.0.

        DSS property name: `XL`, DSS property index: 10.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 10)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @XL.setter
    def XL(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(10, value)

    @property
    def Harm(self) -> List[Float64Array]:
        """
        ARRAY of harmonics to which each step is tuned. Zero is interpreted as meaning zero reactance (no filter). Default is zero.

        DSS property name: `Harm`, DSS property index: 11.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 11)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Harm.setter
    def Harm(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(11, value)

    @property
    def NumSteps(self) -> BatchInt32ArrayProxy:
        """
        Number of steps in this capacitor bank. Default = 1. Forces reallocation of the capacitance, reactor, and states array.  Rules: If this property was previously =1, the value in the kvar property is divided equally among the steps. The kvar property does not need to be reset if that is accurate.  If the Cuf or Cmatrix property was used previously, all steps are set to the value of the first step. The states property is set to all steps on. All filter steps are set to the same harmonic. If this property was previously >1, the arrays are reallocated, but no values are altered. You must SUBSEQUENTLY assign all array properties.

        DSS property name: `NumSteps`, DSS property index: 12.
        """
        return BatchInt32ArrayProxy(self, 12)

    @NumSteps.setter
    def NumSteps(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(12, value)

    @property
    def States(self) -> List[Int32Array]:
        """
        ARRAY of integers {1|0} states representing the state of each step (on|off). Defaults to 1 when reallocated (on). Capcontrol will modify this array as it turns steps on or off.

        DSS property name: `States`, DSS property index: 13.
        """
        return [
            self._get_int32_array(self._lib.Obj_GetInt32Array, x, 13)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @States.setter
    def States(self, value: Union[Int32Array, List[Int32Array]]):
        self._set_batch_int32_array_prop(13, value)

    @property
    def NormAmps(self) -> BatchFloat64ArrayProxy:
        """
        Normal rated current. Defaults to 180% of per-phase rated current.

        DSS property name: `NormAmps`, DSS property index: 14.
        """
        return BatchFloat64ArrayProxy(self, 14)

    @NormAmps.setter
    def NormAmps(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(14, value)

    @property
    def EmergAmps(self) -> BatchFloat64ArrayProxy:
        """
        Maximum or emerg current. Defaults to 180% of per-phase rated current.

        DSS property name: `EmergAmps`, DSS property index: 15.
        """
        return BatchFloat64ArrayProxy(self, 15)

    @EmergAmps.setter
    def EmergAmps(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(15, value)

    @property
    def FaultRate(self) -> BatchFloat64ArrayProxy:
        """
        Failure rate per year.

        DSS property name: `FaultRate`, DSS property index: 16.
        """
        return BatchFloat64ArrayProxy(self, 16)

    @FaultRate.setter
    def FaultRate(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(16, value)

    @property
    def pctPerm(self) -> BatchFloat64ArrayProxy:
        """
        Percent of failures that become permanent.

        DSS property name: `pctPerm`, DSS property index: 17.
        """
        return BatchFloat64ArrayProxy(self, 17)

    @pctPerm.setter
    def pctPerm(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(17, value)

    @property
    def Repair(self) -> BatchFloat64ArrayProxy:
        """
        Hours to repair.

        DSS property name: `Repair`, DSS property index: 18.
        """
        return BatchFloat64ArrayProxy(self, 18)

    @Repair.setter
    def Repair(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(18, value)

    @property
    def BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 19.
        """
        return BatchFloat64ArrayProxy(self, 19)

    @BaseFreq.setter
    def BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(19, value)

    @property
    def Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 20.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 20)
        ]
    @Enabled.setter
    def Enabled(self, value: bool):
        self._set_batch_int32_array(20, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 21.
        """
        self._set_batch_string(21, value)

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

class ICapacitor(IDSSObj):
    def __init__(self, iobj):
        super().__init__(iobj, Capacitor, CapacitorBatch)

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Capacitor:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[CapacitorProperties]) -> Capacitor:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[CapacitorBatchProperties]) -> CapacitorBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
