# {py:mod}`dss.IMeters`

```{py:module} dss.IMeters
```

```{autodoc2-docstring} dss.IMeters
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IMeters <dss.IMeters.IMeters>`
  - ```{autodoc2-docstring} dss.IMeters.IMeters
    :summary:
    ```
````

### API

`````{py:class} IMeters(api_util)
:canonical: dss.IMeters.IMeters

Bases: {py:obj}`dss._cffi_api_util.Iterable`

```{autodoc2-docstring} dss.IMeters.IMeters
```

````{py:property} AllBranchesInZone
:canonical: dss.IMeters.IMeters.AllBranchesInZone
:type: typing.List[str]

```{autodoc2-docstring} dss.IMeters.IMeters.AllBranchesInZone
```

````

````{py:property} AllEndElements
:canonical: dss.IMeters.IMeters.AllEndElements
:type: typing.List[str]

```{autodoc2-docstring} dss.IMeters.IMeters.AllEndElements
```

````

````{py:property} AllNames
:canonical: dss.IMeters.IMeters.AllNames
:type: typing.List[str]

```{autodoc2-docstring} dss.IMeters.IMeters.AllNames
```

````

````{py:property} AllocFactors
:canonical: dss.IMeters.IMeters.AllocFactors
:type: dss._types.Float64Array

```{autodoc2-docstring} dss.IMeters.IMeters.AllocFactors
```

````

````{py:property} AvgRepairTime
:canonical: dss.IMeters.IMeters.AvgRepairTime
:type: float

```{autodoc2-docstring} dss.IMeters.IMeters.AvgRepairTime
```

````

````{py:property} CalcCurrent
:canonical: dss.IMeters.IMeters.CalcCurrent
:type: dss._types.Float64Array

```{autodoc2-docstring} dss.IMeters.IMeters.CalcCurrent
```

````

````{py:method} CloseAllDIFiles()
:canonical: dss.IMeters.IMeters.CloseAllDIFiles

```{autodoc2-docstring} dss.IMeters.IMeters.CloseAllDIFiles
```

````

````{py:property} Count
:canonical: dss.IMeters.IMeters.Count
:type: int

```{autodoc2-docstring} dss.IMeters.IMeters.Count
```

````

````{py:property} CountBranches
:canonical: dss.IMeters.IMeters.CountBranches
:type: int

```{autodoc2-docstring} dss.IMeters.IMeters.CountBranches
```

````

````{py:property} CountEndElements
:canonical: dss.IMeters.IMeters.CountEndElements
:type: int

```{autodoc2-docstring} dss.IMeters.IMeters.CountEndElements
```

````

````{py:property} CustInterrupts
:canonical: dss.IMeters.IMeters.CustInterrupts
:type: float

```{autodoc2-docstring} dss.IMeters.IMeters.CustInterrupts
```

````

````{py:property} DIFilesAreOpen
:canonical: dss.IMeters.IMeters.DIFilesAreOpen
:type: bool

```{autodoc2-docstring} dss.IMeters.IMeters.DIFilesAreOpen
```

````

````{py:method} DoReliabilityCalc(AssumeRestoration: bool)
:canonical: dss.IMeters.IMeters.DoReliabilityCalc

```{autodoc2-docstring} dss.IMeters.IMeters.DoReliabilityCalc
```

````

````{py:property} FaultRateXRepairHrs
:canonical: dss.IMeters.IMeters.FaultRateXRepairHrs
:type: float

```{autodoc2-docstring} dss.IMeters.IMeters.FaultRateXRepairHrs
```

````

````{py:property} First
:canonical: dss.IMeters.IMeters.First
:type: int

```{autodoc2-docstring} dss.IMeters.IMeters.First
```

````

````{py:property} MeteredElement
:canonical: dss.IMeters.IMeters.MeteredElement
:type: str

```{autodoc2-docstring} dss.IMeters.IMeters.MeteredElement
```

````

````{py:property} MeteredTerminal
:canonical: dss.IMeters.IMeters.MeteredTerminal
:type: int

```{autodoc2-docstring} dss.IMeters.IMeters.MeteredTerminal
```

````

````{py:property} Name
:canonical: dss.IMeters.IMeters.Name
:type: str

```{autodoc2-docstring} dss.IMeters.IMeters.Name
```

````

````{py:property} Next
:canonical: dss.IMeters.IMeters.Next
:type: int

```{autodoc2-docstring} dss.IMeters.IMeters.Next
```

````

````{py:property} NumSectionBranches
:canonical: dss.IMeters.IMeters.NumSectionBranches
:type: int

```{autodoc2-docstring} dss.IMeters.IMeters.NumSectionBranches
```

````

````{py:property} NumSectionCustomers
:canonical: dss.IMeters.IMeters.NumSectionCustomers
:type: int

```{autodoc2-docstring} dss.IMeters.IMeters.NumSectionCustomers
```

````

````{py:property} NumSections
:canonical: dss.IMeters.IMeters.NumSections
:type: int

```{autodoc2-docstring} dss.IMeters.IMeters.NumSections
```

````

````{py:property} OCPDeviceType
:canonical: dss.IMeters.IMeters.OCPDeviceType
:type: dss.enums.OCPDevType

```{autodoc2-docstring} dss.IMeters.IMeters.OCPDeviceType
```

````

````{py:method} OpenAllDIFiles()
:canonical: dss.IMeters.IMeters.OpenAllDIFiles

```{autodoc2-docstring} dss.IMeters.IMeters.OpenAllDIFiles
```

````

````{py:property} Peakcurrent
:canonical: dss.IMeters.IMeters.Peakcurrent
:type: dss._types.Float64Array

```{autodoc2-docstring} dss.IMeters.IMeters.Peakcurrent
```

````

````{py:property} RegisterNames
:canonical: dss.IMeters.IMeters.RegisterNames
:type: typing.List[str]

```{autodoc2-docstring} dss.IMeters.IMeters.RegisterNames
```

````

````{py:property} RegisterValues
:canonical: dss.IMeters.IMeters.RegisterValues
:type: dss._types.Float64Array

```{autodoc2-docstring} dss.IMeters.IMeters.RegisterValues
```

````

````{py:method} Reset()
:canonical: dss.IMeters.IMeters.Reset

```{autodoc2-docstring} dss.IMeters.IMeters.Reset
```

````

````{py:method} ResetAll()
:canonical: dss.IMeters.IMeters.ResetAll

```{autodoc2-docstring} dss.IMeters.IMeters.ResetAll
```

````

````{py:property} SAIDI
:canonical: dss.IMeters.IMeters.SAIDI
:type: float

```{autodoc2-docstring} dss.IMeters.IMeters.SAIDI
```

````

````{py:property} SAIFI
:canonical: dss.IMeters.IMeters.SAIFI
:type: float

```{autodoc2-docstring} dss.IMeters.IMeters.SAIFI
```

````

````{py:property} SAIFIKW
:canonical: dss.IMeters.IMeters.SAIFIKW
:type: float

```{autodoc2-docstring} dss.IMeters.IMeters.SAIFIKW
```

````

````{py:method} Sample()
:canonical: dss.IMeters.IMeters.Sample

```{autodoc2-docstring} dss.IMeters.IMeters.Sample
```

````

````{py:method} SampleAll()
:canonical: dss.IMeters.IMeters.SampleAll

```{autodoc2-docstring} dss.IMeters.IMeters.SampleAll
```

````

````{py:method} Save()
:canonical: dss.IMeters.IMeters.Save

```{autodoc2-docstring} dss.IMeters.IMeters.Save
```

````

````{py:method} SaveAll()
:canonical: dss.IMeters.IMeters.SaveAll

```{autodoc2-docstring} dss.IMeters.IMeters.SaveAll
```

````

````{py:property} SectSeqIdx
:canonical: dss.IMeters.IMeters.SectSeqIdx
:type: int

```{autodoc2-docstring} dss.IMeters.IMeters.SectSeqIdx
```

````

````{py:property} SectTotalCust
:canonical: dss.IMeters.IMeters.SectTotalCust
:type: int

```{autodoc2-docstring} dss.IMeters.IMeters.SectTotalCust
```

````

````{py:property} SeqListSize
:canonical: dss.IMeters.IMeters.SeqListSize
:type: int

```{autodoc2-docstring} dss.IMeters.IMeters.SeqListSize
```

````

````{py:property} SequenceIndex
:canonical: dss.IMeters.IMeters.SequenceIndex
:type: int

```{autodoc2-docstring} dss.IMeters.IMeters.SequenceIndex
```

````

````{py:method} SetActiveSection(SectIdx: int)
:canonical: dss.IMeters.IMeters.SetActiveSection

```{autodoc2-docstring} dss.IMeters.IMeters.SetActiveSection
```

````

````{py:property} SumBranchFltRates
:canonical: dss.IMeters.IMeters.SumBranchFltRates
:type: float

```{autodoc2-docstring} dss.IMeters.IMeters.SumBranchFltRates
```

````

````{py:property} TotalCustomers
:canonical: dss.IMeters.IMeters.TotalCustomers
:type: int

```{autodoc2-docstring} dss.IMeters.IMeters.TotalCustomers
```

````

````{py:property} Totals
:canonical: dss.IMeters.IMeters.Totals
:type: dss._types.Float64Array

```{autodoc2-docstring} dss.IMeters.IMeters.Totals
```

````

````{py:property} ZonePCE
:canonical: dss.IMeters.IMeters.ZonePCE
:type: typing.List[str]

```{autodoc2-docstring} dss.IMeters.IMeters.ZonePCE
```

````

````{py:method} __init__(api_util)
:canonical: dss.IMeters.IMeters.__init__

```{autodoc2-docstring} dss.IMeters.IMeters.__init__
```

````

````{py:method} __iter__() -> typing.Iterator[dss._cffi_api_util.Iterable]
:canonical: dss.IMeters.IMeters.__iter__

```{autodoc2-docstring} dss.IMeters.IMeters.__iter__
```

````

````{py:method} __len__() -> int
:canonical: dss.IMeters.IMeters.__len__

```{autodoc2-docstring} dss.IMeters.IMeters.__len__
```

````

````{py:property} idx
:canonical: dss.IMeters.IMeters.idx
:type: int

```{autodoc2-docstring} dss.IMeters.IMeters.idx
```

````

`````
