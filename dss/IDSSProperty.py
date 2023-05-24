'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2023 Paulo Meira

Copyright (c) 2018-2023 DSS-Extensions contributors
'''
from ._cffi_api_util import Base
from typing import AnyStr, Union
from typing_extensions import Self

class IDSSProperty(Base):
    __slots__ = []

    _columns = [
        'Description', 
        'Name', 
        'Val',
    ]
    
    @property
    def Description(self) -> str:
        '''Description of the property.'''
        return self._get_string(self.CheckForError(self._lib.DSSProperty_Get_Description()))

    @property
    def Name(self) -> str:
        '''Name of Property'''
        return self._get_string(self.CheckForError(self._lib.DSSProperty_Get_Name()))

    @property
    def Val(self) -> str:
        return self._get_string(self.CheckForError(self._lib.DSSProperty_Get_Val()))

    @Val.setter
    def Val(self, Value: AnyStr):
        if type(Value) is not bytes:
            Value = str(Value).encode(self._api_util.codec)

        self.CheckForError(self._lib.DSSProperty_Set_Val(Value))

    def __getitem__(self, propname_index: Union[AnyStr, int]) -> Self:
        if isinstance(propname_index, int):
            self.CheckForError(self._lib.DSSProperty_Set_Index(propname_index))
        else:
            if type(propname_index) is not bytes:
                propname_index = propname_index.encode(self._api_util.codec)

            self.CheckForError(self._lib.DSSProperty_Set_Name(propname_index))

        return self

    def __call__(self, propname_index) -> Self:
        return self.__getitem__(propname_index)

