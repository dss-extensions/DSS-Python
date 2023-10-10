import json
import numpy as np

try:
    from ._settings import BASE_DIR, WIN32
except ImportError:
    from _settings import BASE_DIR, WIN32

if WIN32:
    # When running pytest, the faulthandler seems to eager to grab FPC's exceptions, even when handled
    import faulthandler
    faulthandler.disable()
    import dss
    faulthandler.enable()
else:
    import dss

from dss import dss, Edit, IDSS #, YMatrixModes
from dss.IObj import (
    Vsource, Transformer, LineCode, Load, Line, Capacitor, 
    Connection as Conn, RegControl, DimensionUnits as Units,
)    



LoadModel = Load.LoadModel

def create_ref_ckt13(ref):
    ref.Text.Command = f'redirect "{BASE_DIR}/Version8/Distrib/IEEETestCases/13Bus/IEEE13Nodeckt.dss"'


def create_ckt13_verbose(dss):
    dss.ClearAll()
    dss.NewCircuit('IEEE13Nodeckt')
    dss.AdvancedTypes = True
    Obj = dss.Obj

    src: Vsource = Obj.Vsource[1]
    with Edit(src):
        src.basekv = 115
        src.pu = 1.0001
        src.phases = 3
        src.bus1 = 'SourceBus'
        src.angle = 30 # advance angle 30 deg so result agree with published angle
        src.MVAsc3 = 20000
        src.MVAsc1 = 21000 # stiffen the source to approximate inf source

    # Transformers and regulators
    sub: Transformer = Obj.Transformer.new('Sub')
    sub.phases = 3
    sub.windings = 2
    sub.XHL = 8 / 1000
    sub.buses = ['SourceBus', '650']
    sub.conns = [Conn.delta, Conn.wye]
    sub.kVs = [115, 4.16]
    sub.kVAs = [5000, 5000]
    sub.pctRs = [0.5 / 1000, 0.5 / 1000]
    sub.end_edit()

    for i in (1, 2, 3):
        tr: Transformer = Obj.Transformer.new(f'Reg{i}')

        tr.phases = 1
        tr.bank = 'reg1'
        tr.XHL = 0.01
        tr.kVAs = [1666, 1666]
        tr.buses = [f'650.{i}', f'RG60.{i}']
        tr.kVs = [2.4, 2.4]
        tr.pctloadloss = 0.01
        tr.end_edit()

        reg: RegControl = Obj.RegControl.new(f'Reg{i}')
        reg.transformer = tr
        reg.winding = 2
        reg.vreg = 122
        reg.band = 2
        reg.ptratio = 20
        reg.CTprim = 700
        reg.R = 3
        reg.X = 9
        reg.end_edit()

    xfm1: Transformer = Obj.Transformer.new('XFM1')
    xfm1.phases = 3
    xfm1.windings = 2
    xfm1.XHL = 2
    xfm1.buses = ['633', '634']
    xfm1.conns = [Conn.wye, Conn.wye]
    xfm1.kVs = [4.16, 0.480]
    xfm1.kVAs = [500, 500]
    xfm1.pctRs = [0.55, 0.55]
    xfm1.end_edit()

    # Line codes
    mtx601: LineCode = Obj.LineCode.new('mtx601')
    mtx601.nphases = 3
    mtx601.baseFreq = 60
    mtx601.rmatrix = [0.3465, 0.1560, 0.3375, 0.1580, 0.1535, 0.3414]
    mtx601.xmatrix = [1.0179, 0.5017, 1.0478, 0.4236, 0.3849, 1.0348]
    mtx601.units = Units.miles
    mtx601.end_edit()

    mtx602: LineCode = Obj.LineCode.new('mtx602')
    mtx602.nphases = 3
    mtx602.baseFreq = 60
    # We can pass the triangle or the full matrix for these
    # If someone calculated the matrix somehow, it would
    # be easier to pass it directly in the full form.
    mtx602.rmatrix = [
        [0.7526, 0.1580, 0.1560], 
        [0.1580, 0.7475, 0.1535], 
        [0.1560, 0.1535, 0.7436]
    ]
    mtx602.xmatrix = (1.1814, 0.4236, 1.1983, 0.5017, 0.3849, 1.2112)
    mtx602.units = Units.miles
    mtx602.end_edit()

    mtx603: LineCode = Obj.LineCode.new('mtx603')
    mtx603.nphases = 2
    mtx603.baseFreq = 60
    mtx603.rmatrix = [1.3238, 0.2066, 0.2066, 1.3294]
    mtx603.xmatrix = [1.3569, 0.4591, 0.4591, 1.3471]
    mtx603.units = Units.miles
    mtx603.end_edit()

    mtx604: LineCode = Obj.LineCode.new('mtx604')
    mtx604.nphases = 2
    mtx604.baseFreq = 60
    mtx604.rmatrix = (1.3238, 0.2066, 0.2066, 1.3294)
    mtx604.xmatrix = (1.3569, 0.4591, 0.4591, 1.3471)
    mtx604.units = Units.miles
    mtx604.end_edit()

    mtx605: LineCode = Obj.LineCode.new('mtx605')
    mtx605.nphases = 1
    mtx605.baseFreq = 60
    mtx605.rmatrix = [1.3292]
    mtx605.xmatrix = [1.3475]
    mtx605.units = Units.miles
    mtx605.end_edit()

    mtx606: LineCode = Obj.LineCode.new('mtx606')
    mtx606.nphases = 3
    mtx606.units = Units.miles
    mtx606.rmatrix = [0.791721, 0.318476, 0.781649, 0.28345, 0.318476, 0.791721]
    mtx606.xmatrix = [0.438352, 0.0276838, 0.396697, -0.0184204, 0.0276838, 0.438352]
    mtx606.cmatrix = [383.948, 0, 383.948, 0, 0, 383.948]
    mtx606.end_edit()

    mtx607: LineCode = Obj.LineCode.new('mtx607')
    mtx607.nphases = 1
    mtx607.baseFreq = 60
    mtx607.rmatrix = (1.3425,)
    mtx607.xmatrix = (0.5124,)
    mtx607.cmatrix = [236]
    mtx607.units = Units.miles
    mtx607.end_edit()

    # Loads
    l671: Load = Obj.Load.new('671')
    l671.bus1 = '671.1.2.3'
    l671.phases = 3
    l671.conn = Conn.delta
    l671.model = LoadModel.ConstantPQ
    l671.kV = 4.16
    l671.kW = 1155
    l671.kvar = 660 
    l671.end_edit()

    l634a: Load = Obj.Load.new('634a')
    l634a.bus1 = '634.1'
    l634a.phases = 1
    l634a.conn = Conn.wye
    l634a.model = LoadModel.ConstantPQ
    l634a.kV = 0.277
    l634a.kW = 160
    l634a.kvar = 110
    l634a.end_edit()

    l634b: Load = Obj.Load.new('634b')
    l634b.bus1 = '634.2'
    l634b.phases = 1
    l634b.conn = Conn.wye
    l634b.model = LoadModel.ConstantPQ
    l634b.kV = 0.277
    l634b.kW = 120
    l634b.kvar = 90
    l634b.end_edit()

    l634c: Load = Obj.Load.new('634c')
    l634c.bus1 = '634.3'
    l634c.phases = 1
    l634c.conn = Conn.wye
    l634c.model = LoadModel.ConstantPQ
    l634c.kV = 0.277
    l634c.kW = 120
    l634c.kvar = 90
    l634c.end_edit()

    l645: Load = Obj.Load.new('645')
    l645.bus1 = '645.2'
    l645.phases = 1
    l645.conn = Conn.wye
    l645.model = LoadModel.ConstantPQ
    l645.kV = 2.4
    l645.kW = 170
    l645.kvar = 125
    l645.end_edit()

    l646: Load = Obj.Load.new('646')
    l646.bus1 = '646.2.3'
    l646.phases = 1
    l646.conn = Conn.delta
    l646.model = LoadModel.ConstantZ
    l646.kV = 4.16
    l646.kW = 230
    l646.kvar = 132
    l646.end_edit()

    l692: Load = Obj.Load.new('692')
    l692.bus1 = '692.3.1'
    l692.phases = 1
    l692.conn = Conn.delta
    l692.model = LoadModel.ConstantI
    l692.kV = 4.16
    l692.kW = 170
    l692.kvar = 151
    l692.end_edit()

    l675a: Load = Obj.Load.new('675a')
    l675a.bus1 = '675.1'
    l675a.phases = 1
    l675a.conn = Conn.wye
    l675a.model = LoadModel.ConstantPQ
    l675a.kV = 2.4
    l675a.kW = 485
    l675a.kvar = 190
    l675a.end_edit()

    l675b: Load = Obj.Load.new('675b')
    l675b.bus1 = '675.2'
    l675b.phases = 1
    l675b.conn = Conn.wye
    l675b.model = LoadModel.ConstantPQ
    l675b.kV = 2.4
    l675b.kW = 68
    l675b.kvar = 60
    l675b.end_edit()

    l675c: Load = Obj.Load.new('675c')
    l675c.bus1 = '675.3'
    l675c.phases = 1
    l675c.conn = Conn.wye
    l675c.model = LoadModel.ConstantPQ
    l675c.kV = 2.4
    l675c.kW = 290
    l675c.kvar = 212
    l675c.end_edit()

    l611: Load = Obj.Load.new('611')
    l611.bus1 = '611.3'
    l611.phases = 1
    l611.conn = Conn.wye
    l611.model = LoadModel.ConstantI
    l611.kV = 2.4
    l611.kW = 170
    l611.kvar = 80
    l611.end_edit()

    l652: Load = Obj.Load.new('652')
    l652.bus1 = '652.1'
    l652.phases = 1
    l652.conn = Conn.wye
    l652.model = LoadModel.ConstantZ
    l652.kV = 2.4
    l652.kW = 128
    l652.kvar = 86
    l652.end_edit()

    l670a: Load = Obj.Load.new('670a')
    l670a.bus1 = '670.1'
    l670a.phases = 1
    l670a.conn = Conn.wye
    l670a.model = LoadModel.ConstantPQ
    l670a.kV = 2.4
    l670a.kW = 17
    l670a.kvar = 10
    l670a.end_edit()

    l670b: Load = Obj.Load.new('670b')
    l670b.bus1 = '670.2'
    l670b.phases = 1
    l670b.conn = Conn.wye
    l670b.model = LoadModel.ConstantPQ
    l670b.kV = 2.4
    l670b.kW = 66
    l670b.kvar = 38
    l670b.end_edit()

    l670c: Load = Obj.Load.new('670c')
    l670c.bus1 = '670.3'
    l670c.phases = 1
    l670c.conn = Conn.wye
    l670c.model = LoadModel.ConstantPQ
    l670c.kV = 2.4
    l670c.kW = 117
    l670c.kvar = 68
    l670c.end_edit()

    # Capacitors
    cap1: Capacitor = Obj.Capacitor.new('Cap1')
    cap1.bus1 = '675'
    cap1.phases = 3
    cap1.kvar = 600
    cap1.kv = 4.16
    cap1.end_edit()

    cap2: Capacitor = Obj.Capacitor.new('Cap2')
    cap2.bus1 = '611.3'
    cap2.phases = 1
    cap2.kvar = 100
    cap2.kv = 2.4
    cap2.end_edit()

    # Lines
    l650632 = Obj.Line.new('650632')
    l650632.phases = 3
    l650632.bus1 = 'RG60.1.2.3'
    l650632.bus2 = '632.1.2.3'
    l650632.linecode = mtx601
    l650632.length = 2000
    l650632.units = Units.ft
    l650632.end_edit()

    l632670 = Obj.Line.new('632670')
    l632670.phases = 3
    l632670.bus1 = '632.1.2.3'
    l632670.bus2 = '670.1.2.3'
    l632670.linecode = mtx601
    l632670.length = 667
    l632670.units = Units.ft
    l632670.end_edit()

    l670671 = Obj.Line.new('670671')
    l670671.phases = 3
    l670671.bus1 = '670.1.2.3'
    l670671.bus2 = '671.1.2.3'
    l670671.linecode = mtx601
    l670671.length = 1333
    l670671.units = Units.ft
    l670671.end_edit()

    l671680 = Obj.Line.new('671680')
    l671680.phases = 3
    l671680.bus1 = '671.1.2.3'
    l671680.bus2 = '680.1.2.3'
    l671680.linecode = mtx601
    l671680.length = 1000
    l671680.units = Units.ft
    l671680.end_edit()
    
    l632633 = Obj.Line.new('632633')
    l632633.phases = 3
    l632633.bus1 = '632.1.2.3'
    l632633.bus2 = '633.1.2.3'
    l632633.linecode = mtx602
    l632633.length = 500
    l632633.units = Units.ft 
    l671680.end_edit()

    l632645 = Obj.Line.new('632645')
    l632645.phases = 2
    l632645.bus1 = '632.3.2'
    l632645.bus2 = '645.3.2'
    l632645.linecode = mtx603
    l632645.length = 500
    l632645.units = Units.ft
    l632645.end_edit()

    l645646 = Obj.Line.new('645646')
    l645646.phases = 2
    l645646.bus1 = '645.3.2'
    l645646.bus2 = '646.3.2'
    l645646.linecode = mtx603
    l645646.length = 300
    l645646.units = Units.ft
    l645646.end_edit()

    l692675 = Obj.Line.new('692675')
    l692675.phases = 3
    l692675.bus1 = '692.1.2.3'
    l692675.bus2 = '675.1.2.3'
    l692675.linecode = mtx606
    l692675.length = 500
    l692675.units = Units.ft
    l692675.end_edit()

    l671684 = Obj.Line.new('671684')
    l671684.phases = 2
    l671684.bus1 = '671.1.3'
    l671684.bus2 = '684.1.3'
    l671684.linecode = mtx604
    l671684.length = 300
    l671684.units = Units.ft
    l671684.end_edit()

    l684611 = Obj.Line.new('684611')
    l684611.phases = 1
    l684611.bus1 = '684.3'
    l684611.bus2= '611.3'
    l684611.linecode = mtx605
    l684611.length = 300
    l684611.units = Units.ft
    l684611.end_edit()

    l684652 = Obj.Line.new('684652')
    l684652.phases = 1
    l684652.bus1 = '684.1'
    l684652.bus2 = '652.1'
    l684652.linecode = mtx607
    l684652.length = 800
    l684652.units = Units.ft
    l684652.end_edit()

    # Switch
    sw671692 = Obj.Line.new('671692')
    sw671692.phases = 3
    sw671692.bus1 = '671'
    sw671692.bus2 = '692'
    sw671692.Switch = True
    sw671692.r1 = 1e-4
    sw671692.r0 = 1e-4
    sw671692.x1 = 0.0
    sw671692.x0 = 0.0
    sw671692.C1 = 0.0
    sw671692.C0 = 0.0
    sw671692.end_edit()

    dss.Text.Command = 'Set VoltageBases=[115, 4.16, .48]'
    dss.Text.Command = 'CalcV'
    dss.ActiveCircuit.Solution.Solve()


