'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class ICNData(Base):
    '''Experimental API extension exposing CNData objects'''

    __slots__ = []

    @property
    def AllNames(self):
        '''(read-only) Array of strings with names of all devices'''
        return self._get_string_array(self._lib.CNData_Get_AllNames)

    @property
    def Conductors(self):
        '''(read-only) Array of strings with names of all conductors in the active CNData object'''
        return self._get_string_array(self._lib.CNData_Get_Conductors)

    @property
    def Count(self):
        '''(read-only) Number of CNData'''
        return self._lib.CNData_Get_Count()

    @property
    def First(self):
        return self._lib.CNData_Get_First()

    @property
    def Next(self):
        return self._lib.CNData_Get_Next()

    @property
    def Name(self):
        '''Name of active CNData'''
        return self._get_string(self._lib.CNData_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.CNData_Set_Name(Value)
        self.CheckForError()

    def __len__(self):
        return self._lib.CNData_Get_Count()

    def __iter__(self):
        idx = self.First
        while idx != 0:
            yield self
            idx = self.Next

    @property
    def EmergAmps(self):
        '''Emergency ampere rating'''
        return self._lib.CNData_Get_EmergAmps()

    @EmergAmps.setter
    def EmergAmps(self, Value):
        self._lib.CNData_Set_EmergAmps(Value)
        self.CheckForError()

    @property
    def NormAmps(self):
        '''Normal Ampere rating'''
        return self._lib.CNData_Get_NormAmps()

    @NormAmps.setter
    def NormAmps(self, Value):
        self._lib.CNData_Set_NormAmps(Value)
        self.CheckForError()

    @property
    def Rdc(self):
        return self._lib.CNData_Get_Rdc()

    @Rdc.setter
    def Rdc(self, Value):
        self._lib.CNData_Set_Rdc(Value)
        self.CheckForError()

    @property
    def Rac(self):
        return self._lib.CNData_Get_Rac()

    @Rac.setter
    def Rac(self, Value):
        self._lib.CNData_Set_Rac(Value)
        self.CheckForError()

    @property
    def GMRac(self):
        return self._lib.CNData_Get_GMRac()

    @GMRac.setter
    def GMRac(self, Value):
        self._lib.CNData_Set_GMRac(Value)
        self.CheckForError()

    @property
    def GMRUnits(self):
        return self._lib.CNData_Get_GMRUnits()

    @GMRUnits.setter
    def GMRUnits(self, Value):
        self._lib.CNData_Set_GMRUnits(Value)
        self.CheckForError()

    @property
    def Radius(self):
        return self._lib.CNData_Get_Radius()

    @Radius.setter
    def Radius(self, Value):
        self._lib.CNData_Set_Radius(Value)
        self.CheckForError()

    @property
    def RadiusUnits(self):
        return self._lib.CNData_Get_RadiusUnits()

    @RadiusUnits.setter
    def RadiusUnits(self, Value):
        self._lib.CNData_Set_RadiusUnits(Value)
        self.CheckForError()

    @property
    def ResistanceUnits(self):
        return self._lib.CNData_Get_ResistanceUnits()

    @ResistanceUnits.setter
    def ResistanceUnits(self, Value):
        self._lib.CNData_Set_ResistanceUnits(Value)
        self.CheckForError()

    @property
    def Diameter(self):
        return self._lib.CNData_Get_Diameter()

    @Diameter.setter
    def Diameter(self, Value):
        self._lib.CNData_Set_Diameter(Value)
        self.CheckForError()

    @property
    def EpsR(self):
        return self._lib.CNData_Get_EpsR()

    @EpsR.setter
    def EpsR(self, Value):
        self._lib.CNData_Set_EpsR(Value)
        self.CheckForError()

    @property
    def InsLayer(self):
        return self._lib.CNData_Get_InsLayer()

    @InsLayer.setter
    def InsLayer(self, Value):
        self._lib.CNData_Set_InsLayer(Value)
        self.CheckForError()

    @property
    def DiaIns(self):
        return self._lib.CNData_Get_DiaIns()

    @DiaIns.setter
    def DiaIns(self, Value):
        self._lib.CNData_Set_DiaIns(Value)
        self.CheckForError()

    @property
    def DiaCable(self):
        return self._lib.CNData_Get_DiaCable()

    @DiaCable.setter
    def DiaCable(self, Value):
        self._lib.CNData_Set_DiaCable(Value)
        self.CheckForError()

    @property
    def k(self):
        return self._lib.CNData_Get_k()

    @k.setter
    def k(self, Value):
        self._lib.CNData_Set_k(Value)
        self.CheckForError()

    @property
    def DiaStrand(self):
        return self._lib.CNData_Get_DiaStrand()

    @DiaStrand.setter
    def DiaStrand(self, Value):
        self._lib.CNData_Set_DiaStrand(Value)
        self.CheckForError()

    @property
    def GmrStrand(self):
        return self._lib.CNData_Get_GmrStrand()

    @GmrStrand.setter
    def GmrStrand(self, Value):
        self._lib.CNData_Set_GmrStrand(Value)
        self.CheckForError()

    @property
    def RStrand(self):
        return self._lib.CNData_Get_RStrand()

    @RStrand.setter
    def RStrand(self, Value):
        self._lib.CNData_Set_RStrand(Value)
        self.CheckForError()


