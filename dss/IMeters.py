# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Iterable
from typing import List, AnyStr
from ._types import Float64Array
from .enums import OCPDevType as OCPDevTypeEnum

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
        '''
        Close All Demand Interval Files. Users are required to close the DI files at the end of a run.

        Original COM help: https://opendss.epri.com/CloseAllDIFiles.html
        '''
        self._check_for_error(self._lib.Meters_CloseAllDIFiles())

    def DoReliabilityCalc(self, AssumeRestoration: bool):
        '''
        Calculate reliability indices

        Original COM help: https://opendss.epri.com/DoReliabilityCalc.html
        '''
        self._check_for_error(self._lib.Meters_DoReliabilityCalc(AssumeRestoration))

    def OpenAllDIFiles(self):
        '''
        Open Demand Interval (DI) files

        Original COM help: https://opendss.epri.com/OpenAllDIFiles.html
        '''
        self._check_for_error(self._lib.Meters_OpenAllDIFiles())

    def Reset(self):
        '''
        Resets registers of active meter.

        Original COM help: https://opendss.epri.com/Reset2.html
        '''
        self._check_for_error(self._lib.Meters_Reset())

    def ResetAll(self):
        '''
        Resets registers of all meter objects.

        Original COM help: https://opendss.epri.com/ResetAll.html
        '''
        self._check_for_error(self._lib.Meters_ResetAll())

    def Sample(self):
        '''
        Forces active Meter to take a sample.

        Original COM help: https://opendss.epri.com/Sample1.html
        '''
        self._check_for_error(self._lib.Meters_Sample())

    def SampleAll(self):
        '''
        Causes all EnergyMeter objects to take a sample at the present time.

        Original COM help: https://opendss.epri.com/SampleAll.html
        '''
        self._check_for_error(self._lib.Meters_SampleAll())

    def Save(self):
        '''
        Saves meter register values.

        Original COM help: https://opendss.epri.com/Save.html
        '''
        self._check_for_error(self._lib.Meters_Save())

    def SaveAll(self):
        '''
        Save All EnergyMeter objects

        Original COM help: https://opendss.epri.com/SaveAll.html
        '''
        self._check_for_error(self._lib.Meters_SaveAll())

    def SetActiveSection(self, SectIdx: int):
        self._check_for_error(self._lib.Meters_SetActiveSection(SectIdx))

    @property
    def AllBranchesInZone(self) -> List[str]:
        '''
        Wide string list of all branches in zone of the active EnergyMeter object.

        Original COM help: https://opendss.epri.com/AllBranchesInZone.html
        '''
        return self._check_for_error(self._get_string_array(self._lib.Meters_Get_AllBranchesInZone))

    @property
    def AllEndElements(self) -> List[str]:
        '''
        Array of names of all zone end elements.

        Original COM help: https://opendss.epri.com/AllEndElements.html
        '''
        return self._check_for_error(self._get_string_array(self._lib.Meters_Get_AllEndElements))

    @property
    def AllocFactors(self) -> Float64Array:
        '''
        Array of doubles: set the phase allocation factors for the active meter.

        Original COM help: https://opendss.epri.com/AllocFactors.html
        '''
        self._check_for_error(self._lib.Meters_Get_AllocFactors_GR())
        return self._get_float64_gr_array()

    @AllocFactors.setter
    def AllocFactors(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.Meters_Set_AllocFactors(ValuePtr, ValueCount))

    @property
    def AvgRepairTime(self) -> float:
        '''
        Average Repair time in this section of the meter zone

        Original COM help: https://opendss.epri.com/AvgRepairTime.html
        '''
        return self._check_for_error(self._lib.Meters_Get_AvgRepairTime())

    @property
    def CalcCurrent(self) -> Float64Array:
        '''
        Set the magnitude of the real part of the Calculated Current (normally determined by solution) for the Meter to force some behavior on Load Allocation

        Original COM help: https://opendss.epri.com/CalcCurrent.html
        '''
        self._check_for_error(self._lib.Meters_Get_CalcCurrent_GR())
        return self._get_float64_gr_array()

    @CalcCurrent.setter
    def CalcCurrent(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.Meters_Set_CalcCurrent(ValuePtr, ValueCount))

    @property
    def CountBranches(self) -> int:
        '''
        Number of branches in Active EnergyMeter zone. (Same as sequence list size)

        Original COM help: https://opendss.epri.com/CountBranches.html
        '''
        return self._check_for_error(self._lib.Meters_Get_CountBranches())

    @property
    def CountEndElements(self) -> int:
        '''
        Number of zone end elements in the active meter zone.

        Original COM help: https://opendss.epri.com/CountEndElements.html
        '''
        return self._check_for_error(self._lib.Meters_Get_CountEndElements())

    @property
    def CustInterrupts(self) -> float:
        '''
        Total customer interruptions for this Meter zone based on reliability calcs.
        
        Original COM help: https://opendss.epri.com/CustInterrupts.html
        '''
        return self._check_for_error(self._lib.Meters_Get_CustInterrupts())

    @property
    def DIFilesAreOpen(self) -> bool:
        '''
        Global Flag in the DSS to indicate if Demand Interval (DI) files have been properly opened.
        
        Original COM help: https://opendss.epri.com/DIFilesAreOpen.html
        '''
        return self._check_for_error(self._lib.Meters_Get_DIFilesAreOpen()) != 0

    @property
    def FaultRateXRepairHrs(self) -> float:
        '''
        Sum of Fault Rate time Repair Hrs in this section of the meter zone
        
        Original COM help: https://opendss.epri.com/FaultRateXRepairHrs.html
        '''
        return self._check_for_error(self._lib.Meters_Get_FaultRateXRepairHrs())

    @property
    def MeteredElement(self) -> str:
        '''
        Name of metered element
        
        Original COM help: https://opendss.epri.com/MeteredElement.html
        '''
        return self._get_string(self._check_for_error(self._lib.Meters_Get_MeteredElement()))

    @MeteredElement.setter
    def MeteredElement(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Meters_Set_MeteredElement(Value))

    @property
    def MeteredTerminal(self) -> int:
        '''
        Number of Metered Terminal
        
        Original COM help: https://opendss.epri.com/MeteredTerminal.html
        '''
        return self._check_for_error(self._lib.Meters_Get_MeteredTerminal())

    @MeteredTerminal.setter
    def MeteredTerminal(self, Value: int):
        self._check_for_error(self._lib.Meters_Set_MeteredTerminal(Value))

    @property
    def NumSectionBranches(self) -> int:
        '''
        Number of branches (lines) in this section
        
        Original COM help: https://opendss.epri.com/NumSectionBranches.html
        '''
        return self._check_for_error(self._lib.Meters_Get_NumSectionBranches())

    @property
    def NumSectionCustomers(self) -> int:
        '''
        Number of Customers in the active section.
        
        Original COM help: https://opendss.epri.com/NumSectionCustomers.html
        '''
        return self._check_for_error(self._lib.Meters_Get_NumSectionCustomers())

    @property
    def NumSections(self) -> int:
        '''
        Number of feeder sections in this meter's zone
        
        Original COM help: https://opendss.epri.com/NumSections.html
        '''
        return self._check_for_error(self._lib.Meters_Get_NumSections())

    @property
    def OCPDeviceType(self) -> OCPDevTypeEnum:
        '''
        Type of OCP device. 1=Fuse; 2=Recloser; 3=Relay
        
        Original COM help: https://opendss.epri.com/OCPDeviceType.html
        '''
        return OCPDevTypeEnum(self._check_for_error(self._lib.Meters_Get_OCPDeviceType()))

    @property
    def Peakcurrent(self) -> Float64Array:
        '''
        Array of doubles to set values of Peak Current property
        
        Original COM help: https://opendss.epri.com/Peakcurrent.html
        '''
        self._check_for_error(self._lib.Meters_Get_Peakcurrent_GR())
        return self._get_float64_gr_array()

    @Peakcurrent.setter
    def Peakcurrent(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.Meters_Set_Peakcurrent(ValuePtr, ValueCount))

    @property
    def RegisterNames(self) -> List[str]:
        '''
        Array of strings containing the names of the registers.
        
        See also the enum `EnergyMeterRegisters` for the standard register names.
        Besides those listed in the enumeration, users may need to check `RegisterNames`
        in order to find a specific register index at runtime.

        Original COM help: https://opendss.epri.com/RegisterNames1.html
        '''
        return self._check_for_error(self._get_string_array(self._lib.Meters_Get_RegisterNames))

    @property
    def RegisterValues(self) -> Float64Array:
        '''
        Array of all the values contained in the Meter registers for the active Meter.

        Original COM help: https://opendss.epri.com/RegisterValues1.html
        '''
        self._check_for_error(self._lib.Meters_Get_RegisterValues_GR())
        return self._get_float64_gr_array()

    @property
    def SAIDI(self) -> float:
        '''
        SAIDI for this meter's zone. Execute DoReliabilityCalc first.

        Original COM help: https://opendss.epri.com/SAIDI.html
        '''
        return self._check_for_error(self._lib.Meters_Get_SAIDI())

    @property
    def SAIFI(self) -> float:
        '''
        Returns SAIFI for this meter's Zone. Execute Reliability Calc method first.

        Original COM help: https://opendss.epri.com/SAIFI.html
        '''
        return self._check_for_error(self._lib.Meters_Get_SAIFI())

    @property
    def SAIFIKW(self) -> float:
        '''
        SAIFI based on kW rather than number of customers. Get after reliability calcs.

        Original COM help: https://opendss.epri.com/SAIFIKW.html
        '''
        return self._check_for_error(self._lib.Meters_Get_SAIFIKW())

    @property
    def SectSeqIdx(self) -> int:
        '''
        SequenceIndex of the branch at the head of this section

        Original COM help: https://opendss.epri.com/SectSeqIdx.html
        '''
        return self._check_for_error(self._lib.Meters_Get_SectSeqIdx())

    @property
    def SectTotalCust(self) -> int:
        '''
        Total Customers downline from this section

        Original COM help: https://opendss.epri.com/SectTotalCust.html
        '''
        return self._check_for_error(self._lib.Meters_Get_SectTotalCust())

    @property
    def SeqListSize(self) -> int:
        '''
        Size of the Sequence List

        Original COM help: https://opendss.epri.com/SeqListSize.html
        '''
        return self._check_for_error(self._lib.Meters_Get_SeqListSize())

    @property
    def SequenceIndex(self) -> int:
        '''
        Get/set Index into Meter's SequenceList that contains branch pointers in lexical order. 
        Earlier index guaranteed to be upline from later index. Sets PDelement active.

        Original COM help: https://opendss.epri.com/SequenceIndex.html
        '''
        return self._check_for_error(self._lib.Meters_Get_SequenceIndex())

    @SequenceIndex.setter
    def SequenceIndex(self, Value: int):
        self._check_for_error(self._lib.Meters_Set_SequenceIndex(Value))

    @property
    def SumBranchFltRates(self) -> float:
        '''
        Sum of the branch fault rates in this section of the meter's zone

        Original COM help: https://opendss.epri.com/SumBranchFltRates.html
        '''
        return self._check_for_error(self._lib.Meters_Get_SumBranchFltRates())

    @property
    def TotalCustomers(self) -> int:
        '''
        Total Number of customers in this zone (downline from the EnergyMeter)

        Original COM help: https://opendss.epri.com/TotalCustomers.html
        '''
        return self._check_for_error(self._lib.Meters_Get_TotalCustomers())

    @property
    def Totals(self) -> Float64Array:
        '''
        Totals of all registers of all meters

        Original COM help: https://opendss.epri.com/Totals.html
        '''
        self._check_for_error(self._lib.Meters_Get_Totals_GR())
        return self._get_float64_gr_array()

    @property
    def ZonePCE(self) -> List[str]:
        '''
        Returns the list of all PCE within the area covered by the energy meter
        
        Original COM help: https://opendss.epri.com/ZonePCE.html
        '''
        result = self._check_for_error(self._get_string_array(self._lib.Meters_Get_ZonePCE))
        if not result:
            result = ['NONE'] #TODO: remove
            
        return result
