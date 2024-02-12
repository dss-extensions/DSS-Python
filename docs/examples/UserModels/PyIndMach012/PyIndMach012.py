'''
A `dss_python` User-Model implementation of the IndMach012 Generator model from OpenDSS.

Based on the following files from the official OpenDSS source code:
- Source/PCElements/IndMach012.pas
- Source/IndMach012a/IndMach012Model.pas

This Python version was written by Paulo Meira. 
Original code by EPRI, licensed under the 3-clause BSD. See OPENDSS_LICENSE.

This sample code doesn't interact with the main OpenDSS interface directly,
it only uses the user-model interface. Thus, it is compatible with the official OpenDSS
distribution as well as DSS-Python. Note that OpenDSS version 7 has a bug on 64-bit 
systems and user-models most likely won't run via COM.

Recent version of OpenDSS 8 also present a bug when handling the editing of 
user-model parameters after the creation of the generator. You can, of course,
edit the data in Python if you desire.

'''
from dss.UserModels import GenUserModel
from dss.enums import SolveModes
import numpy as np

# This is the user-model we'll use as a base
Base = GenUserModel.Base

# Symmetrical component transformation matrices
a = np.exp(1j * 2 * np.pi/3)
aa = np.exp(1j * 4 * np.pi/3)

Ap2s = np.array([
    [1, 1, 1], 
    [1, a, aa],
    [1, aa, a]
]) / 3.0

As2p = np.array([
    [1, 1, 1], 
    [1, aa, a],
    [1, a, aa]
])


