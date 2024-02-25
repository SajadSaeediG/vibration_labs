"""
Vibration Computer Lab
Sajad Saeedi - 2024
Toronto Metropolitan University
"""


from mdoflab.mdof_mk import MDOFModal
from mdoflab.mdof_animation import MDOFAnimation
import numpy as np
from mdoflab.mdof_make_plots import plot_amplitudes


def main() -> None:
	
	m = [2, 2, 2]  
	k = [2, 2, 2, 2] 
	x0 = [0, 0, 0] 
	v0 = [0, 0, 0]
	tf = 40
	N = 4000

	mdof = MDOFModal(m, k, x0, v0, tf, N)
	physical_answers, modal_answers, t = mdof.solve_modal()
	plot_amplitudes(physical_answers, modal_answers, t)

	mdof_animation = MDOFAnimation(m, k, x0, v0, tf, N)
	mdof_animation.run_animation(physical_answers)


if __name__ == '__main__':
	main()