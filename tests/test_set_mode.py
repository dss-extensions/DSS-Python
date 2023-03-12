from dss import DSS, SolveModes as SM

# import comtypes.client
# DSS = comtypes.client.CreateObject('OpenDSSEngine.DSS')

DSS.Text.Command = "new circuit.test"
DSS.Text.Command = "solve"

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

