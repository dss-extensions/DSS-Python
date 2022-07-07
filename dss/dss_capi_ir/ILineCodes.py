'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira
Copyright (c) 2018-2022 DSS Extensions contributors
'''
from .._cffi_api_util import Iterable

class ILineCodes(Iterable):
    __slots__ = []

    _columns = [
        'Name',
        'idx',
        'Phases',
        'Units',
        'IsZ1Z0',
        'R0',
        'R1',
        'X0',
        'X1',
        'C0',
        'C1',
        'Rmatrix',
        'Xmatrix',
        'Cmatrix',
        'EmergAmps',
        'NormAmps',
    ]

    @property
    def C0(self):
        '''Zero-sequence capacitance, nF per unit length'''
        return self.CheckForError(self._lib.LineCodes_Get_C0())

    @C0.setter
    def C0(self, Value):
        self.CheckForError(self._lib.LineCodes_Set_C0(Value))

    @property
    def C1(self):
        '''Positive-sequence capacitance, nF per unit length'''
        return self.CheckForError(self._lib.LineCodes_Get_C1())

    @C1.setter
    def C1(self, Value):
        self.CheckForError(self._lib.LineCodes_Set_C1(Value))

    @property
    def Cmatrix(self):
        '''Capacitance matrix, nF per unit length'''
        return self._get_float64_array(self._lib.LineCodes_Get_Cmatrix)

    @Cmatrix.setter
    def Cmatrix(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.LineCodes_Set_Cmatrix(ValuePtr, ValueCount))

    @property
    def EmergAmps(self):
        '''Emergency ampere rating'''
        return self.CheckForError(self._lib.LineCodes_Get_EmergAmps())

    @EmergAmps.setter
    def EmergAmps(self, Value):
        self.CheckForError(self._lib.LineCodes_Set_EmergAmps(Value))

    @property
    def IsZ1Z0(self):
        '''(read-only) Flag denoting whether impedance data were entered in symmetrical components'''
        return self.CheckForError(self._lib.LineCodes_Get_IsZ1Z0()) != 0

    @property
    def NormAmps(self):
        '''Normal Ampere rating'''
        return self.CheckForError(self._lib.LineCodes_Get_NormAmps())

    @NormAmps.setter
    def NormAmps(self, Value):
        self.CheckForError(self._lib.LineCodes_Set_NormAmps(Value))

    @property
    def Phases(self):
        '''Number of Phases'''
        return self.CheckForError(self._lib.LineCodes_Get_Phases())

    @Phases.setter
    def Phases(self, Value):
        self.CheckForError(self._lib.LineCodes_Set_Phases(Value))

    @property
    def R0(self):
        '''Zero-Sequence Resistance, ohms per unit length'''
        return self.CheckForError(self._lib.LineCodes_Get_R0())

    @R0.setter
    def R0(self, Value):
        self.CheckForError(self._lib.LineCodes_Set_R0(Value))

    @property
    def R1(self):
        '''Positive-sequence resistance ohms per unit length'''
        return self.CheckForError(self._lib.LineCodes_Get_R1())

    @R1.setter
    def R1(self, Value):
        self.CheckForError(self._lib.LineCodes_Set_R1(Value))

    @property
    def Rmatrix(self):
        '''Resistance matrix, ohms per unit length'''
        return self._get_float64_array(self._lib.LineCodes_Get_Rmatrix)

    @Rmatrix.setter
    def Rmatrix(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.LineCodes_Set_Rmatrix(ValuePtr, ValueCount))

    @property
    def Units(self):
        return self.CheckForError(self._lib.LineCodes_Get_Units()) # TODO: use enum

    @Units.setter
    def Units(self, Value):
        self.CheckForError(self._lib.LineCodes_Set_Units(Value))

    @property
    def X0(self):
        '''Zero Sequence Reactance, Ohms per unit length'''
        return self.CheckForError(self._lib.LineCodes_Get_X0())

    @X0.setter
    def X0(self, Value):
        self.CheckForError(self._lib.LineCodes_Set_X0(Value))

    @property
    def X1(self):
        '''Posiive-sequence reactance, ohms per unit length'''
        return self.CheckForError(self._lib.LineCodes_Get_X1())

    @X1.setter
    def X1(self, Value):
        self.CheckForError(self._lib.LineCodes_Set_X1(Value))

    @property
    def Xmatrix(self):
        '''Reactance matrix, ohms per unit length'''
        return self._get_float64_array(self._lib.LineCodes_Get_Xmatrix)

    @Xmatrix.setter
    def Xmatrix(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.LineCodes_Set_Xmatrix(ValuePtr, ValueCount))
