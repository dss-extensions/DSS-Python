'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class IBus(Base):
    __slots__ = []

    def GetUniqueNodeNumber(self, StartNumber):
        return self._lib.Bus_GetUniqueNodeNumber(StartNumber)

    def ZscRefresh(self):
        return self._lib.Bus_ZscRefresh() != 0

    @property
    def Coorddefined(self):
        '''(read-only) False=0 else True. Indicates whether a coordinate has been defined for this bus'''
        return self._lib.Bus_Get_Coorddefined() != 0

    @property
    def CplxSeqVoltages(self):
        '''(read-only) Complex Double array of Sequence Voltages (0, 1, 2) at this Bus.'''
        self._lib.Bus_Get_CplxSeqVoltages_GR()
        return self._get_float64_gr_array()

    @property
    def Cust_Duration(self):
        '''(read-only) Accumulated customer outage durations'''
        return self._lib.Bus_Get_Cust_Duration()

    @property
    def Cust_Interrupts(self):
        '''(read-only) Annual number of customer-interruptions from this bus'''
        return self._lib.Bus_Get_Cust_Interrupts()

    @property
    def Distance(self):
        '''(read-only) Distance from energymeter (if non-zero)'''
        return self._lib.Bus_Get_Distance()

    @property
    def Int_Duration(self):
        '''(read-only) Average interruption duration, hr.'''
        return self._lib.Bus_Get_Int_Duration()

    @property
    def Isc(self):
        '''(read-only) Short circuit currents at bus; Complex Array.'''
        self._lib.Bus_Get_Isc_GR()
        return self._get_float64_gr_array()

    @property
    def Lambda(self):
        '''(read-only) Accumulated failure rate downstream from this bus; faults per year'''
        return self._lib.Bus_Get_Lambda()

    @property
    def N_Customers(self):
        '''(read-only) Total numbers of customers served downline from this bus'''
        return self._lib.Bus_Get_N_Customers()

    @property
    def N_interrupts(self):
        '''(read-only) Number of interruptions this bus per year'''
        return self._lib.Bus_Get_N_interrupts()

    @property
    def Name(self):
        '''(read-only) Name of Bus'''
        return self._get_string(self._lib.Bus_Get_Name())

    @property
    def Nodes(self):
        '''(read-only) Integer Array of Node Numbers defined at the bus in same order as the voltages.'''
        self._lib.Bus_Get_Nodes_GR()
        return self._get_int32_gr_array()

    @property
    def NumNodes(self):
        '''(read-only) Number of Nodes this bus.'''
        return self._lib.Bus_Get_NumNodes()

    @property
    def SectionID(self):
        '''(read-only) Integer ID of the feeder section in which this bus is located.'''
        return self._lib.Bus_Get_SectionID()

    @property
    def SeqVoltages(self):
        '''(read-only) Double Array of sequence voltages at this bus.'''
        self._lib.Bus_Get_SeqVoltages_GR()
        return self._get_float64_gr_array()

    @property
    def TotalMiles(self):
        '''(read-only) Total length of line downline from this bus, in miles. For recloser siting algorithm.'''
        return self._lib.Bus_Get_TotalMiles()

    @property
    def VLL(self):
        '''(read-only) For 2- and 3-phase buses, returns array of complex numbers represetin L-L voltages in volts. Returns -1.0 for 1-phase bus. If more than 3 phases, returns only first 3.'''
        self._lib.Bus_Get_VLL_GR()
        return self._get_float64_gr_array()

    @property
    def VMagAngle(self):
        '''(read-only) Variant Array of doubles containing voltages in Magnitude (VLN), angle (deg) '''
        self._lib.Bus_Get_VMagAngle_GR()
        return self._get_float64_gr_array()

    @property
    def Voc(self):
        '''(read-only) Open circuit voltage; Complex array.'''
        self._lib.Bus_Get_Voc_GR()
        return self._get_float64_gr_array()

    @property
    def Voltages(self):
        '''(read-only) Complex array of voltages at this bus.'''
        self._lib.Bus_Get_Voltages_GR()
        return self._get_float64_gr_array()

    @property
    def YscMatrix(self):
        '''(read-only) Complex array of Ysc matrix at bus. Column by column.'''
        self._lib.Bus_Get_YscMatrix_GR()
        return self._get_float64_gr_array()

    @property
    def Zsc0(self):
        '''(read-only) Complex Zero-Sequence short circuit impedance at bus.'''
        self._lib.Bus_Get_Zsc0_GR()
        return self._get_float64_gr_array()

    @property
    def Zsc1(self):
        '''(read-only) Complex Positive-Sequence short circuit impedance at bus..'''
        self._lib.Bus_Get_Zsc1_GR()
        return self._get_float64_gr_array()

    @property
    def ZscMatrix(self):
        '''(read-only) Complex array of Zsc matrix at bus. Column by column.'''
        self._lib.Bus_Get_ZscMatrix_GR()
        return self._get_float64_gr_array()

    @property
    def kVBase(self):
        '''(read-only) Base voltage at bus in kV'''
        return self._lib.Bus_Get_kVBase()

    @property
    def puVLL(self):
        '''(read-only) Returns Complex array of pu L-L voltages for 2- and 3-phase buses. Returns -1.0 for 1-phase bus. If more than 3 phases, returns only 3 phases.'''
        self._lib.Bus_Get_puVLL_GR()
        return self._get_float64_gr_array()

    @property
    def puVmagAngle(self):
        '''(read-only) Array of doubles containig voltage magnitude, angle pairs in per unit'''
        self._lib.Bus_Get_puVmagAngle_GR()
        return self._get_float64_gr_array()

    @property
    def puVoltages(self):
        '''(read-only) Complex Array of pu voltages at the bus.'''
        self._lib.Bus_Get_puVoltages_GR()
        return self._get_float64_gr_array()

    @property
    def x(self):
        '''X Coordinate for bus (double)'''
        return self._lib.Bus_Get_x()

    @x.setter
    def x(self, Value):
        self._lib.Bus_Set_x(Value)
        self.CheckForError()

    @property
    def y(self):
        '''Y coordinate for bus(double)'''
        return self._lib.Bus_Get_y()

    @y.setter
    def y(self, Value):
        self._lib.Bus_Set_y(Value)
        self.CheckForError()

    def __getitem__(self, index):
        if isinstance(index, int):
            # bus index is zero based, pass it directly
            self._lib.Circuit_SetActiveBusi(index)
        else:
            if type(index) is not bytes:
                index = index.encode(self._api_util.codec)

            self._lib.Circuit_SetActiveBus(index)

        return self

    def __call__(self, index):
        return self.__getitem__(index)

    def __iter__(self):
        n = self._lib.Circuit_SetActiveBusi(0)
        while n == 0:
            yield self
            n = self._lib.Bus_Get_Next()
