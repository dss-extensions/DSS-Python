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
