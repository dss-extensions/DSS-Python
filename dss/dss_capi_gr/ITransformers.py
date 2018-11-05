'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class ITransformers(Base):
    __slots__ = []

    @property
    def AllNames(self):
        '''(read-only) Array of strings with all Transformer names in the active circuit.'''
        return self._get_string_array(self._lib.Transformers_Get_AllNames)

    @property
    def Count(self):
        return self._lib.Transformers_Get_Count()

    def __len__(self):
        return self._lib.Transformers_Get_Count()

    @property
    def First(self):
        '''(read-only) Sets the first Transformer active. Returns 0 if no more.'''
        return self._lib.Transformers_Get_First()

    @property
    def IsDelta(self):
        '''Active Winding delta or wye connection?'''
        return self._lib.Transformers_Get_IsDelta() != 0

    @IsDelta.setter
    def IsDelta(self, Value):
        self._lib.Transformers_Set_IsDelta(Value)
        self.CheckForError()

    @property
    def MaxTap(self):
        '''Active Winding maximum tap in per-unit.'''
        return self._lib.Transformers_Get_MaxTap()

    @MaxTap.setter
    def MaxTap(self, Value):
        self._lib.Transformers_Set_MaxTap(Value)
        self.CheckForError()

    @property
    def MinTap(self):
        '''Active Winding minimum tap in per-unit.'''
        return self._lib.Transformers_Get_MinTap()

    @MinTap.setter
    def MinTap(self, Value):
        self._lib.Transformers_Set_MinTap(Value)
        self.CheckForError()

    @property
    def Name(self):
        '''Sets a Transformer active by Name.'''
        return self._get_string(self._lib.Transformers_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Transformers_Set_Name(Value)
        self.CheckForError()

    @property
    def Next(self):
        '''(read-only) Sets the next Transformer active. Returns 0 if no more.'''
        return self._lib.Transformers_Get_Next()

    @property
    def NumTaps(self):
        '''Active Winding number of tap steps betwein MinTap and MaxTap.'''
        return self._lib.Transformers_Get_NumTaps()

    @NumTaps.setter
    def NumTaps(self, Value):
        self._lib.Transformers_Set_NumTaps(Value)
        self.CheckForError()

    @property
    def NumWindings(self):
        '''Number of windings on this transformer. Allocates memory; set or change this property first.'''
        return self._lib.Transformers_Get_NumWindings()

    @NumWindings.setter
    def NumWindings(self, Value):
        self._lib.Transformers_Set_NumWindings(Value)
        self.CheckForError()

    @property
    def R(self):
        '''Active Winding resistance in %'''
        return self._lib.Transformers_Get_R()

    @R.setter
    def R(self, Value):
        self._lib.Transformers_Set_R(Value)
        self.CheckForError()

    @property
    def Rneut(self):
        '''Active Winding neutral resistance [ohms] for wye connections. Set less than zero for ungrounded wye.'''
        return self._lib.Transformers_Get_Rneut()

    @Rneut.setter
    def Rneut(self, Value):
        self._lib.Transformers_Set_Rneut(Value)
        self.CheckForError()

    @property
    def Tap(self):
        '''Active Winding tap in per-unit.'''
        return self._lib.Transformers_Get_Tap()

    @Tap.setter
    def Tap(self, Value):
        self._lib.Transformers_Set_Tap(Value)
        self.CheckForError()

    @property
    def Wdg(self):
        '''Active Winding Number from 1..NumWindings. Update this before reading or setting a sequence of winding properties (R, Tap, kV, kVA, etc.)'''
        return self._lib.Transformers_Get_Wdg()

    @Wdg.setter
    def Wdg(self, Value):
        self._lib.Transformers_Set_Wdg(Value)
        self.CheckForError()

    @property
    def XfmrCode(self):
        '''Name of an XfrmCode that supplies electircal parameters for this Transformer.'''
        return self._get_string(self._lib.Transformers_Get_XfmrCode())

    @XfmrCode.setter
    def XfmrCode(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Transformers_Set_XfmrCode(Value)
        self.CheckForError()

    @property
    def Xhl(self):
        '''Percent reactance between windings 1 and 2, on winding 1 kVA base. Use for 2-winding or 3-winding transformers.'''
        return self._lib.Transformers_Get_Xhl()

    @Xhl.setter
    def Xhl(self, Value):
        self._lib.Transformers_Set_Xhl(Value)
        self.CheckForError()

    @property
    def Xht(self):
        '''Percent reactance between windigns 1 and 3, on winding 1 kVA base.  Use for 3-winding transformers only.'''
        return self._lib.Transformers_Get_Xht()

    @Xht.setter
    def Xht(self, Value):
        self._lib.Transformers_Set_Xht(Value)
        self.CheckForError()

    @property
    def Xlt(self):
        '''Percent reactance between windings 2 and 3, on winding 1 kVA base. Use for 3-winding transformers only.'''
        return self._lib.Transformers_Get_Xlt()

    @Xlt.setter
    def Xlt(self, Value):
        self._lib.Transformers_Set_Xlt(Value)
        self.CheckForError()

    @property
    def Xneut(self):
        '''Active Winding neutral reactance [ohms] for wye connections.'''
        return self._lib.Transformers_Get_Xneut()

    @Xneut.setter
    def Xneut(self, Value):
        self._lib.Transformers_Set_Xneut(Value)
        self.CheckForError()

    @property
    def kV(self):
        '''Active Winding kV rating.  Phase-phase for 2 or 3 phases, actual winding kV for 1 phase transformer.'''
        return self._lib.Transformers_Get_kV()

    @kV.setter
    def kV(self, Value):
        self._lib.Transformers_Set_kV(Value)
        self.CheckForError()

    @property
    def kVA(self):
        '''Active Winding kVA rating. On winding 1, this also determines normal and emergency current ratings for all windings.'''
        return self._lib.Transformers_Get_kVA()

    @kVA.setter
    def kVA(self, Value):
        self._lib.Transformers_Set_kVA(Value)
        self.CheckForError()

    kva = kVA

    @property
    def WdgVoltages(self):
        '''(read-only) Complex array of voltages for active winding'''
        self._lib.Transformers_Get_WdgVoltages_GR()
        return self._get_float64_gr_array()

    @property
    def WdgCurrents(self):
        '''(read-only) All Winding currents (ph1, wdg1, wdg2,... ph2, wdg1, wdg2 ...)'''
        self._lib.Transformers_Get_WdgCurrents_GR()
        return self._get_float64_gr_array()

    @property
    def strWdgCurrents(self):
        '''(read-only) All winding currents in CSV string form like the WdgCurrents property'''
        return self._get_string(self._lib.Transformers_Get_strWdgCurrents())

    @property
    def CoreType(self):
        '''Transformer Core Type: 0=shell;1 = 1-phase; 3= 3-leg; 5= 5-leg'''
        return self._lib.Transformers_Get_CoreType()

    @CoreType.setter
    def CoreType(self, Value):
        self._lib.Transformers_Set_CoreType(Value)
        self.CheckForError()

    @property
    def RdcOhms(self):
        '''dc Resistance of active winding in ohms for GIC analysis'''
        return self._lib.Transformers_Get_RdcOhms()

    @RdcOhms.setter
    def RdcOhms(self, Value):
        self._lib.Transformers_Set_RdcOhms(Value)
        self.CheckForError()

    def __iter__(self):
        idx = self.First
        while idx != 0:
            yield self
            idx = self.Next

