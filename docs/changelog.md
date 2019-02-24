# 0.10.2

(not released)

- `CtrlQueue`: Add the missing function `Push`.


# 0.10.1

Released on 2019-02-17.

This is a minor DSS Python release that contains lots of changes from DSS C-API. See also the [changes from DSS C-API](https://github.com/dss-extensions/dss_capi/blob/ed2a6b322a5e102ba61c6565e5e0eb23247b9221/docs/changelog.md#version-0101) for details, including changes from the official OpenDSS code since 0.10.0.

DSS Python has recently moved from https://github.com/PMeira/dss_python/ to the new https://dss-extensions.org/ and https://github.com/dss-extensions/dss_python/

## Major changes:

- More and faster error-checking! Python exception will be raised for more errors and with a lower overhead.
- Fix for `YMatrix.getI` and `YMatrix.getV` (ported from OpenDSSDirect.py)
- Fix for `ActiveCircuit.ActiveCktElement.Variable` and `ActiveCircuit.ActiveCktElement.Variablei`: now returns a tuple of `(value, errorcode)`, compatible with COM.
- New `DSS.Error.EarlyAbort`: controls whether all errors halts the DSS script processing (Compile/Redirect), defaults to True.

# 0.10.0

Released on 2018-11-17.

## Major changes:
- The creation of the binary modules has been automated using Travis-CI and AppVeyor. We expect that this will allow us to release more often, bringing new features sooner.
- Integrates many fixes from the upstream OpenDSS and changes specific to DSS C-API.
- Reorganizes and reuses the code across DSS versions (v7 and v8) 
- Uses `__slots__` to simplify attribute handling.
- Exposes both the our classic API (e.g. `dss.v7.DSS_IR` for the immediate/direct results) and global result API (e.g. `dss.v7.DSS_GR` for the global result interface). See [DSS C-API's docs](https://github.com/dss-extensions/dss_capi/blob/master/docs/usage.md) for a detailed explanation. We default to the GR interface since it will generally be faster at the cost of a small memory overhead.
- Although still experimental, the v8/PM module is more stable. If you try it, please give feedback.
- Error checking is now done for most API writes. That is, if a an OpenDSS error occurs, it should cause a Python exception soon after. Previously, you need to call `CheckForError()` manually to trigger this. This change was introduced after user reports indicated that manually checking for errors is a common behavior.
- Exposes API extensions for the classes `LineGeometry`, `WireData`, `LineSpacing`, `CNData`, `TSData`, `Reactor`.
- Makes most DSS classes iterable (including buses), e.g. you can now use:
```python
for l in DSS.ActiveCircuit.Loads:
    print(l.Name)
```
- Adds a COM patching function (`dss.patch_dss_com`) -- that is, extend the COM instance with iterators like above and some other few functions to make it easier to exchange between COM and DSS Python:
```python

import win32com.client, dss
com = dss.patch_dss_com(win32com.client.gencache.EnsureDispatch("OpenDSSEngine.DSS"))

# ...compile a circuit, etc.

for l in com.ActiveCircuit.Loads:
    print(l.Name, l.kva)

for b in com.ActiveCircuit.ActiveBus:
    print(b.Name, b.x, b.y)
```

## Performance
On microbenchmarks, the GR interface can reduce the running time up to 50% (typically 25%) on properties that return arrays. If you find issues using the default GR interface, you can always use the classic interface from 0.9.8 by importing the appropriate module: `from dss import DSS_IR as DSS`. Currently, the GR changes do not affect writing data (setting properties), only reading them.

## Mixed-cased handling
If you were using `use_com_compat` to allow mixed-cased attributes, it should work better than before. You may now use `use_com_compat(warn=True)` to warn when you use an attribute that wouldn't exist without calling `use_com_compat`. The intention is that the user should run their code to get a list of warnings, fix it, and then remove `use_com_compat` since it does have a small performance impact.

