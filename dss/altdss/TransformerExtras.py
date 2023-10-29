from .types import ComplexArray

class TransformerObjMixin: #TODO: batch version?
    __slots__ = ()
    _extra_slots = []

    def WindingCurrents(self) -> ComplexArray:
        '''
        All Winding currents (ph1, wdg1, wdg2,... ph2, wdg1, wdg2 ...)

        WARNING: If the transformer has open terminal(s), results may be wrong, i.e. avoid using this
        in those situations. For more information, see https://github.com/dss-extensions/dss-extensions/issues/24
        '''
        return self._get_fcomplex128_array(self._lib.Alt_Transformer_Get_WdgCurrents, self._ptr)

    def WindingVoltages(self, winding: int) -> ComplexArray:
        '''
        Complex array of voltages for a target winding
        
        WARNING: If the transformer has open terminal(s), results may be wrong, i.e. avoid using this
        in those situations. For more information, see https://github.com/dss-extensions/dss-extensions/issues/24
        '''
        return self._get_fcomplex128_array(self._lib.Alt_Transformer_Get_WdgVoltages, self._ptr, winding)

    def LossesByType(self) -> ComplexArray:
        '''
        Complex array with the losses by type (total losses, load losses, no-load losses), in VA
        '''
        return self._get_fcomplex128_array(self._lib.Alt_Transformer_Get_LossesByType, self._ptr)

__all__ = ('TransformerObjMixin', )