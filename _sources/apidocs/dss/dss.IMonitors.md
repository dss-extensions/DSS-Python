# {py:mod}`dss.IMonitors`

```{py:module} dss.IMonitors
```

```{autodoc2-docstring} dss.IMonitors
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IMonitors <dss.IMonitors.IMonitors>`
  - ```{autodoc2-docstring} dss.IMonitors.IMonitors
    :summary:
    ```
````

### API

`````{py:class} IMonitors(api_util)
:canonical: dss.IMonitors.IMonitors

Bases: {py:obj}`dss._cffi_api_util.Iterable`

```{autodoc2-docstring} dss.IMonitors.IMonitors
```

````{py:property} AllNames
:canonical: dss.IMonitors.IMonitors.AllNames
:type: typing.List[str]

```{autodoc2-docstring} dss.IMonitors.IMonitors.AllNames
```

````

````{py:method} AsMatrix() -> dss._types.Float64Array
:canonical: dss.IMonitors.IMonitors.AsMatrix

```{autodoc2-docstring} dss.IMonitors.IMonitors.AsMatrix
```

````

````{py:property} ByteStream
:canonical: dss.IMonitors.IMonitors.ByteStream
:type: dss._types.Int8Array

```{autodoc2-docstring} dss.IMonitors.IMonitors.ByteStream
```

````

````{py:method} Channel(Index: int) -> dss._types.Float32Array
:canonical: dss.IMonitors.IMonitors.Channel

```{autodoc2-docstring} dss.IMonitors.IMonitors.Channel
```

````

````{py:property} Count
:canonical: dss.IMonitors.IMonitors.Count
:type: int

```{autodoc2-docstring} dss.IMonitors.IMonitors.Count
```

````

````{py:property} Element
:canonical: dss.IMonitors.IMonitors.Element
:type: str

```{autodoc2-docstring} dss.IMonitors.IMonitors.Element
```

````

````{py:property} FileName
:canonical: dss.IMonitors.IMonitors.FileName
:type: str

```{autodoc2-docstring} dss.IMonitors.IMonitors.FileName
```

````

````{py:property} FileVersion
:canonical: dss.IMonitors.IMonitors.FileVersion
:type: int

```{autodoc2-docstring} dss.IMonitors.IMonitors.FileVersion
```

````

````{py:property} First
:canonical: dss.IMonitors.IMonitors.First
:type: int

```{autodoc2-docstring} dss.IMonitors.IMonitors.First
```

````

````{py:property} Header
:canonical: dss.IMonitors.IMonitors.Header
:type: typing.List[str]

```{autodoc2-docstring} dss.IMonitors.IMonitors.Header
```

````

````{py:property} Mode
:canonical: dss.IMonitors.IMonitors.Mode
:type: int

```{autodoc2-docstring} dss.IMonitors.IMonitors.Mode
```

````

````{py:property} Name
:canonical: dss.IMonitors.IMonitors.Name
:type: str

```{autodoc2-docstring} dss.IMonitors.IMonitors.Name
```

````

````{py:property} Next
:canonical: dss.IMonitors.IMonitors.Next
:type: int

```{autodoc2-docstring} dss.IMonitors.IMonitors.Next
```

````

````{py:property} NumChannels
:canonical: dss.IMonitors.IMonitors.NumChannels
:type: int

```{autodoc2-docstring} dss.IMonitors.IMonitors.NumChannels
```

````

````{py:method} Process()
:canonical: dss.IMonitors.IMonitors.Process

```{autodoc2-docstring} dss.IMonitors.IMonitors.Process
```

````

````{py:method} ProcessAll()
:canonical: dss.IMonitors.IMonitors.ProcessAll

```{autodoc2-docstring} dss.IMonitors.IMonitors.ProcessAll
```

````

````{py:property} RecordSize
:canonical: dss.IMonitors.IMonitors.RecordSize
:type: int

```{autodoc2-docstring} dss.IMonitors.IMonitors.RecordSize
```

````

````{py:method} Reset()
:canonical: dss.IMonitors.IMonitors.Reset

```{autodoc2-docstring} dss.IMonitors.IMonitors.Reset
```

````

````{py:method} ResetAll()
:canonical: dss.IMonitors.IMonitors.ResetAll

```{autodoc2-docstring} dss.IMonitors.IMonitors.ResetAll
```

````

````{py:method} Sample()
:canonical: dss.IMonitors.IMonitors.Sample

```{autodoc2-docstring} dss.IMonitors.IMonitors.Sample
```

````

````{py:method} SampleAll()
:canonical: dss.IMonitors.IMonitors.SampleAll

```{autodoc2-docstring} dss.IMonitors.IMonitors.SampleAll
```

````

````{py:property} SampleCount
:canonical: dss.IMonitors.IMonitors.SampleCount
:type: int

```{autodoc2-docstring} dss.IMonitors.IMonitors.SampleCount
```

````

````{py:method} Save()
:canonical: dss.IMonitors.IMonitors.Save

```{autodoc2-docstring} dss.IMonitors.IMonitors.Save
```

````

````{py:method} SaveAll()
:canonical: dss.IMonitors.IMonitors.SaveAll

```{autodoc2-docstring} dss.IMonitors.IMonitors.SaveAll
```

````

````{py:method} Show()
:canonical: dss.IMonitors.IMonitors.Show

```{autodoc2-docstring} dss.IMonitors.IMonitors.Show
```

````

````{py:property} Terminal
:canonical: dss.IMonitors.IMonitors.Terminal
:type: int

```{autodoc2-docstring} dss.IMonitors.IMonitors.Terminal
```

````

````{py:method} __init__(api_util)
:canonical: dss.IMonitors.IMonitors.__init__

```{autodoc2-docstring} dss.IMonitors.IMonitors.__init__
```

````

````{py:method} __iter__() -> typing.Iterator[dss._cffi_api_util.Iterable]
:canonical: dss.IMonitors.IMonitors.__iter__

```{autodoc2-docstring} dss.IMonitors.IMonitors.__iter__
```

````

````{py:method} __len__() -> int
:canonical: dss.IMonitors.IMonitors.__len__

```{autodoc2-docstring} dss.IMonitors.IMonitors.__len__
```

````

````{py:property} dblFreq
:canonical: dss.IMonitors.IMonitors.dblFreq
:type: dss._types.Float64Array

```{autodoc2-docstring} dss.IMonitors.IMonitors.dblFreq
```

````

````{py:property} dblHour
:canonical: dss.IMonitors.IMonitors.dblHour
:type: dss._types.Float64Array

```{autodoc2-docstring} dss.IMonitors.IMonitors.dblHour
```

````

````{py:property} idx
:canonical: dss.IMonitors.IMonitors.idx
:type: int

```{autodoc2-docstring} dss.IMonitors.IMonitors.idx
```

````

`````
