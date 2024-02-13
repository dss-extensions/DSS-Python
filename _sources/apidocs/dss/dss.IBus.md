# {py:mod}`dss.IBus`

```{py:module} dss.IBus
```

```{autodoc2-docstring} dss.IBus
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IBus <dss.IBus.IBus>`
  - ```{autodoc2-docstring} dss.IBus.IBus
    :summary:
    ```
````

### API

`````{py:class} IBus(api_util, prefer_lists=False)
:canonical: dss.IBus.IBus

Bases: {py:obj}`dss._cffi_api_util.Base`

```{autodoc2-docstring} dss.IBus.IBus
```

````{py:property} AllPCEatBus
:canonical: dss.IBus.IBus.AllPCEatBus
:type: typing.List[str]

```{autodoc2-docstring} dss.IBus.IBus.AllPCEatBus
```

````

````{py:property} AllPDEatBus
:canonical: dss.IBus.IBus.AllPDEatBus
:type: typing.List[str]

```{autodoc2-docstring} dss.IBus.IBus.AllPDEatBus
```

````

````{py:property} Coorddefined
:canonical: dss.IBus.IBus.Coorddefined
:type: bool

```{autodoc2-docstring} dss.IBus.IBus.Coorddefined
```

````

````{py:property} CplxSeqVoltages
:canonical: dss.IBus.IBus.CplxSeqVoltages
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.IBus.IBus.CplxSeqVoltages
```

````

````{py:property} Cust_Duration
:canonical: dss.IBus.IBus.Cust_Duration
:type: float

```{autodoc2-docstring} dss.IBus.IBus.Cust_Duration
```

````

````{py:property} Cust_Interrupts
:canonical: dss.IBus.IBus.Cust_Interrupts
:type: float

```{autodoc2-docstring} dss.IBus.IBus.Cust_Interrupts
```

````

````{py:property} Distance
:canonical: dss.IBus.IBus.Distance
:type: float

```{autodoc2-docstring} dss.IBus.IBus.Distance
```

````

````{py:method} GetUniqueNodeNumber(StartNumber: int) -> int
:canonical: dss.IBus.IBus.GetUniqueNodeNumber

```{autodoc2-docstring} dss.IBus.IBus.GetUniqueNodeNumber
```

````

````{py:property} Int_Duration
:canonical: dss.IBus.IBus.Int_Duration
:type: float

```{autodoc2-docstring} dss.IBus.IBus.Int_Duration
```

````

````{py:property} Isc
:canonical: dss.IBus.IBus.Isc
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.IBus.IBus.Isc
```

````

````{py:property} Lambda
:canonical: dss.IBus.IBus.Lambda
:type: float

```{autodoc2-docstring} dss.IBus.IBus.Lambda
```

````

````{py:property} LineList
:canonical: dss.IBus.IBus.LineList
:type: typing.List[str]

```{autodoc2-docstring} dss.IBus.IBus.LineList
```

````

````{py:property} LoadList
:canonical: dss.IBus.IBus.LoadList
:type: typing.List[str]

```{autodoc2-docstring} dss.IBus.IBus.LoadList
```

````

````{py:property} N_Customers
:canonical: dss.IBus.IBus.N_Customers
:type: int

```{autodoc2-docstring} dss.IBus.IBus.N_Customers
```

````

````{py:property} N_interrupts
:canonical: dss.IBus.IBus.N_interrupts
:type: float

```{autodoc2-docstring} dss.IBus.IBus.N_interrupts
```

````

````{py:property} Name
:canonical: dss.IBus.IBus.Name
:type: str

```{autodoc2-docstring} dss.IBus.IBus.Name
```

````

````{py:property} Nodes
:canonical: dss.IBus.IBus.Nodes
:type: dss._types.Int32Array

```{autodoc2-docstring} dss.IBus.IBus.Nodes
```

````

````{py:property} NumNodes
:canonical: dss.IBus.IBus.NumNodes
:type: int

```{autodoc2-docstring} dss.IBus.IBus.NumNodes
```

````

````{py:property} SectionID
:canonical: dss.IBus.IBus.SectionID
:type: int

```{autodoc2-docstring} dss.IBus.IBus.SectionID
```

````

````{py:property} SeqVoltages
:canonical: dss.IBus.IBus.SeqVoltages
:type: dss._types.Float64Array

```{autodoc2-docstring} dss.IBus.IBus.SeqVoltages
```

````

````{py:property} TotalMiles
:canonical: dss.IBus.IBus.TotalMiles
:type: float

```{autodoc2-docstring} dss.IBus.IBus.TotalMiles
```

````

````{py:property} VLL
:canonical: dss.IBus.IBus.VLL
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.IBus.IBus.VLL
```

