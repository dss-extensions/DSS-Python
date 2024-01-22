from typing import List
import numpy as np
from dss.enums import SolveModes
from .common import DSSException
from .types import Float64Array, Int8Array, Float32Array

class MonitorObjMixin:
    #TODO: dataframe
    __slots__ = ()
    _extra_slots = []

    def Show(self):
        self._lib.Alt_Monitor_Show(self._ptr)

    def Header(self) -> List[str]:
        return self._get_string_array(self._lib.Alt_Monitor_Get_Header, self._ptr)

    def ByteStream(self) -> Int8Array:
        return self._get_int8_array(self._lib.Alt_Monitor_Get_ByteStream, self._ptr)

    def FileName(self) -> str:
        return self._get_string(self._lib.Alt_Monitor_Get_FileName(self._ptr))

    def SampleCount(self) -> int:
        return self._lib.Alt_Monitor_Get_SampleCount(self._ptr)

    def NumChannels(self) -> int:
        return self._lib.Alt_Monitor_Get_NumChannels(self._ptr)

    def RecordSize(self) -> int:
        return self._lib.Alt_Monitor_Get_RecordSize(self._ptr)

    def dblFreq(self) -> Float64Array:
        '''
        Frequency values for harmonics mode solutions.
        Empty for time mode solutions (use dblHour instead).
        '''
        return self._get_float64_array(self._lib.Alt_Monitor_Get_dblFreq, self._ptr)

    def dblHour(self) -> Float64Array:
        '''
        Time value in hours for time-sampled monitor values. 
        Empty if frequency-sampled values for harmonics solution (use dblFreq instead).
        '''
        return self._get_float64_array(self._lib.Alt_Monitor_Get_dblHour, self._ptr)

    def Channel(self, index: int) -> Float32Array:
        '''
        Array of float32 for the specified channel.
        A Save or SaveAll should be executed first, and that is done automatically by most standard solution modes.
        Channels start at index 1.
        '''
        num_channels = self.NumChannels()
        if index < 1 or index > num_channels:
            raise DSSException(
                0,
                'Monitor Channel: Invalid channel index ({}), monitor "{}" has {} channels.'.format(
                index, self.Name, num_channels
            ))
        
        buffer = self._get_int8_array(self._lib.Alt_Monitor_Get_ByteStream, self._ptr)
        
        if len(buffer) <= 1:
            return None
        record_size = buffer.view(dtype=np.int32)[2] + 2
        data = buffer[272:].view(dtype=np.float32)
        data = data.reshape((len(data) // record_size, record_size)).copy()
        return data


    def AsMatrix(self) -> Float64Array:
        '''
        Returns a copy of the matrix of this monitor, containing the hour vector, seconds vector, and all channels
        (index 2 = channel 1). If you need multiple channels, prefer using this function as it processes the monitor 
        byte-stream once.

        For harmonic solutions, the first two columns are the frequency and the harmonic, respectively.
        '''

        buffer = self._get_int8_array(self._lib.Alt_Monitor_Get_ByteStream, self._ptr)

        if len(buffer) <= 1:
            return None

        record_size = buffer.view(dtype=np.int32)[2] + 2
        data = buffer[272:].view(dtype=np.float32)
        data = data.reshape((len(data) // record_size, record_size)).copy()
        return data


    def ToDataFrame(self):
        '''
        Returns this monitor's data as a Pandas DataFrame

        Requires pandas
        '''
        try:
            import pandas as pd
        except ImportError:
            raise RuntimeError("Pandas is required to use this function")
            
        if self._lib.Solution_Get_Mode() in (SolveModes.Harmonic, SolveModes.HarmonicT):
            columns = ['frequency', 'harmonic']
        else:
            columns = ['hour', 'second']

        columns.extend(col.strip() for col in self.Header())
        data = self.AsMatrix()

        return pd.DataFrame(data, columns=columns)

