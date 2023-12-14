# NOTE: This file is used to test some of the extensions or more complex behaviors of 
#       the DSS engine and API state. The validation through compare_outputs.py
#       covers detailed check of API states, etc.
import sys, os, itertools, threading
from time import perf_counter
from math import sqrt, pi
try:
    from ._settings import BASE_DIR, ZIP_FN, WIN32
except ImportError:
    from _settings import BASE_DIR, ZIP_FN, WIN32

if WIN32:
    # When running pytest, the faulthandler seems to eager to grab FPC's exceptions, even when handled
    import faulthandler
    faulthandler.disable()
    import dss
    faulthandler.enable()
else:
    import dss

from dss import DSS, IDSS, DSSException, SparseSolverOptions, SolveModes, set_case_insensitive_attributes, DSSCompatFlags, LoadModels, DSSPropertyNameStyle
import numpy as np
import pytest


def setup_function():
    DSS.ClearAll()
    DSS.AllowEditor = False
    DSS.AdvancedTypes = False
    DSS.AllowChangeDir = True
    DSS.COMErrorResults = True # TODO: change to False
    DSS.CompatFlags = 0
    DSS.Error.UseExceptions = True
    DSS.Text.Command = 'set DefaultBaseFreq=60'

def test_zip_redirect():
    with pytest.raises(DSSException):
        DSS.ZIP.Redirect('13Bus/IEEE13Nodeckt.dss')

    DSS.ZIP.Close()
    DSS.ZIP.Open(ZIP_FN)
    DSS.ZIP.Redirect('13Bus/IEEE13Nodeckt.dss')
    DSS.ZIP.Close()
    assert DSS.ActiveCircuit.Name == 'ieee13nodeckt'
    assert DSS.ActiveCircuit.NumNodes == 41
    assert DSS.ActiveCircuit.NumBuses == 16


def test_zip_contains():
    with pytest.raises(DSSException):
        assert 'before open' in DSS.ZIP

    DSS.ZIP.Open(ZIP_FN)
    assert '13Bus/README.txt' in DSS.ZIP
    assert '13Bus/some/wrong/entry.txt' not in DSS.ZIP
    DSS.ZIP.Close()


def test_zip_exists():
    with pytest.raises(DSSException):
        DSS.ZIP.Open('something1/something2/something3.zip')

def test_zip_filelist():
    DSS.ZIP.Open(ZIP_FN)
    assert set(DSS.ZIP.List()) == {'13Bus/', '13Bus/IEEE13Node_BusXY.csv', '13Bus/IEEE13Nodeckt.dss', '13Bus/IEEELineCodes.DSS', '13Bus/README.txt'}
    assert DSS.ZIP.List('.*/RE.*') == ['13Bus/README.txt']


def test_zipv():
    DSS.Text.Command = 'clear'
    DSS.Text.Command = 'new circuit.test_circuit'
    DSS.Text.Command = 'new load.test_load'
    load = DSS.ActiveCircuit.Loads
    load.First
    
    with pytest.raises(DSSException):
        # Too few elements
        load.ZIPV = [1, 2, 3, 4]

    with pytest.raises(DSSException):
        # Too many elements
        load.ZIPV = [1, 2, 3, 4, 5, 6, 7, 8]

    load.ZIPV = [1, 0, 0, 1, 0, 0, 0.6]
    assert list(load.ZIPV) == [1, 0, 0, 1, 0, 0, 0.6]


def _run_mode(mode):
    DSS.Text.Command = f'redirect "{BASE_DIR}/Version8/Distrib/EPRITestCircuits/ckt7/Master_ckt7.dss"'
    DSS.ActiveCircuit.Solution.Mode = SolveModes.Daily
    DSS.YMatrix.SolverOptions = mode
    assert DSS.YMatrix.SolverOptions == mode
    DSS.ActiveCircuit.Solution.Number = 1
    DSS.ActiveCircuit.Solution.Solve()
    DSS.Text.Command = 'Set SampleEnergyMeters=NO'
    DSS.ActiveCircuit.Solution.Number = 300
    DSS.ActiveCircuit.Solution.Solve()
    return DSS.ActiveCircuit.AllBusVolts


