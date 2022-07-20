'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira
Copyright (c) 2018-2022 DSS Extensions contributors
'''
from .._cffi_api_util import Iterable

class ISensors(Iterable):
    __slots__ = []

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
    def Currents(self):
        '''Array of doubles for the line current measurements; don't use with kWS and kVARS.'''
        return self._get_float64_array(self._lib.Sensors_Get_Currents)

    @Currents.setter
    def Currents(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Sensors_Set_Currents(ValuePtr, ValueCount))

    @property
    def IsDelta(self):
        '''True if measured voltages are line-line. Currents are always line currents.'''
        return self.CheckForError(self._lib.Sensors_Get_IsDelta()) != 0

    @IsDelta.setter
    def IsDelta(self, Value):
        self.CheckForError(self._lib.Sensors_Set_IsDelta(Value))

    @property
    def MeteredElement(self):
        '''Full Name of the measured element'''
        return self._get_string(self.CheckForError(self._lib.Sensors_Get_MeteredElement()))

    @MeteredElement.setter
    def MeteredElement(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Sensors_Set_MeteredElement(Value))

    @property
    def MeteredTerminal(self):
        '''Number of the measured terminal in the measured element.'''
        return self.CheckForError(self._lib.Sensors_Get_MeteredTerminal())

    @MeteredTerminal.setter
    def MeteredTerminal(self, Value):
        self.CheckForError(self._lib.Sensors_Set_MeteredTerminal(Value))

    @property
    def PctError(self):
        '''Assumed percent error in the Sensor measurement. Default is 1.'''
        return self.CheckForError(self._lib.Sensors_Get_PctError())

    @PctError.setter
    def PctError(self, Value):
        self.CheckForError(self._lib.Sensors_Set_PctError(Value))

    @property
    def ReverseDelta(self):
        '''True if voltage measurements are 1-3, 3-2, 2-1.'''
        return self.CheckForError(self._lib.Sensors_Get_ReverseDelta()) != 0

    @ReverseDelta.setter
    def ReverseDelta(self, Value):
        self.CheckForError(self._lib.Sensors_Set_ReverseDelta(Value))

    @property
    def Weight(self):
        '''Weighting factor for this Sensor measurement with respect to other Sensors. Default is 1.'''
        return self.CheckForError(self._lib.Sensors_Get_Weight())

    @Weight.setter
    def Weight(self, Value):
        self.CheckForError(self._lib.Sensors_Set_Weight(Value))

    @property
    def kVARS(self):
        '''Array of doubles for Q measurements. Overwrites Currents with a new estimate using kWS.'''
        return self._get_float64_array(self._lib.Sensors_Get_kVARS)

    @kVARS.setter
    def kVARS(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Sensors_Set_kVARS(ValuePtr, ValueCount))

    @property
    def kVS(self):
        '''Array of doubles for the LL or LN (depending on Delta connection) voltage measurements.'''
        return self._get_float64_array(self._lib.Sensors_Get_kVS)

    @kVS.setter
    def kVS(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Sensors_Set_kVS(ValuePtr, ValueCount))

    @property
    def kVbase(self):
        '''Voltage base for the sensor measurements. LL for 2 and 3-phase sensors, LN for 1-phase sensors.'''
        return self.CheckForError(self._lib.Sensors_Get_kVbase())

    @kVbase.setter
    def kVbase(self, Value):
        self.CheckForError(self._lib.Sensors_Set_kVbase(Value))

    @property
    def kWS(self):
        '''Array of doubles for P measurements. Overwrites Currents with a new estimate using kVARS.'''
        return self._get_float64_array(self._lib.Sensors_Get_kWS)

    @kWS.setter
    def kWS(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Sensors_Set_kWS(ValuePtr, ValueCount))

    @property
    def AllocationFactor(self):
        '''Array of doubles for the allocation factors for each phase.'''
        return self._get_float64_array(self._lib.Sensors_Get_AllocationFactor)
