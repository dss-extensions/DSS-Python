# Copyright (c) 2023 Paulo Meira
# Copyright (c) 2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from dss.enums import DSSJSONFlags
from .types import Float64Array, Int32Array, ComplexArray
from .common import Base, InvalidatedBus
from .PCElement import PCElementBatch
from .PDElement import PDElementBatch
from .Load import LoadBatch
from .Line import LineBatch

class Bus:
    __slots__ = (
        '_ptr',
        '_lib',
        '_get_fcomplex128_array',
        '_get_float64_array',
        '_get_int32_array',
        '_get_string',
        '_api_util',
        '__weakref__',
    )
    
    def _invalidate_ptr(self):
        self._ptr = InvalidatedBus

    def __init__(self, api_util, ptr):
        self._get_float64_array = api_util.get_float64_array
        self._get_fcomplex128_array = api_util.get_fcomplex128_array
        self._get_int32_array = api_util.get_int32_array
        self._get_string = api_util.get_string
        self._lib = api_util.lib
        self._ptr = ptr
        self._api_util = api_util
        api_util.track_obj(self)

    def __repr__(self):
        return f'<Bus.{self.Name}>'

    def GetUniqueNodeNumber(self, startNumber: int) -> int:
        return self._lib.Alt_Bus_GetUniqueNodeNumber(self._ptr, startNumber)

    def ZscRefresh(self) -> bool:
        '''Refreshes the Zsc matrix for this bus.'''
        return self._lib.Alt_Bus_ZscRefresh(self._ptr) != 0

    @property
    def CoordDefined(self) -> bool:
        '''Indicates whether a coordinate has been defined for this bus.'''
        return self._lib.Alt_Bus_Get_CoordDefined(self._ptr) != 0

    @property
    def ComplexSeqVoltages(self) -> ComplexArray:
        '''Array of complex numbers, sequence voltages (0, 1, 2) at this bus.'''
        return self._get_fcomplex128_array(self._lib.Alt_Bus_Get_ComplexSeqVoltages, self._ptr)

    @property
    def CustDuration(self) -> float:
        '''Accumulated customer outage durations.'''
        return self._lib.Alt_Bus_Get_CustDuration(self._ptr)

    @property
    def CustInterrupts(self) -> float:
        '''Annual number of customer-interruptions from this bus.'''
        return self._lib.Alt_Bus_Get_CustInterrupts(self._ptr)

    @property
    def Distance(self) -> float:
        '''Distance from energymeter (if non-zero)'''
        return self._lib.Alt_Bus_Get_Distance(self._ptr)

    @property
    def IntDuration(self) -> float:
        '''Average interruption duration, hr.'''
        return self._lib.Alt_Bus_Get_IntDuration(self._ptr)

    @property
    def Isc(self) -> ComplexArray:
        '''Short circuit currents at bus; Complex Array.'''
        return self._get_fcomplex128_array(self._lib.Alt_Bus_Get_Isc, self._ptr)

    @property
    def Lambda(self) -> float:
        '''Accumulated failure rate downstream from this bus; faults per year'''
        return self._lib.Alt_Bus_Get_Lambda(self._ptr)

    @property
    def NumCustomers(self) -> int:
        '''Total numbers of customers served downline from this bus'''
        return self._lib.Alt_Bus_Get_N_Customers(self._ptr)

    @property
    def NumInterrupts(self) -> float:
        '''Number of interruptions on this bus per year'''
        return self._lib.Alt_Bus_Get_N_interrupts(self._ptr)

    @property
    def Name(self) -> str:
        '''Name of Bus'''
        return self._get_string(self._lib.Alt_Bus_Get_Name(self._ptr))

    @property
    def Nodes(self) -> Int32Array:
        '''Integer Array of Node Numbers defined at the bus in same order as the voltages.'''
        return self._get_int32_array(self._lib.Alt_Bus_Get_Nodes, self._ptr)

    @property
    def NumNodes(self) -> int:
        '''Number of Nodes this bus.'''
        return self._lib.Alt_Bus_Get_NumNodes(self._ptr)

    @property
    def SectionID(self) -> int:
        '''Integer ID of the feeder section in which this bus is located.'''
        return self._lib.Alt_Bus_Get_SectionID(self._ptr)

    @property
    def SeqVoltages(self) -> Float64Array:
        '''Array of sequence voltages at this bus. Magnitudes only.'''
        return self._get_float64_array(self._lib.Alt_Bus_Get_SeqVoltages, self._ptr)

    @property
    def TotalMiles(self) -> float:
        '''Total length of line downline from this bus, in miles. For recloser siting algorithm.'''
        return self._lib.Alt_Bus_Get_TotalMiles(self._ptr)

    @property
    def TotalKilometers(self) -> float:
        '''Total length of line downline from this bus, in kilometers.'''
        return self._lib.Alt_Bus_Get_TotalMiles(self._ptr) * 1.609344

    @property
    def VLL(self) -> ComplexArray:
        '''For 2- and 3-phase buses, returns array of complex numbers represetin L-L voltages in volts. Returns -1.0 for 1-phase bus. If more than 3 phases, returns only first 3.'''
        return self._get_fcomplex128_array(self._lib.Alt_Bus_Get_VLL, self._ptr)

    @property
    def VMagAngle(self) -> Float64Array:
        '''Array of doubles containing voltages in Magnitude (VLN), angle (degrees) '''
        return self._get_float64_array(self._lib.Alt_Bus_Get_VMagAngle, self._ptr)

    @property
    def Voc(self) -> ComplexArray:
        '''Open circuit voltage; Complex array.'''
        return self._get_fcomplex128_array(self._lib.Alt_Bus_Get_Voc_GR, self._ptr)

    @property
    def Voltages(self) -> ComplexArray:
        '''Complex array of voltages at this bus.'''
        return self._get_complex128_array(self._lib.Alt_Bus_Get_Voltages, self._ptr)

    @property
    def YscMatrix(self) -> ComplexArray:
        '''Complex array of Ysc matrix at bus. Column by column.'''
        return self._get_complex128_array(self._lib.Alt_Bus_Get_YscMatrix, self._ptr)

    @property
    def Zsc0(self) -> complex:
        '''Complex Zero-Sequence short circuit impedance at bus.'''
        return self._get_fcomplex128_simple(self._lib.Alt_Bus_Get_Zsc0, self._ptr)

    @property
    def Zsc1(self) -> complex:
        '''Complex Positive-Sequence short circuit impedance at bus.'''
        return self._get_fcomplex128_simple(self._lib.Alt_Bus_Get_Zsc1, self._ptr)

    @property
    def ZscMatrix(self) -> ComplexArray:
        '''Complex array of Zsc matrix at bus. Column by column.'''
        return self._get_fcomplex128_array(self._lib.Alt_Bus_Get_ZscMatrix, self._ptr)

    @property
    def kVBase(self) -> float:
        '''Base voltage at bus in kV'''
        return self._lib.Alt_Bus_Get_kVBase(self._ptr)

    @property
    def puVLL(self) -> ComplexArray:
        '''Returns Complex array of pu L-L voltages for 2- and 3-phase buses. Returns -1.0 for 1-phase bus. If more than 3 phases, returns only 3 phases.'''
        return self._get_fcomplex128_array(self._lib.Alt_Bus_Get_puVLL, self._ptr)

    @property
    def puVmagAngle(self) -> Float64Array:
        '''Array of doubles containing voltage magnitude, angle (degrees) pairs in per unit'''
        return self._get_float64_array(self._lib.Alt_Bus_Get_puVmagAngle, self._ptr)

    @property
    def puVoltages(self) -> ComplexArray:
        '''Complex Array of pu voltages at the bus.'''
        return self._get_fcomplex128_array(self._lib.Alt_Bus_Get_puVoltages, self._ptr)

    @property
    def Zsc012Matrix(self) -> ComplexArray:
        '''
        Array of doubles (complex) containing the complete 012 Zsc matrix. 
        Only available after Zsc is computed, either through the "ZscRefresh" command, or running a "FaultStudy" solution.
        Only available for buses with 3 nodes. 
        '''
        return self._get_fcomplex128_array(self._lib.Alt_Bus_Get_Zsc012Matrix, self._ptr)

    @property
    def X(self) -> float:
        '''X Coordinate for bus'''
        return self._lib.Alt_Bus_Get_X(self._ptr)

    @X.setter
    def X(self, value: float):
        self._lib.Alt_Bus_Set_X(self._ptr, value)

    @property
    def Y(self) -> float:
        '''Y coordinate for bus'''
        return self._lib.Alt_Bus_Get_Y(self._ptr)

    @Y.setter
    def Y(self, value: float):
        self._lib.Alt_Bus_Set_Y(self._ptr, value)

    def Loads(self) -> LoadBatch:
        '''Batch of load objects connected to this bus.'''
        return LoadBatch(self._api_util, from_func=(self._lib.Alt_Bus_Get_Loads, self._ptr))
    
    def Lines(self) -> LineBatch:
        '''Batch of line objects connected to this bus.'''
        return LineBatch(self._api_util, from_func=(self._lib.Alt_Bus_Get_Lines, self._ptr))

    def PCElements(self) -> PCElementBatch:
        '''Batch of all PC elements connected to this bus.'''
        return PCElementBatch(self._lib.Alt_Bus_Get_PCElements, self, copy_safe=True)

    def PDElements(self) -> PDElementBatch:
        '''Batch of all PD elements connected to this bus.'''
        return PDElementBatch(self._lib.Alt_Bus_Get_PDElements, self, copy_safe=True)

    def to_json(self, options: Union[int, DSSJSONFlags] = 0):
        '''
        Returns the data of this bus as a JSON-encoded string.

        Currently, only the basic data is included (name, coordinates, base voltage).
        '''
        s = self._api_util.ffi.gc(self._lib.Alt_Bus_ToJSON(self._ptr, options), self._lib.DSS_Dispose_String)
        return self._get_string(s)
        


