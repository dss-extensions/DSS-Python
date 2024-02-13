# {py:mod}`dss.UserModels.wrappers`

```{py:module} dss.UserModels.wrappers
```

```{autodoc2-docstring} dss.UserModels.wrappers
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CommonWrapper <dss.UserModels.wrappers.CommonWrapper>`
  - ```{autodoc2-docstring} dss.UserModels.wrappers.CommonWrapper
    :summary:
    ```
* - {py:obj}`DynamicsWrapper <dss.UserModels.wrappers.DynamicsWrapper>`
  - ```{autodoc2-docstring} dss.UserModels.wrappers.DynamicsWrapper
    :summary:
    ```
* - {py:obj}`GenUserModelWrapper <dss.UserModels.wrappers.GenUserModelWrapper>`
  - ```{autodoc2-docstring} dss.UserModels.wrappers.GenUserModelWrapper
    :summary:
    ```
* - {py:obj}`SaveRestoreMixin <dss.UserModels.wrappers.SaveRestoreMixin>`
  - ```{autodoc2-docstring} dss.UserModels.wrappers.SaveRestoreMixin
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`GenUserModel <dss.UserModels.wrappers.GenUserModel>`
  - ```{autodoc2-docstring} dss.UserModels.wrappers.GenUserModel
    :summary:
    ```
````

### API

`````{py:class} CommonWrapper()
:canonical: dss.UserModels.wrappers.CommonWrapper

Bases: {py:obj}`object`

```{autodoc2-docstring} dss.UserModels.wrappers.CommonWrapper
```

````{py:attribute} Base
:canonical: dss.UserModels.wrappers.CommonWrapper.Base
:value: >
   None

```{autodoc2-docstring} dss.UserModels.wrappers.CommonWrapper.Base
```

````

````{py:method} Delete(ID)
:canonical: dss.UserModels.wrappers.CommonWrapper.Delete

```{autodoc2-docstring} dss.UserModels.wrappers.CommonWrapper.Delete
```

````

````{py:method} Edit(edit_str, max_len)
:canonical: dss.UserModels.wrappers.CommonWrapper.Edit

```{autodoc2-docstring} dss.UserModels.wrappers.CommonWrapper.Edit
```

````

````{py:method} Select(ID)
:canonical: dss.UserModels.wrappers.CommonWrapper.Select

```{autodoc2-docstring} dss.UserModels.wrappers.CommonWrapper.Select
```

````

````{py:method} UpdateModel()
:canonical: dss.UserModels.wrappers.CommonWrapper.UpdateModel

```{autodoc2-docstring} dss.UserModels.wrappers.CommonWrapper.UpdateModel
```

````

````{py:method} __init__()
:canonical: dss.UserModels.wrappers.CommonWrapper.__init__

```{autodoc2-docstring} dss.UserModels.wrappers.CommonWrapper.__init__
```

````

````{py:method} register(cls)
:canonical: dss.UserModels.wrappers.CommonWrapper.register

```{autodoc2-docstring} dss.UserModels.wrappers.CommonWrapper.register
```

````

`````

`````{py:class} DynamicsWrapper()
:canonical: dss.UserModels.wrappers.DynamicsWrapper

Bases: {py:obj}`dss.UserModels.wrappers.CommonWrapper`

```{autodoc2-docstring} dss.UserModels.wrappers.DynamicsWrapper
```

````{py:attribute} Base
:canonical: dss.UserModels.wrappers.DynamicsWrapper.Base
:value: >
   None

```{autodoc2-docstring} dss.UserModels.wrappers.DynamicsWrapper.Base
```

````

````{py:method} Calc(V, I)
:canonical: dss.UserModels.wrappers.DynamicsWrapper.Calc

```{autodoc2-docstring} dss.UserModels.wrappers.DynamicsWrapper.Calc
```

````

````{py:method} Delete(ID)
:canonical: dss.UserModels.wrappers.DynamicsWrapper.Delete

```{autodoc2-docstring} dss.UserModels.wrappers.DynamicsWrapper.Delete
```

````

````{py:method} Edit(edit_str, max_len)
:canonical: dss.UserModels.wrappers.DynamicsWrapper.Edit

```{autodoc2-docstring} dss.UserModels.wrappers.DynamicsWrapper.Edit
```

````

````{py:method} GetAllVars(vars)
:canonical: dss.UserModels.wrappers.DynamicsWrapper.GetAllVars

