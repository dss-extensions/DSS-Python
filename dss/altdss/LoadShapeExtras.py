
class LoadShapeObjMixin:
    # TODO: integrate Alt_LoadShape_Set_Points
    __slots__ = ()
    _extra_slots = []

    def UseFloat32(self):
        '''
        If this loadshape is using float64/double precision internal data, use this function
        to convert to float32/single precision. If the data is not owned by the loadshape,
        this operation is not allowed.
        '''
        self._lib.Alt_LoadShape_UseFloat32(self._ptr)

    def UseFloat64(self):
        '''
        If this loadshape is using float32/single precision internal data, use this function
        to convert to float64/double precision. If the data is not owned by the loadshape,
        this operation is not allowed.
        '''
        self._lib.Alt_LoadShape_UseFloat64(self._ptr)


class LoadShapeBatchMixin:
    __slots__ = ()

    def UseFloat32(self):
        '''
        If the loadshapes are using float64/double precision internal data, use this function
        to convert to float32/single precision. If the data is not owned by the loadshape,
        this operation is not allowed.
        '''
        for ptr in self._unpack():
            self._lib.Alt_LoadShape_UseFloat32(ptr)

    def UseFloat64(self):
        '''
        If the loadshape are using float32/single precision internal data, use this function
        to convert to float64/double precision. If the data is not owned by the loadshape,
        this operation is not allowed.
        '''
        for ptr in self._unpack():
            self._lib.Alt_LoadShape_UseFloat64(ptr)


__all__ = ('LoadShapeObjMixin', 'LoadShapeBatchMixin',)