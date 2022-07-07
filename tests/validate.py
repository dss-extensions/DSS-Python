import os, sys, platform, traceback, pickle
import concurrent.futures
from threading import current_thread, local
from time import time
import numpy as np
from scipy.sparse import csc_matrix
from dss import enums
from dss import DSSException


original_working_dir = os.getcwd()
NO_PROPERTIES = os.getenv('DSS_PYTHON_VALIDATE') == 'NOPROP'
NO_V9 = False
WIN32 = (sys.platform == 'win32')

COM_VLL_BROKEN = True

num_failures = 0

USE_THREADS = True

SAVE_OUTPUT = 'save' in sys.argv
LOAD_OUTPUT = (not WIN32) or ('load' in sys.argv) 
SAVE_DSSX_OUTPUT = SAVE_OUTPUT and ('dss-extensions' in sys.argv)
LOAD_PLATFORM = None

if SAVE_OUTPUT:
    LOAD_OUTPUT = False

    class FakeDict:
        def __setitem__(self, key, value):
            # ignore the value
            pass

    
if LOAD_OUTPUT:
    LOAD_PLATFORM = sys.argv[-1] 

if LOAD_OUTPUT or SAVE_OUTPUT:
    import zstandard as zstd

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
    def __init__(self, fn, dss_variants, line_by_line):
        self.fn = fn
        if len(dss_variants) == 2:
            self.dss_a, self.dss_b = dss_variants
        else:
            if SAVE_OUTPUT:
                self.dss_a, self.dss_b = dss_variants[0], None
            else:
                self.dss_a, self.dss_b = None, dss_variants[0]

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
        dss.Text.Command = f'cd "{original_working_dir}"'
        dss.Start(0)
        
        # Reset script -- EarthModel is not properly reset with just a Clear
        dss.Text.Command = 'Clear'
        dss.Text.Command = 'new circuit.RESET'
        dss.Text.Command = 'Set DefaultBaseFreq=60'
        dss.Text.Command = 'Set EarthModel=deri'
        dss.Text.Command = 'new wiredata.wire Runits=mi Rac=0.306 GMRunits=ft GMRac=0.0244  Radunits=in Diam=0.721'
        dss.Text.Command = 'new linegeometry.reset nconds=1 nphases=1 cond=1 wire=wire units=ft x=-4 h=28'
        dss.Text.Command = 'new line.line1 geometry=reset length=2000 units=ft bus1=sourcebus bus2=n2'
        dss.Text.Command = 'solve'
        dss.Text.Command = 'Clear'

        if self.line_by_line:
            with open(self.fn, 'r') as f:

                dss.Text.Command = f'cd "{os.path.dirname(self.fn)}"'
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
                            input_line = input_line.replace('C:\\Users\\prdu001\\OpenDSS\\Distrib\\Examples\\Scripts\\', '../Version8/Distrib/Examples/Scripts/')
                            #print(input_line)
                            dss.Text.Command = input_line
                except StopIteration:
                    pass
        else:
            dss.Text.Command = 'Compile "{}"'.format(self.fn)


        if solve:
            dss.ActiveCircuit.Solution.Mode = enums.SolveModes.Daily
            dss.ActiveCircuit.Solution.Solve()

        self.realibity_ran = True
        try:
            dss.ActiveCircuit.Meters.DoReliabilityCalc(False)
        except DSSException as ex:
            if ex.args[0] == 52902:
                self.realibity_ran = False
            
                

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
        num_nodes = dss.ActiveCircuit.NumNodes
        # if ((num_nodes * num_nodes * 16) >> 20) < 500:
            # self.SystemY.append(dss.ActiveCircuit.SystemY)
        
        self.TotalPower.append(dss.ActiveCircuit.TotalPower)
        self.YCurrents.append(dss.ActiveCircuit.YCurrents)
        self.YNodeOrder.append(dss.ActiveCircuit.YNodeOrder)
        self.YNodeVarray.append(dss.ActiveCircuit.YNodeVarray)


    def validate_CktElement(self):
        if LOAD_OUTPUT or SAVE_OUTPUT: 
            #TODO: not implemented
            return
        
        A = self.dss_a.ActiveCircuit.ActiveElement
        B = self.dss_b.ActiveCircuit.ActiveElement

        for field in ['AllPropertyNames']:
            fA = set(x.lower() for x in getattr(A, field))
            fB = set(x.lower() for x in getattr(B, field))
            for propA in fA:
                assert propA in fB, propA
                
            # Since the list of properties vary in releases, 
            # we don't check it the list is the same anymore.
            # if not SAVE_OUTPUT: assert all(x[0] == x[1] for x in zip(fA, fB)), (field, fA, fB)
            
        for field in 'AllVariableNames,BusNames'.split(','):
            fA = getattr(A, field)
            if not SAVE_OUTPUT: 
                fB = getattr(B, field)
                if fA == ('',) and fB == [None]: continue # comtypes and win32com results are a bit different here
                assert all(x[0] == x[1] for x in zip(fA, fB)), (field, fA, fB)
            
          
        # Check if setting bus names works
        BusNames = list(A.BusNames)
        A.BusNames = BusNames
        B.BusNames = BusNames

        # Check if they match again
        field = 'BusNames'
        fA = getattr(A, field)
        if not SAVE_OUTPUT: 
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
                if val_A.lower() == val_B.lower():
                    continue
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
                    if (val_A.startswith('[') and val_A.endswith(']')) or (val_A.startswith('(') and val_A.endswith(')')):
                        val_A = parse_dss_matrix(val_A)
                        val_B = parse_dss_matrix(val_B)
                        if not isinstance(val_A, str):
                            is_equal = True
                            for row_A, row_B in zip(val_A, val_B):
                                if not np.allclose(row_A, row_B, atol=self.atol, rtol=self.rtol):
                                    is_equal = False
                                    break
                    
                # special treatment for WdgCurrents, which uses a CSV of %.7g, (%.5g) -- Mag (Ang)
                if prop_name == 'WdgCurrents': 
                    val_A = A.Properties(prop_name).Val.replace('(', ' ').replace(')', ' ').strip(' ').strip(',')
                    val_B = B.Properties(prop_name).Val.replace('(', ' ').replace(')', ' ').strip(' ').strip(',')
                    nval_A = np.fromstring(val_A, dtype=float, sep=',')
                    nval_B = np.fromstring(val_B, dtype=float, sep=',')
                    
                    mag_A = nval_A[::2]
                    mag_B = nval_B[::2]
                    rad_A = np.radians(nval_A[1::2])
                    rad_B = np.radians(nval_B[1::2])
                    
                    c_A = mag_A * (np.cos(rad_A) + 1j * np.sin(rad_A))
                    c_B = mag_B * (np.cos(rad_B) + 1j * np.sin(rad_B))
                    
                    is_equal = np.allclose(c_A, c_B, atol=1e-5, rtol=1e-4)

                elif prop_name == 'ZIPV':
                    if A.Properties(prop_name).Val == '':
                        is_equal = B.Properties(prop_name).Val == ' 0 0 0 0 0 0 0'
                        
                
                allow_lower = set(['conn'])

                if not (is_equal or val_A == val_B or A.Properties(prop_name).Val == B.Properties(prop_name).Val or (prop_name in allow_lower and A.Properties(prop_name).Val.lower() == B.Properties(prop_name).Val.lower())):
                    print('ERROR: CktElement({}).Properties({}).Val'.format(A.Name, prop_name), repr(A.Properties(prop_name).Val), repr(B.Properties(prop_name).Val))
            
            if not SAVE_OUTPUT: assert (A.Properties(prop_name).Name.lower() == B.Properties(prop_name).Name.lower()), ('Properties({}).name'.format(prop_name), A.Properties(prop_name).Name, B.Properties(prop_name).Name)

            if not SAVE_OUTPUT: assert (B.Properties(prop_name).Val == B.Properties[prop_name].Val)
            if not SAVE_OUTPUT: assert (B.Properties(prop_name).Description == B.Properties[prop_name].Description)
            if not SAVE_OUTPUT: assert (B.Properties(prop_name).Name == B.Properties[prop_name].Name)


    def validate_Buses(self):
        if not LOAD_OUTPUT:
            for idx in range(len(self.AllBusNames)):
                A = self.dss_a.ActiveCircuit.Buses(idx)
                if not SAVE_OUTPUT: 
                    B = self.dss_b.ActiveCircuit.Buses(idx)
                    assert A.Name == B.Name
                
            for name in self.AllBusNames[-1]:
                A = self.dss_a.ActiveCircuit.Buses(name)
                if not SAVE_OUTPUT: 
                    B = self.dss_b.ActiveCircuit.Buses(name)
                    assert A.Name == B.Name
            
            A = self.dss_a.ActiveCircuit.ActiveBus
        
        if not SAVE_OUTPUT:
            B = self.dss_b.ActiveCircuit.ActiveBus

        for name in self.AllBusNames[-1]:
            if not LOAD_OUTPUT:
                self.dss_a.ActiveCircuit.SetActiveBus(name)

            if not SAVE_OUTPUT:
                self.dss_b.ActiveCircuit.SetActiveBus(name)

            if not LOAD_OUTPUT and not SAVE_OUTPUT: 
                assert A.Name == B.Name
                
            if (self.dss_b if self.dss_b is not None else self.dss_a).ActiveCircuit.NumNodes < 1000 and not NO_V9:
                for field in ['LoadList', 'LineList']:#, 'AllPCEatBus', 'AllPDEatBus']:
                    fA = self.output[f'ActiveCircuit.ActiveBus[{name}].{field}'] if LOAD_OUTPUT else getattr(A, field)
                    if SAVE_OUTPUT: 
                        self.output[f'ActiveCircuit.ActiveBus[{name}].{field}'] = fA
                    else:
                        fB = getattr(B, field)
                        assert list(fA) == list(fB), (fA, fB)
                    

            for field in ('Coorddefined', 'Cust_Duration', 'Cust_Interrupts', 'Distance', 'Int_Duration', 'Isc', 'Lambda', 'N_Customers', 'N_interrupts', 'Nodes', 'NumNodes', 'SectionID', 'TotalMiles', 'VLL', 'VMagAngle', 'Voc', 'Voltages', 'YscMatrix', 'Zsc0', 'Zsc1', 'ZscMatrix', 'kVBase', 'puVLL', 'puVmagAngle', 'puVoltages', 'x', 'y',  'SeqVoltages', 'CplxSeqVoltages'):
                if COM_VLL_BROKEN and field in ('VLL', 'puVLL'):
                    continue

                fA = self.output[f'ActiveCircuit.ActiveBus[{name}].{field}'] if LOAD_OUTPUT else getattr(A, field)
                if SAVE_OUTPUT:
                    self.output[f'ActiveCircuit.ActiveBus[{name}].{field}'] = fA

                if not SAVE_OUTPUT: 
                    fB = getattr(B, field)

                if type(fA) == tuple and len(fA) == 0:
                    if not SAVE_OUTPUT:
                        assert fB is None or len(fB) == 0, ('ActiveBus.{}'.format(field), fA, fB)
                    continue

                if field in ('SeqVoltages', 'CplxSeqVoltages', 'VLL'): continue # skip

                if field == 'CplxSeqVoltages':
                    vA = np.array(A.Voltages).view(dtype=complex)

                    if len(vA) < 3: continue

                    if not SAVE_OUTPUT: 
                        vB = B.Voltages.view(dtype=complex)                        
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

                if field in ('VMagAngle', 'puVmagAngle'):
                    fA = np.asarray(fA)
                    aa = np.deg2rad(fA[1::2])
                    fA = fA[::2] * (np.cos(aa) + 1j * np.sin(aa))

                    if not SAVE_OUTPUT:
                        fB = np.asarray(fB)                    
                        ab = np.deg2rad(fB[1::2])
                        fB = fB[::2] * (np.cos(ab) + 1j * np.sin(ab))
               
                elif field in ('Voltages', 'puVLL', 'puVoltages') and (len(fA) % 2 == 0):
                    fA = np.asarray(fA).view(dtype=complex)
                    if not SAVE_OUTPUT: 
                        fB = np.asarray(fB).view(dtype=complex)
                

                if not SAVE_OUTPUT: 
                    assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), ('ActiveBus.' + field, name, fA, fB)


    def validate_Capacitors(self):
        A, B = None, None
        if not SAVE_OUTPUT:
            B = self.dss_b.ActiveCircuit.Capacitors
        
        if not LOAD_OUTPUT: 
            A = self.dss_a.ActiveCircuit.Capacitors
            nA = A.First
            if not SAVE_OUTPUT: 
                assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
                assert A.Count == B.Count
                assert len(A) == len(B)
                nB = B.First
                assert nA == nB
        else:
            nA = nB = (B if B is not None else A).First

        count = 0
        while nA != 0:
            count += 1
            for field in ('States',):
                fA = self.output['ActiveCircuit.Capacitors[{}].{}'.format(nA, field)] if LOAD_OUTPUT else getattr(A, field)
                if SAVE_OUTPUT: self.output['ActiveCircuit.Capacitors[{}].{}'.format(nA, field)] = fA
                if not SAVE_OUTPUT: 
                    fB = getattr(B, field)
                    assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), field

            for field in ('AvailableSteps', 'NumSteps', 'kvar', 'kV', 'Name', 'IsDelta'):
                fA = self.output['ActiveCircuit.Capacitors[{}].{}'.format(nA, field)] if LOAD_OUTPUT else getattr(A, field)
                if SAVE_OUTPUT: self.output['ActiveCircuit.Capacitors[{}].{}'.format(nA, field)] = fA
                if not SAVE_OUTPUT: 
                    fB = getattr(B, field)
                    assert fA == fB, field

            self.validate_CktElement()

            if not SAVE_OUTPUT: 
                nB = B.Next
            if not LOAD_OUTPUT: 
                nA = A.Next
                if not SAVE_OUTPUT: 
                    assert nA == nB
            else:
                nA = nB

        # if not LOAD_OUTPUT and count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))


    def validate_LineCodes(self):
        A, B = None, None
        if not SAVE_OUTPUT:
            B = self.dss_b.ActiveCircuit.LineCodes

        if not LOAD_OUTPUT: 
            A = self.dss_a.ActiveCircuit.LineCodes
            
            has_AllNames = True
            try:
                _ = A.AllNames
            except:
                has_AllNames = False
               
            if has_AllNames:
                if not SAVE_OUTPUT: 
                    assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))

            nA = A.First
            if not SAVE_OUTPUT: 
                nB = B.First
                assert A.Count == B.Count, (A.Count, B.Count)
                assert len(A) == len(B)
                assert nA == nB
        else:
            nA = nB = (B if B is not None else A).First
            
            
        count = 0
        while nA != 0:
            count += 1
            for field in 'Cmatrix,Rmatrix,Xmatrix'.split(','):
                fA = self.output['ActiveCircuit.LineCodes[{}].{}'.format(nA, field)] if LOAD_OUTPUT else getattr(A, field)
                if SAVE_OUTPUT: self.output['ActiveCircuit.LineCodes[{}].{}'.format(nA, field)] = fA
                if not SAVE_OUTPUT: 
                    fB = getattr(B, field)
                    assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB, B.Name)

