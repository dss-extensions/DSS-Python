'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base
import numpy as np

class IMonitors(Base):
    __slots__ = []

    def Channel(self, Index):
        '''(read-only) Array of float32 for the specified channel  (usage: MyArray = DSSMonitor.Channel(i)) A Save or SaveAll  should be executed first. Done automatically by most standard solution modes.'''
        
        ffi = self.api_util.ffi
        self.lib.Monitors_Get_ByteStream_GR()
        ptr, cnt = self.api_util.gr_int8_pointers
        cnt = cnt[0]
        if cnt == 272:
            return np.zeros((1,), dtype=np.float32)

        ptr = ptr[0]
        record_size = ffi.cast('int32_t*', ptr)[2] + 2
        data = np.frombuffer(ffi.buffer(ptr, cnt), dtype=np.float32, offset=272)
        return data[(Index + 1)::record_size]

    def AsMatrix(self):
        '''(read-only) Matrix of the active monitor, containing the hour vector, second vector, and all channels (index 2 = channel 1)'''
        
        ffi = self.api_util.ffi
        self.lib.Monitors_Get_ByteStream_GR()
        ptr, cnt = self.api_util.gr_int8_pointers
        cnt = cnt[0]
        if cnt == 272:
            return None #np.zeros((0,), dtype=np.float32)

        ptr = ptr[0]
        record_size = ffi.cast('int32_t*', ptr)[2] + 2
        data = np.frombuffer(ffi.buffer(ptr, cnt), dtype=np.float32, offset=272)
        data = data.reshape((len(data) // record_size, record_size)).copy()
        return data

    def Process(self):
        self.lib.Monitors_Process()

    def ProcessAll(self):
        self.lib.Monitors_ProcessAll()

    def Reset(self):
        self.lib.Monitors_Reset()

    def ResetAll(self):
        self.lib.Monitors_ResetAll()

    def Sample(self):
        self.lib.Monitors_Sample()

    def SampleAll(self):
        self.lib.Monitors_SampleAll()

    def Save(self):
        self.lib.Monitors_Save()

    def SaveAll(self):
        self.lib.Monitors_SaveAll()

    def Show(self):
        self.lib.Monitors_Show()

    @property
    def AllNames(self):
        '''(read-only) Array of all Monitor Names'''
        return self.get_string_array(self.lib.Monitors_Get_AllNames)

    @property
    def ByteStream(self):
        '''(read-only) Byte Array containing monitor stream values. Make sure a "save" is done first (standard solution modes do this automatically)'''
        self.lib.Monitors_Get_ByteStream_GR()
        return self.get_int8_gr_array()

    @property
    def Count(self):
        '''(read-only) Number of Monitors'''
        return self.lib.Monitors_Get_Count()

    def __len__(self):
        return self.lib.Monitors_Get_Count()

    @property
    def Element(self):
        '''Full object name of element being monitored.'''
        return self.get_string(self.lib.Monitors_Get_Element())

    @Element.setter
    def Element(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.Monitors_Set_Element(Value)

    @property
    def FileName(self):
        '''(read-only) Name of CSV file associated with active Monitor.'''
        return self.get_string(self.lib.Monitors_Get_FileName())

    @property
    def FileVersion(self):
        '''(read-only) Monitor File Version (integer)'''
        return self.lib.Monitors_Get_FileVersion()

    @property
    def First(self):
        '''(read-only) Sets the first Monitor active.  Returns 0 if no monitors.'''
        return self.lib.Monitors_Get_First()

    @property
    def Header(self):
        '''(read-only) Header string;  Array of strings containing Channel names'''
        return self.get_string_array(self.lib.Monitors_Get_Header)

    @property
    def Mode(self):
        '''Set Monitor mode (bitmask integer - see DSS Help)'''
        return self.lib.Monitors_Get_Mode()

    @Mode.setter
    def Mode(self, Value):
        self.lib.Monitors_Set_Mode(Value)

    @property
    def Name(self):
        '''Sets the active Monitor object by name'''
        return self.get_string(self.lib.Monitors_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.Monitors_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Sets next monitor active.  Returns 0 if no more.'''
        return self.lib.Monitors_Get_Next()

    @property
    def NumChannels(self):
        '''(read-only) Number of Channels in the active Monitor'''
        return self.lib.Monitors_Get_NumChannels()

    @property
    def RecordSize(self):
        '''(read-only) Size of each record in ByteStream (Integer). Same as NumChannels.'''
        return self.lib.Monitors_Get_RecordSize()

    @property
    def SampleCount(self):
        '''(read-only) Number of Samples in Monitor at Present'''
        return self.lib.Monitors_Get_SampleCount()

    @property
    def Terminal(self):
        '''Terminal number of element being monitored.'''
        return self.lib.Monitors_Get_Terminal()

    @Terminal.setter
    def Terminal(self, Value):
        self.lib.Monitors_Set_Terminal(Value)

    @property
    def dblFreq(self):
        '''(read-only) Array of doubles containing frequency values for harmonics mode solutions; Empty for time mode solutions (use dblHour)'''
        self.lib.Monitors_Get_dblFreq_GR()
        return self.get_float64_gr_array()

    @property
    def dblHour(self):
        '''(read-only) Array of doubles containgin time value in hours for time-sampled monitor values; Empty if frequency-sampled values for harmonics solution  (see dblFreq)'''
        self.lib.Monitors_Get_dblHour_GR()
        return self.get_float64_gr_array()

    def __iter__(self):
        idx = self.First
        while idx != 0:
            yield self
            idx = self.Next
