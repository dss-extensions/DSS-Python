# A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.
# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from ._cffi_api_util import Iterable
from ._types import Float64Array
from typing import AnyStr, Union
from .enums import LoadStatus, LoadModels

class ILoads(Iterable):
    __slots__ = []
    _is_circuit_element = True

    _columns = [
        'Name',
        'idx',
        'Phases',
        'Class',
        'Model',
        'NumCust',
        'IsDelta',
        'Rneut',
        'Xneut',
        'PF',
        'ZIPV',
        'CVRcurve',
        'CVRvars',
        'CVRwatts',
        'Cfactor',
        'Growth',
        'daily',
        'duty',
        'Yearly',
        'PctMean',
        'PctStdDev',
        'RelWeight',
        'Spectrum',
        'Status',
        'Vminnorm',
        'Vminemerg',
        'Vminpu',
        'Vmaxpu',
        'kV',
        'kW',
        'kva',
        'kvar',
        'kwh',
        'kwhdays',
        'AllocationFactor',
        'xfkVA',
        'pctSeriesRL',
        'Sensor',
    ]

    @property
    def AllocationFactor(self) -> float:
        '''
        Factor for allocating loads by connected xfkva

        Original COM help: https://opendss.epri.com/AllocationFactor.html
        '''
        return self._check_for_error(self._lib.Loads_Get_AllocationFactor())

    @AllocationFactor.setter
    def AllocationFactor(self, Value: float):
        self._check_for_error(self._lib.Loads_Set_AllocationFactor(Value))

    @property
    def CVRcurve(self) -> str:
        '''
        Name of a loadshape with both Mult and Qmult, for CVR factors as a function of time.

        Original COM help: https://opendss.epri.com/CVRcurve.html
        '''
        return self._get_string(self._check_for_error(self._lib.Loads_Get_CVRcurve()))

    @CVRcurve.setter
    def CVRcurve(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Loads_Set_CVRcurve(Value))

    @property
    def CVRvars(self) -> float:
        '''
        Percent reduction in Q for percent reduction in V. Must be used with dssLoadModelCVR.

        Original COM help: https://opendss.epri.com/CVRvars.html
        '''
        return self._check_for_error(self._lib.Loads_Get_CVRvars())

    @CVRvars.setter
    def CVRvars(self, Value: float):
        self._check_for_error(self._lib.Loads_Set_CVRvars(Value))

    @property
    def CVRwatts(self) -> float:
        '''
        Percent reduction in P for percent reduction in V. Must be used with dssLoadModelCVR.

        Original COM help: https://opendss.epri.com/CVRwatts.html
        '''
        return self._check_for_error(self._lib.Loads_Get_CVRwatts())

    @CVRwatts.setter
    def CVRwatts(self, Value: float):
        self._check_for_error(self._lib.Loads_Set_CVRwatts(Value))

    @property
    def Cfactor(self) -> float:
        '''
        Factor relates average to peak kw.  Used for allocation with kwh and kwhdays

        Original COM help: https://opendss.epri.com/Cfactor.html
        '''
        return self._check_for_error(self._lib.Loads_Get_Cfactor())

    @Cfactor.setter
    def Cfactor(self, Value: float):
        self._check_for_error(self._lib.Loads_Set_Cfactor(Value))

    @property
    def Class(self) -> int:
        '''
        Code number used to separate loads by class or group. No effect on the solution.
        
        Original COM help: https://opendss.epri.com/Class.html
        '''
        return self._check_for_error(self._lib.Loads_Get_Class_())

    @Class.setter
    def Class(self, Value: int):
        self._check_for_error(self._lib.Loads_Set_Class_(Value))

    @property
    def Growth(self) -> str:
        '''
        Name of the growthshape curve for yearly load growth factors.

        Original COM help: https://opendss.epri.com/Growth.html
        '''
        return self._get_string(self._check_for_error(self._lib.Loads_Get_Growth()))

    @Growth.setter
    def Growth(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Loads_Set_Growth(Value))

    @property
    def IsDelta(self) -> bool:
        '''
        Delta loads are connected line-to-line.

        Original COM help: https://opendss.epri.com/IsDelta1.html
        '''
        return self._check_for_error(self._lib.Loads_Get_IsDelta()) != 0

    @IsDelta.setter
    def IsDelta(self, Value: bool):
        self._check_for_error(self._lib.Loads_Set_IsDelta(Value))

    @property
    def Model(self) -> LoadModels:
        '''
        The Load Model defines variation of P and Q with voltage.

        Original COM help: https://opendss.epri.com/Model1.html
        '''
        return self._check_for_error(self._lib.Loads_Get_Model())

    @Model.setter
    def Model(self, Value: Union[int, LoadModels]):
        self._check_for_error(self._lib.Loads_Set_Model(Value))

    @property
    def NumCust(self) -> int:
        '''
        Number of customers in this load, defaults to one.

        Original COM help: https://opendss.epri.com/NumCust1.html
        '''
        return self._check_for_error(self._lib.Loads_Get_NumCust())

    @NumCust.setter
    def NumCust(self, Value: int):
        self._check_for_error(self._lib.Loads_Set_NumCust(Value))

    @property
    def PF(self) -> float:
        '''
        Get or set Power Factor for Active Load. Specify leading PF as negative. Updates kvar based on present value of kW

        Original COM help: https://opendss.epri.com/PF1.html
        '''
        return self._check_for_error(self._lib.Loads_Get_PF())

    @PF.setter
    def PF(self, Value: float):
        self._check_for_error(self._lib.Loads_Set_PF(Value))

    @property
    def PctMean(self) -> float:
        '''
        Average percent of nominal load in Monte Carlo studies; only if no loadshape defined for this load.

        Original COM help: https://opendss.epri.com/PctMean.html
        '''
        return self._check_for_error(self._lib.Loads_Get_PctMean())

    @PctMean.setter
    def PctMean(self, Value: float):
        self._check_for_error(self._lib.Loads_Set_PctMean(Value))

    @property
    def PctStdDev(self) -> float:
        '''
        Percent standard deviation for Monte Carlo load studies; if there is no loadshape assigned to this load.

        Original COM help: https://opendss.epri.com/PctStdDev.html
        '''
        return self._check_for_error(self._lib.Loads_Get_PctStdDev())

    @PctStdDev.setter
    def PctStdDev(self, Value: float):
        self._check_for_error(self._lib.Loads_Set_PctStdDev(Value))

    @property
    def RelWeight(self) -> float:
        '''
        Relative Weighting factor for the active LOAD

        Original COM help: https://opendss.epri.com/RelWeight.html
        '''
        return self._check_for_error(self._lib.Loads_Get_RelWeight())

    @RelWeight.setter
    def RelWeight(self, Value: float):
        self._check_for_error(self._lib.Loads_Set_RelWeight(Value))

    @property
    def Rneut(self) -> float:
        '''
        Neutral resistance for wye-connected loads.

        Original COM help: https://opendss.epri.com/Rneut.html
        '''
        return self._check_for_error(self._lib.Loads_Get_Rneut())

    @Rneut.setter
    def Rneut(self, Value: float):
        self._check_for_error(self._lib.Loads_Set_Rneut(Value))

    @property
    def Spectrum(self) -> str:
        '''
        Name of harmonic current spectrum shape.

        Original COM help: https://opendss.epri.com/Spectrum.html
        '''
        return self._get_string(self._check_for_error(self._lib.Loads_Get_Spectrum()))

    @Spectrum.setter
    def Spectrum(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Loads_Set_Spectrum(Value))

    @property
    def Status(self) -> LoadStatus:
        '''
        Response to load multipliers: Fixed (growth only), Exempt (no LD curve), Variable (all).

        Original COM help: https://opendss.epri.com/Status.html
        '''
        return LoadStatus(self._check_for_error(self._lib.Loads_Get_Status()))

    @Status.setter
    def Status(self, Value: Union[int, LoadStatus]):
        self._check_for_error(self._lib.Loads_Set_Status(Value))

    @property
    def Vmaxpu(self) -> float:
        '''
        Maximum per-unit voltage to use the load model. Above this, constant Z applies.

        Original COM help: https://opendss.epri.com/Vmaxpu1.html
        '''
        return self._check_for_error(self._lib.Loads_Get_Vmaxpu())

    @Vmaxpu.setter
    def Vmaxpu(self, Value: float):
        self._check_for_error(self._lib.Loads_Set_Vmaxpu(Value))

    @property
    def Vminemerg(self) -> float:
        '''
        Minimum voltage for unserved energy (UE) evaluation.

        Original COM help: https://opendss.epri.com/Vminemerg.html
        '''
        return self._check_for_error(self._lib.Loads_Get_Vminemerg())

    @Vminemerg.setter
    def Vminemerg(self, Value: float):
        self._check_for_error(self._lib.Loads_Set_Vminemerg(Value))

    @property
    def Vminnorm(self) -> float:
        '''
        Minimum voltage for energy exceeding normal (EEN) evaluations.

        Original COM help: https://opendss.epri.com/Vminnorm.html
        '''
        return self._check_for_error(self._lib.Loads_Get_Vminnorm())

    @Vminnorm.setter
    def Vminnorm(self, Value: float):
        self._check_for_error(self._lib.Loads_Set_Vminnorm(Value))

    @property
    def Vminpu(self) -> float:
        '''
        Minimum voltage to apply the load model. Below this, constant Z is used.

        Original COM help: https://opendss.epri.com/Vminpu1.html
        '''
        return self._check_for_error(self._lib.Loads_Get_Vminpu())

    @Vminpu.setter
    def Vminpu(self, Value: float):
        self._check_for_error(self._lib.Loads_Set_Vminpu(Value))

    @property
    def Xneut(self) -> float:
        '''
        Neutral reactance for wye-connected loads.

        Original COM help: https://opendss.epri.com/Xneut.html
        '''
        return self._check_for_error(self._lib.Loads_Get_Xneut())

    @Xneut.setter
    def Xneut(self, Value: float):
        self._check_for_error(self._lib.Loads_Set_Xneut(Value))

    @property
    def Yearly(self) -> str:
        '''
        Name of yearly duration loadshape
        
        Original COM help: https://opendss.epri.com/Yearly.html
        '''
        return self._get_string(self._check_for_error(self._lib.Loads_Get_Yearly()))

    @Yearly.setter
    def Yearly(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Loads_Set_Yearly(Value))

    @property
    def ZIPV(self) -> Float64Array:
        '''
        Array of 7 doubles with values for ZIPV property of the load object
        
        Original COM help: https://opendss.epri.com/ZIPV.html
        '''
        self._check_for_error(self._lib.Loads_Get_ZIPV_GR())
        return self._get_float64_gr_array()

    @ZIPV.setter
    def ZIPV(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.Loads_Set_ZIPV(ValuePtr, ValueCount))

    @property
    def daily(self) -> str:
        '''
        Name of the loadshape for a daily load profile.
        
        Original COM help: https://opendss.epri.com/daily.html
        '''
        return self._get_string(self._check_for_error(self._lib.Loads_Get_daily()))

    @daily.setter
    def daily(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Loads_Set_daily(Value))

    @property
    def duty(self) -> str:
        '''
        Name of the loadshape for a duty cycle simulation.
        
        Original COM help: https://opendss.epri.com/duty.html
        '''
        return self._get_string(self._check_for_error(self._lib.Loads_Get_duty()))

    @duty.setter
    def duty(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Loads_Set_duty(Value))

    @property
    def kV(self) -> float:
        '''
        kV rating for active Load. For 2 or more phases set Line-Line kV. Else actual kV across terminals.

        Original COM help: https://opendss.epri.com/kV2.html
        '''
        return self._check_for_error(self._lib.Loads_Get_kV())

    @kV.setter
    def kV(self, Value: float):
        self._check_for_error(self._lib.Loads_Set_kV(Value))

    @property
    def kW(self) -> float:
        '''
        Set kW for active Load. Updates kvar based on present PF.

        Original COM help: https://opendss.epri.com/kW1.html
        '''
        return self._check_for_error(self._lib.Loads_Get_kW())

    @kW.setter
    def kW(self, Value: float):
        self._check_for_error(self._lib.Loads_Set_kW(Value))

    @property
    def kva(self) -> float:
        '''
        Base load kva. Also defined kw and kvar or pf input, or load allocation by kwh or xfkva.
        
        Original COM help: https://opendss.epri.com/kva.html
        '''
        return self._check_for_error(self._lib.Loads_Get_kva())

    @kva.setter
    def kva(self, Value: float):
        self._check_for_error(self._lib.Loads_Set_kva(Value))

    @property
    def kvar(self) -> float:
        '''Reactive power in kvar for active Load. If set, updates PF based on present kW.
        
        Original COM help: https://opendss.epri.com/kvar1.html
        '''
        return self._check_for_error(self._lib.Loads_Get_kvar())

    @kvar.setter
    def kvar(self, Value: float):
        self._check_for_error(self._lib.Loads_Set_kvar(Value))

    @property
    def kwh(self) -> float:
        '''
        kWh billed for this period. Can be used with Cfactor for load allocation.

        Original COM help: https://opendss.epri.com/kwh.html
        '''
        return self._check_for_error(self._lib.Loads_Get_kwh())

    @kwh.setter
    def kwh(self, Value: float):
        self._check_for_error(self._lib.Loads_Set_kwh(Value))

    @property
    def kwhdays(self) -> float:
        '''
        Length of kWh billing period for average demand calculation. Default 30.

        Original COM help: https://opendss.epri.com/kwhdays.html
        '''
        return self._check_for_error(self._lib.Loads_Get_kwhdays())

    @kwhdays.setter
    def kwhdays(self, Value: float):
        self._check_for_error(self._lib.Loads_Set_kwhdays(Value))

    @property
    def pctSeriesRL(self) -> float:
        '''
        Percent of Load that is modeled as series R-L for harmonics studies

        Original COM help: https://opendss.epri.com/pctSeriesRL.html
        '''
        return self._check_for_error(self._lib.Loads_Get_pctSeriesRL())

    @pctSeriesRL.setter
    def pctSeriesRL(self, Value: float):
        self._check_for_error(self._lib.Loads_Set_pctSeriesRL(Value))

    @property
    def xfkVA(self) -> float:
        '''
        Rated service transformer kVA for load allocation, using AllocationFactor. Affects kW, kvar, and pf.

        Original COM help: https://opendss.epri.com/xfkVA.html
        '''
        return self._check_for_error(self._lib.Loads_Get_xfkVA())

    @xfkVA.setter
    def xfkVA(self, Value: float):
        self._check_for_error(self._lib.Loads_Set_xfkVA(Value))

    @property
    def Sensor(self) -> str:
        '''
        Name of the sensor monitoring this load.

        Original COM help: https://opendss.epri.com/Sensor.html
        '''
        return self._get_string(self._check_for_error(self._lib.Loads_Get_Sensor()))

    # API extensions
    @property
    def Phases(self) -> int:
        '''
        Number of phases
        
        **(API Extension)**
        '''
        return self._check_for_error(self._lib.Loads_Get_Phases())

    @Phases.setter
    def Phases(self, Value: int):
        self._check_for_error(self._lib.Loads_Set_Phases(Value))
