"""
Vibration Computer Lab
Sajad Saeedi - 2024
Toronto Metropolitan University
"""

from excitationlab.mass_spring_damper import MassSpringDamperExcitedODE
import numpy as np
from excitationlab.make_plots import plot_amplitude_velocity, plot_dampings, animate_plots


def main() -> None:
    
    msde = MassSpringDamperExcitedODE(m = 75, c = 8, a = 8, k = 250, k1 = 80, 
                                        x0 = 0.01, v0 = 0.5, 
                                        F0 = [50, 25], w = [3, 6], 
                                        tf= 40, N = 4000)
    x, t = msde.solve_EOM_lin_k_lin_c()
    plot_amplitude_velocity(x, t, 'a1-external-force-amplitude.png')
    
    # use this to create animations. ffmpeg needed to be installed.
    #animate_plots(x, t, F0 = 50, w = 3, tf= 40, N = 4000) 


    target_speed = 0.60
    target_amplitude = 0.26
    max_amplitude = []
    max_velocity = []
    c_coeffiecnt = []
    ########################################
    # TODO2: adjust the range values      
    for c_coeff in range(30,34):
        ########################################    
        msde = MassSpringDamperExcitedODE(m = 75, c = c_coeff, a = 8, k = 250, k1 = 80, 
                                            x0 = 0.01, v0 = 0.5, 
                                            F0 = [50, 25], w = [3, 6], 
                                            tf= 40, N = 4000)
        x, t = msde.solve_EOM_lin_k_lin_c()
  
        amplitude = x[:,0]
        velocity = x[:,1]
        max_amplitude.append(np.max(np.abs(amplitude)))
        max_velocity.append(np.max(np.abs(velocity)))
        c_coeffiecnt.append(c_coeff)
        
    print(c_coeffiecnt)
    plot_dampings(c_coeffiecnt, max_amplitude, max_velocity, 
                    target_amplitude, target_speed, 
                    "a2i-external-force-dampings.png")



    ########################################
    # TODO3: pick the right value for c    
    ########################################
    msde = MassSpringDamperExcitedODE(m = 75, c = 30, a = 8, k = 250, k1 = 80, 
                                        x0 = 0.01, v0 = 0.5, 
                                        F0 = [50, 25], w = [3, 6], 
                                        tf= 40, N = 4000)
    x, t = msde.solve_EOM_lin_k_lin_c()
    plot_amplitude_velocity(x, t, 'a2i-external-force-amplitude.png')


if __name__ == '__main__':
    main()