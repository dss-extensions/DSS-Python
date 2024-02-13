# {py:mod}`dss.IYMatrix`

```{py:module} dss.IYMatrix
```

```{autodoc2-docstring} dss.IYMatrix
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IYMatrix <dss.IYMatrix.IYMatrix>`
  - ```{autodoc2-docstring} dss.IYMatrix.IYMatrix
    :summary:
    ```
````

### API

`````{py:class} IYMatrix(api_util, prefer_lists=False)
:canonical: dss.IYMatrix.IYMatrix

Bases: {py:obj}`dss._cffi_api_util.Base`

```{autodoc2-docstring} dss.IYMatrix.IYMatrix
```

````{py:method} AddInAuxCurrents(SType)
:canonical: dss.IYMatrix.IYMatrix.AddInAuxCurrents

```{autodoc2-docstring} dss.IYMatrix.IYMatrix.AddInAuxCurrents
```

````

````{py:method} BuildYMatrixD(BuildOps: int, AllocateVI: bool)
:canonical: dss.IYMatrix.IYMatrix.BuildYMatrixD

```{autodoc2-docstring} dss.IYMatrix.IYMatrix.BuildYMatrixD
```

````

````{py:method} CheckConvergence() -> bool
:canonical: dss.IYMatrix.IYMatrix.CheckConvergence

```{autodoc2-docstring} dss.IYMatrix.IYMatrix.CheckConvergence
```

````

````{py:method} GetCompressedYMatrix(factor: bool = True) -> typing.Tuple[dss._types.ComplexArray, dss._types.Int32Array, dss._types.Int32Array]
:canonical: dss.IYMatrix.IYMatrix.GetCompressedYMatrix

```{autodoc2-docstring} dss.IYMatrix.IYMatrix.GetCompressedYMatrix
```

````

````{py:method} GetIPointer()
:canonical: dss.IYMatrix.IYMatrix.GetIPointer

```{autodoc2-docstring} dss.IYMatrix.IYMatrix.GetIPointer
```

````

````{py:method} GetPCInjCurr()
:canonical: dss.IYMatrix.IYMatrix.GetPCInjCurr

```{autodoc2-docstring} dss.IYMatrix.IYMatrix.GetPCInjCurr
```

````

````{py:method} GetSourceInjCurrents()
:canonical: dss.IYMatrix.IYMatrix.GetSourceInjCurrents

```{autodoc2-docstring} dss.IYMatrix.IYMatrix.GetSourceInjCurrents
```

````

````{py:method} GetVPointer()
:canonical: dss.IYMatrix.IYMatrix.GetVPointer

```{autodoc2-docstring} dss.IYMatrix.IYMatrix.GetVPointer
```

````

````{py:property} Iteration
:canonical: dss.IYMatrix.IYMatrix.Iteration
:type: int

```{autodoc2-docstring} dss.IYMatrix.IYMatrix.Iteration
```

````

````{py:property} LoadsNeedUpdating
:canonical: dss.IYMatrix.IYMatrix.LoadsNeedUpdating
:type: bool

```{autodoc2-docstring} dss.IYMatrix.IYMatrix.LoadsNeedUpdating
```

````

````{py:method} SetGeneratordQdV()
:canonical: dss.IYMatrix.IYMatrix.SetGeneratordQdV

```{autodoc2-docstring} dss.IYMatrix.IYMatrix.SetGeneratordQdV
```

````

````{py:property} SolutionInitialized
:canonical: dss.IYMatrix.IYMatrix.SolutionInitialized
:type: bool

```{autodoc2-docstring} dss.IYMatrix.IYMatrix.SolutionInitialized
```

````

````{py:method} SolveSystem(NodeV=None) -> int
:canonical: dss.IYMatrix.IYMatrix.SolveSystem

```{autodoc2-docstring} dss.IYMatrix.IYMatrix.SolveSystem
```

````

````{py:property} SolverOptions
:canonical: dss.IYMatrix.IYMatrix.SolverOptions
:type: int

```{autodoc2-docstring} dss.IYMatrix.IYMatrix.SolverOptions
```

````

````{py:property} SystemYChanged
:canonical: dss.IYMatrix.IYMatrix.SystemYChanged
:type: bool

```{autodoc2-docstring} dss.IYMatrix.IYMatrix.SystemYChanged
```

````

````{py:property} UseAuxCurrents
:canonical: dss.IYMatrix.IYMatrix.UseAuxCurrents
:type: bool

```{autodoc2-docstring} dss.IYMatrix.IYMatrix.UseAuxCurrents
```

````

````{py:method} ZeroInjCurr()
:canonical: dss.IYMatrix.IYMatrix.ZeroInjCurr

```{autodoc2-docstring} dss.IYMatrix.IYMatrix.ZeroInjCurr
```

````

````{py:method} __init__(api_util, prefer_lists=False)
:canonical: dss.IYMatrix.IYMatrix.__init__

```{autodoc2-docstring} dss.IYMatrix.IYMatrix.__init__
```

````

````{py:method} getI() -> typing.List[float]
:canonical: dss.IYMatrix.IYMatrix.getI

```{autodoc2-docstring} dss.IYMatrix.IYMatrix.getI
```

````

````{py:method} getV() -> typing.List[float]
:canonical: dss.IYMatrix.IYMatrix.getV

```{autodoc2-docstring} dss.IYMatrix.IYMatrix.getV
```

````

````{py:attribute} getYSparse
:canonical: dss.IYMatrix.IYMatrix.getYSparse
:value: >
   None

```{autodoc2-docstring} dss.IYMatrix.IYMatrix.getYSparse
```

````

`````
