'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base
import warnings
from .ICircuit import ICircuit
from .IError import IError
from .IText import IText
from .IDSSProgress import IDSSProgress
from .IActiveClass import IActiveClass
from .IDSS_Executive import IDSS_Executive
from .IDSSEvents import IDSSEvents
from .ICmathLib import ICmathLib
from .IParser import IParser
from .IDSSimComs import IDSSimComs
from .IYMatrix import IYMatrix

class IDSS(Base):
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
    ]

    def __init__(self, api_util):
        self.ActiveCircuit = ICircuit(api_util)
        self.Circuits = ICircuit(api_util)
        self.Error = IError(api_util)
        self.Text = IText(api_util)
        # self.NewCircuit = ICircuit(api_util)
        self.DSSProgress = IDSSProgress(api_util)
        self.ActiveClass = IActiveClass(api_util)
        self.Executive = IDSS_Executive(api_util)
        self.Events = IDSSEvents(api_util)
        self.CmathLib = ICmathLib(api_util)
        self.Parser = IParser(api_util)
        self.DSSim_Coms = IDSSimComs(api_util)
        self.YMatrix = IYMatrix(api_util)

        Base.__init__(self, api_util)    

        
    def ClearAll(self):
        self._lib.DSS_ClearAll()

    def Reset(self):
        self._lib.DSS_Reset()

    def SetActiveClass(self, ClassName):
        if type(ClassName) is not bytes:
            ClassName = ClassName.encode(self._api_util.codec)

        return self._lib.DSS_SetActiveClass(ClassName)

    def Start(self, code):
        return self._lib.DSS_Start(code) != 0

    @property
    def Classes(self):
        '''(read-only) List of DSS intrinsic classes (names of the classes)'''
        return self._get_string_array(self._lib.DSS_Get_Classes)

    @property
    def DataPath(self):
        '''DSS Data File Path.  Default path for reports, etc. from DSS'''
        return self._get_string(self._lib.DSS_Get_DataPath())

    @DataPath.setter
    def DataPath(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.DSS_Set_DataPath(Value)
        self.CheckForError()

    @property
    def DefaultEditor(self):
        '''(read-only) Returns the path name for the default text editor.'''
        return self._get_string(self._lib.DSS_Get_DefaultEditor())

    @property
    def NumCircuits(self):
        '''(read-only) Number of Circuits currently defined'''
        return self._lib.DSS_Get_NumCircuits()

    @property
    def NumClasses(self):
        '''(read-only) Number of DSS intrinsic classes'''
        return self._lib.DSS_Get_NumClasses()

    @property
    def NumUserClasses(self):
        '''(read-only) Number of user-defined classes'''
        return self._lib.DSS_Get_NumUserClasses()

    @property
    def UserClasses(self):
        '''(read-only) List of user-defined classes'''
        return self._get_string_array(self._lib.DSS_Get_UserClasses)

    @property
    def Version(self):
        '''(read-only) Get version string for the DSS.'''
        return self._get_string(self._lib.DSS_Get_Version())

    @property
    def AllowForms(self):
        '''Gets/sets whether text output is allowed'''
        return self._lib.DSS_Get_AllowForms() != 0

    @AllowForms.setter
    def AllowForms(self, value):
        self._lib.DSS_Set_AllowForms(value)
        self.CheckForError()

    def ShowPanel(self):
        warnings.warn('ShowPanel is not implemented.')

    def NewCircuit(self, name):
        if type(name) is not bytes:
            name = name.encode(self._api_util.codec)

        self._lib.DSS_NewCircuit(name)
        self.CheckForError()

        return self.ActiveCircuit
