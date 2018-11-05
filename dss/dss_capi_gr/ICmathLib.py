'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class ICmathLib(Base):
    __slots__ = []

    def cabs(self, realpart, imagpart):
        '''(read-only) Return abs value of complex number given in real and imag doubles'''
        return self._lib.CmathLib_Get_cabs(realpart, imagpart)

    def cdang(self, RealPart, ImagPart):
        '''(read-only) Returns the angle, in degrees, of a complex number specified as two doubles: Realpart and imagpart.'''
        return self._lib.CmathLib_Get_cdang(RealPart, ImagPart)

    def cdiv(self, a1, b1, a2, b2):
        '''(read-only) Divide two complex number: (a1, b1)/(a2, b2). Returns array of two doubles representing complex result.'''
        self._lib.CmathLib_Get_cdiv_GR(a1, b1, a2, b2)
        return self._get_float64_gr_array()

    def cmplx(self, RealPart, ImagPart):
        '''(read-only) Convert real and imaginary doubles to Array of doubles'''
        self._lib.CmathLib_Get_cmplx_GR(RealPart, ImagPart)
        return self._get_float64_gr_array()

    def cmul(self, a1, b1, a2, b2):
        '''(read-only) Multiply two complex numbers: (a1, b1) * (a2, b2). Returns result as a array of two doubles.'''
        self._lib.CmathLib_Get_cmul_GR(a1, b1, a2, b2)
        return self._get_float64_gr_array()

    def ctopolardeg(self, RealPart, ImagPart):
        '''(read-only) Convert complex number to magnitude and angle, degrees. Returns array of two doubles.'''
        self._lib.CmathLib_Get_ctopolardeg_GR(RealPart, ImagPart)
        return self._get_float64_gr_array()

    def pdegtocomplex(self, magnitude, angle):
        '''(read-only) Convert magnitude, angle in degrees to a complex number. Returns Array of two doubles.'''
        self._lib.CmathLib_Get_pdegtocomplex_GR(magnitude, angle)
        return self._get_float64_gr_array()