def test_sparse_options():
    expected = _run_mode(SparseSolverOptions.ReuseNothing)
    for mode in [
        SparseSolverOptions.AlwaysResetYPrimInvalid,
        SparseSolverOptions.ReuseCompressedMatrix | SparseSolverOptions.AlwaysResetYPrimInvalid,
        SparseSolverOptions.ReuseCompressedMatrix,
        SparseSolverOptions.ReuseSymbolicFactorization | SparseSolverOptions.AlwaysResetYPrimInvalid,
        SparseSolverOptions.ReuseSymbolicFactorization,
        SparseSolverOptions.ReuseNumericFactorization | SparseSolverOptions.AlwaysResetYPrimInvalid,
        SparseSolverOptions.ReuseNumericFactorization,
    ]:
        np.testing.assert_allclose(expected, _run_mode(mode))


def test_pd_extras():
    DSS.Text.Command = f'redirect "{BASE_DIR}/Version8/Distrib/IEEETestCases/13Bus/IEEE13Nodeckt.dss"'
    DSS.ActiveCircuit.Solution.Solve()
    
    allPowers = []
    allSeqPowers = []
    allSeqCurrents = []
    allCplxSeqCurrents = []
    allCurrents = []

    DSS.ActiveCircuit.Settings.IterateDisabled = True
    e = DSS.ActiveCircuit.ActiveCktElement

    for pd in DSS.ActiveCircuit.PDElements:
        if e.Enabled:
            allPowers.extend(e.Powers)
            allSeqPowers.extend(e.SeqPowers)
            allSeqCurrents.extend(e.SeqCurrents)
            allCplxSeqCurrents.extend(e.CplxSeqCurrents)
            allCurrents.extend(e.Currents)

    np.testing.assert_equal(pd.AllPowers, allPowers)
    np.testing.assert_equal(pd.AllSeqPowers, allSeqPowers)
    np.testing.assert_equal(pd.AllSeqCurrents, allSeqCurrents)
    np.testing.assert_equal(pd.AllCplxSeqCurrents, allCplxSeqCurrents)
    np.testing.assert_equal(pd.AllCurrents, allCurrents)


def test_case_check():
    DSS.Text.Command = f'redirect "{BASE_DIR}/Version8/Distrib/IEEETestCases/13Bus/IEEE13Nodeckt.dss"'

    # Test if we get errors by default
    with pytest.raises(AttributeError):
        for l in DSS.ActiveCircuit.Loads:
            name = l.nAme

    # Test mixed case
    set_case_insensitive_attributes(True, False)
    for l in DSS.ActiveCircuit.Loads:
        name = l.namE

    # Test warnings
    set_case_insensitive_attributes(True, True)
    for l in DSS.ActiveCircuit.Loads:
        with pytest.warns(UserWarning):
            name = l.name

    for b in DSS.ActiveCircuit.Buses:
        with pytest.warns(UserWarning):
            voltages = b.PUVoltages

    # Make sure we can disable the case magic
    set_case_insensitive_attributes(False, False)
    with pytest.raises(AttributeError):
        for l in DSS.ActiveCircuit.Loads:
            name = l.name


def test_basic_ctx():
    prime_engine = DSS
    prime_engine.AllowChangeDir = False
    prime_engine.Text.Command = 'new circuit.test_prime'

    dss_engines = [prime_engine.NewContext() for _ in range(10)]
    for i, engine in enumerate(dss_engines, start=1):
        engine.Text.Command = f'new circuit.test{i}'

    for i, engine in enumerate(dss_engines, start=1):
        assert engine.ActiveCircuit.Name == f'test{i}'

    assert prime_engine.ActiveCircuit.Name == 'test_prime'


