'''A compatibility layer for DSS_CAPI that mimics the official OpenDSS COM interface.

``dss`` is the main package for DSS Python. DSS Python is a compatibility layer for the DSS C-API library that mimics the official OpenDSS COM interface, with many extensions and a few limitations.
'''
from __future__ import absolute_import
from .v7 import *
from .patch_dss_com import patch_dss_com

__version__ = '0.10.5'
