# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Iterable
from typing import AnyStr

class IRegControls(Iterable):
    __slots__ = []
    _is_circuit_element = True

    _columns = [
        'Name',
        'idx',
        'Transformer',
        'Winding',
        'MonitoredBus',
        'CTPrimary',
        'PTratio',
        'Delay',
        'IsInverseTime',
        'IsReversible',
        'MaxTapChange',
        'TapDelay',
        'TapNumber',
        'TapWinding',
        'VoltageLimit',
        'ForwardBand',
        'ForwardR',
        'ForwardX',
        'ForwardVreg',
        'ReverseBand',
        'ReverseR',
        'ReverseX',
        'ReverseVreg',
    ]

    def Reset(self):
        self._check_for_error(self._lib.RegControls_Reset())

    @property
    def CTPrimary(self) -> float:
        '''
        CT primary ampere rating (secondary is 0.2 amperes)

        Original COM help: https://opendss.epri.com/CTPrimary.html
        '''
        return self._check_for_error(self._lib.RegControls_Get_CTPrimary())

    @CTPrimary.setter
    def CTPrimary(self, Value: float):
        self._check_for_error(self._lib.RegControls_Set_CTPrimary(Value))

    @property
    def Delay(self) -> float:
        '''
        Time delay [s] after arming before the first tap change. Control may reset before actually changing taps.

        Original COM help: https://opendss.epri.com/Delay2.html
        '''
        return self._check_for_error(self._lib.RegControls_Get_Delay())

    @Delay.setter
    def Delay(self, Value: float):
        self._check_for_error(self._lib.RegControls_Set_Delay(Value))

    @property
    def ForwardBand(self) -> float:
        '''
        Regulation bandwidth in forward direction, centered on Vreg

        Original COM help: https://opendss.epri.com/ForwardBand.html
        '''
        return self._check_for_error(self._lib.RegControls_Get_ForwardBand())

    @ForwardBand.setter
    def ForwardBand(self, Value: float):
        self._check_for_error(self._lib.RegControls_Set_ForwardBand(Value))

    @property
    def ForwardR(self) -> float:
        '''
        LDC R setting in Volts

        Original COM help: https://opendss.epri.com/ForwardR.html
        '''
        return self._check_for_error(self._lib.RegControls_Get_ForwardR())

    @ForwardR.setter
    def ForwardR(self, Value: float):
        self._check_for_error(self._lib.RegControls_Set_ForwardR(Value))

    @property
    def ForwardVreg(self) -> float:
        '''
        Target voltage in the forward direction, on PT secondary base.

        Original COM help: https://opendss.epri.com/ForwardVreg.html
        '''
        return self._check_for_error(self._lib.RegControls_Get_ForwardVreg())

    @ForwardVreg.setter
    def ForwardVreg(self, Value: float):
        self._check_for_error(self._lib.RegControls_Set_ForwardVreg(Value))

    @property
    def ForwardX(self) -> float:
        '''
        LDC X setting in Volts

        Original COM help: https://opendss.epri.com/ForwardX.html
        '''
        return self._check_for_error(self._lib.RegControls_Get_ForwardX())

    @ForwardX.setter
    def ForwardX(self, Value: float):
        self._check_for_error(self._lib.RegControls_Set_ForwardX(Value))

    @property
    def IsInverseTime(self) -> bool:
        '''
        Time delay is inversely adjusted, proportional to the amount of voltage outside the regulating band.

        Original COM help: https://opendss.epri.com/IsInverseTime.html
        '''
        return self._check_for_error(self._lib.RegControls_Get_IsInverseTime()) != 0

    @IsInverseTime.setter
    def IsInverseTime(self, Value: bool):
        self._check_for_error(self._lib.RegControls_Set_IsInverseTime(Value))

    @property
    def IsReversible(self) -> bool:
        '''
        Regulator can use different settings in the reverse direction.  Usually not applicable to substation transformers.

        Original COM help: https://opendss.epri.com/IsReversible.html
        '''
        return self._check_for_error(self._lib.RegControls_Get_IsReversible()) != 0

    @IsReversible.setter
    def IsReversible(self, Value: bool):
        self._check_for_error(self._lib.RegControls_Set_IsReversible(Value))

    @property
    def MaxTapChange(self) -> int:
        '''
        Maximum tap change per iteration in STATIC solution mode. 1 is more realistic, 16 is the default for a faster solution.

        Original COM help: https://opendss.epri.com/MaxTapChange.html
        '''
        return self._check_for_error(self._lib.RegControls_Get_MaxTapChange())

    @MaxTapChange.setter
    def MaxTapChange(self, Value: int):
        self._check_for_error(self._lib.RegControls_Set_MaxTapChange(Value))

    @property
    def MonitoredBus(self) -> str:
        '''
        Name of a remote regulated bus, in lieu of LDC settings

        Original COM help: https://opendss.epri.com/MonitoredBus.html
        '''
        return self._get_string(self._check_for_error(self._lib.RegControls_Get_MonitoredBus()))

    @MonitoredBus.setter
    def MonitoredBus(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.RegControls_Set_MonitoredBus(Value))

    @property
    def PTratio(self) -> float:
        '''
        PT ratio for voltage control settings

        Original COM help: https://opendss.epri.com/PTratio1.html
        '''
        return self._check_for_error(self._lib.RegControls_Get_PTratio())

    @PTratio.setter
    def PTratio(self, Value: float):
        self._check_for_error(self._lib.RegControls_Set_PTratio(Value))

    @property
    def ReverseBand(self) -> float:
        '''
        Bandwidth in reverse direction, centered on reverse Vreg.

        Original COM help: https://opendss.epri.com/ReverseBand.html
        '''
        return self._check_for_error(self._lib.RegControls_Get_ReverseBand())

    @ReverseBand.setter
    def ReverseBand(self, Value: float):
        self._check_for_error(self._lib.RegControls_Set_ReverseBand(Value))

    @property
    def ReverseR(self) -> float:
        '''
        Reverse LDC R setting in Volts.

        Original COM help: https://opendss.epri.com/ReverseR.html
        '''
        return self._check_for_error(self._lib.RegControls_Get_ReverseR())

    @ReverseR.setter
    def ReverseR(self, Value: float):
        self._check_for_error(self._lib.RegControls_Set_ReverseR(Value))

    @property
    def ReverseVreg(self) -> float:
        '''
        Target voltage in the revese direction, on PT secondary base.

        Original COM help: https://opendss.epri.com/ReverseVreg.html
        '''
        return self._check_for_error(self._lib.RegControls_Get_ReverseVreg())

    @ReverseVreg.setter
    def ReverseVreg(self, Value: float):
        self._check_for_error(self._lib.RegControls_Set_ReverseVreg(Value))

    @property
    def ReverseX(self) -> float:
        '''
        Reverse LDC X setting in volts.

        Original COM help: https://opendss.epri.com/ReverseX.html
        '''
        return self._check_for_error(self._lib.RegControls_Get_ReverseX())

    @ReverseX.setter
    def ReverseX(self, Value: float):
        self._check_for_error(self._lib.RegControls_Set_ReverseX(Value))

    @property
    def TapDelay(self) -> float:
        '''
        Time delay [s] for subsequent tap changes in a set. Control may reset before actually changing taps.

        Original COM help: https://opendss.epri.com/TapDelay.html
        '''
        return self._check_for_error(self._lib.RegControls_Get_TapDelay())

    @TapDelay.setter
    def TapDelay(self, Value: float):
        self._check_for_error(self._lib.RegControls_Set_TapDelay(Value))

    @property
    def TapNumber(self) -> int:
        '''
        Integer number of the tap that the controlled transformer winding is currently on.

        Original COM help: https://opendss.epri.com/TapNumber.html
        '''
        return self._check_for_error(self._lib.RegControls_Get_TapNumber())

    @TapNumber.setter
    def TapNumber(self, Value: int):
        self._check_for_error(self._lib.RegControls_Set_TapNumber(Value))

    @property
    def TapWinding(self) -> int:
        '''
        Tapped winding number

        Original COM help: https://opendss.epri.com/TapWinding.html
        '''
        return self._check_for_error(self._lib.RegControls_Get_TapWinding())

    @TapWinding.setter
    def TapWinding(self, Value: int):
        self._check_for_error(self._lib.RegControls_Set_TapWinding(Value))

    @property
    def Transformer(self) -> str:
        '''
        Name of the transformer this regulator controls

        Original COM help: https://opendss.epri.com/Transformer.html
        '''
        return self._get_string(self._check_for_error(self._lib.RegControls_Get_Transformer()))

    @Transformer.setter
    def Transformer(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.RegControls_Set_Transformer(Value))

    @property
    def VoltageLimit(self) -> float:
        '''
        First house voltage limit on PT secondary base.  Setting to 0 disables this function.

        Original COM help: https://opendss.epri.com/VoltageLimit.html
        '''
        return self._check_for_error(self._lib.RegControls_Get_VoltageLimit())

    @VoltageLimit.setter
    def VoltageLimit(self, Value: float):
        self._check_for_error(self._lib.RegControls_Set_VoltageLimit(Value))

    @property
    def Winding(self) -> int:
        '''
        Winding number for PT and CT connections

        Original COM help: https://opendss.epri.com/Winding.html
        '''
        return self._check_for_error(self._lib.RegControls_Get_Winding())

    @Winding.setter
    def Winding(self, Value: int):
        self._check_for_error(self._lib.RegControls_Set_Winding(Value))


