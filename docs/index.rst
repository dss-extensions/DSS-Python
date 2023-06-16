DSS-Python's API reference
==========================

.. toctree::
   :maxdepth: 1
   :caption: Contents:
   
   self
   dss
   obj
   Integrated plot commands <examples/Plotting>
   Export JSON data (WIP) <examples/JSON>
   User-models (PyIndMach012 example) <examples/UserModels/PyIndMach012/README>
   Changelog <changelog>


Brief introduction
------------------

DSS-Python uses CFFI and NumPy to expose the OpenDSS engine, as implemented in our alternative engine through DSS C-API
library from DSS-Extensions. This package is available for Windows, Linux and macOS, including Intel and ARM processes, 
both 32 and 64-bit. As such, it enables OpenDSS to run in many environments the official implementation cannot, 
from a Raspberry Pi to a HPC cluster, and cloud environments like Google Colab (some of our notebooks are ready-to-run
on Colab).

Install it with `pip` (or `pip3` depending on your environment), e.g.:

      pip install dss_python

In this documentation, since many features from DSS-Python are not available in the official version, we mark the extra
features as "**(API Extension)**". As such, the documentation could be somewhat useful for OpenDSS users stuck with the
COM version. As a reminder, we provide `patch_dss_com` to introduce some of the quality-of-life features such as Python
iterators and more to an `OpenDSSengine.DSS` COM object, in an effort to provide compatibility when users are either
migrating, validating results or just need to provide support for both the official engine and the DSS-Extensions
version. "**(API Extension)**" is used to mark whole classes, as seen below, or individual extra properties and
functions. Not all extensions are marked, so be sure to check when in doubt.

Independent of which OpenDSS implementation you use, it is good practice to list the specific implementation begin used
(e.g. from EPRI or from DSS-Extensions). At the moment we do not generate DOIs for our packages, but users can always
cite a specific version on PyPI, e.g. https://pypi.org/project/dss-python/0.12.1/

Check http://dss-extensions.org and https://github.com/dss-extensions/dss-extensions for links to more documentation
and examples. Besides our own documentation, the official OpenDSS documentation is extensive and covers various topics.
We recommend looking especially in the following resources:

   * https://sourceforge.net/p/electricdss/code/HEAD/tree/trunk/Version8/Distrib/Doc/
   * https://sourceforge.net/p/electricdss/code/HEAD/tree/trunk/Version8/Distrib/x64/OpenDSS_COM.chm?format=raw

See also https://dss-extensions.org/OpenDSSDirect.py/ for a package that uses function-style getters and setters, 
instead of Python properties, but reusing the base of this package. Most concepts presented here are shared and 
we avoid duplicating the effort. We envision a joint documentation site in the future.

Missing features and limitations
--------------------------------

Most limitations are inherited from `dss_capi`, i.e., these are not implemented:

- `DSSEvents` from `DLL/ImplEvents.pas`: seems too dependent on COM, we may implement it someday.
- `DSSProgress` from `DLL/ImplDSSProgress.pas`: would need a reimplementation depending on the target UI (GUI, text, headless, etc.). Can be achieved with the current API.
- OpenDSS-GIS features are not implemented since they're not open-source (nor free/openly available).

Extra features
--------------

In general, the `dss_capi` library from DSS-Extensions provides more features than both the official Direct DLL and the
COM object.

Besides most of the methods available in the OpenDSS COM DLL, some of the unique DDLL methods are also exposed in
adapted forms, namely the methods from `DYMatrix.pas`, especially `GetCompressedYMatrix` (check the source files for
more information).

While OpenDSS relies on windows/forms to report errors, or require the user to check the `Error` interface manually, most
DSS-Extensions do that automatically for the majority of the API calls. We also introduce extended error messages, more
thorough error checking in the Pascal code, and even some basic tracebacks for the .DSS script handling. All the changes
combined should result in a more comfortable and fluid experience for the Python user.

**TO BE EXPANDED**

The DSS instance
----------------

Although there are many classes and modules in DSS-Python, the main usage is typically
through the default DSS instance, and that is the most interest aspect for most users.

