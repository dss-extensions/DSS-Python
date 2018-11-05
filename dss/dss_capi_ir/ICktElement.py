'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base
from .IDSSProperty import IDSSProperty

class ICktElement(Base):
    __slots__ = [
        'Properties'
    ]

    def __init__(self, api_util):
        self.Properties = IDSSProperty(api_util)
        Base.__init__(self, api_util)    
    
    def Close(self, Term, Phs):
        self._lib.CktElement_Close(Term, Phs)

    def Controller(self, idx):
        '''(read-only) Full name of the i-th controller attached to this element. Ex: str = Controller(2).  See NumControls to determine valid index range'''
        return self._get_string(self._lib.CktElement_Get_Controller(idx))

    def Variable(self, MyVarName, Code):
        '''(read-only) For PCElement, get the value of a variable by name. If Code>0 Then no variable by this name or not a PCelement.'''
        if type(MyVarName) is not bytes:
            MyVarName = MyVarName.encode(self._api_util.codec)

        return self._lib.CktElement_Get_Variable(MyVarName, Code)

    def Variablei(self, Idx, Code):
        '''(read-only) For PCElement, get the value of a variable by integer index.'''
        return self._lib.CktElement_Get_Variablei(Idx, Code)

    def IsOpen(self, Term, Phs):
        return self._lib.CktElement_IsOpen(Term, Phs) != 0

    def Open(self, Term, Phs):
        self._lib.CktElement_Open(Term, Phs)

    @property
    def AllPropertyNames(self):
        '''(read-only) Array containing all property names of the active device.'''
        return self._get_string_array(self._lib.CktElement_Get_AllPropertyNames)

    @property
    def AllVariableNames(self):
        '''(read-only) Array of strings listing all the published variable names, if a PCElement. Otherwise, null string.'''
        return self._get_string_array(self._lib.CktElement_Get_AllVariableNames)

    @property
    def AllVariableValues(self):
        '''(read-only) Array of doubles. Values of state variables of active element if PC element.'''
        return self._get_float64_array(self._lib.CktElement_Get_AllVariableValues)

    @property
    def BusNames(self):
        '''
        (read) Array of strings. Get  Bus definitions to which each terminal is connected. 0-based array.
        (write) Array of strings. Set Bus definitions for each terminal is connected.
        '''
        return self._get_string_array(self._lib.CktElement_Get_BusNames)

    @BusNames.setter
    def BusNames(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_string_array(Value)
        self._lib.CktElement_Set_BusNames(ValuePtr, ValueCount)
        self.CheckForError()

    @property
    def CplxSeqCurrents(self):
        '''(read-only) Complex double array of Sequence Currents for all conductors of all terminals of active circuit element.'''
        return self._get_float64_array(self._lib.CktElement_Get_CplxSeqCurrents)

    @property
    def CplxSeqVoltages(self):
        '''(read-only) Complex double array of Sequence Voltage for all terminals of active circuit element.'''
        return self._get_float64_array(self._lib.CktElement_Get_CplxSeqVoltages)

    @property
    def Currents(self):
        '''(read-only) Complex array of currents into each conductor of each terminal'''
        return self._get_float64_array(self._lib.CktElement_Get_Currents)

    @property
    def CurrentsMagAng(self):
        '''(read-only) Currents in magnitude, angle format as a array of doubles.'''
        return self._get_float64_array(self._lib.CktElement_Get_CurrentsMagAng)

    @property
    def DisplayName(self):
        '''Display name of the object (not necessarily unique)'''
        return self._get_string(self._lib.CktElement_Get_DisplayName())

    @DisplayName.setter
    def DisplayName(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.CktElement_Set_DisplayName(Value)
        self.CheckForError()

    @property
    def EmergAmps(self):
        '''
        (read) Emergency Ampere Rating for PD elements
        (write) Emergency Ampere Rating
        '''
        return self._lib.CktElement_Get_EmergAmps()

    @EmergAmps.setter
    def EmergAmps(self, Value):
        self._lib.CktElement_Set_EmergAmps(Value)
        self.CheckForError()

    @property
    def Enabled(self):
        '''Boolean indicating that element is currently in the circuit.'''
        return self._lib.CktElement_Get_Enabled() != 0

    @Enabled.setter
    def Enabled(self, Value):
        self._lib.CktElement_Set_Enabled(Value)
        self.CheckForError()

    @property
    def EnergyMeter(self):
        '''(read-only) Name of the Energy Meter this element is assigned to.'''
        return self._get_string(self._lib.CktElement_Get_EnergyMeter())

    @property
    def GUID(self):
        '''(read-only) globally unique identifier for this object'''
        return self._get_string(self._lib.CktElement_Get_GUID())

    @property
    def Handle(self):
        '''(read-only) Pointer to this object'''
        return self._lib.CktElement_Get_Handle()

    @property
    def HasOCPDevice(self):
        '''(read-only) True if a recloser, relay, or fuse controlling this ckt element. OCP = Overcurrent Protection '''
        return self._lib.CktElement_Get_HasOCPDevice() != 0

    @property
    def HasSwitchControl(self):
        '''(read-only) This element has a SwtControl attached.'''
        return self._lib.CktElement_Get_HasSwitchControl() != 0

    @property
    def HasVoltControl(self):
        '''(read-only) This element has a CapControl or RegControl attached.'''
        return self._lib.CktElement_Get_HasVoltControl() != 0

    @property
    def Losses(self):
        '''(read-only) Total losses in the element: two-element complex array'''
        return self._get_float64_array(self._lib.CktElement_Get_Losses)

    @property
    def Name(self):
        '''(read-only) Full Name of Active Circuit Element'''
        return self._get_string(self._lib.CktElement_Get_Name())

    @property
    def NodeOrder(self):
        '''(read-only) Array of integer containing the node numbers (representing phases, for example) for each conductor of each terminal. '''
        return self._get_int32_array(self._lib.CktElement_Get_NodeOrder)

    @property
    def NormalAmps(self):
        '''
        (read) Normal ampere rating for PD Elements
        (write) Normal ampere rating
        '''
        return self._lib.CktElement_Get_NormalAmps()

    @NormalAmps.setter
    def NormalAmps(self, Value):
        self._lib.CktElement_Set_NormalAmps(Value)
        self.CheckForError()

    @property
    def NumConductors(self):
        '''(read-only) Number of Conductors per Terminal'''
        return self._lib.CktElement_Get_NumConductors()

    @property
    def NumControls(self):
        '''(read-only) Number of controls connected to this device. Use to determine valid range for index into Controller array.'''
        return self._lib.CktElement_Get_NumControls()

    @property
    def NumPhases(self):
        '''(read-only) Number of Phases'''
        return self._lib.CktElement_Get_NumPhases()

    @property
    def NumProperties(self):
        '''(read-only) Number of Properties this Circuit Element.'''
        return self._lib.CktElement_Get_NumProperties()

    @property
    def NumTerminals(self):
        '''(read-only) Number of Terminals this Circuit Element'''
        return self._lib.CktElement_Get_NumTerminals()

    @property
    def OCPDevIndex(self):
        '''(read-only) Index into Controller list of OCP Device controlling this CktElement'''
        return self._lib.CktElement_Get_OCPDevIndex()

    @property
    def OCPDevType(self):
        '''(read-only) 0=None; 1=Fuse; 2=Recloser; 3=Relay;  Type of OCP controller device'''
        return self._lib.CktElement_Get_OCPDevType()

    @property
    def PhaseLosses(self):
        '''(read-only) Complex array of losses by phase'''
        return self._get_float64_array(self._lib.CktElement_Get_PhaseLosses)

    @property
    def Powers(self):
        '''(read-only) Complex array of powers into each conductor of each terminal'''
        return self._get_float64_array(self._lib.CktElement_Get_Powers)

    @property
    def Residuals(self):
        '''(read-only) Residual currents for each terminal: (mag, angle)'''
        return self._get_float64_array(self._lib.CktElement_Get_Residuals)

    @property
    def SeqCurrents(self):
        '''(read-only) Double array of symmetrical component currents into each 3-phase terminal'''
        return self._get_float64_array(self._lib.CktElement_Get_SeqCurrents)

    @property
    def SeqPowers(self):
        '''(read-only) Double array of sequence powers into each 3-phase teminal'''
        return self._get_float64_array(self._lib.CktElement_Get_SeqPowers)

    @property
    def SeqVoltages(self):
        '''(read-only) Double array of symmetrical component voltages at each 3-phase terminal'''
        return self._get_float64_array(self._lib.CktElement_Get_SeqVoltages)

    @property
    def Voltages(self):
        '''(read-only) Complex array of voltages at terminals'''
        return self._get_float64_array(self._lib.CktElement_Get_Voltages)

    @property
    def VoltagesMagAng(self):
        '''(read-only) Voltages at each conductor in magnitude, angle form as array of doubles.'''
        return self._get_float64_array(self._lib.CktElement_Get_VoltagesMagAng)

    @property
    def Yprim(self):
        '''(read-only) YPrim matrix, column order, complex numbers (paired)'''
        return self._get_float64_array(self._lib.CktElement_Get_Yprim)

    def __getitem__(self, index):
        if isinstance(index, int):
            # index is zero based, pass it directly
            self._lib.Circuit_SetCktElementIndex(index)
        else:
            if type(index) is not bytes:
                index = index.encode(self._api_util.codec)

            self._lib.Circuit_SetCktElementName(index)

        return self

    def __call__(self, index):
        return self.__getitem__(index)

