"""
Vibration Computer Lab
Sajad Saeedi - 2024
Toronto Metropolitan University
"""

import numpy as np
import cmath
import math 
from scipy.integrate import odeint  # pip install scipy
from dataclasses import dataclass, field


@dataclass
class MassSpringDamperClosedForm():
    
    # Vibration system parameters
    m: float                                # mass
    c: float                                # damping coefficient
    k: float                                # spring constant

    x0: float                               # initial position
    v0: float                               # initial velocity

    tf: float                               # simulation duration
    N: int                                  # number of point of simulation

    def calcaulte_canonical_param(self) -> list[float]:
        zeta = self.c/(2*np.sqrt(self.k * self.m))
        wn = np.sqrt(self.k / self.m)
        wd = wn * math.sqrt(1-zeta**2)
        return [zeta, wn, wd]


    def calcualte_ampilitude_phase(self, zeta, wn, wd) -> list[float]:
        amp = np.sqrt((self.v0 + zeta*wn*self.x0)**2 + (self.x0*wd)**2) / wd

        ########################################
        # TODO2: insert the correct formula here
        phi = np.arctan(0)

        return [amp, phi]

    def calculate_x_v_a(self, zeta, wn, wd, amp, phi) -> list[np.ndarray]:
        t = np.linspace(0, self.tf, self.N);
        
        ########################################
        # TODO3: insert the correct formula here
        x = np.zeros(1000)     
        
        ########################################
        # TODO4: insert the correct formula here
        v = np.zeros(1000)
        
        ########################################
        # TODO5: insert the correct formula here
        a = np.zeros(1000)

        
        return [t, x, v, a]

    def calculate_roots(self): 
        delta = cmath.sqrt(self.c**2 - 4*self.k*self.m)

        ########################################
        # TODO1: insert the correct formula here
        root1 = 0
        root2 = 0

        return [root1, root2]



@dataclass
class MassSpringDamperODE:

    # Vibration system parameters
    m: float            # mass
    c: float            # damping coefficient
    k: float            # spring constant

    x0: float           # initial position
    v0: float           # initial velocity

    tf: float           # simulation duration
    N: int              # number of point of simulation  
    _delta_t: float = field(init = False)   # delta t, e.g. 0.01 sec


    def __post_init__(self) -> None:
        self._delta_t = self.tf / self.N

    def solve_motion(self):
        # Part [b]
        x, t = self.solve_EOM(self.tf, self.m, self.c, self.k, self.x0, self.v0, self.N)
        position = x[:,0]
        velocity = x[:,1]
        return t, position, velocity, self.N

    def sdof(self, x, t, m, c, k):
        ########################################
        # TODO6: insert the correct formula here      
        return (x[1], x[0]);
        ########################################

    def solve_EOM(self, tf, m, c, k, x0, v0, N):
        tspan = np.linspace(0, tf, N);
        ########################################
        # TODO7: insert the correct formula here 
        inial_conditions = [0, 0]
        ########################################
        x = odeint(self.sdof, inial_conditions , tspan, args=(m, c, k))
        return x, tspan

    def calculate_KE(self, position, velocity):
        almost_zero_position = [x for x in position if x < 0]
     
        if almost_zero_position:
            time_step = np.where(position == almost_zero_position[0])
            
            closing_velocity = velocity[time_step[0]]
            closing_time = time_step[0] * self._delta_t;

            ########################################
            # TODO8: insert the correct formula here            
            kinetic_energy = 0
            ########################################
            drawer_closed = True;            
        else:
            closing_velocity = [-1]
            closing_time = [-1]
            kinetic_energy = [-1]
            drawer_closed = False;
        return closing_velocity[0], closing_time[0], kinetic_energy[0], drawer_closed
