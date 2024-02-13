# {py:mod}`dss.ICktElement`

```{py:module} dss.ICktElement
```

```{autodoc2-docstring} dss.ICktElement
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ICktElement <dss.ICktElement.ICktElement>`
  - ```{autodoc2-docstring} dss.ICktElement.ICktElement
    :summary:
    ```
````

### API

`````{py:class} ICktElement(api_util)
:canonical: dss.ICktElement.ICktElement

Bases: {py:obj}`dss._cffi_api_util.Base`

```{autodoc2-docstring} dss.ICktElement.ICktElement
```

````{py:property} AllPropertyNames
:canonical: dss.ICktElement.ICktElement.AllPropertyNames
:type: typing.List[str]

```{autodoc2-docstring} dss.ICktElement.ICktElement.AllPropertyNames
```

````

````{py:property} AllVariableNames
:canonical: dss.ICktElement.ICktElement.AllVariableNames
:type: typing.List[str]

```{autodoc2-docstring} dss.ICktElement.ICktElement.AllVariableNames
```

````

````{py:property} AllVariableValues
:canonical: dss.ICktElement.ICktElement.AllVariableValues
:type: dss._types.Float64Array

```{autodoc2-docstring} dss.ICktElement.ICktElement.AllVariableValues
```

````

````{py:property} BusNames
:canonical: dss.ICktElement.ICktElement.BusNames
:type: typing.List[str]

```{autodoc2-docstring} dss.ICktElement.ICktElement.BusNames
```

````

````{py:method} Close(Term: int, Phs: int)
:canonical: dss.ICktElement.ICktElement.Close

```{autodoc2-docstring} dss.ICktElement.ICktElement.Close
```

````

````{py:method} Controller(idx: int) -> str
:canonical: dss.ICktElement.ICktElement.Controller

```{autodoc2-docstring} dss.ICktElement.ICktElement.Controller
```

````

````{py:property} CplxSeqCurrents
:canonical: dss.ICktElement.ICktElement.CplxSeqCurrents
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.ICktElement.ICktElement.CplxSeqCurrents
```

````

````{py:property} CplxSeqVoltages
:canonical: dss.ICktElement.ICktElement.CplxSeqVoltages
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.ICktElement.ICktElement.CplxSeqVoltages
```

````

````{py:property} Currents
:canonical: dss.ICktElement.ICktElement.Currents
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.ICktElement.ICktElement.Currents
```

````

````{py:property} CurrentsMagAng
:canonical: dss.ICktElement.ICktElement.CurrentsMagAng
:type: dss._types.Float64Array

```{autodoc2-docstring} dss.ICktElement.ICktElement.CurrentsMagAng
```

````

````{py:property} DisplayName
:canonical: dss.ICktElement.ICktElement.DisplayName
:type: str

```{autodoc2-docstring} dss.ICktElement.ICktElement.DisplayName
```

````

````{py:property} EmergAmps
:canonical: dss.ICktElement.ICktElement.EmergAmps
:type: float

```{autodoc2-docstring} dss.ICktElement.ICktElement.EmergAmps
```

````

````{py:property} Enabled
:canonical: dss.ICktElement.ICktElement.Enabled
:type: bool

```{autodoc2-docstring} dss.ICktElement.ICktElement.Enabled
```

````

````{py:property} EnergyMeter
:canonical: dss.ICktElement.ICktElement.EnergyMeter
:type: str

```{autodoc2-docstring} dss.ICktElement.ICktElement.EnergyMeter
```

````

````{py:property} GUID
:canonical: dss.ICktElement.ICktElement.GUID
:type: str

```{autodoc2-docstring} dss.ICktElement.ICktElement.GUID
```

````

````{py:property} Handle
:canonical: dss.ICktElement.ICktElement.Handle
:type: int

```{autodoc2-docstring} dss.ICktElement.ICktElement.Handle
```

````

````{py:property} HasOCPDevice
:canonical: dss.ICktElement.ICktElement.HasOCPDevice
:type: bool

```{autodoc2-docstring} dss.ICktElement.ICktElement.HasOCPDevice
```

````

