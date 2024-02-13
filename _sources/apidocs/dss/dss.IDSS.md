# {py:mod}`dss.IDSS`

```{py:module} dss.IDSS
```

```{autodoc2-docstring} dss.IDSS
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IDSS <dss.IDSS.IDSS>`
  - ```{autodoc2-docstring} dss.IDSS.IDSS
    :summary:
    ```
````

### API

`````{py:class} IDSS(api_util)
:canonical: dss.IDSS.IDSS

Bases: {py:obj}`dss._cffi_api_util.Base`

```{autodoc2-docstring} dss.IDSS.IDSS
```

````{py:attribute} ActiveCircuit
:canonical: dss.IDSS.IDSS.ActiveCircuit
:type: dss.ICircuit.ICircuit
:value: >
   None

```{autodoc2-docstring} dss.IDSS.IDSS.ActiveCircuit
```

````

````{py:attribute} ActiveClass
:canonical: dss.IDSS.IDSS.ActiveClass
:type: dss.IActiveClass.IActiveClass
:value: >
   None

```{autodoc2-docstring} dss.IDSS.IDSS.ActiveClass
```

````

````{py:property} AdvancedTypes
:canonical: dss.IDSS.IDSS.AdvancedTypes
:type: bool

```{autodoc2-docstring} dss.IDSS.IDSS.AdvancedTypes
```

````

````{py:property} AllowChangeDir
:canonical: dss.IDSS.IDSS.AllowChangeDir
:type: bool

```{autodoc2-docstring} dss.IDSS.IDSS.AllowChangeDir
```

````

````{py:property} AllowDOScmd
:canonical: dss.IDSS.IDSS.AllowDOScmd
:type: bool

```{autodoc2-docstring} dss.IDSS.IDSS.AllowDOScmd
```

````

````{py:property} AllowEditor
:canonical: dss.IDSS.IDSS.AllowEditor
:type: bool

```{autodoc2-docstring} dss.IDSS.IDSS.AllowEditor
```

````

````{py:property} AllowForms
:canonical: dss.IDSS.IDSS.AllowForms
:type: bool

```{autodoc2-docstring} dss.IDSS.IDSS.AllowForms
```

````

````{py:property} COMErrorResults
:canonical: dss.IDSS.IDSS.COMErrorResults
:type: bool

```{autodoc2-docstring} dss.IDSS.IDSS.COMErrorResults
```

````

````{py:attribute} Circuits
:canonical: dss.IDSS.IDSS.Circuits
:type: dss.ICircuit.ICircuit
:value: >
   None

```{autodoc2-docstring} dss.IDSS.IDSS.Circuits
```

````

````{py:property} Classes
:canonical: dss.IDSS.IDSS.Classes
:type: typing.List[str]

```{autodoc2-docstring} dss.IDSS.IDSS.Classes
```

````

````{py:method} ClearAll()
:canonical: dss.IDSS.IDSS.ClearAll

```{autodoc2-docstring} dss.IDSS.IDSS.ClearAll
```

````

````{py:property} CompatFlags
:canonical: dss.IDSS.IDSS.CompatFlags
:type: int

```{autodoc2-docstring} dss.IDSS.IDSS.CompatFlags
```

````

````{py:attribute} DSSProgress
:canonical: dss.IDSS.IDSS.DSSProgress
:type: dss.IDSSProgress.IDSSProgress
:value: >
   None

```{autodoc2-docstring} dss.IDSS.IDSS.DSSProgress
```

````

````{py:attribute} DSSim_Coms
:canonical: dss.IDSS.IDSS.DSSim_Coms
:type: dss.IDSSimComs.IDSSimComs
:value: >
   None

```{autodoc2-docstring} dss.IDSS.IDSS.DSSim_Coms
```

````

````{py:property} DataPath
:canonical: dss.IDSS.IDSS.DataPath
:type: str

```{autodoc2-docstring} dss.IDSS.IDSS.DataPath
```

````

````{py:property} DefaultEditor
:canonical: dss.IDSS.IDSS.DefaultEditor
:type: str

```{autodoc2-docstring} dss.IDSS.IDSS.DefaultEditor
```

````

````{py:attribute} Error
:canonical: dss.IDSS.IDSS.Error
:type: dss.IError.IError
:value: >
   None

```{autodoc2-docstring} dss.IDSS.IDSS.Error
```

````

````{py:attribute} Events
:canonical: dss.IDSS.IDSS.Events
:type: dss.IDSSEvents.IDSSEvents
:value: >
   None

```{autodoc2-docstring} dss.IDSS.IDSS.Events
```

````

````{py:attribute} Executive
:canonical: dss.IDSS.IDSS.Executive
:type: dss.IDSS_Executive.IDSS_Executive
:value: >
   None

```{autodoc2-docstring} dss.IDSS.IDSS.Executive
```

````

````{py:property} LegacyModels
:canonical: dss.IDSS.IDSS.LegacyModels
:type: bool

```{autodoc2-docstring} dss.IDSS.IDSS.LegacyModels
```

````

````{py:method} NewCircuit(name) -> dss.ICircuit.ICircuit
:canonical: dss.IDSS.IDSS.NewCircuit

```{autodoc2-docstring} dss.IDSS.IDSS.NewCircuit
```

````

````{py:method} NewContext() -> dss.IDSS.IDSS
:canonical: dss.IDSS.IDSS.NewContext

```{autodoc2-docstring} dss.IDSS.IDSS.NewContext
```

````

````{py:property} NumCircuits
:canonical: dss.IDSS.IDSS.NumCircuits
:type: int

```{autodoc2-docstring} dss.IDSS.IDSS.NumCircuits
```

````

````{py:property} NumClasses
:canonical: dss.IDSS.IDSS.NumClasses
:type: int

```{autodoc2-docstring} dss.IDSS.IDSS.NumClasses
```

````

````{py:property} NumUserClasses
:canonical: dss.IDSS.IDSS.NumUserClasses
:type: int

```{autodoc2-docstring} dss.IDSS.IDSS.NumUserClasses
```

````

````{py:property} Obj
:canonical: dss.IDSS.IDSS.Obj
:type: altdss.AltDSS

```{autodoc2-docstring} dss.IDSS.IDSS.Obj
```

````

````{py:attribute} Parser
:canonical: dss.IDSS.IDSS.Parser
:type: dss.IParser.IParser
:value: >
   None

```{autodoc2-docstring} dss.IDSS.IDSS.Parser
```

````

````{py:property} Plotting
:canonical: dss.IDSS.IDSS.Plotting

```{autodoc2-docstring} dss.IDSS.IDSS.Plotting
```

````

````{py:method} Reset()
:canonical: dss.IDSS.IDSS.Reset

```{autodoc2-docstring} dss.IDSS.IDSS.Reset
```

````

````{py:method} SetActiveClass(ClassName: typing.AnyStr) -> int
:canonical: dss.IDSS.IDSS.SetActiveClass

```{autodoc2-docstring} dss.IDSS.IDSS.SetActiveClass
```

````

````{py:method} ShowPanel()
:canonical: dss.IDSS.IDSS.ShowPanel

```{autodoc2-docstring} dss.IDSS.IDSS.ShowPanel
```

````

````{py:method} Start(code: int) -> bool
:canonical: dss.IDSS.IDSS.Start

```{autodoc2-docstring} dss.IDSS.IDSS.Start
```

````

````{py:attribute} Text
:canonical: dss.IDSS.IDSS.Text
:type: dss.IText.IText
:value: >
   None

```{autodoc2-docstring} dss.IDSS.IDSS.Text
```

````

````{py:property} UserClasses
:canonical: dss.IDSS.IDSS.UserClasses
:type: typing.List[str]

```{autodoc2-docstring} dss.IDSS.IDSS.UserClasses
```

````

````{py:property} Version
:canonical: dss.IDSS.IDSS.Version
:type: str

```{autodoc2-docstring} dss.IDSS.IDSS.Version
```

````

````{py:attribute} YMatrix
:canonical: dss.IDSS.IDSS.YMatrix
:type: dss.IYMatrix.IYMatrix
:value: >
   None

```{autodoc2-docstring} dss.IDSS.IDSS.YMatrix
```

````

````{py:attribute} ZIP
:canonical: dss.IDSS.IDSS.ZIP
:type: dss.IZIP.IZIP
:value: >
   None

```{autodoc2-docstring} dss.IDSS.IDSS.ZIP
```

````

````{py:method} __call__(cmds: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]])
:canonical: dss.IDSS.IDSS.__call__

```{autodoc2-docstring} dss.IDSS.IDSS.__call__
```

````

````{py:method} __init__(api_util)
:canonical: dss.IDSS.IDSS.__init__

```{autodoc2-docstring} dss.IDSS.IDSS.__init__
```

````

````{py:method} to_altdss() -> altdss.AltDSS
:canonical: dss.IDSS.IDSS.to_altdss

```{autodoc2-docstring} dss.IDSS.IDSS.to_altdss
```

````

````{py:method} to_opendssdirect() -> opendssdirect.OpenDSSDirect.OpenDSSDirect
:canonical: dss.IDSS.IDSS.to_opendssdirect

```{autodoc2-docstring} dss.IDSS.IDSS.to_opendssdirect
```

````

`````
