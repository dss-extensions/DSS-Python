# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Base
from ._types import Float64Array
import warnings

class IDSSimComs(Base):
    '''
    **Deprecated**; use `DSS.ActiveCircuit.ActiveBus` API or the AltDSS alternatives instead
    '''
    __slots__ = []

    def BusVoltage(self, Index: int) -> Float64Array:
        warnings.warn('Use ActiveCircuit.ActiveBus or the AltDSS (AltDSS-Python) alternatives.', DeprecationWarning, stacklevel=2)
        return self._lib.DSSimComs_BusVoltage_GR(Index)

    def BusVoltagepu(self, Index: int) -> Float64Array:
        warnings.warn('Use ActiveCircuit.ActiveBus or the AltDSS (AltDSS-Python) alternatives.', DeprecationWarning, stacklevel=2)
        return self._lib.DSSimComs_BusVoltagepu_GR(Index)


