"""
Vibration Computer Lab
Sajad Saeedi - 2024
Toronto Metropolitan University
"""

import numpy as np
from numpy import linalg as LA
from dataclasses import dataclass, field
from icecream import ic

@dataclass
class MDOFModal():

	# Vibration system parameters
	m: float							   # mass
	k: float							   # spring constant
	x0: float							  # initial position
	v0: float							  # initial position

	tf: float							   # simulation duration
	N: int								  # number of point of simulation


	def make_matrices(self):
		####################################
		# TODO1 Mass Matrix
		M = np.array([[self.m[0], 0, 0], \
					  [0, 1, 0], \
					  [0, 0, 1]])

		####################################
		# TODO2 Stiffness Matrix   
		K = np.array([[1, 		0, 			0], \
					  [0, 		1, 			0], \
					  [0, 		0, 	 		1]])

		####################################
		# TODO3 Initial Position
		X0 = np.array([[self.x0[0]], [0], [0]])

		####################################
		# TODO4 Initial Velocity
		V0 = np.array([[0], [0], [0]])

		t = np.linspace(0, self.tf, self.N);

		return [M, K, X0, V0, t]

	@staticmethod
	def compute_natfreq_modalic_transformation(M, K, X0, V0):
		####################################
		# TODO5 M^(-1/2)
		# remove np.eye(3) and write the correct formula 
		# use LA.inv() and np.sqrt() 
		Minv2 = np.eye(3)
		KMinv2 = np.matmul(K, Minv2)

		####################################
		# TODO6 Mass Normlized Stiffness Matrix
		# remove np.eye(3) and write the correct formula
		Kt = np.eye(3)
		
		# D: wigen values, P: eigen vectors
		D, P = LA.eig(Kt) 
		print(f"Eigen Values: {D}")

		####################################
		# TODO7 S in x(t)=Sr(t)
		# remove np.eye(3) and write the correct formula
		S = np.eye(3)

		Sinv = LA.inv(S)

		####################################
		# TODO8: initial position in the modal space
		# remove np.eye(3) and write the correct formula
		r0 = np.eye(3)

		####################################
		# TODO9: initial velocity in the modal space  
		# remove np.eye(5) and write the correct formula	
		rdot0 = np.eye(3)

		####################################
		# TODO10: natural frequencies	 
		# remove np.ones(3).tolist() and write the correct formula	
		w = np.ones(3).tolist()
		print(f"Natural Frequencies: {w}")
		print(f"Natural Frequencies: {w}")

		return [w, r0, rdot0, S]

	@staticmethod
	def compute_modal_answers(w, r0, rdot0, t):
		modal_answers = []
		for mode in range(0,3):
			if w[mode] != 0:
				############################################
				# TODO11: type in the closed form solution of the modal answer, r(t)
				# remove t and write the correct formula   
				r = t  
			
			if w[mode] < 0.000001: 
				############################################
				# TODO13: type in the closed form solution of the modal answer, r(t)
				# this is not needed for [a]-1 to [a]-4
				# remove t and write the correct formula   
				r = t  

			modal_answers.append(r)
		return modal_answers


	@staticmethod
	def compute_physical_answer(S, modal_answers):
		# TODO12: Transform the modal answers to the physical answers  
		# remove np.eye(5) and write the correct formula	 
		X = np.matmul(np.eye(3), modal_answers)
		return X

	def solve_modal(self):
		[M,K,X0,V0,t] = self.make_matrices()
		print(f"M = \n{M}\n")
		print(f"K = \n{K}\n")
		print(f"X0 = \n{X0}\n")
		print(f"V0 = \n{V0}\n")

		[w,r0,rdot0,S] = type(self).compute_natfreq_modalic_transformation(M,K,X0,V0)
		print(f"w = \n{w}\n")
		print(f"r0 = \n{r0}\n")
		print(f"rdot0 = \n{rdot0}\n")

		modal_answers = type(self).compute_modal_answers(w, r0, rdot0, t)

		physical_answers = type(self).compute_physical_answer(S, modal_answers)

		return physical_answers, modal_answers, t
