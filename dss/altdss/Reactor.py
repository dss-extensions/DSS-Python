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
from .XYcurve import XYcurve

class Reactor(DSSObj, CktElementMixin, PDElementMixin):
    __slots__ = CktElementMixin._extra_slots + PDElementMixin._extra_slots
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

    @property
    def Bus1(self) -> str:
        """
        Name of first bus. Examples:
        bus1=busname
        bus1=busname.1.2.3

        Bus2 property will default to this bus, node 0, unless previously specified. Only Bus1 need be specified for a Yg shunt reactor.

        DSS property name: `Bus1`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    @Bus1.setter
    def Bus1(self, value: AnyStr):
        self._set_string_o(1, value)

    @property
    def Bus2(self) -> str:
        """
        Name of 2nd bus. Defaults to all phases connected to first bus, node 0, (Shunt Wye Connection) except when Bus2 is specifically defined.

        Not necessary to specify for delta (LL) connection

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
    def kvar(self) -> float:
        """
        Total kvar, all phases.  Evenly divided among phases. Only determines X. Specify R separately

        DSS property name: `kvar`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @kvar.setter
    def kvar(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def kV(self) -> float:
        """
        For 2, 3-phase, kV phase-phase. Otherwise specify actual coil rating.

        DSS property name: `kV`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @kV.setter
    def kV(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def Conn(self) -> enums.Connection:
        """
        ={wye | delta |LN |LL}  Default is wye, which is equivalent to LN. If Delta, then only one terminal.

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
        ={wye | delta |LN |LL}  Default is wye, which is equivalent to LN. If Delta, then only one terminal.

        DSS property name: `Conn`, DSS property index: 6.
        """
        return self._get_prop_string(6)

    @Conn_str.setter
    def Conn_str(self, value: AnyStr):
        self.Conn = value

    @property
    def RMatrix(self) -> Float64Array:
        """
        Resistance matrix, lower triangle, ohms at base frequency. Order of the matrix is the number of phases. Mutually exclusive to specifying parameters by kvar or X.

        DSS property name: `RMatrix`, DSS property index: 7.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 7)

    @RMatrix.setter
    def RMatrix(self, value: Float64Array):
        self._set_float64_array_o(7, value)

    @property
    def XMatrix(self) -> Float64Array:
        """
        Reactance matrix, lower triangle, ohms at base frequency. Order of the matrix is the number of phases. Mutually exclusive to specifying parameters by kvar or X.

        DSS property name: `XMatrix`, DSS property index: 8.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 8)

    @XMatrix.setter
    def XMatrix(self, value: Float64Array):
        self._set_float64_array_o(8, value)

    @property
    def Parallel(self) -> bool:
        """
        {Yes | No}  Default=No. Indicates whether Rmatrix and Xmatrix are to be considered in parallel. Default is series. For other models, specify R and Rp.

        DSS property name: `Parallel`, DSS property index: 9.
        """
        return self._lib.Obj_GetInt32(self._ptr, 9) != 0

    @Parallel.setter
    def Parallel(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 9, value)

    @property
    def R(self) -> float:
        """
        Resistance (in series with reactance), each phase, ohms. This property applies to REACTOR specified by either kvar or X. See also help on Z.

        DSS property name: `R`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @R.setter
    def R(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def X(self) -> float:
        """
        Reactance, each phase, ohms at base frequency. See also help on Z and LmH properties.

        DSS property name: `X`, DSS property index: 11.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @X.setter
    def X(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def Rp(self) -> float:
        """
        Resistance in parallel with R and X (the entire branch). Assumed infinite if not specified.

        DSS property name: `Rp`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @Rp.setter
    def Rp(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def Z1(self) -> complex:
        """
        Positive-sequence impedance, ohms, as a 2-element array representing a complex number. Example: 

        Z1=[1, 2]  ! represents 1 + j2 

        If defined, Z1, Z2, and Z0 are used to define the impedance matrix of the REACTOR. Z1 MUST BE DEFINED TO USE THIS OPTION FOR DEFINING THE MATRIX.

        Side Effect: Sets Z2 and Z0 to same values unless they were previously defined.

        DSS property name: `Z1`, DSS property index: 13.
        """
        return self._get_complex(13)

    @Z1.setter
    def Z1(self, value: complex):
        self._set_complex(13, value)

    @property
    def Z2(self) -> complex:
        """
        Negative-sequence impedance, ohms, as a 2-element array representing a complex number. Example: 

        Z2=[1, 2]  ! represents 1 + j2 

        Used to define the impedance matrix of the REACTOR if Z1 is also specified. 

        Note: Z2 defaults to Z1 if it is not specifically defined. If Z2 is not equal to Z1, the impedance matrix is asymmetrical.

        DSS property name: `Z2`, DSS property index: 14.
        """
        return self._get_complex(14)

    @Z2.setter
    def Z2(self, value: complex):
        self._set_complex(14, value)

    @property
    def Z0(self) -> complex:
        """
        Zer0-sequence impedance, ohms, as a 2-element array representing a complex number. Example: 

        Z0=[3, 4]  ! represents 3 + j4 

        Used to define the impedance matrix of the REACTOR if Z1 is also specified. 

        Note: Z0 defaults to Z1 if it is not specifically defined. 

        DSS property name: `Z0`, DSS property index: 15.
        """
        return self._get_complex(15)

    @Z0.setter
    def Z0(self, value: complex):
        self._set_complex(15, value)

    @property
    def RCurve(self) -> str:
        """
        Name of XYCurve object, previously defined, describing per-unit variation of phase resistance, R, vs. frequency. Applies to resistance specified by R or Z property. If actual values are not known, R often increases by approximately the square root of frequency.

        DSS property name: `RCurve`, DSS property index: 17.
        """
        return self._get_prop_string(17)

    @RCurve.setter
    def RCurve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(17, value)
            return

        self._set_string_o(17, value)

    @property
    def RCurve_obj(self) -> XYcurve:
        """
        Name of XYCurve object, previously defined, describing per-unit variation of phase resistance, R, vs. frequency. Applies to resistance specified by R or Z property. If actual values are not known, R often increases by approximately the square root of frequency.

        DSS property name: `RCurve`, DSS property index: 17.
        """
        return self._get_obj(17, XYcurve)

    @RCurve_obj.setter
    def RCurve_obj(self, value: XYcurve):
        self._set_obj(17, value)

    @property
    def LCurve(self) -> str:
        """
        Name of XYCurve object, previously defined, describing per-unit variation of phase inductance, L=X/w, vs. frequency. Applies to reactance specified by X, LmH, Z, or kvar property.L generally decreases somewhat with frequency above the base frequency, approaching a limit at a few kHz.

        DSS property name: `LCurve`, DSS property index: 18.
        """
        return self._get_prop_string(18)

    @LCurve.setter
    def LCurve(self, value: Union[AnyStr, XYcurve]):
        if isinstance(value, DSSObj):
            self._set_obj(18, value)
            return

        self._set_string_o(18, value)

    @property
    def LCurve_obj(self) -> XYcurve:
        """
        Name of XYCurve object, previously defined, describing per-unit variation of phase inductance, L=X/w, vs. frequency. Applies to reactance specified by X, LmH, Z, or kvar property.L generally decreases somewhat with frequency above the base frequency, approaching a limit at a few kHz.

        DSS property name: `LCurve`, DSS property index: 18.
        """
        return self._get_obj(18, XYcurve)

    @LCurve_obj.setter
    def LCurve_obj(self, value: XYcurve):
        self._set_obj(18, value)

    @property
    def LmH(self) -> float:
        """
        Inductance, mH. Alternate way to define the reactance, X, property.

        DSS property name: `LmH`, DSS property index: 19.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    @LmH.setter
    def LmH(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 19, value)

    @property
    def NormAmps(self) -> float:
        """
        Normal rated current. Defaults to per-phase rated current when reactor is specified with rated power and voltage.

        DSS property name: `NormAmps`, DSS property index: 20.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    @NormAmps.setter
    def NormAmps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 20, value)

    @property
    def EmergAmps(self) -> float:
        """
        Maximum or emerg current. Defaults to 135% of per-phase rated current when reactor is specified with rated power and voltage.

        DSS property name: `EmergAmps`, DSS property index: 21.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @EmergAmps.setter
    def EmergAmps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    @property
    def FaultRate(self) -> float:
        """
        Failure rate per year.

        DSS property name: `FaultRate`, DSS property index: 22.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    @FaultRate.setter
    def FaultRate(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 22, value)

    @property
    def pctPerm(self) -> float:
        """
        Percent of failures that become permanent.

        DSS property name: `pctPerm`, DSS property index: 23.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    @pctPerm.setter
    def pctPerm(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 23, value)

    @property
    def Repair(self) -> float:
        """
        Hours to repair.

        DSS property name: `Repair`, DSS property index: 24.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    @Repair.setter
    def Repair(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 24, value)

    @property
    def BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 25.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 25)

    @BaseFreq.setter
    def BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 25, value)

    @property
    def Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 26.
        """
        return self._lib.Obj_GetInt32(self._ptr, 26) != 0

    @Enabled.setter
    def Enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 26, value)

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

