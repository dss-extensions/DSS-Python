'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class ISensors(Base):
    __slots__ = []

    def Reset(self):
        self.lib.Sensors_Reset()

    def ResetAll(self):
        self.lib.Sensors_ResetAll()

    @property
    def AllNames(self):
        '''(read-only) Array of Sensor names.'''
        return self.get_string_array(self.lib.Sensors_Get_AllNames)

    @property
    def Count(self):
        '''(read-only) Number of Sensors in Active Circuit.'''
        return self.lib.Sensors_Get_Count()

    def __len__(self):
        return self.lib.Sensors_Get_Count()

    @property
    def Currents(self):
        '''Array of doubles for the line current measurements; don't use with kWS and kVARS.'''
        self.lib.Sensors_Get_Currents_GR()
        return self.get_float64_gr_array()

    @Currents.setter
    def Currents(self, Value):
        Value, ValuePtr, ValueCount = self.prepare_float64_array(Value)
        self.lib.Sensors_Set_Currents(ValuePtr, ValueCount)

    @property
    def First(self):
        '''(read-only) Sets the first sensor active. Returns 0 if none.'''
        return self.lib.Sensors_Get_First()

    @property
    def IsDelta(self):
        '''True if measured voltages are line-line. Currents are always line currents.'''
        return self.lib.Sensors_Get_IsDelta() != 0

    @IsDelta.setter
    def IsDelta(self, Value):
        self.lib.Sensors_Set_IsDelta(Value)

    @property
    def MeteredElement(self):
        '''Full Name of the measured element'''
        return self.get_string(self.lib.Sensors_Get_MeteredElement())

    @MeteredElement.setter
    def MeteredElement(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.Sensors_Set_MeteredElement(Value)

    @property
    def MeteredTerminal(self):
        '''Number of the measured terminal in the measured element.'''
        return self.lib.Sensors_Get_MeteredTerminal()

    @MeteredTerminal.setter
    def MeteredTerminal(self, Value):
        self.lib.Sensors_Set_MeteredTerminal(Value)

    @property
    def Name(self):
        '''
        (read) Name of the active sensor.
        (write) Set the active Sensor by name.
        '''
        return self.get_string(self.lib.Sensors_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.Sensors_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Sets the next Sensor active. Returns 0 if no more.'''
        return self.lib.Sensors_Get_Next()

    @property
    def PctError(self):
        '''Assumed percent error in the Sensor measurement. Default is 1.'''
        return self.lib.Sensors_Get_PctError()

    @PctError.setter
    def PctError(self, Value):
        self.lib.Sensors_Set_PctError(Value)

    @property
    def ReverseDelta(self):
        '''True if voltage measurements are 1-3, 3-2, 2-1.'''
        return self.lib.Sensors_Get_ReverseDelta() != 0

    @ReverseDelta.setter
    def ReverseDelta(self, Value):
        self.lib.Sensors_Set_ReverseDelta(Value)

    @property
    def Weight(self):
        '''Weighting factor for this Sensor measurement with respect to other Sensors. Default is 1.'''
        return self.lib.Sensors_Get_Weight()

    @Weight.setter
    def Weight(self, Value):
        self.lib.Sensors_Set_Weight(Value)

    @property
    def kVARS(self):
        '''Array of doubles for Q measurements. Overwrites Currents with a new estimate using kWS.'''
        self.lib.Sensors_Get_kVARS_GR()
        return self.get_float64_gr_array()

    @kVARS.setter
    def kVARS(self, Value):
        Value, ValuePtr, ValueCount = self.prepare_float64_array(Value)
        self.lib.Sensors_Set_kVARS(ValuePtr, ValueCount)

    @property
    def kVS(self):
        '''Array of doubles for the LL or LN (depending on Delta connection) voltage measurements.'''
        self.lib.Sensors_Get_kVS_GR()
        return self.get_float64_gr_array()

    @kVS.setter
    def kVS(self, Value):
        Value, ValuePtr, ValueCount = self.prepare_float64_array(Value)
        self.lib.Sensors_Set_kVS(ValuePtr, ValueCount)

    @property
    def kVbase(self):
        '''Voltage base for the sensor measurements. LL for 2 and 3-phase sensors, LN for 1-phase sensors.'''
        return self.lib.Sensors_Get_kVbase()

    @kVbase.setter
    def kVbase(self, Value):
        self.lib.Sensors_Set_kVbase(Value)

    @property
    def kWS(self):
        '''Array of doubles for P measurements. Overwrites Currents with a new estimate using kVARS.'''
        self.lib.Sensors_Get_kWS_GR()
        return self.get_float64_gr_array()

    @kWS.setter
    def kWS(self, Value):
        Value, ValuePtr, ValueCount = self.prepare_float64_array(Value)
        self.lib.Sensors_Set_kWS(ValuePtr, ValueCount)

    def __iter__(self):
        idx = self.First
        while idx != 0:
            yield self
            idx = self.Next

