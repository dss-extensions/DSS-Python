import os, io
# import numpy as np
import pandas as pd
from dss import dss, Edit, IDSS
from dss.IObj import (
    Vsource, Transformer, LineCode, Load, Line, Capacitor,
    Connection as Conn, RegControl, DimensionUnits as Units,
)
try:
    from ._settings import BASE_DIR
except ImportError:
    from _settings import BASE_DIR

LoadModel = Load.LoadModel

loads_cols = 'name,bus1,phases,conn,model,kV,kW,kvar'.split(',')
loads_data = (
    ('671', '671.1.2.3', 3, Conn.delta, LoadModel.ConstantPQ, 4.16, 1155, 660),
    ('634a', '634.1', 1, Conn.wye, LoadModel.ConstantPQ, 0.277, 160, 110),
    ('634b', '634.2', 1, Conn.wye, LoadModel.ConstantPQ, 0.277, 120, 90),
    ('634c', '634.3', 1, Conn.wye, LoadModel.ConstantPQ, 0.277, 120, 90),
    ('645', '645.2', 1, Conn.wye, LoadModel.ConstantPQ, 2.4, 170, 125),
    ('646', '646.2.3', 1, Conn.delta, LoadModel.ConstantZ, 4.16, 230, 132),
    ('692', '692.3.1', 1, Conn.delta, LoadModel.ConstantI, 4.16, 170, 151),
    ('675a', '675.1', 1, Conn.wye, LoadModel.ConstantPQ, 2.4, 485, 190),
    ('675b', '675.2', 1, Conn.wye, LoadModel.ConstantPQ, 2.4, 68, 60),
    ('675c', '675.3', 1, Conn.wye, LoadModel.ConstantPQ, 2.4, 290, 212),
    ('611', '611.3', 1, Conn.wye, LoadModel.ConstantI, 2.4, 170, 80),
    ('652', '652.1', 1, Conn.wye, LoadModel.ConstantZ, 2.4, 128, 86),
    ('670a', '670.1', 1, Conn.wye, LoadModel.ConstantPQ, 2.4, 17, 10),
    ('670b', '670.2', 1, Conn.wye, LoadModel.ConstantPQ, 2.4, 66, 38),
    ('670c', '670.3', 1, Conn.wye, LoadModel.ConstantPQ, 2.4, 117, 68),
)

lines_cols = 'name,phases,bus1,bus2,linecode,length,units'.split(',')
lines_data = (
    ('650632', 3, 'RG60.1.2.3', '632.1.2.3', 'mtx601', 2000, Units.ft),
    ('632670', 3, '632.1.2.3', '670.1.2.3', 'mtx601', 667, Units.ft),
    ('670671', 3, '670.1.2.3', '671.1.2.3', 'mtx601', 1333, Units.ft),
    ('671680', 3, '671.1.2.3', '680.1.2.3', 'mtx601', 1000, Units.ft),
    ('632633', 3, '632.1.2.3', '633.1.2.3', 'mtx602', 500, Units.ft),
    ('632645', 2, '632.3.2', '645.3.2', 'mtx603', 500, Units.ft),
    ('645646', 2, '645.3.2', '646.3.2', 'mtx603', 300, Units.ft),
    ('692675', 3, '692.1.2.3', '675.1.2.3', 'mtx606', 500, Units.ft),
    ('671684', 2, '671.1.3', '684.1.3', 'mtx604', 300, Units.ft),
    ('684611', 1, '684.3', '611.3', 'mtx605', 300, Units.ft),
    ('684652', 1, '684.1', '652.1', 'mtx607', 800, Units.ft),
)

