# Harmonic Excitation
## Harmonic Excitation with Linear and Nonlinear Models


### Problem Statement
Harmonic excitation is very common in vibrating systems. More complex excitation can be considered as summation of multiple harmonic excitations.

![module](./images/electronics_module.png)

An electronics module is mounted on a machine and is modeled as an SDOF spring-mass-damper system. The module is subject to a harmonic forces F<sub>01</sub> = 50 N at w<sub>1</sub> = 3 rad/s and F<sub>02</sub> = 25 N at w<sub>2</sub> = 6 rad/s. Assume the following parameters: m =75 kg, K = 250 N/m, c = 8 kg/s. Assume the initial conditions of the system are x<sub>0/sub> = 0.01 m and v<sub>0</sub> = 0.5 m/s. The module’s amplitude of vibration must be less than 0.4 m,  and its speed must be under 0.8 m/s, both even during the transient stage.

This lab has parts a, b, and c.


### Part A
[a][45%] Simulate the response of the system. Solve the equations of the motion numerically using ODE library.


Deliverables: 

**\[a-1\]** Determine the roots of the system \[2%\]. What do the roots state about the system? \[1%\]
Hint: open the file `drawerlab/mass_spring_damper.py` and complete **TODO1**.
By running `drawer_a.py`, you will see the results.
	
**\[a-2\]** Once you know the type of the system, in file `drawer_a.py`, complete **TODO2-5**.

Reports three graphs, showing the time response of the system, i.e. (i) position vs time \[4%\], (ii) velocity vs time \[4%\], and (iii) acceleration vs time \[4%\]. These graphs are saved on your computer.

**\[a-3\]** In your lab report, report the code you developed for only **TODO1-5** \[5%\]. Attached full code.


### Animations
Animation of mass-spring-damper system under harmonic excitation:\
![overdamped](./images/harmonic_excitation.gif)


