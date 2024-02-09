# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Iterable
from ._types import Int32Array

class ICapacitors(Iterable):
    __slots__ = []
    _is_circuit_element = True

    _columns = [
        'Name',
        'idx',
        'kV',
        'NumSteps',
        'AvailableSteps',
        'IsDelta',
        'States',
        'kvar',
    ]

    def AddStep(self) -> bool:
        return self._check_for_error(self._lib.Capacitors_AddStep()) != 0

    def Close(self):
        self._check_for_error(self._lib.Capacitors_Close())

    def Open(self):
        self._check_for_error(self._lib.Capacitors_Open())

    def SubtractStep(self) -> bool:
        return self._check_for_error(self._lib.Capacitors_SubtractStep()) != 0

    @property
    def AvailableSteps(self) -> int:
        '''
        Number of Steps available in cap bank to be switched ON.

        Original COM help: https://opendss.epri.com/AvailableSteps.html
        '''
        return self._check_for_error(self._lib.Capacitors_Get_AvailableSteps())

    @property
    def IsDelta(self) -> bool:
        '''
        Delta connection or wye?

        Original COM help: https://opendss.epri.com/IsDelta.html
        '''
        return self._check_for_error(self._lib.Capacitors_Get_IsDelta()) != 0

    @IsDelta.setter
    def IsDelta(self, Value: bool):
        self._check_for_error(self._lib.Capacitors_Set_IsDelta(Value))

    @property
    def NumSteps(self) -> int:
        '''
        Number of steps (default 1) for distributing and switching the total bank kVAR.

        Original COM help: https://opendss.epri.com/NumSteps.html
        '''
        return self._check_for_error(self._lib.Capacitors_Get_NumSteps())

    @NumSteps.setter
    def NumSteps(self, Value: int):
        self._check_for_error(self._lib.Capacitors_Set_NumSteps(Value))

    @property
    def States(self) -> Int32Array:
        '''
        An array of integers [0..NumSteps-1] indicating state of each step. If the read value is -1 an error has occurred.

        Original COM help: https://opendss.epri.com/States.html
        '''
        self._check_for_error(self._lib.Capacitors_Get_States_GR())
        return self._get_int32_gr_array()

    @States.setter
    def States(self, Value: Int32Array):
        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)
        self._check_for_error(self._lib.Capacitors_Set_States(ValuePtr, ValueCount))

    @property
    def kV(self) -> float:
        '''
        Bank kV rating. Use LL for 2 or 3 phases, or actual can rating for 1 phase.

        Original COM help: https://opendss.epri.com/kV.html
        '''
        return self._check_for_error(self._lib.Capacitors_Get_kV())

    @kV.setter
    def kV(self, Value):
        self._check_for_error(self._lib.Capacitors_Set_kV(Value))

    @property
    def kvar(self) -> float:
        '''Total bank KVAR, distributed equally among phases and steps.'''
        return self._check_for_error(self._lib.Capacitors_Get_kvar())

    @kvar.setter
    def kvar(self, Value: float):
        self._check_for_error(self._lib.Capacitors_Set_kvar(Value))
