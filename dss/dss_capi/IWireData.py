'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class IWireData(Base):
    '''Experimental API extension exposing part of the WireData objects'''

    __slots__ = []

    @property
    def AllNames(self):
        '''(read-only) Array of strings with names of all devices'''
        return self.get_string_array(self.lib.WireData_Get_AllNames)

    @property
    def Count(self):
        '''(read-only) Number of WireData'''
        return self.lib.WireData_Get_Count()

    @property
    def First(self):
        return self.lib.WireData_Get_First()

    @property
    def Next(self):
        return self.lib.WireData_Get_Next()

    @property
    def Name(self):
        '''Name of active WireData'''
        return self.get_string(self.lib.WireData_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.WireData_Set_Name(Value)

    def __len__(self):
        return self.lib.WireData_Get_Count()

    @property
    def EmergAmps(self):
        '''Emergency ampere rating'''
        return self.lib.WireData_Get_EmergAmps()

    @EmergAmps.setter
    def EmergAmps(self, Value):
        self.lib.WireData_Set_EmergAmps(Value)

    @property
    def NormAmps(self):
        '''Normal Ampere rating'''
        return self.lib.WireData_Get_NormAmps()

    @NormAmps.setter
    def NormAmps(self, Value):
        self.lib.WireData_Set_NormAmps(Value)

    @property
    def Rdc(self):
        return self.lib.WireData_Get_Rdc()

    @Rdc.setter
    def Rdc(self, Value):
        self.lib.WireData_Set_Rdc(Value)

    @property
    def Rac(self):
        return self.lib.WireData_Get_Rac()

    @Rac.setter
    def Rac(self, Value):
        self.lib.WireData_Set_Rac(Value)

    @property
    def GMRac(self):
        return self.lib.WireData_Get_GMRac()

    @GMRac.setter
    def GMRac(self, Value):
        self.lib.WireData_Set_GMRac(Value)

    @property
    def GMRUnits(self):
        return self.lib.WireData_Get_GMRUnits()

    @GMRUnits.setter
    def GMRUnits(self, Value):
        self.lib.WireData_Set_GMRUnits(Value)

    @property
    def Radius(self):
        return self.lib.WireData_Get_Radius()

    @Radius.setter
    def Radius(self, Value):
        self.lib.WireData_Set_Radius(Value)

    @property
    def RadiusUnits(self):
        return self.lib.WireData_Get_RadiusUnits()

    @RadiusUnits.setter
    def RadiusUnits(self, Value):
        self.lib.WireData_Set_RadiusUnits(Value)

    @property
    def ResistanceUnits(self):
        return self.lib.WireData_Get_ResistanceUnits()

    @ResistanceUnits.setter
    def ResistanceUnits(self, Value):
        self.lib.WireData_Set_ResistanceUnits(Value)

    @property
    def Diameter(self):
        return self.lib.WireData_Get_Diameter()

    @Diameter.setter
    def Diameter(self, Value):
        self.lib.WireData_Set_Diameter(Value)

    def __iter__(self):
        idx = self.First
        while idx != 0:
            yield self
            idx = self.Next

