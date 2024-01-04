# MEC721-W2024
## Simulation of an SDOF vibration system
### Lab1: Sliding Drawer

**Format:** Individual lab/report

**Note1:** Plagiarism is a serious academic offense, which can affect your status in the program. You are expected to finish the lab independently and report your own results honestly.

**Note2:** Attendance in the lab is mandatory. No show means 0 grade for that lab, even if you submit a report. There is no make-up session. You are not allowed to change your section.

**Due date:** A week after your lab session, right before the start of the next session. For example, if your lab session started at 2 PM, Jan 1st, 2020, your report is due at 2 PM, Jan 8th, 2020.



**Problem Statement:**  Soft-close drawer slides are used to make sure the drawer is closed softly. One of the advantages of such systems is that no electricity is required to close the drawer. 

The system can be modeled as a single degree of freedom, with a point mass of m \[kg\] (for the drawer), spring stiffness of k \[N/m\], and the damping coefficient of c \[F/m/s\]. Refer to the course material for the EOM of the system. Assume m = 1, k = 3, c = 2.

This lab has parts a, b, c, d, e.


### Part a
*\[a\]\[20%\]* Simulate the response of the system, assuming the drawer is opened by 50 cm and released from rest. Use a closed-form solution to simulate the response of the system. Refer to your textbook, for the formulations. To use the right formulation, you need to know if the system is underdamped, overdamped etc. Follow the steps below.

Deliverables: 
\[a-1\] Determine the roots of the system \[2%\]. What do the roots state about the system? \[1%\]
Hint: open the file drawerlab/mass_spring_damper.py and complete TODO1
By running drawer_a.py, you will see the results.
	
\[a-2\] Once you know the type of the system, in file drawer_a.py, complete TODO2-5.

Reports three graphs, showing the time response of the system, i.e. (i) position vs time \[4%\], (ii) velocity vs time \[4%\], and (iii) acceleration vs time \[4%\]. These graphs are saved on your computer.

\[a-3\] In your lab report, report the code you developed for only TODO1-5 \[5%\]. Attached the full code.


