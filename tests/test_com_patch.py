import os
old_dir = os.getcwd()
#com = win32com.client.Dispatch("OpenDSSEngine.DSS")

import win32com.client, dss
com = dss.patch_dss_com(win32com.client.gencache.EnsureDispatch("OpenDSSEngine.DSS"))

os.chdir(old_dir)
com.Text.Command = 'redirect ../../electricdss-tst/Version7/Distrib/IEEETestCases/13Bus/IEEE13Nodeckt.dss'

# Make sure our iterators work
for l in com.ActiveCircuit.Loads:
    print(l.Name, l.kva)
    
    
for b in com.ActiveCircuit.ActiveBus:
    print(b.Name, b.x, b.y)
    