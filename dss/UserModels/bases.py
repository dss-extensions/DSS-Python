class CommonBase(object):
    @classmethod
    def extract_names(cls):
        names = []
        names.extend(v[0] for v in getattr(cls, '_inputs', []))
        names.extend(getattr(cls, '_outputs', []))
        st_vars = getattr(cls, '_state_vars', [])
        for v in st_vars:
            names.extend([v, '{}n'.format(name), 'd{}_dt'.format(name), 'd{}n_dt'.format(name)])
        
        for v in getattr(cls, '_var_limits', []):
            assert v['var'] in cls._outputs
            assert v['min'] in names
            assert v['max'] in names
            
        names.extend(v[k] for k in ('min', 'max') for v in getattr(cls, '_var_limits', []))
        
        return names


    def __init__(self, callbacks, populate=None):
        self.callbacks = callbacks
        self.input_vars = []
        self.input_types = []
        self.input_to_index = {}
        self.debug = False
        self.add_input('pymodel', '')
        
        if populate or (populate is None and hasattr(self, '_inputs')):
            self.add_inputs(self._inputs)


    def update(self):
        pass #raise NotImplementedError


    def add_input(self, name, value=0.0):
        setattr(self, name, value)
        self.input_vars.append(name)
        self.input_types.append(type(value))
        name = name.lower()
        param_pointer = len(self.input_vars)

        self.input_to_index[name] = param_pointer
        
        for num in range(1, len(name)):
            partial = name[:num]
            if partial not in self.input_to_index:
                self.input_to_index[partial] = param_pointer
                
                
    def add_inputs(self, *args):
        for arg in args:
            if isinstance(arg, (list, tuple)):
                self.add_input(*arg)
            else:
                self.add_input(arg)
        
        
    def set_input_param(self, i, value):
        return setattr(self, self.input_vars[i - 1], value)

        
    def edit(self, edit_str, max_len):
        self.callbacks.LoadParser(edit_str, max_len)
        
        BUFFER_SIZE = 4095
        param_pointer = 0
        ffi = self.ffi
        param_str = ffi.new('char[%d]'%(BUFFER_SIZE + 1,), b'')
        param_name = ffi.new('char[%d]'%(BUFFER_SIZE + 1,), b'')
        dbl_value = ffi.new('double*')
        num_vars = len(self.input_vars)
        
        changed = False
        
        while self.callbacks.NextParam(param_name, BUFFER_SIZE):
            self.callbacks.GetStrValue(param_str, BUFFER_SIZE)
            
            py_param_name = ffi.string(param_name).decode('ascii').lower()
            py_param_str = ffi.string(param_str).decode('ascii')
            # print(repr(py_param_name), repr(py_param_str))
            
            if len(py_param_name) == 0:
                if py_param_str.lower() == 'help':
                    param_pointer = num_vars + 2
                else:
                    param_pointer += 1 
            
            else:
                # partial strings are already included in the map
                if py_param_name == 'option':
                    param_pointer = num_vars + 1
                else:
                    param_pointer = self.input_to_index[py_param_name]
            
               
            if param_pointer >= 1 and param_pointer <= num_vars:
                if self.input_types[param_pointer - 1] in (float, int):
                    self.callbacks.GetDblValue(dbl_value)
                    self.set_input_param(param_pointer, dbl_value[0])
                # elif self.input_types[param_pointer - 1] in (int, long):
                    # self.callbacks.GetIntValue(int_value)
                    # self.set_input_param(param_pointer, int_value[0])
                else:
                    self.set_input_param(param_pointer, py_param_str)
                    
                changed = True
                
            elif param_pointer == num_vars + 1:
                # debug option
                opt = py_param_str[0].lower()
                if opt == 'd':
                    self.debug = True
                elif opt == 'n':
                    self.debug = False
            
            elif param_pointer == num_vars + 2:
                help_str = u"option={Debug | NoDebug }\n";
                help_str += u"Help: this help message."
                
                tmp = help_str.encode('ascii')[:max_len]
                max_len_ = min(max_len, len(tmp))
                param_str[0:max_len_] = tmp[0:max_len_]
                param_str[max_len_max_len] = b'\0'
                
                self.callBacks.MsgCallBack(param_str, len(help_str) + 1)
        
        if changed:
            self.update()
        