@GenUserModel.register # The class needs to be registered
class PyIndMach012(Base):
    '''
    A Python User-Model implementation of the IndMach012 Generator model for OpenDSS 
    '''
    def __init__(self, gen, dyn, callbacks):
        '''
        Initialize the model object instance
        Note: OpenDSS calls `Init` from the UserModel DLL later,
              which calls our `init_state_vars`
        '''
    
        Base.__init__(self, gen, dyn, callbacks)
        
        # You can list the DSS model inputs and default values like this.
        # The UserModel wrapper will create attributes in the instance with
        # the default values and update them later when the UserModel
        # `Edit` function is called.
        self.add_inputs(
            ('H', 0.02),
            ('D', 0.02),
            ('puRs', 0.0053),
            ('puXs', 0.106),
            ('puRr', 0.007),
            ('puXr', 0.12),
            ('puXm', 4.0),
            ('slip', 0.007),
            ('MaxSlip', 0.1),
            ('slipOption', 'variable')
        )
        
        # The outputs can be any variable or Python property, i.e. it can be an 
        # input, state variable, property, etc., as long as it is available in
        # the model class
        self.add_outputs(
            'Slip', # The current slip (`slip` is the DSS input param)
            
            # There don't need to be in the output (they're constant) but are listed 
            # in IndMach012.pas -- most likely to debug
            'puRs',
            'puXs',
            'puRr',
            'puXr',
            'puXm',
            'MaxSlip',
            
            # complex variables like these are exported as their absolute values
            'Is1', 
            'Is2',
            'Ir1',
            'Ir2',
            
            # Some properties to mimic the Pascal version
            'E1_pu',
            'StatorLosses',
            'RotorLosses',
            'ShaftPower_hp',
            'PowerFactor',
            'Efficiency_pct'
        )
        
        # These are the state variables. DSS-Python will automatically
        # setup auxiliary variables such as dE1_dt, dE1_dtn, E1n used in
        # the solution process
        self.add_state_vars(
            'E1', 'E2'
        )
        
        # For some advanced usage, we need some CFFI code.
        # We plan to add a simple wrapper to the callback interface.
        # While writing this, I noticed that there were some changes in 
        # OpenDSS version 8 that introduce an extra ActorID parameter in 
        # many of the callback functions. This means that we cannot write
        # a user-model that is compatible with both versions. 
        # An issue ticket was created to track this at:
        # 
        # self.char_buffer = self.ffi.new('char[1024]')
        # self.callbacks.GetActiveElementName(self.char_buffer, 1024)
        # self.element_name = self.ffi.string(self.char_buffer)#.decode('ascii')
        
        # This one is used for the Power property, left as an example
        # self.double_buffer = self.ffi.new('double[2]')

        # Update other variables that depend on the input parameters
        self.update()


    def init_state_vars(self, Vabc, Iabc):
        '''
        Initialize state variables (dynamics mode), equivalent to
        TIndMach012Obj.InitStateVars
        '''

        V012 = np.dot(Ap2s, Vabc)
        I012 = np.dot(Ap2s, Iabc)
        
        # The following is done in TIndMach012Obj.InitModel:
        # Compute Voltage behind transient reactance and set derivatives to zero
        self.E1 = V012[1] - I012[1] * self.Zsp
        self.dE1dt = 0
        self.E2 = V012[2] - I012[2] * self.Zsp
        self.dE2dt = 0

        # Copy the current state to the previous state
        self.copy_state()
        
        # Initial rotor speed
        self.gen.Speed = -self.S1 * self.gen.w0
        self.gen.dSpeed = 0
        self.gen.Theta = np.angle(self.E1) # overwrite Theta
        self.gen.dTheta = 0


    def integrate(self):
        '''
        Equivalent to TIndMach012Obj.Integrate
        '''
        if self.dyn.IterationFlag == 0: 
            # First iteration of new time step, copy the previous state
            # to be used in the integration process
            self.copy_state()
        
        # Some copies to reduce `self.` spam
        gen = self.gen
        w0 = gen.w0
        S1, S2 = self.S1, self.S2
        E1, E2 = self.E1, self.E2
        Is1, Is2 = self.Is1, self.Is2
        T0p = self.T0p
        Xopen, Xp = self.Xopen, self.Xp
        
        # Derivative of E
        self.dE1_dt = (1j * -w0 * S1 * E1) - ((E1 - 1j * (Xopen - Xp) * Is1) / T0p)
        self.dE2_dt = (1j * -w0 * S2 * E2) - ((E2 - 1j * (Xopen - Xp) * Is2) / T0p)
        
        # Trapezoidal Integration
        Base.integrate(self)
            
        
    def update(self): 
        '''
        Propagate changes from the input parameters to the model.
        
        Equivalent to part of TIndMach012Obj.RecalcElementData
        '''
        
        gen = self.gen
        
        self._set_local_slip(self.slip)
        
        # make generator speed agree
        gen.Speed = -self.S1 * self.gen.w0
        self.gen.dSpeed = 0.0
    
        self.fixed_slip = (self.slipOption) and (self.slipOption[0].upper() == 'F')
        self.first_iteration = True

        ZBase = 1000.0 * (gen.kVGeneratorBase**2 / gen.kVArating)
        
        Rs = self.puRs * ZBase
        Xs = self.puXs * ZBase
        Rr = self.puRr * ZBase
        Xr = self.puXr * ZBase
        Xm = self.puXm * ZBase
        
        self.Zs = complex(Rs, Xs)
        self.Zm = complex(0, Xm)
        self.Zr = complex(Rr, Xr)
        
        self.Xopen = Xs + Xm
        self.Xp  = Xs + (Xr * Xm) / (Xr + Xm)
        self.Zsp = complex(Rs, self.Xp)
        self.T0p = (Xr + Xm) / (gen.w0 * Rr)
        # self.Zrsc = self.Zr + (self.Zs * self.Zm) / (self.Zs + selfg.Zm)
        
        # Init dSdP based on rated slip and rated voltage
        self.V1 = complex(gen.kVGeneratorBase * 1000.0/np.sqrt(3))
        if self.S1 != 0:
            self.Is1, self.Ir1 = self._pfmodel_current(self.V1, self.S1)
        
        self.dSdP = self.S1/(self.V1 * np.conjugate(self.Is1)).real
        
        self.Is1 = complex(0)
        self.V1 = complex(0)
        self.Is2 = complex(0)
        self.V2 = complex(0)


    def calc(self, Vabc, Iabc):
        '''
        Calculate the new model state. Vabc is used as an
        input, while Iabc is the ouput used in OpenDSS.
        '''
        
        # The next version of DSS-Python should have an option to 
        # provide the values in 012 space to simplify the model code
        V012 = np.dot(Ap2s, Vabc)
        I012 = np.dot(Ap2s, Iabc)
        
        if self.dyn.SolutionMode == SolveModes.Dynamic:
            self.calc_dynamic(V012, I012)
        else:
            self.calc_power_flow(V012, I012)

        Iabc[:] = iabc = np.dot(As2p, I012)
        
        # We can get the current total power here, or we can use 
        # the power property below 
        self.Power = sum(np.asarray(Vabc) * iabc.conj())


    # @property
    # def Power(self):
        # '''
        # This is an example of callback usage, returning the power of the 
        # element. Note that we don't really need this here since we can 
        # calculate the power in the calc function.
        # '''
        # cmd = b'select %s' % (self.element_name)
        # self.callbacks.DoDSSCommand(cmd, len(cmd) + 1)
        # self.callbacks.GetActiveElementPower(1, self.double_buffer)
        # return complex(self.double_buffer[0], self.double_buffer[1])


    def calc_dynamic(self, V012, I012):
        '''Equivalent to TIndMach012Obj.CalcDynamic'''
        
        # In dynamics mode, slip is allowed to vary
        
        # Copy some values to local variables
        V1, V2 = self.V1, self.V2 = V012[1], V012[2]
        E1, E2 = self.E1, self.E2
        Zsp, Zm = self.Zsp, self.Zm
        
        # Gets slip from shaft speed
        self._set_local_slip(-self.gen.Speed / self.gen.w0)
        
        # The stator and rotor currents from the Pascal code are 
        # computed in TIndMach012Obj.Get_DynamicModelCurrent

        # Stator current
        self.Is1 = (V1 - E1) / self.Zsp
        self.Is2 = (V2 - E2) / self.Zsp

        # Rotor current
        self.Ir1 = self.Is1 - (V1 - self.Is1 * Zsp) / Zm
        self.Ir2 = self.Is2 - (V2 - self.Is2 * Zsp) / Zm        
        
        I012[:] = complex(0.0, 0.0), self.Is1, self.Is2
        

    def calc_power_flow(self, V012, I012):
        '''Equivalent to TIndMach012Obj.CalcPFlow'''
        
        self.V1, self.V2 = V012[1], V012[2]
        
        if self.first_iteration:
            # Initialize Is1
            self.Is1, self.Ir1 = self._pfmodel_current(self.V1, self.S1)


        # If fixed slip option set, then use the value set by the user
        if not self.fixed_slip:
            P_Error = self.gen.PNominalPerPhase - (self.V1 * self.Is1.conjugate()).real
            
            # make new guess at slip
            self._set_local_slip(self.S1 + self.dSdP * P_Error)

        
        self.Is1, self.Ir1 = self._pfmodel_current(self.V1, self.S1)
        self.Is2, self.Ir2 = self._pfmodel_current(self.V2, self.S2)
        
        I012[:] = complex(0.0, 0.0), self.Is1, self.Is2

        
    def _pfmodel_current(self, V, s, show=False):
        '''Equivalent to TIndMach012Obj.Get_PFlowModelCurrent'''
    
        if s != 0.0:
            RL = self.Zr.real * (1 - s) / s
        else:
            RL = self.Zr.real * 1.0e6
            
        Zrotor = RL + self.Zr
        Zmotor = self.Zs + (Zrotor * self.Zm) / (Zrotor + self.Zm)
        Istator = V / Zmotor
        Irotor = Istator - (V - self.Zs * Istator) / self.Zm
        
        return Istator, Irotor


    def _set_local_slip(self, value):
        '''Equivalent to TIndMach012Obj.set_Localslip'''
        
        self.S1 = value
        if self.dyn.SolutionMode != SolveModes.Dynamic:
            # Put limits on the slip unless dynamics
            if abs(self.S1) > self.MaxSlip:
                self.S1 = np.sign(self.S1) * self.MaxSlip    
            
        self.S2 = 2 - self.S1

    
    # The following are properties to emulate the model outputs from 
    # the Pascal version of built-in IndMach012 
    
    @property
    def E1_pu(self):
        return np.sqrt(3) * abs(self.E1) / (1000 * self.gen.kVGeneratorBase)

    @property
    def Slip(self):
        return self.S1

    @property
    def RotorLosses(self):
        Ir1, Ir2, Zr = self.Ir1, self.Ir2, self.Zr
        return 3 * (Ir1.real**2 + Ir1.imag**2 + Ir2.real**2 + Ir2.imag**2) * Zr.real
        
    @property
    def StatorLosses(self):
        Is1, Is2, Zs = self.Is1, self.Is2, self.Zs
        return 3 * (Is1.real**2 + Is1.imag**2 + Is2.real**2 + Is2.imag**2) * Zs.real
    
    @property
    def PowerFactor(self):
        power = self.Power
        return np.sign(power.imag) * power.real / abs(power)
        
    @property
    def Efficiency_pct(self):
        power = self.Power
        return np.clip((1 - (self.StatorLosses + self.RotorLosses) / power.real) * 100, 0, 100)
        
    @property
    def ShaftPower_hp(self):
        Ir1, Ir2, Zr, S1, S2 = self.Ir1, self.Ir2, self.Zr, self.S1, self.S2
        return (3.0/746) * (abs(Ir1)**2 * (1 - S1) / S1 + abs(Ir2)**2 * (1 - S2)/S2) * Zr.real

