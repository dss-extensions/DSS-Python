'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira

Copyright (c) 2018-2022 DSS-Extensions contributors
'''
from ._cffi_api_util import Base

class IDSS_Executive(Base):
    __slots__ = []

    _columns = [
        'NumCommands', 
        'NumOptions',
    ]

    def Command(self, i: int) -> str:
        '''Get i-th command'''
        return self._get_string(self.CheckForError(self._lib.DSS_Executive_Get_Command(i)))

    def CommandHelp(self, i: int) -> str:
        '''Get help string for i-th command'''
        return self._get_string(self.CheckForError(self._lib.DSS_Executive_Get_CommandHelp(i)))

    def Option(self, i: int) -> str:
        '''Get i-th option'''
        return self._get_string(self.CheckForError(self._lib.DSS_Executive_Get_Option(i)))

    def OptionHelp(self, i: int) -> str:
        '''Get help string for i-th option'''
        return self._get_string(self.CheckForError(self._lib.DSS_Executive_Get_OptionHelp(i)))

    def OptionValue(self, i: int) -> str:
        '''Get present value of i-th option'''
        return self._get_string(self.CheckForError(self._lib.DSS_Executive_Get_OptionValue(i)))

    @property
    def NumCommands(self) -> int:
        '''Number of DSS Executive Commands'''
        return self.CheckForError(self._lib.DSS_Executive_Get_NumCommands())

    @property
    def NumOptions(self) -> int:
        '''Number of DSS Executive Options'''
        return self.CheckForError(self._lib.DSS_Executive_Get_NumOptions())

