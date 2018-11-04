'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class IDSS_Executive(Base):
    __slots__ = []

    def Command(self, i):
        '''(read-only) Get i-th command'''
        return self._get_string(self._lib.DSS_Executive_Get_Command(i))

    def CommandHelp(self, i):
        '''(read-only) Get help string for i-th command'''
        return self._get_string(self._lib.DSS_Executive_Get_CommandHelp(i))

    def Option(self, i):
        '''(read-only) Get i-th option'''
        return self._get_string(self._lib.DSS_Executive_Get_Option(i))

    def OptionHelp(self, i):
        '''(read-only) Get help string for i-th option'''
        return self._get_string(self._lib.DSS_Executive_Get_OptionHelp(i))

    def OptionValue(self, i):
        '''(read-only) Get present value of i-th option'''
        return self._get_string(self._lib.DSS_Executive_Get_OptionValue(i))

    @property
    def NumCommands(self):
        '''(read-only) Number of DSS Executive Commands'''
        return self._lib.DSS_Executive_Get_NumCommands()

    @property
    def NumOptions(self):
        '''(read-only) Number of DSS Executive Options'''
        return self._lib.DSS_Executive_Get_NumOptions()