loads_data_csv = '''name,bus1,phases,conn,model,kV,kW,kvar
671,671.1.2.3,3,delta,1,4.16,1155,660
634a,634.1,1,wye,1,0.277,160,110
634b,634.2,1,wye,1,0.277,120,90
634c,634.3,1,wye,1,0.277,120,90
645,645.2,1,wye,1,2.4,170,125
646,646.2.3,1,delta,2,4.16,230,132
692,692.3.1,1,delta,5,4.16,170,151
675a,675.1,1,wye,1,2.4,485,190
675b,675.2,1,wye,1,2.4,68,60
675c,675.3,1,wye,1,2.4,290,212
611,611.3,1,wye,5,2.4,170,80
652,652.1,1,wye,2,2.4,128,86
670a,670.1,1,wye,1,2.4,17,10
670b,670.2,1,wye,1,2.4,66,38
670c,670.3,1,wye,1,2.4,117,68
''' 

lines_data_csv = '''name,phases,bus1,bus2,linecode,length,units
650632,3,RG60.1.2.3,632.1.2.3,mtx601,2000,ft
632670,3,632.1.2.3,670.1.2.3,mtx601,667,ft
670671,3,670.1.2.3,671.1.2.3,mtx601,1333,ft
671680,3,671.1.2.3,680.1.2.3,mtx601,1000,ft
632633,3,632.1.2.3,633.1.2.3,mtx602,500,ft
632645,2,632.3.2,645.3.2,mtx603,500,ft
645646,2,645.3.2,646.3.2,mtx603,300,ft
692675,3,692.1.2.3,675.1.2.3,mtx606,500,ft
671684,2,671.1.3,684.1.3,mtx604,300,ft
684611,1,684.3,611.3,mtx605,300,ft
684652,1,684.1,652.1,mtx607,800,ft
'''

def create_ref_ckt13(ref):
    ref.Text.Command = f'redirect "{BASE_DIR}/Version8/Distrib/IEEETestCases/13Bus/IEEE13Nodeckt.dss"'

