'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira
Copyright (c) 2018-2022 DSS Extensions contributors
'''
from .._cffi_api_util import Base

class ICtrlQueue(Base):
    __slots__ = []
    
    _columns = [
        'Queue', 
        'DeviceHandle', 
        'QueueSize', 
        'ActionCode', 
        'NumActions',  
    ]

    def ClearActions(self):
        self.CheckForError(self._lib.CtrlQueue_ClearActions())

    def ClearQueue(self):
        self.CheckForError(self._lib.CtrlQueue_ClearQueue())

    def Delete(self, ActionHandle):
        self.CheckForError(self._lib.CtrlQueue_Delete(ActionHandle))

    def DoAllQueue(self):
        self.CheckForError(self._lib.CtrlQueue_DoAllQueue())

    def Show(self):
        self.CheckForError(self._lib.CtrlQueue_Show())

    @property
    def ActionCode(self):
        '''(read-only) Code for the active action. Long integer code to tell the control device what to do'''
        return self.CheckForError(self._lib.CtrlQueue_Get_ActionCode())

    @property
    def DeviceHandle(self):
        '''(read-only) Handle (User defined) to device that must act on the pending action.'''
        return self.CheckForError(self._lib.CtrlQueue_Get_DeviceHandle())

    @property
    def NumActions(self):
        '''(read-only) Number of Actions on the current actionlist (that have been popped off the control queue by CheckControlActions)'''
        return self.CheckForError(self._lib.CtrlQueue_Get_NumActions())

    def Push(self, Hour, Seconds, ActionCode, DeviceHandle):
        '''Push a control action onto the DSS control queue by time, action code, and device handle (user defined). Returns Control Queue handle.'''
        return self.CheckForError(self._lib.CtrlQueue_Push(Hour, Seconds, ActionCode, DeviceHandle))

    @property
    def PopAction(self):
        '''(read-only) Pops next action off the action list and makes it the active action. Returns zero if none.'''
        return self.CheckForError(self._lib.CtrlQueue_Get_PopAction())

    @property
    def Queue(self):
        '''(read-only) Array of strings containing the entire queue in CSV format'''
        return self.CheckForError(self._get_string_array(self._lib.CtrlQueue_Get_Queue))

    @property
    def QueueSize(self):
        '''(read-only) Number of items on the OpenDSS control Queue'''
        return self.CheckForError(self._lib.CtrlQueue_Get_QueueSize())

    @property
    def Action(self):
        '''(write-only) Set the active action by index'''
        raise AttributeError("This property is write-only!")

    @Action.setter
    def Action(self, Param1):
        self.CheckForError(self._lib.CtrlQueue_Set_Action(Param1))

