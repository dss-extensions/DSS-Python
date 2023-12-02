from typing import Dict, List, Union, AnyStr
from dss.enums import OCPDevType
from .enums import ExtraClassIDs
from .types import Float64Array, Int32Array, ComplexArray, BoolArray
from .Batch import NonUniformBatch
from .DSSObj import DSSObj

class CircuitElementMixin:
    __slots__ = () 
    # To avoid layout issues, let the final class use the following instead
    _extra_slots = ['Controllers', ]

    def __init__(self, *args):
        self.Controllers = NonUniformBatch(self._lib.Alt_CE_Get_Controllers, self)

    def GUID(self) -> str:
        '''Object's GUID/UUID. Currently used only in the CIM-related methods.'''
        return self._get_string(self._lib.Alt_CE_Get_GUID(self._ptr))

    def _get_DisplayName(self) -> str:
        return self._get_string(self._lib.Alt_CE_Get_DisplayName(self._ptr))
    
    def _set_DisplayName(self, value: AnyStr):
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Alt_CE_Set_DisplayName(self._ptr, value)

    DisplayName = property(_get_DisplayName, _set_DisplayName) # type: str

    # TODO: is BusNames too redundant to keep?
    # def GetBusNames(self) -> List[str]:
    #     return self._get_string_array(self._lib.Alt_CE_Get_BusNames, self._ptr)

    # def SetBusNames(self, value: List[AnyStr]):
    #     value, value_ptr, value_count = self._prepare_string_array(value)
    #     self._lib.Alt_CE_Set_BusNames(self._ptr, value_ptr, value_count)

    # BusNames = property(GetBusNames, SetBusNames)

    def Handle(self) -> int:
        return self._lib.Alt_CE_Get_Handle(self._ptr)

    def NumConductors(self) -> int:
        return self._lib.Alt_CE_Get_NumConductors(self._ptr)

    def NumPhases(self) -> int:
        return self._lib.Alt_CE_Get_NumPhases(self._ptr)

    def NumTerminals(self) -> int:
        return self._lib.Alt_CE_Get_NumTerminals(self._ptr)

    def NumControllers(self) -> int:
        return self._lib.Alt_CE_Get_NumControllers(self._ptr)

    def OCPDevice(self) -> Union[DSSObj, None]:
        return self._get_obj_from_ptr(self._lib.Alt_CE_Get_OCPDevice(self._ptr))

    def OCPDeviceIndex(self) -> int:
        return self._lib.Alt_CE_Get_OCPDeviceIndex(self._ptr)

    def OCPDeviceType(self) -> OCPDevType:
        return OCPDevType(self._lib.Alt_CE_Get_OCPDeviceType(self._ptr))

    def IsIsolated(self) -> bool:
        return self._lib.Alt_CE_Get_IsIsolated(self._ptr) != 0

    def HasOCPDevice(self) -> bool:
        return self._lib.Alt_CE_Get_HasOCPDevice(self._ptr) != 0

    def HasSwitchControl(self) -> bool:
        return self._lib.Alt_CE_Get_HasSwitchControl(self._ptr) != 0

    def HasVoltControl(self) -> bool:
        return self._lib.Alt_CE_Get_HasVoltControl(self._ptr) != 0

    def IsOpen(self, terminal: int, phase: int) -> bool:
        return self._lib.Alt_CE_IsOpen(self._ptr, terminal, phase) != 0

    def MaxCurrent(self, terminal: int) -> float:
        '''
        Returns the maximum current (magnitude) at the specificed terminal. 
        Use -1 as terminal to get the value across all terminals.
        '''
        return self._lib.Alt_CE_MaxCurrent(self._ptr, terminal)

    def Open(self, terminal: int, phase: int) -> None:
        self._lib.Alt_CE_Open(self._ptr, terminal, phase)

    def Close(self, terminal: int, phase: int) -> None:
        self._lib.Alt_CE_Close(self._ptr, terminal, phase)

    def NodeOrder(self) -> Int32Array:
        return self._get_int32_array(self._lib.Alt_CE_Get_NodeOrder, self._ptr)

    def NodeRef(self) -> Int32Array:
        return self._get_int32_array(self._lib.Alt_CE_Get_NodeRef, self._ptr)

    def ComplexSeqVoltages(self) -> ComplexArray:
        return self._get_fcomplex128_array(self._lib.Alt_CE_Get_ComplexSeqVoltages, self._ptr)

    def ComplexSeqCurrents(self) -> ComplexArray:
        return self._get_fcomplex128_array(self._lib.Alt_CE_Get_ComplexSeqCurrents, self._ptr)

    def Currents(self) -> ComplexArray:
        return self._get_fcomplex128_array(self._lib.Alt_CE_Get_Currents, self._ptr)

    def Voltages(self) -> ComplexArray:
        return self._get_fcomplex128_array(self._lib.Alt_CE_Get_Voltages, self._ptr)

    def Losses(self) -> complex:
        '''Total (complex) losses in the element, in VA (watts, vars)'''
        return self._get_fcomplex128_simple(self._lib.Alt_CE_Get_Losses, self._ptr)

    def PhaseLosses(self) -> ComplexArray:
        '''Complex array of losses (kVA) by phase'''
        return self._get_fcomplex128_array(self._lib.Alt_CE_Get_PhaseLosses, self._ptr)

    def Powers(self) -> ComplexArray:
        return self._get_fcomplex128_array(self._lib.Alt_CE_Get_Powers, self._ptr)

    def SeqCurrents(self) -> Float64Array:
        return self._get_float64_array(self._lib.Alt_CE_Get_SeqCurrents, self._ptr)

    def SeqPowers(self) -> ComplexArray:
        return self._get_fcomplex128_array(self._lib.Alt_CE_Get_SeqPowers, self._ptr)

    def SeqVoltages(self) -> Float64Array:
        return self._get_float64_array(self._lib.Alt_CE_Get_SeqVoltages, self._ptr)

    def Residuals(self) -> Float64Array:
        return self._get_float64_array(self._lib.Alt_CE_Get_Residuals, self._ptr)

    def YPrim(self) -> ComplexArray:
        return self._get_fcomplex128_array(self._lib.Alt_CE_Get_YPrim, self._ptr)

    def VoltagesMagAng(self) -> Float64Array:
        return self._get_float64_array(self._lib.Alt_CE_Get_VoltagesMagAng, self._ptr)

    def TotalPowers(self) -> ComplexArray:
        return self._get_fcomplex128_array(self._lib.Alt_CE_Get_TotalPowers, self._ptr)


