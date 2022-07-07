'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2021-2022 Paulo Meira
'''
from .._cffi_api_util import Base

class IZIP(Base):
    __slots__ = []

    _columns = []

    def Open(self, Value):
        '''
        Opens and prepares a ZIP file to be used by the DSS text parser
        
        (API Extension)
        '''
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.ZIP_Open(Value))

    def Close(self):
        '''
        Closes the current open ZIP file
        
        (API Extension)
        '''
        self.CheckForError(self._lib.ZIP_Close())

    def Redirect(self, Value):
        '''
        Runs a "Redirect" command inside the current (open) ZIP file.
        In the current implementation, all files required by the script must
        be present inside the ZIP, using relative paths.

        (API Extension)
        '''
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.ZIP_Redirect(Value))
