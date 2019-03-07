'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2019 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Iterable

class ISwtControls(Iterable):
    __slots__ = []

    def Reset(self):
        self._lib.SwtControls_Reset()

    @property
    def Action(self):
        '''Open or Close the switch. No effect if switch is locked.  However, Reset removes any lock and then closes the switch (shelf state).'''
        return self._lib.SwtControls_Get_Action()

    @Action.setter
    def Action(self, Value):
        self._lib.SwtControls_Set_Action(Value)
        self.CheckForError()

    @property
    def Delay(self):
        '''Time delay [s] betwen arming and opening or closing the switch.  Control may reset before actually operating the switch.'''
        return self._lib.SwtControls_Get_Delay()

    @Delay.setter
    def Delay(self, Value):
        self._lib.SwtControls_Set_Delay(Value)
        self.CheckForError()

    @property
    def IsLocked(self):
        '''The lock prevents both manual and automatic switch operation.'''
        return self._lib.SwtControls_Get_IsLocked() != 0

    @IsLocked.setter
    def IsLocked(self, Value):
        self._lib.SwtControls_Set_IsLocked(Value)
        self.CheckForError()

    @property
    def NormalState(self):
        '''
        (read) Get Normal state of switch
        (write) set Normal state of switch  (see actioncodes) dssActionOpen or dssActionClose
        '''
        return self._lib.SwtControls_Get_NormalState()

    @NormalState.setter
    def NormalState(self, Value):
        self._lib.SwtControls_Set_NormalState(Value)
        self.CheckForError()

    @property
    def State(self):
        '''
        (read) Force switch to specified state
        (write) Get Present state of switch
        '''
        return self._lib.SwtControls_Get_State()

    @State.setter
    def State(self, Value):
        self._lib.SwtControls_Set_State(Value)
        self.CheckForError()

    @property
    def SwitchedObj(self):
        '''Full name of the switched element.'''
        return self._get_string(self._lib.SwtControls_Get_SwitchedObj())

    @SwitchedObj.setter
    def SwitchedObj(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.SwtControls_Set_SwitchedObj(Value)
        self.CheckForError()

    @property
    def SwitchedTerm(self):
        '''Terminal number where the switch is located on the SwitchedObj'''
        return self._lib.SwtControls_Get_SwitchedTerm()

    @SwitchedTerm.setter
    def SwitchedTerm(self, Value):
        self._lib.SwtControls_Set_SwitchedTerm(Value)
        self.CheckForError()

