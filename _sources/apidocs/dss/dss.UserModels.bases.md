# {py:mod}`dss.UserModels.bases`

```{py:module} dss.UserModels.bases
```

```{autodoc2-docstring} dss.UserModels.bases
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CommonBase <dss.UserModels.bases.CommonBase>`
  - ```{autodoc2-docstring} dss.UserModels.bases.CommonBase
    :summary:
    ```
* - {py:obj}`DynamicsBase <dss.UserModels.bases.DynamicsBase>`
  - ```{autodoc2-docstring} dss.UserModels.bases.DynamicsBase
    :summary:
    ```
* - {py:obj}`GenUserModelBase <dss.UserModels.bases.GenUserModelBase>`
  - ```{autodoc2-docstring} dss.UserModels.bases.GenUserModelBase
    :summary:
    ```
* - {py:obj}`SaveRestoreMixin <dss.UserModels.bases.SaveRestoreMixin>`
  - ```{autodoc2-docstring} dss.UserModels.bases.SaveRestoreMixin
    :summary:
    ```
````

### API

`````{py:class} CommonBase(callbacks, populate=None)
:canonical: dss.UserModels.bases.CommonBase

Bases: {py:obj}`object`

```{autodoc2-docstring} dss.UserModels.bases.CommonBase
```

````{py:method} __init__(callbacks, populate=None)
:canonical: dss.UserModels.bases.CommonBase.__init__

```{autodoc2-docstring} dss.UserModels.bases.CommonBase.__init__
```

````

````{py:method} add_input(name, value=0.0)
:canonical: dss.UserModels.bases.CommonBase.add_input

```{autodoc2-docstring} dss.UserModels.bases.CommonBase.add_input
```

````

````{py:method} add_inputs(*args)
:canonical: dss.UserModels.bases.CommonBase.add_inputs

```{autodoc2-docstring} dss.UserModels.bases.CommonBase.add_inputs
```

````

````{py:method} edit(edit_str, max_len)
:canonical: dss.UserModels.bases.CommonBase.edit

```{autodoc2-docstring} dss.UserModels.bases.CommonBase.edit
```

````

````{py:method} extract_names()
:canonical: dss.UserModels.bases.CommonBase.extract_names
:classmethod:

```{autodoc2-docstring} dss.UserModels.bases.CommonBase.extract_names
```

````

````{py:method} set_input_param(i, value)
:canonical: dss.UserModels.bases.CommonBase.set_input_param

```{autodoc2-docstring} dss.UserModels.bases.CommonBase.set_input_param
```

````

````{py:method} update()
:canonical: dss.UserModels.bases.CommonBase.update

```{autodoc2-docstring} dss.UserModels.bases.CommonBase.update
```

````

`````

