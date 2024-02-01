"""
This module provides a **work-in-progress** implementation of the original OpenDSS plots
using the new features from DSS C-API v0.12+ and common Python modules such as matplotlib.

This is not a complete implementation and there are known limitations, but should suffice
for many use-cases. We'd like to add another backend later.
"""
import warnings
from typing import List
import os
from . import api_util
from . import DSS as DSSPrime
from ._cffi_api_util import CffiApiUtil
from .IDSS import IDSS
from .IBus import IBus
try:
    import numpy as np
    from matplotlib import pyplot as plt
    from matplotlib.path import Path
    from matplotlib.collections import LineCollection
    from mpl_toolkits.mplot3d.art3d import Line3DCollection
    from matplotlib.patches import Rectangle
    import matplotlib.colors
    import scipy.sparse.coo as coo
except:
    raise ImportError("SciPy and matplotlib are required to use this module.")

import re, json, sys, warnings

try:
    from IPython import get_ipython
    from IPython.display import FileLink, display, display_html, HTML
    from IPython.core.magic import register_cell_magic
    ipython = get_ipython()
    if ipython is None:
        raise ImportError

    import html

    def link_file(fn):
        relfn = os.path.relpath(fn, os.getcwd())
        if relfn.startswith('..'):
            # cannot show in the notebook :(
            display(HTML(f'<p><b>File output</b> ("{html.escape(relfn)}") outside current workspace.<p>'))
        else:    
            display(FileLink(relfn, result_html_prefix=f'<b>File output</b> ("{html.escape(fn)}"):&nbsp;'))

    def show(text):
        display(text)


    @register_cell_magic
    def dss(line, cell):
        DSSPrime.Text.Commands(cell)

    DSSPrime.AllowChangeDir = False
except:
    def link_file(fn):
        print(f'Output file: "{fn}"')

    def show(text):
        print(text)


    #FileLink('path_to_file/filename.extension')

# import os
# import html
# import tqdm
# from tqdm.notebook import tqdm
# import IPython.display

include_3d = '2d' # '2d' (default), '3d' (prefer 3d), 'both'

PROFILE3PH = -1 # Default
PROFILEALL = -2 # All
PROFILEALLPRI = -3 # Primary
PROFILELL3PH = -4 # LL3Ph
PROFILELLALL = -5 # LLAll
PROFILELLPRI = -6 # LLPrimary

(pqVoltage, pqCurrent, pqPower, pqLosses, pqCapacity, pqNone) = range(6)

str_to_pq = {
    'Voltages': pqVoltage,
    'Currents': pqCurrent,
    'Powers': pqPower,
    'Losses': pqLosses,
    'Capacities': pqCapacity,
}

quantity_str = {v: k for k, v in str_to_pq.items()}
quantity_str[pqLosses] = 'Loss Density'

str_to_pq.update({    
    'Voltage': pqVoltage,
    'Current': pqCurrent,
    'Power': pqPower,
    'Loss': pqLosses,
    'Capacity': pqCapacity
})

# Markers
DSS_MARKER_37 = Path([(0.0, -0.5), (0.0, 0.196), (-0.36, -0.5), (0.361, -0.5)], [1, 2, 1, 2])
DSS_MARKER_38 = Path([(0.0, -0.23), (0.0, 0.196), (-0.36, 0.196), (0.361, 0.196), (-0.36, -0.23), (0.361, -0.23)], [1, 2, 1, 2, 1, 2])
DSS_MARKER_20 = Path([(-0.23, -0.147), (0.0, 0.13), (0.23, -0.147)], [1, 2, 2])
DSS_MARKER_21 = Path([(-0.28, -0.147), (0.0, 0.13), (0.28, -0.147)], [1, 2, 2])
DSS_MARKER_22 = Path([(-0.23, 0.147), (0.0, -0.13), (0.23, 0.147)], [1, 2, 2])
DSS_MARKER_23 = Path([(-0.28, 0.147), (0.0, -0.13), (0.28, 0.147)], [1, 2, 2])

MARKER_MAP = {
    # marker, size multiplier (1=normal, 2=small, 3=tiny), fill
    0: (',', 1, 1),
    1: ('+', 3, 1),
    2: ('+', 2, 1),
    3: ('+', 1, 1),
    4: ('x', 3, 1),
    5: ('x', 2, 1),
    6: ('x', 1, 1),
    7: ('s', 3, 1),
    8: ('s', 2, 1),
    9: ('s', 1, 1),
    10: ('s', 3, 0),
    11: ('s', 2, 0),
    12: ('s', 1, 0),
    13: ('D', 3, 1),
    14: ('D', 2, 1),
    15: ('D', 1, 1),
    16: ('o', 2, 0),
    17: ('o', 1, 0),
    18: ('s', 1, 0.5),
    19: ('D', 1, 0),
    20: (DSS_MARKER_20, 2, 0),
    21: (DSS_MARKER_21, 1, 0),
    22: (DSS_MARKER_22, 2, 0),
    23: (DSS_MARKER_23, 1, 0),
    24: ('o', 1, 1),
    25: ('X', 1, 1),
    26: ('o', 2, 1),
    27: ('o', 3, 0),
    28: ('o', 3, 1),
    29: (DSS_MARKER_22, 3, 1),
    30: (DSS_MARKER_23, 2, 1),
    31: ('v', 3, 0), 
    32: ('v', 2, 0),
    33: (7, 1, 0),
    34: (7, 2, 1),
    35: ('^', 1, 0),
    36: (6, 1, 1), 
    37: (DSS_MARKER_37, 1, 0), 
    38: (DSS_MARKER_38, 1, 0), 
    39: ('$⊕$', 1, 1), # normal (circled plus)
    40: (8, 2, 0), # small
    41: (8, 2, 1), # small
    42: (8, 1, 0), # normal
    43: (8, 1, 1), # normal
    44: (9, 2, 0), # small
    45: (9, 2, 1), # small
    46: (9, 1, 0), # normal
    47: (9, 1, 1), # normal
}

LINES_STYLE_CODE = {1: '-', 2: '--', 3: ':', 4: '-.', 5: (0, (5, 1, 1, 1, 1, 1)), 6: (0, (0, 1))}

Colors = [
    '#000000',
    '#FF0000',
    '#0000FF',
    '#FF00FF',
    '#008000',
    '#80FF00',
    '#FF8040',
    '#DADE21',
    '#B56AFF',
    '#804000',
    '#808000',
    '#0000A0',
    '#FF8080',
    '#000080',
    '#7F7F7F',
    '#8E0F7B',
    '#07968E'
]

sizes = np.array([0, 9, 6, 4], dtype=float) * 0.7

MARKER_SEQ = (5, 15, 2, 8, 26, 36, 39, 19, 18)

def get_marker_dict(dss_code):
    marker, size, fill = MARKER_MAP[dss_code]
    res = dict(
        marker=marker, 
        markersize=sizes[size], 
        markerfacecolor=None if fill else 'none', 
        # fillstyle='full' if fill else 'none',
        alpha=0.5 if fill not in (0, 1) else 1, 
        markeredgecolor='none' if dss_code == 39 else None,
        markeredgewidth=1
    )
    for k, v in list(res.items()):
        if v is None:
            del res[k]
    
    return res

def nodot(b):
    return b.split('.', 1)[0]

class ToggleAdvancedTypes:
    def __init__(self, dss: IDSS, value: bool):
        self._value = value
        self._dss = dss
        self._previous = self._dss.AdvancedTypes
    
    def __enter__(self):
        if self._value != self._previous:
            self._dss.AdvancedTypes = self._value

        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._value != self._previous:
            self._dss.AdvancedTypes = self._previous


def dss_monitor_plot(DSS: IDSS, params):
    monitor = DSS.ActiveCircuit.Monitors
    monitor.Name = params['ObjectName']
    data = monitor.AsMatrix()
    if data is None or len(data) == 0:
        raise ValueError("There is not data to plot in the monitor. Hint: check the solution mode, solve the circuit and retry.")
    
    channels = params['Channels']
    num_ch = monitor.NumChannels
    channels = [ch for ch in channels if ch >= 1 and ch <= num_ch]
    if len(channels) == 0:
        raise IndexError("No valid channel numbers were specified.")

    bases = params['Bases']
    header = monitor.Header
    if len(monitor.dblHour) < len(monitor.dblFreq):
        header.insert(0, 'Frequency')
        header.insert(1, 'Harmonic')
        xlabel = 'Frequency (Hz)'
        h = data[:, 0]
    else:
        header.insert(0, 'Hour')
        header.insert(1, 'Seconds')
        h = data[:, 0] * 3600 + data[:, 1]
        total_seconds = max(h) - min(h)
        if total_seconds < 7200:
            xlabel = 'Time (s)'
        else:
            xlabel = 'Time (h)'
            h /= 3600

    separate = False
    if separate:
        fig, axs = plt.subplots(len(channels), sharex=True)#, figsize=(8, 9))
        icolor = -1
        for ax, base, ch in zip(axs, bases, channels):
            ch += 1
            icolor += 1
            ax.plot(h, data[:, ch] / base, color=Colors[icolor % len(Colors)])
            ax.grid()
            ax.set_ylabel(header[ch])

    else:
        fig, ax = plt.subplots(1)
        icolor = -1
        for base, ch in zip(bases, channels):
            ch += 1
            icolor += 1
            ax.plot(h, data[:, ch] / base, label=header[ch], color=Colors[icolor % len(Colors)])

        ax.grid()
        ax.legend()
        ax.set_ylabel('Mag') # Where "Mag" comes from?

    ax.set_title(params['ObjectName'])
    ax.set_xlabel(xlabel)



