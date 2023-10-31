'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira

Copyright (c) 2018-2022 DSS-Extensions contributors
'''
from .common import Base
from typing import List

class IControlQueue(Base):
    __slots__ = []
    
    _columns = [
        'Queue', 
        'DeviceHandle', 
        'QueueSize', 
        'ActionCode', 
        'NumActions',  
    ]

    def ClearActions(self):
        self._check_for_error(self._lib.CtrlQueue_ClearActions())

    def ClearQueue(self):
        self._check_for_error(self._lib.CtrlQueue_ClearQueue())

    def Delete(self, ActionHandle):
        self._check_for_error(self._lib.CtrlQueue_Delete(ActionHandle))

    def DoAllQueue(self):
        self._check_for_error(self._lib.CtrlQueue_DoAllQueue())

    def Show(self):
        self._check_for_error(self._lib.CtrlQueue_Show())

    @property
    def ActionCode(self) -> int:
        '''Code for the active action. Long integer code to tell the control device what to do'''
        return self._check_for_error(self._lib.CtrlQueue_Get_ActionCode())

    @property
    def DeviceHandle(self) -> int:
        '''Handle (User defined) to device that must act on the pending action.'''
        return self._check_for_error(self._lib.CtrlQueue_Get_DeviceHandle())

    @property
    def NumActions(self) -> int:
        '''Number of Actions on the current actionlist (that have been popped off the control queue by CheckControlActions)'''
        return self._check_for_error(self._lib.CtrlQueue_Get_NumActions())

    def Push(self, Hour: int, Seconds: float, ActionCode: int, DeviceHandle: int):
        '''Push a control action onto the DSS control queue by time, action code, and device handle (user defined). Returns Control Queue handle.'''
        return self._check_for_error(self._lib.CtrlQueue_Push(Hour, Seconds, ActionCode, DeviceHandle))

    @property
    def PopAction(self) -> int:
        '''Pops next action off the action list and makes it the active action. Returns zero if none.'''
        return self._check_for_error(self._lib.CtrlQueue_Get_PopAction())

    @property
    def Queue(self) -> List[str]:
        '''Array of strings containing the entire queue in CSV format'''
        return self._check_for_error(self._get_string_array(self._lib.CtrlQueue_Get_Queue))

    @property
    def QueueSize(self) -> int:
        '''Number of items on the OpenDSS control Queue'''
        return self._check_for_error(self._lib.CtrlQueue_Get_QueueSize())

    def SetAction(self, index: int):
        '''Set the active action by index'''
        self._check_for_error(self._lib.CtrlQueue_Set_Action(index))

