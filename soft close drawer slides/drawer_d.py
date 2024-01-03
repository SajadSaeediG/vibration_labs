"""
Vibration Computer Lab
Sajad Saeedi - 2024
Toronto Metropolitan University
"""

from drawerlab.mass_spring_damper import MassSpringDamperODE
import matplotlib.pyplot as plt 
import numpy as np

def plot_figure(damping_coefficient: list, kinetic_energy_valaues: np.arange) -> None:
    plt.figure('Kinetic Energy vs Damping Coefficient')
    plt.semilogy(damping_coefficient, kinetic_energy_valaues, 'o-'); 
    plt.ylabel('kinetic energy (J)');
    plt.xlabel('damping coefficient (N/m/s}'); 
    plt.grid(); 
    plt.savefig('drawer-d1.png')
    plt.show()

def main():
    kinetic_energy_valaues = []
    damping_coefficient = np.arange(0.1, 3.2, 0.1)
    for damping in damping_coefficient:
        msd = MassSpringDamperODE(m = 1, c = damping, k = 3, x0 = 0.5, v0 = 0, tf= 10, N = 1000)
        t, position, velocity, number_of_points = msd.solve_motion()

        closing_velocity, closing_time, kinetic_energy, door_closed = msd.calculate_KE(position, velocity)  
        kinetic_energy_valaues.append(kinetic_energy)

    plot_figure(damping_coefficient, kinetic_energy_valaues)    

    ########################################
    # TODO9: insert the correct formula here  
    damoing = 1
    ########################################

    msd = MassSpringDamperODE(m = 1, c = damping, k = 3, x0 = 0.5, v0 = 0, tf= 10, N = 1000)
    t, position, velocity, number_of_points = msd.solve_motion()

    plt.figure('Position vs Time')    
    plt.plot(t, position); plt.ylabel('position (m)'); plt.xlabel('time (sec)'); plt.grid(); 
    plt.savefig('drawer-d2i.png')
    plt.show()

    plt.figure('Velocity vs Time')
    plt.plot(t, velocity); plt.ylabel('velocity (m/s)'); plt.xlabel('time (sec)'); plt.grid(); 
    plt.savefig('drawer-d2ii.png')
    plt.show()

    closing_velocity, closing_time, kinetic_energy, drawer_closed = msd.calculate_KE(position, velocity)  

    print(f"closing velocity: {closing_velocity}, \nclosing time {closing_time}, \nkinetic energy: {kinetic_energy}, \ndrawer closed: {drawer_closed}")
    print("----------------------------------------")


if __name__ == '__main__':
    main()
