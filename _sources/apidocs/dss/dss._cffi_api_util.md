---
orphan: true
---

# {py:mod}`dss._cffi_api_util`

```{py:module} dss._cffi_api_util
```

```{autodoc2-docstring} dss._cffi_api_util
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Base <dss._cffi_api_util.Base>`
  - ```{autodoc2-docstring} dss._cffi_api_util.Base
    :summary:
    ```
* - {py:obj}`CffiApiUtil <dss._cffi_api_util.CffiApiUtil>`
  - ```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil
    :summary:
    ```
* - {py:obj}`CtxLib <dss._cffi_api_util.CtxLib>`
  - ```{autodoc2-docstring} dss._cffi_api_util.CtxLib
    :summary:
    ```
* - {py:obj}`Iterable <dss._cffi_api_util.Iterable>`
  - ```{autodoc2-docstring} dss._cffi_api_util.Iterable
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`altdss_python_util_callback <dss._cffi_api_util.altdss_python_util_callback>`
  - ```{autodoc2-docstring} dss._cffi_api_util.altdss_python_util_callback
    :summary:
    ```
* - {py:obj}`set_case_insensitive_attributes <dss._cffi_api_util.set_case_insensitive_attributes>`
  - ```{autodoc2-docstring} dss._cffi_api_util.set_case_insensitive_attributes
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DssException <dss._cffi_api_util.DssException>`
  - ```{autodoc2-docstring} dss._cffi_api_util.DssException
    :summary:
    ```
* - {py:obj}`codec <dss._cffi_api_util.codec>`
  - ```{autodoc2-docstring} dss._cffi_api_util.codec
    :summary:
    ```
* - {py:obj}`interface_classes <dss._cffi_api_util.interface_classes>`
  - ```{autodoc2-docstring} dss._cffi_api_util.interface_classes
    :summary:
    ```
* - {py:obj}`use_com_compat <dss._cffi_api_util.use_com_compat>`
  - ```{autodoc2-docstring} dss._cffi_api_util.use_com_compat
    :summary:
    ```
* - {py:obj}`warn_wrong_case <dss._cffi_api_util.warn_wrong_case>`
  - ```{autodoc2-docstring} dss._cffi_api_util.warn_wrong_case
    :summary:
    ```
````

### API

`````{py:class} Base(api_util, prefer_lists=False)
:canonical: dss._cffi_api_util.Base

```{autodoc2-docstring} dss._cffi_api_util.Base
```

````{py:method} __init__(api_util, prefer_lists=False)
:canonical: dss._cffi_api_util.Base.__init__

```{autodoc2-docstring} dss._cffi_api_util.Base.__init__
```

````

`````

`````{py:class} CffiApiUtil(ffi, lib, ctx=None)
:canonical: dss._cffi_api_util.CffiApiUtil

Bases: {py:obj}`object`

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil
```

````{py:method} __del__()
:canonical: dss._cffi_api_util.CffiApiUtil.__del__

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.__del__
```

````

````{py:method} __init__(ffi, lib, ctx=None)
:canonical: dss._cffi_api_util.CffiApiUtil.__init__

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.__init__
```

````

````{py:method} clear_buffers()
:canonical: dss._cffi_api_util.CffiApiUtil.clear_buffers

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.clear_buffers
```

````

````{py:method} clear_callback(step: int)
:canonical: dss._cffi_api_util.CffiApiUtil.clear_callback

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.clear_callback
```

````

````{py:method} get_complex128_array(func, *args) -> dss._types.Float64ArrayOrComplexArray
:canonical: dss._cffi_api_util.CffiApiUtil.get_complex128_array

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.get_complex128_array
```

````

````{py:method} get_complex128_array2(func, *args) -> dss._types.Float64ArrayOrComplexArray
:canonical: dss._cffi_api_util.CffiApiUtil.get_complex128_array2

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.get_complex128_array2
```

````

````{py:method} get_complex128_gr_array() -> dss._types.ComplexArray
:canonical: dss._cffi_api_util.CffiApiUtil.get_complex128_gr_array

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.get_complex128_gr_array
```

````

