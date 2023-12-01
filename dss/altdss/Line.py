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
from .LineCode import LineCode as LineCodeObj
from .LineGeometry import LineGeometry
from .LineSpacing import LineSpacing
from .WireData import WireData

class Line(DSSObj, CircuitElementMixin, PDElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots + PDElementMixin._extra_slots
    _cls_name = 'Line'
    _cls_idx = 15
    _cls_prop_idx = {
        'bus1': 1,
        'bus2': 2,
        'linecode': 3,
        'length': 4,
        'phases': 5,
        'r1': 6,
        'x1': 7,
        'r0': 8,
        'x0': 9,
        'c1': 10,
        'c0': 11,
        'rmatrix': 12,
        'xmatrix': 13,
        'cmatrix': 14,
        'switch': 15,
        'rg': 16,
        'xg': 17,
        'rho': 18,
        'geometry': 19,
        'units': 20,
        'spacing': 21,
        'wires': 22,
        'conductors': 22,
        'earthmodel': 23,
        'cncables': 24,
        'tscables': 25,
        'b1': 26,
        'b0': 27,
        'seasons': 28,
        'ratings': 29,
        'linetype': 30,
        'normamps': 31,
        'emergamps': 32,
        'faultrate': 33,
        'pctperm': 34,
        'repair': 35,
        'basefreq': 36,
        'enabled': 37,
        'like': 38,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)
       PDElementMixin.__init__(self)

    def _get_Bus1(self) -> str:
        """
        Name of bus to which first terminal is connected.
        Example:
        bus1=busname   (assumes all terminals connected in normal phase order)
        bus1=busname.3.1.2.0 (specify terminal to node connections explicitly)

        DSS property name: `Bus1`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    def _set_Bus1(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(1, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: str

    def _get_Bus2(self) -> str:
        """
        Name of bus to which 2nd terminal is connected.

        DSS property name: `Bus2`, DSS property index: 2.
        """
        return self._get_prop_string(2)

    def _set_Bus2(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(2, value, flags)

    Bus2 = property(_get_Bus2, _set_Bus2) # type: str

    def _get_LineCode_str(self) -> str:
        """
        Name of linecode object describing line impedances.
        If you use a line code, you do not need to specify the impedances here. The line code must have been PREVIOUSLY defined. The values specified last will prevail over those specified earlier (left-to-right sequence of properties).  You can subsequently change the number of phases if symmetrical component quantities are specified.If no line code or impedance data are specified, the line object defaults to 336 MCM ACSR on 4 ft spacing.

        DSS property name: `LineCode`, DSS property index: 3.
        """
        return self._get_prop_string(3)

    def _set_LineCode_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(3, value, flags)

    LineCode_str = property(_get_LineCode_str, _set_LineCode_str) # type: str

    def _get_LineCode(self) -> LineCodeObj:
        """
        Name of linecode object describing line impedances.
        If you use a line code, you do not need to specify the impedances here. The line code must have been PREVIOUSLY defined. The values specified last will prevail over those specified earlier (left-to-right sequence of properties).  You can subsequently change the number of phases if symmetrical component quantities are specified.If no line code or impedance data are specified, the line object defaults to 336 MCM ACSR on 4 ft spacing.

        DSS property name: `LineCode`, DSS property index: 3.
        """
        return self._get_obj(3, LineCodeObj)

    def _set_LineCode(self, value: Union[AnyStr, LineCodeObj], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(3, value, flags)
            return

        self._set_string_o(3, value, flags)

    LineCode = property(_get_LineCode, _set_LineCode) # type: LineCodeObj

    def _get_Length(self) -> float:
        """
        Length of line. Default is 1.0. If units do not match the impedance data, specify "units" property. 

        DSS property name: `Length`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    def _set_Length(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 4, value, flags)

    Length = property(_get_Length, _set_Length) # type: float

    def _get_Phases(self) -> int:
        """
        Number of phases, this line.

        DSS property name: `Phases`, DSS property index: 5.
        """
        return self._lib.Obj_GetInt32(self._ptr, 5)

    def _set_Phases(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 5, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: int

    def _get_R1(self) -> float:
        """
        Positive-sequence Resistance, ohms per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition. See also Rmatrix.

        DSS property name: `R1`, DSS property index: 6.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    def _set_R1(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 6, value, flags)

    R1 = property(_get_R1, _set_R1) # type: float

    def _get_X1(self) -> float:
        """
        Positive-sequence Reactance, ohms per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.  See also Xmatrix

        DSS property name: `X1`, DSS property index: 7.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    def _set_X1(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 7, value, flags)

    X1 = property(_get_X1, _set_X1) # type: float

    def _get_R0(self) -> float:
        """
        Zero-sequence Resistance, ohms per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.

        DSS property name: `R0`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    def _set_R0(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 8, value, flags)

    R0 = property(_get_R0, _set_R0) # type: float

    def _get_X0(self) -> float:
        """
        Zero-sequence Reactance, ohms per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.

        DSS property name: `X0`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    def _set_X0(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 9, value, flags)

    X0 = property(_get_X0, _set_X0) # type: float

    def _get_C1(self) -> float:
        """
        Positive-sequence capacitance, nf per unit length.  Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition. See also Cmatrix and B1.

        DSS property name: `C1`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    def _set_C1(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 10, value, flags)

    C1 = property(_get_C1, _set_C1) # type: float

    def _get_C0(self) -> float:
        """
        Zero-sequence capacitance, nf per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.See also B0.

        DSS property name: `C0`, DSS property index: 11.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    def _set_C0(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 11, value, flags)

    C0 = property(_get_C0, _set_C0) # type: float

    def _get_RMatrix(self) -> Float64Array:
        """
        Resistance matrix, lower triangle, ohms per unit length. Order of the matrix is the number of phases. May be used to specify the impedance of any line configuration. Using any of Rmatrix, Xmatrix, Cmatrix forces program to use the matrix values for line impedance definition. For balanced line models, you may use the standard symmetrical component data definition instead.

        DSS property name: `RMatrix`, DSS property index: 12.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 12)

    def _set_RMatrix(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(12, value, flags)

    RMatrix = property(_get_RMatrix, _set_RMatrix) # type: Float64Array

    def _get_XMatrix(self) -> Float64Array:
        """
        Reactance matrix, lower triangle, ohms per unit length. Order of the matrix is the number of phases. May be used to specify the impedance of any line configuration. Using any of Rmatrix, Xmatrix, Cmatrix forces program to use the matrix values for line impedance definition.  For balanced line models, you may use the standard symmetrical component data definition instead.

        DSS property name: `XMatrix`, DSS property index: 13.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 13)

    def _set_XMatrix(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(13, value, flags)

    XMatrix = property(_get_XMatrix, _set_XMatrix) # type: Float64Array

    def _get_CMatrix(self) -> Float64Array:
        """
        Nodal Capacitance matrix, lower triangle, nf per unit length.Order of the matrix is the number of phases. May be used to specify the shunt capacitance of any line configuration. Using any of Rmatrix, Xmatrix, Cmatrix forces program to use the matrix values for line impedance definition.  For balanced line models, you may use the standard symmetrical component data definition instead.

        DSS property name: `CMatrix`, DSS property index: 14.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 14)

    def _set_CMatrix(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(14, value, flags)

    CMatrix = property(_get_CMatrix, _set_CMatrix) # type: Float64Array

    def _get_Switch(self) -> bool:
        """
        {y/n | T/F}  Default= no/false.  Designates this line as a switch for graphics and algorithmic purposes. 
        SIDE EFFECT: Sets r1 = 1.0; x1 = 1.0; r0 = 1.0; x0 = 1.0; c1 = 1.1 ; c0 = 1.0;  length = 0.001; You must reset if you want something different.

        DSS property name: `Switch`, DSS property index: 15.
        """
        return self._lib.Obj_GetInt32(self._ptr, 15) != 0

    def _set_Switch(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 15, value, flags)

    Switch = property(_get_Switch, _set_Switch) # type: bool

    def _get_Rg(self) -> float:
        """
        Carson earth return resistance per unit length used to compute impedance values at base frequency. Default is 0.01805 = 60 Hz value in ohms per kft (matches default line impedances). This value is required for harmonic solutions if you wish to adjust the earth return impedances for frequency. If not, set both Rg and Xg = 0.

        DSS property name: `Rg`, DSS property index: 16.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    def _set_Rg(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 16, value, flags)

    Rg = property(_get_Rg, _set_Rg) # type: float

    def _get_Xg(self) -> float:
        """
        Carson earth return reactance per unit length used to compute impedance values at base frequency.  For making better frequency adjustments. Default is 0.155081 = 60 Hz value in ohms per kft (matches default line impedances). This value is required for harmonic solutions if you wish to adjust the earth return impedances for frequency. If not, set both Rg and Xg = 0.

        DSS property name: `Xg`, DSS property index: 17.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    def _set_Xg(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 17, value, flags)

    Xg = property(_get_Xg, _set_Xg) # type: float

    def _get_rho(self) -> float:
        """
        Default=100 meter ohms.  Earth resistivity used to compute earth correction factor. Overrides Line geometry definition if specified.

        DSS property name: `rho`, DSS property index: 18.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    def _set_rho(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 18, value, flags)

    rho = property(_get_rho, _set_rho) # type: float

    def _get_Geometry_str(self) -> str:
        """
        Geometry code for LineGeometry Object. Supersedes any previous definition of line impedance. Line constants are computed for each frequency change or rho change. CAUTION: may alter number of phases. You cannot subsequently change the number of phases unless you change how the line impedance is defined.

        DSS property name: `Geometry`, DSS property index: 19.
        """
        return self._get_prop_string(19)

    def _set_Geometry_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(19, value, flags)

    Geometry_str = property(_get_Geometry_str, _set_Geometry_str) # type: str

    def _get_Geometry(self) -> LineGeometry:
        """
        Geometry code for LineGeometry Object. Supersedes any previous definition of line impedance. Line constants are computed for each frequency change or rho change. CAUTION: may alter number of phases. You cannot subsequently change the number of phases unless you change how the line impedance is defined.

        DSS property name: `Geometry`, DSS property index: 19.
        """
        return self._get_obj(19, LineGeometry)

    def _set_Geometry(self, value: Union[AnyStr, LineGeometry], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(19, value, flags)
            return

        self._set_string_o(19, value, flags)

    Geometry = property(_get_Geometry, _set_Geometry) # type: LineGeometry

    def _get_Units(self) -> enums.LengthUnit:
        """
        Length Units = {none | mi|kft|km|m|Ft|in|cm } Default is None - assumes length units match impedance units.

        DSS property name: `Units`, DSS property index: 20.
        """
        return enums.LengthUnit(self._lib.Obj_GetInt32(self._ptr, 20))

    def _set_Units(self, value: Union[AnyStr, int, enums.LengthUnit], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(20, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 20, value, flags)

    Units = property(_get_Units, _set_Units) # type: enums.LengthUnit

    def _get_Units_str(self) -> str:
        """
        Length Units = {none | mi|kft|km|m|Ft|in|cm } Default is None - assumes length units match impedance units.

        DSS property name: `Units`, DSS property index: 20.
        """
        return self._get_prop_string(20)

    def _set_Units_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Units(value, flags)

    Units_str = property(_get_Units_str, _set_Units_str) # type: str

    def _get_Spacing_str(self) -> str:
        """
        Reference to a LineSpacing for use in a line constants calculation.
        Must be used in conjunction with the Wires property.
        Specify this before the wires property.

        DSS property name: `Spacing`, DSS property index: 21.
        """
        return self._get_prop_string(21)

    def _set_Spacing_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(21, value, flags)

    Spacing_str = property(_get_Spacing_str, _set_Spacing_str) # type: str

    def _get_Spacing(self) -> LineSpacing:
        """
        Reference to a LineSpacing for use in a line constants calculation.
        Must be used in conjunction with the Wires property.
        Specify this before the wires property.

        DSS property name: `Spacing`, DSS property index: 21.
        """
        return self._get_obj(21, LineSpacing)

    def _set_Spacing(self, value: Union[AnyStr, LineSpacing], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(21, value, flags)
            return

        self._set_string_o(21, value, flags)

    Spacing = property(_get_Spacing, _set_Spacing) # type: LineSpacing

    def _get_Conductors_str(self) -> List[str]:
        """
        Array of WireData names for use in an overhead line constants calculation.
        Must be used in conjunction with the Spacing property.
        Specify the Spacing first, and "ncond" wires.
        May also be used to specify bare neutrals with cables, using "ncond-nphase" wires.

        DSS property name: `Wires`, DSS property index: 22.
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 22)

    def _set_Conductors_str(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        self._set_string_array_o(22, value, flags)

    Conductors_str = property(_get_Conductors_str, _set_Conductors_str) # type: List[str]

    def _get_Conductors(self) -> List[WireData]:
        """
        Array of WireData names for use in an overhead line constants calculation.
        Must be used in conjunction with the Spacing property.
        Specify the Spacing first, and "ncond" wires.
        May also be used to specify bare neutrals with cables, using "ncond-nphase" wires.

        DSS property name: `Wires`, DSS property index: 22.
        """
        return self._get_obj_array(22, WireData)

    def _set_Conductors(self, value: List[Union[AnyStr, WireData]], flags: enums.SetterFlags = 0):
        if value is None or len(value) == 0 or not isinstance(value[0], DSSObj):
            self._set_string_array_o(22, value, flags)
            return

        self._set_obj_array(22, value, flags)

    Conductors = property(_get_Conductors, _set_Conductors) # type: List[WireData]

    def _get_EarthModel(self) -> enums.EarthModel:
        """
        One of {Carson | FullCarson | Deri}. Default is the global value established with the Set EarthModel command. See the Options Help on EarthModel option. This is used to override the global value for this line. This option applies only when the "geometry" property is used.

        DSS property name: `EarthModel`, DSS property index: 23.
        """
        return enums.EarthModel(self._lib.Obj_GetInt32(self._ptr, 23))

    def _set_EarthModel(self, value: Union[AnyStr, int, enums.EarthModel], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(23, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 23, value, flags)

    EarthModel = property(_get_EarthModel, _set_EarthModel) # type: enums.EarthModel

    def _get_EarthModel_str(self) -> str:
        """
        One of {Carson | FullCarson | Deri}. Default is the global value established with the Set EarthModel command. See the Options Help on EarthModel option. This is used to override the global value for this line. This option applies only when the "geometry" property is used.

        DSS property name: `EarthModel`, DSS property index: 23.
        """
        return self._get_prop_string(23)

    def _set_EarthModel_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_EarthModel(value, flags)

    EarthModel_str = property(_get_EarthModel_str, _set_EarthModel_str) # type: str

    def _get_B1(self) -> float:
        """
        Alternate way to specify C1. MicroS per unit length

        DSS property name: `B1`, DSS property index: 26.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 26)

    def _set_B1(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 26, value, flags)

    B1 = property(_get_B1, _set_B1) # type: float

    def _get_B0(self) -> float:
        """
        Alternate way to specify C0. MicroS per unit length

        DSS property name: `B0`, DSS property index: 27.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 27)

    def _set_B0(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 27, value, flags)

    B0 = property(_get_B0, _set_B0) # type: float

    def _get_Seasons(self) -> int:
        """
        Defines the number of ratings to be defined for the wire, to be used only when defining seasonal ratings using the "Ratings" property.

        DSS property name: `Seasons`, DSS property index: 28.
        """
        return self._lib.Obj_GetInt32(self._ptr, 28)

    def _set_Seasons(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 28, value, flags)

    Seasons = property(_get_Seasons, _set_Seasons) # type: int

    def _get_Ratings(self) -> Float64Array:
        """
        An array of ratings to be used when the seasonal ratings flag is True. It can be used to insert
        multiple ratings to change during a QSTS simulation to evaluate different ratings in lines.

        DSS property name: `Ratings`, DSS property index: 29.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 29)

    def _set_Ratings(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(29, value, flags)

    Ratings = property(_get_Ratings, _set_Ratings) # type: Float64Array

    def _get_LineType(self) -> enums.LineType:
        """
        Code designating the type of line. 
        One of: OH, UG, UG_TS, UG_CN, SWT_LDBRK, SWT_FUSE, SWT_SECT, SWT_REC, SWT_DISC, SWT_BRK, SWT_ELBOW, BUSBAR

        OpenDSS currently does not use this internally. For whatever purpose the user defines. Default is OH.

        DSS property name: `LineType`, DSS property index: 30.
        """
        return enums.LineType(self._lib.Obj_GetInt32(self._ptr, 30))

    def _set_LineType(self, value: Union[AnyStr, int, enums.LineType], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(30, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 30, value, flags)

    LineType = property(_get_LineType, _set_LineType) # type: enums.LineType

    def _get_LineType_str(self) -> str:
        """
        Code designating the type of line. 
        One of: OH, UG, UG_TS, UG_CN, SWT_LDBRK, SWT_FUSE, SWT_SECT, SWT_REC, SWT_DISC, SWT_BRK, SWT_ELBOW, BUSBAR

        OpenDSS currently does not use this internally. For whatever purpose the user defines. Default is OH.

        DSS property name: `LineType`, DSS property index: 30.
        """
        return self._get_prop_string(30)

    def _set_LineType_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_LineType(value, flags)

    LineType_str = property(_get_LineType_str, _set_LineType_str) # type: str

    def _get_NormAmps(self) -> float:
        """
        Normal rated current.

        DSS property name: `NormAmps`, DSS property index: 31.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 31)

    def _set_NormAmps(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 31, value, flags)

    NormAmps = property(_get_NormAmps, _set_NormAmps) # type: float

    def _get_EmergAmps(self) -> float:
        """
        Maximum or emerg current.

        DSS property name: `EmergAmps`, DSS property index: 32.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 32)

    def _set_EmergAmps(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 32, value, flags)

    EmergAmps = property(_get_EmergAmps, _set_EmergAmps) # type: float

    def _get_FaultRate(self) -> float:
        """
        Failure rate PER UNIT LENGTH per year. Length must be same units as LENGTH property. Default is 0.1 fault per unit length per year.

        DSS property name: `FaultRate`, DSS property index: 33.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 33)

    def _set_FaultRate(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 33, value, flags)

    FaultRate = property(_get_FaultRate, _set_FaultRate) # type: float

    def _get_pctPerm(self) -> float:
        """
        Percent of failures that become permanent. Default is 20.

        DSS property name: `pctPerm`, DSS property index: 34.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 34)

    def _set_pctPerm(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 34, value, flags)

    pctPerm = property(_get_pctPerm, _set_pctPerm) # type: float

    def _get_Repair(self) -> float:
        """
        Hours to repair. Default is 3 hr.

        DSS property name: `Repair`, DSS property index: 35.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 35)

    def _set_Repair(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 35, value, flags)

    Repair = property(_get_Repair, _set_Repair) # type: float

    def _get_BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 36.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 36)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 36, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float

    def _get_Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 37.
        """
        return self._lib.Obj_GetInt32(self._ptr, 37) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 37, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 38.
        """
        self._set_string_o(38, value)


class LineProperties(TypedDict):
    Bus1: AnyStr
    Bus2: AnyStr
    LineCode: Union[AnyStr, LineCodeObj]
    Length: float
    Phases: int
    R1: float
    X1: float
    R0: float
    X0: float
    C1: float
    C0: float
    RMatrix: Float64Array
    XMatrix: Float64Array
    CMatrix: Float64Array
    Switch: bool
    Rg: float
    Xg: float
    rho: float
    Geometry: Union[AnyStr, LineGeometry]
    Units: Union[AnyStr, int, enums.LengthUnit]
    Spacing: Union[AnyStr, LineSpacing]
    Conductors: List[Union[AnyStr, WireData]]
    EarthModel: Union[AnyStr, int, enums.EarthModel]
    B1: float
    B0: float
    Seasons: int
    Ratings: Float64Array
    LineType: Union[AnyStr, int, enums.LineType]
    NormAmps: float
    EmergAmps: float
    FaultRate: float
    pctPerm: float
    Repair: float
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class LineBatch(DSSBatch, CircuitElementBatchMixin, PDElementBatchMixin):
    _cls_name = 'Line'
    _obj_cls = Line
    _cls_idx = 15

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)
       PDElementBatchMixin.__init__(self)

    def _get_Bus1(self) -> List[str]:
        """
        Name of bus to which first terminal is connected.
        Example:
        bus1=busname   (assumes all terminals connected in normal phase order)
        bus1=busname.3.1.2.0 (specify terminal to node connections explicitly)

        DSS property name: `Bus1`, DSS property index: 1.
        """
        return self._get_batch_str_prop(1)

    def _set_Bus1(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(1, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: List[str]

    def _get_Bus2(self) -> List[str]:
        """
        Name of bus to which 2nd terminal is connected.

        DSS property name: `Bus2`, DSS property index: 2.
        """
        return self._get_batch_str_prop(2)

    def _set_Bus2(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(2, value, flags)

    Bus2 = property(_get_Bus2, _set_Bus2) # type: List[str]

    def _get_LineCode_str(self) -> List[str]:
        """
        Name of linecode object describing line impedances.
        If you use a line code, you do not need to specify the impedances here. The line code must have been PREVIOUSLY defined. The values specified last will prevail over those specified earlier (left-to-right sequence of properties).  You can subsequently change the number of phases if symmetrical component quantities are specified.If no line code or impedance data are specified, the line object defaults to 336 MCM ACSR on 4 ft spacing.

        DSS property name: `LineCode`, DSS property index: 3.
        """
        return self._get_batch_str_prop(3)

    def _set_LineCode_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(3, value, flags)

    LineCode_str = property(_get_LineCode_str, _set_LineCode_str) # type: List[str]

    def _get_LineCode(self) -> List[LineCodeObj]:
        """
        Name of linecode object describing line impedances.
        If you use a line code, you do not need to specify the impedances here. The line code must have been PREVIOUSLY defined. The values specified last will prevail over those specified earlier (left-to-right sequence of properties).  You can subsequently change the number of phases if symmetrical component quantities are specified.If no line code or impedance data are specified, the line object defaults to 336 MCM ACSR on 4 ft spacing.

        DSS property name: `LineCode`, DSS property index: 3.
        """
        return self._get_batch_obj_prop(3)

    def _set_LineCode(self, value: Union[AnyStr, LineCodeObj, List[AnyStr], List[LineCodeObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(3, value, flags)

    LineCode = property(_get_LineCode, _set_LineCode) # type: List[LineCodeObj]

    def _get_Length(self) -> BatchFloat64ArrayProxy:
        """
        Length of line. Default is 1.0. If units do not match the impedance data, specify "units" property. 

        DSS property name: `Length`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    def _set_Length(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(4, value, flags)

    Length = property(_get_Length, _set_Length) # type: BatchFloat64ArrayProxy

    def _get_Phases(self) -> BatchInt32ArrayProxy:
        """
        Number of phases, this line.

        DSS property name: `Phases`, DSS property index: 5.
        """
        return BatchInt32ArrayProxy(self, 5)

    def _set_Phases(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(5, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: BatchInt32ArrayProxy

    def _get_R1(self) -> BatchFloat64ArrayProxy:
        """
        Positive-sequence Resistance, ohms per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition. See also Rmatrix.

        DSS property name: `R1`, DSS property index: 6.
        """
        return BatchFloat64ArrayProxy(self, 6)

    def _set_R1(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(6, value, flags)

    R1 = property(_get_R1, _set_R1) # type: BatchFloat64ArrayProxy

    def _get_X1(self) -> BatchFloat64ArrayProxy:
        """
        Positive-sequence Reactance, ohms per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.  See also Xmatrix

        DSS property name: `X1`, DSS property index: 7.
        """
        return BatchFloat64ArrayProxy(self, 7)

    def _set_X1(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(7, value, flags)

    X1 = property(_get_X1, _set_X1) # type: BatchFloat64ArrayProxy

    def _get_R0(self) -> BatchFloat64ArrayProxy:
        """
        Zero-sequence Resistance, ohms per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.

        DSS property name: `R0`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    def _set_R0(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(8, value, flags)

    R0 = property(_get_R0, _set_R0) # type: BatchFloat64ArrayProxy

    def _get_X0(self) -> BatchFloat64ArrayProxy:
        """
        Zero-sequence Reactance, ohms per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.

        DSS property name: `X0`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    def _set_X0(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(9, value, flags)

    X0 = property(_get_X0, _set_X0) # type: BatchFloat64ArrayProxy

    def _get_C1(self) -> BatchFloat64ArrayProxy:
        """
        Positive-sequence capacitance, nf per unit length.  Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition. See also Cmatrix and B1.

        DSS property name: `C1`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    def _set_C1(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(10, value, flags)

    C1 = property(_get_C1, _set_C1) # type: BatchFloat64ArrayProxy

    def _get_C0(self) -> BatchFloat64ArrayProxy:
        """
        Zero-sequence capacitance, nf per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.See also B0.

        DSS property name: `C0`, DSS property index: 11.
        """
        return BatchFloat64ArrayProxy(self, 11)

    def _set_C0(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(11, value, flags)

    C0 = property(_get_C0, _set_C0) # type: BatchFloat64ArrayProxy

    def _get_RMatrix(self) -> List[Float64Array]:
        """
        Resistance matrix, lower triangle, ohms per unit length. Order of the matrix is the number of phases. May be used to specify the impedance of any line configuration. Using any of Rmatrix, Xmatrix, Cmatrix forces program to use the matrix values for line impedance definition. For balanced line models, you may use the standard symmetrical component data definition instead.

        DSS property name: `RMatrix`, DSS property index: 12.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 12)
            for x in self._unpack()
        ]

    def _set_RMatrix(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(12, value, flags)

    RMatrix = property(_get_RMatrix, _set_RMatrix) # type: List[Float64Array]

    def _get_XMatrix(self) -> List[Float64Array]:
        """
        Reactance matrix, lower triangle, ohms per unit length. Order of the matrix is the number of phases. May be used to specify the impedance of any line configuration. Using any of Rmatrix, Xmatrix, Cmatrix forces program to use the matrix values for line impedance definition.  For balanced line models, you may use the standard symmetrical component data definition instead.

        DSS property name: `XMatrix`, DSS property index: 13.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 13)
            for x in self._unpack()
        ]

    def _set_XMatrix(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(13, value, flags)

    XMatrix = property(_get_XMatrix, _set_XMatrix) # type: List[Float64Array]

    def _get_CMatrix(self) -> List[Float64Array]:
        """
        Nodal Capacitance matrix, lower triangle, nf per unit length.Order of the matrix is the number of phases. May be used to specify the shunt capacitance of any line configuration. Using any of Rmatrix, Xmatrix, Cmatrix forces program to use the matrix values for line impedance definition.  For balanced line models, you may use the standard symmetrical component data definition instead.

        DSS property name: `CMatrix`, DSS property index: 14.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 14)
            for x in self._unpack()
        ]

    def _set_CMatrix(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(14, value, flags)

    CMatrix = property(_get_CMatrix, _set_CMatrix) # type: List[Float64Array]

    def _get_Switch(self) -> List[bool]:
        """
        {y/n | T/F}  Default= no/false.  Designates this line as a switch for graphics and algorithmic purposes. 
        SIDE EFFECT: Sets r1 = 1.0; x1 = 1.0; r0 = 1.0; x0 = 1.0; c1 = 1.1 ; c0 = 1.0;  length = 0.001; You must reset if you want something different.

        DSS property name: `Switch`, DSS property index: 15.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(15)
        ]

    def _set_Switch(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(15, value, flags)

    Switch = property(_get_Switch, _set_Switch) # type: List[bool]

    def _get_Rg(self) -> BatchFloat64ArrayProxy:
        """
        Carson earth return resistance per unit length used to compute impedance values at base frequency. Default is 0.01805 = 60 Hz value in ohms per kft (matches default line impedances). This value is required for harmonic solutions if you wish to adjust the earth return impedances for frequency. If not, set both Rg and Xg = 0.

        DSS property name: `Rg`, DSS property index: 16.
        """
        return BatchFloat64ArrayProxy(self, 16)

    def _set_Rg(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(16, value, flags)

    Rg = property(_get_Rg, _set_Rg) # type: BatchFloat64ArrayProxy

    def _get_Xg(self) -> BatchFloat64ArrayProxy:
        """
        Carson earth return reactance per unit length used to compute impedance values at base frequency.  For making better frequency adjustments. Default is 0.155081 = 60 Hz value in ohms per kft (matches default line impedances). This value is required for harmonic solutions if you wish to adjust the earth return impedances for frequency. If not, set both Rg and Xg = 0.

        DSS property name: `Xg`, DSS property index: 17.
        """
        return BatchFloat64ArrayProxy(self, 17)

    def _set_Xg(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(17, value, flags)

    Xg = property(_get_Xg, _set_Xg) # type: BatchFloat64ArrayProxy

    def _get_rho(self) -> BatchFloat64ArrayProxy:
        """
        Default=100 meter ohms.  Earth resistivity used to compute earth correction factor. Overrides Line geometry definition if specified.

        DSS property name: `rho`, DSS property index: 18.
        """
        return BatchFloat64ArrayProxy(self, 18)

    def _set_rho(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(18, value, flags)

    rho = property(_get_rho, _set_rho) # type: BatchFloat64ArrayProxy

    def _get_Geometry_str(self) -> List[str]:
        """
        Geometry code for LineGeometry Object. Supersedes any previous definition of line impedance. Line constants are computed for each frequency change or rho change. CAUTION: may alter number of phases. You cannot subsequently change the number of phases unless you change how the line impedance is defined.

        DSS property name: `Geometry`, DSS property index: 19.
        """
        return self._get_batch_str_prop(19)

    def _set_Geometry_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(19, value, flags)

    Geometry_str = property(_get_Geometry_str, _set_Geometry_str) # type: List[str]

    def _get_Geometry(self) -> List[LineGeometry]:
        """
        Geometry code for LineGeometry Object. Supersedes any previous definition of line impedance. Line constants are computed for each frequency change or rho change. CAUTION: may alter number of phases. You cannot subsequently change the number of phases unless you change how the line impedance is defined.

        DSS property name: `Geometry`, DSS property index: 19.
        """
        return self._get_batch_obj_prop(19)

    def _set_Geometry(self, value: Union[AnyStr, LineGeometry, List[AnyStr], List[LineGeometry]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(19, value, flags)

    Geometry = property(_get_Geometry, _set_Geometry) # type: List[LineGeometry]

    def _get_Units(self) -> BatchInt32ArrayProxy:
        """
        Length Units = {none | mi|kft|km|m|Ft|in|cm } Default is None - assumes length units match impedance units.

        DSS property name: `Units`, DSS property index: 20.
        """
        return BatchInt32ArrayProxy(self, 20)

    def _set_Units(self, value: Union[AnyStr, int, enums.LengthUnit, List[AnyStr], List[int], List[enums.LengthUnit], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(20, value, flags)
            return

        self._set_batch_int32_array(20, value, flags)

    Units = property(_get_Units, _set_Units) # type: BatchInt32ArrayProxy

    def _get_Units_str(self) -> List[str]:
        """
        Length Units = {none | mi|kft|km|m|Ft|in|cm } Default is None - assumes length units match impedance units.

        DSS property name: `Units`, DSS property index: 20.
        """
        return self._get_batch_str_prop(20)

    def _set_Units_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Units(value, flags)

    Units_str = property(_get_Units_str, _set_Units_str) # type: List[str]

    def _get_Spacing_str(self) -> List[str]:
        """
        Reference to a LineSpacing for use in a line constants calculation.
        Must be used in conjunction with the Wires property.
        Specify this before the wires property.

        DSS property name: `Spacing`, DSS property index: 21.
        """
        return self._get_batch_str_prop(21)

    def _set_Spacing_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(21, value, flags)

    Spacing_str = property(_get_Spacing_str, _set_Spacing_str) # type: List[str]

    def _get_Spacing(self) -> List[LineSpacing]:
        """
        Reference to a LineSpacing for use in a line constants calculation.
        Must be used in conjunction with the Wires property.
        Specify this before the wires property.

        DSS property name: `Spacing`, DSS property index: 21.
        """
        return self._get_batch_obj_prop(21)

    def _set_Spacing(self, value: Union[AnyStr, LineSpacing, List[AnyStr], List[LineSpacing]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(21, value, flags)

    Spacing = property(_get_Spacing, _set_Spacing) # type: List[LineSpacing]

    def _get_Conductors_str(self) -> List[List[str]]:
        """
        Array of WireData names for use in an overhead line constants calculation.
        Must be used in conjunction with the Spacing property.
        Specify the Spacing first, and "ncond" wires.
        May also be used to specify bare neutrals with cables, using "ncond-nphase" wires.

        DSS property name: `Wires`, DSS property index: 22.
        """
        return self._get_string_ll(22)

    def _set_Conductors_str(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        self._set_batch_stringlist_prop(22, value, flags)

    Conductors_str = property(_get_Conductors_str, _set_Conductors_str) # type: List[List[str]]

    def _get_Conductors(self) -> List[List[WireData]]:
        """
        Array of WireData names for use in an overhead line constants calculation.
        Must be used in conjunction with the Spacing property.
        Specify the Spacing first, and "ncond" wires.
        May also be used to specify bare neutrals with cables, using "ncond-nphase" wires.

        DSS property name: `Wires`, DSS property index: 22.
        """
        return self._get_obj_ll(22, WireData)

    def _set_Conductors(self, value: Union[List[AnyStr], List[WireData]], flags: enums.SetterFlags = 0):
        if (not len(value)) or isinstance(value[0], (bytes, str)) or (len(value[0]) and isinstance(value[0][0], (bytes, str))):
            self._set_batch_stringlist_prop(22, value, flags)
            return

        self._set_batch_objlist_prop(22, value, flags)

    Conductors = property(_get_Conductors, _set_Conductors) # type: List[List[WireData]]

    def _get_EarthModel(self) -> BatchInt32ArrayProxy:
        """
        One of {Carson | FullCarson | Deri}. Default is the global value established with the Set EarthModel command. See the Options Help on EarthModel option. This is used to override the global value for this line. This option applies only when the "geometry" property is used.

        DSS property name: `EarthModel`, DSS property index: 23.
        """
        return BatchInt32ArrayProxy(self, 23)

    def _set_EarthModel(self, value: Union[AnyStr, int, enums.EarthModel, List[AnyStr], List[int], List[enums.EarthModel], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(23, value, flags)
            return

        self._set_batch_int32_array(23, value, flags)

    EarthModel = property(_get_EarthModel, _set_EarthModel) # type: BatchInt32ArrayProxy

    def _get_EarthModel_str(self) -> List[str]:
        """
        One of {Carson | FullCarson | Deri}. Default is the global value established with the Set EarthModel command. See the Options Help on EarthModel option. This is used to override the global value for this line. This option applies only when the "geometry" property is used.

        DSS property name: `EarthModel`, DSS property index: 23.
        """
        return self._get_batch_str_prop(23)

    def _set_EarthModel_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_EarthModel(value, flags)

    EarthModel_str = property(_get_EarthModel_str, _set_EarthModel_str) # type: List[str]

    def _get_B1(self) -> BatchFloat64ArrayProxy:
        """
        Alternate way to specify C1. MicroS per unit length

        DSS property name: `B1`, DSS property index: 26.
        """
        return BatchFloat64ArrayProxy(self, 26)

    def _set_B1(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(26, value, flags)

    B1 = property(_get_B1, _set_B1) # type: BatchFloat64ArrayProxy

    def _get_B0(self) -> BatchFloat64ArrayProxy:
        """
        Alternate way to specify C0. MicroS per unit length

        DSS property name: `B0`, DSS property index: 27.
        """
        return BatchFloat64ArrayProxy(self, 27)

    def _set_B0(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(27, value, flags)

    B0 = property(_get_B0, _set_B0) # type: BatchFloat64ArrayProxy

    def _get_Seasons(self) -> BatchInt32ArrayProxy:
        """
        Defines the number of ratings to be defined for the wire, to be used only when defining seasonal ratings using the "Ratings" property.

        DSS property name: `Seasons`, DSS property index: 28.
        """
        return BatchInt32ArrayProxy(self, 28)

    def _set_Seasons(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(28, value, flags)

    Seasons = property(_get_Seasons, _set_Seasons) # type: BatchInt32ArrayProxy

    def _get_Ratings(self) -> List[Float64Array]:
        """
        An array of ratings to be used when the seasonal ratings flag is True. It can be used to insert
        multiple ratings to change during a QSTS simulation to evaluate different ratings in lines.

        DSS property name: `Ratings`, DSS property index: 29.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 29)
            for x in self._unpack()
        ]

    def _set_Ratings(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(29, value, flags)

    Ratings = property(_get_Ratings, _set_Ratings) # type: List[Float64Array]

    def _get_LineType(self) -> BatchInt32ArrayProxy:
        """
        Code designating the type of line. 
        One of: OH, UG, UG_TS, UG_CN, SWT_LDBRK, SWT_FUSE, SWT_SECT, SWT_REC, SWT_DISC, SWT_BRK, SWT_ELBOW, BUSBAR

        OpenDSS currently does not use this internally. For whatever purpose the user defines. Default is OH.

        DSS property name: `LineType`, DSS property index: 30.
        """
        return BatchInt32ArrayProxy(self, 30)

    def _set_LineType(self, value: Union[AnyStr, int, enums.LineType, List[AnyStr], List[int], List[enums.LineType], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(30, value, flags)
            return

        self._set_batch_int32_array(30, value, flags)

    LineType = property(_get_LineType, _set_LineType) # type: BatchInt32ArrayProxy

    def _get_LineType_str(self) -> List[str]:
        """
        Code designating the type of line. 
        One of: OH, UG, UG_TS, UG_CN, SWT_LDBRK, SWT_FUSE, SWT_SECT, SWT_REC, SWT_DISC, SWT_BRK, SWT_ELBOW, BUSBAR

        OpenDSS currently does not use this internally. For whatever purpose the user defines. Default is OH.

        DSS property name: `LineType`, DSS property index: 30.
        """
        return self._get_batch_str_prop(30)

    def _set_LineType_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_LineType(value, flags)

    LineType_str = property(_get_LineType_str, _set_LineType_str) # type: List[str]

    def _get_NormAmps(self) -> BatchFloat64ArrayProxy:
        """
        Normal rated current.

        DSS property name: `NormAmps`, DSS property index: 31.
        """
        return BatchFloat64ArrayProxy(self, 31)

    def _set_NormAmps(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(31, value, flags)

    NormAmps = property(_get_NormAmps, _set_NormAmps) # type: BatchFloat64ArrayProxy

    def _get_EmergAmps(self) -> BatchFloat64ArrayProxy:
        """
        Maximum or emerg current.

        DSS property name: `EmergAmps`, DSS property index: 32.
        """
        return BatchFloat64ArrayProxy(self, 32)

    def _set_EmergAmps(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(32, value, flags)

    EmergAmps = property(_get_EmergAmps, _set_EmergAmps) # type: BatchFloat64ArrayProxy

    def _get_FaultRate(self) -> BatchFloat64ArrayProxy:
        """
        Failure rate PER UNIT LENGTH per year. Length must be same units as LENGTH property. Default is 0.1 fault per unit length per year.

        DSS property name: `FaultRate`, DSS property index: 33.
        """
        return BatchFloat64ArrayProxy(self, 33)

    def _set_FaultRate(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(33, value, flags)

    FaultRate = property(_get_FaultRate, _set_FaultRate) # type: BatchFloat64ArrayProxy

    def _get_pctPerm(self) -> BatchFloat64ArrayProxy:
        """
        Percent of failures that become permanent. Default is 20.

        DSS property name: `pctPerm`, DSS property index: 34.
        """
        return BatchFloat64ArrayProxy(self, 34)

    def _set_pctPerm(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(34, value, flags)

    pctPerm = property(_get_pctPerm, _set_pctPerm) # type: BatchFloat64ArrayProxy

    def _get_Repair(self) -> BatchFloat64ArrayProxy:
        """
        Hours to repair. Default is 3 hr.

        DSS property name: `Repair`, DSS property index: 35.
        """
        return BatchFloat64ArrayProxy(self, 35)

    def _set_Repair(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(35, value, flags)

    Repair = property(_get_Repair, _set_Repair) # type: BatchFloat64ArrayProxy

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 36.
        """
        return BatchFloat64ArrayProxy(self, 36)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(36, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy

    def _get_Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 37.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(37)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(37, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 38.
        """
        self._set_batch_string(38, value, flags)

class LineBatchProperties(TypedDict):
    Bus1: Union[AnyStr, List[AnyStr]]
    Bus2: Union[AnyStr, List[AnyStr]]
    LineCode: Union[AnyStr, LineCodeObj, List[AnyStr], List[LineCodeObj]]
    Length: Union[float, Float64Array]
    Phases: Union[int, Int32Array]
    R1: Union[float, Float64Array]
    X1: Union[float, Float64Array]
    R0: Union[float, Float64Array]
    X0: Union[float, Float64Array]
    C1: Union[float, Float64Array]
    C0: Union[float, Float64Array]
    RMatrix: Float64Array
    XMatrix: Float64Array
    CMatrix: Float64Array
    Switch: bool
    Rg: Union[float, Float64Array]
    Xg: Union[float, Float64Array]
    rho: Union[float, Float64Array]
    Geometry: Union[AnyStr, LineGeometry, List[AnyStr], List[LineGeometry]]
    Units: Union[AnyStr, int, enums.LengthUnit, List[AnyStr], List[int], List[enums.LengthUnit], Int32Array]
    Spacing: Union[AnyStr, LineSpacing, List[AnyStr], List[LineSpacing]]
    Conductors: Union[List[AnyStr], List[WireData]]
    EarthModel: Union[AnyStr, int, enums.EarthModel, List[AnyStr], List[int], List[enums.EarthModel], Int32Array]
    B1: Union[float, Float64Array]
    B0: Union[float, Float64Array]
    Seasons: Union[int, Int32Array]
    Ratings: Float64Array
    LineType: Union[AnyStr, int, enums.LineType, List[AnyStr], List[int], List[enums.LineType], Int32Array]
    NormAmps: Union[float, Float64Array]
    EmergAmps: Union[float, Float64Array]
    FaultRate: Union[float, Float64Array]
    pctPerm: Union[float, Float64Array]
    Repair: Union[float, Float64Array]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class ILine(IDSSObj, LineBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, Line, LineBatch)
        LineBatch.__init__(self, self._api_util, sync_cls_idx=Line._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Line:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[LineProperties]) -> Line:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[LineBatchProperties]) -> LineBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
