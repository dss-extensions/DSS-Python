import sys, os
from time import perf_counter
import dss
from dss import DSS, IDSS, DSSException, SparseSolverOptions, SolveModes, set_case_insensitive_attributes
import numpy as np
import pytest

WIN32 = (sys.platform == 'win32')
DSS.AllowEditor = False
if os.path.exists('../../electricdss-tst/'):
    BASE_DIR = os.path.abspath('../../electricdss-tst/')
    ZIP_FN = os.path.abspath('data/13Bus.zip')
else:
    BASE_DIR = os.path.abspath('../electricdss-tst/')
    ZIP_FN = os.path.abspath('tests/data/13Bus.zip')


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

