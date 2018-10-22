'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class IDSSimComs(Base):
    __slots__ = []

    def BusVoltage(self, Index):
        self.lib.DSSimComs_BusVoltage_GR(Index)
        return self.get_float64_gr_array()

    def BusVoltagepu(self, Index):
        self.lib.DSSimComs_BusVoltagepu_GR(Index)
        return self.get_float64_gr_array()


