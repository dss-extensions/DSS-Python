from __future__ import print_function
import os, sys
from time import time
import numpy as np
from scipy.sparse import csc_matrix
from dss import enums
import pickle
from dss import DSSException

original_working_dir = os.getcwd()
NO_PROPERTIES = os.getenv('DSS_PYTHON_VALIDATE') == 'NOPROP'
USE_V8 = (os.getenv('DSS_PYTHON_V8') == '1')
WIN32 = (sys.platform == 'win32')

COM_VLL_BROKEN = False

# COM Output
SAVE_COM_OUTPUT = 'save' in sys.argv
LOAD_COM_OUTPUT = (not WIN32) or ('load' in sys.argv)

if SAVE_COM_OUTPUT:
    LOAD_COM_OUTPUT = False
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
        self.SystemY.append(dss.ActiveCircuit.SystemY)
        self.TotalPower.append(dss.ActiveCircuit.TotalPower)
        self.YCurrents.append(dss.ActiveCircuit.YCurrents)
        self.YNodeOrder.append(dss.ActiveCircuit.YNodeOrder)
        self.YNodeVarray.append(dss.ActiveCircuit.YNodeVarray)


    def validate_CktElement(self):
        if LOAD_COM_OUTPUT: 
            #TODO: not implemented
            return
        
        A = self.com.ActiveCircuit.ActiveElement
        B = self.capi.ActiveCircuit.ActiveElement

        for field in ['AllPropertyNames']:
            fA = set(x.lower() for x in getattr(A, field))
            fB = set(x.lower() for x in getattr(B, field))
            for propA in fA:
                assert propA in fB, propA
                
            # Since the list of properties vary in releases, 
            # we don't check it the list is the same anymore.
            # if not SAVE_COM_OUTPUT: assert all(x[0] == x[1] for x in zip(fA, fB)), (field, fA, fB)
            
        for field in 'AllVariableNames,BusNames'.split(','):
            fA = getattr(A, field)
            fB = getattr(B, field)
            if fA == ('',) and fB == [None]: continue # comtypes and win32com results are a bit different here
            if not SAVE_COM_OUTPUT: assert all(x[0] == x[1] for x in zip(fA, fB)), (field, fA, fB)
            
          
        # Check if setting bus names works
        BusNames = list(A.BusNames)
        A.BusNames = BusNames
        B.BusNames = BusNames

        # Check if they match again
        field = 'BusNames'
        fA = getattr(A, field)
        fB = getattr(B, field)
        if not (fA == ('',) and fB == [None]): # comtypes and win32com results are a bit different here
            if not SAVE_COM_OUTPUT: assert all(x[0] == x[1] for x in zip(fA, fB)), field
          
          
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

                if not (is_equal or val_A == val_B or A.Properties(prop_name).Val == B.Properties(prop_name).Val):
                    print('ERROR: CktElement({}).Properties({}).Val'.format(A.Name, prop_name), repr(A.Properties(prop_name).Val), repr(B.Properties(prop_name).Val))
            
