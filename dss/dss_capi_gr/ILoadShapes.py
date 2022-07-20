'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira
Copyright (c) 2018-2022 DSS Extensions contributors
'''
from .._cffi_api_util import Iterable

class ILoadShapes(Iterable):
    __slots__ = []

    _columns = [
        'Name',
        'idx',
        'UseActual',
        'Npts',
        'HrInterval',
        'MinInterval',
        'sInterval',
        'PBase',
        'Pmult',
        'QBase',
        'Qmult',
        'TimeArray',
    ]

    def New(self, Name):
        if type(Name) is not bytes:
            Name = Name.encode(self._api_util.codec)

        return self.CheckForError(self._lib.LoadShapes_New(Name))

    def Normalize(self):
        self.CheckForError(self._lib.LoadShapes_Normalize())

    @property
    def HrInterval(self):
        '''Fixed interval time value, hours.'''
        return self.CheckForError(self._lib.LoadShapes_Get_HrInterval())

    @HrInterval.setter
    def HrInterval(self, Value):
        self.CheckForError(self._lib.LoadShapes_Set_HrInterval(Value))

    @property
    def MinInterval(self):
        '''Fixed Interval time value, in minutes'''
        return self.CheckForError(self._lib.LoadShapes_Get_MinInterval())

    @MinInterval.setter
    def MinInterval(self, Value):
        self.CheckForError(self._lib.LoadShapes_Set_MinInterval(Value))

    @property
    def Npts(self):
        '''Get/set Number of points in active Loadshape.'''
        return self.CheckForError(self._lib.LoadShapes_Get_Npts())

    @Npts.setter
    def Npts(self, Value):
        self.CheckForError(self._lib.LoadShapes_Set_Npts(Value))

    @property
    def PBase(self):
        return self.CheckForError(self._lib.LoadShapes_Get_PBase())

    @PBase.setter
    def PBase(self, Value):
        self.CheckForError(self._lib.LoadShapes_Set_PBase(Value))

    Pbase = PBase

    @property
    def Pmult(self):
        '''Array of doubles for the P multiplier in the Loadshape.'''
        self.CheckForError(self._lib.LoadShapes_Get_Pmult_GR())
        return self._get_float64_gr_array()

    @Pmult.setter
    def Pmult(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.LoadShapes_Set_Pmult(ValuePtr, ValueCount))

    @property
    def QBase(self):
        '''Base for normalizing Q curve. If left at zero, the peak value is used.'''
        return self.CheckForError(self._lib.LoadShapes_Get_Qbase())

    @QBase.setter
    def QBase(self, Value):
        self.CheckForError(self._lib.LoadShapes_Set_Qbase(Value))

    Qbase = QBase

    @property
    def Qmult(self):
        '''Array of doubles containing the Q multipliers.'''
        self.CheckForError(self._lib.LoadShapes_Get_Qmult_GR())
        return self._get_float64_gr_array()

    @Qmult.setter
    def Qmult(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.LoadShapes_Set_Qmult(ValuePtr, ValueCount))

    @property
    def TimeArray(self):
        '''Time array in hours correscponding to P and Q multipliers when the Interval=0.'''
        self.CheckForError(self._lib.LoadShapes_Get_TimeArray_GR())
        return self._get_float64_gr_array()

    @TimeArray.setter
    def TimeArray(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self.CheckForError(self._lib.LoadShapes_Set_TimeArray(ValuePtr, ValueCount))

    @property
    def UseActual(self):
        '''Boolean flag to let Loads know to use the actual value in the curve rather than use the value as a multiplier.'''
        return self.CheckForError(self._lib.LoadShapes_Get_UseActual()) != 0

    @UseActual.setter
    def UseActual(self, Value):
        self.CheckForError(self._lib.LoadShapes_Set_UseActual(Value))

    @property
    def sInterval(self):
        return self.CheckForError(self._lib.LoadShapes_Get_SInterval())

    @sInterval.setter
    def sInterval(self, Value):
        self.CheckForError(self._lib.LoadShapes_Set_SInterval(Value))

    Sinterval = sInterval
    SInterval = sInterval

    def UseFloat32(self):
        '''
        Converts the current LoadShape data to float32/single precision.
        If there is no data or the data is already represented using float32, nothing is done.

        (API Extension)
        '''
        self.CheckForError(self._lib.LoadShapes_UseFloat32())

    def UseFloat64(self):
        '''
        Converts the current LoadShape data to float64/double precision.
        If there is no data or the data is already represented using float64, nothing is done.
        
        (API Extension)
        '''
        self.CheckForError(self._lib.LoadShapes_UseFloat64())