def create_ckt13_shortcut(dss: IDSS):
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
    Load.new('671', bus1='671.1.2.3', phases=3, conn=Conn.delta, model=LoadModel.ConstantPQ, kV=4.16, kW=1155, kvar=660)
    Load.new('634a', bus1='634.1', phases=1, conn=Conn.wye, model=LoadModel.ConstantPQ, kV=0.277, kW=160, kvar=110)
    Load.new('634b', bus1='634.2', phases=1, conn=Conn.wye, model=LoadModel.ConstantPQ, kV=0.277, kW=120, kvar=90)
    Load.new('634c', bus1='634.3', phases=1, conn=Conn.wye, model=LoadModel.ConstantPQ, kV=0.277, kW=120, kvar=90)
    Load.new('645', bus1='645.2', phases=1, conn=Conn.wye, model=LoadModel.ConstantPQ, kV=2.4, kW=170, kvar=125)
    Load.new('646', bus1='646.2.3', phases=1, conn=Conn.delta, model=LoadModel.ConstantZ, kV=4.16, kW=230, kvar=132)
    Load.new('692', bus1='692.3.1', phases=1, conn=Conn.delta, model=LoadModel.ConstantI, kV=4.16, kW=170, kvar=151)
    Load.new('675a', bus1='675.1', phases=1, conn=Conn.wye, model=LoadModel.ConstantPQ, kV=2.4, kW=485, kvar=190)
    Load.new('675b', bus1='675.2', phases=1, conn=Conn.wye, model=LoadModel.ConstantPQ, kV=2.4, kW=68, kvar=60)
    Load.new('675c', bus1='675.3', phases=1, conn=Conn.wye, model=LoadModel.ConstantPQ, kV=2.4, kW=290, kvar=212)
    Load.new('611', bus1='611.3', phases=1, conn=Conn.wye, model=LoadModel.ConstantI, kV=2.4, kW=170, kvar=80)
    Load.new('652', bus1='652.1', phases=1, conn=Conn.wye, model=LoadModel.ConstantZ, kV=2.4, kW=128, kvar=86)
    Load.new('670a', bus1='670.1', phases=1, conn=Conn.wye, model=LoadModel.ConstantPQ, kV=2.4, kW=17, kvar=10)
    Load.new('670b', bus1='670.2', phases=1, conn=Conn.wye, model=LoadModel.ConstantPQ, kV=2.4, kW=66, kvar=38)
    Load.new('670c', bus1='670.3', phases=1, conn=Conn.wye, model=LoadModel.ConstantPQ, kV=2.4, kW=117, kvar=68)

    # Capacitors
    Capacitor.new('Cap1', bus1='675', phases=3, kvar=600, kv=4.16)
    Capacitor.new('Cap2', bus1='611.3', phases=1, kvar=100, kv=2.4)

    # Lines
    Line.new('650632', phases=3, bus1='RG60.1.2.3', bus2='632.1.2.3', linecode=mtx601, length=2000, units=Units.ft)
    Line.new('632670', phases=3, bus1='632.1.2.3', bus2='670.1.2.3', linecode=mtx601, length=667, units=Units.ft)
    Line.new('670671', phases=3, bus1='670.1.2.3', bus2='671.1.2.3', linecode=mtx601, length=1333, units=Units.ft)
    Line.new('671680', phases=3, bus1='671.1.2.3', bus2='680.1.2.3', linecode=mtx601, length=1000, units=Units.ft)
    Line.new('632633', phases=3, bus1='632.1.2.3', bus2='633.1.2.3', linecode=mtx602, length=500, units=Units.ft)
    Line.new('632645', phases=2, bus1='632.3.2', bus2='645.3.2', linecode=mtx603, length=500, units=Units.ft)
    Line.new('645646', phases=2, bus1='645.3.2', bus2='646.3.2', linecode=mtx603, length=300, units=Units.ft)
    Line.new('692675', phases=3, bus1='692.1.2.3', bus2='675.1.2.3', linecode=mtx606, length=500, units=Units.ft)
    Line.new('671684', phases=2, bus1='671.1.3', bus2='684.1.3', linecode=mtx604, length=300, units=Units.ft)
    Line.new('684611', phases=1, bus1='684.3', bus2='611.3', linecode=mtx605, length=300, units=Units.ft)
    Line.new('684652', phases=1, bus1='684.1', bus2='652.1', linecode=mtx607, length=800, units=Units.ft)

    # Switch
    Line.new('671692', phases=3, bus1='671', bus2='692', Switch=True, r1=1e-4, r0=1e-4, x1=0.0, x0=0.0, C1=0.0, C0=0.0)

    dss.Text.Command = 'Set VoltageBases=[115, 4.16, .48]'
    dss.Text.Command = 'CalcV'
    dss.ActiveCircuit.Solution.Solve()


