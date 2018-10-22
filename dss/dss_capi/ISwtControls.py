'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class ISwtControls(Base):
    __slots__ = []

    def Reset(self):
        self.lib.SwtControls_Reset()

    @property
    def Action(self):
        '''Open or Close the switch. No effect if switch is locked.  However, Reset removes any lock and then closes the switch (shelf state).'''
        return self.lib.SwtControls_Get_Action()

    @Action.setter
    def Action(self, Value):
        self.lib.SwtControls_Set_Action(Value)

    @property
    def AllNames(self):
        '''(read-only) Array of strings with all SwtControl names in the active circuit.'''
        return self.get_string_array(self.lib.SwtControls_Get_AllNames)

    @property
    def Count(self):
        return self.lib.SwtControls_Get_Count()

    def __len__(self):
        return self.lib.SwtControls_Get_Count()

    @property
    def Delay(self):
        '''Time delay [s] betwen arming and opening or closing the switch.  Control may reset before actually operating the switch.'''
        return self.lib.SwtControls_Get_Delay()

    @Delay.setter
    def Delay(self, Value):
        self.lib.SwtControls_Set_Delay(Value)

    @property
    def First(self):
        '''(read-only) Sets the first SwtControl active. Returns 0 if no more.'''
        return self.lib.SwtControls_Get_First()

    @property
    def IsLocked(self):
        '''The lock prevents both manual and automatic switch operation.'''
        return self.lib.SwtControls_Get_IsLocked() != 0

    @IsLocked.setter
    def IsLocked(self, Value):
        self.lib.SwtControls_Set_IsLocked(Value)

    @property
    def Name(self):
        '''Sets a SwtControl active by Name.'''
        return self.get_string(self.lib.SwtControls_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.SwtControls_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Sets the next SwtControl active. Returns 0 if no more.'''
        return self.lib.SwtControls_Get_Next()

    @property
    def NormalState(self):
        '''
        (read) Get Normal state of switch
        (write) set Normal state of switch  (see actioncodes) dssActionOpen or dssActionClose
        '''
        return self.lib.SwtControls_Get_NormalState()

    @NormalState.setter
    def NormalState(self, Value):
        self.lib.SwtControls_Set_NormalState(Value)

    @property
    def State(self):
        '''
        (read) Force switch to specified state
        (write) Get Present state of switch
        '''
        return self.lib.SwtControls_Get_State()

    @State.setter
    def State(self, Value):
        self.lib.SwtControls_Set_State(Value)

    @property
    def SwitchedObj(self):
        '''Full name of the switched element.'''
        return self.get_string(self.lib.SwtControls_Get_SwitchedObj())

    @SwitchedObj.setter
    def SwitchedObj(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.SwtControls_Set_SwitchedObj(Value)

    @property
    def SwitchedTerm(self):
        '''Terminal number where the switch is located on the SwitchedObj'''
        return self.lib.SwtControls_Get_SwitchedTerm()

    @SwitchedTerm.setter
    def SwitchedTerm(self, Value):
        self.lib.SwtControls_Set_SwitchedTerm(Value)

    def __iter__(self):
        idx = self.First
        while idx != 0:
            yield self
            idx = self.Next


