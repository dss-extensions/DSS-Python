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