def create_ckt13_batch_attr(dss: IDSS):
    dss.ClearAll()
    dss.NewCircuit('IEEE13Nodeckt')
    dss.AdvancedTypes = True

    # Get some local names for cleaner syntax
    Obj = dss.Obj
    LineCode = Obj.LineCode
    Line = Obj.Line
    Load = Obj.Load
    Transformer = Obj.Transformer
    Capacitor = Obj.Capacitor
    RegControl = Obj.RegControl

    src: Vsource = Obj.Vsource[1]
    with Edit(src):
        src.basekv = 115
        src.pu = 1.0001
        src.phases = 3
        src.bus1 = 'SourceBus'
        src.angle = 30
        src.MVAsc3 = 20000
        src.MVAsc1 = 21000

    # Transformers and regulators
    Transformer.new('Sub', phases=3, windings=2, XHL=8 / 1000, buses=['SourceBus', '650'], conns=[Conn.delta, Conn.wye], kVs=[115, 4.16], kVAs=[5000, 5000], pctRs=[0.5 / 1000, 0.5 / 1000])
    for i in (1, 2, 3):
        tr = Transformer.new(f'Reg{i}', phases=1, bank='reg1', XHL=0.01, kVAs=[1666, 1666], buses=[f'650.{i}', f'RG60.{i}'], kVs=[2.4, 2.4], pctloadloss=0.01)
        RegControl.new(f'Reg{i}', transformer=tr, winding=2, vreg=122, band=2, ptratio=20, CTprim=700, R=3, X=9)

    Transformer.new('XFM1', phases=3, windings=2, XHL=2, buses=['633', '634'], conns=[Conn.wye, Conn.wye], kVs=[4.16, 0.480], kVAs=[500, 500], pctRs=[0.55, 0.55])

    # Line codes
    mtx601 = LineCode.new('mtx601', nphases=3, baseFreq=60,
        rmatrix=[0.3465, 0.1560, 0.3375, 0.1580, 0.1535, 0.3414],
        xmatrix=[1.0179, 0.5017, 1.0478, 0.4236, 0.3849, 1.0348],
        units=Units.miles
    )
    mtx602 = LineCode.new('mtx602', nphases=3, baseFreq=60,
        rmatrix=[[0.7526, 0.1580, 0.1560], [0.1580, 0.7475, 0.1535], [0.1560, 0.1535, 0.7436]],
        xmatrix=(1.1814, 0.4236, 1.1983, 0.5017, 0.3849, 1.2112),
        units=Units.miles
    )
    mtx603 = LineCode.new('mtx603', nphases=2, baseFreq=60,
        rmatrix=[1.3238, 0.2066, 0.2066, 1.3294], xmatrix=[1.3569, 0.4591, 0.4591, 1.3471],
        units=Units.miles
    )
    mtx604 = LineCode.new('mtx604', nphases=2, baseFreq=60,
        rmatrix=(1.3238, 0.2066, 0.2066, 1.3294), xmatrix=(1.3569, 0.4591, 0.4591, 1.3471),
        units=Units.miles)
    mtx605 = LineCode.new('mtx605', nphases=1, baseFreq=60, rmatrix=[1.3292], xmatrix=[1.3475], units=Units.miles)
    mtx606 = LineCode.new('mtx606', nphases=3, units=Units.miles,
        rmatrix=[0.791721, 0.318476, 0.781649, 0.28345, 0.318476, 0.791721],
        xmatrix=[0.438352, 0.0276838, 0.396697, -0.0184204, 0.0276838, 0.438352],
        cmatrix=[383.948, 0, 383.948, 0, 0, 383.948]
    )
    mtx607 = LineCode.new('mtx607', nphases=1, baseFreq=60, rmatrix=(1.3425,), xmatrix=(0.5124,), cmatrix=[236], units=Units.miles)

    # Loads
    name, bus1, phases, conn, model, kV, kW, kvar = zip(*loads_data)
    
    # Either use as a context manager, or remember to call `loads.end_edit()`
    with Edit(Load.batch_new(name), needs_begin=False) as loads:
        loads.bus1 = bus1
        loads.conn = conn
        loads.phases = phases
        loads.model = model
        loads.kV = kV
        loads.kW = kW
        loads.kvar = kvar

    # Capacitors
    Capacitor.new('Cap1', bus1='675', phases=3, kvar=600, kv=4.16)
    Capacitor.new('Cap2', bus1='611.3', phases=1, kvar=100, kv=2.4)

    # Lines
    name, phases, bus1, bus2, linecode, length, units = zip(*lines_data)

    # Either use as a context manager, or remember to call `lines.end_edit()`
    with Edit(Line.batch_new(name), needs_begin=False) as lines:
        lines.phases = phases
        lines.bus1 = bus1
        lines.bus2 = bus2
        lines.linecode = linecode
        lines.length = length
        lines.units = Units.ft # all the same

    # Switch
    Line.new('671692', phases=3, bus1='671', bus2='692', Switch=True, r1=1e-4, r0=1e-4, x1=0.0, x0=0.0, C1=0.0, C0=0.0)

    dss.Text.Command = 'Set VoltageBases=[115, 4.16, .48]'
    dss.Text.Command = 'CalcV'
    dss.ActiveCircuit.Solution.Solve()


