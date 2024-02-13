# DSS-Python changelog

Remember that changes in our alternative OpenDSS engine, currently known as DSS C-API, are always
relevant. See [DSS C-API's repository](https://github.com/dss-extensions/dss_capi/) for more information.

## 0.15.x

### 0.15.0

Released on 2024-02-09.

- Upgrade the backend to [**DSS C-API 0.14.0**](https://github.com/dss-extensions/dss_capi/releases/tag/0.14.0). **A lot** of changes there, please check the changelog. Includes many small bugfixes, improvements, and ports of a few changes from the official OpenDSS codebase, matching OpenDSS v9.8.0.1.

- Enums:
    - Move to DSS-Python-Backend to allow easier sharing among all Python packages from DSS-Extensions.
    - Convert enum comments to docstrings for better user experience.
    - New `DSSCompatFlags.ActiveLine`.
    - New `DSSJSONFlags.SkipTimestamp`, `DSSJSONFlags.SkipBuses`, `DSSJSONFlags.IncludeDefaultObjs`.
    - New `DSSSaveFlags` (used in the new function `Circuit.Save`)
    - New `EnergyMeterRegisters` and `GeneratorRegisters` to simplify handling register indexes from EnergyMeters (`EnergyMeterRegisters`), Generators, PVSystems, and Storage objects (these last three use `GeneratorRegisters`).
    - Use enums in a few more methods.

- Packaging: Migrate build system to `pyproject.toml` and Hatch.
- Implement the DSSEvents interface. Note that this is not a popular interface and we haven't seen it used in Python with COM yet. OpenDSS comes with a couple of examples using VBA in Excel though.
- Drop `CheckForError()`; use `_check_for_error()` instead (same function, but the latter doesn't pollute the public scope).
- Expose `Circuit.Save()` function
- Expose `Circuit.FromJSON()` function
- Move `DSS.Obj` to the new [AltDSS-Python package](https://github.com/dss-extensions/AltDSS-Python) (`pip install altdss`, `from altdss import altdss`).
    - **Breaking change**: the main object classes previously used indices starting at 1, but it seemed unnatural in Python and when used with the rest of the API, so they now behave as normal batches and start at 0. Affects both the `find()` method and the brackets (e.g. `altdss.Load[0]`) syntax.
    - **Lots** of new features.
- Use weakrefs to avoid accidentally extending the lifetime of DSSContexts.
- Update documentation framework (Sphinx) to use Markdown, based on MyST and autodoc2.

## 0.14.x

### 0.14.4

Released on 2023-06-27.

- Upgrade the backend to [**DSS C-API 0.13.4**](https://github.com/dss-extensions/dss_capi/releases/tag/0.13.4). Includes a bugfix to CapControl, some more error handling, DSSEvents backend functions. This matches the changes in OpenDSS v9.6.1.3, plus our custom changes as usual.
- Use better DSSContext pointer to IDSS mapping.
- Plotting: handle empty monitors better, ignore invalid channels.
- Documentation updated.


### 0.14.3

Released on 2023-06-12.

- Upgrade the backend to [**DSS C-API 0.13.3**](https://github.com/dss-extensions/dss_capi/releases/tag/0.13.3). Includes important fixes to some OpenDSS components affected by bugs for several years. This matches the changes in OpenDSS v9.6.1.2, plus our custom changes as usual.
- Add `DSS.Error.UseExceptions` to allow disabling the automatic mapping of error numbers to Python exceptions. When disabling, users take full responsibility to actually check for errors through the `DSS.Error` interface.
- Add `DSSCompatFlags.SaveCalcVoltageBases`.
- Transformers: add a warning in the docstrings of `WdgCurrents`, `WdgVoltages` (these don't work well when the transformer has open terminals).
- Plotting: handle GICLines in circuit plots.

### 0.14.2

Released on 2023-05-25.

- Append DSS-Python's version in `DSS.Version`.
- Complement and fix most plot types, leaving only a couple of plots without implementation. An example notebook will be added later.
- Upgrade the backend to DSS C-API v0.13.2.
- Fix some batch property setters, namely when the values are lists of lists, lists of arrays, or 2-d arrays.
- Update Obj and Batch to include newer DSS properties.
- Add JSON option `SkipDSSClass`.
- Coupled with the backend changes, the JSON output should be more well-behaved for Transformer and Line variations.

### 0.14.1

Released on 2023-04-13.

- Fix issue with newer NumPy versions with YMatrix (`GetCompressedYMatrix`), after the removal of `numpy.complex`.
- Use some mode enums.

### 0.14.0

Released on 2023-04-03.

Same as version 0.13.1, except that the organization of the module has changed to facilitate fast iteration of the Python side of the code.

We introduced the new package `dss_python_backend` that will contain all native libs and CFFI bindings from this point on. This leaves DSS-Python itself as a pure Python package, which is much easier to package and distribute.

## 0.13.x

### 0.13.1

Released on 2023-04-02.

- Engine updated to [**DSS C-API 0.13.1**](https://github.com/dss-extensions/dss_capi/releases/tag/0.13.1). Contains tiny changes to address potential issues with a few PVSystem properties (which passed undetected by our tests).
- `DSS.AdvancedTypes`: fix `Lines.Yprim` and `PDElements.AllCurrentsMagAng` when `AdvancedTypes` is enabled.

### 0.13.0

Released on 2023-03-28.

- Engine updated to [**DSS C-API 0.13.0**](https://github.com/dss-extensions/dss_capi/releases/tag/0.13.0), which is very compatible with OpenDSS 9.6.1.1 (plus some official SVN commits up to rev 3595, plus our own changes.
- **New test suite,** which runs many more files and validates more of the API. We now use `pytest` for some more complex tests, while the numeric validation is done with the new `compare_outputs.py`.
- **New `DSS.AdvancedTypes`:** toggle matrix shapes and complex numbers in many of the properties and functions of the API. This is disabled by default.
- **New `DSS.CompatFlags`:** to address some concerns about compatibility, we added a few toggles to toggle behavior that matches the official OpenDSS more closely. This flags will be refined in later releases.
- Drop deprecated IR classes and a few undocumented functions.
- Use **more enums** throughout the code, which helps both readability and documentation. Some enums were complemented.
- **`DSS.AdvancedTypes`** toggle: enabling `AdvancedTypes` allows using **array/matrix shapes and complex numbers** as results from properties/functions in the API.
- **Plotting**: Implement several plot types. Only a few issues need to be addressed to consider the plotting system complete!
- **Notebook integration**: Initial prototype available. It is enabled automatically when `DSS.Plotting.enable()` is run in a notebook, providing integration with some DSS messages and outputs.
    - It also registers the **`%%dss` cell magic**. Use it in a cell to run DSS-language code directly. We found it useful for exploration and learning.
- Updated `patch_dss_com` to patch a few more classes.
- Drop Python 3.6 support, include 3.11 officially in the tests.
- **DSSContext disposal:** use CFFI to track the disposal of the contexts instead of manually tracking. This could remove memory leaks if you application creates too many DSSContexts (which is not recommended).
- **DSS.Obj:** remove some redundant properties, fix several issues. While it's not complete yet (some known limitations), you can see the tests for a few examples of how to create circuits without .DSS scripts/files in [tests/test_obj.py](https://github.com/dss-extensions/dss_python/blob/master/tests/test_obj.py) and [tests/test_batch.py](https://github.com/dss-extensions/dss_python/blob/master/tests/test_batch.py) — the first creates each object explicitly, while the second uses batch operations to fill properties from arrays and lists.
- Add `typing_extensions` as a dependency to address Python typing needs in the main API code and the new Obj API.
- Docs: mark more properties as "**(API Extension)**".
- Internal code refactoring and clean-up.

#### DSS C-API 0.13.0 changes 

[**check its repo for more info**](https://github.com/dss-extensions/dss_capi/)

- Clean-up several files to ease the transition from Pascal to C++; more enum usage, remove redundant internal properties, rename some class members, etc. Some final steps still remain (that work is done in private branches).
- Fixes a couple of minor memory leaks.
- Removed our old *Legacy Models* mechanism. Right now, the API functions still exist, but will have no effect when setting and will throw an error. For a future version, the functions will be removed. This toggle was introduced in 2020, some time after the removal of the legacy models in the official OpenDSS. We believe users had enough time to fully migrate and the extra maintenance burden is not justified anymore.
- Transition some deprecated and buggy properties to throw specific errors, instead of generic messages. Issue: https://github.com/dss-extensions/dss_capi/issues/118
- `Export` command: When the user provides a filename, use it as-is, otherwise could be an invalid path in case-sensitive file systems (e.g. Linux, most likely).
- `Dump` and `Save` commands: in some cases, our internal "hybrid enums" were not being converted correctly for dumps. A few classes had incomplete dump implementations since v0.12.0; some strings needed to be escaped for correct output.
- CtrlQueue: adjust string formatting of items; although this doesn't affect the numeric results, the strings from the queue had some truncated numbers.
- Property system: For compatibility with the official version, allow autoresizing some arrays when given conflicting number of elements through the text interface or scripts.
- `Like` property: Although not recommended and [deprecated in the official OpenDSS](https://sourceforge.net/p/electricdss/discussion/861977/thread/8b59d21eb6/?limit=25#b57c/f668), the sequence of properties filled in the original copy is also copied. If you use `Like`, remember to check if the copy actually worked since some classes are known to not copy every property correctly.
- Plotting and UI: The engine side plotting callback system is now complete. There are fixes for `DaisyPlot` and `GeneralDataPlot`, especially multi-platform handling. Changed how some properties are exposed in the JSON interchange to the callbacks. Implement argument handling and callback dispatch for `DI_Plot`, `CompareCases` and `YearlyCurves`.
- `New` commands: Fix potential issue with null pointers and duplicate names when `DuplicatesAllowed=False`.
- EnergyMeter: Fix error message when the metered element is not a PDElement.
- CIMXML export: Fix issues present since v0.12.0; reported in https://github.com/dss-extensions/OpenDSSDirect.py/issues/121
- Parser: properly error out when given excessive number of elements for matrices; implemented due to the report in https://github.com/dss-extensions/OpenDSSDirect.py/issues/122
- Port most changes from the official OpenDSS up to SVN revision 3595 (OpenDSS v9.6.1.1 + a couple of CIMXML updates); check [OpenDSS v9.6.1.1 README.txt](https://sourceforge.net/p/electricdss/code/3595/tree/trunk/Version8/README.txt) for some complementary info to the list below.
    - Relay, UPFC, UPFCControl changes ported.
    - CIMXML exports: Various updates.
    - RegControl: More log and debug trace entries.
    - LoadMult: Set `SystemYChanged` when changing `LoadMult` **through a DSS script or DSS command** (doesn't affect `Solution_Set_LoadMult`)
    - Port PVSystem, Storage, InvControl, and StorageController changes, including the new grid-forming mode (GFM). For DSS-Extensions, we added a new class InvBasedPCE to avoid some redundancy and make things clearer.
    - Port DynamicExp and related functionality. In our implementation, we also add a new class DynEqPCE to avoid some redundant code (could still be improved). the Generator and the new InvBasePCE derive from this new DynEqPCE. **Note**: the `DynamicEq` functionality from the upstream still seems incomplete and some things are not fully implemented or maybe buggy, so we only ported now to remove the burden of porting this down the line. If you find issues, feel free to report here on DSS-Extensions, but we recommended checking first with the official OpenDSS — if the issue is also found in the official version, prefer to report in the official OpenDSS forum first so everyone gets the fixes and our implementation doesn't diverge too much.
    - CktElement/API: add a few new functions related to state variables.
    - Circuit, Line: port the `LongLineCorrection` flag now that it seems to be fixed upstream. Note that we didn't publish releases with the previous buggy version from the upstream OpenDSS (that applied the long-line correction for everything).
    - LineSpacing: port side-effect from upstream; changing `nconds` now reallocates and doesn't leak previously allocated memory. Not a common operation, so it's not very relevant.
    - CktElement: port code for handling losses in AutoTrans
- Other API updates:
    - DSSContext API: allow `null` pointer for the prime/default instance. This should ease the transition. Issue: https://github.com/dss-extensions/dss_capi/issues/119
    - Error API: add `Error_Set_Description` to allow easier setting an error message from callbacks (this is for advanced usage)
    - Batch and Obj API: 
        - For a couple of fast-path operations, add checks for edit state, automatically issuing `BeginEdit` and `EndEdit` for the objects in the batch.
        - Allow passing strings (object names) instead of pointers for object references
        - Automatically add new elements to the current DSSContext (since we have not yet published a manipulation API)
        - For symmetric matrices, if the user passes only the triangle, follow the same convention as the Text interface. Includes specific fix for (parts of) complex matrices (like the R or X matrices when internally Z is stored). If the user provides full matrices, the previous behavior was correct, no changes required.
    - `Fuses_Reset`: fix C header (remove extra/unused parameter)
    - `Fuses_Get_State` and `Fuses_Get_NormalState`: add missing string copy. Sometimes this could cause memory corruption.
    - `Bus_Get_ZSC012Matrix`: check for nulls
    - `Bus_Get_AllPCEatBus`, `Bus_Get_AllPDEatBus`: faster implementations
    - `Meters_Get_CountBranches`: reimplemented
    - `Monitors_Get_dblHour`: For harmonics solution, return empty array. Previously, it was returning a large array instead of a single element (`[0]`) array. A small issue adjusted for compatibility with the official COM API results.
    - `Reactors_Set_Bus1`: Match the side-effects of the property API for two-terminal reactors. 
    - New `DSS_Set_CompatFlags`/`DSS_Get_CompatFlags` function pair: introduced to address some current and potential future concerns about compatibility of results with the official OpenDSS. See the API docs for more info.
    - New `DSS_Set_EnableArrayDimensions`/`DSS_Get_EnableArrayDimensions`: for Array results in the API, implement optional matrix sizes; when setting `DSS_Set_EnableArrayDimensions(true)`, the array size pointer will be filled with two extra elements to represent the matrix size (if the data is a matrix instead of a plain vector). For complex number, the dimensions are filled in relation to complex elements instead of double/float64 elements even though we currently reuse the double/float64 array interface. Issue: https://github.com/dss-extensions/dss_capi/issues/113

Note that a couple of SVN changes were ignored on purpose since they introduced potential issues, while many other changes and bug-fixes did not affect the DSS C-API version since our implementation is quite different in some places.

## 0.12.x

### 0.12.1

Released on 2022-07-16.

- Expose `Storages` in Python
- Include the missing property descriptions from 0.12.0
- Use DSS C-API v0.12.1 for some incremental fixes

### 0.12.0

Released on 2022-07-14.

- Removed CmathLib: not useful in Python or most programming languages targeted by DSS-Extensions.
- Allow creating multiple DSS engine instances via `DSS.NewContext()`.
- Reenabled Parallel interface and PM functions (actors and so on), based on a new implementation.
- Enable incremental Y matrix options — controlled by `DSS.YMatrix.SolverOptions`, options listed in `SparseSolverOptions`.
- New `ToJSON` functions to dump object properties (power flow state is not included at the moment)
- Initial implementation of the new `DSS.Obj` API for direct DSS object and uniform batch manipulation, covering all DSS classes implemented in DSS C-API. The shape of this API may change for the next releases. At the moment it is intended for advanced users. For example, if you get an object handle from the engine and load a new circuit, the handle is invalid and you should not access it anymore (otherwise, crashes are expected).
- Initial (work-in-progress) implementation of plotting functions. This will also be finished and polished in following releases.
- Due to some changes ported from the official OpenDSS since 0.10.7, some results may change, especially for circuits that used miles as length units. The same is observed across the official OpenDSS releases.


#### DSS C-API 0.12.0 changes

**Includes porting of most official OpenDSS features up to revision 3460.** Check the OpenDSS SVN commits for details.

Since version 0.11 accumulated too many changes for too long (nearly 2 years), making it hard to keep two parallel but increasingly distinct codebases, version 0.12 is a stepping stone to the next big version (planned as 0.13) that will contain all of the 0.11 changes. As such, only some of the 0.11 features are included. The previous 0.10.8 changes are also included here.

This version still maintains basic compatibility with the 0.10.x series of releases, but there are many important changes. Version 0.13 will break API and ABI compatibility since function signatures and datatypes will be extensively adjusted. Still, if you use DSS C-API through one of the projects from DSS-Extensions, we expect that your code will require few or no changes.

- The binary releases now use Free Pascal 3.2.2.
- The library name was changed from `dss_capi_v7` to `dss_capi`. The codebase was cleaned up and reorganized.
- The code was finally unified, merging remaining features from OpenDSS v8+ (with few exceptions). Most of the DSS PM commands and functions were enabled. To achieve this, most of the global variables from the OpenDSS engine were encapsulated in a new class, a DSS Context class. Multi-threaded features are based on DSSContexts, both the original OpenDSS PM features and new extensions.
- Using DSS Contexts, user threads are now possible.
- Initial ARM64/AARCH64 support added. ARM32 building scripts were also added. Support includes Apple M1 support, including parallel/multi-threading features.
- Finally use KLUSolveX (our KLUSolve fork, rewritten and extended), enabling incremental Y updates for transformers and capacitor banks. **Documentation including usage notes and limitations still not written.** This was planned for version v0.13, but moved back to v0.12 to enable ARM32 (armv7l) support and better results in ARM64 (aarch64).
- Experimental callbacks for plotting and message output. Expect initial support in Python soon after DSS C-API v0.12 is released.
- Introduce `AllowChangeDir` mechanism: defaults to enabled state for backwards compatibility. When disabled, the engine will not change the current working directory in any situation. This is exposed through a new pair of functions `DSS_Set_AllowChangeDir` and `DSS_Get_AllowChangeDir`, besides the environment variable `DSS_CAPI_ALLOW_CHANGE_DIR`.
- New setting to toggle `DOScmd` command. Can be controlled through the environment variable `DSS_CAPI_ALLOW_DOSCMD` or functions `DSS_Get_AllowDOScmd`/`DSS_Set_AllowDOScmd`.
- Use `OutputDirectory` more. `OutputDirectory` is set to the current `DataPath` if `DataPath` is writable. If not, it's set to a general location (`%LOCALAPPDATA%/dss-extensions` and `/tmp/dss-extensions` since this release). This should make life easier for a user running files from a read-only location. Note that this is only an issue when running a `compile` command. If the user only uses `redirect` commands, the `DataPath` and `OutputDirectory` are left empty, meaning the files are written to the current working directory (CWD), which the user can control through the programming language driving DSS C-API. Note that the official OpenDSS COM behavior is different, since it loads the `DataPath` saved in the registry and modifies the CWD accordingly when OpenDSS is initialized.
- File IO rewritten to drop deprecated Pascal functions and features. This removes some limitations related to long paths due to the legacy implementation being limited to 255 chars.
- Reworked `TPowerTerminal` to achieve better memory layout. This makes simulations running `LoadsTerminalCheck=false` and `LoadsTerminalCheck=true` closer in performance, yet disabling the check is still faster.
- Use `TFPHashList` where possible (replacing the custom, original THashList implementation from OpenDSS).
- New LoadShape functions and internals: 

    - Port memory-mapped files from the official OpenDSS, used when `MemoryMapping=Yes` from a DSS script while creating a LoadShape object.
    - Release the `LoadShape_Set_Points` function, which can be used for faster LoadShape input, memory-mapping externally, shared memory, chunked input, etc.

- Some new functions: 

    - `Circuit_Get_ElementLosses`
    - `CktElement_Get_NodeRef`

- `DSS_Get_COMErrorResults`/`DSS_Set_COMErrorResults`: New compatibility setting for error/empty result. If enabled, in case of errors or empty arrays, the API returns arrays with values compatible with the official OpenDSS COM interface. 
    
    For example, consider the function Loads_Get_ZIPV. If there is no active circuit or active load element:
    - In the disabled state (COMErrorResults=False), the function will return "[]", an array with 0 elements.
    - In the enabled state (COMErrorResults=True), the function will return "[0.0]" instead. This should be compatible with the return value of the official COM interface.
    
    Defaults to True/1 (enabled state) in the v0.12.x series. This will change to false in future series.
    
    This can also be set through the environment variable DSS_CAPI_COM_DEFAULTS. Setting it to 0 disables
    the legacy/COM behavior. The value can be toggled through the API at any time.

- Drop function aliases: previously deprecated function aliases (`LoadShapes_Set_Sinterval` and `LoadShapes_Get_sInterval`) were removed to simplify the build process. Use `LoadShapes_Set_SInterval` and `LoadShapes_Get_SInterval` instead.
- Monitor headers: From the official OpenDSS, since May 2021, the monitor binary stream doesn't include the header anymore. When porting the change to DSS-Extensions, we took the opportunity to rewrite the related code, simplifying it. As such, the implementation in DSS-Extensions deviates from the official one. Extra blank chars are not included, and fields should be more consistent. As a recommendation, if your code needs to be compatible with both implementations, trimming the fields should be enough.
- Error messages: most messages are now more specific and, if running a DSS script from files, include the file names and line numbers.
- Spectrum: To reduce overhead during object edits, now required to exist before the object that uses it. This is consistent with most of the other types in OpenDSS.
- New object and batch APIs for direct manipulation of DSS objects and batches of objects
- New experimental API for loading scripts/data from ZIP files
- New convenience functions to bulk load commands from the API
- User-models: headers updated, and removed support for user-models in `LegacyModels` mode. `LegacyModels` will be removed in v0.13.
- New functions to export the DSS properties of objects as JSON-encoded strings
- The C headers for our library were updated to include the `const` modifier for various of the parameters. A few function declarations were fixed.
- Initial batch of i18n changes.

Due to the high number of IO changes, we recommend checking the performance before and after the upgrade to ensure your use case is not affected negatively, especially if your application relies heavily on OpenDSS text output. If issues are found, please do report.

## 0.10.x

### 0.10.7

Released on 2020-12-29.

- Maintenance release. 
- Updated to DSS C-API 0.10.7, which includes most changes up to OpenDSS v9.1.3.4.
- Includes an important bug fix related to the `CapRadius` DSS property. If your DSS scripts included the pattern `GMRac=... rad=...` or `GMRac=... diam=...` (in this order and without specifying `CapRadius`), you should upgrade and re-evaluate the results. 
- New API properties ported from the official COM interface: `Bus.AllPCEatBus`, `Bus.AllPDEatBus`, `CktElement.TotalPowers`, `Meters.ZonePCE`

DSS C-API 0.10.7 changes:

- Simple maintenance release, which includes most changes up to OpenDSS v9.1.3.4 (revision 2963).
- Includes an important bug fix related to the `CapRadius` DSS property. If your DSS scripts included the pattern `GMRac=... rad=...` or `GMRac=... diam=...` (in this order and without specifying `CapRadius`), you should upgrade and re-evaluate the results. 
- This version should be fully API compatible with 0.10.3+.
- A reference document listing the DSS commands and properties for all DSS elements is now available at https://github.com/dss-extensions/dss_capi/blob/0.10.x/docs/dss_properties.md
- New functions API ported from the official OpenDSS include: `Bus_Get_AllPCEatBus`, `Bus_Get_AllPDEatBus`, `CktElement_Get_TotalPowers`, `Meters_Get_ZonePCE`.
- The changes ported from the official OpenDSS include the following (check the repository for more details):
    - "Adds LineType property to LineCode and LineGeometry objects."
    - "Correcting bug found in storage device when operating in idling mode. It was preventing the solution of other test feeders (IEEE 9500)"
    - "Enabling fuel option for generator, fixing bug found in TotalPower command."
    - "Adding kvar compensation calculation for normalizing reactive power at feeder head. v 9.1.2.4"
    - "Adding: - Line type variable to line definition. - AllPCEatBus and AllPDEatBus commands to the executive command set. - AllPCEatBus and AllPDEatBus commands to bus interface in COM/DLL. (...)"
    - "Adding capability to energy meter for getting the list of all PCE (shunt) within a zone. Interface "AllPCEatZone" for COM/DLL created."
    - "Fixing bug found when calculating voltage bases with large amount of numbers (large array)."


### 0.10.6

Released on 2020-08-01.

- Updated to DSS C-API 0.10.6, which includes most changes up to OpenDSS v9.0.0.3.
- Debug builds of DSS C-API are now included. See the [Debugging](https://github.com/dss-extensions/dss_capi/blob/0.10.x/docs/debug.md) document.
- New `DSS.LegacyModels`: allow using the legacy/deprecated models for `PVsystem`, `Storage`, `InvControl`, and `StorageController`. 
- New `DSS.Error.ExtendedErrors`: controls if the new extended error messages are used.
- Many new properties and functions in `DSS.ActiveCircuit.PDElements`.
- Now most of the low-level API calls are checked, mapping the errors from the `DSS.Error` interface to Python exceptions more frequently.

DSS C-API 0.10.6 changes:

- This version should be fully API compatible with 0.10.3+. The behavior of some functions changed with the new extensions. Especially, empty strings are explicitly return as nulls instead of "\0". This conforms to the behavior already seen in arrays of strings.
- The binary releases now use Free Pascal 3.2.0. We observed the solution process is around 6% faster, and results are even closer to the official OpenDSS.
- The releases now include both the optimized/default binary and a non-optimized/debug version. See the [Debugging](https://github.com/dss-extensions/dss_capi/blob/0.10.x/docs/debug.md) document for more.
- Extended API validation and **Extended Errors** mechanism: 
    - The whole API was reviewed to add basic checks for active circuit and element access. 
    - By default, invalid accesses now result in errors reported through the Error interface. This can be disabled to achieve the previous behavior, more compatible with the official COM implementation — that is, ignore the error, just return a default/invalid value and assume the user has handled it.
    - The mechanism can be toggled by API functions `DSS_Set_ExtendedErrors` and `DSS_Get_ExtendedErrors`, or environment variable `DSS_CAPI_EXTENDED_ERRORS=0` to disable (defaults to enabled state).
- New **Legacy Models** mechanism:
    - OpenDSS 9.0+ dropped the old `PVsystem`, `Storage`, `InvControl`, and `StorageController` models, replacing with the new versions previously known as `PVsystem2`, `Storage2`, `InvControl2` and `StorageController2`.
    - The behavior and parameters from the new models are different — they are better, more complete and versatile models. Check the official OpenDSS docs and examples for further information. 
    - The implementation of the new models in DSS C-API was validated successfully with all test cases available. As such, we mirror the decision to make them the default models.
    - As an extension, we implemented the Legacy Models option. By toggling it, a `clear` command will be issued and the alternative models will be loaded. This should allow users to migrate to the new version but, if something that used to work with the old models stopped working somehow, the user can toggle the old models. The idea is to keep reproducibility of results while we keep updating the engine and the API.
    - Since EPRI dropped/deprecated the old models, we might drop them too, in a future release. Please open an issue on GitHub or send a message if those old models are important to you.
    - The mechanism can be controlled by API functions `DSS_Set_LegacyModels` and `DSS_Get_LegacyModels`, or environment variable `DSS_CAPI_LEGACY_MODELS=1` to enable (defaults to disabled state).
- WireData API: expose the `CapRadius` property as a new pair of functions.
- PDElements API: extended with many batch functions exposing equivalents to some CSV reports: `AllNames`, `AllMaxCurrents`, `AllPctNorm`, `AllPctEmerg`, `AllCurrents`, `AllCurrentsMagAng`, `AllCplxSeqCurrents`, `AllSeqCurrents`, `AllPowers`, `AllSeqPowers`, `AllNumPhases`, `AllNumConductors`, `AllNumTerminals`.
- `CktElement_Get_SeqPowers`: fix issue for positive sequence circuits (wrong results could corrupt memory).
- Many API functions were optimized to avoid unnecessary allocations and copies.
- Some bugs found in DSS C-API and also reported upstream (already fixed in SVN):
    - `CapRadius` DSS property: if the radius was initialized using `GMRac`, `CapRadius` was left uninitialized, resulting in invalid/NaN values.
    - `Sensors` API: some functions edited capacitors instead of sensors.
- Updated to the official OpenDSS revision 2903, corresponding to versions 9.0.0+. Changes include:
    - ExportCIMXML: updated.
    - Relay: Fix in `GetPropertyValue`.
    - Line: In `DumpProperties` and `MakePosSequence`, the length is handled differently for lines with `LineGeometry` or `LineSpacing`.
    - Bus API: new `LineList`, `LoadList` functions.
    - Lines API: SeasonRating now returns NormAmps if there's no SeasonSignal.
    - New command DSS `Zsc012`: "Returns symmetrical component short circuit impedances Z0, Z1, and Z2 for the ACTIVE 3-PHASE BUS. Determined from Zsc matrix."
    - `PVsystem2`, `Storage2`, `InvControl2`, `StorageController2` updated and renamed.


### 0.10.5

Released on 2020-03-03. This is a maintenance release.

- Updated to DSS C-API 0.10.5, which includes most changes up to OpenDSS v8.6.7.1. Includes new properties and new experimental components (under testing).
- New properties exposed: `ActiveClass.ActiveClassParent`, `PVSystems.Pmpp`, `PVSystems.IrradianceNow`.
- For the time being, `dss.v8` doesn't use the parallel-machine version anymore. This will be addressed in a future release, most likely in the 0.11.x series coming in the following months.

DSS C-API 0.10.5 changes:

- Disable builds and distribution of v8-only variation — the extra/missing parallel-machine will be completely merged in a mixed (v7+v8) codebase in the coming months.
- This version should be fully API compatible with 0.10.3+.
- `Bus` and `CktElement` API functions reworked with some more checks.
- Updated up to revision 2837 of the official OpenDSS code:
    - Ported changes from SVN (v7 and v8) into DSS C-API v7 variation (v8 was left untouched).
    - 4 new API level functions (`ActiveClass_Get_ActiveClassParent`, `PVSystems_Get_Pmpp`, `PVSystems_Set_Pmpp`, `PVSystems_Get_IrradianceNow`)
    - 4 new components: `PVsystem2`, `Storage2`, `InvControl2`, `StorageController2` — *added for early testing, no dedicated API functions yet*. At the moment, please consider them experimental features subject to change.
    - `CIM100`: several changes
    - `ExpControl`: new `Tresponse` property
    - `ConductorData`, `LineConstants`, `LineGeometry`: new `Capradius` property
    - `XfmrCode`, `Transformer`: new Seasons and Ratings properties
    - `Bus_Get_puVLL` and `Bus_Get_VLL` — see revision 2836 (official SVN). Included an extra fix in DSS C-API to avoid some corner cases.
    - Other small bug fixes like the Full Carson fix — see https://sourceforge.net/p/electricdss/discussion/861976/thread/2de01d0cdb/ and revision 2805 (official SVN)

### 0.10.4

Released on 2019-11-16. This is a maintenance release.

- Updated to DSS C-API 0.10.4.
- Fix `dss.enums.YMatrixModes`
- Make `DSS.ActiveCircuit.CktElements` iterable (e.g. `for element in DSS.ActiveCircuit.CktElements: ...`);


DSS C-API 0.10.4 changes include:

- Updated up to revision 2761 of the official OpenDSS code. The changes affect at least the following components: CIMXML export, `Capacitor`, `InvControl`, `LineGeometry`, `PVsystem`, `StorageController`, `Storage`, `Vsource`, `VCCS`.
- This version should be fully compatible with 0.10.3.
- Fixes issue with long paths on Linux, potentially other platforms too.

### 0.10.3

Released on 2019-05-22. This is the last release to provide pre-built binaries for Python 3.4.

- Includes fix for issue with the line parameters on Linux and macOS due to memory-address aliasing issues.
- Prebuilt binaries for DSS C-API and KLUSolve are used instead of rebuilding everything from source.
- Prebuilt packages (wheels) for 32-bit Linux are now available.
- Development artifacts are now included in the distribution package. This enables advanced usage and easier integration with compiled languages (examples pending, please open an issue if you'd like to know more).
- `ReduceCkt` ported from COM: new circuit reduction methods available in `DSS.ActiveCircuit.ReduceCkt`
- `Lines`: ported from COM, new seasonal ratings mechanism that allows changing the current rating through the simulation
- Optimization and extended error-checking in many properties
- Includes new `Settings.LoadsTerminalCheck`: on static scenarios (no open terminals for loads) to toggle the costly checks for open terminals. If set to false, it can save around 25% of simulation time, depending on the circuit characteristics.
- All components now can be accessed by index (`idx` property)
- All components now have faster `Name` iteration
- Ported to v7/default interface: the DSS commands `CalcIncMatrix`, `CalcIncMatrix_O`, `Refine_BusLevels`, `CalcLaplacian`, and related export options: `IncMatrix`, `IncMatrixRows`, `IncMatrixCols`, `BusLevels`, `Laplacian`, `ZLL`, `ZCC`, `Contours`, `Y4`. Also includes related Python-level properties.
- Some other new properties:
    - `CktElement.IsIsolated`
    - `Lines.IsSwitch`
    - `Transformers.LossesByType` and `Transformers.AllLossesByType`

### 0.10.2

Released on 2019-02-28.

- `CtrlQueue`: Add the missing function `Push`. See [CtrlQueueTest.py](https://github.com/dss-extensions/electricdss-tst/blob/master/Test/CtrlQueueTest.py) for an example ported from the Excel VBA example.
- New `DSS.AllowEditor`: this new property controls if the external editor is called on DSS commands like `Show`. If set to `False`, the editor is not called, but other side effects should not be affected (e.g. files can be created).
- The `enum34` module was added as a dependency for Python < 3.5.
- The `Options` enumeration was split into several new enumerations (`AutoAddTypes`, `CktModels`, `ControlModes`, `SolutionLoadModels`, `SolutionAlgorithms`, `RandomModes`). It is now marked as deprecated for future removal.
- `LoadShapes` are faster due to [changes from DSS C-API](https://github.com/dss-extensions/dss_capi/blob/master/docs/changelog.md#version-0102)


### 0.10.1

Released on 2019-02-17.

This is a minor DSS-Python release that contains lots of changes from DSS C-API. See also the [changes from DSS C-API](https://github.com/dss-extensions/dss_capi/blob/ed2a6b322a5e102ba61c6565e5e0eb23247b9221/docs/changelog.md#version-0101) for details, including changes from the official OpenDSS code since 0.10.0.

DSS-Python has recently moved from https://github.com/PMeira/dss_python/ to the new https://dss-extensions.org/ and https://github.com/dss-extensions/dss_python/

Major changes:

- More and faster error-checking! Python exception will be raised for more errors and with a lower overhead.
- Fix for `YMatrix.getI` and `YMatrix.getV` (ported from OpenDSSDirect.py)
- Fix for `ActiveCircuit.ActiveCktElement.Variable` and `ActiveCircuit.ActiveCktElement.Variablei`: now returns a tuple of `(value, errorcode)`, compatible with COM.
- New `DSS.Error.EarlyAbort`: controls whether all errors halts the DSS script processing (Compile/Redirect), defaults to True.

### 0.10.0

Released on 2018-11-17.

Major changes:

- The creation of the binary modules has been automated using Travis-CI and AppVeyor. We expect that this will allow us to release more often, bringing new features sooner.
- Integrates many fixes from the upstream OpenDSS and changes specific to DSS C-API.
- Reorganizes and reuses the code across DSS versions (v7 and v8) 
- Uses `__slots__` to simplify attribute handling.
- Exposes both the our classic API (e.g. `dss.v7.DSS_IR` for the immediate/direct results) and global result API (e.g. `dss.v7.DSS_GR` for the global result interface). See [DSS C-API's docs](https://github.com/dss-extensions/dss_capi/blob/master/docs/usage.md) for a detailed explanation. We default to the GR interface since it will generally be faster at the cost of a small memory overhead.
- Although still experimental, the v8/PM module is more stable. If you try it, please give feedback.
- Error checking is now done for most API writes. That is, if a an OpenDSS error occurs, it should cause a Python exception soon after. Previously, you need to call `_check_for_error()` manually to trigger this. This change was introduced after user reports indicated that manually checking for errors is a common behavior.
- Exposes API extensions for the classes `LineGeometry`, `WireData`, `LineSpacing`, `CNData`, `TSData`, `Reactor`.
- Makes most DSS classes iterable (including buses), e.g. you can now use:

```python
for l in DSS.ActiveCircuit.Loads:
    print(l.Name)
```

- Adds a COM patching function (`dss.patch_dss_com`) — that is, extend the COM instance with iterators like above and some other few functions to make it easier to exchange between COM and DSS-Python:

```python

import win32com.client, dss
com = dss.patch_dss_com(win32com.client.gencache.EnsureDispatch("OpenDSSEngine.DSS"))

# ...compile a circuit, etc.

for l in com.ActiveCircuit.Loads:
    print(l.Name, l.kva)

for b in com.ActiveCircuit.ActiveBus:
    print(b.Name, b.x, b.y)
```

## 0.9.x

Sorry, we didn't track the changes at the time. Check the Git logs below plus the related changes under DSS C-API.

### 0.9.8

https://github.com/dss-extensions/dss_python/compare/0.9.7...0.9.8

### 0.9.7

https://github.com/dss-extensions/dss_python/compare/0.9.6...0.9.7

### 0.9.6

https://github.com/dss-extensions/dss_python/compare/0.9.5...0.9.6

### 0.9.5

https://github.com/dss-extensions/dss_python/compare/0.9.4...0.9.5

### 0.9.4

https://github.com/dss-extensions/dss_python/compare/0.9.3...0.9.4

### 0.9.3

https://github.com/dss-extensions/dss_python/compare/0.9.2...0.9.3

### 0.9.2

https://github.com/dss-extensions/dss_python/compare/0.9.1...0.9.2

### 0.9.1

Released on 2018-02-08.

First public release!
