'''A compatibility layer for DSS C-API V8 that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from ._dss_capi_v8 import ffi, lib
from ._cffi_api_util import CffiApiUtil, use_com_compat
from . import dss_capi_gr, dss_capi_ir, enums
from .enums import *

# Bind to the FFI module instance for OpenDSS-v8
api_util = CffiApiUtil(ffi, lib)

DSS_GR = dss_capi_gr.IDSS(api_util)
DSS_IR = dss_capi_ir.IDSS(api_util)
DSS = DSS_GR
