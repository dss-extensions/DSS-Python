# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Base

class IError(Base):
    __slots__ = []

    _columns = [
        'Description',
        'Number',
        'EarlyAbort',
    ]
    
    @property
    def Description(self) -> str:
        '''
        Description of error for last operation

        Original COM help: https://opendss.epri.com/Description1.html
        '''
        return self._get_string(self._lib.Error_Get_Description())

    @property
    def Number(self) -> int:
        '''
        Error Number (returns current value and then resets to zero)

        Original COM help: https://opendss.epri.com/Number.html
        '''
        return self._lib.Error_Get_Number()

    @property
    def EarlyAbort(self) -> bool:
        '''
        EarlyAbort controls whether all errors halts the DSS script processing (Compile/Redirect), defaults to True.
        
        **(API Extension)**
        '''
        return self._lib.Error_Get_EarlyAbort() != 0
        
    @EarlyAbort.setter
    def EarlyAbort(self, Value: bool):
        self._lib.Error_Set_EarlyAbort(Value)

    @property
    def ExtendedErrors(self) -> bool:
        '''
        Controls whether the extended error mechanism is used. Defaults to True.
        
        Extended errors are errors derived from checks across the API to ensure
        a valid state. Although many of these checks are already present in the 
        original/official COM interface, the checks do not produce any error 
        message. An error value can be returned by a function but this value
        can, for many of the functions, be a valid value. As such, the user
        has no means to detect an invalid API call. 
        
        Extended errors use the Error interface to provide a more clear message
        and should help users, especially new users, to find usage issues earlier.

        At Python level, an exception is raised when an error is detected through
        the Error interface.
        
        The current default state is ON. For compatibility, the user can turn it
        off to restore the previous behavior.
        
        **(API Extension)**
        '''
        return self._lib.Error_Get_ExtendedErrors() != 0
        
    @ExtendedErrors.setter
    def ExtendedErrors(self, Value: bool):
        self._lib.Error_Set_ExtendedErrors(Value)

    @property
    def UseExceptions(self) -> bool:
        """
        Controls whether the automatic error checking mechanism is enable, i.e., if
        the DSS engine errors (from the `Error` interface) are mapped exception when
        detected. 
        
        **When disabled, the user takes responsibility for checking for errors.**
        This can be done through the `Error` interface. When `Error.Number` is not
        zero, there should be an error message in `Error.Description`. This is compatible
        with the behavior on the official OpenDSS (Windows-only COM implementation) when 
        `AllowForms` is disabled.

        Users can also use the DSS command `Export ErrorLog` to inspect for errors.

        **WARNING:** This is a global setting, affects all DSS instances from DSS-Python,
        OpenDSSDirect.py and AltDSS.

        **(API Extension)**
        """
        return Base._use_exceptions
    
    @UseExceptions.setter
    def UseExceptions(self, value: bool):
        Base._enable_exceptions(value)