def test_compat_precision():
    DSS.ZIP.Open(ZIP_FN)
    DSS.ZIP.Redirect('13Bus/IEEE13Nodeckt.dss')
    DSS.ZIP.Close()

    DSS.ActiveCircuit.Vsources.First
    good = DSS.ActiveCircuit.ActiveCktElement.SeqVoltages.view(dtype=complex)
    DSS.CompatFlags = DSSCompatFlags.BadPrecision
    bad = DSS.ActiveCircuit.ActiveCktElement.SeqVoltages.view(dtype=complex)
    assert max(abs(good - bad)) > 1e-6


def test_compat_activeline():
    DSS.Text.Command = f'redirect "{BASE_DIR}/Version8/Distrib/IEEETestCases/13Bus/IEEE13Nodeckt.dss"'
    
    Lines = DSS.ActiveCircuit.Lines
    Lines.First
    Lines.Next
    Lines.Next
    name = Lines.Name

    DSS.ActiveCircuit.Loads.First
    
    assert name == Lines.Name

    DSS.CompatFlags = DSSCompatFlags.ActiveLine
    with pytest.raises(DSSException):
        assert name == Lines.Name


def test_set_mode():
    DSS.Text.Command = "new circuit.test"
    DSS.Text.Command = "solve"
    SM = SolveModes
    for s, m in [
        ('Snap', SM.SnapShot),
        ('Daily', SM.Daily),
        ('Yearly', SM.Yearly),
        ('M1', SM.Monte1),
        ('LD1', SM.LD1),
        ('PeakDay', SM.PeakDay),
        ('DutyCycle', SM.DutyCycle),
        ('Direct', SM.Direct),
        ('MF', SM.MonteFault),
        ('FaultStudy', SM.FaultStudy),
        ('M2', SM.Monte2),
        ('M3', SM.Monte3),
        ('LD2', SM.LD2),
        ('AutoAdd', SM.AutoAdd),
        ('Dynamic', SM.Dynamic),
        ('Harmonic', SM.Harmonic),
        ('Time', SM.Time),
        ('HarmonicT', SM.HarmonicT),
        ('Snapshot', SM.SnapShot),

        ('S', SM.SnapShot),
        ('Y', SM.Yearly),
        ('M1', SM.Monte1),
        ('LD1', SM.LD1),
        ('Peak', SM.PeakDay),
        ('Du', SM.DutyCycle),
        ('Di', SM.Direct),
        ('MF', SM.MonteFault),
        ('Fa', SM.FaultStudy),
        ('M2', SM.Monte2),
        ('M3', SM.Monte3),
        ('LD2', SM.LD2),
        ('Auto', SM.AutoAdd),
        ('Dyn', SM.Dynamic),
        ('Harm', SM.Harmonic),
        ('T', SM.Time),
        ('HarmonicT', SM.HarmonicT),
        ('Snaps', SM.SnapShot),

        ('Dynamics', SM.Dynamic),
        ('Harmonics', SM.Harmonic),
    ]:
        DSS.Text.Command = f"set mode={s}"
        result = SM(DSS.ActiveCircuit.Solution.Mode)
        assert result == m, (s, result, m)


