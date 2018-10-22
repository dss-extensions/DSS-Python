'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class IParallel(Base):
    '''Parallel machine interface. Available only in OpenDSS v8+'''

    __slots__ = []

    def CreateActor(self):
        self.lib.Parallel_CreateActor()

    def Wait(self):
        self.lib.Parallel_Wait()

    @property
    def ActiveActor(self):
        '''
        (read) Gets the ID of the Active Actor
        (write) Sets the Active Actor
        '''
        return self.lib.Parallel_Get_ActiveActor()

    @ActiveActor.setter
    def ActiveActor(self, Value):
        self.lib.Parallel_Set_ActiveActor(Value)

    @property
    def ActiveParallel(self):
        '''
        (read) Sets ON/OFF (1/0) Parallel features of the Engine
        (write) Delivers if the Parallel features of the Engine are Active
        '''
        return self.lib.Parallel_Get_ActiveParallel()

    @ActiveParallel.setter
    def ActiveParallel(self, Value):
        self.lib.Parallel_Set_ActiveParallel(Value)

    @property
    def ActorCPU(self):
        '''
        (read) Gets the CPU of the Active Actor
        (write) Sets the CPU for the Active Actor
        '''
        return self.lib.Parallel_Get_ActorCPU()

    @ActorCPU.setter
    def ActorCPU(self, Value):
        self.lib.Parallel_Set_ActorCPU(Value)

    @property
    def ActorProgress(self):
        '''(read-only) Gets the progress of all existing actors in pct'''
        self.lib.Parallel_Get_ActorProgress_GR()
        return self.get_int32_gr_array()

    @property
    def ActorStatus(self):
        '''(read-only) Gets the status of each actor'''
        self.lib.Parallel_Get_ActorStatus_GR()
        return self.get_int32_gr_array()

    @property
    def ConcatenateReports(self):
        '''
        (read) Reads the values of the ConcatenateReports option (1=enabled, 0=disabled)
        (write) Enable/Disable (1/0) the ConcatenateReports option for extracting monitors data
        '''
        return self.lib.Parallel_Get_ConcatenateReports()

    @ConcatenateReports.setter
    def ConcatenateReports(self, Value):
        self.lib.Parallel_Set_ConcatenateReports(Value)

    @property
    def NumCPUs(self):
        '''(read-only) Delivers the number of CPUs on the current PC'''
        return self.lib.Parallel_Get_NumCPUs()

    @property
    def NumCores(self):
        '''(read-only) Delivers the number of Cores of the local PC'''
        return self.lib.Parallel_Get_NumCores()

    @property
    def NumOfActors(self):
        '''(read-only) Gets the number of Actors created'''
        return self.lib.Parallel_Get_NumOfActors()


