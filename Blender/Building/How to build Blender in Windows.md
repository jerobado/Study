# How to build Blender in Windows

### Prerequisites
- Visual Studio 2022 or later
- Git for Windows
- CMake

### Steps

1. Clone repository inside the `blender-git` directory

    ```
    cd C:\blender-git
    git clone https://projects.blender.org/blender/blender.git
    ```

2. Download dependencies

    ```
    ./make.bat update
    ```

3. Compile source code

    ```
    ./make.bat
    ```

    Or for faster build
    ```
    ./make.bat debug developer
    ```


## References
- [Building Blender on Windows](https://developer.blender.org/docs/handbook/building_blender/windows/)
- [Visual Studio](https://developer.blender.org/docs/handbook/development_environments/visual_studio/)