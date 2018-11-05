'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class IPDElements(Base):
    __slots__ = []

    @property
    def AccumulatedL(self):
        '''(read-only) accummulated failure rate for this branch on downline'''
        return self._lib.PDElements_Get_AccumulatedL()

    @property
    def Count(self):
        '''(read-only) Number of PD elements (including disabled elements)'''
        return self._lib.PDElements_Get_Count()

    def __len__(self):
        return self._lib.PDElements_Get_Count()

    @property
    def FaultRate(self):
        '''Get/Set Number of failures per year. For LINE elements: Number of failures per unit length per year. '''
        return self._lib.PDElements_Get_FaultRate()

    @FaultRate.setter
    def FaultRate(self, Value):
        self._lib.PDElements_Set_FaultRate(Value)
        self.CheckForError()

    @property
    def First(self):
        '''(read-only) Set the first enabled PD element to be the active element.  Returns 0 if none found.'''
        return self._lib.PDElements_Get_First()

    @property
    def FromTerminal(self):
        '''(read-only) Number of the terminal of active PD element that is on the "from" side. This is set after the meter zone is determined.'''
        return self._lib.PDElements_Get_FromTerminal()

    @property
    def IsShunt(self):
        '''(read-only) Variant boolean indicating of PD element should be treated as a shunt element rather than a series element. Applies to Capacitor and Reactor elements in particular.'''
        return self._lib.PDElements_Get_IsShunt() != 0

    @property
    def Lambda(self):
        '''(read-only) Failure rate for this branch. Faults per year including length of line.'''
        return self._lib.PDElements_Get_Lambda()

    @property
    def Name(self):
        '''Get/Set name of active PD Element. Returns null string if active element is not PDElement type.'''
        return self._get_string(self._lib.PDElements_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.PDElements_Set_Name(Value)
        self.CheckForError()

    @property
    def Next(self):
        '''(read-only) Advance to the next PD element in the circuit. Enabled elements only. Returns 0 when no more elements.'''
        return self._lib.PDElements_Get_Next()

    @property
    def Numcustomers(self):
        '''(read-only) Number of customers, this branch'''
        return self._lib.PDElements_Get_Numcustomers()

    @property
    def ParentPDElement(self):
        '''(read-only) Sets the parent PD element to be the active circuit element.  Returns 0 if no more elements upline.'''
        return self._lib.PDElements_Get_ParentPDElement()

    @property
    def RepairTime(self):
        '''Average repair time for this element in hours'''
        return self._lib.PDElements_Get_RepairTime()

    @RepairTime.setter
    def RepairTime(self, Value):
        self._lib.PDElements_Set_RepairTime(Value)
        self.CheckForError()

    @property
    def SectionID(self):
        '''(read-only) Integer ID of the feeder section that this PDElement branch is part of'''
        return self._lib.PDElements_Get_SectionID()

    @property
    def TotalMiles(self):
        '''(read-only) Total miles of line from this element to the end of the zone. For recloser siting algorithm.'''
        return self._lib.PDElements_Get_TotalMiles()

    @property
    def Totalcustomers(self):
        '''(read-only) Total number of customers from this branch to the end of the zone'''
        return self._lib.PDElements_Get_Totalcustomers()

    @property
    def pctPermanent(self):
        '''Get/Set percent of faults that are permanent (require repair). Otherwise, fault is assumed to be transient/temporary.'''
        return self._lib.PDElements_Get_pctPermanent()

    @pctPermanent.setter
    def pctPermanent(self, Value):
        self._lib.PDElements_Set_pctPermanent(Value)
        self.CheckForError()

    def __iter__(self):
        idx = self.First
        while idx != 0:
            yield self
            idx = self.Next
