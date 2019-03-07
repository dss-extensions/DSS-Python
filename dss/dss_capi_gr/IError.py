'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2019 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class IError(Base):
    __slots__ = []

    @property
    def Description(self):
        '''(read-only) Description of error for last operation'''
        return self._get_string(self._lib.Error_Get_Description())

    @property
    def Number(self):
        '''(read-only) Error Number (returns current value and then resets to zero)'''
        return self._lib.Error_Get_Number()

    @property
    def EarlyAbort(self):
        '''
        EarlyAbort controls whether all errors halts the DSS script processing (Compile/Redirect), defaults to True.
        '''
        return self._lib.Error_Get_EarlyAbort() != 0
        
    @EarlyAbort.setter
    def EarlyAbort(self, Value):
        self._lib.Error_Set_EarlyAbort(Value)
