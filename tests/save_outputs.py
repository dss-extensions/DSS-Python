import os, sys, platform, traceback, json, re
from glob import glob
from inspect import ismethod
from math import isfinite
from time import perf_counter
from tempfile import TemporaryDirectory
import numpy as np
from zipfile import ZipFile, ZIP_DEFLATED
from dss import enums, DSSException
import dss

original_working_dir = os.getcwd()

NO_PROPERTIES = os.getenv('DSS_PYTHON_VALIDATE') == 'NOPROP'
WIN32 = (sys.platform == 'win32')
COM_VLL_BROKEN = True
SAVE_DSSX_OUTPUT = ('dss-extensions' in sys.argv) or not WIN32
VERBOSE = ('-v' in sys.argv)
suffix = ''

class COMDSSException(Exception):
    def __str__(self):
        return f'(COM#{self.args[0]}) {self.args[1]}'

def check_error():
    number = DSS.Error.Number
    if not SAVE_DSSX_OUTPUT and number:
        msg = DSS.Error.Description
        if "ignore_me_invalid_executable" not in msg:
            raise COMDSSException(number, msg)

if VERBOSE:
    printv = print
else:
    def printv(*args):
        pass
    
def run(dss: dss.IDSS, fn: str, line_by_line: bool):
    os.chdir(original_working_dir)
    dss.Text.Command = f'cd "{original_working_dir}"'
    dss.Start(0)
    
    dss.Text.Command = 'Clear'
    dss.Text.Command = 'new circuit.RESET'
    dss.Text.Command = 'Set DefaultBaseFreq=60'
    dss.Text.Command = 'Set EarthModel=deri'
    dss.Text.Command = 'new wiredata.wire Runits=mi Rac=0.306 GMRunits=ft GMRac=0.0244  Radunits=in Diam=0.721'
    dss.Text.Command = 'new linegeometry.reset nconds=1 nphases=1 cond=1 wire=wire units=ft x=-4 h=28'
    dss.Text.Command = 'new line.line1 geometry=reset length=2000 units=ft bus1=sourcebus bus2=n2'
    dss.Text.Command = 'solve'
    dss.Text.Command = 'Clear'

    with open(os.path.join(ROOT_DIR, fn), 'r') as f:
        full_text = f.read().lower()
        needs_solve = '\nsolve' not in full_text
        has_closedi = '\nclosedi' in full_text

    if line_by_line:
        with open(fn, 'r') as f:
            dss.Text.Command = f'cd "{os.path.dirname(fn)}"'
            iter_f = iter(f)
            try:
                while True:
                    input_line = next(iter_f).strip()
                    if input_line.startswith('/*'):
                        #print('Skipping input:', repr(input_line))
                        while True:
                            input_line = next(iter_f).strip()
                            if '*/' in input_line:
                                input_line = ''
                                break

                    if not input_line: 
                        continue

                    lc_input_line = input_line.lower()
                    if any(lc_input_line.startswith(x) for x in ['show', 'plot', 'visualize', 'dump', 'export', 'help', 'fileedit']) or ord(input_line[0]) > 127:
                        #print('Skipping input:', repr(input_line))
                        continue
                    else:
                        #print(input_line)
                        dss.Text.Command = input_line
                        check_error()

            except StopIteration:
                pass
    else:
        dss.Text.Command = 'Compile "{}"'.format(os.path.join(ROOT_DIR, fn))
        check_error()

    if needs_solve:
        dss.ActiveCircuit.Solution.Mode = enums.SolveModes.Daily
        dss.ActiveCircuit.Solution.Solve()
        check_error()
    else:
        dss.Text.Command = 'Makebuslist'

    reliabity_ran = True
    try:
        dss.ActiveCircuit.Meters.DoReliabilityCalc(False)
        check_error()
        
    except (DSSException, COMDSSException) as ex:
        if ex.args[0] == 52902:
            reliabity_ran = False

    return reliabity_ran, has_closedi


