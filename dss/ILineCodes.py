'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2023 Paulo Meira

Copyright (c) 2018-2023 DSS-Extensions contributors
'''
from ._cffi_api_util import Iterable
from ._types import Float64Array
from typing import Union
from .enums import LineUnits

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
    def Cmatrix(self) -> Float64Array:
        '''Capacitance matrix, nF per unit length'''
        self.CheckForError(self._lib.LineCodes_Get_Cmatrix_GR())
        return self._get_float64_gr_array()

    @Cmatrix.setter
    def Cmatrix(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.LineCodes_Set_Cmatrix(ValuePtr, ValueCount))

    @property
    def EmergAmps(self) -> float:
        '''Emergency ampere rating'''
        return self.CheckForError(self._lib.LineCodes_Get_EmergAmps())

    @EmergAmps.setter
    def EmergAmps(self, Value: float):
        self.CheckForError(self._lib.LineCodes_Set_EmergAmps(Value))

    @property
    def IsZ1Z0(self) -> bool:
        '''Flag denoting whether impedance data were entered in symmetrical components'''
        return self.CheckForError(self._lib.LineCodes_Get_IsZ1Z0()) != 0

    @property
    def NormAmps(self) -> float:
        '''Normal Ampere rating'''
        return self.CheckForError(self._lib.LineCodes_Get_NormAmps())

    @NormAmps.setter
    def NormAmps(self, Value: float):
        self.CheckForError(self._lib.LineCodes_Set_NormAmps(Value))

    @property
    def Phases(self) -> int:
        '''Number of Phases'''
        return self.CheckForError(self._lib.LineCodes_Get_Phases())

    @Phases.setter
    def Phases(self, Value: int):
        self.CheckForError(self._lib.LineCodes_Set_Phases(Value))

    @property
    def R0(self) -> float:
        '''Zero-Sequence Resistance, ohms per unit length'''
        return self.CheckForError(self._lib.LineCodes_Get_R0())

    @R0.setter
    def R0(self, Value: float):
        self.CheckForError(self._lib.LineCodes_Set_R0(Value))

    @property
    def R1(self) -> float:
        '''Positive-sequence resistance ohms per unit length'''
        return self.CheckForError(self._lib.LineCodes_Get_R1())

    @R1.setter
    def R1(self, Value: float):
        self.CheckForError(self._lib.LineCodes_Set_R1(Value))

    @property
    def Rmatrix(self) -> Float64Array:
        '''Resistance matrix, ohms per unit length'''
        self.CheckForError(self._lib.LineCodes_Get_Rmatrix_GR())
        return self._get_float64_gr_array()

    @Rmatrix.setter
    def Rmatrix(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.LineCodes_Set_Rmatrix(ValuePtr, ValueCount))

    @property
    def Units(self) -> LineUnits:
        return LineUnits(self.CheckForError(self._lib.LineCodes_Get_Units()))

    @Units.setter
    def Units(self, Value: Union[int, LineUnits]):
        self.CheckForError(self._lib.LineCodes_Set_Units(Value))

    @property
    def X0(self) -> float:
        '''Zero Sequence Reactance, Ohms per unit length'''
        return self.CheckForError(self._lib.LineCodes_Get_X0())

    @X0.setter
    def X0(self, Value: float):
        self.CheckForError(self._lib.LineCodes_Set_X0(Value))

    @property
    def X1(self) -> float:
        '''Posiive-sequence reactance, ohms per unit length'''
        return self.CheckForError(self._lib.LineCodes_Get_X1())

    @X1.setter
    def X1(self, Value: float):
        self.CheckForError(self._lib.LineCodes_Set_X1(Value))

    @property
    def Xmatrix(self) -> Float64Array:
        '''Reactance matrix, ohms per unit length'''
        self.CheckForError(self._lib.LineCodes_Get_Xmatrix_GR())
        return self._get_float64_gr_array()

    @Xmatrix.setter
    def Xmatrix(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.LineCodes_Set_Xmatrix(ValuePtr, ValueCount))
