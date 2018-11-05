'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class IDSSEvents(object): # Not implemented
    __slots__ = []
    
    def __init__(self, api_util):
        pass
