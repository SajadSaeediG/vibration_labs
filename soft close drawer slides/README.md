# MEC721-W2024
## Simulation of an SDOF vibration system
### Lab1: Sliding Drawer

**Format:** Individual lab/report

**Note1:** Plagiarism is a serious academic offense, which can affect your status in the program. You are expected to finish the lab independently and report your results honestly.

**Note2:** Attendance in the lab is mandatory. No show means a 0 grade for that lab, even if you submit a report. There is no make-up session. You are not allowed to change your section.

**Due date:** A week after your lab session, right before the start of the next session. For example, if your lab session started at 2 PM, Jan 1st, 2020, your report is due at 2 PM, Jan 8th, 2020.



**Problem Statement:**  Soft-close drawer slides are used to make sure the drawer is closed softly. One of the advantages of such systems is that no electricity is required to close the drawer. 

![drawer](./images/drawer.png)

The system can be modeled as a single degree of freedom, with a point mass of m \[kg\] (for the drawer), spring stiffness of k \[N/m\], and the damping coefficient of c \[F/m/s\]. Refer to the course material for the EOM of the system. Assume m = 1, k = 3, c = 2.

This lab has parts a, b, c, d, and e.


### Part a
**\[a\]\[20%\]** Simulate the response of the system, assuming the drawer is opened by 50 cm and released from rest. Use a closed-form solution to simulate the response of the system. Refer to your textbook, for the formulations. To use the right formulation, you need to know if the system is underdamped, overdamped, etc. Follow the steps below.

Deliverables: 

**\[a-1\]** Determine the roots of the system \[2%\]. What do the roots state about the system? \[1%\]
Hint: open the file `drawerlab/mass_spring_damper.py` and complete **TODO1**
By running `drawer_a.py`, you will see the results.
	
**\[a-2\]** Once you know the type of the system, in file `drawer_a.py`, complete **TODO2-5**.

Reports three graphs, showing the time response of the system, i.e. (i) position vs time \[4%\], (ii) velocity vs time \[4%\], and (iii) acceleration vs time \[4%\]. These graphs are saved on your computer.

**\[a-3\]** In your lab report, report the code you developed for only **TODO1-5** \[5%\]. Attached full code.


### Part b
**\[b\]\[15%\]** Solve the equations of the motion numerically using ODE library.

Note: You can disable/enable simulation from here: `drawerlab/settings.py`. 
 
**_Deliverables:_** 

**\[b-1\]** You will need to run `drawer_b.py`. But first, open file `drawerlab/mass_spring_damper.py` and complete task **TODO6-7**. Refer to your textbook or online resource for solving differential equations using ODE.

Report two graphs, showing the time response of the system, i.e. (i) position vs time [5%], (ii) velocity vs time [5%].  

**\[b-2\]** In your lab report, report the code you developed for only TODO6-7 [5%]. Attached full code.



### Part c
**\[c\]\[10%\]** Calculate the amount of kinetic energy, if the drawer comes in contact with the cabinet frame when closing. 

**_Deliverables_** 

You will need to run `drawer_c.py`. But first, open file `drawerlab/mass_spring_damper.py` again and complete task **TODO8**

**\[c-1\]** Report the formulation of calculations [2%]

**\[c-2\]** Report the amount of kinetic energy in Joules which is calculated once you run the code [4%]

**\[c-3\]** How long did it take for the drawer to close, assume the drawer closes once it hits the frame [2%]

**\[c-4\]** In your lab report, report the code you developed for only **TODO8** [2%]. Attached full code.



### Part d
**\[d\]\[20%\]** You are allowed to choose the damping coefficient from 0.1, 0.2, …, 3.0, 3.1. such that the kinetic energy upon impact is at most 0.01 [J]. 

**_Deliverables_** 

You will need to run `drawer_d.py`. 

**\[d-1\]** Report a plot demonstrating the kinetic energy on the y-axis vs the permitted damping coefficient on the x-axis, i.e. 0.1, 0.2, …, 3.0, 3.1. [8%]

**\[d-2\]** Pick the first values for c from the range such that the kinetic energy is less than 0.01 [J] and plot position-time [4%], and velocity-time [4%]. You can choose the right values for c from the graph. Then complete task **TODO9**.

**\[d-3\]** With the value selected, how long did it take for the drawer to close, assume the drawer closes once it hits the frame [2%].

**\[d-4\]** In your lab report, report the code you developed for only **TODO9** [2%]. Attached full code.




### Part e
**\[e\]\[35%\]** You are allowed to change both spring constant in range {0.1, 0.2, …, 2.3, 2.4} and the damping coefficient in range {0.1, 0.2, …, 2.3, 2.4}.

**_Deliverables_** 

Open `drawer_e.py`, complete task **TODO10**, and run the code.

**\[e-1\]** Report a plot demonstrating all k values on the y-axis vs all c values on the x-axis. The plot should show the permissible range for c and k, such that the drawer is closed in 10 seconds. [10%]

**\[e-2\]** Pick a value for c and k from the permissible range, such that the KE is minimized [5%]. Report the closing time [5%].

**\[e-3\]** Pick a value for c and k from the permissible range, such that the KE is maximized [5%]. Report the closing time [5%].

**\[e-4\]** In your lab report, report the code you developed for only **TODO10** [5%]. Attach the full code.



### Animations
An example of overdamped design
![overdamped](./images/drawer_overdamped.gif)
