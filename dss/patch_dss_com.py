import numpy as np

def custom_iter(self):
    idx = self.First
    while idx != 0:
        yield self
        idx = self.Next

def Monitors_AsMatrix(self):
    '''(read-only) Matrix of the active monitor, containing the hour vector, seconds vector, and all channels (index 2 = channel 1)'''
    
    buffer = np.array(self.ByteStream, dtype=np.int8)
    if len(buffer) <= 1:
        return None #np.zeros((0,), dtype=np.float32)
        
    record_size = buffer.view(dtype=np.int32)[2] + 2
    data = buffer[272:].view(dtype=np.float32)
    data = data.reshape((len(data) // record_size, record_size)).copy()
    return data        

    
def patch_dss_com(obj):
    
    def Load_Phases(self):
        current_load = self.Name
        obj.Text.Command = '? Load.{name}.Phases'.format(name=current_load)
        return int(obj.Text.Result)
        
    def Load_Set_Phases(self, value):
        try:
            current_load = self.Name
            obj.Text.Command = 'Load.{name}.Phases={value}'.format(name=current_load, value=value)
        except e:
            print('Error')
            print(e)
    
    def custom_bus_iter(self):
        for i in range(obj.ActiveCircuit.NumBuses):
            obj.ActiveCircuit.SetActiveBusi(i)
            yield self
   
    # Monitors AsMatrix
    type(obj.ActiveCircuit.Monitors).AsMatrix = Monitors_AsMatrix
    
    # Load Phases (implemented as read-only)
    type(obj.ActiveCircuit.Loads).Phases = property(Load_Phases)
   
    # Bus iterators
    type(obj.ActiveCircuit.ActiveBus).__iter__ = custom_bus_iter
    
    # General iterators
    type(obj.ActiveCircuit.Capacitors).__iter__ = custom_iter
    type(obj.ActiveCircuit.CapControls).__iter__ = custom_iter
    type(obj.ActiveCircuit.ISources).__iter__ = custom_iter
    type(obj.ActiveCircuit.Generators).__iter__ = custom_iter
    type(obj.ActiveCircuit.Fuses).__iter__ = custom_iter
    type(obj.ActiveCircuit.LineCodes).__iter__ = custom_iter
    type(obj.ActiveCircuit.Meters).__iter__ = custom_iter
    type(obj.ActiveCircuit.LoadShapes).__iter__ = custom_iter
    type(obj.ActiveCircuit.Lines).__iter__ = custom_iter
    type(obj.ActiveCircuit.Loads).__iter__ = custom_iter
    type(obj.ActiveCircuit.Monitors).__iter__ = custom_iter
    type(obj.ActiveCircuit.PDElements).__iter__ = custom_iter
    type(obj.ActiveCircuit.PVSystems).__iter__ = custom_iter
    type(obj.ActiveCircuit.Relays).__iter__ = custom_iter
    type(obj.ActiveCircuit.Reclosers).__iter__ = custom_iter
    type(obj.ActiveCircuit.Sensors).__iter__ = custom_iter
    type(obj.ActiveCircuit.RegControls).__iter__ = custom_iter
    type(obj.ActiveCircuit.SwtControls).__iter__ = custom_iter
    type(obj.ActiveCircuit.Vsources).__iter__ = custom_iter
    type(obj.ActiveCircuit.Transformers).__iter__ = custom_iter
    type(obj.ActiveCircuit.XYCurves).__iter__ = custom_iter
    
    return obj
    
__all__ = ['patch_dss_com']
    
if __name__ == '__main__':
    # Simple test
    
    import win32com.client as cc
    DSS = cc.gencache.EnsureDispatch("OpenDSSEngine.DSS")
    patch_dss_com(DSS)
    ckt = DSS.ActiveCircuit
    
    DSS.Text.Command = r'compile "Z:\dss\electricdss-tst\Distrib\IEEETestCases\13Bus\IEEE13Nodeckt.dss"'
      
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