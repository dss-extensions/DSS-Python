import faulthandler
faulthandler.disable()

import sys, os, warnings
from time import perf_counter
import dss
from dss import IDSS, DSSException, SparseSolverOptions, SolveModes, set_case_insensitive_attributes
import numpy as np
import pytest
try:
    import scipy.sparse as sp
except:
    sp = None
    


try:
    from ._settings import BASE_DIR, WIN32, ZIP_FN, DSS
except ImportError:
    from _settings import BASE_DIR, WIN32, ZIP_FN, DSS

faulthandler.enable()

def setup_function():
    DSS.ClearAll()

    DSS.AllowForms = False
    DSS.ActiveCircuit.Settings.AdvancedTypes = False

    if not DSS.is_oddie():
        DSS.ActiveCircuit.Settings.CompatFlags = 0
        DSS.AllowEditor = False
        DSS.AllowChangeDir = True
        DSS.ActiveCircuit.Settings.COMErrorResults = False

    DSS.Error.UseExceptions = True
    DSS.Text.Command = 'set DefaultBaseFreq=60'


def test_rxmatrix():
    DSS.ClearAll()
    DSS.NewCircuit('test_rxmatrix')
    for r_or_x in 'rx':
        DSS.Text.Command = f'new Line.ourline{r_or_x} phases=3'
        
        if not DSS.is_oddie(): # This works but pops up an annoying window with the Delphi ODD.DLL
            DSS.Text.Command = f'~ {r_or_x}matrix=[1,2,3]'
        
        DSS.Text.Command = f'~ {r_or_x}matrix=[1,2,3 | 4,5,6 | 7,8,9]'
        DSS.Text.Command = f'? Line.ourline{r_or_x}.{r_or_x}matrix'
        assert DSS.Text.Result == '[1 |4 5 |7 8 9 ]' 

        if not DSS.is_oddie(): # This works but pops up an annoying window with the Delphi ODD.DLL
            with pytest.raises(DSSException):
                DSS.Text.Command = f'~ {r_or_x}matrix=[10,20,30,40]'

        DSS.Text.Command = f'? Line.ourline{r_or_x}.{r_or_x}matrix'
        assert DSS.Text.Result == '[1 |4 5 |7 8 9 ]'

        if not DSS.is_oddie(): # This would crash the official Delphi ODD.DLL
            with pytest.raises(DSSException):
                DSS.Text.Command = f'~ {r_or_x}matrix={list(range(1000))}'

            with pytest.raises(DSSException):
                DSS.Text.Command = f'~ {r_or_x}matrix=[1,2,3 | 4,5,6,7]'

        DSS.Text.Command = f'~ {r_or_x}matrix=[11 | 22, 33 | 44, 55, 66]'
        DSS.Text.Command = f'? Line.ourline{r_or_x}.{r_or_x}matrix'
        assert DSS.Text.Result == '[11 |22 33 |44 55 66 ]'


def test_create_no_circuit():
    general_classes = (
        'CNData', 'DynamicExp', 'GrowthShape', 'LineSpacing', 'LoadShape', 'PriceShape', 'Spectrum', 
        'TShape', 'TCC_Curve', 'TSData', 'XfmrCode', 'XYcurve', 'WireData',
    )
    for cls in DSS.Classes:
        if cls == 'Solution':
            continue # Added for OpenDSSDirect.DLL

        DSS.ClearAll()

        if cls in general_classes:
            if cls == 'GrowthShape' and DSS.is_oddie():
                continue

            DSS.Text.Command = f'new {cls}.test'
        else:
            if not DSS.is_oddie():
                with pytest.raises(DSSException, match=r'\(#(279)|(265)\)'):
                    DSS.Text.Command = f'new {cls}.test'
                    pytest.fail(f'Object of type "{cls}" was allowed to be created without a circuit!')

    DSS.Text.Command = 'new circuit.test'


def test_create_with_circuit():
    if DSS.is_oddie():
        pytest.skip("This test is dangerous with EPRI's OpenDSS and OpenDSS-C. Skipping.")
        return

    for cls in DSS.Classes:
        DSS.ClearAll()
        DSS.NewCircuit(f'test_{cls}')
        if cls in ('CapControl', 'RegControl', 'GenDispatcher', 'StorageController', 'Relay', 'Fuse', 'SwtControl', 'ESPVLControl', 'GICsource', 'FMonitor', 'Generic5'):
            with pytest.raises(DSSException):
                DSS.Text.Command = f'new {cls}.test{cls}'

            DSS.Text.Command = f'new Transformer.testtr'
            DSS.Text.Command = f'new Capacitor.testcap'
            if cls == 'RegControl':
                DSS.Text.Command = f'new {cls}.test{cls}2 transformer=testtr'
            elif cls == 'CapControl':
                DSS.Text.Command = f'new {cls}.test{cls}2 element=transformer.testtr capacitor=testcap'
            elif cls == 'GenDispatcher':
                DSS.Text.Command = f'new {cls}.test{cls}2 element=transformer.testtr'
            elif cls in ('FMonitor', 'Generic5'):
                # Skip these for now... they are disabled by default
                # DSS.Text.Command = f'new {cls}.test{cls}2 element=transformer.testtr'
                pass

        else:
            DSS.Text.Command = f'new {cls}.test{cls}'


def test_ymatrix_csc():
    # We accidentally left a np.complex in the ymatrix code before, 
    # so let's always check if it's working now

    DSS.Text.Command = f'redirect "{BASE_DIR}/Version8/Distrib/IEEETestCases/13Bus/IEEE13Nodeckt.dss"'
    DSS.ActiveCircuit.Solution.Solve()
    DSS.ActiveCircuit.Settings.AdvancedTypes = True
    ydense = DSS.ActiveCircuit.SystemY
    if sp is not None:
        assert np.all(ydense == sp.csc_matrix(DSS.YMatrix.GetCompressedYMatrix()))
    else:
        pytest.skip("SciPy is not installed, skipping sparse-dense comparison.")
