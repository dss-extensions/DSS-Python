# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from __future__ import annotations
from ._cffi_api_util import Base
from typing import List, AnyStr, Iterator
from ._types import Float64Array, Int32Array, Float64ArrayOrComplexArray

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
    def AccumulatedL(self) -> float:
        '''
        Accumulated failure rate for this branch on downline

        Original COM help: https://opendss.epri.com/AccumulatedL.html
        '''
        return self._check_for_error(self._lib.PDElements_Get_AccumulatedL())

    @property
    def Count(self) -> int:
        '''
        Number of PD elements (including disabled elements)

        Original COM help: https://opendss.epri.com/Count12.html
        '''
        return self._check_for_error(self._lib.PDElements_Get_Count())

    def __len__(self) -> int:
        return self._check_for_error(self._lib.PDElements_Get_Count())

    @property
    def FaultRate(self) -> float:
        '''
        Get/Set Number of failures per year. 
        For LINE elements: Number of failures per unit length per year.
        '''
        return self._check_for_error(self._lib.PDElements_Get_FaultRate())

    @FaultRate.setter
    def FaultRate(self, Value: float):
        self._check_for_error(self._lib.PDElements_Set_FaultRate(Value))

    @property
    def First(self) -> int:
        '''
        (read-only) Set the first enabled PD element to be the active element.
        Returns 0 if none found.
        '''
        return self._check_for_error(self._lib.PDElements_Get_First())

    @property
    def FromTerminal(self) -> int:
        '''
        (read-only) Number of the terminal of active PD element that is on the "from" 
        side. This is set after the meter zone is determined.
        '''
        return self._check_for_error(self._lib.PDElements_Get_FromTerminal())

    @property
    def IsShunt(self) -> bool:
        '''
        (read-only) Boolean indicating of PD element should be treated as a shunt 
        element rather than a series element. Applies to Capacitor and Reactor 
        elements in particular.
        '''
        return self._check_for_error(self._lib.PDElements_Get_IsShunt()) != 0

    @property
    def Lambda(self) -> float:
        '''
        Failure rate for this branch. Faults per year including length of line.

        Original COM help: https://opendss.epri.com/Lambda1.html
        '''
        return self._check_for_error(self._lib.PDElements_Get_Lambda())

    @property
    def Name(self) -> str:
        '''
        Get/Set name of active PD Element. Returns null string if active element 
        is not PDElement type.
        '''
        return self._get_string(self._check_for_error(self._lib.PDElements_Get_Name()))

    @Name.setter
    def Name(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.PDElements_Set_Name(Value))

    @property
    def Next(self) -> int:
        '''
        (read-only) Advance to the next PD element in the circuit. Enabled elements 
        only. Returns 0 when no more elements.
        '''
        return self._check_for_error(self._lib.PDElements_Get_Next())

    @property
    def Numcustomers(self) -> int:
        '''
        Number of customers, this branch

        Original COM help: https://opendss.epri.com/Numcustomers.html
        '''
        return self._check_for_error(self._lib.PDElements_Get_Numcustomers())

    @property
    def ParentPDElement(self) -> int:
        '''
        (read-only) Sets the parent PD element to be the active circuit element.
        Returns 0 if no more elements upline.
        '''
        return self._check_for_error(self._lib.PDElements_Get_ParentPDElement())

    @property
    def RepairTime(self) -> float:
        '''
        Average repair time for this element in hours

        Original COM help: https://opendss.epri.com/RepairTime.html
        '''
        return self._check_for_error(self._lib.PDElements_Get_RepairTime())

    @RepairTime.setter
    def RepairTime(self, Value: float):
        self._check_for_error(self._lib.PDElements_Set_RepairTime(Value))

    @property
    def SectionID(self) -> int:
        '''
        Integer ID of the feeder section that this PDElement branch is part of

        Original COM help: https://opendss.epri.com/SectionID1.html
        '''
        return self._check_for_error(self._lib.PDElements_Get_SectionID())

    @property
    def TotalMiles(self) -> float:
        '''
        Total miles of line from this element to the end of the zone. For recloser siting algorithm.

        Original COM help: https://opendss.epri.com/TotalMiles1.html
        '''
        return self._check_for_error(self._lib.PDElements_Get_TotalMiles())

    @property
    def Totalcustomers(self) -> int:
        '''
        Total number of customers from this branch to the end of the zone

        Original COM help: https://opendss.epri.com/TotalCustomers1.html
        '''
        return self._check_for_error(self._lib.PDElements_Get_Totalcustomers())

    @property
    def pctPermanent(self) -> float:
        '''
        Get/Set percent of faults that are permanent (require repair). Otherwise, fault is assumed to be transient/temporary.

        Original COM help: https://opendss.epri.com/pctPermanent.html
        '''
        return self._check_for_error(self._lib.PDElements_Get_pctPermanent())

    @pctPermanent.setter
    def pctPermanent(self, Value: float):
        self._check_for_error(self._lib.PDElements_Set_pctPermanent(Value))

    def __iter__(self) -> Iterator[IPDElements]:
        idx = self.First
        while idx != 0:
            yield self
            idx = self.Next

    @property
    def AllNames(self) -> List[str]:
        '''
        Array of strings consisting of all PD element names.
        
        **(API Extension)**
        '''
        return self._check_for_error(self._get_string_array(self._lib.PDElements_Get_AllNames))

    def AllMaxCurrents(self, AllNodes: bool = False) -> Float64Array:
        '''
        Array of doubles with the maximum current across the conductors, for each PD 
        element.
        
        By default, only the *first terminal* is used for the maximum current, matching
        the behavior of the "export capacity" command. Pass `AllNodes=True` to 
        force the analysis to all terminals.
        
        See also: 
        https://sourceforge.net/p/electricdss/discussion/beginners/thread/da5b93ca/
        
        **(API Extension)**
        '''
        self._check_for_error(self._lib.PDElements_Get_AllMaxCurrents_GR(AllNodes))
        return self._get_float64_gr_array()

    def AllPctNorm(self, AllNodes: bool = False) -> Float64Array:
        '''
        Array of doubles with the maximum current across the conductors as a percentage 
        of the Normal Ampere Rating, for each PD element.

        By default, only the *first terminal* is used for the maximum current, matching
        the behavior of the "export capacity" command. Pass `AllNodes=True` to 
        force the analysis to all terminals.
        
        See also: 
        https://sourceforge.net/p/electricdss/discussion/beginners/thread/da5b93ca/
        
        **(API Extension)**
        '''
        self._check_for_error(self._lib.PDElements_Get_AllPctNorm_GR(AllNodes))
        return self._get_float64_gr_array()

    def AllPctEmerg(self, AllNodes: bool = False) -> Float64Array:
        '''
        Array of doubles with the maximum current across the conductors as a percentage
        of the Emergency Ampere Rating, for each PD element.

        By default, only the *first terminal* is used for the maximum current, matching
        the behavior of the "export capacity" command. Pass `AllNodes=True` to 
        force the analysis to all terminals.
        
        See also: 
        https://sourceforge.net/p/electricdss/discussion/beginners/thread/da5b93ca/
        
        **(API Extension)**
        '''
        self._check_for_error(self._lib.PDElements_Get_AllPctEmerg_GR(AllNodes))
        return self._get_float64_gr_array()

    @property
    def AllCurrents(self) -> Float64ArrayOrComplexArray:
        '''
        Complex array of currents for all conductors, all terminals, for each PD element.
        
        **(API Extension)**
        '''
        self._check_for_error(self._lib.PDElements_Get_AllCurrents_GR())
        return self._get_complex128_gr_array()

    @property
    def AllCurrentsMagAng(self) -> Float64Array:
        '''
        Complex array (magnitude and angle format) of currents for all conductors, all terminals, for each PD element.
        
        **(API Extension)**
        '''
        self._check_for_error(self._lib.PDElements_Get_AllCurrentsMagAng_GR())
        return self._get_float64_gr_array()

    @property
    def AllCplxSeqCurrents(self) -> Float64ArrayOrComplexArray:
        '''
        Complex double array of Sequence Currents for all conductors of all terminals, for each PD elements.

        **(API Extension)**
        '''
        self._check_for_error(self._lib.PDElements_Get_AllCplxSeqCurrents_GR())
        return self._get_complex128_gr_array()

    @property
    def AllSeqCurrents(self) -> Float64Array:
        '''
        Double array of the symmetrical component currents (magnitudes only) into each 3-phase terminal, for each PD element.
        
        **(API Extension)**
        '''
        self._check_for_error(self._lib.PDElements_Get_AllSeqCurrents_GR())
        return self._get_float64_gr_array()

    @property
    def AllPowers(self) -> Float64ArrayOrComplexArray:
        '''
        Complex array of powers into each conductor of each terminal, for each PD element.
        
        **(API Extension)**
        '''
        self._check_for_error(self._lib.PDElements_Get_AllPowers_GR())
        return self._get_complex128_gr_array()

    @property
    def AllSeqPowers(self) -> Float64ArrayOrComplexArray:
        '''
        Complex array of sequence powers into each 3-phase terminal, for each PD element
        
        **(API Extension)**
        '''
        self._check_for_error(self._lib.PDElements_Get_AllSeqPowers_GR())
        return self._get_complex128_gr_array()

    @property
    def AllNumPhases(self) -> Int32Array:
        '''
        Integer array listing the number of phases of all PD elements
        
        **(API Extension)**
        '''
        self._check_for_error(self._lib.PDElements_Get_AllNumPhases_GR())
        return self._get_int32_gr_array()

    @property
    def AllNumConductors(self) -> Int32Array:
        '''
        Integer array listing the number of conductors of all PD elements
        
        **(API Extension)**
        '''
        self._check_for_error(self._lib.PDElements_Get_AllNumConductors_GR())
        return self._get_int32_gr_array()


    @property
    def AllNumTerminals(self) -> Int32Array:
        '''
        Integer array listing the number of terminals of all PD elements
        
        **(API Extension)**
        '''
        self._check_for_error(self._lib.PDElements_Get_AllNumTerminals_GR())
        return self._get_int32_gr_array()


