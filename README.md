[![Builds](https://github.com/dss-extensions/dss_python/actions/workflows/builds.yml/badge.svg)](https://github.com/dss-extensions/dss_python/actions/workflows/builds.yml)
[![PyPI](https://img.shields.io/pypi/v/dss_python)](https://pypi.org/project/dss-python/) 
[![PyPI Download stats](https://static.pepy.tech/badge/dss-python/month)](https://pepy.tech/project/dss-python)
 <img alt="Supports Linux" src="https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black"> <img alt="Supports macOS" src="https://img.shields.io/badge/macOS-000000?logo=apple&logoColor=white"> <img alt="Supports Microsoft Windows" src="https://img.shields.io/badge/Windows-0078D6?logo=windows&logoColor=white">

# DSS-Python: Extended bindings for an alternative implementation of EPRI's OpenDSS

Python bindings and misc tools for using our to [our customized/alternative implementation](https://github.com/dss-extensions/dss_capi) of [OpenDSS](http://smartgrid.epri.com/SimulationTool.aspx), AltDSS/DSS C-API library. OpenDSS is an open-source electric power distribution system simulator [distributed by EPRI](https://sourceforge.net/p/electricdss/). Based on DSS C-API, CFFI and NumPy, aiming for enhanced performance and full compatibility with the official COM object API on Windows, Linux and macOS. Support includes Intel-based (x86 and x64) processors, as well as ARM processors for Linux (including Raspberry Pi devices) and macOS (including Apple M1 and later).

More context about this project and its components (including alternatives in [Julia](https://dss-extensions.org/OpenDSSDirect.jl/latest/), [MATLAB](https://github.com/dss-extensions/dss_matlab/), C++, [C#/.NET](https://github.com/dss-extensions/dss_sharp/), [Go](https://github.com/dss-extensions/AltDSS-Go/), and [Rust](https://github.com/dss-extensions/AltDSS-Rust/)), please check [https://dss-extensions.org/](https://dss-extensions.org/) and our hub repository at [dss-extensions/dss-extensions](https://github.com/dss-extensions/dss-extensions) for more documentation, discussions and the [FAQ](https://dss-extensions.org/faq.html).

This package can be used as a companion to [OpenDSSDirect.py](http://github.com/dss-extensions/OpenDSSDirect.py/), if you don't need COM compatibility, or just would like to check its extra functionalities. Yet another alternative Python package is being developed in [AltDSS-Python](https://dss-extensions.org/AltDSS-Python/). The three packages can be used together, allowing the different API styles to be used in the same program.

While we plan to add a lot more functionality into DSS-Python, the main goal of creating a COM-compatible API has been reached in 2018. If you find an unexpected missing feature, please report it! Currently missing features that will be implemented eventually are interactive features and diakoptics (planned for a future version).

This module mimics the COM structure (as exposed via `win32com` or `comtypes`) — see [The DSS instance](https://dss-extensions.org/DSS-Python/#the-dss-instance) as well as [OpenDSS COM/classic APIs](https://dss-extensions.org/classic_api.html) for some docs — effectively enabling multi-platform compatibility at Python level. Compared to other options, it provides easier migration from code that uses the official OpenDSS through COM. See also [OpenDSS: Python APIs](https://dss-extensions.org/python_apis.html).
Most of the COM documentation can be used as-is, but instead of returning tuples or lists, this module returns/accepts NumPy arrays for numeric data exchange, which is usually preferred by the users. By toggle `DSS.AdvancedTypes`, complex numbers and matrices (shaped arrays) are also used to provide a more modern experience.

The module depends mostly on CFFI, NumPy, typing_extensions and, optionally, SciPy.Sparse for reading the sparse system admittance matrix. Pandas and matplotlib are optional dependencies [to enable plotting](https://github.com/dss-extensions/dss_python/blob/master/docs/examples/Plotting.ipynb) and other features.

## Release history

Check [the Releases page](https://github.com/dss-extensions/dss_python/releases) and [the changelog](https://github.com/dss-extensions/dss_python/blob/master/docs/changelog.md).

## Missing features and limitations

Most limitations are inherited from AltDSS/DSS C-API, i.e., these are not implemented:

- `DSSProgress` from `DLL/ImplDSSProgress.pas`: would need a reimplementation depending on the target UI (GUI, text, headless, etc.). Part of it can already be handled through the callback mechanisms.
- OpenDSS-GIS features are not implemented since they're not open-source.

In general, the DLL from `dss_capi` provides more features than both the official Direct DLL and the COM object.
    
## Extra features

Besides most of the COM methods, some of the unique DDLL methods are also exposed in adapted forms, namely the methods from `DYMatrix.pas`, especially `GetCompressedYMatrix` (check the source files for more information).

Since no GUI components are used in the FreePascal DLL, we map nearly all OpenDSS errors to Python exceptions, which seems a more natural way of working in Python. You can still manually trigger an error check by calling the function `_check_for_error()` from the main class or manually checking the `DSS.Error` interface.

For general engine features, see also: [What are some features from DSS-Extensions not available in EPRI’s OpenDSS?](https://dss-extensions.org/faq.html#what-are-some-features-from-dss-extensions-not-available-in-epris-opendss)

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

The compiled documentation is hosted at https://dss-extensions.org/DSS-Python

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

- More examples, especially for the extra features. There is a growing documentation hosted at [https://dss-extensions.org/Python/](https://dss-extensions.org/DSS-Python/) and [https://dss-extensions.org/docs.html](https://dss-extensions.org/docs.html); watch also https://github.com/dss-extensions/dss-extensions for more.
- Reports integrated in Python and interactive features on plots. Since most of the plot types from the official OpenDSS are optionally available since DSS-Python 0.14.2, advanced integration and interactive features are planned for a future feature.

Expect news about these items by version 1.0. 

While the base library (AltDSS/DSS C-API) will go through some API changes before v1.0, those do not affect usage from the Python side. This package has been API-stable for several years.

## Questions?

If you have any question, feel free to open a ticket on GitHub (here or at https://github.com/dss-extensions/dss-extensions), or contact directly me through email (pmeira at ieee.org). Please allow me a few days to respond.


## Credits / Acknowledgments

DSS-Python is based on EPRI's OpenDSS via the [`dss_capi`](http://github.com/dss-extensions/dss_capi/) project, so check its licensing information too.

This project is licensed under the (new) BSD, available in the `LICENSE` file. It's the same license OpenDSS uses (`OPENDSS_LICENSE`). OpenDSS itself uses KLUSolve and SuiteSparse, licensed under the GNU LGPL 2.1.

I thank my colleagues at the University of Campinas, Brazil, for providing feedback and helping me test this package during its inception in 2016-2017, as well as the many users and collaborators that have been using this or other DSS-Extensions since the public releases in 2018.
