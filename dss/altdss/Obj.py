# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from .DSSObj import DSSObj
from .common import Base

from .enums import *
from .LineCode import ILineCode, LineCode
from .LoadShape import ILoadShape, LoadShape
from .TShape import ITShape, TShape
from .PriceShape import IPriceShape, PriceShape
from .XYcurve import IXYcurve, XYcurve
from .GrowthShape import IGrowthShape, GrowthShape
from .TCC_Curve import ITCC_Curve, TCC_Curve
from .Spectrum import ISpectrum, Spectrum
from .WireData import IWireData, WireData
from .CNData import ICNData, CNData
from .TSData import ITSData, TSData
from .LineSpacing import ILineSpacing, LineSpacing
from .LineGeometry import ILineGeometry, LineGeometry
from .XfmrCode import IXfmrCode, XfmrCode
from .Line import ILine, Line
from .Vsource import IVsource, Vsource
from .Isource import IIsource, Isource
from .VCCS import IVCCS, VCCS
from .Load import ILoad, Load
from .Transformer import ITransformer, Transformer
from .Capacitor import ICapacitor, Capacitor
from .Reactor import IReactor, Reactor
from .CapControl import ICapControl, CapControl
from .Fault import IFault, Fault
from .DynamicExp import IDynamicExp, DynamicExp
from .Generator import IGenerator, Generator
from .GenDispatcher import IGenDispatcher, GenDispatcher
from .Storage import IStorage, Storage
from .StorageController import IStorageController, StorageController
from .Relay import IRelay, Relay
from .Recloser import IRecloser, Recloser
from .Fuse import IFuse, Fuse
from .SwtControl import ISwtControl, SwtControl
from .PVSystem import IPVSystem, PVSystem
from .UPFC import IUPFC, UPFC
from .UPFCControl import IUPFCControl, UPFCControl
from .ESPVLControl import IESPVLControl, ESPVLControl
from .IndMach012 import IIndMach012, IndMach012
from .GICsource import IGICsource, GICsource
from .AutoTrans import IAutoTrans, AutoTrans
from .RegControl import IRegControl, RegControl
from .InvControl import IInvControl, InvControl
from .ExpControl import IExpControl, ExpControl
from .GICLine import IGICLine, GICLine
from .GICTransformer import IGICTransformer, GICTransformer
from .VSConverter import IVSConverter, VSConverter
from .Monitor import IMonitor, Monitor
from .EnergyMeter import IEnergyMeter, EnergyMeter
from .Sensor import ISensor, Sensor

_idx_to_cls = {}


class IObj(Base):
    __slots__ = [
        'LineCode',
        'LoadShape',
        'TShape',
        'PriceShape',
        'XYcurve',
        'GrowthShape',
        'TCC_Curve',
        'Spectrum',
        'WireData',
        'CNData',
        'TSData',
        'LineSpacing',
        'LineGeometry',
        'XfmrCode',
        'Line',
        'Vsource',
        'Isource',
        'VCCS',
        'Load',
        'Transformer',
        'Capacitor',
        'Reactor',
        'CapControl',
        'Fault',
        'DynamicExp',
        'Generator',
        'GenDispatcher',
        'Storage',
        'StorageController',
        'Relay',
        'Recloser',
        'Fuse',
        'SwtControl',
        'PVSystem',
        'UPFC',
        'UPFCControl',
        'ESPVLControl',
        'IndMach012',
        'GICsource',
        'AutoTrans',
        'RegControl',
        'InvControl',
        'ExpControl',
        'GICLine',
        'GICTransformer',
        'VSConverter',
        'Monitor',
        'EnergyMeter',
        'Sensor',
    ]

    LineCode: ILineCode
    LoadShape: ILoadShape
    TShape: ITShape
    PriceShape: IPriceShape
    XYcurve: IXYcurve
    GrowthShape: IGrowthShape
    TCC_Curve: ITCC_Curve
    Spectrum: ISpectrum
    WireData: IWireData
    CNData: ICNData
    TSData: ITSData
    LineSpacing: ILineSpacing
    LineGeometry: ILineGeometry
    XfmrCode: IXfmrCode
    Line: ILine
    Vsource: IVsource
    Isource: IIsource
    VCCS: IVCCS
    Load: ILoad
    Transformer: ITransformer
    Capacitor: ICapacitor
    Reactor: IReactor
    CapControl: ICapControl
    Fault: IFault
    DynamicExp: IDynamicExp
    Generator: IGenerator
    GenDispatcher: IGenDispatcher
    Storage: IStorage
    StorageController: IStorageController
    Relay: IRelay
    Recloser: IRecloser
    Fuse: IFuse
    SwtControl: ISwtControl
    PVSystem: IPVSystem
    UPFC: IUPFC
    UPFCControl: IUPFCControl
    ESPVLControl: IESPVLControl
    IndMach012: IIndMach012
    GICsource: IGICsource
    AutoTrans: IAutoTrans
    RegControl: IRegControl
    InvControl: IInvControl
    ExpControl: IExpControl
    GICLine: IGICLine
    GICTransformer: IGICTransformer
    VSConverter: IVSConverter
    Monitor: IMonitor
    EnergyMeter: IEnergyMeter
    Sensor: ISensor

    def __init__(self, api_util):
        Base.__init__(self, api_util)
        # self._idx_to_cls = dict()
        DSSObj._idx_to_cls = _idx_to_cls


        self.LineCode = ILineCode(self)
        self.LoadShape = ILoadShape(self)
        self.TShape = ITShape(self)
        self.PriceShape = IPriceShape(self)
        self.XYcurve = IXYcurve(self)
        self.GrowthShape = IGrowthShape(self)
        self.TCC_Curve = ITCC_Curve(self)
        self.Spectrum = ISpectrum(self)
        self.WireData = IWireData(self)
        self.CNData = ICNData(self)
        self.TSData = ITSData(self)
        self.LineSpacing = ILineSpacing(self)
        self.LineGeometry = ILineGeometry(self)
        self.XfmrCode = IXfmrCode(self)
        self.Line = ILine(self)
        self.Vsource = IVsource(self)
        self.Isource = IIsource(self)
        self.VCCS = IVCCS(self)
        self.Load = ILoad(self)
        self.Transformer = ITransformer(self)
        self.Capacitor = ICapacitor(self)
        self.Reactor = IReactor(self)
        self.CapControl = ICapControl(self)
        self.Fault = IFault(self)
        self.DynamicExp = IDynamicExp(self)
        self.Generator = IGenerator(self)
        self.GenDispatcher = IGenDispatcher(self)
        self.Storage = IStorage(self)
        self.StorageController = IStorageController(self)
        self.Relay = IRelay(self)
        self.Recloser = IRecloser(self)
        self.Fuse = IFuse(self)
        self.SwtControl = ISwtControl(self)
        self.PVSystem = IPVSystem(self)
        self.UPFC = IUPFC(self)
        self.UPFCControl = IUPFCControl(self)
        self.ESPVLControl = IESPVLControl(self)
        self.IndMach012 = IIndMach012(self)
        self.GICsource = IGICsource(self)
        self.AutoTrans = IAutoTrans(self)
        self.RegControl = IRegControl(self)
        self.InvControl = IInvControl(self)
        self.ExpControl = IExpControl(self)
        self.GICLine = IGICLine(self)
        self.GICTransformer = IGICTransformer(self)
        self.VSConverter = IVSConverter(self)
        self.Monitor = IMonitor(self)
        self.EnergyMeter = IEnergyMeter(self)
        self.Sensor = ISensor(self)

