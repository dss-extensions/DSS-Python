'''
This package tries to implement the OpenDSSDirect.py API using dss_CAPI instead
of the official OpenDSS Direct DLL.
'''

from . import dss, utils
from .dss import *

dss.dss = dss