#            for field in 'C0,C1,EmergAmps,IsZ1Z0,Name,NormAmps,Phases,R0,R1,Units,X0,X1'.split(','):
            for field in 'EmergAmps,IsZ1Z0,Name,NormAmps,Phases,R0,R1,Units,X0,X1'.split(','):
                fA = self.output['ActiveCircuit.LineCodes[{}].{}'.format(nA, field)] if LOAD_OUTPUT else getattr(A, field)
                if SAVE_OUTPUT: self.output['ActiveCircuit.LineCodes[{}].{}'.format(nA, field)] = fA
                if not SAVE_OUTPUT: 
                    fB = getattr(B, field)
                    assert fA == fB or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB, B.Name)

            if not SAVE_OUTPUT:
                nB = B.Next
            if not LOAD_OUTPUT: 
                nA = A.Next
                if not SAVE_OUTPUT: 
                    assert nA == nB
            else:
                nA = nB

        if not LOAD_OUTPUT and count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))

        
    def validate_Lines(self):
        A, B = None, None
        if not SAVE_OUTPUT:
            B = self.dss_b.ActiveCircuit.Lines
        
        if not LOAD_OUTPUT: 
            A = self.dss_a.ActiveCircuit.Lines
            nA = A.First
            if not SAVE_OUTPUT: 
                nB = B.First
                assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
                assert A.Count == B.Count
                assert len(A) == len(B)
                assert nA == nB
        else:
            nA = nB = (B if B is not None else A).First
            
        count = 0
        while nA != 0:
            count += 1
            # Notes: - removed property Parent from the analysis since it raises a popup
            #        - temporarily removed R1/X1/C1 since COM is broken    
            #for field in 'Bus1,Bus2,C0,C1,EmergAmps,Geometry,Length,LineCode,Name,NormAmps,NumCust,Phases,R0,R1,Rg,Rho,Spacing,TotalCust,Units,X0,X1,Xg'.split(','):
            for field in 'Bus1,Bus2,C0,EmergAmps,Geometry,Length,LineCode,Name,NormAmps,NumCust,Phases,R0,Rg,Rho,Spacing,TotalCust,Units,X0,Xg'.split(','):
                fA = self.output['ActiveCircuit.Lines[{}].{}'.format(nA, field)] if LOAD_OUTPUT else getattr(A, field)
                if SAVE_OUTPUT: self.output['ActiveCircuit.Lines[{}].{}'.format(nA, field)] = fA
                if not SAVE_OUTPUT: 
                    fB = getattr(B, field)
                    assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            for field in 'Cmatrix,Rmatrix,Xmatrix,Yprim'.split(','):
                key = 'ActiveCircuit.Lines[{}].{}'.format(nA, field)
                fA = self.output[key] if LOAD_OUTPUT else getattr(A, field)
                if SAVE_OUTPUT: self.output['ActiveCircuit.Lines[{}].{}'.format(nA, field)] = fA
                if not SAVE_OUTPUT: 
                    fB = getattr(B, field)
                    assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB, max(abs(fA - fB)), B.Name)

            self.validate_CktElement()

            if not SAVE_OUTPUT:
                nB = B.Next
            if not LOAD_OUTPUT: 
                nA = A.Next
                if not SAVE_OUTPUT: 
                    assert nA == nB
            else:
                nA = nB

        if not LOAD_OUTPUT and count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))


    def validate_Loads(self):
        A = B = None
        if not SAVE_OUTPUT:
            B = self.dss_b.ActiveCircuit.Loads
        
        if not LOAD_OUTPUT: 
            A = self.dss_a.ActiveCircuit.Loads
            nA = A.First
            if not SAVE_OUTPUT: 
                nB = B.First
                assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
                assert A.Count == B.Count
                assert len(A) == len(B)
                assert nA == nB
        else:
            nA = nB = (B if B is not None else A).First
            
        count = 0
        while nA != 0:
            count += 1
            # yearly was removed, duty is broken everywhere before 2021-10 (at least)
            for field in 'AllocationFactor,CVRcurve,CVRvars,CVRwatts,Cfactor,Class,Growth,IsDelta,Model,Name,NumCust,PF,PctMean,PctStdDev,RelWeight,Rneut,Spectrum,Status,Vmaxpu,Vminemerg,Vminnorm,Vminpu,Xneut,daily,idx,kV,kW,kva,kvar,kwh,kwhdays,pctSeriesRL,xfkVA'.split(','): #TODO: ZIPV
                fA = self.output['ActiveCircuit.Loads[{}].{}'.format(nA, field)] if LOAD_OUTPUT else getattr(A, field)
                if SAVE_OUTPUT: self.output['ActiveCircuit.Loads[{}].{}'.format(nA, field)] = fA
                if not SAVE_OUTPUT: 
                    fB = getattr(B, field)
                    if type(fB) == float:
                        assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, B.Name, fA, fB)
                    else:
                        if type(fB) == str:
                            if fA is None:
                                assert fB == '', (field, fA, fB)
                            else:
                                assert fA.lower() == fB.lower(), (field, fA, fB)
                        else:
                            assert (fA == fB) or (type(fB) == str and ((fA is None and fB == '') or (fA.lower() == fB.lower()))) or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            self.validate_CktElement()

            if not SAVE_OUTPUT: 
                nB = B.Next
            if not LOAD_OUTPUT: 
                nA = A.Next
                if not SAVE_OUTPUT: 
                    assert nA == nB
            else:
                nA = nB

        if not LOAD_OUTPUT and count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))


    def validate_Loadshapes(self):
        A, B = None, None
        if not SAVE_OUTPUT:
            B = self.dss_b.ActiveCircuit.LoadShapes
        
        if not LOAD_OUTPUT: 
            A = self.dss_a.ActiveCircuit.LoadShapes
            nA = A.First
            if not SAVE_OUTPUT: 
                assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
                assert A.Count == B.Count
                assert len(A) == len(B)
                nB = B.First
                assert nA == nB
        else:
            nA = nB = (B if B is not None else A).First
            
        count = 0
        while nA != 0:
            count += 1
            for field in 'HrInterval,MinInterval,Name,Npts,Pbase,Qbase,UseActual,Sinterval'.split(','): #TODO: ZIPV
                fA = self.output['ActiveCircuit.LoadShapes[{}].{}'.format(nA, field)] if LOAD_OUTPUT else getattr(A, field)
                if SAVE_OUTPUT: self.output['ActiveCircuit.LoadShapes[{}].{}'.format(nA, field)] = fA
                if not SAVE_OUTPUT: 
                    fB = getattr(B, field)
                    assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            for field in 'Pmult,Qmult,TimeArray'.split(','):
                fA = self.output['ActiveCircuit.LoadShapes[{}].{}'.format(nA, field)] if LOAD_OUTPUT else getattr(A, field)
                if SAVE_OUTPUT: self.output['ActiveCircuit.LoadShapes[{}].{}'.format(nA, field)] = fA
                if not SAVE_OUTPUT: 
                    fB = getattr(B, field)
                    assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, list(fB), B.Name)

            if not SAVE_OUTPUT: 
                nB = B.Next
            if not LOAD_OUTPUT: 
                nA = A.Next
                if not SAVE_OUTPUT: 
                    assert nA == nB
            else:
                nA = nB

        if not LOAD_OUTPUT and count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))


    def validate_Transformers(self):
        A = B = None
        if not SAVE_OUTPUT:
            B = self.dss_b.ActiveCircuit.Transformers
            B_element = self.dss_b.ActiveCircuit.CktElements
            
            # Validate the LossesByType extension
            if B.Count:
                AllLossesByType = B.AllLossesByType.view(dtype=complex).reshape((B.Count, 3))
                for tr, losses in zip(B, AllLossesByType):
                    assert np.all(losses == B.LossesByType.view(dtype=complex))
                    assert np.allclose(losses[0], losses[1] + losses[2], atol=self.atol, rtol=self.rtol) 
                    assert np.allclose(losses[0], losses[1] + losses[2], atol=self.atol, rtol=self.rtol) 
                    assert B_element.Losses.view(dtype=complex) == losses[0]


        if not LOAD_OUTPUT: 
            A = self.dss_a.ActiveCircuit.Transformers
            nA = A.First
            if not SAVE_OUTPUT: 
                nB = B.First
                assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
                assert A.Count == B.Count
                assert len(A) == len(B)
                assert nA == nB
        else:
            nA = nB = (B if B is not None else A).First
        
        count = 0
        while nA != 0:
            count += 1

            #for field in 'IsDelta,MaxTap,MinTap,Name,NumTaps,NumWindings,R,Rneut,Tap,Wdg,XfmrCode,Xhl,Xht,Xlt,Xneut,kV,kva'.split(','):
            for field in 'IsDelta,MaxTap,MinTap,Name,NumTaps,NumWindings,R,Rneut,Tap,Wdg,XfmrCode,Xneut,kV,kva'.split(','):
                fA = self.output['ActiveCircuit.Transformers[{}].{}'.format(nA, field)] if LOAD_OUTPUT else getattr(A, field)
                if SAVE_OUTPUT: 
                    self.output['ActiveCircuit.Transformers[{}].{}'.format(nA, field)] = fA
                if not SAVE_OUTPUT: 
                    fB = getattr(B, field)
                    assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            self.validate_CktElement()

            if not SAVE_OUTPUT: 
                nB = B.Next
            if not LOAD_OUTPUT: 
                nA = A.Next
                if not SAVE_OUTPUT: 
                    assert nA == nB
            else:
                nA = nB

        if not LOAD_OUTPUT and count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))


    def validate_Generators(self):
        A, B = None, None
        if not SAVE_OUTPUT:
            B = self.dss_b.ActiveCircuit.Generators

        if not LOAD_OUTPUT: 
            A = self.dss_a.ActiveCircuit.Generators
            nA = A.First
            if not SAVE_OUTPUT: 
                nB = B.First
                assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
                assert A.Count == B.Count
                assert len(A) == len(B)
                assert nA == nB
        else:
            nA = nB = (B if B is not None else A).First
        
        count = 0
        while nA != 0:
            count += 1

            for field in 'RegisterNames'.split(','):
                fA = self.output['ActiveCircuit.Generators[{}].{}'.format(nA, field)] if LOAD_OUTPUT else getattr(A, field)
                if SAVE_OUTPUT: self.output['ActiveCircuit.Generators[{}].{}'.format(nA, field)] = fA
                if not SAVE_OUTPUT: 
                    if fA == ('',) and fB == [None]: continue # Comtypes and win32com results are a bit different here
                    fB = getattr(B, field)
                    assert all(x[0] == x[1] for x in zip(fA, fB)), field

            for field in 'RegisterValues,kvar'.split(','):
                fA = self.output['ActiveCircuit.Generators[{}].{}'.format(nA, field)] if LOAD_OUTPUT else getattr(A, field)
                if SAVE_OUTPUT: self.output['ActiveCircuit.Generators[{}].{}'.format(nA, field)] = fA
                if not SAVE_OUTPUT: 
                    fB = getattr(B, field)
                    assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), field


            for field in 'ForcedON,Model,Name,PF,Phases,Vmaxpu,Vminpu,idx,kV,kVArated,kW'.split(','):
                fA = self.output['ActiveCircuit.Generators[{}].{}'.format(nA, field)] if LOAD_OUTPUT else getattr(A, field)
                if SAVE_OUTPUT: self.output['ActiveCircuit.Generators[{}].{}'.format(nA, field)] = fA
                if not SAVE_OUTPUT: 
                    fB = getattr(B, field)
                    assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            if not SAVE_OUTPUT: 
                nB = B.Next
            if not LOAD_OUTPUT: 
                nA = A.Next
                if not SAVE_OUTPUT: 
                    assert nA == nB
            else:
                nA = nB


    def validate_Isources(self):
        A, B = None, None
        if not SAVE_OUTPUT:
            B = self.dss_b.ActiveCircuit.Isources

        if not LOAD_OUTPUT: 
            A = self.dss_a.ActiveCircuit.ISources
            nA = A.First
            if not SAVE_OUTPUT: 
                nB = B.First
                assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
                assert A.Count == B.Count
                assert len(A) == len(B)
                assert nA == nB
        else:
            nA = nB = (B if B is not None else A).First
        
        count = 0
        while nA != 0:
            count += 1
            for field in 'Amps,AngleDeg,Frequency,Name'.split(','):
                fA = self.output['ActiveCircuit.ISources[{}].{}'.format(nA, field)] if LOAD_OUTPUT else getattr(A, field)
                if SAVE_OUTPUT: self.output['ActiveCircuit.ISources[{}].{}'.format(nA, field)] = fA
                if not SAVE_OUTPUT: 
                    fB = getattr(B, field)
                    assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            if not SAVE_OUTPUT: 
                nB = B.Next
            if not LOAD_OUTPUT: 
                nA = A.Next
                if not SAVE_OUTPUT: 
                    assert nA == nB
            else:
                nA = nB
        if not LOAD_OUTPUT and count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))

        
    def validate_Vsources(self):
        A, B = None, None
        if not SAVE_OUTPUT:
            B = self.dss_b.ActiveCircuit.Vsources
        
        if not LOAD_OUTPUT: 
            A = self.dss_a.ActiveCircuit.Vsources
            nA = A.First
            if not SAVE_OUTPUT: 
                nB = B.First
                assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
                assert A.Count == B.Count
                assert len(A) == len(B)
                assert nA == nB
        else:
            nA = nB = (B if B is not None else A).First
        
        count = 0
        while nA != 0:
            count += 1
            for field in 'AngleDeg,BasekV,Frequency,Name,Phases,pu'.split(','):
                fA = self.output['ActiveCircuit.Vsources[{}].{}'.format(nA, field)] if LOAD_OUTPUT else getattr(A, field)
                if SAVE_OUTPUT: self.output['ActiveCircuit.Vsources[{}].{}'.format(nA, field)] = fA
                if not SAVE_OUTPUT: 
                    fB = getattr(B, field)
                    assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            if not SAVE_OUTPUT: 
                nB = B.Next
            if not LOAD_OUTPUT: 
                nA = A.Next
                if not SAVE_OUTPUT: 
                    assert nA == nB
            else:
                nA = nB

        if not LOAD_OUTPUT and count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))


    def validate_Reclosers(self):
        A, B = None, None
        if not SAVE_OUTPUT:
            B = self.dss_b.ActiveCircuit.Reclosers

        if not LOAD_OUTPUT: 
            A = self.dss_a.ActiveCircuit.Reclosers
            nA = A.First
            if not SAVE_OUTPUT: 
                nB = B.First
                assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
                assert A.Count == B.Count
                assert len(A) == len(B)
                assert nA == nB
        else:
            nA = nB = (B if B is not None else A).First
        
        count = 0
        while nA != 0:
            count += 1
            for field in 'RecloseIntervals'.split(','):
                fA = self.output['ActiveCircuit.Reclosers[{}].{}'.format(nA, field)] if LOAD_OUTPUT else getattr(A, field)
                if SAVE_OUTPUT: self.output['ActiveCircuit.Reclosers[{}].{}'.format(nA, field)] = fA
                if not SAVE_OUTPUT: 
                    fB = getattr(B, field)
                    fA = np.array(fA, dtype=fB.dtype)
                    assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), field

            for field in 'GroundInst,GroundTrip,MonitoredObj,MonitoredTerm,Name,NumFast,PhaseInst,PhaseTrip,Shots,SwitchedObj,SwitchedTerm,idx'.split(','):
                fA = self.output['ActiveCircuit.Reclosers[{}].{}'.format(nA, field)] if LOAD_OUTPUT else getattr(A, field)
                if SAVE_OUTPUT: self.output['ActiveCircuit.Reclosers[{}].{}'.format(nA, field)] = fA
                if not SAVE_OUTPUT: 
                    fB = getattr(B, field)
                    assert (fA == fB) or (type(fA) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            if not SAVE_OUTPUT: 
                nB = B.Next
            if not LOAD_OUTPUT: 
                nA = A.Next
                if not SAVE_OUTPUT: 
                    assert nA == nB
            else:
                nA = nB

        if not LOAD_OUTPUT and count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))


    def validate_XYCurves(self):
        A, B = None, None
        if not SAVE_OUTPUT:
            B = self.dss_b.ActiveCircuit.XYCurves

        if not LOAD_OUTPUT: 
            A = self.dss_a.ActiveCircuit.XYCurves
            nA = A.First
