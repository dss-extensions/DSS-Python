# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from typing_extensions import TypedDict, Unpack
from ._obj_bases import (
    CktElementMixin,
    EnergyMeterObjMixin,
    ElementHasRegistersMixin,
    IEnergyMeterMixin,
    BatchFloat64ArrayProxy,
    BatchInt32ArrayProxy,
    DSSObj,
    DSSBatch,
    IDSSObj,
    LIST_LIKE,
    # NotSet,
)
from .._types import Float64Array, Int32Array
from .._cffi_api_util import Base
from . import enums

class EnergyMeter(DSSObj, CktElementMixin, EnergyMeterObjMixin, ElementHasRegistersMixin):
    __slots__ = CktElementMixin._extra_slots + EnergyMeterObjMixin._extra_slots + ElementHasRegistersMixin._extra_slots
    _cls_name = 'EnergyMeter'
    _cls_idx = 48
    _cls_prop_idx = {
        'element': 1,
        'terminal': 2,
        'action': 3,
        'option': 4,
        'kvanormal': 5,
        'kvaemerg': 6,
        'peakcurrent': 7,
        'zonelist': 8,
        'localonly': 9,
        'mask': 10,
        'losses': 11,
        'linelosses': 12,
        'xfmrlosses': 13,
        'seqlosses': 14,
        'threephaselosses': 15,
        '3phaselosses': 15,
        'vbaselosses': 16,
        'phasevoltagereport': 17,
        'int_rate': 18,
        'int_duration': 19,
        'saifi': 20,
        'saifikw': 21,
        'saidi': 22,
        'caidi': 23,
        'custinterrupts': 24,
        'basefreq': 25,
        'enabled': 26,
        'like': 27,
    }

    @property
    def Element(self) -> str:
        """
        Name (Full Object name) of element to which the monitor is connected.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    @Element.setter
    def Element(self, value: Union[AnyStr, DSSObj]):
        if isinstance(value, DSSObj):
            self._set_obj(1, value)
            return

        self._set_string_o(1, value)

    @property
    def Element_obj(self) -> DSSObj:
        """
        Name (Full Object name) of element to which the monitor is connected.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_obj(1, None)

    @Element_obj.setter
    def Element_obj(self, value: DSSObj):
        self._set_obj(1, value)

    @property
    def Terminal(self) -> int:
        """
        Number of the terminal of the circuit element to which the monitor is connected. 1 or 2, typically.

        DSS property name: `Terminal`, DSS property index: 2.
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    @Terminal.setter
    def Terminal(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 2, value)

    def Action(self, value: Union[AnyStr, int, enums.EnergyMeterAction]):
        """
        {Clear (reset) | Save | Take | Zonedump | Allocate | Reduce} 

        (A)llocate = Allocate loads on the meter zone to match PeakCurrent.
        (C)lear = reset all registers to zero
        (R)educe = reduces zone by merging lines (see Set Keeplist & ReduceOption)
        (S)ave = saves the current register values to a file.
           File name is "MTR_metername.csv".
        (T)ake = Takes a sample at present solution
        (Z)onedump = Dump names of elements in meter zone to a file
           File name is "Zone_metername.csv".

        DSS property name: `Action`, DSS property index: 3.
        """
        if isinstance(value, int):
            self._lib.Obj_SetInt32(self._ptr, 3, value)
            return
    
        self._set_string_o(3, value)

    def Allocate(self):
        '''Shortcut to Action(EnergyMeterAction.Allocate)'''
        self._lib.Obj_SetInt32(self._ptr, 3, enums.EnergyMeterAction.Allocate)

    def Clear(self):
        '''Shortcut to Action(EnergyMeterAction.Clear)'''
        self._lib.Obj_SetInt32(self._ptr, 3, enums.EnergyMeterAction.Clear)

    def Reduce(self):
        '''Shortcut to Action(EnergyMeterAction.Reduce)'''
        self._lib.Obj_SetInt32(self._ptr, 3, enums.EnergyMeterAction.Reduce)

    def Save(self):
        '''Shortcut to Action(EnergyMeterAction.Save)'''
        self._lib.Obj_SetInt32(self._ptr, 3, enums.EnergyMeterAction.Save)

    def TakeSample(self):
        '''Shortcut to Action(EnergyMeterAction.TakeSample)'''
        self._lib.Obj_SetInt32(self._ptr, 3, enums.EnergyMeterAction.TakeSample)

    def ZoneDump(self):
        '''Shortcut to Action(EnergyMeterAction.ZoneDump)'''
        self._lib.Obj_SetInt32(self._ptr, 3, enums.EnergyMeterAction.ZoneDump)

    @property
    def Option(self) -> List[str]:
        """
        Enter a string ARRAY of any combination of the following. Options processed left-to-right:

        (E)xcess : (default) UE/EEN is estimate of energy over capacity 
        (T)otal : UE/EEN is total energy after capacity exceeded
        (R)adial : (default) Treats zone as a radial circuit
        (M)esh : Treats zone as meshed network (not radial).
        (C)ombined : (default) Load UE/EEN computed from combination of overload and undervoltage.
        (V)oltage : Load UE/EEN computed based on voltage only.

        Example: option=(E, R)

        DSS property name: `Option`, DSS property index: 4.
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 4)

    @Option.setter
    def Option(self, value: List[AnyStr]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 4, value_ptr, value_count)
        self._check_for_error()

    @property
    def kVANormal(self) -> float:
        """
        Upper limit on kVA load in the zone, Normal configuration. Default is 0.0 (ignored). Overrides limits on individual lines for overload EEN. With "LocalOnly=Yes" option, uses only load in metered branch.

        DSS property name: `kVANormal`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @kVANormal.setter
    def kVANormal(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def kVAEmerg(self) -> float:
        """
        Upper limit on kVA load in the zone, Emergency configuration. Default is 0.0 (ignored). Overrides limits on individual lines for overload UE. With "LocalOnly=Yes" option, uses only load in metered branch.

        DSS property name: `kVAEmerg`, DSS property index: 6.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    @kVAEmerg.setter
    def kVAEmerg(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 6, value)

    @property
    def PeakCurrent(self) -> Float64Array:
        """
        ARRAY of current magnitudes representing the peak currents measured at this location for the load allocation function.  Default is (400, 400, 400). Enter one current for each phase

        DSS property name: `PeakCurrent`, DSS property index: 7.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 7)

    @PeakCurrent.setter
    def PeakCurrent(self, value: Float64Array):
        self._set_float64_array_o(7, value)

    @property
    def ZoneList(self) -> List[str]:
        """
        ARRAY of full element names for this meter's zone.  Default is for meter to find it's own zone. If specified, DSS uses this list instead.  Can access the names in a single-column text file.  Examples: 

        zonelist=[line.L1, transformer.T1, Line.L3] 
        zonelist=(file=branchlist.txt)

        DSS property name: `ZoneList`, DSS property index: 8.
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 8)

    @ZoneList.setter
    def ZoneList(self, value: List[AnyStr]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 8, value_ptr, value_count)
        self._check_for_error()

    @property
    def LocalOnly(self) -> bool:
        """
        {Yes | No}  Default is NO.  If Yes, meter considers only the monitored element for EEN and UE calcs.  Uses whole zone for losses.

        DSS property name: `LocalOnly`, DSS property index: 9.
        """
        return self._lib.Obj_GetInt32(self._ptr, 9) != 0

    @LocalOnly.setter
    def LocalOnly(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 9, value)

    @property
    def Mask(self) -> Float64Array:
        """
        Mask for adding registers whenever all meters are totalized.  Array of floating point numbers representing the multiplier to be used for summing each register from this meter. Default = (1, 1, 1, 1, ... ).  You only have to enter as many as are changed (positional). Useful when two meters monitor same energy, etc.

        DSS property name: `Mask`, DSS property index: 10.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 10)

    @Mask.setter
    def Mask(self, value: Float64Array):
        self._set_float64_array_o(10, value)

    @property
    def Losses(self) -> bool:
        """
        {Yes | No}  Default is YES. Compute Zone losses. If NO, then no losses at all are computed.

        DSS property name: `Losses`, DSS property index: 11.
        """
        return self._lib.Obj_GetInt32(self._ptr, 11) != 0

    @Losses.setter
    def Losses(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 11, value)

    @property
    def LineLosses(self) -> bool:
        """
        {Yes | No}  Default is YES. Compute Line losses. If NO, then none of the losses are computed.

        DSS property name: `LineLosses`, DSS property index: 12.
        """
        return self._lib.Obj_GetInt32(self._ptr, 12) != 0

    @LineLosses.setter
    def LineLosses(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 12, value)

    @property
    def XfmrLosses(self) -> bool:
        """
        {Yes | No}  Default is YES. Compute Transformer losses. If NO, transformers are ignored in loss calculations.

        DSS property name: `XfmrLosses`, DSS property index: 13.
        """
        return self._lib.Obj_GetInt32(self._ptr, 13) != 0

    @XfmrLosses.setter
    def XfmrLosses(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 13, value)

    @property
    def SeqLosses(self) -> bool:
        """
        {Yes | No}  Default is YES. Compute Sequence losses in lines and segregate by line mode losses and zero mode losses.

        DSS property name: `SeqLosses`, DSS property index: 14.
        """
        return self._lib.Obj_GetInt32(self._ptr, 14) != 0

    @SeqLosses.setter
    def SeqLosses(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 14, value)

    @property
    def ThreePhaseLosses(self) -> bool:
        """
        {Yes | No}  Default is YES. Compute Line losses and segregate by 3-phase and other (1- and 2-phase) line losses. 

        DSS property name: `3PhaseLosses`, DSS property index: 15.
        """
        return self._lib.Obj_GetInt32(self._ptr, 15) != 0

    @ThreePhaseLosses.setter
    def ThreePhaseLosses(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 15, value)

    @property
    def VBaseLosses(self) -> bool:
        """
        {Yes | No}  Default is YES. Compute losses and segregate by voltage base. If NO, then voltage-based tabulation is not reported.

        DSS property name: `VBaseLosses`, DSS property index: 16.
        """
        return self._lib.Obj_GetInt32(self._ptr, 16) != 0

    @VBaseLosses.setter
    def VBaseLosses(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 16, value)

    @property
    def PhaseVoltageReport(self) -> bool:
        """
        {Yes | No}  Default is NO.  Report min, max, and average phase voltages for the zone and tabulate by voltage base. Demand Intervals must be turned on (Set Demand=true) and voltage bases must be defined for this property to take effect. Result is in a separate report file.

        DSS property name: `PhaseVoltageReport`, DSS property index: 17.
        """
        return self._lib.Obj_GetInt32(self._ptr, 17) != 0

    @PhaseVoltageReport.setter
    def PhaseVoltageReport(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 17, value)

    @property
    def Int_Rate(self) -> float:
        """
        Average number of annual interruptions for head of the meter zone (source side of zone or feeder).

        DSS property name: `Int_Rate`, DSS property index: 18.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    @Int_Rate.setter
    def Int_Rate(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 18, value)

    @property
    def Int_Duration(self) -> float:
        """
        Average annual duration, in hr, of interruptions for head of the meter zone (source side of zone or feeder).

        DSS property name: `Int_Duration`, DSS property index: 19.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    @Int_Duration.setter
    def Int_Duration(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 19, value)

    @property
    def SAIFI(self) -> float:
        """
        (Read only) Makes SAIFI result available via return on query (? energymeter.myMeter.SAIFI.

        DSS property name: `SAIFI`, DSS property index: 20.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    @SAIFI.setter
    def SAIFI(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 20, value)

    @property
    def SAIFIkW(self) -> float:
        """
        (Read only) Makes SAIFIkW result available via return on query (? energymeter.myMeter.SAIFIkW.

        DSS property name: `SAIFIkW`, DSS property index: 21.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    @SAIFIkW.setter
    def SAIFIkW(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 21, value)

    @property
    def SAIDI(self) -> float:
        """
        (Read only) Makes SAIDI result available via return on query (? energymeter.myMeter.SAIDI.

        DSS property name: `SAIDI`, DSS property index: 22.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    @SAIDI.setter
    def SAIDI(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 22, value)

    @property
    def CAIDI(self) -> float:
        """
        (Read only) Makes CAIDI result available via return on query (? energymeter.myMeter.CAIDI.

        DSS property name: `CAIDI`, DSS property index: 23.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    @CAIDI.setter
    def CAIDI(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 23, value)

    @property
    def CustInterrupts(self) -> float:
        """
        (Read only) Makes Total Customer Interrupts value result available via return on query (? energymeter.myMeter.CustInterrupts.

        DSS property name: `CustInterrupts`, DSS property index: 24.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    @CustInterrupts.setter
    def CustInterrupts(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 24, value)

    @property
    def BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 25.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 25)

    @BaseFreq.setter
    def BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 25, value)

    @property
    def Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 26.
        """
        return self._lib.Obj_GetInt32(self._ptr, 26) != 0

    @Enabled.setter
    def Enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 26, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 27.
        """
        self._set_string_o(27, value)


class EnergyMeterProperties(TypedDict):
    Element: Union[AnyStr, DSSObj]
    Terminal: int
    Action: Union[AnyStr, int, enums.EnergyMeterAction]
    Option: List[AnyStr]
    kVANormal: float
    kVAEmerg: float
    PeakCurrent: Float64Array
    ZoneList: List[AnyStr]
    LocalOnly: bool
    Mask: Float64Array
    Losses: bool
    LineLosses: bool
    XfmrLosses: bool
    SeqLosses: bool
    ThreePhaseLosses: bool
    VBaseLosses: bool
    PhaseVoltageReport: bool
    Int_Rate: float
    Int_Duration: float
    SAIFI: float
    SAIFIkW: float
    SAIDI: float
    CAIDI: float
    CustInterrupts: float
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class EnergyMeterBatch(DSSBatch):
    _cls_name = 'EnergyMeter'
    _obj_cls = EnergyMeter
    _cls_idx = 48


    @property
    def Element(self) -> List[str]:
        """
        Name (Full Object name) of element to which the monitor is connected.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1)

    @Element.setter
    def Element(self, value: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]]):
        self._set_batch_obj_prop(1, value)

    @property
    def Element_obj(self) -> List[DSSObj]:
        """
        Name (Full Object name) of element to which the monitor is connected.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 1)

    @Element_obj.setter
    def Element_obj(self, value: DSSObj):
        self._set_batch_string(1, value)

    @property
    def Terminal(self) -> BatchInt32ArrayProxy:
        """
        Number of the terminal of the circuit element to which the monitor is connected. 1 or 2, typically.

        DSS property name: `Terminal`, DSS property index: 2.
        """
        return BatchInt32ArrayProxy(self, 2)

    @Terminal.setter
    def Terminal(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(2, value)

    def Action(self, value: Union[AnyStr, int, enums.EnergyMeterAction]):
        """
        {Clear (reset) | Save | Take | Zonedump | Allocate | Reduce} 

        (A)llocate = Allocate loads on the meter zone to match PeakCurrent.
        (C)lear = reset all registers to zero
        (R)educe = reduces zone by merging lines (see Set Keeplist & ReduceOption)
        (S)ave = saves the current register values to a file.
           File name is "MTR_metername.csv".
        (T)ake = Takes a sample at present solution
        (Z)onedump = Dump names of elements in meter zone to a file
           File name is "Zone_metername.csv".

        DSS property name: `Action`, DSS property index: 3.
        """
        if isinstance(value, (bytes, str)) or (isinstance(value, LIST_LIKE) and len(value) > 0 and isinstance(value[0], (bytes, str))):
            self._set_batch_string(3, value)
        else:
            self._set_batch_int32_array(3, value)

    def Allocate(self):
        '''Shortcut to Action(EnergyMeterAction.Allocate)'''
        self._set_batch_int32_array(3, enums.EnergyMeterAction.Allocate)

    def Clear(self):
        '''Shortcut to Action(EnergyMeterAction.Clear)'''
        self._set_batch_int32_array(3, enums.EnergyMeterAction.Clear)

    def Reduce(self):
        '''Shortcut to Action(EnergyMeterAction.Reduce)'''
        self._set_batch_int32_array(3, enums.EnergyMeterAction.Reduce)

    def Save(self):
        '''Shortcut to Action(EnergyMeterAction.Save)'''
        self._set_batch_int32_array(3, enums.EnergyMeterAction.Save)

    def TakeSample(self):
        '''Shortcut to Action(EnergyMeterAction.TakeSample)'''
        self._set_batch_int32_array(3, enums.EnergyMeterAction.TakeSample)

    def ZoneDump(self):
        '''Shortcut to Action(EnergyMeterAction.ZoneDump)'''
        self._set_batch_int32_array(3, enums.EnergyMeterAction.ZoneDump)

    @property
    def Option(self) -> List[List[str]]:
        """
        Enter a string ARRAY of any combination of the following. Options processed left-to-right:

        (E)xcess : (default) UE/EEN is estimate of energy over capacity 
        (T)otal : UE/EEN is total energy after capacity exceeded
        (R)adial : (default) Treats zone as a radial circuit
        (M)esh : Treats zone as meshed network (not radial).
        (C)ombined : (default) Load UE/EEN computed from combination of overload and undervoltage.
        (V)oltage : Load UE/EEN computed based on voltage only.

        Example: option=(E, R)

        DSS property name: `Option`, DSS property index: 4.
        """
        return self._get_string_ll(4)

    @Option.setter
    def Option(self, value: List[AnyStr]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._ffi.unpack(self.pointer[0], self.count[0]):
            self._lib.Obj_SetStringArray(x, 4, value_ptr, value_count)
    
        self._check_for_error()

    @property
    def kVANormal(self) -> BatchFloat64ArrayProxy:
        """
        Upper limit on kVA load in the zone, Normal configuration. Default is 0.0 (ignored). Overrides limits on individual lines for overload EEN. With "LocalOnly=Yes" option, uses only load in metered branch.

        DSS property name: `kVANormal`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    @kVANormal.setter
    def kVANormal(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(5, value)

    @property
    def kVAEmerg(self) -> BatchFloat64ArrayProxy:
        """
        Upper limit on kVA load in the zone, Emergency configuration. Default is 0.0 (ignored). Overrides limits on individual lines for overload UE. With "LocalOnly=Yes" option, uses only load in metered branch.

        DSS property name: `kVAEmerg`, DSS property index: 6.
        """
        return BatchFloat64ArrayProxy(self, 6)

    @kVAEmerg.setter
    def kVAEmerg(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(6, value)

    @property
    def PeakCurrent(self) -> List[Float64Array]:
        """
        ARRAY of current magnitudes representing the peak currents measured at this location for the load allocation function.  Default is (400, 400, 400). Enter one current for each phase

        DSS property name: `PeakCurrent`, DSS property index: 7.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 7)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @PeakCurrent.setter
    def PeakCurrent(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(7, value)

    @property
    def ZoneList(self) -> List[List[str]]:
        """
        ARRAY of full element names for this meter's zone.  Default is for meter to find it's own zone. If specified, DSS uses this list instead.  Can access the names in a single-column text file.  Examples: 

        zonelist=[line.L1, transformer.T1, Line.L3] 
        zonelist=(file=branchlist.txt)

        DSS property name: `ZoneList`, DSS property index: 8.
        """
        return self._get_string_ll(8)

    @ZoneList.setter
    def ZoneList(self, value: List[AnyStr]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._ffi.unpack(self.pointer[0], self.count[0]):
            self._lib.Obj_SetStringArray(x, 8, value_ptr, value_count)
    
        self._check_for_error()

    @property
    def LocalOnly(self) -> List[bool]:
        """
        {Yes | No}  Default is NO.  If Yes, meter considers only the monitored element for EEN and UE calcs.  Uses whole zone for losses.

        DSS property name: `LocalOnly`, DSS property index: 9.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 9)
        ]
    @LocalOnly.setter
    def LocalOnly(self, value: bool):
        self._set_batch_int32_array(9, value)

    @property
    def Mask(self) -> List[Float64Array]:
        """
        Mask for adding registers whenever all meters are totalized.  Array of floating point numbers representing the multiplier to be used for summing each register from this meter. Default = (1, 1, 1, 1, ... ).  You only have to enter as many as are changed (positional). Useful when two meters monitor same energy, etc.

        DSS property name: `Mask`, DSS property index: 10.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 10)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Mask.setter
    def Mask(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(10, value)

    @property
    def Losses(self) -> List[bool]:
        """
        {Yes | No}  Default is YES. Compute Zone losses. If NO, then no losses at all are computed.

        DSS property name: `Losses`, DSS property index: 11.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 11)
        ]
    @Losses.setter
    def Losses(self, value: bool):
        self._set_batch_int32_array(11, value)

    @property
    def LineLosses(self) -> List[bool]:
        """
        {Yes | No}  Default is YES. Compute Line losses. If NO, then none of the losses are computed.

        DSS property name: `LineLosses`, DSS property index: 12.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 12)
        ]
    @LineLosses.setter
    def LineLosses(self, value: bool):
        self._set_batch_int32_array(12, value)

    @property
    def XfmrLosses(self) -> List[bool]:
        """
        {Yes | No}  Default is YES. Compute Transformer losses. If NO, transformers are ignored in loss calculations.

        DSS property name: `XfmrLosses`, DSS property index: 13.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 13)
        ]
    @XfmrLosses.setter
    def XfmrLosses(self, value: bool):
        self._set_batch_int32_array(13, value)

    @property
    def SeqLosses(self) -> List[bool]:
        """
        {Yes | No}  Default is YES. Compute Sequence losses in lines and segregate by line mode losses and zero mode losses.

        DSS property name: `SeqLosses`, DSS property index: 14.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 14)
        ]
    @SeqLosses.setter
    def SeqLosses(self, value: bool):
        self._set_batch_int32_array(14, value)

    @property
    def ThreePhaseLosses(self) -> List[bool]:
        """
        {Yes | No}  Default is YES. Compute Line losses and segregate by 3-phase and other (1- and 2-phase) line losses. 

        DSS property name: `3PhaseLosses`, DSS property index: 15.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 15)
        ]
    @ThreePhaseLosses.setter
    def ThreePhaseLosses(self, value: bool):
        self._set_batch_int32_array(15, value)

    @property
    def VBaseLosses(self) -> List[bool]:
        """
        {Yes | No}  Default is YES. Compute losses and segregate by voltage base. If NO, then voltage-based tabulation is not reported.

        DSS property name: `VBaseLosses`, DSS property index: 16.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 16)
        ]
    @VBaseLosses.setter
    def VBaseLosses(self, value: bool):
        self._set_batch_int32_array(16, value)

    @property
    def PhaseVoltageReport(self) -> List[bool]:
        """
        {Yes | No}  Default is NO.  Report min, max, and average phase voltages for the zone and tabulate by voltage base. Demand Intervals must be turned on (Set Demand=true) and voltage bases must be defined for this property to take effect. Result is in a separate report file.

        DSS property name: `PhaseVoltageReport`, DSS property index: 17.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 17)
        ]
    @PhaseVoltageReport.setter
    def PhaseVoltageReport(self, value: bool):
        self._set_batch_int32_array(17, value)

    @property
    def Int_Rate(self) -> BatchFloat64ArrayProxy:
        """
        Average number of annual interruptions for head of the meter zone (source side of zone or feeder).

        DSS property name: `Int_Rate`, DSS property index: 18.
        """
        return BatchFloat64ArrayProxy(self, 18)

    @Int_Rate.setter
    def Int_Rate(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(18, value)

    @property
    def Int_Duration(self) -> BatchFloat64ArrayProxy:
        """
        Average annual duration, in hr, of interruptions for head of the meter zone (source side of zone or feeder).

        DSS property name: `Int_Duration`, DSS property index: 19.
        """
        return BatchFloat64ArrayProxy(self, 19)

    @Int_Duration.setter
    def Int_Duration(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(19, value)

    @property
    def SAIFI(self) -> BatchFloat64ArrayProxy:
        """
        (Read only) Makes SAIFI result available via return on query (? energymeter.myMeter.SAIFI.

        DSS property name: `SAIFI`, DSS property index: 20.
        """
        return BatchFloat64ArrayProxy(self, 20)

    @SAIFI.setter
    def SAIFI(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(20, value)

    @property
    def SAIFIkW(self) -> BatchFloat64ArrayProxy:
        """
        (Read only) Makes SAIFIkW result available via return on query (? energymeter.myMeter.SAIFIkW.

        DSS property name: `SAIFIkW`, DSS property index: 21.
        """
        return BatchFloat64ArrayProxy(self, 21)

    @SAIFIkW.setter
    def SAIFIkW(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(21, value)

    @property
    def SAIDI(self) -> BatchFloat64ArrayProxy:
        """
        (Read only) Makes SAIDI result available via return on query (? energymeter.myMeter.SAIDI.

        DSS property name: `SAIDI`, DSS property index: 22.
        """
        return BatchFloat64ArrayProxy(self, 22)

    @SAIDI.setter
    def SAIDI(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(22, value)

    @property
    def CAIDI(self) -> BatchFloat64ArrayProxy:
        """
        (Read only) Makes CAIDI result available via return on query (? energymeter.myMeter.CAIDI.

        DSS property name: `CAIDI`, DSS property index: 23.
        """
        return BatchFloat64ArrayProxy(self, 23)

    @CAIDI.setter
    def CAIDI(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(23, value)

    @property
    def CustInterrupts(self) -> BatchFloat64ArrayProxy:
        """
        (Read only) Makes Total Customer Interrupts value result available via return on query (? energymeter.myMeter.CustInterrupts.

        DSS property name: `CustInterrupts`, DSS property index: 24.
        """
        return BatchFloat64ArrayProxy(self, 24)

    @CustInterrupts.setter
    def CustInterrupts(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(24, value)

    @property
    def BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 25.
        """
        return BatchFloat64ArrayProxy(self, 25)

    @BaseFreq.setter
    def BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(25, value)

    @property
    def Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 26.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 26)
        ]
    @Enabled.setter
    def Enabled(self, value: bool):
        self._set_batch_int32_array(26, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 27.
        """
        self._set_batch_string(27, value)

class EnergyMeterBatchProperties(TypedDict):
    Element: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]]
    Terminal: Union[int, Int32Array]
    Action: Union[AnyStr, int, enums.EnergyMeterAction]
    Option: List[AnyStr]
    kVANormal: Union[float, Float64Array]
    kVAEmerg: Union[float, Float64Array]
    PeakCurrent: Float64Array
    ZoneList: List[AnyStr]
    LocalOnly: bool
    Mask: Float64Array
    Losses: bool
    LineLosses: bool
    XfmrLosses: bool
    SeqLosses: bool
    ThreePhaseLosses: bool
    VBaseLosses: bool
    PhaseVoltageReport: bool
    Int_Rate: Union[float, Float64Array]
    Int_Duration: Union[float, Float64Array]
    SAIFI: Union[float, Float64Array]
    SAIFIkW: Union[float, Float64Array]
    SAIDI: Union[float, Float64Array]
    CAIDI: Union[float, Float64Array]
    CustInterrupts: Union[float, Float64Array]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IEnergyMeter(IDSSObj, IEnergyMeterMixin):
    __slots__ = ()

    def __init__(self, iobj):
        super().__init__(iobj, EnergyMeter, EnergyMeterBatch)

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> EnergyMeter:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[EnergyMeterProperties]) -> EnergyMeter:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[EnergyMeterBatchProperties]) -> EnergyMeterBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