class ReactorBatch(DSSBatch):
    _cls_name = 'Reactor'
    _obj_cls = Reactor
    _cls_idx = 23


    @property
    def Bus1(self) -> List[str]:
        """
        Name of first bus. Examples:
        bus1=busname
        bus1=busname.1.2.3

        Bus2 property will default to this bus, node 0, unless previously specified. Only Bus1 need be specified for a Yg shunt reactor.

        DSS property name: `Bus1`, DSS property index: 1.
        """
        return self._get_batch_str_prop(1) 

    @Bus1.setter
    def Bus1(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(1, value)

    @property
    def Bus2(self) -> List[str]:
        """
        Name of 2nd bus. Defaults to all phases connected to first bus, node 0, (Shunt Wye Connection) except when Bus2 is specifically defined.

        Not necessary to specify for delta (LL) connection

        DSS property name: `Bus2`, DSS property index: 2.
        """
        return self._get_batch_str_prop(2) 

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
    def kvar(self) -> BatchFloat64ArrayProxy:
        """
        Total kvar, all phases.  Evenly divided among phases. Only determines X. Specify R separately

        DSS property name: `kvar`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    @kvar.setter
    def kvar(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(4, value)

    @property
    def kV(self) -> BatchFloat64ArrayProxy:
        """
        For 2, 3-phase, kV phase-phase. Otherwise specify actual coil rating.

        DSS property name: `kV`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    @kV.setter
    def kV(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(5, value)

    @property
    def Conn(self) -> BatchInt32ArrayProxy:
        """
        ={wye | delta |LN |LL}  Default is wye, which is equivalent to LN. If Delta, then only one terminal.

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
        ={wye | delta |LN |LL}  Default is wye, which is equivalent to LN. If Delta, then only one terminal.

        DSS property name: `Conn`, DSS property index: 6.
        """
        return self._get_batch_str_prop(6)

    @Conn_str.setter
    def Conn_str(self, value: AnyStr):
        self.Conn = value

    @property
    def RMatrix(self) -> List[Float64Array]:
        """
        Resistance matrix, lower triangle, ohms at base frequency. Order of the matrix is the number of phases. Mutually exclusive to specifying parameters by kvar or X.

        DSS property name: `RMatrix`, DSS property index: 7.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 7)
            for x in self._unpack()
        ]

    @RMatrix.setter
    def RMatrix(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(7, value)

    @property
    def XMatrix(self) -> List[Float64Array]:
        """
        Reactance matrix, lower triangle, ohms at base frequency. Order of the matrix is the number of phases. Mutually exclusive to specifying parameters by kvar or X.

        DSS property name: `XMatrix`, DSS property index: 8.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 8)
            for x in self._unpack()
        ]

    @XMatrix.setter
    def XMatrix(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(8, value)

    @property
    def Parallel(self) -> List[bool]:
        """
        {Yes | No}  Default=No. Indicates whether Rmatrix and Xmatrix are to be considered in parallel. Default is series. For other models, specify R and Rp.

        DSS property name: `Parallel`, DSS property index: 9.
        """
        return [v != 0 for v in 
            self._get_batch_int32_prop(9)
        ]
    @Parallel.setter
    def Parallel(self, value: bool):
        self._set_batch_int32_array(9, value)

    @property
    def R(self) -> BatchFloat64ArrayProxy:
        """
        Resistance (in series with reactance), each phase, ohms. This property applies to REACTOR specified by either kvar or X. See also help on Z.

        DSS property name: `R`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    @R.setter
    def R(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(10, value)

    @property
    def X(self) -> BatchFloat64ArrayProxy:
        """
        Reactance, each phase, ohms at base frequency. See also help on Z and LmH properties.

        DSS property name: `X`, DSS property index: 11.
        """
        return BatchFloat64ArrayProxy(self, 11)

    @X.setter
    def X(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(11, value)

    @property
    def Rp(self) -> BatchFloat64ArrayProxy:
        """
        Resistance in parallel with R and X (the entire branch). Assumed infinite if not specified.

        DSS property name: `Rp`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    @Rp.setter
    def Rp(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(12, value)

    @property
    def Z1(self) -> List[complex]:
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

    @Z1.setter
    def Z1(self, value: Union[complex, List[complex]]):
        if isinstance(value, complex):
            value, value_ptr, value_count = self._prepare_float64_array([value.real, value.imag])
            for x in self._unpack():
                self._lib.Obj_SetFloat64Array(x, 13, value_ptr, value_count)
            return

        values = value
        if len(values) != len(self):
            raise ValueError('Number of elements provided must match the number of objects in the batch.')

        value, value_ptr, value_count = self._prepare_float64_array([0, 0])
        for v, x in zip(values, self._unpack()):
            value[0] = v.real
            value[1] = v.imag
            self._lib.Obj_SetFloat64Array(x, 13, value_ptr, value_count)

    @property
    def Z2(self) -> List[complex]:
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

    @Z2.setter
    def Z2(self, value: Union[complex, List[complex]]):
        if isinstance(value, complex):
            value, value_ptr, value_count = self._prepare_float64_array([value.real, value.imag])
            for x in self._unpack():
                self._lib.Obj_SetFloat64Array(x, 14, value_ptr, value_count)
            return

        values = value
        if len(values) != len(self):
            raise ValueError('Number of elements provided must match the number of objects in the batch.')

        value, value_ptr, value_count = self._prepare_float64_array([0, 0])
        for v, x in zip(values, self._unpack()):
            value[0] = v.real
            value[1] = v.imag
            self._lib.Obj_SetFloat64Array(x, 14, value_ptr, value_count)

    @property
    def Z0(self) -> List[complex]:
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

    @Z0.setter
    def Z0(self, value: Union[complex, List[complex]]):
        if isinstance(value, complex):
            value, value_ptr, value_count = self._prepare_float64_array([value.real, value.imag])
            for x in self._unpack():
                self._lib.Obj_SetFloat64Array(x, 15, value_ptr, value_count)
            return

        values = value
        if len(values) != len(self):
            raise ValueError('Number of elements provided must match the number of objects in the batch.')

        value, value_ptr, value_count = self._prepare_float64_array([0, 0])
        for v, x in zip(values, self._unpack()):
            value[0] = v.real
            value[1] = v.imag
            self._lib.Obj_SetFloat64Array(x, 15, value_ptr, value_count)

    @property
    def RCurve(self) -> List[str]:
        """
        Name of XYCurve object, previously defined, describing per-unit variation of phase resistance, R, vs. frequency. Applies to resistance specified by R or Z property. If actual values are not known, R often increases by approximately the square root of frequency.

        DSS property name: `RCurve`, DSS property index: 17.
        """
        return self._get_batch_str_prop(17)

    @RCurve.setter
    def RCurve(self, value: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]):
        self._set_batch_obj_prop(17, value)

    @property
    def RCurve_obj(self) -> List[XYcurve]:
        """
        Name of XYCurve object, previously defined, describing per-unit variation of phase resistance, R, vs. frequency. Applies to resistance specified by R or Z property. If actual values are not known, R often increases by approximately the square root of frequency.

        DSS property name: `RCurve`, DSS property index: 17.
        """
        return self._get_batch_obj_prop(17)

    @RCurve_obj.setter
    def RCurve_obj(self, value: XYcurve):
        self._set_batch_string(17, value)

    @property
    def LCurve(self) -> List[str]:
        """
        Name of XYCurve object, previously defined, describing per-unit variation of phase inductance, L=X/w, vs. frequency. Applies to reactance specified by X, LmH, Z, or kvar property.L generally decreases somewhat with frequency above the base frequency, approaching a limit at a few kHz.

        DSS property name: `LCurve`, DSS property index: 18.
        """
        return self._get_batch_str_prop(18)

    @LCurve.setter
    def LCurve(self, value: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]):
        self._set_batch_obj_prop(18, value)

    @property
    def LCurve_obj(self) -> List[XYcurve]:
        """
        Name of XYCurve object, previously defined, describing per-unit variation of phase inductance, L=X/w, vs. frequency. Applies to reactance specified by X, LmH, Z, or kvar property.L generally decreases somewhat with frequency above the base frequency, approaching a limit at a few kHz.

        DSS property name: `LCurve`, DSS property index: 18.
        """
        return self._get_batch_obj_prop(18)

    @LCurve_obj.setter
    def LCurve_obj(self, value: XYcurve):
        self._set_batch_string(18, value)

    @property
    def LmH(self) -> BatchFloat64ArrayProxy:
        """
        Inductance, mH. Alternate way to define the reactance, X, property.

        DSS property name: `LmH`, DSS property index: 19.
        """
        return BatchFloat64ArrayProxy(self, 19)

    @LmH.setter
    def LmH(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(19, value)

    @property
    def NormAmps(self) -> BatchFloat64ArrayProxy:
        """
        Normal rated current. Defaults to per-phase rated current when reactor is specified with rated power and voltage.

        DSS property name: `NormAmps`, DSS property index: 20.
        """
        return BatchFloat64ArrayProxy(self, 20)

    @NormAmps.setter
    def NormAmps(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(20, value)

    @property
    def EmergAmps(self) -> BatchFloat64ArrayProxy:
        """
        Maximum or emerg current. Defaults to 135% of per-phase rated current when reactor is specified with rated power and voltage.

        DSS property name: `EmergAmps`, DSS property index: 21.
        """
        return BatchFloat64ArrayProxy(self, 21)

    @EmergAmps.setter
    def EmergAmps(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(21, value)

    @property
    def FaultRate(self) -> BatchFloat64ArrayProxy:
        """
        Failure rate per year.

        DSS property name: `FaultRate`, DSS property index: 22.
        """
        return BatchFloat64ArrayProxy(self, 22)

    @FaultRate.setter
    def FaultRate(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(22, value)

    @property
    def pctPerm(self) -> BatchFloat64ArrayProxy:
        """
        Percent of failures that become permanent.

        DSS property name: `pctPerm`, DSS property index: 23.
        """
        return BatchFloat64ArrayProxy(self, 23)

    @pctPerm.setter
    def pctPerm(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(23, value)

    @property
    def Repair(self) -> BatchFloat64ArrayProxy:
        """
        Hours to repair.

        DSS property name: `Repair`, DSS property index: 24.
        """
        return BatchFloat64ArrayProxy(self, 24)

    @Repair.setter
    def Repair(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(24, value)

    @property
    def BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 25.
        """
        return BatchFloat64ArrayProxy(self, 25)

    @BaseFreq.setter
    def BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(25, value)

    @property
    def Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 26.
        """
        return [v != 0 for v in 
            self._get_batch_int32_prop(26)
        ]
    @Enabled.setter
    def Enabled(self, value: bool):
        self._set_batch_int32_array(26, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 27.
        """
        self._set_batch_string(27, value)

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

class IReactor(IDSSObj,ReactorBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, Reactor, ReactorBatch)
        ReactorBatch.__init__(self, self._api_util, sync_cls=True)
        

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Reactor:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[ReactorProperties]) -> Reactor:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[ReactorBatchProperties]) -> ReactorBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