#            if not SAVE_OUTPUT: assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
            if not SAVE_OUTPUT: 
                nB = B.First
                assert A.Count == B.Count
                assert len(A) == len(B)
                assert nA == nB
        else:
            nA = nB = (B if B is not None else A).First
        
        count = 0
        while nA != 0:
            count += 1
            for field in 'Xarray,Yarray'.split(','):
                fA = self.output['ActiveCircuit.XYCurves[{}].{}'.format(nA, field)] if LOAD_OUTPUT else getattr(A, field)
                if SAVE_OUTPUT: self.output['ActiveCircuit.XYCurves[{}].{}'.format(nA, field)] = fA
                if not SAVE_OUTPUT: 
                    fB = getattr(B, field)
                    assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), field

            for field in 'Name,Npts,Xscale,Xshift,Yscale,Yshift,x,y'.split(','):
                fA = self.output['ActiveCircuit.XYCurves[{}].{}'.format(nA, field)] if LOAD_OUTPUT else getattr(A, field)
                if SAVE_OUTPUT: self.output['ActiveCircuit.XYCurves[{}].{}'.format(nA, field)] = fA
                if not SAVE_OUTPUT: 
                    fB = getattr(B, field)
                    assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            if not SAVE_OUTPUT: 
                nB = B.Next
            if not LOAD_OUTPUT: 
                nA = A.Next
                if not SAVE_OUTPUT: 
                    assert nA == nB
            else:
                nA = nB

        if not LOAD_OUTPUT and count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))


    def validate_Monitors(self):
        A, B = None, None
        if not SAVE_OUTPUT:
            B = self.dss_b.ActiveCircuit.Monitors
        
        if not LOAD_OUTPUT: 
            A = self.dss_a.ActiveCircuit.Monitors
            nA = A.First
            if not SAVE_OUTPUT: 
                nB = B.First
                assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
                assert A.Count == B.Count
                assert len(A) == len(B)
                assert nA == nB
        else:
            nA = nB = (B if B is not None else A).First
        
        count = 0
        while nA != 0:
            count += 1
            header = (B if B is not None else A).Header
            monitor_name = (B if B is not None else A).Name
            
            for field in 'dblFreq,dblHour'.split(','): # Skipped ByteStream since it's indirectly compared through Channel()
                fA = self.output['ActiveCircuit.Monitors[{}].{}'.format(count, field)] if LOAD_OUTPUT else getattr(A, field)
                if SAVE_OUTPUT: self.output['ActiveCircuit.Monitors[{}].{}'.format(count, field)] = fA
                if not SAVE_OUTPUT: 
                    fB = getattr(B, field)
                    fA = np.array(fA, dtype=fB.dtype)
                    assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), field

            #TODO: FileVersion (broken in COM)
