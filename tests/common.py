# Lines starting with "L!" indicate the file will be run line by line, 
# filtering interactive commands

new_examples = '''
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/NewFeatures/ConstantPF/SnapShot_PFP_kvarlimitation-PV2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/Daily_voltwatt_noOperation-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/Daily_voltwatt_noOperation_PF-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/Daily_voltwatt_PAVAILABLEPU-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/Daily_voltwatt_PAVAILABLEPU_pctPmpp60-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/Daily_voltwatt_PCTPMPPPU-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/Daily_voltwatt_PMPPPU-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/Daily_voltwatt_PMPPPU_pctPmpp60-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/Daily_voltwatt_PMPPPU_pctPmpp60_PF-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/Daily_voltwatt_PMPPPU_PF-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/Daily_voltwatt_PMPPPU_PFP_kVAlimitation-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/Daily_voltwatt_PMPPPU_PFP_kvarlimitation-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/Daily_voltwatt_PMPPPU_wattP_kVAlimitation-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_KVARATINGPU-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_noOperation_PF-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_PAVAILABLEPU-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_PAVAILABLEPU_PF-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_PCTPMPPPU-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_PCTPMPPPU_PF-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_pf-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_PMPPPU-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_PMPPPU_pctPmpp60_PF-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_PMPPPU_PF-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_PMPPPU_PFP_kVAlimitation-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_PMPPPU_PFP_kvarlimitation-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_PMPPPU_pmpp_greater_kva-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_PMPPPU_varP_kVAlimitation-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_PMPPPU_wattP_kVAlimitation-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_VW/Daily_voltvar_pctPmpp60-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_VW/Daily_VVVW_varAval_PMPPPU_kvarlimit-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_VW/Daily_VVVW_varMax_PMPPPU-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_VW/Daily_VVVW_varMax_PMPPPU_kVAlimitation_Ppriority-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_VW/Daily_VVVW_varMax_PMPPPU_kVAlimitation_Qpriority-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_VW/Daily_VVVW_varMax_PMPPPU_pctPmpp60-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_VW/Daily_VVVW_VWnooperation-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_VW/SnapShot_VVVW_varAval_PMPPPU_kvarlimit-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_VW/SnapShot_VVVW_varMax_PMPPPU-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_VW/SnapShot_VVVW_varMax_PMPPPU_kVAlimitation_Ppriority-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_VW/SnapShot_VVVW_varMax_PMPPPU_kVAlimitation_Qpriority-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_VW/SnapShot_VVVW_varMax_PMPPPU_pctPmpp60-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_VW/SnapShot_VVVW_VWnooperation-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/watt-pf_watt-var/dss/SnapShot_wattpf.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/watt-pf_watt-var/dss/SnapShot_wattvar.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/NewFeatures/ConstantPF/SnapShot_PFP_kVAlimitation-PV2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/NewFeatures/ConstantPF/SnapShot_PFP_pctPmpplimitation-PV2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/NewFeatures/ConstantPF/SnapShot_PFP_Standard-PV2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/NewFeatures/varCapability/PV_currentkvarLimit_kvar.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/NewFeatures/varCapability/PV_currentkvarLimit_kvarNEG.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/DRC/Daily_DRC_avg-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/CurrentkvarLimite/PV_currentkvarLimit_kvarNEG.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/CurrentkvarLimite/PV_currentkvarLimit_kvar.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/CurrentkvarLimite/PV_currentkvarLimit_VV.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/DRC/Daily_DRC_kVAlimitation_P-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/DRC/Daily_DRC_kVAlimitation_Q-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/DRC/Daily_DRC_kvarlimitation-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/DRC/Daily_DRC-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_noOperation-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_PAVAILABLEPU_pctPmpp60-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_PMPPPU_pctPmpp60-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_DRC/Daily_VVDRC-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_DRC/Daily_VVDRC_avg-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_DRC/Daily_VVDRC_kVAlimitation_P-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_DRC/Daily_VVDRC_kVAlimitation_Q-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_DRC/Daily_VVDRC_kvarlimitation-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_DRC/Daily_VVDRC_kvarlimitation-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_DRC/Daily_VVDRC_ravg-2.dss
../../electricdss-tst/Version8/Distrib/Examples/StorageTechNote/Example_9_1_Default/Storage_default.dss
../../electricdss-tst/Version8/Distrib/Examples/StorageTechNote/Example_9_2_Follow/Storage_follow.dss
../../electricdss-tst/Version8/Distrib/Examples/StorageTechNote/Example_9_3_Price/Storage_price.dss
../../electricdss-tst/Version8/Distrib/Examples/StorageTechNote/Example_9_4_External/Storage_external.dss
../../electricdss-tst/Version8/Distrib/Examples/StorageTechNote/Example_9_5_ReactivePower/Constantkvar_9_5_1/Storage_follow_kvar.dss
../../electricdss-tst/Version8/Distrib/Examples/StorageTechNote/Example_9_5_ReactivePower/ConstantPF_9_5_2/Storage_follow_PF.dss
L!../../electricdss-tst/Version8/Distrib/Examples/StorageControllerTechNote/Follow/FollowRun.dss
L!../../electricdss-tst/Version8/Distrib/Examples/StorageControllerTechNote/LoadShape/LoadShapeRun.dss
L!../../electricdss-tst/Version8/Distrib/Examples/StorageControllerTechNote/PeakShave/PeakShaveMonPhaseRun.dss
L!../../electricdss-tst/Version8/Distrib/Examples/StorageControllerTechNote/PeakShaveDch_PeakShaveLow_Ch/PeakShaveDch_PeakShaveLow_ChRun.dss
L!../../electricdss-tst/Version8/Distrib/Examples/StorageControllerTechNote/PeakShave/PeakShaveRun.dss
L!../../electricdss-tst/Version8/Distrib/Examples/StorageControllerTechNote/Schedule/ScheduleRun.dss
L!../../electricdss-tst/Version8/Distrib/Examples/StorageControllerTechNote/Support/SupportRun.dss
L!../../electricdss-tst/Version8/Distrib/Examples/StorageControllerTechNote/Time/TimeRun.dss
L!../../electricdss-tst/Version8/Distrib/Examples/Microgrid/Master.DSS
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/MonitoredVoltage/Local_voltage_2-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/MonitoredVoltage/Local_voltage_average-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/MonitoredVoltage/Local_voltage_max-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/MonitoredVoltage/Local_voltage_min-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/MonitoredVoltage/Mon_voltage_average-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/MonitoredVoltage/Mon_voltage_average_LL-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/MonitoredVoltage/Mon_voltage_average_Mix-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/MonitoredVoltage/Mon_voltage_MAX_Mix-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/MonitoredVoltage/Mon_voltage_MAX_Mix_avg-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/MonitoredVoltage/Mon_voltage_MAX_Mix_avg_VVDRC-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/MonitoredVoltage/Mon_voltage_MAX_Mix_ravg-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-var/Daily_voltvar_avg-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-var/Daily_voltvar_greater_kVA_ppriority-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-var/Daily_voltvar_greater_kVA_qpriority-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-var/Daily_voltvar_kvarlimit-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-var/Daily_voltvar_pctPmpp60-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-var/Daily_voltvar_ravg-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-var/Daily_voltvar_Standard-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-var/SnapShot_voltvar_greater_kvA_ppriority-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-var/SnapShot_voltvar_greater_kvA_qpriority-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-var/SnapShot_voltvar_pctPmpp60-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-var/SnapShot_voltvar_Standard-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-var/SnapShot_voltvar_Standard_varaval-2.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-var/SnapShot_voltvar_Standard_varaval_kvarlimitation-2.dss
'''.strip().split('\n')


