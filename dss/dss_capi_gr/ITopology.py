'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira
Copyright (c) 2018-2022 DSS Extensions contributors
'''
from .._cffi_api_util import Base

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
    def ActiveBranch(self):
        '''(read-only) Returns index of the active branch'''
        return self.CheckForError(self._lib.Topology_Get_ActiveBranch())

    @property
    def ActiveLevel(self):
        '''(read-only) Topological depth of the active branch'''
        return self.CheckForError(self._lib.Topology_Get_ActiveLevel())

    @property
    def AllIsolatedBranches(self):
        '''(read-only) Array of all isolated branch names.'''
        return self.CheckForError(self._get_string_array(self._lib.Topology_Get_AllIsolatedBranches))

    @property
    def AllIsolatedLoads(self):
        '''(read-only) Array of all isolated load names.'''
        return self.CheckForError(self._get_string_array(self._lib.Topology_Get_AllIsolatedLoads))

    @property
    def AllLoopedPairs(self):
        '''(read-only) Array of all looped element names, by pairs.'''
        return self.CheckForError(self._get_string_array(self._lib.Topology_Get_AllLoopedPairs))

    @property
    def BackwardBranch(self):
        '''(read-only) MOve back toward the source, return index of new active branch, or 0 if no more.'''
        return self.CheckForError(self._lib.Topology_Get_BackwardBranch())

    @property
    def BranchName(self):
        '''Name of the active branch.'''
        return self._get_string(self.CheckForError(self._lib.Topology_Get_BranchName()))

    @BranchName.setter
    def BranchName(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Topology_Set_BranchName(Value))

    @property
    def BusName(self):
        '''Set the active branch to one containing this bus, return index or 0 if not found'''
        return self._get_string(self.CheckForError(self._lib.Topology_Get_BusName()))

    @BusName.setter
    def BusName(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Topology_Set_BusName(Value))

    @property
    def First(self):
        '''(read-only) Sets the first branch active, returns 0 if none.'''
        return self.CheckForError(self._lib.Topology_Get_First())

    @property
    def FirstLoad(self):
        '''(read-only) First load at the active branch, return index or 0 if none.'''
        return self.CheckForError(self._lib.Topology_Get_FirstLoad())

    @property
    def ForwardBranch(self):
        '''(read-only) Move forward in the tree, return index of new active branch or 0 if no more'''
        return self.CheckForError(self._lib.Topology_Get_ForwardBranch())

    @property
    def LoopedBranch(self):
        '''(read-only) Move to looped branch, return index or 0 if none.'''
        return self.CheckForError(self._lib.Topology_Get_LoopedBranch())

    @property
    def Next(self):
        '''(read-only) Sets the next branch active, returns 0 if no more.'''
        return self.CheckForError(self._lib.Topology_Get_Next())

    @property
    def NextLoad(self):
        '''(read-only) Next load at the active branch, return index or 0 if no more.'''
        return self.CheckForError(self._lib.Topology_Get_NextLoad())

    @property
    def NumIsolatedBranches(self):
        '''(read-only) Number of isolated branches (PD elements and capacitors).'''
        return self.CheckForError(self._lib.Topology_Get_NumIsolatedBranches())

    @property
    def NumIsolatedLoads(self):
        '''(read-only) Number of isolated loads'''
        return self.CheckForError(self._lib.Topology_Get_NumIsolatedLoads())

    @property
    def NumLoops(self):
        '''(read-only) Number of loops'''
        return self.CheckForError(self._lib.Topology_Get_NumLoops())

    @property
    def ParallelBranch(self):
        '''(read-only) Move to directly parallel branch, return index or 0 if none.'''
        return self.CheckForError(self._lib.Topology_Get_ParallelBranch())

