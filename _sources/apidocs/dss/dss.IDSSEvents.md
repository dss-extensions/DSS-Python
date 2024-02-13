# {py:mod}`dss.IDSSEvents`

```{py:module} dss.IDSSEvents
```

```{autodoc2-docstring} dss.IDSSEvents
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DSSEventsConnection <dss.IDSSEvents.DSSEventsConnection>`
  - ```{autodoc2-docstring} dss.IDSSEvents.DSSEventsConnection
    :summary:
    ```
* - {py:obj}`IDSSEvents <dss.IDSSEvents.IDSSEvents>`
  - ```{autodoc2-docstring} dss.IDSSEvents.IDSSEvents
    :summary:
    ```
````

### API

`````{py:class} DSSEventsConnection(api_util, handler)
:canonical: dss.IDSSEvents.DSSEventsConnection

```{autodoc2-docstring} dss.IDSSEvents.DSSEventsConnection
```

````{py:method} __init__(api_util, handler)
:canonical: dss.IDSSEvents.DSSEventsConnection.__init__

```{autodoc2-docstring} dss.IDSSEvents.DSSEventsConnection.__init__
```

````

````{py:method} close()
:canonical: dss.IDSSEvents.DSSEventsConnection.close

```{autodoc2-docstring} dss.IDSSEvents.DSSEventsConnection.close
```

````

````{py:method} disconnect()
:canonical: dss.IDSSEvents.DSSEventsConnection.disconnect

```{autodoc2-docstring} dss.IDSSEvents.DSSEventsConnection.disconnect
```

````

`````

`````{py:class} IDSSEvents(api_util, prefer_lists=False)
:canonical: dss.IDSSEvents.IDSSEvents

Bases: {py:obj}`dss._cffi_api_util.Base`

```{autodoc2-docstring} dss.IDSSEvents.IDSSEvents
```

````{py:method} GetEvents(handler_obj) -> dss.IDSSEvents.DSSEventsConnection
:canonical: dss.IDSSEvents.IDSSEvents.GetEvents

```{autodoc2-docstring} dss.IDSSEvents.IDSSEvents.GetEvents
```

````

````{py:method} WithEvents(handler_class) -> dss.IDSSEvents.DSSEventsConnection
:canonical: dss.IDSSEvents.IDSSEvents.WithEvents

```{autodoc2-docstring} dss.IDSSEvents.IDSSEvents.WithEvents
```

````

````{py:method} __init__(api_util, prefer_lists=False)
:canonical: dss.IDSSEvents.IDSSEvents.__init__

```{autodoc2-docstring} dss.IDSSEvents.IDSSEvents.__init__
```

````

`````