def test_pm_threads():
    DSS.AllowChangeDir = False

    Parallel = DSS.ActiveCircuit.Parallel
    if Parallel.NumCPUs < 4:
        return # Cannot run in this machine, e.g. won't run on GitHub Actions

    DSS.AdvancedTypes = True

    DSS.Text.Command = 'set parallel=No'
    fn = os.path.abspath(f'{BASE_DIR}/Version8/Distrib/EPRITestCircuits/ckt5/Master_ckt5.dss')

    t0 = perf_counter()
    DSS.Text.Command = f'compile "{fn}"'
    DSS.ActiveCircuit.Solution.Solve()
    DSS.Text.Command = 'Clone 3'

    # Let's run 4 days in 4 actors
    Parallel.ActiveParallel = 1
    DSS.Text.Command = 'set activeActor=*'
    DSS.Text.Command = 'set mode=yearly number=144 hour=0 controlmode=off stepsize=600'

    DSS.Text.Command = 'set activeActor=1'
    DSS.Text.Command = 'set hour=0'

    DSS.Text.Command = 'set activeActor=2'
    DSS.Text.Command = 'set hour=24'

    DSS.Text.Command = 'set activeActor=3'
    DSS.Text.Command = 'set hour=48'

    DSS.Text.Command = 'set activeActor=4'
    DSS.Text.Command = 'set hour=72'

    DSS.ActiveCircuit.Solution.SolveAll()
    DSS.Text.Command = 'wait'
    
    assert tuple(Parallel.ActorStatus) == (1, 1, 1, 1)
    assert tuple(Parallel.ActorProgress) == (100, 100, 100, 100)
    t1 = perf_counter()
    dt_pm = t1 - t0

    v_pm = []
    Parallel.ActiveActor = 1
    v_pm.append(DSS.ActiveCircuit.AllBusVolts)
    Parallel.ActiveActor = 2
    v_pm.append(DSS.ActiveCircuit.AllBusVolts)
    Parallel.ActiveActor = 3
    v_pm.append(DSS.ActiveCircuit.AllBusVolts)
    Parallel.ActiveActor = 4
    v_pm.append(DSS.ActiveCircuit.AllBusVolts)

    # Now let's run the same thing sequentially for comparison
    DSS.Text.Command = 'set parallel=No'
    DSS.ClearAll()
    v_seq = []

    t0 = perf_counter()
    DSS.Text.Command = f'compile "{fn}"'
    DSS.ActiveCircuit.Solution.Solve()
    DSS.Text.Command = 'set mode=yearly number=144 hour=0 controlmode=off stepsize=600'
    DSS.ActiveCircuit.Solution.Solve()
    v_seq.append(DSS.ActiveCircuit.AllBusVolts)

    DSS.ActiveCircuit.Solution.Solve()
    v_seq.append(DSS.ActiveCircuit.AllBusVolts)

    DSS.ActiveCircuit.Solution.Solve()
    v_seq.append(DSS.ActiveCircuit.AllBusVolts)

    DSS.ActiveCircuit.Solution.Solve()
    v_seq.append(DSS.ActiveCircuit.AllBusVolts)
    t1 = perf_counter()
    dt_seq = t1 - t0

    np.testing.assert_allclose(v_pm[0], v_seq[0])
    np.testing.assert_allclose(v_pm[1], v_seq[1])
    np.testing.assert_allclose(v_pm[2], v_seq[2])
    np.testing.assert_allclose(v_pm[3], v_seq[3])
    assert max(abs(v_pm[3] - v_pm[0])) > 1e-1
    assert dt_pm < dt_seq

    # Let's run with threads, using DSSContexts too
    v_ctx = [None] * 4

    def _run(ctx, i):
        ctx.Text.Command = f'compile "{fn}"'
        ctx.ActiveCircuit.Solution.Solve()
        ctx.Text.Command = f'set mode=yearly number=144 hour={i * 24} controlmode=off stepsize=600'
        ctx.ActiveCircuit.Solution.Solve()
        v_ctx[i] = ctx.ActiveCircuit.AllBusVolts

    ctxs = [DSS.NewContext() for _ in range(4)]
    t0 = perf_counter()
    threads = []
    for i, ctx in enumerate(ctxs):
        t = threading.Thread(target=_run, args=(ctx, i))
        threads.append(t)

    for t in threads:
        t.start()
        
    for t in threads:
        t.join()
        
    t1 = perf_counter()
    dt_ctx = t1 - t0

    np.testing.assert_allclose(v_ctx[0], v_seq[0])
    np.testing.assert_allclose(v_ctx[1], v_seq[1])
    np.testing.assert_allclose(v_ctx[2], v_seq[2])
    np.testing.assert_allclose(v_ctx[3], v_seq[3])
    
    print(f"PM: {dt_pm:.3g} s; Python threads: {dt_ctx:.3g} s; Sequential: {dt_seq:.3g} s")


