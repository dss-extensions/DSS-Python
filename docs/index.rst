DSS Python's API reference
==========================

.. toctree::
   :maxdepth: 3
   :caption: Contents:
   
   dss
   obj

Brief introduction
------------------

DSS Python uses CFFI and NumPy to expose the OpenDSS engine, as implemented in the (unofficial) DSS C-API library from
DSS Extensions. This package is available for Windows, Linux and macOS, including Intel and ARM processes, both 32 and
64-bit. As such, it enables OpenDSS to run in many environments the official implementation cannot, from a RaspBerry Pi
to a HPC cluster, and cloud environments like Google Colab.

Install it with `pip` (or `pip3` depending on your environment), e.g.:

      pip install dss_python

In this documentation, since many features from DSS Python are not available in the official version, we mark the extra
features as "**(API Extension)**". As such, the documentation could be somewhat useful for OpenDSS users stuck with the
COM version. As a reminder, we provide `patch_dss_com` to introduce some of the quality-of-life features such as Python
iterators and more to an `OpenDSSengine.DSS` COM object, in an effort to provide compatibility when users are either
migrating, validating results or just need to provide support for both the official engine and the DSS Extensions
version. "**(API Extension)**" is used to mark whole classes, as seen below, or individual extra properties and
functions. Not all extensions are marked, so be sure to check when in doubt.

Independent of which OpenDSS implementation you use, it is good practice to list the specific implementation begin used
(e.g. from EPRI or from DSS Extensions). At the moment we do not generate DOIs for our packages, but users can always
cite a specific version on PyPI, e.g. https://pypi.org/project/dss-python/0.12.1/

Check http://dss-extensions.org and https://github.com/dss-extensions/dss-extensions for links to more documentation
and examples. Besides our own documentation, the official OpenDSS documentation is extensive and covers various topics.
We recommend looking especially in the following resources:

   * https://sourceforge.net/p/electricdss/code/HEAD/tree/trunk/Version8/Distrib/Doc/
   * https://sourceforge.net/p/electricdss/code/HEAD/tree/trunk/Version8/Distrib/x64/OpenDSS_COM.chm?format=raw

See also https://dss-extensions.org/OpenDSSDirect.py/ for a package that uses function-style getters and setters, instead
of Python properties, but reusing the base of this package.

Missing features and limitations
--------------------------------

Most limitations are inherited from `dss_capi`, i.e., these are not implemented:

- `DSSEvents` from `DLL/ImplEvents.pas`: seems too dependent on COM.
- `DSSProgress` from `DLL/ImplDSSProgress.pas`: would need a reimplementation depending on the target UI (GUI, text, headless, etc.).
- OpenDSS-GIS features are not implemented since they're not open-source.

Extra features
--------------

In general, the `dss_capi` library from DSS Extensions provides more features than both the official Direct DLL and the
COM object.

Besides most of the methods available in the OpenDSS COM DLL, some of the unique DDLL methods are also exposed in
adapted forms, namely the methods from `DYMatrix.pas`, especially `GetCompressedYMatrix` (check the source files for
more information).

While OpenDSS relies on windows/forms to report errors, or require the user to check the Error interface manually, most
DSS Extensions do that automatically for the majority of the API calls. We also introduce extended error messages, more
thorough error checking in the Pascal code, and even some basic tracebacks for the .DSS script handling. All the changes
combined should result in a more comfortale and fluid experience for the Python user.

**TO BE EXPANDED**

The DSS instance
----------------

Although there are many classes and modules in DSS Python, the main usage is typically
through the default DSS instance, and that is the most interest aspect for most users.

DSS Python tries to be a drop-in replacement for the official OpenDSS COM implementation, within reasonable limits.
There are two main Python packages that allow instantiating COM objects, `win32com` and `comtypes`. Usually, your
code would contain the instantiation of the objects such as:

.. code-block:: python

   import win32com.client 
   DSS = win32com.client.gencache.EnsureDispatch("OpenDSSEngine.DSS")

or maybe:

.. code-block:: python

   import win32com.client 
   DSS = win32com.client.Dispatch("OpenDSSEngine.DSS")

or with `comtypes`:

.. code-block:: python

   import comtypes.client
   DSS = comtypes.client.CreateObject("OpenDSSEngine.DSS")

Either way, to use DSS Python, you can replace that fragment with:

.. code-block:: python

   from dss import DSS

If the code didn't depend on very specific details like lists vs tuples vs NumPy arrays, it should be compatible. Note
that even exchange `win32com` with `comtypes` already introduces small inconsistencies. These, though, should not
matter much in Python.

For a quick overview of DSS Python, the main DSS class is organized as follows. Click through :class:`DSS <dss.IDSS.IDSS>`
to browse and discover other properties and methods, including many of the extensions we've been adding in the past 
several years.

