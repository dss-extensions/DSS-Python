# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from typing_extensions import TypedDict, Unpack
from .types import Float64Array, Int32Array
from . import enums
from .DSSObj import IDSSObj, DSSObj
from .Batch import DSSBatch
from .ArrayProxy import BatchInt32ArrayProxy

class Spectrum(DSSObj):
    __slots__ = DSSObj._extra_slots
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


    def _get_NumHarm(self) -> int:
        """
        Number of frequencies in this spectrum. (See CSVFile)

        DSS property name: `NumHarm`, DSS property index: 1.
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    def _set_NumHarm(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 1, value, flags)

    NumHarm = property(_get_NumHarm, _set_NumHarm) # type: int

    def _get_Harmonic(self) -> Float64Array:
        """
        Array of harmonic values. You can also use the syntax
        harmonic = (file=filename)     !for text file one value per line
        harmonic = (dblfile=filename)  !for packed file of doubles
        harmonic = (sngfile=filename)  !for packed file of singles 

        DSS property name: `Harmonic`, DSS property index: 2.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 2)

    def _set_Harmonic(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(2, value, flags)

    Harmonic = property(_get_Harmonic, _set_Harmonic) # type: Float64Array

    def _get_pctMag(self) -> Float64Array:
        """
        Array of magnitude values, assumed to be in PERCENT. You can also use the syntax
        %mag = (file=filename)     !for text file one value per line
        %mag = (dblfile=filename)  !for packed file of doubles
        %mag = (sngfile=filename)  !for packed file of singles 

        DSS property name: `%Mag`, DSS property index: 3.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 3)

    def _set_pctMag(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(3, value, flags)

    pctMag = property(_get_pctMag, _set_pctMag) # type: Float64Array

    def _get_Angle(self) -> Float64Array:
        """
        Array of phase angle values, degrees.You can also use the syntax
        angle = (file=filename)     !for text file one value per line
        angle = (dblfile=filename)  !for packed file of doubles
        angle = (sngfile=filename)  !for packed file of singles 

        DSS property name: `Angle`, DSS property index: 4.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 4)

    def _set_Angle(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(4, value, flags)

    Angle = property(_get_Angle, _set_Angle) # type: Float64Array

    def _get_CSVFile(self) -> str:
        """
        File of spectrum points with (harmonic, magnitude-percent, angle-degrees) values, one set of 3 per line, in CSV format. If fewer than NUMHARM frequencies found in the file, NUMHARM is set to the smaller value.

        DSS property name: `CSVFile`, DSS property index: 5.
        """
        return self._get_prop_string(5)

    def _set_CSVFile(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(5, value, flags)

    CSVFile = property(_get_CSVFile, _set_CSVFile) # type: str

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


    def _get_NumHarm(self) -> BatchInt32ArrayProxy:
        """
        Number of frequencies in this spectrum. (See CSVFile)

        DSS property name: `NumHarm`, DSS property index: 1.
        """
        return BatchInt32ArrayProxy(self, 1)

    def _set_NumHarm(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(1, value, flags)

    NumHarm = property(_get_NumHarm, _set_NumHarm) # type: BatchInt32ArrayProxy

    def _get_Harmonic(self) -> List[Float64Array]:
        """
        Array of harmonic values. You can also use the syntax
        harmonic = (file=filename)     !for text file one value per line
        harmonic = (dblfile=filename)  !for packed file of doubles
        harmonic = (sngfile=filename)  !for packed file of singles 

        DSS property name: `Harmonic`, DSS property index: 2.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 2)
            for x in self._unpack()
        ]

    def _set_Harmonic(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(2, value, flags)

    Harmonic = property(_get_Harmonic, _set_Harmonic) # type: List[Float64Array]

    def _get_pctMag(self) -> List[Float64Array]:
        """
        Array of magnitude values, assumed to be in PERCENT. You can also use the syntax
        %mag = (file=filename)     !for text file one value per line
        %mag = (dblfile=filename)  !for packed file of doubles
        %mag = (sngfile=filename)  !for packed file of singles 

        DSS property name: `%Mag`, DSS property index: 3.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 3)
            for x in self._unpack()
        ]

    def _set_pctMag(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(3, value, flags)

    pctMag = property(_get_pctMag, _set_pctMag) # type: List[Float64Array]

    def _get_Angle(self) -> List[Float64Array]:
        """
        Array of phase angle values, degrees.You can also use the syntax
        angle = (file=filename)     !for text file one value per line
        angle = (dblfile=filename)  !for packed file of doubles
        angle = (sngfile=filename)  !for packed file of singles 

        DSS property name: `Angle`, DSS property index: 4.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 4)
            for x in self._unpack()
        ]

    def _set_Angle(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(4, value, flags)

    Angle = property(_get_Angle, _set_Angle) # type: List[Float64Array]

    def _get_CSVFile(self) -> List[str]:
        """
        File of spectrum points with (harmonic, magnitude-percent, angle-degrees) values, one set of 3 per line, in CSV format. If fewer than NUMHARM frequencies found in the file, NUMHARM is set to the smaller value.

        DSS property name: `CSVFile`, DSS property index: 5.
        """
        return self._get_batch_str_prop(5)

    def _set_CSVFile(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(5, value, flags)

    CSVFile = property(_get_CSVFile, _set_CSVFile) # type: List[str]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 6.
        """
        self._set_batch_string(6, value, flags)

class SpectrumBatchProperties(TypedDict):
    NumHarm: Union[int, Int32Array]
    Harmonic: Float64Array
    pctMag: Float64Array
    Angle: Float64Array
    CSVFile: Union[AnyStr, List[AnyStr]]
    Like: AnyStr

class ISpectrum(IDSSObj, SpectrumBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, Spectrum, SpectrumBatch)
        SpectrumBatch.__init__(self, self._api_util, sync_cls_idx=Spectrum._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Spectrum:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[SpectrumProperties]) -> Spectrum:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[SpectrumBatchProperties]) -> SpectrumBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