def dss_tshape_plot(DSS, params):
    # There is no dedicated API yet but we can move to the Obj API
    name = params['ObjectName']
    DSS.Text.Command = f'? tshape.{name}.temp'
    p = np.fromstring(DSS.Text.Result[1:-1].strip(), dtype=float, sep=' ')
    try:
        DSS.Text.Command = f'? tshape.{name}.hour'
        h = np.fromstring(DSS.Text.Result[1:-1].strip(), dtype=float, sep=' ')
    except:
        h = np.array([])

    try:
        interval = f'? tshape.{name}.interval' # hours
        interval = float(DSS.Text.Result)
    except:
        interval = 1

    fig, ax = plt.subplots(1)#, figsize=(8.5, 6))#, num=f"TShape.{params['ObjectName']}")

    if not h.size:
        h = interval * np.array(range(len(p)))

    x_unit = 'h'
    if h[-1] < 1:
        h *= 3600
        x_unit = 's'

    color1 = params['Color1']
    ax.plot(h, p, color=color1, label="Price")
    ax.set_title(f"TShape = {params['ObjectName']}")
    ax.set_xlabel(f'Time ({x_unit})')
    ax.set_ylabel('Temperature')

    ax.grid(ls='--')
    plt.tight_layout()



def dss_priceshape_plot(DSS, params):
    # There is no dedicated API yet but we can move to the Obj API
    name = params['ObjectName']
    DSS.Text.Command = f'? priceshape.{name}.price'
    p = np.fromstring(DSS.Text.Result[1:-1].strip(), dtype=float, sep=' ')
    try:
        DSS.Text.Command = f'? priceshape.{name}.hour'
        h = np.fromstring(DSS.Text.Result[1:-1].strip(), dtype=float, sep=' ')
    except:
        h = np.array([])

    try:
        interval = f'? priceshape.{name}.interval' # hours
        interval = float(DSS.Text.Result)
    except:
        interval = 1

    fig, ax = plt.subplots(1)#, figsize=(8.5, 6))#, num=f"PriceShape.{params['ObjectName']}")

    if not h.size:
        h = interval * np.array(range(len(p)))

    x_unit = 'h'
    if h[-1] < 1:
        h *= 3600
        x_unit = 's'

    color1 = params['Color1']

    ax.plot(h, p, color=color1, label="Price")
    ax.set_title(f"PriceShape = {params['ObjectName']}")
    ax.set_xlabel(f'Time ({x_unit})')
    ax.set_ylabel('Price')

    ax.grid(ls='--')
    plt.tight_layout()


def dss_loadshape_plot(DSS, params):
#     pprint(params)
    
    ls = DSS.ActiveCircuit.LoadShapes
    ls.Name = params['ObjectName']
    h = ls.TimeArray
    p = ls.Pmult
    q = ls.Qmult
    
    fig, ax = plt.subplots(1)#, figsize=(8.5, 6))#, num=f"LoadShape.{params['ObjectName']}")

    if not h.size or h is None or len(h) != len(p):
        h = ls.HrInterval * np.array(range(len(p)))

    x_unit = 'h'
    if h[-1] < 1:
        h *= 3600
        x_unit = 's'

    color1 = params['Color1']
    color2 = params['Color2']

    ax.plot(h, p, color=color1, label="Pmult")
    if q.size == p.size:
        ax.plot(h, q, color=color2, label="Qmult")

    ax.set_title(f"LoadShape = {params['ObjectName']}")
    ax.set_xlabel(f'Time ({x_unit})')
    if ls.UseActual:
        if q.size == p.size:
            ax.set_ylabel('kW, kvar')
        else:
            ax.set_ylabel('kW')
    else:
        ax.set_ylabel('p.u.')

    ax.grid(ls='--')
    if q.size == p.size:
        ax.legend()
    plt.tight_layout()


node_re = re.compile(r'(.*?)(\.[0-9])*$')


def remove_nodes(bus):
    match = node_re.match(bus)
    return match.group(1)

# def remove_nodes2(bus):
    # dot_pos = bus.find('.')
    # if dot_pos == -1: 
        # return bus
        
    # return bus[:dot_pos]

def get_branch_data(DSS, branch_objects, bus_coords, do_values=pqNone, do_switches=False, idxs=None, single_ph_line_style =1, three_ph_line_style=1):
    line_count = branch_objects.Count if not idxs else len(idxs)
    lines = np.empty(shape=(line_count, 2, 2), dtype=np.float64)
    lines.fill(np.nan)
    values = np.empty(shape=(line_count, ), dtype=np.float64)
    values.fill(np.nan)
    lines_styles = np.zeros(shape=(line_count,), dtype=np.int8)

    element = DSS.ActiveCircuit.ActiveCktElement

    if do_switches:
        switch_idxs = []
        isolated_idxs = []
        extra = [switch_idxs, isolated_idxs]
    else:
        extra = []
    # def get_buses_line(l):
        # b1 = remove_nodes(l.Bus1)
        # b2 = remove_nodes(l.Bus2)

    offset = 0
    skip = set()

    # norm_min_volts = DSS.ActiveCircuit.Settings.NormVminpu
    # norm_max_volts = DSS.ActiveCircuit.Settings.NormVmaxpu
    # emerg_min_volts = DSS.ActiveCircuit.Settings.EmergVminpu
    # emerg_max_volts = DSS.ActiveCircuit.Settings.EmergVmaxpu
    
    vbs = None
    if do_values == pqCurrent:
        #max_currents = dict(zip(DSS.ActiveCircuit.PDElements.AllNames, DSS.ActiveCircuit.PDElements.AllMaxCurrents(True)))
        max_currents = dict(zip(DSS.ActiveCircuit.PDElements.AllNames, DSS.ActiveCircuit.PDElements.AllPctNorm(True)))
    elif do_values == pqCapacity:
        capacities = dict(zip(DSS.ActiveCircuit.PDElements.AllNames, DSS.ActiveCircuit.PDElements.AllPctNorm(True)))
    elif do_values == pqVoltage:
        node_volts = dict(zip(DSS.ActiveCircuit.AllNodeNames, DSS.ActiveCircuit.AllBusVmag * 1e-3))
        vbs = np.empty(shape=(line_count, ), dtype=np.float64)
        vbs.fill(0)
        extra.append(vbs)
    
    if idxs:
        l = branch_objects
        for idx in idxs:
            l.idx = idx
            buses = element.BusNames
            b1 = remove_nodes(buses[0])
            b2 = remove_nodes(buses[1])
            
            fr = bus_coords.get(b1)
            to = bus_coords.get(b2)
            
            if fr is None or to is None:
                skip.add(idx)
                continue
                
            lines[offset, 0] = fr
            lines[offset, 1] = to
            offset += 1
            
        if do_values == pqNone:
            return lines[:offset]
            
        offset = 0
        for idx in idxs:
            if idx in skip:
                continue
                
            l.idx = idx
            
            if do_values == pqPower:
                values[offset] = np.abs(element.TotalPowers[0])
            elif do_values == pqLosses:
                values[offset] = abs(element.Losses[0]) / l.Length
            elif do_values == pqVoltage:
                b2name = nodot(l.Bus2)
                b = DSS.ActiveCircuit.Buses[b2name]
                vb = b.kVBase
                vbs[offset] = vb
                value = 1e30
                if vb > 0:
                    for n in b.Nodes:
                        if n > 0 and n <= 3:
                            value = min(value, node_volts[f'{b2name}.{n}'] / vb)
                            
                values[offset] = value
            elif do_values == pqCurrent:
                values[offset] = max_currents.get(element.Name, np.NaN)
            elif do_values == pqCapacity:
                values[offset] = capacities.get(element.Name, np.NaN)
                        
            offset += 1
        
        return lines[:offset], values[:offset]
    
    else:
        for i, l in enumerate(branch_objects):
            buses = element.BusNames
            b1 = remove_nodes(buses[0])
            b2 = remove_nodes(buses[1])
            
            fr = bus_coords.get(b1)
            to = bus_coords.get(b2)
            
            if fr is None or to is None or not element.Enabled:
                skip.add(i)
                continue

            if do_switches:
                if element.IsIsolated:
                    isolated_idxs.append(offset)
                if l.IsSwitch:
                    #skip.add(i)
                    switch_idxs.append(offset)
                    #continue

            lines[offset, 0] = fr
            lines[offset, 1] = to

            offset += 1
            
        if do_values == pqNone:
            return [lines[:offset], None, None] + extra
            
        offset = 0

        for i, l in enumerate(branch_objects):
            if i in skip:
                continue
                
            if do_values == pqPower:
                values[offset] = np.abs(element.TotalPowers[0])
            elif do_values == pqLosses:
                values[offset] = abs(element.Losses[0]) / l.Length
            elif do_values == pqVoltage:
                b2name = nodot(l.Bus2)
                b = DSS.ActiveCircuit.Buses[b2name]
                vb = b.kVBase
                vbs[offset] = vb
                value = 1e30

                if l.Phases < 3:
                    lines_styles[offset] = 1

                if vb > 0:
                    for n in b.Nodes:
                        if n > 0 and n <= 3:
                            value = min(value, node_volts[f'{b2name}.{n}'] / vb)
                            
                values[offset] = value
            elif do_values == pqCurrent:
                values[offset] = max_currents.get(element.Name, np.NaN)
            elif do_values == pqCapacity:
                values[offset] = capacities.get(element.Name, np.NaN)
            
            lines_styles[offset] = single_ph_line_style if l.Phases == 1 else three_ph_line_style
            offset += 1
        
        return [lines[:offset], values[:offset], lines_styles[:offset]] + extra
    