`````{py:class} DynamicsBase(dyn, callbacks, populate=None)
:canonical: dss.UserModels.bases.DynamicsBase

Bases: {py:obj}`dss.UserModels.bases.CommonBase`

```{autodoc2-docstring} dss.UserModels.bases.DynamicsBase
```

````{py:method} __init__(dyn, callbacks, populate=None)
:canonical: dss.UserModels.bases.DynamicsBase.__init__

```{autodoc2-docstring} dss.UserModels.bases.DynamicsBase.__init__
```

````

````{py:method} add_input(name, value=0.0)
:canonical: dss.UserModels.bases.DynamicsBase.add_input

```{autodoc2-docstring} dss.UserModels.bases.DynamicsBase.add_input
```

````

````{py:method} add_inputs(*args)
:canonical: dss.UserModels.bases.DynamicsBase.add_inputs

```{autodoc2-docstring} dss.UserModels.bases.DynamicsBase.add_inputs
```

````

````{py:method} add_output(name, init_value=0.0)
:canonical: dss.UserModels.bases.DynamicsBase.add_output

```{autodoc2-docstring} dss.UserModels.bases.DynamicsBase.add_output
```

````

````{py:method} add_outputs(*args)
:canonical: dss.UserModels.bases.DynamicsBase.add_outputs

```{autodoc2-docstring} dss.UserModels.bases.DynamicsBase.add_outputs
```

````

````{py:method} add_state_var(name, init_value=0.0)
:canonical: dss.UserModels.bases.DynamicsBase.add_state_var

```{autodoc2-docstring} dss.UserModels.bases.DynamicsBase.add_state_var
```

````

````{py:method} add_state_vars(*args)
:canonical: dss.UserModels.bases.DynamicsBase.add_state_vars

```{autodoc2-docstring} dss.UserModels.bases.DynamicsBase.add_state_vars
```

````

````{py:method} calc(V, I)
:canonical: dss.UserModels.bases.DynamicsBase.calc
:abstractmethod:

```{autodoc2-docstring} dss.UserModels.bases.DynamicsBase.calc
```

````

````{py:method} copy_state()
:canonical: dss.UserModels.bases.DynamicsBase.copy_state

```{autodoc2-docstring} dss.UserModels.bases.DynamicsBase.copy_state
```

````

````{py:method} edit(edit_str, max_len)
:canonical: dss.UserModels.bases.DynamicsBase.edit

```{autodoc2-docstring} dss.UserModels.bases.DynamicsBase.edit
```

````

````{py:method} extract_names()
:canonical: dss.UserModels.bases.DynamicsBase.extract_names
:classmethod:

```{autodoc2-docstring} dss.UserModels.bases.DynamicsBase.extract_names
```

````

````{py:method} get_all_outputs(var_vector)
:canonical: dss.UserModels.bases.DynamicsBase.get_all_outputs

```{autodoc2-docstring} dss.UserModels.bases.DynamicsBase.get_all_outputs
```

````

````{py:method} get_num_outputs()
:canonical: dss.UserModels.bases.DynamicsBase.get_num_outputs

```{autodoc2-docstring} dss.UserModels.bases.DynamicsBase.get_num_outputs
```

````

````{py:method} get_output(i)
:canonical: dss.UserModels.bases.DynamicsBase.get_output

```{autodoc2-docstring} dss.UserModels.bases.DynamicsBase.get_output
```

````

````{py:method} get_output_name(i)
:canonical: dss.UserModels.bases.DynamicsBase.get_output_name

```{autodoc2-docstring} dss.UserModels.bases.DynamicsBase.get_output_name
```

````

````{py:method} init_dstate()
:canonical: dss.UserModels.bases.DynamicsBase.init_dstate

```{autodoc2-docstring} dss.UserModels.bases.DynamicsBase.init_dstate
```

````

````{py:method} init_state_vars(V, I)
:canonical: dss.UserModels.bases.DynamicsBase.init_state_vars
:abstractmethod:

```{autodoc2-docstring} dss.UserModels.bases.DynamicsBase.init_state_vars
```

````

````{py:method} integrate()
:canonical: dss.UserModels.bases.DynamicsBase.integrate

```{autodoc2-docstring} dss.UserModels.bases.DynamicsBase.integrate
```

````

````{py:method} saturate()
:canonical: dss.UserModels.bases.DynamicsBase.saturate

```{autodoc2-docstring} dss.UserModels.bases.DynamicsBase.saturate
```

````

````{py:method} set_input_param(i, value)
:canonical: dss.UserModels.bases.DynamicsBase.set_input_param

```{autodoc2-docstring} dss.UserModels.bases.DynamicsBase.set_input_param
```

````

````{py:method} set_var_limits(name, min=None, max=None)
:canonical: dss.UserModels.bases.DynamicsBase.set_var_limits

```{autodoc2-docstring} dss.UserModels.bases.DynamicsBase.set_var_limits
```

````

````{py:method} update()
:canonical: dss.UserModels.bases.DynamicsBase.update

```{autodoc2-docstring} dss.UserModels.bases.DynamicsBase.update
```

````

`````

