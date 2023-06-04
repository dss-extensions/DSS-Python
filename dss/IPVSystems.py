# -*- coding: utf-8 -*-
'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2023 Paulo Meira

Copyright (c) 2018-2023 DSS-Extensions contributors
'''
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
        '''Get/set the present value of the Irradiance property in kW/m²'''
        return self.CheckForError(self._lib.PVSystems_Get_Irradiance())

    @Irradiance.setter
    def Irradiance(self, Value: float):
        self.CheckForError(self._lib.PVSystems_Set_Irradiance(Value))

    @property
    def PF(self) -> float:
        '''Get/set the power factor for the active PVSystem'''
        return self.CheckForError(self._lib.PVSystems_Get_PF())

    @PF.setter
    def PF(self, Value: float):
        self.CheckForError(self._lib.PVSystems_Set_PF(Value))

    @property
    def RegisterNames(self) -> List[str]:
        '''Array of PVSYSTEM energy meter register names'''
        return self.CheckForError(self._get_string_array(self._lib.PVSystems_Get_RegisterNames))

    @property
    def RegisterValues(self) -> Float64Array:
        '''Array of doubles containing values in PVSystem registers.'''
        self.CheckForError(self._lib.PVSystems_Get_RegisterValues_GR())
        return self._get_float64_gr_array()

    @property
    def kVArated(self) -> float:
        '''Get/set Rated kVA of the PVSystem'''
        return self.CheckForError(self._lib.PVSystems_Get_kVArated())

    @kVArated.setter
    def kVArated(self, Value: float):
        self.CheckForError(self._lib.PVSystems_Set_kVArated(Value))

    @property
    def kW(self) -> float:
        '''Get kW output'''
        return self.CheckForError(self._lib.PVSystems_Get_kW())

    @property
    def kvar(self) -> float:
        '''Get/set kvar output value'''
        return self.CheckForError(self._lib.PVSystems_Get_kvar())

    @kvar.setter
    def kvar(self, Value: float):
        self.CheckForError(self._lib.PVSystems_Set_kvar(Value))

    @property
    def daily(self) -> str:
        '''
        Name of the dispatch shape to use for daily simulations. Must be previously
        defined as a Loadshape object of 24 hrs, typically. In the default dispatch
        mode, the PVSystem element uses this loadshape to trigger State changes.
        
        (API Extension)
        '''
        return self._get_string(self.CheckForError(self._lib.PVSystems_Get_daily()))

    @daily.setter
    def daily(self, Value: AnyStr):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.PVSystems_Set_daily(Value))

    @property
    def duty(self) -> str:
        '''
        Name of the load shape to use for duty cycle dispatch simulations such as
        for solar ramp rate studies. Must be previously defined as a Loadshape
        object. Typically would have time intervals of 1-5 seconds.

        (API Extension)
        '''
        return self._get_string(self.CheckForError(self._lib.PVSystems_Get_duty()))

    @duty.setter
    def duty(self, Value: AnyStr):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.PVSystems_Set_duty(Value))

    @property
    def yearly(self) -> str:
        '''
        Dispatch shape to use for yearly simulations. Must be previously defined
        as a Loadshape object. If this is not specified, the Daily dispatch shape,
        if any, is repeated during Yearly solution modes. In the default dispatch
        mode, the PVSystem element uses this loadshape to trigger State changes.

        (API Extension)
        '''
        return self._get_string(self.CheckForError(self._lib.PVSystems_Get_yearly()))

    @yearly.setter
    def yearly(self, Value: AnyStr):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.PVSystems_Set_yearly(Value))
        
    @property
    def Tdaily(self) -> str:
        '''
        Temperature shape to use for daily simulations. Must be previously defined
        as a TShape object of 24 hrs, typically. The PVSystem element uses this
        TShape to determine the Pmpp from the Pmpp vs T curve. Units must agree
        with the Pmpp vs T curve.

        (API Extension)
        '''
        return self._get_string(self.CheckForError(self._lib.PVSystems_Get_Tdaily()))

    @Tdaily.setter
    def Tdaily(self, Value: AnyStr):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.PVSystems_Set_Tdaily(Value))

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

        (API Extension)
        '''
        return self._get_string(self.CheckForError(self._lib.PVSystems_Get_Tduty()))

    @Tduty.setter
    def Tduty(self, Value: AnyStr):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.PVSystems_Set_Tduty(Value))

    @property
    def Tyearly(self) -> str:
        '''
        Temperature shape to use for yearly simulations. Must be previously defined
        as a TShape object. If this is not specified, the Daily dispatch shape, if
        any, is repeated during Yearly solution modes. The PVSystem element uses
        this TShape to determine the Pmpp from the Pmpp vs T curve. Units must
        agree with the Pmpp vs T curve.

        (API Extension)
        '''
        return self._get_string(self.CheckForError(self._lib.PVSystems_Get_Tyearly()))

    @Tyearly.setter
    def Tyearly(self, Value: AnyStr):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.PVSystems_Set_Tyearly(Value))

    @property 
    def IrradianceNow(self) -> float:
        '''
        Returns the current irradiance value for the active PVSystem. Use it to 
        know what's the current irradiance value for the PV during a simulation.
        '''
        return self.CheckForError(self._lib.PVSystems_Get_IrradianceNow())

    @property 
    def Pmpp(self) -> float:
        '''
        Gets/sets the rated max power of the PV array for 1.0 kW/sq-m irradiance 
        and a user-selected array temperature of the active PVSystem.
        '''
        return self.CheckForError(self._lib.PVSystems_Get_Pmpp())

    @Pmpp.setter
    def Pmpp(self, Value: float):
        self.CheckForError(self._lib.PVSystems_Set_Pmpp(Value))

    @property
    def Sensor(self) -> str:
        '''Name of the sensor monitoring this element.'''
        return self._get_string(self.CheckForError(self._lib.PVSystems_Get_Sensor()))
