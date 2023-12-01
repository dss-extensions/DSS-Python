from typing import Union, List, AnyStr, Dict
from .enums import ExtraClassIDs
from .types import Float64Array
from .DSSObj import DSSObj
from .CircuitElement import CircuitElementBatch, ElementHasRegistersMixin


class PCElementMixin:
    __slots__ = ()
    _extra_slots = []

    def VariableNames(self) -> List[str]:
        return self._get_string_array(self._lib.Alt_PCE_Get_VariableNames, self._ptr)

    def VariableValues(self) -> Float64Array:
        return self._get_float64_array(self._lib.Alt_PCE_Get_VariableValues, self._ptr)
    
    def VariablesDict(self) -> Dict[str, float]:
        return dict(*zip(self.VariableNames(), self.VariableValues()))

    def GetVariableValue(self, varIdxName: Union[AnyStr, int]) -> float:
        if isinstance(varIdxName, int):
            return self._lib.Alt_PCE_Get_VariableValue(self._ptr, varIdxName)
        else:
            if not isinstance(varIdxName, bytes):
                varIdxName = varIdxName.encode(self._api_util.codec)

            return self._lib.Alt_PCE_Get_VariableValueS(self._ptr, varIdxName)


    def SetVariableValue(self, varIdxName: Union[AnyStr, int], value: float):
        if isinstance(varIdxName, int):
            self._lib.Alt_PCE_Set_VariableValue(self._ptr, varIdxName, value)
        else:
            if not isinstance(varIdxName, bytes):
                varIdxName = varIdxName.encode(self._api_util.codec)

            self._lib.Alt_PCE_Set_VariableValueS(self._ptr, varIdxName, value)

    def EnergyMeter(self) -> DSSObj:
        return self._get_obj_from_ptr(self._lib.Alt_PCE_Get_EnergyMeter(self._ptr))

    def EnergyMeterName(self) -> str:
        return self._get_string(self._lib.Alt_PCE_Get_EnergyMeterName(self._ptr))


class PCElementBatchMixin:
    __slots__ = ()

    def EnergyMeter(self) -> List[DSSObj]:
        return [self._get_obj_from_ptr(self._lib.Alt_PCE_Get_EnergyMeter(ptr)) for ptr in self._unpack()]

    def EnergyMeterName(self) -> List[str]:
        return [self._get_string(self._lib.Alt_PCE_Get_EnergyMeterName(ptr)) for ptr in self._unpack()]


class PCElementBatch(CircuitElementBatch, PCElementBatchMixin, ElementHasRegistersMixin):
    '''
    Non-uniform batch of PC elements. Can contain distinct PC types, while providing 
    common functions
    '''

    __slots__ = ()

    def __init__(self, func, parent, sync_cls_idx=ExtraClassIDs.PCElements):
        CircuitElementBatch.__init__(self, func, parent, sync_cls_idx=sync_cls_idx)
        PCElementBatchMixin.__init__(self)
        ElementHasRegistersMixin.__init__(self)
