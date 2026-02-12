# A compatibility layer for DSS C-API that mimics EPRI's OpenDSS COM interface.
# Copyright (c) 2016-2025 Paulo Meira
# Copyright (c) 2018-2025 DSS-Extensions contributors
from ._cffi_api_util import Base
from ._types import Float64Array, Int32Array
from typing import AnyStr, Union, List
from .enums import DSSPropertyNameStyle, CktModels


class SettingsContext:
    def __init__(self, settings):
        self._settings = settings
    
    def __enter__(self):
        # Using try...except since the official engine doesn't implement these.
        # Only a few are (and can be) implemented through Oddie.
        try:
            self._AdvancedTypes = self._settings.AdvancedTypes
        except:
            pass

        try:
            self._CompatFlags = self._settings.CompatFlags
        except:
            pass

        try:
            self._IterateDisabled = self._settings.IterateDisabled
        except:
            pass
        
        try:
            self._PreferLists = self._settings.PreferLists
        except:
            pass

        try:
            self._SkipCommands = self._settings.SkipCommands
        except:
            pass

        try:
            self._SkipFileRegExp = self._settings.SkipFileRegExp
        except:
            pass

        try:
            self._AllowDOScmd = self._settings.AllowDOScmd
        except:
            pass

        return self._settings
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self._settings.AdvancedTypes = self._AdvancedTypes
        except:
            pass

        try:
            self._settings.CompatFlags = self._CompatFlags
        except:
            pass

        try:
            self._settings.IterateDisabled = self._IterateDisabled
        except:
            pass

        try:
            self._settings.PreferLists = self._PreferLists
        except:
            pass

        try:
            self._settings.SkipCommands = self._SkipCommands
        except:
            pass

        try:
            self._settings.SkipFileRegExp = self._SkipFileRegExp
        except:
            pass

        try:
            self._settings.AllowDOScmd = self._AllowDOScmd
        except:
            pass


