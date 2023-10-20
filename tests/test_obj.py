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
from dss.altdss import (
    Vsource, Transformer, LineCode, Load, Line, Capacitor, 
    Connection as Conn, RegControl, LengthUnit as Units,
    IObj, LoadModel
)    

def create_ref_ckt13(ref):
    ref.Text.Command = f'redirect "{BASE_DIR}/Version8/Distrib/IEEETestCases/13Bus/IEEE13Nodeckt.dss"'


def create_ckt13_verbose(dss: IDSS):
    dss.ClearAll()
    dss.NewCircuit('IEEE13Nodeckt')
    dss.AdvancedTypes = True
    Obj = dss.Obj

    src = Obj.Vsource[1]
    with Edit(src):
        src.BasekV = 115
        src.pu = 1.0001
        src.Phases = 3
        src.Bus1 = 'SourceBus'
        src.Angle = 30 # advance angle 30 deg so result agree with published angle
        src.MVASC3 = 20000
        src.MVASC1 = 21000 # stiffen the source to approximate inf source

    # Transformers and regulators
    sub: Transformer = Obj.Transformer.new('Sub')
    sub.Phases = 3
    sub.Windings = 2
    sub.XHL = 8 / 1000
    sub.Buses = ['SourceBus', '650']
    sub.Conns = [Conn.delta, Conn.wye]
    sub.kVs = [115, 4.16]
    sub.kVAs = [5000, 5000]
    sub.pctRs = [0.5 / 1000, 0.5 / 1000]
    sub.end_edit()

    for i in (1, 2, 3):
        tr: Transformer = Obj.Transformer.new(f'Reg{i}')

        tr.Phases = 1
        tr.Bank = 'reg1'
        tr.XHL = 0.01
        tr.kVAs = [1666, 1666]
        tr.Buses = [f'650.{i}', f'RG60.{i}']
        tr.kVs = [2.4, 2.4]
        tr.pctLoadLoss = 0.01
        tr.end_edit()

        reg: RegControl = Obj.RegControl.new(f'Reg{i}')
        reg.Transformer = tr
        reg.Winding = 2
        reg.VReg = 122
        reg.Band = 2
        reg.PTRatio = 20
        reg.CTPrim = 700
        reg.R = 3
        reg.X = 9
        reg.end_edit()

    xfm1: Transformer = Obj.Transformer.new('XFM1')
    xfm1.Phases = 3
    xfm1.Windings = 2
    xfm1.XHL = 2
    xfm1.Buses = ['633', '634']
    xfm1.Conns = [Conn.wye, Conn.wye]
    xfm1.kVs = [4.16, 0.480]
    xfm1.kVAs = [500, 500]
    xfm1.pctRs = [0.55, 0.55]
    xfm1.end_edit()

    # Line codes
    mtx601: LineCode = Obj.LineCode.new('mtx601')
    mtx601.NPhases = 3
    mtx601.BaseFreq = 60
    mtx601.RMatrix = [0.3465, 0.1560, 0.3375, 0.1580, 0.1535, 0.3414]
    mtx601.XMatrix = [1.0179, 0.5017, 1.0478, 0.4236, 0.3849, 1.0348]
    mtx601.Units = Units.miles
    mtx601.end_edit()

    mtx602: LineCode = Obj.LineCode.new('mtx602')
    mtx602.NPhases = 3
    mtx602.BaseFreq = 60
    # We can pass the triangle or the full matrix for these
    # If someone calculated the matrix somehow, it would
    # be easier to pass it directly in the full form.
    mtx602.RMatrix = [
        [0.7526, 0.1580, 0.1560], 
        [0.1580, 0.7475, 0.1535], 
        [0.1560, 0.1535, 0.7436]
    ]
    mtx602.XMatrix = (1.1814, 0.4236, 1.1983, 0.5017, 0.3849, 1.2112)
    mtx602.Units = Units.miles
    mtx602.end_edit()

    mtx603: LineCode = Obj.LineCode.new('mtx603')
    mtx603.NPhases = 2
    mtx603.BaseFreq = 60
    mtx603.RMatrix = [1.3238, 0.2066, 0.2066, 1.3294]
    mtx603.XMatrix = [1.3569, 0.4591, 0.4591, 1.3471]
    mtx603.Units = Units.miles
    mtx603.end_edit()

    mtx604: LineCode = Obj.LineCode.new('mtx604')
    mtx604.NPhases = 2
    mtx604.BaseFreq = 60
    mtx604.RMatrix = (1.3238, 0.2066, 0.2066, 1.3294)
    mtx604.XMatrix = (1.3569, 0.4591, 0.4591, 1.3471)
    mtx604.Units = Units.miles
    mtx604.end_edit()

    mtx605: LineCode = Obj.LineCode.new('mtx605')
    mtx605.NPhases = 1
    mtx605.BaseFreq = 60
    mtx605.RMatrix = [1.3292]
    mtx605.XMatrix = [1.3475]
    mtx605.Units = Units.miles
    mtx605.end_edit()

    mtx606: LineCode = Obj.LineCode.new('mtx606')
    mtx606.NPhases = 3
    mtx606.Units = Units.miles
    mtx606.RMatrix = [0.791721, 0.318476, 0.781649, 0.28345, 0.318476, 0.791721]
    mtx606.XMatrix = [0.438352, 0.0276838, 0.396697, -0.0184204, 0.0276838, 0.438352]
    mtx606.CMatrix = [383.948, 0, 383.948, 0, 0, 383.948]
    mtx606.end_edit()

    mtx607: LineCode = Obj.LineCode.new('mtx607')
    mtx607.NPhases = 1
    mtx607.BaseFreq = 60
    mtx607.RMatrix = (1.3425,)
    mtx607.XMatrix = (0.5124,)
    mtx607.CMatrix = [236]
    mtx607.Units = Units.miles
    mtx607.end_edit()

    # Loads
    l671: Load = Obj.Load.new('671')
    l671.Bus1 = '671.1.2.3'
    l671.Phases = 3
    l671.Conn = Conn.delta
    l671.Model = LoadModel.ConstantPQ
    l671.kV = 4.16
    l671.kW = 1155
    l671.kvar = 660 
    l671.end_edit()

    l634a: Load = Obj.Load.new('634a')
    l634a.Bus1 = '634.1'
    l634a.Phases = 1
    l634a.Conn = Conn.wye
    l634a.Model = LoadModel.ConstantPQ
    l634a.kV = 0.277
    l634a.kW = 160
    l634a.kvar = 110
    l634a.end_edit()

    l634b: Load = Obj.Load.new('634b')
    l634b.Bus1 = '634.2'
    l634b.Phases = 1
    l634b.Conn = Conn.wye
    l634b.Model = LoadModel.ConstantPQ
    l634b.kV = 0.277
    l634b.kW = 120
    l634b.kvar = 90
    l634b.end_edit()

    l634c: Load = Obj.Load.new('634c')
    l634c.Bus1 = '634.3'
    l634c.Phases = 1
    l634c.Conn = Conn.wye
    l634c.Model = LoadModel.ConstantPQ
    l634c.kV = 0.277
    l634c.kW = 120
    l634c.kvar = 90
    l634c.end_edit()

    l645: Load = Obj.Load.new('645')
    l645.Bus1 = '645.2'
    l645.Phases = 1
    l645.Conn = Conn.wye
    l645.Model = LoadModel.ConstantPQ
    l645.kV = 2.4
    l645.kW = 170
    l645.kvar = 125
    l645.end_edit()

    l646: Load = Obj.Load.new('646')
    l646.Bus1 = '646.2.3'
    l646.Phases = 1
    l646.Conn = Conn.delta
    l646.Model = LoadModel.ConstantZ
    l646.kV = 4.16
    l646.kW = 230
    l646.kvar = 132
    l646.end_edit()

    l692: Load = Obj.Load.new('692')
    l692.Bus1 = '692.3.1'
    l692.Phases = 1
    l692.Conn = Conn.delta
    l692.Model = LoadModel.ConstantI
    l692.kV = 4.16
    l692.kW = 170
    l692.kvar = 151
    l692.end_edit()

    l675a: Load = Obj.Load.new('675a')
    l675a.Bus1 = '675.1'
    l675a.Phases = 1
    l675a.Conn = Conn.wye
    l675a.Model = LoadModel.ConstantPQ
    l675a.kV = 2.4
    l675a.kW = 485
    l675a.kvar = 190
    l675a.end_edit()

    l675b: Load = Obj.Load.new('675b')
    l675b.Bus1 = '675.2'
    l675b.Phases = 1
    l675b.Conn = Conn.wye
    l675b.Model = LoadModel.ConstantPQ
    l675b.kV = 2.4
    l675b.kW = 68
    l675b.kvar = 60
    l675b.end_edit()

    l675c: Load = Obj.Load.new('675c')
    l675c.Bus1 = '675.3'
    l675c.Phases = 1
    l675c.Conn = Conn.wye
    l675c.Model = LoadModel.ConstantPQ
    l675c.kV = 2.4
    l675c.kW = 290
    l675c.kvar = 212
    l675c.end_edit()

    l611: Load = Obj.Load.new('611')
    l611.Bus1 = '611.3'
    l611.Phases = 1
    l611.Conn = Conn.wye
    l611.Model = LoadModel.ConstantI
    l611.kV = 2.4
    l611.kW = 170
    l611.kvar = 80
    l611.end_edit()

    l652: Load = Obj.Load.new('652')
    l652.Bus1 = '652.1'
    l652.Phases = 1
    l652.Conn = Conn.wye
    l652.Model = LoadModel.ConstantZ
    l652.kV = 2.4
    l652.kW = 128
    l652.kvar = 86
    l652.end_edit()

    l670a: Load = Obj.Load.new('670a')
    l670a.Bus1 = '670.1'
    l670a.Phases = 1
    l670a.Conn = Conn.wye
    l670a.Model = LoadModel.ConstantPQ
    l670a.kV = 2.4
    l670a.kW = 17
    l670a.kvar = 10
    l670a.end_edit()

    l670b: Load = Obj.Load.new('670b')
    l670b.Bus1 = '670.2'
    l670b.Phases = 1
    l670b.Conn = Conn.wye
    l670b.Model = LoadModel.ConstantPQ
    l670b.kV = 2.4
    l670b.kW = 66
    l670b.kvar = 38
    l670b.end_edit()

    l670c: Load = Obj.Load.new('670c')
    l670c.Bus1 = '670.3'
    l670c.Phases = 1
    l670c.Conn = Conn.wye
    l670c.Model = LoadModel.ConstantPQ
    l670c.kV = 2.4
    l670c.kW = 117
    l670c.kvar = 68
    l670c.end_edit()

    # Capacitors
    cap1: Capacitor = Obj.Capacitor.new('Cap1')
    cap1.Bus1 = '675'
    cap1.Phases = 3
    cap1.kvar = 600
    cap1.kV = 4.16
    cap1.end_edit()

    cap2: Capacitor = Obj.Capacitor.new('Cap2')
    cap2.Bus1 = '611.3'
    cap2.Phases = 1
    cap2.kvar = 100
    cap2.kV = 2.4
    cap2.end_edit()

    # Lines
    l650632 = Obj.Line.new('650632')
    l650632.Phases = 3
    l650632.Bus1 = 'RG60.1.2.3'
    l650632.Bus2 = '632.1.2.3'
    l650632.LineCode = mtx601
    l650632.Length = 2000
    l650632.Units = Units.ft
    l650632.end_edit()

    l632670 = Obj.Line.new('632670')
    l632670.Phases = 3
    l632670.Bus1 = '632.1.2.3'
    l632670.Bus2 = '670.1.2.3'
    l632670.LineCode = mtx601
    l632670.Length = 667
    l632670.Units = Units.ft
    l632670.end_edit()

    l670671 = Obj.Line.new('670671')
    l670671.Phases = 3
    l670671.Bus1 = '670.1.2.3'
    l670671.Bus2 = '671.1.2.3'
    l670671.LineCode = mtx601
    l670671.Length = 1333
    l670671.Units = Units.ft
    l670671.end_edit()

    l671680 = Obj.Line.new('671680')
    l671680.Phases = 3
    l671680.Bus1 = '671.1.2.3'
    l671680.Bus2 = '680.1.2.3'
    l671680.LineCode = mtx601
    l671680.Length = 1000
    l671680.Units = Units.ft
    l671680.end_edit()
    
    l632633 = Obj.Line.new('632633')
    l632633.Phases = 3
    l632633.Bus1 = '632.1.2.3'
    l632633.Bus2 = '633.1.2.3'
    l632633.LineCode = mtx602
    l632633.Length = 500
    l632633.Units = Units.ft 
    l671680.end_edit()

    l632645 = Obj.Line.new('632645')
    l632645.Phases = 2
    l632645.Bus1 = '632.3.2'
    l632645.Bus2 = '645.3.2'
    l632645.LineCode = mtx603
    l632645.Length = 500
    l632645.Units = Units.ft
    l632645.end_edit()

    l645646 = Obj.Line.new('645646')
    l645646.Phases = 2
    l645646.Bus1 = '645.3.2'
    l645646.Bus2 = '646.3.2'
    l645646.LineCode = mtx603
    l645646.Length = 300
    l645646.Units = Units.ft
    l645646.end_edit()

    l692675 = Obj.Line.new('692675')
    l692675.Phases = 3
    l692675.Bus1 = '692.1.2.3'
    l692675.Bus2 = '675.1.2.3'
    l692675.LineCode = mtx606
    l692675.Length = 500
    l692675.Units = Units.ft
    l692675.end_edit()

    l671684 = Obj.Line.new('671684')
    l671684.Phases = 2
    l671684.Bus1 = '671.1.3'
    l671684.Bus2 = '684.1.3'
    l671684.LineCode = mtx604
    l671684.Length = 300
    l671684.Units = Units.ft
    l671684.end_edit()

    l684611 = Obj.Line.new('684611')
    l684611.Phases = 1
    l684611.Bus1 = '684.3'
    l684611.Bus2 = '611.3'
    l684611.LineCode = mtx605
    l684611.Length = 300
    l684611.Units = Units.ft
    l684611.end_edit()

    l684652 = Obj.Line.new('684652')
    l684652.Phases = 1
    l684652.Bus1 = '684.1'
    l684652.Bus2 = '652.1'
    l684652.LineCode = mtx607
    l684652.Length = 800
    l684652.Units = Units.ft
    l684652.end_edit()

    # Switch
    sw671692 = Obj.Line.new('671692')
    sw671692.Phases = 3
    sw671692.Bus1 = '671'
    sw671692.Bus2 = '692'
    sw671692.Switch = True
    sw671692.R1 = 1e-4
    sw671692.R0 = 1e-4
    sw671692.X1 = 0.0
    sw671692.X0 = 0.0
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

    src = Obj.Vsource[1]
    with Edit(src):
        src.BasekV = 115
        src.pu = 1.0001
        src.Phases = 3
        src.Bus1 = 'SourceBus'
        src.Angle = 30
        src.MVASC3 = 20000
        src.MVASC1 = 21000

    # Transformers and regulators
    Transformer.new('Sub', Phases=3, Windings=2, XHL=8 / 1000, Buses=['SourceBus', '650'], Conns=[Conn.delta, Conn.wye], kVs=[115, 4.16], kVAs=[5000, 5000], pctRs=[0.5 / 1000, 0.5 / 1000])
    for i in (1, 2, 3):
        tr = Transformer.new(f'Reg{i}', Phases=1, Bank='reg1', XHL=0.01, kVAs=[1666, 1666], Buses=[f'650.{i}', f'RG60.{i}'], kVs=[2.4, 2.4], pctLoadLoss=0.01)
        RegControl.new(f'Reg{i}', Transformer=tr, Winding=2, VReg=122, Band=2, PTRatio=20, CTPrim=700, R=3, X=9)

    Transformer.new('XFM1', Phases=3, Windings=2, XHL=2, Buses=['633', '634'], Conns=[Conn.wye, Conn.wye], kVs=[4.16, 0.480], kVAs=[500, 500], pctRs=[0.55, 0.55])
    
    # Line codes
    mtx601 = LineCode.new('mtx601', NPhases=3, BaseFreq=60, 
        RMatrix=[0.3465, 0.1560, 0.3375, 0.1580, 0.1535, 0.3414],
        XMatrix=[1.0179, 0.5017, 1.0478, 0.4236, 0.3849, 1.0348],
        Units=Units.miles
    )
    mtx602 = LineCode.new('mtx602', NPhases=3, BaseFreq=60, 
        RMatrix=[[0.7526, 0.1580, 0.1560], [0.1580, 0.7475, 0.1535], [0.1560, 0.1535, 0.7436]], 
        XMatrix=(1.1814, 0.4236, 1.1983, 0.5017, 0.3849, 1.2112), 
        Units=Units.miles
    )
    mtx603 = LineCode.new('mtx603', NPhases=2, BaseFreq=60, 
        RMatrix=[1.3238, 0.2066, 0.2066, 1.3294], XMatrix=[1.3569, 0.4591, 0.4591, 1.3471], 
        Units=Units.miles
    )
    mtx604 = LineCode.new('mtx604', NPhases=2, BaseFreq=60, 
        RMatrix=(1.3238, 0.2066, 0.2066, 1.3294), XMatrix=(1.3569, 0.4591, 0.4591, 1.3471), 
        Units=Units.miles)
    mtx605 = LineCode.new('mtx605', NPhases=1, BaseFreq=60, RMatrix=[1.3292], XMatrix=[1.3475], Units=Units.miles)
    mtx606 = LineCode.new('mtx606', NPhases=3, Units=Units.miles, 
        RMatrix=[0.791721, 0.318476, 0.781649, 0.28345, 0.318476, 0.791721], 
        XMatrix=[0.438352, 0.0276838, 0.396697, -0.0184204, 0.0276838, 0.438352], 
        CMatrix=[383.948, 0, 383.948, 0, 0, 383.948]
    )
    mtx607 = LineCode.new('mtx607', NPhases=1, BaseFreq=60, RMatrix=(1.3425,), XMatrix=(0.5124,), CMatrix=[236], Units=Units.miles)

    # Loads
    Load.new('671', Bus1='671.1.2.3', Phases=3, Conn=Conn.delta, Model=LoadModel.ConstantPQ, kV=4.16, kW=1155, kvar=660)
    Load.new('634a', Bus1='634.1', Phases=1, Conn=Conn.wye, Model=LoadModel.ConstantPQ, kV=0.277, kW=160, kvar=110)
    Load.new('634b', Bus1='634.2', Phases=1, Conn=Conn.wye, Model=LoadModel.ConstantPQ, kV=0.277, kW=120, kvar=90)
    Load.new('634c', Bus1='634.3', Phases=1, Conn=Conn.wye, Model=LoadModel.ConstantPQ, kV=0.277, kW=120, kvar=90)
    Load.new('645', Bus1='645.2', Phases=1, Conn=Conn.wye, Model=LoadModel.ConstantPQ, kV=2.4, kW=170, kvar=125)
    Load.new('646', Bus1='646.2.3', Phases=1, Conn=Conn.delta, Model=LoadModel.ConstantZ, kV=4.16, kW=230, kvar=132)
    Load.new('692', Bus1='692.3.1', Phases=1, Conn=Conn.delta, Model=LoadModel.ConstantI, kV=4.16, kW=170, kvar=151)
    Load.new('675a', Bus1='675.1', Phases=1, Conn=Conn.wye, Model=LoadModel.ConstantPQ, kV=2.4, kW=485, kvar=190)
    Load.new('675b', Bus1='675.2', Phases=1, Conn=Conn.wye, Model=LoadModel.ConstantPQ, kV=2.4, kW=68, kvar=60)
    Load.new('675c', Bus1='675.3', Phases=1, Conn=Conn.wye, Model=LoadModel.ConstantPQ, kV=2.4, kW=290, kvar=212)
    Load.new('611', Bus1='611.3', Phases=1, Conn=Conn.wye, Model=LoadModel.ConstantI, kV=2.4, kW=170, kvar=80)
    Load.new('652', Bus1='652.1', Phases=1, Conn=Conn.wye, Model=LoadModel.ConstantZ, kV=2.4, kW=128, kvar=86)
    Load.new('670a', Bus1='670.1', Phases=1, Conn=Conn.wye, Model=LoadModel.ConstantPQ, kV=2.4, kW=17, kvar=10)
    Load.new('670b', Bus1='670.2', Phases=1, Conn=Conn.wye, Model=LoadModel.ConstantPQ, kV=2.4, kW=66, kvar=38)
    Load.new('670c', Bus1='670.3', Phases=1, Conn=Conn.wye, Model=LoadModel.ConstantPQ, kV=2.4, kW=117, kvar=68)

    # Capacitors
    Capacitor.new('Cap1', Bus1='675', Phases=3, kvar=600, kV=4.16)
    Capacitor.new('Cap2', Bus1='611.3', Phases=1, kvar=100, kV=2.4)

    # Lines
    Line.new('650632', Phases=3, Bus1='RG60.1.2.3', Bus2='632.1.2.3', LineCode=mtx601, Length=2000, Units=Units.ft)
    Line.new('632670', Phases=3, Bus1='632.1.2.3', Bus2='670.1.2.3', LineCode=mtx601, Length=667, Units=Units.ft)
    Line.new('670671', Phases=3, Bus1='670.1.2.3', Bus2='671.1.2.3', LineCode=mtx601, Length=1333, Units=Units.ft)
    Line.new('671680', Phases=3, Bus1='671.1.2.3', Bus2='680.1.2.3', LineCode=mtx601, Length=1000, Units=Units.ft)
    Line.new('632633', Phases=3, Bus1='632.1.2.3', Bus2='633.1.2.3', LineCode=mtx602, Length=500, Units=Units.ft)
    Line.new('632645', Phases=2, Bus1='632.3.2', Bus2='645.3.2', LineCode=mtx603, Length=500, Units=Units.ft)
    Line.new('645646', Phases=2, Bus1='645.3.2', Bus2='646.3.2', LineCode=mtx603, Length=300, Units=Units.ft)
    Line.new('692675', Phases=3, Bus1='692.1.2.3', Bus2='675.1.2.3', LineCode=mtx606, Length=500, Units=Units.ft)
    Line.new('671684', Phases=2, Bus1='671.1.3', Bus2='684.1.3', LineCode=mtx604, Length=300, Units=Units.ft)
    Line.new('684611', Phases=1, Bus1='684.3', Bus2='611.3', LineCode=mtx605, Length=300, Units=Units.ft)
    Line.new('684652', Phases=1, Bus1='684.1', Bus2='652.1', LineCode=mtx607, Length=800, Units=Units.ft)

    # Switch
    Line.new('671692', Phases=3, Bus1='671', Bus2='692', Switch=True, R1=1e-4, R0=1e-4, X1=0.0, X0=0.0, C1=0.0, C0=0.0)

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
