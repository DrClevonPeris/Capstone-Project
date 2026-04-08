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
**verify the folder or directories using the command**

During the setup of the ArduPilot SITL environment, I encountered several technical issues related to file paths, permissions, and missing dependencies. These errors were important learning points and helped me better understand how the system operates. 
Initially, when attempting to run the simulation using: 

**"./Tools/autotest/sim_vehicle.py --map –console"**

![Ardupilot Directoy missing](./screenshots/Ardupilot_directory_missing_1.png)

**"Sudo chown -R $USER:$USER /home/jena"**

We need to enter our wsl password to finish the installation and to Clone ArduPilot properly, I used this command and successfully done. 

**"Git clone https://github.com/ArduPilot/ardupilot.git"**

![Ardupilot Installed Successfully](./screenshots/Ardupilot_Installed_successfully.png)

------------------------------
![Ardupilot Directory or folder](./screenshots/Ardupilot_Installed_successfully_2.png)

-----------------------------

**Geospy Python error**

After successfully navigating to the correct directory, I attempted to run the simulation again. This time, I encountered a Python error

![Geospy Python error](./screenshots/Geospy_Python_error1.png)

I resolved this issue by installing the required package using these commands **"pip3 install pexpect"** and **"pip3 install geospy"**

![Geospy Installation](./screenshots/geopy_installation.png)

----------------------------------
![subdirectory ArduCopter missing error](./screenshots/ArduoCopter_subdirectory_missing.png)

This error occurred because I executed the simulation command from the wrong directory level. The system could not determine which vehicle type to simulate.

I fixed this issue with the command **"Cd ~/ardupilot/ArduCopter"** And rerunning the command, the simulation started successfully. 

![simulation started successfully](./screenshots/ArduCopter_simulation_started_1.png)

![ArduPilot SITL environment](./screenshots/ArduCopter_simulation_started_2.png)

![ArduPilot SITL environment with console and map](./screenshots/Ardupilot_Map_with_drone_works_1.png)
