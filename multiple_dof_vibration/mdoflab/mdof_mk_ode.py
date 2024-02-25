import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt 
from scipy.integrate import odeint  # pip install scipy
from dataclasses import dataclass, field
from icecream import ic

@dataclass
class MDoFODE:
	"""ODE solvers for linear and nonlineasr EOMs""" 

	# Vibration system parameters
	m: float							   # mass
	k: float							   # spring constant
	x0: float							  # initial position
	v0: float							  # initial position

	tf: float							   # simulation duration
	N: int								  # number of point of simulation

	def make_matrices(self):
		####################################
		# TODO14 Mass Matrix
		M = np.array([[1, 0, 0], \
					  [0, 1, 0], \
					  [0, 0, 1]])


		####################################
		# TODO15 Stiffness Matrix   
		K = np.array([[1,	   0,		  0], \
					  [0,	   1,		  0], \
					  [0,	   0,		  1]])

		####################################
		# TODO16 Initial Position
		X0 = np.array([[0], [0], [0]])

		####################################
		# TODO17 Initial Velocity
		V0 = np.array([[0], [0], [0]])

		c = np.concatenate((X0,V0), axis=0)
		d = c.flatten()
		I0 = d.tolist()

		t = np.linspace(0, self.tf, self.N);

		return [M, K, I0, X0, V0, t]		


		

	def mdof(self, X, t, M, K):
		########################################
		# TODO18: Mi is inverse of M	  
		# remove np.eye(3) and write the correct formula	
		Mi =  np.eye(3)

		########################################
		# TODO19: MiK M^(-1)*K		
		# remove np.eye(3) and write the correct formula		
		MiK = np.eye(3)

		########################################
		# TODO20: fill in the spot with the right formula		
		# remove np.eye(3) and write the correct formula	   
		position_states = np.matmul(np.eye(3), np.array([[X[2]], [X[1]], [X[0]]]))

		velocity_states = np.array([[X[5]],[X[4]],[X[3]]])
		states  = np.concatenate((velocity_states, position_states), axis = 0)
		L = states.reshape(1,6).tolist()
		L = np.array(L)
		differntail_equations = L.flatten()

		return differntail_equations
		########################################


	def solve_EOM(self):
		[M,K,I0,X0,V0,t] = self.make_matrices()
		print(f"M = \n{M}\n")
		print(f"K = \n{K}\n")
		print(f"X0 = \n{X0}\n")
		print(f"V0 = \n{V0}\n")

		inial_conditions = I0
		X = odeint(self.mdof, inial_conditions , t, args=(M, K))
		return X, t