````{py:property} HasSwitchControl
:canonical: dss.ICktElement.ICktElement.HasSwitchControl
:type: bool

```{autodoc2-docstring} dss.ICktElement.ICktElement.HasSwitchControl
```

````

````{py:property} HasVoltControl
:canonical: dss.ICktElement.ICktElement.HasVoltControl
:type: bool

```{autodoc2-docstring} dss.ICktElement.ICktElement.HasVoltControl
```

````

````{py:property} IsIsolated
:canonical: dss.ICktElement.ICktElement.IsIsolated
:type: bool

```{autodoc2-docstring} dss.ICktElement.ICktElement.IsIsolated
```

````

````{py:method} IsOpen(Term: int, Phs: int) -> bool
:canonical: dss.ICktElement.ICktElement.IsOpen

```{autodoc2-docstring} dss.ICktElement.ICktElement.IsOpen
```

````

````{py:property} Losses
:canonical: dss.ICktElement.ICktElement.Losses
:type: dss._types.Float64ArrayOrSimpleComplex

```{autodoc2-docstring} dss.ICktElement.ICktElement.Losses
```

````

````{py:property} Name
:canonical: dss.ICktElement.ICktElement.Name
:type: str

```{autodoc2-docstring} dss.ICktElement.ICktElement.Name
```

````

````{py:property} NodeOrder
:canonical: dss.ICktElement.ICktElement.NodeOrder
:type: dss._types.Int32Array

```{autodoc2-docstring} dss.ICktElement.ICktElement.NodeOrder
```

````

````{py:property} NodeRef
:canonical: dss.ICktElement.ICktElement.NodeRef
:type: dss._types.Int32Array

```{autodoc2-docstring} dss.ICktElement.ICktElement.NodeRef
```

````

````{py:property} NormalAmps
:canonical: dss.ICktElement.ICktElement.NormalAmps
:type: float

```{autodoc2-docstring} dss.ICktElement.ICktElement.NormalAmps
```

````

````{py:property} NumConductors
:canonical: dss.ICktElement.ICktElement.NumConductors
:type: int

```{autodoc2-docstring} dss.ICktElement.ICktElement.NumConductors
```

````

````{py:property} NumControls
:canonical: dss.ICktElement.ICktElement.NumControls
:type: int

```{autodoc2-docstring} dss.ICktElement.ICktElement.NumControls
```

````

````{py:property} NumPhases
:canonical: dss.ICktElement.ICktElement.NumPhases
:type: int

```{autodoc2-docstring} dss.ICktElement.ICktElement.NumPhases
```

````

````{py:property} NumProperties
:canonical: dss.ICktElement.ICktElement.NumProperties
:type: int

```{autodoc2-docstring} dss.ICktElement.ICktElement.NumProperties
```

````

````{py:property} NumTerminals
:canonical: dss.ICktElement.ICktElement.NumTerminals
:type: int

```{autodoc2-docstring} dss.ICktElement.ICktElement.NumTerminals
```

````

````{py:property} OCPDevIndex
:canonical: dss.ICktElement.ICktElement.OCPDevIndex
:type: int

```{autodoc2-docstring} dss.ICktElement.ICktElement.OCPDevIndex
```

````

````{py:property} OCPDevType
:canonical: dss.ICktElement.ICktElement.OCPDevType
:type: dss.enums.OCPDevType

```{autodoc2-docstring} dss.ICktElement.ICktElement.OCPDevType
```

````

````{py:method} Open(Term: int, Phs: int)
:canonical: dss.ICktElement.ICktElement.Open

```{autodoc2-docstring} dss.ICktElement.ICktElement.Open
```

````

````{py:property} PhaseLosses
:canonical: dss.ICktElement.ICktElement.PhaseLosses
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.ICktElement.ICktElement.PhaseLosses
```

````

````{py:property} Powers
:canonical: dss.ICktElement.ICktElement.Powers
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.ICktElement.ICktElement.Powers
```

````

````{py:attribute} Properties
:canonical: dss.ICktElement.ICktElement.Properties
:type: dss.IDSSProperty.IDSSProperty
:value: >
   None