def get_point_data(DSS: IDSS, point_objects, bus_coords, do_values=False):
    if isinstance(point_objects, str):
        cls = point_objects
        DSS.SetActiveClass(cls)
        point_objects = DSS.ActiveClass
    
    point_count = point_objects.Count

    points = np.empty(shape=(point_count, 2), dtype=np.float64)
    values = np.empty(shape=(point_count, ), dtype=np.float64)

    offset = 0
    skip = set()
    element = DSS.ActiveCircuit.ActiveCktElement
    for i, _ in enumerate(point_objects):
        buses = element.BusNames
        all_coords = []
        buses = [remove_nodes(b) for b in buses]
        all_coords = [c for c in (bus_coords.get(b) for b in buses) if c]
        
        if not all_coords:
            skip.add(i)
            continue

        coords = tuple(sum(c) / len(all_coords) for c in zip(*all_coords)) 
            
        points[offset] = coords
        offset += 1
        
    if not do_values:
        return points[:offset]
        
    offset = 0
    for i, _ in enumerate(point_objects):
        if i in skip:
            continue
            
        values[offset] = np.abs(element.TotalPowers[0])
        offset += 1
    
    return points[:offset], values[:offset]


def dss_profile_plot(DSS, params):
    if len(DSS.ActiveCircuit.Meters) == 0:
        raise RuntimeError(f"An EnergyMeter is required to use 'plot profile'")

    PhasesToPlot = params['PhasesToPlot']
    ProfileScale = params['ProfileScale']
    
    vmin = DSS.ActiveCircuit.Settings.NormVminpu
    vmax = DSS.ActiveCircuit.Settings.NormVmaxpu
    if ProfileScale == '120kft':
        xlabel = 'Distance (kft)'
        ylabel = '120 Base Voltage'
        DenomLN = 1.0 / 120.0
        # DenomLL = 1.732 / 120.0
        LenScale = 3.2809
        # RangeScale = 120.0
    else:
        xlabel = 'Distance (km)'
        ylabel = 'p.u. Voltage'
        DenomLN = 1.0
        # DenomLL = 1.732
        LenScale = 1.0
        # RangeScale = 1.0

    busnode_to_index = {(bn.rsplit('.', 1)[0], int(bn.rsplit('.', 1)[1])): num for (num, bn) in enumerate(DSS.ActiveCircuit.AllNodeNames)}
    bus_to_kvbase = {b.Name: b.kVBase for b in DSS.ActiveCircuit.Buses}
    puV = DSS.ActiveCircuit.AllBusVmagPu / DenomLN
    distances = {name: d for (name, d) in zip(DSS.ActiveCircuit.AllBusNames, DSS.ActiveCircuit.AllBusDistances * LenScale)}
    linewidths = []
    segments = []
    colors = []
    linestyles = []
    seg_phases = []
    pri_only = (PhasesToPlot == PROFILEALLPRI)
    if PhasesToPlot in [PROFILEALL, PROFILEALLPRI, PROFILE3PH]:
        phases = (1, 2, 3)
    else:
        phases = PhasesToPlot
        try:
            _ = iter(phases)
        except:
            phases = [phases]
        
    for em in DSS.ActiveCircuit.Meters:
        branch_names = em.AllBranchesInZone
        br: str
        for br in branch_names:
            if not br.startswith('Line.'):
                continue

            ls = '-'
            lw = 2

            DSS.ActiveCircuit.Lines.Name = br[len('Line.'):]

            if PROFILE3PH == PhasesToPlot and DSS.ActiveCircuit.Lines.Phases < 3:
                continue

            bus1 = nodot(DSS.ActiveCircuit.Lines.Bus1)
            bus2 = nodot(DSS.ActiveCircuit.Lines.Bus2)

             # Plot all phases present (between 1 and 3)
            for iphs in phases:
                try:
                    b1n_idx = busnode_to_index[(bus1, iphs)]
                    b2n_idx = busnode_to_index[(bus2, iphs)]
                except:
                    continue

                if bus_to_kvbase[bus1] < 1.0:
                    if pri_only:
                        continue
                    ls = ':'
                    lw = 1

                segments.append(((distances[bus1], puV[b1n_idx]), (distances[bus2], puV[b2n_idx])))
                colors.append(Colors[iphs - 1])
                seg_phases.append(iphs)
                linestyles.append(ls)
                linewidths.append(lw)
                #TODO: NodeMarkerCode, NodeMarkerWidth

    if include_3d in ('both', '2d'):
        fig = plt.figure()#figsize=(9, 5))
        ax = fig.add_subplot(1, 1, 1)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        if PhasesToPlot in (PROFILELL3PH, PROFILELLALL, PROFILELLPRI):
            ax.set_title('L-L Voltage Profile')
        else:
            ax.set_title('L-N Voltage Profile')
        

        lc = LineCollection(segments, linewidth=linewidths, colors=colors, linestyles=linestyles)

        # ax.set_title('{}:{}, max: {:3g}'.format(DSS.ActiveCircuit.Name, quantity, quantity_max_value))
        ax.get_xaxis().get_major_formatter().set_scientific(False)
        ax.get_yaxis().get_major_formatter().set_scientific(False)
        ax.add_collection(lc)
        ax.autoscale_view()
        ax.axhline(vmin, color='darkred', ls='-', lw=3)
        ax.axhline(vmax, color='darkred', ls='-', lw=3)
        ax.grid(ls='--')
        plt.tight_layout()
       
    if include_3d in ('both', '3d'):
        fig2 = plt.figure()#figsize=(7, 7))
        ax2 = fig2.add_subplot(1, 1, 1, projection='3d')
        ax2.set_xlabel(xlabel)
        ax2.set_ylabel(ylabel)
        if PhasesToPlot in (PROFILELL3PH, PROFILELLALL, PROFILELLPRI):
            ax2.set_title('L-L Voltage Profile')
        else:
            ax2.set_title('L-N Voltage Profile')

        segments_3d = [
            [(*p, ph) for p in seg] for seg, ph in zip(segments, seg_phases)
        ]
        rseg = np.ravel(segments)
        max_x = np.max(rseg[::2])
        max_y = np.max(rseg[1::2])
        min_y = np.min(rseg[1::2])
        lc3d = Line3DCollection(segments_3d, colors=colors, linestyles=linestyles)
        ax2.add_collection(lc3d)
        ax2.set_xlabel(xlabel)
        ax2.set_ylabel(ylabel)
        ax2.set_zlabel('Phase')
        xl = [0, max_x]
        yl = [min(min_y, vmin) - 0.05, min(max_y, vmax) + 0.05]
        maxph = np.max(seg_phases) + 1
        ax2.set_xlim(xl)
        ax2.set_ylim(yl)
        ax2.set_zlim(0, maxph)
        ax2.plot_surface(
            np.array([xl, xl]), 
            np.array([[vmax, vmax]] * 2), 
            np.array([[0, 0], [maxph, maxph]]),
            color='k', 
            alpha=0.5
        )
        ax2.plot_surface(
            np.array([xl, xl]), 
            np.array([[vmin, vmin]] * 2), 
            np.array([[0, 0], [maxph, maxph]]),
            color='k', 
            alpha=0.5
        )
        ax2.autoscale_view()



def get_gic_line_data(DSS: IDSS, bus_coords, single_ph_line_style=1, three_ph_line_style=1):
    branch_objects = DSS.Obj.GICLine    
    line_count = len(branch_objects)# if not idxs else len(idxs)
    lines = np.empty(shape=(line_count, 2, 2), dtype=np.float64)
    lines.fill(np.nan)
    values = np.empty(shape=(line_count, ), dtype=np.float64)
    values.fill(np.nan)
    lines_styles = np.zeros(shape=(line_count,), dtype=np.int8)
    offset = 0
    # skip = set()

    # GIC lines are not exposed nicely in the classic API, so we'll use the new Obj API
    for gic_line in DSS.Obj.GICLine:
        if not gic_line.enabled:
            continue

        b1 = remove_nodes(gic_line.bus1)
        b2 = remove_nodes(gic_line.bus2)
        fr = bus_coords.get(b1)
        to = bus_coords.get(b2)
            
        if fr is None or to is None:
            # skip.add(idx)
            continue
            
        lines[offset, 0] = fr
        lines[offset, 1] = to

        lines_styles[offset] = single_ph_line_style if gic_line.phases == 1 else three_ph_line_style
        max_current = DSS._lib.Obj_CktElement_MaxCurrent(gic_line._ptr, 1)
        values[offset] = max_current
        offset += 1

    return lines[:offset], values[:offset], lines_styles[:offset]

