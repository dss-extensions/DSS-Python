# {py:mod}`dss.ILineGeometries`

```{py:module} dss.ILineGeometries
```

```{autodoc2-docstring} dss.ILineGeometries
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ILineGeometries <dss.ILineGeometries.ILineGeometries>`
  - ```{autodoc2-docstring} dss.ILineGeometries.ILineGeometries
    :summary:
    ```
````

### API

`````{py:class} ILineGeometries(api_util)
:canonical: dss.ILineGeometries.ILineGeometries

Bases: {py:obj}`dss._cffi_api_util.Iterable`

```{autodoc2-docstring} dss.ILineGeometries.ILineGeometries
```

````{py:property} AllNames
:canonical: dss.ILineGeometries.ILineGeometries.AllNames
:type: typing.List[str]

```{autodoc2-docstring} dss.ILineGeometries.ILineGeometries.AllNames
```

````

````{py:method} Cmatrix(Frequency: float, Length: float, Units: int) -> dss._types.Float64Array
:canonical: dss.ILineGeometries.ILineGeometries.Cmatrix

```{autodoc2-docstring} dss.ILineGeometries.ILineGeometries.Cmatrix
```

````

````{py:property} Conductors
:canonical: dss.ILineGeometries.ILineGeometries.Conductors
:type: typing.List[str]

```{autodoc2-docstring} dss.ILineGeometries.ILineGeometries.Conductors
```

````

````{py:property} Count
:canonical: dss.ILineGeometries.ILineGeometries.Count
:type: int

```{autodoc2-docstring} dss.ILineGeometries.ILineGeometries.Count
```

````

````{py:property} EmergAmps
:canonical: dss.ILineGeometries.ILineGeometries.EmergAmps
:type: float

```{autodoc2-docstring} dss.ILineGeometries.ILineGeometries.EmergAmps
```

````

````{py:property} First
:canonical: dss.ILineGeometries.ILineGeometries.First
:type: int

```{autodoc2-docstring} dss.ILineGeometries.ILineGeometries.First
```

````

````{py:property} Name
:canonical: dss.ILineGeometries.ILineGeometries.Name
:type: str

```{autodoc2-docstring} dss.ILineGeometries.ILineGeometries.Name
```

````

````{py:property} Nconds
:canonical: dss.ILineGeometries.ILineGeometries.Nconds
:type: int

```{autodoc2-docstring} dss.ILineGeometries.ILineGeometries.Nconds
```

````

````{py:property} Next
:canonical: dss.ILineGeometries.ILineGeometries.Next
:type: int

```{autodoc2-docstring} dss.ILineGeometries.ILineGeometries.Next
```

````

````{py:property} NormAmps
:canonical: dss.ILineGeometries.ILineGeometries.NormAmps
:type: float

```{autodoc2-docstring} dss.ILineGeometries.ILineGeometries.NormAmps
```

````

````{py:property} Phases
:canonical: dss.ILineGeometries.ILineGeometries.Phases
:type: int

```{autodoc2-docstring} dss.ILineGeometries.ILineGeometries.Phases
```

````

````{py:property} Reduce
:canonical: dss.ILineGeometries.ILineGeometries.Reduce
:type: bool

```{autodoc2-docstring} dss.ILineGeometries.ILineGeometries.Reduce
```

````

````{py:property} RhoEarth
:canonical: dss.ILineGeometries.ILineGeometries.RhoEarth
:type: float

```{autodoc2-docstring} dss.ILineGeometries.ILineGeometries.RhoEarth
```

````

````{py:method} Rmatrix(Frequency: float, Length: float, Units: int) -> dss._types.Float64Array
:canonical: dss.ILineGeometries.ILineGeometries.Rmatrix

```{autodoc2-docstring} dss.ILineGeometries.ILineGeometries.Rmatrix
```

````

````{py:property} Units
:canonical: dss.ILineGeometries.ILineGeometries.Units
:type: typing.List[dss.enums.LineUnits]

```{autodoc2-docstring} dss.ILineGeometries.ILineGeometries.Units
```

````

````{py:property} Xcoords
:canonical: dss.ILineGeometries.ILineGeometries.Xcoords
:type: dss._types.Float64Array

```{autodoc2-docstring} dss.ILineGeometries.ILineGeometries.Xcoords
```

````

````{py:method} Xmatrix(Frequency: float, Length: float, Units: int) -> dss._types.Float64Array
:canonical: dss.ILineGeometries.ILineGeometries.Xmatrix

```{autodoc2-docstring} dss.ILineGeometries.ILineGeometries.Xmatrix
```

````

````{py:property} Ycoords
:canonical: dss.ILineGeometries.ILineGeometries.Ycoords
:type: dss._types.Float64Array

```{autodoc2-docstring} dss.ILineGeometries.ILineGeometries.Ycoords
```

````

````{py:method} Zmatrix(Frequency: float, Length: float, Units: int) -> dss._types.Float64ArrayOrComplexArray
:canonical: dss.ILineGeometries.ILineGeometries.Zmatrix

```{autodoc2-docstring} dss.ILineGeometries.ILineGeometries.Zmatrix
```

````

````{py:method} __init__(api_util)
:canonical: dss.ILineGeometries.ILineGeometries.__init__

```{autodoc2-docstring} dss.ILineGeometries.ILineGeometries.__init__
```

````

````{py:method} __iter__() -> typing.Iterator[dss._cffi_api_util.Iterable]
:canonical: dss.ILineGeometries.ILineGeometries.__iter__

```{autodoc2-docstring} dss.ILineGeometries.ILineGeometries.__iter__
```

````

````{py:method} __len__() -> int
:canonical: dss.ILineGeometries.ILineGeometries.__len__

```{autodoc2-docstring} dss.ILineGeometries.ILineGeometries.__len__
```

````

````{py:property} idx
:canonical: dss.ILineGeometries.ILineGeometries.idx
:type: int

```{autodoc2-docstring} dss.ILineGeometries.ILineGeometries.idx
```

````

`````
