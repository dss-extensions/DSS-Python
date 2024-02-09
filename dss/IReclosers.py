# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Iterable
from ._types import Float64Array
from typing import AnyStr

class IReclosers(Iterable):
    __slots__ = []
    _is_circuit_element = True

    _columns = [
        'Name',
        'idx',
        'GroundInst',
        'GroundTrip',
        'MonitoredObj',
        'MonitoredTerm',
        'SwitchedObj',
        'SwitchedTerm',
        'NumFast',
        'PhaseInst',
        'PhaseTrip',
        'RecloseIntervals',
        'Shots',
        'State',
        'NormalState',
    ]

    def Close(self):
        self._check_for_error(self._lib.Reclosers_Close())

    def Open(self):
        self._check_for_error(self._lib.Reclosers_Open())

    @property
    def GroundInst(self) -> float:
        '''
        Ground (3I0) instantaneous trip setting - curve multiplier or actual amps.

        Original COM help: https://opendss.epri.com/GroundInst.html
        '''
        return self._check_for_error(self._lib.Reclosers_Get_GroundInst())

    @GroundInst.setter
    def GroundInst(self, Value: float):
        self._check_for_error(self._lib.Reclosers_Set_GroundInst(Value))

    @property
    def GroundTrip(self) -> float:
        '''
        Ground (3I0) trip multiplier or actual amps

        Original COM help: https://opendss.epri.com/GroundTrip.html
        '''
        return self._check_for_error(self._lib.Reclosers_Get_GroundTrip())

    @GroundTrip.setter
    def GroundTrip(self, Value: float):
        self._check_for_error(self._lib.Reclosers_Set_GroundTrip(Value))

    @property
    def MonitoredObj(self) -> str:
        '''
        Full name of object this Recloser to be monitored.

        Original COM help: https://opendss.epri.com/MonitoredObj2.html
        '''
        return self._get_string(self._check_for_error(self._lib.Reclosers_Get_MonitoredObj()))

    @MonitoredObj.setter
    def MonitoredObj(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Reclosers_Set_MonitoredObj(Value))

    @property
    def MonitoredTerm(self) -> int:
        '''
        Terminal number of Monitored object for the Recloser 

        Original COM help: https://opendss.epri.com/MonitoredTerm2.html
        '''
        return self._check_for_error(self._lib.Reclosers_Get_MonitoredTerm())

    @MonitoredTerm.setter
    def MonitoredTerm(self, Value: int):
        self._check_for_error(self._lib.Reclosers_Set_MonitoredTerm(Value))

    @property
    def NumFast(self) -> int:
        '''
        Number of fast shots

        Original COM help: https://opendss.epri.com/NumFast.html
        '''
        return self._check_for_error(self._lib.Reclosers_Get_NumFast())

    @NumFast.setter
    def NumFast(self, Value: int):
        self._check_for_error(self._lib.Reclosers_Set_NumFast(Value))

    @property
    def PhaseInst(self) -> float:
        '''
        Phase instantaneous curve multiplier or actual amps

        Original COM help: https://opendss.epri.com/PhaseInst.html
        '''
        return self._check_for_error(self._lib.Reclosers_Get_PhaseInst())

    @PhaseInst.setter
    def PhaseInst(self, Value: float):
        self._check_for_error(self._lib.Reclosers_Set_PhaseInst(Value))

    @property
    def PhaseTrip(self) -> float:
        '''
        Phase trip curve multiplier or actual amps

        Original COM help: https://opendss.epri.com/PhaseTrip.html
        '''
        return self._check_for_error(self._lib.Reclosers_Get_PhaseTrip())

    @PhaseTrip.setter
    def PhaseTrip(self, Value: float):
        self._check_for_error(self._lib.Reclosers_Set_PhaseTrip(Value))

    @property
    def RecloseIntervals(self) -> Float64Array:
        '''
        Array of Doubles: reclose intervals, s, between shots.

        Original COM help: https://opendss.epri.com/RecloseIntervals.html
        '''
        self._check_for_error(self._lib.Reclosers_Get_RecloseIntervals_GR())
        return self._get_float64_gr_array()

    @property
    def Shots(self) -> int:
        '''
        Number of shots to lockout (fast + delayed)

        Original COM help: https://opendss.epri.com/Shots.html
        '''
        return self._check_for_error(self._lib.Reclosers_Get_Shots())

    @Shots.setter
    def Shots(self, Value: int):
        self._check_for_error(self._lib.Reclosers_Set_Shots(Value))

    @property
    def SwitchedObj(self) -> str:
        '''
        Full name of the circuit element that is being switched by the Recloser.

        Original COM help: https://opendss.epri.com/SwitchedObj1.html
        '''
        return self._get_string(self._check_for_error(self._lib.Reclosers_Get_SwitchedObj()))

    @SwitchedObj.setter
    def SwitchedObj(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Reclosers_Set_SwitchedObj(Value))

    @property
    def SwitchedTerm(self) -> int:
        '''
        Terminal number of the controlled device being switched by the Recloser

        Original COM help: https://opendss.epri.com/SwitchedTerm1.html
        '''
        return self._check_for_error(self._lib.Reclosers_Get_SwitchedTerm())

    @SwitchedTerm.setter
    def SwitchedTerm(self, Value: int):
        self._check_for_error(self._lib.Reclosers_Set_SwitchedTerm(Value))


    def Reset(self):
        '''
        Reset recloser to normal state. 
        If open, lock out the recloser. 
        If closed, resets recloser to first operation.
        '''
        self._check_for_error(self._lib.Reclosers_Reset())

    @property
    def State(self) -> int:
        '''
        Get/Set present state of recloser. 
        If set to open (ActionCodes.Open=1), open recloser's controlled element and lock out the recloser. 
        If set to close (ActionCodes.Close=2), close recloser's controlled element and resets recloser to first operation.
        '''
        return self._check_for_error(self._lib.Reclosers_Get_State())

    @State.setter
    def State(self, Value: int):
        self._check_for_error(self._lib.Reclosers_Set_State(Value))

    @property
    def NormalState(self) -> int:
        '''
        Get/set normal state (ActionCodes.Open=1, ActionCodes.Close=2) of the recloser.

        Original COM help: https://opendss.epri.com/NormalState1.html
        '''
        return self._check_for_error(self._lib.Reclosers_Get_NormalState())

    @NormalState.setter
    def NormalState(self, Value: int):
        self._check_for_error(self._lib.Reclosers_Set_NormalState(Value))