def create_ckt13_batch_new(dss: IDSS):
    dss.ClearAll()
    dss.NewCircuit('IEEE13Nodeckt')
    dss.AdvancedTypes = True

    # Get some local names for cleaner syntax
    Obj = dss.Obj
    LineCode = Obj.LineCode
    Line = Obj.Line
    Load = Obj.Load
    Transformer = Obj.Transformer
    Capacitor = Obj.Capacitor
    RegControl = Obj.RegControl

    src: Vsource = Obj.Vsource[1]
    with Edit(src):
        src.basekv = 115
        src.pu = 1.0001
        src.phases = 3
        src.bus1 = 'SourceBus'
        src.angle = 30
        src.MVAsc3 = 20000
        src.MVAsc1 = 21000

    # Transformers and regulators
    Transformer.new('Sub', phases=3, windings=2, XHL=8 / 1000, buses=['SourceBus', '650'], conns=[Conn.delta, Conn.wye], kVs=[115, 4.16], kVAs=[5000, 5000], pctRs=[0.5 / 1000, 0.5 / 1000])
    for i in (1, 2, 3):
        tr = Transformer.new(f'Reg{i}', phases=1, bank='reg1', XHL=0.01, kVAs=[1666, 1666], buses=[f'650.{i}', f'RG60.{i}'], kVs=[2.4, 2.4], pctloadloss=0.01)
        RegControl.new(f'Reg{i}', transformer=tr, winding=2, vreg=122, band=2, ptratio=20, CTprim=700, R=3, X=9)

    Transformer.new('XFM1', phases=3, windings=2, XHL=2, buses=['633', '634'], conns=[Conn.wye, Conn.wye], kVs=[4.16, 0.480], kVAs=[500, 500], pctRs=[0.55, 0.55])

    # Line codes
    mtx601 = LineCode.new('mtx601', nphases=3, baseFreq=60,
        rmatrix=[0.3465, 0.1560, 0.3375, 0.1580, 0.1535, 0.3414],
        xmatrix=[1.0179, 0.5017, 1.0478, 0.4236, 0.3849, 1.0348],
        units=Units.miles
    )
    mtx602 = LineCode.new('mtx602', nphases=3, baseFreq=60,
        rmatrix=[[0.7526, 0.1580, 0.1560], [0.1580, 0.7475, 0.1535], [0.1560, 0.1535, 0.7436]],
        xmatrix=(1.1814, 0.4236, 1.1983, 0.5017, 0.3849, 1.2112),
        units=Units.miles
    )
    mtx603 = LineCode.new('mtx603', nphases=2, baseFreq=60,
        rmatrix=[1.3238, 0.2066, 0.2066, 1.3294], xmatrix=[1.3569, 0.4591, 0.4591, 1.3471],
        units=Units.miles
    )
    mtx604 = LineCode.new('mtx604', nphases=2, baseFreq=60,
        rmatrix=(1.3238, 0.2066, 0.2066, 1.3294), xmatrix=(1.3569, 0.4591, 0.4591, 1.3471),
        units=Units.miles)
    mtx605 = LineCode.new('mtx605', nphases=1, baseFreq=60, rmatrix=[1.3292], xmatrix=[1.3475], units=Units.miles)
    mtx606 = LineCode.new('mtx606', nphases=3, units=Units.miles,
        rmatrix=[0.791721, 0.318476, 0.781649, 0.28345, 0.318476, 0.791721],
        xmatrix=[0.438352, 0.0276838, 0.396697, -0.0184204, 0.0276838, 0.438352],
        cmatrix=[383.948, 0, 383.948, 0, 0, 383.948]
    )
    mtx607 = LineCode.new('mtx607', nphases=1, baseFreq=60, rmatrix=(1.3425,), xmatrix=(0.5124,), cmatrix=[236], units=Units.miles)

    # Loads
    name, bus1, phases, conn, model, kV, kW, kvar = zip(*loads_data)
    Load.batch_new(name, bus1=bus1, conn=conn, phases=phases, model=model, kV=kV, kW=kW, kvar=kvar)

    # Capacitors
    Capacitor.new('Cap1', bus1='675', phases=3, kvar=600, kv=4.16)
    Capacitor.new('Cap2', bus1='611.3', phases=1, kvar=100, kv=2.4)

    # Lines
    Line.batch_new(**dict(zip(lines_cols, zip(*lines_data))))

    # Switch
    Line.new('671692', phases=3, bus1='671', bus2='692', Switch=True, r1=1e-4, r0=1e-4, x1=0.0, x0=0.0, C1=0.0, C0=0.0)

    dss.Text.Command = 'Set VoltageBases=[115, 4.16, .48]'
    dss.Text.Command = 'CalcV'
    dss.ActiveCircuit.Solution.Solve()


