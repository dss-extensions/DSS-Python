'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira
Copyright (c) 2018-2022 DSS Extensions contributors
'''
from .._cffi_api_util import Base
from .IDSSProperty import IDSSProperty

class IDSSElement(Base):
    __slots__ = [
        'Properties'
    ]
    
    _columns = [
        'AllPropertyNames', 
        'Name', 
        'NumProperties',
    ]
    
    def __init__(self, api_util):
        self.Properties = IDSSProperty(api_util)
        Base.__init__(self, api_util)    

    @property
    def AllPropertyNames(self):
        '''(read-only) Array of strings containing the names of all properties for the active DSS object.'''
        return self.CheckForError(self._get_string_array(self._lib.DSSElement_Get_AllPropertyNames))

    @property
    def Name(self):
        '''(read-only) Full Name of Active DSS Object (general element or circuit element).'''
        return self._get_string(self.CheckForError(self._lib.DSSElement_Get_Name()))

    @property
    def NumProperties(self):
        '''(read-only) Number of Properties for the active DSS object.'''
        return self.CheckForError(self._lib.DSSElement_Get_NumProperties())

    def ToJSON(self, options=0):
        '''
        Returns the properties of the active DSS object as a JSON-encoded string.

        The `options` parameter contains bit-flags to toggle specific features.
        See `Obj_ToJSON` (C-API) for more, or `DSSObj.to_json` in Python.

        (API Extension)
        '''
        return self._get_string(self.CheckForError(self._lib.DSSElement_ToJSON(options)))
