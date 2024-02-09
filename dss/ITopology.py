# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Base
from typing import List, AnyStr

class ITopology(Base):
    __slots__ = []

    _columns = [
        'NumIsolatedLoads',
        'AllIsolatedBranches',
        'NumIsolatedBranches',
        'AllIsolatedLoads',
        'ActiveLevel',
        'BranchName',
        'AllLoopedPairs',
        'NumLoops',
        'ActiveBranch'
    ]

    @property
    def ActiveBranch(self) -> int:
        '''
        Returns index of the active branch

        Original COM help: https://opendss.epri.com/ActiveBranch.html
        '''
        return self._check_for_error(self._lib.Topology_Get_ActiveBranch())

    @property
    def ActiveLevel(self) -> int:
        '''
        Topological depth of the active branch

        Original COM help: https://opendss.epri.com/ActiveLevel.html
        '''
        return self._check_for_error(self._lib.Topology_Get_ActiveLevel())

    @property
    def AllIsolatedBranches(self) -> List[str]:
        '''
        Array of all isolated branch names.

        Original COM help: https://opendss.epri.com/AllIsolatedBranches.html
        '''
        return self._check_for_error(self._get_string_array(self._lib.Topology_Get_AllIsolatedBranches))

    @property
    def AllIsolatedLoads(self) -> List[str]:
        '''
        Array of all isolated load names.

        Original COM help: https://opendss.epri.com/AllIsolatedLoads.html
        '''
        return self._check_for_error(self._get_string_array(self._lib.Topology_Get_AllIsolatedLoads))

    @property
    def AllLoopedPairs(self) -> List[str]:
        '''
        Array of all looped element names, by pairs.

        Original COM help: https://opendss.epri.com/AllLoopedPairs.html
        '''
        return self._check_for_error(self._get_string_array(self._lib.Topology_Get_AllLoopedPairs))

    @property
    def BackwardBranch(self) -> int:
        '''
        Move back toward the source, return index of new active branch, or 0 if no more.

        Original COM help: https://opendss.epri.com/BackwardBranch.html
        '''
        return self._check_for_error(self._lib.Topology_Get_BackwardBranch())

    @property
    def BranchName(self) -> str:
        '''
        Name of the active branch.

        Original COM help: https://opendss.epri.com/BranchName.html
        '''
        return self._get_string(self._check_for_error(self._lib.Topology_Get_BranchName()))

    @BranchName.setter
    def BranchName(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Topology_Set_BranchName(Value))

    @property
    def BusName(self) -> str:
        '''
        Set the active branch to one containing this bus, return index or 0 if not found

        Original COM help: https://opendss.epri.com/BusName.html
        '''
        return self._get_string(self._check_for_error(self._lib.Topology_Get_BusName()))

    @BusName.setter
    def BusName(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Topology_Set_BusName(Value))

    @property
    def First(self) -> int:
        '''
        Sets the first branch active, returns 0 if none.

        Original COM help: https://opendss.epri.com/First19.html
        '''
        return self._check_for_error(self._lib.Topology_Get_First())

    @property
    def FirstLoad(self) -> int:
        '''
        First load at the active branch, return index or 0 if none.

        Original COM help: https://opendss.epri.com/FirstLoad.html
        '''
        return self._check_for_error(self._lib.Topology_Get_FirstLoad())

    @property
    def ForwardBranch(self) -> int:
        '''
        Move forward in the tree, return index of new active branch or 0 if no more

        Original COM help: https://opendss.epri.com/ForwardBranch.html
        '''
        return self._check_for_error(self._lib.Topology_Get_ForwardBranch())

    @property
    def LoopedBranch(self) -> int:
        '''
        Move to looped branch, return index or 0 if none.

        Original COM help: https://opendss.epri.com/LoopedBranch.html
        '''
        return self._check_for_error(self._lib.Topology_Get_LoopedBranch())

    @property
    def Next(self) -> int:
        '''
        Sets the next branch active, returns 0 if no more.

        Original COM help: https://opendss.epri.com/Next18.html
        '''
        return self._check_for_error(self._lib.Topology_Get_Next())

    @property
    def NextLoad(self) -> int:
        '''
        Next load at the active branch, return index or 0 if no more.

        Original COM help: https://opendss.epri.com/NextLoad.html
        '''
        return self._check_for_error(self._lib.Topology_Get_NextLoad())

    @property
    def NumIsolatedBranches(self) -> int:
        '''
        Number of isolated branches (PD elements and capacitors).

        Original COM help: https://opendss.epri.com/NumIsolatedBranches.html
        '''
        return self._check_for_error(self._lib.Topology_Get_NumIsolatedBranches())

    @property
    def NumIsolatedLoads(self) -> int:
        '''
        Number of isolated loads

        Original COM help: https://opendss.epri.com/NumIsolatedLoads.html
        '''
        return self._check_for_error(self._lib.Topology_Get_NumIsolatedLoads())

    @property
    def NumLoops(self) -> int:
        '''
        Number of loops

        Original COM help: https://opendss.epri.com/NumLoops.html
        '''
        return self._check_for_error(self._lib.Topology_Get_NumLoops())

    @property
    def ParallelBranch(self) -> int:
        '''
        Move to directly parallel branch, return index or 0 if none.

        Original COM help: https://opendss.epri.com/ParallelBranch.html
        '''
        return self._check_for_error(self._lib.Topology_Get_ParallelBranch())