#            for field in 'Element,Header,FileName,Mode,Name,NumChannels,RecordSize,SampleCount,Terminal'.split(','):
           
            for field in 'Element,FileName,Mode,Name,NumChannels,RecordSize,SampleCount,Terminal'.split(','):
                if field == 'FileName': continue # the path will be different on purpose
                fA = self.output['ActiveCircuit.Monitors[{}].{}'.format(count, field)] if LOAD_OUTPUT else getattr(A, field)
                if not SAVE_OUTPUT: 
                    fB = getattr(B, field)
                    if field == 'Header':
                        fAmod = [x.strip() for x in fA]
                        assert fAmod == fB, (field, fA, fB)
                    else:
                        assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)
                else:
                    self.output['ActiveCircuit.Monitors[{}].{}'.format(count, field)] = fA

            for channel in range((B if B is not None else A).NumChannels):
                if header[channel].strip() in ('SolveSnap_uSecs', 'TimeStep_uSecs'): continue # these can't be equal
                field = 'Channel({})'.format(channel + 1)
                output_key = 'ActiveCircuit.Monitors[{}].{}'.format(monitor_name, field)
                fA = self.output[output_key] if LOAD_OUTPUT else A.Channel(channel + 1)
                if SAVE_OUTPUT: self.output[output_key] = fA
                if not SAVE_OUTPUT: 
                    fB = B.Channel(channel + 1)
                    # assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), ('Channel', channel + 1)
                    header_lower = header[channel].lower()
                    if any(x in header_lower for x in ['ang']): # 'q1', 'q2', 'q3'
                        # Angles for very small values have no meaning
                        # We just skip any angle comparison for the time being
                        # TODO: add a complete validation using the two channels from the monitor
                        #       like what is done with WdgCurrents
                        continue 
                    
                    if not np.allclose(fA, fB, atol=self.atol, rtol=self.rtol):
                        # 'q1', 'q2', 'q3' may be different. This is expected since
                        # we use a different/better transformation matrix
                        print('Possible channel error', output_key, header[channel], np.array(fA), np.array(fB))

            if not SAVE_OUTPUT: 
                nB = B.Next
            if not LOAD_OUTPUT: 
                nA = A.Next
                if not SAVE_OUTPUT: 
                    assert nA == nB
            else:
                nA = nB

        if not LOAD_OUTPUT and count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))


    def validate_Meters(self):
        A, B = None, None
        if not SAVE_OUTPUT:
            B = self.dss_b.ActiveCircuit.Meters
        
        if not LOAD_OUTPUT: 
            A = self.dss_a.ActiveCircuit.Meters
            nA = A.First
            if not SAVE_OUTPUT: 
                nB = B.First
                assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
                assert A.Count == B.Count
                assert len(A) == len(B)
                assert nA == nB
        else:
            nA = nB = (B if B is not None else A).First
        
        count = 0
        while nA != 0:
            count += 1
            for field in 'AllBranchesInZone,AllEndElements,RegisterNames,ZonePCE'.split(','):
                if field == 'ZonePCE' and NO_V9:
                    continue
                    
                fA = self.output['ActiveCircuit.Meters[{}].{}'.format(nA, field)] if LOAD_OUTPUT else getattr(A, field)
                if SAVE_OUTPUT: self.output['ActiveCircuit.Meters[{}].{}'.format(nA, field)] = fA
                if not SAVE_OUTPUT: 
                    fB = getattr(B, field)
                    if fA == ('',) and fB == [None]: continue # Comtypes and win32com results are a bit different here
                    fA = [x for x in fA if x]
                    fB = [x for x in fB if x]
                    assert len(fA) == len(fB), (fA, fB)
                    assert all(x[0] == x[1] for x in zip(fA, fB)), (field, fA, fB)


            # NOTE: CalcCurrent and AllocFactors removed since it seemed to contain (maybe?) uninitialized values in certain situations
            fields = 'AvgRepairTime,Peakcurrent,RegisterValues,Totals' if self.realibity_ran else 'Peakcurrent,RegisterValues'
            for field in fields.split(','):
                fA = self.output['ActiveCircuit.Meters[{}].{}'.format(nA, field)] if LOAD_OUTPUT else getattr(A, field)
                if SAVE_OUTPUT: self.output['ActiveCircuit.Meters[{}].{}'.format(nA, field)] = fA
                if not SAVE_OUTPUT: 
                    fB = getattr(B, field)
                    assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), ('Meters("{}").{}'.format(A.Name, field), fA, fB)

            fields = 'CountBranches,CountEndElements,CustInterrupts,DIFilesAreOpen,FaultRateXRepairHrs,MeteredElement,MeteredTerminal,Name,NumSectionBranches,NumSectionCustomers,NumSections,OCPDeviceType,SAIDI,SAIFI,SAIFIKW,SectSeqIdx,SectTotalCust,SeqListSize,SequenceIndex,SumBranchFltRates,TotalCustomers' if self.realibity_ran else 'MeteredElement,MeteredTerminal,Name'
            for field in fields.split(','):
                fA = self.output['ActiveCircuit.Meters[{}].{}'.format(nA, field)] if LOAD_OUTPUT else getattr(A, field)
                if SAVE_OUTPUT: self.output['ActiveCircuit.Meters[{}].{}'.format(nA, field)] = fA
                if not SAVE_OUTPUT: 
                    fB = getattr(B, field)
                    assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            if not SAVE_OUTPUT: 
                nB = B.Next
            if not LOAD_OUTPUT: 
                nA = A.Next
                if not SAVE_OUTPUT: 
                    assert nA == nB
            else:
                nA = nB

        if not LOAD_OUTPUT and count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))

        
    def validate_Settings(self):
        A, B = None, None
        if not SAVE_OUTPUT:
            B = self.dss_b.ActiveCircuit.Settings
        
        if not LOAD_OUTPUT: 
            A = self.dss_a.ActiveCircuit.Settings

        for field in 'LossRegs,UEregs,VoltageBases'.split(','):
            fA = self.output['ActiveCircuit.Settings.{}'.format(field)] if LOAD_OUTPUT else getattr(A, field)
            if SAVE_OUTPUT: self.output['ActiveCircuit.Settings.{}'.format(field)] = fA
            if not SAVE_OUTPUT: 
                fB = getattr(B, field)
                assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), field
        
        
        # AutoBusList is broken in COM, doesn't clear the GlobalResult first.
        # for field in 'AutoBusList'.split(','):
        #     fA = self.output['ActiveCircuit.Settings.{}'.format(field)] if LOAD_OUTPUT else getattr(A, field)
        #     fB = getattr(B, field)
        #     if SAVE_OUTPUT: self.output['ActiveCircuit.Settings.{}'.format(field)] = fA
        #     if not SAVE_OUTPUT: assert fA == fB, (field, (fA, fB))
        
        for field in 'AllowDuplicates,CktModel,ControlTrace,EmergVmaxpu,EmergVminpu,LossWeight,NormVmaxpu,NormVminpu,PriceCurve,PriceSignal,Trapezoidal,UEweight,ZoneLock'.split(','):
            fA = self.output['ActiveCircuit.Settings.{}'.format(field)] if LOAD_OUTPUT else getattr(A, field)
            if SAVE_OUTPUT: self.output['ActiveCircuit.Settings.{}'.format(field)] = fA
            if not SAVE_OUTPUT: 
                fB = getattr(B, field)
                assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

    def validate_Solution(self):
        A, B = None, None
        if not SAVE_OUTPUT:
            B = self.dss_b.ActiveCircuit.Solution
        
        if not LOAD_OUTPUT: 
            A = self.dss_a.ActiveCircuit.Solution

        for field in 'AddType,Algorithm,Capkvar,ControlActionsDone,ControlIterations,ControlMode,Converged,DefaultDaily,DefaultYearly,Frequency,GenMult,GenPF,GenkW,Hour,Iterations,LDCurve,LoadModel,LoadMult,MaxControlIterations,MaxIterations,Mode,ModeID,MostIterationsDone,Number,Random,Seconds,StepSize,Tolerance,Totaliterations,Year,dblHour,pctGrowth'.split(','): #TODO: EventLog, IntervalHrs, MinIterations, Process_Time, Total_Time, Time_of_Step, SystemYChanged
            # if LOAD_OUTPUT and field == 'SystemYChanged':
                # continue
        
            fA = self.output['ActiveCircuit.Solution.{}'.format(field)] if LOAD_OUTPUT else getattr(A, field)
            if SAVE_OUTPUT: self.output['ActiveCircuit.Solution.{}'.format(field)] = fA
            if not SAVE_OUTPUT: 
                fB = getattr(B, field)
                assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            # if field == 'SystemYChanged':
                # print('SystemYChanged', fA, fB)
            

    def _get_circuit_fields(self, imin=0, imax=2):
        return {
            "AllBusDistances" : self.AllBusDistances[imin:imax],
            "AllBusNames" : self.AllBusNames[imin:imax],
            "AllBusVmag" : self.AllBusVmag[imin:imax],
            "AllBusVmagPu" : self.AllBusVmagPu[imin:imax],
            "AllBusVolts" : self.AllBusVolts[imin:imax],
            "AllElementLosses" : self.AllElementLosses[imin:imax],
            "AllElementNames" : self.AllElementNames[imin:imax],
            "AllNodeDistances" : self.AllNodeDistances[imin:imax],
            "AllNodeNames" : self.AllNodeNames[imin:imax],
            "LineLosses" : self.LineLosses[imin:imax],
            "Losses" : self.Losses[imin:imax],
            "Name" : self.Name[imin:imax],
            "NumBuses" : self.NumBuses[imin:imax],
            "NumCktElements" : self.NumCktElements[imin:imax],
            "NumNodes" : self.NumNodes[imin:imax],
            "ParentPDElement" : self.ParentPDElement[imin:imax],
            "SubstationLosses" : self.SubstationLosses[imin:imax],
#            "SystemY" : self.SystemY[imin:imax],
            "TotalPower" : self.TotalPower[imin:imax],
            "YCurrents" : self.YCurrents[imin:imax],
            "YNodeOrder" : self.YNodeOrder[imin:imax],
            "YNodeVarray" : self.YNodeVarray[imin:imax],
        }
    
    def _set_circuit_fields(self, data):
        self.AllBusDistances = data["AllBusDistances"]
        self.AllBusNames = data["AllBusNames"]
        self.AllBusVmag = data["AllBusVmag"]
        self.AllBusVmagPu = data["AllBusVmagPu"]
        self.AllBusVolts = data["AllBusVolts"]
        self.AllElementLosses = data["AllElementLosses"]
        self.AllElementNames = data["AllElementNames"]
        self.AllNodeDistances = data["AllNodeDistances"]
        self.AllNodeNames = data["AllNodeNames"]
        self.LineLosses = data["LineLosses"]
        self.Losses = data["Losses"]
        self.Name = data["Name"]
        self.NumBuses = data["NumBuses"]
        self.NumCktElements = data["NumCktElements"]
        self.NumNodes = data["NumNodes"]
        self.ParentPDElement = data["ParentPDElement"]
        self.SubstationLosses = data["SubstationLosses"]
