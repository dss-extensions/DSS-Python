import pytest
from dss import DSS, DSSException

try:
    from ._settings import BASE_DIR
except ImportError:
    from _settings import BASE_DIR

class EventHandler:
    # Note: for real usage, prefer to generate local classes bound to some
    # state, use the comtype style (pass an object) to allow more complex
    # initialization, or post-initialize the instance somehow.
    event_sequence = []
    
    def OnInitControls(self):
        EventHandler.event_sequence.append('Init')

    def OnStepControls(self):
        EventHandler.event_sequence.append('Step')

    def OnCheckControls(self):
        EventHandler.event_sequence.append('Check')


def test_events_style_win32com():
    EventHandler.event_sequence.clear()
    evt_conn = DSS.Events.WithEvents(EventHandler)

    DSS.Text.Command = f'redirect "{BASE_DIR}/Version8/Distrib/IEEETestCases/13Bus/IEEE13Nodeckt.dss"'
    DSS.Text.Command = 'solve mode=daily number=1'
    assert EventHandler.event_sequence == ['Init', 'Check', 'Check', 'Check', 'Step', 'Init', 'Check', 'Step']
    evt_conn.close()
    DSS.Text.Command = 'solve'
    assert EventHandler.event_sequence == ['Init', 'Check', 'Check', 'Check', 'Step', 'Init', 'Check', 'Step']

    with pytest.raises(DSSException):
        evt_conn.close()


def test_events_style_comtypes():
    EventHandler.event_sequence.clear()
    evt_conn = DSS.Events.GetEvents(EventHandler())

    DSS.Text.Command = f'redirect "{BASE_DIR}/Version8/Distrib/IEEETestCases/13Bus/IEEE13Nodeckt.dss"'
    DSS.Text.Command = 'solve mode=daily number=1'
    assert EventHandler.event_sequence == ['Init', 'Check', 'Check', 'Check', 'Step', 'Init', 'Check', 'Step']
    evt_conn.close()
    DSS.Text.Command = 'solve'
    assert EventHandler.event_sequence == ['Init', 'Check', 'Check', 'Check', 'Step', 'Init', 'Check', 'Step']

    with pytest.raises(DSSException):
        evt_conn.close()