def adjust_to_json(cls, field):
    try:
        data = getattr(cls, field)
        if ismethod(data):
            raise StopIteration
        if isinstance(data, np.ndarray):
            # Replace NaN with None, etc.
            data = [x if isfinite(x) else None for x in data.tolist()]

        check_error()
        # json.dumps(data)

        return data
    except StopIteration:
        return
    except:
        print(cls, field)
        raise

ckt_elem_columns_meta = {'AllPropertyNames'}
ckt_iter_columns_meta = {'Count', 'AllNames'}
pc_elem_columns = {'AllVariableValues', 'AllVariableNames'}

def export_dss_api_cls(dss: dss.IDSS, dss_cls):
    printv(dss_cls)
    has_iter = hasattr(type(dss_cls), '__iter__')
    is_ckt_element = getattr(type(dss_cls), '_is_circuit_element', False)
    ckt_elem = dss.ActiveCircuit.ActiveCktElement
    ckt_elem_columns = set(type(ckt_elem)._columns) - ckt_elem_columns_meta - pc_elem_columns
    fields = list(type(dss_cls)._columns)
    
    if 'SAIFIKW' in fields:
        meter_section_fields = fields[fields.index('NumSections'):]
        fields = fields[:fields.index('NumSections')]
    else:
        meter_section_fields = None

    if not SAVE_DSSX_OUTPUT:
        if 'TotalPowers' in ckt_elem_columns:
            ckt_elem_columns.remove('TotalPowers')

        if COM_VLL_BROKEN and 'Coorddefined' in fields:
            fields.remove('puVLL')
            fields.remove('VLL')
            fields.remove('AllPCEatBus')
            fields.remove('AllPDEatBus')

        # if 'Sensor' in fields: # Both  Loads and PVSystems
        if 'ipvsystems' in type(dss_cls).__name__.lower():
            fields.remove('Sensor')

        # if 'IrradianceNow' in fields:
        #     fields.remove('IrradianceNow')

        # if 'IFuses' in type(dss_cls).__name__:
        #     fields.remove('State')
        #     fields.remove('NormalState')

        # if 'IReclosers' in type(dss_cls).__name__:
        #     fields.remove('State')
        #     fields.remove('NormalState')

        # if 'IRelays' in type(dss_cls).__name__:
        #     fields.remove('State')
        #     fields.remove('NormalState')


    records = []
    metadata_record = {}
    extra = {}
    if has_iter:
        # Iterating this will already call First, Next, etc.
        items = dss_cls
    else:
        items = [dss_cls]

    for _ in items:
        record = {}
        for field in fields:
            printv('>', field)
            try:
                record[field] = adjust_to_json(dss_cls, field)
            except StopIteration:
                # Some fields are functions, skip those
                continue
            except AttributeError:
                # Depending on the version, a field doesn't exist
                continue

        if meter_section_fields:
            if dss_cls.NumSections > 0:
                dss_cls.SetActiveSection(1)
                for field in meter_section_fields:
                    printv('>', field)
                    try:
                        record[field] = adjust_to_json(dss_cls, field)
                    except StopIteration:
                        # Some fields are functions, skip those
                        continue

        if is_ckt_element:
            # also dump the circuit element info
            ckt_record = {}
            for field in ckt_elem_columns:
                printv('>', field)
                ckt_record[field] = adjust_to_json(ckt_elem, field)

            record['ActiveCktElement'] = ckt_record


        if not has_iter:
            # simple record
            return record

        # accumulate records
        records.append(record)

    if is_ckt_element and not metadata_record:
        if records:
            for field in ckt_elem_columns_meta:
                printv('>', field)
                metadata_record[field] = adjust_to_json(ckt_elem, field)

        for field in ckt_iter_columns_meta:
            printv('>', field)
            metadata_record[field] = adjust_to_json(dss_cls, field)

        if 'Meters' in type(dss_cls).__name__:
            # This breaks the iteration
            extra = {'Totals': adjust_to_json(dss_cls, 'Totals')}

    # elif has_iter and not metadata_record:
    #     for field in iter_columns_meta:
    #         metadata_record[field] = adjust_to_json(dss_cls, field)

    return {'records': records, 'metadata': metadata_record, **extra}


