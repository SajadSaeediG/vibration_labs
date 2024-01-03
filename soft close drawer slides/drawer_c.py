"""
Vibration Computer Lab
Sajad Saeedi - 2024
Toronto Metropolitan University
"""

from drawerlab.mass_spring_damper import MassSpringDamperODE
import matplotlib.pyplot as plt 


def plot_figures(t, position, velocity):
	plt.figure('Position vs Time')
	plt.plot(t, position); plt.ylabel('position (m)'); plt.xlabel('time (sec)'); plt.grid(); 
	#plt.savefig('drawer-b2i.png')
	plt.show()

	plt.figure('Velocity vs Time')
	plt.plot(t, velocity); plt.ylabel('velocity (m/s)'); plt.xlabel('time (sec)'); plt.grid(); 
	#plt.savefig('drawer-b2ii.png')
	plt.show()

def main():
	# Part [b]
    msd = MassSpringDamperODE(m = 1, c = 2, k = 3, x0 = 0.5, v0 = 0, tf= 10, N = 1000)
    t, position, velocity, number_of_points = msd.solve_motion()
    plot_figures(t, position, velocity)

	# Part [c]
    closing_velocity, closing_time, kinetic_energy, drawer_closed = msd.calculate_KE(position, velocity)
    print(f"closing velocity: {closing_velocity}, \nclosing time {closing_time}, \nkinetic energy: {kinetic_energy}, \ndrawer closed: {drawer_closed}")
    print("----------------------------------------")

if __name__ == '__main__':
    main()
