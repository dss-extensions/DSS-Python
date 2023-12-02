from typing import List
from .enums import ExtraClassIDs
from .types import Float64Array, Int32Array
from .DSSObj import DSSObj
from .CircuitElement import CircuitElementBatch

class PDElementMixin:
    __slots__ = ()
    _extra_slots = []

    def EnergyMeter(self) -> DSSObj:
        return self._get_obj_from_ptr(self._lib.Alt_PDE_Get_EnergyMeter(self._ptr))

    def EnergyMeterName(self) -> str:
        return self._get_string(self._lib.Alt_PDE_Get_EnergyMeterName(self._ptr))

    def IsShunt(self) -> bool:
        return self._lib.Alt_PDE_Get_IsShunt(self._ptr) != 0

    def AccumulatedL(self) -> float:
        return self._lib.Alt_PDE_Get_AccumulatedL(self._ptr)

    def Lambda(self) -> float:
        return self._lib.Alt_PDE_Get_Lambda(self._ptr)

    def NumCustomers(self) -> int:
        return self._lib.Alt_PDE_Get_NumCustomers(self._ptr)

    def ParentPDElement(self) -> DSSObj:
        return self._lib.Alt_PDE_Get_ParentPDElement(self._ptr)

    def TotalCustomers(self) -> int:
        return self._lib.Alt_PDE_Get_TotalCustomers(self._ptr)

    def FromTerminal(self) -> int:
        return self._lib.Alt_PDE_Get_FromTerminal(self._ptr)

    def TotalMiles(self) -> float:
        return self._lib.Alt_PDE_Get_TotalMiles(self._ptr)

    def SectionID(self) -> int:
        return self._lib.Alt_PDE_Get_SectionID(self._ptr)

    def pctNorm(self, allNodes=False) -> float:
        '''
        '''
        return self._lib.Alt_PDE_Get_pctNorm(self._ptr, allNodes)

    def pctEmerg(self, allNodes=False) -> float:
        '''
        '''
        return self._lib.Alt_PDE_Get_pctEmerg(self._ptr, allNodes)


class PDElementBatchMixin:
    __slots__ = ()

    def EnergyMeter(self) -> List[DSSObj]:
        return [self._get_obj_from_ptr(self._lib.Alt_PDE_Get_EnergyMeter(ptr)) for ptr in self._unpack()]

    def EnergyMeterName(self) -> List[str]:
        return [self._get_string(self._lib.Alt_PDE_Get_EnergyMeterName(ptr)) for ptr in self._unpack()]

    def IsShunt(self) -> List[bool]:
        return [self._lib.Alt_PDE_Get_IsShunt(ptr) != 0 for ptr in self._unpack()]

    def AccumulatedL(self) -> Float64Array:
        return self._get_batch_float_func("Alt_PDE_Get_AccumulatedL")

    def Lambda(self) -> Float64Array:
        return self._get_batch_float_func("Alt_PDE_Get_Lambda")

    def NumCustomers(self) -> Int32Array:
        return self._get_batch_int32_func("Alt_PDE_Get_NumCustomers")

    def ParentPDElement(self) -> List[DSSObj]:
        return [self._lib.Alt_PDE_Get_ParentPDElement(self._ptr) for ptr in self._unpack()]

    def TotalCustomers(self) -> Int32Array:
        return self._get_batch_int32_func("Alt_PDE_Get_TotalCustomers")

    def FromTerminal(self) -> Int32Array:
        return self._get_batch_int32_func("Alt_PDE_Get_FromTerminal")

    def TotalMiles(self) -> Float64Array:
        return self._get_batch_float_func("Alt_PDE_Get_TotalMiles")

    def SectionID(self) -> Int32Array:
        return self._get_batch_int32_func("Alt_PDE_Get_SectionID")
    

class PDElementBatch(CircuitElementBatch, PDElementBatchMixin):
    '''
    Non-uniform batch of PD elements. Can contain distinct PD types, while providing 
    common functions
    '''

    __slots__ = ()

    def __init__(self, func, parent, sync_cls_idx=ExtraClassIDs.PDElements):
        CircuitElementBatch.__init__(self, func, parent, sync_cls_idx=sync_cls_idx)
        PDElementBatchMixin.__init__(self)


__all__ = ('PDElementMixin', 'PDElementBatchMixin', 'PDElementBatch',)