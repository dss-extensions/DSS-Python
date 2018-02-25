import sys
if (sys.version_info.major, sys.version_info.minor) >= (3, 4):
    import enum
    Base = enum.IntEnum
else:
    Base = object

class MonitorModes(Base):
    VI = 0x00000000
    Power = 0x00000001
    Sequence = 0x00000010
    Magnitude = 0x00000020
    PosOnly = 0x00000040
    Taps = 0x00000002
    States = 0x00000003

class SolveModes(Base):
    SnapShot = 0x00000000
    DutyCycle = 0x00000006
    Direct = 0x00000007
    Daily = 0x00000001
    Monte1 = 0x00000003
    Monte2 = 0x0000000A
    Monte3 = 0x0000000B
    FaultStudy = 0x00000009
    Yearly = 0x00000002
    MonteFault = 0x00000008
    PeakDay = 0x00000005
    LD1 = 0x00000004
    LD2 = 0x0000000C
    AutoAdd = 0x0000000D
    Harmonic = 0x0000000F
    Dynamic = 0x0000000E

class Options(Base):
    PowerFlow = 0x00000001
    Admittance = 0x00000002
    NormalSolve = 0x00000000
    NewtonSolve = 0x00000001
    Static = 0x00000000
    Event = 0x00000001
    Time = 0x00000002
    Multiphase = 0x00000000
    PositiveSeq = 0x00000001
    Gaussian = 0x00000001
    Uniform = 0x00000002
    LogNormal = 0x00000003
    AddGen = 0x00000001
    AddCap = 0x00000002
    ControlOFF = 0xFFFFFFFF

class CapControlModes(Base):
    Voltage = 0x00000001
    KVAR = 0x00000002
    Current = 0x00000000
    PF = 0x00000004
    Time = 0x00000003

class ActionCodes:
    none = 0x00000000
    Open = 0x00000001
    Close = 0x00000002
    Reset = 0x00000003
    Lock = 0x00000004
    Unlock = 0x00000005
    TapUp = 0x00000006
    TapDown = 0x00000007

class LoadStatus(Base):
    Variable = 0x00000000
    Fixed = 0x00000001
    Exempt = 0x00000002

class LoadModels(Base):
    ConstPQ = 0x00000001
    ConstZ = 0x00000002
    Motor = 0x00000003
    CVR = 0x00000004
    ConstI = 0x00000005
    ConstPFixedQ = 0x00000006
    ConstPFixedX = 0x00000007
    ZIPV = 0x00000008

class LineUnits(Base):
    none = 0x00000000
    Miles = 0x00000001
    kFt = 0x00000002
    km = 0x00000003
    meter = 0x00000004
    ft = 0x00000005
    inch = 0x00000006
    cm = 0x00000007
    mm = 0x00000008
    Maxnum = 0x00000009
