# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
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
        self._check_for_error(self._lib.Sensors_Reset())

    def ResetAll(self):
        self._check_for_error(self._lib.Sensors_ResetAll())

    @property
    def Currents(self) -> Float64Array:
        '''
        Array of doubles for the line current measurements; don't use with kWS and kVARS.

        Original COM help: https://opendss.epri.com/Currents2.html
        '''
        self._check_for_error(self._lib.Sensors_Get_Currents_GR())
        return self._get_float64_gr_array()

    @Currents.setter
    def Currents(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.Sensors_Set_Currents(ValuePtr, ValueCount))

    @property
    def IsDelta(self) -> bool:
        '''
        True if measured voltages are line-line. Currents are always line currents.

        Original COM help: https://opendss.epri.com/IsDelta2.html
        '''
        return self._check_for_error(self._lib.Sensors_Get_IsDelta()) != 0

    @IsDelta.setter
    def IsDelta(self, Value: bool):
        self._check_for_error(self._lib.Sensors_Set_IsDelta(Value))

    @property
    def MeteredElement(self) -> str:
        '''
        Full Name of the measured element

        Original COM help: https://opendss.epri.com/MeteredElement1.html
        '''
        return self._get_string(self._check_for_error(self._lib.Sensors_Get_MeteredElement()))

    @MeteredElement.setter
    def MeteredElement(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Sensors_Set_MeteredElement(Value))

    @property
    def MeteredTerminal(self) -> int:
        '''
        Number of the measured terminal in the measured element.

        Original COM help: https://opendss.epri.com/MeteredTerminal1.html
        '''
        return self._check_for_error(self._lib.Sensors_Get_MeteredTerminal())

    @MeteredTerminal.setter
    def MeteredTerminal(self, Value: int):
        self._check_for_error(self._lib.Sensors_Set_MeteredTerminal(Value))

    @property
    def PctError(self) -> float:
        '''
        Assumed percent error in the Sensor measurement. Default is 1.

        Original COM help: https://opendss.epri.com/PctError.html
        '''
        return self._check_for_error(self._lib.Sensors_Get_PctError())

    @PctError.setter
    def PctError(self, Value: float):
        self._check_for_error(self._lib.Sensors_Set_PctError(Value))

    @property
    def ReverseDelta(self) -> bool:
        '''
        True if voltage measurements are 1-3, 3-2, 2-1.

        Original COM help: https://opendss.epri.com/ReverseDelta.html
        '''
        return self._check_for_error(self._lib.Sensors_Get_ReverseDelta()) != 0

    @ReverseDelta.setter
    def ReverseDelta(self, Value: bool):
        self._check_for_error(self._lib.Sensors_Set_ReverseDelta(Value))

    @property
    def Weight(self) -> float:
        '''
        Weighting factor for this Sensor measurement with respect to other Sensors. Default is 1.

        Original COM help: https://opendss.epri.com/Weight.html
        '''
        return self._check_for_error(self._lib.Sensors_Get_Weight())

    @Weight.setter
    def Weight(self, Value: float):
        self._check_for_error(self._lib.Sensors_Set_Weight(Value))

    @property
    def kVARS(self) -> Float64Array:
        '''
        Array of doubles for Q measurements. Overwrites Currents with a new estimate using kWS.

        Original COM help: https://opendss.epri.com/kVARS.html
        '''
        self._check_for_error(self._lib.Sensors_Get_kVARS_GR())
        return self._get_float64_gr_array()

    @kVARS.setter
    def kVARS(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.Sensors_Set_kVARS(ValuePtr, ValueCount))

    @property
    def kVS(self) -> Float64Array:
        '''
        Array of doubles for the LL or LN (depending on Delta connection) voltage measurements.

        Original COM help: https://opendss.epri.com/kVS.html
        '''
        self._check_for_error(self._lib.Sensors_Get_kVS_GR())
        return self._get_float64_gr_array()

    @kVS.setter
    def kVS(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.Sensors_Set_kVS(ValuePtr, ValueCount))

    @property
    def kVbase(self) -> float:
        '''
        Voltage base for the sensor measurements. LL for 2 and 3-phase sensors, LN for 1-phase sensors.

        Original COM help: https://opendss.epri.com/kVBase1.html
        '''
        return self._check_for_error(self._lib.Sensors_Get_kVbase())

    @kVbase.setter
    def kVbase(self, Value: float):
        self._check_for_error(self._lib.Sensors_Set_kVbase(Value))

    @property
    def kWS(self) -> Float64Array:
        '''
        Array of doubles for P measurements. Overwrites Currents with a new estimate using kVARS.

        Original COM help: https://opendss.epri.com/kWS.html
        '''
        self._check_for_error(self._lib.Sensors_Get_kWS_GR())
        return self._get_float64_gr_array()

    @kWS.setter
    def kWS(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.Sensors_Set_kWS(ValuePtr, ValueCount))

    @property
    def AllocationFactor(self):
        '''
        Array of doubles for the allocation factors for each phase.

        Original COM help: https://opendss.epri.com/AllocationFactor1.html
        '''
        self._check_for_error(self._lib.Sensors_Get_AllocationFactor_GR())
        return self._get_float64_gr_array()
