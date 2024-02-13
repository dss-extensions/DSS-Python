# {py:mod}`dss.ISolution`

```{py:module} dss.ISolution
```

```{autodoc2-docstring} dss.ISolution
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ISolution <dss.ISolution.ISolution>`
  - ```{autodoc2-docstring} dss.ISolution.ISolution
    :summary:
    ```
````

### API

`````{py:class} ISolution(api_util, prefer_lists=False)
:canonical: dss.ISolution.ISolution

Bases: {py:obj}`dss._cffi_api_util.Base`

```{autodoc2-docstring} dss.ISolution.ISolution
```

````{py:property} AddType
:canonical: dss.ISolution.ISolution.AddType
:type: int

```{autodoc2-docstring} dss.ISolution.ISolution.AddType
```

````

````{py:property} Algorithm
:canonical: dss.ISolution.ISolution.Algorithm
:type: dss.enums.SolutionAlgorithms

```{autodoc2-docstring} dss.ISolution.ISolution.Algorithm
```

````

````{py:method} BuildYMatrix(BuildOption: int, AllocateVI: bool)
:canonical: dss.ISolution.ISolution.BuildYMatrix

```{autodoc2-docstring} dss.ISolution.ISolution.BuildYMatrix
```

````

````{py:property} BusLevels
:canonical: dss.ISolution.ISolution.BusLevels
:type: dss._types.Int32Array

```{autodoc2-docstring} dss.ISolution.ISolution.BusLevels
```

````

````{py:property} Capkvar
:canonical: dss.ISolution.ISolution.Capkvar
:type: float

```{autodoc2-docstring} dss.ISolution.ISolution.Capkvar
```

````

````{py:method} CheckControls()
:canonical: dss.ISolution.ISolution.CheckControls

```{autodoc2-docstring} dss.ISolution.ISolution.CheckControls
```

````

````{py:method} CheckFaultStatus()
:canonical: dss.ISolution.ISolution.CheckFaultStatus

```{autodoc2-docstring} dss.ISolution.ISolution.CheckFaultStatus
```

````

````{py:method} Cleanup()
:canonical: dss.ISolution.ISolution.Cleanup

```{autodoc2-docstring} dss.ISolution.ISolution.Cleanup
```

````

````{py:property} ControlActionsDone
:canonical: dss.ISolution.ISolution.ControlActionsDone
:type: bool

```{autodoc2-docstring} dss.ISolution.ISolution.ControlActionsDone
```

````

````{py:property} ControlIterations
:canonical: dss.ISolution.ISolution.ControlIterations
:type: int

```{autodoc2-docstring} dss.ISolution.ISolution.ControlIterations
```

````

````{py:property} ControlMode
:canonical: dss.ISolution.ISolution.ControlMode
:type: dss.enums.ControlModes

```{autodoc2-docstring} dss.ISolution.ISolution.ControlMode
```

````

````{py:property} Converged
:canonical: dss.ISolution.ISolution.Converged
:type: bool

```{autodoc2-docstring} dss.ISolution.ISolution.Converged
```

````

````{py:property} DefaultDaily
:canonical: dss.ISolution.ISolution.DefaultDaily
:type: str

```{autodoc2-docstring} dss.ISolution.ISolution.DefaultDaily
```

````

````{py:property} DefaultYearly
:canonical: dss.ISolution.ISolution.DefaultYearly
:type: str

```{autodoc2-docstring} dss.ISolution.ISolution.DefaultYearly
```

````

````{py:method} DoControlActions()
:canonical: dss.ISolution.ISolution.DoControlActions

```{autodoc2-docstring} dss.ISolution.ISolution.DoControlActions
```

````

````{py:property} EventLog
:canonical: dss.ISolution.ISolution.EventLog
:type: typing.List[str]

```{autodoc2-docstring} dss.ISolution.ISolution.EventLog
```

````

````{py:method} FinishTimeStep()
:canonical: dss.ISolution.ISolution.FinishTimeStep

```{autodoc2-docstring} dss.ISolution.ISolution.FinishTimeStep
```

````

````{py:property} Frequency
:canonical: dss.ISolution.ISolution.Frequency
:type: float

```{autodoc2-docstring} dss.ISolution.ISolution.Frequency
```

````

````{py:property} GenMult
:canonical: dss.ISolution.ISolution.GenMult
:type: float

```{autodoc2-docstring} dss.ISolution.ISolution.GenMult
```

````

````{py:property} GenPF
:canonical: dss.ISolution.ISolution.GenPF
:type: float

```{autodoc2-docstring} dss.ISolution.ISolution.GenPF
```

````

````{py:property} GenkW
:canonical: dss.ISolution.ISolution.GenkW
:type: float

```{autodoc2-docstring} dss.ISolution.ISolution.GenkW
```

````

````{py:property} Hour
:canonical: dss.ISolution.ISolution.Hour
:type: int

```{autodoc2-docstring} dss.ISolution.ISolution.Hour
```

````

````{py:property} IncMatrix
:canonical: dss.ISolution.ISolution.IncMatrix
:type: dss._types.Int32Array

```{autodoc2-docstring} dss.ISolution.ISolution.IncMatrix
```

````

````{py:property} IncMatrixCols
:canonical: dss.ISolution.ISolution.IncMatrixCols
:type: typing.List[str]

```{autodoc2-docstring} dss.ISolution.ISolution.IncMatrixCols
```

````

````{py:property} IncMatrixRows
:canonical: dss.ISolution.ISolution.IncMatrixRows
:type: typing.List[str]

```{autodoc2-docstring} dss.ISolution.ISolution.IncMatrixRows
```

````

````{py:method} InitSnap()
:canonical: dss.ISolution.ISolution.InitSnap

```{autodoc2-docstring} dss.ISolution.ISolution.InitSnap
```

````

````{py:property} IntervalHrs
:canonical: dss.ISolution.ISolution.IntervalHrs
:type: float

```{autodoc2-docstring} dss.ISolution.ISolution.IntervalHrs
```

````

````{py:property} Iterations
:canonical: dss.ISolution.ISolution.Iterations
:type: int

```{autodoc2-docstring} dss.ISolution.ISolution.Iterations
```

````

````{py:property} LDCurve
:canonical: dss.ISolution.ISolution.LDCurve
:type: str

```{autodoc2-docstring} dss.ISolution.ISolution.LDCurve
```

````

````{py:property} Laplacian
:canonical: dss.ISolution.ISolution.Laplacian
:type: dss._types.Int32Array

```{autodoc2-docstring} dss.ISolution.ISolution.Laplacian
```

````

````{py:property} LoadModel
:canonical: dss.ISolution.ISolution.LoadModel
:type: int

```{autodoc2-docstring} dss.ISolution.ISolution.LoadModel
```

````

````{py:property} LoadMult
:canonical: dss.ISolution.ISolution.LoadMult
:type: float

```{autodoc2-docstring} dss.ISolution.ISolution.LoadMult
```

````

````{py:property} MaxControlIterations
:canonical: dss.ISolution.ISolution.MaxControlIterations
:type: int

```{autodoc2-docstring} dss.ISolution.ISolution.MaxControlIterations
```

````

````{py:property} MaxIterations
:canonical: dss.ISolution.ISolution.MaxIterations
:type: int

```{autodoc2-docstring} dss.ISolution.ISolution.MaxIterations
```

````

````{py:property} MinIterations
:canonical: dss.ISolution.ISolution.MinIterations
:type: int

```{autodoc2-docstring} dss.ISolution.ISolution.MinIterations
```

````

````{py:property} Mode
:canonical: dss.ISolution.ISolution.Mode
:type: dss.enums.SolveModes

```{autodoc2-docstring} dss.ISolution.ISolution.Mode
```

````

````{py:property} ModeID
:canonical: dss.ISolution.ISolution.ModeID
:type: str

```{autodoc2-docstring} dss.ISolution.ISolution.ModeID
```

````

````{py:property} MostIterationsDone
:canonical: dss.ISolution.ISolution.MostIterationsDone
:type: int

```{autodoc2-docstring} dss.ISolution.ISolution.MostIterationsDone
```

````

````{py:property} Number
:canonical: dss.ISolution.ISolution.Number
:type: int

```{autodoc2-docstring} dss.ISolution.ISolution.Number
```

````

````{py:property} Process_Time
:canonical: dss.ISolution.ISolution.Process_Time
:type: float

```{autodoc2-docstring} dss.ISolution.ISolution.Process_Time
```

````

````{py:property} Random
:canonical: dss.ISolution.ISolution.Random
:type: int

```{autodoc2-docstring} dss.ISolution.ISolution.Random
```

````

````{py:method} SampleControlDevices()
:canonical: dss.ISolution.ISolution.SampleControlDevices

```{autodoc2-docstring} dss.ISolution.ISolution.SampleControlDevices
```

````

````{py:method} Sample_DoControlActions()
:canonical: dss.ISolution.ISolution.Sample_DoControlActions

```{autodoc2-docstring} dss.ISolution.ISolution.Sample_DoControlActions
```

````

````{py:property} Seconds
:canonical: dss.ISolution.ISolution.Seconds
:type: float

```{autodoc2-docstring} dss.ISolution.ISolution.Seconds
```

````

````{py:method} Solve()
:canonical: dss.ISolution.ISolution.Solve

```{autodoc2-docstring} dss.ISolution.ISolution.Solve
```

````

````{py:method} SolveAll()
:canonical: dss.ISolution.ISolution.SolveAll

```{autodoc2-docstring} dss.ISolution.ISolution.SolveAll
```

````

````{py:method} SolveDirect()
:canonical: dss.ISolution.ISolution.SolveDirect

```{autodoc2-docstring} dss.ISolution.ISolution.SolveDirect
```

````

````{py:method} SolveNoControl()
:canonical: dss.ISolution.ISolution.SolveNoControl

```{autodoc2-docstring} dss.ISolution.ISolution.SolveNoControl
```

````

````{py:method} SolvePflow()
:canonical: dss.ISolution.ISolution.SolvePflow

```{autodoc2-docstring} dss.ISolution.ISolution.SolvePflow
```

````

````{py:method} SolvePlusControl()
:canonical: dss.ISolution.ISolution.SolvePlusControl

```{autodoc2-docstring} dss.ISolution.ISolution.SolvePlusControl
```

````

````{py:method} SolveSnap()
:canonical: dss.ISolution.ISolution.SolveSnap

```{autodoc2-docstring} dss.ISolution.ISolution.SolveSnap
```

````

````{py:property} StepSize
:canonical: dss.ISolution.ISolution.StepSize
:type: float

```{autodoc2-docstring} dss.ISolution.ISolution.StepSize
```

````

````{py:property} StepsizeHr
:canonical: dss.ISolution.ISolution.StepsizeHr
:type: float

```{autodoc2-docstring} dss.ISolution.ISolution.StepsizeHr
```

````

````{py:property} StepsizeMin
:canonical: dss.ISolution.ISolution.StepsizeMin
:type: float

```{autodoc2-docstring} dss.ISolution.ISolution.StepsizeMin
```

````

````{py:property} SystemYChanged
:canonical: dss.ISolution.ISolution.SystemYChanged
:type: bool

```{autodoc2-docstring} dss.ISolution.ISolution.SystemYChanged
```

````

````{py:property} Time_of_Step
:canonical: dss.ISolution.ISolution.Time_of_Step
:type: float

```{autodoc2-docstring} dss.ISolution.ISolution.Time_of_Step
```

````

````{py:property} Tolerance
:canonical: dss.ISolution.ISolution.Tolerance
:type: float

```{autodoc2-docstring} dss.ISolution.ISolution.Tolerance
```

````

````{py:property} Total_Time
:canonical: dss.ISolution.ISolution.Total_Time
:type: float

```{autodoc2-docstring} dss.ISolution.ISolution.Total_Time
```

````

````{py:property} Totaliterations
:canonical: dss.ISolution.ISolution.Totaliterations
:type: int

```{autodoc2-docstring} dss.ISolution.ISolution.Totaliterations
```

````

````{py:property} Year
:canonical: dss.ISolution.ISolution.Year
:type: int

```{autodoc2-docstring} dss.ISolution.ISolution.Year
```

````

````{py:method} __init__(api_util, prefer_lists=False)
:canonical: dss.ISolution.ISolution.__init__

```{autodoc2-docstring} dss.ISolution.ISolution.__init__
```

````

````{py:property} dblHour
:canonical: dss.ISolution.ISolution.dblHour
:type: float

```{autodoc2-docstring} dss.ISolution.ISolution.dblHour
```

````

````{py:property} pctGrowth
:canonical: dss.ISolution.ISolution.pctGrowth
:type: float

```{autodoc2-docstring} dss.ISolution.ISolution.pctGrowth
```

````

`````
