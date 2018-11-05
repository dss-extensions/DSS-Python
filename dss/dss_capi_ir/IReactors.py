'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class IReactors(Base):
    '''Experimental API extension exposing Reactor objects'''

    __slots__ = []

    @property
    def AllNames(self):
        '''(read-only) Array of strings with names of all devices'''
        return self._get_string_array(self._lib.Reactors_Get_AllNames)

    @property
    def Conductors(self):
        '''(read-only) Array of strings with names of all conductors in the active Reactor object'''
        return self._get_string_array(self._lib.Reactors_Get_Conductors)

    @property
    def Count(self):
        '''(read-only) Number of Reactors'''
        return self._lib.Reactors_Get_Count()

    @property
    def First(self):
        return self._lib.Reactors_Get_First()

    @property
    def Next(self):
        return self._lib.Reactors_Get_Next()

    @property
    def Name(self):
        '''Name of active Reactor'''
        return self._get_string(self._lib.Reactors_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Reactors_Set_Name(Value)
        self.CheckForError()

    def __len__(self):
        return self._lib.Reactors_Get_Count()

    def __iter__(self):
        idx = self.First
        while idx != 0:
            yield self
            idx = self.Next

    @property
    def SpecType(self):
        '''
        How the reactor data was provided: 1=kvar, 2=R+jX, 3=R and X matrices, 4=sym components.
        Depending on this value, only some properties are filled or make sense in the context.
        '''
        return self._lib.Reactors_Get_SpecType()

    @property
    def IsDelta(self):
        '''Delta connection or wye?'''
        return self._lib.Reactors_Get_IsDelta() != 0

    @IsDelta.setter
    def IsDelta(self, Value):
        self._lib.Reactors_Set_IsDelta(Value)
        self.CheckForError()

    @property
    def Parallel(self):
        '''Indicates whether Rmatrix and Xmatrix are to be considered in parallel.'''
        return self._lib.Reactors_Get_Parallel() != 0

    @Parallel.setter
    def Parallel(self, Value):
        self._lib.Reactors_Set_Parallel(Value)
        self.CheckForError()

    @property
    def LmH(self):
        '''Inductance, mH. Alternate way to define the reactance, X, property.'''
        return self._lib.Reactors_Get_LmH()

    @LmH.setter
    def LmH(self, Value):
        self._lib.Reactors_Set_LmH(Value)
        self.CheckForError()

    @property
    def kV(self):
        '''For 2, 3-phase, kV phase-phase. Otherwise specify actual coil rating.'''
        return self._lib.Reactors_Get_kV()

    @kV.setter
    def kV(self, Value):
        self._lib.Reactors_Set_kV(Value)
        self.CheckForError()

    @property
    def kvar(self):
        '''Total kvar, all phases.  Evenly divided among phases. Only determines X. Specify R separately'''
        return self._lib.Reactors_Get_kvar()

    @kvar.setter
    def kvar(self, Value):
        self._lib.Reactors_Set_kvar(Value)
        self.CheckForError()

    @property
    def Phases(self):
        '''Number of phases.'''
        return self._lib.Reactors_Get_Phases()

    @Phases.setter
    def Phases(self, Value):
        self._lib.Reactors_Set_Phases(Value)
        self.CheckForError()

    @property
    def Bus1(self):
        '''
        Name of first bus.
        Bus2 property will default to this bus, node 0, unless previously specified.
        Only Bus1 need be specified for a Yg shunt reactor.
        '''
        return self._get_string(self._lib.Reactors_Get_Bus1())

    @Bus1.setter
    def Bus1(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Reactors_Set_Bus1(Value)
        self.CheckForError()

    @property
    def Bus2(self):
        '''
        Name of 2nd bus. Defaults to all phases connected to first bus, node 0, (Shunt Wye Connection) except when Bus2 is specifically defined.
        Not necessary to specify for delta (LL) connection
        '''
        return self._get_string(self._lib.Reactors_Get_Bus2())

    @Bus2.setter
    def Bus2(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Reactors_Set_Bus2(Value)
        self.CheckForError()

    @property
    def LCurve(self):
        '''Name of XYCurve object, previously defined, describing per-unit variation of phase inductance, L=X/w, vs. frequency. Applies to reactance specified by X, LmH, Z, or kvar property. L generally decreases somewhat with frequency above the base frequency, approaching a limit at a few kHz.'''
        return self._get_string(self._lib.Reactors_Get_LCurve())

    @LCurve.setter
    def LCurve(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Reactors_Set_LCurve(Value)
        self.CheckForError()

    @property
    def RCurve(self):
        '''Name of XYCurve object, previously defined, describing per-unit variation of phase resistance, R, vs. frequency. Applies to resistance specified by R or Z property. If actual values are not known, R often increases by approximately the square root of frequency.'''
        return self._get_string(self._lib.Reactors_Get_RCurve())

    @RCurve.setter
    def RCurve(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Reactors_Set_RCurve(Value)
        self.CheckForError()

    @property
    def R(self):
        '''Resistance (in series with reactance), each phase, ohms. This property applies to REACTOR specified by either kvar or X. See also help on Z.'''
        return self._lib.Reactors_Get_R()

    @R.setter
    def R(self, Value):
        self._lib.Reactors_Set_R(Value)
        self.CheckForError()

    @property
    def X(self):
        '''Reactance, each phase, ohms at base frequency. See also help on Z and LmH properties.'''
        return self._lib.Reactors_Get_X()

    @X.setter
    def X(self, Value):
        self._lib.Reactors_Set_X(Value)
        self.CheckForError()

    @property
    def Rp(self):
        '''Resistance in parallel with R and X (the entire branch). Assumed infinite if not specified.'''
        return self._lib.Reactors_Get_Rp()

    @Rp.setter
    def Rp(self, Value):
        self._lib.Reactors_Set_Rp(Value)
        self.CheckForError()

    @property
    def Rmatrix(self):
        '''Resistance matrix, ohms at base frequency. Order of the matrix is the number of phases. Mutually exclusive to specifying parameters by kvar or X.'''
        return self._get_float64_array(self._lib.Reactors_Get_Rmatrix)

    @Rmatrix.setter
    def Rmatrix(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.Reactors_Set_Rmatrix(ValuePtr, ValueCount)
        self.CheckForError()

    @property
    def Xmatrix(self):
        '''Reactance matrix, ohms at base frequency. Order of the matrix is the number of phases. Mutually exclusive to specifying parameters by kvar or X.'''
        return self._get_float64_array(self._lib.Reactors_Get_Xmatrix)

    @Xmatrix.setter
    def Xmatrix(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.Reactors_Set_Xmatrix(ValuePtr, ValueCount)
        self.CheckForError()

    @property
    def Z(self):
        '''Alternative way of defining R and X properties. Enter a 2-element array representing R +jX in ohms.'''
        return self._get_float64_array(self._lib.Reactors_Get_Z)

    @Z.setter
    def Z(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.Reactors_Set_Z(ValuePtr, ValueCount)
        self.CheckForError()

    @property
    def Z1(self):
        '''
        Positive-sequence impedance, ohms, as a 2-element array representing a complex number.

        If defined, Z1, Z2, and Z0 are used to define the impedance matrix of the REACTOR.

        Z1 MUST BE DEFINED TO USE THIS OPTION FOR DEFINING THE MATRIX.

        Side Effect: Sets Z2 and Z0 to same values unless they were previously defined.
        '''
        return self._get_float64_array(self._lib.Reactors_Get_Z1)

    @Z1.setter
    def Z1(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.Reactors_Set_Z1(ValuePtr, ValueCount)
        self.CheckForError()

    @property
    def Z2(self):
        '''
        Negative-sequence impedance, ohms, as a 2-element array representing a complex number.

        Used to define the impedance matrix of the REACTOR if Z1 is also specified.

        Note: Z2 defaults to Z1 if it is not specifically defined. If Z2 is not equal to Z1, the impedance matrix is asymmetrical.
        '''
        return self._get_float64_array(self._lib.Reactors_Get_Z2)

    @Z2.setter
    def Z2(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.Reactors_Set_Z2(ValuePtr, ValueCount)
        self.CheckForError()

    @property
    def Z0(self):
        '''
        Zero-sequence impedance, ohms, as a 2-element array representing a complex number.

        Used to define the impedance matrix of the REACTOR if Z1 is also specified.

        Note: Z0 defaults to Z1 if it is not specifically defined.
        '''
        return self._get_float64_array(self._lib.Reactors_Get_Z0)

    @Z0.setter
    def Z0(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.Reactors_Set_Z0(ValuePtr, ValueCount)
        self.CheckForError()

