'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class ILoads(Base):
    __slots__ = []

    @property
    def AllNames(self):
        '''(read-only) Array of strings containing all Load names'''
        return self._get_string_array(self._lib.Loads_Get_AllNames)

    @property
    def AllocationFactor(self):
        '''Factor for allocating loads by connected xfkva'''
        return self._lib.Loads_Get_AllocationFactor()

    @AllocationFactor.setter
    def AllocationFactor(self, Value):
        self._lib.Loads_Set_AllocationFactor(Value)

    @property
    def CVRcurve(self):
        '''Name of a loadshape with both Mult and Qmult, for CVR factors as a function of time.'''
        return self._get_string(self._lib.Loads_Get_CVRcurve())

    @CVRcurve.setter
    def CVRcurve(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Loads_Set_CVRcurve(Value)
        self.CheckForError()

    @property
    def CVRvars(self):
        '''Percent reduction in Q for percent reduction in V. Must be used with dssLoadModelCVR.'''
        return self._lib.Loads_Get_CVRvars()

    @CVRvars.setter
    def CVRvars(self, Value):
        self._lib.Loads_Set_CVRvars(Value)
        self.CheckForError()

    @property
    def CVRwatts(self):
        '''Percent reduction in P for percent reduction in V. Must be used with dssLoadModelCVR.'''
        return self._lib.Loads_Get_CVRwatts()

    @CVRwatts.setter
    def CVRwatts(self, Value):
        self._lib.Loads_Set_CVRwatts(Value)
        self.CheckForError()

    @property
    def Cfactor(self):
        '''Factor relates average to peak kw.  Used for allocation with kwh and kwhdays/'''
        return self._lib.Loads_Get_Cfactor()

    @Cfactor.setter
    def Cfactor(self, Value):
        self._lib.Loads_Set_Cfactor(Value)
        self.CheckForError()

    @property
    def Class(self):
        return self._lib.Loads_Get_Class_()

    @Class.setter
    def Class(self, Value):
        self._lib.Loads_Set_Class_(Value)
        self.CheckForError()

    @property
    def Count(self):
        '''(read-only) Number of Load objects in active circuit.'''
        return self._lib.Loads_Get_Count()

    def __len__(self):
        return self._lib.Loads_Get_Count()

    @property
    def First(self):
        '''(read-only) Set first Load element to be active; returns 0 if none.'''
        return self._lib.Loads_Get_First()

    @property
    def Growth(self):
        '''Name of the growthshape curve for yearly load growth factors.'''
        return self._get_string(self._lib.Loads_Get_Growth())

    @Growth.setter
    def Growth(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Loads_Set_Growth(Value)
        self.CheckForError()

    @property
    def IsDelta(self):
        '''Delta loads are connected line-to-line.'''
        return self._lib.Loads_Get_IsDelta() != 0

    @IsDelta.setter
    def IsDelta(self, Value):
        self._lib.Loads_Set_IsDelta(Value)
        self.CheckForError()

    @property
    def Model(self):
        '''The Load Model defines variation of P and Q with voltage.'''
        return self._lib.Loads_Get_Model()

    @Model.setter
    def Model(self, Value):
        self._lib.Loads_Set_Model(Value)
        self.CheckForError()

    @property
    def Name(self):
        '''Set active load by name.'''
        return self._get_string(self._lib.Loads_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Loads_Set_Name(Value)
        self.CheckForError()

    @property
    def Next(self):
        '''(read-only) Sets next Load element to be active; returns 0 of none else index of active load.'''
        return self._lib.Loads_Get_Next()

    @property
    def NumCust(self):
        '''Number of customers in this load, defaults to one.'''
        return self._lib.Loads_Get_NumCust()

    @NumCust.setter
    def NumCust(self, Value):
        self._lib.Loads_Set_NumCust(Value)
        self.CheckForError()

    @property
    def PF(self):
        '''
        (read) Set Power Factor for Active Load. Specify leading PF as negative. Updates kvar based on kW value
        (write) Set Power Factor for Active Load. Specify leading PF as negative. Updates kvar based on present value of kW.
        '''
        return self._lib.Loads_Get_PF()

    @PF.setter
    def PF(self, Value):
        self._lib.Loads_Set_PF(Value)
        self.CheckForError()

    @property
    def PctMean(self):
        '''Average percent of nominal load in Monte Carlo studies; only if no loadshape defined for this load.'''
        return self._lib.Loads_Get_PctMean()

    @PctMean.setter
    def PctMean(self, Value):
        self._lib.Loads_Set_PctMean(Value)
        self.CheckForError()

    @property
    def PctStdDev(self):
        '''Percent standard deviation for Monte Carlo load studies; if there is no loadshape assigned to this load.'''
        return self._lib.Loads_Get_PctStdDev()

    @PctStdDev.setter
    def PctStdDev(self, Value):
        self._lib.Loads_Set_PctStdDev(Value)
        self.CheckForError()

    @property
    def RelWeight(self):
        '''Relative Weighting factor for the active LOAD'''
        return self._lib.Loads_Get_RelWeight()

    @RelWeight.setter
    def RelWeight(self, Value):
        self._lib.Loads_Set_RelWeight(Value)
        self.CheckForError()

    @property
    def Rneut(self):
        '''Neutral resistance for wye-connected loads.'''
        return self._lib.Loads_Get_Rneut()

    @Rneut.setter
    def Rneut(self, Value):
        self._lib.Loads_Set_Rneut(Value)
        self.CheckForError()

    @property
    def Spectrum(self):
        '''Name of harmonic current spectrrum shape.'''
        return self._get_string(self._lib.Loads_Get_Spectrum())

    @Spectrum.setter
    def Spectrum(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Loads_Set_Spectrum(Value)
        self.CheckForError()

    @property
    def Status(self):
        '''Response to load multipliers: Fixed (growth only), Exempt (no LD curve), Variable (all).'''
        return self._lib.Loads_Get_Status()

    @Status.setter
    def Status(self, Value):
        self._lib.Loads_Set_Status(Value)
        self.CheckForError()

    @property
    def Vmaxpu(self):
        '''Maximum per-unit voltage to use the load model. Above this, constant Z applies.'''
        return self._lib.Loads_Get_Vmaxpu()

    @Vmaxpu.setter
    def Vmaxpu(self, Value):
        self._lib.Loads_Set_Vmaxpu(Value)
        self.CheckForError()

    @property
    def Vminemerg(self):
        '''Minimum voltage for unserved energy (UE) evaluation.'''
        return self._lib.Loads_Get_Vminemerg()

    @Vminemerg.setter
    def Vminemerg(self, Value):
        self._lib.Loads_Set_Vminemerg(Value)
        self.CheckForError()

    @property
    def Vminnorm(self):
        '''Minimum voltage for energy exceeding normal (EEN) evaluations.'''
        return self._lib.Loads_Get_Vminnorm()

    @Vminnorm.setter
    def Vminnorm(self, Value):
        self._lib.Loads_Set_Vminnorm(Value)
        self.CheckForError()

    @property
    def Vminpu(self):
        '''Minimum voltage to apply the load model. Below this, constant Z is used.'''
        return self._lib.Loads_Get_Vminpu()

    @Vminpu.setter
    def Vminpu(self, Value):
        self._lib.Loads_Set_Vminpu(Value)
        self.CheckForError()

    @property
    def Xneut(self):
        '''Neutral reactance for wye-connected loads.'''
        return self._lib.Loads_Get_Xneut()

    @Xneut.setter
    def Xneut(self, Value):
        self._lib.Loads_Set_Xneut(Value)
        self.CheckForError()

    @property
    def Yearly(self):
        '''Name of yearly duration loadshape'''
        return self._get_string(self._lib.Loads_Get_Yearly())

    @Yearly.setter
    def Yearly(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Loads_Set_Yearly(Value)
        self.CheckForError()

    @property
    def ZIPV(self):
        '''Array of 7  doubles with values for ZIPV property of the LOAD object'''
        return self._get_float64_array(self._lib.Loads_Get_ZIPV)

    @ZIPV.setter
    def ZIPV(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.Loads_Set_ZIPV(ValuePtr, ValueCount)
        self.CheckForError()

    @property
    def daily(self):
        '''Name of the loadshape for a daily load profile.'''
        return self._get_string(self._lib.Loads_Get_daily())

    @daily.setter
    def daily(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Loads_Set_daily(Value)
        self.CheckForError()

    @property
    def duty(self):
        '''Name of the loadshape for a duty cycle simulation.'''
        return self._get_string(self._lib.Loads_Get_duty())

    @duty.setter
    def duty(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Loads_Set_duty(Value)
        self.CheckForError()

    @property
    def idx(self):
        return self._lib.Loads_Get_idx()

    @idx.setter
    def idx(self, Value):
        self._lib.Loads_Set_idx(Value)
        self.CheckForError()

    @property
    def kV(self):
        '''Set kV rating for active Load. For 2 or more phases set Line-Line kV. Else actual kV across terminals.'''
        return self._lib.Loads_Get_kV()

    @kV.setter
    def kV(self, Value):
        self._lib.Loads_Set_kV(Value)
        self.CheckForError()

    @property
    def kW(self):
        '''Set kW for active Load. Updates kvar based on present PF.'''
        return self._lib.Loads_Get_kW()

    @kW.setter
    def kW(self, Value):
        self._lib.Loads_Set_kW(Value)
        self.CheckForError()

    @property
    def kva(self):
        '''Base load kva. Also defined kw and kvar or pf input, or load allocation by kwh or xfkva.'''
        return self._lib.Loads_Get_kva()

    @kva.setter
    def kva(self, Value):
        self._lib.Loads_Set_kva(Value)
        self.CheckForError()

    @property
    def kvar(self):
        '''Set kvar for active Load. Updates PF based on present kW.'''
        return self._lib.Loads_Get_kvar()

    @kvar.setter
    def kvar(self, Value):
        self._lib.Loads_Set_kvar(Value)
        self.CheckForError()

    @property
    def kwh(self):
        '''kwh billed for this period. Can be used with Cfactor for load allocation.'''
        return self._lib.Loads_Get_kwh()

    @kwh.setter
    def kwh(self, Value):
        self._lib.Loads_Set_kwh(Value)
        self.CheckForError()

    @property
    def kwhdays(self):
        '''Length of kwh billing period for average demand calculation. Default 30.'''
        return self._lib.Loads_Get_kwhdays()

    @kwhdays.setter
    def kwhdays(self, Value):
        self._lib.Loads_Set_kwhdays(Value)
        self.CheckForError()

    @property
    def pctSeriesRL(self):
        '''Percent of Load that is modeled as series R-L for harmonics studies'''
        return self._lib.Loads_Get_pctSeriesRL()

    @pctSeriesRL.setter
    def pctSeriesRL(self, Value):
        self._lib.Loads_Set_pctSeriesRL(Value)
        self.CheckForError()

    @property
    def xfkVA(self):
        '''Rated service transformer kVA for load allocation, using AllocationFactor. Affects kW, kvar, and pf.'''
        return self._lib.Loads_Get_xfkVA()

    @xfkVA.setter
    def xfkVA(self, Value):
        self._lib.Loads_Set_xfkVA(Value)
        self.CheckForError()

    # API extensions
    @property
    def Phases(self):
        '''Number of phases'''
        return self._lib.Loads_Get_Phases()

    @Phases.setter
    def Phases(self, Value):
        self._lib.Loads_Set_Phases(Value)
        self.CheckForError()

    def __iter__(self):
        idx = self.First
        while idx != 0:
            yield self
            idx = self.Next

