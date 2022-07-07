'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira
Copyright (c) 2018-2022 DSS Extensions contributors
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

        num_channels = self.CheckForError(self._lib.Monitors_Get_NumChannels())
        if Index < 1 or Index > num_channels:
            raise DSSException(
                'Monitors.Channel: Invalid channel index ({}), monitor "{}" has {} channels.'.format(
                Index, self.Name, num_channels
            ))
        
        ffi = self._api_util.ffi
        self.CheckForError(self._lib.Monitors_Get_ByteStream_GR())
        ptr, cnt = self._api_util.gr_int8_pointers
        cnt = cnt[0]
        if cnt == 272:
            return np.zeros((1,), dtype=np.float32)

        ptr = ptr[0]
        record_size = ffi.cast('int32_t*', ptr)[2] + 2
        data = np.frombuffer(ffi.buffer(ptr, cnt), dtype=np.float32, offset=272)
        return data[(Index + 1)::record_size].copy()

    def AsMatrix(self):
        '''
        Matrix of the active monitor, containing the hour vector, seconds vector, and all channels (index 2 = channel 1).
        If you need multiple channels, prefer using this function as it processes the monitor byte-stream once.
        '''
        
        ffi = self._api_util.ffi
        self.CheckForError(self._lib.Monitors_Get_ByteStream_GR())
        ptr, cnt = self._api_util.gr_int8_pointers
        cnt = cnt[0]
        if cnt == 272:
            return None #np.zeros((0,), dtype=np.float32)

        ptr = ptr[0]
        record_size = ffi.cast('int32_t*', ptr)[2] + 2
        data = np.frombuffer(ffi.buffer(ptr, cnt), dtype=np.float32, offset=272)
        data = data.reshape((len(data) // record_size, record_size)).copy()
        return data

    def Process(self):
        self.CheckForError(self._lib.Monitors_Process())

    def ProcessAll(self):
        self.CheckForError(self._lib.Monitors_ProcessAll())

    def Reset(self):
        self.CheckForError(self._lib.Monitors_Reset())

    def ResetAll(self):
        self.CheckForError(self._lib.Monitors_ResetAll())

    def Sample(self):
        self.CheckForError(self._lib.Monitors_Sample())

    def SampleAll(self):
        self.CheckForError(self._lib.Monitors_SampleAll())

    def Save(self):
        self.CheckForError(self._lib.Monitors_Save())

    def SaveAll(self):
        self.CheckForError(self._lib.Monitors_SaveAll())

    def Show(self):
        self.CheckForError(self._lib.Monitors_Show())

    @property
    def ByteStream(self):
        '''(read-only) Byte Array containing monitor stream values. Make sure a "save" is done first (standard solution modes do this automatically)'''
        self.CheckForError(self._lib.Monitors_Get_ByteStream_GR())
        return self._get_int8_gr_array()

    @property
    def Element(self):
        '''Full object name of element being monitored.'''
        return self._get_string(self.CheckForError(self._lib.Monitors_Get_Element()))

    @Element.setter
    def Element(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.Monitors_Set_Element(Value))

    @property
    def FileName(self):
        '''(read-only) Name of CSV file associated with active Monitor.'''
        return self._get_string(self.CheckForError(self._lib.Monitors_Get_FileName()))

    @property
    def FileVersion(self):
        '''(read-only) Monitor File Version (integer)'''
        return self.CheckForError(self._lib.Monitors_Get_FileVersion())

    @property
    def Header(self):
        '''(read-only) Header string;  Array of strings containing Channel names'''
        return self.CheckForError(self._get_string_array(self._lib.Monitors_Get_Header))

    @property
    def Mode(self):
        '''Set Monitor mode (bitmask integer - see DSS Help)'''
        return self.CheckForError(self._lib.Monitors_Get_Mode()) # TODO: expose this better

    @Mode.setter
    def Mode(self, Value):
        self.CheckForError(self._lib.Monitors_Set_Mode(Value))

    @property
    def NumChannels(self):
        '''(read-only) Number of Channels in the active Monitor'''
        return self.CheckForError(self._lib.Monitors_Get_NumChannels())

    @property
    def RecordSize(self):
        '''(read-only) Size of each record in ByteStream (Integer). Same as NumChannels.'''
        return self.CheckForError(self._lib.Monitors_Get_RecordSize())

    @property
    def SampleCount(self):
        '''(read-only) Number of Samples in Monitor at Present'''
        return self.CheckForError(self._lib.Monitors_Get_SampleCount())

    @property
    def Terminal(self):
        '''Terminal number of element being monitored.'''
        return self.CheckForError(self._lib.Monitors_Get_Terminal())

    @Terminal.setter
    def Terminal(self, Value):
        self.CheckForError(self._lib.Monitors_Set_Terminal(Value))

    @property
    def dblFreq(self):
        '''(read-only) Array of doubles containing frequency values for harmonics mode solutions; Empty for time mode solutions (use dblHour)'''
        self.CheckForError(self._lib.Monitors_Get_dblFreq_GR())
        return self._get_float64_gr_array()

    @property
    def dblHour(self):
        '''(read-only) Array of doubles containing time value in hours for time-sampled monitor values; Empty if frequency-sampled values for harmonics solution (see dblFreq)'''
        self.CheckForError(self._lib.Monitors_Get_dblHour_GR())
        return self._get_float64_gr_array()
