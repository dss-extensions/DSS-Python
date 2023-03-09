import os, sys, platform, traceback, json
from inspect import ismethod, getdoc
from math import isfinite
from time import perf_counter
import numpy as np
from zipfile import ZipFile
from dss import enums, DSSException, DSS
import dss

original_working_dir = os.getcwd()

NO_PROPERTIES = os.getenv('DSS_PYTHON_VALIDATE') == 'NOPROP'
NO_V9 = False
WIN32 = (sys.platform == 'win32')
COM_VLL_BROKEN = True

USE_THREADS = False
SAVE_OUTPUT = 'save' in sys.argv
LOAD_OUTPUT = (not WIN32) or ('load' in sys.argv) 
SAVE_DSSX_OUTPUT = SAVE_OUTPUT and ('dss-extensions' in sys.argv)
LOAD_PLATFORM = None

def parse_dss_matrix(m):
    try:
        sep = ' '
        if ',' in m:
            sep = ','
            
        data = []
        for row in m[1:-1].split(' |'):
            row_float = []
            for e in row.strip(sep).strip(' ').split(sep):
                if not e: continue
                row_float.append(float(e))
                
            data.append(row_float)
            
        return data
    except:
        return m


'''
We need to save various outputs to compare different versions and implementation of the DSS engine.

From the official COM API implementation, ...
'''

def run(dss: dss.IDSS, fn: str, solve: bool):
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

    line_by_line = fn.startswith('L!')
    if line_by_line:
        fn = fn[2:]
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

                    if not input_line: continue
                    lc_input_line = input_line.lower()
                    if any(lc_input_line.startswith(x) for x in ['show', 'plot', 'visualize', 'dump', 'export']) or ord(input_line[0]) > 127:
                        #print('Skipping input:', repr(input_line))
                        continue
                    else:
                        # Some scripts have hardcoded paths...
                        input_line = input_line.replace('C:\\Users\\prdu001\\OpenDSS\\Test\\', '')
                        input_line = input_line.replace('C:\\Users\\prdu001\\OpenDSS\\Distrib\\Examples\\Scripts\\', '../Version8/Distrib/Examples/Scripts/')
                        #print(input_line)
                        dss.Text.Command = input_line
            except StopIteration:
                pass
    else:
        dss.Text.Command = 'Compile "{}"'.format(fn)

    if solve:
        dss.ActiveCircuit.Solution.Mode = enums.SolveModes.Daily
        dss.ActiveCircuit.Solution.Solve()

    realibity_ran = True
    try:
        dss.ActiveCircuit.Meters.DoReliabilityCalc(False)
    except DSSException as ex:
        if ex.args[0] == 52902:
            realibity_ran = False

    return realibity_ran


def adjust_to_json(cls, field):
    try:
        data = getattr(cls, field)
        if ismethod(data):
            raise StopIteration
        if isinstance(data, np.ndarray):
            # Replace NaN with None, etc.
            data = [x if isfinite(x) else None for x in data.tolist()]

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
ckt_elem_columns = set(DSS.ActiveCircuit.ActiveCktElement._columns) - ckt_elem_columns_meta - pc_elem_columns

def export_dss_api_cls(dss: dss.IDSS, dss_cls):
    has_iter = hasattr(dss_cls, '__iter__')
    is_ckt_element = getattr(dss_cls, '_is_circuit_element', False)
    ckt_elem = dss.ActiveCircuit.ActiveCktElement
    fields = dss_cls._columns
    if 'SAIFIKW' in fields:
        meter_section_fields = fields[fields.index('NumSections'):]
        fields = fields[:fields.index('NumSections')]
    else:
        meter_section_fields = None

    records = []
    metadata_record = {}
    if has_iter:
        # Iterating this will already call First, Next, etc.
        items = dss_cls
    else:
        items = [dss_cls]

    for _ in items:
        record = {}
        for field in fields:
            # print('>', field)
            try:
                record[field] = adjust_to_json(dss_cls, field)
            except StopIteration:
                # Some fields are functions, skip those
                continue

        if meter_section_fields:
            if dss_cls.NumSections > 0:
                dss_cls.SetActiveSection(1)
                for field in meter_section_fields:
                    # print('>', field)
                    try:
                        record[field] = adjust_to_json(dss_cls, field)
                    except StopIteration:
                        # Some fields are functions, skip those
                        continue

        if is_ckt_element:
            # also dump the circuit element info
            ckt_record = {}
            for field in ckt_elem_columns:
                # print('>', field)
                ckt_record[field] = adjust_to_json(ckt_elem, field)

            record['ActiveCktElement'] = ckt_record

            if not metadata_record:
                for field in ckt_elem_columns_meta:
                    # print('>', field)
                    metadata_record[field] = adjust_to_json(ckt_elem, field)

                for field in ckt_iter_columns_meta:
                    # print('>', field)
                    metadata_record[field] = adjust_to_json(dss_cls, field)

        # elif has_iter and not metadata_record:
        #     for field in iter_columns_meta:
        #         metadata_record[field] = adjust_to_json(dss_cls, field)

        # 'ActiveDSSElement: dss.ActiveCircuit.ActiveDSSElement,
        # 'ReduceCkt': dss.ActiveCircuit.ReduceCkt,
        # 'ActiveClass': dss.ActiveCircuit.ActiveClass,
        # 'Parallel': dss.ActiveCircuit.Parallel,


        if not has_iter:
            # simple record
            return record

        # accumulate records
        records.append(record)

    return {'records': records, 'metadata': metadata_record}


