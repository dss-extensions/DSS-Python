"""
This module provides a **work-in-progress** implementation of the original OpenDSS plots
using the new features from DSS C-API v0.12 and common Python modules such as matplotlib.

This is not a complete implementation yet and there are known limitations
"""
try:
    import numpy as np
    from matplotlib import pyplot as plt
    from matplotlib.path import Path
    from matplotlib.collections import LineCollection
    from mpl_toolkits.mplot3d.art3d import Line3DCollection
    from matplotlib.patches import Rectangle
    import scipy.sparse.coo as coo
except:
    raise ImportError("SciPy and matplotlib are required to use this module.")

import re, json, sys, warnings
from . import api_util
from . import DSS as DSSPrime
from ._cffi_api_util import CffiApiUtil
from .dss_capi_gr import IDSS

# import os
# import html
# import tqdm
# from tqdm.notebook import tqdm
# import IPython.display

include_3d = '2d' # '2d' (default), '3d' (prefer 3d), 'both'

PROFILE3PH = 9999
PROFILEALL = 9998
PROFILEALLPRI = 9997
PROFILELLALL = 9996
PROFILELLPRI = 9995
PROFILELL = 9994 
PROFILE_SCALE_PUKM = 9993 # PROFILEPUKM
PROFILE_SCALE_120KFT = 9992 # PROFILE120KFT

(pqVoltage, pqCurrent, pqPower, pqLosses, pqCapacity, pqNone) = range(6)

str_to_pq = {
    'Voltage': pqVoltage,
    'Current': pqCurrent,
    'Power': pqPower,
    'Losses': pqLosses,
    'Capacity': pqCapacity
}

quantity_str = {v: k for k, v in str_to_pq.items()}
quantity_str[pqLosses] = 'Loss Density'

# Markers
DSS_MARKER_37 = Path([(0.0, -0.5), (0.0, 0.196), (-0.36, -0.5), (0.361, -0.5)], [1, 2, 1, 2])
DSS_MARKER_38 = Path([(0.0, -0.23), (0.0, 0.196), (-0.36, 0.196), (0.361, 0.196), (-0.36, -0.23), (0.361, -0.23)], [1, 2, 1, 2, 1, 2])
DSS_MARKER_20 = Path([(-0.23, -0.147), (0.0, 0.13), (0.23, -0.147)], [1, 2, 2])
DSS_MARKER_21 = Path([(-0.28, -0.147), (0.0, 0.13), (0.28, -0.147)], [1, 2, 2])
DSS_MARKER_22 = Path([(-0.23, 0.147), (0.0, -0.13), (0.23, 0.147)], [1, 2, 2])
DSS_MARKER_23 = Path([(-0.28, 0.147), (0.0, -0.13), (0.28, 0.147)], [1, 2, 2])

