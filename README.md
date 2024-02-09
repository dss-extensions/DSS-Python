[![Builds](https://github.com/dss-extensions/dss_python/actions/workflows/builds.yml/badge.svg)](https://github.com/dss-extensions/dss_python/actions/workflows/builds.yml)
[![PyPI](https://img.shields.io/pypi/v/dss_python)](https://pypi.org/project/dss-python/) [![PyPI Download stats](https://img.shields.io/pypi/dw/dss-python)](https://pypi.org/project/dss-python/) <img alt="Supports Linux" src="https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black"> <img alt="Supports macOS" src="https://img.shields.io/badge/macOS-000000?logo=apple&logoColor=white"> <img alt="Supports Microsoft Windows" src="https://img.shields.io/badge/Windows-0078D6?logo=windows&logoColor=white">


# DSS-Python: Extended bindings for an alternative implementation of EPRI's OpenDSS

Python bindings and misc tools for using our alternative OpenDSS (EPRI Distribution System Simulator) engine, materialized in the DSS C-API library. Based on DSS C-API, CFFI and NumPy, aiming for enhanced performance and full compatibility with the official COM object API on Windows, Linux and macOS. Support includes Intel-based (x86 and x64) processors, as well as ARM processors for Linux (including Raspberry Pi devices) and macOS (including Apple M1 and later).

Please see [FAQ](https://github.com/dss-extensions/dss-extensions#faq) for a couple of notes. Check also the other projects from [DSS-Extensions.org](https://dss-extensions.org/):

- [DSS C-API library](http://github.com/dss-extensions/dss_capi/): the base library that exposes a modified version (**alternative implementation**) of EPRI's OpenDSS through a more traditional C interface, built with the open-source Free Pascal compiler instead of Delphi. As of 2022, this base library includes several extensive changes, while retaining very good compatibility.
- [dss.hpp](https://dss-extensions.org/dss_capi/): header-only library for C++, hosted within DSS C-API (`include/` directory). Allows using DSS C-API more comfortably from C++, abstract memory management and low-level details such as API conventions of the DSS C-API library.
- [OpenDSSDirect.py](http://github.com/dss-extensions/OpenDSSDirect.py/): if you don't need COM compatibility, or just would like to check its extra functionalities. You can mix DSS-Python and OpenDSSDirect.py — for example, if you have old code using the official COM objects, you could quickly switch to DSS-Python with very few code changes, and then use [`opendssdirect.utils`](https://dss-extensions.org/OpenDSSDirect.py/opendssdirect.html#module-opendssdirect.utils) to generate some DataFrames.
- [OpenDSSDirect.jl](http://github.com/dss-extensions/OpenDSSDirect.jl/) is a Julia module, created by Tom Short (@tshort), migrated with the help of Dheepak Krishnamurthy (@kdheepak) to DSS C-API instead of the DDLL in Feb 2019.
- [DSS Sharp](http://github.com/dss-extensions/dss_sharp/) is available for .NET/C#, [packaged on NuGet](https://www.nuget.org/packages/dss_sharp/), also mimics the COM classes (drop-in replacement for `OpenDSSengine.DLL`). The current version is now multi-platform too! Soon it will be possible to use it via COM.
- [DSS MATLAB](http://github.com/dss-extensions/dss_matlab/) presents multi-platform integration (Windows, Linux, MacOS) with DSS C-API and is also very compatible with the API of the official OpenDSS COM classes.

While we plan to add a lot more functionality into DSS-Python, the main goal of creating a COM-compatible API has been reached in 2018. If you find an unexpected missing feature, please report it! Currently missing features that will be implemented eventually are interactive features and diakoptics (planned for a future version).

This module mimics the COM structure (as exposed via `win32com` or `comtypes`) — see [The DSS instance](https://dss-extensions.org/dss_python/#the-dss-instance) for some docs — effectively enabling multi-platform compatibility at Python level. Compared to other options, it provides easier migration from code that uses the official OpenDSS through COM. See also [DSS-Extensions — OpenDSS: Overview of Python APIs](https://dss-extensions.org/python_apis.html).
Most of the COM documentation can be used as-is, but instead of returning tuples or lists, this module returns/accepts NumPy arrays for numeric data exchange, which is usually preferred by the users. By toggle `DSS.AdvancedTypes`, complex numbers and matrices (shaped arrays) are also used to provide a more modern experience.

The module depends mostly on CFFI, NumPy, typing_extensions and, optionally, SciPy.Sparse for reading the sparse system admittance matrix. Pandas and matplotlib are optional dependencies [to enable plotting](https://github.com/dss-extensions/dss_python/blob/master/docs/examples/Plotting.ipynb) and other features.

## Release history

Check [the Releases page](https://github.com/dss-extensions/dss_python/releases) and [the changelog](https://github.com/dss-extensions/dss_python/blob/master/docs/changelog.md).

## Missing features and limitations

Most limitations are inherited from `dss_capi`, i.e., these are not implemented:

- `DSSProgress` from `DLL/ImplDSSProgress.pas`: would need a reimplementation depending on the target UI (GUI, text, headless, etc.). Part of it can already be handled through the callback mechanisms.
- OpenDSS-GIS features are not implemented since they're not open-source.

In general, the DLL from `dss_capi` provides more features than both the official Direct DLL and the COM object.
    
## Extra features

Besides most of the COM methods, some of the unique DDLL methods are also exposed in adapted forms, namely the methods from `DYMatrix.pas`, especially `GetCompressedYMatrix` (check the source files for more information).

Since no GUI components are used in the FreePascal DLL, we map nearly all OpenDSS errors to Python exceptions, which seems a more natural way of working in Python. You can still manually trigger an error check by calling the function `_check_for_error()` from the main class or manually checking the `DSS.Error` interface.

## Installing

On all major platforms, you can install directly from pip:

```
    pip install dss-python
```

For a full experience, install the optional dependencies with:

```
    pip install dss-python[all]
```

Binary wheels are provided for all major platforms (Windows, Linux and MacOS) and many combinations of Python versions (3.7 to 3.12). If you have issues with a specific version, please open an issue about it.

After a successful installation, you can then import the `dss` module from your Python interpreter.

## Building

Since v0.14.0, dss_python itself is a pure-Python package, i.e., the usual install methods should work fine for itself. However, you may still need to build the backend yourself in some situations.

The backend is now in `dss_python_backend`. The 

Get the repositories

```
    git clone https://github.com/dss-extensions/dss_python.git
    git clone https://github.com/dss-extensions/dss_python_backend.git
```
    
Assuming you successfully built or downloaded the DSS C-API DLLs (check [its repository](http://github.com/dss-extensions/dss_capi/) for instructions), keep the folder organization as follows:

```
dss_capi/
dss_python/
dss_python_backend/
```

Open a command prompt in the `dss_python_backend` subfolder and run the build process:

```
python -m pip install .
cd ../dss_python
python -m pip install .
```


## Documentation

The compiled documentation is hosted at https://dss-extensions.org/dss_python

## Example usage

**Check the documentation for more details.**


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

If you need support for arbitrary capitalization (that is, you were not using early bindings with win32com), add a call to `dss.set_case_insensitive_attributes()`.

Assuming you have a DSS script named `master.dss`, you should be able to run it as shown below:

```python
from dss import DSS as dss_engine

dss_engine.Text.Command = "compile 'c:/dss_files/master.dss'"
dss_engine.ActiveCircuit.Solution.Solve()
voltages = dss_engine.ActiveCircuit.AllBusVolts

for i in range(len(voltages) // 2):
    print('node %d: %f + j%f' % (i, voltages[2*i], voltages[2*i + 1]))
```

## Testing

Since the DLL is built using the Free Pascal compiler, which is not officially supported by EPRI, the results are validated running sample networks provided in the official OpenDSS distribution. The only modifications are done directly by the script, removing interactive features and some other minor issues. Most of the sample files from the official OpenDSS repository are used for validation.

The validation scripts is `tests/validation.py` and requires the same folder structure as the building process. You need `win32com` to run it on Windows.

As of version 0.11, the full validation suite can be run on the three supported platforms. This is possible by saving the official COM DLL output and loading it on macOS and Linux. We hope to fully automate this validation in the future.

## Roadmap: docs and interactive features

Besides bug fixes, the main functionality of this library is mostly done. Notable desirable features that may be implemented are:

- More examples, especially for the extra features. There is a growing documentation hosted at [https://dss-extensions.org/dss_python/](https://dss-extensions.org/dss_python/); watch also https://github.com/dss-extensions/dss-extensions for more.
- Reports integrated in Python and interactive features on plots. Since most of the plot types from the official OpenDSS are optionally available since DSS-Python 0.14.2, advanced integration and interactive features are planned for a future feature.

Expect news about these items by version 1.0. 

While the base library (AltDSS/DSS C-API) will go through some API changes before v1.0, those do not affect usage from the Python side.

## Questions?

If you have any question, feel free to open a ticket on GitHub (here or at https://github.com/dss-extensions/dss-extensions), or contact directly me through email (pmeira at ieee.org). Please allow me a few days to respond.


## Credits / Acknowledgments

DSS-Python is based on EPRI's OpenDSS via the [`dss_capi`](http://github.com/dss-extensions/dss_capi/) project, so check its licensing information too.

This project is licensed under the (new) BSD, available in the `LICENSE` file. It's the same license OpenDSS uses (`OPENDSS_LICENSE`). OpenDSS itself uses KLUSolve and SuiteSparse, licensed under the GNU LGPL 2.1.

I thank my colleagues at the University of Campinas, Brazil, for providing feedback and helping me test this package during its inception in 2016-2017, as well as the many users and collaborators that have been using this or other DSS-Extensions since the public releases in 2018.
