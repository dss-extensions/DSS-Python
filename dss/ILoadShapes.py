# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Iterable
from ._types import Float64Array
from typing import AnyStr

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

    def New(self, Name: AnyStr):
        '''Create a new LoadShape, with default parameters'''
        if not isinstance(Name, bytes):
            Name = Name.encode(self._api_util.codec)

        return self._check_for_error(self._lib.LoadShapes_New(Name))

    def Normalize(self):
        '''Normalize the LoadShape data inplace'''
        self._check_for_error(self._lib.LoadShapes_Normalize())

    @property
    def HrInterval(self) -> float:
        '''
        Fixed interval time value, in hours.

        Original COM help: https://opendss.epri.com/HrInterval.html
        '''
        return self._check_for_error(self._lib.LoadShapes_Get_HrInterval())

    @HrInterval.setter
    def HrInterval(self, Value: float):
        self._check_for_error(self._lib.LoadShapes_Set_HrInterval(Value))

    @property
    def MinInterval(self) -> float:
        '''
        Fixed Interval time value, in minutes

        Original COM help: https://opendss.epri.com/MinInterval.html
        '''
        return self._check_for_error(self._lib.LoadShapes_Get_MinInterval())

    @MinInterval.setter
    def MinInterval(self, Value: float):
        self._check_for_error(self._lib.LoadShapes_Set_MinInterval(Value))

    @property
    def Npts(self) -> int:
        '''
        Get/set Number of points in active Loadshape.

        Original COM help: https://opendss.epri.com/Npts.html
        '''
        return self._check_for_error(self._lib.LoadShapes_Get_Npts())

    @Npts.setter
    def Npts(self, Value: int):
        self._check_for_error(self._lib.LoadShapes_Set_Npts(Value))

    @property
    def PBase(self) -> float:
        '''
        Base P value for normalization. Default is zero, meaning the peak will be used.

        Original COM help: https://opendss.epri.com/Pbase.html
        '''
        return self._check_for_error(self._lib.LoadShapes_Get_PBase())

    @PBase.setter
    def PBase(self, Value: float):
        self._check_for_error(self._lib.LoadShapes_Set_PBase(Value))

    Pbase = PBase

    @property
    def Pmult(self) -> Float64Array:
        '''
        Array of doubles for the P multiplier in the Loadshape.

        Original COM help: https://opendss.epri.com/Pmult.html
        '''
        self._check_for_error(self._lib.LoadShapes_Get_Pmult_GR())
        return self._get_float64_gr_array()

    @Pmult.setter
    def Pmult(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.LoadShapes_Set_Pmult(ValuePtr, ValueCount))

    @property
    def QBase(self) -> float:
        '''
        Base for normalizing Q curve. If left at zero, the peak value is used.

        Original COM help: https://opendss.epri.com/Qbase.html
        '''
        return self._check_for_error(self._lib.LoadShapes_Get_Qbase())

    @QBase.setter
    def QBase(self, Value: float):
        self._check_for_error(self._lib.LoadShapes_Set_Qbase(Value))

    Qbase = QBase

    @property
    def Qmult(self) -> Float64Array:
        '''
        Array of doubles containing the Q multipliers.

        Original COM help: https://opendss.epri.com/Qmult.html
        '''
        self._check_for_error(self._lib.LoadShapes_Get_Qmult_GR())
        return self._get_float64_gr_array()

    @Qmult.setter
    def Qmult(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.LoadShapes_Set_Qmult(ValuePtr, ValueCount))

    @property
    def TimeArray(self) -> Float64Array:
        '''
        Time array in hours corresponding to P and Q multipliers when the Interval=0.

        Original COM help: https://opendss.epri.com/TimeArray.html
        '''
        self._check_for_error(self._lib.LoadShapes_Get_TimeArray_GR())
        return self._get_float64_gr_array()

    @TimeArray.setter
    def TimeArray(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.LoadShapes_Set_TimeArray(ValuePtr, ValueCount))

    @property
    def UseActual(self) -> bool:
        '''
        Boolean flag to let Loads know to use the actual value in the curve rather than use the value as a multiplier.

        Original COM help: https://opendss.epri.com/UseActual.html
        '''
        return self._check_for_error(self._lib.LoadShapes_Get_UseActual()) != 0

    @UseActual.setter
    def UseActual(self, Value: bool):
        self._check_for_error(self._lib.LoadShapes_Set_UseActual(Value))

    @property
    def sInterval(self) -> float:
        '''
        Fixed interval time value, in seconds.

        Original COM help: https://opendss.epri.com/Sinterval.html
        '''
        return self._check_for_error(self._lib.LoadShapes_Get_SInterval())

    @sInterval.setter
    def sInterval(self, Value: float):
        self._check_for_error(self._lib.LoadShapes_Set_SInterval(Value))

    Sinterval = sInterval
    SInterval = sInterval

    def UseFloat32(self):
        '''
        Converts the current LoadShape data to float32/single precision.
        If there is no data or the data is already represented using float32, nothing is done.

        **(API Extension)**
        '''
        self._check_for_error(self._lib.LoadShapes_UseFloat32())

    def UseFloat64(self):
        '''
        Converts the current LoadShape data to float64/double precision.
        If there is no data or the data is already represented using float64, nothing is done.
        
        **(API Extension)**
        '''
        self._check_for_error(self._lib.LoadShapes_UseFloat64())
