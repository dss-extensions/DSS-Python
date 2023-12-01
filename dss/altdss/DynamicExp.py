# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from typing_extensions import TypedDict, Unpack
from .types import Float64Array, Int32Array
from . import enums
from .DSSObj import IDSSObj, DSSObj
from .Batch import DSSBatch
from .ArrayProxy import BatchInt32ArrayProxy
from .common import LIST_LIKE

class DynamicExp(DSSObj):
    __slots__ = DSSObj._extra_slots
    _cls_name = 'DynamicExp'
    _cls_idx = 26
    _cls_prop_idx = {
        'nvariables': 1,
        'varnames': 2,
        'var': 3,
        'varidx': 4,
        'expression': 5,
        'domain': 6,
        'like': 7,
    }


    def _get_NVariables(self) -> int:
        """
        (Int) Number of state variables to be considered in the differential equation.

        DSS property name: `NVariables`, DSS property index: 1.
        """
        return self._lib.Obj_GetInt32(self._ptr, 1)

    def _set_NVariables(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 1, value, flags)

    NVariables = property(_get_NVariables, _set_NVariables) # type: int

    def _get_VarNames(self) -> List[str]:
        """
        ([String]) Array of strings with the names of the state variables.

        DSS property name: `VarNames`, DSS property index: 2.
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 2)

    def _set_VarNames(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 2, value_ptr, value_count, flags)
        self._check_for_error()

    VarNames = property(_get_VarNames, _set_VarNames) # type: List[str]

    def _get_Var(self) -> str:
        """
        (String) Activates the state variable using the given name.

        DSS property name: `Var`, DSS property index: 3.
        """
        return self._get_prop_string(3)

    def _set_Var(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(3, value, flags)

    Var = property(_get_Var, _set_Var) # type: str

    def _get_VarIdx(self) -> int:
        """
        (Int) read-only, returns the index of the active state variable.

        DSS property name: `VarIdx`, DSS property index: 4.
        """
        return self._lib.Obj_GetInt32(self._ptr, 4)

    def _set_VarIdx(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 4, value, flags)

    VarIdx = property(_get_VarIdx, _set_VarIdx) # type: int

    def _get_Expression(self) -> str:
        """
        It is the differential expression using OpenDSS RPN syntax. The expression must be contained within brackets in case of having multiple equations, for example:

        expression="[w dt = 1 M / (P_m D*w - P_e -) *]"

        DSS property name: `Expression`, DSS property index: 5.
        """
        return self._get_prop_string(5)

    def _set_Expression(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(5, value, flags)

    Expression = property(_get_Expression, _set_Expression) # type: str

    def _get_Domain(self) -> enums.DynamicExpDomain:
        """
        It is the domain for which the equation is defined, it can be one of [time*, dq]. By deafult, dynamic epxressions are defined in the time domain.

        DSS property name: `Domain`, DSS property index: 6.
        """
        return enums.DynamicExpDomain(self._lib.Obj_GetInt32(self._ptr, 6))

    def _set_Domain(self, value: Union[AnyStr, int, enums.DynamicExpDomain], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(6, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 6, value, flags)

    Domain = property(_get_Domain, _set_Domain) # type: enums.DynamicExpDomain

    def _get_Domain_str(self) -> str:
        """
        It is the domain for which the equation is defined, it can be one of [time*, dq]. By deafult, dynamic epxressions are defined in the time domain.

        DSS property name: `Domain`, DSS property index: 6.
        """
        return self._get_prop_string(6)

    def _set_Domain_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Domain(value, flags)

    Domain_str = property(_get_Domain_str, _set_Domain_str) # type: str

    def Like(self, value: AnyStr):
        """
        DynamicExp.like

        DSS property name: `Like`, DSS property index: 7.
        """
        self._set_string_o(7, value)


class DynamicExpProperties(TypedDict):
    NVariables: int
    VarNames: List[AnyStr]
    Var: AnyStr
    VarIdx: int
    Expression: AnyStr
    Domain: Union[AnyStr, int, enums.DynamicExpDomain]
    Like: AnyStr

class DynamicExpBatch(DSSBatch):
    _cls_name = 'DynamicExp'
    _obj_cls = DynamicExp
    _cls_idx = 26


    def _get_NVariables(self) -> BatchInt32ArrayProxy:
        """
        (Int) Number of state variables to be considered in the differential equation.

        DSS property name: `NVariables`, DSS property index: 1.
        """
        return BatchInt32ArrayProxy(self, 1)

    def _set_NVariables(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(1, value, flags)

    NVariables = property(_get_NVariables, _set_NVariables) # type: BatchInt32ArrayProxy

    def _get_VarNames(self) -> List[List[str]]:
        """
        ([String]) Array of strings with the names of the state variables.

        DSS property name: `VarNames`, DSS property index: 2.
        """
        return self._get_string_ll(2)

    def _set_VarNames(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._unpack():
            self._lib.Obj_SetStringArray(x, 2, value_ptr, value_count, flags)

        self._check_for_error()

    VarNames = property(_get_VarNames, _set_VarNames) # type: List[List[str]]

    def _get_Var(self) -> List[str]:
        """
        (String) Activates the state variable using the given name.

        DSS property name: `Var`, DSS property index: 3.
        """
        return self._get_batch_str_prop(3)

    def _set_Var(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(3, value, flags)

    Var = property(_get_Var, _set_Var) # type: List[str]

    def _get_VarIdx(self) -> BatchInt32ArrayProxy:
        """
        (Int) read-only, returns the index of the active state variable.

        DSS property name: `VarIdx`, DSS property index: 4.
        """
        return BatchInt32ArrayProxy(self, 4)

    def _set_VarIdx(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(4, value, flags)

    VarIdx = property(_get_VarIdx, _set_VarIdx) # type: BatchInt32ArrayProxy

    def _get_Expression(self) -> List[str]:
        """
        It is the differential expression using OpenDSS RPN syntax. The expression must be contained within brackets in case of having multiple equations, for example:

        expression="[w dt = 1 M / (P_m D*w - P_e -) *]"

        DSS property name: `Expression`, DSS property index: 5.
        """
        return self._get_batch_str_prop(5)

    def _set_Expression(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(5, value, flags)

    Expression = property(_get_Expression, _set_Expression) # type: List[str]

    def _get_Domain(self) -> BatchInt32ArrayProxy:
        """
        It is the domain for which the equation is defined, it can be one of [time*, dq]. By deafult, dynamic epxressions are defined in the time domain.

        DSS property name: `Domain`, DSS property index: 6.
        """
        return BatchInt32ArrayProxy(self, 6)

    def _set_Domain(self, value: Union[AnyStr, int, enums.DynamicExpDomain, List[AnyStr], List[int], List[enums.DynamicExpDomain], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(6, value, flags)
            return

        self._set_batch_int32_array(6, value, flags)

    Domain = property(_get_Domain, _set_Domain) # type: BatchInt32ArrayProxy

    def _get_Domain_str(self) -> List[str]:
        """
        It is the domain for which the equation is defined, it can be one of [time*, dq]. By deafult, dynamic epxressions are defined in the time domain.

        DSS property name: `Domain`, DSS property index: 6.
        """
        return self._get_batch_str_prop(6)

    def _set_Domain_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Domain(value, flags)

    Domain_str = property(_get_Domain_str, _set_Domain_str) # type: List[str]

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        DynamicExp.like

        DSS property name: `Like`, DSS property index: 7.
        """
        self._set_batch_string(7, value, flags)

class DynamicExpBatchProperties(TypedDict):
    NVariables: Union[int, Int32Array]
    VarNames: List[AnyStr]
    Var: Union[AnyStr, List[AnyStr]]
    VarIdx: Union[int, Int32Array]
    Expression: Union[AnyStr, List[AnyStr]]
    Domain: Union[AnyStr, int, enums.DynamicExpDomain, List[AnyStr], List[int], List[enums.DynamicExpDomain], Int32Array]
    Like: AnyStr

class IDynamicExp(IDSSObj, DynamicExpBatch):
    # __slots__ = () #TODO

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, DynamicExp, DynamicExpBatch)
        DynamicExpBatch.__init__(self, self._api_util, sync_cls_idx=DynamicExp._cls_idx)


    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> DynamicExp:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[DynamicExpProperties]) -> DynamicExp:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[DynamicExpBatchProperties]) -> DynamicExpBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
