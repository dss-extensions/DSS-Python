# NOTE: This file is used to test some of the extensions or more complex behaviors of 
#       the DSS engine and API state. The validation through compare_outputs.py
#       covers detailed check of API states, etc.
import sys, os, itertools, threading
from time import perf_counter
import dss
from dss import DSS, IDSS, DSSException, SparseSolverOptions, SolveModes, set_case_insensitive_attributes
import numpy as np
import pytest

WIN32 = (sys.platform == 'win32')
DSS.AllowEditor = False
if os.path.exists('../../electricdss-tst/'):
    BASE_DIR = os.path.abspath('../../electricdss-tst/')
    ZIP_FN = os.path.abspath('data/13Bus.zip')
else:
    BASE_DIR = os.path.abspath('../electricdss-tst/')
    ZIP_FN = os.path.abspath('tests/data/13Bus.zip')

assert os.path.exists(BASE_DIR)

def setup_function():
    DSS.ClearAll()
    DSS.AdvancedTypes = False
    DSS.AllowChangeDir = True
    DSS.COMErrorResults = True # TODO: change to False


def test_zip_redirect():
    DSS.ZIP.Open(ZIP_FN)
    DSS.ZIP.Redirect('13Bus/IEEE13Nodeckt.dss')
    DSS.ZIP.Close()
    assert DSS.ActiveCircuit.Name == 'ieee13nodeckt'
    assert DSS.ActiveCircuit.NumNodes == 41
    assert DSS.ActiveCircuit.NumBuses == 16


def test_zip_contains():
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
    DSS.Text.Command = f'redirect "${BASE_DIR}/Version8/Distrib/EPRITestCircuits/ckt7/Master_ckt7.dss"'
    DSS.ActiveCircuit.Solution.Mode = SolveModes.Daily
    DSS.YMatrix.SolverOptions = mode
    assert DSS.YMatrix.SolverOptions == mode
    DSS.ActiveCircuit.Solution.Number = 1
    DSS.ActiveCircuit.Solution.Solve()
    DSS.Text.Command = 'Set SampleEnergyMeters=NO'
    DSS.ActiveCircuit.Solution.Number = 300
    DSS.ActiveCircuit.Solution.Solve()
    return DSS.ActiveCircuit.AllBusVolts


def xtest_sparse_options():
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
    DSS.AllowChangeDir = False

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
    assert len(DSS.ActiveCircuit.Buses) == 0
    Text.Command = 'MakeBusList'
    assert len(DSS.ActiveCircuit.Buses) == 4
    for expected, b in zip(['sourcebus', '1', '2', '3'], DSS.ActiveCircuit.Buses):
        assert expected == b.Name

if WIN32:
    def test_patch_comtypes():
        import comtypes.client
        DSS_COM = dss.patch_dss_com(comtypes.client.CreateObject("OpenDSSengine.DSS"))
        test_essentials(DSS_COM)

    def test_patch_comtypes():
        import win32com.client
        DSS_COM = dss.patch_dss_com(win32com.client.Dispatch("OpenDSSengine.DSS"))
        test_essentials(DSS_COM)
