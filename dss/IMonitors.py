# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import DSSException, Iterable
import numpy as np
from typing import List, AnyStr
from ._types import Float64Array, Float32Array, Int8Array

class IMonitors(Iterable):
    __slots__ = []
    _is_circuit_element = True

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

    def Channel(self, Index: int) -> Float32Array:
        '''
        (read-only) Array of float32 for the specified channel (usage: MyArray = DSSMonitor.Channel(i)).
        A Save or SaveAll should be executed first. Done automatically by most standard solution modes.
        Channels start at index 1.

        Original COM help: https://opendss.epri.com/Channel.html
        '''

        num_channels = self._check_for_error(self._lib.Monitors_Get_NumChannels())
        if Index < 1 or Index > num_channels:
            raise DSSException(
                0,
                'Monitors.Channel: Invalid channel index ({}), monitor "{}" has {} channels.'.format(
                Index, self.Name, num_channels
            ))
        
        ffi = self._api_util.ffi
        self._check_for_error(self._lib.Monitors_Get_ByteStream_GR())
        ptr, cnt = self._api_util.gr_int8_pointers
        cnt = cnt[0]
        if cnt == 272:
            return np.zeros((1,), dtype=np.float32)

        ptr = ptr[0]
        record_size = ffi.cast('int32_t*', ptr)[2] + 2
        data = np.frombuffer(ffi.buffer(ptr, cnt), dtype=np.float32, offset=272)
        return data[(Index + 1)::record_size].copy()


    def AsMatrix(self) -> Float64Array:
        '''
        Matrix of the active monitor, containing the hour vector, seconds vector, and all channels (index 2 = channel 1).
        If you need multiple channels, prefer using this function as it processes the monitor byte-stream once.

        **(API Extension)**
        '''
        
        ffi = self._api_util.ffi
        self._check_for_error(self._lib.Monitors_Get_ByteStream_GR())
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
        '''
        Post-process monitor samples taken so far, e.g., Pst for mode=4.

        Original COM help: https://opendss.epri.com/Process.html
        '''
        self._check_for_error(self._lib.Monitors_Process())

    def ProcessAll(self):
        '''
        Post-process all monitor samples taken so far, e.g., Pst for mode=4.

        Original COM help: https://opendss.epri.com/ProcessAll.html
        '''
        self._check_for_error(self._lib.Monitors_ProcessAll())

    def Reset(self):
        '''
        Reset active Monitor object.

        Original COM help: https://opendss.epri.com/Reset3.html
        '''
        self._check_for_error(self._lib.Monitors_Reset())

    def ResetAll(self):
        '''
        Reset all Monitor objects.

        Original COM help: https://opendss.epri.com/ResetAll1.html
        '''
        self._check_for_error(self._lib.Monitors_ResetAll())

    def Sample(self):
        '''
        Instruct the active Monitor to take a sample of the present state.

        Original COM help: https://opendss.epri.com/Sample2.html
        '''
        self._check_for_error(self._lib.Monitors_Sample())

    def SampleAll(self):
        '''
        Instruct all Monitor objects to take a sample of the present state.

        Original COM help: https://opendss.epri.com/SampleAll1.html
        '''
        self._check_for_error(self._lib.Monitors_SampleAll())

    def Save(self):
        '''
        Instructs the active monitor to save its current sample buffer to its monitor stream. 
        
        After the data is on the stream, you can access the ByteStream or channel data. 

        **Most standard solution modes do this automatically.**

        Original COM help: https://opendss.epri.com/Save1.html
        '''
        self._check_for_error(self._lib.Monitors_Save())

    def SaveAll(self):
        '''
        Instructs the all monitor objects to save their current sample buffers to the respective monitor streams.
        
        **Most standard solution modes do this automatically.**

        Original COM help: https://opendss.epri.com/SaveAll1.html
        '''
        self._check_for_error(self._lib.Monitors_SaveAll())

    def Show(self):
        '''
        Convert the monitor data to text and displays it with the text editor.

        Original COM help: https://opendss.epri.com/Show3.html
        '''
        self._check_for_error(self._lib.Monitors_Show())

    @property
    def ByteStream(self) -> Int8Array:
        '''
        Byte Array containing monitor stream values. Make sure a "save" is done first (standard solution modes do this automatically)

        Original COM help: https://opendss.epri.com/ByteStream.html
        '''
        self._check_for_error(self._lib.Monitors_Get_ByteStream_GR())
        return self._get_int8_gr_array()

    @property
    def Element(self) -> str:
        '''
        Full object name of element being monitored.

        Original COM help: https://opendss.epri.com/Element.html
        '''
        return self._get_string(self._check_for_error(self._lib.Monitors_Get_Element()))

    @Element.setter
    def Element(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Monitors_Set_Element(Value))

    @property
    def FileName(self) -> str:
        '''
        Name of CSV file associated with active Monitor.

        Original COM help: https://opendss.epri.com/FileName.html
        '''
        return self._get_string(self._check_for_error(self._lib.Monitors_Get_FileName()))

    @property
    def FileVersion(self) -> int:
        '''
        Monitor File Version (integer)

        Original COM help: https://opendss.epri.com/FileVersion.html
        '''
        return self._check_for_error(self._lib.Monitors_Get_FileVersion())

    @property
    def Header(self) -> List[str]:
        '''
        Header string;  Array of strings containing Channel names

        Original COM help: https://opendss.epri.com/Header.html
        '''
        return self._check_for_error(self._get_string_array(self._lib.Monitors_Get_Header))

    @property
    def Mode(self) -> int:
        '''
        Set Monitor mode (bitmask integer - see DSS Help)

        Original COM help: https://opendss.epri.com/Mode1.html
        '''
        return self._check_for_error(self._lib.Monitors_Get_Mode()) # TODO: expose this better

    @Mode.setter
    def Mode(self, Value: int):
        self._check_for_error(self._lib.Monitors_Set_Mode(Value))

    @property
    def NumChannels(self) -> int:
        '''
        Number of Channels in the active Monitor

        Original COM help: https://opendss.epri.com/NumChannels.html
        '''
        return self._check_for_error(self._lib.Monitors_Get_NumChannels())

    @property
    def RecordSize(self) -> int:
        '''
        Size of each record in ByteStream (Integer). Same as NumChannels.

        Original COM help: https://opendss.epri.com/RecordSize.html
        '''
        return self._check_for_error(self._lib.Monitors_Get_RecordSize())

    @property
    def SampleCount(self) -> int:
        '''
        Number of Samples in Monitor at Present

        Original COM help: https://opendss.epri.com/SampleCount.html
        '''
        return self._check_for_error(self._lib.Monitors_Get_SampleCount())

    @property
    def Terminal(self) -> int:
        '''
        Terminal number of element being monitored.
        
        Original COM help: https://opendss.epri.com/Terminal.html
        '''
        return self._check_for_error(self._lib.Monitors_Get_Terminal())

    @Terminal.setter
    def Terminal(self, Value: int):
        self._check_for_error(self._lib.Monitors_Set_Terminal(Value))

    @property
    def dblFreq(self) -> Float64Array:
        '''
        Array of doubles containing frequency values for harmonics mode solutions; Empty for time mode solutions (use dblHour)
        
        Original COM help: https://opendss.epri.com/dblFreq.html
        '''
        self._check_for_error(self._lib.Monitors_Get_dblFreq_GR())
        return self._get_float64_gr_array()

    @property
    def dblHour(self) -> Float64Array:
        '''
        Array of doubles containing time value in hours for time-sampled monitor values; Empty if frequency-sampled values for harmonics solution (see dblFreq)
        
        Original COM help: https://opendss.epri.com/dblHour.html
        '''
        self._check_for_error(self._lib.Monitors_Get_dblHour_GR())
        return self._get_float64_gr_array()
