# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Base
from typing import AnyStr

class IDSSProgress(Base):
    __slots__ = []

    def Close(self):
        self._check_for_error(self._lib.DSSProgress_Close())

    def Show(self):
        self._check_for_error(self._lib.DSSProgress_Show())

    @property
    def Caption(self) -> str:
        '''
        (write-only) Caption to appear on the bottom of the DSS Progress form.

        Original COM help: https://opendss.epri.com/Caption.html
        '''
        raise AttributeError("This property is write-only!")

    @Caption.setter
    def Caption(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.DSSProgress_Set_Caption(Value))

    @property
    def PctProgress(self) -> int:
        '''
        (write-only) Percent progress to indicate [0..100]

        Original COM help: https://opendss.epri.com/PctProgress.html
        '''
        raise AttributeError("This property is write-only!")

    @PctProgress.setter
    def PctProgress(self, Value: int):
        self._check_for_error(self._lib.DSSProgress_Set_PctProgress(Value))


