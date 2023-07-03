'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2023 Paulo Meira

Copyright (c) 2018-2023 DSS-Extensions contributors
'''
import warnings
from typing import List, Union, AnyStr
from typing_extensions import Self
from ._cffi_api_util import Base, CffiApiUtil, DSSException
from .ICircuit import ICircuit
from .IError import IError
from .IText import IText
from .IDSSProgress import IDSSProgress
from .IActiveClass import IActiveClass
from .IDSS_Executive import IDSS_Executive
from .IDSSEvents import IDSSEvents
from .IParser import IParser
from .IDSSimComs import IDSSimComs
from .IYMatrix import IYMatrix
from .IZIP import IZIP

class IDSS(Base):
    '''
    Main OpenDSS interface. Organizes the subclasses trying to mimic the `OpenDSSengine.DSS` object
    as seen from `win32com.client` or `comtypes.client`.

    This main class also includes some global settings. See more settings in `ActiveCircuit.Settings`.
    '''
    __slots__ = [
        'ActiveCircuit',
        'Circuits',
        'Error',
        'Text',
        'DSSProgress',
        'ActiveClass',
        'Executive',
        'Events',
        'Parser',
        'DSSim_Coms',
        'YMatrix',
        'ZIP',
        # 'Obj',
        '_version',
        '_obj',
    ]
    
    _columns = [
        'Version', 
        'Classes', 
        'NumUserClasses', 
        'DataPath', 
        'NumClasses', 
        'NumCircuits', 
        'UserClasses', 
        'DefaultEditor',
    ]

    _ctx_to_dss = {}

    ActiveCircuit: ICircuit
    Circuits: ICircuit
    Error: IError
    Text: IText
    DSSProgress: IDSSProgress
    ActiveClass: IActiveClass
    Executive: IDSS_Executive
    Events: IDSSEvents
    Parser: IParser
    DSSim_Coms: IDSSimComs
    YMatrix: IYMatrix
    ZIP: IZIP
    # Obj: IObj

    def __init__(self, api_util):
        if api_util.ctx not in IDSS._ctx_to_dss:
            IDSS._ctx_to_dss[api_util.ctx] = self

        if None not in IDSS._ctx_to_dss:
            # use this as the default instance
            IDSS._ctx_to_dss[None] = self

        self._version = None
        self._obj = None

        #: Provides access to the circuit attributes and objects in general.
        self.ActiveCircuit = ICircuit(api_util)
        
        #: Kept for compatibility. Currently it is an alias to ActiveCircuit.
        self.Circuits = ICircuit(api_util)
        
        #: The Error interface provides the current error state and messages. In DSS-Python, 
        #: this is already mapped to Python exceptions, so the user typpically does not need 
        #: to worry about this.
        self.Error = IError(api_util)
        
        #: Provides access to command
        self.Text = IText(api_util)

        # self.NewCircuit = ICircuit(api_util)

        #: Kept for compatibility. Controls the progress dialog/output, if avaiable.
        self.DSSProgress = IDSSProgress(api_util)

        #: General information about the current active DSS class.
        self.ActiveClass = IActiveClass(api_util)
        
        #: Access to the list of available commands and options, including help text.
        self.Executive = IDSS_Executive(api_util)
        
        #: Kept for compatibility.
        self.Events = IDSSEvents(api_util)
        
        #: Kept for compatibility.
        self.Parser = IParser(api_util)
        
        #: Kept for compatibility. Apparently was used for DSSim-PC (now OpenDSS-G), a 
        #: closed-source software developed by EPRI using LabView.
        self.DSSim_Coms = IDSSimComs(api_util)
        
        #: The YMatrix interface provides advanced access to the internals of
        #: the DSS engine. The sparse admittance matrix of the system is also 
        #: available here.
        #: 
        #: The original OpenDSSDirect.DLL had some `YMatrix_*` functions, but we 
        #: add a lot more here.
        #: 
        #: (API Extension)
        self.YMatrix = IYMatrix(api_util)
        
        #: The ZIP interface provides functions to open compressed ZIP packages
        #: and run scripts inside the ZIP, without creating extra files on disk.
        #: 
        #: (API Extension)
        self.ZIP = IZIP(api_util)

        #: An experimental API that exposes all data classes of the DSS engine in a
        #: new and pythonic API.
        #:
        #: (API Extension)
        # self.Obj = IObj(api_util)

        Base.__init__(self, api_util)    

    @property
    def Obj(self):
        """
        Returns the Obj API instance.
        Since this will be moved out of DSS-Python eventually, the Obj API is created lazily,
        only when the user actually uses it, since it has some overhead.
        """
        if self._obj is not None:
            return self._obj

        #: An experimental API that exposes all data classes of the DSS engine in a
        #: new and pythonic API.
        #:
        #: (API Extension)
        from .IObj import IObj
        self._obj = IObj(self._api_util)
        return self._obj


    def ClearAll(self):
        self.CheckForError(self._lib.DSS_ClearAll())

    def Reset(self):
        self.CheckForError(self._lib.DSS_Reset())

    def SetActiveClass(self, ClassName: AnyStr) -> int:
        if type(ClassName) is not bytes:
            ClassName = ClassName.encode(self._api_util.codec)

        return self.CheckForError(self._lib.DSS_SetActiveClass(ClassName))

    def Start(self, code: int) -> bool:
        return self.CheckForError(self._lib.DSS_Start(code)) != 0

    @property
    def Classes(self) -> List[str]:
        '''List of DSS intrinsic classes (names of the classes)'''
        return self.CheckForError(self._get_string_array(self._lib.DSS_Get_Classes))

    @property
    def DataPath(self) -> str:
        '''DSS Data File Path.  Default path for reports, etc. from DSS'''
        return self._get_string(self.CheckForError(self._lib.DSS_Get_DataPath()))

    @DataPath.setter
    def DataPath(self, Value: AnyStr):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.DSS_Set_DataPath(Value))

    @property
    def DefaultEditor(self) -> str:
        '''Returns the path name for the default text editor.'''
        return self._get_string(self.CheckForError(self._lib.DSS_Get_DefaultEditor()))

    @property
    def NumCircuits(self) -> int:
        '''Number of Circuits currently defined'''
        return self.CheckForError(self._lib.DSS_Get_NumCircuits())

    @property
    def NumClasses(self) -> int:
        '''Number of DSS intrinsic classes'''
        return self.CheckForError(self._lib.DSS_Get_NumClasses())

    @property
    def NumUserClasses(self) -> int:
        '''Number of user-defined classes'''
        return self.CheckForError(self._lib.DSS_Get_NumUserClasses())

    @property
    def UserClasses(self) -> List[str]:
        '''List of user-defined classes'''
        return self.CheckForError(self._get_string_array(self._lib.DSS_Get_UserClasses))

    @property
    def Version(self) -> str:
        '''Get version string for the DSS.'''

        if self._version is None:
            from . import __version__ as dss_python_version
            self._version = dss_python_version

        return self._get_string(self.CheckForError(self._lib.DSS_Get_Version())) + f'\nDSS-Python version: {self._version}'

    @property
    def AllowForms(self) -> bool:
        '''Gets/sets whether text output is allowed'''
        return self.CheckForError(self._lib.DSS_Get_AllowForms()) != 0

    @AllowForms.setter
    def AllowForms(self, value: bool):
        self.CheckForError(self._lib.DSS_Set_AllowForms(value))

    @property
    def AllowEditor(self) -> bool:
        '''
        Gets/sets whether running the external editor for "Show" is allowed
        
        AllowEditor controls whether the external editor is used in commands like "Show".
        If you set to 0 (false), the editor is not executed. Note that other side effects,
        such as the creation of files, are not affected.

        (API Extension)
        '''
        return self.CheckForError(self._lib.DSS_Get_AllowEditor()) != 0

    @AllowEditor.setter
    def AllowEditor(self, value: bool):
        self.CheckForError(self._lib.DSS_Set_AllowEditor(value))

    def ShowPanel(self):
        warnings.warn('ShowPanel is not implemented.')

    def NewCircuit(self, name) -> ICircuit:
        if type(name) is not bytes:
            name = name.encode(self._api_util.codec)

        self.CheckForError(self._lib.DSS_NewCircuit(name))

        return self.ActiveCircuit

    @property
    def LegacyModels(self) -> bool:
        '''
        LegacyModels was a flag used to toggle legacy (pre-2019) models for PVSystem, InvControl, Storage and
        StorageControl.
        In the official OpenDSS version 9.0, the old models were removed. They were temporarily present here
        but were also removed in DSS C-API v0.13.0.
            
        **NOTE**: this property will be removed for v1.0. It is left to avoid breaking the current API too soon.
        
        (API Extension)
        '''
        return self.CheckForError(self._lib.DSS_Get_LegacyModels()) != 0

    @LegacyModels.setter
    def LegacyModels(self, Value: bool):
        self.CheckForError(self._lib.DSS_Set_LegacyModels(Value))

    @property
    def AllowChangeDir(self) -> bool:
        '''
        If disabled, the engine will not change the active working directory during execution. E.g. a "compile"
        command will not "chdir" to the file path.
        
        If you have issues with long paths, enabling this might help in some scenarios.
        
        Defaults to True (allow changes, backwards compatible) in the 0.10.x versions of DSS C-API. 
        This might change to False in future versions.
        
        This can also be set through the environment variable DSS_CAPI_ALLOW_CHANGE_DIR. Set it to 0 to
        disallow changing the active working directory.
        
        (API Extension)
        '''
        return self.CheckForError(self._lib.DSS_Get_AllowChangeDir()) != 0

    @AllowChangeDir.setter
    def AllowChangeDir(self, Value: bool):
        self.CheckForError(self._lib.DSS_Set_AllowChangeDir(Value))

    @property
    def AllowDOScmd(self) -> bool:
        '''
        If enabled, the `DOScmd` command is allowed. Otherwise, an error is reported if the user tries to use it.
        
        Defaults to False/0 (disabled state). Users should consider DOScmd deprecated on DSS-Extensions.
        
        This can also be set through the environment variable DSS_CAPI_ALLOW_DOSCMD. Setting it to 1 enables
        the command.
        
        (API Extension)
        '''
        return self.CheckForError(self._lib.DSS_Get_AllowDOScmd()) != 0

    @AllowDOScmd.setter
    def AllowDOScmd(self, Value: bool):
        self.CheckForError(self._lib.DSS_Set_AllowDOScmd(Value))

    @property
    def COMErrorResults(self) -> bool:
        '''
        If enabled, in case of errors or empty arrays, the API returns arrays with values compatible with the 
        official OpenDSS COM interface. 
        
        For example, consider the function `Loads_Get_ZIPV`. If there is no active circuit or active load element:
        - In the disabled state (COMErrorResults=False), the function will return "[]", an array with 0 elements.
        - In the enabled state (COMErrorResults=True), the function will return "[0.0]" instead. This should
        be compatible with the return value of the official COM interface.
        
        Defaults to True/1 (enabled state) in the v0.12.x series. This will change to false in future series.
        
        This can also be set through the environment variable DSS_CAPI_COM_DEFAULTS. Setting it to 0 disables
        the legacy/COM behavior. The value can be toggled through the API at any time.
        
        (API Extension)
        '''
        return self.CheckForError(self._lib.DSS_Get_COMErrorResults()) != 0

    @COMErrorResults.setter
    def COMErrorResults(self, Value: bool):
        self.CheckForError(self._lib.DSS_Set_COMErrorResults(Value))

    def NewContext(self) -> Self:
        '''
        Creates a new DSS engine context.
        A DSS Context encapsulates most of the global state of the original OpenDSS engine,
        allowing the user to create multiple instances in the same process. By creating contexts
        manually, the management of threads and potential issues should be handled by the user.

        (API Extension)
        '''
        ffi = self._api_util.ffi
        lib = self._api_util.lib_unpatched
        new_ctx = ffi.gc(lib.ctx_New(), lib.ctx_Dispose)
        new_api_util = CffiApiUtil(ffi, lib, new_ctx)
        new_api_util._allow_complex = self._api_util._allow_complex
        return IDSS(new_api_util)

    def __call__(self, single:Union[AnyStr, List[AnyStr]]=None, block : AnyStr = None): #TODO: benchmark and simplify (single argument)
        '''
        Shortcut to pass text commands.

        If `single` is set and is a string, a normal `DSS.Text.Command = single` is called.
        Otherwise, the value is passed to `DSS.Text.Commands`.

        Examples:

            # single command
            DSS("new Circuit.test") 
            DSS(single="new Circuit.test")

            # list of commands (either will work)
            DSS(["new Circuit.test", "new Line.line1 bus1=a bus2=b"])
            DSS(single=["new circuit.test", "new Line.line1 bus1=a bus2=b"])
            DSS(block=["new circuit.test", "new Line.line1 bus1=a bus2=b"])

            # block of commands in a big string
            DSS(block="""
                clear
                new Circuit.test
                new Line.line1 bus1=a bus2=b
                new Load.load1 bus1=a bus2=b
            """)

        (API Extension)
        '''
        if (single is not None) and (block is not None):
           raise DSSException("Only a single argument is accepted.")

        if (single is None) and (block is None):
           raise DSSException("A value is required.")

        if single is not None:
            self.Text.Command = single
            return

        self.Text.Commands(single or block)

    @property
    def Plotting(self):
        '''
        Shortcut for the plotting module. This property is equivalent to:

        ```
        from dss import plot
        return plot
        ```

        Gives access to the `enable()` and `disable()` functions.
        Requires matplotlib and SciPy to be installed, hence it is an
        optional feature.

        (API Extension)
        '''
        from dss import plot
        return plot

    @property
    def AdvancedTypes(self) -> bool:
        '''
        When enabled, there are **two side-effects**:
        
        - **Per DSS Context:** Complex arrays and complex numbers can be returned and consumed by the Python API.
        - **Global effect:** The low-level API provides matrix dimensions when available (`EnableArrayDimensions` is enabled).
        
        As a result, for example, `DSS.ActiveCircuit.ActiveCktElement.Yprim` is returned as a complex matrix instead
        of a plain array.
        
        When disabled, the legacy plain arrays are used and complex numbers cannot be consumed by the Python API.

        *Defaults to **False** for backwards compatibility.*
        
        (API Extension)
        '''
        
        arr_dim = self.CheckForError(self._lib.DSS_Get_EnableArrayDimensions()) != 0
        allow_complex = self._api_util._allow_complex
        return arr_dim and allow_complex

    @AdvancedTypes.setter
    def AdvancedTypes(self, Value: bool):
        self.CheckForError(self._lib.DSS_Set_EnableArrayDimensions(Value))
        self._api_util._allow_complex = bool(Value)

    @property
    def CompatFlags(self) -> int:
        '''
        Controls some compatibility flags introduced to toggle some behavior from the official OpenDSS.

        **THESE FLAGS ARE GLOBAL, affecting all DSS engines in the process.**

        The current bit flags are:

        - 0x1 (bit 0): If enabled, don't check for NaNs in the inner solution loop. This can lead to various errors.
            This flag is useful for legacy applications that don't handle OpenDSS API errors properly. Through the 
            development of DSS-Extensions, we noticed this is actually a quite common issue.
        - 0x2 (bit 1): Toggle worse precision for certain aspects of the engine. For example, the sequence-to-phase 
            (`As2p`) and sequence-to-phase (`Ap2s`) transform matrices. On DSS C-API, we fill the matrix explicitly
            using higher precision, while numerical inversion of an initially worse precision matrix is used in the 
            official OpenDSS. We will introduce better precision for other aspects of the engine in the future, 
            so this flag can be used to toggle the old/bad values where feasible.
        - 0x4 (bit 2): Toggle some InvControl behavior introduced in OpenDSS 9.6.1.1. It could be a regression 
            but needs further investigation, so we added this flag in the time being.

        These flags may change for each version of DSS C-API, but the same value will not be reused. That is,
        when we remove a compatibility flag, it will have no effect but will also not affect anything else
        besides raising an error if the user tries to toggle a flag that was available in a previous version.

        We expect to keep a very limited number of flags. Since the flags are more transient than the other
        options/flags, it was preferred to add this generic function instead of a separate function per
        flag.

        Related enumeration: DSSCompatFlags

        (API Extension)
        '''
        return self.CheckForError(self._lib.DSS_Get_CompatFlags())

    @CompatFlags.setter
    def CompatFlags(self, Value: int):
        self.CheckForError(self._lib.DSS_Set_CompatFlags(Value))
