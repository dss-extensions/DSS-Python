from ._utils import *

def Description():
    '''(read-only) Description of the property.'''
    return get_string(lib.DSSProperty_Get_Description())

def Name():
    '''(read-only) Name of Property'''
    return get_string(lib.DSSProperty_Get_Name())

def Value(*args):
    if len(args) == 0:
        # General getter 
        return get_string(lib.DSSProperty_Get_Val())
    elif len(args) == 1:
        # Getter by index as str
        lib.DSSProperty_Set_Index(int(args[0]))
        return get_string(lib.DSSProperty_Get_Val())
    
    # Setter by index as strs
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.DSSProperty_Set_Index(int(args[0]))
    lib.DSSProperty_Set_Val(Value)
    return '0'



_columns = ['Description', 'Name', 'Value']
__all__ = ['Description', 'Name', 'Value']

