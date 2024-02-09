# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Base
from ._types import Int32Array

class IParallel(Base):
    '''
    Parallel machine interface
    
    On DSS-Extensions, prefer using DSSContexts and native threading capabilities of your programming
    language, if available.
    '''

    __slots__ = []

    def CreateActor(self):
        '''
        Create a new actor, if there are still cores available.
        '''
        self._check_for_error(self._lib.Parallel_CreateActor())

    def Wait(self):
        '''
        Suspends the host's thread until all the OpenDSS running jobs finish.

        Original COM help: https://opendss.epri.com/Wait.html
        '''
        self._check_for_error(self._lib.Parallel_Wait())

    @property
    def ActiveActor(self) -> int:
        '''
        Gets/sets the ID of the Active Actor

        Original COM help: https://opendss.epri.com/ActiveActor.html
        '''
        return self._check_for_error(self._lib.Parallel_Get_ActiveActor())

    @ActiveActor.setter
    def ActiveActor(self, Value: int):
        self._check_for_error(self._lib.Parallel_Set_ActiveActor(Value))

    @property
    def ActiveParallel(self) -> int:
        '''
        (read) Sets ON/OFF (1/0) Parallel features of the Engine
        (write) Delivers if the Parallel features of the Engine are Active

        Original COM help: https://opendss.epri.com/ActiveParallel.html
        '''
        return self._check_for_error(self._lib.Parallel_Get_ActiveParallel())  #TODO: use boolean for consistency

    @ActiveParallel.setter
    def ActiveParallel(self, Value: int):
        self._check_for_error(self._lib.Parallel_Set_ActiveParallel(Value))

    @property
    def ActorCPU(self) -> int:
        '''
        Gets/sets the CPU of the Active Actor

        Original COM help: https://opendss.epri.com/ActorCPU.html
        '''
        return self._check_for_error(self._lib.Parallel_Get_ActorCPU())

    @ActorCPU.setter
    def ActorCPU(self, Value: int):
        self._check_for_error(self._lib.Parallel_Set_ActorCPU(Value))

    @property
    def ActorProgress(self) -> Int32Array:
        '''
        Gets the progress of all existing actors in pct

        Original COM help: https://opendss.epri.com/ActorProgress.html
        '''
        self._check_for_error(self._lib.Parallel_Get_ActorProgress_GR())
        return self._get_int32_gr_array()

    @property
    def ActorStatus(self) -> Int32Array:
        '''
        Gets the status of each actor

        Original COM help: https://opendss.epri.com/ActorStatus.html
        '''
        self._check_for_error(self._lib.Parallel_Get_ActorStatus_GR())
        return self._get_int32_gr_array()

    @property
    def ConcatenateReports(self) -> int:
        '''
        (read) Reads the values of the ConcatenateReports option (1=enabled, 0=disabled)
        (write) Enable/Disable (1/0) the ConcatenateReports option for extracting monitors data

        Original COM help: https://opendss.epri.com/ConcatenateReports.html
        '''
        return self._check_for_error(self._lib.Parallel_Get_ConcatenateReports()) #TODO: use boolean for consistency

    @ConcatenateReports.setter
    def ConcatenateReports(self, Value: int):
        self._check_for_error(self._lib.Parallel_Set_ConcatenateReports(Value))

    @property
    def NumCPUs(self) -> int:
        '''
        Delivers the number of CPUs on the current PC

        Original COM help: https://opendss.epri.com/NumCPUs.html
        '''
        return self._check_for_error(self._lib.Parallel_Get_NumCPUs())

    @property
    def NumCores(self) -> int:
        '''
        Delivers the number of Cores of the local PC

        Original COM help: https://opendss.epri.com/NumCores.html
        '''
        return self._check_for_error(self._lib.Parallel_Get_NumCores())

    @property
    def NumOfActors(self) -> int:
        '''
        Gets the number of Actors created

        Original COM help: https://opendss.epri.com/NumOfActors.html
        '''
        return self._check_for_error(self._lib.Parallel_Get_NumOfActors())


