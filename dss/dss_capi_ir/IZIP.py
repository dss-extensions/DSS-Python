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
        Opens and prepares a ZIP file to be used by the DSS text parser.
        Currently, the ZIP format support is limited by what is provided in the Free Pascal distribution.
        Besides that, the full filenames inside the ZIP must be shorter than 256 characters.
        The limitations should be removed in a future revision.
        
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

    def Redirect(self, FileName):
        '''
        Runs a "Redirect" command inside the current (open) ZIP file.
        In the current implementation, all files required by the script must
        be present inside the ZIP, using relative paths. The only exceptions are
        memory-mapped files.

        (API Extension)
        '''
        if type(FileName) is not bytes:
            FileName = FileName.encode(self._api_util.codec)

        self.CheckForError(self._lib.ZIP_Redirect(FileName))

    def Extract(self, FileName):
        '''
        Extracts the contents of the file "FileName" from the current (open) ZIP file.
        Returns a byte-string.

        (API Extension)
        '''
        api_util = self._api_util
        ptr = api_util.ffi.new('int8_t**')
        cnt = api_util.ffi.new('int32_t[2]')
        if type(FileName) is not bytes:
            FileName = FileName.encode(api_util.codec)

        self.CheckForError(self._lib.ZIP_Extract(ptr, cnt, FileName))
        result = bytes(api_util.ffi.buffer(ptr[0], cnt[0]))
        self._lib.DSS_Dispose_PByte(ptr)
        return result

    def List(self, regexp=None):
        '''
        List of strings consisting of all names match the regular expression provided in regexp.
        If no expression is provided, all names in the current open ZIP are returned.
        
        See https://regex.sorokin.engineer/en/latest/regular_expressions.html for information on 
        the expression syntax and options.

        (API Extension)
        '''
        if regexp is None or not regexp:
            regexp = self._api_util.ffi.NULL
        else:
            if type(regexp) is not bytes:
                regexp = regexp.encode(self._api_util.codec)
        
        return self.CheckForError(self._get_string_array(self._lib.ZIP_List, regexp))

    def Contains(self, Name):
        '''
        Check if the given path name is present in the current ZIP file.
        
        (API Extension)
        '''
        if type(Name) is not bytes:
            Name = Name.encode(self._api_util.codec)

        return self.CheckForError(self._lib.ZIP_Contains(Name)) != 0

    def __getitem__(self, FileName):
        return self.Extract(FileName)

    def __contains__(self, Name):
        return self.Contains(Name)

