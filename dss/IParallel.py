'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira

Copyright (c) 2018-2022 DSS-Extensions contributors
'''
from ._cffi_api_util import Base
from ._types import Int32Array

class IParallel(Base):
    '''Parallel machine interface'''

    __slots__ = []

    def CreateActor(self):
        self.CheckForError(self._lib.Parallel_CreateActor())

    def Wait(self):
        self.CheckForError(self._lib.Parallel_Wait())

    @property
    def ActiveActor(self) -> int:
        '''Gets/sets the ID of the Active Actor'''
        return self.CheckForError(self._lib.Parallel_Get_ActiveActor())

    @ActiveActor.setter
    def ActiveActor(self, Value: int):
        self.CheckForError(self._lib.Parallel_Set_ActiveActor(Value))

    @property
    def ActiveParallel(self) -> int:
        '''
        (read) Sets ON/OFF (1/0) Parallel features of the Engine
        (write) Delivers if the Parallel features of the Engine are Active
        '''
        return self.CheckForError(self._lib.Parallel_Get_ActiveParallel())  #TODO: use boolean for consistency

    @ActiveParallel.setter
    def ActiveParallel(self, Value: int):
        self.CheckForError(self._lib.Parallel_Set_ActiveParallel(Value))

    @property
    def ActorCPU(self) -> int:
        '''Gets/sets the CPU of the Active Actor'''
        return self.CheckForError(self._lib.Parallel_Get_ActorCPU())

    @ActorCPU.setter
    def ActorCPU(self, Value: int):
        self.CheckForError(self._lib.Parallel_Set_ActorCPU(Value))

    @property
    def ActorProgress(self) -> Int32Array:
        '''Gets the progress of all existing actors in pct'''
        self.CheckForError(self._lib.Parallel_Get_ActorProgress_GR())
        return self._get_int32_gr_array()

    @property
    def ActorStatus(self) -> Int32Array:
        '''Gets the status of each actor'''
        self.CheckForError(self._lib.Parallel_Get_ActorStatus_GR())
        return self._get_int32_gr_array()

    @property
    def ConcatenateReports(self) -> int:
        '''
        (read) Reads the values of the ConcatenateReports option (1=enabled, 0=disabled)
        (write) Enable/Disable (1/0) the ConcatenateReports option for extracting monitors data
        '''
        return self.CheckForError(self._lib.Parallel_Get_ConcatenateReports()) #TODO: use boolean for consistency

    @ConcatenateReports.setter
    def ConcatenateReports(self, Value: int):
        self.CheckForError(self._lib.Parallel_Set_ConcatenateReports(Value))

    @property
    def NumCPUs(self) -> int:
        '''Delivers the number of CPUs on the current PC'''
        return self.CheckForError(self._lib.Parallel_Get_NumCPUs())

    @property
    def NumCores(self) -> int:
        '''Delivers the number of Cores of the local PC'''
        return self.CheckForError(self._lib.Parallel_Get_NumCores())

    @property
    def NumOfActors(self) -> int:
        '''Gets the number of Actors created'''
        return self.CheckForError(self._lib.Parallel_Get_NumOfActors())