```{autodoc2-docstring} dss.UserModels.wrappers.DynamicsWrapper.GetAllVars
```

````

````{py:method} GetVarName(i, var_name, max_len)
:canonical: dss.UserModels.wrappers.DynamicsWrapper.GetVarName

```{autodoc2-docstring} dss.UserModels.wrappers.DynamicsWrapper.GetVarName
```

````

````{py:method} GetVariable(i)
:canonical: dss.UserModels.wrappers.DynamicsWrapper.GetVariable

```{autodoc2-docstring} dss.UserModels.wrappers.DynamicsWrapper.GetVariable
```

````

````{py:method} Init(V, I)
:canonical: dss.UserModels.wrappers.DynamicsWrapper.Init

```{autodoc2-docstring} dss.UserModels.wrappers.DynamicsWrapper.Init
```

````

````{py:method} Integrate()
:canonical: dss.UserModels.wrappers.DynamicsWrapper.Integrate

```{autodoc2-docstring} dss.UserModels.wrappers.DynamicsWrapper.Integrate
```

````

````{py:method} NumVars()
:canonical: dss.UserModels.wrappers.DynamicsWrapper.NumVars

```{autodoc2-docstring} dss.UserModels.wrappers.DynamicsWrapper.NumVars
```

````

````{py:method} Select(ID)
:canonical: dss.UserModels.wrappers.DynamicsWrapper.Select

```{autodoc2-docstring} dss.UserModels.wrappers.DynamicsWrapper.Select
```

````

````{py:method} SetVariable(i, value)
:canonical: dss.UserModels.wrappers.DynamicsWrapper.SetVariable

```{autodoc2-docstring} dss.UserModels.wrappers.DynamicsWrapper.SetVariable
```

````

````{py:method} UpdateModel()
:canonical: dss.UserModels.wrappers.DynamicsWrapper.UpdateModel

```{autodoc2-docstring} dss.UserModels.wrappers.DynamicsWrapper.UpdateModel
```

````

````{py:method} __init__()
:canonical: dss.UserModels.wrappers.DynamicsWrapper.__init__

```{autodoc2-docstring} dss.UserModels.wrappers.DynamicsWrapper.__init__
```

````

````{py:method} register(cls)
:canonical: dss.UserModels.wrappers.DynamicsWrapper.register

```{autodoc2-docstring} dss.UserModels.wrappers.DynamicsWrapper.register
```

````

`````

````{py:data} GenUserModel
:canonical: dss.UserModels.wrappers.GenUserModel
:value: >
   None

```{autodoc2-docstring} dss.UserModels.wrappers.GenUserModel
```

````

`````{py:class} GenUserModelWrapper()
:canonical: dss.UserModels.wrappers.GenUserModelWrapper

Bases: {py:obj}`dss.UserModels.wrappers.DynamicsWrapper`, {py:obj}`dss.UserModels.wrappers.SaveRestoreMixin`

```{autodoc2-docstring} dss.UserModels.wrappers.GenUserModelWrapper
```

````{py:attribute} Base
:canonical: dss.UserModels.wrappers.GenUserModelWrapper.Base
:value: >
   None

```{autodoc2-docstring} dss.UserModels.wrappers.GenUserModelWrapper.Base
```

````

````{py:method} Calc(V, I)
:canonical: dss.UserModels.wrappers.GenUserModelWrapper.Calc

```{autodoc2-docstring} dss.UserModels.wrappers.GenUserModelWrapper.Calc
```

````

````{py:method} Delete(ID)
:canonical: dss.UserModels.wrappers.GenUserModelWrapper.Delete

```{autodoc2-docstring} dss.UserModels.wrappers.GenUserModelWrapper.Delete
```

````

````{py:method} Edit(edit_str, max_len)
:canonical: dss.UserModels.wrappers.GenUserModelWrapper.Edit

```{autodoc2-docstring} dss.UserModels.wrappers.GenUserModelWrapper.Edit
```

````

````{py:method} GetAllVars(vars)
:canonical: dss.UserModels.wrappers.GenUserModelWrapper.GetAllVars

```{autodoc2-docstring} dss.UserModels.wrappers.GenUserModelWrapper.GetAllVars
```

````

````{py:method} GetVarName(i, var_name, max_len)
:canonical: dss.UserModels.wrappers.GenUserModelWrapper.GetVarName

```{autodoc2-docstring} dss.UserModels.wrappers.GenUserModelWrapper.GetVarName
```

