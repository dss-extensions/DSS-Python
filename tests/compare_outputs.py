import json, os
from inspect import getdoc
from collections import defaultdict
from zipfile import ZipFile, BadZipFile
import numpy as np
from pprint import pprint
from dss import ICircuit, IDSS

np.set_printoptions(linewidth=300)

BAD_PI = 3.14159265359 # from OpenDSS source code
BAD_RAD_TO_DEG = 57.29577951

class MISSING:
    pass

tol = 1e-5

VERBOSE = False

KNOWN_COM_DIFF = set([
    # On official COM, uninitialized values for CalcCurrent, AllocFactors
    # Note that this could be a bug on the upstream version, but debugging without Delphi gets tricky
    *[('Version8/Distrib/Examples/DOCTechNote/1_2.dss.json', 'Meters', 'records', x, 'CalcCurrent') for x in range(77)],
    *[('Version8/Distrib/Examples/DOCTechNote/2_1.dss.json', 'Meters', 'records', x, 'CalcCurrent') for x in range(77)],
    *[('Version8/Distrib/Examples/DOCTechNote/2_2.dss.json', 'Meters', 'records', x, 'CalcCurrent') for x in range(77)],
    *[('Version8/Distrib/Examples/DOCTechNote/1_2.dss.json', 'Meters', 'records', x, 'AllocFactors') for x in range(77)],
    *[('Version8/Distrib/Examples/DOCTechNote/2_1.dss.json', 'Meters', 'records', x, 'AllocFactors') for x in range(77)],
    *[('Version8/Distrib/Examples/DOCTechNote/2_2.dss.json', 'Meters', 'records', x, 'AllocFactors') for x in range(77)],
    ('Version8/Distrib/IEEETestCases/123Bus/SolarRamp.DSS.json', 'Meters', 'records', 0, 'AllocFactors'),
    ('Version8/Distrib/IEEETestCases/SecondaryTestCircuit_modified/Master.DSS.json', 'Meters', 'records', 0, 'AllocFactors'),
    ('Version8/Distrib/Examples/Microgrid/GridFormingInverter/GFM_IEEE123/Run_IEEE123Bus_GFMSnap-A.DSS.json', 'Meters', 'records', 0, 'AllocFactors'),
    ('Version8/Distrib/Examples/Microgrid/GridFormingInverter/GFM_IEEE123/Run_IEEE123Bus_GFMSnap-C.DSS.json', 'Meters', 'records', 0, 'AllocFactors'),
    ('Version8/Distrib/Examples/Microgrid/GridFormingInverter/GFM_IEEE123/Run_IEEE123Bus_GFMWholeDaily.DSS.json', 'Meters', 'records', 0, 'AllocFactors'),
    ('Version8/Distrib/Examples/Scripts/IEEE-TIA-LV Model/master_large_1phase.dss.json', 'Meters', 'records', 0, 'CalcCurrent'),
    ('Version8/Distrib/Examples/Scripts/IEEE-TIA-LV Model/master_small_1phase.dss.json', 'Meters', 'records', 0, 'CalcCurrent'),
    ('Version8/Distrib/Examples/Microgrid/GridFormingInverter/GFM_IEEE123/Run_IEEE123Bus_GFMWholeDaily.DSS.json', 'Meters', 'records', 0, 'AllocFactors'),
    ('Version8/Distrib/Examples/Microgrid/GridFormingInverter/GFM_IEEE123/Run_IEEE123Bus_GFMSnap-A.DSS.json', 'Meters', 'records', 0, 'AllocFactors'),
    ('Version8/Distrib/Examples/Microgrid/GridFormingInverter/GFM_IEEE123/Run_IEEE123Bus_GFMSnap-B.DSS.json', 'Meters', 'records', 0, 'AllocFactors'),
    ('Version8/Distrib/Examples/Microgrid/GridFormingInverter/GFM_IEEE123/Run_IEEE123Bus_GFMSnap-C.DSS.json', 'Meters', 'records', 0, 'AllocFactors'),
    ('Version8/Distrib/Examples/IBRDynamics_Cases/GFM_IEEE123/Run_IEEE123Bus_GFMDaily.DSS.json', 'Meters', 'records', 0, 'AllocFactors'),
    ('Version8/Distrib/Examples/IBRDynamics_Cases/GFL_IEEE123/Run_IEEE123Bus_GFLDaily.DSS.json', 'Meters', 'records', 0, 'AllocFactors'),

    # Close enough for the system, especially since everything else matches
    # Some of these are due to tiny line segments, others various sources
    ('Test/AutoTrans/Auto3bus.dss.json', 'Lines', 'records', 1, 'ActiveCktElement', 'Residuals'),
    ('Test/AutoTrans/AutoHLT.dss.json', 'Lines', 'records', 0, 'ActiveCktElement', 'Residuals'),
    ('Version8/Distrib/Examples/InverterModels/PVSystem/InvControl/VV_VW/Daily_VVVW_varMax_PMPPPU_kVAlimitation_Qpriority-2.dss.json', 'PVSystems', 'records', 0, 'RegisterValues'),
    ('Version8/Distrib/EPRITestCircuits/epri_dpv/M1/Master_NoPV.dss.json', 'Lines', 'records', 235, 'ActiveCktElement', 'Losses'),
    ('Version8/Distrib/EPRITestCircuits/epri_dpv/M1/Master_NoPV.dss.json', 'Lines', 'records', 332, 'ActiveCktElement', 'Losses'),
    ('Version8/Distrib/EPRITestCircuits/epri_dpv/M1/Master_NoPV.dss.json', 'Lines', 'records', 395, 'ActiveCktElement', 'Losses'),
    ('Version8/Distrib/EPRITestCircuits/epri_dpv/M1/Master_NoPV.dss.json', 'Lines', 'records', 398, 'ActiveCktElement', 'Losses'),
    ('Version8/Distrib/IEEETestCases/SecondaryTestCircuit_modified/Master.DSS.json', 'Lines', 'records', 0, 'ActiveCktElement', 'Currents'),
    ('Version8/Distrib/IEEETestCases/SecondaryTestCircuit_modified/Master.DSS.json', 'Lines', 'records', 0, 'ActiveCktElement', 'SeqCurrents'),
    ('Version8/Distrib/IEEETestCases/SecondaryTestCircuit_modified/Master.DSS.json', 'Lines', 'records', 0, 'ActiveCktElement', 'CplxSeqCurrents'),
    ('Version8/Distrib/IEEETestCases/SecondaryTestCircuit_modified/Master.DSS.json', 'Lines', 'records', 0, 'ActiveCktElement', 'Powers'),
    ('Version8/Distrib/IEEETestCases/SecondaryTestCircuit_modified/Master.DSS.json', 'Lines', 'records', 0, 'ActiveCktElement', 'CurrentsMagAng'),
    ('Version8/Distrib/IEEETestCases/SecondaryTestCircuit_modified/Master.DSS.json', 'Lines', 'records', 0, 'ActiveCktElement', 'Residuals'),
    ('Version8/Distrib/EPRITestCircuits/ckt5/Master_ckt5.dss.json', 'Lines', 'records', 99, 'ActiveCktElement', 'Powers'),
    ('Version8/Distrib/EPRITestCircuits/ckt5/Master_ckt5.dss.json', 'Lines', 'records', 109, 'ActiveCktElement', 'Powers'),
    ('Version8/Distrib/EPRITestCircuits/ckt5/Master_ckt5.dss.json', 'Lines', 'records', 708, 'ActiveCktElement', 'Powers'),
    ('Version8/Distrib/EPRITestCircuits/ckt7/Master_ckt7.dss.json', 'Lines', 'records', 164, 'ActiveCktElement', 'Losses'),
    ('Version8/Distrib/EPRITestCircuits/ckt7/Master_ckt7.dss.json', 'Lines', 'records', 245, 'ActiveCktElement', 'Losses'),
    ('Version8/Distrib/EPRITestCircuits/ckt7/Master_ckt7.dss.json', 'Lines', 'records', 262, 'ActiveCktElement', 'Losses'),
    ('Version8/Distrib/EPRITestCircuits/ckt24/master_ckt24.dss.json', 'Lines', 'records', 487, 'ActiveCktElement', 'Losses'),
    ('Version8/Distrib/EPRITestCircuits/ckt24/master_ckt24.dss.json', 'Lines', 'records', 5221, 'ActiveCktElement', 'PhaseLosses'),
    ('Version8/Distrib/EPRITestCircuits/ckt24/master_ckt24.dss.json', 'Lines', 'records', 5221, 'ActiveCktElement', 'Losses'),
    ('Version8/Distrib/Examples/StorageControllerTechNote/LoadShape/LoadShapeRun.dss.json', 'Lines', 'records', 2029, 'ActiveCktElement', 'Losses'),
    ('Version8/Distrib/Examples/StorageControllerTechNote/PeakShave/PeakShaveMonPhaseRun.dss.json', 'Lines', 'records', 2029, 'ActiveCktElement', 'Losses'),
    ('Version8/Distrib/Examples/StorageControllerTechNote/PeakShaveDch_PeakShaveLow_Ch/PeakShaveDch_PeakShaveLow_ChRun.dss.json', 'Lines', 'records', 2029, 'ActiveCktElement', 'Losses'),
    ('Version8/Distrib/Examples/StorageControllerTechNote/Support/SupportRun.dss.json', 'Lines', 'records', 2029, 'ActiveCktElement', 'Losses')
])


