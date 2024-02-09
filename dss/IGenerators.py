# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Iterable
from typing import List, AnyStr, Union
from ._types import Float64Array
from .enums import GeneratorStatus

class IGenerators(Iterable):
    __slots__ = []
    _is_circuit_element = True

    _columns = [
        'Name',
        'idx',
        'ForcedON',
        'Model',
        'Phases',
        'PF',
        'kVArated',
        'kV',
        'kW',
        'kvar',
        'Vminpu',
        'Vmaxpu',
        'RegisterNames',
        'RegisterValues',
        'Bus1',
        'Class',
        'kva',
        'IsDelta',
        'Status',
        'daily',
        'duty',
        'Yearly',
    ]

    @property
    def ForcedON(self) -> bool:
        '''
        Indicates whether the generator is forced ON regardless of other dispatch criteria.

        Original COM help: https://opendss.epri.com/ForcedON.html
        '''
        return self._check_for_error(self._lib.Generators_Get_ForcedON()) != 0

    @ForcedON.setter
    def ForcedON(self, Value: bool):
        self._check_for_error(self._lib.Generators_Set_ForcedON(Value))

    @property
    def Model(self) -> int:
        '''
        Generator Model

        Original COM help: https://opendss.epri.com/Model.html
        '''
        return self._check_for_error(self._lib.Generators_Get_Model()) #TODO: use enum

    @Model.setter
    def Model(self, Value: int):
        self._check_for_error(self._lib.Generators_Set_Model(Value))

    @property
    def PF(self) -> float:
        '''
        Power factor (pos. = producing vars). Updates kvar based on present kW value.

        Original COM help: https://opendss.epri.com/PF.html
        '''
        return self._check_for_error(self._lib.Generators_Get_PF())

    @PF.setter
    def PF(self, Value: float):
        self._check_for_error(self._lib.Generators_Set_PF(Value))

    @property
    def Phases(self) -> int:
        '''
        Number of phases

        Original COM help: https://opendss.epri.com/Phases.html
        '''
        return self._check_for_error(self._lib.Generators_Get_Phases())

    @Phases.setter
    def Phases(self, Value: int):
        self._check_for_error(self._lib.Generators_Set_Phases(Value))

    @property
    def RegisterNames(self) -> List[str]:
        '''
        Array of Names of all generator energy meter registers
        
        See also the enum `GeneratorRegisters`.
        '''
        return self._check_for_error(self._get_string_array(self._lib.Generators_Get_RegisterNames))

    @property
    def RegisterValues(self) -> Float64Array:
        '''
        Array of values in generator energy meter registers.

        Original COM help: https://opendss.epri.com/RegisterValues.html
        '''
        self._check_for_error(self._lib.Generators_Get_RegisterValues_GR())
        return self._get_float64_gr_array()

    @property
    def Vmaxpu(self) -> float:
        '''
        Vmaxpu for generator model

        Original COM help: https://opendss.epri.com/Vmaxpu.html
        '''
        return self._check_for_error(self._lib.Generators_Get_Vmaxpu())

    @Vmaxpu.setter
    def Vmaxpu(self, Value: float):
        self._check_for_error(self._lib.Generators_Set_Vmaxpu(Value))

    @property
    def Vminpu(self) -> float:
        '''
        Vminpu for Generator model

        Original COM help: https://opendss.epri.com/Vminpu.html
        '''
        return self._check_for_error(self._lib.Generators_Get_Vminpu())

    @Vminpu.setter
    def Vminpu(self, Value: float):
        self._check_for_error(self._lib.Generators_Set_Vminpu(Value))

    @property
    def kV(self) -> float:
        '''
        Voltage base for the active generator, kV

        Original COM help: https://opendss.epri.com/kV1.html
        '''
        return self._check_for_error(self._lib.Generators_Get_kV())

    @kV.setter
    def kV(self, Value: float):
        self._check_for_error(self._lib.Generators_Set_kV(Value))

    @property
    def kVArated(self) -> float:
        '''
        kVA rating of the generator

        Original COM help: https://opendss.epri.com/kVArated.html
        '''
        return self._check_for_error(self._lib.Generators_Get_kVArated())

    @kVArated.setter
    def kVArated(self, Value: float):
        self._check_for_error(self._lib.Generators_Set_kVArated(Value))

    @property
    def kW(self) -> float:
        '''
        kW output for the active generator. kvar is updated for current power factor.

        Original COM help: https://opendss.epri.com/kW.html
        '''
        return self._check_for_error(self._lib.Generators_Get_kW())

    @kW.setter
    def kW(self, Value: float):
        self._check_for_error(self._lib.Generators_Set_kW(Value))

    @property
    def kvar(self) -> float:
        '''
        kvar output for the active generator. Updates power factor based on present kW value.

        Original COM help: https://opendss.epri.com/kvar.html
        '''
        return self._check_for_error(self._lib.Generators_Get_kvar())

    @kvar.setter
    def kvar(self, Value: float):
        self._check_for_error(self._lib.Generators_Set_kvar(Value))

    @property
    def daily(self) -> str:
        '''
        Name of the loadshape for a daily generation profile.

        **(API Extension)**
        '''
        return self._get_string(self._check_for_error(self._lib.Generators_Get_daily()))

    @daily.setter
    def daily(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Generators_Set_daily(Value))

    @property
    def duty(self) -> str:
        '''
        Name of the loadshape for a duty cycle simulation.

        **(API Extension)**
        '''
        return self._get_string(self._check_for_error(self._lib.Generators_Get_duty()))

    @duty.setter
    def duty(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Generators_Set_duty(Value))

    @property
    def Yearly(self) -> str:
        '''
        Name of yearly loadshape

        **(API Extension)**
        '''
        return self._get_string(self._check_for_error(self._lib.Generators_Get_Yearly()))

    @Yearly.setter
    def Yearly(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Generators_Set_Yearly(Value))

    @property
    def Status(self) -> GeneratorStatus:
        '''
        Response to dispatch multipliers: Fixed=1 (dispatch multipliers do not apply), Variable=0 (follows curves).

        Related enumeration: GeneratorStatus

        **(API Extension)**
        '''
        return GeneratorStatus(self._check_for_error(self._lib.Generators_Get_Status()))

    @Status.setter
    def Status(self, Value: Union[int, GeneratorStatus]):
        self._check_for_error(self._lib.Generators_Set_Status(Value))

    @property
    def IsDelta(self) -> bool:
        '''
        Generator connection. True/1 if delta connection, False/0 if wye.

        **(API Extension)**
        '''
        return self._check_for_error(self._lib.Generators_Get_IsDelta()) != 0

    @IsDelta.setter
    def IsDelta(self, Value: bool):
        self._check_for_error(self._lib.Generators_Set_IsDelta(Value))

    @property
    def kva(self) -> float:
        '''
        kVA rating of electrical machine. Applied to machine or inverter definition for Dynamics mode solutions.

        **(API Extension)**
        '''
        return self._check_for_error(self._lib.Generators_Get_kva())

    @kva.setter
    def kva(self, Value: float):
        self._check_for_error(self._lib.Generators_Set_kva(Value))

    @property
    def Class(self) -> int:
        '''
        An arbitrary integer number representing the class of Generator so that Generator values may be segregated by class.

        **(API Extension)**
        '''
        return self._check_for_error(self._lib.Generators_Get_Class_())

    @Class.setter
    def Class(self, Value: int):
        self._check_for_error(self._lib.Generators_Set_Class_(Value))

    @property
    def Bus1(self) -> str:
        '''
        Bus to which the Generator is connected. May include specific node specification.

        **(API Extension)**
        '''
        return self._get_string(self._check_for_error(self._lib.Generators_Get_Bus1()))

    @Bus1.setter
    def Bus1(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Generators_Set_Bus1(Value))

