# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from __future__ import annotations
from ._cffi_api_util import Base
from ._types import Float64Array, Float64ArrayOrComplexArray, Float64ArrayOrSimpleComplex, Int32Array
from typing import List, Union, Iterator

class IBus(Base):
    __slots__ = []
    
    _columns = [
        'Name',
        'NumNodes',
        'Nodes',
        'Coorddefined',
        'CplxSeqVoltages',
        'Cust_Duration',
        'Cust_Interrupts',
        'Cust_Interrupts',
        'Distance',
        'Int_Duration',
        'Isc',
        'Lambda',
        'N_Customers',
        'N_interrupts',
        'SectionID',
        'SeqVoltages',
        'TotalMiles',
        'VLL',
        'VMagAngle',
        'Voc',
        'Voltages',
        'YscMatrix',
        'Zsc0',
        'Zsc1',
        'ZscMatrix',
        'kVBase',
        'puVLL',
        'puVmagAngle',
        'puVoltages',
        'x',
        'y',
        'AllPCEatBus',
        'AllPDEatBus'
    ]

    def GetUniqueNodeNumber(self, StartNumber: int) -> int:
        '''
        Return a unique node number at the active bus to avoid node collisions and adds 
        it to the node list for the bus.

        Original COM help: https://opendss.epri.com/GetUniqueNodeNumber.html
        '''
        return self._check_for_error(self._lib.Bus_GetUniqueNodeNumber(StartNumber))

    def ZscRefresh(self) -> bool:
        '''
        Refreshes the Zsc matrix for the active bus.

        Original COM help: https://opendss.epri.com/ZscRefresh.html
        '''
        return self._check_for_error(self._lib.Bus_ZscRefresh()) != 0

    @property
    def Coorddefined(self) -> bool:
        '''
        Indicates whether a coordinate has been defined for this bus

        Original COM help: https://opendss.epri.com/Coorddefined.html
        '''
        return self._check_for_error(self._lib.Bus_Get_Coorddefined()) != 0

    @property
    def CplxSeqVoltages(self) -> Float64ArrayOrComplexArray:
        '''
        Complex Double array of Sequence Voltages (0, 1, 2) at this Bus.

        Original COM help: https://opendss.epri.com/CplxSeqVoltages.html
        '''
        self._check_for_error(self._lib.Bus_Get_CplxSeqVoltages_GR())
        return self._get_complex128_gr_array()

    @property
    def Cust_Duration(self) -> float:
        '''
        Accumulated customer outage durations

        Original COM help: https://opendss.epri.com/Cust_Duration.html
        '''
        return self._check_for_error(self._lib.Bus_Get_Cust_Duration())

    @property
    def Cust_Interrupts(self) -> float:
        '''
        Annual number of customer-interruptions from this bus

        Original COM help: https://opendss.epri.com/Cust_Interrupts.html
        '''
        return self._check_for_error(self._lib.Bus_Get_Cust_Interrupts())

    @property
    def Distance(self) -> float:
        '''
        Distance from energymeter (if non-zero)

        Original COM help: https://opendss.epri.com/Distance.html
        '''
        return self._check_for_error(self._lib.Bus_Get_Distance())

    @property
    def Int_Duration(self) -> float:
        '''
        Average interruption duration, hr.

        Original COM help: https://opendss.epri.com/Int_Duration.html
        '''
        return self._check_for_error(self._lib.Bus_Get_Int_Duration())

    @property
    def Isc(self) -> Float64ArrayOrComplexArray:
        '''
        Short circuit currents at bus; Complex Array.

        Original COM help: https://opendss.epri.com/Isc.html
        '''
        self._check_for_error(self._lib.Bus_Get_Isc_GR())
        return self._get_complex128_gr_array()

    @property
    def Lambda(self) -> float:
        '''
        Accumulated failure rate downstream from this bus; faults per year

        Original COM help: https://opendss.epri.com/Lambda.html
        '''
        return self._check_for_error(self._lib.Bus_Get_Lambda())

    @property
    def N_Customers(self) -> int:
        '''
        Total numbers of customers served downline from this bus

        Original COM help: https://opendss.epri.com/N_Customers.html
        '''
        return self._check_for_error(self._lib.Bus_Get_N_Customers())

    @property
    def N_interrupts(self) -> float:
        '''
        Number of interruptions this bus per year

        Original COM help: https://opendss.epri.com/N_interrupts.html
        '''
        return self._check_for_error(self._lib.Bus_Get_N_interrupts())

    @property
    def Name(self) -> str:
        '''
        Name of Bus

        Original COM help: https://opendss.epri.com/Name1.html
        '''
        return self._get_string(self._check_for_error(self._lib.Bus_Get_Name()))

    @property
    def Nodes(self) -> Int32Array:
        '''
        Integer Array of Node Numbers defined at the bus in same order as the voltages.

        Original COM help: https://opendss.epri.com/Nodes.html
        '''
        self._check_for_error(self._lib.Bus_Get_Nodes_GR())
        return self._get_int32_gr_array()

    @property
    def NumNodes(self) -> int:
        '''
        Number of Nodes this bus.

        Original COM help: https://opendss.epri.com/NumNodes.html
        '''
        return self._check_for_error(self._lib.Bus_Get_NumNodes())

    @property
    def SectionID(self) -> int:
        '''
        Integer ID of the feeder section in which this bus is located.

        Original COM help: https://opendss.epri.com/SectionID.html
        '''
        return self._check_for_error(self._lib.Bus_Get_SectionID())

    @property
    def SeqVoltages(self) -> Float64Array:
        '''
        Double Array of sequence voltages at this bus. Magnitudes only.

        Original COM help: https://opendss.epri.com/SeqVoltages.html
        '''
        self._check_for_error(self._lib.Bus_Get_SeqVoltages_GR())
        return self._get_float64_gr_array()

    @property
    def TotalMiles(self) -> float:
        '''
        Total length of line downline from this bus, in miles. For recloser siting algorithm.

        Original COM help: https://opendss.epri.com/TotalMiles.html
        '''
        return self._check_for_error(self._lib.Bus_Get_TotalMiles())

    @property
    def VLL(self) -> Float64ArrayOrComplexArray:
        '''
        For 2- and 3-phase buses, returns array of complex numbers representing L-L voltages in volts. Returns -1.0 for 1-phase bus. If more than 3 phases, returns only first 3.

        Original COM help: https://opendss.epri.com/VLL.html
        '''
        self._check_for_error(self._lib.Bus_Get_VLL_GR())
        return self._get_complex128_gr_array()

    @property
    def VMagAngle(self) -> Float64Array:
        '''
        Array of doubles containing voltages in Magnitude (VLN), angle (degrees) 

        Original COM help: https://opendss.epri.com/VMagAngle.html
        '''
        self._check_for_error(self._lib.Bus_Get_VMagAngle_GR())
        return self._get_float64_gr_array()

    @property
    def Voc(self) -> Float64ArrayOrComplexArray:
        '''
        Open circuit voltage; Complex array.

        Original COM help: https://opendss.epri.com/Voc.html
        '''
        self._check_for_error(self._lib.Bus_Get_Voc_GR())
        return self._get_complex128_gr_array()

    @property
    def Voltages(self) -> Float64ArrayOrComplexArray:
        '''
        Complex array of voltages at this bus.

        Original COM help: https://opendss.epri.com/Voltages.html
        '''
        self._check_for_error(self._lib.Bus_Get_Voltages_GR())
        return self._get_complex128_gr_array()

    @property
    def YscMatrix(self) -> Float64ArrayOrComplexArray:
        '''
        Complex array of Ysc matrix at bus. Column by column.

        Original COM help: https://opendss.epri.com/YscMatrix.html
        '''
        self._check_for_error(self._lib.Bus_Get_YscMatrix_GR())
        return self._get_complex128_gr_array()

    @property
    def Zsc0(self) -> Float64ArrayOrSimpleComplex:
        '''
        Complex Zero-Sequence short circuit impedance at bus.

        Original COM help: https://opendss.epri.com/Zsc0.html
        '''
        self._check_for_error(self._lib.Bus_Get_Zsc0_GR())
        return self._get_complex128_gr_simple()

    @property
    def Zsc1(self) -> Float64ArrayOrSimpleComplex:
        '''
        Complex Positive-Sequence short circuit impedance at bus.

        Original COM help: https://opendss.epri.com/Zsc1.html
        '''
        self._check_for_error(self._lib.Bus_Get_Zsc1_GR())
        return self._get_complex128_gr_simple()

    @property
    def ZscMatrix(self) -> Float64ArrayOrComplexArray:
        '''
        Complex array of Zsc matrix at bus. Column by column.

        Original COM help: https://opendss.epri.com/ZscMatrix.html
        '''
        self._check_for_error(self._lib.Bus_Get_ZscMatrix_GR())
        return self._get_complex128_gr_array()

    @property
    def kVBase(self) -> float:
        '''
        Base voltage at bus in kV

        Original COM help: https://opendss.epri.com/kVBase.html
        '''
        return self._check_for_error(self._lib.Bus_Get_kVBase())

    @property
    def puVLL(self) -> Float64ArrayOrComplexArray:
        '''
        Returns Complex array of pu L-L voltages for 2- and 3-phase buses. Returns -1.0 for 1-phase bus. If more than 3 phases, returns only 3 phases.

        Original COM help: https://opendss.epri.com/puVLL.html
        '''
        self._check_for_error(self._lib.Bus_Get_puVLL_GR())
        return self._get_complex128_gr_array()

    @property
    def puVmagAngle(self) -> Float64Array:
        '''
        Array of doubles containing voltage magnitude, angle (degrees) pairs in per unit

        Original COM help: https://opendss.epri.com/puVmagAngle.html
        '''
        self._check_for_error(self._lib.Bus_Get_puVmagAngle_GR())
        return self._get_float64_gr_array()

    @property
    def puVoltages(self) -> Float64ArrayOrComplexArray:
        '''
        Complex Array of pu voltages at the bus.

        Original COM help: https://opendss.epri.com/puVoltages.html
        '''
        self._check_for_error(self._lib.Bus_Get_puVoltages_GR())
        return self._get_complex128_gr_array()

    @property
    def ZSC012Matrix(self) -> Float64ArrayOrComplexArray:
        '''
        Array of doubles (complex) containing the complete 012 Zsc matrix. 
        Only available after Zsc is computed, either through the "ZscRefresh" command, or running a "FaultStudy" solution.
        Only available for buses with 3 nodes.

        Original COM help: https://opendss.epri.com/ZSC012Matrix.html
        '''
        self._check_for_error(self._lib.Bus_Get_ZSC012Matrix_GR())
        return self._get_complex128_gr_array()

    @property
    def x(self) -> float:
        '''
        X Coordinate for bus

        Original COM help: https://opendss.epri.com/x.html
        '''
        return self._check_for_error(self._lib.Bus_Get_x())

    @x.setter
    def x(self, Value: float):
        self._check_for_error(self._lib.Bus_Set_x(Value))

    @property
    def y(self) -> float:
        '''
        Y coordinate for bus

        Original COM help: https://opendss.epri.com/y.html
        '''
        return self._check_for_error(self._lib.Bus_Get_y())

    @y.setter
    def y(self, Value: float):
        self._check_for_error(self._lib.Bus_Set_y(Value))

    @property
    def LoadList(self) -> List[str]:
        '''
        List of strings: Full Names of LOAD elements connected to the active bus.

        Original COM help: https://opendss.epri.com/LoadList.html
        '''
        return self._check_for_error(self._get_string_array(self._lib.Bus_Get_LoadList))
    
    @property
    def LineList(self) -> List[str]:
        '''
        List of strings: Full Names of LINE elements connected to the active bus.

        Original COM help: https://opendss.epri.com/LineList.html
        '''
        return self._check_for_error(self._get_string_array(self._lib.Bus_Get_LineList))

    @property
    def AllPCEatBus(self) -> List[str]:
        '''
        Returns an array with the names of all PCE connected to the active bus

        Original COM help: https://opendss.epri.com/AllPCEatBus.html
        '''
        result = self._check_for_error(self._get_string_array(self._lib.Bus_Get_AllPCEatBus))
        if result:
            result.append('') #TODO: remove this -- added for full compatibility with COM
        else:
            result = ['None']

        return result

    @property
    def AllPDEatBus(self) -> List[str]:
        '''
        Returns an array with the names of all PDE connected to the active bus

        Original COM help: https://opendss.epri.com/AllPDEatBus1.html
        '''
        result = self._check_for_error(self._get_string_array(self._lib.Bus_Get_AllPDEatBus))
        if result:
            result.append('') #TODO: remove this -- added for full compatibility with COM
        else:
            result = ['None']

        return result

    def __getitem__(self, index: Union[int, str]) -> IBus:
        if isinstance(index, int):
            # bus index is zero based, pass it directly
            self._check_for_error(self._lib.Circuit_SetActiveBusi(index))
        else:
            if not isinstance(index, bytes):
                index = index.encode(self._api_util.codec)

            self._check_for_error(self._lib.Circuit_SetActiveBus(index))

        return self

    def __call__(self, index: Union[int, str]) -> IBus:
        return self.__getitem__(index)

    def __iter__(self) -> Iterator[IBus]:
        n = self._check_for_error(self._lib.Circuit_SetActiveBusi(0))
        while n == 0:
            yield self
            n = self._check_for_error(self._lib.Bus_Get_Next())

    def __len__(self) -> int:
        '''Total number of Buses in the circuit.'''
        return self._check_for_error(self._lib.Circuit_Get_NumBuses())
