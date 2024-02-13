# {py:mod}`dss.IPDElements`

```{py:module} dss.IPDElements
```

```{autodoc2-docstring} dss.IPDElements
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IPDElements <dss.IPDElements.IPDElements>`
  - ```{autodoc2-docstring} dss.IPDElements.IPDElements
    :summary:
    ```
````

### API

`````{py:class} IPDElements(api_util, prefer_lists=False)
:canonical: dss.IPDElements.IPDElements

Bases: {py:obj}`dss._cffi_api_util.Base`

```{autodoc2-docstring} dss.IPDElements.IPDElements
```

````{py:property} AccumulatedL
:canonical: dss.IPDElements.IPDElements.AccumulatedL
:type: float

```{autodoc2-docstring} dss.IPDElements.IPDElements.AccumulatedL
```

````

````{py:property} AllCplxSeqCurrents
:canonical: dss.IPDElements.IPDElements.AllCplxSeqCurrents
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.IPDElements.IPDElements.AllCplxSeqCurrents
```

````

````{py:property} AllCurrents
:canonical: dss.IPDElements.IPDElements.AllCurrents
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.IPDElements.IPDElements.AllCurrents
```

````

````{py:property} AllCurrentsMagAng
:canonical: dss.IPDElements.IPDElements.AllCurrentsMagAng
:type: dss._types.Float64Array

```{autodoc2-docstring} dss.IPDElements.IPDElements.AllCurrentsMagAng
```

````

````{py:method} AllMaxCurrents(AllNodes: bool = False) -> dss._types.Float64Array
:canonical: dss.IPDElements.IPDElements.AllMaxCurrents

```{autodoc2-docstring} dss.IPDElements.IPDElements.AllMaxCurrents
```

````

````{py:property} AllNames
:canonical: dss.IPDElements.IPDElements.AllNames
:type: typing.List[str]

```{autodoc2-docstring} dss.IPDElements.IPDElements.AllNames
```

````

````{py:property} AllNumConductors
:canonical: dss.IPDElements.IPDElements.AllNumConductors
:type: dss._types.Int32Array

```{autodoc2-docstring} dss.IPDElements.IPDElements.AllNumConductors
```

````

````{py:property} AllNumPhases
:canonical: dss.IPDElements.IPDElements.AllNumPhases
:type: dss._types.Int32Array

```{autodoc2-docstring} dss.IPDElements.IPDElements.AllNumPhases
```

````

````{py:property} AllNumTerminals
:canonical: dss.IPDElements.IPDElements.AllNumTerminals
:type: dss._types.Int32Array

```{autodoc2-docstring} dss.IPDElements.IPDElements.AllNumTerminals
```

````

````{py:method} AllPctEmerg(AllNodes: bool = False) -> dss._types.Float64Array
:canonical: dss.IPDElements.IPDElements.AllPctEmerg

```{autodoc2-docstring} dss.IPDElements.IPDElements.AllPctEmerg
```

````

````{py:method} AllPctNorm(AllNodes: bool = False) -> dss._types.Float64Array
:canonical: dss.IPDElements.IPDElements.AllPctNorm

```{autodoc2-docstring} dss.IPDElements.IPDElements.AllPctNorm
```

````

````{py:property} AllPowers
:canonical: dss.IPDElements.IPDElements.AllPowers
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.IPDElements.IPDElements.AllPowers
```

````

````{py:property} AllSeqCurrents
:canonical: dss.IPDElements.IPDElements.AllSeqCurrents
:type: dss._types.Float64Array

```{autodoc2-docstring} dss.IPDElements.IPDElements.AllSeqCurrents
```

````

````{py:property} AllSeqPowers
:canonical: dss.IPDElements.IPDElements.AllSeqPowers
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.IPDElements.IPDElements.AllSeqPowers
```

````

````{py:property} Count
:canonical: dss.IPDElements.IPDElements.Count
:type: int

```{autodoc2-docstring} dss.IPDElements.IPDElements.Count
```

````

````{py:property} FaultRate
:canonical: dss.IPDElements.IPDElements.FaultRate
:type: float

```{autodoc2-docstring} dss.IPDElements.IPDElements.FaultRate
```

````

````{py:property} First
:canonical: dss.IPDElements.IPDElements.First
:type: int

```{autodoc2-docstring} dss.IPDElements.IPDElements.First
```

````

````{py:property} FromTerminal
:canonical: dss.IPDElements.IPDElements.FromTerminal
:type: int

```{autodoc2-docstring} dss.IPDElements.IPDElements.FromTerminal
```

````

````{py:property} IsShunt
:canonical: dss.IPDElements.IPDElements.IsShunt
:type: bool

```{autodoc2-docstring} dss.IPDElements.IPDElements.IsShunt
```

````

````{py:property} Lambda
:canonical: dss.IPDElements.IPDElements.Lambda
:type: float

```{autodoc2-docstring} dss.IPDElements.IPDElements.Lambda
```

````

````{py:property} Name
:canonical: dss.IPDElements.IPDElements.Name
:type: str

```{autodoc2-docstring} dss.IPDElements.IPDElements.Name
```

````

````{py:property} Next
:canonical: dss.IPDElements.IPDElements.Next
:type: int

```{autodoc2-docstring} dss.IPDElements.IPDElements.Next
```

````

````{py:property} Numcustomers
:canonical: dss.IPDElements.IPDElements.Numcustomers
:type: int

```{autodoc2-docstring} dss.IPDElements.IPDElements.Numcustomers
```

````

````{py:property} ParentPDElement
:canonical: dss.IPDElements.IPDElements.ParentPDElement
:type: int

```{autodoc2-docstring} dss.IPDElements.IPDElements.ParentPDElement
```

````

````{py:property} RepairTime
:canonical: dss.IPDElements.IPDElements.RepairTime
:type: float

```{autodoc2-docstring} dss.IPDElements.IPDElements.RepairTime
```

````

````{py:property} SectionID
:canonical: dss.IPDElements.IPDElements.SectionID
:type: int

```{autodoc2-docstring} dss.IPDElements.IPDElements.SectionID
```

````

````{py:property} TotalMiles
:canonical: dss.IPDElements.IPDElements.TotalMiles
:type: float

```{autodoc2-docstring} dss.IPDElements.IPDElements.TotalMiles
```

````

````{py:property} Totalcustomers
:canonical: dss.IPDElements.IPDElements.Totalcustomers
:type: int

```{autodoc2-docstring} dss.IPDElements.IPDElements.Totalcustomers
```

````

````{py:method} __init__(api_util, prefer_lists=False)
:canonical: dss.IPDElements.IPDElements.__init__

```{autodoc2-docstring} dss.IPDElements.IPDElements.__init__
```

````

````{py:method} __iter__() -> typing.Iterator[dss.IPDElements.IPDElements]
:canonical: dss.IPDElements.IPDElements.__iter__

```{autodoc2-docstring} dss.IPDElements.IPDElements.__iter__
```

````

````{py:method} __len__() -> int
:canonical: dss.IPDElements.IPDElements.__len__

```{autodoc2-docstring} dss.IPDElements.IPDElements.__len__
```

````

````{py:property} pctPermanent
:canonical: dss.IPDElements.IPDElements.pctPermanent
:type: float

```{autodoc2-docstring} dss.IPDElements.IPDElements.pctPermanent
```

````

`````