#            if not USE_V8:
#                if not SAVE_COM_OUTPUT: assert (A.Properties(prop_name).Description == B.Properties(prop_name).Description), ('Properties({}).Description'.format(prop_name), A.Properties(prop_name).Description, B.Properties(prop_name).Description)
                
            if not SAVE_COM_OUTPUT: assert (A.Properties(prop_name).Name.lower() == B.Properties(prop_name).Name.lower()), ('Properties({}).name'.format(prop_name), A.Properties(prop_name).Name, B.Properties(prop_name).Name)

            if not SAVE_COM_OUTPUT: assert (B.Properties(prop_name).Val == B.Properties[prop_name].Val)
            if not SAVE_COM_OUTPUT: assert (B.Properties(prop_name).Description == B.Properties[prop_name].Description)
            if not SAVE_COM_OUTPUT: assert (B.Properties(prop_name).Name == B.Properties[prop_name].Name)


    def validate_Buses(self):
        if not LOAD_COM_OUTPUT:
            for idx in range(len(self.AllBusNames)):
                A = self.com.ActiveCircuit.Buses(idx)
                B = self.capi.ActiveCircuit.Buses(idx)
                if not SAVE_COM_OUTPUT: assert A.Name == B.Name
                
            for name in self.AllBusNames[-1]:
                A = self.com.ActiveCircuit.Buses(name)
                B = self.capi.ActiveCircuit.Buses(name)
                if not SAVE_COM_OUTPUT: assert A.Name == B.Name
            
            A = self.com.ActiveCircuit.ActiveBus
        
        B = self.capi.ActiveCircuit.ActiveBus
        for name in self.AllBusNames[-1]:
            self.capi.ActiveCircuit.SetActiveBus(name)
            if not LOAD_COM_OUTPUT:
                self.com.ActiveCircuit.SetActiveBus(name)
                if not SAVE_COM_OUTPUT: assert A.Name == B.Name
                
            for field in ('Coorddefined', 'Cust_Duration', 'Cust_Interrupts', 'Distance', 'Int_Duration', 'Isc', 'Lambda', 'N_Customers', 'N_interrupts', 'Nodes', 'NumNodes', 'SectionID', 'TotalMiles', 'VLL', 'VMagAngle', 'Voc', 'Voltages', 'YscMatrix', 'Zsc0', 'Zsc1', 'ZscMatrix', 'kVBase', 'puVLL', 'puVmagAngle', 'puVoltages', 'x', 'y',  'SeqVoltages', 'CplxSeqVoltages'):
                fB = getattr(B, field)
                if COM_VLL_BROKEN and field in ('VLL', 'puVLL') and len(fB) == 1:
                    print('Bus.{}: this COM version could freeze, skipping; bus = {}, nodes = {}'.format(field, name, A.Nodes))
                    fA = fB
                else:
                    fA = output['ActiveCircuit.ActiveBus[{}].{}'.format(name, field)] if LOAD_COM_OUTPUT else getattr(A, field)
                    
                if SAVE_COM_OUTPUT: output['ActiveCircuit.ActiveBus[{}].{}'.format(name, field)] = fA
                
                if type(fA) == tuple and len(fA) == 0:
                    if not SAVE_COM_OUTPUT: assert fB is None or len(fB) == 0, ('ActiveBus.{}'.format(field), fA, fB)
                    continue

                if field in ('SeqVoltages', 'CplxSeqVoltages', 'VLL'): continue # skip

                if field == 'CplxSeqVoltages':
                    vA = np.array(A.Voltages).view(dtype=complex)
                    vB = B.Voltages.view(dtype=complex)

                    if len(vA) < 3: continue

                    if not SAVE_COM_OUTPUT: assert np.allclose(vA, vB, atol=self.atol, rtol=self.rtol), (vA, vB)

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
                        if not SAVE_COM_OUTPUT: assert np.isclose(pasA, pasB, atol=self.atol, rtol=self.rtol), ('ActiveBus.' + field, name, pasA, pasB)

                    continue

                if field in ('VMagAngle', 'puVmagAngle'):
                    fA = np.asarray(fA)
                    fB = np.asarray(fB)
                    
                    aa = np.deg2rad(fA[1::2])
                    fA = fA[::2] * (np.cos(aa) + 1j * np.sin(aa))
                    ab = np.deg2rad(fB[1::2])
                    fB = fB[::2] * (np.cos(ab) + 1j * np.sin(ab))
                

                if not SAVE_COM_OUTPUT: assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), ('ActiveBus.' + field, name, fA, fB)


    def validate_Capacitors(self):
        B = self.capi.ActiveCircuit.Capacitors
        
        if not LOAD_COM_OUTPUT: 
            A = self.com.ActiveCircuit.Capacitors
            if not SAVE_COM_OUTPUT: assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
            if not SAVE_COM_OUTPUT: assert A.Count == B.Count
            if not SAVE_COM_OUTPUT: assert len(A) == len(B)
            nA = A.First
            nB = B.First
            if not SAVE_COM_OUTPUT: assert nA == nB
        else:
            nA = nB = B.First

        count = 0
        while nA != 0:
            count += 1
            for field in ('States',):
                fA = output['ActiveCircuit.Capacitors[{}].{}'.format(nA, field)] if LOAD_COM_OUTPUT else getattr(A, field)
                fB = getattr(B, field)
                if SAVE_COM_OUTPUT: output['ActiveCircuit.Capacitors[{}].{}'.format(nA, field)] = fA
                if not SAVE_COM_OUTPUT: assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), field

            for field in ('AvailableSteps', 'NumSteps', 'kvar', 'kV', 'Name', 'IsDelta'):
                fA = output['ActiveCircuit.Capacitors[{}].{}'.format(nA, field)] if LOAD_COM_OUTPUT else getattr(A, field)
                fB = getattr(B, field)
                if SAVE_COM_OUTPUT: output['ActiveCircuit.Capacitors[{}].{}'.format(nA, field)] = fA
                if not SAVE_COM_OUTPUT: assert fA == fB, field

            self.validate_CktElement()

            nB = B.Next
            if not LOAD_COM_OUTPUT: 
                nA = A.Next
                if not SAVE_COM_OUTPUT: assert nA == nB
            else:
                nA = nB

        # if not LOAD_COM_OUTPUT and count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))


    def validate_LineCodes(self):
        B = self.capi.ActiveCircuit.LineCodes

        if not LOAD_COM_OUTPUT: 
            A = self.com.ActiveCircuit.LineCodes
            
            has_AllNames = True
            try:
                _ = A.AllNames
            except:
                has_AllNames = False
               
            if has_AllNames:
                if not SAVE_COM_OUTPUT: assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))

            if not SAVE_COM_OUTPUT: assert A.Count == B.Count, (A.Count, B.Count)
            if not SAVE_COM_OUTPUT: assert len(A) == len(B)
            nA = A.First
            nB = B.First
            if not SAVE_COM_OUTPUT: assert nA == nB
        else:
            nA = nB = B.First
            
            
        count = 0
        while nA != 0:
            count += 1
            for field in 'Cmatrix,Rmatrix,Xmatrix'.split(','):
                fA = output['ActiveCircuit.LineCodes[{}].{}'.format(nA, field)] if LOAD_COM_OUTPUT else getattr(A, field)
                fB = getattr(B, field)
                if SAVE_COM_OUTPUT: output['ActiveCircuit.LineCodes[{}].{}'.format(nA, field)] = fA
                if not SAVE_COM_OUTPUT: assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB, A.Name, B.Name)

            for field in 'C0,C1,EmergAmps,IsZ1Z0,Name,NormAmps,Phases,R0,R1,Units,X0,X1'.split(','):
                fA = output['ActiveCircuit.LineCodes[{}].{}'.format(nA, field)] if LOAD_COM_OUTPUT else getattr(A, field)
                fB = getattr(B, field)
                if SAVE_COM_OUTPUT: output['ActiveCircuit.LineCodes[{}].{}'.format(nA, field)] = fA
                if not SAVE_COM_OUTPUT: assert fA == fB or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            nB = B.Next
            if not LOAD_COM_OUTPUT: 
                nA = A.Next
                if not SAVE_COM_OUTPUT: assert nA == nB
            else:
                nA = nB

        if not LOAD_COM_OUTPUT and count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))

        
    def validate_Lines(self):
        B = self.capi.ActiveCircuit.Lines
        
        if not LOAD_COM_OUTPUT: 
            A = self.com.ActiveCircuit.Lines
            if not SAVE_COM_OUTPUT: assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
            if not SAVE_COM_OUTPUT: assert A.Count == B.Count
            if not SAVE_COM_OUTPUT: assert len(A) == len(B)
            nA = A.First
            nB = B.First
            if not SAVE_COM_OUTPUT: assert nA == nB
        else:
            nA = nB = B.First
            
        count = 0
        while nA != 0:
            count += 1
            # Notes: - removed property Parent from the analysis since it raises a popup
            #        - temporarily removed R1/X1/C1 since COM is broken    
            #for field in 'Bus1,Bus2,C0,C1,EmergAmps,Geometry,Length,LineCode,Name,NormAmps,NumCust,Phases,R0,R1,Rg,Rho,Spacing,TotalCust,Units,X0,X1,Xg'.split(','):
            for field in 'Bus1,Bus2,C0,EmergAmps,Geometry,Length,LineCode,Name,NormAmps,NumCust,Phases,R0,Rg,Rho,Spacing,TotalCust,Units,X0,Xg'.split(','):
                fA = output['ActiveCircuit.Lines[{}].{}'.format(nA, field)] if LOAD_COM_OUTPUT else getattr(A, field)
                fB = getattr(B, field)
                if SAVE_COM_OUTPUT: output['ActiveCircuit.Lines[{}].{}'.format(nA, field)] = fA
                if not SAVE_COM_OUTPUT: assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            for field in 'Cmatrix,Rmatrix,Xmatrix,Yprim'.split(','):
                fA = output['ActiveCircuit.Lines[{}].{}'.format(nA, field)] if LOAD_COM_OUTPUT else getattr(A, field)
                fB = getattr(B, field)
                if SAVE_COM_OUTPUT: output['ActiveCircuit.Lines[{}].{}'.format(nA, field)] = fA
                if not SAVE_COM_OUTPUT: assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB, max(abs(fA - fB)), A.Name, B.Name)

            self.validate_CktElement()

            nB = B.Next
            if not LOAD_COM_OUTPUT: 
                nA = A.Next
                if not SAVE_COM_OUTPUT: assert nA == nB
            else:
                nA = nB

        if not LOAD_COM_OUTPUT and count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))


    def validate_Loads(self):
        B = self.capi.ActiveCircuit.Loads
        
        if not LOAD_COM_OUTPUT: 
            A = self.com.ActiveCircuit.Loads
            if not SAVE_COM_OUTPUT: assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
            if not SAVE_COM_OUTPUT: assert A.Count == B.Count
            if not SAVE_COM_OUTPUT: assert len(A) == len(B)
            nA = A.First
            nB = B.First
            if not SAVE_COM_OUTPUT: assert nA == nB
        else:
            nA = nB = B.First
            
        count = 0
        while nA != 0:
            count += 1
            for field in 'AllocationFactor,CVRcurve,CVRvars,CVRwatts,Cfactor,Class,Growth,IsDelta,Model,Name,NumCust,PF,PctMean,PctStdDev,RelWeight,Rneut,Spectrum,Status,Vmaxpu,Vminemerg,Vminnorm,Vminpu,Xneut,Yearly,daily,duty,idx,kV,kW,kva,kvar,kwh,kwhdays,pctSeriesRL,xfkVA'.split(','): #TODO: ZIPV
                fA = output['ActiveCircuit.Loads[{}].{}'.format(nA, field)] if LOAD_COM_OUTPUT else getattr(A, field)
                fB = getattr(B, field)
                if SAVE_COM_OUTPUT: output['ActiveCircuit.Loads[{}].{}'.format(nA, field)] = fA
                if type(fB) == float:
                    if not SAVE_COM_OUTPUT: assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), field
                else:
                    if not SAVE_COM_OUTPUT: assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            self.validate_CktElement()

            nB = B.Next
            if not LOAD_COM_OUTPUT: 
                nA = A.Next
                if not SAVE_COM_OUTPUT: assert nA == nB
            else:
                nA = nB

        if not LOAD_COM_OUTPUT and count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))


    def validate_Loadshapes(self):
        B = self.capi.ActiveCircuit.LoadShapes
        
        if not LOAD_COM_OUTPUT: 
            A = self.com.ActiveCircuit.LoadShapes
            if not SAVE_COM_OUTPUT: assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
            if not SAVE_COM_OUTPUT: assert A.Count == B.Count
            if not SAVE_COM_OUTPUT: assert len(A) == len(B)
            nA = A.First
            nB = B.First
            if not SAVE_COM_OUTPUT: assert nA == nB
        else:
            nA = nB = B.First
            
        count = 0
        while nA != 0:
            count += 1
            for field in 'Pmult,Qmult,TimeArray'.split(','):
                fA = output['ActiveCircuit.LoadShapes[{}].{}'.format(nA, field)] if LOAD_COM_OUTPUT else getattr(A, field)
                fB = getattr(B, field)
                if SAVE_COM_OUTPUT: output['ActiveCircuit.LoadShapes[{}].{}'.format(nA, field)] = fA
                if not SAVE_COM_OUTPUT: assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), field

            for field in 'HrInterval,MinInterval,Name,Npts,Pbase,Qbase,UseActual,Sinterval'.split(','): #TODO: ZIPV
                fA = output['ActiveCircuit.LoadShapes[{}].{}'.format(nA, field)] if LOAD_COM_OUTPUT else getattr(A, field)
                fB = getattr(B, field)
                if SAVE_COM_OUTPUT: output['ActiveCircuit.LoadShapes[{}].{}'.format(nA, field)] = fA
                if not SAVE_COM_OUTPUT: assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            nB = B.Next
            if not LOAD_COM_OUTPUT: 
                nA = A.Next
                if not SAVE_COM_OUTPUT: assert nA == nB
            else:
                nA = nB

        if not LOAD_COM_OUTPUT and count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))


    def validate_Transformers(self):
        B = self.capi.ActiveCircuit.Transformers
        B_element = self.capi.ActiveCircuit.CktElements
        
        # Validate the LossesByType extension
        if B.Count:
            AllLossesByType = B.AllLossesByType.view(dtype=complex).reshape((B.Count, 3))
            for tr, losses in zip(B, AllLossesByType):
                assert np.all(losses == B.LossesByType.view(dtype=complex))
                assert np.allclose(losses[0], losses[1] + losses[2], atol=self.atol, rtol=self.rtol) 
                assert np.allclose(losses[0], losses[1] + losses[2], atol=self.atol, rtol=self.rtol) 
                assert B_element.Losses.view(dtype=complex) == losses[0]


        if not LOAD_COM_OUTPUT: 
            A = self.com.ActiveCircuit.Transformers
            if not SAVE_COM_OUTPUT: assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
            if not SAVE_COM_OUTPUT: assert A.Count == B.Count
            if not SAVE_COM_OUTPUT: assert len(A) == len(B)
            nA = A.First
            nB = B.First
            if not SAVE_COM_OUTPUT: assert nA == nB
        else:
            nA = nB = B.First
        
        count = 0
        while nA != 0:
            count += 1
            for field in 'IsDelta,MaxTap,MinTap,Name,NumTaps,NumWindings,R,Rneut,Tap,Wdg,XfmrCode,Xhl,Xht,Xlt,Xneut,kV,kva'.split(','):
                fA = output['ActiveCircuit.Transformers[{}].{}'.format(nA, field)] if LOAD_COM_OUTPUT else getattr(A, field)
                fB = getattr(B, field)
                if SAVE_COM_OUTPUT: output['ActiveCircuit.Transformers[{}].{}'.format(nA, field)] = fA
                if not SAVE_COM_OUTPUT: assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            self.validate_CktElement()

            nB = B.Next
            if not LOAD_COM_OUTPUT: 
                nA = A.Next
                if not SAVE_COM_OUTPUT: assert nA == nB
            else:
                nA = nB

        if not LOAD_COM_OUTPUT and count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))


    def validate_Generators(self):
        B = self.capi.ActiveCircuit.Generators

        if not LOAD_COM_OUTPUT: 
            A = self.com.ActiveCircuit.Generators
            if not SAVE_COM_OUTPUT: assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
            if not SAVE_COM_OUTPUT: assert A.Count == B.Count
            if not SAVE_COM_OUTPUT: assert len(A) == len(B)
            nA = A.First
            nB = B.First
            if not SAVE_COM_OUTPUT: assert nA == nB
        else:
            nA = nB = B.First
        
        count = 0
        while nA != 0:
            count += 1

            for field in 'RegisterNames'.split(','):
                fA = output['ActiveCircuit.Generators[{}].{}'.format(nA, field)] if LOAD_COM_OUTPUT else getattr(A, field)
                fB = getattr(B, field)
                if SAVE_COM_OUTPUT: output['ActiveCircuit.Generators[{}].{}'.format(nA, field)] = fA
                if fA == ('',) and fB == [None]: continue # Comtypes and win32com results are a bit different here
                if not SAVE_COM_OUTPUT: assert all(x[0] == x[1] for x in zip(fA, fB)), field

            for field in 'RegisterValues,kvar'.split(','):
                fA = output['ActiveCircuit.Generators[{}].{}'.format(nA, field)] if LOAD_COM_OUTPUT else getattr(A, field)
                fB = getattr(B, field)
                if SAVE_COM_OUTPUT: output['ActiveCircuit.Generators[{}].{}'.format(nA, field)] = fA
                if not SAVE_COM_OUTPUT: assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), field


            for field in 'ForcedON,Model,Name,PF,Phases,Vmaxpu,Vminpu,idx,kV,kVArated,kW'.split(','):
                fA = output['ActiveCircuit.Generators[{}].{}'.format(nA, field)] if LOAD_COM_OUTPUT else getattr(A, field)
                fB = getattr(B, field)
                if SAVE_COM_OUTPUT: output['ActiveCircuit.Generators[{}].{}'.format(nA, field)] = fA
                if not SAVE_COM_OUTPUT: assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            nB = B.Next
            if not LOAD_COM_OUTPUT: 
                nA = A.Next
                if not SAVE_COM_OUTPUT: assert nA == nB
            else:
                nA = nB


    def validate_Isources(self):
        B = self.capi.ActiveCircuit.Isources

        if not LOAD_COM_OUTPUT: 
            A = self.com.ActiveCircuit.ISources
            if not SAVE_COM_OUTPUT: assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
            if not SAVE_COM_OUTPUT: assert A.Count == B.Count
            if not SAVE_COM_OUTPUT: assert len(A) == len(B)
            nA = A.First
            nB = B.First
            if not SAVE_COM_OUTPUT: assert nA == nB
        else:
            nA = nB = B.First
        
        count = 0
        while nA != 0:
            count += 1
            for field in 'Amps,AngleDeg,Frequency,Name'.split(','):
                fA = output['ActiveCircuit.ISources[{}].{}'.format(nA, field)] if LOAD_COM_OUTPUT else getattr(A, field)
                fB = getattr(B, field)
                if SAVE_COM_OUTPUT: output['ActiveCircuit.ISources[{}].{}'.format(nA, field)] = fA
                if not SAVE_COM_OUTPUT: assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            nB = B.Next
            if not LOAD_COM_OUTPUT: 
                nA = A.Next
                if not SAVE_COM_OUTPUT: assert nA == nB
            else:
                nA = nB

        if not LOAD_COM_OUTPUT and count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))

        
    def validate_Vsources(self):
        B = self.capi.ActiveCircuit.Vsources
        
        if not LOAD_COM_OUTPUT: 
            A = self.com.ActiveCircuit.Vsources
            if not SAVE_COM_OUTPUT: assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
            if not SAVE_COM_OUTPUT: assert A.Count == B.Count
            if not SAVE_COM_OUTPUT: assert len(A) == len(B)
            nA = A.First
            nB = B.First
            if not SAVE_COM_OUTPUT: assert nA == nB
        else:
            nA = nB = B.First
        
        count = 0
        while nA != 0:
            count += 1
            for field in 'AngleDeg,BasekV,Frequency,Name,Phases,pu'.split(','):
                fA = output['ActiveCircuit.Vsources[{}].{}'.format(nA, field)] if LOAD_COM_OUTPUT else getattr(A, field)
                fB = getattr(B, field)
                if SAVE_COM_OUTPUT: output['ActiveCircuit.Vsources[{}].{}'.format(nA, field)] = fA
                if not SAVE_COM_OUTPUT: assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            nB = B.Next
            if not LOAD_COM_OUTPUT: 
                nA = A.Next
                if not SAVE_COM_OUTPUT: assert nA == nB
            else:
                nA = nB

        if not LOAD_COM_OUTPUT and count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))


    def validate_Reclosers(self):
        B = self.capi.ActiveCircuit.Reclosers

        if not LOAD_COM_OUTPUT: 
            A = self.com.ActiveCircuit.Reclosers
            if not SAVE_COM_OUTPUT: assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
            if not SAVE_COM_OUTPUT: assert A.Count == B.Count
            if not SAVE_COM_OUTPUT: assert len(A) == len(B)
            nA = A.First
            nB = B.First
            if not SAVE_COM_OUTPUT: assert nA == nB
        else:
            nA = nB = B.First
        
        count = 0
        while nA != 0:
            count += 1
            for field in 'RecloseIntervals'.split(','):
                fA = output['ActiveCircuit.Reclosers[{}].{}'.format(nA, field)] if LOAD_COM_OUTPUT else getattr(A, field)
                fB = getattr(B, field)
                if SAVE_COM_OUTPUT: output['ActiveCircuit.Reclosers[{}].{}'.format(nA, field)] = fA
                fA = np.array(fA, dtype=fB.dtype)
                if not SAVE_COM_OUTPUT: assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), field

            for field in 'GroundInst,GroundTrip,MonitoredObj,MonitoredTerm,Name,NumFast,PhaseInst,PhaseTrip,Shots,SwitchedObj,SwitchedTerm,idx'.split(','):
                fA = output['ActiveCircuit.Reclosers[{}].{}'.format(nA, field)] if LOAD_COM_OUTPUT else getattr(A, field)
                fB = getattr(B, field)
                if SAVE_COM_OUTPUT: output['ActiveCircuit.Reclosers[{}].{}'.format(nA, field)] = fA
                if not SAVE_COM_OUTPUT: assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)
                
            nB = B.Next
            if not LOAD_COM_OUTPUT: 
                nA = A.Next
                if not SAVE_COM_OUTPUT: assert nA == nB
            else:
                nA = nB

        if not LOAD_COM_OUTPUT and count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))


    def validate_XYCurves(self):
        B = self.capi.ActiveCircuit.XYCurves
        
        if not LOAD_COM_OUTPUT: 
            A = self.com.ActiveCircuit.XYCurves
