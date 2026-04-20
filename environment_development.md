**Progress on Building AirSim Environment (Windows)**

![AirSim simulation environment on a Windows system](./screenshots/S1_Unreal_engine.png)

During this phase of the project, I focused on setting up and building the AirSim simulation environment on a Windows system.

-----------------------

**Step1:** During this phase of the project, I focused on setting up and building the AirSim simulation environment on a Windows system. I began by cloning the AirSim repository using the Visual Studio Developer Command Prompt, which ensured that all required environment variables were correctly configured. The cloning process completed successfully, confirming that the repository and its dependencies were properly downloaded.

![Visual Studio Developer Command Prompt](./screenshots/S1_Visual_Studio_developer_command_promo_t_for_airsim_clone.png)

-------------------------

**Step2** **During this phase I got an error "AirSim is trying to build with Platform Toolset v143, but MSBuild still cannot find that toolset on your machine"**


The v143 C++ build tools are not actually installed Visual Studio can be installed, but the exact C++ toolset AirSim needs may still be missing. Microsoft’s MSB8020 docs say this error appears when the required platform toolset is not installed or its folder does not exist.

![MSVC v143 - VS 2022 C++ x64/x86 build tools | Windows SDK ](./screenshots/msvc_missing_error.png)

**Step3 Necessary Tools installation on Visual Studio under Desktop development with C++**

![Required Tools](./screenshots/visualstudio_required_tools.png)
