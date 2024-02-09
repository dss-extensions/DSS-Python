# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Base, DSSException
from .enums import AltDSSEvent
from dss_python_backend.events import get_manager_for_ctx

class DSSEventsConnection:
    """
    Wraps a classic DSS Event handler class and its connection state.
    This should not be manually created. Use `DSS.Events.WithEvents()`
    instead.
    """

    def __init__(self, api_util, handler):
        EVENTS = (
            AltDSSEvent.Legacy_InitControls,
            AltDSSEvent.Legacy_CheckControls,
            AltDSSEvent.Legacy_StepControls,
        )
        self._cb_manager = get_manager_for_ctx(api_util.ctx)
        self._handler = handler # keep a reference explicitly
        self._method_pairs = []
        for evt in EVENTS:
            evt_name = evt.name.split('_', 1)[1]
            func = getattr(handler, evt_name, None)
            if func is None:
                func = getattr(handler, 'On' + evt_name, None)

            if func is None:
                raise DSSException(0, f'Events: could not find method for event "{evt_name}".')

            self._method_pairs.append((evt, func))

        for evt, func in self._method_pairs:
            self._cb_manager.register_func(evt, func)

        self._connected = True


    def close(self):
        """
        Alias to disconnect; for compatibility with win32com code.
        """
        self.disconnect()


    def disconnect(self):
        """
        Disconnects the event handler associated to this o
        """
        if not self._connected:
            raise DSSException(0, 'Events: the event handler has already been disconnected.')

        for evt, func in self._method_pairs:
            self._cb_manager.unregister_func(evt, func)

        self._method_pairs.clear()

        self._connected = False


class IDSSEvents(Base):
    """
    This interface provides connection to classic the OpenDSS Events
    API. For official OpenDSS documentation about this feature, see
    the document titled "Evaluation of Distribution Reconfiguration Functions in
    Advanced Distribution Management Systems, Example Assessments of Distribution
    Automation Using Open Distribution Systems Simulator" (2011), which is available from
    EPRI at https://restservice.epri.com/publicdownload/000000000001020090/0/Product
    ([archived copy here](http://web.archive.org/web/20240121050026/https://restservice.epri.com/publicdownload/000000000001020090/0/Product)).

    VBA/Excel examples of the classic COM usage are found in the folder
    ["Examples/civinlar model/"](https://sourceforge.net/p/electricdss/code/HEAD/tree/trunk/Version8/Distrib/Examples/civinlar%20model/)
    ([mirrored here](https://github.com/dss-extensions/electricdss-tst/tree/master/Version8/Distrib/Examples/civinlar%20model),
    with minor changes), which is distributed along with the official OpenDSS.

    For a quick intro, this interface allows connecting an object (event handler)
    that runs custom actions are three points of the solution process
    (`InitControls`, `StepControls`, `CheckControls`).
    Instead of manually writing a full solution loop, users can use this to
    connect an event handler to the existing OpenDSS solution loops/algorithms,
    which allows some customization opportunities.

    Note that AltDSS/DSS C-API provides more/extra events, but this interface is
    intended to replace usage of similar `comtypes` and `win32com` features.
    That is, see [AltDSS-Python](https://github.com/dss-extensions/altdss-python)
    for the extra events, some of which are used by the AltDSS-Python itself to
    provide direct-object access.

    Since the intention is to allow easy migration (and/or interoperability)
    with both the `comtypes` and `win32com` modules, both styles of event handler
    classes are allowed:

    ```python
    class EventHandler:
        '''An event handler in the style of win32com'''
        def OnInitControls(self):
            print('Init')

        def OnStepControls(self):
            print('Step')

        def OnCheckControls(self):
            print('Check')

    # this would be used like:
    evt_conn = win32com.client.WithEvents(DSSObj.Events, EventHandler)
    ```

    or

    ```python
    class EventHandler:
        '''An event handler in the style of comtypes'''
        def InitControls(self):
            print('Init')

        def StepControls(self):
            print('Step')

        def CheckControls(self):
            print('Check')

    # this would be used like:
    iface = comtypes.gen.OpenDSSengine.IDSSEventsEvents
    evt_conn = comtypes.client.GetEvents(DSSObj.Events, EventHandler(), interface=iface)
    ```

    Like the COM implementations, DSS-Python requires that the three event types are handled.
    The method names can be either style (`OnInitControls` or `InitControls`). To make things
    easier, there are two methods in our implementation of the Events API that
    partially mimic the functions used in the COM modules. Use whichever is
    more convenient.

    ```python
    evt_conn = DSSObj.Events.WithEvents(EventHandler) # like win32com, using a class

    # or
    evt_conn = DSSObj.Events.GetEvents(EventHandler()) # like comtypes, using an object instance
    ```
    """

    __slots__ = []
    _columns = []

    @staticmethod
    def _has_required_methods(obj) -> bool:
        has_all_methods = True
        has_extra_methods = False
        if not (hasattr(obj, 'OnInitControls') or hasattr(obj, 'InitControls')):
            has_all_methods = False

        if not (hasattr(obj, 'OnStepControls') or hasattr(obj, 'StepControls')):
            has_all_methods = False

        if not (hasattr(obj, 'OnCheckControls') or hasattr(obj, 'CheckControls')):
            has_all_methods = False

        if (hasattr(obj, 'OnInitControls') == hasattr(obj, 'InitControls')):
            return False

        if (hasattr(obj, 'OnStepControls') == hasattr(obj, 'StepControls')):
            return False

        if (hasattr(obj, 'OnCheckControls') == hasattr(obj, 'CheckControls')):
            return False

        return has_all_methods


    def WithEvents(self, handler_class) -> DSSEventsConnection:
        '''
        Creates an instance of `handler_class` and connects it to
        the classic event system compatibility layer.

        This is intended to replace usage of `win32com.client.WithEvents()`
        (when previously used with the OpenDSS COM engine).

        **(API Extension)**
        '''
        if not IDSSEvents._has_required_methods(handler_class):
            raise DSSException(0, f'Events: not all event handler methods were found in the provided class ({handler_class}).')

        handler_obj = handler_class()
        return DSSEventsConnection(self._api_util, handler_obj)


    def GetEvents(self, handler_obj) -> DSSEventsConnection:
        '''
        Connects an object instance to the classic event system compatibility layer.

        This is intended to replace usage of `comtypes.client.GetEvents()`
        (when previously used with the OpenDSS COM engine).

        **(API Extension)**
        '''
        if not IDSSEvents._has_required_methods(handler_obj):
            raise DSSException(0, f'Events: not all event handler methods were found in the provided object ({handler_obj}).')

        return DSSEventsConnection(self._api_util, handler_obj)

