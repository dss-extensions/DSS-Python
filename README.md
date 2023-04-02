[![Builds](https://github.com/dss-extensions/dss_python/actions/workflows/builds.yml/badge.svg)](https://github.com/dss-extensions/dss_python/actions/workflows/builds.yml)
[![PyPI](https://img.shields.io/pypi/v/dss_python)](https://pypi.org/project/dss-python/)
[![Install with conda](https://anaconda.org/dss-extensions/dss_python/badges/installer/conda.svg)](https://anaconda.org/dss-extensions/dss_python)
[![conda package version](https://anaconda.org/dss-extensions/dss_python/badges/version.svg)](https://anaconda.org/dss-extensions/dss_python) <img alt="Supports Linux" src="https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black"> <img alt="Supports macOS" src="https://img.shields.io/badge/macOS-000000?logo=apple&logoColor=white"> <img alt="Supports Microsoft Windows" src="https://img.shields.io/badge/Windows-0078D6?logo=windows&logoColor=white">

# DSS Python: Extended bindings for an implementation of EPRI's OpenDSS

Python bindings and misc tools for using the OpenDSS (EPRI Distribution System Simulator) engine through the alternative/unofficial implementation from the DSS C-API library. Based on DSS C-API, CFFI and NumPy, aiming for enhanced performance and full compatibility with the official COM object API on Windows, Linux and macOS. Support includes Intel-based (x86 and x64) processors, as well as ARM processors for Linux and macOS (including Apple M1 and later).

Please see [FAQ](https://github.com/dss-extensions/dss-extensions#faq) for a couple of notes. Check also the other projects from [DSS-Extensions.org](https://dss-extensions.org/):

- [DSS C-API library](http://github.com/dss-extensions/dss_capi/): the base library that exposes a modified version of EPRI's OpenDSS through a more traditional C interface, built with the open-source Free Pascal compiler instead of Delphi. As of 2022, this base library includes several extensive changes, while retaining very good compatibility.
- [dss.hpp](https://dss-extensions.org/dss_capi/): header-only library for C++, hosted within DSS C-API (`include/` directory). Allows using DSS C-API more comfortably from C++, abstract memory management and low-level details such as API conventions of the DSS C-API library.
- [OpenDSSDirect.py](http://github.com/dss-extensions/OpenDSSDirect.py/): if you don't need COM compatibility, or just would like to check its extra functionalities. You can mix DSS Python and OpenDSSDirect.py -- for example, if you have old code using the official COM objects, you could quickly switch to DSS Python with very few code changes, and then use [`opendssdirect.utils`](https://dss-extensions.org/OpenDSSDirect.py/opendssdirect.html#module-opendssdirect.utils) to generate some DataFrames.
- [OpenDSSDirect.jl](http://github.com/dss-extensions/OpenDSSDirect.jl/) is a Julia module, created by Tom Short (@tshort), migrated with the help of Dheepak Krishnamurthy (@kdheepak) to DSS C-API instead of the DDLL in Feb 2019.
- [DSS Sharp](http://github.com/dss-extensions/dss_sharp/) is available for .NET/C#, [packaged on NuGet](https://www.nuget.org/packages/dss_sharp/), also mimics the COM classes (drop-in replacement for `OpenDSSengine.DLL`). The current version is now multi-platform too! Soon it will be possible to use it via COM.
- [DSS MATLAB](http://github.com/dss-extensions/dss_matlab/) presents multi-platform integration (Windows, Linux, MacOS) with DSS C-API and is also very compatible with the API of the official OpenDSS COM classes.

Version 0.13.x is based on OpenDSS revision 3595 (few commits after OpenDSS v9.6.1.1, but we pick and choose when to port certain features). While we plan to add a lot more functionality into DSS Python, the main goal of creating a COM-compatible API has been reached in 2018. If you find an unexpected missing feature, please report it! Currently missing features that will be implemented eventually are plotting (partial implementation available) and diakoptics (planned for future version).

This module mimics the COM structure (as exposed via `win32com` or `comtypes`) -- see [The DSS instance](https://dss-extensions.org/dss_python/#the-dss-instance) for some docs --  effectively enabling multi-platform compatibility at Python level. Compared to other options, it provides easier migration from code that uses the official OpenDSS through COM.
Most of the COM documentation can be used as-is, but instead of returning tuples or lists, this modules returns/accepts NumPy arrays for numeric data exchange, which is usually preferred by the users.

The module depends on CFFI, NumPy and, optionally, SciPy.Sparse for reading the sparse system admittance matrix. Pandas and matplotlib are optional dependencies to enable plotting and other features.

## Brief release history

- **2023-04-01 / version 0.13.1: Microupdate to the OpenDSS engine; very minor Python changes.**
- 2023-03-29 / version 0.13.0: Updates to the OpenDSS engine, move plotting and initial notebook integration, matrix shapes and complex numbers, bug fixes, etc.
- 2022-07-16 / version 0.12.1: Very minor release to address a bug found in v0.12.0, to add the Storages API, and include the property descriptions/help.
- 2022-07-14 / version 0.12.0: Major release merging parallel features, multiple DSS engine instances, ZIP file support, incremental Y matrix updates, new API functions, partial plotting support, better performance, and so on. General usage examples for the new features will be incrementally added to https://github.com/dss-extensions/dss-extensions
- 2021-03-09 / version 0.10.7-1: Very minor release to fix issues with some of the energy meter reports.
- 2020-12-28 / version 0.10.7: Maintenance release to match DSS C-API 0.10.7, based on on OpenDSS revision 2963. Includes fixes and new features from the official OpenDSS.
- 2020-07-31 / version 0.10.6: Maintenance release to match DSS C-API 0.10.6, based on on OpenDSS revision 2909. New important settings: `DSS.LegacyModels` and `DSS.Error.ExtendedErrors`.
- 2020-03-03 / version 0.10.5: Maintenance release to match DSS C-API 0.10.5, based on on OpenDSS revision 2837. Temporarily drops the v8 parallel-machine functions, as well as conda packages on Windows.
- 2019-11-16 / version 0.10.4: Maintenance release to match DSS C-API 0.10.4.
- 2019-05-22 / version 0.10.3: Some important fixes, better general performance, new API extensions, new features ported from COM and the OpenDSS version 8 codebase.
- 2019-02-28 / version 0.10.2: Some small fixes, adds the missing `CtrlQueue.Push`, faster LoadShapes and new property `DSS.AllowEditor` to toggle editor calls.
- 2019-02-17 / version 0.10.1: Integrate DSS C-API changes/fix, some small fixes, and more error-checking. 
- 2018-11-17 / version 0.10.0: Lots of changes, fixes and new features. Check the new [changelog](docs/changelog.md#0100) document for a list.
- 2018-08-12 / version 0.9.8: Reorganize modules (v7 and v8), adds 8 missing methods and new backend methods for OpenDSSDirect.py v0.3+. Integrates many fixes from DSS_CAPI and the upstream OpenDSS.
- 2018-04-30 / version 0.9.7: Fix some of the setters that used array data.
- 2018-04-05 / version 0.9.6: Adds missing `ActiveCircuit.CktElements[index]` (or `...CktElements(index)`) and `ActiveCircuit.Buses[index]` (or `...Buses(index)`).
- 2018-03-07 / version 0.9.4: Allows using `len` on several classes, fixes DSSProperty, and includes COM helpstrings as docstrings. Contains changes up to OpenDSS revision 2152.
- 2018-02-16 / version 0.9.3: Integrates COM interface fixes from revision 2136 (`First` `Next` iteration on some elements)
- 2018-02-12 / version 0.9.2: Experimental support for OpenDSS-PM (at the moment, a custom patch is provided for FreePascal support) and port COM interface fixes (OpenDSS revision 2134)
- 2018-02-08 / version 0.9.1: First public release (OpenDSS revision 2123)

## Missing features and limitations

Most limitations are inherited from `dss_capi`, i.e., these are not implemented:

- `DSSEvents` from `DLL/ImplEvents.pas`: seems too dependent on COM.
- `DSSProgress` from `DLL/ImplDSSProgress.pas`: would need a reimplementation depending on the target UI (GUI, text, headless, etc.).
- OpenDSS-GIS features are not implemented since they're not open-source.

In general, the DLL from `dss_capi` provides more features than both the official Direct DLL and the COM object.
    
## Extra features

Besides most of the COM methods, some of the unique DDLL methods are also exposed in adapted forms, namely the methods from `DYMatrix.pas`, especially `GetCompressedYMatrix` (check the source files for more information).

Since no GUI components are used in the FreePascal DLL, we map nearly all OpenDSS errors to Python exceptions, which seems a more natural way of working in Python. You can still manually trigger an error check by calling the function `CheckForError()` from the main module or manually checking the `DSS.Error` interface.

## Installing

On all major platforms, you can install directly from pip:

```
    pip install dss_python
```

Or, if you're using the Anaconda distribution, you can try:

```
    conda install -c dss-extensions dss_python
```

Binary wheels are provided for all major platforms (Windows, Linux and MacOS) and many combinations of Python versions (3.5 to 3.10). If you have issues with a specific version, please open an issue about it. Conda packages support at least Python 3.7 to 3.10 (varying according to the release).

After a successful installation, you can then import the `dss` module from your Python interpreter.

## Building

Get the repository:

```
    git clone https://github.com/dss-extensions/dss_python.git
```    
    
Assuming you successfully built or downloaded the DSS C-API DLLs (check [its repository](http://github.com/dss-extensions/dss_capi/) for instructions), keep the folder organization as follows:

```
dss_capi/
dss_python/
```

Open a command prompt in the `dss_python` subfolder and run the build process:

```
python setup.py build
python setup.py install
```

If you are familiar with `conda-build`, there is a complete recipe to build DSS C-API, KLUSolve(X) and DSS Python in the `conda` subfolder.

Example usage
=============

If you were using `win32com` in code like:

```python
import win32com.client 
dss_engine = win32com.client.gencache.EnsureDispatch("OpenDSSEngine.DSS")
```

or `comtypes` (incidentally, `comtypes` is usually faster than `win32com`, so we recommend it if you need the official OpenDSS COM module):

```python
import comtypes.client
dss_engine = comtypes.client.CreateObject("OpenDSSEngine.DSS")
```

you can replace that fragment with:
```python
from dss import DSS as dss_engine
```

If you need the mixed-cased handling (that is, you were not using early bindings with win32com), add a call to `dss.use_com_compat()`.

Assuming you have a DSS script named `master.dss`, you should be able to run it as shown below:

```python
from dss import DSS as dss_engine

dss_engine.Text.Command = "compile 'c:/dss_files/master.dss'"
dss_engine.ActiveCircuit.Solution.Solve()
voltages = dss_engine.ActiveCircuit.AllBusVolts

for i in range(len(voltages) // 2):
    print('node %d: %f + j%f' % (i, voltages[2*i], voltages[2*i + 1]))
```

Testing
=======
Since the DLL is built using the Free Pascal compiler, which is not officially supported by EPRI, the results are validated running sample networks provided in the official OpenDSS distribution. The only modifications are done directly by the script, removing interactive features and some other minor issues. Most of the sample files from the official OpenDSS repository are used for validation.

The validation scripts is `tests/validation.py` and requires the same folder structure as the building process. You need `win32com` to run it on Windows.

As of version 0.11, the full validation suite can be run on the three supported platforms. This is possible by saving the official COM DLL output and loading it on macOS and Linux. We hope to fully automate this validation in the future.

Roadmap: docs and plotting
==========================
Besides bug fixes, the main functionality of this library is mostly done. Notable desirable features that may be implemented are:

- More and better documentation. Initial reference at [https://dss-extensions.org/dss_python/](https://dss-extensions.org/dss_python/), watch also https://github.com/dss-extensions/dss-extensions for more.
- Plotting and reports integrated in Python. Several of the plot types optionally available in DSS Python 0.12.0, but a few are missing. Reports and advanced integration are planned for a future feature.

Expect news about these items by version 0.13. 

While the base library (DSS C-API) will go through some API changes before v1.0, those do not affect usage from the Python side.

Questions?
==========
If you have any question, feel free to open a ticket on GitHub (here or at https://github.com/dss-extensions/dss-extensions), or contact directly me through email (pmeira at ieee.org). Please allow me a few days to respond.


Credits / Acknowledgment
========================
DSS-Python is based on EPRI's OpenDSS via the [`dss_capi`](http://github.com/dss-extensions/dss_capi/) project, so check its licensing information too.

This project is licensed under the (new) BSD, available in the `LICENSE` file. It's the same license OpenDSS uses (`OPENDSS_LICENSE`). OpenDSS itself uses KLUSolve and SuiteSparse, licensed under the GNU LGPL 2.1.

I thank my colleagues at the University of Campinas, Brazil, for providing feedback and helping me test this package during its inception in 2016-2017, as well as the many users and collaborators that have been using this or other DSS Extensions since the public releases in 2018.
