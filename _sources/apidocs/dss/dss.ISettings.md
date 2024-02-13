# {py:mod}`dss.ISettings`

```{py:module} dss.ISettings
```

```{autodoc2-docstring} dss.ISettings
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ISettings <dss.ISettings.ISettings>`
  - ```{autodoc2-docstring} dss.ISettings.ISettings
    :summary:
    ```
````

### API

`````{py:class} ISettings(api_util, prefer_lists=False)
:canonical: dss.ISettings.ISettings

Bases: {py:obj}`dss._cffi_api_util.Base`

```{autodoc2-docstring} dss.ISettings.ISettings
```

````{py:property} AllocationFactors
:canonical: dss.ISettings.ISettings.AllocationFactors

```{autodoc2-docstring} dss.ISettings.ISettings.AllocationFactors
```

````

````{py:property} AllowDuplicates
:canonical: dss.ISettings.ISettings.AllowDuplicates
:type: bool

```{autodoc2-docstring} dss.ISettings.ISettings.AllowDuplicates
```

````

````{py:property} AutoBusList
:canonical: dss.ISettings.ISettings.AutoBusList
:type: str

```{autodoc2-docstring} dss.ISettings.ISettings.AutoBusList
```

````

````{py:property} CktModel
:canonical: dss.ISettings.ISettings.CktModel
:type: dss.enums.CktModels

```{autodoc2-docstring} dss.ISettings.ISettings.CktModel
```

````

````{py:property} ControlTrace
:canonical: dss.ISettings.ISettings.ControlTrace
:type: bool

```{autodoc2-docstring} dss.ISettings.ISettings.ControlTrace
```

````

````{py:property} EmergVmaxpu
:canonical: dss.ISettings.ISettings.EmergVmaxpu
:type: float

```{autodoc2-docstring} dss.ISettings.ISettings.EmergVmaxpu
```

````

````{py:property} EmergVminpu
:canonical: dss.ISettings.ISettings.EmergVminpu
:type: float

```{autodoc2-docstring} dss.ISettings.ISettings.EmergVminpu
```

````

````{py:property} IterateDisabled
:canonical: dss.ISettings.ISettings.IterateDisabled
:type: int

```{autodoc2-docstring} dss.ISettings.ISettings.IterateDisabled
```

````

````{py:property} LoadsTerminalCheck
:canonical: dss.ISettings.ISettings.LoadsTerminalCheck
:type: bool

```{autodoc2-docstring} dss.ISettings.ISettings.LoadsTerminalCheck
```

````

````{py:property} LossRegs
:canonical: dss.ISettings.ISettings.LossRegs
:type: dss._types.Int32Array

```{autodoc2-docstring} dss.ISettings.ISettings.LossRegs
```

````

````{py:property} LossWeight
:canonical: dss.ISettings.ISettings.LossWeight
:type: float

```{autodoc2-docstring} dss.ISettings.ISettings.LossWeight
```

````

````{py:property} NormVmaxpu
:canonical: dss.ISettings.ISettings.NormVmaxpu
:type: float

```{autodoc2-docstring} dss.ISettings.ISettings.NormVmaxpu
```

````

````{py:property} NormVminpu
:canonical: dss.ISettings.ISettings.NormVminpu
:type: float

```{autodoc2-docstring} dss.ISettings.ISettings.NormVminpu
```

````

````{py:property} PriceCurve
:canonical: dss.ISettings.ISettings.PriceCurve
:type: str

```{autodoc2-docstring} dss.ISettings.ISettings.PriceCurve
```

````

````{py:property} PriceSignal
:canonical: dss.ISettings.ISettings.PriceSignal
:type: float

```{autodoc2-docstring} dss.ISettings.ISettings.PriceSignal
```

````

````{py:method} SetPropertyNameStyle(value: dss.enums.DSSPropertyNameStyle)
:canonical: dss.ISettings.ISettings.SetPropertyNameStyle

```{autodoc2-docstring} dss.ISettings.ISettings.SetPropertyNameStyle
```

````

````{py:property} Trapezoidal
:canonical: dss.ISettings.ISettings.Trapezoidal
:type: bool

```{autodoc2-docstring} dss.ISettings.ISettings.Trapezoidal
```

````

````{py:property} UEregs
:canonical: dss.ISettings.ISettings.UEregs
:type: dss._types.Int32Array

```{autodoc2-docstring} dss.ISettings.ISettings.UEregs
```

````

````{py:property} UEweight
:canonical: dss.ISettings.ISettings.UEweight
:type: float

```{autodoc2-docstring} dss.ISettings.ISettings.UEweight
```

````

````{py:property} VoltageBases
:canonical: dss.ISettings.ISettings.VoltageBases
:type: dss._types.Float64Array

```{autodoc2-docstring} dss.ISettings.ISettings.VoltageBases
```

````

````{py:property} ZoneLock
:canonical: dss.ISettings.ISettings.ZoneLock
:type: bool

```{autodoc2-docstring} dss.ISettings.ISettings.ZoneLock
```

````

````{py:method} __init__(api_util, prefer_lists=False)
:canonical: dss.ISettings.ISettings.__init__

```{autodoc2-docstring} dss.ISettings.ISettings.__init__
```

````

`````