def create_ckt13_batch_df(dss: IDSS):
    dss.ClearAll()
    dss.NewCircuit('IEEE13Nodeckt')
    dss.AdvancedTypes = True

    # Get some local names for cleaner syntax
    Obj = dss.Obj
    LineCode = Obj.LineCode
    Line = Obj.Line
    Load = Obj.Load
    Transformer = Obj.Transformer
    Capacitor = Obj.Capacitor
    RegControl = Obj.RegControl

    src: Vsource = Obj.Vsource[1]
    with Edit(src):
        src.basekv = 115
        src.pu = 1.0001
        src.phases = 3
        src.bus1 = 'SourceBus'
        src.angle = 30
        src.MVAsc3 = 20000
        src.MVAsc1 = 21000

    # Transformers and regulators
    Transformer.new('Sub', phases=3, windings=2, XHL=8 / 1000, buses=['SourceBus', '650'], conns=[Conn.delta, Conn.wye], kVs=[115, 4.16], kVAs=[5000, 5000], pctRs=[0.5 / 1000, 0.5 / 1000])
    for i in (1, 2, 3):
        tr = Transformer.new(f'Reg{i}', phases=1, bank='reg1', XHL=0.01, kVAs=[1666, 1666], buses=[f'650.{i}', f'RG60.{i}'], kVs=[2.4, 2.4], pctloadloss=0.01)
        RegControl.new(f'Reg{i}', transformer=tr, winding=2, vreg=122, band=2, ptratio=20, CTprim=700, R=3, X=9)

    Transformer.new('XFM1', phases=3, windings=2, XHL=2, buses=['633', '634'], conns=[Conn.wye, Conn.wye], kVs=[4.16, 0.480], kVAs=[500, 500], pctRs=[0.55, 0.55])

    # Line codes
    mtx601 = LineCode.new('mtx601', nphases=3, baseFreq=60,
        rmatrix=[0.3465, 0.1560, 0.3375, 0.1580, 0.1535, 0.3414],
        xmatrix=[1.0179, 0.5017, 1.0478, 0.4236, 0.3849, 1.0348],
        units=Units.miles
    )
    mtx602 = LineCode.new('mtx602', nphases=3, baseFreq=60,
        rmatrix=[[0.7526, 0.1580, 0.1560], [0.1580, 0.7475, 0.1535], [0.1560, 0.1535, 0.7436]],
        xmatrix=(1.1814, 0.4236, 1.1983, 0.5017, 0.3849, 1.2112),
        units=Units.miles
    )
    mtx603 = LineCode.new('mtx603', nphases=2, baseFreq=60,
        rmatrix=[1.3238, 0.2066, 0.2066, 1.3294], xmatrix=[1.3569, 0.4591, 0.4591, 1.3471],
        units=Units.miles
    )
    mtx604 = LineCode.new('mtx604', nphases=2, baseFreq=60,
        rmatrix=(1.3238, 0.2066, 0.2066, 1.3294), xmatrix=(1.3569, 0.4591, 0.4591, 1.3471),
        units=Units.miles)
    mtx605 = LineCode.new('mtx605', nphases=1, baseFreq=60, rmatrix=[1.3292], xmatrix=[1.3475], units=Units.miles)
    mtx606 = LineCode.new('mtx606', nphases=3, units=Units.miles,
        rmatrix=[0.791721, 0.318476, 0.781649, 0.28345, 0.318476, 0.791721],
        xmatrix=[0.438352, 0.0276838, 0.396697, -0.0184204, 0.0276838, 0.438352],
        cmatrix=[383.948, 0, 383.948, 0, 0, 383.948]
    )
    mtx607 = LineCode.new('mtx607', nphases=1, baseFreq=60, rmatrix=(1.3425,), xmatrix=(0.5124,), cmatrix=[236], units=Units.miles)

    # Loads
    with io.StringIO(loads_data_csv) as loads_csv:
        df_loads = pd.read_csv(loads_csv)

    Load.batch_new(df=df_loads)

    # Capacitors
    Capacitor.new('Cap1', bus1='675', phases=3, kvar=600, kv=4.16)
    Capacitor.new('Cap2', bus1='611.3', phases=1, kvar=100, kv=2.4)

    # Lines
    with io.StringIO(lines_data_csv) as lines_csv:
        df_lines = pd.read_csv(lines_csv)

    Line.batch_new(df=df_lines)

    # Switch
    Line.new('671692', phases=3, bus1='671', bus2='692', Switch=True, r1=1e-4, r0=1e-4, x1=0.0, x0=0.0, C1=0.0, C0=0.0)

    dss.Text.Command = 'Set VoltageBases=[115, 4.16, .48]'
    dss.Text.Command = 'CalcV'
    dss.ActiveCircuit.Solution.Solve()

