'''A compatibility layer for DSS_CAPI that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .v7 import *
from .patch_dss_com import patch_dss_com

__version__ = '0.10.0'