'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class IReclosers(Base):
    __slots__ = []

    def Close(self):
        self.lib.Reclosers_Close()

    def Open(self):
        self.lib.Reclosers_Open()

    @property
    def AllNames(self):
        '''(read-only) Array of strings with names of all Reclosers in Active Circuit'''
        return self.get_string_array(self.lib.Reclosers_Get_AllNames)

    @property
    def Count(self):
        '''(read-only) Number of Reclosers in active circuit.'''
        return self.lib.Reclosers_Get_Count()

    def __len__(self):
        return self.lib.Reclosers_Get_Count()

    @property
    def First(self):
        '''(read-only) Set First Recloser to be Active Ckt Element. Returns 0 if none.'''
        return self.lib.Reclosers_Get_First()

    @property
    def GroundInst(self):
        '''
        (read) Ground (3I0) instantaneous trip setting - curve multipler or actual amps.
        (write) Ground (3I0) trip instantaneous multiplier or actual amps
        '''
        return self.lib.Reclosers_Get_GroundInst()

    @GroundInst.setter
    def GroundInst(self, Value):
        self.lib.Reclosers_Set_GroundInst(Value)

    @property
    def GroundTrip(self):
        '''Ground (3I0) trip multiplier or actual amps'''
        return self.lib.Reclosers_Get_GroundTrip()

    @GroundTrip.setter
    def GroundTrip(self, Value):
        self.lib.Reclosers_Set_GroundTrip(Value)

    @property
    def MonitoredObj(self):
        '''
        (read) Full name of object this Recloser is monitoring.
        (write) Set monitored object by full name.
        '''
        return self.get_string(self.lib.Reclosers_Get_MonitoredObj())

    @MonitoredObj.setter
    def MonitoredObj(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.Reclosers_Set_MonitoredObj(Value)

    @property
    def MonitoredTerm(self):
        '''Terminal number of Monitored object for the Recloser '''
        return self.lib.Reclosers_Get_MonitoredTerm()

    @MonitoredTerm.setter
    def MonitoredTerm(self, Value):
        self.lib.Reclosers_Set_MonitoredTerm(Value)

    @property
    def Name(self):
        '''Get Name of active Recloser or set the active Recloser by name.'''
        return self.get_string(self.lib.Reclosers_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.Reclosers_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Iterate to the next recloser in the circuit. Returns zero if no more.'''
        return self.lib.Reclosers_Get_Next()

    @property
    def NumFast(self):
        '''Number of fast shots'''
        return self.lib.Reclosers_Get_NumFast()

    @NumFast.setter
    def NumFast(self, Value):
        self.lib.Reclosers_Set_NumFast(Value)

    @property
    def PhaseInst(self):
        '''Phase instantaneous curve multipler or actual amps'''
        return self.lib.Reclosers_Get_PhaseInst()

    @PhaseInst.setter
    def PhaseInst(self, Value):
        self.lib.Reclosers_Set_PhaseInst(Value)

    @property
    def PhaseTrip(self):
        '''
        (read) Phase trip curve multiplier or actual amps
        (write) Phase Trip multiplier or actual amps
        '''
        return self.lib.Reclosers_Get_PhaseTrip()

    @PhaseTrip.setter
    def PhaseTrip(self, Value):
        self.lib.Reclosers_Set_PhaseTrip(Value)

    @property
    def RecloseIntervals(self):
        '''(read-only) Variant Array of Doubles: reclose intervals, s, between shots.'''
        self.lib.Reclosers_Get_RecloseIntervals_GR()
        return self.get_float64_gr_array()

    @property
    def Shots(self):
        '''Number of shots to lockout (fast + delayed)'''
        return self.lib.Reclosers_Get_Shots()

    @Shots.setter
    def Shots(self, Value):
        self.lib.Reclosers_Set_Shots(Value)

    @property
    def SwitchedObj(self):
        '''Full name of the circuit element that is being switched by the Recloser.'''
        return self.get_string(self.lib.Reclosers_Get_SwitchedObj())

    @SwitchedObj.setter
    def SwitchedObj(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.Reclosers_Set_SwitchedObj(Value)

    @property
    def SwitchedTerm(self):
        '''Terminal number of the controlled device being switched by the Recloser'''
        return self.lib.Reclosers_Get_SwitchedTerm()

    @SwitchedTerm.setter
    def SwitchedTerm(self, Value):
        self.lib.Reclosers_Set_SwitchedTerm(Value)

    @property
    def idx(self):
        '''Get/Set the active Recloser by index into the recloser list.  1..Count'''
        return self.lib.Reclosers_Get_idx()

    @idx.setter
    def idx(self, Value):
        self.lib.Reclosers_Set_idx(Value)

    def __iter__(self):
        idx = self.First
        while idx != 0:
            yield self
            idx = self.Next


