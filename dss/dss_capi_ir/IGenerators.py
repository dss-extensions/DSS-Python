'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira
Copyright (c) 2018-2022 DSS Extensions contributors
'''
from .._cffi_api_util import Iterable

class IGenerators(Iterable):
    __slots__ = []

    _columns = [
        'Name',
        'idx',
        'ForcedON',
        'Model',
        'Phases',
        'PF',
        'kVArated',
        'kV',
        'kW',
        'kvar',
        'Vminpu',
        'Vmaxpu',
        'RegisterNames',
        'RegisterValues',
        'Bus1',
        'Class',
        'kva',
        'IsDelta',
        'Status',
        'daily',
        'duty',
        'Yearly',
    ]

    @property
    def ForcedON(self):
        '''Indicates whether the generator is forced ON regardles of other dispatch criteria.'''
        return self.CheckForError(self._lib.Generators_Get_ForcedON()) != 0

    @ForcedON.setter
    def ForcedON(self, Value):
        self.CheckForError(self._lib.Generators_Set_ForcedON(Value))

    @property
    def Model(self):
        '''Generator Model'''
        return self.CheckForError(self._lib.Generators_Get_Model()) #TODO: use enum

    @Model.setter
    def Model(self, Value):
        self.CheckForError(self._lib.Generators_Set_Model(Value))

    @property
    def PF(self):
        '''Power factor (pos. = producing vars). Updates kvar based on present kW value.'''
        return self.CheckForError(self._lib.Generators_Get_PF())

    @PF.setter
    def PF(self, Value):
        self.CheckForError(self._lib.Generators_Set_PF(Value))

    @property
    def Phases(self):
        '''Number of phases'''
        return self.CheckForError(self._lib.Generators_Get_Phases())

    @Phases.setter
    def Phases(self, Value):
        self.CheckForError(self._lib.Generators_Set_Phases(Value))

    @property
    def RegisterNames(self):
        '''(read-only) Array of Names of all generator energy meter registers'''
        return self.CheckForError(self._get_string_array(self._lib.Generators_Get_RegisterNames))

    @property
    def RegisterValues(self):
        '''(read-only) Array of valus in generator energy meter registers.'''
        return self._get_float64_array(self._lib.Generators_Get_RegisterValues)

    @property
    def Vmaxpu(self):
        '''Vmaxpu for generator model'''
        return self.CheckForError(self._lib.Generators_Get_Vmaxpu())

    @Vmaxpu.setter
    def Vmaxpu(self, Value):
        self.CheckForError(self._lib.Generators_Set_Vmaxpu(Value))

    @property
    def Vminpu(self):
        '''Vminpu for Generator model'''
        return self.CheckForError(self._lib.Generators_Get_Vminpu())

    @Vminpu.setter
    def Vminpu(self, Value):
        self.CheckForError(self._lib.Generators_Set_Vminpu(Value))

    @property
    def kV(self):
        '''Voltage base for the active generator, kV'''
        return self.CheckForError(self._lib.Generators_Get_kV())

    @kV.setter
    def kV(self, Value):
        self.CheckForError(self._lib.Generators_Set_kV(Value))

    @property
    def kVArated(self):
        '''kVA rating of the generator'''
        return self.CheckForError(self._lib.Generators_Get_kVArated())

    @kVArated.setter
    def kVArated(self, Value):
        self.CheckForError(self._lib.Generators_Set_kVArated(Value))

    @property
    def kW(self):
        '''kW output for the active generator. kvar is updated for current power factor.'''
        return self.CheckForError(self._lib.Generators_Get_kW())

    @kW.setter
    def kW(self, Value):
        self.CheckForError(self._lib.Generators_Set_kW(Value))

    @property
    def kvar(self):
        '''kvar output for the active generator. Updates power factor based on present kW value.'''
        return self.CheckForError(self._lib.Generators_Get_kvar())

    @kvar.setter
    def kvar(self, Value):
        self.CheckForError(self._lib.Generators_Set_kvar(Value))

    @property
    def daily(self):
        '''
        Name of the loadshape for a daily generation profile.

        (API Extension)
        '''
        return self._get_string(self.CheckForError(self._lib.Generators_Get_daily()))

    @daily.setter
    def daily(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Generators_Set_daily(Value))

    @property
    def duty(self):
        '''
        Name of the loadshape for a duty cycle simulation.

        (API Extension)
        '''
        return self._get_string(self.CheckForError(self._lib.Generators_Get_duty()))

    @duty.setter
    def duty(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Generators_Set_duty(Value))

    @property
    def Yearly(self):
        '''
        Name of yearly loadshape

        (API Extension)
        '''
        return self._get_string(self.CheckForError(self._lib.Generators_Get_Yearly()))

    @Yearly.setter
    def Yearly(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Generators_Set_Yearly(Value))

    @property
    def Status(self):
        '''
        Response to dispatch multipliers: Fixed=1 (dispatch multipliers do not apply), Variable=0 (follows curves).

        Related enumeration: GeneratorStatus

        (API Extension)
        '''
        return self.CheckForError(self._lib.Generators_Get_Status()) #TODO: use enum

    @Status.setter
    def Status(self, Value):
        self.CheckForError(self._lib.Generators_Set_Status(Value))

    @property
    def IsDelta(self):
        '''
        Generator connection. True/1 if delta connection, False/0 if wye.

        (API Extension)
        '''
        return self.CheckForError(self._lib.Generators_Get_IsDelta()) != 0

    @IsDelta.setter
    def IsDelta(self, Value):
        self.CheckForError(self._lib.Generators_Set_IsDelta(Value))

    @property
    def kva(self):
        '''
        kVA rating of electrical machine. Applied to machine or inverter definition for Dynamics mode solutions.

        (API Extension)
        '''
        return self.CheckForError(self._lib.Generators_Get_kva())

    @kva.setter
    def kva(self, Value):
        self.CheckForError(self._lib.Generators_Set_kva(Value))

    @property
    def Class(self):
        '''
        An arbitrary integer number representing the class of Generator so that Generator values may be segregated by class.

        (API Extension)
        '''
        return self.CheckForError(self._lib.Generators_Get_Class_())

    @Class.setter
    def Class(self, Value):
        self.CheckForError(self._lib.Generators_Set_Class_(Value))

    @property
    def Bus1(self):
        '''
        Bus to which the Generator is connected. May include specific node specification.

        (API Extension)
        '''
        return self._get_string(self.CheckForError(self._lib.Generators_Get_Bus1()))

    @Bus1.setter
    def Bus1(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Generators_Set_Bus1(Value))

