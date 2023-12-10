try:
    from enum import IntEnum, IntFlag
except (ModuleNotFoundError, ImportError):
    try:
        from aenum import IntEnum, IntFlag
    except (ModuleNotFoundError, ImportError):
        IntEnum = object
        IntFlag = object

#TODO: add missing enums

class MonitorModes(IntEnum):
    VI = 0x00
    """Monitor records Voltage and Current at the terminal (Default)"""
    
    Power = 0x01
    """Monitor records kW, kvar or kVA, angle values, etc. at the terminal to which it is connected."""
    
    Taps = 0x02 
    """For monitoring Regulator and Transformer taps"""
    
    States = 0x03
    """For monitoring State Variables (for PC Elements only)"""
    
    Sequence = 0x10
    """Reports the monitored quantities as sequence quantities"""
    
    Magnitude = 0x20
    """Reports the monitored quantities in Magnitude Only"""

    PosOnly = 0x40
    """Reports the Positive Seq only or avg of all phases"""

class SolveModes(IntEnum):
    SnapShot = 0
    """Solve a single snapshot power flow"""
    
    Daily = 1
    """Solve following Daily load shapes"""
    
    Yearly = 2
    """Solve following Yearly load shapes"""
    
    Monte1 = 3
    """Monte Carlo Mode 1"""

    LD1 = 4
    """Load-duration Mode 1"""
    
    PeakDay = 5
    """Solves for Peak Day using Daily load curve"""
    
    DutyCycle = 6
    """Solve following Duty Cycle load shapes"""
    
    Direct = 7
    """Solve direct (forced admittance model)"""
    
    MonteFault = 8 
    """Monte carlo Fault Study"""
    
    FaultStudy = 9
    """Fault study at all buses"""

    Monte2 = 10
    """Monte Carlo Mode 2"""

    Monte3 = 11
    """Monte Carlo Mode 3"""
    
    LD2 = 12
    """Load-Duration Mode 2"""
    
    AutoAdd = 13
    """Auto add generators or capacitors"""

    Dynamic = 14
    """Solve for dynamics"""

    Harmonic = 15
    """Harmonic solution mode"""

    Time = 16

    HarmonicT = 17


class Options(IntEnum):
    '''Deprecated. Please use instead: 
        - AutoAddTypes
        - CktModels
        - ControlModes
        - SolutionLoadModels
        - SolutionAlgorithms
        - RandomModes
    '''
    
    PowerFlow = 1
    Admittance = 2
    NormalSolve = 0
    NewtonSolve = 1
    Static = 0
    Event = 1
    Time = 2
    Multiphase = 0
    PositiveSeq = 1
    Gaussian = 1
    Uniform = 2
    LogNormal = 3
    AddGen = 1
    AddCap = 2
    ControlOFF = -1
    
class SolutionLoadModels(IntEnum):
    PowerFlow = 1
    """Power Flow load model option"""

    Admittance = 2
    """Admittance load model option"""

class SolutionAlgorithms(IntEnum):
    NormalSolve = 0 
    """Solution algorithm option - Normal solution"""

    NewtonSolve = 1 
    """Solution algorithm option - Newton solution"""

class ControlModes(IntEnum):
    Static = 0
    """Control Mode option - Static"""
    
    Event = 1
    """Control Mode Option - Event driven solution mode"""

    Time = 2
    """Control mode option - Time driven mode"""
    
    Multirate = 3
    """Control mode option - Multirate mode"""
    
    Off = -1
    """Control Mode OFF"""

class CktModels(IntEnum):
    Multiphase = 0 
    """Circuit model is multiphase (default)"""
    
    PositiveSeq = 1
    """Circuit model is positive sequence model only"""

class RandomModes(IntEnum):
    Gaussian = 1 # Gaussian
    Uniform = 2 # Uniform
    LogNormal = 3 # Log normal
    