def dss_circuit_plot(DSS: IDSS, params={}, fig=None, ax=None, is3d=False):
    quantity = str_to_pq.get(params.get('Quantity', None), pqNone)
    dots = params.get('Dots', False)
    color1 = params.pop('Color1', Colors[0])
    color2 = params.pop('Color2', Colors[1])
    color3 = params.pop('Color3', Colors[2])
    single_ph_line_style = params.get('SinglePhLineStyle', 1)
    three_ph_line_style = params.get('ThreePhLineStyle', 1)
    max_lw = params.get('MaxLineThickness', 5)
    bus_markers = params.get('BusMarkers', [])
    do_labels = params.get('Labels', False)


    norm_min_volts = DSS.ActiveCircuit.Settings.NormVminpu
    # norm_max_volts = DSS.ActiveCircuit.Settings.NormVmaxpu
    emerg_min_volts = DSS.ActiveCircuit.Settings.EmergVminpu
    # emerg_max_volts = DSS.ActiveCircuit.Settings.EmergVmaxpu
    
    # bus_coords = dict((b.Name, (b.x, b.y)) for b in DSS.ActiveCircuit.Buses if (b.x, b.y) != (0.0, 0.0))
    bus_coords = dict((b.Name, (b.x, b.y)) for b in DSS.ActiveCircuit.Buses if b.Coorddefined)
    
    if fig is None:
        fig = plt.figure()#figsize=(8, 7))
        
    given_ax = ax is not None
    if not given_ax:
        ax = plt.gca()
    else:
        plt.sca(ax)

    if not is3d:
        ax.set_aspect('equal', 'datalim')

    lines_lines, lines_values, lines_styles, switch_idxs, isolated_idxs, *extra = get_branch_data(
        DSS, 
        DSS.ActiveCircuit.Lines, 
        bus_coords, 
        do_values=quantity, 
        do_switches=True, 
        single_ph_line_style=single_ph_line_style, 
        three_ph_line_style=three_ph_line_style
    )
    
    if isolated_idxs:
        line_idx = isolated_idxs
        if not is3d:
            ax.add_collection(LineCollection(lines_lines[line_idx, :], linewidths=1, linestyle='-', color='#ff00ff', capstyle='round'))

    if switch_idxs:
        line_idx = switch_idxs
        if not is3d:
            ax.add_collection(LineCollection(lines_lines[line_idx, :], linewidths=1, linestyle='-', color='#000000', capstyle='round'))

    switch_idxs = set(switch_idxs)
    isolated_idxs = set(isolated_idxs)
    #lc_lines = LineCollection(lines_lines, linewidths=0.5, color=color1)# + 3 * lines_values / np.max(lines_values), linestyle='solid', color=color1)
    try:
        quantity_max_value = params.pop('MaxScale')
    except:
        quantity_max_value = 0

    quantity_suffix = ''

    if lines_lines is not None and len(lines_lines) > 0:
        if quantity in (pqVoltage,):
            colors = []
            for v in lines_values:
                if v > norm_min_volts or np.isnan(v):
                    colors.append(color1)
                elif v > emerg_min_volts:
                    colors.append(color2)
                else:
                    colors.append(color3)
            
            
            for ls in set(lines_styles):
                line_idx = [i for i, c in enumerate(lines_styles) if c == ls and i not in isolated_idxs and i not in switch_idxs]
                if not is3d:
                    edgecolors = [colors[i] for i in line_idx]
                    ax.add_collection(LineCollection(lines_lines[line_idx, :], linewidths=1, linestyle=LINES_STYLE_CODE.get(ls, 'solid'), color=edgecolors, capstyle='round'))
                    if dots:
                        ax.scatter(lines_lines[line_idx, 0, 0].ravel(), lines_lines[line_idx, 0, 1].ravel(), marker='o', facecolors='none', edgecolors=edgecolors, s=9, lw=1)
                        ax.scatter(lines_lines[line_idx, 1, 0].ravel(), lines_lines[line_idx, 1, 1].ravel(), marker='o', facecolors='none', edgecolors=edgecolors, s=9, lw=1)

            # if is3d:
            #     ax.add_collection(Line3DCollection(lines_lines, linewidths=1, linestyle='-', color=[colors[i] for i in line_idx], capstyle='round'))
            #     ax.set_xlim(np.min(lines_lines_3d[:, :, 0]), np.max(lines_lines_3d[:, :, 0]))
            #     ax.set_ylim(np.min(lines_lines_3d[:, :, 1]), np.max(lines_lines_3d[:, :, 1]))

            quantity_max_value = 0
        elif quantity in (pqLosses,):
            
            if quantity_max_value == 0:
                # quantity_max_value = max(lines_values) * 1e-3
                # For compatibility with the official version, loop through all lines instead 
                # of the actual plotted lines
                element = DSS.ActiveCircuit.ActiveCktElement
                quantity_max_value = max(
                    abs(element.Losses[0] / line.Length)
                    for line in DSS.ActiveCircuit.Lines 
                    if element.Enabled
                ) * 0.001

            lines_values = np.clip(3 * 1e-3 * lines_values / quantity_max_value, 0.5, max_lw)
            if not is3d:
                for ls in set(lines_styles):
                    line_idx = [i for i, c in enumerate(lines_styles) if c == ls and i not in isolated_idxs and i not in switch_idxs]
                    # edgecolors = [colors[i] for i in line_idx]
                    ax.add_collection(LineCollection(lines_lines[line_idx, :], linewidths=lines_values[line_idx], linestyle=LINES_STYLE_CODE.get(ls, 'solid'), color=color1, capstyle='round'))
                    if dots:
                        ax.scatter(lines_lines[line_idx, 0, 0].ravel(), lines_lines[line_idx, 0, 1].ravel(), marker='o', facecolors='none', edgecolors=color1, s=9, lw=1)
                        ax.scatter(lines_lines[line_idx, 1, 0].ravel(), lines_lines[line_idx, 1, 1].ravel(), marker='o', facecolors='none', edgecolors=color1, s=9, lw=1)

        elif quantity in (pqCurrent, pqCapacity):
            line_idx = [i for i in range(lines_lines.shape[0]) if i not in isolated_idxs and i not in switch_idxs]
            colors = [color3 if v > 100 and not np.isnan(v) else color1 for v in lines_values[line_idx]]

            if quantity_max_value == 0:
                quantity_max_value = max(lines_values)

            lines_values = np.clip(3 * lines_values / quantity_max_value, 0.5, max_lw)
            if not is3d:
                ax.add_collection(LineCollection(lines_lines[line_idx, :], linewidths=lines_values[line_idx], linestyle='-', color=colors, capstyle='round'))
                if dots:
                    ax.scatter(lines_lines[line_idx, 0, 0].ravel(), lines_lines[line_idx, 0, 1].ravel(), marker='o', facecolors='none', edgecolors=colors, s=9, lw=1)
                    ax.scatter(lines_lines[line_idx, 1, 0].ravel(), lines_lines[line_idx, 1, 1].ravel(), marker='o', facecolors='none', edgecolors=colors, s=9, lw=1)

        elif quantity != pqNone:
            if quantity == pqPower:
                quantity_suffix = ' kW'
                if quantity_max_value == 0:
                    #lines_values *= 1e-3

                    # For compatibility with the official version, loop through all lines instead 
                    # of the actual plotted lines
                    element = DSS.ActiveCircuit.ActiveCktElement
                    
                    quantity_max_value = max(
                        element.TotalPowers[0]
                        for _ in DSS.ActiveCircuit.Lines
                        if element.Enabled
                    ) #* 0.001
            else:
                #TODO:may need workaround about GeneralPlotQuantity
                quantity_max_value = max(lines_values)

            for ls in set(lines_styles):
                line_idx = [i for i, c in enumerate(lines_styles) if c == ls and i not in isolated_idxs and i not in switch_idxs]
                if not is3d:
                    ax.add_collection(LineCollection(
                        lines_lines[line_idx, :], 
                        linewidths=np.clip(0.5 + 3 * lines_values[line_idx] / quantity_max_value, 0.5, max_lw), 
                        linestyle=LINES_STYLE_CODE.get(ls, 'solid'), 
                        color=color1,
                        capstyle='round'
                    ))
                    if dots:
                        ax.scatter(lines_lines[line_idx, 0, 0].ravel(), lines_lines[line_idx, 0, 1].ravel(), marker='o', facecolors='none', edgecolors=color1, s=9, lw=1)
                        ax.scatter(lines_lines[line_idx, 1, 0].ravel(), lines_lines[line_idx, 1, 1].ravel(), marker='o', facecolors='none', edgecolors=color1, s=9, lw=1)
        else:
            #TODO: handle 1 and 3 phase, etc.?
            if not is3d:
                ax.add_collection(LineCollection(lines_lines, linewidths=1, linestyle='-', color=color1, capstyle='round'))
            # else:
            #     ax.add_collection(Line3DCollection(lines_lines, linewidths=1, linestyle='-', color=color1, capstyle='round'))
            #     ax.set_xlim(np.min(lines_lines[:, :, 0]), np.max(lines_lines[:, :, 0]))
            #     ax.set_ylim(np.min(lines_lines[:, :, 1]), np.max(lines_lines[:, :, 1]))

    transformers_lines, *_ = get_branch_data(DSS, DSS.ActiveCircuit.Transformers, bus_coords)

    if not is3d:
        lc_transformers = LineCollection(transformers_lines, linewidth=3, linestyle='solid', color='gray')
        ax.add_collection(lc_transformers)

    lines_lines, lines_values, lines_styles, *_ = get_gic_line_data(DSS, bus_coords, single_ph_line_style=single_ph_line_style, three_ph_line_style=three_ph_line_style)
    if len(lines_lines) != 0:
        if quantity_max_value == 0:
            quantity_max_value = max(lines_values)

        lines_values = np.clip(3 * lines_values / quantity_max_value, 0.5, max_lw)
        for ls in set(lines_styles):
            line_idx = [i for i, c in enumerate(lines_styles) if c == ls]
            ax.add_collection(LineCollection(lines_lines[line_idx, :], linewidths=lines_values[line_idx], linestyle=LINES_STYLE_CODE.get(ls, 'solid'), color=color1, capstyle='round'))
            if dots:
                ax.scatter(lines_lines[line_idx, 0, 0].ravel(), lines_lines[line_idx, 0, 1].ravel(), marker='o', facecolors='none', edgecolors=color1, s=9, lw=1)
                ax.scatter(lines_lines[line_idx, 1, 0].ravel(), lines_lines[line_idx, 1, 1].ravel(), marker='o', facecolors='none', edgecolors=color1, s=9, lw=1)



    # 'Daisysize'
    # 'Markercode', 'Nodewidth' # NodeMarkerCode
    
    branch_marker_options = [
        ('MarkSwitches', 'SwitchMarkerCode', None, DSS.ActiveCircuit.Lines, switch_idxs),
        ('MarkFuses', 'FuseMarkerCode', 'FuseMarkerSize', DSS.ActiveCircuit.Fuses, None),
        ('MarkRegulators', 'RegMarkerCode', 'RegMarkerSize', DSS.ActiveCircuit.RegControls, None),
        ('MarkRelays', 'RelayMarkerCode', 'RelayMarkerSize', DSS.ActiveCircuit.Relays, None),
        ('MarkReclosers', 'RecloserMarkerCode', 'RecloserMarkerSize', DSS.ActiveCircuit.Reclosers, None)
    ]
    
    point_marker_options = [    
        ('MarkTransformers', 'TransMarkerCode', 'TransMarkerSize', DSS.ActiveCircuit.Transformers, None),
        ('MarkCapacitors', 'CapMarkerCode', 'CapMarkerSize', DSS.ActiveCircuit.Capacitors, None),
        ('MarkPVSystems', 'PVMarkerCode', 'PVMarkerSize', DSS.ActiveCircuit.PVSystems, None),
        ('MarkStorage', 'StoreMarkerCode', 'StoreMarkerSize', 'Storage', None),
    ]

    pmarkers = params.pop('Markers', None)
    if pmarkers is not None:
        for (mark_opt, code_opt, size_opt, objs, idxs) in branch_marker_options:
            # print(mark_opt, pmarkers[mark_opt])
            if not pmarkers[mark_opt]:
                continue
                
            marker_code = pmarkers[code_opt]
            marker_size = pmarkers[size_opt]
            #TODO: use marker_size?
            marker_dict = get_marker_dict(marker_code)
            if mark_opt == 'MarkRegulators':
                for obj in objs:
                    DSS.ActiveCircuit.Transformers.Name = obj.Transformer
                    bus = remove_nodes(DSS.ActiveCircuit.ActiveCktElement.BusNames[obj.Winding - 1])
                    coords = bus_coords.get(bus)
                    if coords is None:
                        continue
                    ax.plot(*coords, color='red', **marker_dict)
            
            else:
                #TODO? branch_lines = get_branch_data(DSS, objs, bus_coords, idxs=idxs)
                pass
            
            
        for (mark_opt, code_opt, size_opt, objs, idxs) in point_marker_options:
            if not pmarkers[mark_opt]:
                continue
                
            marker_code = pmarkers[code_opt]
            marker_size = pmarkers[size_opt]
            
            points = get_point_data(DSS, objs, bus_coords)
            
    #        if marker_code not in MARKER_MAP:
                #marker_code = 25
                
            marker_dict = get_marker_dict(marker_code)
            #marker_dict['markersize'] *= (marker_size / 2.0)**2
            marker_dict['markersize'] *= (marker_size / 1.2)**2
            
            #marker_dict['marker'] = marker_dict['marker'].vertices
            #marker_dict.pop('markersize')
            #marker_dict.pop('markerfacecolor')
    #         print(mark_opt, marker_dict['marker'])
    #         pprint(marker_dict)
            ax.plot(points[:, 0], points[:, 1], ls='', color='red', **marker_dict)
            #ax.plot(points[:, 0], points[:, 1], color='red', ls='', marker=6, alpha=1)

    for bus_marker in bus_markers:
        name = bus_marker['Name']
        bus = DSS.ActiveCircuit.Buses[name]
        if not bus.Coorddefined:
            raise RuntimeError('Bus markers: coordinates are not defined for bus "{name}"')

        marker_dict = get_marker_dict(bus_marker['Code'])
        marker_size = bus_marker['Size']
        marker_dict['markersize'] *= (marker_size / 6)
        ax.plot(bus.x, bus.y, ls='', color=bus_marker['Color'], **marker_dict)


    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    if not given_ax:       
        if quantity != pqNone:
            ax.set_title('{}:{}, max={:g}{}'.format(DSS.ActiveCircuit.Name.upper(), quantity_str[quantity], quantity_max_value, quantity_suffix))
        ax.autoscale_view()
        ax.get_xaxis().get_major_formatter().set_scientific(False)
        ax.get_yaxis().get_major_formatter().set_scientific(False)
        plt.tight_layout()

        if do_labels:
            coords_to_names = {}
            for name, coords in bus_coords.items():
                prev = coords_to_names.get(coords)
                if prev:
                    coords_to_names[coords] = prev + ',' + name
                else:
                    coords_to_names[coords] = name

            for coords, name in coords_to_names.items():
                ax.text(*coords, name, zorder=11, fontsize='xx-small', va='center', clip_on=True)

    

