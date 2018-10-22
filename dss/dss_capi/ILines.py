'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class ILines(Base):
    __slots__ = []

    def New(self, Name):
        if type(Name) is not bytes:
            Name = Name.encode(self.api_util.codec)

        return self.lib.Lines_New(Name)

    @property
    def AllNames(self):
        '''(read-only) Names of all Line Objects'''
        return self.get_string_array(self.lib.Lines_Get_AllNames)

    @property
    def Bus1(self):
        '''Name of bus for terminal 1.'''
        return self.get_string(self.lib.Lines_Get_Bus1())

    @Bus1.setter
    def Bus1(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.Lines_Set_Bus1(Value)

    @property
    def Bus2(self):
        '''Name of bus for terminal 2.'''
        return self.get_string(self.lib.Lines_Get_Bus2())

    @Bus2.setter
    def Bus2(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.Lines_Set_Bus2(Value)

    @property
    def C0(self):
        '''Zero Sequence capacitance, nanofarads per unit length.'''
        return self.lib.Lines_Get_C0()

    @C0.setter
    def C0(self, Value):
        self.lib.Lines_Set_C0(Value)

    @property
    def C1(self):
        '''Positive Sequence capacitance, nanofarads per unit length.'''
        return self.lib.Lines_Get_C1()

    @C1.setter
    def C1(self, Value):
        self.lib.Lines_Set_C1(Value)

    @property
    def Cmatrix(self):
        self.lib.Lines_Get_Cmatrix_GR()
        return self.get_float64_gr_array()

    @Cmatrix.setter
    def Cmatrix(self, Value):
        Value, ValuePtr, ValueCount = self.prepare_float64_array(Value)
        self.lib.Lines_Set_Cmatrix(ValuePtr, ValueCount)

    @property
    def Count(self):
        '''(read-only) Number of Line objects in Active Circuit.'''
        return self.lib.Lines_Get_Count()

    def __len__(self):
        return self.lib.Lines_Get_Count()

    @property
    def EmergAmps(self):
        '''Emergency (maximum) ampere rating of Line.'''
        return self.lib.Lines_Get_EmergAmps()

    @EmergAmps.setter
    def EmergAmps(self, Value):
        self.lib.Lines_Set_EmergAmps(Value)

    @property
    def First(self):
        '''(read-only) Invoking this property sets the first element active.  Returns 0 if no lines.  Otherwise, index of the line element.'''
        return self.lib.Lines_Get_First()

    @property
    def Geometry(self):
        '''Line geometry code'''
        return self.get_string(self.lib.Lines_Get_Geometry())

    @Geometry.setter
    def Geometry(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.Lines_Set_Geometry(Value)

    @property
    def Length(self):
        '''Length of line section in units compatible with the LineCode definition.'''
        return self.lib.Lines_Get_Length()

    @Length.setter
    def Length(self, Value):
        self.lib.Lines_Set_Length(Value)

    @property
    def LineCode(self):
        '''Name of LineCode object that defines the impedances.'''
        return self.get_string(self.lib.Lines_Get_LineCode())

    @LineCode.setter
    def LineCode(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.Lines_Set_LineCode(Value)

    @property
    def Name(self):
        '''Specify the name of the Line element to set it active.'''
        return self.get_string(self.lib.Lines_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.Lines_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Invoking this property advances to the next Line element active.  Returns 0 if no more lines.  Otherwise, index of the line element.'''
        return self.lib.Lines_Get_Next()

    @property
    def NormAmps(self):
        '''Normal ampere rating of Line.'''
        return self.lib.Lines_Get_NormAmps()

    @NormAmps.setter
    def NormAmps(self, Value):
        self.lib.Lines_Set_NormAmps(Value)

    @property
    def NumCust(self):
        '''(read-only) Number of customers on this line section.'''
        return self.lib.Lines_Get_NumCust()

    @property
    def Parent(self):
        '''(read-only) Sets Parent of the active Line to be the active line. Returns 0 if no parent or action fails.'''
        return self.lib.Lines_Get_Parent()

    @property
    def Phases(self):
        '''Number of Phases, this Line element.'''
        return self.lib.Lines_Get_Phases()

    @Phases.setter
    def Phases(self, Value):
        self.lib.Lines_Set_Phases(Value)

    @property
    def R0(self):
        '''Zero Sequence resistance, ohms per unit length.'''
        return self.lib.Lines_Get_R0()

    @R0.setter
    def R0(self, Value):
        self.lib.Lines_Set_R0(Value)

    @property
    def R1(self):
        '''Positive Sequence resistance, ohms per unit length.'''
        return self.lib.Lines_Get_R1()

    @R1.setter
    def R1(self, Value):
        self.lib.Lines_Set_R1(Value)

    @property
    def Rg(self):
        '''Earth return resistance value used to compute line impedances at power frequency'''
        return self.lib.Lines_Get_Rg()

    @Rg.setter
    def Rg(self, Value):
        self.lib.Lines_Set_Rg(Value)

    @property
    def Rho(self):
        '''Earth Resistivity, m-ohms'''
        return self.lib.Lines_Get_Rho()

    @Rho.setter
    def Rho(self, Value):
        self.lib.Lines_Set_Rho(Value)

    @property
    def Rmatrix(self):
        '''Resistance matrix (full), ohms per unit length. Array of doubles.'''
        self.lib.Lines_Get_Rmatrix_GR()
        return self.get_float64_gr_array()

    @Rmatrix.setter
    def Rmatrix(self, Value):
        Value, ValuePtr, ValueCount = self.prepare_float64_array(Value)
        self.lib.Lines_Set_Rmatrix(ValuePtr, ValueCount)

    @property
    def Spacing(self):
        '''Line spacing code'''
        return self.get_string(self.lib.Lines_Get_Spacing())

    @Spacing.setter
    def Spacing(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.Lines_Set_Spacing(Value)

    @property
    def TotalCust(self):
        '''(read-only) Total Number of customers served from this line section.'''
        return self.lib.Lines_Get_TotalCust()

    @property
    def Units(self):
        return self.lib.Lines_Get_Units()

    @Units.setter
    def Units(self, Value):
        self.lib.Lines_Set_Units(Value)

    @property
    def X0(self):
        '''Zero Sequence reactance ohms per unit length.'''
        return self.lib.Lines_Get_X0()

    @X0.setter
    def X0(self, Value):
        self.lib.Lines_Set_X0(Value)

    @property
    def X1(self):
        '''Positive Sequence reactance, ohms per unit length.'''
        return self.lib.Lines_Get_X1()

    @X1.setter
    def X1(self, Value):
        self.lib.Lines_Set_X1(Value)

    @property
    def Xg(self):
        '''Earth return reactance value used to compute line impedances at power frequency'''
        return self.lib.Lines_Get_Xg()

    @Xg.setter
    def Xg(self, Value):
        self.lib.Lines_Set_Xg(Value)

    @property
    def Xmatrix(self):
        self.lib.Lines_Get_Xmatrix_GR()
        return self.get_float64_gr_array()

    @Xmatrix.setter
    def Xmatrix(self, Value):
        Value, ValuePtr, ValueCount = self.prepare_float64_array(Value)
        self.lib.Lines_Set_Xmatrix(ValuePtr, ValueCount)

    @property
    def Yprim(self):
        '''Yprimitive: Does Nothing at present on Put; Dangerous'''
        self.lib.Lines_Get_Yprim_GR()
        return self.get_float64_gr_array()

    @Yprim.setter
    def Yprim(self, Value):
        Value, ValuePtr, ValueCount = self.prepare_float64_array(Value)
        self.lib.Lines_Set_Yprim(ValuePtr, ValueCount)

    def __iter__(self):
        idx = self.First
        while idx != 0:
            yield self
            idx = self.Next

