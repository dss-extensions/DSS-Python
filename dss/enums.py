try:
    from enum import IntEnum, IntFlag
except:
    try:
        from aenum import IntEnum, IntFlag
    except:
        IntEnum = object
        IntFlag = object

#TODO: add missing enums

class MonitorModes(IntEnum):
    VI = 0x00 # Monitor records Voltage and Current at the terminal (Default)
    Power = 0x01 # Monitor records kW, kvar or kVA, angle values, etc. at the terminal to which it is connected.
    Taps = 0x02 # For monitoring Regulator and Transformer taps
    States = 0x03 # For monitoring State Variables (for PC Elements only)
    Sequence = 0x10 # Reports the monitored quantities as sequence quantities
    Magnitude = 0x20 # Reports the monitored quantities in Magnitude Only
    PosOnly = 0x40 # Reports the Positive Seq only or avg of all phases

class SolveModes(IntEnum):
    SnapShot = 0 # Solve a single snapshot power flow
    Daily = 1 # Solve following Daily load shapes
    Yearly = 2 # Solve following Yearly load shapes
    Monte1 = 3 # Monte Carlo Mode 1
    LD1 = 4 # Load-duration Mode 1
    PeakDay = 5 # Solves for Peak Day using Daily load curve
    DutyCycle = 6 # Solve following Duty Cycle load shapes
    Direct = 7 # Solve direct (forced admittance model)
    MonteFault = 8 # Monte carlo Fault Study
    FaultStudy = 9 # Fault study at all buses
    Monte2 = 10 # Monte Carlo Mode 2
    Monte3 = 11 # Monte Carlo Mode 3
    LD2 = 12 # Load-Duration Mode 2
    AutoAdd = 13 # Auto add generators or capacitors
    Dynamic = 14 # Solve for dynamics
    Harmonic = 15 # Harmonic solution mode

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
    PowerFlow = 1 # Power Flow load model option
    Admittance = 2 # Admittance load model option

class SolutionAlgorithms(IntEnum):
    NormalSolve = 0 # Solution algorithm option - Normal solution
    NewtonSolve = 1 # Solution algorithm option - Newton solution

class ControlModes(IntEnum):
    Static = 0 # Control Mode option - Static
    Event = 1 # Control Mode Option - Event driven solution mode
    Time = 2 # Control mode option - Time driven mode
    Multirate = 3 # Control mode option - Multirate mode
    Off = -1 # Control Mode OFF

class CktModels(IntEnum):
    Multiphase = 0 # Circuit model is multiphase (default)
    PositiveSeq = 1 # Circuit model is positive sequence model only

class RandomModes(IntEnum):
    Gaussian = 1 # Gaussian
    Uniform = 2 # Uniform
    LogNormal = 3 # Log normal
    
class AutoAddTypes(IntEnum):
    AddGen = 1 # Add generators in AutoAdd mode
    AddCap = 2 # Add capacitors in AutoAdd mode

class CapControlModes(IntEnum):
    Current = 0 # Current control, ON and OFF settings on CT secondary
    Voltage = 1 # Voltage control, ON and OFF settings on the PT secondary base
    KVAR = 2 # kVAR control, ON and OFF settings on PT / CT base
    Time = 3 # Time control, ON and OFF settings are seconds from midnight
    PF = 4 # ON and OFF settings are power factor, negative for leading

class ActionCodes(IntEnum):
    none = 0 # No action
    Open = 1 # Open a switch
    Close = 2 # Close a switch
    Reset = 3 # Reset to the shelf state (unlocked, closed for a switch)
    Lock = 4 # Lock a switch, preventing both manual and automatic operation
    Unlock = 5 # Unlock a switch, permitting both manual and automatic operation
    TapUp = 6 # Move a regulator tap up
    TapDown = 7 # Move a regulator tap down

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
    none = 0 # No line length unit
    Miles = 1 # Line length units in miles
    kFt = 2 # Line length units are in thousand feet
    km = 3 # Line length units are km
    meter = 4 # Line length units are meters
    ft = 5 # Line units in feet
    inch = 6 # Line length units are inches
    cm = 7 # Line units are cm
    mm = 8 # Line length units are mm

class YMatrixModes(IntEnum):
    SeriesOnly = 1
    WholeMatrix = 2

class OCPDevType(IntEnum):
    none = 0
    Fuse = 1
    Recloser = 2
    Relay = 3

class SparseSolverOptions(IntEnum):
    ReuseNothing = 0 
    ReuseCompressedMatrix = 1 # Reuse only the prepared CSC matrix
    ReuseSymbolicFactorization = 2 # Reuse the symbolic factorization, implies ReuseCompressedMatrix
    ReuseNumericFactorization = 3 # Reuse the numeric factorization, implies ReuseSymbolicFactorization
    
    AlwaysResetYPrimInvalid = 0x10000000 # Bit flag, see CktElement.pas for details

class DSSJSONFlags(IntFlag):
    Full = 0x00000001
    SkipRedundant = 0x00000002
    EnumAsInt = 0x00000004
    FullNames = 0x00000008
    Pretty = 0x00000010
    ExcludeDisabled = 0x00000020