def test_threading2():
    DSS.AllowChangeDir = False

    fns = [
        f"{BASE_DIR}/Version8/Distrib/EPRITestCircuits/epri_dpv/M1/Master_NoPV.dss",
        f"{BASE_DIR}/Version8/Distrib/EPRITestCircuits/epri_dpv/K1/Master_NoPV.dss",
        f"{BASE_DIR}/Version8/Distrib/EPRITestCircuits/epri_dpv/J1/Master_withPV.dss",
        f"{BASE_DIR}/Version8/Distrib/IEEETestCases/8500-Node/Master-unbal.dss",
        f"{BASE_DIR}/Version8/Distrib/IEEETestCases/NEVTestCase/NEVMASTER.DSS",
    ]

    cases = []
    for fn in fns:
        for loadmult in (0.9, 0.95, 1.0, 1.05, 1.1):
            cases.append((fn, loadmult))

    cases_to_run_threads = list(cases)
    cases_to_run_seq = list(cases)

    # Use the number of threads as CPU count, number of files
    num = min(len(fns), os.cpu_count())

    # Initialize a new context for each of the threads
    ctxs = [DSS.NewContext() for n in range(num)]
    print(f"Using {len(ctxs)} DSS contexts")

    tresults = {}
    tconverged = {}
    sresults = {}
    sconverged = {}

    def _run(ctx: IDSS, case_list, converged, results):
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

    _run(DSS, cases_to_run_seq, sconverged, sresults)

    t1 = perf_counter()
    dt_seq = (t1 - t0)
    print(f'Done in {dt_seq:.3f} s sequentially')

    # Check if each scenario has the same results wheter ran in multiple threads or single thread
    for case in cases:
        np.testing.assert_equal(sresults[case], tresults[case])

    # Check if we actually got a lower time
    if len(ctxs) > 2:
        assert dt_thread < dt_seq


#TODO: finish/fix this for the current framework
# DSS C-API change: to avoid issues with read-only folders, we
# changed this from GetCurrentDir to OutputDirectory. This is 
# also more consistent with other functions
# def test_change_dir():
#     original_dir = os.path.normcase(os.getcwd())
#     subfolder = '37Bus'
#     master = 'ieee37.dss'
#     circ = 'ieee37'

#     for allow, redirect in itertools.product([False, True], [False, True]):
#         if redirect:
#             DSS.AllowChangeDir = True
            
#             # When file_dir is writtable
#             file_dir = os.path.normcase(os.path.abspath(f'Z:/dss/electricdss-tst/Version8/Distrib/IEEETestCases/{subfolder}'))
#             print(file_dir)
#             out_fn = f'{original_dir}/{circ}_SavedVoltages.Txt'
#             if os.path.isfile(out_fn):
#                 os.unlink(out_fn)
            
#             assert os.path.normcase(os.getcwd()) == original_dir
#             DSS.Text.Command = f'redirect "{file_dir}/{master}"'
#             assert os.path.normcase(os.getcwd()) == original_dir
#             DSS.Text.Command = 'save voltages'
#             assert os.path.normcase(os.getcwd()) == original_dir
#             assert os.path.exists(out_fn)
#             os.unlink(out_fn)
#             os.chdir(original_dir)

#             # When file_dir is not writtable:
#             # - OpenDSS COM will fail

#             file_dir = os.path.normcase(os.path.abspath(fr'c:\Program Files\OpenDSS\IEEETestCases\{subfolder}'))
#             out_fn = f'{original_dir}/{circ}_SavedVoltages.Txt'
#             print(file_dir)
#             print(os.path.normcase(os.getcwd()))
#             DSS.Text.Command = f'redirect "{file_dir}/{master}"'
            
            
#             print(os.path.normcase(os.getcwd()))
#             assert os.path.normcase(os.getcwd()) == original_dir
#             print(os.path.normcase(os.getcwd()))
            
#             # We can't save there, this should fail
#             failed = False
#             try:
#                 DSS.Text.Command = 'save voltages'
#             except:
#                 failed = True
                
#             assert not failed
            
#             print('DataPath is', os.path.normcase(os.path.abspath(DSS.DataPath)))
#             out_fn = DSS.Text.Result
#             assert os.path.normcase(os.path.dirname(os.path.abspath(out_fn))) != file_dir
            