````{py:method} get_complex128_gr_array2() -> typing.List[typing.Union[complex, float]]
:canonical: dss._cffi_api_util.CffiApiUtil.get_complex128_gr_array2

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.get_complex128_gr_array2
```

````

````{py:method} get_complex128_gr_simple() -> dss._types.Float64ArrayOrSimpleComplex
:canonical: dss._cffi_api_util.CffiApiUtil.get_complex128_gr_simple

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.get_complex128_gr_simple
```

````

````{py:method} get_complex128_gr_simple2() -> typing.List[typing.Union[complex, float]]
:canonical: dss._cffi_api_util.CffiApiUtil.get_complex128_gr_simple2

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.get_complex128_gr_simple2
```

````

````{py:method} get_complex128_simple(func, *args) -> dss._types.Float64ArrayOrSimpleComplex
:canonical: dss._cffi_api_util.CffiApiUtil.get_complex128_simple

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.get_complex128_simple
```

````

````{py:method} get_complex128_simple2(func, *args) -> typing.List[typing.Union[complex, float]]
:canonical: dss._cffi_api_util.CffiApiUtil.get_complex128_simple2

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.get_complex128_simple2
```

````

````{py:method} get_fcomplex128_array(func, *args) -> typing.Union[dss._types.ComplexArray, None]
:canonical: dss._cffi_api_util.CffiApiUtil.get_fcomplex128_array

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.get_fcomplex128_array
```

````

````{py:method} get_fcomplex128_gr_array() -> dss._types.ComplexArray
:canonical: dss._cffi_api_util.CffiApiUtil.get_fcomplex128_gr_array

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.get_fcomplex128_gr_array
```

````

````{py:method} get_fcomplex128_gr_simple() -> complex
:canonical: dss._cffi_api_util.CffiApiUtil.get_fcomplex128_gr_simple

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.get_fcomplex128_gr_simple
```

````

````{py:method} get_fcomplex128_simple(func, *args) -> dss._types.Float64ArrayOrSimpleComplex
:canonical: dss._cffi_api_util.CffiApiUtil.get_fcomplex128_simple

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.get_fcomplex128_simple
```

````

````{py:method} get_float64_array(func, *args) -> dss._types.Float64Array
:canonical: dss._cffi_api_util.CffiApiUtil.get_float64_array

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.get_float64_array
```

````

````{py:method} get_float64_array2(func, *args)
:canonical: dss._cffi_api_util.CffiApiUtil.get_float64_array2

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.get_float64_array2
```

````

````{py:method} get_float64_gr_array() -> dss._types.Float64Array
:canonical: dss._cffi_api_util.CffiApiUtil.get_float64_gr_array

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.get_float64_gr_array
```

````

````{py:method} get_float64_gr_array2()
:canonical: dss._cffi_api_util.CffiApiUtil.get_float64_gr_array2

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.get_float64_gr_array2
```

````

````{py:method} get_int32_array(func: typing.Callable, *args) -> dss._types.Int32Array
:canonical: dss._cffi_api_util.CffiApiUtil.get_int32_array

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.get_int32_array
```

````

````{py:method} get_int32_array2(func, *args)
:canonical: dss._cffi_api_util.CffiApiUtil.get_int32_array2

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.get_int32_array2
```

````

````{py:method} get_int32_gr_array() -> dss._types.Int32Array
:canonical: dss._cffi_api_util.CffiApiUtil.get_int32_gr_array

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.get_int32_gr_array
```

````

````{py:method} get_int32_gr_array2()
:canonical: dss._cffi_api_util.CffiApiUtil.get_int32_gr_array2

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.get_int32_gr_array2
```

````

````{py:method} get_int8_array(func: typing.Callable, *args: typing.Any) -> dss._types.Int8Array
:canonical: dss._cffi_api_util.CffiApiUtil.get_int8_array

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.get_int8_array
```

````

````{py:method} get_int8_array2(func, *args)
:canonical: dss._cffi_api_util.CffiApiUtil.get_int8_array2

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.get_int8_array2
```

````

````{py:method} get_int8_gr_array() -> dss._types.Int8Array
:canonical: dss._cffi_api_util.CffiApiUtil.get_int8_gr_array

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.get_int8_gr_array
```

