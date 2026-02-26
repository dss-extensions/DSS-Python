# A compatibility layer for DSS C-API that mimics EPRI's OpenDSS COM interface.
# Copyright (c) 2016-2025 Paulo Meira
# Copyright (c) 2018-2025 DSS-Extensions contributors
from ._cffi_api_util import Base
from typing import AnyStr

class IDSSProgress(Base):
    __slots__ = []

    def Close(self):
        '''
        Close progress form

        Typically used with EPRI's OpenDSS, on Windows. Otherwise, it could be a no-op.
        '''
        self._lib.DSSProgress_Close()

    def Show(self):
        '''
        Show progress form

        Typically used with EPRI's OpenDSS, on Windows. Otherwise, it could be a no-op.
        '''
        self._lib.DSSProgress_Show()

    @property
    def Caption(self) -> str:
        '''
        Set the caption to appear on the bottom of the DSS Progress form.

        Typically used with EPRI's OpenDSS, on Windows. Otherwise, it could be a no-op.

        Original COM help: https://opendss.epri.com/Caption.html
        '''
        raise AttributeError("This property is write-only!")

    @Caption.setter
    def Caption(self, Value: AnyStr):
        self._lib.DSSProgress_Set_Caption(Value)

    @property
    def PctProgress(self) -> int:
        '''
        Set the percent progress to indicate [0..100] on the progress form.

        Typically used with EPRI's OpenDSS, on Windows. Otherwise, it could be a no-op.

        Original COM help: https://opendss.epri.com/PctProgress.html
        '''
        raise AttributeError("This property is write-only!")

    @PctProgress.setter
    def PctProgress(self, Value: int):
        self._lib.DSSProgress_Set_PctProgress(Value)