#             print(out_fn)
#             assert os.path.normcase(os.getcwd()) == original_dir
#             assert os.path.isfile(out_fn)
#             os.unlink(out_fn)

#         elif allow:
#             DSS.AllowChangeDir = True
            
#             # When file_dir is writtable
#             file_dir = os.path.normcase(os.path.abspath(f'Z:/dss/electricdss-tst/Version8/Distrib/IEEETestCases/{subfolder}'))
#             print(file_dir)
#             out_fn = f'{file_dir}/{circ}_SavedVoltages.Txt'
#             if os.path.isfile(out_fn):
#                 os.unlink(out_fn)
            
#             assert os.path.normcase(os.getcwd()) == original_dir
#             DSS.Text.Command = f'compile "{file_dir}/{master}"'
#             assert os.path.normcase(os.getcwd()) == file_dir
#             DSS.Text.Command = 'save voltages'
#             assert os.path.normcase(os.getcwd()) == file_dir
#             assert os.path.exists(out_fn)
#             os.unlink(out_fn)
#             os.chdir(original_dir)

#             # When file_dir is not writtable:
#             # - OpenDSS COM will fail

#             file_dir = os.path.normcase(os.path.abspath(fr'c:\Program Files\OpenDSS\IEEETestCases\{subfolder}'))
#             out_fn = f'{file_dir}/{circ}_SavedVoltages.Txt'
#             print(file_dir)
#             print(os.path.normcase(os.getcwd()))
#             DSS.Text.Command = f'compile "{file_dir}/{master}"'
            
            
#             print(os.path.normcase(os.getcwd()))
#             assert os.path.normcase(os.getcwd()) == file_dir
#             print(os.path.normcase(os.getcwd()))
            
#             # We can't save there, this should fail
#             with pytest.raises(DSSException):
#                 DSS.Text.Command = 'save voltages'
                
#             print('DataPath is', os.path.normcase(os.path.abspath(DSS.DataPath)))
#             out_fn = DSS.Text.Result
#             assert os.path.normcase(os.path.dirname(os.path.abspath(out_fn))) != file_dir
            
#             print(out_fn)
#             assert os.path.normcase(os.getcwd()) == file_dir
#             assert os.path.isfile(out_fn)
#         else:
#             DSS.AllowChangeDir = False
#             file_dir = os.path.normcase(os.path.abspath(rf'Z:/dss/electricdss-tst/Version8/Distrib/IEEETestCases/{subfolder}'))
#             print(file_dir)
#             out_fn = f'{file_dir}/{circ}_SavedVoltages.Txt'
#             if os.path.isfile(out_fn):
#                 os.unlink(out_fn)
            
#             assert os.path.normcase(os.getcwd()) == original_dir
#             DSS.Text.Command = f'compile "{file_dir}/{master}"'
#             assert os.path.normcase(os.getcwd()) == original_dir
#             DSS.Text.Command = 'save voltages'
#             assert os.path.normcase(os.getcwd()) == original_dir
#             print(out_fn)
#             assert os.path.isfile(out_fn)
#             os.unlink(out_fn)
#             os.chdir(original_dir)

#             file_dir = os.path.normcase(os.path.abspath(rf'c:\Program Files\OpenDSS\IEEETestCases\{subfolder}'))
#             out_fn = f'{file_dir}/{circ}_SavedVoltages.Txt'
#             print(file_dir)
#             assert os.path.normcase(os.getcwd()) == original_dir
#             DSS.Text.Command = f'compile "{file_dir}/{master}"'
#             assert os.path.normcase(os.getcwd()) == original_dir
#             DSS.Text.Command = 'save voltages'
#             out_fn = DSS.Text.Result
#             print(DSS.DataPath)
#             print(out_fn)
#             assert os.path.normcase(os.getcwd()) == original_dir
#             assert os.path.isfile(out_fn)