def dss_scatter_plot(DSS, params):
    x = np.empty(shape=(DSS.ActiveCircuit.NumBuses, ))
    y = np.empty(shape=(DSS.ActiveCircuit.NumBuses, ))
    vcomplex = np.empty(shape=(DSS.ActiveCircuit.NumBuses, 3), dtype=complex)
    x.fill(np.nan)
    y.fill(np.nan)
    vcomplex.fill(np.nan)
    for idx, b in enumerate(DSS.ActiveCircuit.Buses):
        if not b.Coorddefined:
            continue

        x[idx] = b.x
        y[idx] = b.y
        vnodes = b.puVoltages.view(dtype=complex)
        nnodes = min(3, len(vnodes))
        vcomplex[idx, :nnodes] = vnodes[:nnodes]
    
    vabs = np.abs(vcomplex)
    del vcomplex
    vmean = np.mean(vabs, axis=1, where=np.isfinite(vabs))

    if include_3d in ('both', '2d'):
        fig, ax = plt.subplots(1, 1, constrained_layout=True)#, figsize=(8, 7))
        dss_circuit_plot(DSS, fig=fig, ax=ax, params={})
        ax.get_xaxis().get_major_formatter().set_scientific(False)
        ax.get_yaxis().get_major_formatter().set_scientific(False)
        sc = ax.scatter(x, y, c=vmean)
        fig.colorbar(sc, label='V1 (pu)')
        ax.set_title('{}:{}'.format(DSS.ActiveCircuit.Name.upper(), 'Voltage magnitude'))
    
    if include_3d in ('both', '3d'):
        bus_coords = {}
        for idx, b in enumerate(DSS.ActiveCircuit.Buses):
            if b.Coorddefined:
                bus_coords[b.Name] = (b.x, b.y, vmean[idx])

        fig = plt.figure()#figsize=(7, 7))
        ax = fig.add_subplot(projection='3d')
        dss_circuit_plot(DSS, fig=fig, ax=ax, params={}, is3d=True)
        ax.get_xaxis().get_major_formatter().set_scientific(False)
        ax.get_yaxis().get_major_formatter().set_scientific(False)

        # if is3d:
        #     ax.add_collection(Line3DCollection(lines_lines, linewidths=1, linestyle='-', color=[colors[i] for i in line_idx], capstyle='round'))
        #     ax.set_xlim(np.min(lines_lines_3d[:, :, 0]), np.max(lines_lines_3d[:, :, 0]))
        #     ax.set_ylim(np.min(lines_lines_3d[:, :, 1]), np.max(lines_lines_3d[:, :, 1]))

        sc = ax.scatter(x, y, vmean, c='k', s=2)

        segs = []
        el = DSS.ActiveCircuit.ActiveCktElement
        for pd in DSS.ActiveCircuit.PDElements:
            buses = el.BusNames
            if len(buses) != 2:
                continue

            seg = []
            for b in buses:
                c = bus_coords.get(nodot(b), None)
                if c is not None:
                    seg.append(c)

            if len(seg) == 2:
                segs.append(seg)

        segs = np.array(segs, dtype=float)
        seg_v = (segs[:, 0, 2] + segs[:, 1, 2]) / 2
        lc3d = Line3DCollection(segs)
        ax.add_collection(lc3d)
        lc3d.set_array(seg_v)
        #fig.colorbar(sc, label='V1 (pu)')
        ax.set_title('{}:{}'.format(DSS.ActiveCircuit.Name.upper(), 'Voltage magnitude'))


