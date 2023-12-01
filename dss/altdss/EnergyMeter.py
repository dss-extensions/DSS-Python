# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from typing_extensions import TypedDict, Unpack
from .types import Float64Array, Int32Array
from . import enums
from .DSSObj import IDSSObj, DSSObj
from .Batch import DSSBatch
from .ArrayProxy import BatchFloat64ArrayProxy, BatchInt32ArrayProxy
from .common import LIST_LIKE
from .EnergyMeterExtras import EnergyMeterBatchMixin, IEnergyMeterMixin, EnergyMeterObjMixin
from .CircuitElement import CircuitElementBatchMixin, CircuitElementMixin
from .PCElement import ElementHasRegistersMixin

class EnergyMeter(DSSObj, CircuitElementMixin, EnergyMeterObjMixin, ElementHasRegistersMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots + EnergyMeterObjMixin._extra_slots + ElementHasRegistersMixin._extra_slots
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

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)
       EnergyMeterObjMixin.__init__(self)
       ElementHasRegistersMixin.__init__(self)

    def _get_Element_str(self) -> str:
        """
        Name (Full Object name) of element to which the monitor is connected.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    def _set_Element_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(1, value, flags)

    Element_str = property(_get_Element_str, _set_Element_str) # type: str

    def _get_Element(self) -> DSSObj:
        """
        Name (Full Object name) of element to which the monitor is connected.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_obj(1, None)

    def _set_Element(self, value: Union[AnyStr, DSSObj], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj):
            self._set_obj(1, value, flags)
            return

        self._set_string_o(1, value, flags)

    Element = property(_get_Element, _set_Element) # type: DSSObj

    def _get_Terminal(self) -> int:
        """
        Number of the terminal of the circuit element to which the monitor is connected. 1 or 2, typically.

        DSS property name: `Terminal`, DSS property index: 2.
        """
        return self._lib.Obj_GetInt32(self._ptr, 2)

    def _set_Terminal(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 2, value, flags)

    Terminal = property(_get_Terminal, _set_Terminal) # type: int

    def Action(self, value: Union[AnyStr, int, enums.EnergyMeterAction], flags: enums.SetterFlags = 0):
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
            self._lib.Obj_SetInt32(self._ptr, 3, value, flags)
            return

        self._set_string_o(3, value)

    def Allocate(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(EnergyMeterAction.Allocate)'''
        self._lib.Obj_SetInt32(self._ptr, 3, enums.EnergyMeterAction.Allocate, flags)

    def Clear(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(EnergyMeterAction.Clear)'''
        self._lib.Obj_SetInt32(self._ptr, 3, enums.EnergyMeterAction.Clear, flags)

    def Reduce(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(EnergyMeterAction.Reduce)'''
        self._lib.Obj_SetInt32(self._ptr, 3, enums.EnergyMeterAction.Reduce, flags)

    def Save(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(EnergyMeterAction.Save)'''
        self._lib.Obj_SetInt32(self._ptr, 3, enums.EnergyMeterAction.Save, flags)

    def TakeSample(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(EnergyMeterAction.TakeSample)'''
        self._lib.Obj_SetInt32(self._ptr, 3, enums.EnergyMeterAction.TakeSample, flags)

    def ZoneDump(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(EnergyMeterAction.ZoneDump)'''
        self._lib.Obj_SetInt32(self._ptr, 3, enums.EnergyMeterAction.ZoneDump, flags)

    def _get_Option(self) -> List[str]:
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

    def _set_Option(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 4, value_ptr, value_count, flags)
        self._check_for_error()

    Option = property(_get_Option, _set_Option) # type: List[str]

    def _get_kVANormal(self) -> float:
        """
        Upper limit on kVA load in the zone, Normal configuration. Default is 0.0 (ignored). Overrides limits on individual lines for overload EEN. With "LocalOnly=Yes" option, uses only load in metered branch.

        DSS property name: `kVANormal`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    def _set_kVANormal(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 5, value, flags)

    kVANormal = property(_get_kVANormal, _set_kVANormal) # type: float

    def _get_kVAEmerg(self) -> float:
        """
        Upper limit on kVA load in the zone, Emergency configuration. Default is 0.0 (ignored). Overrides limits on individual lines for overload UE. With "LocalOnly=Yes" option, uses only load in metered branch.

        DSS property name: `kVAEmerg`, DSS property index: 6.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    def _set_kVAEmerg(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 6, value, flags)

    kVAEmerg = property(_get_kVAEmerg, _set_kVAEmerg) # type: float

    def _get_PeakCurrent(self) -> Float64Array:
        """
        ARRAY of current magnitudes representing the peak currents measured at this location for the load allocation function.  Default is (400, 400, 400). Enter one current for each phase

        DSS property name: `PeakCurrent`, DSS property index: 7.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 7)

    def _set_PeakCurrent(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(7, value, flags)

    PeakCurrent = property(_get_PeakCurrent, _set_PeakCurrent) # type: Float64Array

    def _get_ZoneList(self) -> List[str]:
        """
        ARRAY of full element names for this meter's zone.  Default is for meter to find it's own zone. If specified, DSS uses this list instead.  Can access the names in a single-column text file.  Examples: 

        zonelist=[line.L1, transformer.T1, Line.L3] 
        zonelist=(file=branchlist.txt)

        DSS property name: `ZoneList`, DSS property index: 8.
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 8)

    def _set_ZoneList(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 8, value_ptr, value_count, flags)
        self._check_for_error()

    ZoneList = property(_get_ZoneList, _set_ZoneList) # type: List[str]

    def _get_LocalOnly(self) -> bool:
        """
        {Yes | No}  Default is NO.  If Yes, meter considers only the monitored element for EEN and UE calcs.  Uses whole zone for losses.

        DSS property name: `LocalOnly`, DSS property index: 9.
        """
        return self._lib.Obj_GetInt32(self._ptr, 9) != 0

    def _set_LocalOnly(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 9, value, flags)

    LocalOnly = property(_get_LocalOnly, _set_LocalOnly) # type: bool

    def _get_Mask(self) -> Float64Array:
        """
        Mask for adding registers whenever all meters are totalized.  Array of floating point numbers representing the multiplier to be used for summing each register from this meter. Default = (1, 1, 1, 1, ... ).  You only have to enter as many as are changed (positional). Useful when two meters monitor same energy, etc.

        DSS property name: `Mask`, DSS property index: 10.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 10)

    def _set_Mask(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(10, value, flags)

    Mask = property(_get_Mask, _set_Mask) # type: Float64Array

    def _get_Losses(self) -> bool:
        """
        {Yes | No}  Default is YES. Compute Zone losses. If NO, then no losses at all are computed.

        DSS property name: `Losses`, DSS property index: 11.
        """
        return self._lib.Obj_GetInt32(self._ptr, 11) != 0

    def _set_Losses(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 11, value, flags)

    Losses = property(_get_Losses, _set_Losses) # type: bool

    def _get_LineLosses(self) -> bool:
        """
        {Yes | No}  Default is YES. Compute Line losses. If NO, then none of the losses are computed.

        DSS property name: `LineLosses`, DSS property index: 12.
        """
        return self._lib.Obj_GetInt32(self._ptr, 12) != 0

    def _set_LineLosses(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 12, value, flags)

    LineLosses = property(_get_LineLosses, _set_LineLosses) # type: bool

    def _get_XfmrLosses(self) -> bool:
        """
        {Yes | No}  Default is YES. Compute Transformer losses. If NO, transformers are ignored in loss calculations.

        DSS property name: `XfmrLosses`, DSS property index: 13.
        """
        return self._lib.Obj_GetInt32(self._ptr, 13) != 0

    def _set_XfmrLosses(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 13, value, flags)

    XfmrLosses = property(_get_XfmrLosses, _set_XfmrLosses) # type: bool

    def _get_SeqLosses(self) -> bool:
        """
        {Yes | No}  Default is YES. Compute Sequence losses in lines and segregate by line mode losses and zero mode losses.

        DSS property name: `SeqLosses`, DSS property index: 14.
        """
        return self._lib.Obj_GetInt32(self._ptr, 14) != 0

    def _set_SeqLosses(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 14, value, flags)

    SeqLosses = property(_get_SeqLosses, _set_SeqLosses) # type: bool

    def _get_ThreePhaseLosses(self) -> bool:
        """
        {Yes | No}  Default is YES. Compute Line losses and segregate by 3-phase and other (1- and 2-phase) line losses. 

        DSS property name: `3PhaseLosses`, DSS property index: 15.
        """
        return self._lib.Obj_GetInt32(self._ptr, 15) != 0

    def _set_ThreePhaseLosses(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 15, value, flags)

    ThreePhaseLosses = property(_get_ThreePhaseLosses, _set_ThreePhaseLosses) # type: bool

    def _get_VBaseLosses(self) -> bool:
        """
        {Yes | No}  Default is YES. Compute losses and segregate by voltage base. If NO, then voltage-based tabulation is not reported.

        DSS property name: `VBaseLosses`, DSS property index: 16.
        """
        return self._lib.Obj_GetInt32(self._ptr, 16) != 0

    def _set_VBaseLosses(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 16, value, flags)

    VBaseLosses = property(_get_VBaseLosses, _set_VBaseLosses) # type: bool

    def _get_PhaseVoltageReport(self) -> bool:
        """
        {Yes | No}  Default is NO.  Report min, max, and average phase voltages for the zone and tabulate by voltage base. Demand Intervals must be turned on (Set Demand=true) and voltage bases must be defined for this property to take effect. Result is in a separate report file.

        DSS property name: `PhaseVoltageReport`, DSS property index: 17.
        """
        return self._lib.Obj_GetInt32(self._ptr, 17) != 0

    def _set_PhaseVoltageReport(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 17, value, flags)

    PhaseVoltageReport = property(_get_PhaseVoltageReport, _set_PhaseVoltageReport) # type: bool

    def _get_Int_Rate(self) -> float:
        """
        Average number of annual interruptions for head of the meter zone (source side of zone or feeder).

        DSS property name: `Int_Rate`, DSS property index: 18.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    def _set_Int_Rate(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 18, value, flags)

    Int_Rate = property(_get_Int_Rate, _set_Int_Rate) # type: float

    def _get_Int_Duration(self) -> float:
        """
        Average annual duration, in hr, of interruptions for head of the meter zone (source side of zone or feeder).

        DSS property name: `Int_Duration`, DSS property index: 19.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    def _set_Int_Duration(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 19, value, flags)

    Int_Duration = property(_get_Int_Duration, _set_Int_Duration) # type: float

    def _get_SAIFI(self) -> float:
        """
        (Read only) Makes SAIFI result available via return on query (? energymeter.myMeter.SAIFI.

        DSS property name: `SAIFI`, DSS property index: 20.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    def _set_SAIFI(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 20, value, flags)

    SAIFI = property(_get_SAIFI, _set_SAIFI) # type: float

    def _get_SAIFIkW(self) -> float:
        """
        (Read only) Makes SAIFIkW result available via return on query (? energymeter.myMeter.SAIFIkW.

        DSS property name: `SAIFIkW`, DSS property index: 21.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    def _set_SAIFIkW(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 21, value, flags)

    SAIFIkW = property(_get_SAIFIkW, _set_SAIFIkW) # type: float

    def _get_SAIDI(self) -> float:
        """
        (Read only) Makes SAIDI result available via return on query (? energymeter.myMeter.SAIDI.

        DSS property name: `SAIDI`, DSS property index: 22.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    def _set_SAIDI(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 22, value, flags)

    SAIDI = property(_get_SAIDI, _set_SAIDI) # type: float

    def _get_CAIDI(self) -> float:
        """
        (Read only) Makes CAIDI result available via return on query (? energymeter.myMeter.CAIDI.

        DSS property name: `CAIDI`, DSS property index: 23.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    def _set_CAIDI(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 23, value, flags)

    CAIDI = property(_get_CAIDI, _set_CAIDI) # type: float

    def _get_CustInterrupts(self) -> float:
        """
        (Read only) Makes Total Customer Interrupts value result available via return on query (? energymeter.myMeter.CustInterrupts.

        DSS property name: `CustInterrupts`, DSS property index: 24.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    def _set_CustInterrupts(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 24, value, flags)

    CustInterrupts = property(_get_CustInterrupts, _set_CustInterrupts) # type: float

    def _get_BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 25.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 25)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 25, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float

    def _get_Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 26.
        """
        return self._lib.Obj_GetInt32(self._ptr, 26) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 26, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool

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

class EnergyMeterBatch(DSSBatch, CircuitElementBatchMixin, EnergyMeterBatchMixin):
    _cls_name = 'EnergyMeter'
    _obj_cls = EnergyMeter
    _cls_idx = 48

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)
       EnergyMeterBatchMixin.__init__(self)

    def _get_Element_str(self) -> List[str]:
        """
        Name (Full Object name) of element to which the monitor is connected.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_batch_str_prop(1)

    def _set_Element_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(1, value, flags)

    Element_str = property(_get_Element_str, _set_Element_str) # type: List[str]

    def _get_Element(self) -> List[DSSObj]:
        """
        Name (Full Object name) of element to which the monitor is connected.

        DSS property name: `Element`, DSS property index: 1.
        """
        return self._get_batch_obj_prop(1)

    def _set_Element(self, value: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(1, value, flags)

    Element = property(_get_Element, _set_Element) # type: List[DSSObj]

    def _get_Terminal(self) -> BatchInt32ArrayProxy:
        """
        Number of the terminal of the circuit element to which the monitor is connected. 1 or 2, typically.

        DSS property name: `Terminal`, DSS property index: 2.
        """
        return BatchInt32ArrayProxy(self, 2)

    def _set_Terminal(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(2, value, flags)

    Terminal = property(_get_Terminal, _set_Terminal) # type: BatchInt32ArrayProxy

    def Action(self, value: Union[AnyStr, int, enums.EnergyMeterAction], flags: enums.SetterFlags = 0):
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
            self._set_batch_string(3, value, flags)
        else:
            self._set_batch_int32_array(3, value, flags)

    def Allocate(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(EnergyMeterAction.Allocate)'''
        self._set_batch_int32_array(3, enums.EnergyMeterAction.Allocate, flags)

    def Clear(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(EnergyMeterAction.Clear)'''
        self._set_batch_int32_array(3, enums.EnergyMeterAction.Clear, flags)

    def Reduce(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(EnergyMeterAction.Reduce)'''
        self._set_batch_int32_array(3, enums.EnergyMeterAction.Reduce, flags)

    def Save(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(EnergyMeterAction.Save)'''
        self._set_batch_int32_array(3, enums.EnergyMeterAction.Save, flags)

    def TakeSample(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(EnergyMeterAction.TakeSample)'''
        self._set_batch_int32_array(3, enums.EnergyMeterAction.TakeSample, flags)

    def ZoneDump(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(EnergyMeterAction.ZoneDump)'''
        self._set_batch_int32_array(3, enums.EnergyMeterAction.ZoneDump, flags)

    def _get_Option(self) -> List[List[str]]:
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

    def _set_Option(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._unpack():
            self._lib.Obj_SetStringArray(x, 4, value_ptr, value_count, flags)

        self._check_for_error()

    Option = property(_get_Option, _set_Option) # type: List[List[str]]

    def _get_kVANormal(self) -> BatchFloat64ArrayProxy:
        """
        Upper limit on kVA load in the zone, Normal configuration. Default is 0.0 (ignored). Overrides limits on individual lines for overload EEN. With "LocalOnly=Yes" option, uses only load in metered branch.

        DSS property name: `kVANormal`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    def _set_kVANormal(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(5, value, flags)

    kVANormal = property(_get_kVANormal, _set_kVANormal) # type: BatchFloat64ArrayProxy

    def _get_kVAEmerg(self) -> BatchFloat64ArrayProxy:
        """
        Upper limit on kVA load in the zone, Emergency configuration. Default is 0.0 (ignored). Overrides limits on individual lines for overload UE. With "LocalOnly=Yes" option, uses only load in metered branch.

        DSS property name: `kVAEmerg`, DSS property index: 6.
        """
        return BatchFloat64ArrayProxy(self, 6)

    def _set_kVAEmerg(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(6, value, flags)

    kVAEmerg = property(_get_kVAEmerg, _set_kVAEmerg) # type: BatchFloat64ArrayProxy

    def _get_PeakCurrent(self) -> List[Float64Array]:
        """
        ARRAY of current magnitudes representing the peak currents measured at this location for the load allocation function.  Default is (400, 400, 400). Enter one current for each phase

        DSS property name: `PeakCurrent`, DSS property index: 7.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 7)
            for x in self._unpack()
        ]

    def _set_PeakCurrent(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(7, value, flags)

    PeakCurrent = property(_get_PeakCurrent, _set_PeakCurrent) # type: List[Float64Array]

    def _get_ZoneList(self) -> List[List[str]]:
        """
        ARRAY of full element names for this meter's zone.  Default is for meter to find it's own zone. If specified, DSS uses this list instead.  Can access the names in a single-column text file.  Examples: 

        zonelist=[line.L1, transformer.T1, Line.L3] 
        zonelist=(file=branchlist.txt)

        DSS property name: `ZoneList`, DSS property index: 8.
        """
        return self._get_string_ll(8)

    def _set_ZoneList(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._unpack():
            self._lib.Obj_SetStringArray(x, 8, value_ptr, value_count, flags)

        self._check_for_error()

    ZoneList = property(_get_ZoneList, _set_ZoneList) # type: List[List[str]]

    def _get_LocalOnly(self) -> List[bool]:
        """
        {Yes | No}  Default is NO.  If Yes, meter considers only the monitored element for EEN and UE calcs.  Uses whole zone for losses.

        DSS property name: `LocalOnly`, DSS property index: 9.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(9)
        ]

    def _set_LocalOnly(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(9, value, flags)

    LocalOnly = property(_get_LocalOnly, _set_LocalOnly) # type: List[bool]

    def _get_Mask(self) -> List[Float64Array]:
        """
        Mask for adding registers whenever all meters are totalized.  Array of floating point numbers representing the multiplier to be used for summing each register from this meter. Default = (1, 1, 1, 1, ... ).  You only have to enter as many as are changed (positional). Useful when two meters monitor same energy, etc.

        DSS property name: `Mask`, DSS property index: 10.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 10)
            for x in self._unpack()
        ]

    def _set_Mask(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(10, value, flags)

    Mask = property(_get_Mask, _set_Mask) # type: List[Float64Array]

    def _get_Losses(self) -> List[bool]:
        """
        {Yes | No}  Default is YES. Compute Zone losses. If NO, then no losses at all are computed.

        DSS property name: `Losses`, DSS property index: 11.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(11)
        ]

    def _set_Losses(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(11, value, flags)

    Losses = property(_get_Losses, _set_Losses) # type: List[bool]

    def _get_LineLosses(self) -> List[bool]:
        """
        {Yes | No}  Default is YES. Compute Line losses. If NO, then none of the losses are computed.

        DSS property name: `LineLosses`, DSS property index: 12.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(12)
        ]

    def _set_LineLosses(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(12, value, flags)

    LineLosses = property(_get_LineLosses, _set_LineLosses) # type: List[bool]

    def _get_XfmrLosses(self) -> List[bool]:
        """
        {Yes | No}  Default is YES. Compute Transformer losses. If NO, transformers are ignored in loss calculations.

        DSS property name: `XfmrLosses`, DSS property index: 13.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(13)
        ]

    def _set_XfmrLosses(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(13, value, flags)

    XfmrLosses = property(_get_XfmrLosses, _set_XfmrLosses) # type: List[bool]

    def _get_SeqLosses(self) -> List[bool]:
        """
        {Yes | No}  Default is YES. Compute Sequence losses in lines and segregate by line mode losses and zero mode losses.

        DSS property name: `SeqLosses`, DSS property index: 14.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(14)
        ]

    def _set_SeqLosses(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(14, value, flags)

    SeqLosses = property(_get_SeqLosses, _set_SeqLosses) # type: List[bool]

    def _get_ThreePhaseLosses(self) -> List[bool]:
        """
        {Yes | No}  Default is YES. Compute Line losses and segregate by 3-phase and other (1- and 2-phase) line losses. 

        DSS property name: `3PhaseLosses`, DSS property index: 15.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(15)
        ]

    def _set_ThreePhaseLosses(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(15, value, flags)

    ThreePhaseLosses = property(_get_ThreePhaseLosses, _set_ThreePhaseLosses) # type: List[bool]

    def _get_VBaseLosses(self) -> List[bool]:
        """
        {Yes | No}  Default is YES. Compute losses and segregate by voltage base. If NO, then voltage-based tabulation is not reported.

        DSS property name: `VBaseLosses`, DSS property index: 16.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(16)
        ]

    def _set_VBaseLosses(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(16, value, flags)

    VBaseLosses = property(_get_VBaseLosses, _set_VBaseLosses) # type: List[bool]

    def _get_PhaseVoltageReport(self) -> List[bool]:
        """
        {Yes | No}  Default is NO.  Report min, max, and average phase voltages for the zone and tabulate by voltage base. Demand Intervals must be turned on (Set Demand=true) and voltage bases must be defined for this property to take effect. Result is in a separate report file.

        DSS property name: `PhaseVoltageReport`, DSS property index: 17.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(17)
        ]

    def _set_PhaseVoltageReport(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(17, value, flags)

    PhaseVoltageReport = property(_get_PhaseVoltageReport, _set_PhaseVoltageReport) # type: List[bool]

    def _get_Int_Rate(self) -> BatchFloat64ArrayProxy:
        """
        Average number of annual interruptions for head of the meter zone (source side of zone or feeder).

        DSS property name: `Int_Rate`, DSS property index: 18.
        """
        return BatchFloat64ArrayProxy(self, 18)

    def _set_Int_Rate(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(18, value, flags)

    Int_Rate = property(_get_Int_Rate, _set_Int_Rate) # type: BatchFloat64ArrayProxy

    def _get_Int_Duration(self) -> BatchFloat64ArrayProxy:
        """
        Average annual duration, in hr, of interruptions for head of the meter zone (source side of zone or feeder).

        DSS property name: `Int_Duration`, DSS property index: 19.
        """
        return BatchFloat64ArrayProxy(self, 19)

    def _set_Int_Duration(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(19, value, flags)

    Int_Duration = property(_get_Int_Duration, _set_Int_Duration) # type: BatchFloat64ArrayProxy

    def _get_SAIFI(self) -> BatchFloat64ArrayProxy:
        """
        (Read only) Makes SAIFI result available via return on query (? energymeter.myMeter.SAIFI.

        DSS property name: `SAIFI`, DSS property index: 20.
        """
        return BatchFloat64ArrayProxy(self, 20)

    def _set_SAIFI(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(20, value, flags)

    SAIFI = property(_get_SAIFI, _set_SAIFI) # type: BatchFloat64ArrayProxy

    def _get_SAIFIkW(self) -> BatchFloat64ArrayProxy:
        """
        (Read only) Makes SAIFIkW result available via return on query (? energymeter.myMeter.SAIFIkW.

        DSS property name: `SAIFIkW`, DSS property index: 21.
        """
        return BatchFloat64ArrayProxy(self, 21)

    def _set_SAIFIkW(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(21, value, flags)

    SAIFIkW = property(_get_SAIFIkW, _set_SAIFIkW) # type: BatchFloat64ArrayProxy

    def _get_SAIDI(self) -> BatchFloat64ArrayProxy:
        """
        (Read only) Makes SAIDI result available via return on query (? energymeter.myMeter.SAIDI.

        DSS property name: `SAIDI`, DSS property index: 22.
        """
        return BatchFloat64ArrayProxy(self, 22)

    def _set_SAIDI(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(22, value, flags)

    SAIDI = property(_get_SAIDI, _set_SAIDI) # type: BatchFloat64ArrayProxy

    def _get_CAIDI(self) -> BatchFloat64ArrayProxy:
        """
        (Read only) Makes CAIDI result available via return on query (? energymeter.myMeter.CAIDI.

        DSS property name: `CAIDI`, DSS property index: 23.
        """
        return BatchFloat64ArrayProxy(self, 23)

    def _set_CAIDI(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(23, value, flags)

    CAIDI = property(_get_CAIDI, _set_CAIDI) # type: BatchFloat64ArrayProxy

    def _get_CustInterrupts(self) -> BatchFloat64ArrayProxy:
        """
        (Read only) Makes Total Customer Interrupts value result available via return on query (? energymeter.myMeter.CustInterrupts.

        DSS property name: `CustInterrupts`, DSS property index: 24.
        """
        return BatchFloat64ArrayProxy(self, 24)

    def _set_CustInterrupts(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(24, value, flags)

    CustInterrupts = property(_get_CustInterrupts, _set_CustInterrupts) # type: BatchFloat64ArrayProxy

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 25.
        """
        return BatchFloat64ArrayProxy(self, 25)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(25, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy

    def _get_Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 26.
        """
        return [v != 0 for v in
            self._get_batch_int32_prop(26)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(26, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 27.
        """
        self._set_batch_string(27, value, flags)

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

class IEnergyMeter(IDSSObj, EnergyMeterBatch, IEnergyMeterMixin):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, EnergyMeter, EnergyMeterBatch)
        EnergyMeterBatch.__init__(self, self._api_util, sync_cls_idx=EnergyMeter._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> EnergyMeter:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[EnergyMeterProperties]) -> EnergyMeter:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[EnergyMeterBatchProperties]) -> EnergyMeterBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
