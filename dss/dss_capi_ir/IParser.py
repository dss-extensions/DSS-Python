'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class IParser(Base):
    __slots__ = []

    def Matrix(self, ExpectedOrder):
        '''(read-only) Use this property to parse a Matrix token in OpenDSS format.  Returns square matrix of order specified. Order same as default Fortran order: column by column.'''
        return self._get_float64_array(self._lib.Parser_Get_Matrix, ExpectedOrder)

    def SymMatrix(self, ExpectedOrder):
        '''(read-only) Use this property to parse a matrix token specified in lower triangle form. Symmetry is forced.'''
        return self._get_float64_array(self._lib.Parser_Get_SymMatrix, ExpectedOrder)

    def Vector(self, ExpectedSize):
        '''(read-only) Returns token as array of doubles. For parsing quoted array syntax.'''
        return self._get_float64_array(self._lib.Parser_Get_Vector, ExpectedSize)

    def ResetDelimiters(self):
        self._lib.Parser_ResetDelimiters()

    @property
    def AutoIncrement(self):
        '''Default is FALSE. If TRUE parser automatically advances to next token after DblValue, IntValue, or StrValue. Simpler when you don't need to check for parameter names.'''
        return self._lib.Parser_Get_AutoIncrement() != 0

    @AutoIncrement.setter
    def AutoIncrement(self, Value):
        self._lib.Parser_Set_AutoIncrement(Value)
        self.CheckForError()

    @property
    def BeginQuote(self):
        '''
        (read) Get String containing the the characters for Quoting in OpenDSS scripts. Matching pairs defined in EndQuote. Default is "'([{.
        (write) Set String containing the the characters for Quoting in OpenDSS scripts. Matching pairs defined in EndQuote. Default is "'([{.
        '''
        return self._get_string(self._lib.Parser_Get_BeginQuote())

    @BeginQuote.setter
    def BeginQuote(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Parser_Set_BeginQuote(Value)
        self.CheckForError()

    @property
    def CmdString(self):
        '''String to be parsed. Loading this string resets the Parser to the beginning of the line. Then parse off the tokens in sequence.'''
        return self._get_string(self._lib.Parser_Get_CmdString())

    @CmdString.setter
    def CmdString(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Parser_Set_CmdString(Value)
        self.CheckForError()

    @property
    def DblValue(self):
        '''(read-only) Return next parameter as a double.'''
        return self._lib.Parser_Get_DblValue()

    @property
    def Delimiters(self):
        '''String defining hard delimiters used to separate token on the command string. Default is , and =. The = separates token name from token value. These override whitesspace to separate tokens.'''
        return self._get_string(self._lib.Parser_Get_Delimiters())

    @Delimiters.setter
    def Delimiters(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Parser_Set_Delimiters(Value)
        self.CheckForError()

    @property
    def EndQuote(self):
        '''String containing characters, in order, that match the beginning quote characters in BeginQuote. Default is "')]}'''
        return self._get_string(self._lib.Parser_Get_EndQuote())

    @EndQuote.setter
    def EndQuote(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Parser_Set_EndQuote(Value)
        self.CheckForError()

    @property
    def IntValue(self):
        '''(read-only) Return next parameter as a long integer.'''
        return self._lib.Parser_Get_IntValue()

    @property
    def NextParam(self):
        '''(read-only) Get next token and return tag name (before = sign) if any. See AutoIncrement.'''
        return self._get_string(self._lib.Parser_Get_NextParam())

    @property
    def StrValue(self):
        '''(read-only) Return next parameter as a string'''
        return self._get_string(self._lib.Parser_Get_StrValue())

    @property
    def WhiteSpace(self):
        '''
        (read) Get the characters used for White space in the command string.  Default is blank and Tab.
        (write) Set the characters used for White space in the command string.  Default is blank and Tab.
        '''
        return self._get_string(self._lib.Parser_Get_WhiteSpace())

    @WhiteSpace.setter
    def WhiteSpace(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Parser_Set_WhiteSpace(Value)
        self.CheckForError()

