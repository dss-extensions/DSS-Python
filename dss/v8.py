'''
This module presents instances for the OpenDSS Version 8 implementation. It is the parallel-machine version, which allow creating multiple solvers (actors) in a single process. Compared to Version 7, it is less tested, but feel free to open an issue on GitHub if you find any problem.
'''
from __future__ import absolute_import
from ._dss_capi_v8 import ffi, lib
from ._cffi_api_util import CffiApiUtil, use_com_compat, DssException
from . import dss_capi_gr, dss_capi_ir, enums
from .enums import *

# Bind to the FFI module instance for OpenDSS-v8
api_util = CffiApiUtil(ffi, lib) #: API utility functions and low-level access for the Version 8 library

DSS_GR = dss_capi_gr.IDSS(api_util) #: GR (Global Result) interface to the Version 8 library
DSS_IR = dss_capi_ir.IDSS(api_util) #: IR (Immediate Result) interface to the Version 8 library
DSS = DSS_GR #: Same as DSS_GR

#__all__ = ['DSS', 'DSS_GR', 'DSS_IR', 'api_util']