"""
Vibration Computer Lab
Sajad Saeedi - 2024
Toronto Metropolitan University
"""

import matplotlib.pyplot as plt 
import numpy as np
import os
from matplotlib.patches import Rectangle
from excitationlab.make_video import VideoFromMatplotlib

def plot_amplitude_velocity(x, t, filename):
    amplitude = x[:,0]
    velocity = x[:,1]

    fig, ax = plt.subplots(1, 2, figsize=(12, 4))

    ax[0].plot(t, amplitude, '-.k', linewidth=1); 
    ax[0].set_ylabel('amplitude (m)'); 
    ax[0].set_xlabel('time (sec)'); 
    ax[0].grid(); 

    ax[1].plot(t, velocity, '-.k', linewidth=1); 
    ax[1].set_ylabel('velocity (m/s)'); 
    ax[1].set_xlabel('time (sec)'); 
    ax[1].grid(); 
    
    plt.savefig(filename)
    plt.show(block = True)



def plot_amplitude_velocity_error(x1, t1, x2, t2, 
                                    legend1 = "", legend2 = "", 
                                    filename1 = "", filename2 = ""):    
    amplitude1 = x1[:,0]
    velocity1 = x1[:,1]

    amplitude2 = x2[:,0]
    velocity2 = x2[:,1]

    if(filename1):
        fig, ax = plt.subplots(1, 2, figsize=(12, 4))
        ax[0].plot(t1, amplitude1, '-.k', linewidth=1);  
        ax[0].plot(t1, amplitude2, '-r', linewidth=1); 
        ax[0].set_ylabel('amplitude (m)'); ax[0].set_xlabel('time (sec)'); ax[0].grid(); 
        ax[0].legend([legend1, legend2])

        ax[1].plot(t1, amplitude2 - amplitude1, 'k', linewidth=1); 
        ax[1].set_ylabel('amplitude error (m)'); ax[1].set_xlabel('time (sec)'); ax[1].grid(); 
        plt.savefig(filename1)
        print(f"maximum amplitude modeling error is {np.round(np.max(np.abs(amplitude2-amplitude1)),2)} m")

    if(filename2):    
        fig, ax = plt.subplots(1, 2, figsize=(12, 4))
        ax[0].plot(t2, velocity1, '-.k', linewidth=1);  
        ax[0].plot(t2, velocity2, '-r', linewidth=1); 
        ax[0].set_ylabel('velocity (m/s)'); ax[0].set_xlabel('time (sec)'); ax[0].grid(); 
        ax[0].legend([legend1, legend2])


        ax[1].plot(t2, velocity2-velocity1, 'k', linewidth=1); 
        ax[1].set_ylabel('velocity error (m)'); ax[1].set_xlabel('time (sec)'); ax[1].grid(); 
        plt.savefig(filename2)
        print(f"maximum speed modeling error is {np.round(np.max(np.abs(velocity2-velocity1)),2)} m/s")

    plt.show(block = True)



def plot_dampings(c_coeffiecnt, max_amplitude, max_velocity, target_amplitude, target_speed, fig_name):
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    ax1.plot(c_coeffiecnt, max_amplitude, 'sr', linewidth=1, label='maximum amplitude'); 
    ax1.set_ylabel('maximum amplitude (m)', color='r'); ax1.set_xlabel('damping coefficient'); 
    ax1.plot(c_coeffiecnt, target_amplitude * np.ones(len(c_coeffiecnt)), '-.r', linewidth=1, label='target maximum amplitude'); 

    ax2.plot(c_coeffiecnt, max_velocity, 'ob', linewidth=1, label='maximum speed'); 
    ax2.set_ylabel('maximum speed (m)', color='b'); 
    ax2.plot(c_coeffiecnt, target_speed * np.ones(len(c_coeffiecnt)), '-.b', linewidth=1, label='target maximum speed'); 

    ax2.legend(loc='upper right')
    ax1.legend(loc='lower left')

    plt.savefig(fig_name)
    plt.show(block=True)


