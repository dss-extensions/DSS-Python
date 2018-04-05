from __future__ import print_function
import os, sys
import numpy as np

cd = os.getcwd()
no_properties = os.getenv('DSS_PYTHON_VALIDATE') == 'NOPROP'

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
        os.chdir(cd)
        dss.Start(0)
        dss.Text.Command = 'Clear'
        dss.AllowForms = False

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
          
          
        if no_properties: return
            
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
            
            assert (A.Properties(prop_name).Description == B.Properties(prop_name).Description), ('Properties({}).Description'.format(prop_name), A.Properties(prop_name).Description, B.Properties(prop_name).Description)
            assert (A.Properties(prop_name).name == B.Properties(prop_name).name), ('Properties({}).name'.format(prop_name), A.Properties(prop_name).name, B.Properties(prop_name).name)

            assert (B.Properties(prop_name).Val == B.Properties[prop_name].Val)
            assert (B.Properties(prop_name).Description == B.Properties[prop_name].Description)
            assert (B.Properties(prop_name).name == B.Properties[prop_name].name)


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
                if type(fA) == tuple and len(fA) == 0:
                    assert fB is None or len(fB) == 0, ('ActiveBus.{}'.format(field), fA, fB)
                    continue

                if field in ('SeqVoltages', 'CplxSeqVoltages', 'VLL'): continue # skip

                if field == 'CplxSeqVoltages':
                    # Investigating the different in (Cplx)SeqVoltages, I noted that the phase-to-sequence
                    # transform matrix has low precision values in OpenDSS. Currently, the matrix is filled as:
                    #
                    #    SetAMatrix(Ap2s);
                    #    Ap2s.Invert;
                    #
                    # ...but, since SetAMatrix doesn't use high precision values, the inverted
                    # matrix has poor values. This should not be much of an issue, but we cannot
                    # compare high resolution values in this validation since much of the precision
                    # is lost.
                    #
                    # An alternative (untested) would be to fill the Ap2s matrix directly and use
                    # a higher number of digits in "a":
                    #
                    #    Procedure SetAMatrix_inv(Amat:Tcmatrix);
                    #    Var
                    #       a,aa:complex;
                    #       i:Integer;
                    #    Begin
                    #        a := cmplx(-0.5,0.8660254037844387);
                    #        aa := cmplx(-0.5,-0.8660254037844387);
                    #        With Amat Do begin
                    #             For i := 1 to 3 Do SetElemSym(1,i,CONE);
                    #             SetElement(2,2,a);
                    #             SetElement(3,3,a);
                    #             SetElemsym(2,3,aa);
                    #        End;
                    #    End;
                    #    SetAMatrix_inv(Ap2s);
                    #
                    #
                    #

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
                        # assert np.isclose(pyB, pyA, atol=self.atol, rtol=1e-5), ('pyB, pyA =', pyB, pyB)
                    for pasA, pasB in zip(
                        np.array(A.CplxSeqVoltages).view(dtype=complex),
                        np.array(B.CplxSeqVoltages).view(dtype=complex)
                    ):
                        assert np.isclose(pasA, pasB, atol=self.atol, rtol=self.rtol), ('ActiveBus.' + field, name, pasA, pasB)

                    continue

                # if field == 'VMagAngle':
                    # fA = (np.array(fA) * np.pi / 180.0) % (np.pi)
                    # fB = (np.array(fB) * np.pi / 180.0) % (np.pi)

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
                assert np.allclose(getattr(A, field), getattr(B, field), atol=self.atol, rtol=self.rtol), field

            for field in ('AvailableSteps', 'NumSteps', 'kvar', 'kV', 'Name', 'IsDelta'):
                assert getattr(A, field) == getattr(B, field), field

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
                assert np.allclose(getattr(A, field), getattr(B, field), atol=self.atol, rtol=self.rtol), field

            for field in 'C0,C1,EmergAmps,IsZ1Z0,Name,NormAmps,Phases,R0,R1,Units,X0,X1'.split(','):
                assert getattr(A, field) == getattr(B, field), field

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
                assert np.allclose(getattr(A, field), getattr(B, field), atol=self.atol, rtol=self.rtol), field

            # Note: removed property Parent from the analysis since it raises a popup
            for field in 'Bus1,Bus2,C0,C1,EmergAmps,Geometry,Length,LineCode,Name,NormAmps,NumCust,Phases,R0,R1,Rg,Rho,Spacing,TotalCust,Units,X0,X1,Xg'.split(','):
                fA = getattr(A, field)
                fB = getattr(B, field)
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
        A = self.com.ActiveCircuit.Loadshapes
        B = self.capi.ActiveCircuit.Loadshapes
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
                assert np.allclose(getattr(A, field), getattr(B, field), atol=self.atol, rtol=self.rtol), field

            for field in 'HrInterval,MinInterval,Name,Npts,PBase,Qbase,UseActual,sInterval'.split(','): #TODO: ZIPV
                fA = getattr(A, field)
                fB = getattr(B, field)
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
            for field in 'IsDelta,MaxTap,MinTap,Name,NumTaps,NumWindings,R,Rneut,Tap,Wdg,XfmrCode,Xhl,Xht,Xlt,Xneut,kV,kVA'.split(','):
                fA = getattr(A, field)
                fB = getattr(B, field)
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
                if fA == ('',) and fB == [None]: continue # Comtypes and win32com results are a bit different here
                assert all(x[0] == x[1] for x in zip(fA, fB)), field

            for field in 'RegisterValues,kvar'.split(','):
                assert np.allclose(getattr(A, field), getattr(B, field), atol=self.atol, rtol=self.rtol), field


            for field in 'ForcedON,Model,Name,PF,Phases,Vmaxpu,Vminpu,idx,kV,kVArated,kW'.split(','):
                fA = getattr(A, field)
                fB = getattr(B, field)
                assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            nA = A.Next
            nB = B.Next
            assert nA == nB


    def validate_Isources(self):
        A = self.com.ActiveCircuit.Isources
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
                fA = np.array(fA, dtype=fB.dtype)
                assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), field

            for field in 'GroundInst,GroundTrip,MonitoredObj,MonitoredTerm,Name,NumFast,PhaseInst,PhaseTrip,Shots,SwitchedObj,SwitchedTerm,idx'.split(','):
                fA = getattr(A, field)
                fB = getattr(B, field)
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
                assert np.allclose(getattr(A, field), getattr(B, field), atol=self.atol, rtol=self.rtol), field

            for field in 'Name,Npts,Xscale,Xshift,Yscale,Yshift,x,y'.split(','):
                fA = getattr(A, field)
                fB = getattr(B, field)
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
                fA = np.array(fA, dtype=fB.dtype)
                assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), field

            #TODO: FileVersion,Header
            for field in 'Element,FileName,Mode,Name,NumChannels,RecordSize,SampleCount,Terminal'.split(','):
                fA = getattr(A, field)
                fB = getattr(B, field)
                assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

            for channel in range(A.NumChannels):
                fA = A.Channel(channel + 1)
                fB = A.Channel(channel + 1)
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
                if fA == ('',) and fB == [None]: continue # Comtypes and win32com results are a bit different here
                assert all(x[0] == x[1] for x in zip(fA, fB)), field


            # NOTE: CalcCurrent and AllocFactors removed since it seemed to contain (maybe?) uninitialized values in certain situations
            for field in 'AvgRepairTime,Peakcurrent,RegisterValues,Totals'.split(','):
                fA = getattr(A, field)
                fB = getattr(B, field)
                assert np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), ('Meters("{}").{}'.format(A.Name, field), fA, fB)


            for field in 'CountBranches,CountEndElements,CustInterrupts,DIFilesAreOpen,FaultRateXRepairHrs,MeteredElement,MeteredTerminal,Name,NumSectionBranches,NumSectionCustomers,NumSections,OCPDeviceType,SAIDI,SAIFI,SAIFIKW,SectSeqIdx,SectTotalCust,SeqListSize,SequenceIndex,SumBranchFltRates,TotalCustomers'.split(','):
                fA = getattr(A, field)
                fB = getattr(B, field)
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
            assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)

    def validate_Solution(self):
        A = self.com.ActiveCircuit.Solution
        B = self.capi.ActiveCircuit.Solution

        for field in 'AddType,Algorithm,Capkvar,ControlActionsDone,ControlIterations,ControlMode,Converged,DefaultDaily,DefaultYearly,Frequency,GenMult,GenPF,GenkW,Hour,Iterations,LDCurve,LoadModel,LoadMult,MaxControlIterations,MaxIterations,Mode,ModeID,MostIterationsDone,Number,Random,Seconds,StepSize,SystemYChanged,Tolerance,Totaliterations,Year,dblHour,pctGrowth'.split(','): #TODO: EventLog, IntervalHrs, MinIterations, Process_Time, Total_Time, Time_of_Step
            fA = getattr(A, field)
            fB = getattr(B, field)
            assert (fA == fB) or (type(fB) == str and fA is None and fB == '') or np.allclose(fA, fB, atol=self.atol, rtol=self.rtol), (field, fA, fB)


    def validate_Circuit(self):
        all_fields = {
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

        #self.atol = 1e-5
        # print('Buses')
        self.validate_Buses()
        # print('Circuit')
        self.validate_Circuit()

        self.capi.ShowPanel()
        
        print('Done')


def run_tests(fns):
    from dss import DSS, use_com_compat
    use_com_compat()

    import win32com.client
    com = win32com.client.Dispatch("OpenDSSEngine.DSS")
    #com = win32com.client.gencache.EnsureDispatch("OpenDSSEngine.DSS")

    #import comtypes.client
    #com = comtypes.client.CreateObject("OpenDSSEngine.DSS")

    capi = DSS

    for fn in fns:
        line_by_line = fn.startswith('L!')
        if line_by_line:
            fn = fn[2:]

        print("> File", fn)
        test = ValidatingTest(fn, com, capi, line_by_line)
        print("Running using CAPI")
        test.run(capi, solve=True)
        print("Running using COM")
        test.run(com, solve=True)
        print("Validating")
        try:
            test.validate_all()
        except AssertionError as ex:
            print('!!!!!!!!!!!!!!!!!!!!!!')
            print('ERROR:', fn, ex)
            print('!!!!!!!!!!!!!!!!!!!!!!')


if __name__ == '__main__':
    fns = [
        "../../electricdss/Distrib/IEEETestCases/IEEE 30 Bus/Master.dss",
        "../../electricdss/Distrib/EPRITestCircuits/ckt5/Master_ckt5.dss",
         "../../electricdss/Distrib/EPRITestCircuits/ckt7/Master_ckt7.dss",
         "../../electricdss/Distrib/EPRITestCircuits/ckt24/Master_ckt24.dss",
        "../../electricdss/Distrib/IEEETestCases/8500-Node/Master-unbal.dss",
        "../../electricdss/Distrib/IEEETestCases/NEVTestCase/NEVMASTER.DSS",
        "../../electricdss/Distrib/IEEETestCases/37Bus/ieee37.dss",
        "../../electricdss/Distrib/IEEETestCases/4Bus-DY-Bal/4Bus-DY-Bal.DSS",
        "../../electricdss/Distrib/IEEETestCases/4Bus-GrdYD-Bal/4Bus-GrdYD-Bal.DSS",
        "../../electricdss/Distrib/IEEETestCases/4Bus-OYOD-Bal/4Bus-OYOD-Bal.DSS",
        "../../electricdss/Distrib/IEEETestCases/4Bus-OYOD-UnBal/4Bus-OYOD-UnBal.DSS",
        "../../electricdss/Distrib/IEEETestCases/4Bus-YD-Bal/4Bus-YD-Bal.DSS",
        "../../electricdss/Distrib/IEEETestCases/4Bus-YY-Bal/4Bus-YY-Bal.DSS",
        "L!../../electricdss/Distrib/IEEETestCases/123Bus/IEEE123Master.dss",
        "L!../../electricdss/Distrib/IEEETestCases/123Bus/SolarRamp.DSS",
        "../../electricdss/Distrib/IEEETestCases/13Bus/IEEE13Nodeckt.dss",

        "../../electricdss/Test/IEEE13_LineSpacing.dss",
        "../../electricdss/Test/IEEE13_LineGeometry.dss",
        "../../electricdss/Test/IEEE13_LineAndCableSpacing.dss",
        "../../electricdss/Test/IEEE13_Assets.dss",
        "L!../../electricdss/Test/CableParameters.dss",
        "L!../../electricdss/Test/Cable_constants.DSS",
        "L!../../electricdss/Test/BundleDemo.DSS",
        "../../electricdss/Test/IEEE13_SpacingGeometry.dss",
        "../../electricdss/Test/TextTsCable750MCM.dss",
        "L!../../electricdss/Test/TestDDRegulator.dss",
        "../../electricdss/Test/XYCurvetest.dss",
        "L!../../electricdss/Test/PVSystemTestHarm.dss",
        "L!../../electricdss/Test/TestAuto.dss",
        "L!../../electricdss/Test/Stevenson.dss",
        "L!../../electricdss/Test/YgD-Test.dss", # NOTE: this one can be used to test ASLR issues and SET __COMPAT_LAYER=WIN7RTM
        "../../electricdss/Test/Master_TestCapInterface.DSS",
        "../../electricdss/Test/LoadTest.DSS",
        "L!../../electricdss/Test/IEEELineGeometry.dss",
        "L!../../electricdss/Test/ODRegTest.dss",
        "L!../../electricdss/Test/MultiCircuitTest.DSS",
        "L!../../electricdss/Test/TriplexLineCodeCalc.DSS",
        "L!../../electricdss/Test/PVSystemTest-Duty.dss",
        "L!../../electricdss/Test/PVSystemTest.dss",
        "L!../../electricdss/Test/REACTORTest.DSS",

        #"../../electricdss/Distrib/IEEETestCases/DG_Protection/DG_Prot_Fdr.dss", 
        #"../../electricdss/Test/IEEE13_CDPSM.dss",

        #"L!../../electricdss/Test/Run_SimpleStorageTest.DSS", # Missing DLL?
        #"L!../../electricdss/Test/Run_SimpleStorageTest-1ph.DSS", # Missing DLL?
        #"L!../../electricdss/Test/Source012Test.dss", # Different encoding, skipping

        # 'Generator User Model IndMach012a Not Loaded.'
        #"L!../../electricdss/Distrib/IEEETestCases/4wire-Delta/Kersting4wire_Lagging.dss",
        #"L!../../electricdss/Distrib/IEEETestCases/4wire-Delta/Kersting4wire_Leading.dss",
        #"L!../../electricdss/Distrib/IEEETestCases/4wire-Delta/Kersting4wireIndMotor.dss",

    ]

    from time import time
    t0_global = time()
    run_tests(fns)
    print(time() - t0_global, 'seconds')