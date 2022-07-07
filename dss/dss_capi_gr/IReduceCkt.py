'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2019-2020 Paulo Meira
'''
from .._cffi_api_util import Base

class IReduceCkt(Base):
    '''Circuit Reduction interface'''

    __slots__ = []

    @property
    def Zmag(self):
        '''Zmag (ohms) for Reduce Option for Z of short lines'''
        return self.CheckForError(self._lib.ReduceCkt_Get_Zmag())
        
    @Zmag.setter
    def Zmag(self, Value):
        self.CheckForError(self._lib.ReduceCkt_Set_Zmag(Value))

    @property
    def KeepLoad(self):
        '''Keep load flag (T/F) for Reduction options that remove branches'''
        return self.CheckForError(self._lib.ReduceCkt_Get_KeepLoad()) != 0
        
    @KeepLoad.setter
    def KeepLoad(self, Value):
        self.CheckForError(self._lib.ReduceCkt_Set_KeepLoad(bool(Value)))

    @property
    def EditString(self):
        '''Edit String for RemoveBranches functions'''
        return self._get_string(self.CheckForError(self._lib.ReduceCkt_Get_EditString()))
        
    @EditString.setter
    def EditString(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
    
        self.CheckForError(self._lib.ReduceCkt_Set_EditString(Value))

    @property
    def StartPDElement(self):
        '''Start element for Remove Branch function'''
        return self._get_string(self.CheckForError(self._lib.ReduceCkt_Get_StartPDElement()))
        
    @StartPDElement.setter
    def StartPDElement(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
            
        self.CheckForError(self._lib.ReduceCkt_Set_StartPDElement(Value))

    @property
    def EnergyMeter(self):
        '''Name of Energymeter to use for reduction'''
        return self._get_string(self.CheckForError(self._lib.ReduceCkt_Get_EnergyMeter()))
    
    @EnergyMeter.setter
    def EnergyMeter(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
    
        self.CheckForError(self._lib.ReduceCkt_Set_EnergyMeter(Value))

    def SaveCircuit(self, CktName):
        '''
        Save present (reduced) circuit
        Filename is listed in the Text Result interface
        '''
        if type(CktName) is not bytes:
            CktName = CktName.encode(self._api_util.codec)
        
        self.CheckForError(self._lib.ReduceCkt_SaveCircuit(CktName))

    def DoDefault(self):
        '''Do Default Reduction algorithm'''
        self.CheckForError(self._lib.ReduceCkt_DoDefault())

    def DoShortLines(self):
        '''Do ShortLines algorithm: Set Zmag first if you don't want the default'''
        self.CheckForError(self._lib.ReduceCkt_DoShortLines())

    def DoDangling(self):
        '''Reduce Dangling Algorithm; branches with nothing connected'''
        self.CheckForError(self._lib.ReduceCkt_DoDangling())

    def DoLoopBreak(self):
        self.CheckForError(self._lib.ReduceCkt_DoLoopBreak())
    
    def DoParallelLines(self):
        self.CheckForError(self._lib.ReduceCkt_DoParallelLines())
    
    def DoSwitches(self):
        self.CheckForError(self._lib.ReduceCkt_DoSwitches())
    
    def Do1phLaterals(self):
        self.CheckForError(self._lib.ReduceCkt_Do1phLaterals())
    
    def DoBranchRemove(self):
        self.CheckForError(self._lib.ReduceCkt_DoBranchRemove())
