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
class MassSpringDamperExcitedODE:
    """ODE solvers for linear and nonlineasr EOMs""" 

    # Vibration system parameters
    m: float            # mass
    c: float            # linear damping coefficient F=c dx/dt
    a: float            # air damoing coefficient F = a sgn(dx/dt)(dx/dt)^2
    k: float            # spring constant
    k1: float           # onlinear spring coefficient F=kx+k1x^3 

    x0: float           # initial position
    v0: float           # initial velocity

    F0: list[float]           # harmanics excitation force
    w: list[float]            # harmanics excitation frequency

    tf: float           # simulation duration
    N: int              # number of point of simulation  
    _delta_t: float = field(init = False)   # delta t, e.g. 0.01 sec

    def __post_init__(self) -> None:
        self._delta_t = self.tf / self.N


    def sdof_lin_k_lin_c(self, x, t, m, c, k, F0, w):
        ########################################
        # TODO1: insert the correct formula here      
        zeta = 0
        wn = 0
        F01 = self.F0[0]
        F02 = self.F0[1]
        w1 = self.w[0]
        w2 = self.w[1]
        return (x[1], x[0]);
        ########################################

    def sdof_nlin_k_lin_c(self, x, t, m, c, k, k1, F0, w):
        ########################################
        # TODO4: insert the correct formula here      
        zeta = 0
        wn = 0
        F01 = self.F0[0]
        F02 = self.F0[1]
        w1 = self.w[0]
        w2 = self.w[1]
        return (x[1], x[0]);
        ########################################

    def sdof_nlin_k_nlin_c(self, x, t, m, a, k, k1, F0, w):
        ########################################
        # TODO5: insert the correct formula here      
        zeta = 0
        wn = 0
        F01 = self.F0[0]
        F02 = self.F0[1]
        w1 = self.w[0]
        w2 = self.w[1]
        return (x[1], x[0]);
        ########################################


    def solve_EOM_lin_k_lin_c(self):
        tspan = np.linspace(0, self.tf, self.N);
        inial_conditions = [self.x0, self.v0]
        x = odeint(self.sdof_lin_k_lin_c, inial_conditions , tspan, args=(self.m, self.c, self.k, self.F0, self.w))
        return x, tspan

    def solve_EOM_nlin_k_lin_c(self):
        tspan = np.linspace(0, self.tf, self.N);
        inial_conditions = [self.x0, self.v0]
        x = odeint(self.sdof_nlin_k_lin_c, inial_conditions , tspan, args=(self.m, self.c, self.k, self.k1, self.F0, self.w))
        return x, tspan

    def solve_EOM_nlin_k_nlin_c(self):
        tspan = np.linspace(0, self.tf, self.N);
        inial_conditions = [self.x0, self.v0]
        x = odeint(self.sdof_nlin_k_nlin_c, inial_conditions , tspan, args=(self.m, self.a, self.k, self.k1, self.F0, self.w))
        return x, tspan