`````{py:class} GenUserModelBase(gen, dyn, callbacks, populate=None)
:canonical: dss.UserModels.bases.GenUserModelBase

Bases: {py:obj}`dss.UserModels.bases.DynamicsBase`, {py:obj}`dss.UserModels.bases.SaveRestoreMixin`

```{autodoc2-docstring} dss.UserModels.bases.GenUserModelBase
```

````{py:method} __init__(gen, dyn, callbacks, populate=None)
:canonical: dss.UserModels.bases.GenUserModelBase.__init__

```{autodoc2-docstring} dss.UserModels.bases.GenUserModelBase.__init__
```

````

````{py:method} add_input(name, value=0.0)
:canonical: dss.UserModels.bases.GenUserModelBase.add_input

```{autodoc2-docstring} dss.UserModels.bases.GenUserModelBase.add_input
```

````

````{py:method} add_inputs(*args)
:canonical: dss.UserModels.bases.GenUserModelBase.add_inputs

```{autodoc2-docstring} dss.UserModels.bases.GenUserModelBase.add_inputs
```

````

````{py:method} add_output(name, init_value=0.0)
:canonical: dss.UserModels.bases.GenUserModelBase.add_output

```{autodoc2-docstring} dss.UserModels.bases.GenUserModelBase.add_output
```

````

````{py:method} add_outputs(*args)
:canonical: dss.UserModels.bases.GenUserModelBase.add_outputs

```{autodoc2-docstring} dss.UserModels.bases.GenUserModelBase.add_outputs
```

````

````{py:method} add_state_var(name, init_value=0.0)
:canonical: dss.UserModels.bases.GenUserModelBase.add_state_var

```{autodoc2-docstring} dss.UserModels.bases.GenUserModelBase.add_state_var
```

````

````{py:method} add_state_vars(*args)
:canonical: dss.UserModels.bases.GenUserModelBase.add_state_vars

```{autodoc2-docstring} dss.UserModels.bases.GenUserModelBase.add_state_vars
```

````

````{py:method} calc(V, I)
:canonical: dss.UserModels.bases.GenUserModelBase.calc
:abstractmethod:

```{autodoc2-docstring} dss.UserModels.bases.GenUserModelBase.calc
```

````

````{py:method} copy_state()
:canonical: dss.UserModels.bases.GenUserModelBase.copy_state

```{autodoc2-docstring} dss.UserModels.bases.GenUserModelBase.copy_state
```

````

````{py:method} edit(edit_str, max_len)
:canonical: dss.UserModels.bases.GenUserModelBase.edit

```{autodoc2-docstring} dss.UserModels.bases.GenUserModelBase.edit
```

````

````{py:method} extract_names()
:canonical: dss.UserModels.bases.GenUserModelBase.extract_names
:classmethod:

```{autodoc2-docstring} dss.UserModels.bases.GenUserModelBase.extract_names
```

````

````{py:method} get_all_outputs(var_vector)
:canonical: dss.UserModels.bases.GenUserModelBase.get_all_outputs

```{autodoc2-docstring} dss.UserModels.bases.GenUserModelBase.get_all_outputs
```

````

````{py:method} get_num_outputs()
:canonical: dss.UserModels.bases.GenUserModelBase.get_num_outputs

```{autodoc2-docstring} dss.UserModels.bases.GenUserModelBase.get_num_outputs
```

````

````{py:method} get_output(i)
:canonical: dss.UserModels.bases.GenUserModelBase.get_output

```{autodoc2-docstring} dss.UserModels.bases.GenUserModelBase.get_output
```

````

````{py:method} get_output_name(i)
:canonical: dss.UserModels.bases.GenUserModelBase.get_output_name

```{autodoc2-docstring} dss.UserModels.bases.GenUserModelBase.get_output_name
```

````

````{py:method} init_dstate()
:canonical: dss.UserModels.bases.GenUserModelBase.init_dstate

```{autodoc2-docstring} dss.UserModels.bases.GenUserModelBase.init_dstate
```

````

````{py:method} init_state_vars(V, I)
:canonical: dss.UserModels.bases.GenUserModelBase.init_state_vars
:abstractmethod:

```{autodoc2-docstring} dss.UserModels.bases.GenUserModelBase.init_state_vars
```

````

````{py:method} integrate()
:canonical: dss.UserModels.bases.GenUserModelBase.integrate

```{autodoc2-docstring} dss.UserModels.bases.GenUserModelBase.integrate
```

````

````{py:method} restore()
:canonical: dss.UserModels.bases.GenUserModelBase.restore

```{autodoc2-docstring} dss.UserModels.bases.GenUserModelBase.restore
```

````

````{py:method} saturate()
:canonical: dss.UserModels.bases.GenUserModelBase.saturate

```{autodoc2-docstring} dss.UserModels.bases.GenUserModelBase.saturate
```

````

````{py:method} save()
:canonical: dss.UserModels.bases.GenUserModelBase.save

```{autodoc2-docstring} dss.UserModels.bases.GenUserModelBase.save
```

````

````{py:method} set_input_param(i, value)
:canonical: dss.UserModels.bases.GenUserModelBase.set_input_param

```{autodoc2-docstring} dss.UserModels.bases.GenUserModelBase.set_input_param
```

````

````{py:method} set_var_limits(name, min=None, max=None)
:canonical: dss.UserModels.bases.GenUserModelBase.set_var_limits

```{autodoc2-docstring} dss.UserModels.bases.GenUserModelBase.set_var_limits
```

````

````{py:method} update()
:canonical: dss.UserModels.bases.GenUserModelBase.update

```{autodoc2-docstring} dss.UserModels.bases.GenUserModelBase.update
```

````

`````

`````{py:class} SaveRestoreMixin
:canonical: dss.UserModels.bases.SaveRestoreMixin

Bases: {py:obj}`object`

```{autodoc2-docstring} dss.UserModels.bases.SaveRestoreMixin
```

````{py:method} restore()
:canonical: dss.UserModels.bases.SaveRestoreMixin.restore

```{autodoc2-docstring} dss.UserModels.bases.SaveRestoreMixin.restore
```

````

````{py:method} save()
:canonical: dss.UserModels.bases.SaveRestoreMixin.save

```{autodoc2-docstring} dss.UserModels.bases.SaveRestoreMixin.save
```

````

`````
