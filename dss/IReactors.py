# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from typing import AnyStr
from ._types import Float64Array, Float64ArrayOrSimpleComplex
from ._cffi_api_util import Iterable

class IReactors(Iterable):
    '''
    Reactor objects
    
    (API Extension)
    '''
    
    __slots__ = []
    _is_circuit_element = True

    _columns = [
        'Name',
        'idx',
        'Phases',
        'Bus1',
        'Bus2',
        'SpecType',
        'kV',
        'kvar',
        'IsDelta',
        'Parallel',
        'LCurve',
        'RCurve',
        'R',
        'Rp',
        'X',
        'Z0',
        'Z1',
        'Z2',
        'Z',
        'Rmatrix',
        'Xmatrix',
    ]

    @property
    def SpecType(self) -> int:
        '''
        How the reactor data was provided: 1=kvar, 2=R+jX, 3=R and X matrices, 4=sym components.
        Depending on this value, only some properties are filled or make sense in the context.
        '''
        return self._check_for_error(self._lib.Reactors_Get_SpecType()) #TODO: use enum

    @property
    def IsDelta(self) -> bool:
        '''Delta connection or wye?'''
        return self._check_for_error(self._lib.Reactors_Get_IsDelta()) != 0

    @IsDelta.setter
    def IsDelta(self, Value: bool):
        self._check_for_error(self._lib.Reactors_Set_IsDelta(Value))

    @property
    def Parallel(self) -> bool:
        '''Indicates whether Rmatrix and Xmatrix are to be considered in parallel.'''
        return self._check_for_error(self._lib.Reactors_Get_Parallel()) != 0

    @Parallel.setter
    def Parallel(self, Value: bool):
        self._check_for_error(self._lib.Reactors_Set_Parallel(Value))

    @property
    def LmH(self) -> float:
        '''Inductance, mH. Alternate way to define the reactance, X, property.'''
        return self._check_for_error(self._lib.Reactors_Get_LmH())

    @LmH.setter
    def LmH(self, Value: float):
        self._check_for_error(self._lib.Reactors_Set_LmH(Value))

    @property
    def kV(self) -> float:
        '''For 2, 3-phase, kV phase-phase. Otherwise specify actual coil rating.'''
        return self._check_for_error(self._lib.Reactors_Get_kV())

    @kV.setter
    def kV(self, Value: float):
        self._check_for_error(self._lib.Reactors_Set_kV(Value))

    @property
    def kvar(self) -> float:
        '''Total kvar, all phases.  Evenly divided among phases. Only determines X. Specify R separately'''
        return self._check_for_error(self._lib.Reactors_Get_kvar())

    @kvar.setter
    def kvar(self, Value: float):
        self._check_for_error(self._lib.Reactors_Set_kvar(Value))

    @property
    def Phases(self) -> int:
        '''Number of phases.'''
        return self._check_for_error(self._lib.Reactors_Get_Phases())

    @Phases.setter
    def Phases(self, Value: int):
        self._check_for_error(self._lib.Reactors_Set_Phases(Value))

    @property
    def Bus1(self) -> str:
        '''
        Name of first bus.
        Bus2 property will default to this bus, node 0, unless previously specified.
        Only Bus1 need be specified for a Yg shunt reactor.
        '''
        return self._get_string(self._check_for_error(self._lib.Reactors_Get_Bus1()))

    @Bus1.setter
    def Bus1(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Reactors_Set_Bus1(Value))

    @property
    def Bus2(self) -> str:
        '''
        Name of 2nd bus. Defaults to all phases connected to first bus, node 0, (Shunt Wye Connection) except when Bus2 is specifically defined.
        Not necessary to specify for delta (LL) connection
        '''
        return self._get_string(self._check_for_error(self._lib.Reactors_Get_Bus2()))

    @Bus2.setter
    def Bus2(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Reactors_Set_Bus2(Value))

    @property
    def LCurve(self) -> str:
        '''Name of XYCurve object, previously defined, describing per-unit variation of phase inductance, L=X/w, vs. frequency. Applies to reactance specified by X, LmH, Z, or kvar property. L generally decreases somewhat with frequency above the base frequency, approaching a limit at a few kHz.'''
        return self._get_string(self._check_for_error(self._lib.Reactors_Get_LCurve()))

    @LCurve.setter
    def LCurve(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Reactors_Set_LCurve(Value))

    @property
    def RCurve(self) -> str:
        '''Name of XYCurve object, previously defined, describing per-unit variation of phase resistance, R, vs. frequency. Applies to resistance specified by R or Z property. If actual values are not known, R often increases by approximately the square root of frequency.'''
        return self._get_string(self._check_for_error(self._lib.Reactors_Get_RCurve()))

    @RCurve.setter
    def RCurve(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Reactors_Set_RCurve(Value))

    @property
    def R(self) -> float:
        '''Resistance (in series with reactance), each phase, ohms. This property applies to REACTOR specified by either kvar or X. See also help on Z.'''
        return self._check_for_error(self._lib.Reactors_Get_R())

    @R.setter
    def R(self, Value: float):
        self._check_for_error(self._lib.Reactors_Set_R(Value))

    @property
    def X(self) -> float:
        '''Reactance, each phase, ohms at base frequency. See also help on Z and LmH properties.'''
        return self._check_for_error(self._lib.Reactors_Get_X())

    @X.setter
    def X(self, Value: float):
        self._check_for_error(self._lib.Reactors_Set_X(Value))

    @property
    def Rp(self) -> float:
        '''Resistance in parallel with R and X (the entire branch). Assumed infinite if not specified.'''
        return self._check_for_error(self._lib.Reactors_Get_Rp())

    @Rp.setter
    def Rp(self, Value: float):
        self._check_for_error(self._lib.Reactors_Set_Rp(Value))

    @property
    def Rmatrix(self) -> Float64Array:
        '''Resistance matrix, ohms at base frequency. Order of the matrix is the number of phases. Mutually exclusive to specifying parameters by kvar or X.'''
        self._check_for_error(self._lib.Reactors_Get_Rmatrix_GR())
        return self._get_float64_gr_array()

    @Rmatrix.setter
    def Rmatrix(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.Reactors_Set_Rmatrix(ValuePtr, ValueCount))

    @property
    def Xmatrix(self) -> Float64Array:
        '''Reactance matrix, ohms at base frequency. Order of the matrix is the number of phases. Mutually exclusive to specifying parameters by kvar or X.'''
        self._check_for_error(self._lib.Reactors_Get_Xmatrix_GR())
        return self._get_float64_gr_array()

    @Xmatrix.setter
    def Xmatrix(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.Reactors_Set_Xmatrix(ValuePtr, ValueCount))

    @property
    def Z(self) -> Float64ArrayOrSimpleComplex:
        '''Alternative way of defining R and X properties. Enter a 2-element array representing R +jX in ohms.'''
        self._check_for_error(self._lib.Reactors_Get_Z_GR())
        return self._get_complex128_gr_simple()

    @Z.setter
    def Z(self, Value: Float64ArrayOrSimpleComplex):
        Value, ValuePtr, ValueCount = self._prepare_complex128_simple(Value)
        self._check_for_error(self._lib.Reactors_Set_Z(ValuePtr, ValueCount))

    @property
    def Z1(self) -> Float64ArrayOrSimpleComplex:
        '''
        Positive-sequence impedance, ohms, as a 2-element array representing a complex number.

        If defined, Z1, Z2, and Z0 are used to define the impedance matrix of the REACTOR.

        Z1 MUST BE DEFINED TO USE THIS OPTION FOR DEFINING THE MATRIX.

        Side Effect: Sets Z2 and Z0 to same values unless they were previously defined.
        '''
        self._check_for_error(self._lib.Reactors_Get_Z1_GR())
        return self._get_complex128_gr_simple()

    @Z1.setter
    def Z1(self, Value: Float64ArrayOrSimpleComplex):
        Value, ValuePtr, ValueCount = self._prepare_complex128_simple(Value)
        self._check_for_error(self._lib.Reactors_Set_Z1(ValuePtr, ValueCount))

    @property
    def Z2(self) -> Float64ArrayOrSimpleComplex:
        '''
        Negative-sequence impedance, ohms, as a 2-element array representing a complex number.

        Used to define the impedance matrix of the REACTOR if Z1 is also specified.

        Note: Z2 defaults to Z1 if it is not specifically defined. If Z2 is not equal to Z1, the impedance matrix is asymmetrical.
        '''
        self._check_for_error(self._lib.Reactors_Get_Z2_GR())
        return self._get_complex128_gr_simple()

    @Z2.setter
    def Z2(self, Value: Float64ArrayOrSimpleComplex):
        Value, ValuePtr, ValueCount = self._prepare_complex128_simple(Value)
        self._check_for_error(self._lib.Reactors_Set_Z2(ValuePtr, ValueCount))

    @property
    def Z0(self) -> Float64ArrayOrSimpleComplex:
        '''
        Zero-sequence impedance, ohms, as a 2-element array representing a complex number.

        Used to define the impedance matrix of the REACTOR if Z1 is also specified.

        Note: Z0 defaults to Z1 if it is not specifically defined.
        '''
        self._check_for_error(self._lib.Reactors_Get_Z0_GR())
        return self._get_complex128_gr_simple()

    @Z0.setter
    def Z0(self, Value: Float64ArrayOrSimpleComplex):
        Value, ValuePtr, ValueCount = self._prepare_complex128_simple(Value)
        self._check_for_error(self._lib.Reactors_Set_Z0(ValuePtr, ValueCount))

