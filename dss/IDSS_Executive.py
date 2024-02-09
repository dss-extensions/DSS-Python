# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Base

class IDSS_Executive(Base):
    __slots__ = []

    _columns = [
        'NumCommands', 
        'NumOptions',
    ]

    def Command(self, i: int) -> str:
        '''
        Get i-th command

        Original COM help: https://opendss.epri.com/Command.html
        '''
        return self._get_string(self._check_for_error(self._lib.DSS_Executive_Get_Command(i)))

    def CommandHelp(self, i: int) -> str:
        '''
        Get help string for i-th command

        Original COM help: https://opendss.epri.com/CommandHelp.html
        '''
        return self._get_string(self._check_for_error(self._lib.DSS_Executive_Get_CommandHelp(i)))

    def Option(self, i: int) -> str:
        '''
        Get i-th option

        Original COM help: https://opendss.epri.com/Option.html
        '''
        return self._get_string(self._check_for_error(self._lib.DSS_Executive_Get_Option(i)))

    def OptionHelp(self, i: int) -> str:
        '''
        Get help string for i-th option

        Original COM help: https://opendss.epri.com/OptionHelp.html
        '''
        return self._get_string(self._check_for_error(self._lib.DSS_Executive_Get_OptionHelp(i)))

    def OptionValue(self, i: int) -> str:
        '''
        Get present value of i-th option

        Original COM help: https://opendss.epri.com/OptionValue.html
        '''
        return self._get_string(self._check_for_error(self._lib.DSS_Executive_Get_OptionValue(i)))

    @property
    def NumCommands(self) -> int:
        '''
        Number of DSS Executive Commands

        Original COM help: https://opendss.epri.com/NumCommands.html
        '''
        return self._check_for_error(self._lib.DSS_Executive_Get_NumCommands())

    @property
    def NumOptions(self) -> int:
        '''
        Number of DSS Executive Options

        Original COM help: https://opendss.epri.com/NumOptions.html
        '''
        return self._check_for_error(self._lib.DSS_Executive_Get_NumOptions())