class CircuitElementBatchMixin:
    __slots__ = ()

    def GUID(self) -> str:
        '''GUID/UUID for each object. Currently used only in the CIM-related methods.'''
        return [self._get_string(self._lib.Alt_CE_Get_GUID(ptr)) for ptr in self._unpack()]

    def Handle(self) -> Int32Array:
        return self._get_batch_int32_func("Alt_CE_Get_Handle")

    def NumConductors(self) -> Int32Array:
        return self._get_batch_int32_func("Alt_CE_Get_NumConductors")

    def NumPhases(self) -> Int32Array:
        return self._get_batch_int32_func("Alt_CE_Get_NumPhases")

    def NumTerminals(self) -> Int32Array:
        return self._get_batch_int32_func("Alt_CE_Get_NumTerminals")

    def NumControllers(self) -> Int32Array:
        return self._get_batch_int32_func("Alt_CE_Get_NumControllers")

    def OCPDevice(self) -> List[Union[DSSObj, None]]: #TODO
        return self._get_obj_from_ptr(self._lib.Alt_CE_Get_OCPDevice(self._ptr))

    def OCPDeviceIndex(self) -> Int32Array:
        return self._get_batch_int32_func("Alt_CE_Get_OCPDeviceIndex")

    def OCPDeviceType(self) -> OCPDevType:
        return [
            OCPDevType(val) for val in self._get_batch_int32_func("Alt_CE_Get_OCPDeviceType")
        ]

    def MaxCurrent(self, terminal: int) -> float:
        '''
        Returns the maximum current (magnitude) at the specificed terminal for all elements in this batch. 
        Use -1 as terminal to get the value across all terminals.
        '''
        return self._get_batch_float_int32_func("Alt_CE_MaxCurrent", terminal)
    
    def IsIsolated(self) -> BoolArray:
        return self._get_batch_int32_func("Alt_CE_Get_IsIsolated").astype(bool)

    def HasOCPDevice(self) -> bool:
        return self._get_batch_int32_func("Alt_CE_Get_HasOCPDevice").astype(bool)

    def HasSwitchControl(self) -> bool:
        return self._get_batch_int32_func("Alt_CE_Get_HasSwitchControl").astype(bool)

    def HasVoltControl(self) -> bool:
        return self._get_batch_int32_func("Alt_CE_Get_HasVoltControl").astype(bool)

    def Powers(self) -> ComplexArray:
        '''Complex array of powers (kVA) into each conductor of each terminal, of each element in the batch.'''
        return self._get_fcomplex128_array(self._lib.Alt_CEBatch_Get_Powers, *self._get_ptr_cnt())

    def Losses(self) -> ComplexArray:
        '''Total losses for each element, complex VA (watts, vars)'''
        return self._get_fcomplex128_array(self._lib.Alt_CEBatch_Get_Losses, *self._get_ptr_cnt())

    def PhaseLosses(self) -> ComplexArray:
        '''Complex array of losses (kVA) by phase, for each element'''
        return self._get_fcomplex128_array(self._lib.Alt_CEBatch_Get_PhaseLosses, *self._get_ptr_cnt())

    def TotalPowers(self) -> ComplexArray:
        '''
        Returns an array with the total powers (complex, kVA) at all terminals of the circuit elements in this batch.

        The resulting array is equivalent to concatenating the TotalPowers for each element.        
        '''
        return self._get_fcomplex128_array(self._lib.Alt_CEBatch_Get_TotalPowers, *self._get_ptr_cnt())

    def SeqPowers(self) -> ComplexArray:
        return self._get_fcomplex128_array(self._lib.Alt_CEBatch_Get_SeqPowers, *self._get_ptr_cnt())

    def SeqCurrents(self) -> Float64Array:
        return self._get_float64_array(self._lib.Alt_CEBatch_Get_SeqCurrents, *self._get_ptr_cnt())
        
    def ComplexSeqCurrents(self) -> ComplexArray:
        return self._get_float64_array(self._lib.Alt_CEBatch_Get_ComplexSeqCurrents, *self._get_ptr_cnt())

    def Currents(self) -> ComplexArray:
        return self._get_fcomplex128_array(self._lib.Alt_CEBatch_Get_Currents, *self._get_ptr_cnt())

    def CurrentsMagAng(self) -> Float64Array:
        return self._get_float64_array(self._lib.Alt_CEBatch_Get_CurrentsMagAng, *self._get_ptr_cnt())

    def Voltages(self) -> ComplexArray:
        return self._get_fcomplex128_array(self._lib.Alt_CEBatch_Get_Voltages, *self._get_ptr_cnt())

    def SeqVoltages(self) -> Float64Array:
        return self._get_float64_array(self._lib.Alt_CEBatch_Get_SeqVoltages, *self._get_ptr_cnt())

    def VoltagesMagAng(self) -> Float64Array:
        return self._get_float64_array(self._lib.Alt_CEBatch_Get_VoltagesMagAng, *self._get_ptr_cnt())

    def ComplexSeqVoltages(self) -> ComplexArray:
        return self._get_fcomplex128_array(self._lib.Alt_CEBatch_Get_ComplexSeqVoltages, *self._get_ptr_cnt())


class ElementHasRegistersMixin:
    __slots__ = ()
    _extra_slots = []

    def RegisterNames(self) -> List[str]:
        return self._get_string_array(self._lib.Alt_CE_Get_RegisterNames, self._ptr)

    def RegisterValues(self) -> Float64Array:
        return self._get_float64_array(self._lib.Alt_CE_Get_RegisterValues, self._ptr)

    def RegistersDict(self) -> Dict[str, float]:
        return dict(*zip(self.RegisterNames(), self.RegisterValues()))


class CircuitElementBatch(NonUniformBatch, CircuitElementBatchMixin):
    '''
    Non-uniform batch of circuit elements. Can contain distinct types, while providing 
    common functions
    '''

    __slots__ = ()

    def __init__(self, func, parent, sync_cls_idx=ExtraClassIDs.CktElements):
        NonUniformBatch.__init__(self, func, parent, sync_cls_idx=sync_cls_idx)
        CircuitElementBatchMixin.__init__(self)
