import re
from .. import (
    # _dss_CapUserControl, 
    _dss_GenUserModel, 
    # _dss_PVSystemUserModel, 
    # _dss_StoreDynaModel, 
    # _dss_StoreUserModel
)
from . import bases

class CommonWrapper(object):
    Base = None
    
    def __init__(self):
        self.active_instance = None
        self.dll_path = self.cffi_module.__file__
        self.ffi = self.cffi_module.ffi
        self.lib = self.cffi_module.lib
        self.models = []
        self.model_classes = {}

        prefix = self.function_prefix
        for fname in self.function_names:
            self.ffi.def_extern(name='{}_{}'.format(prefix, fname))(getattr(self, fname))

        if self.Base is not None:
            self.Base.ffi = self.ffi
            
        
    def register(self, cls):
        self.model_classes[cls.__name__.lower()] = cls
        return cls
        
    def Delete(self, ID):
        ID = ID[0]
        if ID >= 1 and ID <= len(self.models):
            if self.models[ID - 1] == self.active_instance:
                self.active_instance = None
                
            del self.models[ID - 1]

    def Select(self, ID):
        ID = ID[0]
        if ID > 0 and ID <= len(self.models):
            self.active_instance = self.models[ID - 1]
            return ID
            
        return -1

    def Edit(self, edit_str, max_len):
        active_instance = self.active_instance
        models = self.models
        
        if not active_instance:
            return

        edit_str0 = self.ffi.string(edit_str)
        edit_str = edit_str0.decode('ascii')
        pymodel_res = re.search('pymodel=([a-zA-Z0-9]+) ', edit_str)
        
        if pymodel_res:
            # replace current instance
            pymodel = pymodel_res.group(1)
            old_instance = active_instance
            self.cls = self.model_classes[pymodel.lower()]
            active_instance = self.cls(old_instance.gen, old_instance.dyn, old_instance.callbacks)
            models[models.index(old_instance)] = active_instance
        
        active_instance.edit(edit_str0, max_len)

    def UpdateModel(self):
        if not self.active_instance:
            return
            
        self.active_instance.update()

        
class DynamicsWrapper(CommonWrapper):
    def Init(self, V, I):
        if not self.active_instance:
            return
        
        #TODO: convert V/I to numpy with buffer interface?
        num = self.active_instance.gen.NumConductors
        cV = [complex(V[2*i], V[2*i + 1]) for i in range(num)]
        cI = [complex(I[2*i], I[2*i + 1]) for i in range(num)]
        
        self.active_instance.init_state_vars(cV, cI)

        for i in range(num):
            V[2*i], V[2*i + 1] = cV[i].real, cV[i].imag
            I[2*i], I[2*i + 1] = cI[i].real, cI[i].imag
        

    def Calc(self, V, I):
        if not self.active_instance:
            return
            
        #TODO: convert V/I to numpy with buffer interface??
        num = self.active_instance.gen.NumConductors
        cV = [complex(V[2*i], V[2*i + 1]) for i in range(num)]
        cI = [complex(I[2*i], I[2*i + 1]) for i in range(num)]
        
        self.active_instance.calc(cV, cI)
        
        for i in range(num):
            V[2*i], V[2*i + 1] = cV[i].real, cV[i].imag
            I[2*i], I[2*i + 1] = cI[i].real, cI[i].imag
        
    def Integrate(self):
        if not self.active_instance:
            return
            
        self.active_instance.integrate()
    
    def NumVars(self):
        if not self.active_instance:
            return 0
            
        return self.active_instance.get_num_outputs()
    
    
    def GetAllVars(self, vars):
        if not self.active_instance:
            return
            
        self.active_instance.get_all_outputs(vars)

    
    def GetVariable(self, i):
        if not self.active_instance:
            return 0.0
            
        return self.active_instance.get_output(i[0])
    
    
    def SetVariable(self, i, value):
        if not self.active_instance:
            return
            
        self.active_instance.set_input_param(i[0], value)
    

    def GetVarName(self, i, var_name, max_len):
        if not self.active_instance:
            return
            
        tmp = self.active_instance.get_output_name(i[0]).encode('ascii')[:max_len]
        max_len = min(max_len, len(tmp))
        var_name[0:max_len] = tmp[0:max_len]
        var_name[max_len] = b'\0'

        
class SaveRestoreMixin(object):
    def Save(self):
        if not self.active_instance:
            return
            
        self.active_instance.save()

    def Restore(self):
        if not self.active_instance:
            return
            
        self.active_instance.restore()


