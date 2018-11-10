'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class ISolution(Base):
    __slots__ = []

    def BuildYMatrix(self, BuildOption, AllocateVI):
        self._lib.Solution_BuildYMatrix(BuildOption, AllocateVI)
        self.CheckForError()

    def CheckControls(self):
        self._lib.Solution_CheckControls()
        self.CheckForError()

    def CheckFaultStatus(self):
        self._lib.Solution_CheckFaultStatus()
        self.CheckForError()

    def Cleanup(self):
        self._lib.Solution_Cleanup()
        self.CheckForError()

    def DoControlActions(self):
        self._lib.Solution_DoControlActions()
        self.CheckForError()

    def FinishTimeStep(self):
        self._lib.Solution_FinishTimeStep()
        self.CheckForError()

    def InitSnap(self):
        self._lib.Solution_InitSnap()
        self.CheckForError()

    def SampleControlDevices(self):
        self._lib.Solution_SampleControlDevices()
        self.CheckForError()

    def Sample_DoControlActions(self):
        self._lib.Solution_Sample_DoControlActions()
        self.CheckForError()

    def Solve(self):
        self._lib.Solution_Solve()
        self.CheckForError()

    def SolveDirect(self):
        self._lib.Solution_SolveDirect()
        self.CheckForError()

    def SolveNoControl(self):
        self._lib.Solution_SolveNoControl()
        self.CheckForError()

    def SolvePflow(self):
        self._lib.Solution_SolvePflow()
        self.CheckForError()

    def SolvePlusControl(self):
        self._lib.Solution_SolvePlusControl()
        self.CheckForError()

    def SolveSnap(self):
        self._lib.Solution_SolveSnap()
        self.CheckForError()

    @property
    def AddType(self):
        '''Type of device to add in AutoAdd Mode: {dssGen (Default) | dssCap}'''
        return self._lib.Solution_Get_AddType()

    @AddType.setter
    def AddType(self, Value):
        self._lib.Solution_Set_AddType(Value)
        self.CheckForError()

    @property
    def Algorithm(self):
        '''Base Solution algorithm: {dssNormalSolve | dssNewtonSolve}'''
        return self._lib.Solution_Get_Algorithm()

    @Algorithm.setter
    def Algorithm(self, Value):
        self._lib.Solution_Set_Algorithm(Value)
        self.CheckForError()

    @property
    def Capkvar(self):
        '''Capacitor kvar for adding capacitors in AutoAdd mode'''
        return self._lib.Solution_Get_Capkvar()

    @Capkvar.setter
    def Capkvar(self, Value):
        self._lib.Solution_Set_Capkvar(Value)
        self.CheckForError()

    @property
    def ControlActionsDone(self):
        '''Flag indicating the control actions are done.'''
        return self._lib.Solution_Get_ControlActionsDone() != 0

    @ControlActionsDone.setter
    def ControlActionsDone(self, Value):
        self._lib.Solution_Set_ControlActionsDone(Value)
        self.CheckForError()

    @property
    def ControlIterations(self):
        '''Value of the control iteration counter'''
        return self._lib.Solution_Get_ControlIterations()

    @ControlIterations.setter
    def ControlIterations(self, Value):
        self._lib.Solution_Set_ControlIterations(Value)
        self.CheckForError()

    @property
    def ControlMode(self):
        '''{dssStatic* | dssEvent | dssTime}  Modes for control devices'''
        return self._lib.Solution_Get_ControlMode()

    @ControlMode.setter
    def ControlMode(self, Value):
        self._lib.Solution_Set_ControlMode(Value)
        self.CheckForError()

    @property
    def Converged(self):
        '''Flag to indicate whether the circuit solution converged'''
        return self._lib.Solution_Get_Converged() != 0

    @Converged.setter
    def Converged(self, Value):
        self._lib.Solution_Set_Converged(Value)
        self.CheckForError()

    @property
    def DefaultDaily(self):
        '''Default daily load shape (defaults to "Default")'''
        return self._get_string(self._lib.Solution_Get_DefaultDaily())

    @DefaultDaily.setter
    def DefaultDaily(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Solution_Set_DefaultDaily(Value)
        self.CheckForError()

    @property
    def DefaultYearly(self):
        '''Default Yearly load shape (defaults to "Default")'''
        return self._get_string(self._lib.Solution_Get_DefaultYearly())

    @DefaultYearly.setter
    def DefaultYearly(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Solution_Set_DefaultYearly(Value)
        self.CheckForError()

    @property
    def EventLog(self):
        '''(read-only) Array of strings containing the Event Log'''
        return self._get_string_array(self._lib.Solution_Get_EventLog)

    @property
    def Frequency(self):
        '''Set the Frequency for next solution'''
        return self._lib.Solution_Get_Frequency()

    @Frequency.setter
    def Frequency(self, Value):
        self._lib.Solution_Set_Frequency(Value)
        self.CheckForError()

    @property
    def GenMult(self):
        '''Default Multiplier applied to generators (like LoadMult)'''
        return self._lib.Solution_Get_GenMult()

    @GenMult.setter
    def GenMult(self, Value):
        self._lib.Solution_Set_GenMult(Value)
        self.CheckForError()

    @property
    def GenPF(self):
        '''PF for generators in AutoAdd mode'''
        return self._lib.Solution_Get_GenPF()

    @GenPF.setter
    def GenPF(self, Value):
        self._lib.Solution_Set_GenPF(Value)
        self.CheckForError()

    @property
    def GenkW(self):
        '''Generator kW for AutoAdd mode'''
        return self._lib.Solution_Get_GenkW()

    @GenkW.setter
    def GenkW(self, Value):
        self._lib.Solution_Set_GenkW(Value)
        self.CheckForError()

    @property
    def Hour(self):
        '''Set Hour for time series solutions.'''
        return self._lib.Solution_Get_Hour()

    @Hour.setter
    def Hour(self, Value):
        self._lib.Solution_Set_Hour(Value)
        self.CheckForError()

    @property
    def IntervalHrs(self):
        '''
        (read) Get/Set the Solution.IntervalHrs variable used for devices that integrate
        (write) Get/Set the Solution.IntervalHrs variable for custom solution algorithms
        '''
        return self._lib.Solution_Get_IntervalHrs()

    @IntervalHrs.setter
    def IntervalHrs(self, Value):
        self._lib.Solution_Set_IntervalHrs(Value)
        self.CheckForError()

    @property
    def Iterations(self):
        '''(read-only) Number of iterations taken for last solution. (Same as TotalIterations)'''
        return self._lib.Solution_Get_Iterations()

    @property
    def LDCurve(self):
        '''Load-Duration Curve name for LD modes'''
        return self._get_string(self._lib.Solution_Get_LDCurve())

    @LDCurve.setter
    def LDCurve(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Solution_Set_LDCurve(Value)
        self.CheckForError()

    @property
    def LoadModel(self):
        '''Load Model: {dssPowerFlow (default) | dssAdmittance}'''
        return self._lib.Solution_Get_LoadModel()

    @LoadModel.setter
    def LoadModel(self, Value):
        self._lib.Solution_Set_LoadModel(Value)
        self.CheckForError()

    @property
    def LoadMult(self):
        '''Default load multiplier applied to all non-fixed loads'''
        return self._lib.Solution_Get_LoadMult()

    @LoadMult.setter
    def LoadMult(self, Value):
        self._lib.Solution_Set_LoadMult(Value)
        self.CheckForError()

    @property
    def MaxControlIterations(self):
        '''Maximum allowable control iterations'''
        return self._lib.Solution_Get_MaxControlIterations()

    @MaxControlIterations.setter
    def MaxControlIterations(self, Value):
        self._lib.Solution_Set_MaxControlIterations(Value)
        self.CheckForError()

    @property
    def MaxIterations(self):
        '''Max allowable iterations.'''
        return self._lib.Solution_Get_MaxIterations()

    @MaxIterations.setter
    def MaxIterations(self, Value):
        self._lib.Solution_Set_MaxIterations(Value)
        self.CheckForError()

    @property
    def MinIterations(self):
        '''
        (read) Minimum number of iterations required for a power flow solution.
        (write) Mininum number of iterations required for a power flow solution.
        '''
        return self._lib.Solution_Get_MinIterations()

    @MinIterations.setter
    def MinIterations(self, Value):
        self._lib.Solution_Set_MinIterations(Value)
        self.CheckForError()

    @property
    def Mode(self):
        '''Set present solution mode (by a text code - see DSS Help)'''
        return self._lib.Solution_Get_Mode()

    @Mode.setter
    def Mode(self, Mode):
        self._lib.Solution_Set_Mode(Mode)
        self.CheckForError()

    @property
    def ModeID(self):
        '''(read-only) ID (text) of the present solution mode'''
        return self._get_string(self._lib.Solution_Get_ModeID())

    @property
    def MostIterationsDone(self):
        '''(read-only) Max number of iterations required to converge at any control iteration of the most recent solution.'''
        return self._lib.Solution_Get_MostIterationsDone()

    @property
    def Number(self):
        '''Number of solutions to perform for Monte Carlo and time series simulations'''
        return self._lib.Solution_Get_Number()

    @Number.setter
    def Number(self, Value):
        self._lib.Solution_Set_Number(Value)
        self.CheckForError()

    @property
    def Process_Time(self):
        '''(read-only) Gets the time required to perform the latest solution (Read only)'''
        return self._lib.Solution_Get_Process_Time()

    @property
    def Random(self):
        '''Randomization mode for random variables "Gaussian" or "Uniform"'''
        return self._lib.Solution_Get_Random()

    @Random.setter
    def Random(self, Random):
        self._lib.Solution_Set_Random(Random)
        self.CheckForError()

    @property
    def Seconds(self):
        '''Seconds from top of the hour.'''
        return self._lib.Solution_Get_Seconds()

    @Seconds.setter
    def Seconds(self, Value):
        self._lib.Solution_Set_Seconds(Value)
        self.CheckForError()

    @property
    def StepSize(self):
        '''Time step size in sec'''
        return self._lib.Solution_Get_StepSize()

    @StepSize.setter
    def StepSize(self, Value):
        self._lib.Solution_Set_StepSize(Value)
        self.CheckForError()

    @property
    def SystemYChanged(self):
        '''(read-only) Flag that indicates if elements of the System Y have been changed by recent activity.'''
        return self._lib.Solution_Get_SystemYChanged() != 0

    @property
    def Time_of_Step(self):
        '''(read-only) Get the solution process time + sample time for time step'''
        return self._lib.Solution_Get_Time_of_Step()

    @property
    def Tolerance(self):
        '''Solution convergence tolerance.'''
        return self._lib.Solution_Get_Tolerance()

    @Tolerance.setter
    def Tolerance(self, Value):
        self._lib.Solution_Set_Tolerance(Value)
        self.CheckForError()

    @property
    def Total_Time(self):
        '''
        (read) Gets the accumulated time of the simulation
        (write) Sets the Accumulated time of the simulation
        '''
        return self._lib.Solution_Get_Total_Time()

    @Total_Time.setter
    def Total_Time(self, Value):
        self._lib.Solution_Set_Total_Time(Value)
        self.CheckForError()

    @property
    def Totaliterations(self):
        '''(read-only) Total iterations including control iterations for most recent solution.'''
        return self._lib.Solution_Get_Totaliterations()

    @property
    def Year(self):
        '''Set year for planning studies'''
        return self._lib.Solution_Get_Year()

    @Year.setter
    def Year(self, Value):
        self._lib.Solution_Set_Year(Value)
        self.CheckForError()

    @property
    def dblHour(self):
        '''Hour as a double, including fractional part'''
        return self._lib.Solution_Get_dblHour()

    @dblHour.setter
    def dblHour(self, Value):
        self._lib.Solution_Set_dblHour(Value)
        self.CheckForError()

    @property
    def pctGrowth(self):
        '''Percent default  annual load growth rate'''
        return self._lib.Solution_Get_pctGrowth()

    @pctGrowth.setter
    def pctGrowth(self, Value):
        self._lib.Solution_Set_pctGrowth(Value)
        self.CheckForError()

    @property
    def StepsizeHr(self):
        '''(write-only) Set Stepsize in Hr'''
        raise AttributeError("This property is write-only!")

    @StepsizeHr.setter
    def StepsizeHr(self, Value):
        self._lib.Solution_Set_StepsizeHr(Value)
        self.CheckForError()

    @property
    def StepsizeMin(self):
        '''(write-only) Set Stepsize in minutes'''
        raise AttributeError("This property is write-only!")

    @StepsizeMin.setter
    def StepsizeMin(self, Value):
        self._lib.Solution_Set_StepsizeMin(Value)
        self.CheckForError()

    # The following are officially available only in v8
    @property
    def BusLevels(self):
        self._lib.Solution_Get_BusLevels_GR()
        return self._get_int32_gr_array()

    @property
    def IncMatrix(self):
        self._lib.Solution_Get_IncMatrix_GR()
        return self._get_int32_gr_array()

    @property
    def IncMatrixCols(self):
        return self._get_string_array(self._lib.Solution_Get_IncMatrixCols)

    @property
    def IncMatrixRows(self):
        return self._get_string_array(self._lib.Solution_Get_IncMatrixRows)

    @property
    def Laplacian(self):
        self._lib.Solution_Get_Laplacian_GR()
        return self._get_int32_gr_array()

    def SolveAll(self):
        self._lib.Solution_SolveAll()
        self.CheckForError()
        
