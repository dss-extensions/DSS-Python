# {py:mod}`dss.ILoads`

```{py:module} dss.ILoads
```

```{autodoc2-docstring} dss.ILoads
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ILoads <dss.ILoads.ILoads>`
  - ```{autodoc2-docstring} dss.ILoads.ILoads
    :summary:
    ```
````

### API

`````{py:class} ILoads(api_util)
:canonical: dss.ILoads.ILoads

Bases: {py:obj}`dss._cffi_api_util.Iterable`

```{autodoc2-docstring} dss.ILoads.ILoads
```

````{py:property} AllNames
:canonical: dss.ILoads.ILoads.AllNames
:type: typing.List[str]

```{autodoc2-docstring} dss.ILoads.ILoads.AllNames
```

````

````{py:property} AllocationFactor
:canonical: dss.ILoads.ILoads.AllocationFactor
:type: float

```{autodoc2-docstring} dss.ILoads.ILoads.AllocationFactor
```

````

````{py:property} CVRcurve
:canonical: dss.ILoads.ILoads.CVRcurve
:type: str

```{autodoc2-docstring} dss.ILoads.ILoads.CVRcurve
```

````

````{py:property} CVRvars
:canonical: dss.ILoads.ILoads.CVRvars
:type: float

```{autodoc2-docstring} dss.ILoads.ILoads.CVRvars
```

````

````{py:property} CVRwatts
:canonical: dss.ILoads.ILoads.CVRwatts
:type: float

```{autodoc2-docstring} dss.ILoads.ILoads.CVRwatts
```

````

````{py:property} Cfactor
:canonical: dss.ILoads.ILoads.Cfactor
:type: float

```{autodoc2-docstring} dss.ILoads.ILoads.Cfactor
```

````

````{py:property} Class
:canonical: dss.ILoads.ILoads.Class
:type: int

```{autodoc2-docstring} dss.ILoads.ILoads.Class
```

````

````{py:property} Count
:canonical: dss.ILoads.ILoads.Count
:type: int

```{autodoc2-docstring} dss.ILoads.ILoads.Count
```

````

````{py:property} First
:canonical: dss.ILoads.ILoads.First
:type: int

```{autodoc2-docstring} dss.ILoads.ILoads.First
```

````

````{py:property} Growth
:canonical: dss.ILoads.ILoads.Growth
:type: str

```{autodoc2-docstring} dss.ILoads.ILoads.Growth
```

````

````{py:property} IsDelta
:canonical: dss.ILoads.ILoads.IsDelta
:type: bool

```{autodoc2-docstring} dss.ILoads.ILoads.IsDelta
```

````

````{py:property} Model
:canonical: dss.ILoads.ILoads.Model
:type: dss.enums.LoadModels

```{autodoc2-docstring} dss.ILoads.ILoads.Model
```

````

````{py:property} Name
:canonical: dss.ILoads.ILoads.Name
:type: str

```{autodoc2-docstring} dss.ILoads.ILoads.Name
```

````

````{py:property} Next
:canonical: dss.ILoads.ILoads.Next
:type: int

```{autodoc2-docstring} dss.ILoads.ILoads.Next
```

````

````{py:property} NumCust
:canonical: dss.ILoads.ILoads.NumCust
:type: int

```{autodoc2-docstring} dss.ILoads.ILoads.NumCust
```

````

````{py:property} PF
:canonical: dss.ILoads.ILoads.PF
:type: float

```{autodoc2-docstring} dss.ILoads.ILoads.PF
```

````

````{py:property} PctMean
:canonical: dss.ILoads.ILoads.PctMean
:type: float

```{autodoc2-docstring} dss.ILoads.ILoads.PctMean
```

````

````{py:property} PctStdDev
:canonical: dss.ILoads.ILoads.PctStdDev
:type: float

```{autodoc2-docstring} dss.ILoads.ILoads.PctStdDev
```

````

````{py:property} Phases
:canonical: dss.ILoads.ILoads.Phases
:type: int

```{autodoc2-docstring} dss.ILoads.ILoads.Phases
```

````

````{py:property} RelWeight
:canonical: dss.ILoads.ILoads.RelWeight
:type: float

```{autodoc2-docstring} dss.ILoads.ILoads.RelWeight
```

````

````{py:property} Rneut
:canonical: dss.ILoads.ILoads.Rneut
:type: float

```{autodoc2-docstring} dss.ILoads.ILoads.Rneut
```

````

````{py:property} Sensor
:canonical: dss.ILoads.ILoads.Sensor
:type: str

```{autodoc2-docstring} dss.ILoads.ILoads.Sensor
```

````

````{py:property} Spectrum
:canonical: dss.ILoads.ILoads.Spectrum
:type: str

```{autodoc2-docstring} dss.ILoads.ILoads.Spectrum
```

````

````{py:property} Status
:canonical: dss.ILoads.ILoads.Status
:type: dss.enums.LoadStatus

```{autodoc2-docstring} dss.ILoads.ILoads.Status
```

````

````{py:property} Vmaxpu
:canonical: dss.ILoads.ILoads.Vmaxpu
:type: float

```{autodoc2-docstring} dss.ILoads.ILoads.Vmaxpu
```

````

````{py:property} Vminemerg
:canonical: dss.ILoads.ILoads.Vminemerg
:type: float

```{autodoc2-docstring} dss.ILoads.ILoads.Vminemerg
```

````

````{py:property} Vminnorm
:canonical: dss.ILoads.ILoads.Vminnorm
:type: float

```{autodoc2-docstring} dss.ILoads.ILoads.Vminnorm
```

````

````{py:property} Vminpu
:canonical: dss.ILoads.ILoads.Vminpu
:type: float

```{autodoc2-docstring} dss.ILoads.ILoads.Vminpu
```

````

````{py:property} Xneut
:canonical: dss.ILoads.ILoads.Xneut
:type: float

```{autodoc2-docstring} dss.ILoads.ILoads.Xneut
```

````

````{py:property} Yearly
:canonical: dss.ILoads.ILoads.Yearly
:type: str

```{autodoc2-docstring} dss.ILoads.ILoads.Yearly
```

````

````{py:property} ZIPV
:canonical: dss.ILoads.ILoads.ZIPV
:type: dss._types.Float64Array

```{autodoc2-docstring} dss.ILoads.ILoads.ZIPV
```

````

````{py:method} __init__(api_util)
:canonical: dss.ILoads.ILoads.__init__

```{autodoc2-docstring} dss.ILoads.ILoads.__init__
```

````

````{py:method} __iter__() -> typing.Iterator[dss._cffi_api_util.Iterable]
:canonical: dss.ILoads.ILoads.__iter__

```{autodoc2-docstring} dss.ILoads.ILoads.__iter__
```

````

````{py:method} __len__() -> int
:canonical: dss.ILoads.ILoads.__len__

```{autodoc2-docstring} dss.ILoads.ILoads.__len__
```

````

````{py:property} daily
:canonical: dss.ILoads.ILoads.daily
:type: str

```{autodoc2-docstring} dss.ILoads.ILoads.daily
```

````

````{py:property} duty
:canonical: dss.ILoads.ILoads.duty
:type: str

```{autodoc2-docstring} dss.ILoads.ILoads.duty
```

````

````{py:property} idx
:canonical: dss.ILoads.ILoads.idx
:type: int

```{autodoc2-docstring} dss.ILoads.ILoads.idx
```

````

````{py:property} kV
:canonical: dss.ILoads.ILoads.kV
:type: float

```{autodoc2-docstring} dss.ILoads.ILoads.kV
```

````

````{py:property} kW
:canonical: dss.ILoads.ILoads.kW
:type: float

```{autodoc2-docstring} dss.ILoads.ILoads.kW
```

````

````{py:property} kva
:canonical: dss.ILoads.ILoads.kva
:type: float

```{autodoc2-docstring} dss.ILoads.ILoads.kva
```

````

````{py:property} kvar
:canonical: dss.ILoads.ILoads.kvar
:type: float

```{autodoc2-docstring} dss.ILoads.ILoads.kvar
```

````

````{py:property} kwh
:canonical: dss.ILoads.ILoads.kwh
:type: float

```{autodoc2-docstring} dss.ILoads.ILoads.kwh
```

````

````{py:property} kwhdays
:canonical: dss.ILoads.ILoads.kwhdays
:type: float

```{autodoc2-docstring} dss.ILoads.ILoads.kwhdays
```

````

````{py:property} pctSeriesRL
:canonical: dss.ILoads.ILoads.pctSeriesRL
:type: float

```{autodoc2-docstring} dss.ILoads.ILoads.pctSeriesRL
```

````

````{py:property} xfkVA
:canonical: dss.ILoads.ILoads.xfkVA
:type: float

```{autodoc2-docstring} dss.ILoads.ILoads.xfkVA
```

````

`````
