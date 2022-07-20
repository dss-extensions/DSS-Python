'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira
Copyright (c) 2018-2022 DSS Extensions contributors
'''
from .._cffi_api_util import Iterable

class IWireData(Iterable):
    '''Experimental API extension exposing part of the WireData objects'''

    __slots__ = []

    _columns = [
        'Name',
        'idx',
        'NormAmps',
        'EmergAmps',
        'Rdc',
        'Rac',
        'ResistanceUnits',
        'GMRac',
        'GMRUnits',
        'Radius',
        'Diameter',
        'RadiusUnits',
        'CapRadius',
    ]

    @property
    def EmergAmps(self):
        '''Emergency ampere rating'''
        return self.CheckForError(self._lib.WireData_Get_EmergAmps())

    @EmergAmps.setter
    def EmergAmps(self, Value):
        self.CheckForError(self._lib.WireData_Set_EmergAmps(Value))

    @property
    def NormAmps(self):
        '''Normal Ampere rating'''
        return self.CheckForError(self._lib.WireData_Get_NormAmps())

    @NormAmps.setter
    def NormAmps(self, Value):
        self.CheckForError(self._lib.WireData_Set_NormAmps(Value))

    @property
    def Rdc(self):
        return self.CheckForError(self._lib.WireData_Get_Rdc())

    @Rdc.setter
    def Rdc(self, Value):
        self.CheckForError(self._lib.WireData_Set_Rdc(Value))

    @property
    def Rac(self):
        return self.CheckForError(self._lib.WireData_Get_Rac())

    @Rac.setter
    def Rac(self, Value):
        self.CheckForError(self._lib.WireData_Set_Rac(Value))

    @property
    def GMRac(self):
        return self.CheckForError(self._lib.WireData_Get_GMRac())

    @GMRac.setter
    def GMRac(self, Value):
        self.CheckForError(self._lib.WireData_Set_GMRac(Value))

    @property
    def GMRUnits(self):
        return self.CheckForError(self._lib.WireData_Get_GMRUnits())

    @GMRUnits.setter
    def GMRUnits(self, Value):
        self.CheckForError(self._lib.WireData_Set_GMRUnits(Value)) #TODO: use enum

    @property
    def Radius(self):
        return self.CheckForError(self._lib.WireData_Get_Radius())

    @Radius.setter
    def Radius(self, Value):
        self.CheckForError(self._lib.WireData_Set_Radius(Value))

    @property
    def RadiusUnits(self):
        return self.CheckForError(self._lib.WireData_Get_RadiusUnits())

    @RadiusUnits.setter
    def RadiusUnits(self, Value):
        self.CheckForError(self._lib.WireData_Set_RadiusUnits(Value))

    @property
    def ResistanceUnits(self):
        return self.CheckForError(self._lib.WireData_Get_ResistanceUnits()) #TODO: use enum

    @ResistanceUnits.setter
    def ResistanceUnits(self, Value):
        self.CheckForError(self._lib.WireData_Set_ResistanceUnits(Value))

    @property
    def Diameter(self):
        return self.CheckForError(self._lib.WireData_Get_Diameter())

    @Diameter.setter
    def Diameter(self, Value):
        self.CheckForError(self._lib.WireData_Set_Diameter(Value))

    @property
    def CapRadius(self):
        '''Equivalent conductor radius for capacitance calcs. Specify this for bundled conductors. Defaults to same value as radius.'''
        return self.CheckForError(self._lib.WireData_Get_CapRadius())

    @CapRadius.setter
    def CapRadius(self, Value):
        self.CheckForError(self._lib.WireData_Set_CapRadius(Value))