#        self.SystemY = data["SystemY"]
        self.TotalPower = data["TotalPower"]
        self.YCurrents = data["YCurrents"]
        self.YNodeOrder = data["YNodeOrder"]
        self.YNodeVarray = data["YNodeVarray"]
            
            
    def validate_Circuit(self):
        all_fields = self._get_circuit_fields()
        
        # Test Circuit_SetCktElementName with line names
        if not LOAD_OUTPUT:
            # Get all line names
            lines_names = []
            LA = self.dss_a.ActiveCircuit.Lines
            nA = LA.First
            while nA != 0:
                lines_names.append(LA.Name)
                nA = LA.Next
        
            for name in lines_names:
                A = self.dss_a.ActiveCircuit.CktElements('Line.' + name)
                if not SAVE_OUTPUT: 
                    B = self.dss_b.ActiveCircuit.CktElements('Line.' + name)
                    assert A.Name == B.Name
            
            # Test Circuit_SetCktElementIndex
            num_cktelements = len(self.dss_a.ActiveCircuit.AllElementNames)
            for idx in range(num_cktelements):
                A = self.dss_a.ActiveCircuit.CktElements(idx)
                if not SAVE_OUTPUT:
                    B = self.dss_b.ActiveCircuit.CktElements(idx)
                    assert A.Name == B.Name

            # Try to use an invalid index
            try:
                if not SAVE_OUTPUT:
                    B = self.dss_b.ActiveCircuit.CktElements(999999)
            except DSSException:
                pass
                
            if not SAVE_OUTPUT: 
                A = self.dss_a.ActiveCircuit.CktElements(999999)
                assert A.Name == B.Name

            # Try to use an invalid name
            try:
                if not SAVE_OUTPUT: 
                    B = self.dss_b.ActiveCircuit.CktElements('NONEXISTENT_123456789')
            except DSSException:
                pass

            if not SAVE_OUTPUT:
                A = self.dss_a.ActiveCircuit.CktElements('NONEXISTENT_123456789')
                assert A.Name == B.Name

        if SAVE_OUTPUT:
            return

        element_names = all_fields['AllElementNames'][0]
        for k, v in all_fields.items():
            if k == 'AllElementLosses':
                # Special case for AllElementLosses
                s_a = np.asarray(v[0]).view(dtype=complex)
                s_b = np.asarray(v[1]).view(dtype=complex)
                s_d = abs(s_a - s_b)
                idx = np.argmax(s_d)
                print(k, np.max(s_d), element_names[idx], s_a[idx], s_b[idx])
            elif k == 'LineLosses':
                # Special case for LineLosses
                s_a = complex(*v[0])
                s_b = complex(*v[1])
                p_d = (abs(s_a - s_b))
                print(k, p_d, '' if p_d < self.atol else '!!!')
            elif type(v[1]) == np.ndarray:
                print(k, max(abs(v[1] - v[0])))
                if k == 'TotalPower':
                    cv = [np.asarray(v[0]).view(dtype=complex), np.asarray(v[1]).view(dtype=complex)]
                    assert np.allclose(cv[0], cv[1], atol=self.atol, rtol=self.rtol), (k, cv[0], cv[1])
                    # else:
                        # assert np.allclose(v[0]/v[1], 1, atol=self.atol, rtol=100), (k, type(v[1]), v[0], v[1])
                else:
                    vA, vB = (np.asarray(vx) for vx in v)
                    if k in ('AllBusVolts', 'YNodeVarray'):
                        vA = vA.view(dtype=complex)
                        vB = vB.view(dtype=complex)
                        #vA[np.abs(vA) < 1e-7] = 0
                        #vB[np.abs(vB) < 1e-7] = 0

                    assert np.allclose(vA, vB, atol=self.atol, rtol=self.rtol), (k, type(v[1]))#, v[0], v[1])
            elif type(v[1]) == list:
                assert all(x[0] == x[1] for x in zip(*v)), (k, type(v[1]))
            elif type(v[1]) == int:
                assert v[0] == v[1], (k, type(v[1]))
            elif type(v[1]) == float:
                if not SAVE_COM_OUTPUT: assert abs(v[0] - v[1]) < self.atol, (k, type(v[1]))

    def validate_YMatrix(self):
        if SAVE_OUTPUT:
            return

        NN = self.dss_b.ActiveCircuit.NumNodes
        if NN > 2000: # test only on small strings
            return

        ysparse = csc_matrix(self.dss_b.YMatrix.GetCompressedYMatrix(factor=False))
        ydense = self.dss_b.ActiveCircuit.SystemY.view(dtype=complex).reshape((NN, NN))
        if not SAVE_OUTPUT: 
            assert (np.allclose(ydense, ysparse.todense(), atol=self.atol, rtol=self.rtol))
        
        
    def validate_AllNames(self):
        clss = [
            'Generators',
            'Meters',
            'Monitors',
            'Lines',
            'Loads',
            'CapControls',
            'RegControls',
            'SwtControls',
            'Transformers',
            'Capacitors',
            'Sensors',
            'Reclosers',
            'Relays',
            'LoadShapes',
            'Fuses',
            'ISources',
            'PVSystems',
            'Vsources',
            'LineCodes',
            'LineGeometries',
            'LineSpacings',
            'WireData',
            'CNData',
            'TSData',
            'XYCurves',
            'Reactors',
        ]

        def check_cls_allnames(name, DSS):
            l = getattr(DSS.ActiveCircuit, name)
            if not l.Count:
                return
            l.First
            l.Next
            before = l.Name
            l.AllNames
            after = l.Name
            #assert before == after, (name, before, after)
            return before == after

        if not SAVE_OUTPUT and not LOAD_OUTPUT:
            for cls in clss:
                try:
                    assert (check_cls_allnames(cls, self.dss_a) == check_cls_allnames(cls, self.dss_b)), cls
                except AttributeError:
                    # COM doesn't expose 
                    pass
    
                
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
        
        self.validate_AllNames()

        #self.atol = 1e-5
        #print('Buses')
        self.validate_Buses()
        #print('Circuit')
        self.validate_Circuit()

        # self.dss_b.ShowPanel()
        
        print('Done')



