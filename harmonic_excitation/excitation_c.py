"""
Vibration Computer Lab
Sajad Saeedi - 2024
Toronto Metropolitan University
"""

from excitationlab.mass_spring_damper import MassSpringDamperExcitedODE
from excitationlab.make_plots import plot_amplitude_velocity_error

def main() -> None:
    
    msde = MassSpringDamperExcitedODE(m = 75, c = 8, a = 8, k = 250, k1 = 400, 
                                        x0 = 0.01, v0 = 0.5, 
                                        F0 = [50, 25], w = [3, 6], 
                                        tf= 40, N = 4000)

    x1, t1 = msde.solve_EOM_nlin_k_lin_c()
    x2, t2 = msde.solve_EOM_nlin_k_nlin_c()
    plot_amplitude_velocity_error(x1, t1, x2, t2, 
                                    legend1 = "nonlinear spring - linear damper", 
                                    legend2 = "nonlinear spring - nonlinear damper", 
                                    filename1 = "c1-external-force-amplitude.png")

if __name__ == '__main__':
    main()