DSS-Python tries to be a drop-in replacement for the official OpenDSS COM implementation, within reasonable limits.
There are two main Python packages that allow instantiating COM objects, `win32com` and `comtypes`. 

For a quick look into some Python APIs (COM, DSS-Python, OpenDSSDirect.py) for the OpenDSS (official or our alternative 
implementation), see `DSS-Extensions — OpenDSS: Overview of Python APIs <https://dss-extensions.org/python_apis.html>`_.

Usually, your code would contain the instantiation of the objects such as:

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

Either way, to use DSS-Python, you can replace that fragment with:

.. code-block:: python

   from dss import DSS

If the code didn't depend on very specific details like lists vs tuples vs NumPy arrays, it should be compatible. Note
that even exchange `win32com` with `comtypes` already introduces small inconsistencies. These, though, should not
matter much in Python.

For a quick overview of DSS-Python, the main DSS class is organized as follows. Click through :class:`DSS <dss.IDSS.IDSS>`
to browse and discover other properties and methods, including many of the extensions we've been adding in the past 
several years.

* :class:`DSS.Parser <dss.IParser.IParser>`
* :class:`DSS.Text <dss.IText.IText>`
* :class:`DSS.YMatrix <dss.IYMatrix.IYMatrix>` **(API Extension)**
* :class:`DSS.ZIP <dss.IZIP.IZIP>` **(API Extension)**
* :doc:`DSS.Obj <obj>` (work in progress) **(API Extension)**
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
This was introduced in DSS-Python 0.12.0, after a lot of work in the underlying DSS C-API engine. This feature is also
unique to DSS-Extensions. 

Although multi-threading in Python is not great due to the the GIL (Global Interpreter Lock), it is important to note that
DSS-Python releases when API calls are made, i.e. multiple Python threads that spend most time in power flow solutions
should still be performant.

Check other DSS-Extensions for implementations of multi-threading using multiple DSS contexts in
other programming languages:
- `OpenDSSDirect.jl <https://github.com/dss-extensions/OpenDSSDirect.jl/blob/master/test/ctx_threads.jl>`_
- `dss.hpp <https://dss-extensions.org/dss_capi/>`_ 
- `DSS Sharp <https://dss-extensions.org/dss_sharp/>`_ 

If you are not comfortable with threads, we recommend using
Python's `multiprocessing <https://docs.python.org/3/library/multiprocessing.html>`_, especially for larger circuits. 
`multiprocessing` can be used with most OpenDSS implementations. We provide a 
`basic example here <https://sourceforge.net/p/electricdss/discussion/861976/thread/5703a79b3b/?limit=25#4dbf>`_
in the OpenDSS forum.

If you think threading is more suitable for your scenario, here's an example to illustrate some aspects. This example
is based on one of our tests. A real-life code would remove some of the text output from `print(...)`, but printing
some state transitions is useful to illustrate the process. Remember to watch your process manager or system monitor
to see the CPU usage too.

