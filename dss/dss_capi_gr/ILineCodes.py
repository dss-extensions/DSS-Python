'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class ILineCodes(Base):
    __slots__ = []

    @property
    def AllNames(self):
        '''(read-only) Array of strings with names of all devices'''
        return self._get_string_array(self._lib.LineCodes_Get_AllNames)

    @property
    def C0(self):
        '''Zero-sequence capacitance, nF per unit length'''
        return self._lib.LineCodes_Get_C0()

    @C0.setter
    def C0(self, Value):
        self._lib.LineCodes_Set_C0(Value)
        self.CheckForError()

    @property
    def C1(self):
        '''Positive-sequence capacitance, nF per unit length'''
        return self._lib.LineCodes_Get_C1()

    @C1.setter
    def C1(self, Value):
        self._lib.LineCodes_Set_C1(Value)
        self.CheckForError()

    @property
    def Cmatrix(self):
        '''Capacitance matrix, nF per unit length'''
        self._lib.LineCodes_Get_Cmatrix_GR()
        return self._get_float64_gr_array()

    @Cmatrix.setter
    def Cmatrix(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.LineCodes_Set_Cmatrix(ValuePtr, ValueCount)
        self.CheckForError()

    @property
    def Count(self):
        '''(read-only) Number of LineCodes'''
        return self._lib.LineCodes_Get_Count()

    def __len__(self):
        return self._lib.LineCodes_Get_Count()

    @property
    def EmergAmps(self):
        '''Emergency ampere rating'''
        return self._lib.LineCodes_Get_EmergAmps()

    @EmergAmps.setter
    def EmergAmps(self, Value):
        self._lib.LineCodes_Set_EmergAmps(Value)
        self.CheckForError()

    @property
    def First(self):
        return self._lib.LineCodes_Get_First()

    @property
    def IsZ1Z0(self):
        '''(read-only) Flag denoting whether impedance data were entered in symmetrical components'''
        return self._lib.LineCodes_Get_IsZ1Z0() != 0

    @property
    def Name(self):
        '''Name of active LineCode'''
        return self._get_string(self._lib.LineCodes_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.LineCodes_Set_Name(Value)
        self.CheckForError()

    @property
    def Next(self):
        return self._lib.LineCodes_Get_Next()

    @property
    def NormAmps(self):
        '''Normal Ampere rating'''
        return self._lib.LineCodes_Get_NormAmps()

    @NormAmps.setter
    def NormAmps(self, Value):
        self._lib.LineCodes_Set_NormAmps(Value)
        self.CheckForError()

    @property
    def Phases(self):
        '''Number of Phases'''
        return self._lib.LineCodes_Get_Phases()

    @Phases.setter
    def Phases(self, Value):
        self._lib.LineCodes_Set_Phases(Value)
        self.CheckForError()

    @property
    def R0(self):
        '''Zero-Sequence Resistance, ohms per unit length'''
        return self._lib.LineCodes_Get_R0()

    @R0.setter
    def R0(self, Value):
        self._lib.LineCodes_Set_R0(Value)
        self.CheckForError()

    @property
    def R1(self):
        '''Positive-sequence resistance ohms per unit length'''
        return self._lib.LineCodes_Get_R1()

    @R1.setter
    def R1(self, Value):
        self._lib.LineCodes_Set_R1(Value)
        self.CheckForError()

    @property
    def Rmatrix(self):
        '''Resistance matrix, ohms per unit length'''
        self._lib.LineCodes_Get_Rmatrix_GR()
        return self._get_float64_gr_array()

    @Rmatrix.setter
    def Rmatrix(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.LineCodes_Set_Rmatrix(ValuePtr, ValueCount)
        self.CheckForError()

    @property
    def Units(self):
        return self._lib.LineCodes_Get_Units()

    @Units.setter
    def Units(self, Value):
        self._lib.LineCodes_Set_Units(Value)
        self.CheckForError()

    @property
    def X0(self):
        '''Zero Sequence Reactance, Ohms per unit length'''
        return self._lib.LineCodes_Get_X0()

    @X0.setter
    def X0(self, Value):
        self._lib.LineCodes_Set_X0(Value)
        self.CheckForError()

    @property
    def X1(self):
        '''Posiive-sequence reactance, ohms per unit length'''
        return self._lib.LineCodes_Get_X1()

    @X1.setter
    def X1(self, Value):
        self._lib.LineCodes_Set_X1(Value)
        self.CheckForError()

    @property
    def Xmatrix(self):
        '''Reactance matrix, ohms per unit length'''
        self._lib.LineCodes_Get_Xmatrix_GR()
        return self._get_float64_gr_array()

    @Xmatrix.setter
    def Xmatrix(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.LineCodes_Set_Xmatrix(ValuePtr, ValueCount)
        self.CheckForError()

    def __iter__(self):
        idx = self.First
        while idx != 0:
            yield self
            idx = self.Next