class BusBatch(Base):
    def ZscRefresh(self) -> bool:
        '''
        Refreshes the Zsc matrix for all buses in the batch
        '''
        ptrList, cnt = self._get_ptr_cnt()
        res = True
        for n in range(cnt):
            res = res and (self._lib.Alt_Bus_ZscRefresh(ptrList[n]) != 0)
            
        return res

    def _busbatch_float64(self, fname: str):
        return self._get_float64_array(
            self._lib.Alt_BusBatch_GetFloat64FromFunc, 
            *self._get_ptr_cnt(),
            self._ffi.addressof(self._api_util.lib_unpatched, fname)
        )

    def _busbatch_int32(self, fname: str):
        return self._get_int32_array(
            self._lib.Alt_BusBatch_GetInt32FromFunc, 
            *self._get_ptr_cnt(),
            self._ffi.addressof(self._api_util.lib_unpatched, fname)
        )

    def X(self) -> Float64Array:
        '''For each bus in the batch: get x coordinate'''
        return self._busbatch_float64('Alt_Bus_Get_X')

    def Y(self) -> Float64Array:
        '''For each bus in the batch: get y coordinate'''
        return self._busbatch_float64('Alt_Bus_Get_Y')

    def CustDuration(self) -> Float64Array:
        '''For each bus in the batch: accumulated customer outage durations for the bus.'''
        return self._busbatch_float64('Alt_Bus_Get_CustDuration')

    def CustInterrupts(self) -> Float64Array:
        '''For each bus in the batch: annual number of customer-interruptions from the bus.'''
        return self._busbatch_float64('Alt_Bus_Get_CustInterrupts')

    def Distance(self) -> Float64Array:
        '''For each bus in the batch: distance from energymeter (if non-zero)'''
        return self._busbatch_float64('Alt_Bus_Get_Distance')

    def IntDuration(self) -> Float64Array:
        '''For each bus in the batch: average interruption duration, hours.'''
        return self._busbatch_float64('Alt_Bus_Get_IntDuration')
    
    def Lambda(self) -> Float64Array:
        '''For each bus in the batch: accumulated failure rate downstream from the bus; faults per year'''
        return self._busbatch_float64('Alt_Bus_Get_Lambda')

    def NumCustomers(self) -> Int32Array:
        '''For each bus in the batch: total numbers of customers served downline from the bus'''
        return self._busbatch_int32('Alt_Bus_Get_N_Customers')

    def NumInterrupts(self) -> Float64Array:
        '''For each bus in the batch: number of interruptions on the bus per year'''
        return self._busbatch_float64('Alt_Bus_Get_N_interrupts')

    def NumNodes(self) -> Int32Array:
        '''For each bus in the batch: number of nodes in the bus.'''
        return self._busbatch_int32('Alt_Bus_Get_NumNodes')

    def SectionID(self) -> Int32Array:
        '''For each bus in the batch: integer ID of the feeder section in which the bus is located.'''
        return self._busbatch_int32('Alt_Bus_Get_SectionID')

    def TotalMiles(self) -> Float64Array:
        '''For each bus in the batch: total length of line downline from the bus, in miles. For recloser siting algorithm.'''
        return self._busbatch_float64('Alt_Bus_Get_TotalMiles')

    def TotalKilometers(self) -> Float64Array:
        '''For each bus in the batch: total length of line downline from the bus, in kilometers.'''
        return self._busbatch_float64('Alt_Bus_Get_TotalMiles') * 1.609344

    def kVBase(self) -> Float64Array:
        '''For each bus in the batch: base voltage in kV'''
        return self._busbatch_float64('Alt_Bus_Get_kVBase')

    def _get_ptr_cnt(self):
        return self._ptr, self._cnt

    def __getitem__(self, index: int) -> Bus:
        if index >= 0 and index < self._cnt:
            return Bus(self._api_util, self._ptr[index])
        
        raise IndexError('Invalid bus index inside the batch')

    def __call__(self, index: Union[int, str]) -> Bus:
        return self.__getitem__(index)

    def __len__(self):
        '''Total number of buses in the circuit.'''
        return self._lib.Circuit_Get_NumBuses()
    
    def __iter__(self):
        ptrList, cnt = self._get_ptr_cnt()
        for n in range(cnt):
            yield Bus(self._api_util, ptrList[n])

    def to_json(self, options: Union[int, DSSJSONFlags] = 0):
        '''
        Returns the data of the buses in this batch as a JSON-encoded string.

        Currently, only the basic data is included (name, coordinates, base voltage).
        '''
        s = self._api_util.ffi.gc(self._lib.Alt_BusBatch_ToJSON(*self._get_ptr_cnt(), options), self._lib.DSS_Dispose_String)
        return self._get_string(s)


class IBuses(BusBatch):
    '''
    This is the general bus container, encapsulating operations on **all** buses.
    Use it to find, iterate and operate on individual buses, or extract data from
    all buses.
    '''
    def _get_ptr_cnt(self):
        return self._lib.Alt_Bus_GetListPtr(), self._lib.Circuit_Get_NumBuses()

    def __getitem__(self, index: Union[int, str]) -> Bus:
        if isinstance(index, int):
            # bus index is zero based (externally), pass it directly
            return Bus(self._api_util, self._lib.Alt_Bus_GetByIndex(index))
        else:
            if type(index) is not bytes:
                index = index.encode(self._api_util.codec)

            return Bus(self._api_util, self._lib.Alt_Bus_GetByName(index))

    def __len__(self):
        '''Total number of buses in the circuit.'''
        return self._lib.Circuit_Get_NumBuses()
    
    def find(self, index_or_name: Union[int, str]) -> Bus:
        '''
        Returns a bus object for the selected index or name.
        
        Also available as `Buses[index]`.
        '''
        return self[index_or_name]

