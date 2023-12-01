# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from enum import IntEnum, IntFlag
# Global enumerations


class ExtraClassIDs(IntEnum):
    """
    A very limited set of functions accept the numbers from this enumeration
    as shortcuts to the internal prepared element lists of the engine.
    """
    DSSObjs = -1
    CktElements = -2
    PCElements = -3
    PDElements = -4


class SetterFlags(IntFlag):
    """
    Setter flags for the AltDSS modern API

    These bit flags can change the behavior when setting DSS property values,
    allowing fine tuning of how the internal state of the element being
    edited is updated.
      
    Most of the flags are for advanced uses only. 
    The flags do not affect DSS scripts in general, or the classic APIs, only
    uses through the modern alternative API from AltDSS.
    """

    ImplicitSizes = 0x01
    """
    Most array properties depend on sizes defined by other properties.
    Using this flag, many properties allow users to skip setting the other property
    directly, allowing the engine to use the size of the provided array to
    initialize the other property.
    """

    AvoidFullRecalc = 0x02
    """
    Some components like Loads don't need to update YPrim or full recalc for every change, 
    e.g. setting "`load.a_load.kW=1`" if was "kW" previously 2 should not force a YPrim 
    update, but it does force an update by default.
    Using this flag will reproduce what the classic OpenDSS API for Loads (DSS.ActiveCircuit.Loads)
    does, but removes a lot of duplicated code. Besides that, we can extend the feature 
    for other components if we think it fits.
    """


class VisualizeQuantity(IntEnum):
    """Visualize: Quantity (DSS enumeration)"""
    Currents = 1 # Currents
    Voltages = 2 # Voltages
    Powers = 3 # Powers


class ReductionStrategy(IntEnum):
    """Reduction Strategy (DSS enumeration)"""
    Default = 0 # Default
    ShortLines = 1 # ShortLines
    MergeParallel = 2 # MergeParallel
    BreakLoop = 3 # BreakLoop
    Dangling = 4 # Dangling
    Switches = 5 # Switches
    Laterals = 6 # Laterals


class EarthModel(IntEnum):
    """Earth Model (DSS enumeration)"""
    Carson = 1 # Carson
    FullCarson = 2 # FullCarson
    Deri = 3 # Deri


class LineType(IntEnum):
    """Line Type (DSS enumeration)"""
    oh = 1 # oh
    ug = 2 # ug
    ug_ts = 3 # ug_ts
    ug_cn = 4 # ug_cn
    swt_ldbrk = 5 # swt_ldbrk
    swt_fuse = 6 # swt_fuse
    swt_sect = 7 # swt_sect
    swt_rec = 8 # swt_rec
    swt_disc = 9 # swt_disc
    swt_brk = 10 # swt_brk
    swt_elbow = 11 # swt_elbow
    busbar = 12 # busbar


class LengthUnit(IntEnum):
    """Length Unit (DSS enumeration)"""
    none = 0 # none
    mi = 1 # mi
    kft = 2 # kft
    km = 3 # km
    m = 4 # m
    ft = 5 # ft
    inch = 6 # in
    cm = 7 # cm
    mm = 8 # mm
    meter = 4 # meter
    miles = 1 # miles


class ScanType(IntEnum):
    """Scan Type (DSS enumeration)"""
    none = -1 # None
    Zero = 0 # Zero
    Positive = 1 # Positive


class SequenceType(IntEnum):
    """Sequence Type (DSS enumeration)"""
    Negative = -1 # Negative
    Zero = 0 # Zero
    Positive = 1 # Positive


class Connection(IntEnum):
    """Connection (DSS enumeration)"""
    wye = 0 # wye
    delta = 1 # delta
    y = 0 # y
    ln = 0 # ln
    ll = 1 # ll


class CoreType(IntEnum):
    """Core Type (DSS enumeration)"""
    shell = 0 # shell
    one_phase = 1 # 1-phase
    three_leg = 3 # 3-leg
    four_leg = 4 # 4-leg
    five_leg = 5 # 5-leg
    core_1_phase = 9 # core-1-phase


class PhaseSequence(IntEnum):
    """Phase Sequence (DSS enumeration)"""
    Lag = 0 # Lag
    Lead = 1 # Lead
    ANSI = 0 # ANSI
    Euro = 1 # Euro


