# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from __future__ import annotations
from ._cffi_api_util import Base
from typing import AnyStr, Union

class IDSSProperty(Base):
    __slots__ = []

    _columns = [
        'Description', 
        'Name', 
        'Val',
    ]
    
    @property
    def Description(self) -> str:
        '''
        Description of the property.

        Original COM help: https://opendss.epri.com/Description.html
        '''
        return self._get_string(self._check_for_error(self._lib.DSSProperty_Get_Description()))

    @property
    def Name(self) -> str:
        '''
        Name of Property

        Original COM help: https://opendss.epri.com/Name6.html
        '''
        return self._get_string(self._check_for_error(self._lib.DSSProperty_Get_Name()))

    @property
    def Val(self) -> str:
        '''
        Get/set the value of the active property. The value must be specified as a string.

        Original COM help: https://opendss.epri.com/Val.html
        '''
        return self._get_string(self._check_for_error(self._lib.DSSProperty_Get_Val()))

    @Val.setter
    def Val(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = str(Value).encode(self._api_util.codec)

        self._check_for_error(self._lib.DSSProperty_Set_Val(Value))

    def __getitem__(self, propname_index: Union[AnyStr, int]) -> IDSSProperty:
        if isinstance(propname_index, int):
            self._check_for_error(self._lib.DSSProperty_Set_Index(propname_index))
        else:
            if not isinstance(propname_index, bytes):
                propname_index = propname_index.encode(self._api_util.codec)

            self._check_for_error(self._lib.DSSProperty_Set_Name(propname_index))

        return self

    def __call__(self, propname_index) -> IDSSProperty:
        return self.__getitem__(propname_index)