* :class:`DSS.Parser <dss.IParser.IParser>`
* :class:`DSS.Text <dss.IText.IText>`
* :class:`DSS.YMatrix <dss.IYMatrix.IYMatrix>` **(API Extension)**
* :class:`DSS.ZIP <dss.IZIP.IZIP>` **(API Extension)**
* :ref:`DSS.Obj` (work in progress) **(API Extension)**
* :class:`DSS.ActiveCircuit <dss.ICircuit.ICircuit>`:

    * :class:`DSS.ActiveCircuit.ActiveBus <dss.IBus.IBus>`
    * :class:`DSS.ActiveCircuit.ActiveCktElement <dss.ICktElement.ICktElement>`
    * :class:`DSS.ActiveCircuit.ActiveClass <dss.IActiveClass.IActiveClass>`
    * :class:`DSS.ActiveCircuit.ActiveDSSElement <dss.IDSSElement.IDSSElement>`
    * :class:`DSS.ActiveCircuit.ActiveElement <dss.ICktElement.ICktElement>`
    * :class:`DSS.ActiveCircuit.Buses <dss.IBus.IBus>`
    * :class:`DSS.ActiveCircuit.Capacitors <dss.ICapacitors.ICapacitors>`
    * :class:`DSS.ActiveCircuit.CapControls <dss.ICapControls.ICapControls>`
    * :class:`DSS.ActiveCircuit.CNData <dss.ICNData.ICNData>` **(API Extension)**
    * :class:`DSS.ActiveCircuit.CtrlQueue <dss.ICtrlQueue.ICtrlQueue>`
    * :class:`DSS.ActiveCircuit.DSSim_Coms <dss.IDSSimComs.IDSSimComs>`
    * :class:`DSS.ActiveCircuit.Fuses <dss.IFuses.IFuses>`
    * :class:`DSS.ActiveCircuit.Generators <dss.IGenerators.IGenerators>`
    * :class:`DSS.ActiveCircuit.GICSources <dss.IGICSources.IGICSources>`
    * :class:`DSS.ActiveCircuit.ISources <dss.IISources.IISources>`
    * :class:`DSS.ActiveCircuit.LineCodes <dss.ILineCodes.ILineCodes>`
    * :class:`DSS.ActiveCircuit.LineGeometries <dss.ILineGeometries.ILineGeometries>` **(API Extension)**
    * :class:`DSS.ActiveCircuit.Lines <dss.ILines.ILines>`
    * :class:`DSS.ActiveCircuit.LineSpacings <dss.ILineSpacings.ILineSpacings>` **(API Extension)**
    * :class:`DSS.ActiveCircuit.Loads <dss.ILoads.ILoads>`
    * :class:`DSS.ActiveCircuit.LoadShapes <dss.ILoadShapes.ILoadShapes>`
    * :class:`DSS.ActiveCircuit.Meters <dss.IMeters.IMeters>`
    * :class:`DSS.ActiveCircuit.Monitors <dss.IMonitors.IMonitors>`
    * :class:`DSS.ActiveCircuit.Parallel <dss.IParallel.IParallel>`
    * :class:`DSS.ActiveCircuit.PDElements <dss.IPDElements.IPDElements>`
    * :class:`DSS.ActiveCircuit.PVSystems <dss.IPVSystems.IPVSystems>`
    * :class:`DSS.ActiveCircuit.Reactors <dss.IReactors.IReactors>` **(API Extension)**
    * :class:`DSS.ActiveCircuit.Reclosers <dss.IReclosers.IReclosers>`
    * :class:`DSS.ActiveCircuit.ReduceCkt <dss.IReduceCkt.IReduceCkt>`
    * :class:`DSS.ActiveCircuit.RegControls <dss.IRegControls.IRegControls>`
    * :class:`DSS.ActiveCircuit.Relays <dss.IRelays.IRelays>`
    * :class:`DSS.ActiveCircuit.Sensors <dss.ISensors.ISensors>`
    * :class:`DSS.ActiveCircuit.Settings <dss.ISettings.ISettings>`
    * :class:`DSS.ActiveCircuit.Solution <dss.ISolution.ISolution>`
    * :class:`DSS.ActiveCircuit.Storages <dss.IStorages.IStorages>`
    * :class:`DSS.ActiveCircuit.SwtControls <dss.ISwtControls.ISwtControls>`
    * :class:`DSS.ActiveCircuit.Topology <dss.ITopology.ITopology>`
    * :class:`DSS.ActiveCircuit.Transformers <dss.ITransformers.ITransformers>`
    * :class:`DSS.ActiveCircuit.TSData <dss.ITSData.ITSData>` **(API Extension)**
    * :class:`DSS.ActiveCircuit.Vsources <dss.IVsources.IVsources>`
    * :class:`DSS.ActiveCircuit.WireData <dss.IWireData.IWireData>` **(API Extension)**
    * :class:`DSS.ActiveCircuit.XYCurves <dss.IXYCurves.IXYCurves>`


Multiple OpenDSS instances
--------------------------

If you need to create multiple, independent OpenDSS engines, :class:`DSS.NewContext() <dss.IDSS.IDSS.NewContext>` can be used.
This was introduced in DSS Python 0.12.0, after a lot of work in the underlying DSS C-API engine. This feature is also
unique to DSS Extensions. 

Although multi-threading in Python is not great to the the GIL (Global Interpreter Lock), it is important to note that
DSS Python releases when API calls are made, i.e. multiple Python threads that spend most time in power flow solutions
should still be performant.

Check other DSS Extensions such as `dss.hpp <https://dss-extensions.org/dss_capi/>`_ and `DSS
Sharp <https://dss-extensions.org/dss_sharp/>`_ for implementation of multi-threading using multiple DSS contexts in
other programming languages.


Plotting and notebook integration
---------------------------------

Initial but incomplete plotting support was added in DSS Python v0.12.1.

To enable:

.. code-block:: python

   from dss import DSS, plot
   plot.enable()


After that, running the plot commands from the text interface or compile/redirect scripts will try to use matplotlib to
reproduce most of the plot options from the official OpenDSS.

.. code-block:: python

   DSS.Text.Command = 'compile some_circuit/Master.dss'
   DSS.ActiveCircuit.Solution.Solve()
   DSS.Text.Command = 'plot profile'


**TO BE EXPANDED**

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