def test_essentials(DSS: IDSS = DSS):
    Text = DSS.Text
    Text.Command = 'clear'
    Text.Command = 'new circuit.test789'
    Text.Command = 'new line.line1 bus=1 bus2=2'
    Text.Command = 'new line.line2 bus=2 bus2=3'
    assert DSS.ActiveCircuit.Name == 'test789'
    assert len(DSS.ActiveCircuit.ActiveBus) == 0
    Text.Command = 'MakeBusList'
    assert len(DSS.ActiveCircuit.ActiveBus) == 4
    for expected, b in zip(['sourcebus', '1', '2', '3'], DSS.ActiveCircuit.ActiveBus):
        assert expected == b.Name

def test_exception_control(DSS: IDSS = DSS):
    # Default behavior
    assert DSS.Error.UseExceptions
    with pytest.raises(DSSException):
        DSS.Text.Command = 'this_is_an_invalid_command1'

    # Behavior without exceptions
    DSS.Error.UseExceptions = False
    assert not DSS.Error.UseExceptions
    DSS.Text.Command = 'this_is_an_invalid_command2'
    # There should be an error code waiting for us...
    assert DSS.Error.Number != 0
    # ...but it should be gone after we read it
    assert DSS.Error.Number == 0


def debug_print(s):
    # print(s)
    pass

def test_capacitor_reactor(DSS: IDSS = DSS):
    from itertools import product
    kVA = 1329.53
    kV = 2.222
    DSS.AdvancedTypes = True

    for component, f in product(('Capacitor', 'Reactor'), (50, 60)):
        bus = 1
        sign = 1 if component[0] == 'C' else -1
        DSS.Text.Command = 'clear'
        debug_print('clear')
        DSS.Text.Command = f'set DefaultBaseFreq={f}'
        debug_print(DSS.Text.Command)
        DSS.Text.Command = f'new circuit.test{f} bus1={bus}'
        debug_print(DSS.Text.Command)
        for conn in ('delta', 'wye'):
            for phases0 in (1, 2, 3):
                phases = phases0
                if conn == 'wye':
                    V_eff_ln = kV * 1000
                    if phases == 1:
                        kV_eff = kV
                    else:
                        kV_eff = kV * sqrt(3)
                else:                    
                    V_eff_ll = kV * sqrt(3) * 1000
                    kV_eff = kV * sqrt(3)

                DSS.Text.Command = f'new Line.{bus}-{bus + 1} bus1={bus} bus2={bus + 1}'
                debug_print(DSS.Text.Command)
                bus += 1
                DSS.Text.Command = f'new {component}.{conn}_{phases} bus1={bus} phases={phases} conn={conn} kva={kVA} kV={kV_eff}'
                debug_print(DSS.Text.Command)
                DSS.Text.Command = 'solve'
                # debug_print(DSS.Text.Command)
                assert DSS.ActiveCircuit.ActiveCktElement.Name == f'{component}.{conn}_{phases}'
                Y_dss = DSS.ActiveCircuit.ActiveCktElement.Yprim

                DSS.Text.Command = f'new {component}.{conn}_{phases}_alt bus1={bus} phases=1 conn={conn} phases={phases} kva={kVA} kV={kV_eff}'
                # debug_print(DSS.Text.Command)
                DSS.Text.Command = 'solve'
                # debug_print(DSS.Text.Command)
                assert DSS.ActiveCircuit.ActiveCktElement.Name == f'{component}.{conn}_{phases}_alt'
                Y_dss2 = DSS.ActiveCircuit.ActiveCktElement.Yprim

                np.testing.assert_allclose(Y_dss, Y_dss2)

                if conn == 'wye':
                    VA_branch = 1000 * kVA / phases
                    y = sign * 1j * VA_branch / (V_eff_ln**2)
                    Y_py = np.zeros(shape=(phases * 2, phases * 2), dtype=complex)
                    for ph1 in range(phases):
                        ph2 = ph1 + phases
                        Y_py[ph1, ph1] += y
                        Y_py[ph2, ph2] += y
                        Y_py[ph2, ph1] += -y
                        Y_py[ph1, ph2] += -y

                    np.testing.assert_allclose(Y_py, Y_dss)
                elif conn == 'delta':
                    VA_branch = 1000 * kVA / phases
                    y = sign * 1j * VA_branch / (V_eff_ll**2)
                    if phases0 == 1:
                        branches = [(0, 1)]
                        phases = 2
                    elif phases0 == 2:
                        branches = [(0, 1), (1, 2)]
                        phases = 3
                    elif phases0 == 3:
                        branches = [(0, 1), (1, 2), (2, 0)]
                        phases = 3

                    Y_py = np.zeros(shape=(phases, phases), dtype=complex)
                    for ph1, ph2 in branches:
                        Y_py[ph1, ph1] += y
                        Y_py[ph2, ph2] += y
                        Y_py[ph2, ph1] += -y
                        Y_py[ph1, ph2] += -y

                    np.testing.assert_allclose(Y_py, Y_dss)

                phases = phases0
                model = int(LoadModels.ConstZ)
                DSS.Text.Command = f'new Line.{bus}-{bus + 1} bus1={bus} bus2={bus + 1}'
                debug_print(DSS.Text.Command)
                bus += 1
                DSS.Text.Command = f'new Load.{conn}_{phases} bus1={bus} phases={phases} conn={conn} kw=0 kvar={-sign * kVA} kV={kV_eff} model={model} Xneut=0 Rneut=0'
                debug_print(DSS.Text.Command)
                DSS.Text.Command = 'solve'
                # debug_print(DSS.Text.Command)
                assert DSS.ActiveCircuit.ActiveCktElement.Name == f'Load.{conn}_{phases}'
                Y_load = DSS.ActiveCircuit.ActiveCktElement.Yprim
                Y_load -= Y_load.real
                if conn == 'wye':
                    n = Y_load.shape[0] # wye load is 1 terminal
                    Y_py2 = np.copy(Y_py[:n, :n])
                    Y_py2[:, n - 1] += np.sum(Y_py[:n, n:], axis=1)
                    Y_py2[n - 1, :] += np.sum(Y_py[n:, :n], axis=0)
                    Y_py2[n - 1, n - 1] += np.sum(np.diag(Y_py)[n:])
                    Y_py = Y_py2
                else:
                    n = Y_load.shape[0]
                
                np.testing.assert_allclose(Y_py[:n, :n], Y_load[:n, :n], atol=1e-6)


