'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base
import numpy as np

class IYMatrix(Base):
    __slots__ = []

    def GetCompressedYMatrix(self, factor=True):
        '''Return as (data, indices, indptr) that can fed into scipy.sparse.csc_matrix'''
        
        ffi = self._api_util.ffi
        
        nBus = ffi.new('uint32_t*')
        nBus[0] = 0
        nNz = ffi.new('uint32_t*')
        nNz[0] = 0

        ColPtr = ffi.new('int32_t**')
        RowIdxPtr = ffi.new('int32_t**')
        cValsPtr = ffi.new('double**')

        self._lib.YMatrix_GetCompressedYMatrix(factor, nBus, nNz, ColPtr, RowIdxPtr, cValsPtr)

        if not nBus[0] or not nNz[0]:
            res = None
        else:
            # return as (data, indices, indptr) that can fed into scipy.sparse.csc_matrix
            res = (
                np.fromstring(ffi.buffer(cValsPtr[0], nNz[0] * 16), dtype=np.complex),
                np.fromstring(ffi.buffer(RowIdxPtr[0], nNz[0] * 4), dtype=np.int32),
                np.fromstring(ffi.buffer(ColPtr[0], (nBus[0] + 1) * 4), dtype=np.int32)
            )

        self._lib.DSS_Dispose_PInteger(ColPtr)
        self._lib.DSS_Dispose_PInteger(RowIdxPtr)
        self._lib.DSS_Dispose_PDouble(cValsPtr)

        return res

    def ZeroInjCurr(self):
        self._lib.YMatrix_ZeroInjCurr()

    def GetSourceInjCurrents(self):
        self._lib.YMatrix_GetSourceInjCurrents()

    def GetPCInjCurr(self):
        self._lib.YMatrix_GetPCInjCurr()

    def BuildYMatrixD(self, BuildOps, AllocateVI):
        self._lib.YMatrix_BuildYMatrixD(BuildOps, AllocateVI)

    def AddInAuxCurrents(self, SType):
        self._lib.YMatrix_AddInAuxCurrents(SType)

    def GetIPointer(self):
        '''Get access to the internal Current pointer'''
        IvectorPtr = self._api_util.ffi.new('double**')
        self._lib.YMatrix_getIpointer(IvectorPtr)
        return IvectorPtr[0]

    def GetVPointer(self):
        '''Get access to the internal Voltage pointer'''
        VvectorPtr = self._api_util.ffi.new('double**')
        self._lib.YMatrix_getVpointer(VvectorPtr)
        return VvectorPtr[0]

    def SolveSystem(self, NodeV):
        if type(NodeV) is not np.ndarray:
            NodeV = np.array(NodeV)

        NodeV = self._api_util.ffi.cast("double *", NodeV.ctypes.data)
        NodeVPtr = self._api_util.ffi.new('double**')
        NodeVPtr[0] = NodeV
        result = self._lib.YMatrix_SolveSystem(NodeVPtr)
        return result

    @property
    def SystemYChanged(self):
        return self._lib.YMatrix_Get_SystemYChanged()

    @SystemYChanged.setter
    def SystemYChanged(self, value):
        self._lib.YMatrix_Set_SystemYChanged(value)
        self.CheckForError()

    @property
    def UseAuxCurrents(self):
        return self._lib.YMatrix_Get_UseAuxCurrents()

    @UseAuxCurrents.setter
    def UseAuxCurrents(self, value):
        self._lib.YMatrix_Set_UseAuxCurrents(value)
        self.CheckForError()

    # for better compatibility with OpenDSSDirect.py
    getYSparse = GetCompressedYMatrix

    def getI(self):
        '''Get the data from the internal Current pointer'''
        IvectorPtr = self.IVector()
        return self._api_util.ffi.unpack(IvectorPtr, self._lib.Circuit_Get_NumNodes() + 1)

    def getV(self):
        '''Get the data from the internal Voltage pointer'''
        VvectorPtr = self.VVector()
        return self._api_util.ffi.unpack(VvectorPtr, self._lib.Circuit_Get_NumNodes() + 1)

