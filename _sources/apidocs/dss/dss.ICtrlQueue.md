# {py:mod}`dss.ICtrlQueue`

```{py:module} dss.ICtrlQueue
```

```{autodoc2-docstring} dss.ICtrlQueue
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ICtrlQueue <dss.ICtrlQueue.ICtrlQueue>`
  - ```{autodoc2-docstring} dss.ICtrlQueue.ICtrlQueue
    :summary:
    ```
````

### API

`````{py:class} ICtrlQueue(api_util, prefer_lists=False)
:canonical: dss.ICtrlQueue.ICtrlQueue

Bases: {py:obj}`dss._cffi_api_util.Base`

```{autodoc2-docstring} dss.ICtrlQueue.ICtrlQueue
```

````{py:property} Action
:canonical: dss.ICtrlQueue.ICtrlQueue.Action
:type: int

```{autodoc2-docstring} dss.ICtrlQueue.ICtrlQueue.Action
```

````

````{py:property} ActionCode
:canonical: dss.ICtrlQueue.ICtrlQueue.ActionCode
:type: int

```{autodoc2-docstring} dss.ICtrlQueue.ICtrlQueue.ActionCode
```

````

````{py:method} ClearActions()
:canonical: dss.ICtrlQueue.ICtrlQueue.ClearActions

```{autodoc2-docstring} dss.ICtrlQueue.ICtrlQueue.ClearActions
```

````

````{py:method} ClearQueue()
:canonical: dss.ICtrlQueue.ICtrlQueue.ClearQueue

```{autodoc2-docstring} dss.ICtrlQueue.ICtrlQueue.ClearQueue
```

````

````{py:method} Delete(ActionHandle)
:canonical: dss.ICtrlQueue.ICtrlQueue.Delete

```{autodoc2-docstring} dss.ICtrlQueue.ICtrlQueue.Delete
```

````

````{py:property} DeviceHandle
:canonical: dss.ICtrlQueue.ICtrlQueue.DeviceHandle
:type: int

```{autodoc2-docstring} dss.ICtrlQueue.ICtrlQueue.DeviceHandle
```

````

````{py:method} DoAllQueue()
:canonical: dss.ICtrlQueue.ICtrlQueue.DoAllQueue

```{autodoc2-docstring} dss.ICtrlQueue.ICtrlQueue.DoAllQueue
```

````

````{py:property} NumActions
:canonical: dss.ICtrlQueue.ICtrlQueue.NumActions
:type: int

```{autodoc2-docstring} dss.ICtrlQueue.ICtrlQueue.NumActions
```

````

````{py:property} PopAction
:canonical: dss.ICtrlQueue.ICtrlQueue.PopAction
:type: int

```{autodoc2-docstring} dss.ICtrlQueue.ICtrlQueue.PopAction
```

````

````{py:method} Push(Hour: int, Seconds: float, ActionCode: int, DeviceHandle: int)
:canonical: dss.ICtrlQueue.ICtrlQueue.Push

```{autodoc2-docstring} dss.ICtrlQueue.ICtrlQueue.Push
```

````

````{py:property} Queue
:canonical: dss.ICtrlQueue.ICtrlQueue.Queue
:type: typing.List[str]

```{autodoc2-docstring} dss.ICtrlQueue.ICtrlQueue.Queue
```

````

````{py:property} QueueSize
:canonical: dss.ICtrlQueue.ICtrlQueue.QueueSize
:type: int

```{autodoc2-docstring} dss.ICtrlQueue.ICtrlQueue.QueueSize
```

````

````{py:method} Show()
:canonical: dss.ICtrlQueue.ICtrlQueue.Show

```{autodoc2-docstring} dss.ICtrlQueue.ICtrlQueue.Show
```

````

````{py:method} __init__(api_util, prefer_lists=False)
:canonical: dss.ICtrlQueue.ICtrlQueue.__init__

```{autodoc2-docstring} dss.ICtrlQueue.ICtrlQueue.__init__
```

````

`````
