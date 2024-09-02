# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Base
from ._types import Float64Array, Int32Array
from typing import AnyStr, Union, List
from .enums import DSSPropertyNameStyle, CktModels

class ISettings(Base):
    __slots__ = [
        '_command_dict'
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
        'LoadsTerminalCheck',
        'IterateDisabled',
    ]

    def __init__(self, api_util):
        Base.__init__(self, api_util)
        num_commands = self._lib.DSS_Executive_Get_NumCommands()
        self._command_dict = {
            self._lib.DSS_Executive_Get_Command(i).lower(): i
            for i in range(1, num_commands + 1)
        }

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