class DynamicsBase(CommonBase):
    def __init__(self, dyn, callbacks, populate=None):
        CommonBase.__init__(self, callbacks, populate=populate)
        
        self.dyn = dyn
        self.output_vars = []
        self.state_vars = []
        self.limits = {}
        
        if populate or (populate is None and hasattr(self, '_inputs')):
            self.add_outputs(self._outputs)
            self.add_state_vars(self._state_vars)
            for lim in self._var_limits:
                self.set_var_limits(lim['var'], lim['min'], lim['max'])

    def init_state_vars(self, V, I):
        raise NotImplementedError

    def calc(self, V, I):
        raise NotImplementedError
        
    def integrate(self):
        h_2 = self.dyn.h * 0.5
        for name in self.state_vars:
            value_n = getattr(self, '{}n'.format(name))
            value_d = getattr(self, 'd{}_dt'.format(name))
            value_dn = getattr(self, 'd{}n_dt'.format(name))
            value = value_n + h_2 * (value_d + value_dn)
            setattr(self, name, value)
            
    def saturate(self):
        for name, (min, max) in self.limits.items():
            value = getattr(self, name)
            vmin = getattr(self, min)
            vmax = getattr(self, max)
            
            if value > vmax:
                setattr(self, name, vmax)
            elif value < vmin:
                setattr(self, name, vmin)

    def add_state_vars(self, *args):
        for arg in args:
            self.add_state_var(arg)

    def add_output(self, name, init_value=0.0):
        if not hasattr(type(self), name) and not hasattr(self, name):
            setattr(self, name, init_value)
            
        self.output_vars.append(name)
        
        
    def add_state_var(self, name, init_value=0.0):
        if not hasattr(type(self), name) and not hasattr(self, name):
            setattr(self, name, init_value)
            
        setattr(self, '{}n'.format(name), getattr(self, name))
        setattr(self, 'd{}_dt'.format(name), 0.0)
        setattr(self, 'd{}n_dt'.format(name), 0.0)
            
        self.state_vars.append(name)
            
    def add_outputs(self, *args):
        for arg in args:
            self.add_output(arg)
        
    
    def set_var_limits(self, name, min=None, max=None):
        self.limits[name] = (min, max)
        
        
    def init_dstate(self):
        for name in self.state_vars:
            setattr(self, 'd{}_dt'.format(name), 0.0)
            setattr(self, 'd{}n_dt'.format(name), 0.0)
        
        
    def copy_state(self):
        for name in self.state_vars:
            setattr(self, '{}n'.format(name), getattr(self, name))
            setattr(self, 'd{}n_dt'.format(name), getattr(self, 'd{}_dt'.format(name)))
        

    def get_all_outputs(self, var_vector):
        for i, v in enumerate(self.output_vars):
            value = getattr(self, v)
            if isinstance(value, complex):
                var_vector[i] = abs(value)
            else:
                var_vector[i] = value
            
    def get_output(self, i):
        value = getattr(self, self.output_vars[i - 1])
        if isinstance(value, complex):
            return abs(value)
        
        return value

        
    def set_input_param(self, i, value):
        return setattr(self, self.input_vars[i - 1], value)

        
    def get_output_name(self, i):
        return self.output_vars[i - 1]


    def get_num_outputs(self):
        return len(self.output_vars)


class SaveRestoreMixin(object):
    def save(self):
        pass

    def restore(self):
        pass
    
        

# class CapUserControlBase(CommonBase):
#     def sample(self):
#         pass

class GenUserModelBase(DynamicsBase, SaveRestoreMixin):
    def __init__(self, gen, dyn, callbacks, populate=None):
        DynamicsBase.__init__(self, dyn, callbacks, populate=populate)
        self.gen = gen

# class PVSystemUserModelBase(DynamicsBase, SaveRestoreMixin):
#     def __init__(self, gen, dyn, callbacks, populate=None):
#         DynamicsBase.__init__(self, dyn, callbacks, populate=populate)
#         self.gen = gen

# class StoreUserModelBase(DynamicsBase, SaveRestoreMixin):
#     def __init__(self, dyn, callbacks, populate=None):
#         DynamicsBase.__init__(self, dyn, callbacks, populate=populate)

# class StoreUserModelBase(DynamicsBase, SaveRestoreMixin):
#     def __init__(self, dyn, callbacks, populate=None):
#         DynamicsBase.__init__(self, dyn, callbacks, populate=populate)

# class StoreDynaModelBase(DynamicsBase):
#     def __init__(self, dyn, callbacks, populate=None):
#         DynamicsBase.__init__(self, dyn, callbacks, populate=populate)