````

````{py:method} get_int8_gr_array2()
:canonical: dss._cffi_api_util.CffiApiUtil.get_int8_gr_array2

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.get_int8_gr_array2
```

````

````{py:method} get_ptr_array(func: typing.Callable, *args)
:canonical: dss._cffi_api_util.CffiApiUtil.get_ptr_array

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.get_ptr_array
```

````

````{py:method} get_string(b) -> str
:canonical: dss._cffi_api_util.CffiApiUtil.get_string

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.get_string
```

````

````{py:method} get_string_array(func: typing.Callable, *args: typing.Any) -> typing.List[str]
:canonical: dss._cffi_api_util.CffiApiUtil.get_string_array

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.get_string_array
```

````

````{py:method} get_string_array2(func, *args)
:canonical: dss._cffi_api_util.CffiApiUtil.get_string_array2

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.get_string_array2
```

````

````{py:method} init_buffers()
:canonical: dss._cffi_api_util.CffiApiUtil.init_buffers

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.init_buffers
```

````

````{py:method} prepare_complex128_array(value)
:canonical: dss._cffi_api_util.CffiApiUtil.prepare_complex128_array

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.prepare_complex128_array
```

````

````{py:method} prepare_complex128_simple(value: complex)
:canonical: dss._cffi_api_util.CffiApiUtil.prepare_complex128_simple

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.prepare_complex128_simple
```

````

````{py:method} prepare_float64_array(value)
:canonical: dss._cffi_api_util.CffiApiUtil.prepare_float64_array

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.prepare_float64_array
```

````

````{py:method} prepare_int32_array(value)
:canonical: dss._cffi_api_util.CffiApiUtil.prepare_int32_array

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.prepare_int32_array
```

````

````{py:method} prepare_string_array(value: typing.List[typing.AnyStr])
:canonical: dss._cffi_api_util.CffiApiUtil.prepare_string_array

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.prepare_string_array
```

````

````{py:method} register_callbacks()
:canonical: dss._cffi_api_util.CffiApiUtil.register_callbacks

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.register_callbacks
```

````

````{py:method} reprocess_buses_callback(step: int)
:canonical: dss._cffi_api_util.CffiApiUtil.reprocess_buses_callback

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.reprocess_buses_callback
```

````

````{py:method} set_string_array(func: typing.Callable, value: typing.List[typing.AnyStr], *args)
:canonical: dss._cffi_api_util.CffiApiUtil.set_string_array

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.set_string_array
```

````

````{py:method} track_batch(batch)
:canonical: dss._cffi_api_util.CffiApiUtil.track_batch

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.track_batch
```

````

````{py:method} track_bus(bus)
:canonical: dss._cffi_api_util.CffiApiUtil.track_bus

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.track_bus
```

````

````{py:method} track_obj(obj)
:canonical: dss._cffi_api_util.CffiApiUtil.track_obj

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.track_obj
```

````

````{py:method} unregister_callbacks()
:canonical: dss._cffi_api_util.CffiApiUtil.unregister_callbacks

```{autodoc2-docstring} dss._cffi_api_util.CffiApiUtil.unregister_callbacks
```

````

`````

`````{py:class} CtxLib(ctx, ffi, lib)
:canonical: dss._cffi_api_util.CtxLib

```{autodoc2-docstring} dss._cffi_api_util.CtxLib
```

````{py:method} __init__(ctx, ffi, lib)
:canonical: dss._cffi_api_util.CtxLib.__init__

```{autodoc2-docstring} dss._cffi_api_util.CtxLib.__init__
```

````

`````