def dss_visualize_plot(DSS, params):
    XMAX = 300
    #pprint(params)
    quantity = params['Quantity']

    # Fix for backend v0.13.1
    quantity = {
        'Power': 'Powers',
        'Current': 'Currents',
        'Voltage': 'Voltages',
    }.get(quantity, quantity)

    element = DSS.ActiveCircuit.ActiveCktElement
    etype, ename = params['ElementType'], params['ElementName']
    nconds = element.NumConductors
    # nphases = element.NumPhases
    buses = element.BusNames[:2] # max 2 terminals
    vbases = [max(1, 1000 * DSS.ActiveCircuit.Buses[nodot(b)].kVBase) for b in buses]

    # assert DSS.ActiveCircuit.ActiveCktElement.Name == params['ElementType'] + '.' + params['ElementName']
    fig, ax = plt.subplots(1, gridspec_kw=dict(left=0.05, right=0.95, bottom=0.05, top=0.92))#, figsize=(8.6, 7))
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.grid(False)

    y = 20 + 10 * nconds
    box_xy0 = np.array([100, 10])
    box_xy1 = np.array([XMAX - 100, y])
    box_wh = box_xy1 - box_xy0
    middle_box = Rectangle(box_xy0, *box_wh, facecolor='lightgray', edgecolor='k')
    ax.text(XMAX / 2, 10 + (y - 10) / 2, f'{etype}.{ename.upper()}', ha='center', va='center', fontweight='bold', rotation='vertical')
    ax.add_patch(middle_box)
    ax.plot([0, 300], [0, 0], color='gray', lw=7)
    
    ax.plot([-5] * 2, [5, y - 5], color='k', lw=7)
    ax.text(25, y, buses[0].upper(), ha='left')
    if len(buses) > 1:
        ax.plot([XMAX + 5] * 2, [5, y - 5], color='k', lw=7)
        ax.text(XMAX - 25, y, buses[1].upper(), ha='right')
    
    voltage = (quantity == 'Voltages')

    if quantity == 'Powers':
        values = 1e-3 * (element.Voltages.view(dtype=complex) * np.conj(element.Currents.view(dtype=complex)))
        unit = 'kVA'
    elif voltage:
        values = element.Voltages.view(dtype=complex)
        unit = 'pu'
    elif quantity == 'Currents':
        values = element.Currents.view(dtype=complex)
        unit = 'A'

    ax.set_title(f'{etype}.{ename.upper()} {quantity} ({unit})')
    size = 'x-small'

    def get_text():
        v = values[bus_idx * nconds + cond]
        if quantity == 'Powers':
            arrow_text = f"{v.real:-.6g} {'-' if v.imag < 0 else '+'} j{abs(v.imag):g}"
        else:
            if quantity == 'Voltages':
                v /= vbase
            arrow_text = f"{np.abs(v):-.6g} {unit} ∠ {np.angle(v, deg=True):.2f}°"

        return arrow_text

    for bus_idx, vbase in enumerate(vbases):
        for cond in range(nconds):
            if cond < (nconds - 1):
                weight = 'bold'
                lw = 2
            else:
                weight = 'normal'
                lw = 0.6667

            if bus_idx:
                arrow_x = XMAX + 5
                arrow_y = y - (cond + 1) * 10.0
                dx = box_xy1[0] - arrow_x
                ax.text(arrow_x - 20, arrow_y + 2, get_text(), ha='right', fontweight=weight, size=size)
                if voltage:
                    plt.plot([arrow_x, dx + arrow_x], [arrow_y, arrow_y], color='k', lw=lw*1.5)
                    x = XMAX - 4 * (cond) - 1
                    ax.annotate('', xy=(x, arrow_y), xytext=(x, 0), arrowprops=dict(width=0.2, color='lightgray'))
                else:
                    ax.annotate('', xytext=(arrow_x, arrow_y), xy=(dx + arrow_x, arrow_y), arrowprops=dict(width=lw, color='k'))
                    
            else:
                arrow_x = -5
                arrow_y = y - (cond + 1) * 10.0
                dx = box_xy0[0] + 5
                ax.text(arrow_x + 20, arrow_y + 2, get_text(), ha='left', fontweight=weight, size=size)
                if voltage:
                    plt.plot([arrow_x, dx + arrow_x], [arrow_y, arrow_y], color='k', lw=lw*1.5)
                    x = 4 * (cond) + 1
                    ax.annotate('', xy=(x, arrow_y), xytext=(x, 0), arrowprops=dict(width=0.2, color='lightgray'))
                else:
                    ax.annotate('', xytext=(arrow_x, arrow_y), xy=(dx + arrow_x, arrow_y), arrowprops=dict(width=lw, color='k'))

        if quantity == 'Currents': 
            # Residual
            v = -np.sum(values[(nconds * bus_idx):(nconds * (bus_idx + 1))])
            txt = f"{np.abs(v):-.6g} A ∠ {np.angle(v, deg=True):.2f}°"

            if bus_idx:
                arrow_x = XMAX + 5
                arrow_y = -10
                dx = box_xy1[0] - arrow_x
                ax.text(arrow_x - 5, arrow_y + 2, txt, ha='right', fontweight='normal', size=size)
                ax.annotate('', xytext=(arrow_x, arrow_y), xy=(dx + arrow_x, arrow_y), arrowprops=dict(width=1, color='k'))
            else:
                arrow_x = -5
                arrow_y = -10
                dx = box_xy0[0] + 5
                ax.text(arrow_x + 5, arrow_y + 2, txt, ha='left', fontweight='normal', size=size)
                ax.annotate('', xytext=(arrow_x, arrow_y), xy=(dx + arrow_x, arrow_y), arrowprops=dict(width=1, color='k'))

    ax.set_xlim(-20, XMAX + 20)
    ax.set_ylim(-15, y + 5)


def dss_general_data_plot(DSS, params):
    is_general = params['PlotType'] == 'GeneralData'
    ValueIndex = max(1, params['ValueIndex'] - 1)
    fn = params['ObjectName']
    MaxScaleIsSpecified = params['MaxScaleIsSpecified']
    MinScaleIsSpecified = params['MinScaleIsSpecified']
    MaxScale = params['MaxScale']
    MinScale = params['MinScale']

    # Whenever we add Pandas as a dependency, this could be
    # rewritten to avoid all the extra/slow work
    exp = re.compile('[,=\t]')
    with open(fn, 'r') as f:
        line = f.readline().rstrip()
        field = exp.split(line)[ValueIndex].strip() #TODO: Is this right?!
        f.seek(0)
        # Find min and max
        names, vals = [], []
        for line in f:
            if not line:
                continue

            data = exp.split(line)
            name, val = data[0], data[ValueIndex]
            if len(val):
                names.append(name)
                vals.append(float(val))

    vals = np.asarray(vals)
    min_val = np.min(vals)
    max_val = np.max(vals)

    # Do some sanity checking on the numbers. Don't want to include negative numbers in autoadd plot 
    if not is_general:
        if min_val < 0.0:
            min_val = 0.0
        if max_val < 0.0:
            max_val = 0.0

    if MaxScaleIsSpecified:
        max_val = MaxScale # Override with user specified value
    if MinScaleIsSpecified:
        min_val = MinScale # Override with user specified value

    diff = max_val - min_val
    if diff == 0.0:
        diff = max_val
    if diff == 0.0:
        diff = 1.0 # Everything is zero

    sidxs = np.argsort(vals)
    bus: IBus = DSS.ActiveCircuit.ActiveBus
    data = []
    labels = []
    do_labels = params['Labels']
    colors = []
    c1 = np.asarray(matplotlib.colors.colorConverter.to_rgb(params['Color1']))
    c2 = np.asarray(matplotlib.colors.colorConverter.to_rgb(params['Color2']))
    for i in sidxs:
        name, val = names[i], vals[i]
        if DSS.ActiveCircuit.SetActiveBus(name) <= 0 or not bus.Coorddefined:
            continue

        if is_general:
            data.append((bus.x, bus.y, val))
            s = ((val - min_val) / diff)
            colors.append(c2*s + c1*(1-s))
            # InterpolateGradientColor(Color1, Color2, (GenPlotItem.Value - MinValue) / Diff),
        else: # ptAutoAddLogPlot
            data.append((bus.x, bus.y, val))
            # GetAutoColor((GenPlotItem.Value - MinValue) / Diff), 
            
        if do_labels:
            labels.append(bus.Name)

    data = np.asarray(data)


    dss_circuit_plot(DSS, params)

    #fig = plt.figure(figsize=(8, 7))
    plt.title(f'{field}, Max={max_val:.3g}')
    ax = plt.gca()
    #if not is3d:
    #ax.set_aspect('equal', 'datalim')

    ax.scatter(data[:, 0], data[:, 1], c=colors, zorder=10)
    # ax.colorbar()

    #ax.autoscale_view()
    #ax.get_xaxis().get_major_formatter().set_scientific(False)
    #ax.get_yaxis().get_major_formatter().set_scientific(False)
    #plt.tight_layout()



    # marker_code = MarkerIdx

    # NodeMarkerWidth: int
    # MarkerIdx = NodeMarkerCode

    # marker_code = pmarkers[code_opt]
    # marker_size = pmarkers[size_opt]
    #marker_dict = get_marker_dict(marker_code)
    # ax.plot(*coords, color='red', **marker_dict)
    #MarkSpecialClasses


def dss_matrix_plot(DSS, params):
    # plot_id = params.get('PlotId', None)
    if params['MatrixType'] == 'IncMatrix':
        title = 'Incidence matrix'
        data = DSS.ActiveCircuit.Solution.IncMatrix[:-1]
    else:
        title = 'Laplacian matrix'
        data = DSS.ActiveCircuit.Solution.Laplacian[:-1]

    x, y, v = data[0::3], data[1::3], data[2::3]
    m = coo.coo_matrix((v, (x, y)))
    #fig, [ax, ax2] = plt.subplots(1, 2, figsize=(8.6 * 2, 8.6), constrained_layout=True, num=title)
    
    if include_3d in ('both', '2d'):
        fig = plt.figure(constrained_layout=True)#, num=plot_id) #, figsize=(8.6, 8.6))
        ax = fig.add_subplot(1, 1, 1)
        ax.grid(True)
        ax.spy(m, marker='s', markersize=1, color=params['Color1'])
        ax.set_xlabel('Column')
        ax.set_ylabel('Row')
        ax.set_title(title)

    if include_3d in ('both', '3d'):
        fig = plt.figure()#figsize=(8.6, 8.6), num=plot_id + '_3D')
        ax2 = fig.add_subplot(1, 1, 1, projection='3d')
        ax2.scatter(x, y, v, c=v, marker='s')
        ax2.set_xlabel('Column')
        ax2.set_ylabel('Row')
        ax2.set_zlabel('Value')


