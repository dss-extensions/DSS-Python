'''``dss`` is the main package for DSS-Python. DSS-Python is a compatibility layer for the DSS C-API library that mimics the official OpenDSS COM interface, with many extensions and a few limitations.

This module used to provide instances for the OpenDSS Version 7 implementation. 
As of 2022, most of the parallel-machine functions of EPRI's OpenDSS have been reimplemented using a different approach. Therefore the PM functions are available in the instances of this module too.
Besides the parallel-machine mechanisms, DSS-Python also exposes the DSSContext mechanism provided by DSS-Extensions. DSSContexts allow using multiple OpenDSS instances directly, including user-managed multi-threading, without using the internal OpenDSS actors.

Starting on April 2023, our CFFI extension modules and DSS C-API binaries moved to `dss_python_backend` and are just consumed here.

In January 2024, the code based on our new low-level API extensions, Obj and Alt, move to the new package [AltDSS-Python](https://dss-extensions.org/AltDSS-Python/) (`altdss` on PyPI and in Python).
'''

import os
from .patch_dss_com import patch_dss_com
from dss_python_backend import ffi, lib
_properties_mo = os.path.join(os.path.dirname(__file__), 'messages', 'properties-en-US.mo')
if os.path.exists(_properties_mo):
    lib.DSS_SetPropertiesMO(_properties_mo.encode())

from ._cffi_api_util import CffiApiUtil, DSSException, set_case_insensitive_attributes
# from .altdss import Edit
from .IDSS import IDSS
from .enums import *

DssException = DSSException

# Bind to the FFI module instance for OpenDSS-v7
api_util: CffiApiUtil = CffiApiUtil(ffi, lib) #: API utility functions and low-level access to the classic API

if not hasattr(lib, 'ctx_New'):
    # Module was built without the context API
    prime_api_util = None
    DSS_GR: IDSS = IDSS(api_util) #: GR (Global Result) interface
else:
    prime_api_util = CffiApiUtil(ffi, lib, lib.ctx_Get_Prime()) #: API utility functions and low-level access for DSSContext API
    DSS_GR: IDSS = IDSS(prime_api_util) #: GR (Global Result) interface using the new DSSContext API
    
DSS_IR: IDSS = DSS_GR #: IR was removed in DSS-Python v0.13.x, we'll keep mapping it to DSS_GR for this version

# Added "dss" for v0.12+ (feedback from some users)
dss: IDSS
DSS: IDSS
dss = DSS = DSS_GR #: Same as DSS_GR

try:
    from ._version import __version__
except:
    __version__ = '0.0dev'

__all__ = ['dss', 'DSS', 'DSS_GR', 'prime_api_util', 'api_util', 'DSSException', 'patch_dss_com', 'set_case_insensitive_attributes', 'enums', 'Edit']