test_filenames = [
    # This one is expected to have different results (C-API should be more precise)
    # "../../electricdss-tst/Distrib/IEEETestCases/DG_Protection/DG_Prot_Fdr.dss", 

    "../../electricdss-tst/Distrib/IEEETestCases/NEVTestCase/NEVMASTER.DSS",
    #"L!../../electricdss-tst/Test/Source012Test.dss",
    
    
    "L!../../electricdss-tst/Test/PVSystemTest.dss",
    "L!../../electricdss-tst/Distrib/IEEETestCases/123Bus/SolarRamp.DSS",
    "../../electricdss-tst/Test/IEEE13_CDPSM.dss",
    "../../electricdss-tst/Test/IEEE13_LineAndCableSpacing.dss",
    "L!../../electricdss-tst/Test/YgD-Test.dss", # NOTE: this one can be used to test ASLR issues and SET __COMPAT_LAYER=WIN7RTM
    "L!../../electricdss-tst/Distrib/IEEETestCases/123Bus/IEEE123Master.dss",
    "../../electricdss-tst/Distrib/IEEETestCases/37Bus/ieee37.dss",

    "../../electricdss-tst/Distrib/IEEETestCases/IEEE 30 Bus/Master.dss",
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
    "../../electricdss-tst/Test/TextTsCable750MCM.dss",
    "L!../../electricdss-tst/Test/TriplexLineCodeCalc.DSS",
    "../../electricdss-tst/Test/XYCurvetest.dss",
    "L!../../electricdss-tst/Test/PVSystemTestHarm.dss",
    "L!../../electricdss-tst/Test/IEEELineGeometry.dss",
    "L!../../electricdss-tst/Test/MultiCircuitTest.DSS",
    
    "../../electricdss-tst/Distrib/EPRITestCircuits/epri_dpv/M1/Master_NoPV.dss",
    "../../electricdss-tst/Distrib/EPRITestCircuits/epri_dpv/K1/Master_NoPV.dss",

    "../../electricdss-tst/Distrib/EPRITestCircuits/epri_dpv/J1/Master_withPV.dss",

    "../../electricdss-tst/Version8/Distrib/IEEETestCases/LVTestCaseNorthAmerican/Master.dss",
    
    "L!../../electricdss-tst/Test/Cable_constants.DSS",
    "L!../../electricdss-tst/Test/BundleDemo.DSS",
    "../../electricdss-tst/Test/IEEE13_SpacingGeometry.dss",
    "L!../../electricdss-tst/Test/TestDDRegulator.dss",
    "L!../../electricdss-tst/Test/TestAuto.dss",
    "L!../../electricdss-tst/Test/Stevenson.dss",
    "../../electricdss-tst/Test/Master_TestCapInterface.DSS",
    "../../electricdss-tst/Test/LoadTest.DSS",
    "L!../../electricdss-tst/Test/ODRegTest.dss",
    "L!../../electricdss-tst/Test/PVSystemTest-Duty.dss",
    "L!../../electricdss-tst/Test/REACTORTest.DSS",

    "../../electricdss-tst/Version7/Distrib/Examples/UPFC_Test/UPFC_test_3.dss",

    "../../electricdss-tst/Distrib/EPRITestCircuits/ckt5/Master_ckt5.dss",
    "../../electricdss-tst/Distrib/EPRITestCircuits/ckt7/Master_ckt7.dss",
    "../../electricdss-tst/Distrib/EPRITestCircuits/ckt24/Master_ckt24.dss",
    "../../electricdss-tst/Distrib/IEEETestCases/8500-Node/Master-unbal.dss",
    

    #"L!../../electricdss-tst/Test/Run_SimpleStorageTest.DSS", # Missing DLL?
    #"L!../../electricdss-tst/Test/Run_SimpleStorageTest-1ph.DSS", # Missing DLL?

    # 'Generator User Model IndMach012a Not Loaded.'
    #"L!../../electricdss-tst/Distrib/IEEETestCases/4wire-Delta/Kersting4wire_Lagging.dss",
    #"L!../../electricdss-tst/Distrib/IEEETestCases/4wire-Delta/Kersting4wire_Leading.dss",
    #"L!../../electricdss-tst/Distrib/IEEETestCases/4wire-Delta/Kersting4wireIndMotor.dss",

] + new_examples

