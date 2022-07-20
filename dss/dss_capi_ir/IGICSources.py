'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2022 Paulo Meira
Copyright (c) 2022 DSS Extensions contributors
'''
from .._cffi_api_util import Iterable

class IGICSources(Iterable):
    __slots__ = []

    _columns = [
        'Name',
        'idx',
        'Phases',
        'Bus1',
        'Bus2',
        'EN',
        'EE',
        'Lat1',
        'Lat2',
        'Lon1',
        'Lon2',
        'Volts',
    ]

    @property
    def Bus1(self):
        '''First bus name of GICSource (Created name)'''
        return self._get_string(self.CheckForError(self._lib.GICSources_Get_Bus1()))

    @property
    def Bus2(self):
        '''Second bus name'''
        return self._get_string(self.CheckForError(self._lib.GICSources_Get_Bus2()))

    @property
    def Phases(self):
        '''Number of Phases, this GICSource element.'''
        return self.CheckForError(self._lib.GICSources_Get_Phases())

    @Phases.setter
    def Phases(self, Value):
        self.CheckForError(self._lib.GICSources_Set_Phases(Value))

    @property
    def EN(self):
        '''Northward E Field V/km'''
        return self.CheckForError(self._lib.GICSources_Get_EN())

    @EN.setter
    def EN(self, Value):
        self.CheckForError(self._lib.GICSources_Set_EN(Value))

    @property
    def EE(self):
        '''Eastward E Field, V/km'''
        return self.CheckForError(self._lib.GICSources_Get_EE())

    @EE.setter
    def EE(self, Value):
        self.CheckForError(self._lib.GICSources_Set_EE(Value))

    @property
    def Lat1(self):
        '''Latitude of Bus1 (degrees)'''
        return self.CheckForError(self._lib.GICSources_Get_Lat1())

    @Lat1.setter
    def Lat1(self, Value):
        self.CheckForError(self._lib.GICSources_Set_Lat1(Value))

    @property
    def Lat2(self):
        '''Latitude of Bus2 (degrees)'''
        return self.CheckForError(self._lib.GICSources_Get_Lat2())

    @Lat2.setter
    def Lat2(self, Value):
        self.CheckForError(self._lib.GICSources_Set_Lat2(Value))

    @property
    def Lon1(self):
        '''Longitude of Bus1 (Degrees)'''
        return self.CheckForError(self._lib.GICSources_Get_Lon1())

    @Lon1.setter
    def Lon1(self, Value):
        self.CheckForError(self._lib.GICSources_Set_Lon1(Value))

    @property
    def Lon2(self):
        '''Longitude of Bus2 (Degrees)'''
        return self.CheckForError(self._lib.GICSources_Get_Lon2())

    @Lon2.setter
    def Lon2(self, Value):
        self.CheckForError(self._lib.GICSources_Set_Lon2(Value))

    @property
    def Volts(self):
        '''Specify dc voltage directly'''
        return self.CheckForError(self._lib.GICSources_Get_Volts())

    @Volts.setter
    def Volts(self, Value):
        self.CheckForError(self._lib.GICSources_Set_Volts(Value))
