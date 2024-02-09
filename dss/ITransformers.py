# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Iterable
from ._types import Float64ArrayOrComplexArray
from typing import AnyStr, Union
from .enums import CoreType as TransformerCoreType

class ITransformers(Iterable):
    __slots__ = []
    _is_circuit_element = True

    _columns = [
        'Name',
        'idx',
        'XfmrCode',
        'IsDelta',
        'CoreType',
        'NumWindings',
        'Wdg',
        'NumTaps',
        'MinTap',
        'MaxTap',
        'Tap',
        'kV',
        'kVA',
        'R',
        'Xhl',
        'Xht',
        'Xlt',
        'Rneut',
        'Xneut',
        'RdcOhms',
        'WdgCurrents',
        'WdgVoltages',
        'LossesByType',
    ]

    @property
    def IsDelta(self) -> bool:
        '''
        Active Winding delta or wye connection?

        Original COM help: https://opendss.epri.com/IsDelta3.html
        '''
        return self._check_for_error(self._lib.Transformers_Get_IsDelta()) != 0

    @IsDelta.setter
    def IsDelta(self, Value: bool):
        self._check_for_error(self._lib.Transformers_Set_IsDelta(Value))

    @property
    def MaxTap(self) -> float:
        '''
        Active Winding maximum tap in per-unit.

        Original COM help: https://opendss.epri.com/MaxTap.html
        '''
        return self._check_for_error(self._lib.Transformers_Get_MaxTap())

    @MaxTap.setter
    def MaxTap(self, Value: float):
        self._check_for_error(self._lib.Transformers_Set_MaxTap(Value))

    @property
    def MinTap(self) -> float:
        '''
        Active Winding minimum tap in per-unit.

        Original COM help: https://opendss.epri.com/MinTap.html
        '''
        return self._check_for_error(self._lib.Transformers_Get_MinTap())

    @MinTap.setter
    def MinTap(self, Value: float):
        self._check_for_error(self._lib.Transformers_Set_MinTap(Value))

    @property
    def NumTaps(self) -> int:
        '''
        Active Winding number of tap steps between MinTap and MaxTap.

        Original COM help: https://opendss.epri.com/NumTaps.html
        '''
        return self._check_for_error(self._lib.Transformers_Get_NumTaps())

    @NumTaps.setter
    def NumTaps(self, Value: int):
        self._check_for_error(self._lib.Transformers_Set_NumTaps(Value))

    @property
    def NumWindings(self) -> int:
        '''
        Number of windings on this transformer. Allocates memory; set or change this property first.

        Original COM help: https://opendss.epri.com/NumWindings.html
        '''
        return self._check_for_error(self._lib.Transformers_Get_NumWindings())

    @NumWindings.setter
    def NumWindings(self, Value: int):
        self._check_for_error(self._lib.Transformers_Set_NumWindings(Value))

    @property
    def R(self) -> float:
        '''
        Active Winding resistance in %

        Original COM help: https://opendss.epri.com/R.html
        '''
        return self._check_for_error(self._lib.Transformers_Get_R())

    @R.setter
    def R(self, Value: float):
        self._check_for_error(self._lib.Transformers_Set_R(Value))

    @property
    def Rneut(self) -> float:
        '''
        Active Winding neutral resistance [ohms] for wye connections. Set less than zero for ungrounded wye.

        Original COM help: https://opendss.epri.com/Rneut1.html
        '''
        return self._check_for_error(self._lib.Transformers_Get_Rneut())

    @Rneut.setter
    def Rneut(self, Value: float):
        self._check_for_error(self._lib.Transformers_Set_Rneut(Value))

    @property
    def Tap(self) -> float:
        '''
        Active Winding tap in per-unit.

        Original COM help: https://opendss.epri.com/Tap.html
        '''
        return self._check_for_error(self._lib.Transformers_Get_Tap())

    @Tap.setter
    def Tap(self, Value: float):
        self._check_for_error(self._lib.Transformers_Set_Tap(Value))

    @property
    def Wdg(self) -> int:
        '''
        Active Winding Number from 1..NumWindings. Update this before reading or setting a sequence of winding properties (R, Tap, kV, kVA, etc.)

        Original COM help: https://opendss.epri.com/Wdg.html
        '''
        return self._check_for_error(self._lib.Transformers_Get_Wdg())

    @Wdg.setter
    def Wdg(self, Value: int):
        self._check_for_error(self._lib.Transformers_Set_Wdg(Value))

    @property
    def XfmrCode(self) -> str:
        '''
        Name of an XfrmCode that supplies electrical parameters for this Transformer.

        Original COM help: https://opendss.epri.com/XfmrCode1.html
        '''
        return self._get_string(self._check_for_error(self._lib.Transformers_Get_XfmrCode()))

    @XfmrCode.setter
    def XfmrCode(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Transformers_Set_XfmrCode(Value))

    @property
    def Xhl(self) -> float:
        '''
        Percent reactance between windings 1 and 2, on winding 1 kVA base. Use for 2-winding or 3-winding transformers.

        Original COM help: https://opendss.epri.com/Xhl.html
        '''
        return self._check_for_error(self._lib.Transformers_Get_Xhl())

    @Xhl.setter
    def Xhl(self, Value: float):
        self._check_for_error(self._lib.Transformers_Set_Xhl(Value))

    @property
    def Xht(self) -> float:
        '''
        Percent reactance between windings 1 and 3, on winding 1 kVA base.  Use for 3-winding transformers only.

        Original COM help: https://opendss.epri.com/Xht.html
        '''
        return self._check_for_error(self._lib.Transformers_Get_Xht())

    @Xht.setter
    def Xht(self, Value: float):
        self._check_for_error(self._lib.Transformers_Set_Xht(Value))

    @property
    def Xlt(self) -> float:
        '''
        Percent reactance between windings 2 and 3, on winding 1 kVA base. Use for 3-winding transformers only.

        Original COM help: https://opendss.epri.com/Xlt.html
        '''
        return self._check_for_error(self._lib.Transformers_Get_Xlt())

    @Xlt.setter
    def Xlt(self, Value: float):
        self._check_for_error(self._lib.Transformers_Set_Xlt(Value))

    @property
    def Xneut(self) -> float:
        '''
        Active Winding neutral reactance [ohms] for wye connections.

        Original COM help: https://opendss.epri.com/Xneut1.html
        '''
        return self._check_for_error(self._lib.Transformers_Get_Xneut())

    @Xneut.setter
    def Xneut(self, Value: float):
        self._check_for_error(self._lib.Transformers_Set_Xneut(Value))

    @property
    def kV(self) -> float:
        '''
        Active Winding kV rating.  Phase-phase for 2 or 3 phases, actual winding kV for 1 phase transformer.

        Original COM help: https://opendss.epri.com/kV3.html
        '''
        return self._check_for_error(self._lib.Transformers_Get_kV())

    @kV.setter
    def kV(self, Value: float):
        self._check_for_error(self._lib.Transformers_Set_kV(Value))

    @property
    def kVA(self) -> float:
        '''
        Active Winding kVA rating. On winding 1, this also determines normal and emergency current ratings for all windings.

        Original COM help: https://opendss.epri.com/kva1.html
        '''
        return self._check_for_error(self._lib.Transformers_Get_kVA())

    @kVA.setter
    def kVA(self, Value: float):
        self._check_for_error(self._lib.Transformers_Set_kVA(Value))

    kva = kVA

    @property
    def WdgVoltages(self) -> Float64ArrayOrComplexArray:
        '''
        Complex array of voltages for active winding
        
        **WARNING:** If the transformer has open terminal(s), results may be wrong, i.e. avoid using this
        in those situations. For more information, see https://github.com/dss-extensions/dss-extensions/issues/24

        Original COM help: https://opendss.epri.com/WdgVoltages.html
        '''
        self._check_for_error(self._lib.Transformers_Get_WdgVoltages_GR())
        return self._get_complex128_gr_array()

    @property
    def WdgCurrents(self) -> Float64ArrayOrComplexArray:
        '''
        All Winding currents (ph1, wdg1, wdg2,... ph2, wdg1, wdg2 ...)

        **WARNING:** If the transformer has open terminal(s), results may be wrong, i.e. avoid using this
        in those situations. For more information, see https://github.com/dss-extensions/dss-extensions/issues/24

        Original COM help: https://opendss.epri.com/WdgCurrents.html
        '''
        self._check_for_error(self._lib.Transformers_Get_WdgCurrents_GR())
        return self._get_complex128_gr_array()

    @property
    def strWdgCurrents(self) -> str:
        '''
        All winding currents in CSV string form like the WdgCurrents property

        **WARNING:** If the transformer has open terminal(s), results may be wrong, i.e. avoid using this
        in those situations. For more information, see https://github.com/dss-extensions/dss-extensions/issues/24
        '''
        return self._get_string(self._check_for_error(self._lib.Transformers_Get_strWdgCurrents()))

    @property
    def CoreType(self) -> TransformerCoreType:
        '''
        Transformer Core Type: 0=Shell; 1=1ph; 3-3leg; 4=4-Leg; 5=5-leg; 9=Core-1-phase

        Original COM help: https://opendss.epri.com/CoreType.html
        '''
        return TransformerCoreType(self._check_for_error(self._lib.Transformers_Get_CoreType()))

    @CoreType.setter
    def CoreType(self, Value: Union[int, TransformerCoreType]):
        self._check_for_error(self._lib.Transformers_Set_CoreType(Value))

    @property
    def RdcOhms(self) -> float:
        '''
        dc Resistance of active winding in ohms for GIC analysis

        Original COM help: https://opendss.epri.com/RdcOhms.html
        '''
        return self._check_for_error(self._lib.Transformers_Get_RdcOhms())

    @RdcOhms.setter
    def RdcOhms(self, Value: float):
        self._check_for_error(self._lib.Transformers_Set_RdcOhms(Value))

    @property
    def LossesByType(self) -> Float64ArrayOrComplexArray:
        '''
        Complex array with the losses by type (total losses, load losses, no-load losses), in VA
        
        **(API Extension)**
        '''
        self._check_for_error(self._lib.Transformers_Get_LossesByType_GR())
        return self._get_complex128_gr_array()

    @property
    def AllLossesByType(self) -> Float64ArrayOrComplexArray:
        '''
        Complex array with the losses by type (total losses, load losses, no-load losses), in VA, concatenated for ALL transformers
        
        **(API Extension)**
        '''
        self._check_for_error(self._lib.Transformers_Get_AllLossesByType_GR())
        return self._get_complex128_gr_array()