def test_create_ckt13_verbose():
    '''
    This is the more verbose version; we don't expect anyone to do this since
    the data is usually loaded from other sources... but we still need to test it.
    '''

    create_ckt13_verbose(dss)
    ref: IDSS = dss.NewContext()
    create_ref_ckt13(ref)

    assert dss.ActiveCircuit.Lines.AllNames == ref.ActiveCircuit.Lines.AllNames
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


def test_create_ckt13_shortcut():
    '''
    This is the more verbose version; we don't expect anyone to do this since
    the data is usually loaded from other sources... but we still need to test it.
    '''

    create_ckt13_shortcut(dss)
    ref: IDSS = dss.NewContext()
    create_ref_ckt13(ref)

    assert dss.ActiveCircuit.Lines.AllNames == ref.ActiveCircuit.Lines.AllNames
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


def test_complex_property():
    dss.ClearAll()
    dss.NewCircuit('TestReactor')
    Obj = dss.Obj
    reactor1 = Obj.Reactor.new('reactor1')
    reactor1.Z1 = (1.1 + 4.5j)
    reactor2 = Obj.Reactor.new('reactor2')
    reactor2.Z1 = (7.6 + 2.7j)

    assert reactor1.Z1 == (1.1 + 4.5j)
    assert reactor1.Z2 == (1.1 + 4.5j)
    assert reactor2.Z1 == (7.6 + 2.7j)

    z1_json = complex(*json.loads(reactor1.to_json())['Z1'])
    assert z1_json == (1.1 + 4.5j)

    batch = Obj.Reactor.batch()
    z1s = batch.Z1
    np.testing.assert_equal(z1s, [(1.1 + 4.5j), (7.6 + 2.7j)])

    batch.Z1 = [(31.1 + 24.5j), (27.6 + 52.7j)]
    assert reactor1.Z1 == (31.1 + 24.5j)
    assert reactor2.Z1 == (27.6 + 52.7j)


if __name__ == '__main__':
    # Adjust for manual running a test-case
    test_create_ckt13_shortcut()
