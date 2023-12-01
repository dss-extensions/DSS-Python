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
from .XYcurve import XYcurve

class Reactor(DSSObj, CircuitElementMixin, PDElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots + PDElementMixin._extra_slots
    _cls_name = 'Reactor'
    _cls_idx = 23
    _cls_prop_idx = {
        'bus1': 1,
        'bus2': 2,
        'phases': 3,
        'kvar': 4,
        'kv': 5,
        'conn': 6,
        'rmatrix': 7,
        'xmatrix': 8,
        'parallel': 9,
        'r': 10,
        'x': 11,
        'rp': 12,
        'z1': 13,
        'z2': 14,
        'z0': 15,
        'z': 16,
        'rcurve': 17,
        'lcurve': 18,
        'lmh': 19,
        'normamps': 20,
        'emergamps': 21,
        'faultrate': 22,
        'pctperm': 23,
        'repair': 24,
        'basefreq': 25,
        'enabled': 26,
        'like': 27,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)
       PDElementMixin.__init__(self)

    def _get_Bus1(self) -> str:
        """
        Name of first bus. Examples:
        bus1=busname
        bus1=busname.1.2.3

        Bus2 property will default to this bus, node 0, unless previously specified. Only Bus1 need be specified for a Yg shunt reactor.

        DSS property name: `Bus1`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    def _set_Bus1(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(1, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: str

    def _get_Bus2(self) -> str:
        """
        Name of 2nd bus. Defaults to all phases connected to first bus, node 0, (Shunt Wye Connection) except when Bus2 is specifically defined.

        Not necessary to specify for delta (LL) connection

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

    def _get_kvar(self) -> float:
        """
        Total kvar, all phases.  Evenly divided among phases. Only determines X. Specify R separately

        DSS property name: `kvar`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    def _set_kvar(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 4, value, flags)

    kvar = property(_get_kvar, _set_kvar) # type: float

    def _get_kV(self) -> float:
        """
        For 2, 3-phase, kV phase-phase. Otherwise specify actual coil rating.

        DSS property name: `kV`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    def _set_kV(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 5, value, flags)

    kV = property(_get_kV, _set_kV) # type: float

    def _get_Conn(self) -> enums.Connection:
        """
        ={wye | delta |LN |LL}  Default is wye, which is equivalent to LN. If Delta, then only one terminal.

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
        ={wye | delta |LN |LL}  Default is wye, which is equivalent to LN. If Delta, then only one terminal.

        DSS property name: `Conn`, DSS property index: 6.
        """
        return self._get_prop_string(6)

    def _set_Conn_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Conn(value, flags)

    Conn_str = property(_get_Conn_str, _set_Conn_str) # type: str

    def _get_RMatrix(self) -> Float64Array:
        """
        Resistance matrix, lower triangle, ohms at base frequency. Order of the matrix is the number of phases. Mutually exclusive to specifying parameters by kvar or X.

        DSS property name: `RMatrix`, DSS property index: 7.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 7)

    def _set_RMatrix(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(7, value, flags)

    RMatrix = property(_get_RMatrix, _set_RMatrix) # type: Float64Array

    def _get_XMatrix(self) -> Float64Array:
        """
        Reactance matrix, lower triangle, ohms at base frequency. Order of the matrix is the number of phases. Mutually exclusive to specifying parameters by kvar or X.

        DSS property name: `XMatrix`, DSS property index: 8.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 8)

    def _set_XMatrix(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(8, value, flags)

    XMatrix = property(_get_XMatrix, _set_XMatrix) # type: Float64Array

    def _get_Parallel(self) -> bool:
        """
        {Yes | No}  Default=No. Indicates whether Rmatrix and Xmatrix are to be considered in parallel. Default is series. For other models, specify R and Rp.

        DSS property name: `Parallel`, DSS property index: 9.
        """
        return self._lib.Obj_GetInt32(self._ptr, 9) != 0

    def _set_Parallel(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 9, value, flags)

    Parallel = property(_get_Parallel, _set_Parallel) # type: bool

    def _get_R(self) -> float:
        """
        Resistance (in series with reactance), each phase, ohms. This property applies to REACTOR specified by either kvar or X. See also help on Z.

        DSS property name: `R`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    def _set_R(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 10, value, flags)

    R = property(_get_R, _set_R) # type: float

    def _get_X(self) -> float:
        """
        Reactance, each phase, ohms at base frequency. See also help on Z and LmH properties.

        DSS property name: `X`, DSS property index: 11.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    def _set_X(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 11, value, flags)

    X = property(_get_X, _set_X) # type: float

    def _get_Rp(self) -> float:
        """
        Resistance in parallel with R and X (the entire branch). Assumed infinite if not specified.

        DSS property name: `Rp`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    def _set_Rp(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 12, value, flags)

    Rp = property(_get_Rp, _set_Rp) # type: float

    def _get_Z1(self) -> complex:
        """
        Positive-sequence impedance, ohms, as a 2-element array representing a complex number. Example: 

        Z1=[1, 2]  ! represents 1 + j2 

        If defined, Z1, Z2, and Z0 are used to define the impedance matrix of the REACTOR. Z1 MUST BE DEFINED TO USE THIS OPTION FOR DEFINING THE MATRIX.

        Side Effect: Sets Z2 and Z0 to same values unless they were previously defined.

        DSS property name: `Z1`, DSS property index: 13.
        """
        return self._get_complex(13)

    def _set_Z1(self, value: complex, flags: enums.SetterFlags = 0):
        self._set_complex(13, value, flags)

    Z1 = property(_get_Z1, _set_Z1) # type: complex

    def _get_Z2(self) -> complex:
        """
        Negative-sequence impedance, ohms, as a 2-element array representing a complex number. Example: 

        Z2=[1, 2]  ! represents 1 + j2 

        Used to define the impedance matrix of the REACTOR if Z1 is also specified. 

        Note: Z2 defaults to Z1 if it is not specifically defined. If Z2 is not equal to Z1, the impedance matrix is asymmetrical.

        DSS property name: `Z2`, DSS property index: 14.
        """
        return self._get_complex(14)

    def _set_Z2(self, value: complex, flags: enums.SetterFlags = 0):
        self._set_complex(14, value, flags)

    Z2 = property(_get_Z2, _set_Z2) # type: complex

    def _get_Z0(self) -> complex:
        """
        Zer0-sequence impedance, ohms, as a 2-element array representing a complex number. Example: 

        Z0=[3, 4]  ! represents 3 + j4 

        Used to define the impedance matrix of the REACTOR if Z1 is also specified. 

        Note: Z0 defaults to Z1 if it is not specifically defined. 

        DSS property name: `Z0`, DSS property index: 15.
        """
        return self._get_complex(15)

    def _set_Z0(self, value: complex, flags: enums.SetterFlags = 0):
        self._set_complex(15, value, flags)

    Z0 = property(_get_Z0, _set_Z0) # type: complex

    def _get_RCurve_str(self) -> str:
        """
        Name of XYCurve object, previously defined, describing per-unit variation of phase resistance, R, vs. frequency. Applies to resistance specified by R or Z property. If actual values are not known, R often increases by approximately the square root of frequency.

        DSS property name: `RCurve`, DSS property index: 17.
        """
        return self._get_prop_string(17)

    def _set_RCurve_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(17, value, flags)

    RCurve_str = property(_get_RCurve_str, _set_RCurve_str) # type: str

    def _get_RCurve(self) -> XYcurve:
        """
        Name of XYCurve object, previously defined, describing per-unit variation of phase resistance, R, vs. frequency. Applies to resistance specified by R or Z property. If actual values are not known, R often increases by approximately the square root of frequency.

        DSS property name: `RCurve`, DSS property index: 17.
        """
        return self._get_obj(17, XYcurve)

    def _set_RCurve(self, value: Union[AnyStr, XYcurve], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(17, value, flags)
            return

        self._set_string_o(17, value, flags)

    RCurve = property(_get_RCurve, _set_RCurve) # type: XYcurve

    def _get_LCurve_str(self) -> str:
        """
        Name of XYCurve object, previously defined, describing per-unit variation of phase inductance, L=X/w, vs. frequency. Applies to reactance specified by X, LmH, Z, or kvar property.L generally decreases somewhat with frequency above the base frequency, approaching a limit at a few kHz.

        DSS property name: `LCurve`, DSS property index: 18.
        """
        return self._get_prop_string(18)

    def _set_LCurve_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(18, value, flags)

    LCurve_str = property(_get_LCurve_str, _set_LCurve_str) # type: str

    def _get_LCurve(self) -> XYcurve:
        """
        Name of XYCurve object, previously defined, describing per-unit variation of phase inductance, L=X/w, vs. frequency. Applies to reactance specified by X, LmH, Z, or kvar property.L generally decreases somewhat with frequency above the base frequency, approaching a limit at a few kHz.

        DSS property name: `LCurve`, DSS property index: 18.
        """
        return self._get_obj(18, XYcurve)

    def _set_LCurve(self, value: Union[AnyStr, XYcurve], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(18, value, flags)
            return

        self._set_string_o(18, value, flags)

    LCurve = property(_get_LCurve, _set_LCurve) # type: XYcurve

    def _get_LmH(self) -> float:
        """
        Inductance, mH. Alternate way to define the reactance, X, property.

        DSS property name: `LmH`, DSS property index: 19.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    def _set_LmH(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 19, value, flags)

    LmH = property(_get_LmH, _set_LmH) # type: float

    def _get_NormAmps(self) -> float:
        """
        Normal rated current. Defaults to per-phase rated current when reactor is specified with rated power and voltage.

        DSS property name: `NormAmps`, DSS property index: 20.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    def _set_NormAmps(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 20, value, flags)

    NormAmps = property(_get_NormAmps, _set_NormAmps) # type: float

    def _get_EmergAmps(self) -> float:
        """
        Maximum or emerg current. Defaults to 135% of per-phase rated current when reactor is specified with rated power and voltage.

        DSS property name: `EmergAmps`, DSS property index: 21.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    def _set_EmergAmps(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 21, value, flags)

    EmergAmps = property(_get_EmergAmps, _set_EmergAmps) # type: float

    def _get_FaultRate(self) -> float:
        """
        Failure rate per year.

        DSS property name: `FaultRate`, DSS property index: 22.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    def _set_FaultRate(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 22, value, flags)

    FaultRate = property(_get_FaultRate, _set_FaultRate) # type: float

    def _get_pctPerm(self) -> float:
        """
        Percent of failures that become permanent.

        DSS property name: `pctPerm`, DSS property index: 23.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    def _set_pctPerm(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 23, value, flags)

    pctPerm = property(_get_pctPerm, _set_pctPerm) # type: float

    def _get_Repair(self) -> float:
        """
        Hours to repair.

        DSS property name: `Repair`, DSS property index: 24.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    def _set_Repair(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 24, value, flags)

    Repair = property(_get_Repair, _set_Repair) # type: float

    def _get_BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 25.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 25)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 25, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float

    def _get_Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 26.
        """
        return self._lib.Obj_GetInt32(self._ptr, 26) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 26, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 27.
        """
        self._set_string_o(27, value)


class ReactorProperties(TypedDict):
    Bus1: AnyStr
    Bus2: AnyStr
    Phases: int
    kvar: float
    kV: float
    Conn: Union[AnyStr, int, enums.Connection]
    RMatrix: Float64Array
    XMatrix: Float64Array
    Parallel: bool
    R: float
    X: float
    Rp: float
    Z1: complex
    Z2: complex
    Z0: complex
    RCurve: Union[AnyStr, XYcurve]
    LCurve: Union[AnyStr, XYcurve]
    LmH: float
    NormAmps: float
    EmergAmps: float
    FaultRate: float
    pctPerm: float
    Repair: float
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class ReactorBatch(DSSBatch, CircuitElementBatchMixin, PDElementBatchMixin):
    _cls_name = 'Reactor'
    _obj_cls = Reactor
    _cls_idx = 23

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)
       PDElementBatchMixin.__init__(self)

    def _get_Bus1(self) -> List[str]:
        """
        Name of first bus. Examples:
        bus1=busname
        bus1=busname.1.2.3

        Bus2 property will default to this bus, node 0, unless previously specified. Only Bus1 need be specified for a Yg shunt reactor.

        DSS property name: `Bus1`, DSS property index: 1.
        """
        return self._get_batch_str_prop(1)

    def _set_Bus1(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(1, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: List[str]

    def _get_Bus2(self) -> List[str]:
        """
        Name of 2nd bus. Defaults to all phases connected to first bus, node 0, (Shunt Wye Connection) except when Bus2 is specifically defined.

        Not necessary to specify for delta (LL) connection

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

    def _get_kvar(self) -> BatchFloat64ArrayProxy:
        """
        Total kvar, all phases.  Evenly divided among phases. Only determines X. Specify R separately

        DSS property name: `kvar`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    def _set_kvar(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(4, value, flags)

    kvar = property(_get_kvar, _set_kvar) # type: BatchFloat64ArrayProxy

    def _get_kV(self) -> BatchFloat64ArrayProxy:
        """
        For 2, 3-phase, kV phase-phase. Otherwise specify actual coil rating.

        DSS property name: `kV`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    def _set_kV(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(5, value, flags)

    kV = property(_get_kV, _set_kV) # type: BatchFloat64ArrayProxy

    def _get_Conn(self) -> BatchInt32ArrayProxy:
        """
        ={wye | delta |LN |LL}  Default is wye, which is equivalent to LN. If Delta, then only one terminal.

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
        ={wye | delta |LN |LL}  Default is wye, which is equivalent to LN. If Delta, then only one terminal.

        DSS property name: `Conn`, DSS property index: 6.
        """
        return self._get_batch_str_prop(6)

    def _set_Conn_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Conn(value, flags)

    Conn_str = property(_get_Conn_str, _set_Conn_str) # type: List[str]

    def _get_RMatrix(self) -> List[Float64Array]:
        """
        Resistance matrix, lower triangle, ohms at base frequency. Order of the matrix is the number of phases. Mutually exclusive to specifying parameters by kvar or X.

        DSS property name: `RMatrix`, DSS property index: 7.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 7)
            for x in self._unpack()
        ]

    def _set_RMatrix(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(7, value, flags)

    RMatrix = property(_get_RMatrix, _set_RMatrix) # type: List[Float64Array]

    def _get_XMatrix(self) -> List[Float64Array]:
        """
        Reactance matrix, lower triangle, ohms at base frequency. Order of the matrix is the number of phases. Mutually exclusive to specifying parameters by kvar or X.

        DSS property name: `XMatrix`, DSS property index: 8.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 8)
            for x in self._unpack()
        ]

    def _set_XMatrix(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(8, value, flags)

    XMatrix = property(_get_XMatrix, _set_XMatrix) # type: List[Float64Array]

    def _get_Parallel(self) -> List[bool]:
        """
        {Yes | No}  Default=No. Indicates whether Rmatrix and Xmatrix are to be considered in parallel. Default is series. For other models, specify R and Rp.

        DSS property name: `Parallel`, DSS property index: 9.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(9)
        ]

    def _set_Parallel(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(9, value, flags)

    Parallel = property(_get_Parallel, _set_Parallel) # type: List[bool]

    def _get_R(self) -> BatchFloat64ArrayProxy:
        """
        Resistance (in series with reactance), each phase, ohms. This property applies to REACTOR specified by either kvar or X. See also help on Z.

        DSS property name: `R`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    def _set_R(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(10, value, flags)

    R = property(_get_R, _set_R) # type: BatchFloat64ArrayProxy

    def _get_X(self) -> BatchFloat64ArrayProxy:
        """
        Reactance, each phase, ohms at base frequency. See also help on Z and LmH properties.

        DSS property name: `X`, DSS property index: 11.
        """
        return BatchFloat64ArrayProxy(self, 11)

    def _set_X(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(11, value, flags)

    X = property(_get_X, _set_X) # type: BatchFloat64ArrayProxy

    def _get_Rp(self) -> BatchFloat64ArrayProxy:
        """
        Resistance in parallel with R and X (the entire branch). Assumed infinite if not specified.

        DSS property name: `Rp`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    def _set_Rp(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(12, value, flags)

    Rp = property(_get_Rp, _set_Rp) # type: BatchFloat64ArrayProxy

    def _get_Z1(self) -> List[complex]:
        """
        Positive-sequence impedance, ohms, as a 2-element array representing a complex number. Example: 

        Z1=[1, 2]  ! represents 1 + j2 

        If defined, Z1, Z2, and Z0 are used to define the impedance matrix of the REACTOR. Z1 MUST BE DEFINED TO USE THIS OPTION FOR DEFINING THE MATRIX.

        Side Effect: Sets Z2 and Z0 to same values unless they were previously defined.

        DSS property name: `Z1`, DSS property index: 13.
        """
        return [
            self._get_float64_array(
                self._lib.Obj_GetFloat64Array,
                x,
                13,
            ).view(dtype=complex)[0]
            for x in self._unpack()
        ]

    def _set_Z1(self, value: Union[complex, List[complex]], flags: enums.SetterFlags = 0):
        if isinstance(value, complex):
            value, value_ptr, value_count = self._prepare_float64_array([value.real, value.imag])
            for x in self._unpack():
                self._lib.Obj_SetFloat64Array(x, 13, value_ptr, value_count, flags)
            return

        values = value
        if len(values) != len(self):
            raise ValueError('Number of elements provided must match the number of objects in the batch.')

        value, value_ptr, value_count = self._prepare_float64_array([0, 0])
        for v, x in zip(values, self._unpack()):
            value[0] = v.real
            value[1] = v.imag
            self._lib.Obj_SetFloat64Array(x, 13, value_ptr, value_count, flags)

    Z1 = property(_get_Z1, _set_Z1) # type: List[complex]

    def _get_Z2(self) -> List[complex]:
        """
        Negative-sequence impedance, ohms, as a 2-element array representing a complex number. Example: 

        Z2=[1, 2]  ! represents 1 + j2 

        Used to define the impedance matrix of the REACTOR if Z1 is also specified. 

        Note: Z2 defaults to Z1 if it is not specifically defined. If Z2 is not equal to Z1, the impedance matrix is asymmetrical.

        DSS property name: `Z2`, DSS property index: 14.
        """
        return [
            self._get_float64_array(
                self._lib.Obj_GetFloat64Array,
                x,
                14,
            ).view(dtype=complex)[0]
            for x in self._unpack()
        ]

    def _set_Z2(self, value: Union[complex, List[complex]], flags: enums.SetterFlags = 0):
        if isinstance(value, complex):
            value, value_ptr, value_count = self._prepare_float64_array([value.real, value.imag])
            for x in self._unpack():
                self._lib.Obj_SetFloat64Array(x, 14, value_ptr, value_count, flags)
            return

        values = value
        if len(values) != len(self):
            raise ValueError('Number of elements provided must match the number of objects in the batch.')

        value, value_ptr, value_count = self._prepare_float64_array([0, 0])
        for v, x in zip(values, self._unpack()):
            value[0] = v.real
            value[1] = v.imag
            self._lib.Obj_SetFloat64Array(x, 14, value_ptr, value_count, flags)

    Z2 = property(_get_Z2, _set_Z2) # type: List[complex]

    def _get_Z0(self) -> List[complex]:
        """
        Zer0-sequence impedance, ohms, as a 2-element array representing a complex number. Example: 

        Z0=[3, 4]  ! represents 3 + j4 

        Used to define the impedance matrix of the REACTOR if Z1 is also specified. 

        Note: Z0 defaults to Z1 if it is not specifically defined. 

        DSS property name: `Z0`, DSS property index: 15.
        """
        return [
            self._get_float64_array(
                self._lib.Obj_GetFloat64Array,
                x,
                15,
            ).view(dtype=complex)[0]
            for x in self._unpack()
        ]

    def _set_Z0(self, value: Union[complex, List[complex]], flags: enums.SetterFlags = 0):
        if isinstance(value, complex):
            value, value_ptr, value_count = self._prepare_float64_array([value.real, value.imag])
            for x in self._unpack():
                self._lib.Obj_SetFloat64Array(x, 15, value_ptr, value_count, flags)
            return

        values = value
        if len(values) != len(self):
            raise ValueError('Number of elements provided must match the number of objects in the batch.')

        value, value_ptr, value_count = self._prepare_float64_array([0, 0])
        for v, x in zip(values, self._unpack()):
            value[0] = v.real
            value[1] = v.imag
            self._lib.Obj_SetFloat64Array(x, 15, value_ptr, value_count, flags)

    Z0 = property(_get_Z0, _set_Z0) # type: List[complex]

    def _get_RCurve_str(self) -> List[str]:
        """
        Name of XYCurve object, previously defined, describing per-unit variation of phase resistance, R, vs. frequency. Applies to resistance specified by R or Z property. If actual values are not known, R often increases by approximately the square root of frequency.

        DSS property name: `RCurve`, DSS property index: 17.
        """
        return self._get_batch_str_prop(17)

    def _set_RCurve_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(17, value, flags)

    RCurve_str = property(_get_RCurve_str, _set_RCurve_str) # type: List[str]

    def _get_RCurve(self) -> List[XYcurve]:
        """
        Name of XYCurve object, previously defined, describing per-unit variation of phase resistance, R, vs. frequency. Applies to resistance specified by R or Z property. If actual values are not known, R often increases by approximately the square root of frequency.

        DSS property name: `RCurve`, DSS property index: 17.
        """
        return self._get_batch_obj_prop(17)

    def _set_RCurve(self, value: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(17, value, flags)

    RCurve = property(_get_RCurve, _set_RCurve) # type: List[XYcurve]

    def _get_LCurve_str(self) -> List[str]:
        """
        Name of XYCurve object, previously defined, describing per-unit variation of phase inductance, L=X/w, vs. frequency. Applies to reactance specified by X, LmH, Z, or kvar property.L generally decreases somewhat with frequency above the base frequency, approaching a limit at a few kHz.

        DSS property name: `LCurve`, DSS property index: 18.
        """
        return self._get_batch_str_prop(18)

    def _set_LCurve_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(18, value, flags)

    LCurve_str = property(_get_LCurve_str, _set_LCurve_str) # type: List[str]

    def _get_LCurve(self) -> List[XYcurve]:
        """
        Name of XYCurve object, previously defined, describing per-unit variation of phase inductance, L=X/w, vs. frequency. Applies to reactance specified by X, LmH, Z, or kvar property.L generally decreases somewhat with frequency above the base frequency, approaching a limit at a few kHz.

        DSS property name: `LCurve`, DSS property index: 18.
        """
        return self._get_batch_obj_prop(18)

    def _set_LCurve(self, value: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(18, value, flags)

    LCurve = property(_get_LCurve, _set_LCurve) # type: List[XYcurve]

    def _get_LmH(self) -> BatchFloat64ArrayProxy:
        """
        Inductance, mH. Alternate way to define the reactance, X, property.

        DSS property name: `LmH`, DSS property index: 19.
        """
        return BatchFloat64ArrayProxy(self, 19)

    def _set_LmH(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(19, value, flags)

    LmH = property(_get_LmH, _set_LmH) # type: BatchFloat64ArrayProxy

    def _get_NormAmps(self) -> BatchFloat64ArrayProxy:
        """
        Normal rated current. Defaults to per-phase rated current when reactor is specified with rated power and voltage.

        DSS property name: `NormAmps`, DSS property index: 20.
        """
        return BatchFloat64ArrayProxy(self, 20)

    def _set_NormAmps(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(20, value, flags)

    NormAmps = property(_get_NormAmps, _set_NormAmps) # type: BatchFloat64ArrayProxy

    def _get_EmergAmps(self) -> BatchFloat64ArrayProxy:
        """
        Maximum or emerg current. Defaults to 135% of per-phase rated current when reactor is specified with rated power and voltage.

        DSS property name: `EmergAmps`, DSS property index: 21.
        """
        return BatchFloat64ArrayProxy(self, 21)

    def _set_EmergAmps(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(21, value, flags)

    EmergAmps = property(_get_EmergAmps, _set_EmergAmps) # type: BatchFloat64ArrayProxy

    def _get_FaultRate(self) -> BatchFloat64ArrayProxy:
        """
        Failure rate per year.

        DSS property name: `FaultRate`, DSS property index: 22.
        """
        return BatchFloat64ArrayProxy(self, 22)

    def _set_FaultRate(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(22, value, flags)

    FaultRate = property(_get_FaultRate, _set_FaultRate) # type: BatchFloat64ArrayProxy

    def _get_pctPerm(self) -> BatchFloat64ArrayProxy:
        """
        Percent of failures that become permanent.

        DSS property name: `pctPerm`, DSS property index: 23.
        """
        return BatchFloat64ArrayProxy(self, 23)

    def _set_pctPerm(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(23, value, flags)

    pctPerm = property(_get_pctPerm, _set_pctPerm) # type: BatchFloat64ArrayProxy

    def _get_Repair(self) -> BatchFloat64ArrayProxy:
        """
        Hours to repair.

        DSS property name: `Repair`, DSS property index: 24.
        """
        return BatchFloat64ArrayProxy(self, 24)

    def _set_Repair(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(24, value, flags)

    Repair = property(_get_Repair, _set_Repair) # type: BatchFloat64ArrayProxy

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 25.
        """
        return BatchFloat64ArrayProxy(self, 25)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(25, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy

    def _get_Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 26.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(26)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(26, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 27.
        """
        self._set_batch_string(27, value, flags)

class ReactorBatchProperties(TypedDict):
    Bus1: Union[AnyStr, List[AnyStr]]
    Bus2: Union[AnyStr, List[AnyStr]]
    Phases: Union[int, Int32Array]
    kvar: Union[float, Float64Array]
    kV: Union[float, Float64Array]
    Conn: Union[AnyStr, int, enums.Connection, List[AnyStr], List[int], List[enums.Connection], Int32Array]
    RMatrix: Float64Array
    XMatrix: Float64Array
    Parallel: bool
    R: Union[float, Float64Array]
    X: Union[float, Float64Array]
    Rp: Union[float, Float64Array]
    Z1: Union[complex, List[complex]]
    Z2: Union[complex, List[complex]]
    Z0: Union[complex, List[complex]]
    RCurve: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]
    LCurve: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]
    LmH: Union[float, Float64Array]
    NormAmps: Union[float, Float64Array]
    EmergAmps: Union[float, Float64Array]
    FaultRate: Union[float, Float64Array]
    pctPerm: Union[float, Float64Array]
    Repair: Union[float, Float64Array]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IReactor(IDSSObj, ReactorBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, Reactor, ReactorBatch)
        ReactorBatch.__init__(self, self._api_util, sync_cls_idx=Reactor._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Reactor:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[ReactorProperties]) -> Reactor:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[ReactorBatchProperties]) -> ReactorBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
