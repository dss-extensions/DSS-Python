# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from typing_extensions import TypedDict, Unpack
from ._obj_bases import (
    CktElementMixin,
    PCElementMixin,
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
from .Spectrum import Spectrum as SpectrumObj
from .LoadShape import LoadShape

class IndMach012(DSSObj, CktElementMixin, PCElementMixin):
    __slots__ = CktElementMixin._extra_slots + PCElementMixin._extra_slots
    _cls_name = 'IndMach012'
    _cls_idx = 39
    _cls_prop_idx = {
        'phases': 1,
        'bus1': 2,
        'kv': 3,
        'kw': 4,
        'pf': 5,
        'conn': 6,
        'kva': 7,
        'h': 8,
        'd': 9,
        'purs': 10,
        'puxs': 11,
        'purr': 12,
        'puxr': 13,
        'puxm': 14,
        'slip': 15,
        'maxslip': 16,
        'slipoption': 17,
        'yearly': 18,
        'daily': 19,
        'duty': 20,
        'debugtrace': 21,
        'spectrum': 22,
        'basefreq': 23,
        'enabled': 24,
        'like': 25,
    }

    @property
    def Phases(self) -> int:
        """
        Number of Phases, this Induction Machine.  

        DSS property name: `Phases`, DSS property index: 1.
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    @Phases.setter
    def Phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 1, value)

    @property
    def Bus1(self) -> str:
        """
        Bus to which the Induction Machine is connected.  May include specific node specification.

        DSS property name: `Bus1`, DSS property index: 2.
        """
        return self._get_prop_string(2)

    @Bus1.setter
    def Bus1(self, value: AnyStr):
        self._set_string_o(2, value)

    @property
    def kV(self) -> float:
        """
        Nominal rated (1.0 per unit) voltage, kV. For 2- and 3-phase machines, specify phase-phase kV. Otherwise, specify actual kV across each branch of the machine. If wye (star), specify phase-neutral kV. If delta or phase-phase connected, specify phase-phase kV.

        DSS property name: `kV`, DSS property index: 3.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    @kV.setter
    def kV(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 3, value)

    @property
    def kW(self) -> float:
        """
        Shaft Power, kW, for the Induction Machine.  A positive value denotes power for a load. 
        Negative value denotes an induction generator. 

        DSS property name: `kW`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @kW.setter
    def kW(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def PF(self) -> float:
        """
        [Read Only] Present power factor for the machine. 

        DSS property name: `PF`, DSS property index: 5.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    @PF.setter
    def PF(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 5, value)

    @property
    def Conn(self) -> enums.Connection:
        """
        Connection of stator: Delta or Wye. Default is Delta.

        DSS property name: `Conn`, DSS property index: 6.
        """
        return enums.Connection(self._lib.Obj_GetInt32(self._ptr, 6))

    @Conn.setter
    def Conn(self, value: Union[AnyStr, int, enums.Connection]):
        if not isinstance(value, int):
            self._set_string_o(6, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 6, value)

    @property
    def Conn_str(self) -> str:
        """
        Connection of stator: Delta or Wye. Default is Delta.

        DSS property name: `Conn`, DSS property index: 6.
        """
        return self._get_prop_string(6)

    @Conn_str.setter
    def Conn_str(self, value: AnyStr):
        self.Conn = value

    @property
    def kVA(self) -> float:
        """
        Rated kVA for the machine.

        DSS property name: `kVA`, DSS property index: 7.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @kVA.setter
    def kVA(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def H(self) -> float:
        """
        Per unit mass constant of the machine.  MW-sec/MVA.  Default is 1.0.

        DSS property name: `H`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @H.setter
    def H(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def D(self) -> float:
        """
        Damping constant.  Usual range is 0 to 4. Default is 1.0.  Adjust to get damping in Dynamics mode,

        DSS property name: `D`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @D.setter
    def D(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def puRs(self) -> float:
        """
        Per unit stator resistance. Default is 0.0053.

        DSS property name: `puRs`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @puRs.setter
    def puRs(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def puXs(self) -> float:
        """
        Per unit stator leakage reactance. Default is 0.106.

        DSS property name: `puXs`, DSS property index: 11.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @puXs.setter
    def puXs(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def puRr(self) -> float:
        """
        Per unit rotor  resistance. Default is 0.007.

        DSS property name: `puRr`, DSS property index: 12.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    @puRr.setter
    def puRr(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 12, value)

    @property
    def puXr(self) -> float:
        """
        Per unit rotor leakage reactance. Default is 0.12.

        DSS property name: `puXr`, DSS property index: 13.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    @puXr.setter
    def puXr(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 13, value)

    @property
    def puXm(self) -> float:
        """
        Per unit magnetizing reactance.Default is 4.0.

        DSS property name: `puXm`, DSS property index: 14.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    @puXm.setter
    def puXm(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 14, value)

    @property
    def Slip(self) -> float:
        """
        Initial slip value. Default is 0.007

        DSS property name: `Slip`, DSS property index: 15.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    @Slip.setter
    def Slip(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 15, value)

    @property
    def MaxSlip(self) -> float:
        """
        Max slip value to allow. Default is 0.1. Set this before setting slip.

        DSS property name: `MaxSlip`, DSS property index: 16.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    @MaxSlip.setter
    def MaxSlip(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 16, value)

    @property
    def SlipOption(self) -> enums.IndMach012SlipOption:
        """
        Option for slip model. One of {fixedslip | variableslip*  }

        DSS property name: `SlipOption`, DSS property index: 17.
        """
        return enums.IndMach012SlipOption(self._lib.Obj_GetInt32(self._ptr, 17))

    @SlipOption.setter
    def SlipOption(self, value: Union[AnyStr, int, enums.IndMach012SlipOption]):
        if not isinstance(value, int):
            self._set_string_o(17, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 17, value)

    @property
    def SlipOption_str(self) -> str:
        """
        Option for slip model. One of {fixedslip | variableslip*  }

        DSS property name: `SlipOption`, DSS property index: 17.
        """
        return self._get_prop_string(17)

    @SlipOption_str.setter
    def SlipOption_str(self, value: AnyStr):
        self.SlipOption = value

    @property
    def Yearly(self) -> str:
        """
        LOADSHAPE object to use for yearly simulations.  Must be previously defined as a Loadshape object. Is set to the Daily load shape  when Daily is defined.  The daily load shape is repeated in this case. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. The default is no variation.

        DSS property name: `Yearly`, DSS property index: 18.
        """
        return self._get_prop_string(18)

    @Yearly.setter
    def Yearly(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(18, value)
            return

        self._set_string_o(18, value)

    @property
    def Yearly_obj(self) -> LoadShape:
        """
        LOADSHAPE object to use for yearly simulations.  Must be previously defined as a Loadshape object. Is set to the Daily load shape  when Daily is defined.  The daily load shape is repeated in this case. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. The default is no variation.

        DSS property name: `Yearly`, DSS property index: 18.
        """
        return self._get_obj(18, LoadShape)

    @Yearly_obj.setter
    def Yearly_obj(self, value: LoadShape):
        self._set_obj(18, value)

    @property
    def Daily(self) -> str:
        """
        LOADSHAPE object to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. Default is no variation (constant) if not defined. Side effect: Sets Yearly load shape if not already defined.

        DSS property name: `Daily`, DSS property index: 19.
        """
        return self._get_prop_string(19)

    @Daily.setter
    def Daily(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(19, value)
            return

        self._set_string_o(19, value)

    @property
    def Daily_obj(self) -> LoadShape:
        """
        LOADSHAPE object to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. Default is no variation (constant) if not defined. Side effect: Sets Yearly load shape if not already defined.

        DSS property name: `Daily`, DSS property index: 19.
        """
        return self._get_obj(19, LoadShape)

    @Daily_obj.setter
    def Daily_obj(self, value: LoadShape):
        self._set_obj(19, value)

    @property
    def Duty(self) -> str:
        """
        LOADSHAPE object to use for duty cycle simulations.  Must be previously defined as a Loadshape object.  Typically would have time intervals less than 1 hr. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.Set to NONE to reset to no loadshape. Set Status=Fixed to ignore Loadshape designation.  Defaults to Daily curve If not specified.

        DSS property name: `Duty`, DSS property index: 20.
        """
        return self._get_prop_string(20)

    @Duty.setter
    def Duty(self, value: Union[AnyStr, LoadShape]):
        if isinstance(value, DSSObj):
            self._set_obj(20, value)
            return

        self._set_string_o(20, value)

    @property
    def Duty_obj(self) -> LoadShape:
        """
        LOADSHAPE object to use for duty cycle simulations.  Must be previously defined as a Loadshape object.  Typically would have time intervals less than 1 hr. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.Set to NONE to reset to no loadshape. Set Status=Fixed to ignore Loadshape designation.  Defaults to Daily curve If not specified.

        DSS property name: `Duty`, DSS property index: 20.
        """
        return self._get_obj(20, LoadShape)

    @Duty_obj.setter
    def Duty_obj(self, value: LoadShape):
        self._set_obj(20, value)

    @property
    def DebugTrace(self) -> bool:
        """
        [Yes | No*] Write DebugTrace file.

        DSS property name: `DebugTrace`, DSS property index: 21.
        """
        return self._lib.Obj_GetInt32(self._ptr, 21) != 0

    @DebugTrace.setter
    def DebugTrace(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 21, value)

    @property
    def Spectrum(self) -> str:
        """
        Name of harmonic voltage or current spectrum for this IndMach012. Voltage behind Xd" for machine - default. Current injection for inverter. Default value is "default", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 22.
        """
        return self._get_prop_string(22)

    @Spectrum.setter
    def Spectrum(self, value: Union[AnyStr, SpectrumObj]):
        if isinstance(value, DSSObj):
            self._set_obj(22, value)
            return

        self._set_string_o(22, value)

    @property
    def Spectrum_obj(self) -> SpectrumObj:
        """
        Name of harmonic voltage or current spectrum for this IndMach012. Voltage behind Xd" for machine - default. Current injection for inverter. Default value is "default", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 22.
        """
        return self._get_obj(22, SpectrumObj)

    @Spectrum_obj.setter
    def Spectrum_obj(self, value: SpectrumObj):
        self._set_obj(22, value)

    @property
    def BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 23.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    @BaseFreq.setter
    def BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 23, value)

    @property
    def Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 24.
        """
        return self._lib.Obj_GetInt32(self._ptr, 24) != 0

    @Enabled.setter
    def Enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 24, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 25.
        """
        self._set_string_o(25, value)


class IndMach012Properties(TypedDict):
    Phases: int
    Bus1: AnyStr
    kV: float
    kW: float
    PF: float
    Conn: Union[AnyStr, int, enums.Connection]
    kVA: float
    H: float
    D: float
    puRs: float
    puXs: float
    puRr: float
    puXr: float
    puXm: float
    Slip: float
    MaxSlip: float
    SlipOption: Union[AnyStr, int, enums.IndMach012SlipOption]
    Yearly: Union[AnyStr, LoadShape]
    Daily: Union[AnyStr, LoadShape]
    Duty: Union[AnyStr, LoadShape]
    DebugTrace: bool
    Spectrum: Union[AnyStr, SpectrumObj]
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class IndMach012Batch(DSSBatch):
    _cls_name = 'IndMach012'
    _obj_cls = IndMach012
    _cls_idx = 39


    @property
    def Phases(self) -> BatchInt32ArrayProxy:
        """
        Number of Phases, this Induction Machine.  

        DSS property name: `Phases`, DSS property index: 1.
        """
        return BatchInt32ArrayProxy(self, 1)

    @Phases.setter
    def Phases(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(1, value)

    @property
    def Bus1(self) -> List[str]:
        """
        Bus to which the Induction Machine is connected.  May include specific node specification.

        DSS property name: `Bus1`, DSS property index: 2.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 2) 

    @Bus1.setter
    def Bus1(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(2, value)

    @property
    def kV(self) -> BatchFloat64ArrayProxy:
        """
        Nominal rated (1.0 per unit) voltage, kV. For 2- and 3-phase machines, specify phase-phase kV. Otherwise, specify actual kV across each branch of the machine. If wye (star), specify phase-neutral kV. If delta or phase-phase connected, specify phase-phase kV.

        DSS property name: `kV`, DSS property index: 3.
        """
        return BatchFloat64ArrayProxy(self, 3)

    @kV.setter
    def kV(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(3, value)

    @property
    def kW(self) -> BatchFloat64ArrayProxy:
        """
        Shaft Power, kW, for the Induction Machine.  A positive value denotes power for a load. 
        Negative value denotes an induction generator. 

        DSS property name: `kW`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    @kW.setter
    def kW(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(4, value)

    @property
    def PF(self) -> BatchFloat64ArrayProxy:
        """
        [Read Only] Present power factor for the machine. 

        DSS property name: `PF`, DSS property index: 5.
        """
        return BatchFloat64ArrayProxy(self, 5)

    @PF.setter
    def PF(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(5, value)

    @property
    def Conn(self) -> BatchInt32ArrayProxy:
        """
        Connection of stator: Delta or Wye. Default is Delta.

        DSS property name: `Conn`, DSS property index: 6.
        """
        return BatchInt32ArrayProxy(self, 6)

    @Conn.setter
    def Conn(self, value: Union[AnyStr, int, enums.Connection, List[AnyStr], List[int], List[enums.Connection], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(6, value)
            return
    
        self._set_batch_int32_array(6, value)

    @property
    def Conn_str(self) -> str:
        """
        Connection of stator: Delta or Wye. Default is Delta.

        DSS property name: `Conn`, DSS property index: 6.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 6)

    @Conn_str.setter
    def Conn_str(self, value: AnyStr):
        self.Conn = value

    @property
    def kVA(self) -> BatchFloat64ArrayProxy:
        """
        Rated kVA for the machine.

        DSS property name: `kVA`, DSS property index: 7.
        """
        return BatchFloat64ArrayProxy(self, 7)

    @kVA.setter
    def kVA(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(7, value)

    @property
    def H(self) -> BatchFloat64ArrayProxy:
        """
        Per unit mass constant of the machine.  MW-sec/MVA.  Default is 1.0.

        DSS property name: `H`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    @H.setter
    def H(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(8, value)

    @property
    def D(self) -> BatchFloat64ArrayProxy:
        """
        Damping constant.  Usual range is 0 to 4. Default is 1.0.  Adjust to get damping in Dynamics mode,

        DSS property name: `D`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    @D.setter
    def D(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(9, value)

    @property
    def puRs(self) -> BatchFloat64ArrayProxy:
        """
        Per unit stator resistance. Default is 0.0053.

        DSS property name: `puRs`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    @puRs.setter
    def puRs(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(10, value)

    @property
    def puXs(self) -> BatchFloat64ArrayProxy:
        """
        Per unit stator leakage reactance. Default is 0.106.

        DSS property name: `puXs`, DSS property index: 11.
        """
        return BatchFloat64ArrayProxy(self, 11)

    @puXs.setter
    def puXs(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(11, value)

    @property
    def puRr(self) -> BatchFloat64ArrayProxy:
        """
        Per unit rotor  resistance. Default is 0.007.

        DSS property name: `puRr`, DSS property index: 12.
        """
        return BatchFloat64ArrayProxy(self, 12)

    @puRr.setter
    def puRr(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(12, value)

    @property
    def puXr(self) -> BatchFloat64ArrayProxy:
        """
        Per unit rotor leakage reactance. Default is 0.12.

        DSS property name: `puXr`, DSS property index: 13.
        """
        return BatchFloat64ArrayProxy(self, 13)

    @puXr.setter
    def puXr(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(13, value)

    @property
    def puXm(self) -> BatchFloat64ArrayProxy:
        """
        Per unit magnetizing reactance.Default is 4.0.

        DSS property name: `puXm`, DSS property index: 14.
        """
        return BatchFloat64ArrayProxy(self, 14)

    @puXm.setter
    def puXm(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(14, value)

    @property
    def Slip(self) -> BatchFloat64ArrayProxy:
        """
        Initial slip value. Default is 0.007

        DSS property name: `Slip`, DSS property index: 15.
        """
        return BatchFloat64ArrayProxy(self, 15)

    @Slip.setter
    def Slip(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(15, value)

    @property
    def MaxSlip(self) -> BatchFloat64ArrayProxy:
        """
        Max slip value to allow. Default is 0.1. Set this before setting slip.

        DSS property name: `MaxSlip`, DSS property index: 16.
        """
        return BatchFloat64ArrayProxy(self, 16)

    @MaxSlip.setter
    def MaxSlip(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(16, value)

    @property
    def SlipOption(self) -> BatchInt32ArrayProxy:
        """
        Option for slip model. One of {fixedslip | variableslip*  }

        DSS property name: `SlipOption`, DSS property index: 17.
        """
        return BatchInt32ArrayProxy(self, 17)

    @SlipOption.setter
    def SlipOption(self, value: Union[AnyStr, int, enums.IndMach012SlipOption, List[AnyStr], List[int], List[enums.IndMach012SlipOption], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(17, value)
            return
    
        self._set_batch_int32_array(17, value)

    @property
    def SlipOption_str(self) -> str:
        """
        Option for slip model. One of {fixedslip | variableslip*  }

        DSS property name: `SlipOption`, DSS property index: 17.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 17)

    @SlipOption_str.setter
    def SlipOption_str(self, value: AnyStr):
        self.SlipOption = value

    @property
    def Yearly(self) -> List[str]:
        """
        LOADSHAPE object to use for yearly simulations.  Must be previously defined as a Loadshape object. Is set to the Daily load shape  when Daily is defined.  The daily load shape is repeated in this case. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. The default is no variation.

        DSS property name: `Yearly`, DSS property index: 18.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 18)

    @Yearly.setter
    def Yearly(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]):
        self._set_batch_obj_prop(18, value)

    @property
    def Yearly_obj(self) -> List[LoadShape]:
        """
        LOADSHAPE object to use for yearly simulations.  Must be previously defined as a Loadshape object. Is set to the Daily load shape  when Daily is defined.  The daily load shape is repeated in this case. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. The default is no variation.

        DSS property name: `Yearly`, DSS property index: 18.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 18)

    @Yearly_obj.setter
    def Yearly_obj(self, value: LoadShape):
        self._set_batch_string(18, value)

    @property
    def Daily(self) -> List[str]:
        """
        LOADSHAPE object to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. Default is no variation (constant) if not defined. Side effect: Sets Yearly load shape if not already defined.

        DSS property name: `Daily`, DSS property index: 19.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 19)

    @Daily.setter
    def Daily(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]):
        self._set_batch_obj_prop(19, value)

    @property
    def Daily_obj(self) -> List[LoadShape]:
        """
        LOADSHAPE object to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. Default is no variation (constant) if not defined. Side effect: Sets Yearly load shape if not already defined.

        DSS property name: `Daily`, DSS property index: 19.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 19)

    @Daily_obj.setter
    def Daily_obj(self, value: LoadShape):
        self._set_batch_string(19, value)

    @property
    def Duty(self) -> List[str]:
        """
        LOADSHAPE object to use for duty cycle simulations.  Must be previously defined as a Loadshape object.  Typically would have time intervals less than 1 hr. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.Set to NONE to reset to no loadshape. Set Status=Fixed to ignore Loadshape designation.  Defaults to Daily curve If not specified.

        DSS property name: `Duty`, DSS property index: 20.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 20)

    @Duty.setter
    def Duty(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]):
        self._set_batch_obj_prop(20, value)

    @property
    def Duty_obj(self) -> List[LoadShape]:
        """
        LOADSHAPE object to use for duty cycle simulations.  Must be previously defined as a Loadshape object.  Typically would have time intervals less than 1 hr. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.Set to NONE to reset to no loadshape. Set Status=Fixed to ignore Loadshape designation.  Defaults to Daily curve If not specified.

        DSS property name: `Duty`, DSS property index: 20.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 20)

    @Duty_obj.setter
    def Duty_obj(self, value: LoadShape):
        self._set_batch_string(20, value)

    @property
    def DebugTrace(self) -> List[bool]:
        """
        [Yes | No*] Write DebugTrace file.

        DSS property name: `DebugTrace`, DSS property index: 21.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 21)
        ]
    @DebugTrace.setter
    def DebugTrace(self, value: bool):
        self._set_batch_int32_array(21, value)

    @property
    def Spectrum(self) -> List[str]:
        """
        Name of harmonic voltage or current spectrum for this IndMach012. Voltage behind Xd" for machine - default. Current injection for inverter. Default value is "default", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 22.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 22)

    @Spectrum.setter
    def Spectrum(self, value: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]]):
        self._set_batch_obj_prop(22, value)

    @property
    def Spectrum_obj(self) -> List[SpectrumObj]:
        """
        Name of harmonic voltage or current spectrum for this IndMach012. Voltage behind Xd" for machine - default. Current injection for inverter. Default value is "default", which is defined when the DSS starts.

        DSS property name: `Spectrum`, DSS property index: 22.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 22)

    @Spectrum_obj.setter
    def Spectrum_obj(self, value: SpectrumObj):
        self._set_batch_string(22, value)

    @property
    def BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 23.
        """
        return BatchFloat64ArrayProxy(self, 23)

    @BaseFreq.setter
    def BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(23, value)

    @property
    def Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 24.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 24)
        ]
    @Enabled.setter
    def Enabled(self, value: bool):
        self._set_batch_int32_array(24, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 25.
        """
        self._set_batch_string(25, value)

class IndMach012BatchProperties(TypedDict):
    Phases: Union[int, Int32Array]
    Bus1: Union[AnyStr, List[AnyStr]]
    kV: Union[float, Float64Array]
    kW: Union[float, Float64Array]
    PF: Union[float, Float64Array]
    Conn: Union[AnyStr, int, enums.Connection, List[AnyStr], List[int], List[enums.Connection], Int32Array]
    kVA: Union[float, Float64Array]
    H: Union[float, Float64Array]
    D: Union[float, Float64Array]
    puRs: Union[float, Float64Array]
    puXs: Union[float, Float64Array]
    puRr: Union[float, Float64Array]
    puXr: Union[float, Float64Array]
    puXm: Union[float, Float64Array]
    Slip: Union[float, Float64Array]
    MaxSlip: Union[float, Float64Array]
    SlipOption: Union[AnyStr, int, enums.IndMach012SlipOption, List[AnyStr], List[int], List[enums.IndMach012SlipOption], Int32Array]
    Yearly: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    Daily: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    Duty: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    DebugTrace: bool
    Spectrum: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IIndMach012(IDSSObj):
    __slots__ = ()

    def __init__(self, iobj):
        super().__init__(iobj, IndMach012, IndMach012Batch)

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> IndMach012:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[IndMach012Properties]) -> IndMach012:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[IndMach012BatchProperties]) -> IndMach012Batch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
