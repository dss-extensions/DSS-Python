# {py:mod}`dss.IParser`

```{py:module} dss.IParser
```

```{autodoc2-docstring} dss.IParser
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IParser <dss.IParser.IParser>`
  - ```{autodoc2-docstring} dss.IParser.IParser
    :summary:
    ```
````

### API

`````{py:class} IParser(api_util, prefer_lists=False)
:canonical: dss.IParser.IParser

Bases: {py:obj}`dss._cffi_api_util.Base`

```{autodoc2-docstring} dss.IParser.IParser
```

````{py:property} AutoIncrement
:canonical: dss.IParser.IParser.AutoIncrement
:type: bool

```{autodoc2-docstring} dss.IParser.IParser.AutoIncrement
```

````

````{py:property} BeginQuote
:canonical: dss.IParser.IParser.BeginQuote
:type: str

```{autodoc2-docstring} dss.IParser.IParser.BeginQuote
```

````

````{py:property} CmdString
:canonical: dss.IParser.IParser.CmdString
:type: str

```{autodoc2-docstring} dss.IParser.IParser.CmdString
```

````

````{py:property} DblValue
:canonical: dss.IParser.IParser.DblValue
:type: float

```{autodoc2-docstring} dss.IParser.IParser.DblValue
```

````

````{py:property} Delimiters
:canonical: dss.IParser.IParser.Delimiters
:type: str

```{autodoc2-docstring} dss.IParser.IParser.Delimiters
```

````

````{py:property} EndQuote
:canonical: dss.IParser.IParser.EndQuote
:type: str

```{autodoc2-docstring} dss.IParser.IParser.EndQuote
```

````

````{py:property} IntValue
:canonical: dss.IParser.IParser.IntValue
:type: int

```{autodoc2-docstring} dss.IParser.IParser.IntValue
```

````

````{py:method} Matrix(ExpectedOrder: int) -> dss._types.Float64Array
:canonical: dss.IParser.IParser.Matrix

```{autodoc2-docstring} dss.IParser.IParser.Matrix
```

````

````{py:property} NextParam
:canonical: dss.IParser.IParser.NextParam
:type: str

```{autodoc2-docstring} dss.IParser.IParser.NextParam
```

````

````{py:method} ResetDelimiters()
:canonical: dss.IParser.IParser.ResetDelimiters

```{autodoc2-docstring} dss.IParser.IParser.ResetDelimiters
```

````

````{py:property} StrValue
:canonical: dss.IParser.IParser.StrValue
:type: str

```{autodoc2-docstring} dss.IParser.IParser.StrValue
```

````

````{py:method} SymMatrix(ExpectedOrder: int) -> dss._types.Float64Array
:canonical: dss.IParser.IParser.SymMatrix

```{autodoc2-docstring} dss.IParser.IParser.SymMatrix
```

````

````{py:method} Vector(ExpectedSize: int) -> dss._types.Float64Array
:canonical: dss.IParser.IParser.Vector

```{autodoc2-docstring} dss.IParser.IParser.Vector
```

````

````{py:property} WhiteSpace
:canonical: dss.IParser.IParser.WhiteSpace
:type: str

```{autodoc2-docstring} dss.IParser.IParser.WhiteSpace
```

````

````{py:method} __init__(api_util, prefer_lists=False)
:canonical: dss.IParser.IParser.__init__

```{autodoc2-docstring} dss.IParser.IParser.__init__
```

````

`````