marker_map = {
    # marker, size multipler (1=normal, 2=small, 3=tiny), fill
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
    35: (6, 1, 0),
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

def get_marker_dict(dss_code):
    marker, size, fill = marker_map[dss_code]
    res = dict(
        marker=marker, 
        markersize=sizes[size], 
        markerfacecolor=None if fill else 'none', 
        alpha=0.5 if fill not in (0, 1) else 1, 
        markeredgecolor='none' if dss_code == 39 else None,
        markeredgewidth=2
    )
    for k, v in list(res.items()):
        if v is None:
            del res[k]
    
    return res

def nodot(b):
    return b.split('.', 1)[0]

def dss_monitor_plot(DSS, params):
    monitor = DSS.ActiveCircuit.Monitors
    monitor.Name = params['ObjectName']
    data = monitor.AsMatrix()

    header = monitor.Header
    if header[0].strip().lower() == 'freq':
        xlabel = 'Frequency (Hz)'
        h = data[:, 0]
    else:
        xlabel = 'Time (s)'
        h = data[:, 0] * 3600 + data[:, 1]
    
    separate = False
    if separate:
        fig, axs = plt.subplots(len(params['Channels']), sharex=True, figsize=(8, 9))
        icolor = -1
        for ax, base, ch in zip(axs, params['Bases'], params['Channels']):
            icolor += 1
            ax.plot(h, data[:, ch + 1] / base, color=Colors[icolor % len(Colors)])
            ax.grid()
            ax.set_ylabel(header[ch - 1])
    
    else:
        fig, ax = plt.subplots(1)
        icolor = -1
        for base, ch in zip(params['Bases'], params['Channels']):
            icolor += 1
            ax.plot(h, data[:, ch + 1] / base, label=header[ch - 1], color=Colors[icolor % len(Colors)])

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

    fig, ax = plt.subplots(1, figsize=(8.5, 6))#, num=f"TShape.{params['ObjectName']}")

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
    ax.set_ylabel(f'Temperature')

    ax.grid(ls='--')
    plt.tight_layout()

def dss_priceshape_plot(DSS, params):
    # There is no dedicated API yet
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

    fig, ax = plt.subplots(1, figsize=(8.5, 6))#, num=f"PriceShape.{params['ObjectName']}")

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
    ax.set_ylabel(f'Price')

    ax.grid(ls='--')
    plt.tight_layout()


def dss_loadshape_plot(DSS, params):
#     pprint(params)
    
    ls = DSS.ActiveCircuit.LoadShapes
    ls.Name = params['ObjectName']
    h = ls.TimeArray
    p = ls.Pmult
    q = ls.Qmult
    
    fig, ax = plt.subplots(1, figsize=(8.5, 6))#, num=f"LoadShape.{params['ObjectName']}")

    if not h.size:
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
            ax.set_ylabel(f'kW, kvar')
        else:
            ax.set_ylabel(f'kW')
    else:
        ax.set_ylabel(f'p.u.')

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

def get_branch_data(DSS, branch_objects, bus_coords, do_values=pqNone, do_switches=False, idxs=None):
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

    norm_min_volts = DSS.ActiveCircuit.Settings.NormVminpu
    norm_max_volts = DSS.ActiveCircuit.Settings.NormVmaxpu
    emerg_min_volts = DSS.ActiveCircuit.Settings.EmergVminpu
    emerg_max_volts = DSS.ActiveCircuit.Settings.EmergVmaxpu
    
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
            buses = DSS.ActiveCircuit.ActiveCktElement.BusNames
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
                S = np.asarray(element.Powers).view(dtype=complex)
                values[offset] = np.abs(np.sum(S[(S.shape[0] // 2):])) / 2
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
            buses = DSS.ActiveCircuit.ActiveCktElement.BusNames
            b1 = remove_nodes(buses[0])
            b2 = remove_nodes(buses[1])
            
            fr = bus_coords.get(b1)
            to = bus_coords.get(b2)
            
            if fr is None or to is None:
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
            return lines[:offset], None, None, *extra
            
        offset = 0

        for i, l in enumerate(branch_objects):
            if i in skip:
                continue
                
            if do_values == pqPower:
                S = np.asarray(DSS.ActiveCircuit.ActiveCktElement.Powers).view(dtype=complex)
                values[offset] = np.abs(np.sum(S[(S.shape[0] // 2):])) / 2
                if l.Phases < 3:
                    lines_styles[offset] = 1
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
            
            offset += 1
        
        return lines[:offset], values[:offset], lines_styles, *extra
    

def get_point_data(DSS, point_objects, bus_coords, do_values=False):
    point_count = point_objects.Count
    points = np.empty(shape=(point_count, 2), dtype=np.float64)
    values = np.empty(shape=(point_count, ), dtype=np.float64)

    # def get_buses_point(l):
        # b1 = remove_nodes(l.Bus1)
        # b2 = remove_nodes(l.Bus2)

    offset = 0
    skip = set()
    for i, l in enumerate(point_objects):
        buses = DSS.ActiveCircuit.ActiveCktElement.BusNames
        all_coords = []
        buses = [remove_nodes(b) for b in buses]
        all_coords = [c for c in (bus_coords.get(b) for b in buses) if c]
        
        if not all_coords:
            skip.add(i)
            continue

        coords = tuple(sum(c)/len(all_coords) for c in zip(*all_coords)) 
            
        points[offset] = coords
        offset += 1
        
    if not do_values:
        return points[:offset]
        
    offset = 0
    for i, l in enumerate(DSS.ActiveCircuit.points):
        S = DSS.ActiveCircuit.ActiveCktElement.Powers.view(dtype=complex)
        if i in skip:
            continue
            
        values[offset] = np.abs(np.sum(S[(S.shape[0] // 2):])) / 2
        offset += 1
    
    return points[:offset], values[:offset]


def dss_profile_plot(DSS, params):
    PhasesToPlot = params['PhasesToPlot']
    ProfileScale = params['ProfileScale']
    
    vmin = DSS.ActiveCircuit.Settings.NormVminpu
    vmax = DSS.ActiveCircuit.Settings.NormVmaxpu
    if ProfileScale == PROFILE_SCALE_120KFT:
        xlabel = 'Distance (kft)'
        ylabel = '120 Base Voltage'
        DenomLN = 1.0 / 120.0
        DenomLL = 1.732 / 120.0
        LenScale = 3.2809
        RangeScale = 120.0
    else:
        xlabel = 'Distance (km)'
        ylabel = 'p.u. Voltage'
        DenomLN = 1.0
        DenomLL = 1.732
        LenScale = 1.0
        RangeScale = 1.0

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
        fig = plt.figure(figsize=(9, 5))
        ax = fig.add_subplot(1, 1, 1)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        if PhasesToPlot in (PROFILELL, PROFILELLALL, PROFILELLPRI):
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
        fig2 = plt.figure(figsize=(7, 7))
        ax2 = fig2.add_subplot(1, 1, 1, projection='3d')
        ax2.set_xlabel(xlabel)
        ax2.set_ylabel(ylabel)
        if PhasesToPlot in (PROFILELL, PROFILELLALL, PROFILELLPRI):
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
        ax2.set_xlabel(ax.get_xlabel())
        ax2.set_ylabel(ax.get_ylabel())
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


def dss_circuit_plot(DSS, params={}, fig=None, ax=None, is3d=False):
    quantity = str_to_pq.get(params.pop('Quantity', None), pqNone)
    color1 = params.pop('Color1', Colors[0])
    color2 = params.pop('Color2', Colors[1])
    color3 = params.pop('Color3', Colors[2])
    
    norm_min_volts = DSS.ActiveCircuit.Settings.NormVminpu
    norm_max_volts = DSS.ActiveCircuit.Settings.NormVmaxpu
    emerg_min_volts = DSS.ActiveCircuit.Settings.EmergVminpu
    emerg_max_volts = DSS.ActiveCircuit.Settings.EmergVmaxpu
    
    bus_coords = dict((b.Name, (b.x, b.y)) for b in DSS.ActiveCircuit.Buses if (b.x, b.y) != (0.0, 0.0))
    if fig is None:
        fig = plt.figure(figsize=(8, 7))
        
    given_ax = ax is not None
    if not given_ax:
        ax = plt.gca()
    else:
        plt.sca(ax)

    if not is3d:
        ax.set_aspect('equal', 'datalim')

    lines_lines, lines_values, lines_styles, switch_idxs, isolated_idxs, *extra = get_branch_data(DSS, DSS.ActiveCircuit.Lines, bus_coords, do_values=quantity, do_switches=True)
    
    lines_style_code = {0: '-', 1: '--'}

    if isolated_idxs:
        line_idx = isolated_idxs
        if not is3d:
            ax.add_collection(LineCollection(lines_lines[line_idx, :], linewidths=1, linestyles='-', color='#ff00ff', capstyle='round'))

    if switch_idxs:
        line_idx = switch_idxs
        if not is3d:
            ax.add_collection(LineCollection(lines_lines[line_idx, :], linewidths=1, linestyles='-', color='#000000', capstyle='round'))

    switch_idxs = set(switch_idxs)
    isolated_idxs = set(isolated_idxs)
    #lc_lines = LineCollection(lines_lines, linewidths=0.5, color='b')# + 3 * lines_values / np.max(lines_values), linestyles='solid', color='b')
    if quantity in (pqVoltage,):
        vbs, = extra
        colors = []
        for v in lines_values:
            if v > norm_min_volts or np.isnan(v):
                colors.append(color1)
            elif v > emerg_min_volts:
                colors.append(color2)
            else:
                colors.append(color3)
        
        lines_styles = lines_styles[:len(lines_lines)]
        for ls in set(lines_styles):
            line_idx = [i for i, c in enumerate(lines_styles) if c == ls and i not in isolated_idxs and i not in switch_idxs]
            if not is3d:
                ax.add_collection(LineCollection(lines_lines[line_idx, :], linewidths=1, linestyles=lines_style_code[ls], color=[colors[i] for i in line_idx], capstyle='round'))
        # if is3d:
        #     ax.add_collection(Line3DCollection(lines_lines, linewidths=1, linestyles='-', color=[colors[i] for i in line_idx], capstyle='round'))
        #     ax.set_xlim(np.min(lines_lines_3d[:, :, 0]), np.max(lines_lines_3d[:, :, 0]))
        #     ax.set_ylim(np.min(lines_lines_3d[:, :, 1]), np.max(lines_lines_3d[:, :, 1]))

        quantity_max_value = 0
    elif quantity in (pqLosses,):
        line_idx = [i for i in range(lines_lines.shape[0]) if i not in isolated_idxs and i not in switch_idxs]
        try:
            quantity_max_value = params.pop('MaxScale')
        except:
            quantity_max_value = max(lines_values) * 1e3
        
        lines_values = np.clip(3 * 1e-3 * lines_values / quantity_max_value, 1, 30)
        if not is3d:
            ax.add_collection(LineCollection(lines_lines[line_idx, :], linewidths=lines_values[line_idx], linestyles='-', color='b', capstyle='round'))
        #quantity_max_value *= 1e-3
    elif quantity in (pqCurrent, pqCapacity):
        line_idx = [i for i in range(lines_lines.shape[0]) if i not in isolated_idxs and i not in switch_idxs]
        colors = [color3 if v > 100 and not np.isnan(v) else color1 for v in lines_values[line_idx]]

        try:
            quantity_max_value = params.pop('MaxScale')
        except:
            quantity_max_value = max(lines_values)

        lines_values = np.clip(3 * lines_values / quantity_max_value, 1, 30)
        if not is3d:
            ax.add_collection(LineCollection(lines_lines[line_idx, :], linewidths=lines_values[line_idx], linestyles='-', color=colors, capstyle='round'))
        #quantity_max_value *= 1e-3
    elif quantity != pqNone:
        quantity_max_value = max(lines_values)
        lines_styles = lines_styles[:len(lines_lines)]
        for ls in set(lines_styles):
            line_idx = [i for i, c in enumerate(lines_styles) if c == ls and i not in isolated_idxs and i not in switch_idxs]
            if not is3d:
                ax.add_collection(LineCollection(lines_lines[line_idx, :], linewidths=0.5 + 6 * lines_values[line_idx] / quantity_max_value, linestyles=lines_style_code[ls], color='b', capstyle='round'))
    else:
        #TODO: handle 1 and 3 phase, etc.
        if not is3d:
            ax.add_collection(LineCollection(lines_lines, linewidths=1, linestyles='-', color=color1, capstyle='round'))
        # else:
        #     ax.add_collection(Line3DCollection(lines_lines, linewidths=1, linestyles='-', color=color1, capstyle='round'))
        #     ax.set_xlim(np.min(lines_lines[:, :, 0]), np.max(lines_lines[:, :, 0]))
        #     ax.set_ylim(np.min(lines_lines[:, :, 1]), np.max(lines_lines[:, :, 1]))

    transformers_lines, *_ = get_branch_data(DSS, DSS.ActiveCircuit.Transformers, bus_coords)

    if not is3d:
        lc_transformers = LineCollection(transformers_lines, linewidth=3, linestyles='solid', color='gray')
        ax.add_collection(lc_transformers)


    # 'Daisysize'
    # 'Markercode', 'Nodewidth' # NodeMarkerCode
    
    branch_marker_options = [
        ('MarkSwitches', 'SwitchMarkerCode', None, DSS.ActiveCircuit.Lines, switch_idxs),
        ('MarkFuses', 'FuseMarkerCode', 'FuseMarkerSize', DSS.ActiveCircuit.Fuses, None),
        ('MarkRegulators', 'RegMarkerCode', 'RegMarkerSize', DSS.ActiveCircuit.RegControls, None),
        #('MarkStorage', 'StoreMarkerCode', 'StoreMarkerSize', DSS.ActiveCircuit.Storage, None), -- TODO
        ('MarkRelays', 'RelayMarkerCode', 'RelayMarkerSize', DSS.ActiveCircuit.Relays, None),
        ('MarkReclosers', 'RecloserMarkerCode', 'RecloserMarkerSize', DSS.ActiveCircuit.Reclosers, None)
    ]
    
    point_marker_options = [    
        ('MarkTransformers', 'TransMarkerCode', 'TransMarkerSize', DSS.ActiveCircuit.Transformers, None),
        ('MarkCapacitors', 'CapMarkerCode', 'CapMarkerSize', DSS.ActiveCircuit.Capacitors, None),
        ('MarkPVSystems', 'PVMarkerCode', 'PVMarkerSize', DSS.ActiveCircuit.PVSystems, None)
    ]

    pmarkers = params.pop('Markers', None)
    if pmarkers is not None:
        for (mark_opt, code_opt, size_opt, objs, idxs) in branch_marker_options:
            # print(mark_opt, pmarkers[mark_opt])
            if not pmarkers[mark_opt]:
                continue
                
            marker_code = pmarkers[code_opt]
            marker_size = pmarkers[size_opt]
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
                branch_lines = get_branch_data(DSS, objs, bus_coords, idxs=idxs)
            
            
        for (mark_opt, code_opt, size_opt, objs, idxs) in point_marker_options:
            if not pmarkers[mark_opt]:
                continue
                
            marker_code = pmarkers[code_opt]
            marker_size = pmarkers[size_opt]
            
            points = get_point_data(DSS, objs, bus_coords)
            
    #        if marker_code not in marker_map:
                #marker_code = 25
                
            marker_dict = get_marker_dict(marker_code)
            marker_dict['markersize'] *= (marker_size / 3.0)**2
            
            #marker_dict['marker'] = marker_dict['marker'].vertices
            #marker_dict.pop('markersize')
            #marker_dict.pop('markerfacecolor')
    #         print(mark_opt, marker_dict['marker'])
    #         pprint(marker_dict)
            ax.plot(points[:, 0], points[:, 1], ls='', color='red', **marker_dict)
            #ax.plot(points[:, 0], points[:, 1], color='red', ls='', marker=6, alpha=1)


    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    if not given_ax:       
        ax.set_title('{}:{}, max={:g}'.format(DSS.ActiveCircuit.Name.upper(), quantity_str[quantity], quantity_max_value))
        ax.autoscale_view()
        ax.get_xaxis().get_major_formatter().set_scientific(False)
        ax.get_yaxis().get_major_formatter().set_scientific(False)
        plt.tight_layout()
    

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
        fig, ax = plt.subplots(1, 1, figsize=(8, 7), constrained_layout=True)
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

        fig = plt.figure(figsize=(7, 7))
        ax = fig.add_subplot(projection='3d')
        dss_circuit_plot(DSS, fig=fig, ax=ax, params={}, is3d=True)
        ax.get_xaxis().get_major_formatter().set_scientific(False)
        ax.get_yaxis().get_major_formatter().set_scientific(False)

        # if is3d:
        #     ax.add_collection(Line3DCollection(lines_lines, linewidths=1, linestyles='-', color=[colors[i] for i in line_idx], capstyle='round'))
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
    element = DSS.ActiveCircuit.ActiveCktElement
    etype, ename = params['ElementType'], params['ElementName']
    nconds = element.NumConductors
    nphases = element.NumPhases
    buses = element.BusNames[:2] # max 2 terminals
    vbases = [max(1, 1000 * DSS.ActiveCircuit.Buses[nodot(b)].kVBase) for b in buses]

    # assert DSS.ActiveCircuit.ActiveCktElement.Name == params['ElementType'] + '.' + params['ElementName']
    fig, ax = plt.subplots(1, figsize=(8.6, 7), gridspec_kw=dict(left=0.05, right=0.95, bottom=0.05, top=0.92))
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
    
    voltage = (quantity == 'Voltage')

    if quantity == 'Power':
        values = 1e-3 * (element.Voltages.view(dtype=complex) * np.conj(element.Currents.view(dtype=complex)))
        unit = 'kVA'
    elif voltage:
        values = element.Voltages.view(dtype=complex)
        unit = 'pu'
    elif quantity == 'Current':
        values = element.Currents.view(dtype=complex)
        unit = 'A'

    ax.set_title(f'{etype}.{ename.upper()} {quantity}s ({unit})')

    def get_text():
        v = values[bus_idx * nconds + cond]
        if quantity == 'Power':
            arrow_text = f"{v.real:-.6g} {'-' if v.imag < 0 else '+'} j{abs(v.imag):g}"
        else:
            if quantity == 'Voltage':
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
                ax.text(arrow_x - 20, arrow_y + 2, get_text(), ha='right', fontweight=weight)
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
                ax.text(arrow_x + 20, arrow_y + 2, get_text(), ha='left', fontweight=weight)
                if voltage:
                    plt.plot([arrow_x, dx + arrow_x], [arrow_y, arrow_y], color='k', lw=lw*1.5)
                    x = 4 * (cond) + 1
                    ax.annotate('', xy=(x, arrow_y), xytext=(x, 0), arrowprops=dict(width=0.2, color='lightgray'))
                else:
                    ax.annotate('', xytext=(arrow_x, arrow_y), xy=(dx + arrow_x, arrow_y), arrowprops=dict(width=lw, color='k'))

        if quantity == 'Current': 
            # Residual
            v = -np.sum(values[(nconds * bus_idx):(nconds * (bus_idx + 1))])
            txt = f"{np.abs(v):-.6g} A ∠ {np.angle(v, deg=True):.2f}°"

            if bus_idx:
                arrow_x = XMAX + 5
                arrow_y = -10
                dx = box_xy1[0] - arrow_x
                ax.text(arrow_x - 5, arrow_y + 2, txt, ha='right', fontweight='normal')
                ax.annotate('', xytext=(arrow_x, arrow_y), xy=(dx + arrow_x, arrow_y), arrowprops=dict(width=1, color='k'))
            else:
                arrow_x = -5
                arrow_y = -10
                dx = box_xy0[0] + 5
                ax.text(arrow_x + 5, arrow_y + 2, txt, ha='left', fontweight='normal')
                ax.annotate('', xytext=(arrow_x, arrow_y), xy=(dx + arrow_x, arrow_y), arrowprops=dict(width=1, color='k'))

    ax.set_xlim(-20, XMAX + 20)
    ax.set_ylim(-15, y + 5)


def dss_yearly_curve_plot(DSS, params):
    print("TODO: YearCurveplot")#, params)

def dss_general_data_plot(DSS, params):
    print("TODO: GeneralDataPlot")#, params)



def dss_matrix_plot(DSS, params):
    plot_id = params.get('PlotId', None)
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
        fig = plt.figure(figsize=(8.6, 8.6), constrained_layout=True)#, num=plot_id)
        ax = fig.add_subplot(1, 1, 1)
        ax.grid(True)
        ax.spy(m, marker='s', markersize=1, color=params['Color1'])
        ax.set_xlabel('Column')
        ax.set_ylabel('Row')
        ax.set_title(title)

    if include_3d in ('both', '3d'):
        fig = plt.figure(figsize=(8.6, 8.6))#, num=plot_id + '_3D')
        ax2 = fig.add_subplot(1, 1, 1, projection='3d')
        ax2.scatter(x, y, v, c=v, marker='s')
        ax2.set_xlabel('Column')
        ax2.set_ylabel('Row')
        ax2.set_zlabel('Value')


def dss_daisy_plot(DSS, params):
    dss_circuit_plot(DSS, params)

    print(params['DaisySize'])

    ax = plt.gca()
    title = f"{params['Quantity']}"
    ax.set_title(title)

    daisy_bus_list = params['DaisyBusList']
    element = DSS.ActiveCircuit.ActiveCktElement

    if len(daisy_bus_list) == 0:
        for g in DSS.ActiveCircuit.Generators:
            if element.Enabled:
                daisy_bus_list.append(element.BusNames[0])

    counts = np.zeros(shape=(DSS.ActiveCircuit.NumBuses,), dtype=np.int32)


dss_plot_funcs = {
    'ScatterPlot': dss_scatter_plot,
    'DaisyPlot': dss_daisy_plot,
    'TShape': dss_tshape_plot,
    'PriceShape': dss_priceshape_plot,
    'LoadShape': dss_loadshape_plot,
    'MonitorPlot': dss_monitor_plot,
    'CircuitPlot': dss_circuit_plot,
    'Profile': dss_profile_plot,
    'Visualize': dss_visualize_plot,
    'YearlyCurvePlot': dss_yearly_curve_plot,
    'MatrixPlot': dss_matrix_plot,
    'GeneralDataPlot': dss_general_data_plot
}

def dss_plot(DSS, params):
    dss_plot_funcs.get(params['PlotType'])(DSS, params)


def ctx2dss(ctx, instances={}):
    DSS = instances.get(ctx)
    if DSS is not None:
        return DSS

    # Handle the most likely case    
    if DSSPrime._api_util.ctx == ctx:
        instances[ctx] = DSSPrime
        return DSSPrime

    # For new ctx references, wrap the ctx in a 
    # new DSS instance and cache it for later
    util = CffiApiUtil(api_util.ffi, api_util.lib_unpatched, ctx)
    util.owns_ctx = False
    DSS = IDSS(util)
    instances[ctx] = DSS
    return DSS

# dss_progress_bar = None
# dss_progress_desc = ''

# @api_util.ffi.def_extern(ctx2dss)
# def dss_python_cb_write(ctx, message_str, message_type):
#     global dss_progress_bar
#     global dss_progress_desc

#     DSS = ctx2dss(ctx)
    
#     message_str = api_util.ffi.string(message_str).decode(api_util.codec)
#     if message_type == api_util.lib.DSSMessageType_Error:
#         #print('DSS Error:', message_str, file=sys.stderr)
#         pass
#     elif message_type in (api_util.lib.DSSMessageType_ProgressCaption, api_util.lib.DSSMessageType_ProgressFormCaption):
#         #dss_progress_desc = message_str
#         # print('Progress Caption:', message_str, file=sys.stderr)
#         pass
#     elif message_type == api_util.lib.DSSMessageType_Progress:
#         #print('DSS Progress:', message_str, file=sys.stderr)
#         pass
#     elif message_type == api_util.lib.DSSMessageType_FireOffEditor:
#         dpath = DSS.DataPath
#         if not dpath:
#             dpath = os.getcwd()

#         relfn = os.path.relpath(message_str, dpath)

#         IPython.display.display_html(IPython.display.HTML(f'<b>{html.escape(relfn)}</b><hr>'))
#         try:
#             # print('DSSMessageType_FireOffEditor')
#             with open(message_str, 'r') as f:
#                 text = f.read()
            
#             IPython.display.display({'text/plain': text}, raw=True)
#         except:
#             print(f'Could not display file "{message_str}"')
#             return 1

#     elif message_type == api_util.lib.DSSMessageType_ProgressPercent:
#         try:
#             n = int(message_str)
#             desc = ''
#             if n == 0 and dss_progress_bar is not None:
#                 dss_progress_bar = None
                
#             if dss_progress_bar is None:
#                 dss_progress_bar = tqdm(total=100, desc=dss_progress_desc)
                
#             if n < 0:
#                 del dss_progress_bar
#                 dss_progress_bar = None
#                 return 0
                
                
#             dss_progress_bar.n = n
#             dss_progress_bar.refresh()
# #             if n == 100:
# #                 dss_progress_bar.close()
#         except:
#             import traceback
#             traceback.print_exc()
#             print('DSS Progress:', message_str)
#     # else:
#     #     # print(message_type)
#     #     # print(message_str)
#     #     IPython.display.display({'text/plain': message_str}, raw=True)
#     else:
#         # do nothing for now...
#         pass
        
#     return 0


@api_util.ffi.def_extern()
def dss_python_cb_plot(ctx, paramsStr):
    params = json.loads(api_util.ffi.string(paramsStr))
    try:
        DSS = ctx2dss(ctx)
        dss_plot(DSS, params)
        plt.show()
    except:
        from traceback import print_exc
        print('DSS: Error while plotting. Parameters:', params, file=sys.stderr)
        print_exc()
    return 0

_original_allow_forms = None


def enable(plot3d=False, plot2d=True):
    """
    Enables the experimental plotting subsystem from DSS Extensions.

    Set plot3d to True to try to reproduce some of the plots from the
    alternative OpenDSS Visualization Tool / OpenDSS Viewer addition 
    to OpenDSS.
    """

    global include_3d
    global _original_allow_forms

    warnings.warn('This is still an initial, work-in-progress implementation of plotting for DSS Extensions')

    if plot3d and plot2d:
        include_3d = 'both'
    elif plot3d and not plot2d:
        include_3d = '3d'
    elif plot2d and not plot3d:
        include_3d = '2d'

    api_util.lib.DSS_RegisterPlotCallback(api_util.lib.dss_python_cb_plot)
    # api_util.lib.DSS_RegisterMessageCallback(api_util.lib.dss_python_cb_write)
    _original_allow_forms = DSSPrime.AllowForms
    DSSPrime.AllowForms = True

def disable():
    api_util.lib.DSS_RegisterPlotCallback(api_util.ffi.NULL)
    # api_util.lib.DSS_RegisterMessageCallback(api_util.ffi.NULL)
    if _original_allow_forms is not None:
        DSSPrime.AllowForms = _original_allow_forms


__all__ = ['enable', 'disable']
