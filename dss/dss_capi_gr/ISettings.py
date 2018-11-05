'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class ISettings(Base):
    __slots__ = []

    @property
    def AllowDuplicates(self):
        '''{True | False*} Designates whether to allow duplicate names of objects'''
        return self._lib.Settings_Get_AllowDuplicates() != 0

    @AllowDuplicates.setter
    def AllowDuplicates(self, Value):
        self._lib.Settings_Set_AllowDuplicates(Value)
        self.CheckForError()

    @property
    def AutoBusList(self):
        '''List of Buses or (File=xxxx) syntax for the AutoAdd solution mode.'''
        return self._get_string(self._lib.Settings_Get_AutoBusList())

    @AutoBusList.setter
    def AutoBusList(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Settings_Set_AutoBusList(Value)
        self.CheckForError()

    @property
    def CktModel(self):
        '''{dssMultiphase * | dssPositiveSeq} IIndicate if the circuit model is positive sequence.'''
        return self._lib.Settings_Get_CktModel()

    @CktModel.setter
    def CktModel(self, Value):
        self._lib.Settings_Set_CktModel(Value)
        self.CheckForError()

    @property
    def ControlTrace(self):
        '''{True | False*} Denotes whether to trace the control actions to a file.'''
        return self._lib.Settings_Get_ControlTrace() != 0

    @ControlTrace.setter
    def ControlTrace(self, Value):
        self._lib.Settings_Set_ControlTrace(Value)
        self.CheckForError()

    @property
    def EmergVmaxpu(self):
        '''Per Unit maximum voltage for Emergency conditions.'''
        return self._lib.Settings_Get_EmergVmaxpu()

    @EmergVmaxpu.setter
    def EmergVmaxpu(self, Value):
        self._lib.Settings_Set_EmergVmaxpu(Value)
        self.CheckForError()

    @property
    def EmergVminpu(self):
        '''Per Unit minimum voltage for Emergency conditions.'''
        return self._lib.Settings_Get_EmergVminpu()

    @EmergVminpu.setter
    def EmergVminpu(self, Value):
        self._lib.Settings_Set_EmergVminpu(Value)
        self.CheckForError()

    @property
    def LossRegs(self):
        '''Integer array defining which energy meter registers to use for computing losses'''
        self._lib.Settings_Get_LossRegs_GR()
        return self._get_int32_gr_array()

    @LossRegs.setter
    def LossRegs(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)
        self._lib.Settings_Set_LossRegs(ValuePtr, ValueCount)
        self.CheckForError()

    @property
    def LossWeight(self):
        '''Weighting factor applied to Loss register values.'''
        return self._lib.Settings_Get_LossWeight()

    @LossWeight.setter
    def LossWeight(self, Value):
        self._lib.Settings_Set_LossWeight(Value)
        self.CheckForError()

    @property
    def NormVmaxpu(self):
        '''Per Unit maximum voltage for Normal conditions.'''
        return self._lib.Settings_Get_NormVmaxpu()

    @NormVmaxpu.setter
    def NormVmaxpu(self, Value):
        self._lib.Settings_Set_NormVmaxpu(Value)
        self.CheckForError()

    @property
    def NormVminpu(self):
        '''Per Unit minimum voltage for Normal conditions.'''
        return self._lib.Settings_Get_NormVminpu()

    @NormVminpu.setter
    def NormVminpu(self, Value):
        self._lib.Settings_Set_NormVminpu(Value)
        self.CheckForError()

    @property
    def PriceCurve(self):
        '''Name of LoadShape object that serves as the source of price signal data for yearly simulations, etc.'''
        return self._get_string(self._lib.Settings_Get_PriceCurve())

    @PriceCurve.setter
    def PriceCurve(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Settings_Set_PriceCurve(Value)
        self.CheckForError()

    @property
    def PriceSignal(self):
        '''Price Signal for the Circuit'''
        return self._lib.Settings_Get_PriceSignal()

    @PriceSignal.setter
    def PriceSignal(self, Value):
        self._lib.Settings_Set_PriceSignal(Value)
        self.CheckForError()

    @property
    def Trapezoidal(self):
        '''{True | False *} Gets value of trapezoidal integration flag in energy meters.'''
        return self._lib.Settings_Get_Trapezoidal() != 0

    @Trapezoidal.setter
    def Trapezoidal(self, Value):
        self._lib.Settings_Set_Trapezoidal(Value)
        self.CheckForError()

    @property
    def UEregs(self):
        '''Array of Integers defining energy meter registers to use for computing UE'''
        self._lib.Settings_Get_UEregs_GR()
        return self._get_int32_gr_array()

    @UEregs.setter
    def UEregs(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)
        self._lib.Settings_Set_UEregs(ValuePtr, ValueCount)
        self.CheckForError()

    @property
    def UEweight(self):
        '''Weighting factor applied to UE register values.'''
        return self._lib.Settings_Get_UEweight()

    @UEweight.setter
    def UEweight(self, Value):
        self._lib.Settings_Set_UEweight(Value)
        self.CheckForError()

    @property
    def VoltageBases(self):
        '''Array of doubles defining the legal voltage bases in kV L-L'''
        self._lib.Settings_Get_VoltageBases_GR()
        return self._get_float64_gr_array()

    @VoltageBases.setter
    def VoltageBases(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.Settings_Set_VoltageBases(ValuePtr, ValueCount)
        self.CheckForError()

    @property
    def ZoneLock(self):
        '''{True | False*}  Locks Zones on energy meters to prevent rebuilding if a circuit change occurs.'''
        return self._lib.Settings_Get_ZoneLock() != 0

    @ZoneLock.setter
    def ZoneLock(self, Value):
        self._lib.Settings_Set_ZoneLock(Value)
        self.CheckForError()

    @property
    def AllocationFactors(self):
        '''(write-only) Sets all load allocation factors for all loads defined by XFKVA property to this value.'''
        raise AttributeError("This property is write-only!")

    @AllocationFactors.setter
    def AllocationFactors(self, Value):
        self._lib.Settings_Set_AllocationFactors(Value)
        self.CheckForError()
