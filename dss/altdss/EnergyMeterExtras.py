from .types import Float64Array, Int32Array
from .PCElement import PCElementBatch
from .CircuitElement import CircuitElementBatch
from .PDElement import PDElementBatch
from .Load import LoadBatch
from dss.enums import OCPDevType as OCPDevTypeEnum #TODO: add/import from altdss.enums

class MeterSection:
    '''
    Encapsulates meter section functions
    '''
    __slots__ = (
        '_meter',
        '_idx',
        '_lib',
    )

    def __init__(self, meter, idx):
        self._meter = meter
        self._idx = idx
        self._lib = meter._lib

    def Index(self) -> int:
        return self._idx
        
    def AvgRepairTime(self) -> float:
        return self._lib.Alt_MeterSection_AvgRepairTime(self._meter._ptr, self._idx)

    def FaultRateXRepairHours(self) -> float:
        return self._lib.Alt_MeterSection_FaultRateXRepairHours(self._meter._ptr, self._idx)

    def NumBranches(self) -> int:
        return self._lib.Alt_MeterSection_NumBranches(self._meter._ptr, self._idx)

    def NumCustomers(self) -> int:
        return self._lib.Alt_MeterSection_NumCustomers(self._meter._ptr, self._idx)

    def OCPDeviceType(self) -> OCPDevTypeEnum:
        return OCPDevTypeEnum(self._lib.Alt_MeterSection_OCPDeviceType(self._meter._ptr, self._idx))

    def SumBranchFaultRates(self) -> float:
        return self._lib.Alt_MeterSection_SumBranchFaultRates(self._meter._ptr, self._idx)

    def SequenceIndex(self) -> int:
        return self._lib.Alt_MeterSection_SequenceIndex(self._meter._ptr, self._idx)

    def TotalCustomers(self) -> int:
        return self._lib.Alt_MeterSection_TotalCustomers(self._meter._ptr, self._idx)

    def as_dict(self):
        return {
            k: getattr(self, k)() for k in (
                'Index',
                'AvgRepairTime',
                'FaultRateXRepairHours',
                'NumBranches',
                'NumCustomers',
                'OCPDeviceType',
                'SumBranchFaultRates',
                'SequenceIndex',
                'TotalCustomers'
            )
        }


class MeterSections:
    '''
    Encapsulates meter sections to provide iteration and indexing.
    '''
    __slots__ = (
        '_meter',
    )

    def __init__(self, meter):
        self._meter = meter

    def __call__(self, idx: int) -> MeterSection:
        '''Returns a meter section by index'''
        if idx > 0 and idx <= self._meter.NumSections():
            return MeterSection(self._meter, idx)
        
        raise IndexError(f'Invalid section index for meter "{self._meter.Name}"; this meter has {self._meter.NumSections()} sections in total.')

    __getitem__ = __call__

    def __len__(self):
        return self._meter.NumSections()

    def __iter__(self):
        for idx in range(1, self._meter.NumSections() + 1):
            yield self[idx]


