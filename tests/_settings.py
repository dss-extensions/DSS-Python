import sys, os

WIN32 = (sys.platform == 'win32')
if os.path.exists('../../electricdss-tst/'):
    BASE_DIR = os.path.abspath('../../electricdss-tst/')
    ZIP_FN = os.path.abspath('data/13Bus.zip')
else:
    BASE_DIR = os.path.abspath('../electricdss-tst/')
    ZIP_FN = os.path.abspath('tests/data/13Bus.zip')

assert os.path.exists(BASE_DIR)

# Lines starting with "L!" indicate the file will be run line by line, 
# filtering interactive commands

# This one is expected to have different results (C-API should be more precise)
# "Distrib/IEEETestCases/DG_Protection/DG_Prot_Fdr.dss", 
#"L!Test/Source012Test.dss",
#"L!Test/Run_SimpleStorageTest.DSS", # Missing DLL?
#"L!Test/Run_SimpleStorageTest-1ph.DSS", # Missing DLL?

# 'Generator User Model IndMach012a Not Loaded.'
#"L!Distrib/IEEETestCases/4wire-Delta/Kersting4wire_Lagging.dss",
#"L!Distrib/IEEETestCases/4wire-Delta/Kersting4wire_Leading.dss",
#"L!Distrib/IEEETestCases/4wire-Delta/Kersting4wireIndMotor.dss",

