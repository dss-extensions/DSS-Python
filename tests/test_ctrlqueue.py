'''
2019-02-28: Ported from CtrlQueueTest.bas by Paulo Meira (@pmeira)
2023-03-19: Modified to add to DSS-Python's tests
'''
import sys
import numpy as np

try:
    from ._settings import BASE_DIR, WIN32, DSS as DSSRef
except ImportError:
    from _settings import BASE_DIR, WIN32, DSS as DSSRef


USE_COM = False # Change to True to test with the COM DLL

def test_ctrlqueue():
    '''Example of implementing a simple voltage control for Capacitors via the interface'''

    if not USE_COM:
        if WIN32:
            # When running pytest, the faulthandler seems too eager to grab FPC's exceptions, even when handled
            import faulthandler
            faulthandler.disable()
            DSSobj = DSSRef
            faulthandler.enable()
        else:
            from dss import DSS as DSSobj
        
    else:
        import os
        old_cd = os.getcwd()
        import win32com.client
        DSSobj = win32com.client.gencache.EnsureDispatch('OpenDSSengine.DSS')
        os.chdir(old_cd)

    DSSobj.AllowForms = False
    DSSText = DSSobj.Text
    DSSCircuit = DSSobj.ActiveCircuit
    DSSSolution = DSSCircuit.Solution
    DSSControlQueue = DSSCircuit.CtrlQueue
    DSSMeters = DSSCircuit.Meters
    DSSBus = DSSCircuit.ActiveBus
    DSSCapacitors = DSSCircuit.Capacitors
    # Run simple capacitor interface test and execute local cap control that emulates CapControl
    # with these settings:
    # PT=125.09 Type=voltage onsetting=118.8 offsetting=121.2
    
    # this test case has a four-step capacitor bank named "cap" and can be found in the Test Folder
    
    DSSText.Command = f'Compile "{BASE_DIR}/Test/Master_TestCapInterface.DSS"'
    
    # Set all capacitor steps open for first capacitor
    iCap = DSSCapacitors.First   # should check iCap for >0
    iStates = [0] * DSSCapacitors.NumSteps
    
    for i in range(DSSCapacitors.NumSteps):
        iStates[i] = 0
    
    DSSCapacitors.States = iStates  # push over the interface to OpenDSS

    # check to make sure it worked
    DSSText.Command = "? Capacitor.Cap.States"
    assert DSSText.Result == '[ 0 0 0 0]'

    # Base solution
    DSSSolution.Solve()
    
    # Each message we push onto the queue will get a 5 s delay
    hour = 0
    secDelay = 5  # delay
    
    PTratio = 125.09   # for 26 kV system
    ONsetting = 118.8
    OFFsetting = 121.2
    ActionCodeAdd = 201  # just an arbitrary action code
    ActionCodeSub = 202  # just another arbitrary action code
    DeviceHandle = 123  # arbitrary handle that signifies this control
    
    # now, we'll crank the load up in 10% steps, checking the voltage at each step
    # until all cap steps are on (no more available)
    
    i = 0
    
    # Values updated for OpenDSS 10.1, which include the change to reset YPrimInvalid to false
    v_step_up = [
        119.26520933058164,
        118.53391703558978,
        119.00162278912609,
        118.22495566279100,
        118.66307559565404,
        119.11533205526253,
        118.26023037859353,
    ]
    while DSSCapacitors.AvailableSteps > 0:
        print('DSSCapacitors.AvailableSteps', DSSCapacitors.AvailableSteps)
        i = i + 1
        DSSSolution.LoadMult = 1 + i * 0.1  # 10% more each time
        DSSSolution.InitSnap()
        DSSSolution.SolveNoControl()
        DSSSolution.SampleControlDevices() # sample all other controls
        
        # Emulate the cap control Sample Routine and get the bus voltage
        DSSCircuit.SetActiveBus("feedbus")
        V = DSSBus.VMagAngle
        
        # check the first phase magnitude
        Vreg = V[0] / PTratio
        print("Step", i, "Voltage=", Vreg, "LoadMult=", DSSSolution.LoadMult)
        assert np.isclose(Vreg, v_step_up[i - 1])
        if Vreg < ONsetting: # push a message to bump up the number of steps
            DSSControlQueue.Push(hour, secDelay, ActionCodeAdd, DeviceHandle)
        
        DSSSolution.DoControlActions()   # this sends actions to the local action list
        
        print('DSSControlQueue.NumActions', DSSControlQueue.NumActions)
        if DSSControlQueue.NumActions > 0:
            while DSSControlQueue.PopAction > 0:
                devHandle = DSSControlQueue.DeviceHandle
                if devHandle == DeviceHandle:
                    iCap = DSSCapacitors.First   # Sets designated capacitor active
               
                currentActionCode = DSSControlQueue.ActionCode 
               
                if currentActionCode == ActionCodeAdd:
                    DSSCapacitors.AddStep()
                elif currentActionCode == ActionCodeSub:
                    DSSCapacitors.SubtractStep()
               
                # Print result
                print("Capacitor", DSSCapacitors.Name, "States =", tuple(DSSCapacitors.States))


    # Values updated for OpenDSS 10.1, which include the change to reset YPrimInvalid to false
    v_step_down = [
        121.87640973217214,
        121.19194698692986,
        121.72771816928677,
        121.00166364015094,
        121.51952384526496,
        120.74621507897345,
        121.24285846717471,
        120.41741114839155,
    ]

    # Now let's reverse Direction and start removing steps
    while DSSCapacitors.AvailableSteps < DSSCapacitors.NumSteps:
        i = i - 1
        DSSSolution.LoadMult = 1 + i * 0.1  # 10% more each time
        DSSSolution.InitSnap()
        DSSSolution.SolveNoControl()
        DSSSolution.SampleControlDevices() # sample all other controls
        
        # Emulate the cap control Sample Routine and get the bus voltage
        DSSCircuit.SetActiveBus("feedbus")
        V = DSSBus.VMagAngle
        
        # check the first phase magnitude
        Vreg = V[0] / PTratio
        print("Step", i, "Voltage=", Vreg, "LoadMult=", DSSSolution.LoadMult)
        assert np.isclose(Vreg, v_step_down[i + 1])
        if Vreg > OFFsetting: # push a message to bump down the number of steps
            DSSControlQueue.Push(hour, secDelay, ActionCodeSub, DeviceHandle)
        
        DSSSolution.DoControlActions()   # this send actions to the local action list
        
        if DSSControlQueue.NumActions > 0:
            while DSSControlQueue.PopAction > 0:
                devHandle = DSSControlQueue.DeviceHandle
                if devHandle == DeviceHandle:
                    DSSCapacitors.First   # Sets designated capacitor active
           
                currentActionCode = DSSControlQueue.ActionCode 
                if currentActionCode == ActionCodeAdd:
                    DSSCapacitors.AddStep()
                elif currentActionCode == ActionCodeSub:
                    DSSCapacitors.SubtractStep()
               
                # Print result
                print("Capacitor", DSSCapacitors.Name, "States =", tuple(DSSCapacitors.States))
                


if __name__ == '__main__':
    test_ctrlqueue()
