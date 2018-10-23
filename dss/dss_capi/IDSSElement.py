'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base
from .IDSSProperty import IDSSProperty

class IDSSElement(Base):
    __slots__ = [
        'Properties'
    ]
    
    def __init__(self, api_util):
        self.Properties = IDSSProperty(api_util)
        Base.__init__(self, api_util)    

    @property
    def AllPropertyNames(self):
        '''(read-only) Array of strings containing the names of all properties for the active DSS object.'''
        return self._get_string_array(self._lib.DSSElement_Get_AllPropertyNames)

    @property
    def Name(self):
        '''(read-only) Full Name of Active DSS Object (general element or circuit element).'''
        return self._get_string(self._lib.DSSElement_Get_Name())

    @property
    def NumProperties(self):
        '''(read-only) Number of Properties for the active DSS object.'''
        return self._lib.DSSElement_Get_NumProperties()

