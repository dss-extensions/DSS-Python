# A compatibility layer for DSS C-API that mimics EPRI's OpenDSS COM interface.
# Copyright (c) 2016-2025 Paulo Meira
# Copyright (c) 2018-2025 DSS-Extensions contributors
from __future__ import annotations
from ._cffi_api_util import Base
from .IDSSProperty import IDSSProperty
from ._types import Float64Array, Int32Array, Int32Matrix, ComplexArray, Complex
from typing import List, AnyStr, Tuple, Iterator
from .enums import OCPDevType as OCPDevTypeEnum

class ICktElement(Base):
    '''
    The (Active)CktElement interface allows accessing some common properties and 
    methods shared across circuit elements in the DSS engine.

    Users can enable specific elements by name or use the dedicated interface 
    (e.g. use `Loads.Name`, `Transformers.First/Next`) and access the properties here.

    If you are new to OpenDSS/AltDSS and this classic interface, please read the following document
    for an overview of the "active element" paradigm used by COM and the classic APIs:
        
    https://dss-extensions.org/classic_api.html#the-active-paradigm
    '''

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
        self._lib.CktElement_Close(Term, Phs)

    def Controller(self, idx: int) -> str:
        '''Full name of the i-th controller attached to this element. Ex: str = Controller(2).  See NumControls to determine valid index range'''
        return self._lib.CktElement_Get_Controller(idx)

    def Variable(self, MyVarName: AnyStr) -> Tuple[float, int]:
        '''
        Returns (value, Code). For PCElement, get the value of a variable by name. If Code>0 Then no variable by this name or not a PCelement.

        Original COM help: https://opendss.epri.com/Variable.html
        '''
        if not isinstance(MyVarName, bytes):
            MyVarName = MyVarName.encode(self._api_util.codec)

        Code = self._api_util.ffi.new('int32_t*')
        result = self._lib.CktElement_Get_Variable(MyVarName, Code)
        # if Code[0] == 1:
        #     raise DssException('No variable by this name or not a PCelement')
        return result, Code[0]
    

    def Variablei(self, Idx: int) -> Tuple[float, int]:
        '''
        Returns (value, Code). For PCElement, get the value of a variable by integer index. If Code>0 Then no variable by this index or not a PCelement.

        Original COM help: https://opendss.epri.com/Variablei.html
        '''
        Code = self._api_util.ffi.new('int32_t*')
        result = self._lib.CktElement_Get_Variablei(Idx, Code)
        # if Code[0] == 1:
        #     raise DssException('Invalid variable index or not a PCelement')
        return result, Code[0]

    # for compatibility with OpenDSS 9.4.1.1
    VariableByIndex = Variablei
    VariableByName = Variable

    def setVariableByIndex(self, Idx: int, Value: float) -> int:
        Code = self._api_util.ffi.new('int32_t*')
        self._lib.CktElement_Set_Variablei(Idx, Code, Value)
        # if Code[0] == 1:
        #     raise DSSException('Invalid variable index or not a PCelement')
        return Code[0]

    def setVariableByName(self, Idx: AnyStr, Value: float) -> int:
        Code = self._api_util.ffi.new('int32_t*')
        self._lib.CktElement_Set_Variable(Idx, Code, Value)
        # if Code[0] == 1:
        #     raise DSSException('Invalid variable index or not a PCelement')
        return Code[0]

    def IsOpen(self, Term: int, Phs: int = 0) -> bool:
        '''
        Indicates if the specified terminal and, optionally, a specific phase conductor is open.

        Provide zero in the `Phs` argument to check if any conductor of the terminal `Term` is open.

        Provide a non-zero phase number in `Phs` to check if a specific phase conductor is open.

        Original COM help: https://opendss.epri.com/IsOpen.html
        '''
        return self._lib.CktElement_IsOpen(Term, Phs)

    def Open(self, Term: int, Phs: int):
        '''
        Open the specified terminal and phase, if non-zero, or all conductors at the terminal.

        Original COM help: https://opendss.epri.com/Open1.html
        '''
        self._lib.CktElement_Open(Term, Phs)

    @property
    def AllPropertyNames(self) -> List[str]:
        '''
        Array containing all property names of the active device.

        Original COM help: https://opendss.epri.com/AllPropertyNames.html
        '''
        return self._lib.CktElement_Get_AllPropertyNames()

    @property
    def AllVariableNames(self) -> List[str]:
        '''
        Array of strings listing all the published state variable names.
        Valid only for PCElements.

        Original COM help: https://opendss.epri.com/AllVariableNames.html
        '''
        return self._lib.CktElement_Get_AllVariableNames()

    @property
    def AllVariableValues(self) -> Float64Array:
        '''
        Array of doubles. Values of state variables of active element if PC element.
        Valid only for PCElements.

        Original COM help: https://opendss.epri.com/AllVariableValues.html
        '''
        return self._lib.CktElement_Get_AllVariableValues_GR()

    def _get_BusNames(self, removeNodes: bool = False) -> List[str]:
        '''
        Bus definitions to which each terminal is connected.

        The `removeNodes` argument is an **API Extension**. Use it to get only the bus names, 
        without the connection/node specification, if present.

        Original COM help: https://opendss.epri.com/BusNames.html
        '''
        return self._lib.CktElement_Get_BusNames(removeNodes)

    def _set_BusNames(self, Value: List[AnyStr]):
        self._set_string_array(self._lib.CktElement_Set_BusNames, Value)

    BusNames = property(_get_BusNames, _set_BusNames) # type: List[str]
    '''
    Bus definitions to which each terminal is connected.

    In the getter function (`_get_BusNames`), the `removeNodes` argument is an **API Extension**.
    Use it to get only the bus names, without the connection/node specification, if present.

    Original COM help: https://opendss.epri.com/BusNames.html
    '''

    @property
    def CplxSeqCurrents(self) -> ComplexMatrix:
        '''
        Complex double array of Sequence Currents for all conductors of all terminals of active circuit element.

        Original COM help: https://opendss.epri.com/CplxSeqCurrents.html
        '''
        return self._lib.CktElement_Get_CplxSeqCurrents_GR()

    @property
    def CplxSeqVoltages(self) -> ComplexMatrix:
        '''
        Complex double array of Sequence Voltage for all terminals of active circuit element.

        Original COM help: https://opendss.epri.com/CplxSeqVoltages1.html
        '''
        return self._lib.CktElement_Get_CplxSeqVoltages_GR()

    @property
    def Currents(self) -> ComplexMatrix:
        '''
        Complex array of currents into each conductor of each terminal

        Original COM help: https://opendss.epri.com/Currents1.html
        '''
        return self._lib.CktElement_Get_Currents_GR()

    @property
    def CurrentsMagAng(self) -> Float64Matrix:
        '''
        Currents in magnitude, angle (degrees) format as an array of doubles.

        Original COM help: https://opendss.epri.com/CurrentsMagAng.html
        '''
        return self._lib.CktElement_Get_CurrentsMagAng_GR()

    @property
    def DisplayName(self) -> str:
        '''
        Display name of the object (not necessarily unique)

        Original COM help: https://opendss.epri.com/DisplayName.html
        '''
        return self._lib.CktElement_Get_DisplayName()

    @DisplayName.setter
    def DisplayName(self, Value: AnyStr):
        self._lib.CktElement_Set_DisplayName(Value)

    @property
    def EmergAmps(self) -> float:
        '''
        Emergency Ampere Rating for PD elements

        Original COM help: https://opendss.epri.com/EmergAmps.html
        '''
        return self._lib.CktElement_Get_EmergAmps()

    @EmergAmps.setter
    def EmergAmps(self, Value: float):
        self._lib.CktElement_Set_EmergAmps(Value)

    @property
    def Enabled(self) -> bool:
        '''
        Boolean indicating that element is currently in the circuit.

        Original COM help: https://opendss.epri.com/Enabled.html
        '''
        return self._lib.CktElement_Get_Enabled()

    @Enabled.setter
    def Enabled(self, Value: bool):
        self._lib.CktElement_Set_Enabled(Value)

    @property
    def EnergyMeter(self) -> str:
        '''
        Name of the Energy Meter this element is assigned to.

        *Requires an energy meter with an updated zone.*

        Original COM help: https://opendss.epri.com/EnergyMeter.html
        '''
        return self._lib.CktElement_Get_EnergyMeter()

    @property
    def GUID(self) -> str:
        '''
        GUID/UUID for this object.

        Original COM help: https://opendss.epri.com/GUID.html
        '''
        return self._lib.CktElement_Get_GUID()

    @property
    def Handle(self) -> int:
        '''
        Index of this element into the circuit's element list.

        Original COM help: https://opendss.epri.com/Handle.html
        '''
        return self._lib.CktElement_Get_Handle()

    @property
    def HasOCPDevice(self) -> bool:
        '''
        True if a recloser, relay, or fuse controlling this ckt element. OCP = Overcurrent Protection 

        Original COM help: https://opendss.epri.com/HasOCPDevice.html
        '''
        return self._lib.CktElement_Get_HasOCPDevice()

    @property
    def HasSwitchControl(self) -> bool:
        '''
        True if this element has a SwtControl attached.

        Original COM help: https://opendss.epri.com/HasSwitchControl.html
        '''
        return self._lib.CktElement_Get_HasSwitchControl()

    @property
    def HasVoltControl(self) -> bool:
        '''
        True if this element has a CapControl or RegControl attached.

        Original COM help: https://opendss.epri.com/HasVoltControl.html
        '''
        return self._lib.CktElement_Get_HasVoltControl()

    @property
    def Losses(self) -> Complex:
        '''
        Total losses in the element: two-element double array (complex), in VA (watts, vars)

        Original COM help: https://opendss.epri.com/Losses1.html
        '''
        return self._lib.CktElement_Get_Losses_GR()

    @property
    def AllLosses(self) -> Complex:
        '''
        Complex array with the losses by type (total losses, load losses, no-load losses), in VA, for the active circuit element.

        Added in May 2025. Same as `LossesByType` introduced for Transformers in AltDSS/DSS C-API in May 2019.
        '''
        return self._lib.CktElement_Get_AllLosses_GR()

    @property
    def Name(self) -> str:
        '''
        Full Name of Active Circuit Element

        Original COM help: https://opendss.epri.com/Name4.html
        '''
        return self._lib.CktElement_Get_Name()

    @property
    def NodeOrder(self) -> Int32Matrix:
        '''
        Array of integer containing the node numbers (representing phases, for example) for each conductor of each terminal. 

        Be sure to run a solution to initialize the values after the circuit is created or modified.

        Original COM help: https://opendss.epri.com/NodeOrder.html
        '''
        return self._lib.CktElement_Get_NodeOrder_GR()

    @property
    def NormalAmps(self) -> float:
        '''
        Normal ampere rating for PD Elements

        Original COM help: https://opendss.epri.com/NormalAmps.html
        '''
        return self._lib.CktElement_Get_NormalAmps()

    @NormalAmps.setter
    def NormalAmps(self, Value: float):
        self._lib.CktElement_Set_NormalAmps(Value)

    @property
    def NumConductors(self) -> int:
        '''
        Number of Conductors per Terminal

        Original COM help: https://opendss.epri.com/NumConductors.html
        '''
        return self._lib.CktElement_Get_NumConductors()

    @property
    def NumControls(self) -> int:
        '''
        Number of controls connected to this device. 
        Use to determine valid range for index into Controller array.

        Original COM help: https://opendss.epri.com/NumControls.html
        '''
        return self._lib.CktElement_Get_NumControls()

    @property
    def NumPhases(self) -> int:
        '''
        Number of Phases

        Original COM help: https://opendss.epri.com/NumPhases.html
        '''
        return self._lib.CktElement_Get_NumPhases()

    @property
    def NumProperties(self) -> int:
        '''
        Number of Properties this Circuit Element.

        Original COM help: https://opendss.epri.com/NumProperties.html
        '''
        return self._lib.CktElement_Get_NumProperties()

    @property
    def NumTerminals(self) -> int:
        '''
        Number of terminals in this Circuit Element

        Original COM help: https://opendss.epri.com/NumTerminals.html
        '''
        return self._lib.CktElement_Get_NumTerminals()

    @property
    def OCPDevIndex(self) -> int:
        '''
        Index into Controller list of OCP Device controlling this CktElement

        Original COM help: https://opendss.epri.com/OCPDevIndex.html
        '''
        return self._lib.CktElement_Get_OCPDevIndex()

    @property
    def OCPDevType(self) -> OCPDevTypeEnum:
        '''
        0=None; 1=Fuse; 2=Recloser; 3=Relay;  Type of OCP controller device

        Original COM help: https://opendss.epri.com/OCPDevType.html
        '''
        return OCPDevTypeEnum(self._lib.CktElement_Get_OCPDevType())

    @property
    def PhaseLosses(self) -> ComplexArray:
        '''
        Complex array of losses (kVA) by phase

        Original COM help: https://opendss.epri.com/PhaseLosses.html
        '''
        return self._lib.CktElement_Get_PhaseLosses_GR()

    @property
    def Powers(self) -> ComplexArray:
        '''
        Complex array of powers (kVA) into each conductor of each terminal

        Original COM help: https://opendss.epri.com/Powers.html
        '''
        return self._lib.CktElement_Get_Powers_GR()

    @property
    def Residuals(self) -> Float64Matrix:
        '''
        Residual currents for each terminal: (magnitude, angle in degrees)

        Original COM help: https://opendss.epri.com/Residuals.html
        '''
        return self._lib.CktElement_Get_Residuals_GR()

    @property
    def SeqCurrents(self) -> Float64Matrix:
        '''
        Double array of symmetrical component currents (magnitudes only) into each 3-phase terminal

        Original COM help: https://opendss.epri.com/SeqCurrents.html
        '''
        return self._lib.CktElement_Get_SeqCurrents_GR()

    @property
    def SeqPowers(self) -> ComplexMatrix:
        '''
        Complex array of sequence powers (kW, kvar) into each 3-phase terminal

        Original COM help: https://opendss.epri.com/SeqPowers.html
        '''
        return self._lib.CktElement_Get_SeqPowers_GR()

    @property
    def SeqVoltages(self) -> Float64Matrix:
        '''
        Double array of symmetrical component voltages (magnitudes only) at each 3-phase terminal

        Original COM help: https://opendss.epri.com/SeqVoltages1.html
        '''
        return self._lib.CktElement_Get_SeqVoltages_GR()

    @property
    def Voltages(self) -> ComplexMatrix:
        '''
        Complex array of voltages at terminals

        Original COM help: https://opendss.epri.com/Voltages1.html
        '''
        return self._lib.CktElement_Get_Voltages_GR()

    @property
    def VoltagesMagAng(self) -> Float64Matrix:
        '''
        Voltages at each conductor in magnitude, angle form as array of doubles.

        Original COM help: https://opendss.epri.com/VoltagesMagAng.html
        '''
        return self._lib.CktElement_Get_VoltagesMagAng_GR()

    @property
    def Yprim(self) -> ComplexMatrix:
        '''
        YPrim matrix, column order, complex numbers

        Original COM help: https://opendss.epri.com/Yprim.html
        '''
        return self._lib.CktElement_Get_Yprim_GR()

    @property
    def YprimOrder(self) -> int:
        '''
        Order (size) of the active circuit element's primite Y matrix (Yprim), typically `NumConductors * NumTerminals`

        **(API Extension)**
        '''
        return self._lib.CktElement_Get_YprimOrder()

    @property
    def IsIsolated(self) -> bool:
        '''
        Returns true if the current active element is isolated.
        Note that this only fetches the current value. See also the Topology interface.

        **(API Extension)**
        '''
        return self._lib.CktElement_Get_IsIsolated()

    @property
    def TotalPowers(self) -> ComplexArray:
        '''
        Returns an array with the total powers (complex, kVA) at ALL terminals of the active circuit element.

        Original COM help: https://opendss.epri.com/TotalPowers.html
        '''
        return self._lib.CktElement_Get_TotalPowers_GR()

    @property
    def NodeRef(self) -> Int32Array:
        '''
        Array of integers, a copy of the internal NodeRef of the CktElement.
        
        Be sure to run a solution to initialize the values after the circuit is created or modified.

        **(API Extension)**
        '''
        return self._lib.CktElement_Get_NodeRef_GR()

    def __iter__(self) -> Iterator[ICktElement]:
        for index in range(self._lib.Circuit_Get_NumCktElements()):
            self._lib.Circuit_SetCktElementIndex(index)
            yield self

    def __getitem__(self, index) -> ICktElement:
        if isinstance(index, int):
            # index is zero based, pass it directly
            self._lib.Circuit_SetCktElementIndex(index)
        else:
            self._lib.Circuit_SetCktElementName(index)
            
        return self

    def __call__(self, index) -> ICktElement:
        return self.__getitem__(index)

