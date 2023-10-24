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

class LineCode(DSSObj):
    __slots__ = []
    _cls_name = 'LineCode'
    _cls_idx = 1
    _cls_prop_idx = {
        'nphases': 1,
        'r1': 2,
        'x1': 3,
        'r0': 4,
        'x0': 5,
        'c1': 6,
        'c0': 7,
        'units': 8,
        'rmatrix': 9,
        'xmatrix': 10,
        'cmatrix': 11,
        'basefreq': 12,
        'normamps': 13,
        'emergamps': 14,
        'faultrate': 15,
        'pctperm': 16,
        'repair': 17,
        'kron': 18,
        'rg': 19,
        'xg': 20,
        'rho': 21,
        'neutral': 22,
        'b1': 23,
        'b0': 24,
        'seasons': 25,
        'ratings': 26,
        'linetype': 27,
        'like': 28,
    }

    @property
    def NPhases(self) -> int:
        """
        Number of phases in the line this line code data represents.  Setting this property reinitializes the line code.  Impedance matrix is reset for default symmetrical component.

        DSS property name: `NPhases`, DSS property index: 1.
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @NPhases.setter
    def NPhases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def R1(self) -> float:
        """
        Positive-sequence Resistance, ohms per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition. See also Rmatrix.

        DSS property name: `R1`, DSS property index: 2.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 2)

    @R1.setter
    def R1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 2, value)

    @property
    def X1(self) -> float:
        """
        Positive-sequence Reactance, ohms per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition. See also Xmatrix

        DSS property name: `X1`, DSS property index: 3.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @X1.setter
    def X1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def R0(self) -> float:
        """
        Zero-sequence Resistance, ohms per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.

        DSS property name: `R0`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @R0.setter
    def R0(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def X0(self) -> float:
        """
        Zero-sequence Reactance, ohms per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.

        DSS property name: `X0`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @X0.setter
    def X0(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def C1(self) -> float:
        """
        Positive-sequence capacitance, nf per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition. See also Cmatrix and B1.

        DSS property name: `C1`, DSS property index: 6.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    @C1.setter
    def C1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 6, value)

    @property
    def C0(self) -> float:
        """
        Zero-sequence capacitance, nf per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition. See also B0.

        DSS property name: `C0`, DSS property index: 7.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @C0.setter
    def C0(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def Units(self) -> enums.LengthUnit:
        """
        One of (ohms per ...) {none|mi|km|kft|m|me|ft|in|cm}.  Default is none; assumes units agree with length units given in Line object

        DSS property name: `Units`, DSS property index: 8.
        """
        return enums.LengthUnit(self._lib.Obj_GetInt32(self._ptr, 8))

    @Units.setter
    def Units(self, value: Union[AnyStr, int, enums.LengthUnit]):
        if not isinstance(value, int):
            self._set_string_o(8, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 8, value)

    @property
    def Units_str(self) -> str:
        """
        One of (ohms per ...) {none|mi|km|kft|m|me|ft|in|cm}.  Default is none; assumes units agree with length units given in Line object

        DSS property name: `Units`, DSS property index: 8.
        """
        return self._get_prop_string(8)

    @Units_str.setter
    def Units_str(self, value: AnyStr):
        self.Units = value

    @property
    def RMatrix(self) -> Float64Array:
        """
        Resistance matrix, lower triangle, ohms per unit length. Order of the matrix is the number of phases. May be used to specify the impedance of any line configuration.  For balanced line models, you may use the standard symmetrical component data definition instead.

        DSS property name: `RMatrix`, DSS property index: 9.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 9)

    @RMatrix.setter
    def RMatrix(self, value: Float64Array):
        self._set_float64_array_o(9, value)

    @property
    def XMatrix(self) -> Float64Array:
        """
        Reactance matrix, lower triangle, ohms per unit length. Order of the matrix is the number of phases. May be used to specify the impedance of any line configuration.  For balanced line models, you may use the standard symmetrical component data definition instead.

        DSS property name: `XMatrix`, DSS property index: 10.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 10)

    @XMatrix.setter
    def XMatrix(self, value: Float64Array):
        self._set_float64_array_o(10, value)

    @property
    def CMatrix(self) -> Float64Array:
        """
        Nodal Capacitance matrix, lower triangle, nf per unit length.Order of the matrix is the number of phases. May be used to specify the shunt capacitance of any line configuration.  For balanced line models, you may use the standard symmetrical component data definition instead.

        DSS property name: `CMatrix`, DSS property index: 11.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 11)

    @CMatrix.setter
    def CMatrix(self, value: Float64Array):
        self._set_float64_array_o(11, value)

    @property
    def BaseFreq(self) -> float:
        """
        Frequency at which impedances are specified.

        DSS property name: `BaseFreq`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @BaseFreq.setter
    def BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def NormAmps(self) -> float:
        """
        Normal ampere limit on line.  This is the so-called Planning Limit. It may also be the value above which load will have to be dropped in a contingency.  Usually about 75% - 80% of the emergency (one-hour) rating.

        DSS property name: `NormAmps`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @NormAmps.setter
    def NormAmps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def EmergAmps(self) -> float:
        """
        Emergency ampere limit on line (usually one-hour rating).

        DSS property name: `EmergAmps`, DSS property index: 14.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @EmergAmps.setter
    def EmergAmps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def FaultRate(self) -> float:
        """
        Number of faults per unit length per year.

        DSS property name: `FaultRate`, DSS property index: 15.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @FaultRate.setter
    def FaultRate(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def PctPerm(self) -> float:
        """
        Percentage of the faults that become permanent.

        DSS property name: `PctPerm`, DSS property index: 16.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    @PctPerm.setter
    def PctPerm(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 16, value)

    @property
    def Repair(self) -> float:
        """
        Hours to repair.

        DSS property name: `Repair`, DSS property index: 17.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    @Repair.setter
    def Repair(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 17, value)

    def Kron(self, value: bool = True):
        """
        Kron = Y/N. Default=N.  Perform Kron reduction on the impedance matrix after it is formed, reducing order by 1. Eliminates the conductor designated by the "Neutral=" property. Do this after the R, X, and C matrices are defined. Ignored for symmetrical components. May be issued more than once to eliminate more than one conductor by resetting the Neutral property after the previous invoking of this property. Generally, you do not want to do a Kron reduction on the matrix if you intend to solve at a frequency other than the base frequency and exploit the Rg and Xg values.

        DSS property name: `Kron`, DSS property index: 18.
        """
        self._lib.Obj_SetInt32(self._ptr, 18, value)

    @property
    def Rg(self) -> float:
        """
        Carson earth return resistance per unit length used to compute impedance values at base frequency.  For making better frequency adjustments. Default is 0.01805 = 60 Hz value in ohms per kft (matches default line impedances). This value is required for harmonic solutions if you wish to adjust the earth return impedances for frequency. If not, set both Rg and Xg = 0.

        DSS property name: `Rg`, DSS property index: 19.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    @Rg.setter
    def Rg(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 19, value)

    @property
    def Xg(self) -> float:
        """
        Carson earth return reactance per unit length used to compute impedance values at base frequency.  For making better frequency adjustments. Default value is 0.155081 = 60 Hz value in ohms per kft (matches default line impedances). This value is required for harmonic solutions if you wish to adjust the earth return impedances for frequency. If not, set both Rg and Xg = 0.

        DSS property name: `Xg`, DSS property index: 20.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    @Xg.setter
    def Xg(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 20, value)

    @property
    def rho(self) -> float:
        """
        Default=100 meter ohms.  Earth resitivity used to compute earth correction factor.

        DSS property name: `rho`, DSS property index: 21.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @rho.setter
    def rho(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    @property
    def Neutral(self) -> int:
        """
        Designates which conductor is the "neutral" conductor that will be eliminated by Kron reduction. Default is the last conductor (nphases value). After Kron reduction is set to 0. Subsequent issuing of Kron=Yes will not do anything until this property is set to a legal value. Applies only to LineCodes defined by R, X, and C matrix.

        DSS property name: `Neutral`, DSS property index: 22.
        """
        return self._lib.Obj_GetInt32(self._ptr, 22)

    @Neutral.setter
    def Neutral(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 22, value)

    @property
    def B1(self) -> float:
        """
        Alternate way to specify C1. MicroS per unit length

        DSS property name: `B1`, DSS property index: 23.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    @B1.setter
    def B1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 23, value)

    @property
    def B0(self) -> float:
        """
        Alternate way to specify C0. MicroS per unit length

        DSS property name: `B0`, DSS property index: 24.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    @B0.setter
    def B0(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 24, value)

    @property
    def Seasons(self) -> int:
        """
        Defines the number of ratings to be defined for the wire, to be used only when defining seasonal ratings using the "Ratings" property.

        DSS property name: `Seasons`, DSS property index: 25.
        """
        return self._lib.Obj_GetInt32(self._ptr, 25)

    @Seasons.setter
    def Seasons(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 25, value)

    @property
    def Ratings(self) -> Float64Array:
        """
        An array of ratings to be used when the seasonal ratings flag is True. It can be used to insert
        multiple ratings to change during a QSTS simulation to evaluate different ratings in lines.

        DSS property name: `Ratings`, DSS property index: 26.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 26)

    @Ratings.setter
    def Ratings(self, value: Float64Array):
        self._set_float64_array_o(26, value)

    @property
    def LineType(self) -> enums.LineType:
        """
        Code designating the type of line. 
        One of: OH, UG, UG_TS, UG_CN, SWT_LDBRK, SWT_FUSE, SWT_SECT, SWT_REC, SWT_DISC, SWT_BRK, SWT_ELBOW, BUSBAR

        OpenDSS currently does not use this internally. For whatever purpose the user defines. Default is OH.

        DSS property name: `LineType`, DSS property index: 27.
        """
        return enums.LineType(self._lib.Obj_GetInt32(self._ptr, 27))

    @LineType.setter
    def LineType(self, value: Union[AnyStr, int, enums.LineType]):
        if not isinstance(value, int):
            self._set_string_o(27, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 27, value)

    @property
    def LineType_str(self) -> str:
        """
        Code designating the type of line. 
        One of: OH, UG, UG_TS, UG_CN, SWT_LDBRK, SWT_FUSE, SWT_SECT, SWT_REC, SWT_DISC, SWT_BRK, SWT_ELBOW, BUSBAR

        OpenDSS currently does not use this internally. For whatever purpose the user defines. Default is OH.

        DSS property name: `LineType`, DSS property index: 27.
        """
        return self._get_prop_string(27)

    @LineType_str.setter
    def LineType_str(self, value: AnyStr):
        self.LineType = value

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 28.
        """
        self._set_string_o(28, value)


class LineCodeProperties(TypedDict):
    NPhases: int
    R1: float
    X1: float
    R0: float
    X0: float
    C1: float
    C0: float
    Units: Union[AnyStr, int, enums.LengthUnit]
    RMatrix: Float64Array
    XMatrix: Float64Array
    CMatrix: Float64Array
    BaseFreq: float
    NormAmps: float
    EmergAmps: float
    FaultRate: float
    PctPerm: float
    Repair: float
    Kron: bool
    Rg: float
    Xg: float
    rho: float
    Neutral: int
    B1: float
    B0: float
    Seasons: int
    Ratings: Float64Array
    LineType: Union[AnyStr, int, enums.LineType]
    Like: AnyStr

class LineCodeBatch(DSSBatch):
    _cls_name = 'LineCode'
    _obj_cls = LineCode
    _cls_idx = 1


    @property
    def NPhases(self) -> BatchInt32ArrayProxy:
        """
        Number of phases in the line this line code data represents.  Setting this property reinitializes the line code.  Impedance matrix is reset for default symmetrical component.

        DSS property name: `NPhases`, DSS property index: 1.
        """
        return BatchInt32ArrayProxy(self, 1)

    @NPhases.setter
    def NPhases(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(1, value)

    @property
    def R1(self) -> BatchFloat64ArrayProxy:
        """
        Positive-sequence Resistance, ohms per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition. See also Rmatrix.

        DSS property name: `R1`, DSS property index: 2.
        """
        return BatchFloat64ArrayProxy(self, 2)

    @R1.setter
    def R1(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(2, value)

    @property
    def X1(self) -> BatchFloat64ArrayProxy:
        """
        Positive-sequence Reactance, ohms per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition. See also Xmatrix

        DSS property name: `X1`, DSS property index: 3.
        """
        return BatchFloat64ArrayProxy(self, 3)

    @X1.setter
    def X1(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(3, value)

    @property
    def R0(self) -> BatchFloat64ArrayProxy:
        """
        Zero-sequence Resistance, ohms per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.

        DSS property name: `R0`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    @R0.setter
    def R0(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(4, value)

    @property
    def X0(self) -> BatchFloat64ArrayProxy:
        """
        Zero-sequence Reactance, ohms per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.

        DSS property name: `X0`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    @X0.setter
    def X0(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(5, value)

    @property
    def C1(self) -> BatchFloat64ArrayProxy:
        """
        Positive-sequence capacitance, nf per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition. See also Cmatrix and B1.

        DSS property name: `C1`, DSS property index: 6.
        """
        return BatchFloat64ArrayProxy(self, 6)

    @C1.setter
    def C1(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(6, value)

    @property
    def C0(self) -> BatchFloat64ArrayProxy:
        """
        Zero-sequence capacitance, nf per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition. See also B0.

        DSS property name: `C0`, DSS property index: 7.
        """
        return BatchFloat64ArrayProxy(self, 7)

    @C0.setter
    def C0(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(7, value)

    @property
    def Units(self) -> BatchInt32ArrayProxy:
        """
        One of (ohms per ...) {none|mi|km|kft|m|me|ft|in|cm}.  Default is none; assumes units agree with length units given in Line object

        DSS property name: `Units`, DSS property index: 8.
        """
        return BatchInt32ArrayProxy(self, 8)

    @Units.setter
    def Units(self, value: Union[AnyStr, int, enums.LengthUnit, List[AnyStr], List[int], List[enums.LengthUnit], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(8, value)
            return
    
        self._set_batch_int32_array(8, value)

    @property
    def Units_str(self) -> str:
        """
        One of (ohms per ...) {none|mi|km|kft|m|me|ft|in|cm}.  Default is none; assumes units agree with length units given in Line object

        DSS property name: `Units`, DSS property index: 8.
        """
        return self._get_batch_str_prop(8)

    @Units_str.setter
    def Units_str(self, value: AnyStr):
        self.Units = value

    @property
    def RMatrix(self) -> List[Float64Array]:
        """
        Resistance matrix, lower triangle, ohms per unit length. Order of the matrix is the number of phases. May be used to specify the impedance of any line configuration.  For balanced line models, you may use the standard symmetrical component data definition instead.

        DSS property name: `RMatrix`, DSS property index: 9.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 9)
            for x in self._unpack()
        ]

    @RMatrix.setter
    def RMatrix(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(9, value)

    @property
    def XMatrix(self) -> List[Float64Array]:
        """
        Reactance matrix, lower triangle, ohms per unit length. Order of the matrix is the number of phases. May be used to specify the impedance of any line configuration.  For balanced line models, you may use the standard symmetrical component data definition instead.

        DSS property name: `XMatrix`, DSS property index: 10.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 10)
            for x in self._unpack()
        ]

    @XMatrix.setter
    def XMatrix(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(10, value)

    @property
    def CMatrix(self) -> List[Float64Array]:
        """
        Nodal Capacitance matrix, lower triangle, nf per unit length.Order of the matrix is the number of phases. May be used to specify the shunt capacitance of any line configuration.  For balanced line models, you may use the standard symmetrical component data definition instead.

        DSS property name: `CMatrix`, DSS property index: 11.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 11)
            for x in self._unpack()
        ]

    @CMatrix.setter
    def CMatrix(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(11, value)

    @property
    def BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Frequency at which impedances are specified.

        DSS property name: `BaseFreq`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    @BaseFreq.setter
    def BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(12, value)

    @property
    def NormAmps(self) -> BatchFloat64ArrayProxy:
        """
        Normal ampere limit on line.  This is the so-called Planning Limit. It may also be the value above which load will have to be dropped in a contingency.  Usually about 75% - 80% of the emergency (one-hour) rating.

        DSS property name: `NormAmps`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    @NormAmps.setter
    def NormAmps(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(13, value)

    @property
    def EmergAmps(self) -> BatchFloat64ArrayProxy:
        """
        Emergency ampere limit on line (usually one-hour rating).

        DSS property name: `EmergAmps`, DSS property index: 14.
        """
        return BatchFloat64ArrayProxy(self, 14)

    @EmergAmps.setter
    def EmergAmps(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(14, value)

    @property
    def FaultRate(self) -> BatchFloat64ArrayProxy:
        """
        Number of faults per unit length per year.

        DSS property name: `FaultRate`, DSS property index: 15.
        """
        return BatchFloat64ArrayProxy(self, 15)

    @FaultRate.setter
    def FaultRate(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(15, value)

    @property
    def PctPerm(self) -> BatchFloat64ArrayProxy:
        """
        Percentage of the faults that become permanent.

        DSS property name: `PctPerm`, DSS property index: 16.
        """
        return BatchFloat64ArrayProxy(self, 16)

    @PctPerm.setter
    def PctPerm(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(16, value)

    @property
    def Repair(self) -> BatchFloat64ArrayProxy:
        """
        Hours to repair.

        DSS property name: `Repair`, DSS property index: 17.
        """
        return BatchFloat64ArrayProxy(self, 17)

    @Repair.setter
    def Repair(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(17, value)

    def Kron(self, value: Union[bool, List[bool]] = True):
        """
        Kron = Y/N. Default=N.  Perform Kron reduction on the impedance matrix after it is formed, reducing order by 1. Eliminates the conductor designated by the "Neutral=" property. Do this after the R, X, and C matrices are defined. Ignored for symmetrical components. May be issued more than once to eliminate more than one conductor by resetting the Neutral property after the previous invoking of this property. Generally, you do not want to do a Kron reduction on the matrix if you intend to solve at a frequency other than the base frequency and exploit the Rg and Xg values.

        DSS property name: `Kron`, DSS property index: 18.
        """
        self._set_batch_int32_array(18, value)

    @property
    def Rg(self) -> BatchFloat64ArrayProxy:
        """
        Carson earth return resistance per unit length used to compute impedance values at base frequency.  For making better frequency adjustments. Default is 0.01805 = 60 Hz value in ohms per kft (matches default line impedances). This value is required for harmonic solutions if you wish to adjust the earth return impedances for frequency. If not, set both Rg and Xg = 0.

        DSS property name: `Rg`, DSS property index: 19.
        """
        return BatchFloat64ArrayProxy(self, 19)

    @Rg.setter
    def Rg(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(19, value)

    @property
    def Xg(self) -> BatchFloat64ArrayProxy:
        """
        Carson earth return reactance per unit length used to compute impedance values at base frequency.  For making better frequency adjustments. Default value is 0.155081 = 60 Hz value in ohms per kft (matches default line impedances). This value is required for harmonic solutions if you wish to adjust the earth return impedances for frequency. If not, set both Rg and Xg = 0.

        DSS property name: `Xg`, DSS property index: 20.
        """
        return BatchFloat64ArrayProxy(self, 20)

    @Xg.setter
    def Xg(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(20, value)

    @property
    def rho(self) -> BatchFloat64ArrayProxy:
        """
        Default=100 meter ohms.  Earth resitivity used to compute earth correction factor.

        DSS property name: `rho`, DSS property index: 21.
        """
        return BatchFloat64ArrayProxy(self, 21)

    @rho.setter
    def rho(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(21, value)

    @property
    def Neutral(self) -> BatchInt32ArrayProxy:
        """
        Designates which conductor is the "neutral" conductor that will be eliminated by Kron reduction. Default is the last conductor (nphases value). After Kron reduction is set to 0. Subsequent issuing of Kron=Yes will not do anything until this property is set to a legal value. Applies only to LineCodes defined by R, X, and C matrix.

        DSS property name: `Neutral`, DSS property index: 22.
        """
        return BatchInt32ArrayProxy(self, 22)

    @Neutral.setter
    def Neutral(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(22, value)

    @property
    def B1(self) -> BatchFloat64ArrayProxy:
        """
        Alternate way to specify C1. MicroS per unit length

        DSS property name: `B1`, DSS property index: 23.
        """
        return BatchFloat64ArrayProxy(self, 23)

    @B1.setter
    def B1(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(23, value)

    @property
    def B0(self) -> BatchFloat64ArrayProxy:
        """
        Alternate way to specify C0. MicroS per unit length

        DSS property name: `B0`, DSS property index: 24.
        """
        return BatchFloat64ArrayProxy(self, 24)

    @B0.setter
    def B0(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(24, value)

    @property
    def Seasons(self) -> BatchInt32ArrayProxy:
        """
        Defines the number of ratings to be defined for the wire, to be used only when defining seasonal ratings using the "Ratings" property.

        DSS property name: `Seasons`, DSS property index: 25.
        """
        return BatchInt32ArrayProxy(self, 25)

    @Seasons.setter
    def Seasons(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(25, value)

    @property
    def Ratings(self) -> List[Float64Array]:
        """
        An array of ratings to be used when the seasonal ratings flag is True. It can be used to insert
        multiple ratings to change during a QSTS simulation to evaluate different ratings in lines.

        DSS property name: `Ratings`, DSS property index: 26.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 26)
            for x in self._unpack()
        ]

    @Ratings.setter
    def Ratings(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(26, value)

    @property
    def LineType(self) -> BatchInt32ArrayProxy:
        """
        Code designating the type of line. 
        One of: OH, UG, UG_TS, UG_CN, SWT_LDBRK, SWT_FUSE, SWT_SECT, SWT_REC, SWT_DISC, SWT_BRK, SWT_ELBOW, BUSBAR

        OpenDSS currently does not use this internally. For whatever purpose the user defines. Default is OH.

        DSS property name: `LineType`, DSS property index: 27.
        """
        return BatchInt32ArrayProxy(self, 27)

    @LineType.setter
    def LineType(self, value: Union[AnyStr, int, enums.LineType, List[AnyStr], List[int], List[enums.LineType], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(27, value)
            return
    
        self._set_batch_int32_array(27, value)

    @property
    def LineType_str(self) -> str:
        """
        Code designating the type of line. 
        One of: OH, UG, UG_TS, UG_CN, SWT_LDBRK, SWT_FUSE, SWT_SECT, SWT_REC, SWT_DISC, SWT_BRK, SWT_ELBOW, BUSBAR

        OpenDSS currently does not use this internally. For whatever purpose the user defines. Default is OH.

        DSS property name: `LineType`, DSS property index: 27.
        """
        return self._get_batch_str_prop(27)

    @LineType_str.setter
    def LineType_str(self, value: AnyStr):
        self.LineType = value

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 28.
        """
        self._set_batch_string(28, value)

class LineCodeBatchProperties(TypedDict):
    NPhases: Union[int, Int32Array]
    R1: Union[float, Float64Array]
    X1: Union[float, Float64Array]
    R0: Union[float, Float64Array]
    X0: Union[float, Float64Array]
    C1: Union[float, Float64Array]
    C0: Union[float, Float64Array]
    Units: Union[AnyStr, int, enums.LengthUnit, List[AnyStr], List[int], List[enums.LengthUnit], Int32Array]
    RMatrix: Float64Array
    XMatrix: Float64Array
    CMatrix: Float64Array
    BaseFreq: Union[float, Float64Array]
    NormAmps: Union[float, Float64Array]
    EmergAmps: Union[float, Float64Array]
    FaultRate: Union[float, Float64Array]
    PctPerm: Union[float, Float64Array]
    Repair: Union[float, Float64Array]
    Kron: bool
    Rg: Union[float, Float64Array]
    Xg: Union[float, Float64Array]
    rho: Union[float, Float64Array]
    Neutral: Union[int, Int32Array]
    B1: Union[float, Float64Array]
    B0: Union[float, Float64Array]
    Seasons: Union[int, Int32Array]
    Ratings: Float64Array
    LineType: Union[AnyStr, int, enums.LineType, List[AnyStr], List[int], List[enums.LineType], Int32Array]
    Like: AnyStr

class ILineCode(IDSSObj,LineCodeBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, LineCode, LineCodeBatch)
        LineCodeBatch.__init__(self, self._api_util, sync_cls=True)
        

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> LineCode:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[LineCodeProperties]) -> LineCode:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[LineCodeBatchProperties]) -> LineCodeBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
