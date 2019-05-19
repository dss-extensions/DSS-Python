'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2019 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Iterable


class IPVSystems(Iterable):
    __slots__ = []    

    @property
    def Irradiance(self):
        '''
        (read) Get the present value of the Irradiance property in W/sq-m
        (write) Set the present Irradiance value in W/sq-m
        '''
        return self._lib.PVSystems_Get_Irradiance()

    @Irradiance.setter
    def Irradiance(self, Value):
        self._lib.PVSystems_Set_Irradiance(Value)
        self.CheckForError()

    @property
    def PF(self):
        '''
        (read) Get Power factor
        (write) Set PF
        '''
        return self._lib.PVSystems_Get_PF()

    @PF.setter
    def PF(self, Value):
        self._lib.PVSystems_Set_PF(Value)
        self.CheckForError()

    @property
    def RegisterNames(self):
        '''(read-only) Variant Array of PVSYSTEM energy meter register names'''
        return self._get_string_array(self._lib.PVSystems_Get_RegisterNames)

    @property
    def RegisterValues(self):
        '''(read-only) Array of doubles containing values in PVSystem registers.'''
        return self._get_float64_array(self._lib.PVSystems_Get_RegisterValues)

    @property
    def kVArated(self):
        '''
        (read) Get Rated kVA of the PVSystem
        (write) Set kva rated
        '''
        return self._lib.PVSystems_Get_kVArated()

    @kVArated.setter
    def kVArated(self, Value):
        self._lib.PVSystems_Set_kVArated(Value)
        self.CheckForError()

    @property
    def kW(self):
        '''(read-only) get kW output'''
        return self._lib.PVSystems_Get_kW()

    @property
    def kvar(self):
        '''
        (read) Get kvar value
        (write) Set kvar output value
        '''
        return self._lib.PVSystems_Get_kvar()

    @kvar.setter
    def kvar(self, Value):
        self._lib.PVSystems_Set_kvar(Value)
        self.CheckForError()


    @property
    def daily(self):
        '''Name of the loadshape for a daily PVSystem profile.'''
        return self._get_string(self._lib.PVSystems_Get_daily())

    @daily.setter
    def daily(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.PVSystems_Set_daily(Value)
        self.CheckForError()

    @property
    def duty(self):
        '''
        Name of the load shape to use for duty cycle dispatch simulations such as
        for solar ramp rate studies. Must be previously defined as a Loadshape
        object. Typically would have time intervals of 1-5 seconds.
        '''
        return self._get_string(self._lib.PVSystems_Get_duty())

    @duty.setter
    def duty(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.PVSystems_Set_duty(Value)
        self.CheckForError()

    @property
    def yearly(self):
        '''
        Dispatch shape to use for yearly simulations. Must be previously defined
        as a Loadshape object. If this is not specified, the Daily dispatch shape,
        if any, is repeated during Yearly solution modes. In the default dispatch
        mode, the PVSystem element uses this loadshape to trigger State changes.
        '''
        return self._get_string(self._lib.PVSystems_Get_yearly())

    @yearly.setter
    def yearly(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.PVSystems_Set_yearly(Value)
        self.CheckForError()
        
    @property
    def Tdaily(self):
        '''
        Temperature shape to use for daily simulations. Must be previously defined
        as a TShape object of 24 hrs, typically. The PVSystem element uses this
        TShape to determine the Pmpp from the Pmpp vs T curve. Units must agree
        with the Pmpp vs T curve.
        '''
        return self._get_string(self._lib.PVSystems_Get_Tdaily())

    @Tdaily.setter
    def Tdaily(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.PVSystems_Set_Tdaily(Value)
        self.CheckForError()

    @property
    def Tduty(self):
        '''
        Temperature shape to use for duty cycle dispatch simulations such as for
        solar ramp rate studies. Must be previously defined as a TShape object.
        Typically would have time intervals of 1-5 seconds. Designate the number
        of points to solve using the Set Number=xxxx command. If there are fewer
        points in the actual shape, the shape is assumed to repeat. The PVSystem
        model uses this TShape to determine the Pmpp from the Pmpp vs T curve.
        Units must agree with the Pmpp vs T curve.
        '''
        return self._get_string(self._lib.PVSystems_Get_Tduty())

    @Tduty.setter
    def Tduty(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.PVSystems_Set_Tduty(Value)
        self.CheckForError()

    @property
    def Tyearly(self):
        '''
        Temperature shape to use for yearly simulations. Must be previously defined
        as a TShape object. If this is not specified, the Daily dispatch shape, if
        any, is repeated during Yearly solution modes. The PVSystem element uses
        this TShape to determine the Pmpp from the Pmpp vs T curve. Units must
        agree with the Pmpp vs T curve.
        '''
        return self._get_string(self._lib.PVSystems_Get_Tyearly())

    @Tyearly.setter
    def Tyearly(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.PVSystems_Set_Tyearly(Value)
        self.CheckForError()
