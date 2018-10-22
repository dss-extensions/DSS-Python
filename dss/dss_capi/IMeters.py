'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class IMeters(Base):
    __slots__ = []

    def CloseAllDIFiles(self):
        self.lib.Meters_CloseAllDIFiles()

    def DoReliabilityCalc(self, AssumeRestoration):
        self.lib.Meters_DoReliabilityCalc(AssumeRestoration)

    def OpenAllDIFiles(self):
        self.lib.Meters_OpenAllDIFiles()

    def Reset(self):
        self.lib.Meters_Reset()

    def ResetAll(self):
        self.lib.Meters_ResetAll()

    def Sample(self):
        self.lib.Meters_Sample()

    def SampleAll(self):
        self.lib.Meters_SampleAll()

    def Save(self):
        self.lib.Meters_Save()

    def SaveAll(self):
        self.lib.Meters_SaveAll()

    def SetActiveSection(self, SectIdx):
        self.lib.Meters_SetActiveSection(SectIdx)

    @property
    def AllBranchesInZone(self):
        '''(read-only) Wide string list of all branches in zone of the active energymeter object.'''
        return self.get_string_array(self.lib.Meters_Get_AllBranchesInZone)

    @property
    def AllEndElements(self):
        '''(read-only) Array of names of all zone end elements.'''
        return self.get_string_array(self.lib.Meters_Get_AllEndElements)

    @property
    def AllNames(self):
        '''(read-only) Array of all energy Meter names'''
        return self.get_string_array(self.lib.Meters_Get_AllNames)

    @property
    def AllocFactors(self):
        '''Array of doubles: set the phase allocation factors for the active meter.'''
        self.lib.Meters_Get_AllocFactors_GR()
        return self.get_float64_gr_array()

    @AllocFactors.setter
    def AllocFactors(self, Value):
        Value, ValuePtr, ValueCount = self.prepare_float64_array(Value)
        self.lib.Meters_Set_AllocFactors(ValuePtr, ValueCount)

    @property
    def AvgRepairTime(self):
        '''(read-only) Average Repair time in this section of the meter zone'''
        return self.lib.Meters_Get_AvgRepairTime()

    @property
    def CalcCurrent(self):
        '''Set the magnitude of the real part of the Calculated Current (normally determined by solution) for the Meter to force some behavior on Load Allocation'''
        self.lib.Meters_Get_CalcCurrent_GR()
        return self.get_float64_gr_array()

    @CalcCurrent.setter
    def CalcCurrent(self, Value):
        Value, ValuePtr, ValueCount = self.prepare_float64_array(Value)
        self.lib.Meters_Set_CalcCurrent(ValuePtr, ValueCount)

    @property
    def Count(self):
        '''(read-only) Number of Energy Meters in the Active Circuit'''
        return self.lib.Meters_Get_Count()

    def __len__(self):
        return self.lib.Meters_Get_Count()

    @property
    def CountBranches(self):
        '''(read-only) Number of branches in Active energymeter zone. (Same as sequencelist size)'''
        return self.lib.Meters_Get_CountBranches()

    @property
    def CountEndElements(self):
        '''(read-only) Number of zone end elements in the active meter zone.'''
        return self.lib.Meters_Get_CountEndElements()

    @property
    def CustInterrupts(self):
        '''(read-only) Total customer interruptions for this Meter zone based on reliability calcs.'''
        return self.lib.Meters_Get_CustInterrupts()

    @property
    def DIFilesAreOpen(self):
        '''(read-only) Global Flag in the DSS to indicate if Demand Interval (DI) files have been properly opened.'''
        return self.lib.Meters_Get_DIFilesAreOpen() != 0

    @property
    def FaultRateXRepairHrs(self):
        '''(read-only) Sum of Fault Rate time Repair Hrs in this section of the meter zone'''
        return self.lib.Meters_Get_FaultRateXRepairHrs()

    @property
    def First(self):
        '''(read-only) Set the first energy Meter active. Returns 0 if none.'''
        return self.lib.Meters_Get_First()

    @property
    def MeteredElement(self):
        '''Set Name of metered element'''
        return self.get_string(self.lib.Meters_Get_MeteredElement())

    @MeteredElement.setter
    def MeteredElement(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.Meters_Set_MeteredElement(Value)

    @property
    def MeteredTerminal(self):
        '''set Number of Metered Terminal'''
        return self.lib.Meters_Get_MeteredTerminal()

    @MeteredTerminal.setter
    def MeteredTerminal(self, Value):
        self.lib.Meters_Set_MeteredTerminal(Value)

    @property
    def Name(self):
        '''
        (read) Get/Set the active meter  name.
        (write) Set a meter to be active by name.
        '''
        return self.get_string(self.lib.Meters_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.Meters_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Sets the next energy Meter active.  Returns 0 if no more.'''
        return self.lib.Meters_Get_Next()

    @property
    def NumSectionBranches(self):
        '''(read-only) Number of branches (lines) in this section'''
        return self.lib.Meters_Get_NumSectionBranches()

    @property
    def NumSectionCustomers(self):
        '''(read-only) Number of Customers in the active section.'''
        return self.lib.Meters_Get_NumSectionCustomers()

    @property
    def NumSections(self):
        '''(read-only) Number of feeder sections in this meter's zone'''
        return self.lib.Meters_Get_NumSections()

    @property
    def OCPDeviceType(self):
        '''(read-only) Type of OCP device. 1=Fuse; 2=Recloser; 3=Relay'''
        return self.lib.Meters_Get_OCPDeviceType()

    @property
    def Peakcurrent(self):
        '''Array of doubles to set values of Peak Current property'''
        self.lib.Meters_Get_Peakcurrent_GR()
        return self.get_float64_gr_array()

    @Peakcurrent.setter
    def Peakcurrent(self, Value):
        Value, ValuePtr, ValueCount = self.prepare_float64_array(Value)
        self.lib.Meters_Set_Peakcurrent(ValuePtr, ValueCount)

    @property
    def RegisterNames(self):
        '''(read-only) Array of strings containing the names of the registers.'''
        return self.get_string_array(self.lib.Meters_Get_RegisterNames)

    @property
    def RegisterValues(self):
        '''(read-only) Array of all the values contained in the Meter registers for the active Meter.'''
        self.lib.Meters_Get_RegisterValues_GR()
        return self.get_float64_gr_array()

    @property
    def SAIDI(self):
        '''(read-only) SAIDI for this meter's zone. Execute DoReliabilityCalc first.'''
        return self.lib.Meters_Get_SAIDI()

    @property
    def SAIFI(self):
        '''(read-only) Returns SAIFI for this meter's Zone. Execute Reliability Calc method first.'''
        return self.lib.Meters_Get_SAIFI()

    @property
    def SAIFIKW(self):
        '''(read-only) SAIFI based on kW rather than number of customers. Get after reliability calcs.'''
        return self.lib.Meters_Get_SAIFIKW()

    @property
    def SectSeqIdx(self):
        '''(read-only) SequenceIndex of the branch at the head of this section'''
        return self.lib.Meters_Get_SectSeqIdx()

    @property
    def SectTotalCust(self):
        '''(read-only) Total Customers downline from this section'''
        return self.lib.Meters_Get_SectTotalCust()

    @property
    def SeqListSize(self):
        '''(read-only) Size of Sequence List'''
        return self.lib.Meters_Get_SeqListSize()

    @property
    def SequenceIndex(self):
        '''Get/set Index into Meter's SequenceList that contains branch pointers in lexical order. Earlier index guaranteed to be upline from later index. Sets PDelement active.'''
        return self.lib.Meters_Get_SequenceIndex()

    @SequenceIndex.setter
    def SequenceIndex(self, Value):
        self.lib.Meters_Set_SequenceIndex(Value)

    @property
    def SumBranchFltRates(self):
        '''(read-only) Sum of the branch fault rates in this section of the meter's zone'''
        return self.lib.Meters_Get_SumBranchFltRates()

    @property
    def TotalCustomers(self):
        '''(read-only) Total Number of customers in this zone (downline from the EnergyMeter)'''
        return self.lib.Meters_Get_TotalCustomers()

    @property
    def Totals(self):
        '''(read-only) Totals of all registers of all meters'''
        self.lib.Meters_Get_Totals_GR()
        return self.get_float64_gr_array()

    def __iter__(self):
        idx = self.First
        while idx != 0:
            yield self
            idx = self.Next