def dss_daisy_plot(DSS, params):
    dss_circuit_plot(DSS, params)

    # print(params['DaisySize'])

    ax = plt.gca()
    XMIN, XMAX = ax.get_xlim()
    quantity = str_to_pq.get(params.get('Quantity', None), pqNone)
    daisy_bus_list = params['DaisyBusList']
    do_labels = params['Labels']
    daisy_size = params['DaisySize']

    ax.set_title(f'Device Locations / {quantity_str[quantity]}')
    element = DSS.ActiveCircuit.ActiveCktElement

    if len(daisy_bus_list) == 0:
        for g in DSS.ActiveCircuit.Generators:
            if element.Enabled:
                daisy_bus_list.append(element.BusNames[0])

    counts = np.zeros(shape=(DSS.ActiveCircuit.NumBuses + 1,), dtype=np.int32)
    for b in daisy_bus_list:
        idx = DSS.ActiveCircuit.SetActiveBus(b)
        if idx > 0:
            counts[idx] += 1

    radius = 0.005 * daisy_size * (XMAX - XMIN)
    lines = []
    pointx, pointy = [], []
    for bidx in np.nonzero(counts)[0]:
        bus: IBus = DSS.ActiveCircuit.Buses[int(bidx)]
        if not bus.Coorddefined:
            continue

        cnt = counts[bidx]
        angle0 = 0
        angle = np.pi * 2.0 / cnt
        for j in range(cnt):
            Xc = bus.x + 2 * radius * np.cos(angle * j + angle0)
            Yc = bus.y + 2 * radius * np.sin(angle * j + angle0)
            lines.append([(bus.x, bus.y), (Xc, Yc)])
            pointx.append(Xc)
            pointy.append(Yc)
        

    lc = LineCollection(lines, linewidth=1, colors='r')
    ax.add_collection(lc)
    ax.scatter(pointx, pointy, marker='o', color='yellow', edgecolors='red', s=100, zorder=10)

    if not do_labels:
        return

    for bidx in np.nonzero(counts)[0]:
        bus: IBus = DSS.ActiveCircuit.Buses[int(bidx)]
        if not bus.Coorddefined:
            continue

        ax.text(bus.x, bus.y, bus.Name, zorder=11, fontsize='xx-small', va='center', clip_on=True)


def unquote(field: str):
    field = field.strip()
    if field[0] == '"' and field[-1] == '"':
        return field[1:-1]
    
    return field


def dss_di_plot(DSS: IDSS, params):
    caseYear, caseName, meterName = params['CaseYear'], params['CaseName'], params['MeterName']
    plotRegisters, peakDay = params['Registers'], params['PeakDay']

    fn = os.path.join(DSS.DataPath, caseName, f'DI_yr_{caseYear}', meterName + '.csv')

    if len(plotRegisters) == 0:
        raise RuntimeError("No register indices were provided for DI_Plot")

    if not os.path.exists(fn):
        fn = fn[:-4] + '_1.csv'

    # Whenever we add Pandas as a dependency, this could be
    # rewritten to avoid all the extra/slow work
    selected_data = []
    day_data = []
    mult = 1 if peakDay else 0.001

    # If the file doesn't exist, let the exception raise
    with open(fn, 'r') as f:
        header = f.readline().rstrip()
        allRegisterNames = [unquote(field) for field in header.strip().strip(' \t,').split(',')]
        registerNames = [allRegisterNames[i] for i in plotRegisters]

        if not len(registerNames):
            raise RuntimeError("Could not find any register name in the file")

        for line in f:
            if not line:
                continue

            rawValues = line.split(',')
            selValues = [float(rawValues[0]), *(float(rawValues[i]) for i in plotRegisters)]
            if not peakDay:
                selected_data.append(selValues)
            else:
                day_data.append(selValues)
                if len(day_data) == 24:
                    max_vals = [max(x) for x in zip(*day_data)]
                    max_vals[0] = day_data[0][0]
                    day_data = []
                    selected_data.append(max_vals)

    if day_data:
        max_vals = [max(x) for x in zip(*day_data)]
        max_vals[0] = day_data[0][0]
        day_data = []
        selected_data.append(max_vals)

    vals = np.asarray(selected_data, dtype=float)
    fig, ax = plt.subplots(1)
    icolor = -1
    for idx, name in enumerate(registerNames, start=1):
        icolor += 1
        ax.plot(vals[:, 0], vals[:, idx] * mult, label=name, color=Colors[icolor % len(Colors)])

    ax.set_title(f'{caseName}, Yr={caseYear}')
    ax.set_xlabel('Hour')
    ax.set_ylabel('MW, MWh or MVA')
    ax.legend()
    ax.grid()


def _plot_yearly_case(DSS: IDSS, caseName: str, meterName: str, plotRegisters: List[int], icolor: int, ax, registerNames: List[str]):
    anyData = True
    xvalues = []
    all_yvalues = [[] for _ in plotRegisters]
    for caseYear in range(0, 21):
        fn = os.path.join(DSS.DataPath, caseName, f'DI_yr_{caseYear}', 'Totals_1.csv')
        if not os.path.exists(fn):
            continue

        with open(fn, 'r') as f:
            f.readline() # Skip the header
            # Get started - initialize Registers 1
            registerVals = [float(x) * 0.001 for x in f.readline().split(',')]
            if len(registerVals):
                xvalues.append(registerVals[7])

    if len(xvalues) == 0:
        raise RuntimeError('No data to plot')                

    for caseYear in range(0, 21):
        if meterName.lower() in ('totals', 'systemmeter', 'totals_1', 'systemmeter_1'):
            suffix = '' if meterName.endswith('_1') else '_1'
            meterName = meterName.lower().replace('totals', 'Totals').replace('systemmeter', 'SystemMeter')
            fn = os.path.join(DSS.DataPath, caseName, f'DI_yr_{caseYear}', f'{meterName}{suffix}.csv')
            searchForMeterLine = False
        else:
            fn = os.path.join(DSS.DataPath, caseName, f'DI_yr_{caseYear}', 'EnergyMeterTotals_1.csv')
            searchForMeterLine = True

        if not os.path.exists(fn):
            continue

        with open(fn, 'r') as f:
            header = f.readline()
            if len(registerNames) == 0:
                allRegisterNames = [unquote(field) for field in header.strip(' \t,').split(',')]
                registerNames.extend(allRegisterNames[i] for i in plotRegisters)

            if not searchForMeterLine:
                line = f.readline()
            else:
                for line in f:
                    label, rest = line.split(',', 1)
                    if label.strip().lower() == meterName.lower():
                        line = f'{caseYear},{rest}'
                else:
                    raise RuntimeError("Meter not found")

            registerVals = [float(x) * 0.001 for x in line.strip(' \t,').split(',')]
            if len(registerVals):
                for yvalues, idx in zip(all_yvalues, plotRegisters):
                    yvalues.append(registerVals[idx])
    
    for yvalues, idx, regName in zip(all_yvalues, plotRegisters, registerNames):
        marker_code = MARKER_SEQ[icolor % len(MARKER_SEQ)]
        ax.plot(xvalues, yvalues, label=f'{caseName}:{meterName}:{regName}', color=Colors[icolor % len(Colors)], **get_marker_dict(marker_code))
        icolor += 1

    return icolor


def dss_yearly_curve_plot(DSS: IDSS, params):
    caseNames, meterName, plotRegisters = params['CaseNames'], params['MeterName'], params['Registers']

    fig, ax = plt.subplots(1)
    icolor = 0
    registerNames = []
    for caseName in caseNames:
        icolor = _plot_yearly_case(DSS, caseName, meterName, plotRegisters, icolor, ax, registerNames)

    if icolor == 0:
        plt.close(fig)
        raise RuntimeError('No files found')
    
    fig.suptitle(f"Yearly Curves for case(s): {', '.join(caseNames)}")
    ax.set_title(f"Meter: {meterName}; Registers: {', '.join(registerNames)}", fontsize='small')
    ax.set_xlabel('Total Area MW')
    ax.set_ylabel('MW, MWh or MVA')
    ax.legend()
    ax.grid()


def dss_comparecases_plot(DSS: IDSS, params):
    print('TODO: dss_comparecases_plot', params)

