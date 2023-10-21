# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from enum import IntEnum
from typing_extensions import TypedDict, Unpack
import numpy as np
from ._obj_bases import (
    BatchFloat64ArrayProxy,
    BatchInt32ArrayProxy,
    DSSObj,
    DSSBatch,
    IDSSObj,
    LIST_LIKE,
    # NotSet,
)
from .._types import Float64Array, Int32Array
from .._cffi_api_util import Base
from . import enums

class Spectrum(DSSObj, ):
    __slots__ = []
    _cls_name = 'Spectrum'
    _cls_idx = 8
    _cls_prop_idx = {
        'numharm': 1,
        'harmonic': 2,
        'pctmag': 3,
        '%mag': 3,
        'angle': 4,
        'csvfile': 5,
        'like': 6,
    }

    @property
    def NumHarm(self) -> int:
        """
        Number of frequencies in this spectrum. (See CSVFile)

        DSS property name: `NumHarm`, DSS property index: 1.
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @NumHarm.setter
    def NumHarm(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def Harmonic(self) -> Float64Array:
        """
        Array of harmonic values. You can also use the syntax
        harmonic = (file=filename)     !for text file one value per line
        harmonic = (dblfile=filename)  !for packed file of doubles
        harmonic = (sngfile=filename)  !for packed file of singles 

        DSS property name: `Harmonic`, DSS property index: 2.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 2)

    @Harmonic.setter
    def Harmonic(self, value: Float64Array):
        self._set_float64_array_o(2, value)

    @property
    def pctMag(self) -> Float64Array:
        """
        Array of magnitude values, assumed to be in PERCENT. You can also use the syntax
        %mag = (file=filename)     !for text file one value per line
        %mag = (dblfile=filename)  !for packed file of doubles
        %mag = (sngfile=filename)  !for packed file of singles 

        DSS property name: `%Mag`, DSS property index: 3.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 3)

    @pctMag.setter
    def pctMag(self, value: Float64Array):
        self._set_float64_array_o(3, value)

    @property
    def Angle(self) -> Float64Array:
        """
        Array of phase angle values, degrees.You can also use the syntax
        angle = (file=filename)     !for text file one value per line
        angle = (dblfile=filename)  !for packed file of doubles
        angle = (sngfile=filename)  !for packed file of singles 

        DSS property name: `Angle`, DSS property index: 4.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 4)

    @Angle.setter
    def Angle(self, value: Float64Array):
        self._set_float64_array_o(4, value)

    @property
    def CSVFile(self) -> str:
        """
        File of spectrum points with (harmonic, magnitude-percent, angle-degrees) values, one set of 3 per line, in CSV format. If fewer than NUMHARM frequencies found in the file, NUMHARM is set to the smaller value.

        DSS property name: `CSVFile`, DSS property index: 5.
        """
        return self._get_prop_string(5)

    @CSVFile.setter
    def CSVFile(self, value: AnyStr):
        self._set_string_o(5, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 6.
        """
        self._set_string_o(6, value)


class SpectrumProperties(TypedDict):
    NumHarm: int
    Harmonic: Float64Array
    pctMag: Float64Array
    Angle: Float64Array
    CSVFile: AnyStr
    Like: AnyStr

class SpectrumBatch(DSSBatch):
    _cls_name = 'Spectrum'
    _obj_cls = Spectrum
    _cls_idx = 8


    @property
    def NumHarm(self) -> BatchInt32ArrayProxy:
        """
        Number of frequencies in this spectrum. (See CSVFile)

        DSS property name: `NumHarm`, DSS property index: 1.
        """
        return BatchInt32ArrayProxy(self, 1)

    @NumHarm.setter
    def NumHarm(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(1, value)

    @property
    def Harmonic(self) -> List[Float64Array]:
        """
        Array of harmonic values. You can also use the syntax
        harmonic = (file=filename)     !for text file one value per line
        harmonic = (dblfile=filename)  !for packed file of doubles
        harmonic = (sngfile=filename)  !for packed file of singles 

        DSS property name: `Harmonic`, DSS property index: 2.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 2)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Harmonic.setter
    def Harmonic(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(2, value)

    @property
    def pctMag(self) -> List[Float64Array]:
        """
        Array of magnitude values, assumed to be in PERCENT. You can also use the syntax
        %mag = (file=filename)     !for text file one value per line
        %mag = (dblfile=filename)  !for packed file of doubles
        %mag = (sngfile=filename)  !for packed file of singles 

        DSS property name: `%Mag`, DSS property index: 3.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 3)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @pctMag.setter
    def pctMag(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(3, value)

    @property
    def Angle(self) -> List[Float64Array]:
        """
        Array of phase angle values, degrees.You can also use the syntax
        angle = (file=filename)     !for text file one value per line
        angle = (dblfile=filename)  !for packed file of doubles
        angle = (sngfile=filename)  !for packed file of singles 

        DSS property name: `Angle`, DSS property index: 4.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 4)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Angle.setter
    def Angle(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(4, value)

    @property
    def CSVFile(self) -> List[str]:
        """
        File of spectrum points with (harmonic, magnitude-percent, angle-degrees) values, one set of 3 per line, in CSV format. If fewer than NUMHARM frequencies found in the file, NUMHARM is set to the smaller value.

        DSS property name: `CSVFile`, DSS property index: 5.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 5) 

    @CSVFile.setter
    def CSVFile(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(5, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 6.
        """
        self._set_batch_string(6, value)

class SpectrumBatchProperties(TypedDict):
    NumHarm: Union[int, Int32Array]
    Harmonic: Float64Array
    pctMag: Float64Array
    Angle: Float64Array
    CSVFile: Union[AnyStr, List[AnyStr]]
    Like: AnyStr

class ISpectrum(IDSSObj):
    def __init__(self, iobj):
        super().__init__(iobj, Spectrum, SpectrumBatch)

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Spectrum:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[SpectrumProperties]) -> Spectrum:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[SpectrumBatchProperties]) -> SpectrumBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)