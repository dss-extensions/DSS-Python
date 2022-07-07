'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira
'''
from .._cffi_api_util import DSSException, Iterable
import numpy as np

class IMonitors(Iterable):
    __slots__ = []

    _columns = [
        'Name',
        'FileVersion',
        'NumChannels',
        'RecordSize',
        'dblFreq',
        'Mode',
        'FileName',
        'Element',
        'Header',
        'Terminal',
        'dblHour',
        'SampleCount',
    ]

    def Channel(self, Index):
        '''
        (read-only) Array of float32 for the specified channel (usage: MyArray = DSSMonitor.Channel(i)).
        A Save or SaveAll should be executed first. Done automatically by most standard solution modes.
        Channels start at index 1.
        '''

        return self.CheckForError(self._get_float64_array(self._lib.Monitors_Get_Channel, Index))

    def AsMatrix(self):
        '''
        Matrix of the active monitor, containing the hour vector, seconds vector, and all channels (index 2 = channel 1).
        If you need multiple channels, prefer using this function as it processes the monitor byte-stream once.
        '''
        
        buffer = self._get_int8_array(self._lib.Monitors_Get_ByteStream)
        self.CheckForError()
        if len(buffer) <= 1:
            return None #np.zeros((0,), dtype=np.float32)
            
        record_size = buffer.view(dtype=np.int32)[2] + 2
        data = buffer[272:].view(dtype=np.float32)
        data = data.reshape((len(data) // record_size, record_size)).copy()
        return data

    def Process(self):
        self._lib.Monitors_Process()

    def ProcessAll(self):
        self._lib.Monitors_ProcessAll()

    def Reset(self):
        self._lib.Monitors_Reset()

    def ResetAll(self):
        self._lib.Monitors_ResetAll()

    def Sample(self):
        self._lib.Monitors_Sample()

    def SampleAll(self):
        self._lib.Monitors_SampleAll()

    def Save(self):
        self._lib.Monitors_Save()

    def SaveAll(self):
        self._lib.Monitors_SaveAll()

    def Show(self):
        self._lib.Monitors_Show()

    @property
    def ByteStream(self):
        '''(read-only) Byte Array containing monitor stream values. Make sure a "save" is done first (standard solution modes do this automatically)'''
        return self._get_int8_array(self._lib.Monitors_Get_ByteStream)

    @property
    def Element(self):
        '''Full object name of element being monitored.'''
        return self._get_string(self._lib.Monitors_Get_Element())

    @Element.setter
    def Element(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Monitors_Set_Element(Value)
        self.CheckForError()

    @property
    def FileName(self):
        '''(read-only) Name of CSV file associated with active Monitor.'''
        return self._get_string(self._lib.Monitors_Get_FileName())

    @property
    def FileVersion(self):
        '''(read-only) Monitor File Version (integer)'''
        return self._lib.Monitors_Get_FileVersion()

    @property
    def Header(self):
        '''(read-only) Header string;  Array of strings containing Channel names'''
        return self._get_string_array(self._lib.Monitors_Get_Header)

    @property
    def Mode(self):
        '''Set Monitor mode (bitmask integer - see DSS Help)'''
        return self._lib.Monitors_Get_Mode() # TODO: expose this better

    @Mode.setter
    def Mode(self, Value):
        self._lib.Monitors_Set_Mode(Value)
        self.CheckForError()

    @property
    def NumChannels(self):
        '''(read-only) Number of Channels in the active Monitor'''
        return self._lib.Monitors_Get_NumChannels()

    @property
    def RecordSize(self):
        '''(read-only) Size of each record in ByteStream (Integer). Same as NumChannels.'''
        return self._lib.Monitors_Get_RecordSize()

    @property
    def SampleCount(self):
        '''(read-only) Number of Samples in Monitor at Present'''
        return self._lib.Monitors_Get_SampleCount()

    @property
    def Terminal(self):
        '''Terminal number of element being monitored.'''
        return self._lib.Monitors_Get_Terminal()

    @Terminal.setter
    def Terminal(self, Value):
        self._lib.Monitors_Set_Terminal(Value)
        self.CheckForError()

    @property
    def dblFreq(self):
        '''(read-only) Array of doubles containing frequency values for harmonics mode solutions; Empty for time mode solutions (use dblHour)'''
        return self._get_float64_array(self._lib.Monitors_Get_dblFreq)

    @property
    def dblHour(self):
        '''(read-only) Array of doubles containing time value in hours for time-sampled monitor values; Empty if frequency-sampled values for harmonics solution (see dblFreq)'''
        return self._get_float64_array(self._lib.Monitors_Get_dblHour)