class EnergyMeterObjMixin:
    __slots__ = ()
    # To avoid layout issues, let the final class use the following instead
    _extra_slots = [
        'ZonePCEs',
        'EndElements',
        'Branches',
        'Loads',
        'Sequence',
    ]

    '''Accessor for all power converting elements (PCEs) within the area covered by this energy meter.'''
    ZonePCEs: PCElementBatch
        
    '''Accessor for all zone end elements for this meter.'''
    EndElements: CircuitElementBatch

    '''Accessor for all branches in the meter zone.'''
    Branches: PDElementBatch

    '''Accessor for all loads in the meter zone (internal LoadList).'''
    Loads: LoadBatch #TODO: actually... is this uniform?

    '''Accessor for all branches in the meter zone (internal SequenceList), in lexical order'''
    Sequence: CircuitElementBatch

    def __init__(self):
        self.ZonePCEs = PCElementBatch(self._lib.Alt_Meter_Get_ZonePCEs, self)
        self.EndElements = CircuitElementBatch(self._lib.Alt_Meter_Get_EndElements, self)
        self.Branches = PDElementBatch(self._lib.Alt_Meter_Get_BranchesInZone, self)
        self.Loads = LoadBatch(self._api_util, from_func=(self._lib.Alt_Meter_Get_Loads, self._ptr))
        self.Sequence = CircuitElementBatch(self._lib.Alt_Meter_Get_SequenceList, self)

    def TotalCustomers(self) -> int:
        '''Total Number of customers in this zone (downline from the EnergyMeter)'''
        return self._lib.Alt_Meter_Get_TotalCustomers(self._ptr)

    def NumEndElements(self) -> int:
        '''Number of zone end elements in the active meter zone.'''
        return self._lib.Alt_Meter_Get_NumEndElements(self._ptr)

    def NumSections(self) -> int:
        '''Number of feeder sections in this meter's zone'''
        return self._lib.Alt_Meter_Get_NumSections(self._ptr)

    def DoReliabilityCalc(self, assumeRestoration) -> None:
        '''Calculate reliability indices'''
        self.lib._Alt_Meter_DoReliabilityCalc(self._ptr, assumeRestoration)

    @property
    def CalcCurrent(self) -> Float64Array:
        '''
        Set/get the magnitude of the real part of the Calculated Current (normally determined by solution) 
        for the meter to force some behavior on Load Allocation
        '''
        return self._get_float64_array(self._lib.Alt_Meter_Get_CalcCurrent, self._ptr)

    @CalcCurrent.setter
    def CalcCurrent(self, value: Float64Array):
        value, value_ptr, value_count = self._prepare_float64_array(value)
        self._lib.Alt_Meter_Set_CalcCurrent(self._ptr, value_ptr, value_count)

    @property
    def AllocFactors(self) -> Float64Array:
        '''Set the phase allocation factors for this meter.'''
        return self._get_float64_array(self._lib.Alt_Meter_Get_AllocFactors, self._ptr)

    @AllocFactors.setter
    def AllocFactors(self, value: Float64Array):
        value, value_ptr, value_count = self._prepare_float64_array(value)
        self._lib.Alt_Meter_Set_AllocFactors(self._ptr, value_ptr, value_count)

    def Section(self, idx: int) -> MeterSection:
        '''Returns a wrapper for a single meter section'''
        return MeterSection(self, idx)

    def Sections(self) -> MeterSections:
        '''Returns a wrapper for meter sections'''
        return MeterSections(self)


class EnergyMeterBatchMixin:
    __slots__ = ()

    def TotalCustomers(self) -> Int32Array:
        '''Total Number of customers in this zone (downline from the EnergyMeter)'''
        return self._get_batch_int32_func("Alt_Meter_Get_TotalCustomers")

    def NumEndElements(self) -> Int32Array:
        '''Number of zone end elements in the active meter zone.'''
        return self._get_batch_int32_func("Alt_Meter_Get_NumEndElements")

    def NumSections(self) -> Int32Array:
        '''Number of feeder sections in the zone of each meter'''
        return self._get_batch_int32_func("Alt_Meter_Get_NumSections")

    def DoReliabilityCalc(self, assumeRestoration) -> None:
        '''Calculate reliability indices for each meter'''
        for ptr in self._unpack():
            self.lib._Alt_Meter_DoReliabilityCalc(ptr, assumeRestoration)


class IEnergyMeterMixin:
    #TODO: automate create of these and others
    # SampleAll = IMeters.SampleAll
    # SaveAll = IMeters.SaveAll
    # ResetAll = IMeters.ResetAll

    def CloseDIFiles(self):
        '''
        Close all Demand Interval files.
        Users are required to close the DI files at the end of a run,
        either using this function or the `CloseDI` DSS command.
        '''
        self._check_for_error(self._lib.Meters_CloseAllDIFiles())

    def OpenDIFiles(self):
        '''Open Demand Interval (DI) files'''
        self._check_for_error(self._lib.Meters_OpenAllDIFiles())

    def DIFilesAreOpen(self) -> bool:
        '''Indicates if Demand Interval (DI) files have been properly opened.'''
        return self._check_for_error(self._lib.Meters_Get_DIFilesAreOpen()) != 0

    def Totals(self) -> Float64Array:
        '''Returns the totals of all registers of all meters'''
        self._check_for_error(self._lib.Meters_Get_Totals_GR())
        return self._get_float64_gr_array()
    