local_info = local()

# def init_thread(dss_workers):
#     local_info.capi = dss_workers.pop()
#     print(current_thread().name, local_info.capi, local_info.capi._api_util.ctx)

def init_thread(capi):
    local_info.capi = capi.NewContext()
    print(current_thread().name, local_info.capi, local_info.capi._api_util.ctx)

def run_fn(fn, dss_variants=None, capi=None):
    if LOAD_OUTPUT and USE_THREADS:
        capi = local_info.capi
        dss_variants = [capi]

    line_by_line = fn.startswith('L!')
    if line_by_line:
        fn = fn[2:]
    print("> File", fn)
    assert os.path.exists(os.path.join(original_working_dir, fn)), os.path.join(original_working_dir, fn)
    
    test = ValidatingTest(fn, dss_variants, line_by_line)

    if not LOAD_OUTPUT:
        if SAVE_OUTPUT and not SAVE_DSSX_OUTPUT:
            print("Running using OpenDSS COM")
        else:
            print("Running using DSS Extensions")

        if SAVE_OUTPUT:
            output = test.output = {}
        else:
            output = test.output = FakeDict()

        test.run(dss_variants[0], solve=True)
        output['ActiveCircuit'] = test._get_circuit_fields(0, 1)
    else:
        os.chdir(original_working_dir)
        pickle_fn = fn + f'.{LOAD_PLATFORM}.pickle.zstd'
        with zstd.open(pickle_fn, 'rb') as pickled_output_file:
            output = test.output = pickle.load(pickled_output_file)
            print('Output loaded from', pickle_fn)
            test._set_circuit_fields(output['ActiveCircuit'])
    
    if not SAVE_OUTPUT:
        print("Running using DSS Extensions")
        test.run(capi, solve=True)
    
    
    print("Validating")
    try:
        test.validate_all()
    except (AssertionError, TypeError) as ex:
        global num_failures
        num_failures += 1
        print('!!!!!!!!!!!!!!!!!!!!!!')
        print('ERROR:', fn, ex)
        print('!!!!!!!!!!!!!!!!!!!!!!')
        if colorizer is None:
            traceback.print_exc()
        else:
            colorizer.colorize_traceback(*sys.exc_info())
        print('-'*40)
        print()
        #raise
        return

        
    if SAVE_OUTPUT:
        os.chdir(original_working_dir)
        if SAVE_DSSX_OUTPUT:
            pickle_fn = fn + f'.{sys.platform}-{platform.machine()}-dssx.pickle.zstd'
        else:
            pickle_fn = fn + '.win32com.pickle.zstd'

        with zstd.open(pickle_fn, 'wb') as pickled_output_file:
            pickle.dump(output, pickled_output_file, protocol=4) # use protocol 4 to allow testing under Python 3.7
            print('Output pickled to', pickle_fn)
        
        output = type(output)()