class LoadSolutionModel(IntEnum):
    """Load Solution Model (DSS enumeration)"""
    PowerFlow = 1 # PowerFlow
    Admittance = 2 # Admittance


class RandomType(IntEnum):
    """Random Type (DSS enumeration)"""
    none = 0 # None
    Gaussian = 1 # Gaussian
    Uniform = 2 # Uniform
    LogNormal = 3 # LogNormal


class ControlMode(IntEnum):
    """Control Mode (DSS enumeration)"""
    Off = -1 # Off
    Static = 0 # Static
    Event = 1 # Event
    Time = 2 # Time
    MultiRate = 3 # MultiRate


class InverterControlMode(IntEnum):
    """Inverter Control Mode (DSS enumeration)"""
    GFL = 0 # GFL
    GFM = 1 # GFM


class SolutionMode(IntEnum):
    """Solution Mode (DSS enumeration)"""
    Snap = 0 # Snap
    Daily = 1 # Daily
    Yearly = 2 # Yearly
    M1 = 3 # M1
    LD1 = 4 # LD1
    PeakDay = 5 # PeakDay
    DutyCycle = 6 # DutyCycle
    Direct = 7 # Direct
    MF = 8 # MF
    FaultStudy = 9 # FaultStudy
    M2 = 10 # M2
    M3 = 11 # M3
    LD2 = 12 # LD2
    AutoAdd = 13 # AutoAdd
    Dynamic = 14 # Dynamic
    Harmonic = 15 # Harmonic
    Time = 16 # Time
    HarmonicT = 17 # HarmonicT
    Snapshot = 0 # Snapshot
    Dynamics = 14 # Dynamics
    Harmonics = 15 # Harmonics
    S = 0 # S
    Y = 2 # Y
    H = 15 # H
    T = 16 # T
    F = 9 # F


class SolutionAlgorithm(IntEnum):
    """Solution Algorithm (DSS enumeration)"""
    Normal = 0 # Normal
    Newton = 1 # Newton


class CircuitModel(IntEnum):
    """Circuit Model (DSS enumeration)"""
    Multiphase = 0 # Multiphase
    Positive = 1 # Positive


class AutoAddDeviceType(IntEnum):
    """AutoAdd Device Type (DSS enumeration)"""
    Generator = 1 # Generator
    Capacitor = 2 # Capacitor


class LoadShapeClass(IntEnum):
    """Load Shape Class (DSS enumeration)"""
    none = -1 # None
    Daily = 0 # Daily
    Yearly = 1 # Yearly
    Duty = 2 # Duty


class MonitoredPhase(IntEnum):
    """Monitored Phase (DSS enumeration)"""
    min = -3 # min
    max = -2 # max
    avg = -1 # avg


class PlotProfilePhases(IntEnum):
    """Plot: Profile Phases (DSS enumeration)"""
    Default = -1 # Default
    All = -2 # All
    Primary = -3 # Primary
    LL3Ph = -4 # LL3Ph
    LLAll = -5 # LLAll
    LLPrimary = -6 # LLPrimary



# Class-specific enumerations

class LoadShapeAction(IntEnum):
    """LoadShape: Action (DSS enumeration)"""
    Normalize = 0 # Normalize
    DblSave = 1 # DblSave
    SngSave = 2 # SngSave

class LoadShapeInterpolation(IntEnum):
    """LoadShape: Interpolation (DSS enumeration)"""
    Avg = 0 # Avg
    Edge = 1 # Edge


class TShapeAction(IntEnum):
    """TShape: Action (DSS enumeration)"""
    DblSave = 0 # DblSave
    SngSave = 1 # SngSave


class PriceShapeAction(IntEnum):
    """PriceShape: Action (DSS enumeration)"""
    DblSave = 0 # DblSave
    SngSave = 1 # SngSave


class VSourceModel(IntEnum):
    """VSource: Model (DSS enumeration)"""
    Thevenin = 0 # Thevenin
    Ideal = 1 # Ideal


class LoadModel(IntEnum):
    """Load: Model (DSS enumeration)"""
    ConstantPQ = 1 # Constant PQ
    ConstantZ = 2 # Constant Z
    Motor = 3 # Motor (constant P, quadratic Q)
    CVR = 4 # CVR (linear P, quadratic Q)
    ConstantI = 5 # Constant I
    ConstantP_fixedQ = 6 # Constant P, fixed Q
    ConstantP_fixedX = 7 # Constant P, fixed X
    ZIPV = 8 # ZIPV

