'''DSS-Python provides a compatibility layer for DSS_CAPI that mimics the official OpenDSS COM interface, with various extensions and quality-of-life tweaks.

``dss`` is the main package for DSS Python. DSS Python is a compatibility layer for the DSS C-API library that mimics the official OpenDSS COM interface, with many extensions and a few limitations.

This module used to provide instances for the OpenDSS Version 7 implementation. 
As of 2022, most of the parallel-machine functions of EPRI's OpenDSS have been reimplemented using a different approach. Therefore the PM functions are available in the instances of this module too.
Besides the parallel-machine mechanisms, DSS Python also exposes the DSSContext mechanism provided by DSS Extensions. DSSContexts allow using multiple OpenDSS instances directly, including user-managed multi-threading, without using the internal OpenDSS actors.
'''

__version__ = '0.13.0.dev'

import os
from .patch_dss_com import patch_dss_com

if os.environ.get('DSS_EXTENSIONS_DEBUG', '') != '1':
    from ._dss_capi import ffi, lib
else:
    import warnings
    warnings.warn('Environment variable DSS_EXTENSIONS_DEBUG=1 is set: loading the debug version of the DSS C-API library')
    from ._dss_capid import ffi, lib

# Ensure this is called at least once. This was moved from 
# CffiApiUtil so we call it as soon as the DLL/so is loaded.
lib.DSS_Start(0)
_properties_mo = os.path.join(os.path.dirname(__file__), 'messages', 'properties-en-US.mo')
if os.path.exists(_properties_mo):
    lib.DSS_SetPropertiesMO(_properties_mo.encode())

from ._cffi_api_util import CffiApiUtil, set_case_insensitive_attributes, use_com_compat, DSSException
from . import enums
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
