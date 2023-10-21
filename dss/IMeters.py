'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2023 Paulo Meira

Copyright (c) 2018-2023 DSS-Extensions contributors
'''
from ._cffi_api_util import Iterable
from typing import List, AnyStr
from ._types import Float64Array

class IMeters(Iterable):
    __slots__ = []
    _is_circuit_element = True

    _columns = [
        'Name',
        'MeteredTerminal',
        'SeqListSize',
        'RegisterNames',
        'MeteredElement',
        'Peakcurrent',
        'AllocFactors',
        'AllEndElements',
        'SAIFIKW',
        'CountEndElements',
        'SAIDI',
        'TotalCustomers',
        'RegisterValues',
        'SAIFI',
        'CustInterrupts',
        'CountBranches',
        'CalcCurrent',
        'AllBranchesInZone',

        'NumSections',
        'NumSectionCustomers',
        'SectSeqIdx',
        'SumBranchFltRates',
        'AvgRepairTime',
        'SectTotalCust',
        'OCPDeviceType',
        'FaultRateXRepairHrs',
        'NumSectionBranches'
    ]

    def CloseAllDIFiles(self):
        '''Close All Demand Interval Files. Users are required to close the DI files at the end of a run.'''
        self.CheckForError(self._lib.Meters_CloseAllDIFiles())

    def DoReliabilityCalc(self, AssumeRestoration: bool):
        '''Calculate reliability indices'''
        self.CheckForError(self._lib.Meters_DoReliabilityCalc(AssumeRestoration))

    def OpenAllDIFiles(self):
        '''Open Demand Interval (DI) files'''
        self.CheckForError(self._lib.Meters_OpenAllDIFiles())

    def Reset(self):
        '''Resets registers of active meter.'''
        self.CheckForError(self._lib.Meters_Reset())

    def ResetAll(self):
        '''Resets registers of all meter objects.'''
        self.CheckForError(self._lib.Meters_ResetAll())

    def Sample(self):
        '''Forces active Meter to take a sample.'''
        self.CheckForError(self._lib.Meters_Sample())

    def SampleAll(self):
        '''Causes all EnergyMeter objects to take a sample at the present time.'''
        self.CheckForError(self._lib.Meters_SampleAll())

    def Save(self):
        '''Saves meter register values.'''
        self.CheckForError(self._lib.Meters_Save())

    def SaveAll(self):
        '''Save All EnergyMeter objects'''
        self.CheckForError(self._lib.Meters_SaveAll())

    def SetActiveSection(self, SectIdx: int):
        self.CheckForError(self._lib.Meters_SetActiveSection(SectIdx))

    @property
    def AllBranchesInZone(self) -> List[str]:
        '''Wide string list of all branches in zone of the active EnergyMeter object.'''
        return self.CheckForError(self._get_string_array(self._lib.Meters_Get_AllBranchesInZone))

    @property
    def AllEndElements(self) -> List[str]:
        '''Array of names of all zone end elements.'''
        return self.CheckForError(self._get_string_array(self._lib.Meters_Get_AllEndElements))

    @property
    def AllocFactors(self) -> Float64Array:
        '''Array of doubles: set the phase allocation factors for the active meter.'''
        self.CheckForError(self._lib.Meters_Get_AllocFactors_GR())
        return self._get_float64_gr_array()

    @AllocFactors.setter
    def AllocFactors(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Meters_Set_AllocFactors(ValuePtr, ValueCount))

    @property
    def AvgRepairTime(self) -> float:
        '''Average Repair time in this section of the meter zone'''
        return self.CheckForError(self._lib.Meters_Get_AvgRepairTime())

    @property
    def CalcCurrent(self) -> Float64Array:
        '''Set the magnitude of the real part of the Calculated Current (normally determined by solution) for the Meter to force some behavior on Load Allocation'''
        self.CheckForError(self._lib.Meters_Get_CalcCurrent_GR())
        return self._get_float64_gr_array()

    @CalcCurrent.setter
    def CalcCurrent(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Meters_Set_CalcCurrent(ValuePtr, ValueCount))

    @property
    def CountBranches(self) -> int:
        '''Number of branches in Active energymeter zone. (Same as sequencelist size)'''
        return self.CheckForError(self._lib.Meters_Get_CountBranches())

    @property
    def CountEndElements(self) -> int:
        '''Number of zone end elements in the active meter zone.'''
        return self.CheckForError(self._lib.Meters_Get_CountEndElements())

    @property
    def CustInterrupts(self) -> float:
        '''Total customer interruptions for this Meter zone based on reliability calcs.'''
        return self.CheckForError(self._lib.Meters_Get_CustInterrupts())

    @property
    def DIFilesAreOpen(self) -> bool:
        '''Global Flag in the DSS to indicate if Demand Interval (DI) files have been properly opened.'''
        return self.CheckForError(self._lib.Meters_Get_DIFilesAreOpen()) != 0

    @property
    def FaultRateXRepairHrs(self) -> float:
        '''Sum of Fault Rate time Repair Hrs in this section of the meter zone'''
        return self.CheckForError(self._lib.Meters_Get_FaultRateXRepairHrs())

    @property
    def MeteredElement(self) -> str:
        '''Set Name of metered element'''
        return self._get_string(self.CheckForError(self._lib.Meters_Get_MeteredElement()))

    @MeteredElement.setter
    def MeteredElement(self, Value: AnyStr):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Meters_Set_MeteredElement(Value))

    @property
    def MeteredTerminal(self) -> int:
        '''set Number of Metered Terminal'''
        return self.CheckForError(self._lib.Meters_Get_MeteredTerminal())

    @MeteredTerminal.setter
    def MeteredTerminal(self, Value: int):
        self.CheckForError(self._lib.Meters_Set_MeteredTerminal(Value))

    @property
    def NumSectionBranches(self) -> int:
        '''Number of branches (lines) in this section'''
        return self.CheckForError(self._lib.Meters_Get_NumSectionBranches())

    @property
    def NumSectionCustomers(self) -> int:
        '''Number of Customers in the active section.'''
        return self.CheckForError(self._lib.Meters_Get_NumSectionCustomers())

    @property
    def NumSections(self) -> int:
        '''Number of feeder sections in this meter's zone'''
        return self.CheckForError(self._lib.Meters_Get_NumSections())

    @property
    def OCPDeviceType(self) -> int:
        '''Type of OCP device. 1=Fuse; 2=Recloser; 3=Relay'''
        return self.CheckForError(self._lib.Meters_Get_OCPDeviceType())

    @property
    def Peakcurrent(self) -> Float64Array:
        '''Array of doubles to set values of Peak Current property'''
        self.CheckForError(self._lib.Meters_Get_Peakcurrent_GR())
        return self._get_float64_gr_array()

    @Peakcurrent.setter
    def Peakcurrent(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Meters_Set_Peakcurrent(ValuePtr, ValueCount))

    @property
    def RegisterNames(self) -> List[str]:
        '''Array of strings containing the names of the registers.'''
        return self.CheckForError(self._get_string_array(self._lib.Meters_Get_RegisterNames))

    @property
    def RegisterValues(self) -> Float64Array:
        '''Array of all the values contained in the Meter registers for the active Meter.'''
        self.CheckForError(self._lib.Meters_Get_RegisterValues_GR())
        return self._get_float64_gr_array()

    @property
    def SAIDI(self) -> float:
        '''SAIDI for this meter's zone. Execute DoReliabilityCalc first.'''
        return self.CheckForError(self._lib.Meters_Get_SAIDI())

    @property
    def SAIFI(self) -> float:
        '''Returns SAIFI for this meter's Zone. Execute Reliability Calc method first.'''
        return self.CheckForError(self._lib.Meters_Get_SAIFI())

    @property
    def SAIFIKW(self) -> float:
        '''SAIFI based on kW rather than number of customers. Get after reliability calcs.'''
        return self.CheckForError(self._lib.Meters_Get_SAIFIKW())

    @property
    def SectSeqIdx(self) -> int:
        '''SequenceIndex of the branch at the head of this section'''
        return self.CheckForError(self._lib.Meters_Get_SectSeqIdx())

    @property
    def SectTotalCust(self) -> int:
        '''Total Customers downline from this section'''
        return self.CheckForError(self._lib.Meters_Get_SectTotalCust())

    @property
    def SeqListSize(self) -> int:
        '''Size of Sequence List'''
        return self.CheckForError(self._lib.Meters_Get_SeqListSize())

    @property
    def SequenceIndex(self) -> int:
        '''Get/set Index into Meter's SequenceList that contains branch pointers in lexical order. Earlier index guaranteed to be upline from later index. Sets PDelement active.'''
        return self.CheckForError(self._lib.Meters_Get_SequenceIndex())

    @SequenceIndex.setter
    def SequenceIndex(self, Value: int):
        self.CheckForError(self._lib.Meters_Set_SequenceIndex(Value))

    @property
    def SumBranchFltRates(self) -> float:
        '''Sum of the branch fault rates in this section of the meter's zone'''
        return self.CheckForError(self._lib.Meters_Get_SumBranchFltRates())

    @property
    def TotalCustomers(self) -> int:
        '''Total Number of customers in this zone (downline from the EnergyMeter)'''
        return self.CheckForError(self._lib.Meters_Get_TotalCustomers())

    @property
    def Totals(self) -> Float64Array:
        '''Totals of all registers of all meters'''
        self.CheckForError(self._lib.Meters_Get_Totals_GR())
        return self._get_float64_gr_array()

    @property
    def ZonePCE(self) -> List[str]:
        '''Returns the list of all PCE within the area covered by the energy meter'''
        result = self.CheckForError(self._get_string_array(self._lib.Meters_Get_ZonePCE))
        if not result:
            result = ['NONE'] #TODO: remove
            
        return result
