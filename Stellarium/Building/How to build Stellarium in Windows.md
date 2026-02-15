# How to build Stellarium in Windows

### Prerequisites
- Visual Studio 2022
- CMake
- Qt Framework
    - Qt Positioning
    - Qt Serial Port
- Git for Windows

### Steps

#### Visual Studio 2022

1. Clone repository

    ```
    git clone https://github.com/Stellarium/stellarium.git
    cd stellarium
    ```

2. Create `CMakePresets.json` file with the following content:

    ```json
    {
        "version": 3,
        "cmakeMinimumRequired": {
            "major": 3,
            "minor": 21,
            "patch": 0
        },
        "configurePresets": [
            {
            "name": "vs2022-multi-config",
            "displayName": "Stellarium (VS2022 Multi-Config)",
            "description": "Unified build tree for Debug, Release, and RelWithDebInfo using Visual Studio 2022",
            "generator": "Visual Studio 17 2022",
            "architecture": {
                "value": "x64"
            },
            "binaryDir": "${sourceDir}/build",
            "cacheVariables": {
                "CMAKE_CONFIGURATION_TYPES": "Debug;Release;RelWithDebInfo",
                "CMAKE_BUILD_TYPE": "Debug",
                "CMAKE_SUPPRESS_DEVELOPER_WARNINGS": "1",
                "CMAKE_PREFIX_PATH": "C:/Qt/6.10.2/msvc2022_64;C:/Dev/Libs/exiv2-0.28.7/lib/cmake/exiv2",
                "QT_QMAKE_EXECUTABLE": "C:/Qt/6.10.2/msvc2022_64/bin/qmake.exe",
                "ENABLE_SCRIPTING": "ON",
                "ENABLE_GPS": "ON",
                "ENABLE_TESTING": "ON",
                "ENABLE_NLS": "ON",
                "ENABLE_SPOUT":  "OFF",
                "USE_PLUGIN_SKYCULTUREMAKER": "OFF",
                "SCM_SHOULD_ENABLE_CONVERTER": "TRUE",
                "GETTEXTPO_LIBRARY": "C:/Dev/Libs/gettextpo/lib/libgettextpo.lib",
                "GETTEXTPO_INCLUDE_DIR": "C:/Dev/Libs/gettextpo/include",
                "LIBTIDY_LIBRARY": "C:/Dev/Libs/libtidy/lib/libtidy.lib",
                "LIBTIDY_INCLUDE_DIR": "C:/Dev/Libs/libtidy/include",
                "EXIV2_LIBRARY": "C:/Dev/Libs/exiv2-0.28.7/lib/exiv2.lib",
                "EXIV2_INCLUDE_DIR": "C:/Dev/Libs/exiv2-0.28.7/include",
                "exiv2_DIR": "C:/Dev/Libs/exiv2-0.28.7/lib/cmake/exiv2",
                "Qt6LinguistTools_DIR": "C:/Qt/6.7.3/msvc2022_64/lib/cmake/Qt6LinguistTools"
            }
            }
        ],
        "buildPresets": [
            {
            "name": "Debug",
            "configurePreset": "vs2022-multi-config",
            "configuration": "Debug"
            },
            {
            "name": "Release",
            "configurePreset": "vs2022-multi-config",
            "configuration": "Release"
            },
            {
            "name": "RelWithDebInfo",
            "configurePreset": "vs2022-multi-config",
            "configuration": "RelWithDebInfo"
            }
        ]
        }
    ```

2. Open stellarium folder in Visual Studio

    This will automatically run CMake. You should see _CMake generation finished_ once it completes.

3. Build the solution. Go to **Build > Build All**

    Configuration should be in **Debug**.

    If the **Debug** build was successful you should see the executable `stellarium.exe` generated in the sub-directory `<stel_dir>\build\src\Debug`.

4. Press `F5` to start debugging

### References
- [Building Stellarium](https://github.com/Stellarium/stellarium/blob/master/BUILDING.md)