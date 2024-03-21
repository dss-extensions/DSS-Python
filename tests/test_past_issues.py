import sys, os
from time import perf_counter
import dss
from dss import DSS, IDSS, DSSException, SparseSolverOptions, SolveModes, set_case_insensitive_attributes
import numpy as np
import pytest
import scipy.sparse as sp

try:
    from ._settings import BASE_DIR, WIN32, ZIP_FN, DSS
except ImportError:
    from _settings import BASE_DIR, WIN32, ZIP_FN, DSS

def setup_function():
    DSS.ClearAll()
    DSS.AllowForms = False
    if not DSS._api_util._is_odd:
        DSS.AllowEditor = False
        DSS.AdvancedTypes = False
        DSS.AllowChangeDir = True
        DSS.COMErrorResults = True # TODO: change to False
        DSS.CompatFlags = 0


def test_rxmatrix():
    DSS.ClearAll()
    DSS.NewCircuit('test_rxmatrix')
    for r_or_x in 'rx':
        DSS.Text.Command = f'new Line.ourline{r_or_x} phases=3'
        DSS.Text.Command = f'~ {r_or_x}matrix=[1,2,3]'
        DSS.Text.Command = f'~ {r_or_x}matrix=[1,2,3 | 4,5,6 | 7,8,9]'
        DSS.Text.Command = f'? Line.ourline{r_or_x}.{r_or_x}matrix'
        assert DSS.Text.Result == '[1 |4 5 |7 8 9 ]' 

        with pytest.raises(DSSException):
            DSS.Text.Command = f'~ {r_or_x}matrix=[10,20,30,40]'

        DSS.Text.Command = f'? Line.ourline{r_or_x}.{r_or_x}matrix'
        assert DSS.Text.Result == '[1 |4 5 |7 8 9 ]'

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
        DSS.ClearAll()

        if cls in general_classes:
            DSS.Text.Command = f'new {cls}.test'
        else:
            with pytest.raises(DSSException, match=r'\(#(279)|(265)\)'):
                DSS.Text.Command = f'new {cls}.test'
                pytest.fail(f'Object of type "{cls}" was allowed to be created without a circuit!')


def test_create_with_circuit():
    for cls in DSS.Classes:
        DSS.ClearAll()
        DSS.NewCircuit(f'test_{cls}')
        if cls in ('CapControl', 'RegControl', 'GenDispatcher', 'StorageController', 'Relay', 'Fuse', 'SwtControl', 'ESPVLControl', 'GICsource'):
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

        else:
            DSS.Text.Command = f'new {cls}.test{cls}'


def test_ymatrix_csc():
    # We accidentally left a np.complex in the ymatrix code before, 
    # so let's always check if it's working now

    DSS.Text.Command = f'redirect "{BASE_DIR}/Version8/Distrib/IEEETestCases/13Bus/IEEE13Nodeckt.dss"'
    DSS.ActiveCircuit.Solution.Solve()
    DSS.AdvancedTypes = True
    assert np.all(DSS.ActiveCircuit.SystemY == sp.csc_matrix(DSS.YMatrix.GetCompressedYMatrix()))
