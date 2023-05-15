import numpy as np
import inspect
from .IDSS import IDSS
from .IBus import IBus
from .ICircuit import ICircuit
from .ICtrlQueue import ICtrlQueue
from .ISettings import ISettings
from .ISolution import ISolution
from .ITopology import ITopology

from .ICktElement import ICktElement
from .ICapacitors import ICapacitors
from .ICapControls import ICapControls
from .IISources import IISources
from .IGenerators import IGenerators
from .IFuses import IFuses
from .ILineCodes import ILineCodes
from .IMeters import IMeters
from .ILoadShapes import ILoadShapes
from .ILines import ILines
from .ILoads import ILoads
from .IMonitors import IMonitors
from .IPDElements import IPDElements
from .IPVSystems import IPVSystems
from .IRelays import IRelays
from .IReclosers import IReclosers
from .ISensors import ISensors
from .IRegControls import IRegControls
from .ISwtControls import ISwtControls
from .IVsources import IVsources
from .ITransformers import ITransformers
from .IXYCurves import IXYCurves
from .IGICSources import IGICSources
# from .IStorages import IStorages


def custom_iter(self):
    idx = self.First
    while idx != 0:
        yield self
        idx = self.Next

def custom_len(self):
    return self.Count


def Monitors_AsMatrix(self):
    '''Matrix of the active monitor, containing the hour vector, seconds vector, and all channels (index 2 = channel 1)'''
    
    buffer = np.array(self.ByteStream, dtype=np.int8)
    if len(buffer) <= 1:
        return None #np.zeros((0,), dtype=np.float32)
        
    record_size = buffer.view(dtype=np.int32)[2] + 2
    data = buffer[272:].view(dtype=np.float32)
    data = data.reshape((len(data) // record_size, record_size)).copy()
    return data        

    
def patch_dss_com(obj):
    if hasattr(type(obj.ActiveCircuit.Monitors), 'AsMatrix'):
        raise TypeError("Object already patched")

    def Load_Phases(self):
        current_load = self.Name
        obj.Text.Command = '? Load.{name}.Phases'.format(name=current_load)
        return int(obj.Text.Result)
        
    def Load_Set_Phases(self, value):
        # try:
        current_load = self.Name
        obj.Text.Command = 'Load.{name}.Phases={value}'.format(name=current_load, value=value)
        # except e:
        #     print('Error')
        #     print(e)
    
    def custom_bus_iter(self):
        for i in range(obj.ActiveCircuit.NumBuses):
            obj.ActiveCircuit.SetActiveBusi(i)
            yield self

    def custom_bus_len(self):
        return obj.ActiveCircuit.NumBuses

   
    # Monitors AsMatrix
    type(obj.ActiveCircuit.Monitors).AsMatrix = Monitors_AsMatrix
    
    # Load Phases
    type(obj.ActiveCircuit.Loads).Phases = property(Load_Phases, Load_Set_Phases)
   
    # Bus iterator and len
    type(obj.ActiveCircuit.ActiveBus).__iter__ = custom_bus_iter
    type(obj.ActiveCircuit.ActiveBus).__len__ = custom_bus_len
    type(obj.ActiveCircuit.ActiveBus)._columns = IBus._columns

    def add_dunders(cls):
        cls.__iter__ = custom_iter
        cls.__len__ = custom_len

    # We keep an explicit map since we may change our names later
    com_classes_to_dsspy = {
        'Capacitors': ICapacitors,
        'CapControls': ICapControls,
        'ISources': IISources,
        'Generators': IGenerators,
        'Fuses': IFuses,
        'LineCodes': ILineCodes,
        'Meters': IMeters,
        'LoadShapes': ILoadShapes,
        'Lines': ILines,
        'Loads': ILoads,
        'Monitors': IMonitors,
        'PDElements': IPDElements,
        'PVSystems': IPVSystems,
        'Relays': IRelays,
        'Reclosers': IReclosers,
        'Sensors': ISensors,
        'RegControls': IRegControls,
        'SwtControls': ISwtControls,
        'Vsources': IVsources,
        'Transformers': ITransformers,
        'XYCurves': IXYCurves,
        'GICSources': IGICSources,
        # 'Storages': IStorages,
    }

    def filter_cols(py_cls):
        return [
            c
            for c in py_cls._columns 
            if not (inspect.getdoc(getattr(py_cls, c)) or '').rstrip().endswith('(API Extension)')
        ]        

    # Add some more info to the classes
    type(obj.ActiveCircuit.ActiveCktElement)._py_cls = ICktElement
    type(obj.ActiveCircuit.ActiveCktElement)._columns = filter_cols(ICktElement)

    type(obj)._py_cls = IDSS
    type(obj)._columns = filter_cols(IDSS)

    type(obj.ActiveCircuit)._py_cls = ICircuit
    type(obj.ActiveCircuit)._columns = filter_cols(ICircuit)

    type(obj.ActiveCircuit.CtrlQueue)._py_cls = ICtrlQueue
    type(obj.ActiveCircuit.CtrlQueue)._columns = filter_cols(ICtrlQueue)

    type(obj.ActiveCircuit.Settings)._py_cls = ISettings
    type(obj.ActiveCircuit.Settings)._columns = filter_cols(ISettings)

    type(obj.ActiveCircuit.Solution)._py_cls = ISolution
    type(obj.ActiveCircuit.Solution)._columns = filter_cols(ISolution)

    type(obj.ActiveCircuit.Topology)._py_cls = ITopology
    type(obj.ActiveCircuit.Topology)._columns = filter_cols(ITopology)

    for name, py_cls in com_classes_to_dsspy.items():
        cls = type(getattr(obj.ActiveCircuit, name))
        add_dunders(cls)
        cls._py_cls = py_cls
        # Filter columns, removing 
        cls._columns = filter_cols(py_cls)

        if getattr(py_cls, '_is_circuit_element', False):
            cls._is_circuit_element = True

    add_dunders(cls)

    return obj
    
__all__ = ['patch_dss_com']
    
if __name__ == '__main__':
    # Simple test
    
    import comtypes.client
    DSS = comtypes.client.CreateObject("OpenDSSEngine.DSS")
    patch_dss_com(DSS)
    ckt = DSS.ActiveCircuit
    
    DSS.Text.Command = r'compile "..\electricdss-tst\Distrib\IEEETestCases\13Bus\IEEE13Nodeckt.dss"'
      
    for cls in [ckt.ActiveBus, ckt.Capacitors, ckt.CapControls, ckt.ISources, ckt.Generators, ckt.Fuses, ckt.LineCodes, ckt.Meters, ckt.LoadShapes, ckt.Lines, ckt.Loads, ckt.Monitors, ckt.PDElements, ckt.PVSystems, ckt.Relays, ckt.Reclosers, ckt.Sensors, ckt.RegControls, ckt.SwtControls, ckt.Vsources, ckt.Transformers, ckt.XYCurves]:
        cls_name = type(cls).__name__
        for e in cls:
            print(cls_name, e.Name)
        
    print()
            
    for e in ckt.Loads:
        print('Load {} has {} phases'.format(e.Name, e.Phases))
        e.Phases = int(e.Phases)

    for e in ckt.Monitors:
        print(e, e.name, e.AsMatrix())