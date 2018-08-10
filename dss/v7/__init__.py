'''A compatibility layer for DSS_CAPI_V7 that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .dss_capi import *
from ..enums import *
from .. import enums

__version__ = '0.9.8'