test_filenames = '''
Test/CapControlFollow.dss
Test/CapacitorConfigs.dss
Test/ReactorConfigs.dss
L!Version8/Distrib/Examples/Dynamic_Expressions/Dynamic_KundurDynExp.dss
L!Test/AutoTrans/Auto1bus.dss
L!Test/AutoTrans/Auto3bus.dss
L!Test/AutoTrans/AutoAuto.dss
L!Test/AutoTrans/AutoHLT.dss
L!Version8/Distrib/Examples/DOCTechNote/1_1.dss
L!Version8/Distrib/Examples/DOCTechNote/1_2.dss
L!Version8/Distrib/Examples/DOCTechNote/2_1.dss
L!Version8/Distrib/Examples/DOCTechNote/2_2.dss
Version8/Distrib/IEEETestCases/NEVTestCase/NEVMASTER.DSS
L!Test/PVSystemTest.dss
L!Version8/Distrib/IEEETestCases/123Bus/SolarRamp.DSS
L!Version8/Distrib/IEEETestCases/123Bus/Run_IEEE123Bus.DSS
Test/IEEE13_CDPSM.dss
Test/IEEE13_LineAndCableSpacing.dss
L!Test/YgD-Test.dss
L!Version8/Distrib/IEEETestCases/123Bus/IEEE123Master.dss
Version8/Distrib/IEEETestCases/37Bus/ieee37.dss
Version8/Distrib/IEEETestCases/IEEE 30 Bus/Master.dss
Version8/Distrib/IEEETestCases/4Bus-DY-Bal/4Bus-DY-Bal.DSS
Version8/Distrib/IEEETestCases/4Bus-GrdYD-Bal/4Bus-GrdYD-Bal.DSS
Version8/Distrib/IEEETestCases/4Bus-OYOD-Bal/4Bus-OYOD-Bal.DSS
Version8/Distrib/IEEETestCases/4Bus-OYOD-UnBal/4bus-OYOD-UnBal.dss
Version8/Distrib/IEEETestCases/4Bus-YD-Bal/4Bus-YD-Bal.DSS
Version8/Distrib/IEEETestCases/4Bus-YY-Bal/4Bus-YY-Bal.DSS
Version8/Distrib/IEEETestCases/4Bus-YYD/YYD-Master.DSS
Version8/Distrib/IEEETestCases/13Bus/IEEE13Nodeckt.dss
Test/IEEE13_LineSpacing.dss
Test/IEEE13_LineGeometry.dss
Test/IEEE13_Assets.dss
L!Test/CableParameters.dss
Test/TextTsCable750MCM.dss
L!Test/TriplexLineCodeCalc.DSS
Test/XYCurvetest.dss
L!Test/PVSystemTestHarm.dss
L!Test/IEEELineGeometry.dss
L!Test/MultiCircuitTest.DSS
Version8/Distrib/EPRITestCircuits/epri_dpv/M1/Master_NoPV.dss
Version8/Distrib/EPRITestCircuits/epri_dpv/K1/Master_NoPV.dss
Version8/Distrib/EPRITestCircuits/epri_dpv/J1/Master_withPV.dss
Version8/Distrib/IEEETestCases/LVTestCase/Master.dss
Version8/Distrib/IEEETestCases/LVTestCaseNorthAmerican/Master.dss
Version8/Distrib/IEEETestCases/SecondaryTestCircuit_modified/Master.DSS
L!Test/Cable_constants.DSS
L!Test/BundleDemo.DSS
Test/IEEE13_SpacingGeometry.dss
L!Test/TestDDRegulator.dss
L!Test/TestAuto.dss
L!Test/Stevenson.dss
Test/Master_TestCapInterface.DSS
Test/LoadTest.DSS
L!Test/ODRegTest.dss
L!Test/PVSystemTest-Duty.dss
L!Test/REACTORTest.DSS
Version8/Distrib/Examples/UPFC_Test/UPFC_test_3.dss
Version8/Distrib/EPRITestCircuits/ckt5/Master_ckt5.dss
Version8/Distrib/EPRITestCircuits/ckt7/Master_ckt7.dss
Version8/Distrib/EPRITestCircuits/ckt24/master_ckt24.dss
Version8/Distrib/IEEETestCases/8500-Node/Master-unbal.dss
Version8/Distrib/Examples/Scripts/IEEE-TIA-LV Model/master_large.dss
Version8/Distrib/Examples/Scripts/IEEE-TIA-LV Model/master_large_1phase.dss
Version8/Distrib/Examples/Scripts/IEEE-TIA-LV Model/Split-Phase_IEEE_TIA.dss
Version8/Distrib/Examples/Scripts/IEEE-TIA-LV Model/master_small.dss
Version8/Distrib/Examples/Scripts/IEEE-TIA-LV Model/master_small_1phase.dss
Version8/Distrib/Examples/Scripts/59NRelayDemo.dss
L!Version8/Distrib/Examples/Microgrid/ISource/Master.DSS
L!Version8/Distrib/Examples/Microgrid/GridFormingInverter/GFM_IEEE123/Run_IEEE123Bus_GFMDaily.DSS
L!Version8/Distrib/Examples/Microgrid/GridFormingInverter/GFM_IEEE123/Run_IEEE123Bus_GFMDailySwapRef.DSS
Version8/Distrib/Examples/Microgrid/GridFormingInverter/GFM_IEEE123/Run_IEEE123Bus_GFMSnap-A.DSS
Version8/Distrib/Examples/Microgrid/GridFormingInverter/GFM_IEEE123/Run_IEEE123Bus_GFMSnap-B.DSS
Version8/Distrib/Examples/Microgrid/GridFormingInverter/GFM_IEEE123/Run_IEEE123Bus_GFMSnap-C.DSS
L!Version8/Distrib/Examples/Microgrid/GridFormingInverter/GFM_IEEE123/Run_IEEE123Bus_GFMSnap.DSS
L!Version8/Distrib/Examples/Microgrid/GridFormingInverter/GFM_IEEE123/Run_IEEE123Bus_GFMWholeDaily.DSS
L!Version8/Distrib/Examples/Microgrid/GridFormingInverter/GFM_IEEE8500/Run_8500Node_GFMDaily.dss
L!Version8/Distrib/Examples/Microgrid/GridFormingInverter/GFM_IEEE8500/Run_8500Node_GFMDailySmallerPV.dss
L!Version8/Distrib/Examples/Microgrid/GridFormingInverter/GFM_IEEE8500/Run_8500Node_GFMSnap.dss
L!Version8/Distrib/Examples/Microgrid/GridFormingInverter/GFM_IEEE8500/Run_8500Node_Unbal.dss
L!Version8/Distrib/IEEETestCases/123Bus/RevRegTest.dss
L!Version8/Distrib/Examples/IBRDynamics_Cases/GFM_IEEE123/Run_IEEE123Bus_GFMDaily.DSS
L!Version8/Distrib/Examples/IBRDynamics_Cases/GFM_IEEE123/Run_IEEE123Bus_GFMDaily_CannotPickUpLoad.DSS
L!Version8/Distrib/Examples/IBRDynamics_Cases/GFL_IEEE123/Run_IEEE123Bus_GFLDaily.DSS
L!Version8/Distrib/Examples/IBRDynamics_Cases/GFL_IEEE123/Run_IEEE123Bus_GFLDaily_DynExp.DSS
L!Version8/Distrib/Examples/HarmonicsVariableLoad/IEEE_519.DSS
Version8/Distrib/Examples/InverterModels/PVSystem/NewFeatures/ConstantPF/SnapShot_PFP_kvarlimitation-PV2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/Daily_voltwatt_noOperation-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/Daily_voltwatt_noOperation_PF-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/Daily_voltwatt_PAVAILABLEPU-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/Daily_voltwatt_PAVAILABLEPU_pctPmpp60-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/Daily_voltwatt_PCTPMPPPU-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/Daily_voltwatt_PMPPPU-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/Daily_voltwatt_PMPPPU_pctPmpp60-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/Daily_voltwatt_PMPPPU_pctPmpp60_PF-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/Daily_voltwatt_PMPPPU_PF-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/Daily_voltwatt_PMPPPU_PFP_kVAlimitation-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/Daily_voltwatt_PMPPPU_PFP_kvarlimitation-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/Daily_voltwatt_PMPPPU_wattP_kVAlimitation-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_KVARATINGPU-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_noOperation_PF-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_PAVAILABLEPU-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_PAVAILABLEPU_PF-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_PCTPMPPPU-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_PCTPMPPPU_PF-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_pf-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_PMPPPU-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_PMPPPU_pctPmpp60_PF-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_PMPPPU_PF-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_PMPPPU_PFP_kVAlimitation-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_PMPPPU_PFP_kvarlimitation-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_PMPPPU_pmpp_greater_kva-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_PMPPPU_varP_kVAlimitation-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_PMPPPU_wattP_kVAlimitation-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_VW/Daily_voltvar_pctPmpp60-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_VW/Daily_VVVW_varAval_PMPPPU_kvarlimit-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_VW/Daily_VVVW_varMax_PMPPPU-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_VW/Daily_VVVW_varMax_PMPPPU_kVAlimitation_Ppriority-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_VW/Daily_VVVW_varMax_PMPPPU_kVAlimitation_Qpriority-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_VW/Daily_VVVW_varMax_PMPPPU_pctPmpp60-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_VW/Daily_VVVW_VWnooperation-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_VW/SnapShot_VVVW_varAval_PMPPPU_kvarlimit-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_VW/SnapShot_VVVW_varMax_PMPPPU-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_VW/SnapShot_VVVW_varMax_PMPPPU_kVAlimitation_Ppriority-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_VW/SnapShot_VVVW_varMax_PMPPPU_kVAlimitation_Qpriority-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_VW/SnapShot_VVVW_varMax_PMPPPU_pctPmpp60-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_VW/SnapShot_VVVW_VWnooperation-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/watt-pf_watt-var/dss/SnapShot_wattpf.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/watt-pf_watt-var/dss/SnapShot_wattvar.dss
Version8/Distrib/Examples/InverterModels/PVSystem/NewFeatures/ConstantPF/SnapShot_PFP_kVAlimitation-PV2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/NewFeatures/ConstantPF/SnapShot_PFP_pctPmpplimitation-PV2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/NewFeatures/ConstantPF/SnapShot_PFP_Standard-PV2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/NewFeatures/varCapability/PV_currentkvarLimit_kvar.dss
Version8/Distrib/Examples/InverterModels/PVSystem/NewFeatures/varCapability/PV_currentkvarLimit_kvarNEG.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/DRC/Daily_DRC_avg-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/CurrentkvarLimite/PV_currentkvarLimit_kvarNEG.dss
Version8/Distrib/Examples/InverterModels/PVSystem/CurrentkvarLimite/PV_currentkvarLimit_kvar.dss
Version8/Distrib/Examples/InverterModels/PVSystem/CurrentkvarLimite/PV_currentkvarLimit_VV.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/DRC/Daily_DRC_kVAlimitation_P-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/DRC/Daily_DRC_kVAlimitation_Q-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/DRC/Daily_DRC_kvarlimitation-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/DRC/Daily_DRC-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_noOperation-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_PAVAILABLEPU_pctPmpp60-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-watt/SnapShot_voltwatt_PMPPPU_pctPmpp60-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_DRC/Daily_VVDRC-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_DRC/Daily_VVDRC_avg-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_DRC/Daily_VVDRC_kVAlimitation_P-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_DRC/Daily_VVDRC_kVAlimitation_Q-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_DRC/Daily_VVDRC_kvarlimitation-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_DRC/Daily_VVDRC_ravg-2.dss
Version8/Distrib/Examples/StorageTechNote/Example_9_1_Default/Storage_default.dss
Version8/Distrib/Examples/StorageTechNote/Example_9_2_Follow/Storage_follow.dss
Version8/Distrib/Examples/StorageTechNote/Example_9_3_Price/Storage_price.dss
Version8/Distrib/Examples/StorageTechNote/Example_9_4_External/Storage_external.dss
Version8/Distrib/Examples/StorageTechNote/Example_9_5_ReactivePower/Constantkvar_9_5_1/Storage_follow_kvar.dss
Version8/Distrib/Examples/StorageTechNote/Example_9_5_ReactivePower/ConstantPF_9_5_2/Storage_follow_PF.dss
L!Version8/Distrib/Examples/StorageControllerTechNote/Follow/FollowRun.dss
L!Version8/Distrib/Examples/StorageControllerTechNote/LoadShape/LoadShapeRun.dss
L!Version8/Distrib/Examples/StorageControllerTechNote/PeakShave/PeakShaveMonPhaseRun.dss
L!Version8/Distrib/Examples/StorageControllerTechNote/PeakShaveDch_PeakShaveLow_Ch/PeakShaveDch_PeakShaveLow_ChRun.dss
L!Version8/Distrib/Examples/StorageControllerTechNote/PeakShave/PeakShaveRun.dss
L!Version8/Distrib/Examples/StorageControllerTechNote/Schedule/ScheduleRun.dss
L!Version8/Distrib/Examples/StorageControllerTechNote/Support/SupportRun.dss
L!Version8/Distrib/Examples/StorageControllerTechNote/Time/TimeRun.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/MonitoredVoltage/Local_voltage_2-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/MonitoredVoltage/Local_voltage_average-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/MonitoredVoltage/Local_voltage_max-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/MonitoredVoltage/Local_voltage_min-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/MonitoredVoltage/Mon_voltage_average-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/MonitoredVoltage/Mon_voltage_average_LL-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/MonitoredVoltage/Mon_voltage_average_Mix-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/MonitoredVoltage/Mon_voltage_MAX_Mix-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/MonitoredVoltage/Mon_voltage_MAX_Mix_avg-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/MonitoredVoltage/Mon_voltage_MAX_Mix_avg_VVDRC-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/MonitoredVoltage/Mon_voltage_MAX_Mix_ravg-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-var/Daily_voltvar_avg-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-var/Daily_voltvar_greater_kVA_ppriority-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-var/Daily_voltvar_greater_kVA_qpriority-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-var/Daily_voltvar_kvarlimit-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-var/Daily_voltvar_pctPmpp60-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-var/Daily_voltvar_ravg-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-var/Daily_voltvar_Standard-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-var/SnapShot_voltvar_greater_kvA_ppriority-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-var/SnapShot_voltvar_greater_kvA_qpriority-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-var/SnapShot_voltvar_pctPmpp60-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-var/SnapShot_voltvar_Standard-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-var/SnapShot_voltvar_Standard_varaval-2.dss
Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/volt-var/SnapShot_voltvar_Standard_varaval_kvarlimitation-2.dss
L!Version8/Distrib/Examples/Scripts/Storage-Quasi-Static-Example/Run_Demo1.dss
L!Version8/Distrib/IEEETestCases/123Bus/Run_YearlySim.dss
Version8/Distrib/Examples/GICExample/GIC_Example.dss
'''.strip().split('\n')

cimxml_test_filenames = '''
Version8/Distrib/Examples/CIM/IEEE13_Assets.dss
Version8/Distrib/Examples/CIM/IEEE13_CDPSM.dss
'''.strip().split('\n')
