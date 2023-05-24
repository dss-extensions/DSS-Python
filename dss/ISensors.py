'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2023 Paulo Meira

Copyright (c) 2018-2023 DSS-Extensions contributors
'''
from ._cffi_api_util import Iterable
from ._types import Float64Array
from typing import AnyStr

class ISensors(Iterable):
    __slots__ = []
    _is_circuit_element = True

    _columns = [
        'Name',
        'idx',
        'MeteredElement',
        'MeteredTerminal',
        'IsDelta',
        'ReverseDelta',
        'Currents',
        'PctError',
        'Weight',
        'kVbase',
        'kVARS',
        'kVS',
        'kWS',
        'AllocationFactor',
    ]

    def Reset(self):
        self.CheckForError(self._lib.Sensors_Reset())

    def ResetAll(self):
        self.CheckForError(self._lib.Sensors_ResetAll())

    @property
    def Currents(self) -> Float64Array:
        '''Array of doubles for the line current measurements; don't use with kWS and kVARS.'''
        self.CheckForError(self._lib.Sensors_Get_Currents_GR())
        return self._get_float64_gr_array()

    @Currents.setter
    def Currents(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Sensors_Set_Currents(ValuePtr, ValueCount))

    @property
    def IsDelta(self) -> bool:
        '''True if measured voltages are line-line. Currents are always line currents.'''
        return self.CheckForError(self._lib.Sensors_Get_IsDelta()) != 0

    @IsDelta.setter
    def IsDelta(self, Value: bool):
        self.CheckForError(self._lib.Sensors_Set_IsDelta(Value))

    @property
    def MeteredElement(self) -> str:
        '''Full Name of the measured element'''
        return self._get_string(self.CheckForError(self._lib.Sensors_Get_MeteredElement()))

    @MeteredElement.setter
    def MeteredElement(self, Value: AnyStr):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Sensors_Set_MeteredElement(Value))

    @property
    def MeteredTerminal(self) -> int:
        '''Number of the measured terminal in the measured element.'''
        return self.CheckForError(self._lib.Sensors_Get_MeteredTerminal())

    @MeteredTerminal.setter
    def MeteredTerminal(self, Value: int):
        self.CheckForError(self._lib.Sensors_Set_MeteredTerminal(Value))

    @property
    def PctError(self) -> float:
        '''Assumed percent error in the Sensor measurement. Default is 1.'''
        return self.CheckForError(self._lib.Sensors_Get_PctError())

    @PctError.setter
    def PctError(self, Value: float):
        self.CheckForError(self._lib.Sensors_Set_PctError(Value))

    @property
    def ReverseDelta(self) -> bool:
        '''True if voltage measurements are 1-3, 3-2, 2-1.'''
        return self.CheckForError(self._lib.Sensors_Get_ReverseDelta()) != 0

    @ReverseDelta.setter
    def ReverseDelta(self, Value: bool):
        self.CheckForError(self._lib.Sensors_Set_ReverseDelta(Value))

    @property
    def Weight(self) -> float:
        '''Weighting factor for this Sensor measurement with respect to other Sensors. Default is 1.'''
        return self.CheckForError(self._lib.Sensors_Get_Weight())

    @Weight.setter
    def Weight(self, Value: float):
        self.CheckForError(self._lib.Sensors_Set_Weight(Value))

    @property
    def kVARS(self) -> Float64Array:
        '''Array of doubles for Q measurements. Overwrites Currents with a new estimate using kWS.'''
        self.CheckForError(self._lib.Sensors_Get_kVARS_GR())
        return self._get_float64_gr_array()

    @kVARS.setter
    def kVARS(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Sensors_Set_kVARS(ValuePtr, ValueCount))

    @property
    def kVS(self) -> Float64Array:
        '''Array of doubles for the LL or LN (depending on Delta connection) voltage measurements.'''
        self.CheckForError(self._lib.Sensors_Get_kVS_GR())
        return self._get_float64_gr_array()

    @kVS.setter
    def kVS(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Sensors_Set_kVS(ValuePtr, ValueCount))

    @property
    def kVbase(self) -> float:
        '''Voltage base for the sensor measurements. LL for 2 and 3-phase sensors, LN for 1-phase sensors.'''
        return self.CheckForError(self._lib.Sensors_Get_kVbase())

    @kVbase.setter
    def kVbase(self, Value: float):
        self.CheckForError(self._lib.Sensors_Set_kVbase(Value))

    @property
    def kWS(self) -> Float64Array:
        '''Array of doubles for P measurements. Overwrites Currents with a new estimate using kVARS.'''
        self.CheckForError(self._lib.Sensors_Get_kWS_GR())
        return self._get_float64_gr_array()

    @kWS.setter
    def kWS(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Sensors_Set_kWS(ValuePtr, ValueCount))

    @property
    def AllocationFactor(self):
        '''Array of doubles for the allocation factors for each phase.'''
        self.CheckForError(self._lib.Sensors_Get_AllocationFactor_GR())
        return self._get_float64_gr_array()
