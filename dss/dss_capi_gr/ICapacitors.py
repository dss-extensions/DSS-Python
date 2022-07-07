'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira
Copyright (c) 2018-2022 DSS Extensions contributors
'''
from .._cffi_api_util import Iterable

class ICapacitors(Iterable):
    __slots__ = []

    _columns = [
        'Name',
        'idx',
        'kV',
        'NumSteps',
        'AvailableSteps',
        'IsDelta',
        'States',
        'kvar',
    ]

    def AddStep(self):
        return self.CheckForError(self._lib.Capacitors_AddStep()) != 0

    def Close(self):
        self.CheckForError(self._lib.Capacitors_Close())

    def Open(self):
        self.CheckForError(self._lib.Capacitors_Open())

    def SubtractStep(self):
        return self.CheckForError(self._lib.Capacitors_SubtractStep()) != 0

    @property
    def AvailableSteps(self):
        '''(read-only) Number of Steps available in cap bank to be switched ON.'''
        return self.CheckForError(self._lib.Capacitors_Get_AvailableSteps())

    @property
    def IsDelta(self):
        '''Delta connection or wye?'''
        return self.CheckForError(self._lib.Capacitors_Get_IsDelta()) != 0

    @IsDelta.setter
    def IsDelta(self, Value):
        self.CheckForError(self._lib.Capacitors_Set_IsDelta(Value))

    @property
    def NumSteps(self):
        '''Number of steps (default 1) for distributing and switching the total bank kVAR.'''
        return self.CheckForError(self._lib.Capacitors_Get_NumSteps())

    @NumSteps.setter
    def NumSteps(self, Value):
        self.CheckForError(self._lib.Capacitors_Set_NumSteps(Value))

    @property
    def States(self):
        '''A array of  integer [0..numsteps-1] indicating state of each step. If the read value is -1 an error has occurred.'''
        self.CheckForError(self._lib.Capacitors_Get_States_GR())
        return self._get_int32_gr_array()

    @States.setter
    def States(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)
        self.CheckForError(self._lib.Capacitors_Set_States(ValuePtr, ValueCount))

    @property
    def kV(self):
        '''Bank kV rating. Use LL for 2 or 3 phases, or actual can rating for 1 phase.'''
        return self.CheckForError(self._lib.Capacitors_Get_kV())

    @kV.setter
    def kV(self, Value):
        self.CheckForError(self._lib.Capacitors_Set_kV(Value))

    @property
    def kvar(self):
        '''Total bank KVAR, distributed equally among phases and steps.'''
        return self.CheckForError(self._lib.Capacitors_Get_kvar())

    @kvar.setter
    def kvar(self, Value):
        self.CheckForError(self._lib.Capacitors_Set_kvar(Value))