#            if not SAVE_COM_OUTPUT: assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
            if not SAVE_COM_OUTPUT: assert A.Count == B.Count
            if not SAVE_COM_OUTPUT: assert len(A) == len(B)
            nA = A.First
            nB = B.First
            if not SAVE_COM_OUTPUT: assert nA == nB
        else:
            nA = nB = B.First
        
        count = 0
        while nA != 0:
            count += 1
            for field in 'Xarray,Yarray'.split(','):
                fA = output['ActiveCircuit.XYCurves[{}].{}'.format(nA, field)] if LOAD_COM_OUTPUT else getattr(A, field)
                fB = getattr(B, field)
                if SAVE_COM_OUTPUT: output['ActiveCircuit.XYCurves[{}].{}'.format(nA, field)] = fA
                if not SAVE_COM_OUTPUT: assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), field

            for field in 'Name,Npts,Xscale,Xshift,Yscale,Yshift,x,y'.split(','):
                fA = output['ActiveCircuit.XYCurves[{}].{}'.format(nA, field)] if LOAD_COM_OUTPUT else getattr(A, field)
                fB = getattr(B, field)
                if SAVE_COM_OUTPUT: output['ActiveCircuit.XYCurves[{}].{}'.format(nA, field)] = fA
                if not SAVE_COM_OUTPUT: assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            nB = B.Next
            if not LOAD_COM_OUTPUT: 
                nA = A.Next
                if not SAVE_COM_OUTPUT: assert nA == nB
            else:
                nA = nB

        if not LOAD_COM_OUTPUT and count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))


    def validate_Monitors(self):
        B = self.capi.ActiveCircuit.Monitors
        
        if not LOAD_COM_OUTPUT: 
            A = self.com.ActiveCircuit.Monitors
            if not SAVE_COM_OUTPUT: assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
            if not SAVE_COM_OUTPUT: assert A.Count == B.Count
            if not SAVE_COM_OUTPUT: assert len(A) == len(B)
            nA = A.First
            nB = B.First
            if not SAVE_COM_OUTPUT: assert nA == nB
        else:
            nA = nB = B.First
        
        count = 0
        while nA != 0:
            count += 1
            header = B.Header
            monitor_name = B.Name
            
            for field in 'dblFreq,dblHour'.split(','): # Skipped ByteStream since it's indirectly compared through Channel()
                fA = output['ActiveCircuit.Monitors[{}].{}'.format(nA, field)] if LOAD_COM_OUTPUT else getattr(A, field)
                fB = getattr(B, field)
                if SAVE_COM_OUTPUT: output['ActiveCircuit.Monitors[{}].{}'.format(nA, field)] = fA
                fA = np.array(fA, dtype=fB.dtype)
                if not SAVE_COM_OUTPUT: assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), field

            #TODO: FileVersion (broken in COM)
            for field in 'Element,Header,FileName,Mode,Name,NumChannels,RecordSize,SampleCount,Terminal'.split(','):
                if field == 'FileName': continue # the path will be different on purpose
                fA = output['ActiveCircuit.Monitors[{}].{}'.format(nA, field)] if LOAD_COM_OUTPUT else getattr(A, field)
                fB = getattr(B, field)
                if SAVE_COM_OUTPUT: output['ActiveCircuit.Monitors[{}].{}'.format(nA, field)] = fA
                
                #if not SAVE_COM_OUTPUT: assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            for channel in range(B.NumChannels):
                if header[channel] in (' SolveSnap_uSecs', ' TimeStep_uSecs'): continue # these can't be equal
                field = 'Channel({})'.format(channel + 1)
                output_key = 'ActiveCircuit.Monitors[{}].{}'.format(monitor_name, field)
                fA = output[output_key] if LOAD_COM_OUTPUT else A.Channel(channel + 1)
                fB = B.Channel(channel + 1)
                if SAVE_COM_OUTPUT: output[output_key] = fA
                if not SAVE_COM_OUTPUT: 
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


            nB = B.Next
            if not LOAD_COM_OUTPUT: 
                nA = A.Next
                if not SAVE_COM_OUTPUT: assert nA == nB
            else:
                nA = nB

        if not LOAD_COM_OUTPUT and count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))


    def validate_Meters(self):
        B = self.capi.ActiveCircuit.Meters
        
        if not LOAD_COM_OUTPUT: 
            A = self.com.ActiveCircuit.Meters
            if not SAVE_COM_OUTPUT: assert (all(x[0] == x[1] for x in zip(A.AllNames, B.AllNames)))
            if not SAVE_COM_OUTPUT: assert A.Count == B.Count
            if not SAVE_COM_OUTPUT: assert len(A) == len(B)
            nA = A.First
            nB = B.First
            if not SAVE_COM_OUTPUT: assert nA == nB
        else:
            nA = nB = B.First
        
        count = 0
        while nA != 0:
            count += 1
            for field in 'AllBranchesInZone,AllEndElements,RegisterNames'.split(','):
                fA = output['ActiveCircuit.Meters[{}].{}'.format(nA, field)] if LOAD_COM_OUTPUT else getattr(A, field)
                fB = getattr(B, field)
                if SAVE_COM_OUTPUT: output['ActiveCircuit.Meters[{}].{}'.format(nA, field)] = fA
                if fA == ('',) and fB == [None]: continue # Comtypes and win32com results are a bit different here
                if not SAVE_COM_OUTPUT: assert all(x[0] == x[1] for x in zip(fA, fB)), field


            # NOTE: CalcCurrent and AllocFactors removed since it seemed to contain (maybe?) uninitialized values in certain situations
            fields = 'AvgRepairTime,Peakcurrent,RegisterValues,Totals' if self.realibity_ran else 'Peakcurrent,RegisterValues'
            for field in fields.split(','):
                fA = output['ActiveCircuit.Meters[{}].{}'.format(nA, field)] if LOAD_COM_OUTPUT else getattr(A, field)
                fB = getattr(B, field)
                if SAVE_COM_OUTPUT: output['ActiveCircuit.Meters[{}].{}'.format(nA, field)] = fA
                if not SAVE_COM_OUTPUT: assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), ('Meters("{}").{}'.format(A.Name, field), fA, fB)

            fields = 'CountBranches,CountEndElements,CustInterrupts,DIFilesAreOpen,FaultRateXRepairHrs,MeteredElement,MeteredTerminal,Name,NumSectionBranches,NumSectionCustomers,NumSections,OCPDeviceType,SAIDI,SAIFI,SAIFIKW,SectSeqIdx,SectTotalCust,SeqListSize,SequenceIndex,SumBranchFltRates,TotalCustomers' if self.realibity_ran else 'MeteredElement,MeteredTerminal,Name'
            for field in fields.split(','):
                fA = output['ActiveCircuit.Meters[{}].{}'.format(nA, field)] if LOAD_COM_OUTPUT else getattr(A, field)
                fB = getattr(B, field)
                if SAVE_COM_OUTPUT: output['ActiveCircuit.Meters[{}].{}'.format(nA, field)] = fA
                if not SAVE_COM_OUTPUT: assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            nB = B.Next
            if not LOAD_COM_OUTPUT: 
                nA = A.Next
                if not SAVE_COM_OUTPUT: assert nA == nB
            else:
                nA = nB

        if not LOAD_COM_OUTPUT and count != A.Count: print("!!! WARNING: Iterated count ({}) != Count ({}) property on {}".format(count, A.Count, sys._getframe().f_code.co_name))

        
    def validate_Settings(self):
        B = self.capi.ActiveCircuit.Settings
        
        if not LOAD_COM_OUTPUT: 
            A = self.com.ActiveCircuit.Settings

        for field in 'LossRegs,UEregs,VoltageBases'.split(','):
            fA = output['ActiveCircuit.Settings.{}'.format(field)] if LOAD_COM_OUTPUT else getattr(A, field)
            fB = getattr(B, field)
            if SAVE_COM_OUTPUT: output['ActiveCircuit.Settings.{}'.format(field)] = fA
            if not SAVE_COM_OUTPUT: assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), field
        
        
        # AutoBusList is broken in COM, doesn't clear the GlobalResult first.
        # for field in 'AutoBusList'.split(','):
        #     fA = output['ActiveCircuit.Settings.{}'.format(field)] if LOAD_COM_OUTPUT else getattr(A, field)
        #     fB = getattr(B, field)
        #     if SAVE_COM_OUTPUT: output['ActiveCircuit.Settings.{}'.format(field)] = fA
        #     if not SAVE_COM_OUTPUT: assert fA == fB, (field, (fA, fB))
        
        for field in 'AllowDuplicates,CktModel,ControlTrace,EmergVmaxpu,EmergVminpu,LossWeight,NormVmaxpu,NormVminpu,PriceCurve,PriceSignal,Trapezoidal,UEweight,ZoneLock'.split(','):
            fA = output['ActiveCircuit.Settings.{}'.format(field)] if LOAD_COM_OUTPUT else getattr(A, field)
            fB = getattr(B, field)
            if SAVE_COM_OUTPUT: output['ActiveCircuit.Settings.{}'.format(field)] = fA
            if not SAVE_COM_OUTPUT: assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

    def validate_Solution(self):
        B = self.capi.ActiveCircuit.Solution
        
        if not LOAD_COM_OUTPUT: 
            A = self.com.ActiveCircuit.Solution

        for field in 'AddType,Algorithm,Capkvar,ControlActionsDone,ControlIterations,ControlMode,Converged,DefaultDaily,DefaultYearly,Frequency,GenMult,GenPF,GenkW,Hour,Iterations,LDCurve,LoadModel,LoadMult,MaxControlIterations,MaxIterations,Mode,ModeID,MostIterationsDone,Number,Random,Seconds,StepSize,Tolerance,Totaliterations,Year,dblHour,pctGrowth'.split(','): #TODO: EventLog, IntervalHrs, MinIterations, Process_Time, Total_Time, Time_of_Step, SystemYChanged
            # if LOAD_COM_OUTPUT and field == 'SystemYChanged':
                # continue
        
            fA = output['ActiveCircuit.Solution.{}'.format(field)] if LOAD_COM_OUTPUT else getattr(A, field)
            fB = getattr(B, field)
            if SAVE_COM_OUTPUT: output['ActiveCircuit.Solution.{}'.format(field)] = fA
            if not SAVE_COM_OUTPUT: assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

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
            "SystemY" : self.SystemY[imin:imax],
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
        self.SystemY = data["SystemY"]
        self.TotalPower = data["TotalPower"]
        self.YCurrents = data["YCurrents"]
        self.YNodeOrder = data["YNodeOrder"]
        self.YNodeVarray = data["YNodeVarray"]
            
            
    def validate_Circuit(self):
        all_fields = self._get_circuit_fields()
        
        # Test Circuit_SetCktElementName with line names
        if not LOAD_COM_OUTPUT:
            # Get all line names
            lines_names = []
            LA = self.com.ActiveCircuit.Lines
            nA = LA.First
            while nA != 0:
                lines_names.append(LA.Name)
                nA = LA.Next
        
            for name in lines_names:
                B = self.capi.ActiveCircuit.CktElements('Line.' + name)
                A = self.com.ActiveCircuit.CktElements('Line.' + name)
                if not SAVE_COM_OUTPUT: assert A.Name == B.Name
            
            # Test Circuit_SetCktElementIndex
            num_cktelements = len(self.com.ActiveCircuit.AllElementNames)
            for idx in range(num_cktelements):
                B = self.capi.ActiveCircuit.CktElements(idx)
                A = self.com.ActiveCircuit.CktElements(idx)
                if not SAVE_COM_OUTPUT: assert A.Name == B.Name

            # Try to use an invalid index
            try:
                B = self.capi.ActiveCircuit.CktElements(999999)
            except DSSException:
                pass
                
            A = self.com.ActiveCircuit.CktElements(999999)
            if not SAVE_COM_OUTPUT: assert A.Name == B.Name

            # Try to use an invalid name
            try:
                B = self.capi.ActiveCircuit.CktElements('NONEXISTENT_123456789')
            except DSSException:
                pass

            A = self.com.ActiveCircuit.CktElements('NONEXISTENT_123456789')
            if not SAVE_COM_OUTPUT: assert A.Name == B.Name
        
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
                    if not SAVE_COM_OUTPUT: 
                        cv = [np.asarray(v[0]).view(dtype=complex), np.asarray(v[1]).view(dtype=complex)]
                        assert np.allclose(cv[0], cv[1], atol=self.atol, rtol=self.rtol), (k, cv[0], cv[1])
                        # else:
                            # assert np.allclose(v[0]/v[1], 1, atol=self.atol, rtol=100), (k, type(v[1]), v[0], v[1])
                else:
                    if not SAVE_COM_OUTPUT: assert np.allclose(*v, atol=self.atol, rtol=self.rtol), (k, type(v[1]))#, v[0], v[1])
            elif type(v[1]) == list:
                if not SAVE_COM_OUTPUT: assert all(x[0] == x[1] for x in zip(*v)), (k, type(v[1]))
            elif type(v[1]) == int:
                if not SAVE_COM_OUTPUT: assert v[0] == v[1], (k, type(v[1]))
            elif type(v[1]) == float:
                if not SAVE_COM_OUTPUT: assert abs(v[0] - v[1]) < atol, (k, type(v[1]))

    def validate_YMatrix(self):
        NN = self.capi.ActiveCircuit.NumNodes
        if NN > 2000: # test only on small strings
            return
            
        ysparse = csc_matrix(self.capi.YMatrix.GetCompressedYMatrix(factor=False))
        ydense = self.capi.ActiveCircuit.SystemY.view(dtype=complex).reshape((NN, NN))
        if not SAVE_COM_OUTPUT: assert (np.allclose(ydense, ysparse.todense(), atol=self.atol, rtol=self.rtol))
        
        
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

        for cls in clss:
            try:
                assert (check_cls_allnames(cls, self.com) == check_cls_allnames(cls, self.capi)), cls
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
        print('Buses')
        self.validate_Buses()
        print('Circuit')
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
    if not LOAD_COM_OUTPUT:
        import win32com.client
        com = win32com.client.Dispatch("OpenDSSEngine.DSS")
        com = win32com.client.gencache.EnsureDispatch("OpenDSSEngine.DSS")
        
        import dss
        com = dss.patch_dss_com(com)
        print('COM Version:', com.Version)
        global COM_VLL_BROKEN
        COM_VLL_BROKEN = ('Version 8.6.7.1 ' in com.Version) or ('Version 9.0.0.8 ' in com.Version)
    else:
        com = None

    #import comtypes.client
    #com = comtypes.client.CreateObject("OpenDSSEngine.DSS")

    capi = DSS
    print('C-API Version:', capi.Version)

    for dss in [com, capi]:
        if dss is not None:
            dss.Text.Command = r'set editor=ignore_me_invalid_executable'
        
    capi.AllowEditor = False
    capi.Error.ExtendedErrors = False
    assert capi.Error.EarlyAbort # check the default value, should be True

    # Test toggling console output with C-API, COM can only be disabled
    if not LOAD_COM_OUTPUT:
        for dss in com, capi:
            dss.AllowForms = True
            if not SAVE_COM_OUTPUT: assert dss.AllowForms == True

            dss.AllowForms = False
            if not SAVE_COM_OUTPUT: assert dss.AllowForms == False
            
            dss.AllowForms = True
            if dss != com:
                if not SAVE_COM_OUTPUT: assert dss.AllowForms == True

            dss.AllowForms = False
            if not SAVE_COM_OUTPUT: assert dss.AllowForms == False
    else:
        for dss in [capi]:
            dss.AllowForms = True
            if not SAVE_COM_OUTPUT: assert dss.AllowForms == True

            dss.AllowForms = False
            if not SAVE_COM_OUTPUT: assert dss.AllowForms == False
            
            dss.AllowForms = True
            if not SAVE_COM_OUTPUT: assert dss.AllowForms == True

            dss.AllowForms = False
            if not SAVE_COM_OUTPUT: assert dss.AllowForms == False
    

            
    total_com_time = 0.0
    total_capi_time = 0.0
            
    global output
    
    for fn in fns:
        line_by_line = fn.startswith('L!')
        if line_by_line:
            fn = fn[2:]
        print("> File", fn)
        assert os.path.exists(os.path.join(original_working_dir, fn)), os.path.join(original_working_dir, fn)
        
        test = ValidatingTest(fn, com, capi, line_by_line)

        if not LOAD_COM_OUTPUT:
            print("Running using COM")
            t0 = time()
            test.run(com, solve=True)
            total_com_time += time() - t0
            output['ActiveCircuit'] = test._get_circuit_fields(0, 1)
        else:
            os.chdir(original_working_dir)
            pickle_fn = fn + '.pickle'
            with open(pickle_fn, 'rb') as com_output_file:
                output = pickle.load(com_output_file)
                print('COM output loaded from', pickle_fn)
                test._set_circuit_fields(output['ActiveCircuit'])
        
        print("Running using CAPI")
        t0 = time()
        test.run(capi, solve=True)
        total_capi_time += time() - t0  
        
        
        print("Validating")
        try:
            test.validate_all()
        except (AssertionError, TypeError) as ex:
            print('!!!!!!!!!!!!!!!!!!!!!!')
            print('ERROR:', fn, ex)
            print('!!!!!!!!!!!!!!!!!!!!!!')
            raise

            
        if WIN32 and SAVE_COM_OUTPUT:
            os.chdir(original_working_dir)
            pickle_fn = fn + '.pickle'
            with open(pickle_fn, 'wb') as com_output_file:
                pickle.dump(output, com_output_file, protocol=pickle.HIGHEST_PROTOCOL)
                print('COM output pickled to', pickle_fn)
            
            output = type(output)()
            
           
    if not LOAD_COM_OUTPUT:
        print("Total COM running time: {} seconds".format(int(total_com_time)))
        print("Total C-API running time: {} seconds ({}% of COM)".format(
            int(total_capi_time), 
            round(100 * total_capi_time / total_com_time, 1)
        ))
            
    
    if not LOAD_COM_OUTPUT:
        for dss in com, capi:
            if USE_V8:
                dss.Text.Command = 'ClearAll'
            else:
                dss.Text.Command = 'Clear'
            
if __name__ == '__main__':
    from common import test_filenames
    t0_global = time()
    run_tests(test_filenames)
    print(time() - t0_global, 'seconds')