def save_state(dss: dss.IDSS, runtime: float = 0.0) -> str:
    dss_classes = {
        'DSS': dss,
        'ActiveCircuit': dss.ActiveCircuit,

        'ActiveBus': dss.ActiveCircuit.ActiveBus,
        'Capacitors': dss.ActiveCircuit.Capacitors,
        'CapControls': dss.ActiveCircuit.CapControls,
        'CtrlQueue': dss.ActiveCircuit.CtrlQueue,
        'Fuses': dss.ActiveCircuit.Fuses,
        'Generators': dss.ActiveCircuit.Generators,
        'GICSources': dss.ActiveCircuit.GICSources,
        'ISources': dss.ActiveCircuit.ISources,
        'LineCodes': dss.ActiveCircuit.LineCodes,
        'Lines': dss.ActiveCircuit.Lines,
        'Loads': dss.ActiveCircuit.Loads,
        'LoadShapes': dss.ActiveCircuit.LoadShapes,
        'Meters': dss.ActiveCircuit.Meters,
        'Monitors': dss.ActiveCircuit.Monitors,
        'PDElements': dss.ActiveCircuit.PDElements,
        'PVSystems': dss.ActiveCircuit.PVSystems,
        'Reclosers': dss.ActiveCircuit.Reclosers,
        'RegControls': dss.ActiveCircuit.RegControls,
        'Relays': dss.ActiveCircuit.Relays,
        'Sensors': dss.ActiveCircuit.Sensors,
        'Settings': dss.ActiveCircuit.Settings,
        'Solution': dss.ActiveCircuit.Solution,
        'SwtControls': dss.ActiveCircuit.SwtControls,
        'Topology': dss.ActiveCircuit.Topology,
        'Transformers': dss.ActiveCircuit.Transformers,
        'Vsources': dss.ActiveCircuit.Vsources,
        'XYCurves': dss.ActiveCircuit.XYCurves,
    }

    try:
        dss_classes.update({
            'CNData': dss.ActiveCircuit.CNData,
            'LineGeometries': dss.ActiveCircuit.LineGeometries,
            'LineSpacings': dss.ActiveCircuit.LineSpacings,
            'Reactors': dss.ActiveCircuit.Reactors,
            'Storages': dss.ActiveCircuit.Storages,
            'TSData': dss.ActiveCircuit.TSData,
            'WireData': dss.ActiveCircuit.WireData,
        })
    except AttributeError:
        pass

    document = {
        'runtime': runtime,
        #TODO: machine info?
    }
    for key, dss_api_cls in dss_classes.items():
        # print(key)
        document[key] = export_dss_api_cls(dss, dss_api_cls)
    


    return json.dumps(document)


def get_archive_fn(live_fn):
    actual_fn = os.path.normpath(live_fn)
    common_prefix = os.path.commonprefix([ROOT_DIR, actual_fn])
    archive_fn = actual_fn[len(common_prefix) + 1:]
    if WIN32:
        archive_fn = archive_fn.replace('\\', '/')

    return archive_fn
            
