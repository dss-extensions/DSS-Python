'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira
Copyright (c) 2018-2022 DSS Extensions contributors
'''
from .._cffi_api_util import Iterable

class ITransformers(Iterable):
    __slots__ = []

    _columns = [
        'Name',
        'idx',
        'XfmrCode',
        'IsDelta',
        'CoreType',
        'NumWindings',
        'Wdg',
        'NumTaps',
        'MinTap',
        'MaxTap',
        'Tap',
        'kV',
        'kVA',
        'R',
        'Xhl',
        'Xht',
        'Xlt',
        'Rneut',
        'Xneut',
        'RdcOhms',
        'WdgCurrents',
        'WdgVoltages',
        'LossesByType',
    ]

    @property
    def IsDelta(self):
        '''Active Winding delta or wye connection?'''
        return self.CheckForError(self._lib.Transformers_Get_IsDelta()) != 0

    @IsDelta.setter
    def IsDelta(self, Value):
        self.CheckForError(self._lib.Transformers_Set_IsDelta(Value))

    @property
    def MaxTap(self):
        '''Active Winding maximum tap in per-unit.'''
        return self.CheckForError(self._lib.Transformers_Get_MaxTap())

    @MaxTap.setter
    def MaxTap(self, Value):
        self.CheckForError(self._lib.Transformers_Set_MaxTap(Value))

    @property
    def MinTap(self):
        '''Active Winding minimum tap in per-unit.'''
        return self.CheckForError(self._lib.Transformers_Get_MinTap())

    @MinTap.setter
    def MinTap(self, Value):
        self.CheckForError(self._lib.Transformers_Set_MinTap(Value))

    @property
    def NumTaps(self):
        '''Active Winding number of tap steps betwein MinTap and MaxTap.'''
        return self.CheckForError(self._lib.Transformers_Get_NumTaps())

    @NumTaps.setter
    def NumTaps(self, Value):
        self.CheckForError(self._lib.Transformers_Set_NumTaps(Value))

    @property
    def NumWindings(self):
        '''Number of windings on this transformer. Allocates memory; set or change this property first.'''
        return self.CheckForError(self._lib.Transformers_Get_NumWindings())

    @NumWindings.setter
    def NumWindings(self, Value):
        self.CheckForError(self._lib.Transformers_Set_NumWindings(Value))

    @property
    def R(self):
        '''Active Winding resistance in %'''
        return self.CheckForError(self._lib.Transformers_Get_R())

    @R.setter
    def R(self, Value):
        self.CheckForError(self._lib.Transformers_Set_R(Value))

    @property
    def Rneut(self):
        '''Active Winding neutral resistance [ohms] for wye connections. Set less than zero for ungrounded wye.'''
        return self.CheckForError(self._lib.Transformers_Get_Rneut())

    @Rneut.setter
    def Rneut(self, Value):
        self.CheckForError(self._lib.Transformers_Set_Rneut(Value))

    @property
    def Tap(self):
        '''Active Winding tap in per-unit.'''
        return self.CheckForError(self._lib.Transformers_Get_Tap())

    @Tap.setter
    def Tap(self, Value):
        self.CheckForError(self._lib.Transformers_Set_Tap(Value))

    @property
    def Wdg(self):
        '''Active Winding Number from 1..NumWindings. Update this before reading or setting a sequence of winding properties (R, Tap, kV, kVA, etc.)'''
        return self.CheckForError(self._lib.Transformers_Get_Wdg())

    @Wdg.setter
    def Wdg(self, Value):
        self.CheckForError(self._lib.Transformers_Set_Wdg(Value))

    @property
    def XfmrCode(self):
        '''Name of an XfrmCode that supplies electircal parameters for this Transformer.'''
        return self._get_string(self.CheckForError(self._lib.Transformers_Get_XfmrCode()))

    @XfmrCode.setter
    def XfmrCode(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Transformers_Set_XfmrCode(Value))

    @property
    def Xhl(self):
        '''Percent reactance between windings 1 and 2, on winding 1 kVA base. Use for 2-winding or 3-winding transformers.'''
        return self.CheckForError(self._lib.Transformers_Get_Xhl())

    @Xhl.setter
    def Xhl(self, Value):
        self.CheckForError(self._lib.Transformers_Set_Xhl(Value))

    @property
    def Xht(self):
        '''Percent reactance between windigns 1 and 3, on winding 1 kVA base.  Use for 3-winding transformers only.'''
        return self.CheckForError(self._lib.Transformers_Get_Xht())

    @Xht.setter
    def Xht(self, Value):
        self.CheckForError(self._lib.Transformers_Set_Xht(Value))

    @property
    def Xlt(self):
        '''Percent reactance between windings 2 and 3, on winding 1 kVA base. Use for 3-winding transformers only.'''
        return self.CheckForError(self._lib.Transformers_Get_Xlt())

    @Xlt.setter
    def Xlt(self, Value):
        self.CheckForError(self._lib.Transformers_Set_Xlt(Value))

    @property
    def Xneut(self):
        '''Active Winding neutral reactance [ohms] for wye connections.'''
        return self.CheckForError(self._lib.Transformers_Get_Xneut())

    @Xneut.setter
    def Xneut(self, Value):
        self.CheckForError(self._lib.Transformers_Set_Xneut(Value))

    @property
    def kV(self):
        '''Active Winding kV rating.  Phase-phase for 2 or 3 phases, actual winding kV for 1 phase transformer.'''
        return self.CheckForError(self._lib.Transformers_Get_kV())

    @kV.setter
    def kV(self, Value):
        self.CheckForError(self._lib.Transformers_Set_kV(Value))

    @property
    def kVA(self):
        '''Active Winding kVA rating. On winding 1, this also determines normal and emergency current ratings for all windings.'''
        return self.CheckForError(self._lib.Transformers_Get_kVA())

    @kVA.setter
    def kVA(self, Value):
        self.CheckForError(self._lib.Transformers_Set_kVA(Value))

    kva = kVA

    @property
    def WdgVoltages(self):
        '''(read-only) Complex array of voltages for active winding'''
        self.CheckForError(self._lib.Transformers_Get_WdgVoltages_GR())
        return self._get_float64_gr_array()

    @property
    def WdgCurrents(self):
        '''(read-only) All Winding currents (ph1, wdg1, wdg2,... ph2, wdg1, wdg2 ...)'''
        self.CheckForError(self._lib.Transformers_Get_WdgCurrents_GR())
        return self._get_float64_gr_array()

    @property
    def strWdgCurrents(self):
        '''(read-only) All winding currents in CSV string form like the WdgCurrents property'''
        return self._get_string(self.CheckForError(self._lib.Transformers_Get_strWdgCurrents()))

    @property
    def CoreType(self):
        '''Transformer Core Type: 0=shell;1 = 1-phase; 3= 3-leg; 5= 5-leg'''
        return self.CheckForError(self._lib.Transformers_Get_CoreType()) #TODO: use enum

    @CoreType.setter
    def CoreType(self, Value):
        self.CheckForError(self._lib.Transformers_Set_CoreType(Value))

    @property
    def RdcOhms(self):
        '''dc Resistance of active winding in ohms for GIC analysis'''
        return self.CheckForError(self._lib.Transformers_Get_RdcOhms())

    @RdcOhms.setter
    def RdcOhms(self, Value):
        self.CheckForError(self._lib.Transformers_Set_RdcOhms(Value))

    @property
    def LossesByType(self):
        '''Complex array with the losses by type (total losses, load losses, no-load losses), in VA'''
        self.CheckForError(self._lib.Transformers_Get_LossesByType_GR())
        return self._get_float64_gr_array()

    @property
    def AllLossesByType(self):
        '''Complex array with the losses by type (total losses, load losses, no-load losses), in VA, concatenated for ALL transformers'''
        self.CheckForError(self._lib.Transformers_Get_AllLossesByType_GR())
        return self._get_float64_gr_array()