def animate_plots(x, t, F0 = 50, w = 3, tf= 40, N = 4000):
    fig, ax = plt.subplots(2, 2, figsize=(12, 7))
    plt.ion()  

    amplitude = x[:,0]
    velocity = x[:,1]
    F = F0 * np.sin(w*t)

    graph = ax[0, 0].plot([], [])[0]
    graph = ax[0, 1].plot([], [])[0]
    graph = ax[1, 0].plot([], [])[0]

    mod_x, mod_y = 0.0, amplitude[0]
    animation = ax[0,0]

    mod = animation.add_patch(Rectangle((mod_x - 0.25, mod_y - 0.25), 0.5, 0.5,  alpha=0.5, facecolor='b'))
    GND = animation.add_patch(Rectangle((mod_x - 0.25, mod_y - 1), 0.5, 0.1,  alpha=0.5, facecolor='r'))
    MSD = animation.add_patch(Rectangle((mod_x - 0.02, mod_y - 0.25), 0.1, 0.1,  alpha=0.5, facecolor='g'))
    ARR = animation.annotate("", xy=(0.5, mod_y), xytext=(0.5, 0), arrowprops=dict(arrowstyle="->"))

    ax[0, 0].set_ylim(-0.2, 1.8)
    ax[0, 0].set_xlim(-0.75, .75)
    ax[0, 0].set_ylabel('y (m)')
    ax[0, 0].set_xlabel('x (m)')
    ax[0, 0].grid();
 
    ax[0, 1].set_ylim(-60, 60)
    ax[0, 1].set_xlim(0,40)
    ax[0, 1].set_ylabel('external force (N)')
    ax[0, 1].set_xlabel('time (s)', loc='right')
    ax[0, 1].grid();

    ax[1, 0].set_ylim(-0.4, 0.4)
    ax[1, 0].set_xlim(0,40)
    ax[1, 0].set_xlim(0,40)
    ax[1, 0].set_ylabel('amplitude of module (m)')
    ax[1, 0].set_xlabel('time (s)', loc='right')
    ax[1, 0].grid();

    ax[1, 1].set_ylim(-0.9, 0.9)
    ax[1, 1].set_xlim(0,40)
    ax[1, 1].set_ylabel('velcoity of module (m)')
    ax[1, 1].set_xlabel('time (s)', loc='right')
    ax[1, 1].grid();


    video = VideoFromMatplotlib(os.getcwd())

    inc = 1
    while inc < N:         
        graph.remove()
        mod.remove()
        GND.remove()
        MSD.remove()
        ARR.remove()

        graph = ax[1, 0].plot(t[0:inc], amplitude[0:inc], '-.k', linewidth=1)[0]
        graph = ax[1, 1].plot(t[0:inc], velocity[0:inc],  '-.k', linewidth=1)[0]
        graph = ax[0, 1].plot(t[0:inc], F[0:inc],         'b', linewidth=1)[0]

        DEL_k = 0.5
        mod_W, mod_H = 0.5, 0.5       # module
        GND_W, GND_H = 0.7, 0.1       # ground
        MSD_W = 0.1

        GND_x, GND_y = 0.0 - GND_W/2, 0.0
        MSD_x, MSD_y = 0.0 - MSD_W/2, GND_y + GND_H 
        mod_x, mod_y = 0.0 - mod_W/2, MSD_y + amplitude[inc] + DEL_k
        MSD_H = mod_y - GND_y - GND_H       # mass-spring-damper

        mod = animation.add_patch(Rectangle((mod_x, mod_y), mod_W, mod_H, alpha=0.5, facecolor='r'))
        GND = animation.add_patch(Rectangle((GND_x, GND_y), GND_W, GND_H, alpha=1.0, facecolor='k'))
        MSD = animation.add_patch(Rectangle((MSD_x, MSD_y), MSD_W, MSD_H, alpha=0.5, facecolor='g'))
        ARR = animation.annotate("F", xy=(-(mod_x+0.05), mod_y + mod_H), xytext=(-(mod_x+0.065), mod_y + mod_H +.25), arrowprops=dict(arrowstyle="->"))

        video.make_png(plt)
        plt.pause(0.01)
        
        inc += 10

    plt.show(block=True)
    video.make_mp4()
    plt.ion()