def test_patch_comtypes():
    if WIN32:
        import comtypes.client
        DSS_COM = dss.patch_dss_com(comtypes.client.CreateObject("OpenDSSengine.DSS"))
        test_essentials(DSS_COM)

def test_patch_win32com():
    if WIN32:
        import win32com.client
        win32com.client.Dispatch("OpenDSSengine.DSS")
        DSS_COM = dss.patch_dss_com(win32com.client.gencache.EnsureDispatch("OpenDSSengine.DSS"))
        test_essentials(DSS_COM)

def test_namingstyle():
    DSS.ClearAll()
    DSS('new circuit.test')
    DSS.ActiveCircuit.Vsources.First

    # check only the first 7 elements
    modern7 = ['Bus1', 'BasekV', 'pu', 'Angle', 'Frequency', 'Phases', 'MVASC3']
    lower7 = [x.lower() for x in modern7]
    legacy7 = ['bus1', 'basekv', 'pu', 'angle', 'frequency', 'phases', 'MVAsc3']

    assert modern7 == DSS.ActiveCircuit.ActiveElement.AllPropertyNames[:7]
    
    DSS.ActiveCircuit.Settings.SetPropertyNameStyle(DSSPropertyNameStyle.Legacy)
    assert legacy7 == DSS.ActiveCircuit.ActiveElement.AllPropertyNames[:7]

    DSS.ActiveCircuit.Settings.SetPropertyNameStyle(DSSPropertyNameStyle.Lowercase)
    assert lower7 == DSS.ActiveCircuit.ActiveElement.AllPropertyNames[:7]

    DSS.ActiveCircuit.Settings.SetPropertyNameStyle(DSSPropertyNameStyle.Modern)

if __name__ == '__main__':
    # for _ in range(250):
    #     test_pm_threads()
    test_capacitor_reactor()