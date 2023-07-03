'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2023 Paulo Meira

Copyright (c) 2018-2023 DSS-Extensions contributors
'''
from ._cffi_api_util import Base
from .IDSSProperty import IDSSProperty
from ._types import Float64Array, Int32Array, Float64ArrayOrComplexArray, Float64ArrayOrSimpleComplex
from typing import List, AnyStr, Tuple
from .enums import OCPDevType as OCPDevTypeEnum

class ICktElement(Base):
    __slots__ = [
        'Properties'
    ]

    _columns = [
        'Name', 
        'DisplayName',
        'Handle',
        'GUID',
        'Enabled',
        'NumTerminals',
        'NumPhases',
        'NumConductors',
        'NumControls',
        'NumProperties',
        'AllPropertyNames', 
        'AllVariableValues', 
        'AllVariableNames', 
        'BusNames',
        'NormalAmps',
        'EmergAmps',
        'HasVoltControl',
        'HasSwitchControl',
        'HasOCPDevice',
        'OCPDevType',
        'OCPDevIndex',
        'IsIsolated',
        'EnergyMeter',
        'TotalPowers',

        'Yprim',
        'NodeOrder',
        'Voltages',
        'VoltagesMagAng',
        'SeqVoltages',
        'CplxSeqVoltages',
        'Powers',
        'SeqPowers',
        'Currents',
        'CurrentsMagAng',
        'SeqCurrents',
        'CplxSeqCurrents',
        'Residuals',
        'Losses',
        'PhaseLosses',
    ]

    Properties: IDSSProperty

    def __init__(self, api_util):
        self.Properties = IDSSProperty(api_util)
        Base.__init__(self, api_util)    
    
    def Close(self, Term: int, Phs: int):
        self.CheckForError(self._lib.CktElement_Close(Term, Phs))

    def Controller(self, idx: int) -> str:
        '''Full name of the i-th controller attached to this element. Ex: str = Controller(2).  See NumControls to determine valid index range'''
        return self._get_string(self.CheckForError(self._lib.CktElement_Get_Controller(idx)))

    def Variable(self, MyVarName: AnyStr) -> Tuple[float, int]:
        '''Returns (value, Code). For PCElement, get the value of a variable by name. If Code>0 Then no variable by this name or not a PCelement.'''
        if type(MyVarName) is not bytes:
            MyVarName = MyVarName.encode(self._api_util.codec)

        Code = self._api_util.ffi.new('int32_t*')
        result = self.CheckForError(self._lib.CktElement_Get_Variable(MyVarName, Code))
        # if Code[0] == 1:
        #     raise DssException('No variable by this name or not a PCelement')
        return result, Code[0]
    

    def Variablei(self, Idx: int) -> Tuple[float, int]:
        '''Returns (value, Code). For PCElement, get the value of a variable by integer index. If Code>0 Then no variable by this index or not a PCelement.'''
        Code = self._api_util.ffi.new('int32_t*')
        result = self.CheckForError(self._lib.CktElement_Get_Variablei(Idx, Code))
        # if Code[0] == 1:
        #     raise DssException('Invalid variable index or not a PCelement')
        return result, Code[0]

    # for compatibility with OpenDSS 9.4.1.1
    VariableByIndex = Variablei
    VariableByName = Variable

    def setVariableByIndex(self, Idx: int, Value: float) -> int:
        Code = self._api_util.ffi.new('int32_t*')
        self.CheckForError(self._lib.CktElement_Set_Variablei(Idx, Code, Value))
        # if Code[0] == 1:
        #     raise DSSException('Invalid variable index or not a PCelement')
        return Code[0]

    def setVariableByName(self, Idx: AnyStr, Value: float) -> int:
        Code = self._api_util.ffi.new('int32_t*')
        self.CheckForError(self._lib.CktElement_Set_Variable(Idx, Code, Value))
        # if Code[0] == 1:
        #     raise DSSException('Invalid variable index or not a PCelement')
        return Code[0]

    def IsOpen(self, Term: int, Phs: int) -> bool:
        return self.CheckForError(self._lib.CktElement_IsOpen(Term, Phs)) != 0

    def Open(self, Term: int, Phs: int):
        self.CheckForError(self._lib.CktElement_Open(Term, Phs))

    @property
    def AllPropertyNames(self) -> List[str]:
        '''Array containing all property names of the active device.'''
        return self.CheckForError(self._get_string_array(self._lib.CktElement_Get_AllPropertyNames))

    @property
    def AllVariableNames(self) -> List[str]:
        '''
        Array of strings listing all the published state variable names.
        Valid only for PCElements.
        '''
        return self.CheckForError(self._get_string_array(self._lib.CktElement_Get_AllVariableNames))

    @property
    def AllVariableValues(self) -> Float64Array:
        '''
        Array of doubles. Values of state variables of active element if PC element.
        Valid only for PCElements.
        '''
        self.CheckForError(self._lib.CktElement_Get_AllVariableValues_GR())
        return self._get_float64_gr_array()

    @property
    def BusNames(self) -> List[str]:
        '''
        Array of strings. Get  Bus definitions to which each terminal is connected.
        '''
        return self.CheckForError(self._get_string_array(self._lib.CktElement_Get_BusNames))

    @BusNames.setter
    def BusNames(self, Value: List[AnyStr]):
        self.CheckForError(self._set_string_array(self._lib.CktElement_Set_BusNames, Value))

    @property
    def CplxSeqCurrents(self) -> Float64ArrayOrComplexArray:
        '''Complex double array of Sequence Currents for all conductors of all terminals of active circuit element.'''
        self.CheckForError(self._lib.CktElement_Get_CplxSeqCurrents_GR())
        return self._get_complex128_gr_array()

    @property
    def CplxSeqVoltages(self) -> Float64ArrayOrComplexArray:
        '''Complex double array of Sequence Voltage for all terminals of active circuit element.'''
        self.CheckForError(self._lib.CktElement_Get_CplxSeqVoltages_GR())
        return self._get_complex128_gr_array()

    @property
    def Currents(self) -> Float64ArrayOrComplexArray:
        '''Complex array of currents into each conductor of each terminal'''
        self.CheckForError(self._lib.CktElement_Get_Currents_GR())
        return self._get_complex128_gr_array()

    @property
    def CurrentsMagAng(self) -> Float64Array:
        '''Currents in magnitude, angle (degrees) format as a array of doubles.'''
        self.CheckForError(self._lib.CktElement_Get_CurrentsMagAng_GR())
        return self._get_float64_gr_array()

    @property
    def DisplayName(self) -> str:
        '''Display name of the object (not necessarily unique)'''
        return self._get_string(self.CheckForError(self._lib.CktElement_Get_DisplayName()))

    @DisplayName.setter
    def DisplayName(self, Value: AnyStr):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.CktElement_Set_DisplayName(Value))

    @property
    def EmergAmps(self) -> float:
        '''Emergency Ampere Rating for PD elements'''
        return self.CheckForError(self._lib.CktElement_Get_EmergAmps())

    @EmergAmps.setter
    def EmergAmps(self, Value: float):
        self.CheckForError(self._lib.CktElement_Set_EmergAmps(Value))

    @property
    def Enabled(self) -> bool:
        '''Boolean indicating that element is currently in the circuit.'''
        return self.CheckForError(self._lib.CktElement_Get_Enabled()) != 0

    @Enabled.setter
    def Enabled(self, Value: bool):
        self.CheckForError(self._lib.CktElement_Set_Enabled(Value))

    @property
    def EnergyMeter(self) -> str:
        '''Name of the Energy Meter this element is assigned to.'''
        return self._get_string(self.CheckForError(self._lib.CktElement_Get_EnergyMeter()))

    @property
    def GUID(self) -> str:
        '''globally unique identifier for this object'''
        return self._get_string(self.CheckForError(self._lib.CktElement_Get_GUID()))

    @property
    def Handle(self) -> int:
        '''Pointer to this object'''
        return self.CheckForError(self._lib.CktElement_Get_Handle())

    @property
    def HasOCPDevice(self) -> bool:
        '''True if a recloser, relay, or fuse controlling this ckt element. OCP = Overcurrent Protection '''
        return self.CheckForError(self._lib.CktElement_Get_HasOCPDevice()) != 0

    @property
    def HasSwitchControl(self) -> bool:
        '''This element has a SwtControl attached.'''
        return self.CheckForError(self._lib.CktElement_Get_HasSwitchControl()) != 0

    @property
    def HasVoltControl(self) -> bool:
        '''This element has a CapControl or RegControl attached.'''
        return self.CheckForError(self._lib.CktElement_Get_HasVoltControl()) != 0

    @property
    def Losses(self) -> Float64ArrayOrSimpleComplex:
        '''Total losses in the element: two-element double array (complex), in VA (watts, vars)'''
        self.CheckForError(self._lib.CktElement_Get_Losses_GR())
        return self._get_complex128_gr_simple()

    @property
    def Name(self) -> str:
        '''Full Name of Active Circuit Element'''
        return self._get_string(self.CheckForError(self._lib.CktElement_Get_Name()))

    @property
    def NodeOrder(self) -> Int32Array:
        '''Array of integer containing the node numbers (representing phases, for example) for each conductor of each terminal. '''
        self.CheckForError(self._lib.CktElement_Get_NodeOrder_GR())
        return self._get_int32_gr_array()

    @property
    def NormalAmps(self) -> float:
        '''Normal ampere rating for PD Elements'''
        return self.CheckForError(self._lib.CktElement_Get_NormalAmps())

    @NormalAmps.setter
    def NormalAmps(self, Value: float):
        self.CheckForError(self._lib.CktElement_Set_NormalAmps(Value))

    @property
    def NumConductors(self) -> int:
        '''Number of Conductors per Terminal'''
        return self.CheckForError(self._lib.CktElement_Get_NumConductors())

    @property
    def NumControls(self) -> int:
        '''
        (read-only) Number of controls connected to this device. 
        Use to determine valid range for index into Controller array.
        '''
        return self.CheckForError(self._lib.CktElement_Get_NumControls())

    @property
    def NumPhases(self) -> int:
        '''Number of Phases'''
        return self.CheckForError(self._lib.CktElement_Get_NumPhases())

    @property
    def NumProperties(self) -> int:
        '''Number of Properties this Circuit Element.'''
        return self.CheckForError(self._lib.CktElement_Get_NumProperties())

    @property
    def NumTerminals(self) -> int:
        '''Number of Terminals this Circuit Element'''
        return self.CheckForError(self._lib.CktElement_Get_NumTerminals())

    @property
    def OCPDevIndex(self) -> int:
        '''Index into Controller list of OCP Device controlling this CktElement'''
        return self.CheckForError(self._lib.CktElement_Get_OCPDevIndex())

    @property
    def OCPDevType(self) -> OCPDevTypeEnum:
        '''0=None; 1=Fuse; 2=Recloser; 3=Relay;  Type of OCP controller device'''
        return OCPDevTypeEnum(self.CheckForError(self._lib.CktElement_Get_OCPDevType()))

    @property
    def PhaseLosses(self) -> Float64ArrayOrComplexArray:
        '''Complex array of losses (kVA) by phase'''
        self.CheckForError(self._lib.CktElement_Get_PhaseLosses_GR())
        return self._get_complex128_gr_array()

    @property
    def Powers(self) -> Float64ArrayOrComplexArray:
        '''Complex array of powers (kVA) into each conductor of each terminal'''
        self.CheckForError(self._lib.CktElement_Get_Powers_GR())
        return self._get_complex128_gr_array()

    @property
    def Residuals(self) -> Float64Array:
        '''Residual currents for each terminal: (magnitude, angle in degrees)'''
        self.CheckForError(self._lib.CktElement_Get_Residuals_GR())
        return self._get_float64_gr_array()

    @property
    def SeqCurrents(self) -> Float64Array:
        '''Double array of symmetrical component currents (magnitudes only) into each 3-phase terminal'''
        self.CheckForError(self._lib.CktElement_Get_SeqCurrents_GR())
        return self._get_float64_gr_array()

    @property
    def SeqPowers(self) -> Float64ArrayOrComplexArray:
        '''Complex array of sequence powers (kW, kvar) into each 3-phase teminal'''
        self.CheckForError(self._lib.CktElement_Get_SeqPowers_GR())
        return self._get_complex128_gr_array()

    @property
    def SeqVoltages(self) -> Float64Array:
        '''Double array of symmetrical component voltages (magnitudes only) at each 3-phase terminal'''
        self.CheckForError(self._lib.CktElement_Get_SeqVoltages_GR())
        return self._get_float64_gr_array()

    @property
    def Voltages(self) -> Float64ArrayOrComplexArray:
        '''Complex array of voltages at terminals'''
        self.CheckForError(self._lib.CktElement_Get_Voltages_GR())
        return self._get_complex128_gr_array()

    @property
    def VoltagesMagAng(self) -> Float64Array:
        '''Voltages at each conductor in magnitude, angle form as array of doubles.'''
        self.CheckForError(self._lib.CktElement_Get_VoltagesMagAng_GR())
        return self._get_float64_gr_array()

    @property
    def Yprim(self) -> Float64ArrayOrComplexArray:
        '''YPrim matrix, column order, complex numbers'''
        self.CheckForError(self._lib.CktElement_Get_Yprim_GR())
        return self._get_complex128_gr_array()

    @property
    def IsIsolated(self) -> bool:
        '''
        Returns true if the current active element is isolated.
        Note that this only fetches the current value. See also the Topology interface.

        (API Extension)
        '''
        return self.CheckForError(self._lib.CktElement_Get_IsIsolated()) != 0

    @property
    def TotalPowers(self) -> Float64ArrayOrComplexArray:
        '''Returns an array with the total powers (complex, kVA) at ALL terminals of the active circuit element.'''
        self.CheckForError(self._lib.CktElement_Get_TotalPowers_GR())
        return self._get_complex128_gr_array()

    @property
    def NodeRef(self) -> Int32Array:
        '''Array of integers, a copy of the internal NodeRef of the CktElement.'''
        self._lib.CktElement_Get_NodeRef_GR()
        return self._get_int32_gr_array()

    def __iter__(self):
        for index in range(self.CheckForError(self._lib.Circuit_Get_NumCktElements())):
            self.CheckForError(self._lib.Circuit_SetCktElementIndex(index))
            yield self

    def __getitem__(self, index):
        if isinstance(index, int):
            # index is zero based, pass it directly
            self.CheckForError(self._lib.Circuit_SetCktElementIndex(index))
        else:
            if type(index) is not bytes:
                index = index.encode(self._api_util.codec)

            self.CheckForError(self._lib.Circuit_SetCktElementName(index))
            
        return self

    def __call__(self, index):
        return self.__getitem__(index)

