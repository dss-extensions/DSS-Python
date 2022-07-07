'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira
Copyright (c) 2018-2022 DSS Extensions contributors
'''
from .._cffi_api_util import Base

class IText(Base):
    __slots__ = []

    @property
    def Command(self):
        '''Input command string for the DSS.'''
        return self._get_string(self.CheckForError(self._lib.Text_Get_Command()))

    @Command.setter
    def Command(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Text_Set_Command(Value))

    @property
    def Result(self):
        '''(read-only) Result string for the last command.'''
        return self._get_string(self.CheckForError(self._lib.Text_Get_Result()))
