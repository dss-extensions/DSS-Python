# Lines starting with "L!" indicate the file will be run line by line, 
# filtering interactive commands

test_filenames = [
    # This one is expected to have different results (C-API should be more precise)
    # "../../electricdss-tst/Distrib/IEEETestCases/DG_Protection/DG_Prot_Fdr.dss", 
    
    # This one was checked manually. There is a small difference but the relative 
    # difference in voltage is still <3x10^-7
    # It should be uncommented when all complex number comparisons are rewritten.
    # Currently the re and im parts are compared separatly, which is misleading.
    # "../../electricdss-tst/Version8/Distrib/IEEETestCases/LVTestCaseNorthAmerican/Master.dss",
    
    "../../electricdss-tst/Test/IEEE13_CDPSM.dss",
    "../../electricdss-tst/Test/IEEE13_LineAndCableSpacing.dss",
    "L!../../electricdss-tst/Test/YgD-Test.dss", # NOTE: this one can be used to test ASLR issues and SET __COMPAT_LAYER=WIN7RTM
    "L!../../electricdss-tst/Distrib/IEEETestCases/123Bus/IEEE123Master.dss",
    "L!../../electricdss-tst/Distrib/IEEETestCases/123Bus/SolarRamp.DSS",
    "../../electricdss-tst/Distrib/IEEETestCases/37Bus/ieee37.dss",

    "../../electricdss-tst/Distrib/IEEETestCases/IEEE 30 Bus/Master.dss",
    "../../electricdss-tst/Distrib/EPRITestCircuits/epri_dpv/J1/Master_withPV.dss",
    "../../electricdss-tst/Distrib/EPRITestCircuits/epri_dpv/K1/Master_NoPV.dss",
    "../../electricdss-tst/Distrib/EPRITestCircuits/epri_dpv/M1/Master_NoPV.dss",
    "../../electricdss-tst/Distrib/EPRITestCircuits/ckt5/Master_ckt5.dss",
    "../../electricdss-tst/Distrib/EPRITestCircuits/ckt7/Master_ckt7.dss",
    "../../electricdss-tst/Distrib/EPRITestCircuits/ckt24/Master_ckt24.dss",
    "../../electricdss-tst/Distrib/IEEETestCases/8500-Node/Master-unbal.dss",
    "../../electricdss-tst/Distrib/IEEETestCases/NEVTestCase/NEVMASTER.DSS",
    "../../electricdss-tst/Distrib/IEEETestCases/4Bus-DY-Bal/4Bus-DY-Bal.DSS",
    "../../electricdss-tst/Distrib/IEEETestCases/4Bus-GrdYD-Bal/4Bus-GrdYD-Bal.DSS",
    "../../electricdss-tst/Distrib/IEEETestCases/4Bus-OYOD-Bal/4Bus-OYOD-Bal.DSS",
    "../../electricdss-tst/Distrib/IEEETestCases/4Bus-OYOD-UnBal/4Bus-OYOD-UnBal.DSS",
    "../../electricdss-tst/Distrib/IEEETestCases/4Bus-YD-Bal/4Bus-YD-Bal.DSS",
    "../../electricdss-tst/Distrib/IEEETestCases/4Bus-YY-Bal/4Bus-YY-Bal.DSS",
    "../../electricdss-tst/Distrib/IEEETestCases/13Bus/IEEE13Nodeckt.dss",

    "../../electricdss-tst/Test/IEEE13_LineSpacing.dss",
    "../../electricdss-tst/Test/IEEE13_LineGeometry.dss",
    "../../electricdss-tst/Test/IEEE13_Assets.dss",
    "L!../../electricdss-tst/Test/CableParameters.dss",
    "L!../../electricdss-tst/Test/Cable_constants.DSS",
    "L!../../electricdss-tst/Test/BundleDemo.DSS",
    "../../electricdss-tst/Test/IEEE13_SpacingGeometry.dss",
    "../../electricdss-tst/Test/TextTsCable750MCM.dss",
    "L!../../electricdss-tst/Test/TestDDRegulator.dss",
    "../../electricdss-tst/Test/XYCurvetest.dss",
    "L!../../electricdss-tst/Test/PVSystemTestHarm.dss",
    "L!../../electricdss-tst/Test/TestAuto.dss",
    "L!../../electricdss-tst/Test/Stevenson.dss",
    "../../electricdss-tst/Test/Master_TestCapInterface.DSS",
    "../../electricdss-tst/Test/LoadTest.DSS",
    "L!../../electricdss-tst/Test/IEEELineGeometry.dss",
    "L!../../electricdss-tst/Test/ODRegTest.dss",
    "L!../../electricdss-tst/Test/MultiCircuitTest.DSS",
    "L!../../electricdss-tst/Test/TriplexLineCodeCalc.DSS",
    "L!../../electricdss-tst/Test/PVSystemTest-Duty.dss",
    "L!../../electricdss-tst/Test/PVSystemTest.dss",
    "L!../../electricdss-tst/Test/REACTORTest.DSS",

    "../../electricdss-tst/Version7/Distrib/Examples/UPFC_Test/UPFC_test_3.dss",

    #"L!../../electricdss-tst/Test/Run_SimpleStorageTest.DSS", # Missing DLL?
    #"L!../../electricdss-tst/Test/Run_SimpleStorageTest-1ph.DSS", # Missing DLL?
    #"L!../../electricdss-tst/Test/Source012Test.dss", # Different encoding, skipping

    # 'Generator User Model IndMach012a Not Loaded.'
    #"L!../../electricdss-tst/Distrib/IEEETestCases/4wire-Delta/Kersting4wire_Lagging.dss",
    #"L!../../electricdss-tst/Distrib/IEEETestCases/4wire-Delta/Kersting4wire_Leading.dss",
    #"L!../../electricdss-tst/Distrib/IEEETestCases/4wire-Delta/Kersting4wireIndMotor.dss",

]

