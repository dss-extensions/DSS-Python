'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira
Copyright (c) 2018-2022 DSS Extensions contributors
'''
from .._cffi_api_util import Iterable

class IReactors(Iterable):
    '''Experimental API extension exposing Reactor objects'''
    
    __slots__ = []

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
    def SpecType(self):
        '''
        How the reactor data was provided: 1=kvar, 2=R+jX, 3=R and X matrices, 4=sym components.
        Depending on this value, only some properties are filled or make sense in the context.
        '''
        return self.CheckForError(self._lib.Reactors_Get_SpecType()) #TODO: use enum

    @property
    def IsDelta(self):
        '''Delta connection or wye?'''
        return self.CheckForError(self._lib.Reactors_Get_IsDelta()) != 0

    @IsDelta.setter
    def IsDelta(self, Value):
        self.CheckForError(self._lib.Reactors_Set_IsDelta(Value))

    @property
    def Parallel(self):
        '''Indicates whether Rmatrix and Xmatrix are to be considered in parallel.'''
        return self.CheckForError(self._lib.Reactors_Get_Parallel()) != 0

    @Parallel.setter
    def Parallel(self, Value):
        self.CheckForError(self._lib.Reactors_Set_Parallel(Value))

    @property
    def LmH(self):
        '''Inductance, mH. Alternate way to define the reactance, X, property.'''
        return self.CheckForError(self._lib.Reactors_Get_LmH())

    @LmH.setter
    def LmH(self, Value):
        self.CheckForError(self._lib.Reactors_Set_LmH(Value))

    @property
    def kV(self):
        '''For 2, 3-phase, kV phase-phase. Otherwise specify actual coil rating.'''
        return self.CheckForError(self._lib.Reactors_Get_kV())

    @kV.setter
    def kV(self, Value):
        self.CheckForError(self._lib.Reactors_Set_kV(Value))

    @property
    def kvar(self):
        '''Total kvar, all phases.  Evenly divided among phases. Only determines X. Specify R separately'''
        return self.CheckForError(self._lib.Reactors_Get_kvar())

    @kvar.setter
    def kvar(self, Value):
        self.CheckForError(self._lib.Reactors_Set_kvar(Value))

    @property
    def Phases(self):
        '''Number of phases.'''
        return self.CheckForError(self._lib.Reactors_Get_Phases())

    @Phases.setter
    def Phases(self, Value):
        self.CheckForError(self._lib.Reactors_Set_Phases(Value))

    @property
    def Bus1(self):
        '''
        Name of first bus.
        Bus2 property will default to this bus, node 0, unless previously specified.
        Only Bus1 need be specified for a Yg shunt reactor.
        '''
        return self._get_string(self.CheckForError(self._lib.Reactors_Get_Bus1()))

    @Bus1.setter
    def Bus1(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Reactors_Set_Bus1(Value))

    @property
    def Bus2(self):
        '''
        Name of 2nd bus. Defaults to all phases connected to first bus, node 0, (Shunt Wye Connection) except when Bus2 is specifically defined.
        Not necessary to specify for delta (LL) connection
        '''
        return self._get_string(self.CheckForError(self._lib.Reactors_Get_Bus2()))

    @Bus2.setter
    def Bus2(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Reactors_Set_Bus2(Value))

    @property
    def LCurve(self):
        '''Name of XYCurve object, previously defined, describing per-unit variation of phase inductance, L=X/w, vs. frequency. Applies to reactance specified by X, LmH, Z, or kvar property. L generally decreases somewhat with frequency above the base frequency, approaching a limit at a few kHz.'''
        return self._get_string(self.CheckForError(self._lib.Reactors_Get_LCurve()))

    @LCurve.setter
    def LCurve(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Reactors_Set_LCurve(Value))

    @property
    def RCurve(self):
        '''Name of XYCurve object, previously defined, describing per-unit variation of phase resistance, R, vs. frequency. Applies to resistance specified by R or Z property. If actual values are not known, R often increases by approximately the square root of frequency.'''
        return self._get_string(self.CheckForError(self._lib.Reactors_Get_RCurve()))

    @RCurve.setter
    def RCurve(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Reactors_Set_RCurve(Value))

    @property
    def R(self):
        '''Resistance (in series with reactance), each phase, ohms. This property applies to REACTOR specified by either kvar or X. See also help on Z.'''
        return self.CheckForError(self._lib.Reactors_Get_R())

    @R.setter
    def R(self, Value):
        self.CheckForError(self._lib.Reactors_Set_R(Value))

    @property
    def X(self):
        '''Reactance, each phase, ohms at base frequency. See also help on Z and LmH properties.'''
        return self.CheckForError(self._lib.Reactors_Get_X())

    @X.setter
    def X(self, Value):
        self.CheckForError(self._lib.Reactors_Set_X(Value))

    @property
    def Rp(self):
        '''Resistance in parallel with R and X (the entire branch). Assumed infinite if not specified.'''
        return self.CheckForError(self._lib.Reactors_Get_Rp())

    @Rp.setter
    def Rp(self, Value):
        self.CheckForError(self._lib.Reactors_Set_Rp(Value))

    @property
    def Rmatrix(self):
        '''Resistance matrix, ohms at base frequency. Order of the matrix is the number of phases. Mutually exclusive to specifying parameters by kvar or X.'''
        self.CheckForError(self._lib.Reactors_Get_Rmatrix_GR())
        return self._get_float64_gr_array()

    @Rmatrix.setter
    def Rmatrix(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Reactors_Set_Rmatrix(ValuePtr, ValueCount))

    @property
    def Xmatrix(self):
        '''Reactance matrix, ohms at base frequency. Order of the matrix is the number of phases. Mutually exclusive to specifying parameters by kvar or X.'''
        self.CheckForError(self._lib.Reactors_Get_Xmatrix_GR())
        return self._get_float64_gr_array()

    @Xmatrix.setter
    def Xmatrix(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Reactors_Set_Xmatrix(ValuePtr, ValueCount))

    @property
    def Z(self):
        '''Alternative way of defining R and X properties. Enter a 2-element array representing R +jX in ohms.'''
        self.CheckForError(self._lib.Reactors_Get_Z_GR())
        return self._get_float64_gr_array()

    @Z.setter
    def Z(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Reactors_Set_Z(ValuePtr, ValueCount))

    @property
    def Z1(self):
        '''
        Positive-sequence impedance, ohms, as a 2-element array representing a complex number.

        If defined, Z1, Z2, and Z0 are used to define the impedance matrix of the REACTOR.

        Z1 MUST BE DEFINED TO USE THIS OPTION FOR DEFINING THE MATRIX.

        Side Effect: Sets Z2 and Z0 to same values unless they were previously defined.
        '''
        self.CheckForError(self._lib.Reactors_Get_Z1_GR())
        return self._get_float64_gr_array()

    @Z1.setter
    def Z1(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Reactors_Set_Z1(ValuePtr, ValueCount))

    @property
    def Z2(self):
        '''
        Negative-sequence impedance, ohms, as a 2-element array representing a complex number.

        Used to define the impedance matrix of the REACTOR if Z1 is also specified.

        Note: Z2 defaults to Z1 if it is not specifically defined. If Z2 is not equal to Z1, the impedance matrix is asymmetrical.
        '''
        self.CheckForError(self._lib.Reactors_Get_Z2_GR())
        return self._get_float64_gr_array()

    @Z2.setter
    def Z2(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Reactors_Set_Z2(ValuePtr, ValueCount))

    @property
    def Z0(self):
        '''
        Zero-sequence impedance, ohms, as a 2-element array representing a complex number.

        Used to define the impedance matrix of the REACTOR if Z1 is also specified.

        Note: Z0 defaults to Z1 if it is not specifically defined.
        '''
        self.CheckForError(self._lib.Reactors_Get_Z0_GR())
        return self._get_float64_gr_array()

    @Z0.setter
    def Z0(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Reactors_Set_Z0(ValuePtr, ValueCount))

