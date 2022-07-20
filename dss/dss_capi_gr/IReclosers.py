'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira
Copyright (c) 2018-2022 DSS Extensions contributors
'''
from .._cffi_api_util import Iterable

class IReclosers(Iterable):
    __slots__ = []

    _columns = [
        'Name',
        'idx',
        'GroundInst',
        'GroundTrip',
        'MonitoredObj',
        'MonitoredTerm',
        'SwitchedObj',
        'SwitchedTerm',
        'NumFast',
        'PhaseInst',
        'PhaseTrip',
        'RecloseIntervals',
        'Shots',
        'State',
        'NormalState',
    ]

    def Close(self):
        self.CheckForError(self._lib.Reclosers_Close())

    def Open(self):
        self.CheckForError(self._lib.Reclosers_Open())

    @property
    def GroundInst(self):
        '''Ground (3I0) instantaneous trip setting - curve multipler or actual amps.'''
        return self.CheckForError(self._lib.Reclosers_Get_GroundInst())

    @GroundInst.setter
    def GroundInst(self, Value):
        self.CheckForError(self._lib.Reclosers_Set_GroundInst(Value))

    @property
    def GroundTrip(self):
        '''Ground (3I0) trip multiplier or actual amps'''
        return self.CheckForError(self._lib.Reclosers_Get_GroundTrip())

    @GroundTrip.setter
    def GroundTrip(self, Value):
        self.CheckForError(self._lib.Reclosers_Set_GroundTrip(Value))

    @property
    def MonitoredObj(self):
        '''Full name of object this Recloser to be monitored.'''
        return self._get_string(self.CheckForError(self._lib.Reclosers_Get_MonitoredObj()))

    @MonitoredObj.setter
    def MonitoredObj(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Reclosers_Set_MonitoredObj(Value))

    @property
    def MonitoredTerm(self):
        '''Terminal number of Monitored object for the Recloser '''
        return self.CheckForError(self._lib.Reclosers_Get_MonitoredTerm())

    @MonitoredTerm.setter
    def MonitoredTerm(self, Value):
        self.CheckForError(self._lib.Reclosers_Set_MonitoredTerm(Value))

    @property
    def NumFast(self):
        '''Number of fast shots'''
        return self.CheckForError(self._lib.Reclosers_Get_NumFast())

    @NumFast.setter
    def NumFast(self, Value):
        self.CheckForError(self._lib.Reclosers_Set_NumFast(Value))

    @property
    def PhaseInst(self):
        '''Phase instantaneous curve multipler or actual amps'''
        return self.CheckForError(self._lib.Reclosers_Get_PhaseInst())

    @PhaseInst.setter
    def PhaseInst(self, Value):
        self.CheckForError(self._lib.Reclosers_Set_PhaseInst(Value))

    @property
    def PhaseTrip(self):
        '''Phase trip curve multiplier or actual amps'''
        return self.CheckForError(self._lib.Reclosers_Get_PhaseTrip())

    @PhaseTrip.setter
    def PhaseTrip(self, Value):
        self.CheckForError(self._lib.Reclosers_Set_PhaseTrip(Value))

    @property
    def RecloseIntervals(self):
        '''(read-only) Array of Doubles: reclose intervals, s, between shots.'''
        self.CheckForError(self._lib.Reclosers_Get_RecloseIntervals_GR())
        return self._get_float64_gr_array()

    @property
    def Shots(self):
        '''Number of shots to lockout (fast + delayed)'''
        return self.CheckForError(self._lib.Reclosers_Get_Shots())

    @Shots.setter
    def Shots(self, Value):
        self.CheckForError(self._lib.Reclosers_Set_Shots(Value))

    @property
    def SwitchedObj(self):
        '''Full name of the circuit element that is being switched by the Recloser.'''
        return self._get_string(self.CheckForError(self._lib.Reclosers_Get_SwitchedObj()))

    @SwitchedObj.setter
    def SwitchedObj(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Reclosers_Set_SwitchedObj(Value))

    @property
    def SwitchedTerm(self):
        '''Terminal number of the controlled device being switched by the Recloser'''
        return self.CheckForError(self._lib.Reclosers_Get_SwitchedTerm())

    @SwitchedTerm.setter
    def SwitchedTerm(self, Value):
        self.CheckForError(self._lib.Reclosers_Set_SwitchedTerm(Value))


    def Reset(self):
        '''
        Reset recloser to normal state. 
        If open, lock out the recloser. 
        If closed, resets recloser to first operation.
        '''
        self.CheckForError(self._lib.Reclosers_Reset())

    @property
    def State(self):
        '''
        Get/Set present state of recloser. 
        If set to open (ActionCodes.Open=1), open recloser's controlled element and lock out the recloser. 
        If set to close (ActionCodes.Close=2), close recloser's controlled element and resets recloser to first operation.
        '''
        return self.CheckForError(self._lib.Reclosers_Get_State())

    @State.setter
    def State(self, Value):
        self.CheckForError(self._lib.Reclosers_Set_State(Value))

    @property
    def NormalState(self):
        '''Get/set normal state (ActionCodes.Open=1, ActionCodes.Close=2) of the recloser.'''
        return self.CheckForError(self._lib.Reclosers_Get_NormalState())

    @NormalState.setter
    def NormalState(self, Value):
        self.CheckForError(self._lib.Reclosers_Set_NormalState(Value))
