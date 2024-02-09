# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Iterable
from typing import AnyStr

class IRelays(Iterable):
    __slots__ = []
    _is_circuit_element = True

    _columns = [
        'Name',
        'idx',
        'MonitoredObj',
        'MonitoredTerm',
        'SwitchedObj',
        'SwitchedTerm',
        'State',
        'NormalState'
    ]

    @property
    def MonitoredObj(self) -> str:
        '''
        Full name of object this Relay is monitoring.

        Original COM help: https://opendss.epri.com/MonitoredObj3.html
        '''
        return self._get_string(self._check_for_error(self._lib.Relays_Get_MonitoredObj()))

    @MonitoredObj.setter
    def MonitoredObj(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Relays_Set_MonitoredObj(Value))

    @property
    def MonitoredTerm(self) -> int:
        '''
        Number of terminal of monitored element that this Relay is monitoring.

        Original COM help: https://opendss.epri.com/MonitoredTerm3.html
        '''
        return self._check_for_error(self._lib.Relays_Get_MonitoredTerm())

    @MonitoredTerm.setter
    def MonitoredTerm(self, Value: int):
        self._check_for_error(self._lib.Relays_Set_MonitoredTerm(Value))

    @property
    def SwitchedObj(self) -> str:
        '''
        Full name of element that will be switched when relay trips.

        Original COM help: https://opendss.epri.com/SwitchedObj2.html
        '''
        return self._get_string(self._check_for_error(self._lib.Relays_Get_SwitchedObj()))

    @SwitchedObj.setter
    def SwitchedObj(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Relays_Set_SwitchedObj(Value))

    @property
    def SwitchedTerm(self) -> int:
        '''
        Terminal number of the switched object that will be opened when the relay trips.

        Original COM help: https://opendss.epri.com/SwitchedTerm2.html
        '''
        return self._check_for_error(self._lib.Relays_Get_SwitchedTerm())

    @SwitchedTerm.setter
    def SwitchedTerm(self, Value: int):
        self._check_for_error(self._lib.Relays_Set_SwitchedTerm(Value))

    def Open(self):
        '''
        Open relay's controlled element and lock out the relay.

        Original COM help: https://opendss.epri.com/Open4.html
        '''
        self._check_for_error(self._lib.Relays_Open())

    def Close(self):
        '''
        Close the switched object controlled by the relay. Resets relay to first operation.

        Original COM help: https://opendss.epri.com/Close5.html
        '''
        self._check_for_error(self._lib.Relays_Close())

    def Reset(self):
        '''
        Reset relay to normal state. 
        If open, lock out the relay. 
        If closed, resets relay to first operation.
        '''
        self._check_for_error(self._lib.Relays_Reset())

    @property
    def State(self) -> int:
        '''
        Get/Set present state of relay. 
        If set to open, open relay's controlled element and lock out the relay. 
        If set to close, close relay's controlled element and resets relay to first operation.
        '''
        return self._check_for_error(self._lib.Relays_Get_State())

    @State.setter
    def State(self, Value: int):
        self._check_for_error(self._lib.Relays_Set_State(Value))

    @property
    def NormalState(self) -> int:
        '''
        Normal state of relay.

        Original COM help: https://opendss.epri.com/NormalState3.html
        '''
        return self._check_for_error(self._lib.Relays_Get_NormalState())

    @NormalState.setter
    def NormalState(self, Value: int):
        self._check_for_error(self._lib.Relays_Set_NormalState(Value))