`````{py:exception} DSSException()
:canonical: dss._cffi_api_util.DSSException

Bases: {py:obj}`Exception`

```{autodoc2-docstring} dss._cffi_api_util.DSSException
```

````{py:class} __cause__
:canonical: dss._cffi_api_util.DSSException.__cause__

```{autodoc2-docstring} dss._cffi_api_util.DSSException.__cause__
```

````

````{py:class} __context__
:canonical: dss._cffi_api_util.DSSException.__context__

```{autodoc2-docstring} dss._cffi_api_util.DSSException.__context__
```

````

````{py:method} __delattr__()
:canonical: dss._cffi_api_util.DSSException.__delattr__

```{autodoc2-docstring} dss._cffi_api_util.DSSException.__delattr__
```

````

````{py:method} __dir__()
:canonical: dss._cffi_api_util.DSSException.__dir__

```{autodoc2-docstring} dss._cffi_api_util.DSSException.__dir__
```

````

````{py:method} __eq__()
:canonical: dss._cffi_api_util.DSSException.__eq__

```{autodoc2-docstring} dss._cffi_api_util.DSSException.__eq__
```

````

````{py:method} __format__()
:canonical: dss._cffi_api_util.DSSException.__format__

```{autodoc2-docstring} dss._cffi_api_util.DSSException.__format__
```

````

````{py:method} __ge__()
:canonical: dss._cffi_api_util.DSSException.__ge__

```{autodoc2-docstring} dss._cffi_api_util.DSSException.__ge__
```

````

````{py:method} __getattribute__()
:canonical: dss._cffi_api_util.DSSException.__getattribute__

```{autodoc2-docstring} dss._cffi_api_util.DSSException.__getattribute__
```

````

````{py:method} __getstate__()
:canonical: dss._cffi_api_util.DSSException.__getstate__

```{autodoc2-docstring} dss._cffi_api_util.DSSException.__getstate__
```

````

````{py:method} __gt__()
:canonical: dss._cffi_api_util.DSSException.__gt__

```{autodoc2-docstring} dss._cffi_api_util.DSSException.__gt__
```

````

````{py:method} __hash__()
:canonical: dss._cffi_api_util.DSSException.__hash__

```{autodoc2-docstring} dss._cffi_api_util.DSSException.__hash__
```

````

````{py:method} __init__()
:canonical: dss._cffi_api_util.DSSException.__init__

```{autodoc2-docstring} dss._cffi_api_util.DSSException.__init__
```

````

````{py:method} __le__()
:canonical: dss._cffi_api_util.DSSException.__le__

```{autodoc2-docstring} dss._cffi_api_util.DSSException.__le__
```

````

````{py:method} __lt__()
:canonical: dss._cffi_api_util.DSSException.__lt__

```{autodoc2-docstring} dss._cffi_api_util.DSSException.__lt__
```

````

````{py:method} __ne__()
:canonical: dss._cffi_api_util.DSSException.__ne__

```{autodoc2-docstring} dss._cffi_api_util.DSSException.__ne__
```

````

````{py:method} __new__()
:canonical: dss._cffi_api_util.DSSException.__new__

```{autodoc2-docstring} dss._cffi_api_util.DSSException.__new__
```

````

````{py:method} __reduce__()
:canonical: dss._cffi_api_util.DSSException.__reduce__

```{autodoc2-docstring} dss._cffi_api_util.DSSException.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: dss._cffi_api_util.DSSException.__reduce_ex__

```{autodoc2-docstring} dss._cffi_api_util.DSSException.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: dss._cffi_api_util.DSSException.__repr__

```{autodoc2-docstring} dss._cffi_api_util.DSSException.__repr__
```

````

````{py:method} __setstate__()
:canonical: dss._cffi_api_util.DSSException.__setstate__

```{autodoc2-docstring} dss._cffi_api_util.DSSException.__setstate__
```

````

````{py:method} __sizeof__()
:canonical: dss._cffi_api_util.DSSException.__sizeof__

```{autodoc2-docstring} dss._cffi_api_util.DSSException.__sizeof__
```

````

````{py:method} __str__()
:canonical: dss._cffi_api_util.DSSException.__str__

```{autodoc2-docstring} dss._cffi_api_util.DSSException.__str__
```

````

````{py:method} __subclasshook__()
:canonical: dss._cffi_api_util.DSSException.__subclasshook__

```{autodoc2-docstring} dss._cffi_api_util.DSSException.__subclasshook__
```

````

````{py:class} __suppress_context__
:canonical: dss._cffi_api_util.DSSException.__suppress_context__

```{autodoc2-docstring} dss._cffi_api_util.DSSException.__suppress_context__
```

````

````{py:class} __traceback__
:canonical: dss._cffi_api_util.DSSException.__traceback__

```{autodoc2-docstring} dss._cffi_api_util.DSSException.__traceback__
```

````

````{py:method} add_note()
:canonical: dss._cffi_api_util.DSSException.add_note

```{autodoc2-docstring} dss._cffi_api_util.DSSException.add_note
```

````

````{py:class} args
:canonical: dss._cffi_api_util.DSSException.args

```{autodoc2-docstring} dss._cffi_api_util.DSSException.args
```

````

````{py:method} with_traceback()
:canonical: dss._cffi_api_util.DSSException.with_traceback

```{autodoc2-docstring} dss._cffi_api_util.DSSException.with_traceback
```

````

`````

