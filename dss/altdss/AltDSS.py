from .._cffi_api_util import DSSException, CffiApiUtil
from .Bus import IBuses
from ..ICtrlQueue import ICtrlQueue
from ..IParallel import IParallel
from ..IPDElements import IPDElements
from ..IReduceCkt import IReduceCkt
from ..ISettings import ISettings
from ..ISolution import ISolution
from ..ITopology import ITopology
from ..IYMatrix import IYMatrix
from ..IZIP import IZIP
from ..IText import IText


class AltDSSCircuitMixin:
    __slots__ = [
        'Buses',
        'CtrlQueue',
        'Parallel',
        'PDElements',
        'ReduceCkt',
        'Settings',
        'Solution',
        'Topology',
        'Text',
        'Elements',
        'PCElements',
        'PDElements',
    ]
   
    Buses: IBuses # TODO: new bus API implementation
    CtrlQueue: ICtrlQueue
    Parallel: IParallel
    ReduceCkt: IReduceCkt
    Settings: ISettings
    Solution: ISolution
    Topology: ITopology
    YMatrix: IYMatrix
    Elements: CircuitElementBatch
    PCElements: PCElementBatch
    PDElements: PDElementBatch

    def __init__(self):
        self.Buses = IBuses(self._api_util)
        self.CtrlQueue = ICtrlQueue(self._api_util)
        self.Parallel = IParallel(self._api_util)
        self.ReduceCkt = IReduceCkt(self._api_util)
        self.Settings = ISettings(self._api_util)
        self.Solution = ISolution(self._api_util)
        self.Topology = ITopology(self._api_util)
        self.ZIP = IZIP(self._api_util)
        self.Text = IText(self._api_util)
        self.YMatrix = IYMatrix(self._api_util)

    # def Elements(self) -> NonUniformBatch:
    #     '''Batch of all circuit elements, mapped to Python.'''
    #     return self._get_string_array(self._lib.Alt_Circuit_Get_ElementList) #TODO

    # def PCElements(self) -> NonUniformBatch:
    #     '''Batch of all PC elements, mapped to Python.'''
    #     return self._get_string_array(self._lib.Alt_Circuit_Get_PCElementList) #TODO

    # def PDElements(self) -> NonUniformBatch:
    #     '''Batch of all PD elements, mapped to Python.'''
    #     return self._get_string_array(self._lib.Alt_Circuit_Get_PDElementList) #TODO

        '''
        IError
        IDSS
        IDSSEvents
        '''

    def DisableElement(self, name: AnyStr):
        if type(name) is not bytes:
            name = name.encode(self._api_util.codec)

        self._check_for_error(self._lib.Circuit_Disable(name))

    def EnableElement(self, name: AnyStr):
        if type(name) is not bytes:
            name = name.encode(self._api_util.codec)

        self._check_for_error(self._lib.Circuit_Enable(name))

    def NodeDistancesByPhase(self, Phase: int) -> Float64Array:
        '''Returns an array of doubles representing the distances to parent EnergyMeter. Sequence of array corresponds to other node ByPhase properties.'''
        self._check_for_error(self._lib.Circuit_Get_AllNodeDistancesByPhase_GR(Phase))
        return self._get_float64_gr_array()

    def NodeNamesByPhase(self, Phase: int) -> List[str]:
        '''Return array of strings of the node names for the By Phase criteria. Sequence corresponds to other ByPhase properties.'''
        return self._check_for_error(self._get_string_array(self._lib.Circuit_Get_AllNodeNamesByPhase, Phase))

    def NodeVmagByPhase(self, Phase: int) -> Float64Array:
        '''Returns Array of doubles represent voltage magnitudes for nodes on the specified phase.'''
        self._check_for_error(self._lib.Circuit_Get_AllNodeVmagByPhase_GR(Phase))
        return self._get_float64_gr_array()

    def NodeVmagPUByPhase(self, Phase: int) -> Float64Array:
        '''Returns array of per unit voltage magnitudes for each node by phase'''
        self._check_for_error(self._lib.Circuit_Get_AllNodeVmagPUByPhase_GR(Phase))
        return self._get_float64_gr_array()

    def BusDistances(self) -> Float64Array:
        '''Returns distance from each bus to parent EnergyMeter. Corresponds to sequence in AllBusNames.'''
        self._check_for_error(self._lib.Circuit_Get_AllBusDistances_GR())
        return self._get_float64_gr_array()

    def BusNames(self) -> List[str]:
        '''Array of strings containing names of all buses in circuit (see AllNodeNames).'''
        return self._check_for_error(self._get_string_array(self._lib.Circuit_Get_AllBusNames))

    def BusVmag(self) -> Float64Array:
        '''Array of magnitudes (doubles) of voltages at all buses'''
        self._check_for_error(self._lib.Circuit_Get_AllBusVmag_GR())
        return self._get_float64_gr_array()

    def BusVmagPu(self) -> Float64Array:
        '''Double Array of all bus voltages (each node) magnitudes in Per unit'''
        self._check_for_error(self._lib.Circuit_Get_AllBusVmagPu_GR())
        return self._get_float64_gr_array()

    def BusVolts(self) -> ComplexArray:
        '''Complex array of all bus, node voltages from most recent solution'''
        self._check_for_error(self._lib.Circuit_Get_AllBusVolts_GR())
        return self._get_fcomplex128_gr_array()

    def NodeDistances(self) -> Float64Array:
        '''Returns an array of distances from parent EnergyMeter for each Node. Corresponds to AllBusVMag sequence.'''
        self._check_for_error(self._lib.Circuit_Get_AllNodeDistances_GR())
        return self._get_float64_gr_array()

    def NodeNames(self) -> List[str]:
        '''Array of strings containing full name of each node in system in same order as returned by AllBusVolts, etc.'''
        return self._check_for_error(self._get_string_array(self._lib.Circuit_Get_AllNodeNames))

    def LineLosses(self) -> complex:
        '''Complex total line losses in the circuit'''
        self._check_for_error(self._lib.Circuit_Get_LineLosses_GR())
        return self._get_fcomplex128_gr_simple()

    def Losses(self) -> complex:
        '''Total losses in active circuit, complex number (two-element array of double).'''
        self._check_for_error(self._lib.Circuit_Get_Losses_GR())
        return self._get_fcomplex128_gr_simple()

    @property
    def Name(self) -> str:
        '''Name of the active circuit.'''
        return self._get_string(self._check_for_error(self._lib.Circuit_Get_Name()))

    @property
    def NumBuses(self) -> int:
        '''Total number of Buses in the circuit.'''
        return self._check_for_error(self._lib.Circuit_Get_NumBuses())

    @property
    def NumCircuitElements(self) -> int:
        '''Number of CircuitElements in the circuit.'''
        return self._check_for_error(self._lib.Circuit_Get_NumCircuitElements())

    @property
    def NumNodes(self) -> int:
        '''Total number of nodes in the circuit.'''
        return self._check_for_error(self._lib.Circuit_Get_NumNodes())

    @property
    def SubstationLosses(self) -> complex: 
        '''Complex losses in all transformers designated to substations.'''
        self._check_for_error(self._lib.Circuit_Get_SubstationLosses_GR())
        return self._get_fcomplex128_gr_simple() # TODO: FORCE ALWAYS use complex for AltDSS

    @property
    def SystemY(self, dense_matrix=False) -> ComplexArray: #TODO: replace with sparse
        '''
        (read-only) System Y matrix (after a solution has been performed). 
        This is deprecated as it returns a dense matrix. Only use it for small systems.
        For large-scale systems, prefer YMatrix.GetCompressedYMatrix.
        '''
        if dense_matrix:
            self._check_for_error(self._lib.Circuit_Get_SystemY_GR())
            return self._get_fcomplex128_gr_array()

        ffi = self._api_util.ffi
        
        nBus = ffi.new('uint32_t*')
        nBus[0] = 0
        nNz = ffi.new('uint32_t*')
        nNz[0] = 0

        ColPtr = ffi.new('int32_t**')
        RowIdxPtr = ffi.new('int32_t**')
        cValsPtr = ffi.new('double**')

        self._lib.YMatrix_GetCompressedYMatrix(True, nBus, nNz, ColPtr, RowIdxPtr, cValsPtr)

        if not nBus[0] or not nNz[0]:
            res = None
        else:
            # return as (data, indices, indptr) that can fed into scipy.sparse.csc_matrix
            res = (
                np.frombuffer(ffi.buffer(cValsPtr[0], nNz[0] * 16), dtype=complex).copy(),
                np.frombuffer(ffi.buffer(RowIdxPtr[0], nNz[0] * 4), dtype=np.int32).copy(),
                np.frombuffer(ffi.buffer(ColPtr[0], (nBus[0] + 1) * 4), dtype=np.int32).copy()
            )

        self._lib.DSS_Dispose_PInteger(ColPtr)
        self._lib.DSS_Dispose_PInteger(RowIdxPtr)
        self._lib.DSS_Dispose_PDouble(cValsPtr)
        
        self._check_for_error()

        return res


    def TotalPower(self) -> complex:
        '''Total power (complex), kVA delivered to the circuit'''
        self._check_for_error(self._lib.Circuit_Get_TotalPower_GR())
        return self._get_fcomplex128_gr_simple()

    def YCurrents(self) -> ComplexArray:
        '''Array of doubles containing complex injection currents for the present solution. Is is the "I" vector of I=YV'''
        self._check_for_error(self._lib.Circuit_Get_YCurrents_GR())
        return self._get_fcomplex128_gr_array()

    def YNodeOrder(self) -> List[str]:
        '''Array of strings containing the names of the nodes in the same order as the Y matrix'''
        return self._check_for_error(self._get_string_array(self._lib.Circuit_Get_YNodeOrder))

    def YNodeVarray(self) -> ComplexArray:
        '''Complex array of actual node voltages in same order as SystemY matrix.'''
        self._check_for_error(self._lib.Circuit_Get_YNodeVarray_GR())
        return self._get_fcomplex128_gr_array()

    def ElementLosses(self, value: Optional[Union[List[DSSObj], NonUniformBatch, DSSBatch]]=None) -> ComplexArray:#TODO
        '''
        Array of total losses (complex) in a selection of elements provided by the user, or all elements (default).
        
        Optionally, pass a list of DSS objects or a batch object. Circuit elements are required.
        '''
        if value is None:
            self._check_for_error(self._lib.Circuit_Get_AllElementLosses_GR())
            return self._get_fcomplex128_gr_array()

        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)
        self._check_for_error(self._lib.Circuit_Get_ElementLosses_GR(ValuePtr, ValueCount))        
        return self._get_fcomplex128_gr_array()

    def Capacity(self, Start: float, Increment: float) -> float:
        return self._check_for_error(self._lib.Circuit_Capacity(Start, Increment))

    def EndOfTimeStepUpdate(self):
        self._check_for_error(self._lib.Circuit_EndOfTimeStepUpdate()) #TODO: move to Solution?

    def TakeSample(self):
        self._check_for_error(self._lib.Circuit_Sample())

    def SaveSample(self):
        self._check_for_error(self._lib.Circuit_SaveSample())

    def UpdateStorage(self):
        self._check_for_error(self._lib.Circuit_UpdateStorage()) #TODO: move to the dedicated class/API

    def NewContext(self) -> Self:
        '''
        Creates a new AltDSS engine context.
        
        An AltDSS Context encapsulates most of the global state of the original OpenDSS engine,
        allowing the user to create multiple instances in the same process. By creating contexts
        manually, the management of threads and potential issues should be handled by the user.
        '''
        ffi = self._api_util.ffi
        lib = self._api_util.lib_unpatched
        new_ctx = ffi.gc(lib.ctx_New(), lib.ctx_Dispose)
        new_api_util = CffiApiUtil(ffi, lib, new_ctx)
        new_api_util._allow_complex = self._api_util._allow_complex
        return type(self)(new_api_util)

    def __call__(self, single:Union[AnyStr, List[AnyStr]]=None, block : AnyStr = None): #TODO: benchmark and simplify (single argument)
        '''
        Shortcut to pass text commands.

        If `single` is set and is a string, a normal `DSS.Text.Command = single` is called.
        Otherwise, the value is passed to `DSS.Text.Commands`.

        Examples:

            # single command
            DSS("new Circuit.test") 
            DSS(single="new Circuit.test")

            # list of commands (either will work)
            DSS(["new Circuit.test", "new Line.line1 bus1=a bus2=b"])
            DSS(single=["new circuit.test", "new Line.line1 bus1=a bus2=b"])
            DSS(block=["new circuit.test", "new Line.line1 bus1=a bus2=b"])

            # block of commands in a big string
            DSS(block="""
                clear
                new Circuit.test
                new Line.line1 bus1=a bus2=b
                new Load.load1 bus1=a bus2=b
            """)
        '''
        if (single is not None) and (block is not None):
           raise DSSException("Only a single argument is accepted.")

        if (single is None) and (block is None):
           raise DSSException("A value is required.")

        if single is not None:
            self.Text.Command = single
            return

        self.Text.Commands(single or block)

