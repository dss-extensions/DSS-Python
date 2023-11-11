from dss._cffi_api_util import DSSException, Base, CffiApiUtil

try:
    import pandas as pd
    LIST_LIKE = (pd.Series, list, tuple)
except ModuleNotFoundError:
    LIST_LIKE = (list, tuple)

class InvalidatedDSSObject:
    '''
    If you see this class somewhere, such as a traceback, it means that the related 
    (parent) object was invalidated by an operation in the DSS engine. This could
    be a "clear" command, or destruction of the DSSContext where the objects lived.
    '''
    pass

InvalidatedObject = InvalidatedDSSObject()

class InvalidatedDSSBus:
    '''
    If you see this class somewhere, such as a traceback, it means that the related
    (parent) bus was invalidated by an operation in the DSS engine. This could be
    a "clear" command, destruction of the DSSContext where the buses lived, or a 
    redefinition of the circuit buses.
    '''
    pass

InvalidatedBus = InvalidatedDSSBus()

class Edit:
    '''
    Edit is a helper class that makes block-editing DSS properties
    easier. It supports instances for the new Obj and Batch APIs.
    '''

    def __init__(self, obj_or_batch, num_changes=1, needs_begin=True):
        '''
        `num_changes` is required for a few classes to correctly match the official OpenDSS behavior
        and must be the number of properties modified in the current editing block. As of DSS C-API
        v0.13, this is only required for the Monitor class, when the `Action` property is used with 
        the `Process` value.
        '''
        self.needs_begin = needs_begin
        self.obj_or_batch = obj_or_batch
        self.num_changes = num_changes

    def __enter__(self):
        if self.needs_begin:
            self.obj_or_batch.begin_edit()

        return self.obj_or_batch

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.obj_or_batch.end_edit(self.num_changes)


__all__ = ('DSSException', 'Base', 'CffiApiUtil', 'LIST_LIKE', 'Edit')