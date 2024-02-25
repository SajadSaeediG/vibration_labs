"""
Vibration Computer Lab
Sajad Saeedi - 2024
Toronto Metropolitan University
"""


from mdoflab.mdof_mk_ode import MDoFODE
import numpy as np
from mdoflab.mdof_make_plots import plot_amplitudes
from mdoflab.mdof_make_plots import plot_amplitudes_velocities



def main() -> None:
	
	m = [2, 2, 2]  
	k = [2, 2, 2, 2] 
	x0 = [0, 0, 0] 
	v0 = [0, 0, 0]
	tf = 40
	N = 4000

	########################################################################
	# Part [b]
	solver = MDoFODE(m, k, x0, v0, tf, N)
	x, t = solver.solve_EOM()
	plot_amplitudes_velocities(x,t)


if __name__ == '__main__':
	main()