'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira
Copyright (c) 2018-2022 DSS Extensions contributors
'''
from .._cffi_api_util import Iterable

class IMeters(Iterable):
    __slots__ = []
    
    _columns = [
        'Name',
        'Totals',
        'MeteredTerminal',
        'NumSectionCustomers',
        'SectSeqIdx',
        'SumBranchFltRates',
        'SeqListSize',
        'AvgRepairTime',
        'RegisterNames',
        'SectTotalCust',
        'SequenceList',
        'MeteredElement',
        'Peakcurrent',
        'AllocFactors',
        'AllEndElements',
        'OCPDeviceType',
        'SAIFIKW',
        'CountEndElements',
        'NumSections',
        'SAIDI',
        'TotalCustomers',
        'RegisterValues',
        'SAIFI',
        'CustInterrupts',
        'CountBranches',
        'CalcCurrent',
        'AllBranchesInZone',
        'FaultRateXRepairHrs',
        'NumSectionBranches'
    ]

    def CloseAllDIFiles(self):
        self.CheckForError(self._lib.Meters_CloseAllDIFiles())

    def DoReliabilityCalc(self, AssumeRestoration):
        self.CheckForError(self._lib.Meters_DoReliabilityCalc(AssumeRestoration))

    def OpenAllDIFiles(self):
        self.CheckForError(self._lib.Meters_OpenAllDIFiles())

    def Reset(self):
        self.CheckForError(self._lib.Meters_Reset())

    def ResetAll(self):
        self.CheckForError(self._lib.Meters_ResetAll())

    def Sample(self):
        self.CheckForError(self._lib.Meters_Sample())

    def SampleAll(self):
        self.CheckForError(self._lib.Meters_SampleAll())

    def Save(self):
        self.CheckForError(self._lib.Meters_Save())

    def SaveAll(self):
        self.CheckForError(self._lib.Meters_SaveAll())

    def SetActiveSection(self, SectIdx):
        self.CheckForError(self._lib.Meters_SetActiveSection(SectIdx))

    @property
    def AllBranchesInZone(self):
        '''(read-only) Wide string list of all branches in zone of the active energymeter object.'''
        return self.CheckForError(self._get_string_array(self._lib.Meters_Get_AllBranchesInZone))

    @property
    def AllEndElements(self):
        '''(read-only) Array of names of all zone end elements.'''
        return self.CheckForError(self._get_string_array(self._lib.Meters_Get_AllEndElements))

    @property
    def AllocFactors(self):
        '''Array of doubles: set the phase allocation factors for the active meter.'''
        return self._get_float64_array(self._lib.Meters_Get_AllocFactors)

    @AllocFactors.setter
    def AllocFactors(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Meters_Set_AllocFactors(ValuePtr, ValueCount))

    @property
    def AvgRepairTime(self):
        '''(read-only) Average Repair time in this section of the meter zone'''
        return self.CheckForError(self._lib.Meters_Get_AvgRepairTime())

    @property
    def CalcCurrent(self):
        '''Set the magnitude of the real part of the Calculated Current (normally determined by solution) for the Meter to force some behavior on Load Allocation'''
        return self._get_float64_array(self._lib.Meters_Get_CalcCurrent)

    @CalcCurrent.setter
    def CalcCurrent(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Meters_Set_CalcCurrent(ValuePtr, ValueCount))

    @property
    def CountBranches(self):
        '''(read-only) Number of branches in Active energymeter zone. (Same as sequencelist size)'''
        return self.CheckForError(self._lib.Meters_Get_CountBranches())

    @property
    def CountEndElements(self):
        '''(read-only) Number of zone end elements in the active meter zone.'''
        return self.CheckForError(self._lib.Meters_Get_CountEndElements())

    @property
    def CustInterrupts(self):
        '''(read-only) Total customer interruptions for this Meter zone based on reliability calcs.'''
        return self.CheckForError(self._lib.Meters_Get_CustInterrupts())

    @property
    def DIFilesAreOpen(self):
        '''(read-only) Global Flag in the DSS to indicate if Demand Interval (DI) files have been properly opened.'''
        return self.CheckForError(self._lib.Meters_Get_DIFilesAreOpen()) != 0

    @property
    def FaultRateXRepairHrs(self):
        '''(read-only) Sum of Fault Rate time Repair Hrs in this section of the meter zone'''
        return self.CheckForError(self._lib.Meters_Get_FaultRateXRepairHrs())

    @property
    def MeteredElement(self):
        '''Set Name of metered element'''
        return self._get_string(self.CheckForError(self._lib.Meters_Get_MeteredElement()))

    @MeteredElement.setter
    def MeteredElement(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Meters_Set_MeteredElement(Value))

    @property
    def MeteredTerminal(self):
        '''set Number of Metered Terminal'''
        return self.CheckForError(self._lib.Meters_Get_MeteredTerminal())

    @MeteredTerminal.setter
    def MeteredTerminal(self, Value):
        self.CheckForError(self._lib.Meters_Set_MeteredTerminal(Value))

    @property
    def NumSectionBranches(self):
        '''(read-only) Number of branches (lines) in this section'''
        return self.CheckForError(self._lib.Meters_Get_NumSectionBranches())

    @property
    def NumSectionCustomers(self):
        '''(read-only) Number of Customers in the active section.'''
        return self.CheckForError(self._lib.Meters_Get_NumSectionCustomers())

    @property
    def NumSections(self):
        '''(read-only) Number of feeder sections in this meter's zone'''
        return self.CheckForError(self._lib.Meters_Get_NumSections())

    @property
    def OCPDeviceType(self):
        '''(read-only) Type of OCP device. 1=Fuse; 2=Recloser; 3=Relay'''
        return self.CheckForError(self._lib.Meters_Get_OCPDeviceType())

    @property
    def Peakcurrent(self):
        '''Array of doubles to set values of Peak Current property'''
        return self._get_float64_array(self._lib.Meters_Get_Peakcurrent)

    @Peakcurrent.setter
    def Peakcurrent(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Meters_Set_Peakcurrent(ValuePtr, ValueCount))

    @property
    def RegisterNames(self):
        '''(read-only) Array of strings containing the names of the registers.'''
        return self.CheckForError(self._get_string_array(self._lib.Meters_Get_RegisterNames))

    @property
    def RegisterValues(self):
        '''(read-only) Array of all the values contained in the Meter registers for the active Meter.'''
        return self._get_float64_array(self._lib.Meters_Get_RegisterValues)

    @property
    def SAIDI(self):
        '''(read-only) SAIDI for this meter's zone. Execute DoReliabilityCalc first.'''
        return self.CheckForError(self._lib.Meters_Get_SAIDI())

    @property
    def SAIFI(self):
        '''(read-only) Returns SAIFI for this meter's Zone. Execute Reliability Calc method first.'''
        return self.CheckForError(self._lib.Meters_Get_SAIFI())

    @property
    def SAIFIKW(self):
        '''(read-only) SAIFI based on kW rather than number of customers. Get after reliability calcs.'''
        return self.CheckForError(self._lib.Meters_Get_SAIFIKW())

    @property
    def SectSeqIdx(self):
        '''(read-only) SequenceIndex of the branch at the head of this section'''
        return self.CheckForError(self._lib.Meters_Get_SectSeqIdx())

    @property
    def SectTotalCust(self):
        '''(read-only) Total Customers downline from this section'''
        return self.CheckForError(self._lib.Meters_Get_SectTotalCust())

    @property
    def SeqListSize(self):
        '''(read-only) Size of Sequence List'''
        return self.CheckForError(self._lib.Meters_Get_SeqListSize())

    @property
    def SequenceIndex(self):
        '''Get/set Index into Meter's SequenceList that contains branch pointers in lexical order. Earlier index guaranteed to be upline from later index. Sets PDelement active.'''
        return self.CheckForError(self._lib.Meters_Get_SequenceIndex())

    @SequenceIndex.setter
    def SequenceIndex(self, Value):
        self.CheckForError(self._lib.Meters_Set_SequenceIndex(Value))

    @property
    def SumBranchFltRates(self):
        '''(read-only) Sum of the branch fault rates in this section of the meter's zone'''
        return self.CheckForError(self._lib.Meters_Get_SumBranchFltRates())

    @property
    def TotalCustomers(self):
        '''(read-only) Total Number of customers in this zone (downline from the EnergyMeter)'''
        return self.CheckForError(self._lib.Meters_Get_TotalCustomers())

    @property
    def Totals(self):
        '''(read-only) Totals of all registers of all meters'''
        return self._get_float64_array(self._lib.Meters_Get_Totals)

    @property
    def ZonePCE(self):
        '''Returns the list of all PCE within the area covered by the energy meter'''
        result = self.CheckForError(self._get_string_array(self._lib.Meters_Get_ZonePCE))
        if not result:
            result = ['NONE'] #TODO: remove
            
        return result
        
