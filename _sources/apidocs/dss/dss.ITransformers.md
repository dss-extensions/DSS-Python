# {py:mod}`dss.ITransformers`

```{py:module} dss.ITransformers
```

```{autodoc2-docstring} dss.ITransformers
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ITransformers <dss.ITransformers.ITransformers>`
  - ```{autodoc2-docstring} dss.ITransformers.ITransformers
    :summary:
    ```
````

### API

`````{py:class} ITransformers(api_util)
:canonical: dss.ITransformers.ITransformers

Bases: {py:obj}`dss._cffi_api_util.Iterable`

```{autodoc2-docstring} dss.ITransformers.ITransformers
```

````{py:property} AllLossesByType
:canonical: dss.ITransformers.ITransformers.AllLossesByType
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.ITransformers.ITransformers.AllLossesByType
```

````

````{py:property} AllNames
:canonical: dss.ITransformers.ITransformers.AllNames
:type: typing.List[str]

```{autodoc2-docstring} dss.ITransformers.ITransformers.AllNames
```

````

````{py:property} CoreType
:canonical: dss.ITransformers.ITransformers.CoreType
:type: dss.enums.CoreType

```{autodoc2-docstring} dss.ITransformers.ITransformers.CoreType
```

````

````{py:property} Count
:canonical: dss.ITransformers.ITransformers.Count
:type: int

```{autodoc2-docstring} dss.ITransformers.ITransformers.Count
```

````

````{py:property} First
:canonical: dss.ITransformers.ITransformers.First
:type: int

```{autodoc2-docstring} dss.ITransformers.ITransformers.First
```

````

````{py:property} IsDelta
:canonical: dss.ITransformers.ITransformers.IsDelta
:type: bool

```{autodoc2-docstring} dss.ITransformers.ITransformers.IsDelta
```

````

````{py:property} LossesByType
:canonical: dss.ITransformers.ITransformers.LossesByType
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.ITransformers.ITransformers.LossesByType
```

````

````{py:property} MaxTap
:canonical: dss.ITransformers.ITransformers.MaxTap
:type: float

```{autodoc2-docstring} dss.ITransformers.ITransformers.MaxTap
```

````

````{py:property} MinTap
:canonical: dss.ITransformers.ITransformers.MinTap
:type: float

```{autodoc2-docstring} dss.ITransformers.ITransformers.MinTap
```

````

````{py:property} Name
:canonical: dss.ITransformers.ITransformers.Name
:type: str

```{autodoc2-docstring} dss.ITransformers.ITransformers.Name
```

````

````{py:property} Next
:canonical: dss.ITransformers.ITransformers.Next
:type: int

```{autodoc2-docstring} dss.ITransformers.ITransformers.Next
```

````

````{py:property} NumTaps
:canonical: dss.ITransformers.ITransformers.NumTaps
:type: int

```{autodoc2-docstring} dss.ITransformers.ITransformers.NumTaps
```

````

````{py:property} NumWindings
:canonical: dss.ITransformers.ITransformers.NumWindings
:type: int

```{autodoc2-docstring} dss.ITransformers.ITransformers.NumWindings
```

````

````{py:property} R
:canonical: dss.ITransformers.ITransformers.R
:type: float

```{autodoc2-docstring} dss.ITransformers.ITransformers.R
```

````

````{py:property} RdcOhms
:canonical: dss.ITransformers.ITransformers.RdcOhms
:type: float

```{autodoc2-docstring} dss.ITransformers.ITransformers.RdcOhms
```

````

````{py:property} Rneut
:canonical: dss.ITransformers.ITransformers.Rneut
:type: float

```{autodoc2-docstring} dss.ITransformers.ITransformers.Rneut
```

````

````{py:property} Tap
:canonical: dss.ITransformers.ITransformers.Tap
:type: float

```{autodoc2-docstring} dss.ITransformers.ITransformers.Tap
```

````

````{py:property} Wdg
:canonical: dss.ITransformers.ITransformers.Wdg
:type: int

```{autodoc2-docstring} dss.ITransformers.ITransformers.Wdg
```

````

````{py:property} WdgCurrents
:canonical: dss.ITransformers.ITransformers.WdgCurrents
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.ITransformers.ITransformers.WdgCurrents
```

````

````{py:property} WdgVoltages
:canonical: dss.ITransformers.ITransformers.WdgVoltages
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.ITransformers.ITransformers.WdgVoltages
```

````

````{py:property} XfmrCode
:canonical: dss.ITransformers.ITransformers.XfmrCode
:type: str

```{autodoc2-docstring} dss.ITransformers.ITransformers.XfmrCode
```

````

````{py:property} Xhl
:canonical: dss.ITransformers.ITransformers.Xhl
:type: float

```{autodoc2-docstring} dss.ITransformers.ITransformers.Xhl
```

````

````{py:property} Xht
:canonical: dss.ITransformers.ITransformers.Xht
:type: float

```{autodoc2-docstring} dss.ITransformers.ITransformers.Xht
```

````

````{py:property} Xlt
:canonical: dss.ITransformers.ITransformers.Xlt
:type: float

```{autodoc2-docstring} dss.ITransformers.ITransformers.Xlt
```

````

````{py:property} Xneut
:canonical: dss.ITransformers.ITransformers.Xneut
:type: float

```{autodoc2-docstring} dss.ITransformers.ITransformers.Xneut
```

````

````{py:method} __init__(api_util)
:canonical: dss.ITransformers.ITransformers.__init__

```{autodoc2-docstring} dss.ITransformers.ITransformers.__init__
```

````

````{py:method} __iter__() -> typing.Iterator[dss._cffi_api_util.Iterable]
:canonical: dss.ITransformers.ITransformers.__iter__

```{autodoc2-docstring} dss.ITransformers.ITransformers.__iter__
```

````

````{py:method} __len__() -> int
:canonical: dss.ITransformers.ITransformers.__len__

```{autodoc2-docstring} dss.ITransformers.ITransformers.__len__
```

````

````{py:property} idx
:canonical: dss.ITransformers.ITransformers.idx
:type: int

```{autodoc2-docstring} dss.ITransformers.ITransformers.idx
```

````

````{py:property} kV
:canonical: dss.ITransformers.ITransformers.kV
:type: float

```{autodoc2-docstring} dss.ITransformers.ITransformers.kV
```

````

````{py:property} kVA
:canonical: dss.ITransformers.ITransformers.kVA
:type: float

```{autodoc2-docstring} dss.ITransformers.ITransformers.kVA
```

````

````{py:attribute} kva
:canonical: dss.ITransformers.ITransformers.kva
:value: >
   None

```{autodoc2-docstring} dss.ITransformers.ITransformers.kva
```

````

````{py:property} strWdgCurrents
:canonical: dss.ITransformers.ITransformers.strWdgCurrents
:type: str

```{autodoc2-docstring} dss.ITransformers.ITransformers.strWdgCurrents
```

````

`````
