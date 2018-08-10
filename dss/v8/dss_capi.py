'''
A compatibility layer for DSS_CAPI_V8 that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._dss_capi_v8 import ffi, lib
from .._cffi_api_util import *
import numpy as np
import warnings

# Bind to the FFI module instance for OpenDSS-v8
api_util = CffiApiUtil(ffi, lib)
get_string = api_util.get_string
get_float64_array = api_util.get_float64_array
get_int32_array = api_util.get_int32_array
get_int8_array = api_util.get_int8_array
get_string_array = api_util.get_string_array
prepare_float64_array = api_util.prepare_float64_array
prepare_int32_array = api_util.prepare_int32_array
prepare_string_array = api_util.prepare_string_array

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
        '''(read-only) Returns name of active class.'''
        return get_string(lib.ActiveClass_Get_ActiveClassName())

    @property
    def AllNames(self):
        '''(read-only) Array of strings consisting of all element names in the active class.'''
        return get_string_array(lib.ActiveClass_Get_AllNames)

    @property
    def Count(self):
        '''(read-only) Number of elements in Active Class. Same as NumElements Property.'''
        return lib.ActiveClass_Get_Count()

    def __len__(self):
        return lib.ActiveClass_Get_Count()

    @property
    def First(self):
        '''(read-only) Sets first element in the active class to be the active DSS object. If object is a CktElement, ActiveCktELment also points to this element. Returns 0 if none.'''
        return lib.ActiveClass_Get_First()

    @property
    def Name(self):
        '''Name of the Active Element of the Active Class'''
        return get_string(lib.ActiveClass_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.ActiveClass_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Sets next element in active class to be the active DSS object. If object is a CktElement, ActiveCktElement also points to this element.  Returns 0 if no more.'''
        return lib.ActiveClass_Get_Next()

    @property
    def NumElements(self):
        '''(read-only) Number of elements in this class. Same as Count property.'''
        return lib.ActiveClass_Get_NumElements()


