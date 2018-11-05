'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class IDSSProgress(Base):
    __slots__ = []

    def Close(self):
        self._lib.DSSProgress_Close()

    def Show(self):
        self._lib.DSSProgress_Show()

    @property
    def Caption(self):
        '''(write-only) Caption to appear on the bottom of the DSS Progress form.'''
        raise AttributeError("This property is write-only!")

    @Caption.setter
    def Caption(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.DSSProgress_Set_Caption(Value)
        self.CheckForError()

    @property
    def PctProgress(self):
        '''(write-only) Percent progress to indicate [0..100]'''
        raise AttributeError("This property is write-only!")

    @PctProgress.setter
    def PctProgress(self, Value):
        self._lib.DSSProgress_Set_PctProgress(Value)
        self.CheckForError()