def run_tests(fns):
    from dss import DSS, use_com_compat
    DSS.AllowChangeDir = False
    use_com_compat()

    # NOTE: if win32com errors out, rerun until all files are generated
    com = None
    if not LOAD_OUTPUT:
        if not SAVE_DSSX_OUTPUT:
            import win32com.client
            com = win32com.client.Dispatch("OpenDSSEngine.DSS")
            com = win32com.client.gencache.EnsureDispatch("OpenDSSEngine.DSS")
            
            import dss
            com = dss.patch_dss_com(com)
            print('COM Version:', com.Version)
        #global COM_VLL_BROKEN
        #COM_VLL_BROKEN = ('Version 8.6.7.1 ' in com.Version) or ('Version 9.0.0.8 ' in com.Version)
        

    #import comtypes.client
    #com = comtypes.client.CreateObject("OpenDSSEngine.DSS")

    capi = DSS
    print('C-API Version:', capi.Version)

    if com is None:
        assert LOAD_OUTPUT or SAVE_OUTPUT
        dss_variants = [capi]
    else:
        dss_variants = [com, capi]
    for dss in dss_variants:
        if dss is not None:
            dss.Text.Command = r'set editor=ignore_me_invalid_executable'
        
    capi.AllowEditor = False
    capi.Error.ExtendedErrors = False
    assert capi.Error.EarlyAbort # check the default value, should be True

    # Test toggling console output with C-API, COM can only be disabled
    if not LOAD_OUTPUT:
        for dss in dss_variants:
            dss.AllowForms = True
            if not SAVE_OUTPUT: assert dss.AllowForms == True

            dss.AllowForms = False
            if not SAVE_OUTPUT: assert dss.AllowForms == False
            
            dss.AllowForms = True
            if dss != com:
                if not SAVE_OUTPUT: assert dss.AllowForms == True

            dss.AllowForms = False
            if not SAVE_OUTPUT: assert dss.AllowForms == False
    else:
        for dss in [capi]:
            dss.AllowForms = True
            if not SAVE_OUTPUT: assert dss.AllowForms == True

            dss.AllowForms = False
            if not SAVE_OUTPUT: assert dss.AllowForms == False
            
            dss.AllowForms = True
            if not SAVE_OUTPUT: assert dss.AllowForms == True

            dss.AllowForms = False
            if not SAVE_OUTPUT: assert dss.AllowForms == False
    

    import time
    if USE_THREADS and LOAD_OUTPUT:
        num_workers = 10
            
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers, initializer=init_thread, initargs=(capi,)) as executor:
            futures = [executor.submit(run_fn, fn) for fn in fns]
            for future in concurrent.futures.as_completed(futures):
                fn = fns[futures.index(future)]
                print(fn, future.result())
    else:
        for fn in fns:
            run_fn(fn, dss_variants)
    
    if not LOAD_OUTPUT:
        for dss in dss_variants:
            dss.Text.Command = 'Clear'
            
if __name__ == '__main__':
    from common import test_filenames, errored
    try:
        import colored_traceback
        colored_traceback.add_hook()
        colorizer = colored_traceback.Colorizer('default', False)
    except:
        colorizer = None

    
    t0_global = time()
    if SAVE_OUTPUT:
        # Always save all results, even the broken ones
        run_tests(test_filenames)
    else:
        run_tests([x for x in test_filenames if x not in errored])
        #run_tests(sorted(errored))
        
    print(time() - t0_global, 'seconds')
    print("Failures:", num_failures)
