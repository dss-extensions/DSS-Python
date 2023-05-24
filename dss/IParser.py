'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira

Copyright (c) 2018-2022 DSS-Extensions contributors
'''
from ._cffi_api_util import Base
from ._types import Float64Array
from typing import AnyStr

class IParser(Base):
    __slots__ = []
    
    _columns = [
        'Delimiters', 'EndQuote', 'CmdString', 'BeginQuote', 'WhiteSpace', 'AutoIncrement',
    ]

    def Matrix(self, ExpectedOrder: int) -> Float64Array:
        '''Use this property to parse a Matrix token in OpenDSS format.  Returns square matrix of order specified. Order same as default Fortran order: column by column.'''
        self.CheckForError(self._lib.Parser_Get_Matrix_GR(ExpectedOrder))
        return self._get_float64_gr_array()

    def SymMatrix(self, ExpectedOrder: int) -> Float64Array:
        '''Use this property to parse a matrix token specified in lower triangle form. Symmetry is forced.'''
        self.CheckForError(self._lib.Parser_Get_SymMatrix_GR(ExpectedOrder))
        return self._get_float64_gr_array()

    def Vector(self, ExpectedSize: int) -> Float64Array:
        '''Returns token as array of doubles. For parsing quoted array syntax.'''
        self.CheckForError(self._lib.Parser_Get_Vector_GR(ExpectedSize))
        return self._get_float64_gr_array()

    def ResetDelimiters(self):
        self.CheckForError(self._lib.Parser_ResetDelimiters())

    @property
    def AutoIncrement(self) -> bool:
        '''Default is FALSE. If TRUE parser automatically advances to next token after DblValue, IntValue, or StrValue. Simpler when you don't need to check for parameter names.'''
        return self.CheckForError(self._lib.Parser_Get_AutoIncrement()) != 0

    @AutoIncrement.setter
    def AutoIncrement(self, Value: bool):
        self.CheckForError(self._lib.Parser_Set_AutoIncrement(Value))

    @property
    def BeginQuote(self) -> str:
        '''
        Get/Set String containing the the characters for Quoting in OpenDSS scripts. Matching pairs defined in EndQuote. Default is "'([{.
        '''
        return self._get_string(self.CheckForError(self._lib.Parser_Get_BeginQuote()))

    @BeginQuote.setter
    def BeginQuote(self, Value: AnyStr):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Parser_Set_BeginQuote(Value))

    @property
    def CmdString(self) -> str:
        '''String to be parsed. Loading this string resets the Parser to the beginning of the line. Then parse off the tokens in sequence.'''
        return self._get_string(self.CheckForError(self._lib.Parser_Get_CmdString()))

    @CmdString.setter
    def CmdString(self, Value: AnyStr):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Parser_Set_CmdString(Value))

    @property
    def DblValue(self) -> float:
        '''Return next parameter as a double.'''
        return self.CheckForError(self._lib.Parser_Get_DblValue())

    @property
    def Delimiters(self) -> str:
        '''String defining hard delimiters used to separate token on the command string. Default is , and =. The = separates token name from token value. These override whitesspace to separate tokens.'''
        return self._get_string(self.CheckForError(self._lib.Parser_Get_Delimiters()))

    @Delimiters.setter
    def Delimiters(self, Value: AnyStr):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Parser_Set_Delimiters(Value))

    @property
    def EndQuote(self) -> str:
        '''String containing characters, in order, that match the beginning quote characters in BeginQuote. Default is "')]}'''
        return self._get_string(self.CheckForError(self._lib.Parser_Get_EndQuote()))

    @EndQuote.setter
    def EndQuote(self, Value: AnyStr):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Parser_Set_EndQuote(Value))

    @property
    def IntValue(self) -> int:
        '''Return next parameter as a long integer.'''
        return self.CheckForError(self._lib.Parser_Get_IntValue())

    @property
    def NextParam(self) -> str:
        '''Get next token and return tag name (before = sign) if any. See AutoIncrement.'''
        return self._get_string(self.CheckForError(self._lib.Parser_Get_NextParam()))

    @property
    def StrValue(self) -> str:
        '''Return next parameter as a string'''
        return self._get_string(self.CheckForError(self._lib.Parser_Get_StrValue()))

    @property
    def WhiteSpace(self) -> str:
        '''
        Get/set the characters used for White space in the command string.  Default is blank and Tab.
        '''
        return self._get_string(self.CheckForError(self._lib.Parser_Get_WhiteSpace()))

    @WhiteSpace.setter
    def WhiteSpace(self, Value: AnyStr):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Parser_Set_WhiteSpace(Value))