def save_state(dss: dss.IDSS, runtime: float = 0.0) -> str:
    dss_classes = {
        'ActiveCircuit': dss.ActiveCircuit,

        'ActiveBus': dss.ActiveCircuit.ActiveBus,
        'Capacitors': dss.ActiveCircuit.Capacitors,
        'CapControls': dss.ActiveCircuit.CapControls,
        'CNData': dss.ActiveCircuit.CNData,
        'CtrlQueue': dss.ActiveCircuit.CtrlQueue,
        'Fuses': dss.ActiveCircuit.Fuses,
        'Generators': dss.ActiveCircuit.Generators,
        'GICSources': dss.ActiveCircuit.GICSources,
        'ISources': dss.ActiveCircuit.ISources,
        'LineCodes': dss.ActiveCircuit.LineCodes,
        'LineGeometries': dss.ActiveCircuit.LineGeometries,
        'Lines': dss.ActiveCircuit.Lines,
        'LineSpacings': dss.ActiveCircuit.LineSpacings,
        'Loads': dss.ActiveCircuit.Loads,
        'LoadShapes': dss.ActiveCircuit.LoadShapes,
        'Meters': dss.ActiveCircuit.Meters,
        'Monitors': dss.ActiveCircuit.Monitors,
        'PDElements': dss.ActiveCircuit.PDElements,
        'PVSystems': dss.ActiveCircuit.PVSystems,
        'Reactors': dss.ActiveCircuit.Reactors,
        'Reclosers': dss.ActiveCircuit.Reclosers,
        'RegControls': dss.ActiveCircuit.RegControls,
        'Relays': dss.ActiveCircuit.Relays,
        'Sensors': dss.ActiveCircuit.Sensors,
        'Settings': dss.ActiveCircuit.Settings,
        'Solution': dss.ActiveCircuit.Solution,
        'Storages': dss.ActiveCircuit.Storages,
        'SwtControls': dss.ActiveCircuit.SwtControls,
        'Topology': dss.ActiveCircuit.Topology,
        'Transformers': dss.ActiveCircuit.Transformers,
        'TSData': dss.ActiveCircuit.TSData,
        'Vsources': dss.ActiveCircuit.Vsources,
        'WireData': dss.ActiveCircuit.WireData,
        'XYCurves': dss.ActiveCircuit.XYCurves,
    }

    document = {
        'runtime': runtime,
        #TODO: machine info?
    }
    for key, dss_api_cls in dss_classes.items():
        # print(key)
        document[key] = export_dss_api_cls(dss, dss_api_cls)
    


    return json.dumps(document)

            
if __name__ == '__main__':
    from common import test_filenames, errored
    try:
        import colored_traceback
        colored_traceback.add_hook()
        colorizer = colored_traceback.Colorizer('default', False)
    except:
        colorizer = None

    try:
        DSS.AllowEditor = False
    except:
        pass

    DSS.AllowForms = False

    norm_root = os.path.normpath('../../electricdss-tst')

    t0_global = perf_counter()
    with ZipFile(os.path.join(original_working_dir, 'results.zip'), 'a') as zip_out:
        for fn in test_filenames:
            actual_fn = os.path.normpath(fn if not fn.startswith('L!') else fn[2:])
            common_prefix = os.path.commonprefix([norm_root, actual_fn])
            fn_without_prefix = actual_fn[len(common_prefix) + 1:]
            json_fn = fn_without_prefix + '.json'
            try:
                zip_out.getinfo(json_fn)
                continue
            except KeyError:
                pass

            try:
                tstart_run = perf_counter()
                realibity_ran = run(DSS, fn, True)
                data_str = save_state(DSS, runtime=tstart_run - perf_counter())
                print(fn_without_prefix)
                zip_out.writestr(json_fn, data_str)
            except KeyboardInterrupt:
                exit()
            except:
                print('ERROR:', fn)
                if colorizer:
                    colorizer.colorize_traceback(*sys.exc_info())
                else:
                    traceback.print_exc()

                #raise

        
    print(perf_counter() - t0_global, 'seconds')
    # print(f"{len(failures)} Failures")
    # print(failures)
    # for fn in failures:
    #     print(fn)
