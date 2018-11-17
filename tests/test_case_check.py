from dss import DSS, use_com_compat

DSS.Text.Command = 'redirect ../../electricdss-tst/Version7/Distrib/IEEETestCases/13Bus/IEEE13Nodeckt.dss'

# Test if we get errors by default
got_error = False
try:
    for l in DSS.ActiveCircuit.Loads:
        name = l.nAme
except AttributeError:
    got_error = True

assert got_error


# Test mixed case
use_com_compat(True, False)
got_error = False
try:
    for l in DSS.ActiveCircuit.Loads:
        name = l.namE
except AttributeError:
    got_error = True

assert not got_error


# Test warnings
use_com_compat(True, True)
got_error = False
try:
    for l in DSS.ActiveCircuit.Loads:
        name = l.name
except AttributeError:
    got_error = True

assert not got_error

got_error = False
try:
    for b in DSS.ActiveCircuit.Buses:
        votages = b.PUVoltages
        
except AttributeError:
    got_error = True

assert not got_error


# Make sure we can disable the case magic
use_com_compat(False, True)
got_error = False
try:
    for l in DSS.ActiveCircuit.Loads:
        name = l.name
except AttributeError:
    got_error = True

assert got_error

