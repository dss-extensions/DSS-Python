# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Iterable
from typing import AnyStr, Union
from .enums import CapControlModes

class ICapControls(Iterable):
    __slots__ = []

    _columns = [
        'Name',
        'idx',
        'Capacitor',
        'CTratio',
        'PTratio',
        'DeadTime',
        'Delay',
        'DelayOff',
        'Vmin',
        'Vmax',
        'UseVoltOverride',
        'Mode',
        'MonitoredObj',
        'MonitoredTerm',
        'OFFSetting',
        'ONSetting',
    ]

    def Reset(self):
        '''
        Force a reset of this CapControl.

        Original COM help: https://opendss.epri.com/Reset.html
        '''
        self._check_for_error(self._lib.CapControls_Reset())

    @property
    def CTratio(self) -> float:
        '''
        Transducer ratio from primary current to control current.

        Original COM help: https://opendss.epri.com/CTratio.html
        '''
        return self._check_for_error(self._lib.CapControls_Get_CTratio())

    @CTratio.setter
    def CTratio(self, Value: float):
        self._check_for_error(self._lib.CapControls_Set_CTratio(Value))

    @property
    def Capacitor(self) -> str:
        '''
        Name of the Capacitor that is controlled.

        Original COM help: https://opendss.epri.com/Capacitor.html
        '''
        return self._get_string(self._check_for_error(self._lib.CapControls_Get_Capacitor()))

    @Capacitor.setter
    def Capacitor(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.CapControls_Set_Capacitor(Value))

    @property
    def DeadTime(self) -> float:
        '''
        Dead time after capacitor is turned OFF before it can be turned back ON for the active CapControl.

        Default is 300 sec.

        Original COM help: https://opendss.epri.com/DeadTime.html
        '''
        return self._check_for_error(self._lib.CapControls_Get_DeadTime())

    @DeadTime.setter
    def DeadTime(self, Value: float):
        self._check_for_error(self._lib.CapControls_Set_DeadTime(Value))

    @property
    def Delay(self) -> float:
        '''
        Time delay [s] to switch on after arming.  Control may reset before actually switching.

        Original COM help: https://opendss.epri.com/Delay.html
        '''
        return self._check_for_error(self._lib.CapControls_Get_Delay())

    @Delay.setter
    def Delay(self, Value: float):
        self._check_for_error(self._lib.CapControls_Set_Delay(Value))

    @property
    def DelayOff(self) -> float:
        '''
        Time delay [s] before switching off a step. Control may reset before actually switching.

        Original COM help: https://opendss.epri.com/DelayOff.html
        '''
        return self._check_for_error(self._lib.CapControls_Get_DelayOff())

    @DelayOff.setter
    def DelayOff(self, Value: float):
        self._check_for_error(self._lib.CapControls_Set_DelayOff(Value))

    @property
    def Mode(self) -> CapControlModes:
        '''
        Type of automatic controller.

        Original COM help: https://opendss.epri.com/Mode.html
        '''
        return CapControlModes(self._check_for_error(self._lib.CapControls_Get_Mode()))

    @Mode.setter
    def Mode(self, Value: Union[CapControlModes, int]):
        self._check_for_error(self._lib.CapControls_Set_Mode(Value))

    @property
    def MonitoredObj(self) -> int:
        '''
        Full name of the element that PT and CT are connected to.

        Original COM help: https://opendss.epri.com/MonitoredObj.html
        '''
        return self._get_string(self._check_for_error(self._lib.CapControls_Get_MonitoredObj()))

    @MonitoredObj.setter
    def MonitoredObj(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.CapControls_Set_MonitoredObj(Value))

    @property
    def MonitoredTerm(self) -> int:
        '''
        Terminal number on the element that PT and CT are connected to.

        Original COM help: https://opendss.epri.com/MonitoredTerm.html
        '''
        return self._check_for_error(self._lib.CapControls_Get_MonitoredTerm())

    @MonitoredTerm.setter
    def MonitoredTerm(self, Value: int):
        self._check_for_error(self._lib.CapControls_Set_MonitoredTerm(Value))

    @property
    def OFFSetting(self) -> float:
        '''
        Threshold to switch off a step. See Mode for units.

        Original COM help: https://opendss.epri.com/OFFSetting.html
        '''
        return self._check_for_error(self._lib.CapControls_Get_OFFSetting())

    @OFFSetting.setter
    def OFFSetting(self, Value: float):
        self._check_for_error(self._lib.CapControls_Set_OFFSetting(Value))

    @property
    def ONSetting(self) -> float:
        '''
        Threshold to arm or switch on a step.  See Mode for units.

        Original COM help: https://opendss.epri.com/ONSetting.html
        '''
        return self._check_for_error(self._lib.CapControls_Get_ONSetting())

    @ONSetting.setter
    def ONSetting(self, Value: float):
        self._check_for_error(self._lib.CapControls_Set_ONSetting(Value))

    @property
    def PTratio(self) -> float:
        '''
        Transducer ratio from primary feeder to control voltage.

        Original COM help: https://opendss.epri.com/PTratio.html
        '''
        return self._check_for_error(self._lib.CapControls_Get_PTratio())

    @PTratio.setter
    def PTratio(self, Value: float):
        self._check_for_error(self._lib.CapControls_Set_PTratio(Value))

    @property
    def UseVoltOverride(self) -> float:
        '''
        Enables Vmin and Vmax to override the control Mode

        Original COM help: https://opendss.epri.com/UseVoltOverride.html
        '''
        return self._check_for_error(self._lib.CapControls_Get_UseVoltOverride()) != 0

    @UseVoltOverride.setter
    def UseVoltOverride(self, Value: float):
        self._check_for_error(self._lib.CapControls_Set_UseVoltOverride(Value))

    @property
    def Vmax(self) -> float:
        '''
        With VoltOverride, swtich off whenever PT voltage exceeds this level.

        Original COM help: https://opendss.epri.com/Vmax.html
        '''
        return self._check_for_error(self._lib.CapControls_Get_Vmax())

    @Vmax.setter
    def Vmax(self, Value: float):
        self._check_for_error(self._lib.CapControls_Set_Vmax(Value))

    @property
    def Vmin(self) -> float:
        '''
        With VoltOverride, switch ON whenever PT voltage drops below this level.

        Original COM help: https://opendss.epri.com/Vmin.html
        '''
        return self._check_for_error(self._lib.CapControls_Get_Vmin())

    @Vmin.setter
    def Vmin(self, Value: float):
        self._check_for_error(self._lib.CapControls_Set_Vmin(Value))
