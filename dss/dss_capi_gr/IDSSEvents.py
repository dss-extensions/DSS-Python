'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2019 Paulo Meira
'''
from .._cffi_api_util import Base

class IDSSEvents(object): # Not implemented
    __slots__ = []
    
    def __init__(self, api_util):
        pass
