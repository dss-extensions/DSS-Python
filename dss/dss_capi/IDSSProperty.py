'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class IDSSProperty(Base):
    __slots__ = []

    @property
    def Description(self):
        '''(read-only) Description of the property.'''
        return self.get_string(self.lib.DSSProperty_Get_Description())

    @property
    def Name(self):
        '''(read-only) Name of Property'''
        return self.get_string(self.lib.DSSProperty_Get_Name())

    @property
    def Val(self):
        return self.get_string(self.lib.DSSProperty_Get_Val())

    @Val.setter
    def Val(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.DSSProperty_Set_Val(Value)

    def __getitem__(self, propname_index):
        if isinstance(propname_index, int):
            self.lib.DSSProperty_Set_Index(propname_index)
        else:
            if type(propname_index) is not bytes:
                propname_index = propname_index.encode(self.api_util.codec)

            self.lib.DSSProperty_Set_Name(propname_index)

        return self

    def __call__(self, propname_index):
        return self.__getitem__(propname_index)

