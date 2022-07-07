'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira
Copyright (c) 2018-2022 DSS Extensions contributors
'''
from .._cffi_api_util import Base

class ISolution(Base):
    __slots__ = []
    
    _columns = [
        'MinIterations',
        'MaxIterations',
        'MaxControlIterations',
        'TotalIterations',
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

    def BuildYMatrix(self, BuildOption, AllocateVI):
        self.CheckForError(self._lib.Solution_BuildYMatrix(BuildOption, AllocateVI))

    def CheckControls(self):
        self.CheckForError(self._lib.Solution_CheckControls())

    def CheckFaultStatus(self):
        self.CheckForError(self._lib.Solution_CheckFaultStatus())

    def Cleanup(self):
        self.CheckForError(self._lib.Solution_Cleanup())

    def DoControlActions(self):
        self.CheckForError(self._lib.Solution_DoControlActions())

    def FinishTimeStep(self):
        self.CheckForError(self._lib.Solution_FinishTimeStep())

    def InitSnap(self):
        self.CheckForError(self._lib.Solution_InitSnap())

    def SampleControlDevices(self):
        self.CheckForError(self._lib.Solution_SampleControlDevices())

    def Sample_DoControlActions(self):
        self.CheckForError(self._lib.Solution_Sample_DoControlActions())

    def Solve(self):
        self.CheckForError(self._lib.Solution_Solve())

    def SolveDirect(self):
        self.CheckForError(self._lib.Solution_SolveDirect())

    def SolveNoControl(self):
        self.CheckForError(self._lib.Solution_SolveNoControl())

    def SolvePflow(self):
        self.CheckForError(self._lib.Solution_SolvePflow())

    def SolvePlusControl(self):
        self.CheckForError(self._lib.Solution_SolvePlusControl())

    def SolveSnap(self):
        self.CheckForError(self._lib.Solution_SolveSnap())

    @property
    def AddType(self):
        '''Type of device to add in AutoAdd Mode: {dssGen (Default) | dssCap}'''
        return self.CheckForError(self._lib.Solution_Get_AddType())

    @AddType.setter
    def AddType(self, Value):
        self.CheckForError(self._lib.Solution_Set_AddType(Value))

    @property
    def Algorithm(self):
        '''Base Solution algorithm: {dssNormalSolve | dssNewtonSolve}'''
        return self.CheckForError(self._lib.Solution_Get_Algorithm()) #TODO: use enum

    @Algorithm.setter
    def Algorithm(self, Value):
        self.CheckForError(self._lib.Solution_Set_Algorithm(Value))

    @property
    def Capkvar(self):
        '''Capacitor kvar for adding capacitors in AutoAdd mode'''
        return self.CheckForError(self._lib.Solution_Get_Capkvar())

    @Capkvar.setter
    def Capkvar(self, Value):
        self.CheckForError(self._lib.Solution_Set_Capkvar(Value))

    @property
    def ControlActionsDone(self):
        '''Flag indicating the control actions are done.'''
        return self.CheckForError(self._lib.Solution_Get_ControlActionsDone()) != 0

    @ControlActionsDone.setter
    def ControlActionsDone(self, Value):
        self.CheckForError(self._lib.Solution_Set_ControlActionsDone(Value))

    @property
    def ControlIterations(self):
        '''Value of the control iteration counter'''
        return self.CheckForError(self._lib.Solution_Get_ControlIterations())

    @ControlIterations.setter
    def ControlIterations(self, Value):
        self.CheckForError(self._lib.Solution_Set_ControlIterations(Value))

    @property
    def ControlMode(self):
        '''{dssStatic* | dssEvent | dssTime}  Modes for control devices'''
        return self.CheckForError(self._lib.Solution_Get_ControlMode()) #TODO: use enum

    @ControlMode.setter
    def ControlMode(self, Value):
        self.CheckForError(self._lib.Solution_Set_ControlMode(Value))

    @property
    def Converged(self):
        '''Flag to indicate whether the circuit solution converged'''
        return self.CheckForError(self._lib.Solution_Get_Converged()) != 0

    @Converged.setter
    def Converged(self, Value):
        self.CheckForError(self._lib.Solution_Set_Converged(Value))

    @property
    def DefaultDaily(self):
        '''Default daily load shape (defaults to "Default")'''
        return self._get_string(self.CheckForError(self._lib.Solution_Get_DefaultDaily()))

    @DefaultDaily.setter
    def DefaultDaily(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Solution_Set_DefaultDaily(Value))

    @property
    def DefaultYearly(self):
        '''Default Yearly load shape (defaults to "Default")'''
        return self._get_string(self.CheckForError(self._lib.Solution_Get_DefaultYearly()))

    @DefaultYearly.setter
    def DefaultYearly(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Solution_Set_DefaultYearly(Value))

    @property
    def EventLog(self):
        '''(read-only) Array of strings containing the Event Log'''
        return self.CheckForError(self._get_string_array(self._lib.Solution_Get_EventLog))

    @property
    def Frequency(self):
        '''Set the Frequency for next solution'''
        return self.CheckForError(self._lib.Solution_Get_Frequency())

    @Frequency.setter
    def Frequency(self, Value):
        self.CheckForError(self._lib.Solution_Set_Frequency(Value))

    @property
    def GenMult(self):
        '''Default Multiplier applied to generators (like LoadMult)'''
        return self.CheckForError(self._lib.Solution_Get_GenMult())

    @GenMult.setter
    def GenMult(self, Value):
        self.CheckForError(self._lib.Solution_Set_GenMult(Value))

    @property
    def GenPF(self):
        '''PF for generators in AutoAdd mode'''
        return self.CheckForError(self._lib.Solution_Get_GenPF())

    @GenPF.setter
    def GenPF(self, Value):
        self.CheckForError(self._lib.Solution_Set_GenPF(Value))

    @property
    def GenkW(self):
        '''Generator kW for AutoAdd mode'''
        return self.CheckForError(self._lib.Solution_Get_GenkW())

    @GenkW.setter
    def GenkW(self, Value):
        self.CheckForError(self._lib.Solution_Set_GenkW(Value))

    @property
    def Hour(self):
        '''Set Hour for time series solutions.'''
        return self.CheckForError(self._lib.Solution_Get_Hour())

    @Hour.setter
    def Hour(self, Value):
        self.CheckForError(self._lib.Solution_Set_Hour(Value))

    @property
    def IntervalHrs(self):
        '''
        Get/Set the Solution.IntervalHrs variable used for devices that integrate / custom solution algorithms
        '''
        return self.CheckForError(self._lib.Solution_Get_IntervalHrs())

    @IntervalHrs.setter
    def IntervalHrs(self, Value):
        self.CheckForError(self._lib.Solution_Set_IntervalHrs(Value))

    @property
    def Iterations(self):
        '''(read-only) Number of iterations taken for last solution. (Same as TotalIterations)'''
        return self.CheckForError(self._lib.Solution_Get_Iterations())

    @property
    def LDCurve(self):
        '''Load-Duration Curve name for LD modes'''
        return self._get_string(self.CheckForError(self._lib.Solution_Get_LDCurve()))

    @LDCurve.setter
    def LDCurve(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Solution_Set_LDCurve(Value))

    @property
    def LoadModel(self):
        '''Load Model: {dssPowerFlow (default) | dssAdmittance}'''
        return self.CheckForError(self._lib.Solution_Get_LoadModel())

    @LoadModel.setter
    def LoadModel(self, Value):
        self.CheckForError(self._lib.Solution_Set_LoadModel(Value))

    @property
    def LoadMult(self):
        '''Default load multiplier applied to all non-fixed loads'''
        return self.CheckForError(self._lib.Solution_Get_LoadMult())

    @LoadMult.setter
    def LoadMult(self, Value):
        self.CheckForError(self._lib.Solution_Set_LoadMult(Value))

    @property
    def MaxControlIterations(self):
        '''Maximum allowable control iterations'''
        return self.CheckForError(self._lib.Solution_Get_MaxControlIterations())

    @MaxControlIterations.setter
    def MaxControlIterations(self, Value):
        self.CheckForError(self._lib.Solution_Set_MaxControlIterations(Value))

    @property
    def MaxIterations(self):
        '''Max allowable iterations.'''
        return self.CheckForError(self._lib.Solution_Get_MaxIterations())

    @MaxIterations.setter
    def MaxIterations(self, Value):
        self.CheckForError(self._lib.Solution_Set_MaxIterations(Value))

    @property
    def MinIterations(self):
        '''Minimum number of iterations required for a power flow solution.'''
        return self.CheckForError(self._lib.Solution_Get_MinIterations())

    @MinIterations.setter
    def MinIterations(self, Value):
        self.CheckForError(self._lib.Solution_Set_MinIterations(Value))

    @property
    def Mode(self):
        '''Set present solution mode (by a text code - see DSS Help)'''
        return self.CheckForError(self._lib.Solution_Get_Mode())

    @Mode.setter
    def Mode(self, Value):
        self.CheckForError(self._lib.Solution_Set_Mode(Value)) #TODO: use enum

    @property
    def ModeID(self):
        '''(read-only) ID (text) of the present solution mode'''
        return self._get_string(self.CheckForError(self._lib.Solution_Get_ModeID()))

    @property
    def MostIterationsDone(self):
        '''(read-only) Max number of iterations required to converge at any control iteration of the most recent solution.'''
        return self.CheckForError(self._lib.Solution_Get_MostIterationsDone())

    @property
    def Number(self):
        '''Number of solutions to perform for Monte Carlo and time series simulations'''
        return self.CheckForError(self._lib.Solution_Get_Number())

    @Number.setter
    def Number(self, Value):
        self.CheckForError(self._lib.Solution_Set_Number(Value))

    @property
    def Process_Time(self):
        '''(read-only) Gets the time required to perform the latest solution (Read only)'''
        return self.CheckForError(self._lib.Solution_Get_Process_Time())

    @property
    def Random(self):
        '''Randomization mode for random variables "Gaussian" or "Uniform"'''
        return self.CheckForError(self._lib.Solution_Get_Random())

    @Random.setter
    def Random(self, Value):
        self.CheckForError(self._lib.Solution_Set_Random(Value))

    @property
    def Seconds(self):
        '''Seconds from top of the hour.'''
        return self.CheckForError(self._lib.Solution_Get_Seconds())

    @Seconds.setter
    def Seconds(self, Value):
        self.CheckForError(self._lib.Solution_Set_Seconds(Value))

    @property
    def StepSize(self):
        '''Time step size in sec'''
        return self.CheckForError(self._lib.Solution_Get_StepSize())

    @StepSize.setter
    def StepSize(self, Value):
        self.CheckForError(self._lib.Solution_Set_StepSize(Value))

    @property
    def SystemYChanged(self):
        '''(read-only) Flag that indicates if elements of the System Y have been changed by recent activity.'''
        return self.CheckForError(self._lib.Solution_Get_SystemYChanged() != 0)

    @property
    def Time_of_Step(self):
        '''(read-only) Get the solution process time + sample time for time step'''
        return self.CheckForError(self._lib.Solution_Get_Time_of_Step())

    @property
    def Tolerance(self):
        '''Solution convergence tolerance.'''
        return self.CheckForError(self._lib.Solution_Get_Tolerance())

    @Tolerance.setter
    def Tolerance(self, Value):
        self.CheckForError(self._lib.Solution_Set_Tolerance(Value))

    @property
    def Total_Time(self):
        '''
        Gets/sets the accumulated time of the simulation
        '''
        return self.CheckForError(self._lib.Solution_Get_Total_Time())

    @Total_Time.setter
    def Total_Time(self, Value):
        self.CheckForError(self._lib.Solution_Set_Total_Time(Value))

    @property
    def Totaliterations(self):
        '''(read-only) Total iterations including control iterations for most recent solution.'''
        return self.CheckForError(self._lib.Solution_Get_Totaliterations())

    @property
    def Year(self):
        '''Set year for planning studies'''
        return self.CheckForError(self._lib.Solution_Get_Year())

    @Year.setter
    def Year(self, Value):
        self.CheckForError(self._lib.Solution_Set_Year(Value))

    @property
    def dblHour(self):
        '''Hour as a double, including fractional part'''
        return self.CheckForError(self._lib.Solution_Get_dblHour())

    @dblHour.setter
    def dblHour(self, Value):
        self.CheckForError(self._lib.Solution_Set_dblHour(Value))

    @property
    def pctGrowth(self):
        '''Percent default  annual load growth rate'''
        return self.CheckForError(self._lib.Solution_Get_pctGrowth())

    @pctGrowth.setter
    def pctGrowth(self, Value):
        self.CheckForError(self._lib.Solution_Set_pctGrowth(Value))

    @property
    def StepsizeHr(self):
        '''(write-only) Set Stepsize in Hr'''
        raise AttributeError("This property is write-only!")

    @StepsizeHr.setter
    def StepsizeHr(self, Value):
        self.CheckForError(self._lib.Solution_Set_StepsizeHr(Value))

    @property
    def StepsizeMin(self):
        '''(write-only) Set Stepsize in minutes'''
        raise AttributeError("This property is write-only!")

    @StepsizeMin.setter
    def StepsizeMin(self, Value):
        self.CheckForError(self._lib.Solution_Set_StepsizeMin(Value))

    # The following are officially available only in v8
    @property
    def BusLevels(self):
        self.CheckForError(self._lib.Solution_Get_BusLevels_GR())
        return self._get_int32_gr_array()

    @property
    def IncMatrix(self):
        self.CheckForError(self._lib.Solution_Get_IncMatrix_GR())
        return self._get_int32_gr_array()

    @property
    def IncMatrixCols(self):
        return self.CheckForError(self._get_string_array(self._lib.Solution_Get_IncMatrixCols))

    @property
    def IncMatrixRows(self):
        return self.CheckForError(self._get_string_array(self._lib.Solution_Get_IncMatrixRows))

    @property
    def Laplacian(self):
        self.CheckForError(self._lib.Solution_Get_Laplacian_GR())
        return self._get_int32_gr_array()

    def SolveAll(self):
        self.CheckForError(self._lib.Solution_SolveAll())
        
