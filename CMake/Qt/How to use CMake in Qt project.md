# How to use CMake in Qt project

### Objective
- use CMake as build system in my Qt project
- use Visual Studio 2022 to build and run my Qt project

### Steps

1. Create `CMakeLists.txt` in the root directory of your project with the followin content:

    ```cmake
    cmake_minimum_required(VERSION 3.16)

    project(MinimalCMake VERSION 0.1 LANGUAGES CXX)

    find_package(Qt6 REQUIRED COMPONENTS Core Widgets Gui)

    qt_standard_project_setup()

    add_executable(MinimalCMake
        main.cpp
    )

    target_link_libraries(MinimalCMake
        PRIVATE 
            Qt6::Core
            Qt6::Widgets
            Qt6::Gui
    )

    set(CMAKE_CXX_STANDARD 17)
    set(CMAKE_CXX_STANDARD_REQUIRED ON)
    set(CMAKE_CXX_EXTENSIONS OFF)

    if (MSVC)
        target_compile_options(MinimalCMake PRIVATE /Zc:__cplusplus /permissive-)
    endif()
    ```

2. Create a generator for Visual Studio 2022

    ```powershell
    cmake -S . -B build_msvc -G "Visual Studio 17 2022" -DCMAKE_PREFIX_PATH="path/to/qt/compiler"
    ```

3. Build

    ```powershell
    cmake --build build_msvc
    ```

This will create a solution `<your-project>.sln` file for your Qt project. Open this in Visual Studio 2022 and build from there.