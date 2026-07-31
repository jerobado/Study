# How to build Mixxx in Windows

### Prerequisites 
- Visual Studio 2022
    - Desktop development with C++ should be installed
- Git for Windows

### Steps

1. Clone repository

    ```
    git clone https://github.com/mixxxdj/mixxx.git
    cd mixxx
    ```

2. Download pre-built Mixxx dependencies automatically

    ```
    ./tools/windows_buildenv.bat
    ```

    This script will download the appropriate file from Mixxx servers, and autogenerate a `CMakeSettings.json` file which can later be used to build Mixxx with the default settings from Visual Studio.

3. Open project in Visual Studio
    - in the configuration toolbar select **x64__portable**

4. In the menu bar, go to **Build > Build All** option
    - this will build the solution

## References
- [Compiling on Windows](https://github.com/mixxxdj/mixxx/wiki/Compiling%20on%20Windows)