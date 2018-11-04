'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class IDSSimComs(Base):
    __slots__ = []

    def BusVoltage(self, Index):
        return self._get_float64_array(self._lib.DSSimComs_BusVoltage, Index)

    def BusVoltagepu(self, Index):
        return self._get_float64_array(self._lib.DSSimComs_BusVoltagepu, Index)


