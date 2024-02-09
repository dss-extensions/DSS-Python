# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Base
from typing import AnyStr, List, Union

class IText(Base):
    __slots__ = []

    @property
    def Command(self) -> str:
        '''
        Input command string for the DSS.

        Original COM help: https://opendss.epri.com/Command1.html
        '''
        return self._get_string(self._check_for_error(self._lib.Text_Get_Command()))

    @Command.setter
    def Command(self, Value: str):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Text_Set_Command(Value))

    @property
    def Result(self) -> str:
        '''
        Result string for the last command.

        Original COM help: https://opendss.epri.com/Result.html
        '''
        return self._get_string(self._check_for_error(self._lib.Text_Get_Result()))

    def Commands(self, Value: Union[AnyStr, List[AnyStr]]):
        '''
        Runs a list of strings or a large string as commands directly in the DSS engine.
        Intermediate results (from Text.Result) are ignored.

        Value can be a list of strings, or a single large string (usually faster).

        **(API Extension)**
        '''
        if isinstance(Value, str) or isinstance(Value, bytes):
            if not isinstance(Value, bytes):
                Value = Value.encode(self._api_util.codec)
            
            self._check_for_error(self._lib.Text_CommandBlock(Value))
        else:
            self._check_for_error(self._set_string_array(self._lib.Text_CommandArray, Value))