class LoadStatus(IntEnum):
    """Load: Status (DSS enumeration)"""
    Variable = 0 # Variable
    Fixed = 1 # Fixed
    Exempt = 2 # Exempt


class CapControlType(IntEnum):
    """CapControl: Type (DSS enumeration)"""
    Current = 0 # Current
    Voltage = 1 # Voltage
    kvar = 2 # kvar
    Time = 3 # Time
    PowerFactor = 4 # PowerFactor
    Follow = 5 # Follow


class DynamicExpDomain(IntEnum):
    """DynamicExp: Domain (DSS enumeration)"""
    Time = 0 # Time
    dq = 1 # dq


class GeneratorModel(IntEnum):
    """Generator: Model (DSS enumeration)"""
    ConstantPQ = 1 # Constant PQ
    ConstantZ = 2 # Constant Z
    ConstantPV = 3 # Constant P|V|
    ConstantP_fixedQ = 4 # Constant P, fixed Q
    ConstantP_fixedX = 5 # Constant P, fixed X
    Usermodel = 6 # User model
    Approximateinvertermodel = 7 # Approximate inverter model

class GeneratorDispatchMode(IntEnum):
    """Generator: Dispatch Mode (DSS enumeration)"""
    Default = 0 # Default
    LoadLevel = 1 # LoadLevel
    Price = 2 # Price

class GeneratorStatus(IntEnum):
    """Generator: Status (DSS enumeration)"""
    Variable = 0 # Variable
    Fixed = 1 # Fixed


class StorageState(IntEnum):
    """Storage: State (DSS enumeration)"""
    Charging = -1 # Charging
    Idling = 0 # Idling
    Discharging = 1 # Discharging

class StorageDispatchMode(IntEnum):
    """Storage: Dispatch Mode (DSS enumeration)"""
    Default = 0 # Default
    LoadLevel = 1 # LoadLevel
    Price = 2 # Price
    External = 3 # External
    Follow = 4 # Follow


class StorageControllerDischargeMode(IntEnum):
    """StorageController: Discharge Mode (DSS enumeration)"""
    Peakshave = 5 # Peakshave
    Follow = 1 # Follow
    Support = 3 # Support
    Loadshape = 2 # Loadshape
    Time = 4 # Time
    Schedule = 6 # Schedule
    I_Peakshave = 8 # I-Peakshave

class StorageControllerChargeMode(IntEnum):
    """StorageController: Charge Mode (DSS enumeration)"""
    Loadshape = 2 # Loadshape
    Time = 4 # Time
    PeakshaveLow = 7 # PeakshaveLow
    I_PeakshaveLow = 9 # I-PeakshaveLow


class RelayType(IntEnum):
    """Relay: Type (DSS enumeration)"""
    Current = 0 # Current
    Voltage = 1 # Voltage
    ReversePower = 3 # ReversePower
    relay46 = 4 # 46
    relay47 = 5 # 47
    Generic = 6 # Generic
    Distance = 7 # Distance
    TD21 = 8 # TD21
    DOC = 9 # DOC

class RelayAction(IntEnum):
    """Relay: Action (DSS enumeration)"""
    close = 2 # close
    open = 1 # open
    trip = 1 # trip

class RelayState(IntEnum):
    """Relay: State (DSS enumeration)"""
    closed = 2 # closed
    open = 1 # open
    trip = 1 # trip


class RecloserAction(IntEnum):
    """Recloser: Action (DSS enumeration)"""
    close = 2 # close
    open = 1 # open
    trip = 1 # trip

class RecloserState(IntEnum):
    """Recloser: State (DSS enumeration)"""
    closed = 2 # closed
    open = 1 # open
    trip = 1 # trip


class FuseAction(IntEnum):
    """Fuse: Action (DSS enumeration)"""
    close = 2 # close
    open = 1 # open

class FuseState(IntEnum):
    """Fuse: State (DSS enumeration)"""
    closed = 2 # closed
    open = 1 # open


class SwtControlAction(IntEnum):
    """SwtControl: Action (DSS enumeration)"""
    close = 2 # close
    open = 1 # open

class SwtControlState(IntEnum):
    """SwtControl: State (DSS enumeration)"""
    closed = 2 # closed
    open = 1 # open