def dss_zone_plot(DSS: IDSS, params):
    obj_name = params['ObjectName']
    show_loops = params['ShowLoops']
    color1 = params['Color1']
    color3 = params['Color3']
    single_ph_line_style = LINES_STYLE_CODE.get(params.get('SinglePhLineStyle', 1))
    three_ph_line_style = LINES_STYLE_CODE.get(params.get('ThreePhLineStyle', 1))
    dots = params.get('Dots', False)
    do_labels = params['Labels']
    quantity = str_to_pq.get(params.get('Quantity', None), pqNone)
    max_lw = params.get('MaxLineThickness', 5)

    try:
        quantity_max_value = params.pop('MaxScale')
    except:
        quantity_max_value = 0


    ActiveCircuit = DSS.ActiveCircuit

    if obj_name:
        ActiveCircuit.Meters.Name = obj_name
        meters = [ActiveCircuit.Meters]
    else:
        meters = ActiveCircuit.Meters

    elem = ActiveCircuit.ActiveCktElement
    line = ActiveCircuit.Lines
    topo = ActiveCircuit.Topology

    icolor = 0

    #TODO: check if/where we need to transform to lowercase.
    bus_coords = dict((b.Name.lower(), (b.x, b.y)) for b in ActiveCircuit.Buses if b.Coorddefined)

    meter_marker_dict = get_marker_dict(24)
    meter_marker_dict['markersize'] *= (3 / 3.5)**2

    lines1, lines1_colors, labels1 = [], [], []
    lines3, lines3_colors, labels3 = [], [], []

    # lw1, lw3 will initially hold the values, later transformed to actual widths
    lw1, lw3 = [], []

    if quantity in (pqCurrent, pqCapacity):
        capacities = dict(zip(DSS.ActiveCircuit.PDElements.AllNames, DSS.ActiveCircuit.PDElements.AllPctNorm(True)))

    coords_to_names = {}

    def _name_coords(c, name):
        prev = coords_to_names.get(c)
        if prev is None:
            coords_to_names[c] = name
            return
        elif prev == name:
            return
        
        if prev.endswith(',' + name) or prev.startswith(name + ',') or (',' + name + ',') in prev:
            return

        coords_to_names[c] = prev + ',' + name


    def _add_line(element, color):
        br_name = element.Name
        bus1, bus2 = element.BusNames[:2]
        bus1, bus2 = nodot(bus1).lower(), nodot(bus2).lower()
        c1 = bus_coords.get(bus1)
        c2 = bus_coords.get(bus2)
        lw = 1
        if not c1 or not c2:
            return None, None

        if do_labels:
            _name_coords(c1, f'{bus1}({feeder_name})')
            _name_coords(c2, f'{bus2}({feeder_name})')

        if quantity == pqPower:
            lw = element.TotalPowers[0]
        elif quantity == pqVoltage:
            lw = 1
        elif quantity == pqLosses:
            lw = 0
            try:
                if element.Name.startswith('Line.'):
                    lw = 1e-3 * abs(element.Losses[0] / line.Length)
            except:
                pass
        elif quantity in (pqCurrent, pqCapacity):
            lw = capacities.get(element.Name, np.NaN)

        if (element.NumPhases == 1):
            lines1.append([c1, c2])
            lines1_colors.append(color)
            labels1.append(br_name)
            lw1.append(lw)
            return lines1_colors, len(lines1_colors) - 1
        else:
            lines3.append([c1, c2])
            lines3_colors.append(color)
            labels3.append(br_name)
            lw3.append(lw)
            return lines3_colors, len(lines3_colors) - 1


    fig, ax = plt.subplots(1)
    for meter in meters:
        if not elem.Enabled:
            continue

        feeder_name = meter.Name
        branches = meter.AllBranchesInZone
        if not branches:
            continue
    
        # Meter marker
        _ = topo.First
        coords = bus_coords.get(elem.BusNames[meter.MeteredTerminal - 1])
        if coords:
            plt.plot(*coords, color='red', **meter_marker_dict)

        feeder_color = color1 if show_loops else Colors[icolor % len(Colors)]
        icolor += 1

        br_idx = topo.First
        while br_idx != 0:
            if not elem.Enabled:
                continue

            lcs, lidx = _add_line(elem, feeder_color)
            if show_loops:
                looped = (topo.LoopedBranch != 0)
                if looped:
                    # The looped PDE is set as active by LoopedBranch
                    _add_line(elem, color3)
                    # Adjust the original to color3
                    if lidx is not None:
                        lcs[lidx] = color3
         
            br_idx = topo.Next


    lw1 = np.asarray(lw1)
    lw3 = np.asarray(lw3)

    if quantity_max_value == 0:
        lw1_max_value = 0
        lw3_max_value = 0
        if len(lw1):
            lw1_max_value = np.nanmax(lw1)
            if np.isfinite(lw1_max_value):
                quantity_max_value = max(quantity_max_value, lw1_max_value)
        if len(lw3):
            lw3_max_value = np.nanmax(lw3)
            if np.isfinite(lw3_max_value):
                quantity_max_value = max(quantity_max_value, lw3_max_value)

    if quantity_max_value == 0:
        quantity_max_value = 1

    lw1 = np.clip(3 * lw1 / quantity_max_value, 0.5, max_lw)
    lw3 = np.clip(3 * lw3 / quantity_max_value, 0.5, max_lw)
    lines1 = np.asarray(lines1)
    lines3 = np.asarray(lines3)
    lc1 = LineCollection(lines1, linewidth=lw1, colors=lines1_colors, linestyle=single_ph_line_style)
    lc3 = LineCollection(lines3, linewidth=lw3, colors=lines3_colors, linestyle=three_ph_line_style)
    ax.add_collection(lc1)
    ax.add_collection(lc3)
    if dots:
        for lines, lc in ((lines1, lc1), (lines3, lc3)):
            ax.scatter(lines[:, 0, 0].ravel(), lines[:, 0, 1].ravel(), marker='o', facecolors='none', edgecolors=lc, s=9, lw=1)
            ax.scatter(lines[:, 1, 0].ravel(), lines[:, 1, 1].ravel(), marker='o', facecolors='none', edgecolors=lc, s=9, lw=1)
        
    ax.set_title(f'Meter Zone: {obj_name}' if obj_name else 'All Meter Zones')

    for coords, name in coords_to_names.items():
        ax.text(*coords, name, zorder=11, fontsize='xx-small', va='center', clip_on=True)

    ax.set_aspect('equal', 'datalim')
    ax.autoscale()



dss_plot_funcs = {
    'Scatter': dss_scatter_plot,
    'Daisy': dss_daisy_plot,
    'TShape': dss_tshape_plot,
    'PriceShape': dss_priceshape_plot,
    'LoadShape': dss_loadshape_plot,
    'Monitor': dss_monitor_plot,
    'Circuit': dss_circuit_plot,
    'Profile': dss_profile_plot,
    'Visualize': dss_visualize_plot,
    'YearlyCurve': dss_yearly_curve_plot,
    'Matrix': dss_matrix_plot,
    'GeneralData': dss_general_data_plot,
    'DI': dss_di_plot,
#    'CompareCases': dss_comparecases_plot,
    'MeterZones': dss_zone_plot
}

def dss_plot(DSS, params):
    try:
        ptype = params['PlotType']
        if ptype not in dss_plot_funcs:
            raise NotImplementedError(f'ERROR: not implemented plot type "{ptype}"')
            return -1

        with ToggleAdvancedTypes(DSS, False), warnings.catch_warnings():
            warnings.simplefilter("ignore")
            dss_plot_funcs.get(ptype)(DSS, params)

    except Exception as ex:
        from traceback import format_exc
        # print('DSS: Error while plotting. Parameters:', params, file=sys.stderr)
        DSS._errorPtr[0] = 777
        DSS._lib.Error_Set_Description(f"Error in the plot backend: {ex}\n{format_exc()}".encode())
        return 777
    
    return 0
        

# dss_progress_bar = None
# dss_progress_desc = ''


@api_util.ffi.def_extern()
def dss_python_cb_write(ctx, message_str, message_type: int, message_size: int, message_subtype: int):
    global dss_progress_bar
    global dss_progress_desc

    # DSS = _ctx2dss(ctx)
    
    message_str = api_util.ffi.string(message_str).decode(api_util.codec)
    if message_type == api_util.lib.DSSMessageType_Error:
        #print('DSS Error:', message_str, file=sys.stderr)
        pass
    elif message_type in (api_util.lib.DSSMessageType_ProgressCaption, api_util.lib.DSSMessageType_ProgressFormCaption):
        #dss_progress_desc = message_str
        # print('Progress Caption:', message_str, file=sys.stderr)
        pass
    elif message_type == api_util.lib.DSSMessageType_Progress:
        #print('DSS Progress:', message_str, file=sys.stderr)
        pass
    elif message_type == api_util.lib.DSSMessageType_FireOffEditor:
        link_file(message_str)
        # try:
        #     # print('DSSMessageType_FireOffEditor')
        #     with open(message_str, 'r') as f:
        #         text = f.read()
            
        #     IPython.display.display({'text/plain': text}, raw=True)
        # except:
        #     print(f'Could not display file "{message_str}"')
        #     return 1

    elif message_type == api_util.lib.DSSMessageType_ProgressPercent:
        try:
            pass
            # n = int(message_str)
            # desc = ''
            # if n == 0 and dss_progress_bar is not None:
            #     dss_progress_bar = None
                
            # if dss_progress_bar is None:
            #     dss_progress_bar = tqdm(total=100, desc=dss_progress_desc)
                
            # if n < 0:
            #     del dss_progress_bar
            #     dss_progress_bar = None
            #     return 0
                
                
            # dss_progress_bar.n = n
            # dss_progress_bar.refresh()
#             if n == 100:
#                 dss_progress_bar.close()
        except:
            import traceback
            traceback.print_exc()
            print('DSS Progress:', message_str)

    # else:
    #     # print(message_type)
    #     # print(message_str)
    #     IPython.display.display({'text/plain': message_str}, raw=True)
    else:
        # do nothing for now...
        pass
        
    return 0


@api_util.ffi.def_extern()
def dss_python_cb_plot(ctx, paramsStr):
    params = json.loads(api_util.ffi.string(paramsStr))
    result = 0
    try:
        DSS = IDSS._get_instance(ctx=ctx)
        result = dss_plot(DSS, params)
        if _do_show:
            plt.show()
    except:
        from traceback import print_exc
        print('DSS: Error while plotting. Parameters:', params, file=sys.stderr)
        print_exc()
    return 0 if result is None else result

_original_allow_forms = None
_do_show = True

def enable(plot3d: bool = False, plot2d: bool = True, show: bool = True):
    """
    Enables the plotting subsystem from DSS-Extensions.

    Set plot3d to `True` to try to reproduce some of the plots from the
    alternative OpenDSS Visualization Tool / OpenDSS Viewer addition 
    to OpenDSS.

    Use `show` to control whether this backend should call `pyplot.show()`
    or leave that to the system or the user. If the user plans to customize
    the figure, it is better to set `show=False` in order to preserve the 
    figures, since `pyplot.show()` discards them.
    """

    global include_3d
    global _original_allow_forms
    global _do_show

    _do_show = show

    if plot3d and plot2d:
        include_3d = 'both'
    elif plot3d and not plot2d:
        include_3d = '3d'
    elif plot2d and not plot3d:
        include_3d = '2d'

    api_util.lib.DSS_RegisterPlotCallback(api_util.lib.dss_python_cb_plot)
    api_util.lib.DSS_RegisterMessageCallback(api_util.lib.dss_python_cb_write)
    _original_allow_forms = DSSPrime.AllowForms
    DSSPrime.AllowForms = True

def disable():
    api_util.lib.DSS_RegisterPlotCallback(api_util.ffi.NULL)
    api_util.lib.DSS_RegisterMessageCallback(api_util.ffi.NULL)
    if _original_allow_forms is not None:
        DSSPrime.AllowForms = _original_allow_forms


__all__ = ['enable', 'disable']
