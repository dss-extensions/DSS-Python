# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2019-2024 Paulo Meira
# Copyright (c) 2019-2024 DSS-Extensions contributors
from ._cffi_api_util import Base
from typing import AnyStr

class IReduceCkt(Base):
    '''Circuit Reduction interface'''

    __slots__ = []

    @property
    def Zmag(self) -> float:
        '''
        Zmag (ohms) for Reduce Option for Z of short lines

        Original COM help: https://opendss.epri.com/Zmag.html
        '''
        return self._check_for_error(self._lib.ReduceCkt_Get_Zmag())
        
    @Zmag.setter
    def Zmag(self, Value: float):
        self._check_for_error(self._lib.ReduceCkt_Set_Zmag(Value))

    @property
    def KeepLoad(self) -> bool:
        '''
        Keep load flag for Reduction options that remove branches

        Original COM help: https://opendss.epri.com/KeepLoad.html
        '''
        return self._check_for_error(self._lib.ReduceCkt_Get_KeepLoad()) != 0
        
    @KeepLoad.setter
    def KeepLoad(self, Value: bool):
        self._check_for_error(self._lib.ReduceCkt_Set_KeepLoad(bool(Value)))

    @property
    def EditString(self) -> str:
        '''
        Edit String for RemoveBranches functions

        Original COM help: https://opendss.epri.com/EditString.html
        '''
        return self._get_string(self._check_for_error(self._lib.ReduceCkt_Get_EditString()))
        
    @EditString.setter
    def EditString(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
    
        self._check_for_error(self._lib.ReduceCkt_Set_EditString(Value))

    @property
    def StartPDElement(self) -> str:
        '''
        Start element for Remove Branch function

        Original COM help: https://opendss.epri.com/StartPDElement.html
        '''
        return self._get_string(self._check_for_error(self._lib.ReduceCkt_Get_StartPDElement()))
        
    @StartPDElement.setter
    def StartPDElement(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
            
        self._check_for_error(self._lib.ReduceCkt_Set_StartPDElement(Value))

    @property
    def EnergyMeter(self) -> str:
        '''
        Name of EnergyMeter to use for reduction

        Original COM help: https://opendss.epri.com/EnergyMeter1.html
        '''
        return self._get_string(self._check_for_error(self._lib.ReduceCkt_Get_EnergyMeter()))
    
    @EnergyMeter.setter
    def EnergyMeter(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)
    
        self._check_for_error(self._lib.ReduceCkt_Set_EnergyMeter(Value))

    def SaveCircuit(self, CktName: AnyStr):
        '''
        Save present (reduced) circuit
        Filename is listed in the Text Result interface
        '''
        if not isinstance(CktName, bytes):
            CktName = CktName.encode(self._api_util.codec)
        
        self._check_for_error(self._lib.ReduceCkt_SaveCircuit(CktName))

    def DoDefault(self):
        '''
        Do Default Reduction algorithm

        Original COM help: https://opendss.epri.com/DoDefault.html
        '''
        self._check_for_error(self._lib.ReduceCkt_DoDefault())

    def DoShortLines(self):
        '''
        Do ShortLines algorithm: Set Zmag first if you don't want the default

        Original COM help: https://opendss.epri.com/DoShortLines.html
        '''
        self._check_for_error(self._lib.ReduceCkt_DoShortLines())

    def DoDangling(self):
        '''
        Reduce Dangling Algorithm; branches with nothing connected

        Original COM help: https://opendss.epri.com/DoDangling.html
        '''
        self._check_for_error(self._lib.ReduceCkt_DoDangling())

    def DoLoopBreak(self):
        '''
        Break (disable) all the loops found in the active circuit.
        
        Disables one of the Line objects at the head of a loop to force the circuit to be radial.
        '''
        self._check_for_error(self._lib.ReduceCkt_DoLoopBreak())
    
    def DoParallelLines(self):
        '''
        Merge all parallel lines found in the circuit to facilitate its reduction.
        '''
        self._check_for_error(self._lib.ReduceCkt_DoParallelLines())
    
    def DoSwitches(self):
        '''
        Merge Line objects in which the IsSwitch property is true with the down-line Line object.
        '''
        self._check_for_error(self._lib.ReduceCkt_DoSwitches())
    
    def Do1phLaterals(self):
        '''
        Remove all 1-phase laterals in the active EnergyMeter's zone.
        
        Loads and other shunt elements are moved to the parent 3-phase bus.
        '''
        self._check_for_error(self._lib.ReduceCkt_Do1phLaterals())
    
    def DoBranchRemove(self):
        '''
        Remove (disable) all branches down-line from the active PDElement. 
        
        Circuit must have an EnergyMeter on this branch.
        If KeepLoad=Y (default), a new Load element is defined and kW, kvar are set to present power flow solution for the first element eliminated. 
        The EditString is applied to each new Load element defined. 
        '''
        self._check_for_error(self._lib.ReduceCkt_DoBranchRemove())
