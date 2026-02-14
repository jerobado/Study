# How to build Blender in Windows

### Prerequisites
- Visual Studio 2022 or later
- Git for Windows
- CMake

### Steps

#### Using the CLI

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

#### Using Visual Studio 2022

1. In the `build_xxx` folder, find and open `Blender.sln`

2. Then in the Solution Explorer, find `CMakePredefinedTargets` > `INSTALL` target.

3. Right-click `INSTALL` target and select **Build**

    This will build and install Blender in the output folder. This will take some few hours to complete depending on your machine.

Once the install target has been built once, you can now work with the code as usual in Visual Studio. **Build** > **Build Solution** can be used to rebuild after making changes.


## References
- [Building Blender on Windows](https://developer.blender.org/docs/handbook/building_blender/windows/)
- [Visual Studio](https://developer.blender.org/docs/handbook/development_environments/visual_studio/)