def _test_create_ckt13_batch(which):
    if which == 1:
        create_ckt13_batch_attr(dss)
    elif which == 2:
        create_ckt13_batch_new(dss)
    else:
        create_ckt13_batch_df(dss)

    ref: IDSS = dss.NewContext()
    create_ref_ckt13(ref)

    assert dss.ActiveCircuit.Lines.AllNames == ref.ActiveCircuit.Lines.AllNames
    assert dss.ActiveCircuit.Loads.AllNames == ref.ActiveCircuit.Loads.AllNames
    assert [l.Phases for l in dss.ActiveCircuit.Lines] == [l.Phases for l in ref.ActiveCircuit.Lines]
    assert [l.Length for l in dss.ActiveCircuit.Lines] == [l.Length for l in ref.ActiveCircuit.Lines]
    assert [l.Phases for l in dss.ActiveCircuit.Loads] == [l.Phases for l in ref.ActiveCircuit.Loads]
    assert [l.kW for l in dss.ActiveCircuit.Loads] == [l.kW for l in ref.ActiveCircuit.Loads]
    assert [l.kvar for l in dss.ActiveCircuit.Loads] == [l.kvar for l in ref.ActiveCircuit.Loads]
    assert dss.ActiveCircuit.Transformers.AllNames == ref.ActiveCircuit.Transformers.AllNames
    assert dss.ActiveCircuit.AllElementNames == ref.ActiveCircuit.AllElementNames

    # Should be the same result, except for some parsing detail
    assert max(abs(ref.ActiveCircuit.AllBusVolts - dss.ActiveCircuit.AllBusVolts)) < 1e-12, 'Voltages before changing loads differ'

    all_loads = dss.Obj.Load.batch()

    with Edit(all_loads):
        all_loads.kW += 45

    dss.ActiveCircuit.Solution.Solve()


    # for load in ref.ActiveCircuit.Loads:
    #     load.kW += 45
    # # Need to force-rebuild the matrices here
    # ref.ActiveCircuit.Solution.BuildYMatrix(YMatrixModes.WholeMatrix, False)
    cmds = []
    for l in ref.ActiveCircuit.Loads:
        cmds.append(f'load.{l.Name}.kW={l.kW + 45}')

    for cmd in cmds:
        ref.Text.Command = cmd

    ref.ActiveCircuit.Solution.Solve()

    assert ref.ActiveCircuit.Solution.Converged

    # Should also be the same result now
    assert max(abs(ref.ActiveCircuit.AllBusVolts - dss.ActiveCircuit.AllBusVolts)) < 1e-12, 'Voltages after changing loads differ'

def test_create_ckt13_batch_attr():
    _test_create_ckt13_batch(1)

def test_create_ckt13_batch_new():
    _test_create_ckt13_batch(2)

def test_create_ckt13_batch_df():
    _test_create_ckt13_batch(3)


if __name__ == '__main__':
    # Adjust for manual running a test-case
    test_create_ckt13_batch_df()