````

````{py:property} VMagAngle
:canonical: dss.IBus.IBus.VMagAngle
:type: dss._types.Float64Array

```{autodoc2-docstring} dss.IBus.IBus.VMagAngle
```

````

````{py:property} Voc
:canonical: dss.IBus.IBus.Voc
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.IBus.IBus.Voc
```

````

````{py:property} Voltages
:canonical: dss.IBus.IBus.Voltages
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.IBus.IBus.Voltages
```

````

````{py:property} YscMatrix
:canonical: dss.IBus.IBus.YscMatrix
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.IBus.IBus.YscMatrix
```

````

````{py:property} ZSC012Matrix
:canonical: dss.IBus.IBus.ZSC012Matrix
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.IBus.IBus.ZSC012Matrix
```

````

````{py:property} Zsc0
:canonical: dss.IBus.IBus.Zsc0
:type: dss._types.Float64ArrayOrSimpleComplex

```{autodoc2-docstring} dss.IBus.IBus.Zsc0
```

````

````{py:property} Zsc1
:canonical: dss.IBus.IBus.Zsc1
:type: dss._types.Float64ArrayOrSimpleComplex

```{autodoc2-docstring} dss.IBus.IBus.Zsc1
```

````

````{py:property} ZscMatrix
:canonical: dss.IBus.IBus.ZscMatrix
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.IBus.IBus.ZscMatrix
```

````

````{py:method} ZscRefresh() -> bool
:canonical: dss.IBus.IBus.ZscRefresh

```{autodoc2-docstring} dss.IBus.IBus.ZscRefresh
```

````

````{py:method} __call__(index: typing.Union[int, str]) -> dss.IBus.IBus
:canonical: dss.IBus.IBus.__call__

```{autodoc2-docstring} dss.IBus.IBus.__call__
```

````

````{py:method} __getitem__(index: typing.Union[int, str]) -> dss.IBus.IBus
:canonical: dss.IBus.IBus.__getitem__

```{autodoc2-docstring} dss.IBus.IBus.__getitem__
```

````

````{py:method} __init__(api_util, prefer_lists=False)
:canonical: dss.IBus.IBus.__init__

```{autodoc2-docstring} dss.IBus.IBus.__init__
```

````

````{py:method} __iter__() -> typing.Iterator[dss.IBus.IBus]
:canonical: dss.IBus.IBus.__iter__

```{autodoc2-docstring} dss.IBus.IBus.__iter__
```

````

````{py:method} __len__() -> int
:canonical: dss.IBus.IBus.__len__

```{autodoc2-docstring} dss.IBus.IBus.__len__
```

````

````{py:property} kVBase
:canonical: dss.IBus.IBus.kVBase
:type: float

```{autodoc2-docstring} dss.IBus.IBus.kVBase
```

````

````{py:property} puVLL
:canonical: dss.IBus.IBus.puVLL
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.IBus.IBus.puVLL
```

````

````{py:property} puVmagAngle
:canonical: dss.IBus.IBus.puVmagAngle
:type: dss._types.Float64Array

```{autodoc2-docstring} dss.IBus.IBus.puVmagAngle
```

````

````{py:property} puVoltages
:canonical: dss.IBus.IBus.puVoltages
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.IBus.IBus.puVoltages
```

````

````{py:property} x
:canonical: dss.IBus.IBus.x
:type: float

```{autodoc2-docstring} dss.IBus.IBus.x
```

````

````{py:property} y
:canonical: dss.IBus.IBus.y
:type: float

```{autodoc2-docstring} dss.IBus.IBus.y
```

````

`````
