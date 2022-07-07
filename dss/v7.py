'''
This module use to provide instances for the OpenDSS Version 7 implementation. 
As of 2022, most of the parallel-machine functions of EPRI's OpenDSS have been reimplemented using a different approach. Therefore the PM functions are available in the instances of this module too.
Besides the parallel-machine mechanisms, DSS Python also exposes the DSSContext mechanism provided by DSS Extensions. DSSContexts allow using multiple OpenDSS instances directly, including user-managed multi-threading, without using the internal OpenDSS actors.
'''

import os
if os.environ.get('DSS_EXTENSIONS_DEBUG', '') != '1':
    from ._dss_capi import ffi, lib
else:
    import warnings
    warnings.warn('Environment variable DSS_EXTENSIONS_DEBUG=1 is set: loading the debug version of the DSS C-API library')
    from ._dss_capid import ffi, lib

from ._cffi_api_util import CffiApiUtil, use_com_compat, DSSException
from . import dss_capi_gr, dss_capi_ir, enums
from .enums import *

DssException = DSSException

# Bind to the FFI module instance for OpenDSS-v7
api_util = CffiApiUtil(ffi, lib) #: API utility functions and low-level access for the Version 7 library

if not hasattr(lib, 'ctx_New'):
    # Module was built without the context API
    prime_api_util = None
    DSS_GR = dss_capi_gr.IDSS(api_util) #: GR (Global Result) interface to the Version 7 library
    DSS_IR = dss_capi_ir.IDSS(api_util) #: IR (Immediate Result) interface to the Version 7 library
else:
    prime_api_util = CffiApiUtil(ffi, lib, lib.ctx_Get_Prime()) #: API utility functions and low-level access for the Version 7 library
    DSS_GR = dss_capi_gr.IDSS(prime_api_util) #: GR (Global Result) interface using the new DSSContext API
    DSS_IR = dss_capi_ir.IDSS(prime_api_util) #: IR (Immediate Result) interface using the new DSSContext API

DSS = DSS_GR #: Same as DSS_GR

#__all__ = ['DSS', 'DSS_GR', 'DSS_IR', 'api_util']