__all__ = [
    "IObj",
    "VisualizeQuantity",
    "ReductionStrategy",
    "EarthModel",
    "LineType",
    "LengthUnit",
    "ScanType",
    "SequenceType",
    "Connection",
    "CoreType",
    "PhaseSequence",
    "LoadSolutionModel",
    "RandomType",
    "ControlMode",
    "InverterControlMode",
    "SolutionMode",
    "SolutionAlgorithm",
    "CircuitModel",
    "AutoAddDeviceType",
    "LoadShapeClass",
    "MonitoredPhase",
    "PlotProfilePhases",
    "LoadShapeAction",
    "LoadShapeInterpolation",
    "TShapeAction",
    "PriceShapeAction",
    "VSourceModel",
    "LoadModel",
    "LoadStatus",
    "CapControlType",
    "DynamicExpDomain",
    "GeneratorModel",
    "GeneratorDispatchMode",
    "GeneratorStatus",
    "StorageState",
    "StorageDispatchMode",
    "StorageControllerDischargeMode",
    "StorageControllerChargeMode",
    "RelayType",
    "RelayAction",
    "RelayState",
    "RecloserAction",
    "RecloserState",
    "FuseAction",
    "FuseState",
    "SwtControlAction",
    "SwtControlState",
    "PVSystemModel",
    "UPFCMode",
    "ESPVLControlType",
    "IndMach012SlipOption",
    "AutoTransConnection",
    "RegControlPhaseSelection",
    "InvControlControlMode",
    "InvControlCombiMode",
    "InvControlVoltageCurveXRef",
    "InvControlVoltWattYAxis",
    "InvControlRateOfChangeMode",
    "InvControlReactivePowerReference",
    "InvControlControlModel",
    "GICTransformerType",
    "VSConverterControlMode",
    "MonitorAction",
    "EnergyMeterAction",
    "LineCode",
    "LoadShape",
    "TShape",
    "PriceShape",
    "XYcurve",
    "GrowthShape",
    "TCC_Curve",
    "Spectrum",
    "WireData",
    "CNData",
    "TSData",
    "LineSpacing",
    "LineGeometry",
    "XfmrCode",
    "Line",
    "Vsource",
    "Isource",
    "VCCS",
    "Load",
    "Transformer",
    "Capacitor",
    "Reactor",
    "CapControl",
    "Fault",
    "DynamicExp",
    "Generator",
    "GenDispatcher",
    "Storage",
    "StorageController",
    "Relay",
    "Recloser",
    "Fuse",
    "SwtControl",
    "PVSystem",
    "UPFC",
    "UPFCControl",
    "ESPVLControl",
    "IndMach012",
    "GICsource",
    "AutoTrans",
    "RegControl",
    "InvControl",
    "ExpControl",
    "GICLine",
    "GICTransformer",
    "VSConverter",
    "Monitor",
    "EnergyMeter",
    "Sensor",
]

