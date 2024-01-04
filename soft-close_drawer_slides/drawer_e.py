"""
Vibration Computer Lab
Sajad Saeedi - 2024
Toronto Metropolitan University
"""

from drawerlab.mass_spring_damper import MassSpringDamperODE
import numpy as np
import matplotlib.pyplot as plt 


def plot_figures(kinetic_energy_matrix: np.ndarray, k_range: np.arange, c_range: np.arange) -> None:
    figure = plt.figure('Kinetic Energy')
    axes = figure.add_subplot(111)
    cax = axes.matshow(kinetic_energy_matrix)
    cbar = figure.colorbar(cax);
    cbar.set_label("kinetic energy [J]", loc='center')

    axes.set_xticks(np.arange(0, len(k_range), 1));
    axes.set_yticks(np.arange(0, len(c_range), 1));

    axes.set_xticklabels(k_range, rotation='vertical');
    axes.set_yticklabels(c_range);

    plt.ylabel('damping coefficient, c [Ns/m]'); 
    plt.xlabel('spring constant, k [N/m]'); 
    plt.savefig('drawer-e1.png')
    plt.show()

def find_min_max_KE(kinetic_energy_matrix: np.ndarray, closing_time_matrix: np.ndarray, k_range: np.arange, c_range: np.arange) -> None:
    mask = (kinetic_energy_matrix[:, :] >= 0)
    min_KE = min(kinetic_energy_matrix[mask])
    ind = np.where(kinetic_energy_matrix == min_KE)
    print(f"Minimum KE = {min_KE} [J], \nc = {c_range[ind[0]]} [Ns/m], \nk = {k_range[ind[1]]} [N/m], \nclosing time: {closing_time_matrix[ind]} [s]")
    print("----------------------------------------")


    max_KE = np.max(kinetic_energy_matrix)
    ind = np.unravel_index(np.argmax(kinetic_energy_matrix), kinetic_energy_matrix.shape)
    print(f"Maximum KE = {max_KE} [J], \nc = {c_range[ind[0]]} [Ns/m], \nk = {k_range[ind[1]]} [N/m], \nclosing time: {closing_time_matrix[ind]} [s]")
    print("----------------------------------------")


def main():
    k_range = np.round(np.arange(0.1, 2.5, 0.1),1)
    c_range = np.round(np.arange(0.1, 2.5, 0.1),1)

    W = len(c_range)
    H = len(k_range)
    drawer_closed_matrix = np.zeros((W, H))
    kinetic_energy_matrix = np.zeros((W, H))
    closing_time_matrix = np.zeros((W, H))
 

    ########################################
    # TODO10: insert the correct range for c and k   
    for i, spring in enumerate(range(1,24)):
        for j, damping in enumerate(range(1,24)):
        ########################################

            msd = MassSpringDamperODE(m = 1, c = damping, k = spring, x0 = 0.5, v0 = 0, tf= 10, N = 1000)
            t, position, velocity, number_of_points = msd.solve_motion()

            closing_velocity, closing_time, kinetic_energy, drawer_closed = msd.calculate_KE(position, velocity)  
            drawer_closed_matrix[j, i] = drawer_closed
            kinetic_energy_matrix[j, i] = kinetic_energy
            closing_time_matrix[j, i] = closing_time


    plot_figures(kinetic_energy_matrix, k_range, c_range)
    find_min_max_KE(kinetic_energy_matrix, closing_time_matrix, k_range, c_range)

if __name__ == '__main__':
    main()
