# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Iterable
from ._types import Float64Array
from typing import List, AnyStr

class IPVSystems(Iterable):
    __slots__ = []
    _is_circuit_element = True

    _columns = [
        'Name',
        'idx',
        'PF',
        'Irradiance',
        'IrradianceNow',
        'Pmpp',
        'RegisterNames',
        'RegisterValues',
        'kVArated',
        'kW',
        'kvar',
        'daily',
        'duty',
        'yearly',
        'Tdaily',
        'Tduty',
        'Tyearly',
        'Sensor',
    ]

    @property
    def Irradiance(self) -> float:
        '''
        Get/set the present value of the Irradiance property in kW/m²

        Original COM help: https://opendss.epri.com/Irradiance.html
        '''
        return self._check_for_error(self._lib.PVSystems_Get_Irradiance())

    @Irradiance.setter
    def Irradiance(self, Value: float):
        self._check_for_error(self._lib.PVSystems_Set_Irradiance(Value))

    @property
    def PF(self) -> float:
        '''
        Get/set the power factor for the active PVSystem

        Original COM help: https://opendss.epri.com/PF2.html
        '''
        return self._check_for_error(self._lib.PVSystems_Get_PF())

    @PF.setter
    def PF(self, Value: float):
        self._check_for_error(self._lib.PVSystems_Set_PF(Value))

    @property
    def RegisterNames(self) -> List[str]:
        '''
        Array of PVSystem energy meter register names
        
        See also the enum `GeneratorRegisters`.

        Original COM help: https://opendss.epri.com/RegisterNames2.html
        '''
        return self._check_for_error(self._get_string_array(self._lib.PVSystems_Get_RegisterNames))

    @property
    def RegisterValues(self) -> Float64Array:
        '''
        Array of doubles containing values in PVSystem registers.

        Original COM help: https://opendss.epri.com/RegisterValues2.html
        '''
        self._check_for_error(self._lib.PVSystems_Get_RegisterValues_GR())
        return self._get_float64_gr_array()

    @property
    def kVArated(self) -> float:
        '''
        Get/set Rated kVA of the PVSystem

        Original COM help: https://opendss.epri.com/kVArated1.html
        '''
        return self._check_for_error(self._lib.PVSystems_Get_kVArated())

    @kVArated.setter
    def kVArated(self, Value: float):
        self._check_for_error(self._lib.PVSystems_Set_kVArated(Value))

    @property
    def kW(self) -> float:
        '''
        Get kW output

        Original COM help: https://opendss.epri.com/kW2.html
        '''
        return self._check_for_error(self._lib.PVSystems_Get_kW())

    @property
    def kvar(self) -> float:
        '''
        Get/set kvar output value

        Original COM help: https://opendss.epri.com/kvar2.html
        '''
        return self._check_for_error(self._lib.PVSystems_Get_kvar())

    @kvar.setter
    def kvar(self, Value: float):
        self._check_for_error(self._lib.PVSystems_Set_kvar(Value))

    @property
    def daily(self) -> str:
        '''
        Name of the dispatch shape to use for daily simulations. Must be previously
        defined as a Loadshape object of 24 hrs, typically. In the default dispatch
        mode, the PVSystem element uses this loadshape to trigger State changes.
        
        **(API Extension)**
        '''
        return self._get_string(self._check_for_error(self._lib.PVSystems_Get_daily()))

    @daily.setter
    def daily(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.PVSystems_Set_daily(Value))

    @property
    def duty(self) -> str:
        '''
        Name of the load shape to use for duty cycle dispatch simulations such as
        for solar ramp rate studies. Must be previously defined as a Loadshape
        object. Typically would have time intervals of 1-5 seconds.

        **(API Extension)**
        '''
        return self._get_string(self._check_for_error(self._lib.PVSystems_Get_duty()))

    @duty.setter
    def duty(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.PVSystems_Set_duty(Value))

    @property
    def yearly(self) -> str:
        '''
        Dispatch shape to use for yearly simulations. Must be previously defined
        as a Loadshape object. If this is not specified, the Daily dispatch shape,
        if any, is repeated during Yearly solution modes. In the default dispatch
        mode, the PVSystem element uses this loadshape to trigger State changes.

        **(API Extension)**
        '''
        return self._get_string(self._check_for_error(self._lib.PVSystems_Get_yearly()))

    @yearly.setter
    def yearly(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.PVSystems_Set_yearly(Value))
        
    @property
    def Tdaily(self) -> str:
        '''
        Temperature shape to use for daily simulations. Must be previously defined
        as a TShape object of 24 hrs, typically. The PVSystem element uses this
        TShape to determine the Pmpp from the Pmpp vs T curve. Units must agree
        with the Pmpp vs T curve.

        **(API Extension)**
        '''
        return self._get_string(self._check_for_error(self._lib.PVSystems_Get_Tdaily()))

    @Tdaily.setter
    def Tdaily(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.PVSystems_Set_Tdaily(Value))

    @property
    def Tduty(self) -> str:
        '''
        Temperature shape to use for duty cycle dispatch simulations such as for
        solar ramp rate studies. Must be previously defined as a TShape object.
        Typically would have time intervals of 1-5 seconds. Designate the number
        of points to solve using the Set Number=xxxx command. If there are fewer
        points in the actual shape, the shape is assumed to repeat. The PVSystem
        model uses this TShape to determine the Pmpp from the Pmpp vs T curve.
        Units must agree with the Pmpp vs T curve.

        **(API Extension)**
        '''
        return self._get_string(self._check_for_error(self._lib.PVSystems_Get_Tduty()))

    @Tduty.setter
    def Tduty(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.PVSystems_Set_Tduty(Value))

    @property
    def Tyearly(self) -> str:
        '''
        Temperature shape to use for yearly simulations. Must be previously defined
        as a TShape object. If this is not specified, the Daily dispatch shape, if
        any, is repeated during Yearly solution modes. The PVSystem element uses
        this TShape to determine the Pmpp from the Pmpp vs T curve. Units must
        agree with the Pmpp vs T curve.

        **(API Extension)**
        '''
        return self._get_string(self._check_for_error(self._lib.PVSystems_Get_Tyearly()))

    @Tyearly.setter
    def Tyearly(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.PVSystems_Set_Tyearly(Value))

    @property 
    def IrradianceNow(self) -> float:
        '''
        Returns the current irradiance value for the active PVSystem. Use it to 
        know what's the current irradiance value for the PV during a simulation.

        Original COM help: https://opendss.epri.com/IrradianceNow.html
        '''
        return self._check_for_error(self._lib.PVSystems_Get_IrradianceNow())

    @property 
    def Pmpp(self) -> float:
        '''
        Gets/sets the rated max power of the PV array for 1.0 kW/m² irradiance 
        and a user-selected array temperature of the active PVSystem.

        Original COM help: https://opendss.epri.com/Pmpp.html
        '''
        return self._check_for_error(self._lib.PVSystems_Get_Pmpp())

    @Pmpp.setter
    def Pmpp(self, Value: float):
        self._check_for_error(self._lib.PVSystems_Set_Pmpp(Value))

    @property
    def Sensor(self) -> str:
        '''
        Name of the sensor monitoring this element.

        Original COM help: https://opendss.epri.com/Sensor1.html
        '''
        return self._get_string(self._check_for_error(self._lib.PVSystems_Get_Sensor()))
