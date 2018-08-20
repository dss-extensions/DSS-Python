# dss_python: Unofficial bindings for EPRI's OpenDSS

Python bindings and misc tools for using OpenDSS (EPRI Distribution System Simulator). Based on CFFI and `dss_capi`, aiming for full COM compatibility on Windows, Linux and MacOS.

<p align="center">
    <img alt="Overview of related repositories" src="https://raw.githubusercontent.com/PMeira/dss_python/master/docs/images/repomap.svg?sanitize=true" width=600>
</p>

If you are looking for the custom OpenDSS C-API library, see [`dss_capi`](http://github.com/PMeira/dss_capi/).

Version 0.10.0 (**unreleased**), based on OpenDSS revision 2246. For version 0.9.8, see [here](https://github.com/PMeira/dss_python/tree/0.9.8).
This is a work-in-progress but it's deemed stable enough to be made public. The main goal of creating a COM-compatible API was reached!

This module mimics the COM structure (as exposed via `win32com` or `comtypes`), effectively enabling multi-platform compatibility at Python level.
Most of the COM documentation can be used as-is, but instead of returning tuples or lists, this modules returns/accepts NumPy arrays for numeric data exchange. 

The module depends on CFFI, NumPy and, optionally, SciPy.Sparse for reading the sparse system admittance matrix.

If you are not bound to the COM API and its quirks, you might be insterested in OpenDSSDirect.py. [OpenDSSDirect.py](https://github.com/NREL/OpenDSSDirect.py/) exposes a more Pythonic API and contains extra utilities. Thanks to @kdheepak, OpenDSSDirect.py v0.3+ uses dss_python's backend -- this means you can use both modules at once. For example, if you have old code using the official COM objects, you could quickly switch to dss_python with very few code changes, and then use [`opendssdirect.utils`](https://nrel.github.io/OpenDSSDirect.py/opendssdirect.html#module-opendssdirect.utils) to generate some DataFrames.

## Recent changes

- version 0.10.0 **(WIP)**: Introduce a faster but less compatible module and add optional warnings for the traditional version (e.g. warn when using `DSS.activecircuit` instead of `DSS.ActiveCircuit`).
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

In general, the DLL from `dss_capi` provides more features than both the official Direct DLL and the COM object.
    
## Extra features

Besides most of the COM methods, some of the unique DDLL methods are also exposed in adapted forms, namely the methods from `DYMatrix.pas`, especially `GetCompressedYMatrix` (check the source files for more information).

Since no GUI components are used in the FreePascal DLL, we are experimenting with different ways of handling OpenDSS errors. Currently, the `DSS.Text.Command` call checks for OpenDSS errors (through the `DSS.Error` interface) and converts those to Python exceptions. Ideally every error should be converted to Python exceptions, but that could negatively impact performance. You can manually trigger an error check by calling the function `CheckForError()` from the main module.


## Installing

On all major platforms, you can install directly from pip:

```
pip install dss_python
```

Or, if you're using the Anaconda distribution, you can use:

```
conda install -c pmeira dss_python
```

Binary wheels are provided for all major platforms (Windows, Linux and MacOS) and many combinations of Python versions (2.7, 3.4 to 3.7). If you have issues with a specific version, please open an issue about it. Conda packages support at least Python 2.7, 3.5, 3.6 and 3.7.

After a successful installation, you can then import the `dss` module from your Python interpreter.

## Building

Get this repository:

```
    git clone https://github.com/PMeira/dss_python.git
```    
    
Assuming you successfully built or downloaded the `dss_capi` (check [its repository](http://github.com/PMeira/dss_capi/) for instructions), keep the folder organization as follows:

```
dss_capi/
dss_python/
electricdss-src/
```

Open a command prompt in the `dss_python` subfolder and run the build process:

```
python setup.py build
python setup.py install
```

Example usage
=============

If you were using `win32com` in code like:

```
import win32com.client 
dss_engine = win32com.client.Dispatch("OpenDSSEngine.DSS")
```

or `comtypes`:

```
import comtypes.client
dss_engine = comtypes.client.CreateObject("OpenDSSEngine.DSS")
```

you can replace that fragment with:
```
import dss
dss.use_com_compat()
dss_engine = dss.DSS
```

Assuming you have a DSS script named `master.dss`, you should be able to run it as shown below:

```
import dss
dss.use_com_compat()
dss_engine = dss.DSS

dss_engine.Text.Command = "compile c:/dss_files/master.dss"
dss_engine.ActiveCircuit.Solution.Solve()
voltages = dss_engine.ActiveCircuit.AllBusVolts

for i in range(len(voltages) // 2):
    print('node %d: %f + j%f' % (i, voltages[2*i], voltages[2*i + 1]))
```

If you do not need the mixed-cased handling, you can omit the call to `use_com_compat()` and use the casing used in this project.


If you want to play with the experimental OpenDSS-PM interface (from OpenDSS v8), it is installed side-by-side and you can import it as:

```
import dss.v8
dss.v8.use_com_compat()
dss_engine = dss.v8.DSS
```

*All validation tests succeed with `dss.v8` but beware those don't include parallel machine tests yet!*

Testing
=======
Since the DLL is built using the Free Pascal compiler, which is not officially supported by EPRI, the results are validated running sample networks provided in the official OpenDSS distribution. The only modifications are done directly by the script, removing interactive features and some minor other minor issues.

The validation scripts is `tests/validation.py` and requires the same folder structure as the building process. You need `win32com` to run it.

Currently, the following sample files from the official OpenDSS repository are used:

```
    Distrib/EPRITestCircuits/ckt5/Master_ckt5.dss
    Distrib/EPRITestCircuits/ckt7/Master_ckt7.dss
    Distrib/EPRITestCircuits/ckt24/Master_ckt24.dss
    Distrib/IEEETestCases/8500-Node/Master-unbal.dss
    Distrib/IEEETestCases/IEEE 30 Bus/Master.dss
    Distrib/IEEETestCases/NEVTestCase/NEVMASTER.DSS
    Distrib/IEEETestCases/37Bus/ieee37.dss
    Distrib/IEEETestCases/4Bus-DY-Bal/4Bus-DY-Bal.DSS
    Distrib/IEEETestCases/4Bus-GrdYD-Bal/4Bus-GrdYD-Bal.DSS
    Distrib/IEEETestCases/4Bus-OYOD-Bal/4Bus-OYOD-Bal.DSS
    Distrib/IEEETestCases/4Bus-OYOD-UnBal/4Bus-OYOD-UnBal.DSS
    Distrib/IEEETestCases/4Bus-YD-Bal/4Bus-YD-Bal.DSS
    Distrib/IEEETestCases/4Bus-YY-Bal/4Bus-YY-Bal.DSS
    Distrib/IEEETestCases/123Bus/IEEE123Master.dss
    Distrib/IEEETestCases/123Bus/SolarRamp.DSS
    Distrib/IEEETestCases/13Bus/IEEE13Nodeckt.dss
    Test/IEEE13_LineSpacing.dss
    Test/IEEE13_LineGeometry.dss
    Test/IEEE13_LineAndCableSpacing.dss
    Test/IEEE13_Assets.dss
    Test/CableParameters.dss
    Test/Cable_constants.DSS
    Test/BundleDemo.DSS
    Test/IEEE13_SpacingGeometry.dss
    Test/TextTsCable750MCM.dss
    Test/TestDDRegulator.dss
    Test/XYCurvetest.dss
    Test/PVSystemTestHarm.dss
    Test/TestAuto.dss
    Test/Stevenson.dss
    Test/YgD-Test.dss 
    Test/Master_TestCapInterface.DSS  
    Test/LoadTest.DSS
    Test/IEEELineGeometry.dss
    Test/ODRegTest.dss
    Test/MultiCircuitTest.DSS
    Test/TriplexLineCodeCalc.DSS
    Test/PVSystemTest-Duty.dss
    Test/PVSystemTest.dss 
    Test/REACTORTest.DSS
```

On Windows 10, remember to set the compatibility layer to Windows 7 (set the environment variable `__COMPAT_LAYER=WIN7RTM`), otherwise you may encounter issues with COM due to [ASLR](https://en.wikipedia.org/wiki/Address_space_layout_randomization) on Python 3.6+.

There is no validation on Linux yet since we cannot run the COM module there. The most likely solution will be to pickle the data on Windows and load them on Linux.

Roadmap
=======
Besides bug fixes, the main funcionality of this library is mostly done. Notable desirable features that may be implemented are:

- More and better documentation
- Besides providing binary wheels, create packages for the Anaconda stack with `conda-build`.

Questions?
==========
If you have any question, feel free to open a ticket on GitHub, or contact directly me through email (pmeira at ieee.org) or [Twitter](https://twitter.com/PCMMeira).
Please allow me a few days to respond.


Credits / Acknowlegement
========================
`dss_python` is based on EPRI's OpenDSS via the [`dss_capi`](http://github.com/PMeira/dss_capi/) project, check its licensing information.

This project is licensed under the (new) BSD, available in the `LICENSE` file. It's the same license OpenDSS uses (`OPENDSS_LICENSE`). OpenDSS itself uses KLUSolve and SuiteSparse, licensed under the GNU LGPL 2.1.

I thank my colleagues at the University of Campinas, Brazil, for providing feedback and helping me test this module.
