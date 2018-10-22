'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class ICtrlQueue(Base):
    __slots__ = []

    def ClearActions(self):
        self.lib.CtrlQueue_ClearActions()

    def ClearQueue(self):
        self.lib.CtrlQueue_ClearQueue()

    def Delete(self, ActionHandle):
        self.lib.CtrlQueue_Delete(ActionHandle)

    def DoAllQueue(self):
        self.lib.CtrlQueue_DoAllQueue()

    def Show(self):
        self.lib.CtrlQueue_Show()

    @property
    def ActionCode(self):
        '''(read-only) Code for the active action. Long integer code to tell the control device what to do'''
        return self.lib.CtrlQueue_Get_ActionCode()

    @property
    def DeviceHandle(self):
        '''(read-only) Handle (User defined) to device that must act on the pending action.'''
        return self.lib.CtrlQueue_Get_DeviceHandle()

    @property
    def NumActions(self):
        '''(read-only) Number of Actions on the current actionlist (that have been popped off the control queue by CheckControlActions)'''
        return self.lib.CtrlQueue_Get_NumActions()

    @property
    def PopAction(self):
        '''(read-only) Pops next action off the action list and makes it the active action. Returns zero if none.'''
        return self.lib.CtrlQueue_Get_PopAction()

    @property
    def Queue(self):
        '''(read-only) Array of strings containing the entire queue in CSV format'''
        return self.get_string_array(self.lib.CtrlQueue_Get_Queue)

    @property
    def QueueSize(self):
        '''(read-only) Number of items on the OpenDSS control Queue'''
        return self.lib.CtrlQueue_Get_QueueSize()

    @property
    def Action(self):
        '''(write-only) Set the active action by index'''
        raise AttributeError("This property is write-only!")

    @Action.setter
    def Action(self, Param1):
        self.lib.CtrlQueue_Set_Action(Param1)

