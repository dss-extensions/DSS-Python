'''
This module used to present an instance for the OpenDSS Version 8 implementation. It was based on the official parallel-machine version, which allow creating multiple solvers (actors) in a single process. The mechanism is being reword in DSS C-API, the library used by DSS_Python to implement OpenDSS, to reproduce a stable version in the future.
'''
from __future__ import absolute_import
from .v7 import *
import warnings

warnings.warn('This module (dss.v8) is deprecated. Most parallel-machine functions are planned to be integrated in a future version.')