class AutoAddTypes(IntEnum):
    AddGen = 1
    """Add generators in AutoAdd mode"""
    
    AddCap = 2
    """Add capacitors in AutoAdd mode"""

class CapControlModes(IntEnum):
    Current = 0 
    """Current control, ON and OFF settings on CT secondary"""

    Voltage = 1
    """Voltage control, ON and OFF settings on the PT secondary base"""

    KVAR = 2
    """kVAR control, ON and OFF settings on PT / CT base"""
    
    Time = 3
    """Time control, ON and OFF settings are seconds from midnight"""

    PF = 4
    """ON and OFF settings are power factor, negative for leading"""

class ActionCodes(IntEnum):
    none = 0
    """No action"""

    Open = 1
    """Open a switch"""

    Close = 2
    """Close a switch"""

    Reset = 3
    """Reset to the shelf state (unlocked, closed for a switch)"""

    Lock = 4
    """Lock a switch, preventing both manual and automatic operation"""

    Unlock = 5
    """Unlock a switch, permitting both manual and automatic operation"""

    TapUp = 6
    """Move a regulator tap up"""

    TapDown = 7
    """Move a regulator tap down"""


class LoadStatus(IntEnum):
    Variable = 0
    Fixed = 1
    Exempt = 2

class GeneratorStatus(IntEnum):
    Variable = 0
    Fixed = 1

class LoadModels(IntEnum):
    ConstPQ = 1
    ConstZ = 2
    Motor = 3
    CVR = 4
    ConstI = 5
    ConstPFixedQ = 6
    ConstPFixedX = 7
    ZIPV = 8

class LineUnits(IntEnum):
    none = 0
    """No line length unit"""

    Miles = 1
    """Line length units in miles"""

    kFt = 2
    """Line length units are in thousand feet"""

    km = 3
    """Line length units are km"""

    meter = 4
    """Line length units are meters"""

    ft = 5
    """Line units in feet"""

    inch = 6
    """Line length units are inches"""

    cm = 7
    """Line units are cm"""

    mm = 8
    """Line length units are mm"""


class YMatrixModes(IntEnum):
    SeriesOnly = 1
    WholeMatrix = 2

class OCPDevType(IntEnum):
    """Overcurrent Protection Device Type"""

    none = 0
    Fuse = 1
    Recloser = 2
    Relay = 3


class CoreType(IntEnum):
    """Transformer Core Type"""
    shell = 0 # shell
    one_phase = 1 # 1-phase
    three_leg = 3 # 3-leg
    four_leg = 4 # 4-leg
    five_leg = 5 # 5-leg
    core_1_phase = 9 # core-1-phase


class SparseSolverOptions(IntEnum):
    ReuseNothing = 0 
    """
    Default behavior, following the official OpenDSS implementation.
    """

    ReuseCompressedMatrix = 1
    """
    Reuse only the prepared CSC matrix. This should be numerically exact, but
    may have some cost saving if the number of entries changed in the system Y
    matrix are a small fraction of the total entries.
    """
    
    ReuseSymbolicFactorization = 2
    """
    Reuse the symbolic factorization, implies ReuseCompressedMatrix
    """
    
    ReuseNumericFactorization = 3
    """
    Reuse the numeric factorization, implies ReuseSymbolicFactorization
    """
    
    AlwaysResetYPrimInvalid = 0x10000000 
    """
    Bit flag, see CktElement.pas for details. Some components do not clear the
    dirty flag after their YPrim is updated, so YPrim is updated every time the
    system Y is changed, even if there are no changes to the component. This
    flag forces clearing the dirty flag, keeping the YPrim matrix constant when
    the component has not changed.
    """