class IBus(FrozenClass):
    _isfrozen = freeze

    def GetUniqueNodeNumber(self, StartNumber):
        return lib.Bus_GetUniqueNodeNumber(StartNumber)

    def ZscRefresh(self):
        return lib.Bus_ZscRefresh() != 0

    @property
    def Coorddefined(self):
        '''(read-only) False=0 else True. Indicates whether a coordinate has been defined for this bus'''
        return lib.Bus_Get_Coorddefined() != 0

    @property
    def CplxSeqVoltages(self):
        '''(read-only) Complex Double array of Sequence Voltages (0, 1, 2) at this Bus.'''
        return get_float64_array(lib.Bus_Get_CplxSeqVoltages)

    @property
    def Cust_Duration(self):
        '''(read-only) Accumulated customer outage durations'''
        return lib.Bus_Get_Cust_Duration()

    @property
    def Cust_Interrupts(self):
        '''(read-only) Annual number of customer-interruptions from this bus'''
        return lib.Bus_Get_Cust_Interrupts()

    @property
    def Distance(self):
        '''(read-only) Distance from energymeter (if non-zero)'''
        return lib.Bus_Get_Distance()

    @property
    def Int_Duration(self):
        '''(read-only) Average interruption duration, hr.'''
        return lib.Bus_Get_Int_Duration()

    @property
    def Isc(self):
        '''(read-only) Short circuit currents at bus; Complex Array.'''
        return get_float64_array(lib.Bus_Get_Isc)

    @property
    def Lambda(self):
        '''(read-only) Accumulated failure rate downstream from this bus; faults per year'''
        return lib.Bus_Get_Lambda()

    @property
    def N_Customers(self):
        '''(read-only) Total numbers of customers served downline from this bus'''
        return lib.Bus_Get_N_Customers()

    @property
    def N_interrupts(self):
        '''(read-only) Number of interruptions this bus per year'''
        return lib.Bus_Get_N_interrupts()

    @property
    def Name(self):
        '''(read-only) Name of Bus'''
        return get_string(lib.Bus_Get_Name())

    @property
    def Nodes(self):
        '''(read-only) Integer Array of Node Numbers defined at the bus in same order as the voltages.'''
        return get_int32_array(lib.Bus_Get_Nodes)

    @property
    def NumNodes(self):
        '''(read-only) Number of Nodes this bus.'''
        return lib.Bus_Get_NumNodes()

    @property
    def SectionID(self):
        '''(read-only) Integer ID of the feeder section in which this bus is located.'''
        return lib.Bus_Get_SectionID()

    @property
    def SeqVoltages(self):
        '''(read-only) Double Array of sequence voltages at this bus.'''
        return get_float64_array(lib.Bus_Get_SeqVoltages)

    @property
    def TotalMiles(self):
        '''(read-only) Total length of line downline from this bus, in miles. For recloser siting algorithm.'''
        return lib.Bus_Get_TotalMiles()

    @property
    def VLL(self):
        '''(read-only) For 2- and 3-phase buses, returns array of complex numbers represetin L-L voltages in volts. Returns -1.0 for 1-phase bus. If more than 3 phases, returns only first 3.'''
        return get_float64_array(lib.Bus_Get_VLL)

    @property
    def VMagAngle(self):
        '''(read-only) Variant Array of doubles containing voltages in Magnitude (VLN), angle (deg) '''
        return get_float64_array(lib.Bus_Get_VMagAngle)

    @property
    def Voc(self):
        '''(read-only) Open circuit voltage; Complex array.'''
        return get_float64_array(lib.Bus_Get_Voc)

    @property
    def Voltages(self):
        '''(read-only) Complex array of voltages at this bus.'''
        return get_float64_array(lib.Bus_Get_Voltages)

    @property
    def YscMatrix(self):
        '''(read-only) Complex array of Ysc matrix at bus. Column by column.'''
        return get_float64_array(lib.Bus_Get_YscMatrix)

    @property
    def Zsc0(self):
        '''(read-only) Complex Zero-Sequence short circuit impedance at bus.'''
        return get_float64_array(lib.Bus_Get_Zsc0)

    @property
    def Zsc1(self):
        '''(read-only) Complex Positive-Sequence short circuit impedance at bus..'''
        return get_float64_array(lib.Bus_Get_Zsc1)

    @property
    def ZscMatrix(self):
        '''(read-only) Complex array of Zsc matrix at bus. Column by column.'''
        return get_float64_array(lib.Bus_Get_ZscMatrix)

    @property
    def kVBase(self):
        '''(read-only) Base voltage at bus in kV'''
        return lib.Bus_Get_kVBase()

    @property
    def puVLL(self):
        '''(read-only) Returns Complex array of pu L-L voltages for 2- and 3-phase buses. Returns -1.0 for 1-phase bus. If more than 3 phases, returns only 3 phases.'''
        return get_float64_array(lib.Bus_Get_puVLL)

    @property
    def puVmagAngle(self):
        '''(read-only) Array of doubles containig voltage magnitude, angle pairs in per unit'''
        return get_float64_array(lib.Bus_Get_puVmagAngle)

    @property
    def puVoltages(self):
        '''(read-only) Complex Array of pu voltages at the bus.'''
        return get_float64_array(lib.Bus_Get_puVoltages)

    @property
    def x(self):
        '''X Coordinate for bus (double)'''
        return lib.Bus_Get_x()

    @x.setter
    def x(self, Value):
        lib.Bus_Set_x(Value)

    @property
    def y(self):
        '''Y coordinate for bus(double)'''
        return lib.Bus_Get_y()

    @y.setter
    def y(self, Value):
        lib.Bus_Set_y(Value)

    def __getitem__(self, index):
        if isinstance(index, int):
            # bus index is zero based, pass it directly
            lib.Circuit_SetActiveBusi(index)
        else:
            if type(index) is not bytes:
                index = index.encode(codec)
                
            lib.Circuit_SetActiveBus(index)
    
        return self
        
    def __call__(self, index):
        return self.__getitem__(index)
        



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
        '''(read-only) Array of strings with all Capacitor names in the circuit.'''
        return get_string_array(lib.Capacitors_Get_AllNames)

    @property
    def AvailableSteps(self):
        '''(read-only) Number of Steps available in cap bank to be switched ON.'''
        return lib.Capacitors_Get_AvailableSteps()

    @property
    def Count(self):
        '''(read-only) Number of Capacitor objects in active circuit.'''
        return lib.Capacitors_Get_Count()

    def __len__(self):
        return lib.Capacitors_Get_Count()

    @property
    def First(self):
        '''(read-only) Sets the first Capacitor active. Returns 0 if no more.'''
        return lib.Capacitors_Get_First()

    @property
    def IsDelta(self):
        '''Delta connection or wye?'''
        return lib.Capacitors_Get_IsDelta() != 0

    @IsDelta.setter
    def IsDelta(self, Value):
        lib.Capacitors_Set_IsDelta(Value)

    @property
    def Name(self):
        '''Sets the active Capacitor by Name.'''
        return get_string(lib.Capacitors_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Capacitors_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Sets the next Capacitor active. Returns 0 if no more.'''
        return lib.Capacitors_Get_Next()

    @property
    def NumSteps(self):
        '''Number of steps (default 1) for distributing and switching the total bank kVAR.'''
        return lib.Capacitors_Get_NumSteps()

    @NumSteps.setter
    def NumSteps(self, Value):
        lib.Capacitors_Set_NumSteps(Value)

    @property
    def States(self):
        '''
        (read) A array of  integer [0..numsteps-1] indicating state of each step. If value is -1 an error has occurred.
        (write) Array of integer [0 ..numSteps-1] indicating the state of each step
        '''
        return get_int32_array(lib.Capacitors_Get_States)

    @States.setter
    def States(self, Value):
        Value, ValuePtr, ValueCount = prepare_int32_array(Value)
        lib.Capacitors_Set_States(ValuePtr, ValueCount)

    @property
    def kV(self):
        '''Bank kV rating. Use LL for 2 or 3 phases, or actual can rating for 1 phase.'''
        return lib.Capacitors_Get_kV()

    @kV.setter
    def kV(self, Value):
        lib.Capacitors_Set_kV(Value)

    @property
    def kvar(self):
        '''Total bank KVAR, distributed equally among phases and steps.'''
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
        '''(read-only) Array of strings with all CapControl names.'''
        return get_string_array(lib.CapControls_Get_AllNames)

    @property
    def CTratio(self):
        '''Transducer ratio from pirmary current to control current.'''
        return lib.CapControls_Get_CTratio()

    @CTratio.setter
    def CTratio(self, Value):
        lib.CapControls_Set_CTratio(Value)

    @property
    def Capacitor(self):
        '''Name of the Capacitor that is controlled.'''
        return get_string(lib.CapControls_Get_Capacitor())

    @Capacitor.setter
    def Capacitor(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.CapControls_Set_Capacitor(Value)

    @property
    def Count(self):
        '''(read-only) Number of CapControls in Active Circuit'''
        return lib.CapControls_Get_Count()

    def __len__(self):
        return lib.CapControls_Get_Count()

    @property
    def DeadTime(self):
        return lib.CapControls_Get_DeadTime()

    @DeadTime.setter
    def DeadTime(self, Value):
        lib.CapControls_Set_DeadTime(Value)

    @property
    def Delay(self):
        '''Time delay [s] to switch on after arming.  Control may reset before actually switching.'''
        return lib.CapControls_Get_Delay()

    @Delay.setter
    def Delay(self, Value):
        lib.CapControls_Set_Delay(Value)

    @property
    def DelayOff(self):
        '''Time delay [s] before swithcing off a step. Control may reset before actually switching.'''
        return lib.CapControls_Get_DelayOff()

    @DelayOff.setter
    def DelayOff(self, Value):
        lib.CapControls_Set_DelayOff(Value)

    @property
    def First(self):
        '''(read-only) Sets the first CapControl as active. Return 0 if none.'''
        return lib.CapControls_Get_First()

    @property
    def Mode(self):
        '''Type of automatic controller.'''
        return lib.CapControls_Get_Mode()

    @Mode.setter
    def Mode(self, Value):
        lib.CapControls_Set_Mode(Value)

    @property
    def MonitoredObj(self):
        '''Full name of the element that PT and CT are connected to.'''
        return get_string(lib.CapControls_Get_MonitoredObj())

    @MonitoredObj.setter
    def MonitoredObj(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.CapControls_Set_MonitoredObj(Value)

    @property
    def MonitoredTerm(self):
        '''Terminal number on the element that PT and CT are connected to.'''
        return lib.CapControls_Get_MonitoredTerm()

    @MonitoredTerm.setter
    def MonitoredTerm(self, Value):
        lib.CapControls_Set_MonitoredTerm(Value)

    @property
    def Name(self):
        '''Sets a CapControl active by name.'''
        return get_string(lib.CapControls_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.CapControls_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Gets the next CapControl in the circut. Returns 0 if none.'''
        return lib.CapControls_Get_Next()

    @property
    def OFFSetting(self):
        '''Threshold to switch off a step. See Mode for units.'''
        return lib.CapControls_Get_OFFSetting()

    @OFFSetting.setter
    def OFFSetting(self, Value):
        lib.CapControls_Set_OFFSetting(Value)

    @property
    def ONSetting(self):
        '''Threshold to arm or switch on a step.  See Mode for units.'''
        return lib.CapControls_Get_ONSetting()

    @ONSetting.setter
    def ONSetting(self, Value):
        lib.CapControls_Set_ONSetting(Value)

    @property
    def PTratio(self):
        '''Transducer ratio from primary feeder to control voltage.'''
        return lib.CapControls_Get_PTratio()

    @PTratio.setter
    def PTratio(self, Value):
        lib.CapControls_Set_PTratio(Value)

    @property
    def UseVoltOverride(self):
        '''Enables Vmin and Vmax to override the control Mode'''
        return lib.CapControls_Get_UseVoltOverride() != 0

    @UseVoltOverride.setter
    def UseVoltOverride(self, Value):
        lib.CapControls_Set_UseVoltOverride(Value)

    @property
    def Vmax(self):
        '''With VoltOverride, swtich off whenever PT voltage exceeds this level.'''
        return lib.CapControls_Get_Vmax()

    @Vmax.setter
    def Vmax(self, Value):
        lib.CapControls_Set_Vmax(Value)

    @property
    def Vmin(self):
        '''With VoltOverride, switch ON whenever PT voltage drops below this level.'''
        return lib.CapControls_Get_Vmin()

    @Vmin.setter
    def Vmin(self, Value):
        lib.CapControls_Set_Vmin(Value)


class ICmathLib(FrozenClass):
    _isfrozen = freeze

    def cabs(self, realpart, imagpart):
        '''(read-only) Return abs value of complex number given in real and imag doubles'''
        return lib.CmathLib_Get_cabs(realpart, imagpart)

    def cdang(self, RealPart, ImagPart):
        '''(read-only) Returns the angle, in degrees, of a complex number specified as two doubles: Realpart and imagpart.'''
        return lib.CmathLib_Get_cdang(RealPart, ImagPart)

    def cdiv(self, a1, b1, a2, b2):
        '''(read-only) Divide two complex number: (a1, b1)/(a2, b2). Returns array of two doubles representing complex result.'''
        return get_float64_array(lib.CmathLib_Get_cdiv, a1, b1, a2, b2)

    def cmplx(self, RealPart, ImagPart):
        '''(read-only) Convert real and imaginary doubles to Array of doubles'''
        return get_float64_array(lib.CmathLib_Get_cmplx, RealPart, ImagPart)

    def cmul(self, a1, b1, a2, b2):
        '''(read-only) Multiply two complex numbers: (a1, b1) * (a2, b2). Returns result as a array of two doubles.'''
        return get_float64_array(lib.CmathLib_Get_cmul, a1, b1, a2, b2)

    def ctopolardeg(self, RealPart, ImagPart):
        '''(read-only) Convert complex number to magnitude and angle, degrees. Returns array of two doubles.'''
        return get_float64_array(lib.CmathLib_Get_ctopolardeg, RealPart, ImagPart)

    def pdegtocomplex(self, magnitude, angle):
        '''(read-only) Convert magnitude, angle in degrees to a complex number. Returns Array of two doubles.'''
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
        '''(read-only) Code for the active action. Long integer code to tell the control device what to do'''
        return lib.CtrlQueue_Get_ActionCode()

    @property
    def DeviceHandle(self):
        '''(read-only) Handle (User defined) to device that must act on the pending action.'''
        return lib.CtrlQueue_Get_DeviceHandle()

    @property
    def NumActions(self):
        '''(read-only) Number of Actions on the current actionlist (that have been popped off the control queue by CheckControlActions)'''
        return lib.CtrlQueue_Get_NumActions()

    @property
    def PopAction(self):
        '''(read-only) Pops next action off the action list and makes it the active action. Returns zero if none.'''
        return lib.CtrlQueue_Get_PopAction()

    @property
    def Queue(self):
        '''(read-only) Array of strings containing the entire queue in CSV format'''
        return get_string_array(lib.CtrlQueue_Get_Queue)

    @property
    def QueueSize(self):
        '''(read-only) Number of items on the OpenDSS control Queue'''
        return lib.CtrlQueue_Get_QueueSize()

    @property
    def Action(self):
        '''(write-only) Set the active action by index'''
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
        '''(write-only) Caption to appear on the bottom of the DSS Progress form.'''
        raise AttributeError("This property is write-only!")

    @Caption.setter
    def Caption(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.DSSProgress_Set_Caption(Value)

    @property
    def PctProgress(self):
        '''(write-only) Percent progress to indicate [0..100]'''
        raise AttributeError("This property is write-only!")

    @PctProgress.setter
    def PctProgress(self, Value):
        lib.DSSProgress_Set_PctProgress(Value)


class IDSSProperty(FrozenClass):
    _isfrozen = freeze

    @property
    def Description(self):
        '''(read-only) Description of the property.'''
        return get_string(lib.DSSProperty_Get_Description())

    @property
    def Name(self):
        '''(read-only) Name of Property'''
        return get_string(lib.DSSProperty_Get_Name())

    @property
    def Val(self):
        return get_string(lib.DSSProperty_Get_Val())

    @Val.setter
    def Val(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.DSSProperty_Set_Val(Value)

    def __getitem__(self, propname_index):
        if isinstance(propname_index, int):
            lib.DSSProperty_Set_Index(propname_index)
        else:
            if type(propname_index) is not bytes:
                propname_index = propname_index.encode(codec)
                
            lib.DSSProperty_Set_Name(propname_index)
    
        return self
    
    def __call__(self, propname_index):
        return self.__getitem__(propname_index)



class IDSS_Executive(FrozenClass):
    _isfrozen = freeze

    def Command(self, i):
        '''(read-only) Get i-th command'''
        return get_string(lib.DSS_Executive_Get_Command(i))

    def CommandHelp(self, i):
        '''(read-only) Get help string for i-th command'''
        return get_string(lib.DSS_Executive_Get_CommandHelp(i))

    def Option(self, i):
        '''(read-only) Get i-th option'''
        return get_string(lib.DSS_Executive_Get_Option(i))

    def OptionHelp(self, i):
        '''(read-only) Get help string for i-th option'''
        return get_string(lib.DSS_Executive_Get_OptionHelp(i))

    def OptionValue(self, i):
        '''(read-only) Get present value of i-th option'''
        return get_string(lib.DSS_Executive_Get_OptionValue(i))

    @property
    def NumCommands(self):
        '''(read-only) Number of DSS Executive Commands'''
        return lib.DSS_Executive_Get_NumCommands()

    @property
    def NumOptions(self):
        '''(read-only) Number of DSS Executive Options'''
        return lib.DSS_Executive_Get_NumOptions()


class IError(FrozenClass):
    _isfrozen = freeze

    @property
    def Description(self):
        '''(read-only) Description of error for last operation'''
        return get_string(lib.Error_Get_Description())

    @property
    def Number(self):
        '''(read-only) Error Number'''
        return lib.Error_Get_Number()




class IFuses(FrozenClass):
    _isfrozen = freeze

    def Close(self):
        lib.Fuses_Close()

    def IsBlown(self):
        return lib.Fuses_IsBlown() != 0

    def Open(self):
        lib.Fuses_Open()

    @property
    def AllNames(self):
        '''(read-only) Array of strings containing names of all Fuses in the circuit'''
        return get_string_array(lib.Fuses_Get_AllNames)

    @property
    def Count(self):
        '''(read-only) Number of Fuse elements in the circuit'''
        return lib.Fuses_Get_Count()

    def __len__(self):
        return lib.Fuses_Get_Count()

    @property
    def Delay(self):
        '''
        (read) A fixed delay time in seconds added to the fuse blowing time determined by the TCC curve. Default is 0.
        (write) Fixed delay time in seconds added to the fuse blowing time to represent fuse clear or other delay.
        '''
        return lib.Fuses_Get_Delay()

    @Delay.setter
    def Delay(self, Value):
        lib.Fuses_Set_Delay(Value)

    @property
    def First(self):
        '''(read-only) Set the first Fuse to be the active fuse. Returns 0 if none.'''
        return lib.Fuses_Get_First()

    @property
    def MonitoredObj(self):
        '''Full name of the circuit element to which the fuse is connected.'''
        return get_string(lib.Fuses_Get_MonitoredObj())

    @MonitoredObj.setter
    def MonitoredObj(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Fuses_Set_MonitoredObj(Value)

    @property
    def MonitoredTerm(self):
        '''
        (read) Terminal number to which the fuse is connected.
        (write) Number of the terminal to which the fuse is connected
        '''
        return lib.Fuses_Get_MonitoredTerm()

    @MonitoredTerm.setter
    def MonitoredTerm(self, Value):
        lib.Fuses_Set_MonitoredTerm(Value)

    @property
    def Name(self):
        '''
        (read) Get the name of the active Fuse element
        (write) Set the active Fuse element by name.
        '''
        return get_string(lib.Fuses_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Fuses_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Advance the active Fuse element pointer to the next fuse. Returns 0 if no more fuses.'''
        return lib.Fuses_Get_Next()

    @property
    def NumPhases(self):
        '''(read-only) Number of phases, this fuse. '''
        return lib.Fuses_Get_NumPhases()

    @property
    def RatedCurrent(self):
        '''
        (read) Multiplier or actual amps for the TCCcurve object. Defaults to 1.0.  Multipliy current values of TCC curve by this to get actual amps.
        (write) Multiplier or actual fuse amps for the TCC curve. Defaults to 1.0. Has to correspond to the Current axis of TCCcurve object.
        '''
        return lib.Fuses_Get_RatedCurrent()

    @RatedCurrent.setter
    def RatedCurrent(self, Value):
        lib.Fuses_Set_RatedCurrent(Value)

    @property
    def SwitchedObj(self):
        '''
        (read) Full name of the circuit element switch that the fuse controls. Defaults to the MonitoredObj.
        (write) Full name of the circuit element switch that the fuse controls. Defaults to MonitoredObj.
        '''
        return get_string(lib.Fuses_Get_SwitchedObj())

    @SwitchedObj.setter
    def SwitchedObj(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Fuses_Set_SwitchedObj(Value)

    @property
    def SwitchedTerm(self):
        '''
        (read) Number of the terminal containing the switch controlled by the fuse.
        (write) Number of the terminal of the controlled element containing the switch controlled by the fuse.
        '''
        return lib.Fuses_Get_SwitchedTerm()

    @SwitchedTerm.setter
    def SwitchedTerm(self, Value):
        lib.Fuses_Set_SwitchedTerm(Value)

    @property
    def TCCcurve(self):
        '''Name of the TCCcurve object that determines fuse blowing.'''
        return get_string(lib.Fuses_Get_TCCcurve())

    @TCCcurve.setter
    def TCCcurve(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Fuses_Set_TCCcurve(Value)

    @property
    def idx(self):
        '''
        (read) Get/set active fuse by index into the list of fuses. 1 based: 1..count
        (write) Set Fuse active by index into the list of fuses. 1..count
        '''
        return lib.Fuses_Get_idx()

    @idx.setter
    def idx(self, Value):
        lib.Fuses_Set_idx(Value)


class IGenerators(FrozenClass):
    _isfrozen = freeze

    @property
    def AllNames(self):
        '''(read-only) Array of names of all Generator objects.'''
        return get_string_array(lib.Generators_Get_AllNames)

    @property
    def Count(self):
        '''(read-only) Number of Generator Objects in Active Circuit'''
        return lib.Generators_Get_Count()

    def __len__(self):
        return lib.Generators_Get_Count()

    @property
    def First(self):
        '''(read-only) Sets first Generator to be active.  Returns 0 if none.'''
        return lib.Generators_Get_First()

    @property
    def ForcedON(self):
        '''Indicates whether the generator is forced ON regardles of other dispatch criteria.'''
        return lib.Generators_Get_ForcedON() != 0

    @ForcedON.setter
    def ForcedON(self, Value):
        lib.Generators_Set_ForcedON(Value)

    @property
    def Model(self):
        '''Generator Model'''
        return lib.Generators_Get_Model()

    @Model.setter
    def Model(self, Value):
        lib.Generators_Set_Model(Value)

    @property
    def Name(self):
        '''Sets a generator active by name.'''
        return get_string(lib.Generators_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Generators_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Sets next Generator to be active.  Returns 0 if no more.'''
        return lib.Generators_Get_Next()

    @property
    def PF(self):
        '''Power factor (pos. = producing vars). Updates kvar based on present kW value.'''
        return lib.Generators_Get_PF()

    @PF.setter
    def PF(self, Value):
        lib.Generators_Set_PF(Value)

    @property
    def Phases(self):
        '''Number of phases'''
        return lib.Generators_Get_Phases()

    @Phases.setter
    def Phases(self, Value):
        lib.Generators_Set_Phases(Value)

    @property
    def RegisterNames(self):
        '''(read-only) Array of Names of all generator energy meter registers'''
        return get_string_array(lib.Generators_Get_RegisterNames)

    @property
    def RegisterValues(self):
        '''(read-only) Array of valus in generator energy meter registers.'''
        return get_float64_array(lib.Generators_Get_RegisterValues)

    @property
    def Vmaxpu(self):
        '''Vmaxpu for generator model'''
        return lib.Generators_Get_Vmaxpu()

    @Vmaxpu.setter
    def Vmaxpu(self, Value):
        lib.Generators_Set_Vmaxpu(Value)

    @property
    def Vminpu(self):
        '''Vminpu for Generator model'''
        return lib.Generators_Get_Vminpu()

    @Vminpu.setter
    def Vminpu(self, Value):
        lib.Generators_Set_Vminpu(Value)

    @property
    def idx(self):
        '''Get/Set active Generator by index into generators list.  1..Count'''
        return lib.Generators_Get_idx()

    @idx.setter
    def idx(self, Value):
        lib.Generators_Set_idx(Value)

    @property
    def kV(self):
        '''Voltage base for the active generator, kV'''
        return lib.Generators_Get_kV()

    @kV.setter
    def kV(self, Value):
        lib.Generators_Set_kV(Value)

    @property
    def kVArated(self):
        '''kVA rating of the generator'''
        return lib.Generators_Get_kVArated()

    @kVArated.setter
    def kVArated(self, Value):
        lib.Generators_Set_kVArated(Value)

    @property
    def kW(self):
        '''kW output for the active generator. kvar is updated for current power factor.'''
        return lib.Generators_Get_kW()

    @kW.setter
    def kW(self, Value):
        lib.Generators_Set_kW(Value)

    @property
    def kvar(self):
        '''kvar output for the active generator. Updates power factor based on present kW value.'''
        return lib.Generators_Get_kvar()

    @kvar.setter
    def kvar(self, Value):
        lib.Generators_Set_kvar(Value)


class IISources(FrozenClass):
    _isfrozen = freeze

    @property
    def AllNames(self):
        '''(read-only) Array of strings containing names of all ISOURCE elements.'''
        return get_string_array(lib.ISources_Get_AllNames)

    @property
    def Amps(self):
        '''Magnitude of the ISOURCE in amps'''
        return lib.ISources_Get_Amps()

    @Amps.setter
    def Amps(self, Value):
        lib.ISources_Set_Amps(Value)

    @property
    def AngleDeg(self):
        '''Phase angle for ISOURCE, degrees'''
        return lib.ISources_Get_AngleDeg()

    @AngleDeg.setter
    def AngleDeg(self, Value):
        lib.ISources_Set_AngleDeg(Value)

    @property
    def Count(self):
        '''(read-only) Count: Number of ISOURCE elements.'''
        return lib.ISources_Get_Count()

    def __len__(self):
        return lib.ISources_Get_Count()

    @property
    def First(self):
        '''(read-only) Set the First ISOURCE to be active; returns Zero if none.'''
        return lib.ISources_Get_First()

    @property
    def Frequency(self):
        '''The present frequency of the ISOURCE, Hz'''
        return lib.ISources_Get_Frequency()

    @Frequency.setter
    def Frequency(self, Value):
        lib.ISources_Set_Frequency(Value)

    @property
    def Name(self):
        '''
        (read) Get name of active ISOURCE
        (write) Set Active ISOURCE by name
        '''
        return get_string(lib.ISources_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.ISources_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Sets the next ISOURCE element to be the active one. Returns Zero if no more.'''
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

    def __len__(self):
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
        '''(read-only) Names of all Line Objects'''
        return get_string_array(lib.Lines_Get_AllNames)

    @property
    def Bus1(self):
        '''Name of bus for terminal 1.'''
        return get_string(lib.Lines_Get_Bus1())

    @Bus1.setter
    def Bus1(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Lines_Set_Bus1(Value)

    @property
    def Bus2(self):
        '''Name of bus for terminal 2.'''
        return get_string(lib.Lines_Get_Bus2())

    @Bus2.setter
    def Bus2(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Lines_Set_Bus2(Value)

    @property
    def C0(self):
        '''Zero Sequence capacitance, nanofarads per unit length.'''
        return lib.Lines_Get_C0()

    @C0.setter
    def C0(self, Value):
        lib.Lines_Set_C0(Value)

    @property
    def C1(self):
        '''Positive Sequence capacitance, nanofarads per unit length.'''
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
        '''(read-only) Number of Line objects in Active Circuit.'''
        return lib.Lines_Get_Count()

    def __len__(self):
        return lib.Lines_Get_Count()

    @property
    def EmergAmps(self):
        '''Emergency (maximum) ampere rating of Line.'''
        return lib.Lines_Get_EmergAmps()

    @EmergAmps.setter
    def EmergAmps(self, Value):
        lib.Lines_Set_EmergAmps(Value)

    @property
    def First(self):
        '''(read-only) Invoking this property sets the first element active.  Returns 0 if no lines.  Otherwise, index of the line element.'''
        return lib.Lines_Get_First()

    @property
    def Geometry(self):
        '''Line geometry code'''
        return get_string(lib.Lines_Get_Geometry())

    @Geometry.setter
    def Geometry(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Lines_Set_Geometry(Value)

    @property
    def Length(self):
        '''Length of line section in units compatible with the LineCode definition.'''
        return lib.Lines_Get_Length()

    @Length.setter
    def Length(self, Value):
        lib.Lines_Set_Length(Value)

    @property
    def LineCode(self):
        '''Name of LineCode object that defines the impedances.'''
        return get_string(lib.Lines_Get_LineCode())

    @LineCode.setter
    def LineCode(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Lines_Set_LineCode(Value)

    @property
    def Name(self):
        '''Specify the name of the Line element to set it active.'''
        return get_string(lib.Lines_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Lines_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Invoking this property advances to the next Line element active.  Returns 0 if no more lines.  Otherwise, index of the line element.'''
        return lib.Lines_Get_Next()

    @property
    def NormAmps(self):
        '''Normal ampere rating of Line.'''
        return lib.Lines_Get_NormAmps()

    @NormAmps.setter
    def NormAmps(self, Value):
        lib.Lines_Set_NormAmps(Value)

    @property
    def NumCust(self):
        '''(read-only) Number of customers on this line section.'''
        return lib.Lines_Get_NumCust()

    @property
    def Parent(self):
        '''(read-only) Sets Parent of the active Line to be the active line. Returns 0 if no parent or action fails.'''
        return lib.Lines_Get_Parent()

    @property
    def Phases(self):
        '''Number of Phases, this Line element.'''
        return lib.Lines_Get_Phases()

    @Phases.setter
    def Phases(self, Value):
        lib.Lines_Set_Phases(Value)

    @property
    def R0(self):
        '''Zero Sequence resistance, ohms per unit length.'''
        return lib.Lines_Get_R0()

    @R0.setter
    def R0(self, Value):
        lib.Lines_Set_R0(Value)

    @property
    def R1(self):
        '''Positive Sequence resistance, ohms per unit length.'''
        return lib.Lines_Get_R1()

    @R1.setter
    def R1(self, Value):
        lib.Lines_Set_R1(Value)

    @property
    def Rg(self):
        '''Earth return resistance value used to compute line impedances at power frequency'''
        return lib.Lines_Get_Rg()

    @Rg.setter
    def Rg(self, Value):
        lib.Lines_Set_Rg(Value)

    @property
    def Rho(self):
        '''Earth Resistivity, m-ohms'''
        return lib.Lines_Get_Rho()

    @Rho.setter
    def Rho(self, Value):
        lib.Lines_Set_Rho(Value)

    @property
    def Rmatrix(self):
        '''Resistance matrix (full), ohms per unit length. Array of doubles.'''
        return get_float64_array(lib.Lines_Get_Rmatrix)

    @Rmatrix.setter
    def Rmatrix(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.Lines_Set_Rmatrix(ValuePtr, ValueCount)

    @property
    def Spacing(self):
        '''Line spacing code'''
        return get_string(lib.Lines_Get_Spacing())

    @Spacing.setter
    def Spacing(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Lines_Set_Spacing(Value)

    @property
    def TotalCust(self):
        '''(read-only) Total Number of customers served from this line section.'''
        return lib.Lines_Get_TotalCust()

    @property
    def Units(self):
        return lib.Lines_Get_Units()

    @Units.setter
    def Units(self, Value):
        lib.Lines_Set_Units(Value)

    @property
    def X0(self):
        '''Zero Sequence reactance ohms per unit length.'''
        return lib.Lines_Get_X0()

    @X0.setter
    def X0(self, Value):
        lib.Lines_Set_X0(Value)

    @property
    def X1(self):
        '''Positive Sequence reactance, ohms per unit length.'''
        return lib.Lines_Get_X1()

    @X1.setter
    def X1(self, Value):
        lib.Lines_Set_X1(Value)

    @property
    def Xg(self):
        '''Earth return reactance value used to compute line impedances at power frequency'''
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
        '''Yprimitive: Does Nothing at present on Put; Dangerous'''
        return get_float64_array(lib.Lines_Get_Yprim)

    @Yprim.setter
    def Yprim(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.Lines_Set_Yprim(ValuePtr, ValueCount)


class ILoads(FrozenClass):
    _isfrozen = freeze

    @property
    def AllNames(self):
        '''(read-only) Array of strings containing all Load names'''
        return get_string_array(lib.Loads_Get_AllNames)

    @property
    def AllocationFactor(self):
        '''Factor for allocating loads by connected xfkva'''
        return lib.Loads_Get_AllocationFactor()

    @AllocationFactor.setter
    def AllocationFactor(self, Value):
        lib.Loads_Set_AllocationFactor(Value)

    @property
    def CVRcurve(self):
        '''Name of a loadshape with both Mult and Qmult, for CVR factors as a function of time.'''
        return get_string(lib.Loads_Get_CVRcurve())

    @CVRcurve.setter
    def CVRcurve(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Loads_Set_CVRcurve(Value)

    @property
    def CVRvars(self):
        '''Percent reduction in Q for percent reduction in V. Must be used with dssLoadModelCVR.'''
        return lib.Loads_Get_CVRvars()

    @CVRvars.setter
    def CVRvars(self, Value):
        lib.Loads_Set_CVRvars(Value)

    @property
    def CVRwatts(self):
        '''Percent reduction in P for percent reduction in V. Must be used with dssLoadModelCVR.'''
        return lib.Loads_Get_CVRwatts()

    @CVRwatts.setter
    def CVRwatts(self, Value):
        lib.Loads_Set_CVRwatts(Value)

    @property
    def Cfactor(self):
        '''Factor relates average to peak kw.  Used for allocation with kwh and kwhdays/'''
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
        '''(read-only) Number of Load objects in active circuit.'''
        return lib.Loads_Get_Count()

    def __len__(self):
        return lib.Loads_Get_Count()

    @property
    def First(self):
        '''(read-only) Set first Load element to be active; returns 0 if none.'''
        return lib.Loads_Get_First()

    @property
    def Growth(self):
        '''Name of the growthshape curve for yearly load growth factors.'''
        return get_string(lib.Loads_Get_Growth())

    @Growth.setter
    def Growth(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Loads_Set_Growth(Value)

    @property
    def IsDelta(self):
        '''Delta loads are connected line-to-line.'''
        return lib.Loads_Get_IsDelta() != 0

    @IsDelta.setter
    def IsDelta(self, Value):
        lib.Loads_Set_IsDelta(Value)

    @property
    def Model(self):
        '''The Load Model defines variation of P and Q with voltage.'''
        return lib.Loads_Get_Model()

    @Model.setter
    def Model(self, Value):
        lib.Loads_Set_Model(Value)

    @property
    def Name(self):
        '''Set active load by name.'''
        return get_string(lib.Loads_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Loads_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Sets next Load element to be active; returns 0 of none else index of active load.'''
        return lib.Loads_Get_Next()

    @property
    def NumCust(self):
        '''Number of customers in this load, defaults to one.'''
        return lib.Loads_Get_NumCust()

    @NumCust.setter
    def NumCust(self, Value):
        lib.Loads_Set_NumCust(Value)

    @property
    def PF(self):
        '''
        (read) Set Power Factor for Active Load. Specify leading PF as negative. Updates kvar based on kW value
        (write) Set Power Factor for Active Load. Specify leading PF as negative. Updates kvar based on present value of kW.
        '''
        return lib.Loads_Get_PF()

    @PF.setter
    def PF(self, Value):
        lib.Loads_Set_PF(Value)

    @property
    def PctMean(self):
        '''Average percent of nominal load in Monte Carlo studies; only if no loadshape defined for this load.'''
        return lib.Loads_Get_PctMean()

    @PctMean.setter
    def PctMean(self, Value):
        lib.Loads_Set_PctMean(Value)

    @property
    def PctStdDev(self):
        '''Percent standard deviation for Monte Carlo load studies; if there is no loadshape assigned to this load.'''
        return lib.Loads_Get_PctStdDev()

    @PctStdDev.setter
    def PctStdDev(self, Value):
        lib.Loads_Set_PctStdDev(Value)

    @property
    def RelWeight(self):
        '''Relative Weighting factor for the active LOAD'''
        return lib.Loads_Get_RelWeight()

    @RelWeight.setter
    def RelWeight(self, Value):
        lib.Loads_Set_RelWeight(Value)

    @property
    def Rneut(self):
        '''Neutral resistance for wye-connected loads.'''
        return lib.Loads_Get_Rneut()

    @Rneut.setter
    def Rneut(self, Value):
        lib.Loads_Set_Rneut(Value)

    @property
    def Spectrum(self):
        '''Name of harmonic current spectrrum shape.'''
        return get_string(lib.Loads_Get_Spectrum())

    @Spectrum.setter
    def Spectrum(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Loads_Set_Spectrum(Value)

    @property
    def Status(self):
        '''Response to load multipliers: Fixed (growth only), Exempt (no LD curve), Variable (all).'''
        return lib.Loads_Get_Status()

    @Status.setter
    def Status(self, Value):
        lib.Loads_Set_Status(Value)

    @property
    def Vmaxpu(self):
        '''Maximum per-unit voltage to use the load model. Above this, constant Z applies.'''
        return lib.Loads_Get_Vmaxpu()

    @Vmaxpu.setter
    def Vmaxpu(self, Value):
        lib.Loads_Set_Vmaxpu(Value)

    @property
    def Vminemerg(self):
        '''Minimum voltage for unserved energy (UE) evaluation.'''
        return lib.Loads_Get_Vminemerg()

    @Vminemerg.setter
    def Vminemerg(self, Value):
        lib.Loads_Set_Vminemerg(Value)

    @property
    def Vminnorm(self):
        '''Minimum voltage for energy exceeding normal (EEN) evaluations.'''
        return lib.Loads_Get_Vminnorm()

    @Vminnorm.setter
    def Vminnorm(self, Value):
        lib.Loads_Set_Vminnorm(Value)

    @property
    def Vminpu(self):
        '''Minimum voltage to apply the load model. Below this, constant Z is used.'''
        return lib.Loads_Get_Vminpu()

    @Vminpu.setter
    def Vminpu(self, Value):
        lib.Loads_Set_Vminpu(Value)

    @property
    def Xneut(self):
        '''Neutral reactance for wye-connected loads.'''
        return lib.Loads_Get_Xneut()

    @Xneut.setter
    def Xneut(self, Value):
        lib.Loads_Set_Xneut(Value)

    @property
    def Yearly(self):
        '''Name of yearly duration loadshape'''
        return get_string(lib.Loads_Get_Yearly())

    @Yearly.setter
    def Yearly(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Loads_Set_Yearly(Value)

    @property
    def ZIPV(self):
        '''Array of 7  doubles with values for ZIPV property of the LOAD object'''
        return get_float64_array(lib.Loads_Get_ZIPV)

    @ZIPV.setter
    def ZIPV(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.Loads_Set_ZIPV(ValuePtr, ValueCount)

    @property
    def daily(self):
        '''Name of the loadshape for a daily load profile.'''
        return get_string(lib.Loads_Get_daily())

    @daily.setter
    def daily(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Loads_Set_daily(Value)

    @property
    def duty(self):
        '''Name of the loadshape for a duty cycle simulation.'''
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
        '''Set kV rating for active Load. For 2 or more phases set Line-Line kV. Else actual kV across terminals.'''
        return lib.Loads_Get_kV()

    @kV.setter
    def kV(self, Value):
        lib.Loads_Set_kV(Value)

    @property
    def kW(self):
        '''Set kW for active Load. Updates kvar based on present PF.'''
        return lib.Loads_Get_kW()

    @kW.setter
    def kW(self, Value):
        lib.Loads_Set_kW(Value)

    @property
    def kva(self):
        '''Base load kva. Also defined kw and kvar or pf input, or load allocation by kwh or xfkva.'''
        return lib.Loads_Get_kva()

    @kva.setter
    def kva(self, Value):
        lib.Loads_Set_kva(Value)

    @property
    def kvar(self):
        '''Set kvar for active Load. Updates PF based on present kW.'''
        return lib.Loads_Get_kvar()

    @kvar.setter
    def kvar(self, Value):
        lib.Loads_Set_kvar(Value)

    @property
    def kwh(self):
        '''kwh billed for this period. Can be used with Cfactor for load allocation.'''
        return lib.Loads_Get_kwh()

    @kwh.setter
    def kwh(self, Value):
        lib.Loads_Set_kwh(Value)

    @property
    def kwhdays(self):
        '''Length of kwh billing period for average demand calculation. Default 30.'''
        return lib.Loads_Get_kwhdays()

    @kwhdays.setter
    def kwhdays(self, Value):
        lib.Loads_Set_kwhdays(Value)

    @property
    def pctSeriesRL(self):
        '''Percent of Load that is modeled as series R-L for harmonics studies'''
        return lib.Loads_Get_pctSeriesRL()

    @pctSeriesRL.setter
    def pctSeriesRL(self, Value):
        lib.Loads_Set_pctSeriesRL(Value)

    @property
    def xfkVA(self):
        '''Rated service transformer kVA for load allocation, using AllocationFactor. Affects kW, kvar, and pf.'''
        return lib.Loads_Get_xfkVA()

    @xfkVA.setter
    def xfkVA(self, Value):
        lib.Loads_Set_xfkVA(Value)


class ILoadShapes(FrozenClass):
    _isfrozen = freeze

    def New(self, Name):
        if type(Name) is not bytes:
            Name = Name.encode(codec)

        return lib.LoadShapes_New(Name)

    def Normalize(self):
        lib.LoadShapes_Normalize()

    @property
    def AllNames(self):
        '''(read-only) Array of strings containing names of all Loadshape objects currently defined.'''
        return get_string_array(lib.LoadShapes_Get_AllNames)

    @property
    def Count(self):
        '''(read-only) Number of Loadshape objects currently defined in Loadshape collection'''
        return lib.LoadShapes_Get_Count()

    def __len__(self):
        return lib.LoadShapes_Get_Count()

    @property
    def First(self):
        '''(read-only) Set the first loadshape active and return integer index of the loadshape. Returns 0 if none.'''
        return lib.LoadShapes_Get_First()

    @property
    def HrInterval(self):
        '''Fixed interval time value, hours.'''
        return lib.LoadShapes_Get_HrInterval()

    @HrInterval.setter
    def HrInterval(self, Value):
        lib.LoadShapes_Set_HrInterval(Value)

    @property
    def MinInterval(self):
        '''Fixed Interval time value, in minutes'''
        return lib.LoadShapes_Get_MinInterval()

    @MinInterval.setter
    def MinInterval(self, Value):
        lib.LoadShapes_Set_MinInterval(Value)

    @property
    def Name(self):
        '''
        (read) Get the Name of the active Loadshape
        (write) Set the active Loadshape by name
        '''
        return get_string(lib.LoadShapes_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.LoadShapes_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Advance active Loadshape to the next on in the collection. Returns 0 if no more loadshapes.'''
        return lib.LoadShapes_Get_Next()

    @property
    def Npts(self):
        '''
        (read) Get Number of points in active Loadshape.
        (write) Set number of points to allocate for active Loadshape.
        '''
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
        '''
        (read) Array of Doubles for the P multiplier in the Loadshape.
        (write) Array of doubles containing the P array for the Loadshape.
        '''
        return get_float64_array(lib.LoadShapes_Get_Pmult)

    @Pmult.setter
    def Pmult(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.LoadShapes_Set_Pmult(ValuePtr, ValueCount)

    @property
    def Qbase(self):
        '''Base for normalizing Q curve. If left at zero, the peak value is used.'''
        return lib.LoadShapes_Get_Qbase()

    @Qbase.setter
    def Qbase(self, Value):
        lib.LoadShapes_Set_Qbase(Value)

    @property
    def Qmult(self):
        '''Array of doubles containing the Q multipliers.'''
        return get_float64_array(lib.LoadShapes_Get_Qmult)

    @Qmult.setter
    def Qmult(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.LoadShapes_Set_Qmult(ValuePtr, ValueCount)

    @property
    def TimeArray(self):
        '''Time array in hours correscponding to P and Q multipliers when the Interval=0.'''
        return get_float64_array(lib.LoadShapes_Get_TimeArray)

    @TimeArray.setter
    def TimeArray(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.LoadShapes_Set_TimeArray(ValuePtr, ValueCount)

    @property
    def UseActual(self):
        '''T/F flag to let Loads know to use the actual value in the curve rather than use the value as a multiplier.'''
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
        '''(read-only) Wide string list of all branches in zone of the active energymeter object.'''
        return get_string_array(lib.Meters_Get_AllBranchesInZone)

    @property
    def AllEndElements(self):
        '''(read-only) Array of names of all zone end elements.'''
        return get_string_array(lib.Meters_Get_AllEndElements)

    @property
    def AllNames(self):
        '''(read-only) Array of all energy Meter names'''
        return get_string_array(lib.Meters_Get_AllNames)

    @property
    def AllocFactors(self):
        '''Array of doubles: set the phase allocation factors for the active meter.'''
        return get_float64_array(lib.Meters_Get_AllocFactors)

    @AllocFactors.setter
    def AllocFactors(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.Meters_Set_AllocFactors(ValuePtr, ValueCount)

    @property
    def AvgRepairTime(self):
        '''(read-only) Average Repair time in this section of the meter zone'''
        return lib.Meters_Get_AvgRepairTime()

    @property
    def CalcCurrent(self):
        '''Set the magnitude of the real part of the Calculated Current (normally determined by solution) for the Meter to force some behavior on Load Allocation'''
        return get_float64_array(lib.Meters_Get_CalcCurrent)

    @CalcCurrent.setter
    def CalcCurrent(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.Meters_Set_CalcCurrent(ValuePtr, ValueCount)

    @property
    def Count(self):
        '''(read-only) Number of Energy Meters in the Active Circuit'''
        return lib.Meters_Get_Count()

    def __len__(self):
        return lib.Meters_Get_Count()

    @property
    def CountBranches(self):
        '''(read-only) Number of branches in Active energymeter zone. (Same as sequencelist size)'''
        return lib.Meters_Get_CountBranches()

    @property
    def CountEndElements(self):
        '''(read-only) Number of zone end elements in the active meter zone.'''
        return lib.Meters_Get_CountEndElements()

    @property
    def CustInterrupts(self):
        '''(read-only) Total customer interruptions for this Meter zone based on reliability calcs.'''
        return lib.Meters_Get_CustInterrupts()

    @property
    def DIFilesAreOpen(self):
        '''(read-only) Global Flag in the DSS to indicate if Demand Interval (DI) files have been properly opened.'''
        return lib.Meters_Get_DIFilesAreOpen() != 0

    @property
    def FaultRateXRepairHrs(self):
        '''(read-only) Sum of Fault Rate time Repair Hrs in this section of the meter zone'''
        return lib.Meters_Get_FaultRateXRepairHrs()

    @property
    def First(self):
        '''(read-only) Set the first energy Meter active. Returns 0 if none.'''
        return lib.Meters_Get_First()

    @property
    def MeteredElement(self):
        '''Set Name of metered element'''
        return get_string(lib.Meters_Get_MeteredElement())

    @MeteredElement.setter
    def MeteredElement(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Meters_Set_MeteredElement(Value)

    @property
    def MeteredTerminal(self):
        '''set Number of Metered Terminal'''
        return lib.Meters_Get_MeteredTerminal()

    @MeteredTerminal.setter
    def MeteredTerminal(self, Value):
        lib.Meters_Set_MeteredTerminal(Value)

    @property
    def Name(self):
        '''
        (read) Get/Set the active meter  name.
        (write) Set a meter to be active by name.
        '''
        return get_string(lib.Meters_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Meters_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Sets the next energy Meter active.  Returns 0 if no more.'''
        return lib.Meters_Get_Next()

    @property
    def NumSectionBranches(self):
        '''(read-only) Number of branches (lines) in this section'''
        return lib.Meters_Get_NumSectionBranches()

    @property
    def NumSectionCustomers(self):
        '''(read-only) Number of Customers in the active section.'''
        return lib.Meters_Get_NumSectionCustomers()

    @property
    def NumSections(self):
        '''(read-only) Number of feeder sections in this meter's zone'''
        return lib.Meters_Get_NumSections()

    @property
    def OCPDeviceType(self):
        '''(read-only) Type of OCP device. 1=Fuse; 2=Recloser; 3=Relay'''
        return lib.Meters_Get_OCPDeviceType()

    @property
    def Peakcurrent(self):
        '''Array of doubles to set values of Peak Current property'''
        return get_float64_array(lib.Meters_Get_Peakcurrent)

    @Peakcurrent.setter
    def Peakcurrent(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.Meters_Set_Peakcurrent(ValuePtr, ValueCount)

    @property
    def RegisterNames(self):
        '''(read-only) Array of strings containing the names of the registers.'''
        return get_string_array(lib.Meters_Get_RegisterNames)

    @property
    def RegisterValues(self):
        '''(read-only) Array of all the values contained in the Meter registers for the active Meter.'''
        return get_float64_array(lib.Meters_Get_RegisterValues)

    @property
    def SAIDI(self):
        '''(read-only) SAIDI for this meter's zone. Execute DoReliabilityCalc first.'''
        return lib.Meters_Get_SAIDI()

    @property
    def SAIFI(self):
        '''(read-only) Returns SAIFI for this meter's Zone. Execute Reliability Calc method first.'''
        return lib.Meters_Get_SAIFI()

    @property
    def SAIFIKW(self):
        '''(read-only) SAIFI based on kW rather than number of customers. Get after reliability calcs.'''
        return lib.Meters_Get_SAIFIKW()

    @property
    def SectSeqIdx(self):
        '''(read-only) SequenceIndex of the branch at the head of this section'''
        return lib.Meters_Get_SectSeqIdx()

    @property
    def SectTotalCust(self):
        '''(read-only) Total Customers downline from this section'''
        return lib.Meters_Get_SectTotalCust()

    @property
    def SeqListSize(self):
        '''(read-only) Size of Sequence List'''
        return lib.Meters_Get_SeqListSize()

    @property
    def SequenceIndex(self):
        '''Get/set Index into Meter's SequenceList that contains branch pointers in lexical order. Earlier index guaranteed to be upline from later index. Sets PDelement active.'''
        return lib.Meters_Get_SequenceIndex()

    @SequenceIndex.setter
    def SequenceIndex(self, Value):
        lib.Meters_Set_SequenceIndex(Value)

    @property
    def SumBranchFltRates(self):
        '''(read-only) Sum of the branch fault rates in this section of the meter's zone'''
        return lib.Meters_Get_SumBranchFltRates()

    @property
    def TotalCustomers(self):
        '''(read-only) Total Number of customers in this zone (downline from the EnergyMeter)'''
        return lib.Meters_Get_TotalCustomers()

    @property
    def Totals(self):
        '''(read-only) Totals of all registers of all meters'''
        return get_float64_array(lib.Meters_Get_Totals)


class IMonitors(FrozenClass):
    _isfrozen = freeze

    def Channel(self, Index):
        '''(read-only) Array of doubles for the specified channel  (usage: MyArray = DSSMonitor.Channel(i)) A Save or SaveAll  should be executed first. Done automatically by most standard solution modes.'''
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
        '''(read-only) Array of all Monitor Names'''
        return get_string_array(lib.Monitors_Get_AllNames)

    @property
    def ByteStream(self):
        '''(read-only) Byte Array containing monitor stream values. Make sure a "save" is done first (standard solution modes do this automatically)'''
        return get_int8_array(lib.Monitors_Get_ByteStream)

    @property
    def Count(self):
        '''(read-only) Number of Monitors'''
        return lib.Monitors_Get_Count()

    def __len__(self):
        return lib.Monitors_Get_Count()

    @property
    def Element(self):
        '''Full object name of element being monitored.'''
        return get_string(lib.Monitors_Get_Element())

    @Element.setter
    def Element(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Monitors_Set_Element(Value)

    @property
    def FileName(self):
        '''(read-only) Name of CSV file associated with active Monitor.'''
        return get_string(lib.Monitors_Get_FileName())

    @property
    def FileVersion(self):
        '''(read-only) Monitor File Version (integer)'''
        return lib.Monitors_Get_FileVersion()

    @property
    def First(self):
        '''(read-only) Sets the first Monitor active.  Returns 0 if no monitors.'''
        return lib.Monitors_Get_First()

    @property
    def Header(self):
        '''(read-only) Header string;  Array of strings containing Channel names'''
        return get_string_array(lib.Monitors_Get_Header)

    @property
    def Mode(self):
        '''Set Monitor mode (bitmask integer - see DSS Help)'''
        return lib.Monitors_Get_Mode()

    @Mode.setter
    def Mode(self, Value):
        lib.Monitors_Set_Mode(Value)

    @property
    def Name(self):
        '''Sets the active Monitor object by name'''
        return get_string(lib.Monitors_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Monitors_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Sets next monitor active.  Returns 0 if no more.'''
        return lib.Monitors_Get_Next()

    @property
    def NumChannels(self):
        '''(read-only) Number of Channels in the active Monitor'''
        return lib.Monitors_Get_NumChannels()

    @property
    def RecordSize(self):
        '''(read-only) Size of each record in ByteStream (Integer). Same as NumChannels.'''
        return lib.Monitors_Get_RecordSize()

    @property
    def SampleCount(self):
        '''(read-only) Number of Samples in Monitor at Present'''
        return lib.Monitors_Get_SampleCount()

    @property
    def Terminal(self):
        '''Terminal number of element being monitored.'''
        return lib.Monitors_Get_Terminal()

    @Terminal.setter
    def Terminal(self, Value):
        lib.Monitors_Set_Terminal(Value)

    @property
    def dblFreq(self):
        '''(read-only) Array of doubles containing frequency values for harmonics mode solutions; Empty for time mode solutions (use dblHour)'''
        return get_float64_array(lib.Monitors_Get_dblFreq)

    @property
    def dblHour(self):
        '''(read-only) Array of doubles containgin time value in hours for time-sampled monitor values; Empty if frequency-sampled values for harmonics solution  (see dblFreq)'''
        return get_float64_array(lib.Monitors_Get_dblHour)


class IParallel(FrozenClass):
    _isfrozen = freeze

    def CreateActor(self):
        lib.Parallel_CreateActor()

    def Wait(self):
        lib.Parallel_Wait()

    @property
    def ActiveActor(self):
        '''
        (read) Gets the ID of the Active Actor
        (write) Sets the Active Actor
        '''
        return lib.Parallel_Get_ActiveActor()

    @ActiveActor.setter
    def ActiveActor(self, Value):
        lib.Parallel_Set_ActiveActor(Value)

    @property
    def ActiveParallel(self):
        '''
        (read) Sets ON/OFF (1/0) Parallel features of the Engine
        (write) Delivers if the Parallel features of the Engine are Active
        '''
        return lib.Parallel_Get_ActiveParallel()

    @ActiveParallel.setter
    def ActiveParallel(self, Value):
        lib.Parallel_Set_ActiveParallel(Value)

    @property
    def ActorCPU(self):
        '''
        (read) Gets the CPU of the Active Actor
        (write) Sets the CPU for the Active Actor
        '''
        return lib.Parallel_Get_ActorCPU()

    @ActorCPU.setter
    def ActorCPU(self, Value):
        lib.Parallel_Set_ActorCPU(Value)

    @property
    def ActorProgress(self):
        '''(read-only) Gets the progress of all existing actors in pct'''
        return get_int32_array(lib.Parallel_Get_ActorProgress)

    @property
    def ActorStatus(self):
        '''(read-only) Gets the status of each actor'''
        return get_int32_array(lib.Parallel_Get_ActorStatus)

    @property
    def ConcatenateReports(self):
        '''
        (read) Reads the values of the ConcatenateReports option (1=enabled, 0=disabled)
        (write) Enable/Disable (1/0) the ConcatenateReports option for extracting monitors data
        '''
        return lib.Parallel_Get_ConcatenateReports()

    @ConcatenateReports.setter
    def ConcatenateReports(self, Value):
        lib.Parallel_Set_ConcatenateReports(Value)

    @property
    def NumCPUs(self):
        '''(read-only) Delivers the number of CPUs on the current PC'''
        return lib.Parallel_Get_NumCPUs()

    @property
    def NumCores(self):
        '''(read-only) Delivers the number of Cores of the local PC'''
        return lib.Parallel_Get_NumCores()

    @property
    def NumOfActors(self):
        '''(read-only) Gets the number of Actors created'''
        return lib.Parallel_Get_NumOfActors()


class IParser(FrozenClass):
    _isfrozen = freeze

    def Matrix(self, ExpectedOrder):
        '''(read-only) Use this property to parse a Matrix token in OpenDSS format.  Returns square matrix of order specified. Order same as default Fortran order: column by column.'''
        return get_float64_array(lib.Parser_Get_Matrix, ExpectedOrder)

    def SymMatrix(self, ExpectedOrder):
        '''(read-only) Use this property to parse a matrix token specified in lower triangle form. Symmetry is forced.'''
        return get_float64_array(lib.Parser_Get_SymMatrix, ExpectedOrder)

    def Vector(self, ExpectedSize):
        '''(read-only) Returns token as array of doubles. For parsing quoted array syntax.'''
        return get_float64_array(lib.Parser_Get_Vector, ExpectedSize)

    def ResetDelimiters(self):
        lib.Parser_ResetDelimiters()

    @property
    def AutoIncrement(self):
        '''Default is FALSE. If TRUE parser automatically advances to next token after DblValue, IntValue, or StrValue. Simpler when you don't need to check for parameter names.'''
        return lib.Parser_Get_AutoIncrement() != 0

    @AutoIncrement.setter
    def AutoIncrement(self, Value):
        lib.Parser_Set_AutoIncrement(Value)

    @property
    def BeginQuote(self):
        '''
        (read) Get String containing the the characters for Quoting in OpenDSS scripts. Matching pairs defined in EndQuote. Default is "'([{.
        (write) Set String containing the the characters for Quoting in OpenDSS scripts. Matching pairs defined in EndQuote. Default is "'([{.
        '''
        return get_string(lib.Parser_Get_BeginQuote())

    @BeginQuote.setter
    def BeginQuote(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Parser_Set_BeginQuote(Value)

    @property
    def CmdString(self):
        '''String to be parsed. Loading this string resets the Parser to the beginning of the line. Then parse off the tokens in sequence.'''
        return get_string(lib.Parser_Get_CmdString())

    @CmdString.setter
    def CmdString(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Parser_Set_CmdString(Value)

    @property
    def DblValue(self):
        '''(read-only) Return next parameter as a double.'''
        return lib.Parser_Get_DblValue()

    @property
    def Delimiters(self):
        '''String defining hard delimiters used to separate token on the command string. Default is , and =. The = separates token name from token value. These override whitesspace to separate tokens.'''
        return get_string(lib.Parser_Get_Delimiters())

    @Delimiters.setter
    def Delimiters(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Parser_Set_Delimiters(Value)

    @property
    def EndQuote(self):
        '''String containing characters, in order, that match the beginning quote characters in BeginQuote. Default is "')]}'''
        return get_string(lib.Parser_Get_EndQuote())

    @EndQuote.setter
    def EndQuote(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Parser_Set_EndQuote(Value)

    @property
    def IntValue(self):
        '''(read-only) Return next parameter as a long integer.'''
        return lib.Parser_Get_IntValue()

    @property
    def NextParam(self):
        '''(read-only) Get next token and return tag name (before = sign) if any. See AutoIncrement.'''
        return get_string(lib.Parser_Get_NextParam())

    @property
    def StrValue(self):
        '''(read-only) Return next parameter as a string'''
        return get_string(lib.Parser_Get_StrValue())

    @property
    def WhiteSpace(self):
        '''
        (read) Get the characters used for White space in the command string.  Default is blank and Tab.
        (write) Set the characters used for White space in the command string.  Default is blank and Tab.
        '''
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
        '''(read-only) accummulated failure rate for this branch on downline'''
        return lib.PDElements_Get_AccumulatedL()

    @property
    def Count(self):
        '''(read-only) Number of PD elements (including disabled elements)'''
        return lib.PDElements_Get_Count()

    def __len__(self):
        return lib.PDElements_Get_Count()

    @property
    def FaultRate(self):
        '''Get/Set Number of failures per year. For LINE elements: Number of failures per unit length per year. '''
        return lib.PDElements_Get_FaultRate()

    @FaultRate.setter
    def FaultRate(self, Value):
        lib.PDElements_Set_FaultRate(Value)

    @property
    def First(self):
        '''(read-only) Set the first enabled PD element to be the active element.  Returns 0 if none found.'''
        return lib.PDElements_Get_First()

    @property
    def FromTerminal(self):
        '''(read-only) Number of the terminal of active PD element that is on the "from" side. This is set after the meter zone is determined.'''
        return lib.PDElements_Get_FromTerminal()

    @property
    def IsShunt(self):
        '''(read-only) Variant boolean indicating of PD element should be treated as a shunt element rather than a series element. Applies to Capacitor and Reactor elements in particular.'''
        return lib.PDElements_Get_IsShunt() != 0

    @property
    def Lambda(self):
        '''(read-only) Failure rate for this branch. Faults per year including length of line.'''
        return lib.PDElements_Get_Lambda()

    @property
    def Name(self):
        '''Get/Set name of active PD Element. Returns null string if active element is not PDElement type.'''
        return get_string(lib.PDElements_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.PDElements_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Advance to the next PD element in the circuit. Enabled elements only. Returns 0 when no more elements.'''
        return lib.PDElements_Get_Next()

    @property
    def Numcustomers(self):
        '''(read-only) Number of customers, this branch'''
        return lib.PDElements_Get_Numcustomers()

    @property
    def ParentPDElement(self):
        '''(read-only) Sets the parent PD element to be the active circuit element.  Returns 0 if no more elements upline.'''
        return lib.PDElements_Get_ParentPDElement()

    @property
    def RepairTime(self):
        '''Average repair time for this element in hours'''
        return lib.PDElements_Get_RepairTime()

    @RepairTime.setter
    def RepairTime(self, Value):
        lib.PDElements_Set_RepairTime(Value)

    @property
    def SectionID(self):
        '''(read-only) Integer ID of the feeder section that this PDElement branch is part of'''
        return lib.PDElements_Get_SectionID()

    @property
    def TotalMiles(self):
        '''(read-only) Total miles of line from this element to the end of the zone. For recloser siting algorithm.'''
        return lib.PDElements_Get_TotalMiles()

    @property
    def Totalcustomers(self):
        '''(read-only) Total number of customers from this branch to the end of the zone'''
        return lib.PDElements_Get_Totalcustomers()

    @property
    def pctPermanent(self):
        '''Get/Set percent of faults that are permanent (require repair). Otherwise, fault is assumed to be transient/temporary.'''
        return lib.PDElements_Get_pctPermanent()

    @pctPermanent.setter
    def pctPermanent(self, Value):
        lib.PDElements_Set_pctPermanent(Value)


class IPVSystems(FrozenClass):
    _isfrozen = freeze

    @property
    def AllNames(self):
        '''(read-only) Vairant array of strings with all PVSystem names'''
        return get_string_array(lib.PVSystems_Get_AllNames)

    @property
    def Count(self):
        '''(read-only) Number of PVSystems'''
        return lib.PVSystems_Get_Count()

    def __len__(self):
        return lib.PVSystems_Get_Count()

    @property
    def First(self):
        '''(read-only) Set first PVSystem active; returns 0 if none.'''
        return lib.PVSystems_Get_First()

    @property
    def Irradiance(self):
        '''
        (read) Get the present value of the Irradiance property in W/sq-m
        (write) Set the present Irradiance value in W/sq-m
        '''
        return lib.PVSystems_Get_Irradiance()

    @Irradiance.setter
    def Irradiance(self, Value):
        lib.PVSystems_Set_Irradiance(Value)

    @property
    def Name(self):
        '''
        (read) Get the name of the active PVSystem
        (write) Set the name of the active PVSystem
        '''
        return get_string(lib.PVSystems_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.PVSystems_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Sets next PVSystem active; returns 0 if no more.'''
        return lib.PVSystems_Get_Next()

    @property
    def PF(self):
        '''
        (read) Get Power factor 
        (write) Set PF 
        '''
        return lib.PVSystems_Get_PF()

    @PF.setter
    def PF(self, Value):
        lib.PVSystems_Set_PF(Value)

    @property
    def RegisterNames(self):
        '''(read-only) Variant Array of PVSYSTEM energy meter register names'''
        return get_string_array(lib.PVSystems_Get_RegisterNames)

    @property
    def RegisterValues(self):
        '''(read-only) Array of doubles containing values in PVSystem registers.'''
        return get_float64_array(lib.PVSystems_Get_RegisterValues)

    @property
    def idx(self):
        '''
        (read) Get/set active PVSystem by index;  1..Count
        (write) Get/Set Active PVSystem by index:  1.. Count
        '''
        return lib.PVSystems_Get_idx()

    @idx.setter
    def idx(self, Value):
        lib.PVSystems_Set_idx(Value)

    @property
    def kVArated(self):
        '''
        (read) Get Rated kVA of the PVSystem
        (write) Set kva rated
        '''
        return lib.PVSystems_Get_kVArated()

    @kVArated.setter
    def kVArated(self, Value):
        lib.PVSystems_Set_kVArated(Value)

    @property
    def kW(self):
        '''(read-only) get kW output'''
        return lib.PVSystems_Get_kW()

    @property
    def kvar(self):
        '''
        (read) Get kvar value
        (write) Set kvar output value
        '''
        return lib.PVSystems_Get_kvar()

    @kvar.setter
    def kvar(self, Value):
        lib.PVSystems_Set_kvar(Value)


class IReclosers(FrozenClass):
    _isfrozen = freeze

    def Close(self):
        lib.Reclosers_Close()

    def Open(self):
        lib.Reclosers_Open()

    @property
    def AllNames(self):
        '''(read-only) Array of strings with names of all Reclosers in Active Circuit'''
        return get_string_array(lib.Reclosers_Get_AllNames)

    @property
    def Count(self):
        '''(read-only) Number of Reclosers in active circuit.'''
        return lib.Reclosers_Get_Count()

    def __len__(self):
        return lib.Reclosers_Get_Count()

    @property
    def First(self):
        '''(read-only) Set First Recloser to be Active Ckt Element. Returns 0 if none.'''
        return lib.Reclosers_Get_First()

    @property
    def GroundInst(self):
        '''
        (read) Ground (3I0) instantaneous trip setting - curve multipler or actual amps.
        (write) Ground (3I0) trip instantaneous multiplier or actual amps
        '''
        return lib.Reclosers_Get_GroundInst()

    @GroundInst.setter
    def GroundInst(self, Value):
        lib.Reclosers_Set_GroundInst(Value)

    @property
    def GroundTrip(self):
        '''Ground (3I0) trip multiplier or actual amps'''
        return lib.Reclosers_Get_GroundTrip()

    @GroundTrip.setter
    def GroundTrip(self, Value):
        lib.Reclosers_Set_GroundTrip(Value)

    @property
    def MonitoredObj(self):
        '''
        (read) Full name of object this Recloser is monitoring.
        (write) Set monitored object by full name.
        '''
        return get_string(lib.Reclosers_Get_MonitoredObj())

    @MonitoredObj.setter
    def MonitoredObj(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Reclosers_Set_MonitoredObj(Value)

    @property
    def MonitoredTerm(self):
        '''Terminal number of Monitored object for the Recloser '''
        return lib.Reclosers_Get_MonitoredTerm()

    @MonitoredTerm.setter
    def MonitoredTerm(self, Value):
        lib.Reclosers_Set_MonitoredTerm(Value)

    @property
    def Name(self):
        '''Get Name of active Recloser or set the active Recloser by name.'''
        return get_string(lib.Reclosers_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Reclosers_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Iterate to the next recloser in the circuit. Returns zero if no more.'''
        return lib.Reclosers_Get_Next()

    @property
    def NumFast(self):
        '''Number of fast shots'''
        return lib.Reclosers_Get_NumFast()

    @NumFast.setter
    def NumFast(self, Value):
        lib.Reclosers_Set_NumFast(Value)

    @property
    def PhaseInst(self):
        '''Phase instantaneous curve multipler or actual amps'''
        return lib.Reclosers_Get_PhaseInst()

    @PhaseInst.setter
    def PhaseInst(self, Value):
        lib.Reclosers_Set_PhaseInst(Value)

    @property
    def PhaseTrip(self):
        '''
        (read) Phase trip curve multiplier or actual amps
        (write) Phase Trip multiplier or actual amps
        '''
        return lib.Reclosers_Get_PhaseTrip()

    @PhaseTrip.setter
    def PhaseTrip(self, Value):
        lib.Reclosers_Set_PhaseTrip(Value)

    @property
    def RecloseIntervals(self):
        '''(read-only) Variant Array of Doubles: reclose intervals, s, between shots.'''
        return get_float64_array(lib.Reclosers_Get_RecloseIntervals)

    @property
    def Shots(self):
        '''Number of shots to lockout (fast + delayed)'''
        return lib.Reclosers_Get_Shots()

    @Shots.setter
    def Shots(self, Value):
        lib.Reclosers_Set_Shots(Value)

    @property
    def SwitchedObj(self):
        '''Full name of the circuit element that is being switched by the Recloser.'''
        return get_string(lib.Reclosers_Get_SwitchedObj())

    @SwitchedObj.setter
    def SwitchedObj(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Reclosers_Set_SwitchedObj(Value)

    @property
    def SwitchedTerm(self):
        '''Terminal number of the controlled device being switched by the Recloser'''
        return lib.Reclosers_Get_SwitchedTerm()

    @SwitchedTerm.setter
    def SwitchedTerm(self, Value):
        lib.Reclosers_Set_SwitchedTerm(Value)

    @property
    def idx(self):
        '''Get/Set the active Recloser by index into the recloser list.  1..Count'''
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
        '''(read-only) Array of strings containing all RegControl names'''
        return get_string_array(lib.RegControls_Get_AllNames)

    @property
    def CTPrimary(self):
        '''CT primary ampere rating (secondary is 0.2 amperes)'''
        return lib.RegControls_Get_CTPrimary()

    @CTPrimary.setter
    def CTPrimary(self, Value):
        lib.RegControls_Set_CTPrimary(Value)

    @property
    def Count(self):
        '''(read-only) Number of RegControl objects in Active Circuit'''
        return lib.RegControls_Get_Count()

    def __len__(self):
        return lib.RegControls_Get_Count()

    @property
    def Delay(self):
        '''Time delay [s] after arming before the first tap change. Control may reset before actually changing taps.'''
        return lib.RegControls_Get_Delay()

    @Delay.setter
    def Delay(self, Value):
        lib.RegControls_Set_Delay(Value)

    @property
    def First(self):
        '''(read-only) Sets the first RegControl active. Returns 0 if none.'''
        return lib.RegControls_Get_First()

    @property
    def ForwardBand(self):
        '''Regulation bandwidth in forward direciton, centered on Vreg'''
        return lib.RegControls_Get_ForwardBand()

    @ForwardBand.setter
    def ForwardBand(self, Value):
        lib.RegControls_Set_ForwardBand(Value)

    @property
    def ForwardR(self):
        '''LDC R setting in Volts'''
        return lib.RegControls_Get_ForwardR()

    @ForwardR.setter
    def ForwardR(self, Value):
        lib.RegControls_Set_ForwardR(Value)

    @property
    def ForwardVreg(self):
        '''Target voltage in the forward direction, on PT secondary base.'''
        return lib.RegControls_Get_ForwardVreg()

    @ForwardVreg.setter
    def ForwardVreg(self, Value):
        lib.RegControls_Set_ForwardVreg(Value)

    @property
    def ForwardX(self):
        '''LDC X setting in Volts'''
        return lib.RegControls_Get_ForwardX()

    @ForwardX.setter
    def ForwardX(self, Value):
        lib.RegControls_Set_ForwardX(Value)

    @property
    def IsInverseTime(self):
        '''Time delay is inversely adjsuted, proportinal to the amount of voltage outside the regulating band.'''
        return lib.RegControls_Get_IsInverseTime() != 0

    @IsInverseTime.setter
    def IsInverseTime(self, Value):
        lib.RegControls_Set_IsInverseTime(Value)

    @property
    def IsReversible(self):
        '''Regulator can use different settings in the reverse direction.  Usually not applicable to substation transformers.'''
        return lib.RegControls_Get_IsReversible() != 0

    @IsReversible.setter
    def IsReversible(self, Value):
        lib.RegControls_Set_IsReversible(Value)

    @property
    def MaxTapChange(self):
        '''Maximum tap change per iteration in STATIC solution mode. 1 is more realistic, 16 is the default for a faster soluiton.'''
        return lib.RegControls_Get_MaxTapChange()

    @MaxTapChange.setter
    def MaxTapChange(self, Value):
        lib.RegControls_Set_MaxTapChange(Value)

    @property
    def MonitoredBus(self):
        '''Name of a remote regulated bus, in lieu of LDC settings'''
        return get_string(lib.RegControls_Get_MonitoredBus())

    @MonitoredBus.setter
    def MonitoredBus(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.RegControls_Set_MonitoredBus(Value)

    @property
    def Name(self):
        '''
        (read) Get/set Active RegControl  name
        (write) Sets a RegControl active by name
        '''
        return get_string(lib.RegControls_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.RegControls_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Sets the next RegControl active. Returns 0 if none.'''
        return lib.RegControls_Get_Next()

    @property
    def PTratio(self):
        '''PT ratio for voltage control settings'''
        return lib.RegControls_Get_PTratio()

    @PTratio.setter
    def PTratio(self, Value):
        lib.RegControls_Set_PTratio(Value)

    @property
    def ReverseBand(self):
        '''Bandwidth in reverse direction, centered on reverse Vreg.'''
        return lib.RegControls_Get_ReverseBand()

    @ReverseBand.setter
    def ReverseBand(self, Value):
        lib.RegControls_Set_ReverseBand(Value)

    @property
    def ReverseR(self):
        '''Reverse LDC R setting in Volts.'''
        return lib.RegControls_Get_ReverseR()

    @ReverseR.setter
    def ReverseR(self, Value):
        lib.RegControls_Set_ReverseR(Value)

    @property
    def ReverseVreg(self):
        '''Target voltage in the revese direction, on PT secondary base.'''
        return lib.RegControls_Get_ReverseVreg()

    @ReverseVreg.setter
    def ReverseVreg(self, Value):
        lib.RegControls_Set_ReverseVreg(Value)

    @property
    def ReverseX(self):
        '''Reverse LDC X setting in volts.'''
        return lib.RegControls_Get_ReverseX()

    @ReverseX.setter
    def ReverseX(self, Value):
        lib.RegControls_Set_ReverseX(Value)

    @property
    def TapDelay(self):
        '''Time delay [s] for subsequent tap changes in a set. Control may reset before actually changing taps.'''
        return lib.RegControls_Get_TapDelay()

    @TapDelay.setter
    def TapDelay(self, Value):
        lib.RegControls_Set_TapDelay(Value)

    @property
    def TapNumber(self):
        '''Integer number of the tap that the controlled transformer winding is currentliy on.'''
        return lib.RegControls_Get_TapNumber()

    @TapNumber.setter
    def TapNumber(self, Value):
        lib.RegControls_Set_TapNumber(Value)

    @property
    def TapWinding(self):
        '''Tapped winding number'''
        return lib.RegControls_Get_TapWinding()

    @TapWinding.setter
    def TapWinding(self, Value):
        lib.RegControls_Set_TapWinding(Value)

    @property
    def Transformer(self):
        '''Name of the transformer this regulator controls'''
        return get_string(lib.RegControls_Get_Transformer())

    @Transformer.setter
    def Transformer(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.RegControls_Set_Transformer(Value)

    @property
    def VoltageLimit(self):
        '''First house voltage limit on PT secondary base.  Setting to 0 disables this function.'''
        return lib.RegControls_Get_VoltageLimit()

    @VoltageLimit.setter
    def VoltageLimit(self, Value):
        lib.RegControls_Set_VoltageLimit(Value)

    @property
    def Winding(self):
        '''Winding number for PT and CT connections'''
        return lib.RegControls_Get_Winding()

    @Winding.setter
    def Winding(self, Value):
        lib.RegControls_Set_Winding(Value)


class IRelays(FrozenClass):
    _isfrozen = freeze

    @property
    def AllNames(self):
        '''(read-only) Array of strings containing names of all Relay elements'''
        return get_string_array(lib.Relays_Get_AllNames)

    @property
    def Count(self):
        '''(read-only) Number of Relays in circuit'''
        return lib.Relays_Get_Count()

    def __len__(self):
        return lib.Relays_Get_Count()

    @property
    def First(self):
        '''(read-only) Set First Relay active. If none, returns 0.'''
        return lib.Relays_Get_First()

    @property
    def MonitoredObj(self):
        '''Full name of object this Relay is monitoring.'''
        return get_string(lib.Relays_Get_MonitoredObj())

    @MonitoredObj.setter
    def MonitoredObj(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Relays_Set_MonitoredObj(Value)

    @property
    def MonitoredTerm(self):
        '''Number of terminal of monitored element that this Relay is monitoring.'''
        return lib.Relays_Get_MonitoredTerm()

    @MonitoredTerm.setter
    def MonitoredTerm(self, Value):
        lib.Relays_Set_MonitoredTerm(Value)

    @property
    def Name(self):
        '''
        (read) Get name of active relay.
        (write) Set Relay active by name
        '''
        return get_string(lib.Relays_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Relays_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Advance to next Relay object. Returns 0 when no more relays.'''
        return lib.Relays_Get_Next()

    @property
    def SwitchedObj(self):
        '''Full name of element that will be switched when relay trips.'''
        return get_string(lib.Relays_Get_SwitchedObj())

    @SwitchedObj.setter
    def SwitchedObj(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Relays_Set_SwitchedObj(Value)

    @property
    def SwitchedTerm(self):
        '''Terminal number of the switched object that will be opened when the relay trips.'''
        return lib.Relays_Get_SwitchedTerm()

    @SwitchedTerm.setter
    def SwitchedTerm(self, Value):
        lib.Relays_Set_SwitchedTerm(Value)

    @property
    def idx(self):
        '''
        (read) Get/Set active Relay by index into the Relay list. 1..Count
        (write) Get/Set Relay active by index into relay list. 1..Count
        '''
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
        '''(read-only) Array of Sensor names.'''
        return get_string_array(lib.Sensors_Get_AllNames)

    @property
    def Count(self):
        '''(read-only) Number of Sensors in Active Circuit.'''
        return lib.Sensors_Get_Count()

    def __len__(self):
        return lib.Sensors_Get_Count()

    @property
    def Currents(self):
        '''Array of doubles for the line current measurements; don't use with kWS and kVARS.'''
        return get_float64_array(lib.Sensors_Get_Currents)

    @Currents.setter
    def Currents(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.Sensors_Set_Currents(ValuePtr, ValueCount)

    @property
    def First(self):
        '''(read-only) Sets the first sensor active. Returns 0 if none.'''
        return lib.Sensors_Get_First()

    @property
    def IsDelta(self):
        '''True if measured voltages are line-line. Currents are always line currents.'''
        return lib.Sensors_Get_IsDelta() != 0

    @IsDelta.setter
    def IsDelta(self, Value):
        lib.Sensors_Set_IsDelta(Value)

    @property
    def MeteredElement(self):
        '''Full Name of the measured element'''
        return get_string(lib.Sensors_Get_MeteredElement())

    @MeteredElement.setter
    def MeteredElement(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Sensors_Set_MeteredElement(Value)

    @property
    def MeteredTerminal(self):
        '''Number of the measured terminal in the measured element.'''
        return lib.Sensors_Get_MeteredTerminal()

    @MeteredTerminal.setter
    def MeteredTerminal(self, Value):
        lib.Sensors_Set_MeteredTerminal(Value)

    @property
    def Name(self):
        '''
        (read) Name of the active sensor.
        (write) Set the active Sensor by name.
        '''
        return get_string(lib.Sensors_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Sensors_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Sets the next Sensor active. Returns 0 if no more.'''
        return lib.Sensors_Get_Next()

    @property
    def PctError(self):
        '''Assumed percent error in the Sensor measurement. Default is 1.'''
        return lib.Sensors_Get_PctError()

    @PctError.setter
    def PctError(self, Value):
        lib.Sensors_Set_PctError(Value)

    @property
    def ReverseDelta(self):
        '''True if voltage measurements are 1-3, 3-2, 2-1.'''
        return lib.Sensors_Get_ReverseDelta() != 0

    @ReverseDelta.setter
    def ReverseDelta(self, Value):
        lib.Sensors_Set_ReverseDelta(Value)

    @property
    def Weight(self):
        '''Weighting factor for this Sensor measurement with respect to other Sensors. Default is 1.'''
        return lib.Sensors_Get_Weight()

    @Weight.setter
    def Weight(self, Value):
        lib.Sensors_Set_Weight(Value)

    @property
    def kVARS(self):
        '''Array of doubles for Q measurements. Overwrites Currents with a new estimate using kWS.'''
        return get_float64_array(lib.Sensors_Get_kVARS)

    @kVARS.setter
    def kVARS(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.Sensors_Set_kVARS(ValuePtr, ValueCount)

    @property
    def kVS(self):
        '''Array of doubles for the LL or LN (depending on Delta connection) voltage measurements.'''
        return get_float64_array(lib.Sensors_Get_kVS)

    @kVS.setter
    def kVS(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.Sensors_Set_kVS(ValuePtr, ValueCount)

    @property
    def kVbase(self):
        '''Voltage base for the sensor measurements. LL for 2 and 3-phase sensors, LN for 1-phase sensors.'''
        return lib.Sensors_Get_kVbase()

    @kVbase.setter
    def kVbase(self, Value):
        lib.Sensors_Set_kVbase(Value)

    @property
    def kWS(self):
        '''Array of doubles for P measurements. Overwrites Currents with a new estimate using kVARS.'''
        return get_float64_array(lib.Sensors_Get_kWS)

    @kWS.setter
    def kWS(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.Sensors_Set_kWS(ValuePtr, ValueCount)


class ISettings(FrozenClass):
    _isfrozen = freeze

    @property
    def AllowDuplicates(self):
        '''{True | False*} Designates whether to allow duplicate names of objects'''
        return lib.Settings_Get_AllowDuplicates() != 0

    @AllowDuplicates.setter
    def AllowDuplicates(self, Value):
        lib.Settings_Set_AllowDuplicates(Value)

    @property
    def AutoBusList(self):
        '''List of Buses or (File=xxxx) syntax for the AutoAdd solution mode.'''
        return get_string(lib.Settings_Get_AutoBusList())

    @AutoBusList.setter
    def AutoBusList(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Settings_Set_AutoBusList(Value)

    @property
    def CktModel(self):
        '''{dssMultiphase * | dssPositiveSeq} IIndicate if the circuit model is positive sequence.'''
        return lib.Settings_Get_CktModel()

    @CktModel.setter
    def CktModel(self, Value):
        lib.Settings_Set_CktModel(Value)

    @property
    def ControlTrace(self):
        '''{True | False*} Denotes whether to trace the control actions to a file.'''
        return lib.Settings_Get_ControlTrace() != 0

    @ControlTrace.setter
    def ControlTrace(self, Value):
        lib.Settings_Set_ControlTrace(Value)

    @property
    def EmergVmaxpu(self):
        '''Per Unit maximum voltage for Emergency conditions.'''
        return lib.Settings_Get_EmergVmaxpu()

    @EmergVmaxpu.setter
    def EmergVmaxpu(self, Value):
        lib.Settings_Set_EmergVmaxpu(Value)

    @property
    def EmergVminpu(self):
        '''Per Unit minimum voltage for Emergency conditions.'''
        return lib.Settings_Get_EmergVminpu()

    @EmergVminpu.setter
    def EmergVminpu(self, Value):
        lib.Settings_Set_EmergVminpu(Value)

    @property
    def LossRegs(self):
        '''Integer array defining which energy meter registers to use for computing losses'''
        return get_int32_array(lib.Settings_Get_LossRegs)

    @LossRegs.setter
    def LossRegs(self, Value):
        Value, ValuePtr, ValueCount = prepare_int32_array(Value)
        lib.Settings_Set_LossRegs(ValuePtr, ValueCount)

    @property
    def LossWeight(self):
        '''Weighting factor applied to Loss register values.'''
        return lib.Settings_Get_LossWeight()

    @LossWeight.setter
    def LossWeight(self, Value):
        lib.Settings_Set_LossWeight(Value)

    @property
    def NormVmaxpu(self):
        '''Per Unit maximum voltage for Normal conditions.'''
        return lib.Settings_Get_NormVmaxpu()

    @NormVmaxpu.setter
    def NormVmaxpu(self, Value):
        lib.Settings_Set_NormVmaxpu(Value)

    @property
    def NormVminpu(self):
        '''Per Unit minimum voltage for Normal conditions.'''
        return lib.Settings_Get_NormVminpu()

    @NormVminpu.setter
    def NormVminpu(self, Value):
        lib.Settings_Set_NormVminpu(Value)

    @property
    def PriceCurve(self):
        '''Name of LoadShape object that serves as the source of price signal data for yearly simulations, etc.'''
        return get_string(lib.Settings_Get_PriceCurve())

    @PriceCurve.setter
    def PriceCurve(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Settings_Set_PriceCurve(Value)

    @property
    def PriceSignal(self):
        '''Price Signal for the Circuit'''
        return lib.Settings_Get_PriceSignal()

    @PriceSignal.setter
    def PriceSignal(self, Value):
        lib.Settings_Set_PriceSignal(Value)

    @property
    def Trapezoidal(self):
        '''{True | False *} Gets value of trapezoidal integration flag in energy meters.'''
        return lib.Settings_Get_Trapezoidal() != 0

    @Trapezoidal.setter
    def Trapezoidal(self, Value):
        lib.Settings_Set_Trapezoidal(Value)

    @property
    def UEregs(self):
        '''Array of Integers defining energy meter registers to use for computing UE'''
        return get_int32_array(lib.Settings_Get_UEregs)

    @UEregs.setter
    def UEregs(self, Value):
        Value, ValuePtr, ValueCount = prepare_int32_array(Value)
        lib.Settings_Set_UEregs(ValuePtr, ValueCount)

    @property
    def UEweight(self):
        '''Weighting factor applied to UE register values.'''
        return lib.Settings_Get_UEweight()

    @UEweight.setter
    def UEweight(self, Value):
        lib.Settings_Set_UEweight(Value)

    @property
    def VoltageBases(self):
        '''Array of doubles defining the legal voltage bases in kV L-L'''
        return get_float64_array(lib.Settings_Get_VoltageBases)

    @VoltageBases.setter
    def VoltageBases(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.Settings_Set_VoltageBases(ValuePtr, ValueCount)

    @property
    def ZoneLock(self):
        '''{True | False*}  Locks Zones on energy meters to prevent rebuilding if a circuit change occurs.'''
        return lib.Settings_Get_ZoneLock() != 0

    @ZoneLock.setter
    def ZoneLock(self, Value):
        lib.Settings_Set_ZoneLock(Value)

    @property
    def AllocationFactors(self):
        '''(write-only) Sets all load allocation factors for all loads defined by XFKVA property to this value.'''
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

    def SolveAll(self):
        lib.Solution_SolveAll()

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
        '''Type of device to add in AutoAdd Mode: {dssGen (Default) | dssCap}'''
        return lib.Solution_Get_AddType()

    @AddType.setter
    def AddType(self, Value):
        lib.Solution_Set_AddType(Value)

    @property
    def Algorithm(self):
        '''Base Solution algorithm: {dssNormalSolve | dssNewtonSolve}'''
        return lib.Solution_Get_Algorithm()

    @Algorithm.setter
    def Algorithm(self, Value):
        lib.Solution_Set_Algorithm(Value)

    @property
    def BusLevels(self):
        return get_int32_array(lib.Solution_Get_BusLevels)

    @property
    def Capkvar(self):
        '''Capacitor kvar for adding capacitors in AutoAdd mode'''
        return lib.Solution_Get_Capkvar()

    @Capkvar.setter
    def Capkvar(self, Value):
        lib.Solution_Set_Capkvar(Value)

    @property
    def ControlActionsDone(self):
        '''Flag indicating the control actions are done.'''
        return lib.Solution_Get_ControlActionsDone() != 0

    @ControlActionsDone.setter
    def ControlActionsDone(self, Value):
        lib.Solution_Set_ControlActionsDone(Value)

    @property
    def ControlIterations(self):
        '''Value of the control iteration counter'''
        return lib.Solution_Get_ControlIterations()

    @ControlIterations.setter
    def ControlIterations(self, Value):
        lib.Solution_Set_ControlIterations(Value)

    @property
    def ControlMode(self):
        '''{dssStatic* | dssEvent | dssTime}  Modes for control devices'''
        return lib.Solution_Get_ControlMode()

    @ControlMode.setter
    def ControlMode(self, Value):
        lib.Solution_Set_ControlMode(Value)

    @property
    def Converged(self):
        '''Flag to indicate whether the circuit solution converged'''
        return lib.Solution_Get_Converged() != 0

    @Converged.setter
    def Converged(self, Value):
        lib.Solution_Set_Converged(Value)

    @property
    def DefaultDaily(self):
        '''Default daily load shape (defaults to "Default")'''
        return get_string(lib.Solution_Get_DefaultDaily())

    @DefaultDaily.setter
    def DefaultDaily(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Solution_Set_DefaultDaily(Value)

    @property
    def DefaultYearly(self):
        '''Default Yearly load shape (defaults to "Default")'''
        return get_string(lib.Solution_Get_DefaultYearly())

    @DefaultYearly.setter
    def DefaultYearly(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Solution_Set_DefaultYearly(Value)

    @property
    def EventLog(self):
        '''(read-only) Array of strings containing the Event Log'''
        return get_string_array(lib.Solution_Get_EventLog)

    @property
    def Frequency(self):
        '''Set the Frequency for next solution'''
        return lib.Solution_Get_Frequency()

    @Frequency.setter
    def Frequency(self, Value):
        lib.Solution_Set_Frequency(Value)

    @property
    def GenMult(self):
        '''Default Multiplier applied to generators (like LoadMult)'''
        return lib.Solution_Get_GenMult()

    @GenMult.setter
    def GenMult(self, Value):
        lib.Solution_Set_GenMult(Value)

    @property
    def GenPF(self):
        '''PF for generators in AutoAdd mode'''
        return lib.Solution_Get_GenPF()

    @GenPF.setter
    def GenPF(self, Value):
        lib.Solution_Set_GenPF(Value)

    @property
    def GenkW(self):
        '''Generator kW for AutoAdd mode'''
        return lib.Solution_Get_GenkW()

    @GenkW.setter
    def GenkW(self, Value):
        lib.Solution_Set_GenkW(Value)

    @property
    def Hour(self):
        '''Set Hour for time series solutions.'''
        return lib.Solution_Get_Hour()

    @Hour.setter
    def Hour(self, Value):
        lib.Solution_Set_Hour(Value)

    @property
    def IncMatrix(self):
        return get_int32_array(lib.Solution_Get_IncMatrix)

    @property
    def IncMatrixCols(self):
        return get_string_array(lib.Solution_Get_IncMatrixCols)

    @property
    def IncMatrixRows(self):
        return get_string_array(lib.Solution_Get_IncMatrixRows)

    @property
    def IntervalHrs(self):
        '''
        (read) Get/Set the Solution.IntervalHrs variable used for devices that integrate
        (write) Get/Set the Solution.IntervalHrs variable for custom solution algorithms
        '''
        return lib.Solution_Get_IntervalHrs()

    @IntervalHrs.setter
    def IntervalHrs(self, Value):
        lib.Solution_Set_IntervalHrs(Value)

    @property
    def Iterations(self):
        '''(read-only) Number of iterations taken for last solution. (Same as TotalIterations)'''
        return lib.Solution_Get_Iterations()

    @property
    def LDCurve(self):
        '''Load-Duration Curve name for LD modes'''
        return get_string(lib.Solution_Get_LDCurve())

    @LDCurve.setter
    def LDCurve(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Solution_Set_LDCurve(Value)

    @property
    def LoadModel(self):
        '''Load Model: {dssPowerFlow (default) | dssAdmittance}'''
        return lib.Solution_Get_LoadModel()

    @LoadModel.setter
    def LoadModel(self, Value):
        lib.Solution_Set_LoadModel(Value)

    @property
    def LoadMult(self):
        '''Default load multiplier applied to all non-fixed loads'''
        return lib.Solution_Get_LoadMult()

    @LoadMult.setter
    def LoadMult(self, Value):
        lib.Solution_Set_LoadMult(Value)

    @property
    def MaxControlIterations(self):
        '''Maximum allowable control iterations'''
        return lib.Solution_Get_MaxControlIterations()

    @MaxControlIterations.setter
    def MaxControlIterations(self, Value):
        lib.Solution_Set_MaxControlIterations(Value)

    @property
    def MaxIterations(self):
        '''Max allowable iterations.'''
        return lib.Solution_Get_MaxIterations()

    @MaxIterations.setter
    def MaxIterations(self, Value):
        lib.Solution_Set_MaxIterations(Value)

    @property
    def MinIterations(self):
        '''
        (read) Minimum number of iterations required for a power flow solution.
        (write) Mininum number of iterations required for a power flow solution.
        '''
        return lib.Solution_Get_MinIterations()

    @MinIterations.setter
    def MinIterations(self, Value):
        lib.Solution_Set_MinIterations(Value)

    @property
    def Mode(self):
        '''Set present solution mode (by a text code - see DSS Help)'''
        return lib.Solution_Get_Mode()

    @Mode.setter
    def Mode(self, Mode):
        lib.Solution_Set_Mode(Mode)

    @property
    def ModeID(self):
        '''(read-only) ID (text) of the present solution mode'''
        return get_string(lib.Solution_Get_ModeID())

    @property
    def MostIterationsDone(self):
        '''(read-only) Max number of iterations required to converge at any control iteration of the most recent solution.'''
        return lib.Solution_Get_MostIterationsDone()

    @property
    def Number(self):
        '''Number of solutions to perform for Monte Carlo and time series simulations'''
        return lib.Solution_Get_Number()

    @Number.setter
    def Number(self, Value):
        lib.Solution_Set_Number(Value)

    @property
    def Process_Time(self):
        '''(read-only) Gets the time required to perform the latest solution (Read only)'''
        return lib.Solution_Get_Process_Time()

    @property
    def Random(self):
        '''Randomization mode for random variables "Gaussian" or "Uniform"'''
        return lib.Solution_Get_Random()

    @Random.setter
    def Random(self, Random):
        lib.Solution_Set_Random(Random)

    @property
    def Seconds(self):
        '''Seconds from top of the hour.'''
        return lib.Solution_Get_Seconds()

    @Seconds.setter
    def Seconds(self, Value):
        lib.Solution_Set_Seconds(Value)

    @property
    def StepSize(self):
        '''Time step size in sec'''
        return lib.Solution_Get_StepSize()

    @StepSize.setter
    def StepSize(self, Value):
        lib.Solution_Set_StepSize(Value)

    @property
    def SystemYChanged(self):
        '''(read-only) Flag that indicates if elements of the System Y have been changed by recent activity.'''
        return lib.Solution_Get_SystemYChanged() != 0

    @property
    def Time_of_Step(self):
        '''(read-only) Get the solution process time + sample time for time step'''
        return lib.Solution_Get_Time_of_Step()

    @property
    def Tolerance(self):
        '''Solution convergence tolerance.'''
        return lib.Solution_Get_Tolerance()

    @Tolerance.setter
    def Tolerance(self, Value):
        lib.Solution_Set_Tolerance(Value)

    @property
    def Total_Time(self):
        '''
        (read) Gets the accumulated time of the simulation
        (write) Sets the Accumulated time of the simulation
        '''
        return lib.Solution_Get_Total_Time()

    @Total_Time.setter
    def Total_Time(self, Value):
        lib.Solution_Set_Total_Time(Value)

    @property
    def Totaliterations(self):
        '''(read-only) Total iterations including control iterations for most recent solution.'''
        return lib.Solution_Get_Totaliterations()

    @property
    def Year(self):
        '''Set year for planning studies'''
        return lib.Solution_Get_Year()

    @Year.setter
    def Year(self, Value):
        lib.Solution_Set_Year(Value)

    @property
    def dblHour(self):
        '''Hour as a double, including fractional part'''
        return lib.Solution_Get_dblHour()

    @dblHour.setter
    def dblHour(self, Value):
        lib.Solution_Set_dblHour(Value)

    @property
    def pctGrowth(self):
        '''Percent default  annual load growth rate'''
        return lib.Solution_Get_pctGrowth()

    @pctGrowth.setter
    def pctGrowth(self, Value):
        lib.Solution_Set_pctGrowth(Value)

    @property
    def StepsizeHr(self):
        '''(write-only) Set Stepsize in Hr'''
        raise AttributeError("This property is write-only!")

    @StepsizeHr.setter
    def StepsizeHr(self, Value):
        lib.Solution_Set_StepsizeHr(Value)

    @property
    def StepsizeMin(self):
        '''(write-only) Set Stepsize in minutes'''
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
        '''Open or Close the switch. No effect if switch is locked.  However, Reset removes any lock and then closes the switch (shelf state).'''
        return lib.SwtControls_Get_Action()

    @Action.setter
    def Action(self, Value):
        lib.SwtControls_Set_Action(Value)

    @property
    def AllNames(self):
        '''(read-only) Array of strings with all SwtControl names in the active circuit.'''
        return get_string_array(lib.SwtControls_Get_AllNames)

    @property
    def Count(self):
        return lib.SwtControls_Get_Count()

    def __len__(self):
        return lib.SwtControls_Get_Count()

    @property
    def Delay(self):
        '''Time delay [s] betwen arming and opening or closing the switch.  Control may reset before actually operating the switch.'''
        return lib.SwtControls_Get_Delay()

    @Delay.setter
    def Delay(self, Value):
        lib.SwtControls_Set_Delay(Value)

    @property
    def First(self):
        '''(read-only) Sets the first SwtControl active. Returns 0 if no more.'''
        return lib.SwtControls_Get_First()

    @property
    def IsLocked(self):
        '''The lock prevents both manual and automatic switch operation.'''
        return lib.SwtControls_Get_IsLocked() != 0

    @IsLocked.setter
    def IsLocked(self, Value):
        lib.SwtControls_Set_IsLocked(Value)

    @property
    def Name(self):
        '''Sets a SwtControl active by Name.'''
        return get_string(lib.SwtControls_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.SwtControls_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Sets the next SwtControl active. Returns 0 if no more.'''
        return lib.SwtControls_Get_Next()

    @property
    def NormalState(self):
        '''
        (read) Get Normal state of switch
        (write) set Normal state of switch  (see actioncodes) dssActionOpen or dssActionClose
        '''
        return lib.SwtControls_Get_NormalState()

    @NormalState.setter
    def NormalState(self, Value):
        lib.SwtControls_Set_NormalState(Value)

    @property
    def State(self):
        '''
        (read) Force switch to specified state
        (write) Get Present state of switch
        '''
        return lib.SwtControls_Get_State()

    @State.setter
    def State(self, Value):
        lib.SwtControls_Set_State(Value)

    @property
    def SwitchedObj(self):
        '''Full name of the switched element.'''
        return get_string(lib.SwtControls_Get_SwitchedObj())

    @SwitchedObj.setter
    def SwitchedObj(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.SwtControls_Set_SwitchedObj(Value)

    @property
    def SwitchedTerm(self):
        '''Terminal number where the switch is located on the SwitchedObj'''
        return lib.SwtControls_Get_SwitchedTerm()

    @SwitchedTerm.setter
    def SwitchedTerm(self, Value):
        lib.SwtControls_Set_SwitchedTerm(Value)


class IText(FrozenClass):
    _isfrozen = freeze

    @property
    def Command(self):
        '''Input command string for the DSS.'''
        return get_string(lib.Text_Get_Command())

    @Command.setter
    def Command(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Text_Set_Command(Value)
        CheckForError()

    @property
    def Result(self):
        '''(read-only) Result string for the last command.'''
        return get_string(lib.Text_Get_Result())


class ITopology(FrozenClass):
    _isfrozen = freeze

    @property
    def ActiveBranch(self):
        '''(read-only) Returns index of the active branch'''
        return lib.Topology_Get_ActiveBranch()

    @property
    def ActiveLevel(self):
        '''(read-only) Topological depth of the active branch'''
        return lib.Topology_Get_ActiveLevel()

    @property
    def AllIsolatedBranches(self):
        '''(read-only) Array of all isolated branch names.'''
        return get_string_array(lib.Topology_Get_AllIsolatedBranches)

    @property
    def AllIsolatedLoads(self):
        '''(read-only) Array of all isolated load names.'''
        return get_string_array(lib.Topology_Get_AllIsolatedLoads)

    @property
    def AllLoopedPairs(self):
        '''(read-only) Array of all looped element names, by pairs.'''
        return get_string_array(lib.Topology_Get_AllLoopedPairs)

    @property
    def BackwardBranch(self):
        '''(read-only) MOve back toward the source, return index of new active branch, or 0 if no more.'''
        return lib.Topology_Get_BackwardBranch()

    @property
    def BranchName(self):
        '''Name of the active branch.'''
        return get_string(lib.Topology_Get_BranchName())

    @BranchName.setter
    def BranchName(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Topology_Set_BranchName(Value)

    @property
    def BusName(self):
        '''Set the active branch to one containing this bus, return index or 0 if not found'''
        return get_string(lib.Topology_Get_BusName())

    @BusName.setter
    def BusName(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Topology_Set_BusName(Value)

    @property
    def First(self):
        '''(read-only) Sets the first branch active, returns 0 if none.'''
        return lib.Topology_Get_First()

    @property
    def FirstLoad(self):
        '''(read-only) First load at the active branch, return index or 0 if none.'''
        return lib.Topology_Get_FirstLoad()

    @property
    def ForwardBranch(self):
        '''(read-only) Move forward in the tree, return index of new active branch or 0 if no more'''
        return lib.Topology_Get_ForwardBranch()

    @property
    def LoopedBranch(self):
        '''(read-only) Move to looped branch, return index or 0 if none.'''
        return lib.Topology_Get_LoopedBranch()

    @property
    def Next(self):
        '''(read-only) Sets the next branch active, returns 0 if no more.'''
        return lib.Topology_Get_Next()

    @property
    def NextLoad(self):
        '''(read-only) Next load at the active branch, return index or 0 if no more.'''
        return lib.Topology_Get_NextLoad()

    @property
    def NumIsolatedBranches(self):
        '''(read-only) Number of isolated branches (PD elements and capacitors).'''
        return lib.Topology_Get_NumIsolatedBranches()

    @property
    def NumIsolatedLoads(self):
        '''(read-only) Number of isolated loads'''
        return lib.Topology_Get_NumIsolatedLoads()

    @property
    def NumLoops(self):
        '''(read-only) Number of loops'''
        return lib.Topology_Get_NumLoops()

    @property
    def ParallelBranch(self):
        '''(read-only) Move to directly parallel branch, return index or 0 if none.'''
        return lib.Topology_Get_ParallelBranch()


class ITransformers(FrozenClass):
    _isfrozen = freeze

    @property
    def AllNames(self):
        '''(read-only) Array of strings with all Transformer names in the active circuit.'''
        return get_string_array(lib.Transformers_Get_AllNames)

    @property
    def Count(self):
        return lib.Transformers_Get_Count()

    def __len__(self):
        return lib.Transformers_Get_Count()

    @property
    def First(self):
        '''(read-only) Sets the first Transformer active. Returns 0 if no more.'''
        return lib.Transformers_Get_First()

    @property
    def IsDelta(self):
        '''Active Winding delta or wye connection?'''
        return lib.Transformers_Get_IsDelta() != 0

    @IsDelta.setter
    def IsDelta(self, Value):
        lib.Transformers_Set_IsDelta(Value)

    @property
    def MaxTap(self):
        '''Active Winding maximum tap in per-unit.'''
        return lib.Transformers_Get_MaxTap()

    @MaxTap.setter
    def MaxTap(self, Value):
        lib.Transformers_Set_MaxTap(Value)

    @property
    def MinTap(self):
        '''Active Winding minimum tap in per-unit.'''
        return lib.Transformers_Get_MinTap()

    @MinTap.setter
    def MinTap(self, Value):
        lib.Transformers_Set_MinTap(Value)

    @property
    def Name(self):
        '''Sets a Transformer active by Name.'''
        return get_string(lib.Transformers_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Transformers_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Sets the next Transformer active. Returns 0 if no more.'''
        return lib.Transformers_Get_Next()

    @property
    def NumTaps(self):
        '''Active Winding number of tap steps betwein MinTap and MaxTap.'''
        return lib.Transformers_Get_NumTaps()

    @NumTaps.setter
    def NumTaps(self, Value):
        lib.Transformers_Set_NumTaps(Value)

    @property
    def NumWindings(self):
        '''Number of windings on this transformer. Allocates memory; set or change this property first.'''
        return lib.Transformers_Get_NumWindings()

    @NumWindings.setter
    def NumWindings(self, Value):
        lib.Transformers_Set_NumWindings(Value)

    @property
    def R(self):
        '''Active Winding resistance in %'''
        return lib.Transformers_Get_R()

    @R.setter
    def R(self, Value):
        lib.Transformers_Set_R(Value)

    @property
    def Rneut(self):
        '''Active Winding neutral resistance [ohms] for wye connections. Set less than zero for ungrounded wye.'''
        return lib.Transformers_Get_Rneut()

    @Rneut.setter
    def Rneut(self, Value):
        lib.Transformers_Set_Rneut(Value)

    @property
    def Tap(self):
        '''Active Winding tap in per-unit.'''
        return lib.Transformers_Get_Tap()

    @Tap.setter
    def Tap(self, Value):
        lib.Transformers_Set_Tap(Value)

    @property
    def Wdg(self):
        '''Active Winding Number from 1..NumWindings. Update this before reading or setting a sequence of winding properties (R, Tap, kV, kVA, etc.)'''
        return lib.Transformers_Get_Wdg()

    @Wdg.setter
    def Wdg(self, Value):
        lib.Transformers_Set_Wdg(Value)

    @property
    def XfmrCode(self):
        '''Name of an XfrmCode that supplies electircal parameters for this Transformer.'''
        return get_string(lib.Transformers_Get_XfmrCode())

    @XfmrCode.setter
    def XfmrCode(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Transformers_Set_XfmrCode(Value)

    @property
    def Xhl(self):
        '''Percent reactance between windings 1 and 2, on winding 1 kVA base. Use for 2-winding or 3-winding transformers.'''
        return lib.Transformers_Get_Xhl()

    @Xhl.setter
    def Xhl(self, Value):
        lib.Transformers_Set_Xhl(Value)

    @property
    def Xht(self):
        '''Percent reactance between windigns 1 and 3, on winding 1 kVA base.  Use for 3-winding transformers only.'''
        return lib.Transformers_Get_Xht()

    @Xht.setter
    def Xht(self, Value):
        lib.Transformers_Set_Xht(Value)

    @property
    def Xlt(self):
        '''Percent reactance between windings 2 and 3, on winding 1 kVA base. Use for 3-winding transformers only.'''
        return lib.Transformers_Get_Xlt()

    @Xlt.setter
    def Xlt(self, Value):
        lib.Transformers_Set_Xlt(Value)

    @property
    def Xneut(self):
        '''Active Winding neutral reactance [ohms] for wye connections.'''
        return lib.Transformers_Get_Xneut()

    @Xneut.setter
    def Xneut(self, Value):
        lib.Transformers_Set_Xneut(Value)

    @property
    def kV(self):
        '''Active Winding kV rating.  Phase-phase for 2 or 3 phases, actual winding kV for 1 phase transformer.'''
        return lib.Transformers_Get_kV()

    @kV.setter
    def kV(self, Value):
        lib.Transformers_Set_kV(Value)

    @property
    def kVA(self):
        '''Active Winding kVA rating. On winding 1, this also determines normal and emergency current ratings for all windings.'''
        return lib.Transformers_Get_kVA()

    @kVA.setter
    def kVA(self, Value):
        lib.Transformers_Set_kVA(Value)


class IVsources(FrozenClass):
    _isfrozen = freeze

    @property
    def AllNames(self):
        '''(read-only) Names of all Vsource objects in the circuit'''
        return get_string_array(lib.Vsources_Get_AllNames)

    @property
    def AngleDeg(self):
        '''
        (read) Phase angle of first phase in degrees
        (write) phase angle in degrees
        '''
        return lib.Vsources_Get_AngleDeg()

    @AngleDeg.setter
    def AngleDeg(self, Value):
        lib.Vsources_Set_AngleDeg(Value)

    @property
    def BasekV(self):
        '''Source voltage in kV'''
        return lib.Vsources_Get_BasekV()

    @BasekV.setter
    def BasekV(self, Value):
        lib.Vsources_Set_BasekV(Value)

    @property
    def Count(self):
        '''(read-only) Number of Vsource Object'''
        return lib.Vsources_Get_Count()

    def __len__(self):
        return lib.Vsources_Get_Count()

    @property
    def First(self):
        '''(read-only) Sets the first VSOURCE to be active; Returns 0 if none'''
        return lib.Vsources_Get_First()

    @property
    def Frequency(self):
        '''Source frequency in Hz'''
        return lib.Vsources_Get_Frequency()

    @Frequency.setter
    def Frequency(self, Value):
        lib.Vsources_Set_Frequency(Value)

    @property
    def Name(self):
        '''
        (read) Get Active VSOURCE name
        (write) Set Active VSOURCE by Name
        '''
        return get_string(lib.Vsources_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.Vsources_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Sets the next VSOURCE object to be active; returns zero if no more'''
        return lib.Vsources_Get_Next()

    @property
    def Phases(self):
        '''Number of phases'''
        return lib.Vsources_Get_Phases()

    @Phases.setter
    def Phases(self, Value):
        lib.Vsources_Set_Phases(Value)

    @property
    def pu(self):
        '''
        (read) Source pu voltage.
        (write) Per-unit value of source voltage based on kV
        '''
        return lib.Vsources_Get_pu()

    @pu.setter
    def pu(self, Value):
        lib.Vsources_Set_pu(Value)


class IXYCurves(FrozenClass):
    _isfrozen = freeze

    @property
    def Count(self):
        '''(read-only) Number of XYCurve Objects'''
        return lib.XYCurves_Get_Count()

    def __len__(self):
        return lib.XYCurves_Get_Count()

    @property
    def First(self):
        '''(read-only) Sets first XYcurve object active; returns 0 if none.'''
        return lib.XYCurves_Get_First()

    @property
    def Name(self):
        '''
        (read) Name of active XYCurve Object
        (write) Get Name of active XYCurve Object
        '''
        return get_string(lib.XYCurves_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.XYCurves_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Advances to next XYCurve object; returns 0 if no more objects of this class'''
        return lib.XYCurves_Get_Next()

    @property
    def Npts(self):
        '''Get/Set Number of points in X-Y curve'''
        return lib.XYCurves_Get_Npts()

    @Npts.setter
    def Npts(self, Value):
        lib.XYCurves_Set_Npts(Value)

    @property
    def Xarray(self):
        '''Get/Set X values as a Array of doubles. Set Npts to max number expected if setting'''
        return get_float64_array(lib.XYCurves_Get_Xarray)

    @Xarray.setter
    def Xarray(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.XYCurves_Set_Xarray(ValuePtr, ValueCount)

    @property
    def Xscale(self):
        '''Factor to scale X values from original curve'''
        return lib.XYCurves_Get_Xscale()

    @Xscale.setter
    def Xscale(self, Value):
        lib.XYCurves_Set_Xscale(Value)

    @property
    def Xshift(self):
        '''Amount to shift X value from original curve'''
        return lib.XYCurves_Get_Xshift()

    @Xshift.setter
    def Xshift(self, Value):
        lib.XYCurves_Set_Xshift(Value)

    @property
    def Yarray(self):
        '''Get/Set Y values in curve; Set Npts to max number expected if setting'''
        return get_float64_array(lib.XYCurves_Get_Yarray)

    @Yarray.setter
    def Yarray(self, Value):
        Value, ValuePtr, ValueCount = prepare_float64_array(Value)
        lib.XYCurves_Set_Yarray(ValuePtr, ValueCount)

    @property
    def Yscale(self):
        '''
        (read) Factor to scale Y values from original curve
        (write) Amount to scale Y values from original curve. Represents a curve shift.
        '''
        return lib.XYCurves_Get_Yscale()

    @Yscale.setter
    def Yscale(self, Value):
        lib.XYCurves_Set_Yscale(Value)

    @property
    def Yshift(self):
        '''amount to shift Y valiue from original curve'''
        return lib.XYCurves_Get_Yshift()

    @Yshift.setter
    def Yshift(self, Value):
        lib.XYCurves_Set_Yshift(Value)

    @property
    def x(self):
        '''Set X value or get interpolated value after setting Y'''
        return lib.XYCurves_Get_x()

    @x.setter
    def x(self, Value):
        lib.XYCurves_Set_x(Value)

    @property
    def y(self):
        '''
        (read) Y value for present X or set this value then get corresponding X
        (write) Set Y value or get interpolated Y value after setting X
        '''
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
        '''(read-only) Full name of the i-th controller attached to this element. Ex: str = Controller(2).  See NumControls to determine valid index range'''
        return get_string(lib.CktElement_Get_Controller(idx))

    def Variable(self, MyVarName, Code):
        '''(read-only) For PCElement, get the value of a variable by name. If Code>0 Then no variable by this name or not a PCelement.'''
        if type(MyVarName) is not bytes:
            MyVarName = MyVarName.encode(codec)

        return lib.CktElement_Get_Variable(MyVarName, Code)

    def Variablei(self, Idx, Code):
        '''(read-only) For PCElement, get the value of a variable by integer index.'''
        return lib.CktElement_Get_Variablei(Idx, Code)

    def IsOpen(self, Term, Phs):
        return lib.CktElement_IsOpen(Term, Phs) != 0

    def Open(self, Term, Phs):
        lib.CktElement_Open(Term, Phs)

    @property
    def AllPropertyNames(self):
        '''(read-only) Array containing all property names of the active device.'''
        return get_string_array(lib.CktElement_Get_AllPropertyNames)

    @property
    def AllVariableNames(self):
        '''(read-only) Array of strings listing all the published variable names, if a PCElement. Otherwise, null string.'''
        return get_string_array(lib.CktElement_Get_AllVariableNames)

    @property
    def AllVariableValues(self):
        '''(read-only) Array of doubles. Values of state variables of active element if PC element.'''
        return get_float64_array(lib.CktElement_Get_AllVariableValues)

    @property
    def BusNames(self):
        '''
        (read) Array of strings. Get  Bus definitions to which each terminal is connected. 0-based array.
        (write) Array of strings. Set Bus definitions for each terminal is connected.
        '''
        return get_string_array(lib.CktElement_Get_BusNames)

    @BusNames.setter
    def BusNames(self, Value):
        Value, ValuePtr, ValueCount = prepare_string_array(Value)
        lib.CktElement_Set_BusNames(ValuePtr, ValueCount)

    @property
    def CplxSeqCurrents(self):
        '''(read-only) Complex double array of Sequence Currents for all conductors of all terminals of active circuit element.'''
        return get_float64_array(lib.CktElement_Get_CplxSeqCurrents)

    @property
    def CplxSeqVoltages(self):
        '''(read-only) Complex double array of Sequence Voltage for all terminals of active circuit element.'''
        return get_float64_array(lib.CktElement_Get_CplxSeqVoltages)

    @property
    def Currents(self):
        '''(read-only) Complex array of currents into each conductor of each terminal'''
        return get_float64_array(lib.CktElement_Get_Currents)

    @property
    def CurrentsMagAng(self):
        '''(read-only) Currents in magnitude, angle format as a array of doubles.'''
        return get_float64_array(lib.CktElement_Get_CurrentsMagAng)

    @property
    def DisplayName(self):
        '''Display name of the object (not necessarily unique)'''
        return get_string(lib.CktElement_Get_DisplayName())

    @DisplayName.setter
    def DisplayName(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.CktElement_Set_DisplayName(Value)

    @property
    def EmergAmps(self):
        '''
        (read) Emergency Ampere Rating for PD elements
        (write) Emergency Ampere Rating
        '''
        return lib.CktElement_Get_EmergAmps()

    @EmergAmps.setter
    def EmergAmps(self, Value):
        lib.CktElement_Set_EmergAmps(Value)

    @property
    def Enabled(self):
        '''Boolean indicating that element is currently in the circuit.'''
        return lib.CktElement_Get_Enabled() != 0

    @Enabled.setter
    def Enabled(self, Value):
        lib.CktElement_Set_Enabled(Value)

    @property
    def EnergyMeter(self):
        '''(read-only) Name of the Energy Meter this element is assigned to.'''
        return get_string(lib.CktElement_Get_EnergyMeter())

    @property
    def GUID(self):
        '''(read-only) globally unique identifier for this object'''
        return get_string(lib.CktElement_Get_GUID())

    @property
    def Handle(self):
        '''(read-only) Pointer to this object'''
        return lib.CktElement_Get_Handle()

    @property
    def HasOCPDevice(self):
        '''(read-only) True if a recloser, relay, or fuse controlling this ckt element. OCP = Overcurrent Protection '''
        return lib.CktElement_Get_HasOCPDevice() != 0

    @property
    def HasSwitchControl(self):
        '''(read-only) This element has a SwtControl attached.'''
        return lib.CktElement_Get_HasSwitchControl() != 0

    @property
    def HasVoltControl(self):
        '''(read-only) This element has a CapControl or RegControl attached.'''
        return lib.CktElement_Get_HasVoltControl() != 0

    @property
    def Losses(self):
        '''(read-only) Total losses in the element: two-element complex array'''
        return get_float64_array(lib.CktElement_Get_Losses)

    @property
    def Name(self):
        '''(read-only) Full Name of Active Circuit Element'''
        return get_string(lib.CktElement_Get_Name())

    @property
    def NodeOrder(self):
        '''(read-only) Array of integer containing the node numbers (representing phases, for example) for each conductor of each terminal. '''
        return get_int32_array(lib.CktElement_Get_NodeOrder)

    @property
    def NormalAmps(self):
        '''
        (read) Normal ampere rating for PD Elements
        (write) Normal ampere rating
        '''
        return lib.CktElement_Get_NormalAmps()

    @NormalAmps.setter
    def NormalAmps(self, Value):
        lib.CktElement_Set_NormalAmps(Value)

    @property
    def NumConductors(self):
        '''(read-only) Number of Conductors per Terminal'''
        return lib.CktElement_Get_NumConductors()

    @property
    def NumControls(self):
        '''(read-only) Number of controls connected to this device. Use to determine valid range for index into Controller array.'''
        return lib.CktElement_Get_NumControls()

    @property
    def NumPhases(self):
        '''(read-only) Number of Phases'''
        return lib.CktElement_Get_NumPhases()

    @property
    def NumProperties(self):
        '''(read-only) Number of Properties this Circuit Element.'''
        return lib.CktElement_Get_NumProperties()

    @property
    def NumTerminals(self):
        '''(read-only) Number of Terminals this Circuit Element'''
        return lib.CktElement_Get_NumTerminals()

    @property
    def OCPDevIndex(self):
        '''(read-only) Index into Controller list of OCP Device controlling this CktElement'''
        return lib.CktElement_Get_OCPDevIndex()

    @property
    def OCPDevType(self):
        '''(read-only) 0=None; 1=Fuse; 2=Recloser; 3=Relay;  Type of OCP controller device'''
        return lib.CktElement_Get_OCPDevType()

    @property
    def PhaseLosses(self):
        '''(read-only) Complex array of losses by phase'''
        return get_float64_array(lib.CktElement_Get_PhaseLosses)

    @property
    def Powers(self):
        '''(read-only) Complex array of powers into each conductor of each terminal'''
        return get_float64_array(lib.CktElement_Get_Powers)

    @property
    def Residuals(self):
        '''(read-only) Residual currents for each terminal: (mag, angle)'''
        return get_float64_array(lib.CktElement_Get_Residuals)

    @property
    def SeqCurrents(self):
        '''(read-only) Double array of symmetrical component currents into each 3-phase terminal'''
        return get_float64_array(lib.CktElement_Get_SeqCurrents)

    @property
    def SeqPowers(self):
        '''(read-only) Double array of sequence powers into each 3-phase teminal'''
        return get_float64_array(lib.CktElement_Get_SeqPowers)

    @property
    def SeqVoltages(self):
        '''(read-only) Double array of symmetrical component voltages at each 3-phase terminal'''
        return get_float64_array(lib.CktElement_Get_SeqVoltages)

    @property
    def Voltages(self):
        '''(read-only) Complex array of voltages at terminals'''
        return get_float64_array(lib.CktElement_Get_Voltages)

    @property
    def VoltagesMagAng(self):
        '''(read-only) Voltages at each conductor in magnitude, angle form as array of doubles.'''
        return get_float64_array(lib.CktElement_Get_VoltagesMagAng)

    @property
    def Yprim(self):
        '''(read-only) YPrim matrix, column order, complex numbers (paired)'''
        return get_float64_array(lib.CktElement_Get_Yprim)

    def __getitem__(self, index):
        if isinstance(index, int):
            # index is zero based, pass it directly
            lib.Circuit_SetCktElementIndex(index)
        else:
            if type(index) is not bytes:
                index = index.encode(codec)
                
            lib.Circuit_SetCktElementName(index)
    
        return self
        
    def __call__(self, index):
        return self.__getitem__(index)
        



class IDSSElement(FrozenClass):
    _isfrozen = freeze
    Properties = IDSSProperty()

    @property
    def AllPropertyNames(self):
        '''(read-only) Array of strings containing the names of all properties for the active DSS object.'''
        return get_string_array(lib.DSSElement_Get_AllPropertyNames)

    @property
    def Name(self):
        '''(read-only) Full Name of Active DSS Object (general element or circuit element).'''
        return get_string(lib.DSSElement_Get_Name())

    @property
    def NumProperties(self):
        '''(read-only) Number of Properties for the active DSS object.'''
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
    Parallel = IParallel()
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
        '''(read-only) Returns an array of doubles representing the distances to parent EnergyMeter. Sequence of array corresponds to other node ByPhase properties.'''
        return get_float64_array(lib.Circuit_Get_AllNodeDistancesByPhase, Phase)

    def AllNodeNamesByPhase(self, Phase):
        '''(read-only) Return array of strings of the node names for the By Phase criteria. Sequence corresponds to other ByPhase properties.'''
        return get_string_array(lib.Circuit_Get_AllNodeNamesByPhase, Phase)

    def AllNodeVmagByPhase(self, Phase):
        '''(read-only) Returns Array of doubles represent voltage magnitudes for nodes on the specified phase.'''
        return get_float64_array(lib.Circuit_Get_AllNodeVmagByPhase, Phase)

    def AllNodeVmagPUByPhase(self, Phase):
        '''(read-only) Returns array of per unit voltage magnitudes for each node by phase'''
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
        '''(read-only) Returns distance from each bus to parent EnergyMeter. Corresponds to sequence in AllBusNames.'''
        return get_float64_array(lib.Circuit_Get_AllBusDistances)

    @property
    def AllBusNames(self):
        '''(read-only) Array of strings containing names of all buses in circuit (see AllNodeNames).'''
        return get_string_array(lib.Circuit_Get_AllBusNames)

    @property
    def AllBusVmag(self):
        '''(read-only) Array of magnitudes (doubles) of voltages at all buses'''
        return get_float64_array(lib.Circuit_Get_AllBusVmag)

    @property
    def AllBusVmagPu(self):
        '''(read-only) Double Array of all bus voltages (each node) magnitudes in Per unit'''
        return get_float64_array(lib.Circuit_Get_AllBusVmagPu)

    @property
    def AllBusVolts(self):
        '''(read-only) Complex array of all bus, node voltages from most recent solution'''
        return get_float64_array(lib.Circuit_Get_AllBusVolts)

    @property
    def AllElementLosses(self):
        '''(read-only) Array of total losses (complex) in each circuit element'''
        return get_float64_array(lib.Circuit_Get_AllElementLosses)

    @property
    def AllElementNames(self):
        '''(read-only) Array of strings containing Full Name of all elements.'''
        return get_string_array(lib.Circuit_Get_AllElementNames)

    @property
    def AllNodeDistances(self):
        '''(read-only) Returns an array of distances from parent EnergyMeter for each Node. Corresponds to AllBusVMag sequence.'''
        return get_float64_array(lib.Circuit_Get_AllNodeDistances)

    @property
    def AllNodeNames(self):
        '''(read-only) Array of strings containing full name of each node in system in same order as returned by AllBusVolts, etc.'''
        return get_string_array(lib.Circuit_Get_AllNodeNames)

    @property
    def LineLosses(self):
        '''(read-only) Complex total line losses in the circuit'''
        return get_float64_array(lib.Circuit_Get_LineLosses)

    @property
    def Losses(self):
        '''(read-only) Total losses in active circuit, complex number (two-element array of double).'''
        return get_float64_array(lib.Circuit_Get_Losses)

    @property
    def Name(self):
        '''(read-only) Name of the active circuit.'''
        return get_string(lib.Circuit_Get_Name())

    @property
    def NumBuses(self):
        '''(read-only) Total number of Buses in the circuit.'''
        return lib.Circuit_Get_NumBuses()

    @property
    def NumCktElements(self):
        '''(read-only) Number of CktElements in the circuit.'''
        return lib.Circuit_Get_NumCktElements()

    @property
    def NumNodes(self):
        '''(read-only) Total number of nodes in the circuit.'''
        return lib.Circuit_Get_NumNodes()

    @property
    def ParentPDElement(self):
        '''(read-only) Sets Parent PD element, if any, to be the active circuit element and returns index>0; Returns 0 if it fails or not applicable.'''
        return lib.Circuit_Get_ParentPDElement()

    @property
    def SubstationLosses(self):
        '''(read-only) Complex losses in all transformers designated to substations.'''
        return get_float64_array(lib.Circuit_Get_SubstationLosses)

    @property
    def SystemY(self):
        '''(read-only) System Y matrix (after a solution has been performed)'''
        return get_float64_array(lib.Circuit_Get_SystemY)

    @property
    def TotalPower(self):
        '''(read-only) Total power, watts delivered to the circuit'''
        return get_float64_array(lib.Circuit_Get_TotalPower)

    @property
    def YCurrents(self):
        '''(read-only) Array of doubles containing complex injection currents for the present solution. Is is the "I" vector of I=YV'''
        return get_float64_array(lib.Circuit_Get_YCurrents)

    @property
    def YNodeOrder(self):
        '''(read-only) Array of strings containing the names of the nodes in the same order as the Y matrix'''
        return get_string_array(lib.Circuit_Get_YNodeOrder)

    @property
    def YNodeVarray(self):
        '''(read-only) Complex array of actual node voltages in same order as SystemY matrix.'''
        return get_float64_array(lib.Circuit_Get_YNodeVarray)


class IYMatrix(FrozenClass):
    _isfrozen = freeze
    
    def GetCompressedYMatrix(self, factor=True):
        '''Return as (data, indices, indptr) that can fed into scipy.sparse.csc_matrix'''
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
        '''Get access to the internal Current pointer'''
        IvectorPtr = ffi.new('double**')
        lib.YMatrix_getIpointer(IvectorPtr)
        return IvectorPtr[0]
        
    def GetVPointer(self):
        '''Get access to the internal Voltage pointer'''
        VvectorPtr = ffi.new('double**')
        lib.YMatrix_getVpointer(VvectorPtr)
        return VvectorPtr[0]
        
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

    @UseAuxCurrents.setter
    def UseAuxCurrents(self, value):
        lib.YMatrix_Set_UseAuxCurrents(value)
        
    # for better compatibility with OpenDSSDirect.py
    getYSparse = GetCompressedYMatrix

    def getI(self):
        '''Get the data from the internal Current pointer'''
        IvectorPtr = self.IVector()
        return ffi.unpack(IvectorPtr, lib.Circuit_Get_NumNodes() + 1)
        
    def getV(self):
        '''Get the data from the internal Voltage pointer'''
        VvectorPtr = self.VVector()
        return ffi.unpack(VvectorPtr, lib.Circuit_Get_NumNodes() + 1)


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
        '''(read-only) List of DSS intrinsic classes (names of the classes)'''
        return get_string_array(lib.DSS_Get_Classes)

    @property
    def DataPath(self):
        '''DSS Data File Path.  Default path for reports, etc. from DSS'''
        return get_string(lib.DSS_Get_DataPath())

    @DataPath.setter
    def DataPath(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(codec)

        lib.DSS_Set_DataPath(Value)

    @property
    def DefaultEditor(self):
        '''(read-only) Returns the path name for the default text editor.'''
        return get_string(lib.DSS_Get_DefaultEditor())

    @property
    def NumCircuits(self):
        '''(read-only) Number of Circuits currently defined'''
        return lib.DSS_Get_NumCircuits()

    @property
    def NumClasses(self):
        '''(read-only) Number of DSS intrinsic classes'''
        return lib.DSS_Get_NumClasses()

    @property
    def NumUserClasses(self):
        '''(read-only) Number of user-defined classes'''
        return lib.DSS_Get_NumUserClasses()

    @property
    def UserClasses(self):
        '''(read-only) List of user-defined classes'''
        return get_string_array(lib.DSS_Get_UserClasses)

    @property
    def Version(self):
        '''(read-only) Get version string for the DSS.'''
        return get_string(lib.DSS_Get_Version())

    @property
    def AllowForms(self):
        warnings.warn('AllowForms is not implemented.')

    @AllowForms.setter
    def AllowForms(self, value):
        warnings.warn('AllowForms is not implemented.')
    
    def ShowPanel(self):
        warnings.warn('ShowPanel is not implemented.')
        
    def NewCircuit(self, name):
        if type(name) is not bytes:
            name = name.encode(codec)

        lib.DSS_NewCircuit(name)
        CheckForError()
        
        return self.ActiveCircuit





DSS = IDSS()        

prepare_com_compat(vars())
       
