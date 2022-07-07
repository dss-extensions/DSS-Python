'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira
Copyright (c) 2018-2022 DSS Extensions contributors
'''
from .._cffi_api_util import Iterable

class ISwtControls(Iterable):
    __slots__ = []

    _columns = [
        'Name',
        'idx',
        'Action',
        'Delay',
        'IsLocked',
        'NormalState',
        'State',
        'SwitchedObj',
        'SwitchedTerm',
    ]

    def Reset(self):
        self.CheckForError(self._lib.SwtControls_Reset())

    @property
    def Action(self):
        '''Open or Close the switch. No effect if switch is locked.  However, Reset removes any lock and then closes the switch (shelf state).'''
        return self.CheckForError(self._lib.SwtControls_Get_Action())

    @Action.setter
    def Action(self, Value):
        self.CheckForError(self._lib.SwtControls_Set_Action(Value))

    @property
    def Delay(self):
        '''Time delay [s] betwen arming and opening or closing the switch.  Control may reset before actually operating the switch.'''
        return self.CheckForError(self._lib.SwtControls_Get_Delay())

    @Delay.setter
    def Delay(self, Value):
        self.CheckForError(self._lib.SwtControls_Set_Delay(Value))

    @property
    def IsLocked(self):
        '''The lock prevents both manual and automatic switch operation.'''
        return self.CheckForError(self._lib.SwtControls_Get_IsLocked()) != 0

    @IsLocked.setter
    def IsLocked(self, Value):
        self.CheckForError(self._lib.SwtControls_Set_IsLocked(Value))

    @property
    def NormalState(self):
        '''
        Get/set Normal state of switch (see actioncodes) dssActionOpen or dssActionClose
        '''
        return self.CheckForError(self._lib.SwtControls_Get_NormalState()) #TODO: use enum

    @NormalState.setter
    def NormalState(self, Value):
        self.CheckForError(self._lib.SwtControls_Set_NormalState(Value))

    @property
    def State(self):
        '''Set it to force the switch to a specified state, otherwise read its present state.'''
        return self.CheckForError(self._lib.SwtControls_Get_State())

    @State.setter
    def State(self, Value):
        self.CheckForError(self._lib.SwtControls_Set_State(Value))

    @property
    def SwitchedObj(self):
        '''Full name of the switched element.'''
        return self._get_string(self.CheckForError(self._lib.SwtControls_Get_SwitchedObj()))

    @SwitchedObj.setter
    def SwitchedObj(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.SwtControls_Set_SwitchedObj(Value))

    @property
    def SwitchedTerm(self):
        '''Terminal number where the switch is located on the SwitchedObj'''
        return self.CheckForError(self._lib.SwtControls_Get_SwitchedTerm())

    @SwitchedTerm.setter
    def SwitchedTerm(self, Value):
        self.CheckForError(self._lib.SwtControls_Set_SwitchedTerm(Value))