api_fields = {
    'ActiveCircuit': 'AllBusDistances,AllBusNames,AllBusVmag,AllBusVmagPu,AllBusVolts,AllElementLosses,AllElementNames,AllNodeDistances,AllNodeNames,LineLosses,Losses,Name,NumBuses,NumCktElements,NumNodes,ParentPDElement,SubstationLosses,SystemY,TotalPower,YCurrents,YNodeOrder,YNodeVarray', 
    
    'ActiveCircuit.Settings': 'LossRegs,UEregs,VoltageBases,AllowDuplicates,AutoBusList,CktModel,ControlTrace,EmergVmaxpu,EmergVminpu,LossWeight,NormVmaxpu,NormVminpu,PriceCurve,PriceSignal,Trapezoidal,UEweight,ZoneLock', 
    'ActiveCircuit.Solution': 'AddType,Algorithm,Capkvar,ControlActionsDone,ControlIterations,ControlMode,Converged,DefaultDaily,DefaultYearly,Frequency,GenMult,GenPF,GenkW,Hour,Iterations,LDCurve,LoadModel,LoadMult,MaxControlIterations,MaxIterations,Mode,ModeID,MostIterationsDone,Number,Random,Seconds,StepSize,SystemYChanged,Tolerance,Totaliterations,Year,dblHour,pctGrowth,IntervalHrs,MinIterations,Process_Time,Total_Time,Time_of_Step', 
    
    'ActiveCircuit.ActiveBus': 'Coorddefined,Cust_Duration,Cust_Interrupts,Distance,Int_Duration,Isc,Lambda,N_Customers,N_interrupts,Nodes,NumNodes,SectionID,TotalMiles,VLL,VMagAngle,Voc,Voltages,YscMatrix,Zsc0,Zsc1,ZscMatrix,kVBase,puVLL,puVmagAngle,puVoltages,x,y,SeqVoltages,CplxSeqVoltages', 
    'ActiveCircuit.Capacitors': 'States,AvailableSteps,NumSteps,kvar,kV,Name,IsDelta', 
    'ActiveCircuit.Generators': 'RegisterNames,RegisterValues,kvar,ForcedON,Model,Name,PF,Phases,Vmaxpu,Vminpu,idx,kV,kVArated,kW', 
    'ActiveCircuit.ISources': 'Amps,AngleDeg,Frequency,Name', 
    'ActiveCircuit.LineCodes': 'Cmatrix,Rmatrix,Xmatrix,C0,C1,EmergAmps,IsZ1Z0,Name,NormAmps,Phases,R0,R1,Units,X0,X1', 
    'ActiveCircuit.Lines': 'Cmatrix,Rmatrix,Xmatrix,Yprim,Bus1,Bus2,C0,C1,EmergAmps,Geometry,Length,LineCode,Name,NormAmps,NumCust,Phases,R0,R1,Rg,Rho,Spacing,TotalCust,Units,X0,X1,Xg', 
    'ActiveCircuit.Loads': 'AllocationFactor,CVRcurve,CVRvars,CVRwatts,Cfactor,Class,Growth,IsDelta,Model,Name,NumCust,PF,PctMean,PctStdDev,RelWeight,Rneut,Spectrum,Status,Vmaxpu,Vminemerg,Vminnorm,Vminpu,Xneut,Yearly,daily,duty,idx,kV,kW,kva,kvar,kwh,kwhdays,pctSeriesRL,xfkVA,ZIPV', 
    'ActiveCircuit.LoadShapes': 'Pmult,Qmult,TimeArray,HrInterval,MinInterval,Name,Npts,Pbase,Qbase,UseActual,Sinterval', 
    'ActiveCircuit.Meters': 'AllBranchesInZone,AllEndElements,RegisterNames,AvgRepairTime,Peakcurrent,RegisterValues,Totals,CountBranches,CountEndElements,CustInterrupts,DIFilesAreOpen,FaultRateXRepairHrs,MeteredElement,MeteredTerminal,Name,NumSectionBranches,NumSectionCustomers,NumSections,OCPDeviceType,SAIDI,SAIFI,SAIFIKW,SectSeqIdx,SectTotalCust,SeqListSize,SequenceIndex,SumBranchFltRates,TotalCustomers', 
    'ActiveCircuit.Monitors': 'dblFreq,dblHour,Element,FileName,Mode,Name,NumChannels,RecordSize,SampleCount,Terminal',
    'ActiveCircuit.Reclosers': 'RecloseIntervals,GroundInst,GroundTrip,MonitoredObj,MonitoredTerm,Name,NumFast,PhaseInst,PhaseTrip,Shots,SwitchedObj,SwitchedTerm,idx', 
    'ActiveCircuit.Transformers': 'IsDelta,MaxTap,MinTap,Name,NumTaps,NumWindings,R,Rneut,Tap,Wdg,XfmrCode,Xhl,Xht,Xlt,Xneut,kV,kva', 
    'ActiveCircuit.Vsources': 'AngleDeg,BasekV,Frequency,Name,Phases,pu', 
    'ActiveCircuit.XYCurves': 'Xarray,Yarray,Name,Npts,Xscale,Xshift,Yscale,Yshift,x,y',
}

ckt_elements = {
    'ActiveCircuit.Capacitors',
    'ActiveCircuit.Generators',
    'ActiveCircuit.ISources',
    'ActiveCircuit.LineCodes', 
    'ActiveCircuit.Lines',
    'ActiveCircuit.Loads',
    'ActiveCircuit.Meters',
    'ActiveCircuit.Monitors',
    'ActiveCircuit.Reclosers', 
    'ActiveCircuit.Transformers',
    'ActiveCircuit.Vsources',
}

single = {
    'ActiveCircuit',
    'ActiveCircuit.Settings',
    'ActiveCircuit.Solution'
}

for k in api_fields.keys():
    api_fields[k] = api_fields[k].split(',')
