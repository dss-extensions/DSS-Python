# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Base
from ._types import Int32Array
from typing import Union, AnyStr, List
from .enums import SolveModes, ControlModes, SolutionAlgorithms

class ISolution(Base):
    __slots__ = []

    _columns = [
        'MinIterations',
        'MaxIterations',
        'MaxControlIterations',
        'Totaliterations',
        'ControlIterations',
        'MostIterationsDone',
        'Number',
        'Process_Time',
        'AddType',
        'GenkW',
        'dblHour',
        'Capkvar',
        'Seconds',
        'GenMult',
        'DefaultYearly',
        'IntervalHrs',
        'Converged',
        'ModeID',
        'Time_of_Step',
        'Total_Time',
        'LoadModel',
        'EventLog',
        'Iterations',
        'GenPF',
        'Frequency',
        'LoadMult',
        'Random',
        'pctGrowth',
        'Year',
        'Algorithm',
        'Hour',
        'Tolerance',
        'ControlMode',
        'LDCurve',
        'StepSize',
        'DefaultDaily',
        'ControlActionsDone',
        'Mode',
        'SystemYChanged',
    ]

    def BuildYMatrix(self, BuildOption: int, AllocateVI: bool):
        self._check_for_error(self._lib.Solution_BuildYMatrix(BuildOption, AllocateVI))

    def CheckControls(self):
        self._check_for_error(self._lib.Solution_CheckControls())

    def CheckFaultStatus(self):
        self._check_for_error(self._lib.Solution_CheckFaultStatus())

    def Cleanup(self):
        self._check_for_error(self._lib.Solution_Cleanup())

    def DoControlActions(self):
        self._check_for_error(self._lib.Solution_DoControlActions())

    def FinishTimeStep(self):
        self._check_for_error(self._lib.Solution_FinishTimeStep())

    def InitSnap(self):
        self._check_for_error(self._lib.Solution_InitSnap())

    def SampleControlDevices(self):
        self._check_for_error(self._lib.Solution_SampleControlDevices())

    def Sample_DoControlActions(self):
        self._check_for_error(self._lib.Solution_Sample_DoControlActions())

    def Solve(self):
        self._check_for_error(self._lib.Solution_Solve())

    def SolveDirect(self):
        self._check_for_error(self._lib.Solution_SolveDirect())

    def SolveNoControl(self):
        self._check_for_error(self._lib.Solution_SolveNoControl())

    def SolvePflow(self):
        self._check_for_error(self._lib.Solution_SolvePflow())

    def SolvePlusControl(self):
        self._check_for_error(self._lib.Solution_SolvePlusControl())

    def SolveSnap(self):
        self._check_for_error(self._lib.Solution_SolveSnap())

    @property
    def AddType(self) -> int:
        '''
        Type of device to add in AutoAdd Mode: {dssGen (Default) | dssCap}

        Original COM help: https://opendss.epri.com/AddType.html
        '''
        return self._check_for_error(self._lib.Solution_Get_AddType())

    @AddType.setter
    def AddType(self, Value: int):
        self._check_for_error(self._lib.Solution_Set_AddType(Value))

    @property
    def Algorithm(self) -> SolutionAlgorithms:
        '''
        Base Solution algorithm

        Original COM help: https://opendss.epri.com/Algorithm.html
        '''
        return SolutionAlgorithms(self._check_for_error(self._lib.Solution_Get_Algorithm()))

    @Algorithm.setter
    def Algorithm(self, Value: Union[int, SolutionAlgorithms]):
        self._check_for_error(self._lib.Solution_Set_Algorithm(Value))

    @property
    def Capkvar(self) -> float:
        '''
        Capacitor kvar for adding capacitors in AutoAdd mode

        Original COM help: https://opendss.epri.com/Capkvar.html
        '''
        return self._check_for_error(self._lib.Solution_Get_Capkvar())

    @Capkvar.setter
    def Capkvar(self, Value: float):
        self._check_for_error(self._lib.Solution_Set_Capkvar(Value))

    @property
    def ControlActionsDone(self) -> bool:
        '''
        Flag indicating the control actions are done.

        Original COM help: https://opendss.epri.com/ControlActionsDone.html
        '''
        return self._check_for_error(self._lib.Solution_Get_ControlActionsDone()) != 0

    @ControlActionsDone.setter
    def ControlActionsDone(self, Value: bool):
        self._check_for_error(self._lib.Solution_Set_ControlActionsDone(Value))

    @property
    def ControlIterations(self) -> int:
        '''
        Value of the control iteration counter

        Original COM help: https://opendss.epri.com/ControlIterations.html
        '''
        return self._check_for_error(self._lib.Solution_Get_ControlIterations())

    @ControlIterations.setter
    def ControlIterations(self, Value: int):
        self._check_for_error(self._lib.Solution_Set_ControlIterations(Value))

    @property
    def ControlMode(self) -> ControlModes:
        '''
        Modes for control devices

        Original COM help: https://opendss.epri.com/ControlMode.html
        '''
        return ControlModes(self._check_for_error(self._lib.Solution_Get_ControlMode()))

    @ControlMode.setter
    def ControlMode(self, Value: Union[int, ControlModes]):
        self._check_for_error(self._lib.Solution_Set_ControlMode(Value))

    @property
    def Converged(self) -> bool:
        '''
        Flag to indicate whether the circuit solution converged

        Original COM help: https://opendss.epri.com/Converged.html
        '''
        return self._check_for_error(self._lib.Solution_Get_Converged()) != 0

    @Converged.setter
    def Converged(self, Value: bool):
        self._check_for_error(self._lib.Solution_Set_Converged(Value))

    @property
    def DefaultDaily(self) -> str:
        '''
        Default daily load shape (defaults to "Default")

        Original COM help: https://opendss.epri.com/DefaultDaily.html
        '''
        return self._get_string(self._check_for_error(self._lib.Solution_Get_DefaultDaily()))

    @DefaultDaily.setter
    def DefaultDaily(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Solution_Set_DefaultDaily(Value))

    @property
    def DefaultYearly(self) -> str:
        '''
        Default Yearly load shape (defaults to "Default")

        Original COM help: https://opendss.epri.com/DefaultYearly.html
        '''
        return self._get_string(self._check_for_error(self._lib.Solution_Get_DefaultYearly()))

    @DefaultYearly.setter
    def DefaultYearly(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Solution_Set_DefaultYearly(Value))

    @property
    def EventLog(self) -> List[str]:
        '''
        Array of strings containing the Event Log

        Original COM help: https://opendss.epri.com/EventLog.html
        '''
        return self._check_for_error(self._get_string_array(self._lib.Solution_Get_EventLog))

    @property
    def Frequency(self) -> float:
        '''
        Set the Frequency for next solution

        Original COM help: https://opendss.epri.com/Frequency1.html
        '''
        return self._check_for_error(self._lib.Solution_Get_Frequency())

    @Frequency.setter
    def Frequency(self, Value: float):
        self._check_for_error(self._lib.Solution_Set_Frequency(Value))

    @property
    def GenMult(self) -> float:
        '''
        Default Multiplier applied to generators (like LoadMult)

        Original COM help: https://opendss.epri.com/GenMult.html
        '''
        return self._check_for_error(self._lib.Solution_Get_GenMult())

    @GenMult.setter
    def GenMult(self, Value: float):
        self._check_for_error(self._lib.Solution_Set_GenMult(Value))

    @property
    def GenPF(self) -> float:
        '''
        PF for generators in AutoAdd mode

        Original COM help: https://opendss.epri.com/GenPF.html
        '''
        return self._check_for_error(self._lib.Solution_Get_GenPF())

    @GenPF.setter
    def GenPF(self, Value: float):
        self._check_for_error(self._lib.Solution_Set_GenPF(Value))

    @property
    def GenkW(self) -> float:
        '''
        Generator kW for AutoAdd mode

        Original COM help: https://opendss.epri.com/GenkW.html
        '''
        return self._check_for_error(self._lib.Solution_Get_GenkW())

    @GenkW.setter
    def GenkW(self, Value: float):
        self._check_for_error(self._lib.Solution_Set_GenkW(Value))

    @property
    def Hour(self) -> int:
        '''
        Set Hour for time series solutions.

        Original COM help: https://opendss.epri.com/Hour.html
        '''
        return self._check_for_error(self._lib.Solution_Get_Hour())

    @Hour.setter
    def Hour(self, Value: int):
        self._check_for_error(self._lib.Solution_Set_Hour(Value))

    @property
    def IntervalHrs(self) -> float:
        '''
        Get/Set the Solution.IntervalHrs variable used for devices that integrate / custom solution algorithms
        '''
        return self._check_for_error(self._lib.Solution_Get_IntervalHrs())

    @IntervalHrs.setter
    def IntervalHrs(self, Value: float):
        self._check_for_error(self._lib.Solution_Set_IntervalHrs(Value))

    @property
    def Iterations(self) -> int:
        '''
        Number of iterations taken for last solution. (Same as Totaliterations)

        Original COM help: https://opendss.epri.com/Iterations.html
        '''
        return self._check_for_error(self._lib.Solution_Get_Iterations())

    @property
    def LDCurve(self) -> str:
        '''
        Load-Duration Curve name for LD modes

        Original COM help: https://opendss.epri.com/LDCurve.html
        '''
        return self._get_string(self._check_for_error(self._lib.Solution_Get_LDCurve()))

    @LDCurve.setter
    def LDCurve(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Solution_Set_LDCurve(Value))

    @property
    def LoadModel(self) -> int:
        '''
        Load Model: {dssPowerFlow (default) | dssAdmittance}

        Original COM help: https://opendss.epri.com/LoadModel.html
        '''
        return self._check_for_error(self._lib.Solution_Get_LoadModel())

    @LoadModel.setter
    def LoadModel(self, Value: int):
        self._check_for_error(self._lib.Solution_Set_LoadModel(Value))

    @property
    def LoadMult(self) -> float:
        '''
        Default load multiplier applied to all non-fixed loads

        Original COM help: https://opendss.epri.com/LoadMult.html
        '''
        return self._check_for_error(self._lib.Solution_Get_LoadMult())

    @LoadMult.setter
    def LoadMult(self, Value: float):
        self._check_for_error(self._lib.Solution_Set_LoadMult(Value))

    @property
    def MaxControlIterations(self) -> int:
        '''
        Maximum allowable control iterations

        Original COM help: https://opendss.epri.com/MaxControlIterations.html
        '''
        return self._check_for_error(self._lib.Solution_Get_MaxControlIterations())

    @MaxControlIterations.setter
    def MaxControlIterations(self, Value):
        self._check_for_error(self._lib.Solution_Set_MaxControlIterations(Value))

    @property
    def MaxIterations(self) -> int:
        '''
        Max allowable iterations.

        Original COM help: https://opendss.epri.com/MaxIterations.html
        '''
        return self._check_for_error(self._lib.Solution_Get_MaxIterations())

    @MaxIterations.setter
    def MaxIterations(self, Value: int):
        self._check_for_error(self._lib.Solution_Set_MaxIterations(Value))

    @property
    def MinIterations(self) -> int:
        '''
        Minimum number of iterations required for a power flow solution.

        Original COM help: https://opendss.epri.com/MinIterations.html
        '''
        return self._check_for_error(self._lib.Solution_Get_MinIterations())

    @MinIterations.setter
    def MinIterations(self, Value: int):
        self._check_for_error(self._lib.Solution_Set_MinIterations(Value))

    @property
    def Mode(self) -> SolveModes:
        '''
        Set present solution mode

        Original COM help: https://opendss.epri.com/Mode2.html
        '''
        return SolveModes(self._check_for_error(self._lib.Solution_Get_Mode()))

    @Mode.setter
    def Mode(self, Value: Union[int, SolveModes]):
        self._check_for_error(self._lib.Solution_Set_Mode(Value))

    @property
    def ModeID(self) -> str:
        '''
        ID (text) of the present solution mode

        Original COM help: https://opendss.epri.com/ModeID.html
        '''
        return self._get_string(self._check_for_error(self._lib.Solution_Get_ModeID()))

    @property
    def MostIterationsDone(self) -> int:
        '''
        Max number of iterations required to converge at any control iteration of the most recent solution.

        Original COM help: https://opendss.epri.com/MostIterationsDone.html
        '''
        return self._check_for_error(self._lib.Solution_Get_MostIterationsDone())

    @property
    def Number(self) -> int:
        '''
        Number of solutions to perform for Monte Carlo and time series simulations

        Original COM help: https://opendss.epri.com/Number1.html
        '''
        return self._check_for_error(self._lib.Solution_Get_Number())

    @Number.setter
    def Number(self, Value: int):
        self._check_for_error(self._lib.Solution_Set_Number(Value))

    @property
    def Process_Time(self) -> float:
        '''
        Gets the time required to perform the latest solution (Read only)

        Original COM help: https://opendss.epri.com/Process_Time.html
        '''
        return self._check_for_error(self._lib.Solution_Get_Process_Time())

    @property
    def Random(self) -> int:
        '''
        Randomization mode for random variables "Gaussian" or "Uniform"

        Original COM help: https://opendss.epri.com/Random.html
        '''
        return self._check_for_error(self._lib.Solution_Get_Random())

    @Random.setter
    def Random(self, Value: int):
        self._check_for_error(self._lib.Solution_Set_Random(Value))

    @property
    def Seconds(self) -> float:
        '''
        Seconds from top of the hour.

        Original COM help: https://opendss.epri.com/Seconds.html
        '''
        return self._check_for_error(self._lib.Solution_Get_Seconds())

    @Seconds.setter
    def Seconds(self, Value: float):
        self._check_for_error(self._lib.Solution_Set_Seconds(Value))

    @property
    def StepSize(self) -> float:
        '''
        Time step size in sec

        Original COM help: https://opendss.epri.com/StepSize.html
        '''
        return self._check_for_error(self._lib.Solution_Get_StepSize())

    @StepSize.setter
    def StepSize(self, Value: float):
        self._check_for_error(self._lib.Solution_Set_StepSize(Value))

    @property
    def SystemYChanged(self) -> bool:
        '''
        Flag that indicates if elements of the System Y have been changed by recent activity.

        Original COM help: https://opendss.epri.com/SystemYChanged.html
        '''
        return self._check_for_error(self._lib.Solution_Get_SystemYChanged() != 0)

    @property
    def Time_of_Step(self) -> float:
        '''
        Get the solution process time + sample time for time step

        Original COM help: https://opendss.epri.com/Time_of_Step.html
        '''
        return self._check_for_error(self._lib.Solution_Get_Time_of_Step())

    @property
    def Tolerance(self) -> float:
        '''
        Solution convergence tolerance.

        Original COM help: https://opendss.epri.com/Tolerance.html
        '''
        return self._check_for_error(self._lib.Solution_Get_Tolerance())

    @Tolerance.setter
    def Tolerance(self, Value: float):
        self._check_for_error(self._lib.Solution_Set_Tolerance(Value))

    @property
    def Total_Time(self) -> float:
        '''
        Gets/sets the accumulated time of the simulation

        This accumulator has to be reset manually.

        Original COM help: https://opendss.epri.com/Total_Time.html
        '''
        return self._check_for_error(self._lib.Solution_Get_Total_Time())

    @Total_Time.setter
    def Total_Time(self, Value: float):
        self._check_for_error(self._lib.Solution_Set_Total_Time(Value))

    @property
    def Totaliterations(self) -> int:
        '''
        Total iterations including control iterations for most recent solution.

        Original COM help: https://opendss.epri.com/Totaliterations.html
        '''
        return self._check_for_error(self._lib.Solution_Get_Totaliterations())

    @property
    def Year(self) -> int:
        '''
        Set year for planning studies

        Original COM help: https://opendss.epri.com/Year.html
        '''
        return self._check_for_error(self._lib.Solution_Get_Year())

    @Year.setter
    def Year(self, Value: int):
        self._check_for_error(self._lib.Solution_Set_Year(Value))

    @property
    def dblHour(self) -> float:
        '''
        Hour as a double, including fractional part

        Original COM help: https://opendss.epri.com/dblHour1.html
        '''
        return self._check_for_error(self._lib.Solution_Get_dblHour())

    @dblHour.setter
    def dblHour(self, Value: float):
        self._check_for_error(self._lib.Solution_Set_dblHour(Value))

    @property
    def pctGrowth(self) -> float:
        '''
        Percent default  annual load growth rate

        Original COM help: https://opendss.epri.com/pctGrowth.html
        '''
        return self._check_for_error(self._lib.Solution_Get_pctGrowth())

    @pctGrowth.setter
    def pctGrowth(self, Value: float):
        self._check_for_error(self._lib.Solution_Set_pctGrowth(Value))

    @property
    def StepsizeHr(self) -> float:
        '''(write-only) Set Stepsize in Hr'''
        raise AttributeError("This property is write-only!")

    @StepsizeHr.setter
    def StepsizeHr(self, Value: float):
        self._check_for_error(self._lib.Solution_Set_StepsizeHr(Value))

    @property
    def StepsizeMin(self) -> float:
        '''(write-only) Set Stepsize in minutes'''
        raise AttributeError("This property is write-only!")

    @StepsizeMin.setter
    def StepsizeMin(self, Value: float):
        self._check_for_error(self._lib.Solution_Set_StepsizeMin(Value))

    # The following are officially available only in v8
    @property
    def BusLevels(self) -> Int32Array:
        '''
        Bus levels for all the buses in the model. 
        
        The bus levels are calculated after calculating the incidence branch-to-node (B2N) 
        matrix and they represent the distance from the buses to a reference that goes from
        the feeder head to the farthest bus in the model. The bus level index matches with
        the bus list obtained with the circuit interface.

        Original COM help: https://opendss.epri.com/BusLevels.html
        '''
        self._check_for_error(self._lib.Solution_Get_BusLevels_GR())
        return self._get_int32_gr_array()

    @property
    def IncMatrix(self) -> Int32Array:
        '''
        Incidence branch-to-node (B2N) matrix calculated for the model as a vector of integers.
        
        The vector represents a sparse matrix (non-zero values are the only ones delivered) and
        can be interpreted as follows: The first element is the row number, the second one is
        the column and the third is the value, this way, by dividing the number of elements
        in the array by 3 the user can obtain the number of rows in case of wanting to sort 
        the vector values within a matrix.

        Original COM help: https://opendss.epri.com/IncMatrix.html
        '''
        #TODO: expose as sparse matrix
        self._check_for_error(self._lib.Solution_Get_IncMatrix_GR())
        return self._get_int32_gr_array()

    @property
    def IncMatrixCols(self) -> List[str]:
        '''
        Names of the columns of the branch-to-node (B2N) matrix.

        Original COM help: https://opendss.epri.com/IncMatrixCols.html
        '''
        return self._check_for_error(self._get_string_array(self._lib.Solution_Get_IncMatrixCols))

    @property
    def IncMatrixRows(self) -> List[str]:
        '''
        Names of the rows of the branch-to-node (B2N) matrix.

        Original COM help: https://opendss.epri.com/IncMatrixRows.html
        '''
        return self._check_for_error(self._get_string_array(self._lib.Solution_Get_IncMatrixRows))

    @property
    def Laplacian(self) -> Int32Array:
        '''
        Laplacian matrix calculated in OpenDSS based on the latest branch-to-node (B2N) matrix.
        
        The vector represents a sparse matrix (non-zero values are the only ones delivered) and
        can be interpreted as follows: The first element is the row number, the second one is
        the column and the third is the value, this way, by dividing the number of elements
        in the array by 3 the user can obtain the number of rows in case of wanting to sort
        the vector values within a matrix. The tables for the columns and rows are the same
        as the columns for the B2N columns (square matrix).        

        Original COM help: https://opendss.epri.com/Laplacian.html
        '''
        #TODO: expose as sparse matrix
        self._check_for_error(self._lib.Solution_Get_Laplacian_GR())
        return self._get_int32_gr_array()

    def SolveAll(self):
        '''
        Solves all the circuits (Actors) loaded into memory by the user.

        Original COM help: https://opendss.epri.com/SolveAll.html
        '''
        self._check_for_error(self._lib.Solution_SolveAll())
        
