'''
A compatibility layer for DSS_CAPI that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from ._dss_capi import lib, ffi
from ._cffi_api_util import *
import numpy as np

if not freeze:
    FrozenClass = object

class IDSSEvents: # Not implemented
    pass 

class DssException(Exception):
    pass
    
def CheckForError():
    error_num = lib.Error_Get_Number()
    if error_num:
        raise DssException(error_num, get_string(lib.Error_Get_Description()))

    
class IActiveClass(FrozenClass):
    _isfrozen = freeze

    @property
    def ActiveClassName(self):
        return get_string(lib.ActiveClass_Get_ActiveClassName())

    @property
    def AllNames(self):
        return get_string_array(lib.ActiveClass_Get_AllNames)

    @property
    def Count(self):
        return lib.ActiveClass_Get_Count()

    @property
    def First(self):
        return lib.ActiveClass_Get_First()

    @property
    def Name(self):
        return get_string(lib.ActiveClass_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.ActiveClass_Set_Name(Value)

    @property
    def Next(self):
        return lib.ActiveClass_Get_Next()

    @property
    def NumElements(self):
        return lib.ActiveClass_Get_NumElements()


class IBus(FrozenClass):
    _isfrozen = freeze

    def GetUniqueNodeNumber(self, StartNumber):
        return lib.Bus_GetUniqueNodeNumber(StartNumber)

    def ZscRefresh(self):
        return lib.Bus_ZscRefresh() != 0

    @property
    def Coorddefined(self):
        return lib.Bus_Get_Coorddefined() != 0

    @property
    def CplxSeqVoltages(self):
        return get_float64_array(lib.Bus_Get_CplxSeqVoltages)

    @property
    def Cust_Duration(self):
        return lib.Bus_Get_Cust_Duration()

    @property
    def Cust_Interrupts(self):
        return lib.Bus_Get_Cust_Interrupts()

    @property
    def Distance(self):
        return lib.Bus_Get_Distance()

    @property
    def Int_Duration(self):
        return lib.Bus_Get_Int_Duration()

    @property
    def Isc(self):
        return get_float64_array(lib.Bus_Get_Isc)

    @property
    def Lambda(self):
        return lib.Bus_Get_Lambda()

    @property
    def N_Customers(self):
        return lib.Bus_Get_N_Customers()

    @property
    def N_interrupts(self):
        return lib.Bus_Get_N_interrupts()

    @property
    def Name(self):
        return get_string(lib.Bus_Get_Name())

    @property
    def Nodes(self):
        return get_int32_array(lib.Bus_Get_Nodes)

    @property
    def NumNodes(self):
        return lib.Bus_Get_NumNodes()

    @property
    def SectionID(self):
        return lib.Bus_Get_SectionID()

    @property
    def SeqVoltages(self):
        return get_float64_array(lib.Bus_Get_SeqVoltages)

    @property
    def TotalMiles(self):
        return lib.Bus_Get_TotalMiles()

    @property
    def VLL(self):
        return get_float64_array(lib.Bus_Get_VLL)

    @property
    def VMagAngle(self):
        return get_float64_array(lib.Bus_Get_VMagAngle)

    @property
    def Voc(self):
        return get_float64_array(lib.Bus_Get_Voc)

    @property
    def Voltages(self):
        return get_float64_array(lib.Bus_Get_Voltages)

    @property
    def YscMatrix(self):
        return get_float64_array(lib.Bus_Get_YscMatrix)

    @property
    def Zsc0(self):
        return get_float64_array(lib.Bus_Get_Zsc0)

    @property
    def Zsc1(self):
        return get_float64_array(lib.Bus_Get_Zsc1)

    @property
    def ZscMatrix(self):
        return get_float64_array(lib.Bus_Get_ZscMatrix)

    @property
    def kVBase(self):
        return lib.Bus_Get_kVBase()

    @property
    def puVLL(self):
        return get_float64_array(lib.Bus_Get_puVLL)

    @property
    def puVmagAngle(self):
        return get_float64_array(lib.Bus_Get_puVmagAngle)

    @property
    def puVoltages(self):
        return get_float64_array(lib.Bus_Get_puVoltages)

    @property
    def x(self):
        return lib.Bus_Get_x()

    @x.setter
    def x(self, Value):
        lib.Bus_Set_x(Value)

    @property
    def y(self):
        return lib.Bus_Get_y()

    @y.setter
    def y(self, Value):
        lib.Bus_Set_y(Value)


class ICapacitors(FrozenClass):
    _isfrozen = freeze

    def AddStep(self):
        return lib.Capacitors_AddStep() != 0

    def Close(self):
        lib.Capacitors_Close()

    def Open(self):
        lib.Capacitors_Open()

    def SubtractStep(self):
        return lib.Capacitors_SubtractStep() != 0

    @property
    def AllNames(self):
        return get_string_array(lib.Capacitors_Get_AllNames)

    @property
    def AvailableSteps(self):
        return lib.Capacitors_Get_AvailableSteps()

    @property
    def Count(self):
        return lib.Capacitors_Get_Count()

    @property
    def First(self):
        return lib.Capacitors_Get_First()

    @property
    def IsDelta(self):
        return lib.Capacitors_Get_IsDelta() != 0

    @IsDelta.setter
    def IsDelta(self, Value):
        lib.Capacitors_Set_IsDelta(Value)

    @property
    def Name(self):
        return get_string(lib.Capacitors_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Capacitors_Set_Name(Value)

    @property
    def Next(self):
        return lib.Capacitors_Get_Next()

    @property
    def NumSteps(self):
        return lib.Capacitors_Get_NumSteps()

    @NumSteps.setter
    def NumSteps(self, Value):
        lib.Capacitors_Set_NumSteps(Value)

    @property
    def States(self):
        return get_int32_array(lib.Capacitors_Get_States)

    @States.setter
    def States(self, Value):
        Value, ValuePtr, ValueCount = prepare_int32_array(Value)
        lib.Capacitors_Set_States(ValuePtr, ValueCount)

    @property
    def kV(self):
        return lib.Capacitors_Get_kV()

    @kV.setter
    def kV(self, Value):
        lib.Capacitors_Set_kV(Value)

    @property
    def kvar(self):
        return lib.Capacitors_Get_kvar()

    @kvar.setter
    def kvar(self, Value):
        lib.Capacitors_Set_kvar(Value)


class ICapControls(FrozenClass):
    _isfrozen = freeze

    def Reset(self):
        lib.CapControls_Reset()

    @property
    def AllNames(self):
        return get_string_array(lib.CapControls_Get_AllNames)

    @property
    def CTratio(self):
        return lib.CapControls_Get_CTratio()

    @CTratio.setter
    def CTratio(self, Value):
        lib.CapControls_Set_CTratio(Value)

    @property
    def Capacitor(self):
        return get_string(lib.CapControls_Get_Capacitor())

    @Capacitor.setter
    def Capacitor(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.CapControls_Set_Capacitor(Value)

    @property
    def Count(self):
        return lib.CapControls_Get_Count()

    @property
    def DeadTime(self):
        return lib.CapControls_Get_DeadTime()

    @DeadTime.setter
    def DeadTime(self, Value):
        lib.CapControls_Set_DeadTime(Value)

    @property
    def Delay(self):
        return lib.CapControls_Get_Delay()

    @Delay.setter
    def Delay(self, Value):
        lib.CapControls_Set_Delay(Value)

    @property
    def DelayOff(self):
        return lib.CapControls_Get_DelayOff()

    @DelayOff.setter
    def DelayOff(self, Value):
        lib.CapControls_Set_DelayOff(Value)

    @property
    def First(self):
        return lib.CapControls_Get_First()

    @property
    def Mode(self):
        return lib.CapControls_Get_Mode()

    @Mode.setter
    def Mode(self, Value):
        lib.CapControls_Set_Mode(Value)

    @property
    def MonitoredObj(self):
        return get_string(lib.CapControls_Get_MonitoredObj())

    @MonitoredObj.setter
    def MonitoredObj(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.CapControls_Set_MonitoredObj(Value)

    @property
    def MonitoredTerm(self):
        return lib.CapControls_Get_MonitoredTerm()

    @MonitoredTerm.setter
    def MonitoredTerm(self, Value):
        lib.CapControls_Set_MonitoredTerm(Value)

    @property
    def Name(self):
        return get_string(lib.CapControls_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.CapControls_Set_Name(Value)

    @property
    def Next(self):
        return lib.CapControls_Get_Next()

    @property
    def OFFSetting(self):
        return lib.CapControls_Get_OFFSetting()

    @OFFSetting.setter
    def OFFSetting(self, Value):
        lib.CapControls_Set_OFFSetting(Value)

    @property
    def ONSetting(self):
        return lib.CapControls_Get_ONSetting()

    @ONSetting.setter
    def ONSetting(self, Value):
        lib.CapControls_Set_ONSetting(Value)

    @property
    def PTratio(self):
        return lib.CapControls_Get_PTratio()

    @PTratio.setter
    def PTratio(self, Value):
        lib.CapControls_Set_PTratio(Value)

    @property
    def UseVoltOverride(self):
        return lib.CapControls_Get_UseVoltOverride() != 0

    @UseVoltOverride.setter
    def UseVoltOverride(self, Value):
        lib.CapControls_Set_UseVoltOverride(Value)

    @property
    def Vmax(self):
        return lib.CapControls_Get_Vmax()

    @Vmax.setter
    def Vmax(self, Value):
        lib.CapControls_Set_Vmax(Value)

    @property
    def Vmin(self):
        return lib.CapControls_Get_Vmin()

    @Vmin.setter
    def Vmin(self, Value):
        lib.CapControls_Set_Vmin(Value)


class ICmathLib(FrozenClass):
    _isfrozen = freeze

    def cabs(self, realpart, imagpart):
        return lib.CmathLib_Get_cabs(realpart, imagpart)

    def cdang(self, RealPart, ImagPart):
        return lib.CmathLib_Get_cdang(RealPart, ImagPart)

    def cdiv(self, a1, b1, a2, b2):
        return get_float64_array(lib.CmathLib_Get_cdiv, a1, b1, a2, b2)

    def cmplx(self, RealPart, ImagPart):
        return get_float64_array(lib.CmathLib_Get_cmplx, RealPart, ImagPart)

    def cmul(self, a1, b1, a2, b2):
        return get_float64_array(lib.CmathLib_Get_cmul, a1, b1, a2, b2)

    def ctopolardeg(self, RealPart, ImagPart):
        return get_float64_array(lib.CmathLib_Get_ctopolardeg, RealPart, ImagPart)

    def pdegtocomplex(self, magnitude, angle):
        return get_float64_array(lib.CmathLib_Get_pdegtocomplex, magnitude, angle)


class ICtrlQueue(FrozenClass):
    _isfrozen = freeze

    def ClearActions(self):
        lib.CtrlQueue_ClearActions()

    def ClearQueue(self):
        lib.CtrlQueue_ClearQueue()

    def Delete(self, ActionHandle):
        lib.CtrlQueue_Delete(ActionHandle)

    def DoAllQueue(self):
        lib.CtrlQueue_DoAllQueue()

    def Show(self):
        lib.CtrlQueue_Show()

    @property
    def ActionCode(self):
        return lib.CtrlQueue_Get_ActionCode()

    @property
    def DeviceHandle(self):
        return lib.CtrlQueue_Get_DeviceHandle()

    @property
    def NumActions(self):
        return lib.CtrlQueue_Get_NumActions()

    @property
    def PopAction(self):
        return lib.CtrlQueue_Get_PopAction()

    @property
    def Queue(self):
        return get_string_array(lib.CtrlQueue_Get_Queue)

    @property
    def QueueSize(self):
        return lib.CtrlQueue_Get_QueueSize()

    @property
    def Action(self):
        raise AttributeError("This property is write-only!")

    @Action.setter
    def Action(self, Param1):
        lib.CtrlQueue_Set_Action(Param1)


class IDSSimComs(FrozenClass):
    _isfrozen = freeze

    def BusVoltage(self, Index):
        return get_float64_array(lib.DSSimComs_BusVoltage, Index)

    def BusVoltagepu(self, Index):
        return get_float64_array(lib.DSSimComs_BusVoltagepu, Index)


class IDSSProgress(FrozenClass):
    _isfrozen = freeze

    def Close(self):
        lib.DSSProgress_Close()

    def Show(self):
        lib.DSSProgress_Show()

    @property
    def Caption(self):
        raise AttributeError("This property is write-only!")

    @Caption.setter
    def Caption(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.DSSProgress_Set_Caption(Value)

    @property
    def PctProgress(self):
        raise AttributeError("This property is write-only!")

    @PctProgress.setter
    def PctProgress(self, Value):
        lib.DSSProgress_Set_PctProgress(Value)


class IDSSProperty(FrozenClass):
    _isfrozen = freeze

    @property
    def Description(self):
        return get_string(lib.DSSProperty_Get_Description())

    @property
    def Name(self):
        return get_string(lib.DSSProperty_Get_Name())

    @property
    def Val(self):
        return get_string(lib.DSSProperty_Get_Val())

    @Val.setter
    def Val(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.DSSProperty_Set_Val(Value)


class IDSS_Executive(FrozenClass):
    _isfrozen = freeze

    def Command(self, i):
        return get_string(lib.DSS_Executive_Get_Command(i))

    def CommandHelp(self, i):
        return get_string(lib.DSS_Executive_Get_CommandHelp(i))

    def Option(self, i):
        return get_string(lib.DSS_Executive_Get_Option(i))

    def OptionHelp(self, i):
        return get_string(lib.DSS_Executive_Get_OptionHelp(i))

    def OptionValue(self, i):
        return get_string(lib.DSS_Executive_Get_OptionValue(i))

    @property
    def NumCommands(self):
        return lib.DSS_Executive_Get_NumCommands()

    @property
    def NumOptions(self):
        return lib.DSS_Executive_Get_NumOptions()


class IError(FrozenClass):
    _isfrozen = freeze

    @property
    def Description(self):
        return get_string(lib.Error_Get_Description())

    @property
    def Number(self):
        return lib.Error_Get_Number()




class IFuses(FrozenClass):
    _isfrozen = freeze

    def Close(self):
        lib.Fuses_Close()

    def Open(self):
        lib.Fuses_Open()

    @property
    def AllNames(self):
        return get_string_array(lib.Fuses_Get_AllNames)

    @property
    def Count(self):
        return lib.Fuses_Get_Count()

    @property
    def Delay(self):
        return lib.Fuses_Get_Delay()

    @Delay.setter
    def Delay(self, Value):
        lib.Fuses_Set_Delay(Value)

    @property
    def First(self):
        return lib.Fuses_Get_First()

    @property
    def MonitoredObj(self):
        return get_string(lib.Fuses_Get_MonitoredObj())

    @MonitoredObj.setter
    def MonitoredObj(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Fuses_Set_MonitoredObj(Value)

    @property
    def MonitoredTerm(self):
        return lib.Fuses_Get_MonitoredTerm()

    @MonitoredTerm.setter
    def MonitoredTerm(self, Value):
        lib.Fuses_Set_MonitoredTerm(Value)

    @property
    def Name(self):
        return get_string(lib.Fuses_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Fuses_Set_Name(Value)

    @property
    def Next(self):
        return lib.Fuses_Get_Next()

    @property
    def NumPhases(self):
        return lib.Fuses_Get_NumPhases()

    @property
    def RatedCurrent(self):
        return lib.Fuses_Get_RatedCurrent()

    @RatedCurrent.setter
    def RatedCurrent(self, Value):
        lib.Fuses_Set_RatedCurrent(Value)

    @property
    def SwitchedObj(self):
        return get_string(lib.Fuses_Get_SwitchedObj())

    @SwitchedObj.setter
    def SwitchedObj(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Fuses_Set_SwitchedObj(Value)

    @property
    def SwitchedTerm(self):
        return lib.Fuses_Get_SwitchedTerm()

    @SwitchedTerm.setter
    def SwitchedTerm(self, Value):
        lib.Fuses_Set_SwitchedTerm(Value)

    @property
    def TCCcurve(self):
        return get_string(lib.Fuses_Get_TCCcurve())

    @TCCcurve.setter
    def TCCcurve(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Fuses_Set_TCCcurve(Value)

    @property
    def idx(self):
        return lib.Fuses_Get_idx()

    @idx.setter
    def idx(self, Value):
        lib.Fuses_Set_idx(Value)


class IGenerators(FrozenClass):
    _isfrozen = freeze

    @property
    def AllNames(self):
        return get_string_array(lib.Generators_Get_AllNames)

    @property
    def Count(self):
        return lib.Generators_Get_Count()

    @property
    def First(self):
        return lib.Generators_Get_First()

    @property
    def ForcedON(self):
        return lib.Generators_Get_ForcedON() != 0

    @ForcedON.setter
    def ForcedON(self, Value):
        lib.Generators_Set_ForcedON(Value)

    @property
    def Model(self):
        return lib.Generators_Get_Model()

    @Model.setter
    def Model(self, Value):
        lib.Generators_Set_Model(Value)

    @property
    def Name(self):
        return get_string(lib.Generators_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Generators_Set_Name(Value)

    @property
    def Next(self):
        return lib.Generators_Get_Next()

    @property
    def PF(self):
        return lib.Generators_Get_PF()

    @PF.setter
    def PF(self, Value):
        lib.Generators_Set_PF(Value)

    @property
    def Phases(self):
        return lib.Generators_Get_Phases()

    @Phases.setter
    def Phases(self, Value):
        lib.Generators_Set_Phases(Value)

    @property
    def RegisterNames(self):
        return get_string_array(lib.Generators_Get_RegisterNames)

    @property
    def RegisterValues(self):
        return get_float64_array(lib.Generators_Get_RegisterValues)

    @property
    def Vmaxpu(self):
        return lib.Generators_Get_Vmaxpu()

    @Vmaxpu.setter
    def Vmaxpu(self, Value):
        lib.Generators_Set_Vmaxpu(Value)

    @property
    def Vminpu(self):
        return lib.Generators_Get_Vminpu()

    @Vminpu.setter
    def Vminpu(self, Value):
        lib.Generators_Set_Vminpu(Value)

    @property
    def idx(self):
        return lib.Generators_Get_idx()

    @idx.setter
    def idx(self, Value):
        lib.Generators_Set_idx(Value)

    @property
    def kV(self):
        return lib.Generators_Get_kV()

    @kV.setter
    def kV(self, Value):
        lib.Generators_Set_kV(Value)

    @property
    def kVArated(self):
        return lib.Generators_Get_kVArated()

    @kVArated.setter
    def kVArated(self, Value):
        lib.Generators_Set_kVArated(Value)

    @property
    def kW(self):
        return lib.Generators_Get_kW()

    @kW.setter
    def kW(self, Value):
        lib.Generators_Set_kW(Value)

    @property
    def kvar(self):
        return lib.Generators_Get_kvar()

    @kvar.setter
    def kvar(self, Value):
        lib.Generators_Set_kvar(Value)


class IISources(FrozenClass):
    _isfrozen = freeze

    @property
    def AllNames(self):
        return get_string_array(lib.ISources_Get_AllNames)

    @property
    def Amps(self):
        return lib.ISources_Get_Amps()

    @Amps.setter
    def Amps(self, Value):
        lib.ISources_Set_Amps(Value)

    @property
    def AngleDeg(self):
        return lib.ISources_Get_AngleDeg()

    @AngleDeg.setter
    def AngleDeg(self, Value):
        lib.ISources_Set_AngleDeg(Value)

    @property
    def Count(self):
        return lib.ISources_Get_Count()

    @property
    def First(self):
        return lib.ISources_Get_First()

    @property
    def Frequency(self):
        return lib.ISources_Get_Frequency()

    @Frequency.setter
    def Frequency(self, Value):
        lib.ISources_Set_Frequency(Value)

    @property
    def Name(self):
        return get_string(lib.ISources_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.ISources_Set_Name(Value)

    @property
    def Next(self):
        return lib.ISources_Get_Next()


class ILineCodes(FrozenClass):
    _isfrozen = freeze

    @property
    def AllNames(self):
        return get_string_array(lib.LineCodes_Get_AllNames)

    @property
    def C0(self):
        return lib.LineCodes_Get_C0()

    @C0.setter
    def C0(self, Value):
        lib.LineCodes_Set_C0(Value)

    @property
    def C1(self):
        return lib.LineCodes_Get_C1()

    @C1.setter
    def C1(self, Value):
        lib.LineCodes_Set_C1(Value)

    @property
    def Cmatrix(self):
        return get_float64_array(lib.LineCodes_Get_Cmatrix)

    @Cmatrix.setter
    def Cmatrix(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.LineCodes_Set_Cmatrix(ValuePtr, ValueCount)

    @property
    def Count(self):
        return lib.LineCodes_Get_Count()

    @property
    def EmergAmps(self):
        return lib.LineCodes_Get_EmergAmps()

    @EmergAmps.setter
    def EmergAmps(self, Value):
        lib.LineCodes_Set_EmergAmps(Value)

    @property
    def First(self):
        return lib.LineCodes_Get_First()

    @property
    def IsZ1Z0(self):
        return lib.LineCodes_Get_IsZ1Z0() != 0

    @property
    def Name(self):
        return get_string(lib.LineCodes_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.LineCodes_Set_Name(Value)

    @property
    def Next(self):
        return lib.LineCodes_Get_Next()

    @property
    def NormAmps(self):
        return lib.LineCodes_Get_NormAmps()

    @NormAmps.setter
    def NormAmps(self, Value):
        lib.LineCodes_Set_NormAmps(Value)

    @property
    def Phases(self):
        return lib.LineCodes_Get_Phases()

    @Phases.setter
    def Phases(self, Value):
        lib.LineCodes_Set_Phases(Value)

    @property
    def R0(self):
        return lib.LineCodes_Get_R0()

    @R0.setter
    def R0(self, Value):
        lib.LineCodes_Set_R0(Value)

    @property
    def R1(self):
        return lib.LineCodes_Get_R1()

    @R1.setter
    def R1(self, Value):
        lib.LineCodes_Set_R1(Value)

    @property
    def Rmatrix(self):
        return get_float64_array(lib.LineCodes_Get_Rmatrix)

    @Rmatrix.setter
    def Rmatrix(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.LineCodes_Set_Rmatrix(ValuePtr, ValueCount)

    @property
    def Units(self):
        return lib.LineCodes_Get_Units()

    @Units.setter
    def Units(self, Value):
        lib.LineCodes_Set_Units(Value)

    @property
    def X0(self):
        return lib.LineCodes_Get_X0()

    @X0.setter
    def X0(self, Value):
        lib.LineCodes_Set_X0(Value)

    @property
    def X1(self):
        return lib.LineCodes_Get_X1()

    @X1.setter
    def X1(self, Value):
        lib.LineCodes_Set_X1(Value)

    @property
    def Xmatrix(self):
        return get_float64_array(lib.LineCodes_Get_Xmatrix)

    @Xmatrix.setter
    def Xmatrix(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.LineCodes_Set_Xmatrix(ValuePtr, ValueCount)


class ILines(FrozenClass):
    _isfrozen = freeze

    def New(self, Name):
        if type(Name) is not bytes:
            Name = Name.encode(codec)

        return lib.Lines_New(Name)

    @property
    def AllNames(self):
        return get_string_array(lib.Lines_Get_AllNames)

    @property
    def Bus1(self):
        return get_string(lib.Lines_Get_Bus1())

    @Bus1.setter
    def Bus1(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Lines_Set_Bus1(Value)

    @property
    def Bus2(self):
        return get_string(lib.Lines_Get_Bus2())

    @Bus2.setter
    def Bus2(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Lines_Set_Bus2(Value)

    @property
    def C0(self):
        return lib.Lines_Get_C0()

    @C0.setter
    def C0(self, Value):
        lib.Lines_Set_C0(Value)

    @property
    def C1(self):
        return lib.Lines_Get_C1()

    @C1.setter
    def C1(self, Value):
        lib.Lines_Set_C1(Value)

    @property
    def Cmatrix(self):
        return get_float64_array(lib.Lines_Get_Cmatrix)

    @Cmatrix.setter
    def Cmatrix(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.Lines_Set_Cmatrix(ValuePtr, ValueCount)

    @property
    def Count(self):
        return lib.Lines_Get_Count()

    @property
    def EmergAmps(self):
        return lib.Lines_Get_EmergAmps()

    @EmergAmps.setter
    def EmergAmps(self, Value):
        lib.Lines_Set_EmergAmps(Value)

    @property
    def First(self):
        return lib.Lines_Get_First()

    @property
    def Geometry(self):
        return get_string(lib.Lines_Get_Geometry())

    @Geometry.setter
    def Geometry(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Lines_Set_Geometry(Value)

    @property
    def Length(self):
        return lib.Lines_Get_Length()

    @Length.setter
    def Length(self, Value):
        lib.Lines_Set_Length(Value)

    @property
    def LineCode(self):
        return get_string(lib.Lines_Get_LineCode())

    @LineCode.setter
    def LineCode(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Lines_Set_LineCode(Value)

    @property
    def Name(self):
        return get_string(lib.Lines_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Lines_Set_Name(Value)

    @property
    def Next(self):
        return lib.Lines_Get_Next()

    @property
    def NormAmps(self):
        return lib.Lines_Get_NormAmps()

    @NormAmps.setter
    def NormAmps(self, Value):
        lib.Lines_Set_NormAmps(Value)

    @property
    def NumCust(self):
        return lib.Lines_Get_NumCust()

    @property
    def Parent(self):
        return lib.Lines_Get_Parent()

    @property
    def Phases(self):
        return lib.Lines_Get_Phases()

    @Phases.setter
    def Phases(self, Value):
        lib.Lines_Set_Phases(Value)

    @property
    def R0(self):
        return lib.Lines_Get_R0()

    @R0.setter
    def R0(self, Value):
        lib.Lines_Set_R0(Value)

    @property
    def R1(self):
        return lib.Lines_Get_R1()

    @R1.setter
    def R1(self, Value):
        lib.Lines_Set_R1(Value)

    @property
    def Rg(self):
        return lib.Lines_Get_Rg()

    @Rg.setter
    def Rg(self, Value):
        lib.Lines_Set_Rg(Value)

    @property
    def Rho(self):
        return lib.Lines_Get_Rho()

    @Rho.setter
    def Rho(self, Value):
        lib.Lines_Set_Rho(Value)

    @property
    def Rmatrix(self):
        return get_float64_array(lib.Lines_Get_Rmatrix)

    @Rmatrix.setter
    def Rmatrix(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.Lines_Set_Rmatrix(ValuePtr, ValueCount)

    @property
    def Spacing(self):
        return get_string(lib.Lines_Get_Spacing())

    @Spacing.setter
    def Spacing(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Lines_Set_Spacing(Value)

    @property
    def TotalCust(self):
        return lib.Lines_Get_TotalCust()

    @property
    def Units(self):
        return lib.Lines_Get_Units()

    @Units.setter
    def Units(self, Value):
        lib.Lines_Set_Units(Value)

    @property
    def X0(self):
        return lib.Lines_Get_X0()

    @X0.setter
    def X0(self, Value):
        lib.Lines_Set_X0(Value)

    @property
    def X1(self):
        return lib.Lines_Get_X1()

    @X1.setter
    def X1(self, Value):
        lib.Lines_Set_X1(Value)

    @property
    def Xg(self):
        return lib.Lines_Get_Xg()

    @Xg.setter
    def Xg(self, Value):
        lib.Lines_Set_Xg(Value)

    @property
    def Xmatrix(self):
        return get_float64_array(lib.Lines_Get_Xmatrix)

    @Xmatrix.setter
    def Xmatrix(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.Lines_Set_Xmatrix(ValuePtr, ValueCount)

    @property
    def Yprim(self):
        return get_float64_array(lib.Lines_Get_Yprim)

    @Yprim.setter
    def Yprim(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.Lines_Set_Yprim(ValuePtr, ValueCount)


class ILoads(FrozenClass):
    _isfrozen = freeze

    @property
    def AllNames(self):
        return get_string_array(lib.Loads_Get_AllNames)

    @property
    def AllocationFactor(self):
        return lib.Loads_Get_AllocationFactor()

    @AllocationFactor.setter
    def AllocationFactor(self, Value):
        lib.Loads_Set_AllocationFactor(Value)

    @property
    def CVRcurve(self):
        return get_string(lib.Loads_Get_CVRcurve())

    @CVRcurve.setter
    def CVRcurve(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Loads_Set_CVRcurve(Value)

    @property
    def CVRvars(self):
        return lib.Loads_Get_CVRvars()

    @CVRvars.setter
    def CVRvars(self, Value):
        lib.Loads_Set_CVRvars(Value)

    @property
    def CVRwatts(self):
        return lib.Loads_Get_CVRwatts()

    @CVRwatts.setter
    def CVRwatts(self, Value):
        lib.Loads_Set_CVRwatts(Value)

    @property
    def Cfactor(self):
        return lib.Loads_Get_Cfactor()

    @Cfactor.setter
    def Cfactor(self, Value):
        lib.Loads_Set_Cfactor(Value)

    @property
    def Class(self):
        return lib.Loads_Get_Class_()

    @Class.setter
    def Class(self, Value):
        lib.Loads_Set_Class_(Value)

    @property
    def Count(self):
        return lib.Loads_Get_Count()

    @property
    def First(self):
        return lib.Loads_Get_First()

    @property
    def Growth(self):
        return get_string(lib.Loads_Get_Growth())

    @Growth.setter
    def Growth(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Loads_Set_Growth(Value)

    @property
    def IsDelta(self):
        return lib.Loads_Get_IsDelta() != 0

    @IsDelta.setter
    def IsDelta(self, Value):
        lib.Loads_Set_IsDelta(Value)

    @property
    def Model(self):
        return lib.Loads_Get_Model()

    @Model.setter
    def Model(self, Value):
        lib.Loads_Set_Model(Value)

    @property
    def Name(self):
        return get_string(lib.Loads_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Loads_Set_Name(Value)

    @property
    def Next(self):
        return lib.Loads_Get_Next()

    @property
    def NumCust(self):
        return lib.Loads_Get_NumCust()

    @NumCust.setter
    def NumCust(self, Value):
        lib.Loads_Set_NumCust(Value)

    @property
    def PF(self):
        return lib.Loads_Get_PF()

    @PF.setter
    def PF(self, Value):
        lib.Loads_Set_PF(Value)

    @property
    def PctMean(self):
        return lib.Loads_Get_PctMean()

    @PctMean.setter
    def PctMean(self, Value):
        lib.Loads_Set_PctMean(Value)

    @property
    def PctStdDev(self):
        return lib.Loads_Get_PctStdDev()

    @PctStdDev.setter
    def PctStdDev(self, Value):
        lib.Loads_Set_PctStdDev(Value)

    @property
    def RelWeight(self):
        return lib.Loads_Get_RelWeight()

    @property
    def Rneut(self):
        return lib.Loads_Get_Rneut()

    @Rneut.setter
    def Rneut(self, Value):
        lib.Loads_Set_Rneut(Value)

    @property
    def Spectrum(self):
        return get_string(lib.Loads_Get_Spectrum())

    @Spectrum.setter
    def Spectrum(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Loads_Set_Spectrum(Value)

    @property
    def Status(self):
        return lib.Loads_Get_Status()

    @Status.setter
    def Status(self, Value):
        lib.Loads_Set_Status(Value)

    @property
    def Vmaxpu(self):
        return lib.Loads_Get_Vmaxpu()

    @Vmaxpu.setter
    def Vmaxpu(self, Value):
        lib.Loads_Set_Vmaxpu(Value)

    @property
    def Vminemerg(self):
        return lib.Loads_Get_Vminemerg()

    @Vminemerg.setter
    def Vminemerg(self, Value):
        lib.Loads_Set_Vminemerg(Value)

    @property
    def Vminnorm(self):
        return lib.Loads_Get_Vminnorm()

    @Vminnorm.setter
    def Vminnorm(self, Value):
        lib.Loads_Set_Vminnorm(Value)

    @property
    def Vminpu(self):
        return lib.Loads_Get_Vminpu()

    @Vminpu.setter
    def Vminpu(self, Value):
        lib.Loads_Set_Vminpu(Value)

    @property
    def Xneut(self):
        return lib.Loads_Get_Xneut()

    @Xneut.setter
    def Xneut(self, Value):
        lib.Loads_Set_Xneut(Value)

    @property
    def Yearly(self):
        return get_string(lib.Loads_Get_Yearly())

    @Yearly.setter
    def Yearly(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Loads_Set_Yearly(Value)

    @property
    def ZIPV(self):
        return get_float64_array(lib.Loads_Get_ZIPV)

    @ZIPV.setter
    def ZIPV(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.Loads_Set_ZIPV(ValuePtr, ValueCount)

    @property
    def daily(self):
        return get_string(lib.Loads_Get_daily())

    @daily.setter
    def daily(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Loads_Set_daily(Value)

    @property
    def duty(self):
        return get_string(lib.Loads_Get_duty())

    @duty.setter
    def duty(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Loads_Set_duty(Value)

    @property
    def idx(self):
        return lib.Loads_Get_idx()

    @idx.setter
    def idx(self, Value):
        lib.Loads_Set_idx(Value)

    @property
    def kV(self):
        return lib.Loads_Get_kV()

    @kV.setter
    def kV(self, Value):
        lib.Loads_Set_kV(Value)

    @property
    def kW(self):
        return lib.Loads_Get_kW()

    @kW.setter
    def kW(self, Value):
        lib.Loads_Set_kW(Value)

    @property
    def kva(self):
        return lib.Loads_Get_kva()

    @kva.setter
    def kva(self, Value):
        lib.Loads_Set_kva(Value)

    @property
    def kvar(self):
        return lib.Loads_Get_kvar()

    @kvar.setter
    def kvar(self, Value):
        lib.Loads_Set_kvar(Value)

    @property
    def kwh(self):
        return lib.Loads_Get_kwh()

    @kwh.setter
    def kwh(self, Value):
        lib.Loads_Set_kwh(Value)

    @property
    def kwhdays(self):
        return lib.Loads_Get_kwhdays()

    @kwhdays.setter
    def kwhdays(self, Value):
        lib.Loads_Set_kwhdays(Value)

    @property
    def pctSeriesRL(self):
        return lib.Loads_Get_pctSeriesRL()

    @pctSeriesRL.setter
    def pctSeriesRL(self, Value):
        lib.Loads_Set_pctSeriesRL(Value)

    @property
    def xfkVA(self):
        return lib.Loads_Get_xfkVA()

    @xfkVA.setter
    def xfkVA(self, Value):
        lib.Loads_Set_xfkVA(Value)


class ILoadShapes(FrozenClass):
    _isfrozen = freeze

    def Normalize(self):
        lib.LoadShapes_Normalize()

    @property
    def AllNames(self):
        return get_string_array(lib.LoadShapes_Get_AllNames)

    @property
    def Count(self):
        return lib.LoadShapes_Get_Count()

    @property
    def First(self):
        return lib.LoadShapes_Get_First()

    @property
    def HrInterval(self):
        return lib.LoadShapes_Get_HrInterval()

    @HrInterval.setter
    def HrInterval(self, Value):
        lib.LoadShapes_Set_HrInterval(Value)

    @property
    def MinInterval(self):
        return lib.LoadShapes_Get_MinInterval()

    @MinInterval.setter
    def MinInterval(self, Value):
        lib.LoadShapes_Set_MinInterval(Value)

    @property
    def Name(self):
        return get_string(lib.LoadShapes_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.LoadShapes_Set_Name(Value)

    @property
    def Next(self):
        return lib.LoadShapes_Get_Next()

    @property
    def Npts(self):
        return lib.LoadShapes_Get_Npts()

    @Npts.setter
    def Npts(self, Value):
        lib.LoadShapes_Set_Npts(Value)

    @property
    def PBase(self):
        return lib.LoadShapes_Get_PBase()

    @PBase.setter
    def PBase(self, Value):
        lib.LoadShapes_Set_PBase(Value)

    @property
    def Pmult(self):
        return get_float64_array(lib.LoadShapes_Get_Pmult)

    @Pmult.setter
    def Pmult(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.LoadShapes_Set_Pmult(ValuePtr, ValueCount)

    @property
    def Qbase(self):
        return lib.LoadShapes_Get_Qbase()

    @Qbase.setter
    def Qbase(self, Value):
        lib.LoadShapes_Set_Qbase(Value)

    @property
    def Qmult(self):
        return get_float64_array(lib.LoadShapes_Get_Qmult)

    @Qmult.setter
    def Qmult(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.LoadShapes_Set_Qmult(ValuePtr, ValueCount)

    @property
    def TimeArray(self):
        return get_float64_array(lib.LoadShapes_Get_TimeArray)

    @TimeArray.setter
    def TimeArray(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.LoadShapes_Set_TimeArray(ValuePtr, ValueCount)

    @property
    def UseActual(self):
        return lib.LoadShapes_Get_UseActual() != 0

    @UseActual.setter
    def UseActual(self, Value):
        lib.LoadShapes_Set_UseActual(Value)

    @property
    def sInterval(self):
        return lib.LoadShapes_Get_sInterval()

    @sInterval.setter
    def sInterval(self, Value):
        lib.LoadShapes_Set_Sinterval(Value)


class IMeters(FrozenClass):
    _isfrozen = freeze

    def CloseAllDIFiles(self):
        lib.Meters_CloseAllDIFiles()

    def DoReliabilityCalc(self, AssumeRestoration):
        lib.Meters_DoReliabilityCalc(AssumeRestoration)

    def OpenAllDIFiles(self):
        lib.Meters_OpenAllDIFiles()

    def Reset(self):
        lib.Meters_Reset()

    def ResetAll(self):
        lib.Meters_ResetAll()

    def Sample(self):
        lib.Meters_Sample()

    def SampleAll(self):
        lib.Meters_SampleAll()

    def Save(self):
        lib.Meters_Save()

    def SaveAll(self):
        lib.Meters_SaveAll()

    def SetActiveSection(self, SectIdx):
        lib.Meters_SetActiveSection(SectIdx)

    @property
    def AllBranchesInZone(self):
        return get_string_array(lib.Meters_Get_AllBranchesInZone)

    @property
    def AllEndElements(self):
        return get_string_array(lib.Meters_Get_AllEndElements)

    @property
    def AllNames(self):
        return get_string_array(lib.Meters_Get_AllNames)

    @property
    def AllocFactors(self):
        return get_float64_array(lib.Meters_Get_AllocFactors)

    @AllocFactors.setter
    def AllocFactors(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.Meters_Set_AllocFactors(ValuePtr, ValueCount)

    @property
    def AvgRepairTime(self):
        return lib.Meters_Get_AvgRepairTime()

    @property
    def CalcCurrent(self):
        return get_float64_array(lib.Meters_Get_CalcCurrent)

    @CalcCurrent.setter
    def CalcCurrent(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.Meters_Set_CalcCurrent(ValuePtr, ValueCount)

    @property
    def Count(self):
        return lib.Meters_Get_Count()

    @property
    def CountBranches(self):
        return lib.Meters_Get_CountBranches()

    @property
    def CountEndElements(self):
        return lib.Meters_Get_CountEndElements()

    @property
    def CustInterrupts(self):
        return lib.Meters_Get_CustInterrupts()

    @property
    def DIFilesAreOpen(self):
        return lib.Meters_Get_DIFilesAreOpen() != 0

    @property
    def FaultRateXRepairHrs(self):
        return lib.Meters_Get_FaultRateXRepairHrs()

    @property
    def First(self):
        return lib.Meters_Get_First()

    @property
    def MeteredElement(self):
        return get_string(lib.Meters_Get_MeteredElement())

    @MeteredElement.setter
    def MeteredElement(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Meters_Set_MeteredElement(Value)

    @property
    def MeteredTerminal(self):
        return lib.Meters_Get_MeteredTerminal()

    @MeteredTerminal.setter
    def MeteredTerminal(self, Value):
        lib.Meters_Set_MeteredTerminal(Value)

    @property
    def Name(self):
        return get_string(lib.Meters_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Meters_Set_Name(Value)

    @property
    def Next(self):
        return lib.Meters_Get_Next()

    @property
    def NumSectionBranches(self):
        return lib.Meters_Get_NumSectionBranches()

    @property
    def NumSectionCustomers(self):
        return lib.Meters_Get_NumSectionCustomers()

    @property
    def NumSections(self):
        return lib.Meters_Get_NumSections()

    @property
    def OCPDeviceType(self):
        return lib.Meters_Get_OCPDeviceType()

    @property
    def Peakcurrent(self):
        return get_float64_array(lib.Meters_Get_Peakcurrent)

    @Peakcurrent.setter
    def Peakcurrent(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.Meters_Set_Peakcurrent(ValuePtr, ValueCount)

    @property
    def RegisterNames(self):
        return get_string_array(lib.Meters_Get_RegisterNames)

    @property
    def RegisterValues(self):
        return get_float64_array(lib.Meters_Get_RegisterValues)

    @property
    def SAIDI(self):
        return lib.Meters_Get_SAIDI()

    @property
    def SAIFI(self):
        return lib.Meters_Get_SAIFI()

    @property
    def SAIFIKW(self):
        return lib.Meters_Get_SAIFIKW()

    @property
    def SectSeqIdx(self):
        return lib.Meters_Get_SectSeqIdx()

    @property
    def SectTotalCust(self):
        return lib.Meters_Get_SectTotalCust()

    @property
    def SeqListSize(self):
        return lib.Meters_Get_SeqListSize()

    @property
    def SequenceIndex(self):
        return lib.Meters_Get_SequenceIndex()

    @SequenceIndex.setter
    def SequenceIndex(self, Value):
        lib.Meters_Set_SequenceIndex(Value)

    @property
    def SumBranchFltRates(self):
        return lib.Meters_Get_SumBranchFltRates()

    @property
    def TotalCustomers(self):
        return lib.Meters_Get_TotalCustomers()

    @property
    def Totals(self):
        return get_float64_array(lib.Meters_Get_Totals)


class IMonitors(FrozenClass):
    _isfrozen = freeze

    def Channel(self, Index):
        return get_float64_array(lib.Monitors_Get_Channel, Index)

    def Process(self):
        lib.Monitors_Process()

    def ProcessAll(self):
        lib.Monitors_ProcessAll()

    def Reset(self):
        lib.Monitors_Reset()

    def ResetAll(self):
        lib.Monitors_ResetAll()

    def Sample(self):
        lib.Monitors_Sample()

    def SampleAll(self):
        lib.Monitors_SampleAll()

    def Save(self):
        lib.Monitors_Save()

    def SaveAll(self):
        lib.Monitors_SaveAll()

    def Show(self):
        lib.Monitors_Show()

    @property
    def AllNames(self):
        return get_string_array(lib.Monitors_Get_AllNames)

    @property
    def ByteStream(self):
        return get_int8_array(lib.Monitors_Get_ByteStream)

    @property
    def Count(self):
        return lib.Monitors_Get_Count()

    @property
    def Element(self):
        return get_string(lib.Monitors_Get_Element())

    @Element.setter
    def Element(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Monitors_Set_Element(Value)

    @property
    def FileName(self):
        return get_string(lib.Monitors_Get_FileName())

    @property
    def FileVersion(self):
        return lib.Monitors_Get_FileVersion()

    @property
    def First(self):
        return lib.Monitors_Get_First()

    @property
    def Header(self):
        return get_string_array(lib.Monitors_Get_Header)

    @property
    def Mode(self):
        return lib.Monitors_Get_Mode()

    @Mode.setter
    def Mode(self, Value):
        lib.Monitors_Set_Mode(Value)

    @property
    def Name(self):
        return get_string(lib.Monitors_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Monitors_Set_Name(Value)

    @property
    def Next(self):
        return lib.Monitors_Get_Next()

    @property
    def NumChannels(self):
        return lib.Monitors_Get_NumChannels()

    @property
    def RecordSize(self):
        return lib.Monitors_Get_RecordSize()

    @property
    def SampleCount(self):
        return lib.Monitors_Get_SampleCount()

    @property
    def Terminal(self):
        return lib.Monitors_Get_Terminal()

    @Terminal.setter
    def Terminal(self, Value):
        lib.Monitors_Set_Terminal(Value)

    @property
    def dblFreq(self):
        return get_float64_array(lib.Monitors_Get_dblFreq)

    @property
    def dblHour(self):
        return get_float64_array(lib.Monitors_Get_dblHour)


class IParser(FrozenClass):
    _isfrozen = freeze

    def Matrix(self, ExpectedOrder):
        return get_float64_array(lib.Parser_Get_Matrix, ExpectedOrder)

    def SymMatrix(self, ExpectedOrder):
        return get_float64_array(lib.Parser_Get_SymMatrix, ExpectedOrder)

    def Vector(self, ExpectedSize):
        return get_float64_array(lib.Parser_Get_Vector, ExpectedSize)

    def ResetDelimiters(self):
        lib.Parser_ResetDelimiters()

    @property
    def AutoIncrement(self):
        return lib.Parser_Get_AutoIncrement() != 0

    @AutoIncrement.setter
    def AutoIncrement(self, Value):
        lib.Parser_Set_AutoIncrement(Value)

    @property
    def BeginQuote(self):
        return get_string(lib.Parser_Get_BeginQuote())

    @BeginQuote.setter
    def BeginQuote(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Parser_Set_BeginQuote(Value)

    @property
    def CmdString(self):
        return get_string(lib.Parser_Get_CmdString())

    @CmdString.setter
    def CmdString(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Parser_Set_CmdString(Value)

    @property
    def DblValue(self):
        return lib.Parser_Get_DblValue()

    @property
    def Delimiters(self):
        return get_string(lib.Parser_Get_Delimiters())

    @Delimiters.setter
    def Delimiters(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Parser_Set_Delimiters(Value)

    @property
    def EndQuote(self):
        return get_string(lib.Parser_Get_EndQuote())

    @EndQuote.setter
    def EndQuote(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Parser_Set_EndQuote(Value)

    @property
    def IntValue(self):
        return lib.Parser_Get_IntValue()

    @property
    def NextParam(self):
        return get_string(lib.Parser_Get_NextParam())

    @property
    def StrValue(self):
        return get_string(lib.Parser_Get_StrValue())

    @property
    def WhiteSpace(self):
        return get_string(lib.Parser_Get_WhiteSpace())

    @WhiteSpace.setter
    def WhiteSpace(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Parser_Set_WhiteSpace(Value)


class IPDElements(FrozenClass):
    _isfrozen = freeze

    @property
    def AccumulatedL(self):
        return lib.PDElements_Get_AccumulatedL()

    @property
    def Count(self):
        return lib.PDElements_Get_Count()

    @property
    def FaultRate(self):
        return lib.PDElements_Get_FaultRate()

    @FaultRate.setter
    def FaultRate(self, Value):
        lib.PDElements_Set_FaultRate(Value)

    @property
    def First(self):
        return lib.PDElements_Get_First()

    @property
    def FromTerminal(self):
        return lib.PDElements_Get_FromTerminal()

    @property
    def IsShunt(self):
        return lib.PDElements_Get_IsShunt() != 0

    @property
    def Lambda(self):
        return lib.PDElements_Get_Lambda()

    @property
    def Name(self):
        return get_string(lib.PDElements_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.PDElements_Set_Name(Value)

    @property
    def Next(self):
        return lib.PDElements_Get_Next()

    @property
    def Numcustomers(self):
        return lib.PDElements_Get_Numcustomers()

    @property
    def ParentPDElement(self):
        return lib.PDElements_Get_ParentPDElement()

    @property
    def RepairTime(self):
        return lib.PDElements_Get_RepairTime()

    @RepairTime.setter
    def RepairTime(self, Value):
        lib.PDElements_Set_RepairTime(Value)

    @property
    def SectionID(self):
        return lib.PDElements_Get_SectionID()

    @property
    def TotalMiles(self):
        return lib.PDElements_Get_TotalMiles()

    @property
    def Totalcustomers(self):
        return lib.PDElements_Get_Totalcustomers()

    @property
    def pctPermanent(self):
        return lib.PDElements_Get_pctPermanent()

    @pctPermanent.setter
    def pctPermanent(self, Value):
        lib.PDElements_Set_pctPermanent(Value)


class IPVSystems(FrozenClass):
    _isfrozen = freeze

    @property
    def AllNames(self):
        return get_string_array(lib.PVSystems_Get_AllNames)

    @property
    def Count(self):
        return lib.PVSystems_Get_Count()

    @property
    def First(self):
        return lib.PVSystems_Get_First()

    @property
    def Irradiance(self):
        return lib.PVSystems_Get_Irradiance()

    @Irradiance.setter
    def Irradiance(self, Value):
        lib.PVSystems_Set_Irradiance(Value)

    @property
    def Name(self):
        return get_string(lib.PVSystems_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.PVSystems_Set_Name(Value)

    @property
    def Next(self):
        return lib.PVSystems_Get_Next()

    @property
    def PF(self):
        return lib.PVSystems_Get_PF()

    @property
    def RegisterNames(self):
        return get_string_array(lib.PVSystems_Get_RegisterNames)

    @property
    def RegisterValues(self):
        return get_float64_array(lib.PVSystems_Get_RegisterValues)

    @property
    def idx(self):
        return lib.PVSystems_Get_idx()

    @idx.setter
    def idx(self, Value):
        lib.PVSystems_Set_idx(Value)

    @property
    def kVArated(self):
        return lib.PVSystems_Get_kVArated()

    @property
    def kW(self):
        return lib.PVSystems_Get_kW()

    @property
    def kvar(self):
        return lib.PVSystems_Get_kvar()


class IReclosers(FrozenClass):
    _isfrozen = freeze

    def Close(self):
        lib.Reclosers_Close()

    def Open(self):
        lib.Reclosers_Open()

    @property
    def AllNames(self):
        return get_string_array(lib.Reclosers_Get_AllNames)

    @property
    def Count(self):
        return lib.Reclosers_Get_Count()

    @property
    def First(self):
        return lib.Reclosers_Get_First()

    @property
    def GroundInst(self):
        return lib.Reclosers_Get_GroundInst()

    @GroundInst.setter
    def GroundInst(self, Value):
        lib.Reclosers_Set_GroundInst(Value)

    @property
    def GroundTrip(self):
        return lib.Reclosers_Get_GroundTrip()

    @GroundTrip.setter
    def GroundTrip(self, Value):
        lib.Reclosers_Set_GroundTrip(Value)

    @property
    def MonitoredObj(self):
        return get_string(lib.Reclosers_Get_MonitoredObj())

    @MonitoredObj.setter
    def MonitoredObj(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Reclosers_Set_MonitoredObj(Value)

    @property
    def MonitoredTerm(self):
        return lib.Reclosers_Get_MonitoredTerm()

    @MonitoredTerm.setter
    def MonitoredTerm(self, Value):
        lib.Reclosers_Set_MonitoredTerm(Value)

    @property
    def Name(self):
        return get_string(lib.Reclosers_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Reclosers_Set_Name(Value)

    @property
    def Next(self):
        return lib.Reclosers_Get_Next()

    @property
    def NumFast(self):
        return lib.Reclosers_Get_NumFast()

    @NumFast.setter
    def NumFast(self, Value):
        lib.Reclosers_Set_NumFast(Value)

    @property
    def PhaseInst(self):
        return lib.Reclosers_Get_PhaseInst()

    @PhaseInst.setter
    def PhaseInst(self, Value):
        lib.Reclosers_Set_PhaseInst(Value)

    @property
    def PhaseTrip(self):
        return lib.Reclosers_Get_PhaseTrip()

    @PhaseTrip.setter
    def PhaseTrip(self, Value):
        lib.Reclosers_Set_PhaseTrip(Value)

    @property
    def RecloseIntervals(self):
        return get_float64_array(lib.Reclosers_Get_RecloseIntervals)

    @property
    def Shots(self):
        return lib.Reclosers_Get_Shots()

    @Shots.setter
    def Shots(self, Value):
        lib.Reclosers_Set_Shots(Value)

    @property
    def SwitchedObj(self):
        return get_string(lib.Reclosers_Get_SwitchedObj())

    @SwitchedObj.setter
    def SwitchedObj(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Reclosers_Set_SwitchedObj(Value)

    @property
    def SwitchedTerm(self):
        return lib.Reclosers_Get_SwitchedTerm()

    @SwitchedTerm.setter
    def SwitchedTerm(self, Value):
        lib.Reclosers_Set_SwitchedTerm(Value)

    @property
    def idx(self):
        return lib.Reclosers_Get_idx()

    @idx.setter
    def idx(self, Value):
        lib.Reclosers_Set_idx(Value)


class IRegControls(FrozenClass):
    _isfrozen = freeze

    def Reset(self):
        lib.RegControls_Reset()

    @property
    def AllNames(self):
        return get_string_array(lib.RegControls_Get_AllNames)

    @property
    def CTPrimary(self):
        return lib.RegControls_Get_CTPrimary()

    @CTPrimary.setter
    def CTPrimary(self, Value):
        lib.RegControls_Set_CTPrimary(Value)

    @property
    def Count(self):
        return lib.RegControls_Get_Count()

    @property
    def Delay(self):
        return lib.RegControls_Get_Delay()

    @Delay.setter
    def Delay(self, Value):
        lib.RegControls_Set_Delay(Value)

    @property
    def First(self):
        return lib.RegControls_Get_First()

    @property
    def ForwardBand(self):
        return lib.RegControls_Get_ForwardBand()

    @ForwardBand.setter
    def ForwardBand(self, Value):
        lib.RegControls_Set_ForwardBand(Value)

    @property
    def ForwardR(self):
        return lib.RegControls_Get_ForwardR()

    @ForwardR.setter
    def ForwardR(self, Value):
        lib.RegControls_Set_ForwardR(Value)

    @property
    def ForwardVreg(self):
        return lib.RegControls_Get_ForwardVreg()

    @ForwardVreg.setter
    def ForwardVreg(self, Value):
        lib.RegControls_Set_ForwardVreg(Value)

    @property
    def ForwardX(self):
        return lib.RegControls_Get_ForwardX()

    @ForwardX.setter
    def ForwardX(self, Value):
        lib.RegControls_Set_ForwardX(Value)

    @property
    def IsInverseTime(self):
        return lib.RegControls_Get_IsInverseTime() != 0

    @IsInverseTime.setter
    def IsInverseTime(self, Value):
        lib.RegControls_Set_IsInverseTime(Value)

    @property
    def IsReversible(self):
        return lib.RegControls_Get_IsReversible() != 0

    @IsReversible.setter
    def IsReversible(self, Value):
        lib.RegControls_Set_IsReversible(Value)

    @property
    def MaxTapChange(self):
        return lib.RegControls_Get_MaxTapChange()

    @MaxTapChange.setter
    def MaxTapChange(self, Value):
        lib.RegControls_Set_MaxTapChange(Value)

    @property
    def MonitoredBus(self):
        return get_string(lib.RegControls_Get_MonitoredBus())

    @MonitoredBus.setter
    def MonitoredBus(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.RegControls_Set_MonitoredBus(Value)

    @property
    def Name(self):
        return get_string(lib.RegControls_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.RegControls_Set_Name(Value)

    @property
    def Next(self):
        return lib.RegControls_Get_Next()

    @property
    def PTratio(self):
        return lib.RegControls_Get_PTratio()

    @PTratio.setter
    def PTratio(self, Value):
        lib.RegControls_Set_PTratio(Value)

    @property
    def ReverseBand(self):
        return lib.RegControls_Get_ReverseBand()

    @ReverseBand.setter
    def ReverseBand(self, Value):
        lib.RegControls_Set_ReverseBand(Value)

    @property
    def ReverseR(self):
        return lib.RegControls_Get_ReverseR()

    @ReverseR.setter
    def ReverseR(self, Value):
        lib.RegControls_Set_ReverseR(Value)

    @property
    def ReverseVreg(self):
        return lib.RegControls_Get_ReverseVreg()

    @ReverseVreg.setter
    def ReverseVreg(self, Value):
        lib.RegControls_Set_ReverseVreg(Value)

    @property
    def ReverseX(self):
        return lib.RegControls_Get_ReverseX()

    @ReverseX.setter
    def ReverseX(self, Value):
        lib.RegControls_Set_ReverseX(Value)

    @property
    def TapDelay(self):
        return lib.RegControls_Get_TapDelay()

    @TapDelay.setter
    def TapDelay(self, Value):
        lib.RegControls_Set_TapDelay(Value)

    @property
    def TapNumber(self):
        return lib.RegControls_Get_TapNumber()

    @TapNumber.setter
    def TapNumber(self, Value):
        lib.RegControls_Set_TapNumber(Value)

    @property
    def TapWinding(self):
        return lib.RegControls_Get_TapWinding()

    @TapWinding.setter
    def TapWinding(self, Value):
        lib.RegControls_Set_TapWinding(Value)

    @property
    def Transformer(self):
        return get_string(lib.RegControls_Get_Transformer())

    @Transformer.setter
    def Transformer(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.RegControls_Set_Transformer(Value)

    @property
    def VoltageLimit(self):
        return lib.RegControls_Get_VoltageLimit()

    @VoltageLimit.setter
    def VoltageLimit(self, Value):
        lib.RegControls_Set_VoltageLimit(Value)

    @property
    def Winding(self):
        return lib.RegControls_Get_Winding()

    @Winding.setter
    def Winding(self, Value):
        lib.RegControls_Set_Winding(Value)


class IRelays(FrozenClass):
    _isfrozen = freeze

    @property
    def AllNames(self):
        return get_string_array(lib.Relays_Get_AllNames)

    @property
    def Count(self):
        return lib.Relays_Get_Count()

    @property
    def First(self):
        return lib.Relays_Get_First()

    @property
    def MonitoredObj(self):
        return get_string(lib.Relays_Get_MonitoredObj())

    @MonitoredObj.setter
    def MonitoredObj(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Relays_Set_MonitoredObj(Value)

    @property
    def MonitoredTerm(self):
        return lib.Relays_Get_MonitoredTerm()

    @MonitoredTerm.setter
    def MonitoredTerm(self, Value):
        lib.Relays_Set_MonitoredTerm(Value)

    @property
    def Name(self):
        return get_string(lib.Relays_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Relays_Set_Name(Value)

    @property
    def Next(self):
        return lib.Relays_Get_Next()

    @property
    def SwitchedObj(self):
        return get_string(lib.Relays_Get_SwitchedObj())

    @SwitchedObj.setter
    def SwitchedObj(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Relays_Set_SwitchedObj(Value)

    @property
    def SwitchedTerm(self):
        return lib.Relays_Get_SwitchedTerm()

    @SwitchedTerm.setter
    def SwitchedTerm(self, Value):
        lib.Relays_Set_SwitchedTerm(Value)

    @property
    def idx(self):
        return lib.Relays_Get_idx()

    @idx.setter
    def idx(self, Value):
        lib.Relays_Set_idx(Value)


class ISensors(FrozenClass):
    _isfrozen = freeze

    def Reset(self):
        lib.Sensors_Reset()

    def ResetAll(self):
        lib.Sensors_ResetAll()

    @property
    def AllNames(self):
        return get_string_array(lib.Sensors_Get_AllNames)

    @property
    def Count(self):
        return lib.Sensors_Get_Count()

    @property
    def Currents(self):
        return get_float64_array(lib.Sensors_Get_Currents)

    @Currents.setter
    def Currents(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.Sensors_Set_Currents(ValuePtr, ValueCount)

    @property
    def First(self):
        return lib.Sensors_Get_First()

    @property
    def IsDelta(self):
        return lib.Sensors_Get_IsDelta() != 0

    @IsDelta.setter
    def IsDelta(self, Value):
        lib.Sensors_Set_IsDelta(Value)

    @property
    def MeteredElement(self):
        return get_string(lib.Sensors_Get_MeteredElement())

    @MeteredElement.setter
    def MeteredElement(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Sensors_Set_MeteredElement(Value)

    @property
    def MeteredTerminal(self):
        return lib.Sensors_Get_MeteredTerminal()

    @MeteredTerminal.setter
    def MeteredTerminal(self, Value):
        lib.Sensors_Set_MeteredTerminal(Value)

    @property
    def Name(self):
        return get_string(lib.Sensors_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Sensors_Set_Name(Value)

    @property
    def Next(self):
        return lib.Sensors_Get_Next()

    @property
    def PctError(self):
        return lib.Sensors_Get_PctError()

    @PctError.setter
    def PctError(self, Value):
        lib.Sensors_Set_PctError(Value)

    @property
    def ReverseDelta(self):
        return lib.Sensors_Get_ReverseDelta() != 0

    @ReverseDelta.setter
    def ReverseDelta(self, Value):
        lib.Sensors_Set_ReverseDelta(Value)

    @property
    def Weight(self):
        return lib.Sensors_Get_Weight()

    @Weight.setter
    def Weight(self, Value):
        lib.Sensors_Set_Weight(Value)

    @property
    def kVARS(self):
        return get_float64_array(lib.Sensors_Get_kVARS)

    @kVARS.setter
    def kVARS(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.Sensors_Set_kVARS(ValuePtr, ValueCount)

    @property
    def kVS(self):
        return get_float64_array(lib.Sensors_Get_kVS)

    @kVS.setter
    def kVS(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.Sensors_Set_kVS(ValuePtr, ValueCount)

    @property
    def kVbase(self):
        return lib.Sensors_Get_kVbase()

    @kVbase.setter
    def kVbase(self, Value):
        lib.Sensors_Set_kVbase(Value)

    @property
    def kWS(self):
        return get_float64_array(lib.Sensors_Get_kWS)

    @kWS.setter
    def kWS(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.Sensors_Set_kWS(ValuePtr, ValueCount)


class ISettings(FrozenClass):
    _isfrozen = freeze

    @property
    def AllowDuplicates(self):
        return lib.Settings_Get_AllowDuplicates() != 0

    @AllowDuplicates.setter
    def AllowDuplicates(self, Value):
        lib.Settings_Set_AllowDuplicates(Value)

    @property
    def AutoBusList(self):
        return get_string(lib.Settings_Get_AutoBusList())

    @AutoBusList.setter
    def AutoBusList(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Settings_Set_AutoBusList(Value)

    @property
    def CktModel(self):
        return lib.Settings_Get_CktModel()

    @CktModel.setter
    def CktModel(self, Value):
        lib.Settings_Set_CktModel(Value)

    @property
    def ControlTrace(self):
        return lib.Settings_Get_ControlTrace() != 0

    @ControlTrace.setter
    def ControlTrace(self, Value):
        lib.Settings_Set_ControlTrace(Value)

    @property
    def EmergVmaxpu(self):
        return lib.Settings_Get_EmergVmaxpu()

    @EmergVmaxpu.setter
    def EmergVmaxpu(self, Value):
        lib.Settings_Set_EmergVmaxpu(Value)

    @property
    def EmergVminpu(self):
        return lib.Settings_Get_EmergVminpu()

    @EmergVminpu.setter
    def EmergVminpu(self, Value):
        lib.Settings_Set_EmergVminpu(Value)

    @property
    def LossRegs(self):
        return get_int32_array(lib.Settings_Get_LossRegs)

    @LossRegs.setter
    def LossRegs(self, Value):
        Value, ValuePtr, ValueCount = prepare_int32_array(Value)
        lib.Settings_Set_LossRegs(ValuePtr, ValueCount)

    @property
    def LossWeight(self):
        return lib.Settings_Get_LossWeight()

    @LossWeight.setter
    def LossWeight(self, Value):
        lib.Settings_Set_LossWeight(Value)

    @property
    def NormVmaxpu(self):
        return lib.Settings_Get_NormVmaxpu()

    @NormVmaxpu.setter
    def NormVmaxpu(self, Value):
        lib.Settings_Set_NormVmaxpu(Value)

    @property
    def NormVminpu(self):
        return lib.Settings_Get_NormVminpu()

    @NormVminpu.setter
    def NormVminpu(self, Value):
        lib.Settings_Set_NormVminpu(Value)

    @property
    def PriceCurve(self):
        return get_string(lib.Settings_Get_PriceCurve())

    @PriceCurve.setter
    def PriceCurve(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Settings_Set_PriceCurve(Value)

    @property
    def PriceSignal(self):
        return lib.Settings_Get_PriceSignal()

    @PriceSignal.setter
    def PriceSignal(self, Value):
        lib.Settings_Set_PriceSignal(Value)

    @property
    def Trapezoidal(self):
        return lib.Settings_Get_Trapezoidal() != 0

    @Trapezoidal.setter
    def Trapezoidal(self, Value):
        lib.Settings_Set_Trapezoidal(Value)

    @property
    def UEregs(self):
        return get_int32_array(lib.Settings_Get_UEregs)

    @UEregs.setter
    def UEregs(self, Value):
        Value, ValuePtr, ValueCount = prepare_int32_array(Value)
        lib.Settings_Set_UEregs(ValuePtr, ValueCount)

    @property
    def UEweight(self):
        return lib.Settings_Get_UEweight()

    @UEweight.setter
    def UEweight(self, Value):
        lib.Settings_Set_UEweight(Value)

    @property
    def VoltageBases(self):
        return get_float64_array(lib.Settings_Get_VoltageBases)

    @VoltageBases.setter
    def VoltageBases(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.Settings_Set_VoltageBases(ValuePtr, ValueCount)

    @property
    def ZoneLock(self):
        return lib.Settings_Get_ZoneLock() != 0

    @ZoneLock.setter
    def ZoneLock(self, Value):
        lib.Settings_Set_ZoneLock(Value)

    @property
    def AllocationFactors(self):
        raise AttributeError("This property is write-only!")

    @AllocationFactors.setter
    def AllocationFactors(self, Value):
        lib.Settings_Set_AllocationFactors(Value)


class ISolution(FrozenClass):
    _isfrozen = freeze

    def BuildYMatrix(self, BuildOption, AllocateVI):
        lib.Solution_BuildYMatrix(BuildOption, AllocateVI)

    def CheckControls(self):
        lib.Solution_CheckControls()

    def CheckFaultStatus(self):
        lib.Solution_CheckFaultStatus()

    def Cleanup(self):
        lib.Solution_Cleanup()

    def DoControlActions(self):
        lib.Solution_DoControlActions()

    def FinishTimeStep(self):
        lib.Solution_FinishTimeStep()

    def InitSnap(self):
        lib.Solution_InitSnap()

    def SampleControlDevices(self):
        lib.Solution_SampleControlDevices()

    def Sample_DoControlActions(self):
        lib.Solution_Sample_DoControlActions()

    def Solve(self):
        lib.Solution_Solve()

    def SolveDirect(self):
        lib.Solution_SolveDirect()

    def SolveNoControl(self):
        lib.Solution_SolveNoControl()

    def SolvePflow(self):
        lib.Solution_SolvePflow()

    def SolvePlusControl(self):
        lib.Solution_SolvePlusControl()

    def SolveSnap(self):
        lib.Solution_SolveSnap()

    @property
    def AddType(self):
        return lib.Solution_Get_AddType()

    @AddType.setter
    def AddType(self, Value):
        lib.Solution_Set_AddType(Value)

    @property
    def Algorithm(self):
        return lib.Solution_Get_Algorithm()

    @Algorithm.setter
    def Algorithm(self, Value):
        lib.Solution_Set_Algorithm(Value)

    @property
    def Capkvar(self):
        return lib.Solution_Get_Capkvar()

    @Capkvar.setter
    def Capkvar(self, Value):
        lib.Solution_Set_Capkvar(Value)

    @property
    def ControlActionsDone(self):
        return lib.Solution_Get_ControlActionsDone() != 0

    @ControlActionsDone.setter
    def ControlActionsDone(self, Value):
        lib.Solution_Set_ControlActionsDone(Value)

    @property
    def ControlIterations(self):
        return lib.Solution_Get_ControlIterations()

    @ControlIterations.setter
    def ControlIterations(self, Value):
        lib.Solution_Set_ControlIterations(Value)

    @property
    def ControlMode(self):
        return lib.Solution_Get_ControlMode()

    @ControlMode.setter
    def ControlMode(self, Value):
        lib.Solution_Set_ControlMode(Value)

    @property
    def Converged(self):
        return lib.Solution_Get_Converged() != 0

    @Converged.setter
    def Converged(self, Value):
        lib.Solution_Set_Converged(Value)

    @property
    def DefaultDaily(self):
        return get_string(lib.Solution_Get_DefaultDaily())

    @DefaultDaily.setter
    def DefaultDaily(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Solution_Set_DefaultDaily(Value)

    @property
    def DefaultYearly(self):
        return get_string(lib.Solution_Get_DefaultYearly())

    @DefaultYearly.setter
    def DefaultYearly(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Solution_Set_DefaultYearly(Value)

    @property
    def EventLog(self):
        return get_string_array(lib.Solution_Get_EventLog)

    @property
    def Frequency(self):
        return lib.Solution_Get_Frequency()

    @Frequency.setter
    def Frequency(self, Value):
        lib.Solution_Set_Frequency(Value)

    @property
    def GenMult(self):
        return lib.Solution_Get_GenMult()

    @GenMult.setter
    def GenMult(self, Value):
        lib.Solution_Set_GenMult(Value)

    @property
    def GenPF(self):
        return lib.Solution_Get_GenPF()

    @GenPF.setter
    def GenPF(self, Value):
        lib.Solution_Set_GenPF(Value)

    @property
    def GenkW(self):
        return lib.Solution_Get_GenkW()

    @GenkW.setter
    def GenkW(self, Value):
        lib.Solution_Set_GenkW(Value)

    @property
    def Hour(self):
        return lib.Solution_Get_Hour()

    @Hour.setter
    def Hour(self, Value):
        lib.Solution_Set_Hour(Value)

    @property
    def IntervalHrs(self):
        return lib.Solution_Get_IntervalHrs()

    @IntervalHrs.setter
    def IntervalHrs(self, Value):
        lib.Solution_Set_IntervalHrs(Value)

    @property
    def Iterations(self):
        return lib.Solution_Get_Iterations()

    @property
    def LDCurve(self):
        return get_string(lib.Solution_Get_LDCurve())

    @LDCurve.setter
    def LDCurve(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Solution_Set_LDCurve(Value)

    @property
    def LoadModel(self):
        return lib.Solution_Get_LoadModel()

    @LoadModel.setter
    def LoadModel(self, Value):
        lib.Solution_Set_LoadModel(Value)

    @property
    def LoadMult(self):
        return lib.Solution_Get_LoadMult()

    @LoadMult.setter
    def LoadMult(self, Value):
        lib.Solution_Set_LoadMult(Value)

    @property
    def MaxControlIterations(self):
        return lib.Solution_Get_MaxControlIterations()

    @MaxControlIterations.setter
    def MaxControlIterations(self, Value):
        lib.Solution_Set_MaxControlIterations(Value)

    @property
    def MaxIterations(self):
        return lib.Solution_Get_MaxIterations()

    @MaxIterations.setter
    def MaxIterations(self, Value):
        lib.Solution_Set_MaxIterations(Value)

    @property
    def MinIterations(self):
        return lib.Solution_Get_MinIterations()

    @MinIterations.setter
    def MinIterations(self, Value):
        lib.Solution_Set_MinIterations(Value)

    @property
    def Mode(self):
        return lib.Solution_Get_Mode()

    @Mode.setter
    def Mode(self, Mode):
        lib.Solution_Set_Mode(Mode)

    @property
    def ModeID(self):
        return get_string(lib.Solution_Get_ModeID())

    @property
    def MostIterationsDone(self):
        return lib.Solution_Get_MostIterationsDone()

    @property
    def Number(self):
        return lib.Solution_Get_Number()

    @Number.setter
    def Number(self, Value):
        lib.Solution_Set_Number(Value)

    @property
    def Process_Time(self):
        return lib.Solution_Get_Process_Time()

    @property
    def Random(self):
        return lib.Solution_Get_Random()

    @Random.setter
    def Random(self, Random):
        lib.Solution_Set_Random(Random)

    @property
    def Seconds(self):
        return lib.Solution_Get_Seconds()

    @Seconds.setter
    def Seconds(self, Value):
        lib.Solution_Set_Seconds(Value)

    @property
    def StepSize(self):
        return lib.Solution_Get_StepSize()

    @StepSize.setter
    def StepSize(self, Value):
        lib.Solution_Set_StepSize(Value)

    @property
    def SystemYChanged(self):
        return lib.Solution_Get_SystemYChanged() != 0

    @property
    def Time_of_Step(self):
        return lib.Solution_Get_Time_of_Step()

    @property
    def Tolerance(self):
        return lib.Solution_Get_Tolerance()

    @Tolerance.setter
    def Tolerance(self, Value):
        lib.Solution_Set_Tolerance(Value)

    @property
    def Total_Time(self):
        return lib.Solution_Get_Total_Time()

    @Total_Time.setter
    def Total_Time(self, Value):
        lib.Solution_Set_Total_Time(Value)

    @property
    def Totaliterations(self):
        return lib.Solution_Get_Totaliterations()

    @property
    def Year(self):
        return lib.Solution_Get_Year()

    @Year.setter
    def Year(self, Value):
        lib.Solution_Set_Year(Value)

    @property
    def dblHour(self):
        return lib.Solution_Get_dblHour()

    @dblHour.setter
    def dblHour(self, Value):
        lib.Solution_Set_dblHour(Value)

    @property
    def pctGrowth(self):
        return lib.Solution_Get_pctGrowth()

    @pctGrowth.setter
    def pctGrowth(self, Value):
        lib.Solution_Set_pctGrowth(Value)

    @property
    def StepsizeHr(self):
        raise AttributeError("This property is write-only!")

    @StepsizeHr.setter
    def StepsizeHr(self, Value):
        lib.Solution_Set_StepsizeHr(Value)

    @property
    def StepsizeMin(self):
        raise AttributeError("This property is write-only!")

    @StepsizeMin.setter
    def StepsizeMin(self, Value):
        lib.Solution_Set_StepsizeMin(Value)


class ISwtControls(FrozenClass):
    _isfrozen = freeze

    def Reset(self):
        lib.SwtControls_Reset()

    @property
    def Action(self):
        return lib.SwtControls_Get_Action()

    @Action.setter
    def Action(self, Value):
        lib.SwtControls_Set_Action(Value)

    @property
    def AllNames(self):
        return get_string_array(lib.SwtControls_Get_AllNames)

    @property
    def Count(self):
        return lib.SwtControls_Get_Count()

    @property
    def Delay(self):
        return lib.SwtControls_Get_Delay()

    @Delay.setter
    def Delay(self, Value):
        lib.SwtControls_Set_Delay(Value)

    @property
    def First(self):
        return lib.SwtControls_Get_First()

    @property
    def IsLocked(self):
        return lib.SwtControls_Get_IsLocked() != 0

    @IsLocked.setter
    def IsLocked(self, Value):
        lib.SwtControls_Set_IsLocked(Value)

    @property
    def Name(self):
        return get_string(lib.SwtControls_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.SwtControls_Set_Name(Value)

    @property
    def Next(self):
        return lib.SwtControls_Get_Next()

    @property
    def NormalState(self):
        return lib.SwtControls_Get_NormalState()

    @NormalState.setter
    def NormalState(self, Value):
        lib.SwtControls_Set_NormalState(Value)

    @property
    def State(self):
        return lib.SwtControls_Get_State()

    @State.setter
    def State(self, Value):
        lib.SwtControls_Set_State(Value)

    @property
    def SwitchedObj(self):
        return get_string(lib.SwtControls_Get_SwitchedObj())

    @SwitchedObj.setter
    def SwitchedObj(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.SwtControls_Set_SwitchedObj(Value)

    @property
    def SwitchedTerm(self):
        return lib.SwtControls_Get_SwitchedTerm()

    @SwitchedTerm.setter
    def SwitchedTerm(self, Value):
        lib.SwtControls_Set_SwitchedTerm(Value)


class IText(FrozenClass):
    _isfrozen = freeze

    @property
    def Command(self):
        return get_string(lib.Text_Get_Command())

    @Command.setter
    def Command(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Text_Set_Command(Value)
        CheckForError()

    @property
    def Result(self):
        return get_string(lib.Text_Get_Result())


class ITopology(FrozenClass):
    _isfrozen = freeze

    @property
    def ActiveBranch(self):
        return lib.Topology_Get_ActiveBranch()

    @property
    def ActiveLevel(self):
        return lib.Topology_Get_ActiveLevel()

    @property
    def AllIsolatedBranches(self):
        return get_string_array(lib.Topology_Get_AllIsolatedBranches)

    @property
    def AllIsolatedLoads(self):
        return get_string_array(lib.Topology_Get_AllIsolatedLoads)

    @property
    def AllLoopedPairs(self):
        return get_string_array(lib.Topology_Get_AllLoopedPairs)

    @property
    def BackwardBranch(self):
        return lib.Topology_Get_BackwardBranch()

    @property
    def BranchName(self):
        return get_string(lib.Topology_Get_BranchName())

    @BranchName.setter
    def BranchName(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Topology_Set_BranchName(Value)

    @property
    def BusName(self):
        return get_string(lib.Topology_Get_BusName())

    @BusName.setter
    def BusName(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Topology_Set_BusName(Value)

    @property
    def First(self):
        return lib.Topology_Get_First()

    @property
    def FirstLoad(self):
        return lib.Topology_Get_FirstLoad()

    @property
    def ForwardBranch(self):
        return lib.Topology_Get_ForwardBranch()

    @property
    def LoopedBranch(self):
        return lib.Topology_Get_LoopedBranch()

    @property
    def Next(self):
        return lib.Topology_Get_Next()

    @property
    def NextLoad(self):
        return lib.Topology_Get_NextLoad()

    @property
    def NumIsolatedBranches(self):
        return lib.Topology_Get_NumIsolatedBranches()

    @property
    def NumIsolatedLoads(self):
        return lib.Topology_Get_NumIsolatedLoads()

    @property
    def NumLoops(self):
        return lib.Topology_Get_NumLoops()

    @property
    def ParallelBranch(self):
        return lib.Topology_Get_ParallelBranch()


class ITransformers(FrozenClass):
    _isfrozen = freeze

    @property
    def AllNames(self):
        return get_string_array(lib.Transformers_Get_AllNames)

    @property
    def Count(self):
        return lib.Transformers_Get_Count()

    @property
    def First(self):
        return lib.Transformers_Get_First()

    @property
    def IsDelta(self):
        return lib.Transformers_Get_IsDelta() != 0

    @IsDelta.setter
    def IsDelta(self, Value):
        lib.Transformers_Set_IsDelta(Value)

    @property
    def MaxTap(self):
        return lib.Transformers_Get_MaxTap()

    @MaxTap.setter
    def MaxTap(self, Value):
        lib.Transformers_Set_MaxTap(Value)

    @property
    def MinTap(self):
        return lib.Transformers_Get_MinTap()

    @MinTap.setter
    def MinTap(self, Value):
        lib.Transformers_Set_MinTap(Value)

    @property
    def Name(self):
        return get_string(lib.Transformers_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Transformers_Set_Name(Value)

    @property
    def Next(self):
        return lib.Transformers_Get_Next()

    @property
    def NumTaps(self):
        return lib.Transformers_Get_NumTaps()

    @NumTaps.setter
    def NumTaps(self, Value):
        lib.Transformers_Set_NumTaps(Value)

    @property
    def NumWindings(self):
        return lib.Transformers_Get_NumWindings()

    @NumWindings.setter
    def NumWindings(self, Value):
        lib.Transformers_Set_NumWindings(Value)

    @property
    def R(self):
        return lib.Transformers_Get_R()

    @R.setter
    def R(self, Value):
        lib.Transformers_Set_R(Value)

    @property
    def Rneut(self):
        return lib.Transformers_Get_Rneut()

    @Rneut.setter
    def Rneut(self, Value):
        lib.Transformers_Set_Rneut(Value)

    @property
    def Tap(self):
        return lib.Transformers_Get_Tap()

    @Tap.setter
    def Tap(self, Value):
        lib.Transformers_Set_Tap(Value)

    @property
    def Wdg(self):
        return lib.Transformers_Get_Wdg()

    @Wdg.setter
    def Wdg(self, Value):
        lib.Transformers_Set_Wdg(Value)

    @property
    def XfmrCode(self):
        return get_string(lib.Transformers_Get_XfmrCode())

    @XfmrCode.setter
    def XfmrCode(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Transformers_Set_XfmrCode(Value)

    @property
    def Xhl(self):
        return lib.Transformers_Get_Xhl()

    @Xhl.setter
    def Xhl(self, Value):
        lib.Transformers_Set_Xhl(Value)

    @property
    def Xht(self):
        return lib.Transformers_Get_Xht()

    @Xht.setter
    def Xht(self, Value):
        lib.Transformers_Set_Xht(Value)

    @property
    def Xlt(self):
        return lib.Transformers_Get_Xlt()

    @Xlt.setter
    def Xlt(self, Value):
        lib.Transformers_Set_Xlt(Value)

    @property
    def Xneut(self):
        return lib.Transformers_Get_Xneut()

    @Xneut.setter
    def Xneut(self, Value):
        lib.Transformers_Set_Xneut(Value)

    @property
    def kV(self):
        return lib.Transformers_Get_kV()

    @kV.setter
    def kV(self, Value):
        lib.Transformers_Set_kV(Value)

    @property
    def kVA(self):
        return lib.Transformers_Get_kVA()

    @kVA.setter
    def kVA(self, Value):
        lib.Transformers_Set_kVA(Value)


class IVsources(FrozenClass):
    _isfrozen = freeze

    @property
    def AllNames(self):
        return get_string_array(lib.Vsources_Get_AllNames)

    @property
    def AngleDeg(self):
        return lib.Vsources_Get_AngleDeg()

    @AngleDeg.setter
    def AngleDeg(self, Value):
        lib.Vsources_Set_AngleDeg(Value)

    @property
    def BasekV(self):
        return lib.Vsources_Get_BasekV()

    @BasekV.setter
    def BasekV(self, Value):
        lib.Vsources_Set_BasekV(Value)

    @property
    def Count(self):
        return lib.Vsources_Get_Count()

    @property
    def First(self):
        return lib.Vsources_Get_First()

    @property
    def Frequency(self):
        return lib.Vsources_Get_Frequency()

    @Frequency.setter
    def Frequency(self, Value):
        lib.Vsources_Set_Frequency(Value)

    @property
    def Name(self):
        return get_string(lib.Vsources_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Vsources_Set_Name(Value)

    @property
    def Next(self):
        return lib.Vsources_Get_Next()

    @property
    def Phases(self):
        return lib.Vsources_Get_Phases()

    @Phases.setter
    def Phases(self, Value):
        lib.Vsources_Set_Phases(Value)

    @property
    def pu(self):
        return lib.Vsources_Get_pu()

    @pu.setter
    def pu(self, Value):
        lib.Vsources_Set_pu(Value)


class IXYCurves(FrozenClass):
    _isfrozen = freeze

    @property
    def Count(self):
        return lib.XYCurves_Get_Count()

    @property
    def First(self):
        return lib.XYCurves_Get_First()

    @property
    def Name(self):
        return get_string(lib.XYCurves_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.XYCurves_Set_Name(Value)

    @property
    def Next(self):
        return lib.XYCurves_Get_Next()

    @property
    def Npts(self):
        return lib.XYCurves_Get_Npts()

    @Npts.setter
    def Npts(self, Value):
        lib.XYCurves_Set_Npts(Value)

    @property
    def Xarray(self):
        return get_float64_array(lib.XYCurves_Get_Xarray)

    @Xarray.setter
    def Xarray(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.XYCurves_Set_Xarray(ValuePtr, ValueCount)

    @property
    def Xscale(self):
        return lib.XYCurves_Get_Xscale()

    @Xscale.setter
    def Xscale(self, Value):
        lib.XYCurves_Set_Xscale(Value)

    @property
    def Xshift(self):
        return lib.XYCurves_Get_Xshift()

    @Xshift.setter
    def Xshift(self, Value):
        lib.XYCurves_Set_Xshift(Value)

    @property
    def Yarray(self):
        return get_float64_array(lib.XYCurves_Get_Yarray)

    @property
    def Yscale(self):
        return lib.XYCurves_Get_Yscale()

    @Yscale.setter
    def Yscale(self, Value):
        lib.XYCurves_Set_Yscale(Value)

    @property
    def Yshift(self):
        return lib.XYCurves_Get_Yshift()

    @Yshift.setter
    def Yshift(self, Value):
        lib.XYCurves_Set_Yshift(Value)

    @property
    def x(self):
        return lib.XYCurves_Get_x()

    @x.setter
    def x(self, Value):
        lib.XYCurves_Set_x(Value)

    @property
    def y(self):
        return lib.XYCurves_Get_y()

    @y.setter
    def y(self, Value):
        lib.XYCurves_Set_y(Value)


class ICktElement(FrozenClass):
    _isfrozen = freeze
    Properties = IDSSProperty()

    def Close(self, Term, Phs):
        lib.CktElement_Close(Term, Phs)

    def Controller(self, idx):
        return get_string(lib.CktElement_Get_Controller(idx))

    def Variable(self, MyVarName, Code):
        if type(MyVarName) is not bytes:
            MyVarName = MyVarName.encode(codec)

        return lib.CktElement_Get_Variable(MyVarName, Code)

    def Variablei(self, Idx, Code):
        return lib.CktElement_Get_Variablei(Idx, Code)

    def IsOpen(self, Term, Phs):
        return lib.CktElement_IsOpen(Term, Phs) != 0

    def Open(self, Term, Phs):
        lib.CktElement_Open(Term, Phs)

    @property
    def AllPropertyNames(self):
        return get_string_array(lib.CktElement_Get_AllPropertyNames)

    @property
    def AllVariableNames(self):
        return get_string_array(lib.CktElement_Get_AllVariableNames)

    @property
    def AllVariableValues(self):
        return get_float64_array(lib.CktElement_Get_AllVariableValues)

    @property
    def BusNames(self):
        return get_string_array(lib.CktElement_Get_BusNames)

    @BusNames.setter
    def BusNames(self, Value):
        Value, ValuePtr, ValueCount = prepare_string_array(Value)
        lib.CktElement_Set_BusNames(ValuePtr, ValueCount)

    @property
    def CplxSeqCurrents(self):
        return get_float64_array(lib.CktElement_Get_CplxSeqCurrents)

    @property
    def CplxSeqVoltages(self):
        return get_float64_array(lib.CktElement_Get_CplxSeqVoltages)

    @property
    def Currents(self):
        return get_float64_array(lib.CktElement_Get_Currents)

    @property
    def CurrentsMagAng(self):
        return get_float64_array(lib.CktElement_Get_CurrentsMagAng)

    @property
    def DisplayName(self):
        return get_string(lib.CktElement_Get_DisplayName())

    @DisplayName.setter
    def DisplayName(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.CktElement_Set_DisplayName(Value)

    @property
    def EmergAmps(self):
        return lib.CktElement_Get_EmergAmps()

    @EmergAmps.setter
    def EmergAmps(self, Value):
        lib.CktElement_Set_EmergAmps(Value)

    @property
    def Enabled(self):
        return lib.CktElement_Get_Enabled() != 0

    @Enabled.setter
    def Enabled(self, Value):
        lib.CktElement_Set_Enabled(Value)

    @property
    def EnergyMeter(self):
        return get_string(lib.CktElement_Get_EnergyMeter())

    @property
    def GUID(self):
        return get_string(lib.CktElement_Get_GUID())

    @property
    def Handle(self):
        return lib.CktElement_Get_Handle()

    @property
    def HasOCPDevice(self):
        return lib.CktElement_Get_HasOCPDevice() != 0

    @property
    def HasSwitchControl(self):
        return lib.CktElement_Get_HasSwitchControl() != 0

    @property
    def HasVoltControl(self):
        return lib.CktElement_Get_HasVoltControl() != 0

    @property
    def Losses(self):
        return get_float64_array(lib.CktElement_Get_Losses)

    @property
    def Name(self):
        return get_string(lib.CktElement_Get_Name())

    @property
    def NodeOrder(self):
        return get_int32_array(lib.CktElement_Get_NodeOrder)

    @property
    def NormalAmps(self):
        return lib.CktElement_Get_NormalAmps()

    @NormalAmps.setter
    def NormalAmps(self, Value):
        lib.CktElement_Set_NormalAmps(Value)

    @property
    def NumConductors(self):
        return lib.CktElement_Get_NumConductors()

    @property
    def NumControls(self):
        return lib.CktElement_Get_NumControls()

    @property
    def NumPhases(self):
        return lib.CktElement_Get_NumPhases()

    @property
    def NumProperties(self):
        return lib.CktElement_Get_NumProperties()

    @property
    def NumTerminals(self):
        return lib.CktElement_Get_NumTerminals()

    @property
    def OCPDevIndex(self):
        return lib.CktElement_Get_OCPDevIndex()

    @property
    def OCPDevType(self):
        return lib.CktElement_Get_OCPDevType()

    @property
    def PhaseLosses(self):
        return get_float64_array(lib.CktElement_Get_PhaseLosses)

    @property
    def Powers(self):
        return get_float64_array(lib.CktElement_Get_Powers)

    @property
    def Residuals(self):
        return get_float64_array(lib.CktElement_Get_Residuals)

    @property
    def SeqCurrents(self):
        return get_float64_array(lib.CktElement_Get_SeqCurrents)

    @property
    def SeqPowers(self):
        return get_float64_array(lib.CktElement_Get_SeqPowers)

    @property
    def SeqVoltages(self):
        return get_float64_array(lib.CktElement_Get_SeqVoltages)

    @property
    def Voltages(self):
        return get_float64_array(lib.CktElement_Get_Voltages)

    @property
    def VoltagesMagAng(self):
        return get_float64_array(lib.CktElement_Get_VoltagesMagAng)

    @property
    def Yprim(self):
        return get_float64_array(lib.CktElement_Get_Yprim)


class IDSSElement(FrozenClass):
    _isfrozen = freeze
    Properties = IDSSProperty()

    @property
    def AllPropertyNames(self):
        return get_string_array(lib.DSSElement_Get_AllPropertyNames)

    @property
    def Name(self):
        return get_string(lib.DSSElement_Get_Name())

    @property
    def NumProperties(self):
        return lib.DSSElement_Get_NumProperties()


class ICircuit(FrozenClass):
    _isfrozen = freeze
    Buses = IBus()
    CktElements = ICktElement()
    ActiveElement = ICktElement()
    Solution = ISolution()
    ActiveBus = IBus()
    Generators = IGenerators()
    Meters = IMeters()
    Monitors = IMonitors()
    Settings = ISettings()
    Lines = ILines()
    CtrlQueue = ICtrlQueue()
    Loads = ILoads()
    ActiveCktElement = ICktElement()
    ActiveDSSElement = IDSSElement()
    ActiveClass = IActiveClass()
    CapControls = ICapControls()
    RegControls = IRegControls()
    SwtControls = ISwtControls()
    Transformers = ITransformers()
    Capacitors = ICapacitors()
    Topology = ITopology()
    Sensors = ISensors()
    XYCurves = IXYCurves()
    PDElements = IPDElements()
    Reclosers = IReclosers()
    Relays = IRelays()
    LoadShapes = ILoadShapes()
    Fuses = IFuses()
    Isources = IISources()
    DSSim_Coms = IDSSimComs()
    PVSystems = IPVSystems()
    Vsources = IVsources()
    LineCodes = ILineCodes()

    def Capacity(self, Start, Increment):
        return lib.Circuit_Capacity(Start, Increment)

    def Disable(self, Name):
        if type(Name) is not bytes:
            Name = Name.encode(codec)

        lib.Circuit_Disable(Name)

    def Enable(self, Name):
        if type(Name) is not bytes:
            Name = Name.encode(codec)

        lib.Circuit_Enable(Name)

    def EndOfTimeStepUpdate(self):
        lib.Circuit_EndOfTimeStepUpdate()

    def FirstElement(self):
        return lib.Circuit_FirstElement()

    def FirstPCElement(self):
        return lib.Circuit_FirstPCElement()

    def FirstPDElement(self):
        return lib.Circuit_FirstPDElement()

    def AllNodeDistancesByPhase(self, Phase):
        return get_float64_array(lib.Circuit_Get_AllNodeDistancesByPhase, Phase)

    def AllNodeNamesByPhase(self, Phase):
        return get_string_array(lib.Circuit_Get_AllNodeNamesByPhase, Phase)

    def AllNodeVmagByPhase(self, Phase):
        return get_float64_array(lib.Circuit_Get_AllNodeVmagByPhase, Phase)

    def AllNodeVmagPUByPhase(self, Phase):
        return get_float64_array(lib.Circuit_Get_AllNodeVmagPUByPhase, Phase)

    def NextElement(self):
        return lib.Circuit_NextElement()

    def NextPCElement(self):
        return lib.Circuit_NextPCElement()

    def NextPDElement(self):
        return lib.Circuit_NextPDElement()

    def Sample(self):
        lib.Circuit_Sample()

    def SaveSample(self):
        lib.Circuit_SaveSample()

    def SetActiveBus(self, BusName):
        if type(BusName) is not bytes:
            BusName = BusName.encode(codec)

        return lib.Circuit_SetActiveBus(BusName)

    def SetActiveBusi(self, BusIndex):
        return lib.Circuit_SetActiveBusi(BusIndex)

    def SetActiveClass(self, ClassName):
        if type(ClassName) is not bytes:
            ClassName = ClassName.encode(codec)

        return lib.Circuit_SetActiveClass(ClassName)

    def SetActiveElement(self, FullName):
        if type(FullName) is not bytes:
            FullName = FullName.encode(codec)

        return lib.Circuit_SetActiveElement(FullName)

    def UpdateStorage(self):
        lib.Circuit_UpdateStorage()

    @property
    def AllBusDistances(self):
        return get_float64_array(lib.Circuit_Get_AllBusDistances)

    @property
    def AllBusNames(self):
        return get_string_array(lib.Circuit_Get_AllBusNames)

    @property
    def AllBusVmag(self):
        return get_float64_array(lib.Circuit_Get_AllBusVmag)

    @property
    def AllBusVmagPu(self):
        return get_float64_array(lib.Circuit_Get_AllBusVmagPu)

    @property
    def AllBusVolts(self):
        return get_float64_array(lib.Circuit_Get_AllBusVolts)

    @property
    def AllElementLosses(self):
        return get_float64_array(lib.Circuit_Get_AllElementLosses)

    @property
    def AllElementNames(self):
        return get_string_array(lib.Circuit_Get_AllElementNames)

    @property
    def AllNodeDistances(self):
        return get_float64_array(lib.Circuit_Get_AllNodeDistances)

    @property
    def AllNodeNames(self):
        return get_string_array(lib.Circuit_Get_AllNodeNames)

    @property
    def LineLosses(self):
        return get_float64_array(lib.Circuit_Get_LineLosses)

    @property
    def Losses(self):
        return get_float64_array(lib.Circuit_Get_Losses)

    @property
    def Name(self):
        return get_string(lib.Circuit_Get_Name())

    @property
    def NumBuses(self):
        return lib.Circuit_Get_NumBuses()

    @property
    def NumCktElements(self):
        return lib.Circuit_Get_NumCktElements()

    @property
    def NumNodes(self):
        return lib.Circuit_Get_NumNodes()

    @property
    def ParentPDElement(self):
        return lib.Circuit_Get_ParentPDElement()

    @property
    def SubstationLosses(self):
        return get_float64_array(lib.Circuit_Get_SubstationLosses)

    @property
    def SystemY(self):
        return get_float64_array(lib.Circuit_Get_SystemY)

    @property
    def TotalPower(self):
        return get_float64_array(lib.Circuit_Get_TotalPower)

    @property
    def YCurrents(self):
        return get_float64_array(lib.Circuit_Get_YCurrents)

    @property
    def YNodeOrder(self):
        return get_string_array(lib.Circuit_Get_YNodeOrder)

    @property
    def YNodeVarray(self):
        return get_float64_array(lib.Circuit_Get_YNodeVarray)


class IYMatrix(FrozenClass):
    _isfrozen = freeze
    
    def GetCompressedYMatrix(self, factor=False):
        nBus = ffi.new('uint32_t*')
        nBus[0] = 0
        nNz = ffi.new('uint32_t*')
        nNz[0] = 0
        
        ColPtr = ffi.new('int32_t**')
        RowIdxPtr = ffi.new('int32_t**')
        cValsPtr = ffi.new('double**')
        
        lib.YMatrix_GetCompressedYMatrix(factor, nBus, nNz, ColPtr, RowIdxPtr, cValsPtr)
        
        if not nBus[0] or not nNz[0]:
            res = None
        else:
            # return as (data, indices, indptr) that can fed into scipy.sparse.csc_matrix
            res = (
                np.frombuffer(ffi.buffer(cValsPtr[0], nNz[0] * 16), dtype=np.complex).copy(),
                np.frombuffer(ffi.buffer(RowIdxPtr[0], nNz[0] * 4), dtype=np.int32).copy(),
                np.frombuffer(ffi.buffer(ColPtr[0], (nBus[0] + 1) * 4), dtype=np.int32).copy()
            )
        
        lib.DSS_Dispose_PInteger(ColPtr)
        lib.DSS_Dispose_PInteger(RowIdxPtr)
        lib.DSS_Dispose_PDouble(cValsPtr)
        
        return res
        
    def ZeroInjCurr(self):
        lib.YMatrix_ZeroInjCurr()
        
    def GetSourceInjCurrents(self):
        lib.YMatrix_GetSourceInjCurrents()
        
    def GetPCInjCurr(self):
        lib.YMatrix_GetPCInjCurr()
        
    def BuildYMatrixD(self, BuildOps, AllocateVI):
        lib.YMatrix_BuildYMatrixD(BuildOps, AllocateVI)
        
    def AddInAuxCurrents(self, SType):
        lib.YMatrix_AddInAuxCurrents(SType)
    
    def GetIPointer(self):
        IvectorPtr = ffi.new('double**')
        lib.YMatrix_getIpointer(IvectorPtr)
        return IvectorPtr
        
    def GetVPointer(self):
        VvectorPtr = ffi.new('double**')
        lib.YMatrix_getVpointer(VvectorPtr)
        return VvectorPtr
        
    def SolveSystem(self, NodeV):
        if type(NodeV) is not np.ndarray:
            NodeV = np.array(NodeV)
            
        NodeV = ffi.cast("double *", NodeV.ctypes.data)
        NodeVPtr = ffi.new('double**')
        NodeVPtr[0] = NodeV
        result = lib.YMatrix_SolveSystem(NodeVPtr)
        return result
    
    @property
    def SystemYChanged(self):
        return lib.YMatrix_Get_SystemYChanged()

    @SystemYChanged.setter
    def SystemYChanged(self, value):
        lib.YMatrix_Set_SystemYChanged(value)
    
    @property
    def UseAuxCurrents(self):
        return lib.YMatrix_Get_UseAuxCurrents()

    @SystemYChanged.setter
    def UseAuxCurrents(self, value):
        lib.YMatrix_Set_UseAuxCurrents(value)

        
class IDSS(FrozenClass):
    _isfrozen = freeze
    ActiveCircuit = ICircuit()
    Circuits = ICircuit()
    Error = IError()
    Text = IText()
    NewCircuit = ICircuit()
    DSSProgress = IDSSProgress()
    ActiveClass = IActiveClass()
    Executive = IDSS_Executive()
    Events = IDSSEvents()
    CmathLib = ICmathLib()
    Parser = IParser()
    DSSim_Coms = IDSSimComs()
    YMatrix = IYMatrix()

    def ClearAll(self):
        lib.DSS_ClearAll()

    def Reset(self):
        lib.DSS_Reset()

    def SetActiveClass(self, ClassName):
        if type(ClassName) is not bytes:
            ClassName = ClassName.encode(codec)

        return lib.DSS_SetActiveClass(ClassName)

    def Start(self, code):
        return lib.DSS_Start(code) != 0

    @property
    def Classes(self):
        return get_string_array(lib.DSS_Get_Classes)

    @property
    def DataPath(self):
        return get_string(lib.DSS_Get_DataPath())

    @DataPath.setter
    def DataPath(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.DSS_Set_DataPath(Value)

    @property
    def DefaultEditor(self):
        return get_string(lib.DSS_Get_DefaultEditor())

    @property
    def NumCircuits(self):
        return lib.DSS_Get_NumCircuits()

    @property
    def NumClasses(self):
        return lib.DSS_Get_NumClasses()

    @property
    def NumUserClasses(self):
        return lib.DSS_Get_NumUserClasses()

    @property
    def UserClasses(self):
        return get_string_array(lib.DSS_Get_UserClasses)

    @property
    def Version(self):
        return get_string(lib.DSS_Get_Version())




DSS = IDSS()        

prepare_com_compat(vars())
       