````

````{py:method} GetVariable(i)
:canonical: dss.UserModels.wrappers.GenUserModelWrapper.GetVariable

```{autodoc2-docstring} dss.UserModels.wrappers.GenUserModelWrapper.GetVariable
```

````

````{py:method} Init(V, I)
:canonical: dss.UserModels.wrappers.GenUserModelWrapper.Init

```{autodoc2-docstring} dss.UserModels.wrappers.GenUserModelWrapper.Init
```

````

````{py:method} Integrate()
:canonical: dss.UserModels.wrappers.GenUserModelWrapper.Integrate

```{autodoc2-docstring} dss.UserModels.wrappers.GenUserModelWrapper.Integrate
```

````

````{py:method} New(GenData, DynaData, CallBacks)
:canonical: dss.UserModels.wrappers.GenUserModelWrapper.New

```{autodoc2-docstring} dss.UserModels.wrappers.GenUserModelWrapper.New
```

````

````{py:method} NumVars()
:canonical: dss.UserModels.wrappers.GenUserModelWrapper.NumVars

```{autodoc2-docstring} dss.UserModels.wrappers.GenUserModelWrapper.NumVars
```

````

````{py:method} Restore()
:canonical: dss.UserModels.wrappers.GenUserModelWrapper.Restore

```{autodoc2-docstring} dss.UserModels.wrappers.GenUserModelWrapper.Restore
```

````

````{py:method} Save()
:canonical: dss.UserModels.wrappers.GenUserModelWrapper.Save

```{autodoc2-docstring} dss.UserModels.wrappers.GenUserModelWrapper.Save
```

````

````{py:method} Select(ID)
:canonical: dss.UserModels.wrappers.GenUserModelWrapper.Select

```{autodoc2-docstring} dss.UserModels.wrappers.GenUserModelWrapper.Select
```

````

````{py:method} SetVariable(i, value)
:canonical: dss.UserModels.wrappers.GenUserModelWrapper.SetVariable

```{autodoc2-docstring} dss.UserModels.wrappers.GenUserModelWrapper.SetVariable
```

````

````{py:method} UpdateModel()
:canonical: dss.UserModels.wrappers.GenUserModelWrapper.UpdateModel

```{autodoc2-docstring} dss.UserModels.wrappers.GenUserModelWrapper.UpdateModel
```

````

````{py:method} __init__()
:canonical: dss.UserModels.wrappers.GenUserModelWrapper.__init__

```{autodoc2-docstring} dss.UserModels.wrappers.GenUserModelWrapper.__init__
```

````

````{py:attribute} cffi_module
:canonical: dss.UserModels.wrappers.GenUserModelWrapper.cffi_module
:value: >
   None

```{autodoc2-docstring} dss.UserModels.wrappers.GenUserModelWrapper.cffi_module
```

````

````{py:attribute} function_names
:canonical: dss.UserModels.wrappers.GenUserModelWrapper.function_names
:value: >
   ('New', 'Delete', 'Select', 'Init', 'Calc', 'Integrate', 'Edit', 'UpdateModel', 'NumVars', 'GetAllVa...

```{autodoc2-docstring} dss.UserModels.wrappers.GenUserModelWrapper.function_names
```

````

````{py:attribute} function_prefix
:canonical: dss.UserModels.wrappers.GenUserModelWrapper.function_prefix
:value: >
   'pyGenUserModel'

```{autodoc2-docstring} dss.UserModels.wrappers.GenUserModelWrapper.function_prefix
```

````

````{py:method} register(cls)
:canonical: dss.UserModels.wrappers.GenUserModelWrapper.register

```{autodoc2-docstring} dss.UserModels.wrappers.GenUserModelWrapper.register
```

````

`````

`````{py:class} SaveRestoreMixin
:canonical: dss.UserModels.wrappers.SaveRestoreMixin

Bases: {py:obj}`object`

```{autodoc2-docstring} dss.UserModels.wrappers.SaveRestoreMixin
```

````{py:method} Restore()
:canonical: dss.UserModels.wrappers.SaveRestoreMixin.Restore

```{autodoc2-docstring} dss.UserModels.wrappers.SaveRestoreMixin.Restore
```

````

````{py:method} Save()
:canonical: dss.UserModels.wrappers.SaveRestoreMixin.Save

```{autodoc2-docstring} dss.UserModels.wrappers.SaveRestoreMixin.Save
```

````

`````
