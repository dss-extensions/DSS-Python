# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Iterable
from ._types import Float64Array, Float64ArrayOrComplexArray
from typing import AnyStr, Union
from .enums import LineUnits

class ILines(Iterable):
    __slots__ = []
    _is_circuit_element = True

    _columns = [
        'Name',
        'idx',
        'Phases',
        'Bus1',
        'Bus2',
        'LineCode',
        'Geometry',
        'Length',
        'IsSwitch',
        'Spacing',
        'EmergAmps', 
        'NormAmps',
        'SeasonRating',
        'Yprim',
        'NumCust',
        'TotalCust',
        'Rho',
        'R0',
        'R1',
        'X0',
        'X1',
        'Rg', 
        'Xg',
        'C0',
        'C1',
        'Rmatrix',
        'Xmatrix',
        'Cmatrix',
        'Units', 
    ]

    def New(self, Name):
        if not isinstance(Name, bytes):
            Name = Name.encode(self._api_util.codec)

        return self._check_for_error(self._lib.Lines_New(Name))

    @property
    def Bus1(self) -> str:
        '''
        Name of bus for terminal 1.

        Original COM help: https://opendss.epri.com/Bus1.html
        '''
        return self._get_string(self._check_for_error(self._lib.Lines_Get_Bus1()))

    @Bus1.setter
    def Bus1(self, Value):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Lines_Set_Bus1(Value))

    @property
    def Bus2(self) -> str:
        '''
        Name of bus for terminal 2.

        Original COM help: https://opendss.epri.com/Bus2.html
        '''
        return self._get_string(self._check_for_error(self._lib.Lines_Get_Bus2()))

    @Bus2.setter
    def Bus2(self, Value):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Lines_Set_Bus2(Value))

    @property
    def C0(self) -> float:
        '''
        Zero Sequence capacitance, nanofarads per unit length.

        Original COM help: https://opendss.epri.com/C0.html
        '''
        return self._check_for_error(self._lib.Lines_Get_C0())

    @C0.setter
    def C0(self, Value: float):
        self._check_for_error(self._lib.Lines_Set_C0(Value))

    @property
    def C1(self) -> float:
        '''
        Positive Sequence capacitance, nanofarads per unit length.

        Original COM help: https://opendss.epri.com/C1.html
        '''
        return self._check_for_error(self._lib.Lines_Get_C1())

    @C1.setter
    def C1(self, Value: float):
        self._check_for_error(self._lib.Lines_Set_C1(Value))

    @property
    def Cmatrix(self) -> Float64Array:
        self._check_for_error(self._lib.Lines_Get_Cmatrix_GR())
        return self._get_float64_gr_array()

    @Cmatrix.setter
    def Cmatrix(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.Lines_Set_Cmatrix(ValuePtr, ValueCount))

    @property
    def EmergAmps(self) -> float:
        '''
        Emergency (maximum) ampere rating of Line.

        Original COM help: https://opendss.epri.com/EmergAmps1.html
        '''
        return self._check_for_error(self._lib.Lines_Get_EmergAmps())

    @EmergAmps.setter
    def EmergAmps(self, Value: float):
        self._check_for_error(self._lib.Lines_Set_EmergAmps(Value))

    @property
    def Geometry(self) -> str:
        '''
        Line geometry code

        Original COM help: https://opendss.epri.com/Geometry.html
        '''
        return self._get_string(self._check_for_error(self._lib.Lines_Get_Geometry()))

    @Geometry.setter
    def Geometry(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Lines_Set_Geometry(Value))

    @property
    def Length(self) -> float:
        '''
        Length of line section in units compatible with the LineCode definition.

        Original COM help: https://opendss.epri.com/Length.html
        '''
        return self._check_for_error(self._lib.Lines_Get_Length())

    @Length.setter
    def Length(self, Value: float):
        self._check_for_error(self._lib.Lines_Set_Length(Value))

    @property
    def LineCode(self) -> str:
        '''
        Name of LineCode object that defines the impedances.

        Original COM help: https://opendss.epri.com/LineCode.html
        '''
        return self._get_string(self._check_for_error(self._lib.Lines_Get_LineCode()))

    @LineCode.setter
    def LineCode(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Lines_Set_LineCode(Value))

    @property
    def NormAmps(self) -> float:
        '''
        Normal ampere rating of Line.

        Original COM help: https://opendss.epri.com/NormAmps.html
        '''
        return self._check_for_error(self._lib.Lines_Get_NormAmps())

    @NormAmps.setter
    def NormAmps(self, Value: float):
        self._check_for_error(self._lib.Lines_Set_NormAmps(Value))

    @property
    def NumCust(self) -> int:
        '''
        Number of customers on this line section.

        Original COM help: https://opendss.epri.com/NumCust.html
        '''
        return self._check_for_error(self._lib.Lines_Get_NumCust())

    @property
    def Parent(self) -> int:
        '''
        Sets Parent of the active Line to be the active line. Returns 0 if no parent or action fails.

        Original COM help: https://opendss.epri.com/Parent.html
        '''
        return self._check_for_error(self._lib.Lines_Get_Parent())

    @property
    def Phases(self) -> int:
        '''
        Number of Phases, this Line element.

        Original COM help: https://opendss.epri.com/Phases1.html
        '''
        return self._check_for_error(self._lib.Lines_Get_Phases())

    @Phases.setter
    def Phases(self, Value: int):
        self._check_for_error(self._lib.Lines_Set_Phases(Value))

    @property
    def R0(self) -> float:
        '''
        Zero Sequence resistance, ohms per unit length.

        Original COM help: https://opendss.epri.com/R0.html
        '''
        return self._check_for_error(self._lib.Lines_Get_R0())

    @R0.setter
    def R0(self, Value: float):
        self._check_for_error(self._lib.Lines_Set_R0(Value))

    @property
    def R1(self) -> float:
        '''
        Positive Sequence resistance, ohms per unit length.

        Original COM help: https://opendss.epri.com/R1.html
        '''
        return self._check_for_error(self._lib.Lines_Get_R1())

    @R1.setter
    def R1(self, Value: float):
        self._check_for_error(self._lib.Lines_Set_R1(Value))

    @property
    def Rg(self) -> float:
        '''
        Earth return resistance value used to compute line impedances at power frequency

        Original COM help: https://opendss.epri.com/Rg.html
        '''
        return self._check_for_error(self._lib.Lines_Get_Rg())

    @Rg.setter
    def Rg(self, Value: float):
        self._check_for_error(self._lib.Lines_Set_Rg(Value))

    @property
    def Rho(self) -> float:
        '''
        Earth Resistivity, m-ohms

        Original COM help: https://opendss.epri.com/Rho.html
        '''
        return self._check_for_error(self._lib.Lines_Get_Rho())

    @Rho.setter
    def Rho(self, Value: float):
        self._check_for_error(self._lib.Lines_Set_Rho(Value))

    @property
    def Rmatrix(self) -> Float64Array:
        '''
        Resistance matrix (full), ohms per unit length. Array of doubles.

        Original COM help: https://opendss.epri.com/Rmatrix.html
        '''
        self._check_for_error(self._lib.Lines_Get_Rmatrix_GR())
        return self._get_float64_gr_array()

    @Rmatrix.setter
    def Rmatrix(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.Lines_Set_Rmatrix(ValuePtr, ValueCount))

    @property
    def Spacing(self) -> str:
        '''
        Line spacing code

        Original COM help: https://opendss.epri.com/Spacing.html
        '''
        return self._get_string(self._check_for_error(self._lib.Lines_Get_Spacing()))

    @Spacing.setter
    def Spacing(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Lines_Set_Spacing(Value))

    @property
    def TotalCust(self) -> int:
        '''
        Total Number of customers served from this line section.

        Original COM help: https://opendss.epri.com/TotalCust.html
        '''
        return self._check_for_error(self._lib.Lines_Get_TotalCust())

    @property
    def Units(self) -> LineUnits:
        return LineUnits(self._check_for_error(self._lib.Lines_Get_Units()))

    @Units.setter
    def Units(self, Value: Union[int, LineUnits]):
        self._check_for_error(self._lib.Lines_Set_Units(Value))

    @property
    def X0(self) -> float:
        '''
        Zero Sequence reactance ohms per unit length.

        Original COM help: https://opendss.epri.com/X0.html
        '''
        return self._check_for_error(self._lib.Lines_Get_X0())

    @X0.setter
    def X0(self, Value: float):
        self._check_for_error(self._lib.Lines_Set_X0(Value))

    @property
    def X1(self) -> float:
        '''
        Positive Sequence reactance, ohms per unit length.

        Original COM help: https://opendss.epri.com/X1.html
        '''
        return self._check_for_error(self._lib.Lines_Get_X1())

    @X1.setter
    def X1(self, Value: float):
        self._check_for_error(self._lib.Lines_Set_X1(Value))

    @property
    def Xg(self) -> float:
        '''
        Earth return reactance value used to compute line impedances at power frequency

        Original COM help: https://opendss.epri.com/Xg.html
        '''
        return self._check_for_error(self._lib.Lines_Get_Xg())

    @Xg.setter
    def Xg(self, Value: float):
        self._check_for_error(self._lib.Lines_Set_Xg(Value))

    @property
    def Xmatrix(self) -> Float64Array:
        '''
        Reactance matrix (full), ohms per unit length. Array of doubles.

        Original COM help: https://opendss.epri.com/Xmatrix.html
        '''
        self._check_for_error(self._lib.Lines_Get_Xmatrix_GR())
        return self._get_float64_gr_array()

    @Xmatrix.setter
    def Xmatrix(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.Lines_Set_Xmatrix(ValuePtr, ValueCount))

    @property
    def Yprim(self) -> Float64ArrayOrComplexArray:
        '''
        Yprimitive for the active line object (complex array).

        Original COM help: https://opendss.epri.com/Yprim1.html
        '''
        self._check_for_error(self._lib.Lines_Get_Yprim_GR())
        return self._get_complex128_gr_array()

    @Yprim.setter
    def Yprim(self, Value: Float64ArrayOrComplexArray):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.Lines_Set_Yprim(ValuePtr, ValueCount))

    @property
    def SeasonRating(self) -> float:
        '''
        Delivers the rating for the current season (in Amps)  if the "SeasonalRatings" option is active

        Original COM help: https://opendss.epri.com/SeasonRating.html
        '''
        return self._check_for_error(self._lib.Lines_Get_SeasonRating())

    @property
    def IsSwitch(self) -> bool:
        '''
        Sets/gets the Line element switch status. Setting it has side-effects to the line parameters.

        **(API Extension)**
        '''
        return self._check_for_error(self._lib.Lines_Get_IsSwitch()) != 0
        
    @IsSwitch.setter
    def IsSwitch(self, Value: bool):
        self._check_for_error(self._lib.Lines_Set_IsSwitch(Value))

