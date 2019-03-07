'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2019 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Iterable

class IWireData(Iterable):
    '''Experimental API extension exposing part of the WireData objects'''

    __slots__ = []

    @property
    def EmergAmps(self):
        '''Emergency ampere rating'''
        return self._lib.WireData_Get_EmergAmps()

    @EmergAmps.setter
    def EmergAmps(self, Value):
        self._lib.WireData_Set_EmergAmps(Value)
        self.CheckForError()

    @property
    def NormAmps(self):
        '''Normal Ampere rating'''
        return self._lib.WireData_Get_NormAmps()

    @NormAmps.setter
    def NormAmps(self, Value):
        self._lib.WireData_Set_NormAmps(Value)
        self.CheckForError()

    @property
    def Rdc(self):
        return self._lib.WireData_Get_Rdc()

    @Rdc.setter
    def Rdc(self, Value):
        self._lib.WireData_Set_Rdc(Value)
        self.CheckForError()

    @property
    def Rac(self):
        return self._lib.WireData_Get_Rac()

    @Rac.setter
    def Rac(self, Value):
        self._lib.WireData_Set_Rac(Value)
        self.CheckForError()

    @property
    def GMRac(self):
        return self._lib.WireData_Get_GMRac()

    @GMRac.setter
    def GMRac(self, Value):
        self._lib.WireData_Set_GMRac(Value)
        self.CheckForError()

    @property
    def GMRUnits(self):
        return self._lib.WireData_Get_GMRUnits()

    @GMRUnits.setter
    def GMRUnits(self, Value):
        self._lib.WireData_Set_GMRUnits(Value)
        self.CheckForError()

    @property
    def Radius(self):
        return self._lib.WireData_Get_Radius()

    @Radius.setter
    def Radius(self, Value):
        self._lib.WireData_Set_Radius(Value)
        self.CheckForError()

    @property
    def RadiusUnits(self):
        return self._lib.WireData_Get_RadiusUnits()

    @RadiusUnits.setter
    def RadiusUnits(self, Value):
        self._lib.WireData_Set_RadiusUnits(Value)
        self.CheckForError()

    @property
    def ResistanceUnits(self):
        return self._lib.WireData_Get_ResistanceUnits()

    @ResistanceUnits.setter
    def ResistanceUnits(self, Value):
        self._lib.WireData_Set_ResistanceUnits(Value)
        self.CheckForError()

    @property
    def Diameter(self):
        return self._lib.WireData_Get_Diameter()

    @Diameter.setter
    def Diameter(self, Value):
        self._lib.WireData_Set_Diameter(Value)
        self.CheckForError()