````{py:data} DssException
:canonical: dss._cffi_api_util.DssException
:value: >
   None

```{autodoc2-docstring} dss._cffi_api_util.DssException
```

````

`````{py:class} Iterable(api_util)
:canonical: dss._cffi_api_util.Iterable

Bases: {py:obj}`dss._cffi_api_util.Base`

```{autodoc2-docstring} dss._cffi_api_util.Iterable
```

````{py:property} AllNames
:canonical: dss._cffi_api_util.Iterable.AllNames
:type: typing.List[str]

```{autodoc2-docstring} dss._cffi_api_util.Iterable.AllNames
```

````

````{py:property} Count
:canonical: dss._cffi_api_util.Iterable.Count
:type: int

```{autodoc2-docstring} dss._cffi_api_util.Iterable.Count
```

````

````{py:property} First
:canonical: dss._cffi_api_util.Iterable.First
:type: int

```{autodoc2-docstring} dss._cffi_api_util.Iterable.First
```

````

````{py:property} Name
:canonical: dss._cffi_api_util.Iterable.Name
:type: str

```{autodoc2-docstring} dss._cffi_api_util.Iterable.Name
```

````

````{py:property} Next
:canonical: dss._cffi_api_util.Iterable.Next
:type: int

```{autodoc2-docstring} dss._cffi_api_util.Iterable.Next
```

````

````{py:method} __init__(api_util)
:canonical: dss._cffi_api_util.Iterable.__init__

```{autodoc2-docstring} dss._cffi_api_util.Iterable.__init__
```

````

````{py:method} __iter__() -> typing.Iterator[dss._cffi_api_util.Iterable]
:canonical: dss._cffi_api_util.Iterable.__iter__

```{autodoc2-docstring} dss._cffi_api_util.Iterable.__iter__
```

````

````{py:method} __len__() -> int
:canonical: dss._cffi_api_util.Iterable.__len__

```{autodoc2-docstring} dss._cffi_api_util.Iterable.__len__
```

````

````{py:property} idx
:canonical: dss._cffi_api_util.Iterable.idx
:type: int

```{autodoc2-docstring} dss._cffi_api_util.Iterable.idx
```

````

`````

````{py:function} altdss_python_util_callback(ctx, event_code, step, ptr)
:canonical: dss._cffi_api_util.altdss_python_util_callback

```{autodoc2-docstring} dss._cffi_api_util.altdss_python_util_callback
```
````

````{py:data} codec
:canonical: dss._cffi_api_util.codec
:value: >
   'UTF8'

```{autodoc2-docstring} dss._cffi_api_util.codec
```

````

````{py:data} interface_classes
:canonical: dss._cffi_api_util.interface_classes
:value: >
   'set(...)'

```{autodoc2-docstring} dss._cffi_api_util.interface_classes
```

````

````{py:function} set_case_insensitive_attributes(use: bool = True, warn: bool = False)
:canonical: dss._cffi_api_util.set_case_insensitive_attributes

```{autodoc2-docstring} dss._cffi_api_util.set_case_insensitive_attributes
```
````

````{py:data} use_com_compat
:canonical: dss._cffi_api_util.use_com_compat
:value: >
   None

```{autodoc2-docstring} dss._cffi_api_util.use_com_compat
```

````

````{py:data} warn_wrong_case
:canonical: dss._cffi_api_util.warn_wrong_case
:value: >
   False

```{autodoc2-docstring} dss._cffi_api_util.warn_wrong_case
```

````
