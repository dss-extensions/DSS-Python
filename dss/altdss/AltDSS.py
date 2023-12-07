from typing import Union, List, AnyStr, Optional
from typing_extensions import Self
import numpy as np

# These are currently reused directly from DSS-Python; this may change later
from dss.IDSSEvents import IDSSEvents
from dss.IError import IError
from dss.IReduceCkt import IReduceCkt
from dss.ITopology import ITopology
from dss.IYMatrix import IYMatrix

from .common import CffiApiUtil
from dss.enums import DSSJSONFlags
from .enums import *
from .Bus import IBuses
from .CircuitElement import CircuitElementBatch
from .ControlQueue import IControlQueue
from .Obj import IObj
from .PCElement import PCElementBatch
from .PDElement import PDElementBatch
from .Settings import ISettings
from .Solution import ISolution
from .ZIP import IZIP
from .types import Float64Array, ComplexArray

class IAltDSS(IObj):
    __slots__ = [
        'Bus',
        'ControlQueue',
        'Element',
        'Error',
        'Events',
        # 'Parallel',
        'PCElement',
        'PDElement',
        'ReduceCircuit',
        'Settings',
        'Solution',
        'Topology',
        'YMatrix',
        'ZIP',
        '_ptr',
    ]
    _ctx_to_altdss = {}
   
    Bus: IBuses
    ControlQueue: IControlQueue
    Element: CircuitElementBatch
    Error: IError
    Events: IDSSEvents
    # Parallel: IParallel
    PCElement: PCElementBatch
    PDElement: PDElementBatch
    ReduceCircuit: IReduceCkt
    Settings: ISettings
    Solution: ISolution
    Topology: ITopology
    YMatrix: IYMatrix
    ZIP: IZIP


    @staticmethod
    def get_from_context(api_util) -> Self:
        existing = IAltDSS._ctx_to_altdss.get(api_util.ctx)
        if existing is not None:
            return existing
        
        return IAltDSS(api_util)

    def __init__(self, api_util):
        IObj.__init__(self, api_util)
        IAltDSS._ctx_to_altdss[api_util.ctx] = self
        self._ptr = api_util.ctx

        self.Bus = IBuses(self._api_util)
        self.ControlQueue = IControlQueue(self._api_util)
        self.Element = CircuitElementBatch(None, self)
        self.Error = IError(self._api_util)
        self.Events = IDSSEvents(self._api_util)
        # self.Parallel = IParallel(self._api_util)
        self.PCElement = PCElementBatch(None, self)
        self.PDElement = PDElementBatch(None, self)
        self.ReduceCircuit = IReduceCkt(self._api_util)
        self.Settings = ISettings(self._api_util)
        self.Solution = ISolution(self._api_util)
        self.Topology = ITopology(self._api_util)
        self.YMatrix = IYMatrix(self._api_util)
        self.ZIP = IZIP(self._api_util)


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
        return self._get_fcomplex128_gr_simple()

    def SystemY(self, dense_matrix=False) -> ComplexArray:
        '''
        Get the system Y complex matrix.
        Requires either a previous solution or explicitly building the marix.

        In AltDSS, defaults to the sparse matrix data.
        
        Use `dense_matrix=True` to force a dense matrix. Beware the
        memory requirements. The recommendation is to only use dense
        matrices for small systems.
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
        '''Array of doubles containing complex injection currents for the present solution. It is the "I" vector of I=YV'''
        self._check_for_error(self._lib.Circuit_Get_YCurrents_GR())
        return self._get_fcomplex128_gr_array()

    def YNodeOrder(self) -> List[str]:
        '''Array of strings containing the names of the nodes in the same order as the Y matrix'''
        return self._check_for_error(self._get_string_array(self._lib.Circuit_Get_YNodeOrder))

    def YNodeVarray(self) -> ComplexArray:
        '''Complex array of actual node voltages in same order as SystemY matrix.'''
        self._check_for_error(self._lib.Circuit_Get_YNodeVarray_GR())
        return self._get_fcomplex128_gr_array()

    def Capacity(self, Start: float, Increment: float) -> float:
        return self._check_for_error(self._lib.Circuit_Capacity(Start, Increment))

    def TakeSample(self):
        self._check_for_error(self._lib.Circuit_Sample())

    def SaveSample(self):
        self._check_for_error(self._lib.Circuit_SaveSample())

    def UpdateStorage(self):
        self._check_for_error(self._lib.Circuit_UpdateStorage()) #TODO: move to the dedicated class/API

    def Clear(self):
        self('clear')

    def ClearAll(self):
        self._check_for_error(self._lib.DSS_ClearAll())

    def to_json(self, options: DSSJSONFlags = 0) -> str:
        '''
        Returns data for all objects and basic circuit properties as a JSON-encoded string.
        The JSON data is organized using 

        The `options` parameter contains bit-flags to toggle specific features.
        See `Obj_ToJSON` (C-API) for more, or `DSSObj.to_json` in Python.

        (API Extension)
        '''
        return self._get_string(self.CheckForError(self._lib.Circuit_ToJSON(options)))

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


    def Command(self, value: Optional[AnyStr]) -> Optional[str]:
        '''
        Input command **string** for the DSS engine.
        
        If no command is provided, the latest command string is returned.

        Prefer using the `Commands` function or the call operator from this class.
        '''
        if value is None:
            return self._get_string(self._check_for_error(self._lib.Text_Get_Command()))

        if type(value) is not bytes:
            value = value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Text_Set_Command(value))


    def Commands(self, Value: Union[AnyStr, List[AnyStr]]):
        '''
        Runs a list of strings or a large string as commands directly in the DSS engine.
        Intermediate results from the classic Text.Result are ignored.

        Value can be a list of strings, or a single large string (usually faster, but varies).

        (API Extension)
        '''
        if isinstance(Value, str) or isinstance(Value, bytes):
            if type(Value) is not bytes:
                Value = Value.encode(self._api_util.codec)
            
            self._check_for_error(self._lib.Text_CommandBlock(Value))
        else:
            self._check_for_error(self._set_string_array(self._lib.Text_CommandArray, Value))


    def __call__(self, cmds: Union[AnyStr, List[AnyStr]]):
        '''
        Pass either a single string (with either one or multiples commands, separated by new lines),
        or a list of strings.

        Examples:

            # single command
            DSS("new Circuit.test") 

            # list of commands
            DSS(["new Circuit.test", "new Line.line1 bus1=a bus2=b"])

            # block of commands in a big string
            DSS("""
                clear
                new Circuit.test
                new Line.line1 bus1=a bus2=b
                new Load.load1 bus1=a bus2=b
            """)
        '''
        self.Commands(cmds)