if __name__ == '__main__':
    if os.path.exists('../../electricdss-tst/'):
        ROOT_DIR = os.path.abspath('../../electricdss-tst/')
    else:
        ROOT_DIR = os.path.abspath('../electricdss-tst/')

    try:
        from ._settings import test_filenames, cimxml_test_filenames
    except ImportError:
        from _settings import test_filenames, cimxml_test_filenames

    # test_filenames = []
    # cimxml_test_filenames = []
    try:
        import colored_traceback
        colored_traceback.add_hook()
        colorizer = colored_traceback.Colorizer('default', False)
    except:
        colorizer = None


    if SAVE_DSSX_OUTPUT:
        from dss import DSS, DSSCompatFlags
        # DSS.CompatFlags = DSSCompatFlags.InvControl9611
        print("Using DSS Extensions:", DSS.Version)
        match = re.match('DSS C-API Library version ([^ ]+) revision.* ([0-9]+);.*', DSS.Version)
        dssx_ver, dssx_timestamp = match.groups()
        suffix = f'-dssx-{sys.platform}-{platform.machine()}-{dssx_ver}-{dssx_timestamp}'
        DSS.AllowEditor = False
    else:
        import comtypes.client
        DSS = comtypes.client.CreateObject("OpenDSSEngine.DSS")
        DSS = dss.patch_dss_com(DSS)
        #DSS.Text.Command = r'set editor=ignore_me_invalid_executable' -- need to let it open for some reports :|
        print("Using official OpenDSS COM:", DSS.Version)
        com_ver = DSS.Version.split(' ')[1]
        suffix = f'-COM-{platform.machine()}-{com_ver}'

    DSS.AllowForms = False

    try:
        DSS.Text.Command = 'new circuit.dummy'
        check_error()
        DSS.Text.Command = 'set ShowExport=NO'
        check_error()
        DSS.Text.Command = 'clear'
        check_error()
    except:
        pass

    t0_global = perf_counter()
    total_runtime = 0.0
    with ZipFile(os.path.join(original_working_dir, f'results{suffix}.zip'), mode='a', compression=ZIP_DEFLATED) as zip_out:
        for fn in test_filenames + cimxml_test_filenames:
            org_fn = fn
            fixed_fn = fn if not fn.startswith('L!') else fn[2:]
            line_by_line = fn.startswith('L!')
            fn = os.path.join(ROOT_DIR, fixed_fn)
            json_fn = get_archive_fn(fn) + '.json'
            try:
                zip_out.getinfo(json_fn)
                continue
            except KeyError:
                pass

            try:
                has_closedi = False
                tstart_run = perf_counter()
                reliabity_ran, has_closedi = run(DSS, fn, line_by_line)
                runtime = perf_counter() - tstart_run
                total_runtime += runtime
                data_str = save_state(DSS, runtime=runtime)
                print(json_fn)
                zip_out.writestr(json_fn, data_str)
            except KeyboardInterrupt:
                exit()
            except OSError:
                traceback.print_exc()
                exit()
            except:
                print('ERROR:', fn)
                if colorizer:
                    colorizer.colorize_traceback(*sys.exc_info())
                else:
                    traceback.print_exc()

                continue

            if org_fn in cimxml_test_filenames:
                DSS.Text.Command = 'export cim100'
                xml_live_fns = [DSS.Text.Result]
                DSS.Text.Command = 'export cim100fragments'
                xml_live_fns.extend(glob(DSS.Text.Result + '_*.xml'))
                for xml_live_fn in xml_live_fns:
                    zip_out.write(xml_live_fn, get_archive_fn(xml_live_fn).replace('.XML', '.xml'))

            if has_closedi:
                DSS.Text.Command = 'get CaseName'
                res_dir = os.path.join(DSS.DataPath, DSS.Text.Result)
                for csv_live_fn in glob(f'{res_dir}/*/*.csv'):
                    print(csv_live_fn)
                    zip_out.write(csv_live_fn, get_archive_fn(csv_live_fn).replace('.CSV', '.csv'))

            with TemporaryDirectory() as tmp_dir:
                DSS.Text.Command = f'save circuit dir="{tmp_dir}"'
                base_zip_dir = get_archive_fn(fn) + '.saved/'
                for saved_fn in glob(f'{tmp_dir}/**', recursive=True):
                    if os.path.abspath(saved_fn) == tmp_dir:
                        continue

                    rel_saved_fn = os.path.relpath(saved_fn, tmp_dir)
                    # print((json_fn, base_zip_dir, saved_fn, rel_saved_fn.replace('.DSS', '.dss')))
                    zip_out.write(saved_fn, base_zip_dir + rel_saved_fn.replace('.DSS', '.dss'))
                    

    print(perf_counter() - t0_global, 'seconds')
    print(total_runtime, 'seconds (runtime only)')