class ISettings(Base):
    __slots__ = [
        '_command_dict',
    ]

    _columns = [
        'Trapezoidal',
        'LossRegs',
        'VoltageBases',
        'ZoneLock',
        'EmergVminpu',
        'PriceSignal',
        'CktModel',
        'UEregs',
        'UEweight',
        'PriceCurve',
        'NormVminpu',
        'LossWeight',
        'EmergVmaxpu',
        'AutoBusList',
        'NormVmaxpu',
        'AllowDuplicates',
        'ControlTrace',

        # Commented since we don't have these on Oddie with the official engine
        # 'LoadsTerminalCheck',
        # 'IterateDisabled',
        # 'SkipCommands',
        # 'PreferLists',
        # 'SkipFileRegExp',
        # 'CompatFlags',
        # 'PreserveCase',
    ]


    def __init__(self, api_util):
        Base.__init__(self, api_util)
        num_commands = self._lib.DSS_Executive_Get_NumCommands()
        self._command_dict = {
            self._lib.DSS_Executive_Get_Command(i).lower(): i
            for i in range(1, num_commands + 1)
        }


    def Context(self) -> SettingsContext:
        '''
        Returns a Settings context manager. 
        The context manager saves the values of the tracker settings on enter, 
        restoring them on exit. This allows code to change the settings within 
        the context block and they are restored to the initial values automatically.

        Note: this context manager target DSS-Python settings. Use the equivalent for OpenDSSDirect.py.
        A few settings are shared at engine level.

        Settings tracked:
        - AdvancedTypes
        - CompatFlags
        - IterateDisabled
        - PreferLists
        - SkipCommands
        - SkipFileRegExp
        '''
        return SettingsContext(self)

    @property
    def AllowDuplicates(self) -> bool:
        '''
        Designates whether to allow duplicate names of objects

        False by default.
        
        **NOTE**: for DSS-Extensions, we are considering removing this option in a future 
        release since it has performance impacts even when not used.
        '''
        return self._lib.Settings_Get_AllowDuplicates()

    @AllowDuplicates.setter
    def AllowDuplicates(self, Value: bool):
        self._lib.Settings_Set_AllowDuplicates(Value)

    @property
    def AutoBusList(self) -> str:
        '''
        List of Buses or (File=xxxx) syntax for the AutoAdd solution mode.

        Original COM help: https://opendss.epri.com/AutoBusList.html
        '''
        return self._lib.Settings_Get_AutoBusList()

    @AutoBusList.setter
    def AutoBusList(self, Value: AnyStr):
        self._lib.Settings_Set_AutoBusList(Value)

    @property
    def CktModel(self) -> CktModels:
        '''
        Indicate if the circuit model is positive sequence.

        Original COM help: https://opendss.epri.com/CktModel.html
        '''
        return CktModels(self._lib.Settings_Get_CktModel())

    @CktModel.setter
    def CktModel(self, Value: Union[int, CktModels]):
        self._lib.Settings_Set_CktModel(Value)

    @property
    def ControlTrace(self) -> bool:
        '''
        Denotes whether to trace the control actions to a file.

        Original COM help: https://opendss.epri.com/ControlTrace.html
        '''
        return self._lib.Settings_Get_ControlTrace()

    @ControlTrace.setter
    def ControlTrace(self, Value: bool):
        self._lib.Settings_Set_ControlTrace(Value)

    @property
    def EmergVmaxpu(self) -> float:
        '''
        Per Unit maximum voltage for Emergency conditions.

        Original COM help: https://opendss.epri.com/EmergVmaxpu.html
        '''
        return self._lib.Settings_Get_EmergVmaxpu()

    @EmergVmaxpu.setter
    def EmergVmaxpu(self, Value: float):
        self._lib.Settings_Set_EmergVmaxpu(Value)

    @property
    def EmergVminpu(self) -> float:
        '''
        Per Unit minimum voltage for Emergency conditions.

        Original COM help: https://opendss.epri.com/EmergVminpu.html
        '''
        return self._lib.Settings_Get_EmergVminpu()

    @EmergVminpu.setter
    def EmergVminpu(self, Value: float):
        self._lib.Settings_Set_EmergVminpu(Value)

    @property
    def LossRegs(self) -> Int32Array:
        '''
        Integer array defining which energy meter registers to use for computing losses

        Original COM help: https://opendss.epri.com/LossRegs.html
        '''
        return self._lib.Settings_Get_LossRegs_GR()

    @LossRegs.setter
    def LossRegs(self, Value: Int32Array):
        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)
        self._lib.Settings_Set_LossRegs(ValuePtr, ValueCount)

    @property
    def LossWeight(self) -> float:
        '''
        Weighting factor applied to Loss register values.

        Original COM help: https://opendss.epri.com/LossWeight.html
        '''
        return self._lib.Settings_Get_LossWeight()

    @LossWeight.setter
    def LossWeight(self, Value: float):
        self._lib.Settings_Set_LossWeight(Value)

    @property
    def NormVmaxpu(self) -> float:
        '''
        Per Unit maximum voltage for Normal conditions.

        Original COM help: https://opendss.epri.com/NormVmaxpu.html
        '''
        return self._lib.Settings_Get_NormVmaxpu()

    @NormVmaxpu.setter
    def NormVmaxpu(self, Value: float):
        self._lib.Settings_Set_NormVmaxpu(Value)

    @property
    def NormVminpu(self) -> float:
        '''
        Per Unit minimum voltage for Normal conditions.

        Original COM help: https://opendss.epri.com/NormVminpu.html
        '''
        return self._lib.Settings_Get_NormVminpu()

    @NormVminpu.setter
    def NormVminpu(self, Value: float):
        self._lib.Settings_Set_NormVminpu(Value)

    @property
    def PriceCurve(self) -> str:
        '''
        Name of LoadShape object that serves as the source of price signal data for yearly simulations, etc.

        Original COM help: https://opendss.epri.com/PriceCurve.html
        '''
        return self._lib.Settings_Get_PriceCurve()

    @PriceCurve.setter
    def PriceCurve(self, Value: AnyStr):
        self._lib.Settings_Set_PriceCurve(Value)

    @property
    def PriceSignal(self) -> float:
        '''
        Price Signal for the Circuit

        Original COM help: https://opendss.epri.com/PriceSignal.html
        '''
        return self._lib.Settings_Get_PriceSignal()

    @PriceSignal.setter
    def PriceSignal(self, Value: float):
        self._lib.Settings_Set_PriceSignal(Value)

    @property
    def Trapezoidal(self) -> bool:
        '''
        Gets value of trapezoidal integration flag in energy meters. Defaults to `False`.

        Original COM help: https://opendss.epri.com/Trapezoidal.html
        '''
        return self._lib.Settings_Get_Trapezoidal()

    @Trapezoidal.setter
    def Trapezoidal(self, Value: bool):
        self._lib.Settings_Set_Trapezoidal(Value)

    @property
    def UEregs(self) -> Int32Array:
        '''
        Array of Integers defining energy meter registers to use for computing UE

        Original COM help: https://opendss.epri.com/UEregs.html
        '''
        return self._lib.Settings_Get_UEregs_GR()

    @UEregs.setter
    def UEregs(self, Value: Int32Array):
        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)
        self._lib.Settings_Set_UEregs(ValuePtr, ValueCount)

    @property
    def UEweight(self) -> float:
        '''
        Weighting factor applied to UE register values.

        Original COM help: https://opendss.epri.com/UEweight.html
        '''
        return self._lib.Settings_Get_UEweight()

    @UEweight.setter
    def UEweight(self, Value: float):
        self._lib.Settings_Set_UEweight(Value)

    @property
    def VoltageBases(self) -> Float64Array:
        '''
        Array of doubles defining the legal voltage bases in kV L-L

        Original COM help: https://opendss.epri.com/VoltageBases.html
        '''
        return self._lib.Settings_Get_VoltageBases_GR()

    @VoltageBases.setter
    def VoltageBases(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.Settings_Set_VoltageBases(ValuePtr, ValueCount)

    @property
    def ZoneLock(self) -> bool:
        '''
        Locks Zones on energy meters to prevent rebuilding if a circuit change occurs.

        Original COM help: https://opendss.epri.com/ZoneLock.html
        '''
        return self._lib.Settings_Get_ZoneLock()

    @ZoneLock.setter
    def ZoneLock(self, Value: bool):
        self._lib.Settings_Set_ZoneLock(Value)

    @property
    def AllocationFactors(self):
        '''(write-only) Sets all load allocation factors for all loads defined by XFKVA property to this value.'''
        raise AttributeError("This property is write-only!")

    @AllocationFactors.setter
    def AllocationFactors(self, Value: float):
        self._lib.Settings_Set_AllocationFactors(Value)

    @property
    def LoadsTerminalCheck(self) -> bool:
        '''
        Controls whether the terminals are checked when updating the currents in Load component. Defaults to True.
        If the loads are guaranteed to have their terminals closed throughout the simulation, this can be set to False to save some time.
        
        **(API Extension)**
        '''
        return self._lib.Settings_Get_LoadsTerminalCheck()

    @LoadsTerminalCheck.setter
    def LoadsTerminalCheck(self, Value: bool):
        self._lib.Settings_Set_LoadsTerminalCheck(Value)
        
    @property
    def IterateDisabled(self) -> int:
        '''
        Controls whether `First`/`Next` iteration includes or skips disabled circuit elements.
        The default behavior from OpenDSS is to skip those. The user can still activate the element by name or index.
        
        The default value for IterateDisabled is 0, keeping the original behavior.
        Set it to 1 (or `True`) to include disabled elements.
        Other numeric values are reserved for other potential behaviors.
        
        **(API Extension)**
        '''
        return self._lib.Settings_Get_IterateDisabled()

    @IterateDisabled.setter
    def IterateDisabled(self, Value: int):
        self._lib.Settings_Set_IterateDisabled(Value)

    def SetPropertyNameStyle(self, value: DSSPropertyNameStyle):
        '''
        Switch the property names according to the target style.

        Use this method for compatibility with code that doesn't consider that
        OpenDSS is case insensitive. Check the enumeration for more:
        [DSSPropertyNameStyle](#dss_python_backend.enums.DSSPropertyNameStyle)

        **(API Extension)**
        '''
        self._lib.Settings_SetPropertyNameStyle(value)

    @property
    def SkipFileRegExp(self) -> str:
        '''
        Regular expression pattern to skip files.

        If a file name as provided in the input for the `Redirect` and `Compile` commands
        matches the regular expression pattern, it is skipped (the file is not read nor
        commands contained in the file are executed).

        Set to an empty string to reset/disable the filter.

        Case-insensitive.
        See https://regex.sorokin.engineer/en/latest/regular_expressions.html for information on 
        the expression syntax and options.

        Even if the `clear` command is included in `Settings.SkipCommands`, the `DSS.ClearAll()` method can 
        still be called. It resets both skip settings, `SkipCommands` and `SkipFileRegExp`.

        **(API Extension)**
        '''
        return self._lib.Settings_Get_SkipFileRegExp()

    @SkipFileRegExp.setter
    def SkipFileRegExp(self, Value: Union[AnyStr, None]):
        self._lib.Settings_Set_SkipFileRegExp(Value or '')
    
    @property
    def SkipCommands(self) -> List[str]:
        '''
        List of commands to skip

        List of strings representing the command names to skip when processing DSS text commands or files.

        If the `clear` command is included in `Settings.SkipCommands`, the `DSS.ClearAll()` method can 
        still be called and it will reset both skip settings, `SkipCommands` and `SkipFileRegExp`.

        **(API Extension)**
        '''
        
        return [
            self._lib.DSS_Executive_Get_Command(i)
            for i in self._lib.Settings_Get_SkipCommands_GR()
        ]

    @SkipCommands.setter
    def SkipCommands(self, Value: List[str]):
        if len(Value) != 0 and isinstance(Value[0], str):
            # map command names to integer codes
            Value = [self._command_dict[cmd_name] for cmd_name in Value]

        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)
        self._lib.Settings_Set_SkipCommands(ValuePtr, ValueCount)


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
        
        **(API Extension)**
        '''
        return self._lib.advanced_types

    @AdvancedTypes.setter
    def AdvancedTypes(self, Value: bool):
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

        **(API Extension)**
        '''
        return self._lib.DSS_Get_CompatFlags()

    @CompatFlags.setter
    def CompatFlags(self, Value: int):
        self._lib.DSS_Set_CompatFlags(Value)


    @property
    def PreferLists(self) -> bool:
        '''
        Enable this setting to use lists instead of NumPy arrays, where it makes sense.

        This was added for better for compatibility with the COM packages (`comtypes` and  `win32com` use lists
        and tuples by default) and the original OpenDSSDirect.py releases.

        Current releases of OpenDSSDirect.py, DSS-Python, and AltDSS(-Python) all use NumPy arrays by default.
        Users can also activate the related `AdvancedTypes` for a richer experience.

        **(API Extension)**
        '''
        return self._lib.prefer_lists

    @PreferLists.setter
    def PreferLists(self, value: bool):
        self._lib.prefer_lists = value

    @property
    def COMErrorResults(self) -> bool:
        '''
        If enabled, in case of errors or empty arrays, the API returns arrays with values compatible with 
        EPRI's OpenDSS COM interface. 

        For example, consider the property `Loads.ZIPV`. If there is no active circuit or active load element:

        - In the disabled state (`COMErrorResults`=False), the function will return "[]", an array with 0 elements.
        - In the enabled state (`COMErrorResults`=True), the function will return "[0.0]" instead. This should
        be compatible with the return value of EPRI's OpenDSS COM interface.

        Defaults to false (disabled state) in AltDSS since the v0.15.x series.

        This does not affect the results when using EPRI's OpenDSS distribution through Oddie.

        This can also be set through the environment variable `DSS_CAPI_COM_DEFAULTS`. Setting it to 1 enables
        the legacy/COM behavior. The value can be toggled through the API at any time.

        **(API Extension)**
        '''
        return self._lib.DSS_Get_COMErrorResults()

    @COMErrorResults.setter
    def COMErrorResults(self, Value: bool):
        self._lib.DSS_Set_COMErrorResults(Value)

    @property
    def AllowDOScmd(self) -> bool:
        '''
        If enabled, the `DOScmd` command is allowed. Otherwise, an error is reported if the user tries to use it.

        Defaults to False/0 (disabled state). Users should consider DOScmd deprecated on DSS-Extensions.

        This can also be set through the environment variable DSS_CAPI_ALLOW_DOSCMD. Setting it to 1 enables
        the command.

        **(API Extension)**
        '''
        return self._lib.DSS_Get_AllowDOScmd()

    @AllowDOScmd.setter
    def AllowDOScmd(self, Value: bool):
        self._lib.DSS_Set_AllowDOScmd(Value)

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
        
        **(API Extension)**
        '''
        return self._lib.DSS_Get_AllowChangeDir()

    @AllowChangeDir.setter
    def AllowChangeDir(self, Value: bool):
        self._lib.DSS_Set_AllowChangeDir(Value)

    @property
    def AllowEditor(self) -> bool:
        '''
        Gets/sets whether running the external editor for "Show" is allowed
        
        AllowEditor controls whether the external editor is used in commands like "Show".
        If you set to 0 (false), the editor is not executed. Note that other side effects,
        such as the creation of files, are not affected.

        **(API Extension)**
        '''
        return self._lib.DSS_Get_AllowEditor()

    @AllowEditor.setter
    def AllowEditor(self, value: bool):
        self._lib.DSS_Set_AllowEditor(value)

    @property
    def PreserveCase(self) -> bool:
        '''
        Gets/sets whether the engine tries to preserve original names
        
        When enabled, bus and element names in many of the API functions, reports and
        exports are kept as provided by the user, without applying lower or upper case
        transformations.

        Note that, even when enabled, the engine is still case-insensitive.

        **(API Extension)**
        '''
        return self._lib.Settings_Get_Flag(1)

    @PreserveCase.setter
    def PreserveCase(self, value: bool):
        self._lib.Settings_Set_Flag(1, value)