class DSSJSONFlags(IntFlag):
    Full = 0x00000001
    """
    Return all properties, regardless of order or if the property was filled by the user
    """
    
    SkipRedundant = 0x00000002
    """
    Skip redundant properties
    """
    
    EnumAsInt = 0x00000004
    """
    Return enums as integers instead of strings
    """
    
    FullNames = 0x00000008
    """
    Use full names for the elements, including the class name
    """
    
    Pretty = 0x00000010
    """
    Try to "pretty" format the JSON output
    """
    
    ExcludeDisabled = 0x00000020
    """
    Exclude disabled elements (only valid when exporting a collection)
    """
    
    SkipDSSClass = 0x00000040
    """
    Do not add the "DSSClass" property to the output
    """
    
    LowercaseKeys = 0x00000080
    """
    Use lowercase representation for the property names (and other keys) instead of the internal variants.
    """

    IncludeDefaultObjs = 0x00000100
    """
    Include default unchanged objects in the exports. 
    Any default object that has been edited is always exported. Affects whole circuit and batch exports.
    """


class DSSCompatFlags(IntFlag):
    NoSolverFloatChecks = 0x00000001
    """
    If enabled, don't check for NaNs in the inner solution loop. 
    This can lead to various errors. 
    This flag is useful for legacy applications that don't handle OpenDSS API errors properly.
    Through the development of DSS-Extensions, we noticed this is actually a quite common issue.
    """

    BadPrecision = 0x00000002
    """
    If enabled, toggle worse precision for certain aspects of the engine. For
    example, the sequence-to-phase (`As2p`) and sequence-to-phase (`Ap2s`)
    transform matrices. On DSS C-API, we fill the matrix explicitly using
    higher precision, while numerical inversion of an initially worse precision
    matrix is used in the official OpenDSS. We will introduce better precision
    for other aspects of the engine in the future, so this flag can be used to
    toggle the old/bad values where feasible.
    """

    InvControl9611 = 0x00000004
    """
    Toggle some InvControl behavior introduced in OpenDSS 9.6.1.1. It could be a regression 
    but needs further investigation, so we added this flag in the time being.
    """

    SaveCalcVoltageBases = 0x00000008
    """
    When using "save circuit", the official OpenDSS always includes the "CalcVoltageBases" command in the
    saved script. We found that it is not always a good idea, so we removed the command (leaving it commented).
    Use this flag to enable the command in the saved script.
    """

    ActiveLine = 0x00000010
    """
    In the official OpenDSS implementation, the Lines API use the active circuit element instead of the
    active line. This can lead to unexpected behavior if the user is not aware of this detail.
    For example, if the user accidentally enables any other circuit element, the next time they use
    the Lines API, the line object that was previously enabled is overwritten with another unrelated
    object.
    This flag enables this behavior above if compatibility at this level is required. On DSS-Extensions,
    we changed the behavior to follow what most of the other APIs do: use the active object in the internal
    list. This change was done for DSS C-API v0.13.5, as well as the introduction of this flag.
    """

    NoPropertyTracking = 0x00000020
    """
    On DSS-Extensions/AltDSS, when setting a property invalidates a previous input value, the engine
    will try to mark the invalidated data as unset. This allows for better exports and tracking of 
    the current state of DSS objects.
    Set this flag to disable this behavior, following the original OpenDSS implementation for potential
    compatibility with older software that may require the original behavior; note that may lead to
    errorneous interpretation of the data in the DSS properties. This was introduced in DSS C-API v0.14.0
    and will be further developed for future versions.
    """

    SkipSideEffects = 0x00000040
    """
    Some specific functions on the official OpenDSS APIs skip important side-effects.
    By default, on DSS-Extensions/AltDSS, those side-effects are enabled. Use this flag
    to try to follow the behavior of the official APIs. Beware that some side-effects are
    important and skipping them may result in incorrect results.
    This flag only affects some of the classic API functions, especially Loads and Generators.
    """


class AltDSSEvent(IntEnum):
    """
    Event codes used by the event callback system
    """
    Legacy_InitControls = 0
    Legacy_CheckControls = 1
    Legacy_StepControls = 2
    Clear = 3
    ReprocessBuses = 4
    BuildSystemY = 5

