'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira
Copyright (c) 2018-2022 DSS Extensions contributors
'''
from .._cffi_api_util import Base
import warnings
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
    Main OpenDSS interface
    '''
    __slots__ = [
        'ActiveCircuit',
        'Circuits',
        'Error',
        'Text',
        # 'NewCircuit',
        'DSSProgress',
        'ActiveClass',
        'Executive',
        'Events',
        'CmathLib',
        'Parser',
        'DSSim_Coms',
        'YMatrix',
        'ZIP',
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

    def __init__(self, api_util):
        self.ActiveCircuit = ICircuit(api_util)
        '''ActiveCircuit: provides access to the circuit attributes and objects. '''
        
        self.Circuits = ICircuit(api_util)
        self.Error = IError(api_util)
        self.Text = IText(api_util)
        # self.NewCircuit = ICircuit(api_util)
        self.DSSProgress = IDSSProgress(api_util)
        self.ActiveClass = IActiveClass(api_util)
        self.Executive = IDSS_Executive(api_util)
        self.Events = IDSSEvents(api_util)
        self.Parser = IParser(api_util)
        self.DSSim_Coms = IDSSimComs(api_util)
        self.YMatrix = IYMatrix(api_util)
        self.ZIP = IZIP(api_util)

        Base.__init__(self, api_util)    

        
    def ClearAll(self):
        self.CheckForError(self._lib.DSS_ClearAll())

    def Reset(self):
        self.CheckForError(self._lib.DSS_Reset())

    def SetActiveClass(self, ClassName):
        if type(ClassName) is not bytes:
            ClassName = ClassName.encode(self._api_util.codec)

        return self.CheckForError(self._lib.DSS_SetActiveClass(ClassName))

    def Start(self, code):
        return self.CheckForError(self._lib.DSS_Start(code)) != 0

    @property
    def Classes(self):
        '''(read-only) List of DSS intrinsic classes (names of the classes)'''
        return self.CheckForError(self._get_string_array(self._lib.DSS_Get_Classes))

    @property
    def DataPath(self):
        '''DSS Data File Path.  Default path for reports, etc. from DSS'''
        return self._get_string(self.CheckForError(self._lib.DSS_Get_DataPath()))

    @DataPath.setter
    def DataPath(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.DSS_Set_DataPath(Value))

    @property
    def DefaultEditor(self):
        '''(read-only) Returns the path name for the default text editor.'''
        return self._get_string(self.CheckForError(self._lib.DSS_Get_DefaultEditor()))

    @property
    def NumCircuits(self):
        '''(read-only) Number of Circuits currently defined'''
        return self.CheckForError(self._lib.DSS_Get_NumCircuits())

    @property
    def NumClasses(self):
        '''(read-only) Number of DSS intrinsic classes'''
        return self.CheckForError(self._lib.DSS_Get_NumClasses())

    @property
    def NumUserClasses(self):
        '''(read-only) Number of user-defined classes'''
        return self.CheckForError(self._lib.DSS_Get_NumUserClasses())

    @property
    def UserClasses(self):
        '''(read-only) List of user-defined classes'''
        return self.CheckForError(self._get_string_array(self._lib.DSS_Get_UserClasses))

    @property
    def Version(self):
        '''(read-only) Get version string for the DSS.'''
        return self._get_string(self.CheckForError(self._lib.DSS_Get_Version()))

    @property
    def AllowForms(self):
        '''Gets/sets whether text output is allowed'''
        return self.CheckForError(self._lib.DSS_Get_AllowForms()) != 0

    @AllowForms.setter
    def AllowForms(self, value):
        self.CheckForError(self._lib.DSS_Set_AllowForms(value))

    @property
    def AllowEditor(self):
        '''
        Gets/sets whether running the external editor for "Show" is allowed
        
        AllowEditor controls whether the external editor is used in commands like "Show".
        If you set to 0 (false), the editor is not executed. Note that other side effects,
        such as the creation of files, are not affected.
        '''
        return self.CheckForError(self._lib.DSS_Get_AllowEditor()) != 0

    @AllowEditor.setter
    def AllowEditor(self, value):
        self.CheckForError(self._lib.DSS_Set_AllowEditor(value))

    def ShowPanel(self):
        warnings.warn('ShowPanel is not implemented.')

    def NewCircuit(self, name):
        if type(name) is not bytes:
            name = name.encode(self._api_util.codec)

        self.CheckForError(self._lib.DSS_NewCircuit(name))

        return self.ActiveCircuit

    @property
    def LegacyModels(self):
        '''
        If enabled, the legacy/deprecated models for PVSystem, InvControl, Storage and StorageControl are used.
        In the official OpenDSS version 9.0, the old models where removed. They are temporarily present here
        but may be removed in the near future. If they are important to you, please open an issue on GitHub
        or contact the authors from DSS Extensions: https://github.com/dss-extensions/
        
        After toggling LegacyModels, run a "clear" command and the models will be loaded accordingly.
        Defaults to False. 
        
        This can also be enabled by setting the environment variable DSS_CAPI_LEGACY_MODELS to 1.
        
        (API Extension)
        '''
        return self.CheckForError(self._lib.DSS_Get_LegacyModels()) != 0

    @LegacyModels.setter
    def LegacyModels(self, Value):
        self.CheckForError(self._lib.DSS_Set_LegacyModels(Value))

    @property
    def AllowChangeDir(self):
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
    def AllowChangeDir(self, Value):
        self.CheckForError(self._lib.DSS_Set_AllowChangeDir(Value))