class PVSystemModel(IntEnum):
    """PVSystem: Model (DSS enumeration)"""
    ConstantP_PF = 1 # Constant P, PF
    ConstantY = 2 # Constant Y
    Usermodel = 3 # User model


class UPFCMode(IntEnum):
    """UPFC: Mode (DSS enumeration)"""
    Off = 0 # Off
    VoltageRegulator = 1 # Voltage Regulator
    PhaseAngleRegulator = 2 # Phase Angle Regulator
    DualRegulator = 3 # Dual Regulator
    DoubleReference_Voltage = 4 # Double Reference (Voltage)
    DoubleReference_Dual = 5 # Double Reference (Dual)


class ESPVLControlType(IntEnum):
    """ESPVLControl: Type (DSS enumeration)"""
    SystemController = 1 # SystemController
    LocalController = 2 # LocalController


class IndMach012SlipOption(IntEnum):
    """IndMach012: Slip Option (DSS enumeration)"""
    VariableSlip = 0 # VariableSlip
    FixedSlip = 1 # FixedSlip


class AutoTransConnection(IntEnum):
    """AutoTrans: Connection (DSS enumeration)"""
    wye = 0 # wye
    delta = 1 # delta
    series = 2 # series
    y = 0 # y
    ln = 0 # ln
    ll = 1 # ll


class RegControlPhaseSelection(IntEnum):
    """RegControl: Phase Selection (DSS enumeration)"""
    min = -3 # min
    max = -2 # max


class InvControlControlMode(IntEnum):
    """InvControl: Control Mode (DSS enumeration)"""
    Voltvar = 1 # Voltvar
    VoltWatt = 2 # VoltWatt
    DynamicReaccurr = 3 # DynamicReaccurr
    WattPF = 4 # WattPF
    Wattvar = 5 # Wattvar
    AVR = 6 # AVR
    GFM = 7 # GFM

class InvControlCombiMode(IntEnum):
    """InvControl: Combi Mode (DSS enumeration)"""
    VV_VW = 1 # VV_VW
    VV_DRC = 2 # VV_DRC

class InvControlVoltageCurveXRef(IntEnum):
    """InvControl: Voltage Curve X Ref (DSS enumeration)"""
    Rated = 0 # Rated
    Avg = 1 # Avg
    RAvg = 2 # RAvg

class InvControlVoltWattYAxis(IntEnum):
    """InvControl: Volt-Watt Y-Axis (DSS enumeration)"""
    PAvailablePU = 0 # PAvailablePU
    PMPPPU = 1 # PMPPPU
    PctPMPPPU = 2 # PctPMPPPU
    KVARatingPU = 3 # KVARatingPU

class InvControlRateOfChangeMode(IntEnum):
    """InvControl: Rate-of-change Mode (DSS enumeration)"""
    Inactive = 0 # Inactive
    LPF = 1 # LPF
    RiseFall = 2 # RiseFall

class InvControlReactivePowerReference(IntEnum):
    """InvControl: Reactive Power Reference (DSS enumeration)"""
    VARAVAL = 0 # VARAVAL
    VARMAX = 1 # VARMAX

class InvControlControlModel(IntEnum):
    """InvControl: Control Model (DSS enumeration)"""
    Linear = 0 # Linear
    Exponential = 1 # Exponential


class GICTransformerType(IntEnum):
    """GICTransformer: Type (DSS enumeration)"""
    GSU = 1 # GSU
    Auto = 2 # Auto
    YY = 3 # YY


class VSConverterControlMode(IntEnum):
    """VSConverter: Control Mode (DSS enumeration)"""
    Fixed = 0 # Fixed
    PacVac = 1 # PacVac
    PacQac = 2 # PacQac
    VdcVac = 3 # VdcVac
    VdcQac = 4 # VdcQac


class MonitorAction(IntEnum):
    """Monitor: Action (DSS enumeration)"""
    Clear = 0 # Clear
    Save = 1 # Save
    TakeSample = 2 # TakeSample
    Process = 3 # Process
    Reset = 0 # Reset


class EnergyMeterAction(IntEnum):
    """EnergyMeter: Action (DSS enumeration)"""
    Allocate = 0 # Allocate
    Clear = 1 # Clear
    Reduce = 2 # Reduce
    Save = 3 # Save
    TakeSample = 4 # TakeSample
    ZoneDump = 5 # ZoneDump


