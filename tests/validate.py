from __future__ import print_function
import os, sys
from time import time
import numpy as np
from scipy.sparse import csc_matrix
from dss import enums

original_working_dir = os.getcwd()
NO_PROPERTIES = os.getenv('DSS_PYTHON_VALIDATE') == 'NOPROP'
USE_V8 = os.getenv('DSS_PYTHON_V8') == '1'

# COM Output
SAVE_COM_OUTPUT = False
# LOAD_COM_OUTPUT = False

if SAVE_COM_OUTPUT:
#    LOAD_COM_OUTPUT = False
    import pickle
    output = {}
else:
    class FakeDict:
        def __setitem__(self, key, value):
            # ignore the value
            pass

    output = FakeDict()
    

def parse_dss_matrix(m):
    try:
        sep = ' '
        if ',' in m:
            sep = ','
            
        data = []
        for row in m[1:-1].split(' |'):
            row_float = []
            for e in row.strip(sep).strip(' ').split(sep):
                if not e: continue
                row_float.append(float(e))
                
            data.append(row_float)
            
        return data
    except:
        return m
    

class ValidatingTest:
    def __init__(self, fn, com, capi, line_by_line):
        self.fn = fn
        self.com = com
        self.capi = capi
        self.line_by_line = line_by_line

        self.AllBusDistances = []
        self.AllBusNames = []
        self.AllBusVmag = []
        self.AllBusVmagPu = []
        self.AllBusVolts = []
        self.AllElementLosses = []
        self.AllElementNames = []
        self.AllNodeDistances = []
        self.AllNodeNames = []
        self.LineLosses = []
        self.Losses = []
        self.Name = []
        self.NumBuses = []
        self.NumCktElements = []
        self.NumNodes = []
        self.ParentPDElement = []
        self.SubstationLosses = []
        self.SystemY = []
        self.TotalPower = []
        self.YCurrents = []
        self.YNodeOrder = []
        self.YNodeVarray = []


    def run(self, dss, solve=False):
        os.chdir(original_working_dir)
        dss.Start(0)
        dss.Text.Command = 'Clear'

        if self.line_by_line:
            with open(self.fn, 'r') as f:
                os.chdir(os.path.dirname(self.fn))
                iter_f = iter(f)
                try:
                    while True:
                        input_line = next(iter_f).strip()
                        if input_line.startswith('/*'):
                            #print('Skipping input:', repr(input_line))
                            while True:
                                input_line = next(iter_f).strip()
                                if '*/' in input_line:
                                    input_line = ''
                                    break

                        if not input_line: continue
                        lc_input_line = input_line.lower()
                        if any(lc_input_line.startswith(x) for x in ['show', 'plot', 'visualize', 'dump', 'export']) or ord(input_line[0]) > 127:
                            #print('Skipping input:', repr(input_line))
                            continue
                        else:
                            input_line = input_line.replace('C:\\Users\\prdu001\\OpenDSS\\Test\\', '')
                            input_line = input_line.replace('C:\\Users\\prdu001\\OpenDSS\\Distrib\\Examples\\Scripts\\', '../Distrib/Examples/Scripts/')
                            #print(input_line)
                            dss.Text.Command = input_line
                except StopIteration:
                    pass
        else:
            dss.Text.Command = 'Compile "{}"'.format(self.fn)


        if solve:
            dss.ActiveCircuit.Solution.Mode = enums.SolveModes.Daily
            dss.ActiveCircuit.Solution.Solve()

        self.atol = dss.ActiveCircuit.Solution.Tolerance

        self.AllBusDistances.append(dss.ActiveCircuit.AllBusDistances)
        self.AllBusNames.append(dss.ActiveCircuit.AllBusNames)
        self.AllBusVmag.append(dss.ActiveCircuit.AllBusVmag)
        self.AllBusVmagPu.append(dss.ActiveCircuit.AllBusVmagPu)
        self.AllBusVolts.append(dss.ActiveCircuit.AllBusVolts)
        self.AllElementLosses.append(dss.ActiveCircuit.AllElementLosses)
        self.AllElementNames.append(dss.ActiveCircuit.AllElementNames)
        self.AllNodeDistances.append(dss.ActiveCircuit.AllNodeDistances)
        self.AllNodeNames.append(dss.ActiveCircuit.AllNodeNames)
        self.LineLosses.append(dss.ActiveCircuit.LineLosses)
        self.Losses.append(dss.ActiveCircuit.Losses)
        self.Name.append(dss.ActiveCircuit.Name)
        self.NumBuses.append(dss.ActiveCircuit.NumBuses)
        self.NumCktElements.append(dss.ActiveCircuit.NumCktElements)
        self.NumNodes.append(dss.ActiveCircuit.NumNodes)
        self.ParentPDElement.append(dss.ActiveCircuit.ParentPDElement)
        self.SubstationLosses.append(dss.ActiveCircuit.SubstationLosses)
        self.SystemY.append(dss.ActiveCircuit.SystemY)
        self.TotalPower.append(dss.ActiveCircuit.TotalPower)
        self.YCurrents.append(dss.ActiveCircuit.YCurrents)
        self.YNodeOrder.append(dss.ActiveCircuit.YNodeOrder)
        self.YNodeVarray.append(dss.ActiveCircuit.YNodeVarray)


    def validate_CktElement(self):
        A = self.com.ActiveCircuit.ActiveElement
        B = self.capi.ActiveCircuit.ActiveElement

        for field in 'AllPropertyNames,AllVariableNames,BusNames'.split(','):
            fA = getattr(A, field)
            fB = getattr(B, field)
            if fA == ('',) and fB == [None]: continue # comtypes and win32com results are a bit different here
            assert all(x[0] == x[1] for x in zip(fA, fB)), field
            
          
        # Check if setting bus names works
        BusNames = list(A.BusNames)
        A.BusNames = BusNames
        B.BusNames = BusNames

        # Check if they match again
        field = 'BusNames'
        fA = getattr(A, field)
        fB = getattr(B, field)
        if not (fA == ('',) and fB == [None]): # comtypes and win32com results are a bit different here
            assert all(x[0] == x[1] for x in zip(fA, fB)), field
          
          
        if NO_PROPERTIES: return
            
        all_props = list(A.AllPropertyNames)
        for prop_name in all_props:
            is_equal = False
            if A.Properties(prop_name).Val != B.Properties(prop_name).Val:
                val_A = A.Properties(prop_name).Val
                val_B = B.Properties(prop_name).Val
                # Try as floats
                try:
                    val_A = float(val_A)
                    val_B = float(val_B)
                    is_equal = np.isclose(val_A, val_B, atol=self.atol, rtol=self.rtol)
                except:
                    val_A = 0
                    val_B = 1
                    
                if val_A != val_B:
                    val_A = A.Properties(prop_name).Val
                    val_B = B.Properties(prop_name).Val

                    # Try as matrices of floats                    
                    if val_A.startswith('[') and val_A.endswith(']'):
                        val_A = parse_dss_matrix(val_A)
                        val_B = parse_dss_matrix(val_B)
                        if not isinstance(val_A, str):
                            is_equal = True
                            for row_A, row_B in zip(val_A, val_B):
                                if not np.allclose(row_A, row_B, atol=self.atol, rtol=self.rtol):
                                    is_equal = False
                                    break
                    
                
                if not (is_equal or val_A == val_B or A.Properties(prop_name).Val == B.Properties(prop_name).Val):
                    print('ERROR: CktElement.Properties({}).Val'.format(prop_name), A.Properties(prop_name).Val, B.Properties(prop_name).Val)
            
            if not USE_V8:
                assert (A.Properties(prop_name).Description == B.Properties(prop_name).Description), ('Properties({}).Description'.format(prop_name), A.Properties(prop_name).Description, B.Properties(prop_name).Description)
                
            assert (A.Properties(prop_name).Name == B.Properties(prop_name).Name), ('Properties({}).name'.format(prop_name), A.Properties(prop_name).Name, B.Properties(prop_name).Name)

            assert (B.Properties(prop_name).Val == B.Properties[prop_name].Val)
            assert (B.Properties(prop_name).Description == B.Properties[prop_name].Description)
            assert (B.Properties(prop_name).Name == B.Properties[prop_name].Name)


    def validate_Buses(self):
        for idx in range(len(self.AllBusNames)):
            A = self.com.ActiveCircuit.Buses(idx)
            B = self.capi.ActiveCircuit.Buses(idx)
            assert A.Name == B.Name
            
        for name in self.AllBusNames[-1]:
            A = self.com.ActiveCircuit.Buses(name)
            B = self.capi.ActiveCircuit.Buses(name)
            assert A.Name == B.Name

            
        A = self.com.ActiveCircuit.ActiveBus
        B = self.capi.ActiveCircuit.ActiveBus
        for name in self.AllBusNames[-1]:
            self.capi.ActiveCircuit.SetActiveBus(name)
            self.com.ActiveCircuit.SetActiveBus(name)
            assert A.Name == B.Name
            for field in ('Coorddefined', 'Cust_Duration', 'Cust_Interrupts', 'Distance', 'Int_Duration', 'Isc', 'Lambda', 'N_Customers', 'N_interrupts', 'Nodes', 'NumNodes', 'SectionID', 'TotalMiles', 'VLL', 'VMagAngle', 'Voc', 'Voltages', 'YscMatrix', 'Zsc0', 'Zsc1', 'ZscMatrix', 'kVBase', 'puVLL', 'puVmagAngle', 'puVoltages', 'x', 'y',  'SeqVoltages', 'CplxSeqVoltages'):
                fA = getattr(A, field)
                fB = getattr(B, field)
                output['ActiveCircuit.ActiveBus[{}].{}'.format(name, field)] = fA
                
                if type(fA) == tuple and len(fA) == 0:
                    assert fB is None or len(fB) == 0, ('ActiveBus.{}'.format(field), fA, fB)
                    continue

                if field in ('SeqVoltages', 'CplxSeqVoltages', 'VLL'): continue # skip

                if field == 'CplxSeqVoltages':
                    vA = np.array(A.Voltages).view(dtype=complex)
                    vB = B.Voltages.view(dtype=complex)

                    if len(vA) < 3: continue

                    assert np.allclose(vA, vB, atol=self.atol, rtol=self.rtol), (vA, vB)

                    # a = np.exp(1j*2*np.pi/3)
                    # T012 = float(1)/3*np.array([[1,1,1], [1,a,a**2] ,[1,a**2,a]])
                    # for pyA, pasA, pyB, pasB in zip(
                        # np.dot(vA, T012),
                        # np.array(A.CplxSeqVoltages).view(dtype=complex),
                        # np.dot(vB, T012),
                        # B.CplxSeqVoltages.view(dtype=complex)
                    # ):
                        # assert np.isclose(pyB, pyA, atol=self.atol, rtol=1e-5), ('pyB, pyA =', pyB, pyA)
                    for pasA, pasB in zip(
                        np.array(A.CplxSeqVoltages).view(dtype=complex),
                        np.array(B.CplxSeqVoltages).view(dtype=complex)
                    ):
                        assert np.isclose(pasA, pasB, atol=self.atol, rtol=self.rtol), ('ActiveBus.' + field, name, pasA, pasB)

                    continue

                assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), ('ActiveBus.' + field, name, fA, fB)


    def validate_Capacitors(self):
        A = self.com.ActiveCircuit.Capacitors
        B = self.capi.ActiveCircuit.Capacitors
        assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
        assert A.Count == B.Count
        assert len(A) == len(B)
        nA = A.First
        nB = B.First
        assert nA == nB
        count = 0
        while nA != 0:
            count += 1
            for field in ('States',):
                fA = getattr(A, field)
                fB = getattr(B, field)
                output['ActiveCircuit.Capacitors[{}].{}'.format(nA, field)] = fA
                assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), field

            for field in ('AvailableSteps', 'NumSteps', 'kvar', 'kV', 'Name', 'IsDelta'):
                fA = getattr(A, field)
                fB = getattr(B, field)
                output['ActiveCircuit.Capacitors[{}].{}'.format(nA, field)] = fA
                assert fA == fB, field

            self.validate_CktElement()

            nA = A.Next
            nB = B.Next
            assert nA == nB

        if count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))

    def validate_LineCodes(self):
        A = self.com.ActiveCircuit.LineCodes
        B = self.capi.ActiveCircuit.LineCodes

        assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
        assert A.Count == B.Count
        assert len(A) == len(B)
        nA = A.First
        nB = B.First
        assert nA == nB
        count = 0
        while nA != 0:
            count += 1
            for field in 'Cmatrix,Rmatrix,Xmatrix'.split(','):
                fA = getattr(A, field)
                fB = getattr(B, field)
                output['ActiveCircuit.LineCodes[{}].{}'.format(nA, field)] = fA
                assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), field

            for field in 'C0,C1,EmergAmps,IsZ1Z0,Name,NormAmps,Phases,R0,R1,Units,X0,X1'.split(','):
                fA = getattr(A, field)
                fB = getattr(B, field)
                output['ActiveCircuit.LineCodes[{}].{}'.format(nA, field)] = fA
                assert fA == fB, field

            nA = A.Next
            nB = B.Next
            assert nA == nB

        if count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))

    def validate_Lines(self):
        A = self.com.ActiveCircuit.Lines
        B = self.capi.ActiveCircuit.Lines
        assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
        assert A.Count == B.Count
        assert len(A) == len(B)
        cnt = A.Count

        nA = A.First
        nB = B.First
        assert nA == nB
        count = 0
        while nA != 0:
            count += 1
            for field in 'Cmatrix,Rmatrix,Xmatrix,Yprim'.split(','):
                fA = getattr(A, field)
                fB = getattr(B, field)
                output['ActiveCircuit.Lines[{}].{}'.format(nA, field)] = fA
                assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), field

            # Notes: - removed property Parent from the analysis since it raises a popup
            #        - temporarily removed R1/X1/C1 since COM is broken    
            #for field in 'Bus1,Bus2,C0,C1,EmergAmps,Geometry,Length,LineCode,Name,NormAmps,NumCust,Phases,R0,R1,Rg,Rho,Spacing,TotalCust,Units,X0,X1,Xg'.split(','):
            for field in 'Bus1,Bus2,C0,EmergAmps,Geometry,Length,LineCode,Name,NormAmps,NumCust,Phases,R0,Rg,Rho,Spacing,TotalCust,Units,X0,Xg'.split(','):
                fA = getattr(A, field)
                fB = getattr(B, field)
                output['ActiveCircuit.Lines[{}].{}'.format(nA, field)] = fA
                assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            self.validate_CktElement()

            nA = A.Next
            nB = B.Next
            assert nA == nB

        if count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))


    def validate_Loads(self):
        A = self.com.ActiveCircuit.Loads
        B = self.capi.ActiveCircuit.Loads
        assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
        assert A.Count == B.Count
        assert len(A) == len(B)
        nA = A.First
        nB = B.First
        assert nA == nB
        count = 0
        while nA != 0:
            count += 1
            for field in 'AllocationFactor,CVRcurve,CVRvars,CVRwatts,Cfactor,Class,Growth,IsDelta,Model,Name,NumCust,PF,PctMean,PctStdDev,RelWeight,Rneut,Spectrum,Status,Vmaxpu,Vminemerg,Vminnorm,Vminpu,Xneut,Yearly,daily,duty,idx,kV,kW,kva,kvar,kwh,kwhdays,pctSeriesRL,xfkVA'.split(','): #TODO: ZIPV
                fA = getattr(A, field)
                fB = getattr(B, field)
                output['ActiveCircuit.Loads[{}].{}'.format(nA, field)] = fA
                if type(fB) == float:
                    assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), field
                else:
                    assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            self.validate_CktElement()

            nA = A.Next
            nB = B.Next
            assert nA == nB

        if count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))


    def validate_Loadshapes(self):
        A = self.com.ActiveCircuit.LoadShapes
        B = self.capi.ActiveCircuit.LoadShapes
        assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
        assert A.Count == B.Count
        assert len(A) == len(B)
        nA = A.First
        nB = B.First
        assert nA == nB
        count = 0
        while nA != 0:
            count += 1
            for field in 'Pmult,Qmult,TimeArray'.split(','):
                fA = getattr(A, field)
                fB = getattr(B, field)
                output['ActiveCircuit.LoadShapes[{}].{}'.format(nA, field)] = fA
                assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), field

            for field in 'HrInterval,MinInterval,Name,Npts,Pbase,Qbase,UseActual,Sinterval'.split(','): #TODO: ZIPV
                fA = getattr(A, field)
                fB = getattr(B, field)
                output['ActiveCircuit.LoadShapes[{}].{}'.format(nA, field)] = fA
                assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            nA = A.Next
            nB = B.Next
            assert nA == nB

        if count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))

    def validate_Transformers(self):
        A = self.com.ActiveCircuit.Transformers
        B = self.capi.ActiveCircuit.Transformers
        assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
        assert A.Count == B.Count
        assert len(A) == len(B)
        nA = A.First
        nB = B.First
        assert nA == nB
        count = 0
        while nA != 0:
            count += 1
            for field in 'IsDelta,MaxTap,MinTap,Name,NumTaps,NumWindings,R,Rneut,Tap,Wdg,XfmrCode,Xhl,Xht,Xlt,Xneut,kV,kva'.split(','):
                fA = getattr(A, field)
                fB = getattr(B, field)
                output['ActiveCircuit.Transformers[{}].{}'.format(nA, field)] = fA
                assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            self.validate_CktElement()

            nA = A.Next
            nB = B.Next
            assert nA == nB

        if count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))


    def validate_Generators(self):
        A = self.com.ActiveCircuit.Generators
        B = self.capi.ActiveCircuit.Generators
        assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
        assert A.Count == B.Count
        assert len(A) == len(B)
        nA = A.First
        nB = B.First
        assert nA == nB
        count = 0
        while nA != 0:
            count += 1

            for field in 'RegisterNames'.split(','):
                fA = getattr(A, field)
                fB = getattr(B, field)
                output['ActiveCircuit.Generators[{}].{}'.format(nA, field)] = fA
                if fA == ('',) and fB == [None]: continue # Comtypes and win32com results are a bit different here
                assert all(x[0] == x[1] for x in zip(fA, fB)), field

            for field in 'RegisterValues,kvar'.split(','):
                assert np.allclose(getattr(A, field), getattr(B, field), atol=self.atol, rtol=self.rtol), field


            for field in 'ForcedON,Model,Name,PF,Phases,Vmaxpu,Vminpu,idx,kV,kVArated,kW'.split(','):
                fA = getattr(A, field)
                fB = getattr(B, field)
                output['ActiveCircuit.Generators[{}].{}'.format(nA, field)] = fA
                assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            nA = A.Next
            nB = B.Next
            assert nA == nB


    def validate_Isources(self):
        A = self.com.ActiveCircuit.ISources
        B = self.capi.ActiveCircuit.Isources
        assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
        assert A.Count == B.Count
        assert len(A) == len(B)
        nA = A.First
        nB = B.First
        assert nA == nB
        count = 0
        while nA != 0:
            count += 1
            for field in 'Amps,AngleDeg,Frequency,Name'.split(','):
                fA = getattr(A, field)
                fB = getattr(B, field)
                output['ActiveCircuit.ISources[{}].{}'.format(nA, field)] = fA
                assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            nA = A.Next
            nB = B.Next
            assert nA == nB

        if count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))

    def validate_Vsources(self):
        A = self.com.ActiveCircuit.Vsources
        B = self.capi.ActiveCircuit.Vsources
        assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
        assert A.Count == B.Count
        assert len(A) == len(B)
        nA = A.First
        nB = B.First
        assert nA == nB
        count = 0
        while nA != 0:
            count += 1
            for field in 'AngleDeg,BasekV,Frequency,Name,Phases,pu'.split(','):
                fA = getattr(A, field)
                fB = getattr(B, field)
                output['ActiveCircuit.Vsources[{}].{}'.format(nA, field)] = fA
                assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            nA = A.Next
            nB = B.Next
            assert nA == nB

        if count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))


    def validate_Reclosers(self):
        A = self.com.ActiveCircuit.Reclosers
        B = self.capi.ActiveCircuit.Reclosers
        assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
        assert A.Count == B.Count
        assert len(A) == len(B)
        nA = A.First
        nB = B.First
        assert nA == nB
        count = 0
        while nA != 0:
            count += 1
            for field in 'RecloseIntervals'.split(','):
                fA = getattr(A, field)
                fB = getattr(B, field)
                output['ActiveCircuit.Reclosers[{}].{}'.format(nA, field)] = fA
                fA = np.array(fA, dtype=fB.dtype)
                assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), field

            for field in 'GroundInst,GroundTrip,MonitoredObj,MonitoredTerm,Name,NumFast,PhaseInst,PhaseTrip,Shots,SwitchedObj,SwitchedTerm,idx'.split(','):
                fA = getattr(A, field)
                fB = getattr(B, field)
                output['ActiveCircuit.Reclosers[{}].{}'.format(nA, field)] = fA
                assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)
                
            nA = A.Next
            nB = B.Next
            assert nA == nB

        if count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))



    def validate_XYCurves(self):
        A = self.com.ActiveCircuit.XYCurves
        B = self.capi.ActiveCircuit.XYCurves
    #    assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
        assert A.Count == B.Count
        assert len(A) == len(B)
        nA = A.First
        nB = B.First
        assert nA == nB
        count = 0
        while nA != 0:
            count += 1
            for field in 'Xarray,Yarray'.split(','):
                fA = getattr(A, field)
                fB = getattr(B, field)
                output['ActiveCircuit.XYCurves[{}].{}'.format(nA, field)] = fA
                assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), field

            for field in 'Name,Npts,Xscale,Xshift,Yscale,Yshift,x,y'.split(','):
                fA = getattr(A, field)
                fB = getattr(B, field)
                output['ActiveCircuit.XYCurves[{}].{}'.format(nA, field)] = fA
                assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            nA = A.Next
            nB = B.Next
            assert nA == nB

        if count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))

    def validate_Monitors(self):
        A = self.com.ActiveCircuit.Monitors
        B = self.capi.ActiveCircuit.Monitors
        assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
        assert A.Count == B.Count
        assert len(A) == len(B)
        nA = A.First
        nB = B.First
        assert nA == nB
        count = 0
        while nA != 0:
            count += 1
            for field in 'dblFreq,dblHour'.split(','): # Skipped ByteStream since it's indirectly compared through Channel()
                fA = getattr(A, field)
                fB = getattr(B, field)
                output['ActiveCircuit.Monitors[{}].{}'.format(nA, field)] = fA
                fA = np.array(fA, dtype=fB.dtype)
                assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), field

            #TODO: FileVersion,Header
            for field in 'Element,FileName,Mode,Name,NumChannels,RecordSize,SampleCount,Terminal'.split(','):
                if USE_V8 and field == 'FileName': continue
                fA = getattr(A, field)
                fB = getattr(B, field)
                output['ActiveCircuit.Monitors[{}].{}'.format(nA, field)] = fA
                assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            for channel in range(A.NumChannels):
                fA = A.Channel(channel + 1)
                fB = A.Channel(channel + 1)
                output['ActiveCircuit.Monitors[{}].{}'.format(nA, field)] = fA
                assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), ('Channel', channel + 1)

            nA = A.Next
            nB = B.Next
            assert nA == nB

        if count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))


    def validate_Meters(self):
        A = self.com.ActiveCircuit.Meters
        B = self.capi.ActiveCircuit.Meters
        assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
        assert A.Count == B.Count
        assert len(A) == len(B)
        nA = A.First
        nB = B.First
        assert nA == nB
        count = 0
        while nA != 0:
            count += 1
            for field in 'AllBranchesInZone,AllEndElements,RegisterNames'.split(','):
                fA = getattr(A, field)
                fB = getattr(B, field)
                output['ActiveCircuit.Meters[{}].{}'.format(nA, field)] = fA
                if fA == ('',) and fB == [None]: continue # Comtypes and win32com results are a bit different here
                assert all(x[0] == x[1] for x in zip(fA, fB)), field


            # NOTE: CalcCurrent and AllocFactors removed since it seemed to contain (maybe?) uninitialized values in certain situations
            for field in 'AvgRepairTime,Peakcurrent,RegisterValues,Totals'.split(','):
                fA = getattr(A, field)
                fB = getattr(B, field)
                output['ActiveCircuit.Meters[{}].{}'.format(nA, field)] = fA
                assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), ('Meters("{}").{}'.format(A.Name, field), fA, fB)


            for field in 'CountBranches,CountEndElements,CustInterrupts,DIFilesAreOpen,FaultRateXRepairHrs,MeteredElement,MeteredTerminal,Name,NumSectionBranches,NumSectionCustomers,NumSections,OCPDeviceType,SAIDI,SAIFI,SAIFIKW,SectSeqIdx,SectTotalCust,SeqListSize,SequenceIndex,SumBranchFltRates,TotalCustomers'.split(','):
                fA = getattr(A, field)
                fB = getattr(B, field)
                output['ActiveCircuit.Meters[{}].{}'.format(nA, field)] = fA
                assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            nA = A.Next
            nB = B.Next
            assert nA == nB

        if count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))

    def validate_Settings(self):
        A = self.com.ActiveCircuit.Settings
        B = self.capi.ActiveCircuit.Settings

        for field in 'LossRegs,UEregs,VoltageBases'.split(','):
            assert np.allclose(getattr(A, field), getattr(B, field), atol=self.atol, rtol=self.rtol), field

        for field in 'AllowDuplicates,AutoBusList,CktModel,ControlTrace,EmergVmaxpu,EmergVminpu,LossWeight,NormVmaxpu,NormVminpu,PriceCurve,PriceSignal,Trapezoidal,UEweight,ZoneLock'.split(','):
            fA = getattr(A, field)
            fB = getattr(B, field)
            output['ActiveCircuit.Settings.{}'.format(field)] = fA
            assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

    def validate_Solution(self):
        A = self.com.ActiveCircuit.Solution
        B = self.capi.ActiveCircuit.Solution

        for field in 'AddType,Algorithm,Capkvar,ControlActionsDone,ControlIterations,ControlMode,Converged,DefaultDaily,DefaultYearly,Frequency,GenMult,GenPF,GenkW,Hour,Iterations,LDCurve,LoadModel,LoadMult,MaxControlIterations,MaxIterations,Mode,ModeID,MostIterationsDone,Number,Random,Seconds,StepSize,SystemYChanged,Tolerance,Totaliterations,Year,dblHour,pctGrowth'.split(','): #TODO: EventLog, IntervalHrs, MinIterations, Process_Time, Total_Time, Time_of_Step
            fA = getattr(A, field)
            fB = getattr(B, field)
            output['ActiveCircuit.Solution.{}'.format(field)] = fA
            assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)


    def _get_circuit_fields(self):
        return {
            "AllBusDistances" : self.AllBusDistances,
            "AllBusNames" : self.AllBusNames,
            "AllBusVmag" : self.AllBusVmag,
            "AllBusVmagPu" : self.AllBusVmagPu,
            "AllBusVolts" : self.AllBusVolts,
            "AllElementLosses" : self.AllElementLosses,
            "AllElementNames" : self.AllElementNames,
            "AllNodeDistances" : self.AllNodeDistances,
            "AllNodeNames" : self.AllNodeNames,
            "LineLosses" : self.LineLosses,
            "Losses" : self.Losses,
            "Name" : self.Name,
            "NumBuses" : self.NumBuses,
            "NumCktElements" : self.NumCktElements,
            "NumNodes" : self.NumNodes,
            "ParentPDElement" : self.ParentPDElement,
            "SubstationLosses" : self.SubstationLosses,
            "SystemY" : self.SystemY,
            "TotalPower" : self.TotalPower,
            "YCurrents" : self.YCurrents,
            "YNodeOrder" : self.YNodeOrder,
            "YNodeVarray" : self.YNodeVarray,
        }
    
            
    def validate_Circuit(self):
        all_fields = self._get_circuit_fields()
        
        # Get all line names
        lines_names = []
        LA = self.com.ActiveCircuit.Lines
        nA = LA.First
        while nA != 0:
            lines_names.append(LA.Name)
            nA = LA.Next
            
        # Test Circuit_SetCktElementName with line names
        for name in lines_names:
            A = self.capi.ActiveCircuit.CktElements('Line.' + name)
            B = self.com.ActiveCircuit.CktElements('Line.' + name)
            assert A.Name == B.Name
            
        # Test Circuit_SetCktElementIndex
        for idx in range(len(self.AllBusNames[-1])):
            # Note: idx is not the bus index but it is a valid CktElement index 
            A = self.capi.ActiveCircuit.CktElements(idx)
            B = self.com.ActiveCircuit.CktElements(idx)
            assert A.Name == B.Name

        # Try to use an invalid index
        A = self.capi.ActiveCircuit.CktElements(999999)
        B = self.com.ActiveCircuit.CktElements(999999)
        assert A.Name == B.Name

        # Try to use an invalid name
        A = self.capi.ActiveCircuit.CktElements('NONEXISTENT_123456789')
        B = self.com.ActiveCircuit.CktElements('NONEXISTENT_123456789')
        assert A.Name == B.Name
        
        for k, v in all_fields.items():
            if type(v[1]) == np.ndarray:
                print(k, max(abs(v[1] - v[0])))
                assert np.allclose(*v, atol=self.atol, rtol=self.rtol), (k, type(v[1]))
            elif type(v[1]) == list:
                assert all(x[0] == x[1] for x in zip(*v)), (k, type(v[1]))
            elif type(v[1]) == int:
                assert v[0] == v[1], (k, type(v[1]))
            elif type(v[1]) == float:
                assert abs(v[0] - v[1]) < atol, (k, type(v[1]))

    def validate_YMatrix(self):
        NN = self.capi.ActiveCircuit.NumNodes
        if NN > 2000: # test only on small strings
            return
            
        ysparse = csc_matrix(self.capi.YMatrix.GetCompressedYMatrix(factor=False))
        ydense = self.capi.ActiveCircuit.SystemY.view(dtype=complex).reshape((NN, NN))
        assert (np.allclose(ydense, ysparse.todense(), atol=self.atol, rtol=self.rtol))
        
                
    def validate_all(self):
        self.rtol = 1e-5

        # print('LineCodes')
        self.validate_LineCodes()
        # print('Capacitors')
        self.validate_Capacitors()
        # print('Lines')
        self.validate_Lines()
        # print('Loads')
        self.validate_Loads()
        # print('Loadshapes')
        self.validate_Loadshapes()
        # print('Transformers')
        self.validate_Transformers()
        # print('Settings')
        self.validate_Settings()
        # print('Solution')
        self.validate_Solution()
        # print('Isources')
        self.validate_Isources()
        # print('Vsources')
        self.validate_Vsources()
        # print('Generators')
        self.validate_Generators()
        # print('XYCurves')
        self.validate_XYCurves()
        # print('Monitors')
        self.validate_Monitors()
        # print('Meters')
        self.validate_Meters()
        # print('Reclosers')
        self.validate_Reclosers()
        # print('YMatrix')
        self.validate_YMatrix()

        #self.atol = 1e-5
        # print('Buses')
        self.validate_Buses()
        # print('Circuit')
        self.validate_Circuit()

        self.capi.ShowPanel()
        
        print('Done')


