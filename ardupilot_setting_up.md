I have done the process of setting up the Ardupilot, AirSim, and simulation as well. I've uploaded the screenshots too.


**https://learn.microsoft.com/en-us/windows/wsl/install**


**Step 1:**
![WSL Setup on Windows Step 1](./screenshots/Step1_Setting%20up%20WSL.png)


-----------------------
**Step 2**
![WSL Setup on Windows Step 2](./screenshots/Step2_Setting%20up%20WSL.png)

-----------------------

**Step 3**
![WSL Setup on Windows Step 3](./screenshots/Step3_Setting%20up%20WSL.png)

------------------------
**Step 4 Installing Ardupilot extension for VS Code.**

![WSL Setup on Windows Step 4](./screenshots/Step4_Installing%20aardupilot_devnv%20in%20WSL.png)

------------------------
**Step 5**
![WSL Setup on Windows Step 5](./screenshots/Step5_vs%20code%20connected%20with%20WSL.png)

---------------------------
**verify the folder and directories using the command**

During the setup of the ArduPilot SITL environment, I encountered several technical issues related to file paths, permissions, and missing dependencies. These errors were important learning points and helped me better understand how the system operates. 
Initially, when attempting to run the simulation using: 

"./Tools/autotest/sim_vehicle.py --map –console"

![Ardupilot Directoy missing](./screenshots/Ardupilot_directory_missing_1.png)
