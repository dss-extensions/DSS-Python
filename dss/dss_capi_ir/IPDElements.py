'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira
Copyright (c) 2018-2022 DSS Extensions contributors
'''
from .._cffi_api_util import Base

class IPDElements(Base):
    __slots__ = []

    _columns = [
        'Name',
        'AccumulatedL',
        'ParentPDElement',
        'FromTerminal',
        'IsShunt',
        'Numcustomers',
        'SectionID',
        'FaultRate',
        'RepairTime',
        'TotalMiles',
        'Totalcustomers',
        'pctPermanent',
        'Lambda',
    ]

    @property
    def AccumulatedL(self):
        '''(read-only) accummulated failure rate for this branch on downline'''
        return self.CheckForError(self._lib.PDElements_Get_AccumulatedL())

    @property
    def Count(self):
        '''(read-only) Number of PD elements (including disabled elements)'''
        return self.CheckForError(self._lib.PDElements_Get_Count())

    def __len__(self):
        return self.CheckForError(self._lib.PDElements_Get_Count())

    @property
    def FaultRate(self):
        '''
        Get/Set Number of failures per year. 
        For LINE elements: Number of failures per unit length per year.
        '''
        return self.CheckForError(self._lib.PDElements_Get_FaultRate())

    @FaultRate.setter
    def FaultRate(self, Value):
        self.CheckForError(self._lib.PDElements_Set_FaultRate(Value))

    @property
    def First(self):
        '''
        (read-only) Set the first enabled PD element to be the active element.
        Returns 0 if none found.
        '''
        return self.CheckForError(self._lib.PDElements_Get_First())

    @property
    def FromTerminal(self):
        '''
        (read-only) Number of the terminal of active PD element that is on the "from" 
        side. This is set after the meter zone is determined.
        '''
        return self.CheckForError(self._lib.PDElements_Get_FromTerminal())

    @property
    def IsShunt(self):
        '''
        (read-only) Boolean indicating of PD element should be treated as a shunt 
        element rather than a series element. Applies to Capacitor and Reactor 
        elements in particular.
        '''
        return self.CheckForError(self._lib.PDElements_Get_IsShunt()) != 0

    @property
    def Lambda(self):
        '''(read-only) Failure rate for this branch. Faults per year including length of line.'''
        return self.CheckForError(self._lib.PDElements_Get_Lambda())

    @property
    def Name(self):
        '''
        Get/Set name of active PD Element. Returns null string if active element 
        is not PDElement type.
        '''
        return self._get_string(self.CheckForError(self._lib.PDElements_Get_Name()))

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.PDElements_Set_Name(Value))

    @property
    def Next(self):
        '''
        (read-only) Advance to the next PD element in the circuit. Enabled elements 
        only. Returns 0 when no more elements.
        '''
        return self.CheckForError(self._lib.PDElements_Get_Next())

    @property
    def Numcustomers(self):
        '''(read-only) Number of customers, this branch'''
        return self.CheckForError(self._lib.PDElements_Get_Numcustomers())

    @property
    def ParentPDElement(self):
        '''
        (read-only) Sets the parent PD element to be the active circuit element.
        Returns 0 if no more elements upline.
        '''
        return self.CheckForError(self._lib.PDElements_Get_ParentPDElement())

    @property
    def RepairTime(self):
        '''Average repair time for this element in hours'''
        return self.CheckForError(self._lib.PDElements_Get_RepairTime())

    @RepairTime.setter
    def RepairTime(self, Value):
        self.CheckForError(self._lib.PDElements_Set_RepairTime(Value))

    @property
    def SectionID(self):
        '''(read-only) Integer ID of the feeder section that this PDElement branch is part of'''
        return self.CheckForError(self._lib.PDElements_Get_SectionID())

    @property
    def TotalMiles(self):
        '''(read-only) Total miles of line from this element to the end of the zone. For recloser siting algorithm.'''
        return self.CheckForError(self._lib.PDElements_Get_TotalMiles())

    @property
    def Totalcustomers(self):
        '''(read-only) Total number of customers from this branch to the end of the zone'''
        return self.CheckForError(self._lib.PDElements_Get_Totalcustomers())

    @property
    def pctPermanent(self):
        '''Get/Set percent of faults that are permanent (require repair). Otherwise, fault is assumed to be transient/temporary.'''
        return self.CheckForError(self._lib.PDElements_Get_pctPermanent())

    @pctPermanent.setter
    def pctPermanent(self, Value):
        self.CheckForError(self._lib.PDElements_Set_pctPermanent(Value))

    def __iter__(self):
        idx = self.First
        while idx != 0:
            yield self
            idx = self.Next

    @property
    def AllNames(self):
        '''
        Array of strings consisting of all PD element names.
        
        (API Extension)
        '''
        return self.CheckForError(self._get_string_array(self._lib.PDElements_Get_AllNames))

    def AllMaxCurrents(self, AllNodes=False):
        '''
        Array of doubles with the maximum current across the conductors, for each PD 
        element.
        
        By default, only the *first terminal* is used for the maximum current, matching
        the behavior of the "export capacity" command. Pass `AllNodes=True` to 
        force the analysis to all terminals.
        
        See also: 
        https://sourceforge.net/p/electricdss/discussion/beginners/thread/da5b93ca/
        
        (API Extension)
        '''
        return self.CheckForError(self._get_float64_array(self._lib.PDElements_Get_AllMaxCurrents, AllNodes))

    def AllPctNorm(self, AllNodes=False):
        '''
        Array of doubles with the maximum current across the conductors as a percentage 
        of the Normal Ampere Rating, for each PD element.

        By default, only the *first terminal* is used for the maximum current, matching
        the behavior of the "export capacity" command. Pass `AllNodes=True` to 
        force the analysis to all terminals.
        
        See also: 
        https://sourceforge.net/p/electricdss/discussion/beginners/thread/da5b93ca/
        
        (API Extension)
        '''
        return self.CheckForError(self._get_float64_array(self._lib.PDElements_Get_AllPctNorm, AllNodes))

    def AllPctEmerg(self, AllNodes=False):
        '''
        Array of doubles with the maximum current across the conductors as a percentage
        of the Emergency Ampere Rating, for each PD element.

        By default, only the *first terminal* is used for the maximum current, matching
        the behavior of the "export capacity" command. Pass `AllNodes=True` to 
        force the analysis to all terminals.
        
        See also: 
        https://sourceforge.net/p/electricdss/discussion/beginners/thread/da5b93ca/
        
        (API Extension)
        '''
        return self.CheckForError(self._get_float64_array(self._lib.PDElements_Get_AllPctEmerg, AllNodes))

    @property
    def AllCurrents(self):
        '''
        Complex array of currents for all conductors, all terminals, for each PD element.
        
        (API Extension)
        '''
        return self._get_float64_array(self._lib.PDElements_Get_AllCurrents)

    @property
    def AllCurrentsMagAng(self):
        '''
        Complex array (magnitude and angle format) of currents for all conductors, all terminals, for each PD element.
        
        (API Extension)
        '''
        return self._get_float64_array(self._lib.PDElements_Get_AllCurrentsMagAng)

    @property
    def AllCplxSeqCurrents(self):
        '''
        Complex double array of Sequence Currents for all conductors of all terminals, for each PD elements.

        (API Extension)
        '''
        return self._get_float64_array(self._lib.PDElements_Get_AllCplxSeqCurrents)

    @property
    def AllSeqCurrents(self):
        '''
        Double array of the symmetrical component currents into each 3-phase terminal, for each PD element.
        
        (API Extension)
        '''
        return self._get_float64_array(self._lib.PDElements_Get_AllSeqCurrents)

    @property
    def AllPowers(self):
        '''
        Complex array of powers into each conductor of each terminal, for each PD element.
        
        (API Extension)
        '''
        return self._get_float64_array(self._lib.PDElements_Get_AllPowers)

    @property
    def AllSeqPowers(self):
        '''
        Double array of sequence powers into each 3-phase teminal, for each PD element
        
        (API Extension)
        '''
        return self._get_float64_array(self._lib.PDElements_Get_AllSeqPowers)

    @property
    def AllNumPhases(self):
        '''
        Integer array listing the number of phases of all PD elements
        
        (API Extension)
        '''
        return self._get_int32_array(self._lib.PDElements_Get_AllNumPhases)

    @property
    def AllNumConductors(self):
        '''
        Integer array listing the number of conductors of all PD elements
        
        (API Extension)
        '''
        return self._get_int32_array(self._lib.PDElements_Get_AllNumConductors)


    @property
    def AllNumTerminals(self):
        '''
        Integer array listing the number of terminals of all PD elements
        
        (API Extension)
        '''
        return self._get_int32_array(self._lib.PDElements_Get_AllNumTerminals)


