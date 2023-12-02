try:
    from ._settings import BASE_DIR, WIN32
except ImportError:
    from _settings import BASE_DIR, WIN32


import numpy as np
np.set_printoptions(linewidth=999)
from dss import DSS
altdss = DSS.AltDSS

altdss(f'''
    redirect "{BASE_DIR}/Version8/Distrib/IEEETestCases/13Bus/IEEE13Nodeckt.dss"
    new energymeter.m element=Transformer.Sub
    solve
''')
m = altdss.EnergyMeter[1]
print('-' * 40)
print(m.ZonePCEs)
print(m.Loads)
print(m.Branches)
print('-' * 40)
print(m.ZonePCEs.to_list())
print(m.Loads.to_list())
print(np.sum(m.Loads.kW))
print(m.Branches.to_list())
print('-' * 40)
print(m.Branches.NumPhases())
print(m.Branches.TotalCustomers())
print('-' * 40)
for order, element in enumerate(m.Sequence):
    print(order, element)

print('-' * 40)
altdss(f'''
    redirect "{BASE_DIR}/Version8/Distrib/IEEETestCases/LVTestCaseNorthAmerican/Master.dss"
    redirect "{BASE_DIR}/Version8/Distrib/IEEETestCases/LVTestCaseNorthAmerican/network_protectors.dss"
''')
# new energymeter.m element={altdss.PDElement[1].FullName()}
# TypeError: 'PDElementBatch' object is not subscriptable

if len(altdss.EnergyMeter) == 0:
    print('Adding EM to >>>', altdss.PDElement.to_list()[1].FullName())
    altdss(f'''    
        new energymeter.m1 element={altdss.PDElement.to_list()[1].FullName()}
    ''')

altdss(f'''    
    solve
    RelCalc
''')
m = altdss.EnergyMeter[1]
#TODO: add error message in one of these to point that no relcalc was done beforehand
print(m.NumSections())
for section in m.Sections():
    print(section.as_dict())

print(m.Section(65).as_dict())

print(m.CAIDI)
print(m.SAIDI)
print(m.SAIFI)
print(m.SAIFIkW)
print(m.CustInterrupts)
