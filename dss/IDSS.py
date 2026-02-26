# A compatibility layer for DSS C-API that mimics EPRI's OpenDSS COM interface.
# Copyright (c) 2016-2025 Paulo Meira
# Copyright (c) 2018-2025 DSS-Extensions contributors
from __future__ import annotations
import warnings
from weakref import WeakKeyDictionary
from typing import Any, List, Union, AnyStr, TYPE_CHECKING
from ._cffi_api_util import Base, AltDSSAPIUtil, DSSException
from .ICircuit import ICircuit
from .IError import IError
from .IText import IText
from .IDSSProgress import IDSSProgress
from .IActiveClass import IActiveClass
from .IDSS_Executive import IDSS_Executive
from .IDSSEvents import IDSSEvents
from .IParser import IParser
from .ISettings import ISettings
from .IYMatrix import IYMatrix
from .IZIP import IZIP

if TYPE_CHECKING:
    try:
        from altdss import AltDSS
    except:
        pass

    try:
        from opendssdirect.OpenDSSDirect import OpenDSSDirect
    except:
        pass

class IDSS(Base):
    '''
    Main OpenDSS interface. Organizes the subclasses trying to mimic the `OpenDSSengine.DSS` object
    as seen from `win32com.client` or `comtypes.client`.

    This main class also includes some global settings. Most settings at being moved to the dediced 
    `Settings` interface, exposed in the shortcut `Settings` of this object, or `ActiveCircuit.Settings`.
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
        'YMatrix',
        'ZIP',
        '_version',
        '_altdss',
        '_plotter',
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

    _ctx_to_dss = WeakKeyDictionary()

    ActiveCircuit: ICircuit
    Circuits: ICircuit
    Error: IError
    Text: IText
    DSSProgress: IDSSProgress
    ActiveClass: IActiveClass
    Executive: IDSS_Executive
    Events: IDSSEvents
    Parser: IParser
    YMatrix: IYMatrix
    ZIP: IZIP

    @classmethod
    def _get_instance(cls: IDSS, api_util: AltDSSAPIUtil = None, ctx=None) -> IDSS:
        '''
        If there is an existing instance for a DSSContext, returns it.
        Otherwise, tries to wrap the context into a new DSS-Python API instance.
        '''
        if api_util is None:
            # If none exists, something is probably wrong elsewhere,
            # so let's allow the IndexError to propagate
            api_util = AltDSSAPIUtil._ctx_to_util[ctx]

        dss = cls._ctx_to_dss.get(api_util.ctx)
        if dss is None:
            dss = cls(api_util)

        return dss

    def __init__(self, api_util):
        '''
        Wrap a new DSS context with the DSS-Python API.
        This is not typically used directly. Refer to `IDSS.NewContext` or
        `IDSS._get_instance`.

        For Oddie-wrapped libraries (EPRI's OpenDSS and OpenDSS-C), prefer the dedicated constructors and classes
        (e.g. `IOddieDSS`, `EPRIOpenDSSC`, `EPRIOpenDSS`).
        '''

        if api_util.ctx not in IDSS._ctx_to_dss:
            IDSS._ctx_to_dss[api_util.ctx] = self

        if api_util._dss_python is None:
            api_util._dss_python = self

        self._version = None
        self._plotter = None

        #: Provides access to the circuit attributes and objects in general.
        self.ActiveCircuit = ICircuit(api_util)
        
        #: Kept for compatibility. Currently it is an alias to ActiveCircuit.
        self.Circuits = ICircuit(api_util)
        
        #: The Error interface provides the current error state and messages. In DSS-Python
        #: and DSS-Extensions in general, this is already mapped to exceptions, so the user
        #: typically does not need to worry about this.
        self.Error = IError(api_util)
        
        #: Provides access to command
        self.Text = IText(api_util)

        # self.NewCircuit = ICircuit(api_util)

        #: Kept for compatibility. Controls the progress dialog/output, if available.
        self.DSSProgress = IDSSProgress(api_util)

        #: General information about the current active DSS class.
        self.ActiveClass = IActiveClass(api_util)
        
        #: Access to the list of available commands and options, including help text.
        self.Executive = IDSS_Executive(api_util)
        
        #: Kept for compatibility.
        self.Events = IDSSEvents(api_util) if not api_util._is_oddie else None
        
        #: Kept for compatibility.
        self.Parser = IParser(api_util)
        
        #: The YMatrix interface provides advanced access to the internals of
        #: the DSS engine. The sparse admittance matrix of the system is also 
        #: available here.
        #: 
        #: The original OpenDSSDirect.DLL had some `YMatrix_*` functions, but we 
        #: add a lot more here.
        #: 
        #: **(API Extension)**
        self.YMatrix = IYMatrix(api_util)
        
        #: The ZIP interface provides functions to open compressed ZIP packages
        #: and run scripts inside the ZIP, without creating extra files on disk.
        #: 
        #: **(API Extension)**
        self.ZIP = IZIP(api_util) if not api_util._is_oddie else None

        Base.__init__(self, api_util)    

    @property
    def Obj(self) -> AltDSS:
        """
        Deprecated: provides access to the AltDSS API; use `DSS.to_altdss()` instead

        **(API Extension)**
        """
        warnings.warn('Obj identifier is deprecated; use the `to_altdss()` method instead, or import AltDSS directly ("from altdss import altdss") when using it stand-alone.', DeprecationWarning, stacklevel=2)
        return self.to_altdss()
    
    def to_altdss(self) -> AltDSS:
        """
        Returns an instance of AltDSS for the active DSS Context.

        A compatible AltDSS (`pip install altdss`) is required.
        """
        from altdss import AltDSS
        return AltDSS._get_instance(ctx=self._api_util.ctx, api_util=self._api_util)

    def to_opendssdirect(self) -> OpenDSSDirect:
        """
        Returns an instance of OpenDSSDirect.py for the active DSS Context.

        A compatible OpenDSSDirect.py (`pip install OpenDSSDirect.py`) is required.
        """
        from opendssdirect.OpenDSSDirect import OpenDSSDirect
        return OpenDSSDirect._get_instance(ctx=self._api_util.ctx, api_util=self._api_util)

    def is_oddie(self) -> bool:
        """
        Returns True if this instance is based on the Oddie compatibility layer for
        EPRI's OpenDSS Direct API (a.k.a. DCSL).
        
        Note that the default engine in DSS-Python has been based on AltDSS since
        2018, even though it was not called AltDSS then.
        """
        return self._api_util._is_oddie

    def ClearAll(self):
        self._lib.DSS_ClearAll()

    def Reset(self):
        '''
        This is a no-op function, does nothing. Left for compatibility.

        Original COM help: https://opendss.epri.com/Reset1.html
        '''
        self._lib.DSS_Reset()

    def SetActiveClass(self, ClassName: AnyStr) -> int:
        return self._lib.DSS_SetActiveClass(ClassName)

    def Start(self, code: int) -> bool:
        '''
        This is a no-op function, does nothing. Left for compatibility.
        
        Calling `Start` in AltDSS/DSS-Extensions is required but that is already
        handled automatically, so the users do not need to call it manually,
        unless using AltDSS/DSS C-API directly without further tools.

        On EPRI's OpenDSS, `Start` also does nothing at all in the current
        Delphi versions. It is required for OpenDSS-C, but also handled behind
        the scenes on DSS-Extensions.

        Original COM help: https://opendss.epri.com/Start.html
        '''
        return self._lib.DSS_Start(code)

    @property
    def Classes(self) -> List[str]:
        '''
        List of DSS intrinsic classes (names of the classes)

        Original COM help: https://opendss.epri.com/Classes1.html
        '''
        return self._lib.DSS_Get_Classes()

    @property
    def DataPath(self) -> str:
        '''
        DSS Data File Path.  Default path for reports, etc. from DSS

        Original COM help: https://opendss.epri.com/DataPath.html
        '''
        return self._lib.DSS_Get_DataPath()

    @DataPath.setter
    def DataPath(self, Value: AnyStr):
        self._lib.DSS_Set_DataPath(Value)

    @property
    def DefaultEditor(self) -> str:
        '''
        Returns the path name for the default text editor.

        Original COM help: https://opendss.epri.com/DefaultEditor.html
        '''
        return self._lib.DSS_Get_DefaultEditor()

    @property
    def NumCircuits(self) -> int:
        '''
        Number of Circuits currently defined

        Original COM help: https://opendss.epri.com/NumCircuits.html
        '''
        return self._lib.DSS_Get_NumCircuits()

    @property
    def NumClasses(self) -> int:
        '''
        Number of DSS intrinsic classes

        Original COM help: https://opendss.epri.com/NumClasses.html
        '''
        return self._lib.DSS_Get_NumClasses()

    @property
    def NumUserClasses(self) -> int:
        '''
        Number of user-defined classes

        Original COM help: https://opendss.epri.com/NumUserClasses.html
        '''
        return self._lib.DSS_Get_NumUserClasses()

    @property
    def UserClasses(self) -> List[str]:
        '''
        List of user-defined classes

        Original COM help: https://opendss.epri.com/UserClasses.html
        '''
        return self._lib.DSS_Get_UserClasses()

    @property
    def Version(self) -> str:
        '''
        Get version string for the DSS.

        Original COM help: https://opendss.epri.com/Version.html
        '''

        if self._version is None:
            from . import __version__ as dss_python_version
            self._version = dss_python_version

        return self._lib.DSS_Get_Version() + f'\nDSS-Python version: {self._version}'

    @property
    def AllowForms(self) -> bool:
        '''
        Indicates whether text output is allowed or forms are used. Disable to silence most output.

        Currently, forms/windows are only used for EPRI's OpenDSS distribution on Windows.

        Original COM help: https://opendss.epri.com/AllowForms.html
        '''
        return self._lib.DSS_Get_AllowForms()

    @AllowForms.setter
    def AllowForms(self, value: bool):
        self._lib.DSS_Set_AllowForms(value)

    @property
    def AllowEditor(self) -> bool:
        '''
        Gets/sets whether running the external editor for "Show" is allowed
        
        AllowEditor controls whether the external editor is used in commands like "Show".
        If you set to 0 (false), the editor is not executed. Note that other side effects,
        such as the creation of files, are not affected.

        **Deprecated:** Use `Settings.AllowEditor` instead (same behavior, the setting was just moved there for better organization).

        **(API Extension)**
        '''
        warnings.warn('"AllowEditor" was moved to the Settings interface. This property still works, but will be removed in a future release. Please use `...Settings.AllowEditor` instead.', DeprecationWarning, stacklevel=2)
        return self._lib.DSS_Get_AllowEditor()

    @AllowEditor.setter
    def AllowEditor(self, value: bool):
        self._lib.DSS_Set_AllowEditor(value)

    def ShowPanel(self):
        if api_util._is_oddie:
            self._lib.Text_Set_Command('panel')

    def NewCircuit(self, name) -> ICircuit:
        '''
        Make a new circuit and returns the interface to the active circuit.

        Original COM help: https://opendss.epri.com/NewCircuit.html
        '''
        self._lib.DSS_NewCircuit(name)

        return self.ActiveCircuit

    @property
    def LegacyModels(self) -> bool:
        '''
        LegacyModels was a flag used to toggle legacy (pre-2019) models for PVSystem, InvControl, Storage and
        StorageControl.
        In EPRI's OpenDSS version 9.0, the old models were removed. They were temporarily present here
        but were also removed in DSS C-API v0.13.0.
            
        **NOTE**: this property will be removed for v1.0. It is left to avoid breaking the current API too soon.
        
        **(API Extension)**
        '''
        return self._lib.DSS_Get_LegacyModels()

    @LegacyModels.setter
    def LegacyModels(self, Value: bool):
        self._lib.DSS_Set_LegacyModels(Value)

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
        
        **Deprecated:** Use `Settings.AllowChangeDir` instead (same behavior, the setting was just moved there for better organization).

        **(API Extension)**
        '''
        warnings.warn('"AllowChangeDir" was moved to the Settings interface. This property still works, but will be removed in a future release. Please use `...Settings.AllowChangeDir` instead.', DeprecationWarning, stacklevel=2)
        return self._lib.DSS_Get_AllowChangeDir()

    @AllowChangeDir.setter
    def AllowChangeDir(self, Value: bool):
        self._lib.DSS_Set_AllowChangeDir(Value)

    @property
    def AllowDOScmd(self) -> bool:
        '''
        If enabled, the `DOScmd` command is allowed. Otherwise, an error is reported if the user tries to use it.

        Defaults to False/0 (disabled state). Users should consider DOScmd deprecated on DSS-Extensions.

        This can also be set through the environment variable `DSS_CAPI_ALLOW_DOSCMD`. Setting it to 1 enables
        the command.

        **Deprecated:** Use `Settings.AllowDOScmd` instead (same behavior, the setting was just moved there for better organization).

        **(API Extension)**
        '''
        warnings.warn('"AllowDOScmd" was moved to the Settings interface. This property still works, but will be removed in a future release. Please use `...Settings.AllowDOScmd` instead.', DeprecationWarning, stacklevel=2)
        return self._lib.DSS_Get_AllowDOScmd()

    @AllowDOScmd.setter
    def AllowDOScmd(self, Value: bool):
        self._lib.DSS_Set_AllowDOScmd(Value)

    @property
    def COMErrorResults(self) -> bool:
        '''
        If enabled, in case of errors or empty arrays, the API returns arrays with values compatible with 
        EPRI's OpenDSS COM interface. 

        For example, consider the function `Loads_Get_ZIPV`. If there is no active circuit or active load element:

        - In the disabled state (`COMErrorResults`=False), the function will return "[]", an array with 0 elements.
        - In the enabled state (`COMErrorResults`=True), the function will return "[0.0]" instead. This should
        be compatible with the return value of EPRI's OpenDSS COM interface.

        Defaults to false (disabled state) in AltDSS since the v0.15.x series.

        This does not affect the results when using EPRI's OpenDSS distribution through Oddie.

        This can also be set through the environment variable `DSS_CAPI_COM_DEFAULTS`. Setting it to 1 enables
        the legacy/COM behavior. The value can be toggled through the API at any time.

        **Deprecated:** Use `Settings.COMErrorResults` instead (same behavior, the setting was just moved there for better organization).

        **(API Extension)**
        '''
        warnings.warn('"COMErrorResults" was moved to the Settings interface. This property still works, but will be removed in a future release. Please use `...Settings.COMErrorResults` instead.', DeprecationWarning, stacklevel=2)
        return self._lib.DSS_Get_COMErrorResults()

    @COMErrorResults.setter
    def COMErrorResults(self, Value: bool):
        warnings.warn('"COMErrorResults" was moved to the Settings interface. This property still works, but will be removed in a future release. Please use `...Settings.COMErrorResults` instead.', DeprecationWarning, stacklevel=2)
        self._lib.DSS_Set_COMErrorResults(Value)

    def NewContext(self) -> IDSS:
        '''
        Creates a new DSS engine context.

        A DSS Context encapsulates most of the global state of the original OpenDSS engine,
        allowing the user to create multiple instances in the same process. By creating contexts
        manually, the management of threads and potential issues should be handled by the user.

        **(API Extension)**
        '''

        if self._api_util._is_oddie:
            raise NotImplementedError("NewContext is not supported for the EPRI's OpenDSS engines.")

        ffi = self._api_util.ffi
        lib = self._api_util.lib_unpatched
        new_ctx = ffi.gc(lib.ctx_New(), lib.ctx_Dispose)
        new_api_util = AltDSSAPIUtil(ffi, lib, new_ctx, parent=self._api_util)
        return IDSS(new_api_util)

    def __call__(self, cmds: Union[AnyStr, List[AnyStr]]):
        '''
        Shortcut to pass text commands.

        Pass either a single string (with either one or multiples commands, separated by new lines),
        or a list of strings.

        Examples:

            # single command
            DSS("new Circuit.test") 

            # list of commands
            DSS(["new Circuit.test", "new Line.line1 bus1=a bus2=b"])

            # block of commands in a big string
            DSS("""
                clear
                new Circuit.test
                new Line.line1 bus1=a bus2=b
                new Load.load1 bus1=a bus2=b
            """)

        **(API Extension)**
        '''
        self.Text.Commands(cmds)

    @property
    def Plotting(self):
        '''
        Shortcut for the plotting tools for the current DSS engine.

        *Previously, this was just a shortcut to the plotting module. Since
        the plotting tools were extended and refactored, an instance 
        of the DSS plotter is return, allowing the user to plot from 
        multiple instances and different engines.*

        Gives access to the `enable()`/`disable()` functions, and the new
        experimental plotting API in Python.

        Requires matplotlib and SciPy to be installed, hence it is an optional 
        feature, lazily imported.

        **(API Extension)**
        '''
        if self._plotter is None:
            from dss.plot import get_plotter
            self._plotter = get_plotter(self)

        return self._plotter

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

        **Deprecated:** Use `Settings.AdvancedTypes` instead (same behavior, the setting was just moved there for better organization).
        
        **(API Extension)**
        '''
        return self._lib.advanced_types

    @AdvancedTypes.setter
    def AdvancedTypes(self, Value: bool):
        warnings.warn('"AdvancedTypes" was moved to the Settings interface. This property still works, but will be removed in a future release. Please use `...Settings.AdvancedTypes` instead.', DeprecationWarning, stacklevel=2)
        self._lib.advanced_types = bool(Value)

    @property
    def CompatFlags(self) -> int:
        '''
        Controls some compatibility flags introduced to toggle some behavior from EPRI's OpenDSS.

        **THE FLAGS ARE GLOBAL, affecting all AltDSS engines in the process.**  
        CompatFlags for Oddie-loaded instances (OpenDSS and OpenDSS-C engines) are handled by the Oddie code itself,
        so it is global for each Oddie library.

        These flags may change for each version of DSS C-API, but the same value will not be reused. That is,
        when we remove a compatibility flag, it will have no effect but will also not affect anything else
        besides raising an error if the user tries to toggle a flag that was available in a previous version.

        We expect to keep a very limited number of flags. Since the flags are more transient than the other
        options/flags, it was preferred to add this generic function instead of a separate function per
        flag.

        See the enumeration `DSSCompatFlags` for available flags, including description.

        **Deprecated:** Use `Settings.CompatFlags` instead (same behavior, the setting was just moved there for better organization).

        **(API Extension)**
        '''
        return self._lib.DSS_Get_CompatFlags()

    @CompatFlags.setter
    def CompatFlags(self, Value: int):
        warnings.warn('"CompatFlags" was moved to the Settings interface. This property still works, but will be removed in a future release. Please use `...Settings.CompatFlags` instead.', DeprecationWarning, stacklevel=2)
        self._lib.DSS_Set_CompatFlags(Value)


    def ShareGeneral(self, otherContext: IDSS, skip_cmds: Optional[List[str]] = None, skip_file_regexp: str = None):
        '''
        Share general DSS objects from this AltDSS context to another.

        **WARNING:** currently, the pointers are not tracked! The user must ensure this context
        and its objects are kept alive while other contexts require it.

        Optionally, as a shortcut, the user can provide `skip_cmds` to be passed to the `Settings.SkipCommands` 
        and `skip_file_regexp` to be passed to `Settings.SkipFileRegExp`, in the second DSS context. 
        
        *Note*: If the `clear` command is included in `Settings.SkipCommands`, the `DSS.ClearAll()` method can still be called
        and it will reset both skip settings.

        ***EXPERIMENTAL***

        **(API Extension)**
        '''
        if self._api_util._is_oddie or otherContext._api_util._is_oddie:
            raise ValueError("Only AltDSS engine contexts can share data.")

        self._lib.ctx_ShareGeneral(otherContext._api_util.ctx)
        if skip_cmds is not None:
            otherContext.ActiveCircuit.Settings.SkipCommands = skip_cmds

        if skip_file_regexp is not None:
            otherContext.ActiveCircuit.Settings.SkipFileRegExp = skip_file_regexp

    @property
    def Settings(self):
        '''
        For convenience, a shortcut to `ActiveCircuit.Settings`.
        '''
        return self.ActiveCircuit.Settings
