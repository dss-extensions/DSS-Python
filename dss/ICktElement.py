# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from __future__ import annotations
from ._cffi_api_util import Base
from .IDSSProperty import IDSSProperty
from ._types import Float64Array, Int32Array, Float64ArrayOrComplexArray, Float64ArrayOrSimpleComplex
from typing import List, AnyStr, Tuple, Iterator
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
        '''
        Close the specified terminal and phase, if non-zero, or all conductors at the terminal.

        Original COM help: https://opendss.epri.com/Close1.html
        '''
        self._check_for_error(self._lib.CktElement_Close(Term, Phs))

    def Controller(self, idx: int) -> str:
        '''Full name of the i-th controller attached to this element. Ex: str = Controller(2).  See NumControls to determine valid index range'''
        return self._get_string(self._check_for_error(self._lib.CktElement_Get_Controller(idx)))

    def Variable(self, MyVarName: AnyStr) -> Tuple[float, int]:
        '''
        Returns (value, Code). For PCElement, get the value of a variable by name. If Code>0 Then no variable by this name or not a PCelement.

        Original COM help: https://opendss.epri.com/Variable.html
        '''
        if not isinstance(MyVarName, bytes):
            MyVarName = MyVarName.encode(self._api_util.codec)

        Code = self._api_util.ffi.new('int32_t*')
        result = self._check_for_error(self._lib.CktElement_Get_Variable(MyVarName, Code))
        # if Code[0] == 1:
        #     raise DssException('No variable by this name or not a PCelement')
        return result, Code[0]
    

    def Variablei(self, Idx: int) -> Tuple[float, int]:
        '''
        Returns (value, Code). For PCElement, get the value of a variable by integer index. If Code>0 Then no variable by this index or not a PCelement.

        Original COM help: https://opendss.epri.com/Variablei.html
        '''
        Code = self._api_util.ffi.new('int32_t*')
        result = self._check_for_error(self._lib.CktElement_Get_Variablei(Idx, Code))
        # if Code[0] == 1:
        #     raise DssException('Invalid variable index or not a PCelement')
        return result, Code[0]

    # for compatibility with OpenDSS 9.4.1.1
    VariableByIndex = Variablei
    VariableByName = Variable

    def setVariableByIndex(self, Idx: int, Value: float) -> int:
        Code = self._api_util.ffi.new('int32_t*')
        self._check_for_error(self._lib.CktElement_Set_Variablei(Idx, Code, Value))
        # if Code[0] == 1:
        #     raise DSSException('Invalid variable index or not a PCelement')
        return Code[0]

    def setVariableByName(self, Idx: AnyStr, Value: float) -> int:
        Code = self._api_util.ffi.new('int32_t*')
        self._check_for_error(self._lib.CktElement_Set_Variable(Idx, Code, Value))
        # if Code[0] == 1:
        #     raise DSSException('Invalid variable index or not a PCelement')
        return Code[0]

    def IsOpen(self, Term: int, Phs: int) -> bool:
        return self._check_for_error(self._lib.CktElement_IsOpen(Term, Phs)) != 0

    def Open(self, Term: int, Phs: int):
        '''
        Open the specified terminal and phase, if non-zero, or all conductors at the terminal.

        Original COM help: https://opendss.epri.com/Open1.html
        '''
        self._check_for_error(self._lib.CktElement_Open(Term, Phs))

    @property
    def AllPropertyNames(self) -> List[str]:
        '''
        Array containing all property names of the active device.

        Original COM help: https://opendss.epri.com/AllPropertyNames.html
        '''
        return self._check_for_error(self._get_string_array(self._lib.CktElement_Get_AllPropertyNames))

    @property
    def AllVariableNames(self) -> List[str]:
        '''
        Array of strings listing all the published state variable names.
        Valid only for PCElements.

        Original COM help: https://opendss.epri.com/AllVariableNames.html
        '''
        return self._check_for_error(self._get_string_array(self._lib.CktElement_Get_AllVariableNames))

    @property
    def AllVariableValues(self) -> Float64Array:
        '''
        Array of doubles. Values of state variables of active element if PC element.
        Valid only for PCElements.

        Original COM help: https://opendss.epri.com/AllVariableValues.html
        '''
        self._check_for_error(self._lib.CktElement_Get_AllVariableValues_GR())
        return self._get_float64_gr_array()

    @property
    def BusNames(self) -> List[str]:
        '''
        Bus definitions to which each terminal is connected.

        Original COM help: https://opendss.epri.com/BusNames.html
        '''
        return self._check_for_error(self._get_string_array(self._lib.CktElement_Get_BusNames))

    @BusNames.setter
    def BusNames(self, Value: List[AnyStr]):
        self._check_for_error(self._set_string_array(self._lib.CktElement_Set_BusNames, Value))

    @property
    def CplxSeqCurrents(self) -> Float64ArrayOrComplexArray:
        '''
        Complex double array of Sequence Currents for all conductors of all terminals of active circuit element.

        Original COM help: https://opendss.epri.com/CplxSeqCurrents.html
        '''
        self._check_for_error(self._lib.CktElement_Get_CplxSeqCurrents_GR())
        return self._get_complex128_gr_array()

    @property
    def CplxSeqVoltages(self) -> Float64ArrayOrComplexArray:
        '''
        Complex double array of Sequence Voltage for all terminals of active circuit element.

        Original COM help: https://opendss.epri.com/CplxSeqVoltages1.html
        '''
        self._check_for_error(self._lib.CktElement_Get_CplxSeqVoltages_GR())
        return self._get_complex128_gr_array()

    @property
    def Currents(self) -> Float64ArrayOrComplexArray:
        '''
        Complex array of currents into each conductor of each terminal

        Original COM help: https://opendss.epri.com/Currents1.html
        '''
        self._check_for_error(self._lib.CktElement_Get_Currents_GR())
        return self._get_complex128_gr_array()

    @property
    def CurrentsMagAng(self) -> Float64Array:
        '''
        Currents in magnitude, angle (degrees) format as a array of doubles.

        Original COM help: https://opendss.epri.com/CurrentsMagAng.html
        '''
        self._check_for_error(self._lib.CktElement_Get_CurrentsMagAng_GR())
        return self._get_float64_gr_array()

    @property
    def DisplayName(self) -> str:
        '''
        Display name of the object (not necessarily unique)

        Original COM help: https://opendss.epri.com/DisplayName.html
        '''
        return self._get_string(self._check_for_error(self._lib.CktElement_Get_DisplayName()))

    @DisplayName.setter
    def DisplayName(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.CktElement_Set_DisplayName(Value))

    @property
    def EmergAmps(self) -> float:
        '''
        Emergency Ampere Rating for PD elements

        Original COM help: https://opendss.epri.com/EmergAmps.html
        '''
        return self._check_for_error(self._lib.CktElement_Get_EmergAmps())

    @EmergAmps.setter
    def EmergAmps(self, Value: float):
        self._check_for_error(self._lib.CktElement_Set_EmergAmps(Value))

    @property
    def Enabled(self) -> bool:
        '''
        Boolean indicating that element is currently in the circuit.

        Original COM help: https://opendss.epri.com/Enabled.html
        '''
        return self._check_for_error(self._lib.CktElement_Get_Enabled()) != 0

    @Enabled.setter
    def Enabled(self, Value: bool):
        self._check_for_error(self._lib.CktElement_Set_Enabled(Value))

    @property
    def EnergyMeter(self) -> str:
        '''
        Name of the Energy Meter this element is assigned to.

        Original COM help: https://opendss.epri.com/EnergyMeter.html
        '''
        return self._get_string(self._check_for_error(self._lib.CktElement_Get_EnergyMeter()))

    @property
    def GUID(self) -> str:
        '''
        globally unique identifier for this object

        Original COM help: https://opendss.epri.com/GUID.html
        '''
        return self._get_string(self._check_for_error(self._lib.CktElement_Get_GUID()))

    @property
    def Handle(self) -> int:
        '''
        Pointer to this object

        Original COM help: https://opendss.epri.com/Handle.html
        '''
        return self._check_for_error(self._lib.CktElement_Get_Handle())

    @property
    def HasOCPDevice(self) -> bool:
        '''
        True if a recloser, relay, or fuse controlling this ckt element. OCP = Overcurrent Protection 

        Original COM help: https://opendss.epri.com/HasOCPDevice.html
        '''
        return self._check_for_error(self._lib.CktElement_Get_HasOCPDevice()) != 0

    @property
    def HasSwitchControl(self) -> bool:
        '''
        This element has a SwtControl attached.

        Original COM help: https://opendss.epri.com/HasSwitchControl.html
        '''
        return self._check_for_error(self._lib.CktElement_Get_HasSwitchControl()) != 0

    @property
    def HasVoltControl(self) -> bool:
        '''
        This element has a CapControl or RegControl attached.

        Original COM help: https://opendss.epri.com/HasVoltControl.html
        '''
        return self._check_for_error(self._lib.CktElement_Get_HasVoltControl()) != 0

    @property
    def Losses(self) -> Float64ArrayOrSimpleComplex:
        '''
        Total losses in the element: two-element double array (complex), in VA (watts, vars)

        Original COM help: https://opendss.epri.com/Losses1.html
        '''
        self._check_for_error(self._lib.CktElement_Get_Losses_GR())
        return self._get_complex128_gr_simple()

    @property
    def Name(self) -> str:
        '''
        Full Name of Active Circuit Element

        Original COM help: https://opendss.epri.com/Name4.html
        '''
        return self._get_string(self._check_for_error(self._lib.CktElement_Get_Name()))

    @property
    def NodeOrder(self) -> Int32Array:
        '''
        Array of integer containing the node numbers (representing phases, for example) for each conductor of each terminal. 

        Original COM help: https://opendss.epri.com/NodeOrder.html
        '''
        self._check_for_error(self._lib.CktElement_Get_NodeOrder_GR())
        return self._get_int32_gr_array()

    @property
    def NormalAmps(self) -> float:
        '''
        Normal ampere rating for PD Elements

        Original COM help: https://opendss.epri.com/NormalAmps.html
        '''
        return self._check_for_error(self._lib.CktElement_Get_NormalAmps())

    @NormalAmps.setter
    def NormalAmps(self, Value: float):
        self._check_for_error(self._lib.CktElement_Set_NormalAmps(Value))

    @property
    def NumConductors(self) -> int:
        '''
        Number of Conductors per Terminal

        Original COM help: https://opendss.epri.com/NumConductors.html
        '''
        return self._check_for_error(self._lib.CktElement_Get_NumConductors())

    @property
    def NumControls(self) -> int:
        '''
        Number of controls connected to this device. 
        Use to determine valid range for index into Controller array.

        Original COM help: https://opendss.epri.com/NumControls.html
        '''
        return self._check_for_error(self._lib.CktElement_Get_NumControls())

    @property
    def NumPhases(self) -> int:
        '''
        Number of Phases

        Original COM help: https://opendss.epri.com/NumPhases.html
        '''
        return self._check_for_error(self._lib.CktElement_Get_NumPhases())

    @property
    def NumProperties(self) -> int:
        '''
        Number of Properties this Circuit Element.

        Original COM help: https://opendss.epri.com/NumProperties.html
        '''
        return self._check_for_error(self._lib.CktElement_Get_NumProperties())

    @property
    def NumTerminals(self) -> int:
        '''
        Number of Terminals this Circuit Element

        Original COM help: https://opendss.epri.com/NumTerminals.html
        '''
        return self._check_for_error(self._lib.CktElement_Get_NumTerminals())

    @property
    def OCPDevIndex(self) -> int:
        '''
        Index into Controller list of OCP Device controlling this CktElement

        Original COM help: https://opendss.epri.com/OCPDevIndex.html
        '''
        return self._check_for_error(self._lib.CktElement_Get_OCPDevIndex())

    @property
    def OCPDevType(self) -> OCPDevTypeEnum:
        '''
        0=None; 1=Fuse; 2=Recloser; 3=Relay;  Type of OCP controller device

        Original COM help: https://opendss.epri.com/OCPDevType.html
        '''
        return OCPDevTypeEnum(self._check_for_error(self._lib.CktElement_Get_OCPDevType()))

    @property
    def PhaseLosses(self) -> Float64ArrayOrComplexArray:
        '''
        Complex array of losses (kVA) by phase

        Original COM help: https://opendss.epri.com/PhaseLosses.html
        '''
        self._check_for_error(self._lib.CktElement_Get_PhaseLosses_GR())
        return self._get_complex128_gr_array()

    @property
    def Powers(self) -> Float64ArrayOrComplexArray:
        '''
        Complex array of powers (kVA) into each conductor of each terminal

        Original COM help: https://opendss.epri.com/Powers.html
        '''
        self._check_for_error(self._lib.CktElement_Get_Powers_GR())
        return self._get_complex128_gr_array()

    @property
    def Residuals(self) -> Float64Array:
        '''
        Residual currents for each terminal: (magnitude, angle in degrees)

        Original COM help: https://opendss.epri.com/Residuals.html
        '''
        self._check_for_error(self._lib.CktElement_Get_Residuals_GR())
        return self._get_float64_gr_array()

    @property
    def SeqCurrents(self) -> Float64Array:
        '''
        Double array of symmetrical component currents (magnitudes only) into each 3-phase terminal

        Original COM help: https://opendss.epri.com/SeqCurrents.html
        '''
        self._check_for_error(self._lib.CktElement_Get_SeqCurrents_GR())
        return self._get_float64_gr_array()

    @property
    def SeqPowers(self) -> Float64ArrayOrComplexArray:
        '''
        Complex array of sequence powers (kW, kvar) into each 3-phase terminal

        Original COM help: https://opendss.epri.com/SeqPowers.html
        '''
        self._check_for_error(self._lib.CktElement_Get_SeqPowers_GR())
        return self._get_complex128_gr_array()

    @property
    def SeqVoltages(self) -> Float64Array:
        '''
        Double array of symmetrical component voltages (magnitudes only) at each 3-phase terminal

        Original COM help: https://opendss.epri.com/SeqVoltages1.html
        '''
        self._check_for_error(self._lib.CktElement_Get_SeqVoltages_GR())
        return self._get_float64_gr_array()

    @property
    def Voltages(self) -> Float64ArrayOrComplexArray:
        '''
        Complex array of voltages at terminals

        Original COM help: https://opendss.epri.com/Voltages1.html
        '''
        self._check_for_error(self._lib.CktElement_Get_Voltages_GR())
        return self._get_complex128_gr_array()

    @property
    def VoltagesMagAng(self) -> Float64Array:
        '''
        Voltages at each conductor in magnitude, angle form as array of doubles.

        Original COM help: https://opendss.epri.com/VoltagesMagAng.html
        '''
        self._check_for_error(self._lib.CktElement_Get_VoltagesMagAng_GR())
        return self._get_float64_gr_array()

    @property
    def Yprim(self) -> Float64ArrayOrComplexArray:
        '''
        YPrim matrix, column order, complex numbers

        Original COM help: https://opendss.epri.com/Yprim.html
        '''
        self._check_for_error(self._lib.CktElement_Get_Yprim_GR())
        return self._get_complex128_gr_array()

    @property
    def IsIsolated(self) -> bool:
        '''
        Returns true if the current active element is isolated.
        Note that this only fetches the current value. See also the Topology interface.

        **(API Extension)**
        '''
        return self._check_for_error(self._lib.CktElement_Get_IsIsolated()) != 0

    @property
    def TotalPowers(self) -> Float64ArrayOrComplexArray:
        '''
        Returns an array with the total powers (complex, kVA) at ALL terminals of the active circuit element.

        Original COM help: https://opendss.epri.com/TotalPowers.html
        '''
        self._check_for_error(self._lib.CktElement_Get_TotalPowers_GR())
        return self._get_complex128_gr_array()

    @property
    def NodeRef(self) -> Int32Array:
        '''
        Array of integers, a copy of the internal NodeRef of the CktElement.
        
        **(API Extension)**
        '''
        self._lib.CktElement_Get_NodeRef_GR()
        return self._get_int32_gr_array()

    def __iter__(self) -> Iterator[ICktElement]:
        for index in range(self._check_for_error(self._lib.Circuit_Get_NumCktElements())):
            self._check_for_error(self._lib.Circuit_SetCktElementIndex(index))
            yield self

    def __getitem__(self, index) -> ICktElement:
        if isinstance(index, int):
            # index is zero based, pass it directly
            self._check_for_error(self._lib.Circuit_SetCktElementIndex(index))
        else:
            if not isinstance(index, bytes):
                index = index.encode(self._api_util.codec)

            self._check_for_error(self._lib.Circuit_SetCktElementName(index))
            
        return self

    def __call__(self, index) -> ICktElement:
        return self.__getitem__(index)

