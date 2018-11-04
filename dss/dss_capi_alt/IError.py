'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
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
        '''(read-only) Error Number'''
        return self._lib.Error_Get_Number()