def run_tests(fns):
    if USE_V8:
        from dss.v8 import DSS, use_com_compat
        print("Imported DSS V8 version")
    else:
        from dss.v7 import DSS, use_com_compat
        print("Imported DSS V7 version")
        
    use_com_compat()

    # NOTE: if win32com errors out, rerun until all files are generated
    import win32com.client
    com = win32com.client.Dispatch("OpenDSSEngine.DSS")
    com = win32com.client.gencache.EnsureDispatch("OpenDSSEngine.DSS")

    #import comtypes.client
    #com = comtypes.client.CreateObject("OpenDSSEngine.DSS")

    capi = DSS

    # Test toggling console output with C-API, COM can only be disabled
    for dss in com, capi:
        dss.AllowForms = True
        assert dss.AllowForms == True

        dss.AllowForms = False
        assert dss.AllowForms == False
        
        dss.AllowForms = True
        if dss != com:
            assert dss.AllowForms == True

        dss.AllowForms = False
        assert dss.AllowForms == False
            
    total_com_time = 0.0
    total_capi_time = 0.0
            
    global output
    
    for fn in fns:
        line_by_line = fn.startswith('L!')
        if line_by_line:
            fn = fn[2:]

        print("> File", fn)
        test = ValidatingTest(fn, com, capi, line_by_line)

        if sys.platform == 'win32':
            print("Running using COM")
            t0 = time()
            test.run(com, solve=True)
            total_com_time += time() - t0
            output['ActiveCircuit'] = test._get_circuit_fields()
            
        
        print("Running using CAPI")
        t0 = time()
        test.run(capi, solve=True)
        total_capi_time += time() - t0  
        
        
        print("Validating")
        try:
            test.validate_all()
        except AssertionError as ex:
            print('!!!!!!!!!!!!!!!!!!!!!!')
            print('ERROR:', fn, ex)
            print('!!!!!!!!!!!!!!!!!!!!!!')

            
        if sys.platform == 'win32' and SAVE_COM_OUTPUT:
            os.chdir(original_working_dir)
            pickle_fn = fn + '.pickle'
            with open(pickle_fn, 'wb') as com_output_file:
                pickle.dump(output, com_output_file, protocol=pickle.HIGHEST_PROTOCOL)
                print('COM output pickled to', pickle_fn)
            
            output = type(output)()
            
           

    print("Total COM running time: {} seconds".format(int(total_com_time)))
    print("Total C-API running time: {} seconds ({}% of COM)".format(
        int(total_capi_time), 
        round(100 * total_capi_time / total_com_time, 1)
    ))
            
            
if __name__ == '__main__':
    from common import test_filenames
    t0_global = time()
    run_tests(test_filenames)
    print(time() - t0_global, 'seconds')