errored = set('''
../../electricdss-tst/Distrib/EPRITestCircuits/ckt24/Master_ckt24.dss
../../electricdss-tst/Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/watt-pf_watt-var/dss/SnapShot_wattvar.dss
L!../../electricdss-tst/Version8/Distrib/Examples/StorageControllerTechNote/Follow/FollowRun.dss
L!../../electricdss-tst/Version8/Distrib/Examples/StorageControllerTechNote/LoadShape/LoadShapeRun.dss
L!../../electricdss-tst/Version8/Distrib/Examples/StorageControllerTechNote/PeakShave/PeakShaveMonPhaseRun.dss
L!../../electricdss-tst/Version8/Distrib/Examples/StorageControllerTechNote/PeakShaveDch_PeakShaveLow_Ch/PeakShaveDch_PeakShaveLow_ChRun.dss
L!../../electricdss-tst/Version8/Distrib/Examples/StorageControllerTechNote/PeakShave/PeakShaveRun.dss
L!../../electricdss-tst/Version8/Distrib/Examples/StorageControllerTechNote/Schedule/ScheduleRun.dss
L!../../electricdss-tst/Version8/Distrib/Examples/StorageControllerTechNote/Support/SupportRun.dss
L!../../electricdss-tst/Version8/Distrib/Examples/StorageControllerTechNote/Time/TimeRun.dss
'''.strip().split('\n'))

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
