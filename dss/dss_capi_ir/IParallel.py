'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira
Copyright (c) 2018-2022 DSS Extensions contributors
'''
from .._cffi_api_util import Base

class IParallel(Base):
    '''Parallel machine interface. Available only in OpenDSS v8+'''

    __slots__ = []

    def CreateActor(self):
        self.CheckForError(self._lib.Parallel_CreateActor())

    def Wait(self):
        self.CheckForError(self._lib.Parallel_Wait())

    @property
    def ActiveActor(self):
        '''Gets/sets the ID of the Active Actor'''
        return self.CheckForError(self._lib.Parallel_Get_ActiveActor())

    @ActiveActor.setter
    def ActiveActor(self, Value):
        self.CheckForError(self._lib.Parallel_Set_ActiveActor(Value))

    @property
    def ActiveParallel(self):
        '''
        (read) Sets ON/OFF (1/0) Parallel features of the Engine
        (write) Delivers if the Parallel features of the Engine are Active
        '''
        return self.CheckForError(self._lib.Parallel_Get_ActiveParallel())  #TODO: use boolean for consistency

    @ActiveParallel.setter
    def ActiveParallel(self, Value):
        self.CheckForError(self._lib.Parallel_Set_ActiveParallel(Value))

    @property
    def ActorCPU(self):
        '''Gets/sets the CPU of the Active Actor'''
        return self.CheckForError(self._lib.Parallel_Get_ActorCPU())

    @ActorCPU.setter
    def ActorCPU(self, Value):
        self.CheckForError(self._lib.Parallel_Set_ActorCPU(Value))

    @property
    def ActorProgress(self):
        '''(read-only) Gets the progress of all existing actors in pct'''
        return self._get_int32_array(self._lib.Parallel_Get_ActorProgress)

    @property
    def ActorStatus(self):
        '''(read-only) Gets the status of each actor'''
        return self._get_int32_array(self._lib.Parallel_Get_ActorStatus)

    @property
    def ConcatenateReports(self):
        '''
        Controls the ConcatenateReports option (1=enabled, 0=disabled)
        '''
        return self.CheckForError(self._lib.Parallel_Get_ConcatenateReports()) #TODO: use boolean for consistency

    @ConcatenateReports.setter
    def ConcatenateReports(self, Value):
        self.CheckForError(self._lib.Parallel_Set_ConcatenateReports(Value))

    @property
    def NumCPUs(self):
        '''(read-only) Delivers the number of CPUs on the current PC'''
        return self.CheckForError(self._lib.Parallel_Get_NumCPUs())

    @property
    def NumCores(self):
        '''(read-only) Delivers the number of Cores of the local PC'''
        return self.CheckForError(self._lib.Parallel_Get_NumCores())

    @property
    def NumOfActors(self):
        '''(read-only) Gets the number of Actors created'''
        return self.CheckForError(self._lib.Parallel_Get_NumOfActors())


