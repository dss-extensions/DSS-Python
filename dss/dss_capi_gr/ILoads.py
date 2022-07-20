'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira
Copyright (c) 2018-2022 DSS Extensions contributors
'''
from .._cffi_api_util import Iterable

class ILoads(Iterable):
    __slots__ = []

    _columns = [
        'Name',
        'idx',
        'Phases',
        'Class',
        'Model',
        'NumCust',
        'IsDelta',
        'Rneut',
        'Xneut',
        'PF',
        'ZIPV',
        'CVRcurve',
        'CVRvars',
        'CVRwatts',
        'Cfactor',
        'Growth',
        'daily',
        'duty',
        'Yearly',
        'PctMean',
        'PctStdDev',
        'RelWeight',
        'Spectrum',
        'Status',
        'Vminnorm',
        'Vminemerg',
        'Vminpu',
        'Vmaxpu',
        'kV',
        'kW',
        'kva',
        'kvar',
        'kwh',
        'kwhdays',
        'AllocationFactor',
        'xfkVA',
        'pctSeriesRL',
        'Sensor',
    ]

    @property
    def AllocationFactor(self):
        '''Factor for allocating loads by connected xfkva'''
        return self.CheckForError(self._lib.Loads_Get_AllocationFactor())

    @AllocationFactor.setter
    def AllocationFactor(self, Value):
        self.CheckForError(self._lib.Loads_Set_AllocationFactor(Value))

    @property
    def CVRcurve(self):
        '''Name of a loadshape with both Mult and Qmult, for CVR factors as a function of time.'''
        return self._get_string(self.CheckForError(self._lib.Loads_Get_CVRcurve()))

    @CVRcurve.setter
    def CVRcurve(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Loads_Set_CVRcurve(Value))

    @property
    def CVRvars(self):
        '''Percent reduction in Q for percent reduction in V. Must be used with dssLoadModelCVR.'''
        return self.CheckForError(self._lib.Loads_Get_CVRvars())

    @CVRvars.setter
    def CVRvars(self, Value):
        self.CheckForError(self._lib.Loads_Set_CVRvars(Value))

    @property
    def CVRwatts(self):
        '''Percent reduction in P for percent reduction in V. Must be used with dssLoadModelCVR.'''
        return self.CheckForError(self._lib.Loads_Get_CVRwatts())

    @CVRwatts.setter
    def CVRwatts(self, Value):
        self.CheckForError(self._lib.Loads_Set_CVRwatts(Value))

    @property
    def Cfactor(self):
        '''Factor relates average to peak kw.  Used for allocation with kwh and kwhdays'''
        return self.CheckForError(self._lib.Loads_Get_Cfactor())

    @Cfactor.setter
    def Cfactor(self, Value):
        self.CheckForError(self._lib.Loads_Set_Cfactor(Value))

    @property
    def Class(self):
        return self.CheckForError(self._lib.Loads_Get_Class_())

    @Class.setter
    def Class(self, Value):
        self.CheckForError(self._lib.Loads_Set_Class_(Value))

    @property
    def Growth(self):
        '''Name of the growthshape curve for yearly load growth factors.'''
        return self._get_string(self.CheckForError(self._lib.Loads_Get_Growth()))

    @Growth.setter
    def Growth(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Loads_Set_Growth(Value))

    @property
    def IsDelta(self):
        '''Delta loads are connected line-to-line.'''
        return self.CheckForError(self._lib.Loads_Get_IsDelta()) != 0

    @IsDelta.setter
    def IsDelta(self, Value):
        self.CheckForError(self._lib.Loads_Set_IsDelta(Value))

    @property
    def Model(self):
        '''The Load Model defines variation of P and Q with voltage.'''
        return self.CheckForError(self._lib.Loads_Get_Model())

    @Model.setter
    def Model(self, Value):
        self.CheckForError(self._lib.Loads_Set_Model(Value))

    @property
    def NumCust(self):
        '''Number of customers in this load, defaults to one.'''
        return self.CheckForError(self._lib.Loads_Get_NumCust())

    @NumCust.setter
    def NumCust(self, Value):
        self.CheckForError(self._lib.Loads_Set_NumCust(Value))

    @property
    def PF(self):
        '''Get or set Power Factor for Active Load. Specify leading PF as negative. Updates kvar based on present value of kW'''
        return self.CheckForError(self._lib.Loads_Get_PF())

    @PF.setter
    def PF(self, Value):
        self.CheckForError(self._lib.Loads_Set_PF(Value))

    @property
    def PctMean(self):
        '''Average percent of nominal load in Monte Carlo studies; only if no loadshape defined for this load.'''
        return self.CheckForError(self._lib.Loads_Get_PctMean())

    @PctMean.setter
    def PctMean(self, Value):
        self.CheckForError(self._lib.Loads_Set_PctMean(Value))

    @property
    def PctStdDev(self):
        '''Percent standard deviation for Monte Carlo load studies; if there is no loadshape assigned to this load.'''
        return self.CheckForError(self._lib.Loads_Get_PctStdDev())

    @PctStdDev.setter
    def PctStdDev(self, Value):
        self.CheckForError(self._lib.Loads_Set_PctStdDev(Value))

    @property
    def RelWeight(self):
        '''Relative Weighting factor for the active LOAD'''
        return self.CheckForError(self._lib.Loads_Get_RelWeight())

    @RelWeight.setter
    def RelWeight(self, Value):
        self.CheckForError(self._lib.Loads_Set_RelWeight(Value))

    @property
    def Rneut(self):
        '''Neutral resistance for wye-connected loads.'''
        return self.CheckForError(self._lib.Loads_Get_Rneut())

    @Rneut.setter
    def Rneut(self, Value):
        self.CheckForError(self._lib.Loads_Set_Rneut(Value))

    @property
    def Spectrum(self):
        '''Name of harmonic current spectrrum shape.'''
        return self._get_string(self.CheckForError(self._lib.Loads_Get_Spectrum()))

    @Spectrum.setter
    def Spectrum(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Loads_Set_Spectrum(Value))

    @property
    def Status(self):
        '''Response to load multipliers: Fixed (growth only), Exempt (no LD curve), Variable (all).'''
        return self.CheckForError(self._lib.Loads_Get_Status()) #TODO: use enum

    @Status.setter
    def Status(self, Value):
        self.CheckForError(self._lib.Loads_Set_Status(Value))

    @property
    def Vmaxpu(self):
        '''Maximum per-unit voltage to use the load model. Above this, constant Z applies.'''
        return self.CheckForError(self._lib.Loads_Get_Vmaxpu())

    @Vmaxpu.setter
    def Vmaxpu(self, Value):
        self.CheckForError(self._lib.Loads_Set_Vmaxpu(Value))

    @property
    def Vminemerg(self):
        '''Minimum voltage for unserved energy (UE) evaluation.'''
        return self.CheckForError(self._lib.Loads_Get_Vminemerg())

    @Vminemerg.setter
    def Vminemerg(self, Value):
        self.CheckForError(self._lib.Loads_Set_Vminemerg(Value))

    @property
    def Vminnorm(self):
        '''Minimum voltage for energy exceeding normal (EEN) evaluations.'''
        return self.CheckForError(self._lib.Loads_Get_Vminnorm())

    @Vminnorm.setter
    def Vminnorm(self, Value):
        self.CheckForError(self._lib.Loads_Set_Vminnorm(Value))

    @property
    def Vminpu(self):
        '''Minimum voltage to apply the load model. Below this, constant Z is used.'''
        return self.CheckForError(self._lib.Loads_Get_Vminpu())

    @Vminpu.setter
    def Vminpu(self, Value):
        self.CheckForError(self._lib.Loads_Set_Vminpu(Value))

    @property
    def Xneut(self):
        '''Neutral reactance for wye-connected loads.'''
        return self.CheckForError(self._lib.Loads_Get_Xneut())

    @Xneut.setter
    def Xneut(self, Value):
        self.CheckForError(self._lib.Loads_Set_Xneut(Value))

    @property
    def Yearly(self):
        '''Name of yearly duration loadshape'''
        return self._get_string(self.CheckForError(self._lib.Loads_Get_Yearly()))

    @Yearly.setter
    def Yearly(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Loads_Set_Yearly(Value))

    @property
    def ZIPV(self):
        '''Array of 7 doubles with values for ZIPV property of the load object'''
        self.CheckForError(self._lib.Loads_Get_ZIPV_GR())
        return self._get_float64_gr_array()

    @ZIPV.setter
    def ZIPV(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.Loads_Set_ZIPV(ValuePtr, ValueCount))

    @property
    def daily(self):
        '''Name of the loadshape for a daily load profile.'''
        return self._get_string(self.CheckForError(self._lib.Loads_Get_daily()))

    @daily.setter
    def daily(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Loads_Set_daily(Value))

    @property
    def duty(self):
        '''Name of the loadshape for a duty cycle simulation.'''
        return self._get_string(self.CheckForError(self._lib.Loads_Get_duty()))

    @duty.setter
    def duty(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Loads_Set_duty(Value))

    @property
    def kV(self):
        '''Set kV rating for active Load. For 2 or more phases set Line-Line kV. Else actual kV across terminals.'''
        return self.CheckForError(self._lib.Loads_Get_kV())

    @kV.setter
    def kV(self, Value):
        self.CheckForError(self._lib.Loads_Set_kV(Value))

    @property
    def kW(self):
        '''Set kW for active Load. Updates kvar based on present PF.'''
        return self.CheckForError(self._lib.Loads_Get_kW())

    @kW.setter
    def kW(self, Value):
        self.CheckForError(self._lib.Loads_Set_kW(Value))

    @property
    def kva(self):
        '''Base load kva. Also defined kw and kvar or pf input, or load allocation by kwh or xfkva.'''
        return self.CheckForError(self._lib.Loads_Get_kva())

    @kva.setter
    def kva(self, Value):
        self.CheckForError(self._lib.Loads_Set_kva(Value))

    @property
    def kvar(self):
        '''Get/set kvar for active Load. If set, updates PF based on present kW.'''
        return self.CheckForError(self._lib.Loads_Get_kvar())

    @kvar.setter
    def kvar(self, Value):
        self.CheckForError(self._lib.Loads_Set_kvar(Value))

    @property
    def kwh(self):
        '''kwh billed for this period. Can be used with Cfactor for load allocation.'''
        return self.CheckForError(self._lib.Loads_Get_kwh())

    @kwh.setter
    def kwh(self, Value):
        self.CheckForError(self._lib.Loads_Set_kwh(Value))

    @property
    def kwhdays(self):
        '''Length of kwh billing period for average demand calculation. Default 30.'''
        return self.CheckForError(self._lib.Loads_Get_kwhdays())

    @kwhdays.setter
    def kwhdays(self, Value):
        self.CheckForError(self._lib.Loads_Set_kwhdays(Value))

    @property
    def pctSeriesRL(self):
        '''Percent of Load that is modeled as series R-L for harmonics studies'''
        return self.CheckForError(self._lib.Loads_Get_pctSeriesRL())

    @pctSeriesRL.setter
    def pctSeriesRL(self, Value):
        self.CheckForError(self._lib.Loads_Set_pctSeriesRL(Value))

    @property
    def xfkVA(self):
        '''Rated service transformer kVA for load allocation, using AllocationFactor. Affects kW, kvar, and pf.'''
        return self.CheckForError(self._lib.Loads_Get_xfkVA())

    @xfkVA.setter
    def xfkVA(self, Value):
        self.CheckForError(self._lib.Loads_Set_xfkVA(Value))

    @property
    def Sensor(self):
        '''Name of the sensor monitoring this load.'''
        return self._get_string(self.CheckForError(self._lib.Loads_Get_Sensor()))

    # API extensions
    @property
    def Phases(self):
        '''Number of phases'''
        return self.CheckForError(self._lib.Loads_Get_Phases())

    @Phases.setter
    def Phases(self, Value):
        self.CheckForError(self._lib.Loads_Set_Phases(Value))
