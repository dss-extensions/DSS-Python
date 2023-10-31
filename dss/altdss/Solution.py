'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2023 Paulo Meira

Copyright (c) 2018-2023 DSS-Extensions contributors
'''
from .common import Base
from .types import Int32Array
from typing import Union, AnyStr, List
from dss.enums import SolveModes, ControlModes, SolutionAlgorithms

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
        ''''
        
        Same as Circuit.EndOfTimeStepUpdate
        '''
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
        '''Type of device to add in AutoAdd Mode: {dssGen (Default) | dssCap}'''
        return self._check_for_error(self._lib.Solution_Get_AddType())

    @AddType.setter
    def AddType(self, Value: int):
        self._check_for_error(self._lib.Solution_Set_AddType(Value))

    @property
    def Algorithm(self) -> SolutionAlgorithms:
        '''Base Solution algorithm: {dssNormalSolve | dssNewtonSolve}'''
        return SolutionAlgorithms(self._check_for_error(self._lib.Solution_Get_Algorithm()))

    @Algorithm.setter
    def Algorithm(self, Value: Union[int, SolutionAlgorithms]):
        self._check_for_error(self._lib.Solution_Set_Algorithm(Value))

    @property
    def Capkvar(self) -> float:
        '''Capacitor kvar for adding capacitors in AutoAdd mode'''
        return self._check_for_error(self._lib.Solution_Get_Capkvar())

    @Capkvar.setter
    def Capkvar(self, Value: float):
        self._check_for_error(self._lib.Solution_Set_Capkvar(Value))

    @property
    def ControlActionsDone(self) -> bool:
        '''Flag indicating the control actions are done.'''
        return self._check_for_error(self._lib.Solution_Get_ControlActionsDone()) != 0

    @ControlActionsDone.setter
    def ControlActionsDone(self, Value: bool):
        self._check_for_error(self._lib.Solution_Set_ControlActionsDone(Value))

    @property
    def ControlIterations(self) -> int:
        '''Value of the control iteration counter'''
        return self._check_for_error(self._lib.Solution_Get_ControlIterations())

    @ControlIterations.setter
    def ControlIterations(self, Value: int):
        self._check_for_error(self._lib.Solution_Set_ControlIterations(Value))

    @property
    def ControlMode(self) -> ControlModes:
        '''{dssStatic* | dssEvent | dssTime}  Modes for control devices'''
        return ControlModes(self._check_for_error(self._lib.Solution_Get_ControlMode()))

    @ControlMode.setter
    def ControlMode(self, Value: Union[int, ControlModes]):
        self._check_for_error(self._lib.Solution_Set_ControlMode(Value))

    @property
    def Converged(self) -> bool:
        '''Flag to indicate whether the circuit solution converged'''
        return self._check_for_error(self._lib.Solution_Get_Converged()) != 0

    @Converged.setter
    def Converged(self, Value: bool):
        self._check_for_error(self._lib.Solution_Set_Converged(Value))

    @property
    def DefaultDaily(self) -> str:
        '''Default daily load shape (defaults to "Default")'''
        return self._get_string(self._check_for_error(self._lib.Solution_Get_DefaultDaily()))

    @DefaultDaily.setter
    def DefaultDaily(self, Value: AnyStr):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Solution_Set_DefaultDaily(Value))

    @property
    def DefaultYearly(self) -> str:
        '''Default Yearly load shape (defaults to "Default")'''
        return self._get_string(self._check_for_error(self._lib.Solution_Get_DefaultYearly()))

    @DefaultYearly.setter
    def DefaultYearly(self, Value: AnyStr):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Solution_Set_DefaultYearly(Value))

    @property
    def EventLog(self) -> List[str]:
        '''Array of strings containing the Event Log'''
        return self._check_for_error(self._get_string_array(self._lib.Solution_Get_EventLog))

    @property
    def Frequency(self) -> float:
        '''Set the Frequency for next solution'''
        return self._check_for_error(self._lib.Solution_Get_Frequency())

    @Frequency.setter
    def Frequency(self, Value: float):
        self._check_for_error(self._lib.Solution_Set_Frequency(Value))

    @property
    def GenMult(self) -> float:
        '''Default Multiplier applied to generators (like LoadMult)'''
        return self._check_for_error(self._lib.Solution_Get_GenMult())

    @GenMult.setter
    def GenMult(self, Value: float):
        self._check_for_error(self._lib.Solution_Set_GenMult(Value))

    @property
    def GenPF(self) -> float:
        '''PF for generators in AutoAdd mode'''
        return self._check_for_error(self._lib.Solution_Get_GenPF())

    @GenPF.setter
    def GenPF(self, Value: float):
        self._check_for_error(self._lib.Solution_Set_GenPF(Value))

    @property
    def GenkW(self) -> float:
        '''Generator kW for AutoAdd mode'''
        return self._check_for_error(self._lib.Solution_Get_GenkW())

    @GenkW.setter
    def GenkW(self, Value: float):
        self._check_for_error(self._lib.Solution_Set_GenkW(Value))

    @property
    def Hour(self) -> int:
        '''Set Hour for time series solutions.'''
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
        '''Number of iterations taken for last solution. (Same as Totaliterations)'''
        return self._check_for_error(self._lib.Solution_Get_Iterations())

    @property
    def LDCurve(self) -> str:
        '''Load-Duration Curve name for LD modes'''
        return self._get_string(self._check_for_error(self._lib.Solution_Get_LDCurve()))

    @LDCurve.setter
    def LDCurve(self, Value: AnyStr):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Solution_Set_LDCurve(Value))

    @property
    def LoadModel(self) -> int:
        '''Load Model: {dssPowerFlow (default) | dssAdmittance}'''
        return self._check_for_error(self._lib.Solution_Get_LoadModel())

    @LoadModel.setter
    def LoadModel(self, Value: int):
        self._check_for_error(self._lib.Solution_Set_LoadModel(Value))

    @property
    def LoadMult(self) -> float:
        '''Default load multiplier applied to all non-fixed loads'''
        return self._check_for_error(self._lib.Solution_Get_LoadMult())

    @LoadMult.setter
    def LoadMult(self, Value: float):
        self._check_for_error(self._lib.Solution_Set_LoadMult(Value))

    @property
    def MaxControlIterations(self) -> int:
        '''Maximum allowable control iterations'''
        return self._check_for_error(self._lib.Solution_Get_MaxControlIterations())

    @MaxControlIterations.setter
    def MaxControlIterations(self, Value):
        self._check_for_error(self._lib.Solution_Set_MaxControlIterations(Value))

    @property
    def MaxIterations(self) -> int:
        '''Max allowable iterations.'''
        return self._check_for_error(self._lib.Solution_Get_MaxIterations())

    @MaxIterations.setter
    def MaxIterations(self, Value: int):
        self._check_for_error(self._lib.Solution_Set_MaxIterations(Value))

    @property
    def MinIterations(self) -> int:
        '''Minimum number of iterations required for a power flow solution.'''
        return self._check_for_error(self._lib.Solution_Get_MinIterations())

    @MinIterations.setter
    def MinIterations(self, Value: int):
        self._check_for_error(self._lib.Solution_Set_MinIterations(Value))

    @property
    def Mode(self) -> SolveModes:
        '''Set present solution mode'''
        return SolveModes(self._check_for_error(self._lib.Solution_Get_Mode()))

    @Mode.setter
    def Mode(self, Value: Union[int, SolveModes]):
        self._check_for_error(self._lib.Solution_Set_Mode(Value))

    @property
    def ModeID(self) -> str:
        '''ID (text) of the present solution mode'''
        return self._get_string(self._check_for_error(self._lib.Solution_Get_ModeID()))

    @property
    def MostIterationsDone(self) -> int:
        '''Max number of iterations required to converge at any control iteration of the most recent solution.'''
        return self._check_for_error(self._lib.Solution_Get_MostIterationsDone())

    @property
    def Number(self) -> int:
        '''Number of solutions to perform for Monte Carlo and time series simulations'''
        return self._check_for_error(self._lib.Solution_Get_Number())

    @Number.setter
    def Number(self, Value: int):
        self._check_for_error(self._lib.Solution_Set_Number(Value))

    @property
    def Process_Time(self) -> float:
        '''Gets the time required to perform the latest solution (Read only)'''
        return self._check_for_error(self._lib.Solution_Get_Process_Time())

    @property
    def Random(self) -> int:
        '''Randomization mode for random variables "Gaussian" or "Uniform"'''
        return self._check_for_error(self._lib.Solution_Get_Random())

    @Random.setter
    def Random(self, Value: int):
        self._check_for_error(self._lib.Solution_Set_Random(Value))

    @property
    def Seconds(self) -> float:
        '''Seconds from top of the hour.'''
        return self._check_for_error(self._lib.Solution_Get_Seconds())

    @Seconds.setter
    def Seconds(self, Value: float):
        self._check_for_error(self._lib.Solution_Set_Seconds(Value))

    @property
    def StepSize(self) -> float:
        '''Time step size in sec'''
        return self._check_for_error(self._lib.Solution_Get_StepSize())

    @StepSize.setter
    def StepSize(self, Value: float):
        self._check_for_error(self._lib.Solution_Set_StepSize(Value))

    @property
    def SystemYChanged(self) -> bool:
        '''Flag that indicates if elements of the System Y have been changed by recent activity.'''
        return self._check_for_error(self._lib.Solution_Get_SystemYChanged() != 0)

    @property
    def Time_of_Step(self) -> float:
        '''Get the solution process time + sample time for time step'''
        return self._check_for_error(self._lib.Solution_Get_Time_of_Step())

    @property
    def Tolerance(self) -> float:
        '''Solution convergence tolerance.'''
        return self._check_for_error(self._lib.Solution_Get_Tolerance())

    @Tolerance.setter
    def Tolerance(self, Value: float):
        self._check_for_error(self._lib.Solution_Set_Tolerance(Value))

    @property
    def Total_Time(self) -> float:
        '''
        Gets/sets the accumulated time of the simulation
        '''
        return self._check_for_error(self._lib.Solution_Get_Total_Time())

    @Total_Time.setter
    def Total_Time(self, Value: float):
        self._check_for_error(self._lib.Solution_Set_Total_Time(Value))

    @property
    def Totaliterations(self) -> int:
        '''Total iterations including control iterations for most recent solution.'''
        return self._check_for_error(self._lib.Solution_Get_Totaliterations())

    @property
    def Year(self) -> int:
        '''Set year for planning studies'''
        return self._check_for_error(self._lib.Solution_Get_Year())

    @Year.setter
    def Year(self, Value: int):
        self._check_for_error(self._lib.Solution_Set_Year(Value))

    @property
    def dblHour(self) -> float:
        '''Hour as a double, including fractional part'''
        return self._check_for_error(self._lib.Solution_Get_dblHour())

    @dblHour.setter
    def dblHour(self, Value: float):
        self._check_for_error(self._lib.Solution_Set_dblHour(Value))

    @property
    def pctGrowth(self) -> float:
        '''Percent default  annual load growth rate'''
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
        self._check_for_error(self._lib.Solution_Get_BusLevels_GR())
        return self._get_int32_gr_array()

    @property
    def IncMatrix(self) -> Int32Array:
        self._check_for_error(self._lib.Solution_Get_IncMatrix_GR())
        return self._get_int32_gr_array()

    @property
    def IncMatrixCols(self) -> List[str]:
        return self._check_for_error(self._get_string_array(self._lib.Solution_Get_IncMatrixCols))

    @property
    def IncMatrixRows(self) -> List[str]:
        return self._check_for_error(self._get_string_array(self._lib.Solution_Get_IncMatrixRows))

    @property
    def Laplacian(self) -> Int32Array:
        self._check_for_error(self._lib.Solution_Get_Laplacian_GR())
        return self._get_int32_gr_array()

    def SolveAll(self):
        self._check_for_error(self._lib.Solution_SolveAll())
        
