# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Base
from typing import List

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
        '''
        Clear all actions from the Control Proxy's Action List (they are popped off the list). 

        Original COM help: https://opendss.epri.com/ClearActions.html
        '''
        self._check_for_error(self._lib.CtrlQueue_ClearActions())

    def ClearQueue(self):
        '''
        Clear the control queue.

        Original COM help: https://opendss.epri.com/ClearQueue.html
        '''
        self._check_for_error(self._lib.CtrlQueue_ClearQueue())

    def Delete(self, ActionHandle):
        '''
        Delete an Action from the DSS Control Queue by the handle that is returned when the action is added.
        
        (The Push function returns the handle.)

        Original COM help: https://opendss.epri.com/Delete.html
        '''
        self._check_for_error(self._lib.CtrlQueue_Delete(ActionHandle))

    def DoAllQueue(self):
        '''
        Execute all actions currently on the Control Queue. 

        Side effect: clears the queue.

        Original COM help: https://opendss.epri.com/DoAllQueue.html
        '''
        self._check_for_error(self._lib.CtrlQueue_DoAllQueue())

    def Show(self):
        '''
        Export the queue to a CSV table and show it.

        Original COM help: https://opendss.epri.com/Show.html
        '''
        self._check_for_error(self._lib.CtrlQueue_Show())

    @property
    def ActionCode(self) -> int:
        '''
        Code for the active action. Integer code to tell the control device what to do.
        
        Use this to determine what the user-defined controls are supposed to do.
        It can be any 32-bit integer of the user's choosing and is the same value that the control pushed onto the control queue earlier.

        Original COM help: https://opendss.epri.com/ActionCode.html
        '''
        return self._check_for_error(self._lib.CtrlQueue_Get_ActionCode())

    @property
    def DeviceHandle(self) -> int:
        '''
        Handle (User defined) to device that must act on the pending action.
        
        The user-written code driving the interface may support more than one 
        control element as necessary to perform the simulation. This handle is
        an index returned to the user program that lets the program know which
        control is to perform the active action.

        Original COM help: https://opendss.epri.com/DeviceHandle.html   
        '''
        return self._check_for_error(self._lib.CtrlQueue_Get_DeviceHandle())

    @property
    def NumActions(self) -> int:
        '''
        Number of Actions on the current action list (that have been popped off the control queue by CheckControlActions)

        Original COM help: https://opendss.epri.com/NumActions.html
        '''
        return self._check_for_error(self._lib.CtrlQueue_Get_NumActions())

    def Push(self, Hour: int, Seconds: float, ActionCode: int, DeviceHandle: int):
        '''
        Push a control action onto the DSS control queue by time, action code, and device handle (user defined). Returns Control Queue handle.

        Original COM help: https://opendss.epri.com/Push.html
        '''
        return self._check_for_error(self._lib.CtrlQueue_Push(Hour, Seconds, ActionCode, DeviceHandle))

    @property
    def PopAction(self) -> int:
        '''
        Pops next action off the action list and makes it the active action. Returns zero if none.

        Original COM help: https://opendss.epri.com/PopAction.html
        '''
        return self._check_for_error(self._lib.CtrlQueue_Get_PopAction())

    @property
    def Queue(self) -> List[str]:
        '''
        Array of strings containing the entire queue in CSV format

        Original COM help: https://opendss.epri.com/Queue.html
        '''
        return self._check_for_error(self._get_string_array(self._lib.CtrlQueue_Get_Queue))

    @property
    def QueueSize(self) -> int:
        '''
        Number of items on the OpenDSS control Queue

        Original COM help: https://opendss.epri.com/QueueSize.html
        '''
        return self._check_for_error(self._lib.CtrlQueue_Get_QueueSize())

    @property
    def Action(self) -> int:
        '''
        (write-only) Set the active action by index

        Original COM help: https://opendss.epri.com/Action.html
        '''
        raise AttributeError("This property is write-only!")

    @Action.setter
    def Action(self, Param1: int):
        self._check_for_error(self._lib.CtrlQueue_Set_Action(Param1))

