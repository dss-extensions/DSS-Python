'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira

Copyright (c) 2018-2022 DSS Extensions contributors
'''
from ._cffi_api_util import Base
from .enums import DSSJSONFlags
from typing import AnyStr, List

class IActiveClass(Base):
    __slots__ = []

    _columns = [
        'ActiveClassName',
        'ActiveClassParent',
        'Name',
        'NumElements',
    ]

    @property
    def ActiveClassName(self) -> str:
        '''(read-only) Returns name of active class.'''
        return self._get_string(self.CheckForError(self._lib.ActiveClass_Get_ActiveClassName()))

    @property
    def AllNames(self) -> List[str]:
        '''(read-only) Array of strings consisting of all element names in the active class.'''
        return self.CheckForError(self._get_string_array(self._lib.ActiveClass_Get_AllNames))

    @property
    def Count(self) -> int:
        '''(read-only) Number of elements in Active Class. Same as NumElements Property.'''
        return self.CheckForError(self._lib.ActiveClass_Get_Count())

    def __len__(self) -> int:
        return self.CheckForError(self._lib.ActiveClass_Get_Count())

    def __iter__(self):
        n = self.First
        while n:
            yield self
            n = self.Next

    @property
    def First(self) -> int:
        '''(read-only) Sets first element in the active class to be the active DSS object. If object is a CktElement, ActiveCktELment also points to this element. Returns 0 if none.'''
        return self.CheckForError(self._lib.ActiveClass_Get_First())

    @property
    def Name(self) -> str:
        '''Name of the Active Element of the Active Class'''
        return self._get_string(self.CheckForError(self._lib.ActiveClass_Get_Name()))

    @Name.setter
    def Name(self, Value: AnyStr):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.ActiveClass_Set_Name(Value))

    @property
    def Next(self) -> int:
        '''(read-only) Sets next element in active class to be the active DSS object. If object is a CktElement, ActiveCktElement also points to this element.  Returns 0 if no more.'''
        return self.CheckForError(self._lib.ActiveClass_Get_Next())

    @property
    def NumElements(self) -> int:
        '''(read-only) Number of elements in this class. Same as Count property.'''
        return self.CheckForError(self._lib.ActiveClass_Get_NumElements())

    @property
    def ActiveClassParent(self) -> str:
        '''Get the name of the parent class of the active class'''
        return self._get_string(self.CheckForError(self._lib.ActiveClass_Get_ActiveClassParent()))

    def ToJSON(self, options: DSSJSONFlags = 0) -> str:
        '''
        Returns the data (as a list) of all elements from the active class as a JSON-encoded string.

        The `options` parameter contains bit-flags to toggle specific features.
        See `Obj_ToJSON` (C-API) for more, or `DSSObj.to_json` in Python.
        
        Additionally, the `ExcludeDisabled` flag can be used to excluded disabled elements from the output.

        (API Extension)
        '''
        return self._get_string(self.CheckForError(self._lib.ActiveClass_ToJSON(options)))