# class CapUserControlWrapper(CommonWrapper):
#     Base = bases.CapUserControlBase
#     cffi_module = _dss_CapUserControl
#     function_prefix = 'pyCapUserControl'
#     function_names = (
#         'New',
#         'Delete',
#         'Select',
#         'Edit',
#         'UpdateModel'
#     )

#     def Sample(self):
#         if not self.active_instance:
#             return
   
#     def New(self, CallBacks):
#         # Create a base instance to be replaced in Edit
#         self.active_instance = self.Base(CallBacks)
#         self.models.append(self.active_instance)
#         return len(self.models)


class GenUserModelWrapper(DynamicsWrapper, SaveRestoreMixin):
    Base = bases.GenUserModelBase
    cffi_module = _dss_GenUserModel
    function_prefix = 'pyGenUserModel'
    function_names = (
        'New',
        'Delete',
        'Select',
        'Init',
        'Calc',
        'Integrate',
        'Edit',
        'UpdateModel',
        'NumVars',
        'GetAllVars',
        'GetVariable',
        'SetVariable',
        'GetVarName',
        'Save',
        'Restore'
    )

    def New(self, GenData, DynaData, CallBacks):
        # Create a base instance to be replaced in Edit
        self.active_instance = self.Base(GenData, DynaData, CallBacks)
        self.models.append(self.active_instance)
        return len(self.models)

        
# class PVSystemUserModelWrapper(DynamicsWrapper, SaveRestoreMixin):
#     Base = bases.PVSystemUserModelBase
#     cffi_module = _dss_PVSystemUserModel
#     function_prefix = 'pyPVSystemUserModel'
#     function_names = (
#         'New',
#         'Delete',
#         'Select',
#         'Init',
#         'Calc',
#         'Integrate',
#         'Edit',
#         'UpdateModel',
#         'NumVars',
#         'GetAllVars',
#         'GetVariable',
#         'SetVariable',
#         'GetVarName',
#         'Save',
#         'Restore'
#     )

#     def New(self, GenData, DynaData, CallBacks):
#         # Create a base instance to be replaced in Edit
#         self.active_instance = self.Base(GenData, DynaData, CallBacks)
#         self.models.append(self.active_instance)
#         return len(self.models)


# class StoreUserModelWrapper(DynamicsWrapper, SaveRestoreMixin):
#     Base = bases.StoreUserModelBase
#     cffi_module = _dss_StoreUserModel
#     function_prefix = 'pyStoreUserModel'
#     function_names = (
#         'New',
#         'Delete',
#         'Select',
#         'Init',
#         'Calc',
#         'Integrate',
#         'Edit',
#         'UpdateModel',
#         'NumVars',
#         'GetAllVars',
#         'GetVariable',
#         'SetVariable',
#         'GetVarName',
#         'Save',
#         'Restore'
#     )

#     def New(self, DynaData, CallBacks):
#         # Create a base instance to be replaced in Edit
#         self.active_instance = self.Base(DynaData, CallBacks)
#         self.models.append(self.active_instance)
#         return len(self.models)


# class StoreDynaModelWrapper(DynamicsWrapper):
#     Base = bases.StoreDynaModelBase
#     cffi_module = _dss_StoreDynaModel
#     function_prefix = 'pyStoreDynaModel'
#     function_names = (
#         'New',
#         'Delete',
#         'Select',
#         'Init',
#         'Calc',
#         'Integrate',
#         'Edit',
#         'UpdateModel',
#         'NumVars',
#         'GetAllVars',
#         'GetVariable',
#         'SetVariable',
#         'GetVarName',
#     )

#     def New(self, DynaData, CallBacks):
#         # Create a base instance to be replaced in Edit
#         self.active_instance = self.Base(DynaData, CallBacks)
#         self.models.append(self.active_instance)
#         return len(self.models)


# Instantiate the wrappers to link the DLLs to the the Python code
# CapUserControl = CapUserControlWrapper()
GenUserModel = GenUserModelWrapper()
# PVSystemUserModel = PVSystemUserModelWrapper()
# StoreDynaModel = StoreDynaModelWrapper()
# StoreUserModel = StoreUserModelWrapper()

#__all__ = ['CapUserControl', 'GenUserModel', 'PVSystemUserModel', 'StoreDynaModel', 'StoreUserModel']
__all__ = ['GenUserModel']
