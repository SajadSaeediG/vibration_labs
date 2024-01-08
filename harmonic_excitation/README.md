# Harmonic Excitation
## Harmonic Excitation with Linear and Nonlinear Models


### Problem Statement
Harmonic excitation is very common in vibrating systems. More complex excitation can be considered as summation of multiple harmonic excitations.

![module](./images/electronics_module.png)

An electronics module is mounted on a machine and is modeled as an SDOF spring-mass-damper system. The module is subject to a harmonic forces F<sub>01</sub> = 50 N at w<sub>1</sub> = 3 rad/s and F<sub>02</sub> = 25 N at w<sub>2</sub> = 6 rad/s. Assume the following parameters: m =75 kg, K = 250 N/m, c = 8 kg/s. Assume the initial conditions of the system are x<sub>0/sub> = 0.01 m and v<sub>0</sub> = 0.5 m/s. The module’s amplitude of vibration must be less than 0.4 m,  and its speed must be under 0.8 m/s, both even during the transient stage.

This lab has parts a, b, and c.


### Part A
[A][45%] Simulate the response of the system. Solve the equations of the motion numerically using ODE library.


**[A-1]** Plot the response of the system for 40 seconds.  
	**[(I)]** Show a plot, amplitude vs time [5%] and velocity vs time [5%], both on one plot side by side.
	**[(II)]** With the parameters given, is the design constraint achievable? [5%]

Hint: open the file `mass_spring_damper.py` and complete **TODO1**. Then run the code for part a.

**[A-2]** You are allowed to increase the damping coefficient, by the steps of 4 kg/s, starting from 30 kg/s, and ending at 98 kg/s. What is the smallest value of c such that the maximum vibration amplitude is limited to 0.26 m and the maximum speed is limited to 0.60 m/s? Use an exhaustive search method to search for the values of the damping coefficient. In your report, present: 
	**[(I)]** (i) a graph demonstrating max velocity/max amplitude vs damping coefficient [5%]. Reports these graphs for the right value of c, for 40 seconds.
	**[(II)]** Report the value of c satisfying the constraints. [5%].
	**[(III)]** (iii)	For the value satisfying the constraints, preset amplitude vs time [5%] and velocity vs time [5%], both on one plot side by side. 

Hint: In file `excitation_a.py`, complete **TODO2-3**.

**[A-3]**  In your lab report, present the code you developed for only TODO1-3 [10%]. Attached the full code.



### Animations
Animation of mass-spring-damper system under harmonic excitation:\
![overdamped](./images/harmonic_excitation.gif)


