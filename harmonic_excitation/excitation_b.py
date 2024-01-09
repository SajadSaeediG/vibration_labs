"""
Vibration Computer Lab
Sajad Saeedi - 2024
Toronto Metropolitan University
"""

from excitationlab.mass_spring_damper import MassSpringDamperExcitedODE
from excitationlab.make_plots import plot_amplitude_velocity_error, plot_dampings

import matplotlib.pyplot as plt 
from matplotlib.patches import Rectangle
import numpy as np

def main() -> None:
    
    msde = MassSpringDamperExcitedODE(m = 75, c = 8, a = 8, k = 250, k1 = 400, 
                                        x0 = 0.01, v0 = 0.5, 
                                        F0 = [50, 25], w = [3, 6], 
                                        tf= 40, N = 4000)

    x1, t1 = msde.solve_EOM_lin_k_lin_c()
    x2, t2 = msde.solve_EOM_nlin_k_lin_c()
    plot_amplitude_velocity_error(x1, t1, x2, t2, 
                                    legend1 = "linear spring - linear damper", 
                                    legend2 = "nonlinear spring - linear damper", 
                                    filename1 = "b1-external-force-amplitude.png", 
                                    filename2 = "b1-external-force-velocity.png")

    target_speed = 0.60
    target_amplitude = 0.26
    plt.show()
    max_amplitude = []
    max_velocity = []
    c_coeffiecnt = []
    ########################################
    # TODO2: adjust the range values      
    for c_coeff in range(30,34):
        ########################################    
        msde = MassSpringDamperExcitedODE(m = 75, c = c_coeff, a = 8, k = 250, k1 = 400, 
                                            x0 = 0.01, v0 = 0.5, 
                                            F0 = [50, 25], w = [3, 6], 
                                            tf= 40, N = 4000)
        x, t = msde.solve_EOM_nlin_k_lin_c()
  
        amplitude = x[:,0]
        velocity = x[:,1]
        max_amplitude.append(np.max(np.abs(amplitude)))
        max_velocity.append(np.max(np.abs(velocity)))
        c_coeffiecnt.append(c_coeff)
        
    print(c_coeffiecnt)
    plot_dampings(c_coeffiecnt, max_amplitude, max_velocity, target_amplitude, target_speed, 'b1-external-force-dampings.png')


if __name__ == '__main__':
    main()