.. code-block:: python

    import threading, os
    from time import perf_counter
    import numpy as np
    from dss import dss

    # We need to allow each thread to operate independently, so the process
    # current working directory (CWD) cannot change. We disallow changing CWD
    # and track the current directory for each engine separately.
    # This will be the default in a future release.
    dss.AllowChangeDir = False

    # We usually don't want the editor popping up and/or interrupting this
    # kind of batch run
    dss.AllowEditor = False

    # Let's provide some circuits to run. Remember to adjust BASE_DIR
    BASE_DIR = './electricdss-tst'
    fns = [
        f"{BASE_DIR}/Version8/Distrib/EPRITestCircuits/epri_dpv/M1/Master_NoPV.dss",
        f"{BASE_DIR}/Version8/Distrib/EPRITestCircuits/epri_dpv/K1/Master_NoPV.dss",
        f"{BASE_DIR}/Version8/Distrib/EPRITestCircuits/epri_dpv/J1/Master_withPV.dss",
        f"{BASE_DIR}/Version8/Distrib/IEEETestCases/8500-Node/Master-unbal.dss",
        f"{BASE_DIR}/Version8/Distrib/IEEETestCases/NEVTestCase/NEVMASTER.DSS",
    ]

    # Assemble a list of all scenarios to run
    cases = []
    for fn in fns:
        for loadmult in (0.9, 0.95, 1.0, 1.05, 1.1):
            cases.append((fn, loadmult))

    # Let's make two copies of the scenarios, so we can run them sequentially, 
    # and again with threads.
    cases_to_run_threads = list(cases)
    cases_to_run_seq = list(cases)

    # Use the minimum between number of threads as CPU count and number of scenarios
    num = min(len(fns), os.cpu_count())

    # Initialize a new context for each of the threads
    ctxs = [dss.NewContext() for n in range(num)]
    print(f"Using {len(ctxs)} DSS contexts")

    # Some dicts for the results
    tresults = {}
    tconverged = {}
    sresults = {}
    sconverged = {}

    # This function will be run in the threads. Notice that it references some 
    # structures shared as input to the function. Since there is a GIL, we don't need
    # to use locks. You may need to adjust that for more general usage.
    def _run(ctx, case_list, converged, results):
        tname = threading.current_thread().name
        while case_list:
            fn, loadmult = case_list.pop()
            ctx.Text.Command = 'clear'
            try:
                ctx.Text.Command = f'redirect "{fn}"'
                ctx.ActiveCircuit.Solution.LoadMult = loadmult
                print(f'{tname}: Running "{fn}", circuit "{ctx.ActiveCircuit.Name}", mult={loadmult}')
                ctx.Text.Command = 'Solve mode=daily number=20'
            except Exception as ex:
                print('ERROR:', tname, (fn, loadmult))
                print('      ', ex.args)
            
            print(f'{tname}: Done "{fn}" (LoadMult={loadmult}), circuit "{ctx.ActiveCircuit.Name}"')
            converged[(fn, loadmult)] = ctx.ActiveCircuit.Solution.Converged
            results[(fn, loadmult)] = ctx.ActiveCircuit.AllBusVolts

    t0 = perf_counter()
    threads = []
    for ctx in ctxs:
        # The threads will consume input scenarios from `cases_to_run_threads`,
        # outputting to `tconverged` and `tresults`.
        t = threading.Thread(target=_run, args=(ctx, cases_to_run_threads, tconverged, tresults))
        threads.append(t)

    for t in threads:
        t.start()
        
    for t in threads:
        t.join()   

    t1 = perf_counter()

    # Check if all solutions converged
    assert all(tconverged.values())

    dt_thread = (t1 - t0)
    print(f'Done in {dt_thread:.3f} s with {num} threads')

    # Check with a sequential solution
    t0 = perf_counter()

    _run(dss, cases_to_run_seq, sconverged, sresults)

    t1 = perf_counter()
    dt_seq = (t1 - t0)
    print(f'Done in {dt_seq:.3f} s sequentially')

    # Check if each scenario has the same results whether ran in multiple threads or single thread
    for case in cases:
        np.testing.assert_equal(sresults[case], tresults[case])

    # Check if we actually got a lower time
    if len(ctxs) > 2:
        assert dt_thread < dt_seq

    print('Completed without errors')


More examples will be added when new interest uses of this feature are available.

Plotting and notebook integration
---------------------------------

Initial plotting support was added in DSS-Python v0.12.1, and an almost complete implementation is available since
v0.14.2. There are some features lacking in comparison to the official implementation (as of June 2023), especially
interactive inspection. 

To enable:

.. code-block:: python

   from dss import dss, plot
   plot.enable()


After that, running the plot commands from the text interface or compile/redirect scripts will try to use matplotlib to
reproduce most of the plot options from the official OpenDSS.

.. code-block:: python

   dss.Text.Command = 'compile some_circuit/Master.dss'
   dss.ActiveCircuit.Solution.Solve()
   dss.Text.Command = 'plot profile'


As a reminder, after activating, this can be used with `OpenDSSDirect.py <https://dss-extensions.org/OpenDSSDirect.py/>` too.

A notebook with an example gallery of various plot commands and how to customized the matplotlib output is available: :doc:`examples/Plotting`.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
