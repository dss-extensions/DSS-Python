'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class IActiveClass(Base):
    __slots__ = []

    @property
    def ActiveClassName(self):
        '''(read-only) Returns name of active class.'''
        return self.get_string(self.lib.ActiveClass_Get_ActiveClassName())

    @property
    def AllNames(self):
        '''(read-only) Array of strings consisting of all element names in the active class.'''
        return self.get_string_array(self.lib.ActiveClass_Get_AllNames)

    @property
    def Count(self):
        '''(read-only) Number of elements in Active Class. Same as NumElements Property.'''
        return self.lib.ActiveClass_Get_Count()

    def __len__(self):
        return self.lib.ActiveClass_Get_Count()

    @property
    def First(self):
        '''(read-only) Sets first element in the active class to be the active DSS object. If object is a CktElement, ActiveCktELment also points to this element. Returns 0 if none.'''
        return self.lib.ActiveClass_Get_First()

    @property
    def Name(self):
        '''Name of the Active Element of the Active Class'''
        return self.get_string(self.lib.ActiveClass_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.ActiveClass_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Sets next element in active class to be the active DSS object. If object is a CktElement, ActiveCktElement also points to this element.  Returns 0 if no more.'''
        return self.lib.ActiveClass_Get_Next()

    @property
    def NumElements(self):
        '''(read-only) Number of elements in this class. Same as Count property.'''
        return self.lib.ActiveClass_Get_NumElements()
