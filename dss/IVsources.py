# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Iterable

class IVsources(Iterable):
    __slots__ = []
    _is_circuit_element = True

    _columns = [
        'Name',
        'idx',
        'Phases',
        'BasekV',
        'AngleDeg',
        'Frequency',
        'pu',
    ]

    @property
    def AngleDeg(self) -> float:
        '''
        Phase angle of first phase in degrees

        Original COM help: https://opendss.epri.com/AngleDeg1.html
        '''
        return self._check_for_error(self._lib.Vsources_Get_AngleDeg())

    @AngleDeg.setter
    def AngleDeg(self, Value: float):
        self._check_for_error(self._lib.Vsources_Set_AngleDeg(Value))

    @property
    def BasekV(self) -> float:
        '''
        Source voltage in kV

        Original COM help: https://opendss.epri.com/BasekV.html
        '''
        return self._check_for_error(self._lib.Vsources_Get_BasekV())

    @BasekV.setter
    def BasekV(self, Value: float):
        self._check_for_error(self._lib.Vsources_Set_BasekV(Value))

    @property
    def Frequency(self) -> float:
        '''
        Source frequency in Hz

        Original COM help: https://opendss.epri.com/Frequency2.html
        '''
        return self._check_for_error(self._lib.Vsources_Get_Frequency())

    @Frequency.setter
    def Frequency(self, Value: float):
        self._check_for_error(self._lib.Vsources_Set_Frequency(Value))

    @property
    def Phases(self) -> int:
        '''
        Number of phases

        Original COM help: https://opendss.epri.com/Phases3.html
        '''
        return self._check_for_error(self._lib.Vsources_Get_Phases())

    @Phases.setter
    def Phases(self, Value: int):
        self._check_for_error(self._lib.Vsources_Set_Phases(Value))

    @property
    def pu(self) -> float:
        '''
        Per-unit value of source voltage

        Original COM help: https://opendss.epri.com/pu.html
        '''
        return self._check_for_error(self._lib.Vsources_Get_pu())

    @pu.setter
    def pu(self, Value: float):
        self._check_for_error(self._lib.Vsources_Set_pu(Value))