```{autodoc2-docstring} dss.ICktElement.ICktElement.Properties
```

````

````{py:property} Residuals
:canonical: dss.ICktElement.ICktElement.Residuals
:type: dss._types.Float64Array

```{autodoc2-docstring} dss.ICktElement.ICktElement.Residuals
```

````

````{py:property} SeqCurrents
:canonical: dss.ICktElement.ICktElement.SeqCurrents
:type: dss._types.Float64Array

```{autodoc2-docstring} dss.ICktElement.ICktElement.SeqCurrents
```

````

````{py:property} SeqPowers
:canonical: dss.ICktElement.ICktElement.SeqPowers
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.ICktElement.ICktElement.SeqPowers
```

````

````{py:property} SeqVoltages
:canonical: dss.ICktElement.ICktElement.SeqVoltages
:type: dss._types.Float64Array

```{autodoc2-docstring} dss.ICktElement.ICktElement.SeqVoltages
```

````

````{py:property} TotalPowers
:canonical: dss.ICktElement.ICktElement.TotalPowers
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.ICktElement.ICktElement.TotalPowers
```

````

````{py:method} Variable(MyVarName: typing.AnyStr) -> typing.Tuple[float, int]
:canonical: dss.ICktElement.ICktElement.Variable

```{autodoc2-docstring} dss.ICktElement.ICktElement.Variable
```

````

````{py:attribute} VariableByIndex
:canonical: dss.ICktElement.ICktElement.VariableByIndex
:value: >
   None

```{autodoc2-docstring} dss.ICktElement.ICktElement.VariableByIndex
```

````

````{py:attribute} VariableByName
:canonical: dss.ICktElement.ICktElement.VariableByName
:value: >
   None

```{autodoc2-docstring} dss.ICktElement.ICktElement.VariableByName
```

````

````{py:method} Variablei(Idx: int) -> typing.Tuple[float, int]
:canonical: dss.ICktElement.ICktElement.Variablei

```{autodoc2-docstring} dss.ICktElement.ICktElement.Variablei
```

````

````{py:property} Voltages
:canonical: dss.ICktElement.ICktElement.Voltages
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.ICktElement.ICktElement.Voltages
```

````

````{py:property} VoltagesMagAng
:canonical: dss.ICktElement.ICktElement.VoltagesMagAng
:type: dss._types.Float64Array

```{autodoc2-docstring} dss.ICktElement.ICktElement.VoltagesMagAng
```

````

````{py:property} Yprim
:canonical: dss.ICktElement.ICktElement.Yprim
:type: dss._types.Float64ArrayOrComplexArray

```{autodoc2-docstring} dss.ICktElement.ICktElement.Yprim
```

````

````{py:method} __call__(index) -> dss.ICktElement.ICktElement
:canonical: dss.ICktElement.ICktElement.__call__

```{autodoc2-docstring} dss.ICktElement.ICktElement.__call__
```

````

````{py:method} __getitem__(index) -> dss.ICktElement.ICktElement
:canonical: dss.ICktElement.ICktElement.__getitem__

```{autodoc2-docstring} dss.ICktElement.ICktElement.__getitem__
```

````

````{py:method} __init__(api_util)
:canonical: dss.ICktElement.ICktElement.__init__

```{autodoc2-docstring} dss.ICktElement.ICktElement.__init__
```

````

````{py:method} __iter__() -> typing.Iterator[dss.ICktElement.ICktElement]
:canonical: dss.ICktElement.ICktElement.__iter__

```{autodoc2-docstring} dss.ICktElement.ICktElement.__iter__
```

````

````{py:method} setVariableByIndex(Idx: int, Value: float) -> int
:canonical: dss.ICktElement.ICktElement.setVariableByIndex

```{autodoc2-docstring} dss.ICktElement.ICktElement.setVariableByIndex
```

````

````{py:method} setVariableByName(Idx: typing.AnyStr, Value: float) -> int
:canonical: dss.ICktElement.ICktElement.setVariableByName

```{autodoc2-docstring} dss.ICktElement.ICktElement.setVariableByName
```

````

`````
