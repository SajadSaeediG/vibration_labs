"""
Vibration Computer Lab
Sajad Saeedi - 2024
Toronto Metropolitan University
"""

import matplotlib.pyplot as plt 


def plot_amplitudes(physical_answers, modal_answers, t):
    plt.figure(1)
    plt.plot(t, modal_answers[0], '-.r', linewidth=1, label='r1') 
    plt.plot(t, modal_answers[1], '-.g', linewidth=1, label='r2')
    plt.plot(t, modal_answers[2], '-.b', linewidth=1, label='r3') 


    plt.ylabel('amplitude (m)'); plt.xlabel('time (sec)'); 
    plt.title('Modal Responses - Displacement'); plt.grid(); plt.legend() 
    plt.savefig('A-modal-displacement.png')
    plt.show()

    plt.figure(2)
    plt.plot(t, physical_answers[0], '-.r', linewidth=1, label='x1') 
    plt.plot(t, physical_answers[1], '-.g', linewidth=1, label='x2')
    plt.plot(t, physical_answers[2], '-.b', linewidth=1, label='x3') 


    plt.ylabel('amplitude (m)'); plt.xlabel('time (sec)'); 
    plt.title('Physical Responses - Displacement'); plt.grid(); plt.legend() 
    plt.savefig('A-physical-displacement.png')
    plt.show()


def plot_amplitudes_velocities(x,t):

    amplitude_physical = x[:,0:2]
    velocity_physical = x[:,3:5]
    
    # plots
    plt.figure(3)
    plt.plot(t, x[:,0], '-.r', linewidth=1, label='x1') 
    plt.plot(t, x[:,1], '-.g', linewidth=1, label='x2')
    plt.plot(t, x[:,2], '-.b', linewidth=1, label='x3') 

    plt.ylabel('amplitude (m)'); plt.xlabel('time (sec)');
    plt.title('Physical Responses - Displacement'); plt.grid(); plt.legend()  
    plt.savefig('B-physical-displacement.png')
    plt.show()

    # plots
    plt.figure(4)
    plt.plot(t, x[:,3], '-.r', linewidth=1, label='x1') 
    plt.plot(t, x[:,4], '-.g', linewidth=1, label='x2')
    plt.plot(t, x[:,5], '-.b', linewidth=1, label='x3') 

    plt.ylabel('amplitude (m)'); plt.xlabel('time (sec)');
    plt.title('Physical Responses - Velocity'); plt.grid(); plt.legend() 
    plt.savefig('B-physical-velocity.png')
    plt.show()
