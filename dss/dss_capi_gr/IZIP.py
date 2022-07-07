'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2021-2022 Paulo Meira
'''
from .._cffi_api_util import Base

class IZIP(Base):
    __slots__ = []

    _columns = []

    def Open(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.ZIP_Open(Value))

    def Close(self):
        self.CheckForError(self._lib.ZIP_Close())

    def Redirect(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.ZIP_Redirect(Value))
