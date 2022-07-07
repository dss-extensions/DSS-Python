'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira
Copyright (c) 2018-2022 DSS Extensions contributors
'''
from .._cffi_api_util import Iterable

class ICNData(Iterable):
    '''Experimental API extension exposing CNData objects'''
    
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
        'EpsR',
        'InsLayer',
        'DiaIns',
        'DiaCable',
        'DiaStrand',
        'RStrand',
        'k',
    ]

    @property
    def EmergAmps(self):
        '''Emergency ampere rating'''
        return self.CheckForError(self._lib.CNData_Get_EmergAmps())

    @EmergAmps.setter
    def EmergAmps(self, Value):
        self.CheckForError(self._lib.CNData_Set_EmergAmps(Value))

    @property
    def NormAmps(self):
        '''Normal Ampere rating'''
        return self.CheckForError(self._lib.CNData_Get_NormAmps())

    @NormAmps.setter
    def NormAmps(self, Value):
        self.CheckForError(self._lib.CNData_Set_NormAmps(Value))

    @property
    def Rdc(self):
        return self.CheckForError(self._lib.CNData_Get_Rdc())

    @Rdc.setter
    def Rdc(self, Value):
        self.CheckForError(self._lib.CNData_Set_Rdc(Value))

    @property
    def Rac(self):
        return self.CheckForError(self._lib.CNData_Get_Rac())

    @Rac.setter
    def Rac(self, Value):
        self.CheckForError(self._lib.CNData_Set_Rac(Value))

    @property
    def GMRac(self):
        return self.CheckForError(self._lib.CNData_Get_GMRac())

    @GMRac.setter
    def GMRac(self, Value):
        self.CheckForError(self._lib.CNData_Set_GMRac(Value))

    @property
    def GMRUnits(self):
        return self.CheckForError(self._lib.CNData_Get_GMRUnits()) #TODO: use enum

    @GMRUnits.setter
    def GMRUnits(self, Value):
        self.CheckForError(self._lib.CNData_Set_GMRUnits(Value))

    @property
    def Radius(self):
        return self.CheckForError(self._lib.CNData_Get_Radius())

    @Radius.setter
    def Radius(self, Value):
        self.CheckForError(self._lib.CNData_Set_Radius(Value))

    @property
    def RadiusUnits(self):
        return self.CheckForError(self._lib.CNData_Get_RadiusUnits()) #TODO: use enum

    @RadiusUnits.setter
    def RadiusUnits(self, Value):
        self.CheckForError(self._lib.CNData_Set_RadiusUnits(Value))

    @property
    def ResistanceUnits(self):
        return self.CheckForError(self._lib.CNData_Get_ResistanceUnits()) #TODO: use enum

    @ResistanceUnits.setter
    def ResistanceUnits(self, Value):
        self.CheckForError(self._lib.CNData_Set_ResistanceUnits(Value))

    @property
    def Diameter(self):
        return self.CheckForError(self._lib.CNData_Get_Diameter())

    @Diameter.setter
    def Diameter(self, Value):
        self.CheckForError(self._lib.CNData_Set_Diameter(Value))

    @property
    def EpsR(self):
        return self.CheckForError(self._lib.CNData_Get_EpsR())

    @EpsR.setter
    def EpsR(self, Value):
        self.CheckForError(self._lib.CNData_Set_EpsR(Value))

    @property
    def InsLayer(self):
        return self.CheckForError(self._lib.CNData_Get_InsLayer())

    @InsLayer.setter
    def InsLayer(self, Value):
        self.CheckForError(self._lib.CNData_Set_InsLayer(Value))

    @property
    def DiaIns(self):
        return self.CheckForError(self._lib.CNData_Get_DiaIns())

    @DiaIns.setter
    def DiaIns(self, Value):
        self.CheckForError(self._lib.CNData_Set_DiaIns(Value))

    @property
    def DiaCable(self):
        return self.CheckForError(self._lib.CNData_Get_DiaCable())

    @DiaCable.setter
    def DiaCable(self, Value):
        self.CheckForError(self._lib.CNData_Set_DiaCable(Value))

    @property
    def k(self):
        return self.CheckForError(self._lib.CNData_Get_k())

    @k.setter
    def k(self, Value):
        self.CheckForError(self._lib.CNData_Set_k(Value))

    @property
    def DiaStrand(self):
        return self.CheckForError(self._lib.CNData_Get_DiaStrand())

    @DiaStrand.setter
    def DiaStrand(self, Value):
        self.CheckForError(self._lib.CNData_Set_DiaStrand(Value))

    @property
    def GmrStrand(self):
        return self.CheckForError(self._lib.CNData_Get_GmrStrand())

    @GmrStrand.setter
    def GmrStrand(self, Value):
        self.CheckForError(self._lib.CNData_Set_GmrStrand(Value))

    @property
    def RStrand(self):
        return self.CheckForError(self._lib.CNData_Get_RStrand())

    @RStrand.setter
    def RStrand(self, Value):
        self.CheckForError(self._lib.CNData_Set_RStrand(Value))