def is_complex(path, complex_cache={}):
    if isinstance(path[-2], str):
        k = tuple(path[-2:])
    else:
        k = (path[-4], path[-1])

    try:
        try:
            return complex_cache[k]
        except:
            pass

        if k[0] == 'DSS':
            res = 'complex' in (getdoc(getattr(IDSS, k[1])) or '').rstrip().lower()
            complex_cache[k] = res
            return res
        elif k[0] == 'ActiveCircuit':
            res = 'complex' in (getdoc(getattr(ICircuit.ICircuit, k[1])) or '').rstrip().lower()
            complex_cache[k] = res
            return res
        elif k[0] == 'ActiveBus':
            res = 'complex' in (getdoc(getattr(ICircuit.IBus, k[1])) or '').rstrip().lower()
            complex_cache[k] = res
            return res
        elif k[0] == 'ActiveCktElement':
            res = 'complex' in (getdoc(getattr(ICircuit.ICktElement, k[1])) or '').rstrip().lower()
            complex_cache[k] = res
            return res

        res = 'complex' in (getdoc(getattr(getattr(ICircuit, 'I' + k[0]), k[1])) or '').rstrip().lower()
        complex_cache[k] = res
        return res
    except:
        print(path, k)
        raise


class ComparisonHandler:
    def __init__(self, fnA, fnB, fns=None):
        self.fnA = fnA
        self.fnB = fnB
        self.fns = fns
        self.A_IS_COM = None
        self.B_IS_COM = None
        self.per_file = defaultdict(int)
        self.per_file_detail = defaultdict(list)
        self.total = 0

    def printe(self, s, path, *args):
        self.per_file[path[0]] += 1
        self.per_file_detail[path[0]].append((s, path, *args))
        if VERBOSE:
            print(s, path, *args)

    def element_compare(self, va, vb, path):
        if isinstance(va, str):
            if va.lower() != vb.lower():
                self.printe('ERROR (str):', path, repr(va), repr(vb))

            return

        if isinstance(va, int):
            if path[-1] == 'NumProperties' and path[-5] == 'Generators':
                if self.A_IS_COM:
                    va -= 2
                if self.B_IS_COM:
                    va -= 2

            # assert va == vb, (va, vb, path)
            if va != vb:# and not np.isclose(va, vb, tol, tol):
                self.printe('ERROR (int):', path, va, vb, abs(va - vb))

            return

        if isinstance(va, float):
            # assert va == vb, (va, vb, path)
            if va != vb and not np.isclose(va, vb, tol, tol):
                self.printe('ERROR (float):', path, va, vb, abs(va - vb))

            return


    def compare(self, a, b, org_path=None):
        for k in a.keys():
            path = org_path + [k]
            if tuple(path) in KNOWN_COM_DIFF:
                continue

            # print(path)
            va, vb = a.get(k), b.get(k, MISSING)

            if vb is MISSING:
                continue

            if k in ('DefaultEditor', 'DataPath', 'Version', 'NumClasses', 'Classes', 'UserClasses'):
                continue # May/should be different even in the same platform

            if k in ('TotalMiles', 'FaultRate', 'pctPermanent'):
                continue # TODO: investigate

            if k == 'AutoBusList':
                continue # buggy?

            if k == 'duty' and path[-4] == 'Loads':
                continue # buggy

            if k in (
                'Process_Time', 'Time_of_Step', 'Total_Time', 'runtime', # must be different always
                'GUID', # if not explicitly set, random
                'FileName', # different normalization, maybe we could process them
                'FileVersion', # random/uninitialized value in COM
            ):
                continue 

            if isinstance(va, dict):
                # recursive compare
                self.compare(va, vb, path)
                continue

            if isinstance(va, list):
                if ((va == ['none'] or va == ['NONE']) and vb == []) or (va == [] and (vb == ['none'] or vb == ['NONE'])):
                    continue

                if k in ('Isc', 'Voc') and va == [0.0] and vb == []:
                    continue

                if path[-2:] == ['ISources', 'records'] and len(va) == 1 and len(vb) != 1:
                    continue # buggy iteration for Isources

                if k == 'AllPropertyNames' and path[-3] == 'Generators':
                    if self.A_IS_COM:
                        va = list(va)
                        if 'Rneut' in va:
                            va.remove('Rneut')
                            va.remove('Xneut')
                    if self.B_IS_COM:
                        vb = list(vb)
                        if 'Rneut' in vb:
                            vb.remove('Rneut')
                            vb.remove('Xneut')

                if len(va) != len(vb) and k != 'ZIPV':
                    if k == 'dblFreq':
                        if va == [0.0]: #TODO: may be worth adjusting in DSS C-API
                            assert all(x == 0 for x in vb), (path, va, vb)
                            continue

                    # printe('ERROR (list)?', path, va, vb, per_file=per_file, per_file_detail=per_file_detail)
                    self.printe('ERROR (list)?', path, len(va), len(vb))

                if not va:
                    continue

                if isinstance(va[0], dict):
                    # recursive compare, each element
                    for idx, (item_a, item_b) in enumerate(zip(va, vb)):
                        self.compare(item_a, item_b, path + [idx])

                    continue

                if isinstance(va[0], str):
                    if k == 'EventLog':
                        # Too textual, too many details to compare here
                        #TODO: consider fuzzy comparison
                        continue

                    va = [(x or '').strip().lower() for x in va]
                    vb = [(x or '').strip().lower() for x in vb]
                    if va != vb:
                        self.printe('ERROR ([str])', path, va[:10], vb[:10], len(va))
                    
                    continue

                if isinstance(va[0], float) or va[0] is None:
                    if None in va:
                        va = [x if x is not None else np.NaN for x in va]

                    if None in vb:
                        vb = [x if x is not None else np.NaN for x in vb]

                    atol = tol
                    rtol = tol
                    va = np.asarray(va)
                    vb = np.asarray(vb)

                    if (k == 'Residuals' or 'magang' in k.lower()) and len(va) == len(vb) and len(va) % 2 == 0:
                        va = va[::2] * np.exp(1j * va[1::2] / BAD_RAD_TO_DEG)
                        vb = vb[::2] * np.exp(1j * vb[1::2] / BAD_RAD_TO_DEG)
                        rtol = 5e-4 
                        atol = 1e-2

                    elif (k == 'YCurrents' or k.startswith('Cplx') or is_complex(path)) and len(va) % 2 == 0:
                        va = va.view(dtype=complex)
                        vb = vb.view(dtype=complex)
                        rtol = 1e-3
                        
                    if 'Seq' in k:
                        # Official data uses bad precision in the transform
                        # Let's just compare with a wide margin to check for really absurd values. 
                        # The nodal values are compared with full precision
                        rtol = 1e-2
                        atol = 1e-2

                    # abs(b - a) <= (atol + rtol * abs(a))
                    if len(vb) != len(va):
                        self.printe('ERROR (vector, shapes):', path, f'a: {len(va)}, b: {len(vb)}')
                        continue

                    elif not np.allclose(vb, va, atol=atol, rtol=rtol):
                        with np.errstate(divide='ignore', invalid='ignore', over='ignore'):
                            d_rel = np.nan_to_num(1 - abs(vb / va), 0)
                            d_abs = abs(va - vb)
                            if rtol:
                                pct_rel = 100 * sum(d_rel > rtol) / len(va)
                            else:
                                pct_rel = 0

                            if atol:
                                pct_abs = 100 * sum(d_abs > atol) / len(va)
                            else:
                                pct_abs = 0

                        if len(va) > 1000 and pct_rel < 0.1 and pct_abs < 0.1:
                            # Seems OK
                            continue

                        self.printe('ERROR (vector):', path, f'count: {len(va)}, max abs: {max(d_abs)}, max rel: {max(abs(d_rel))}, abs(>{atol}): {pct_abs:.2g}%, rel(>{rtol}): {pct_rel:.2g}%')
                        # print(va)
                        # print(vb)

                    continue

            self.element_compare(va, vb, path)


    def split(self):
        with ZipFile(self.fnA, 'r') as zipA:
            filenames = [finfo.filename for finfo in zipA.filelist]

        step = len(filenames) // os.cpu_count()
        parts = []
        last_proc = os.cpu_count()
        for i in range(last_proc + 1):
            i_start = i * step
            i_last = (i + 1) * step
            if i == last_proc and i_last != len(filenames):
                i_last = len(filenames)

            parts.append((self.fnA, self.fnB, filenames[i_start : i_last], VERBOSE))
        
        return parts


    def merge(self, results):
        for other_per_file, other_per_file_detail, other_total in results:
            self.per_file.update(other_per_file)
            self.per_file_detail.update(other_per_file_detail)
            self.total += other_total


    def compare_all(self):
        print(self.fnA)
        print(self.fnB)

        with ZipFile(self.fnA, 'r') as zipA, ZipFile(self.fnB, 'r') as zipB:
            self.total = 0
            if self.fns:
                filenames = self.fns
            else:
                filenames = [finfo.filename for finfo in zipA.filelist]

            for fn in filenames:
                VERBOSE = True
                try:
                    fB = zipB.open(fn, 'r')
                    fA = zipA.open(fn, 'r')
                    print(fn)
                except KeyError:
                    print('MISSING:', fn)
                    continue
                except BadZipFile:
                    print('BAD:', fn)
                    continue

                dataA = json.load(fA)
                dataB = json.load(fB)

                if not dataA['Solution']['Converged']:
                    print('Skipping, not converged in the official version:', fn)
                    continue

                self.A_IS_COM = 'C-API' not in dataA['DSS']['Version']
                self.B_IS_COM = 'C-API' not in dataB['DSS']['Version']
                try:
                    self.compare(dataA, dataB, [fn])
                except:
                    print("COMPARE ERROR:", fn)
                    raise

                self.total += 1


def compare_filelist(fnA, fnB, fns, verb):
    global VERBOSE
    VERBOSE = verb
    cmp = ComparisonHandler(fnA, fnB, fns)
    cmp.compare_all()
    return (dict(cmp.per_file), dict(cmp.per_file_detail), cmp.total)


if __name__ == '__main__':
    import sys
    _fnA, _fnB = sys.argv[1:3]
    mp = '-p' in sys.argv[3:]
    VERBOSE = ('-v' in sys.argv[3:]) and (not mp)
    
    cmp = ComparisonHandler(_fnA, _fnB)
    if mp:
        print("Using multiprocessing")
        from multiprocessing import Pool
        parts = cmp.split()
        pool = Pool()
        results = pool.starmap(compare_filelist, parts)
        cmp.merge(results)
    else:
        cmp.compare_all()

    print(cmp.fnA)
    print(cmp.fnB)
    pprint(cmp.per_file)

    print()
    print('Total:', cmp.total, 'files')
    print()
    if not VERBOSE:
        for fn, cnt in cmp.per_file.items():
            if cnt < 10:
                print()
                print(fn)

                for l in cmp.per_file_detail[fn]:
                    print(*l)
