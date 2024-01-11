"""
Vibration Computer Lab
Sajad Saeedi - 2024
Toronto Metropolitan University
"""

from drawerlab.mass_spring_damper import MassSpringDamperClosedForm
import matplotlib.pyplot as plt 
from icecream import ic


def make_plots(time_x_v_a) -> None:
    t = time_x_v_a[0]
    x = time_x_v_a[1]
    v = time_x_v_a[2]
    a = time_x_v_a[3]
    # Part [a-2-i]
    plt.figure('Position vs Time')
    plt.plot(t,x); plt.ylabel('position (m)'); plt.xlabel('time (sec)'); plt.grid();
    plt.savefig('drawer-a2i.png')
    plt.show()

    # Part [a-2-ii]
    plt.figure('Velocity vs Time')
    plt.plot(t,v); plt.ylabel('velocity (m/s)'); plt.xlabel('time (sec)'); plt.grid(); 
    plt.savefig('drawer-a2ii.png')
    plt.show()

    # Part [a-2-iii]
    plt.figure('Acceleration vs Time')
    plt.plot(t,a); plt.ylabel('acceleration (m/s/s)'); plt.xlabel('time (sec)'); plt.grid(); 
    plt.savefig('drawer-a2iii.png')
    plt.show()

def main()-> None:
    
    msd = MassSpringDamperClosedForm(m = 1, c = 2, k = 3, x0 = 0.5, v0 = 0, tf= 10, N = 1000)
    [zeta, wn, wd] = msd.calcaulte_canonical_param()
    ic([zeta, wn, wd])

    [amp, phi] = msd.calcualte_ampilitude_phase(zeta, wn, wd)
    ic([amp, phi])    

    [root1, root2] = msd.calculate_roots()
    ic([root1, root2])

    time_x_v_a = msd.calculate_x_v_a(zeta, wn, wd, amp, phi)

    make_plots(time_x_v_a)

if __name__ == "__main__":
    main()
