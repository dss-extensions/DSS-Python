try:
    from ._settings import BASE_DIR, WIN32
except ImportError:
    from _settings import BASE_DIR, WIN32


import numpy
numpy.set_printoptions(linewidth=999)
from dss import DSS
from dss.altdss.CircuitElement import CircuitElementMixin
from dss.altdss.PDElement import PDElementMixin
from dss.altdss.PCElement import PCElementMixin
from dss.altdss.LoadShape import LoadShapeObjMixin
from dss.altdss.Monitor import MonitorObjMixin
from dss.altdss.Transformer import TransformerObjMixin
from dss.altdss.EnergyMeter import EnergyMeterObjMixin

altdss = DSS.AltDSS

altdss(f'redirect "{BASE_DIR}/Version8/Distrib/IEEETestCases/13Bus/IEEE13Nodeckt.dss"')

for objset in [altdss.Element, altdss.PDElement, altdss.PCElement]:
    print(objset.IsIsolated())
    (objset.Currents())
    (objset.CurrentsMagAng())
    (objset.SeqCurrents())
    (objset.ComplexSeqCurrents())
    (objset.Voltages())
    (objset.VoltagesMagAng())
    (objset.SeqVoltages())
    (objset.ComplexSeqVoltages())
    print(objset.HasOCPDevice())
    print(objset.HasSwitchControl())
    print(objset.OCPDeviceType())
    print(objset.HasVoltControl())
    print(objset.Losses())
    print(objset.TotalPowers())
    print(objset.SeqPowers())
    print(objset.NumPhases())

altdss(f'redirect "{BASE_DIR}/Version8/Distrib/IEEETestCases/LVTestCase/Master.dss"')

errors = []

for cname in DSS.Classes:
    cls = getattr(altdss, cname)
    if not len(cls):
        continue

    print('=' * 40)
    c = cls[1]
    for k in dir(c):
        if k.lower() in c._cls_prop_idx:
            print(f'{c.FullName()}.{k}={getattr(c, k)}')

    # DSSObj
    print('Name', c.Name)
    print('FullName', c.FullName())

    if isinstance(c, CircuitElementMixin):
        print('DisplayName', c.DisplayName)
        for funcname in [
            'Handle',
            'NumConductors',
            'NumPhases',
            'NumTerminals',
            'NumControllers',
            'OCPDevice',
            'OCPDeviceType',
            'OCPDeviceIndex',
            'IsIsolated',
            'HasOCPDevice',
            'HasSwitchControl',
            'HasVoltControl',
            'NodeOrder',
            'NodeRef',
            'ComplexSeqVoltages',
            'ComplexSeqCurrents',
            'Currents',
            'Voltages',
            'Losses',
            'PhaseLosses',
            'Powers',
            'SeqVoltages',
            'Residuals',
            'YPrim',
            'VoltagesMagAng',
            'TotalPowers',
        ]:
            if isinstance(c, EnergyMeterObjMixin) and funcname == 'Losses':
                continue

            try:
                print(funcname, getattr(c, funcname)())
            except:
                errors.append((c.FullName(), funcname))
                continue


    if isinstance(c, PCElementMixin):
        for funcname in [
            'VariableNames',
            'VariableValues',
            'VariablesDict',
            'EnergyMeter',
            'EnergyMeterName',
        ]:
            try:
                print(funcname, getattr(c, funcname)())
            except:
                errors.append((c.FullName(), funcname))
                continue

    if isinstance(c, PDElementMixin):
        for funcname in [
            'EnergyMeter',
            'EnergyMeterName',
            'IsShunt',
            'AccumulatedL',
            'Lambda',
            'NumCustomers',
            'ParentPDElement',
            'TotalCustomers',
            'FromTerminal',
            'TotalMiles',
            'SectionID',
            'pctNorm',
            'pctEmerg',
        ]:
            try:
                print(funcname, getattr(c, funcname)())
            except:
                errors.append((c.FullName(), funcname))
                continue


    if isinstance(c, LoadShapeObjMixin):
        print('->' * 20)
        print(c, c.PMult, c.QMult, c.Hour)
        c.UseFloat32()
        print(c, c.PMult, c.QMult, c.Hour)
        print('<-' * 20)
        print()
        print()
        input()
        # c.UseFloat64()


    if isinstance(c, TransformerObjMixin):
        for funcname, *params in [
            ('WindingCurrents',),
            ('WindingVoltages', 1),
            ('LossesByType',),
        ]:
            try:
                print(funcname, getattr(c, funcname)(*params))
            except:
                errors.append((c.FullName(), funcname))
                continue


    if isinstance(c, MonitorObjMixin):
        for funcname in [
            'Header',
            'ByteStream',
            'FileName',
            'SampleCount',
            'NumChannels',
            'RecordSize',
            'dblFreq',
            'dblHour',
            'AsMatrix',
            'ToDataFrame'
        ]:
            try:
                print(funcname, getattr(c, funcname)())
            except:
                errors.append((c.FullName(), funcname))
                continue


    if isinstance(c, EnergyMeterObjMixin):
        print('CalcCurrent', getattr(c, 'CalcCurrent'))
        print('AllocFactors', getattr(c, 'AllocFactors'))
        for funcname in [
            'TotalCustomers',
            'NumEndElements',
            'NumSections',
            # 'Sections',
            # 'ZonePCEs',
            # 'EndElements',
            # 'Branches',
            # 'Loads',
            # 'Sequence',
        ]:
            try:
                print(funcname, getattr(c, funcname)())
            except:
                errors.append((c.FullName(), funcname))
                continue


print('=' * 40)
print('=' * 40)
print('ERRORS:', len(errors))
print('=' * 40)
for error in errors:
    print(*error)

print('=' * 40)
print('=' * 40)


# m1 = altdss.EnergyMeter[1]
# print(m1, m1.NumEndElements())
# print(m1, m1.CalcCurrent)