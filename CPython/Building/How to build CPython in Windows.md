# How to build CPython in Windows

### Prerequisites
- Visual Studio 2022 or later
- Git for Windows
- Python

### Steps

1. Clone repository.

    ```
    git clone https://github.com/python/cpython.git
    ```

2. Run `build.bat` to build and download dependencies.

    ```
    PCBuild\build.bat -c Debug
    ```

5. Run the Python that you build!

    ```
    PCbuild\amd64\python_d.exe
    ```

After the build completes, open `PCBuild\pcbuild.sln` in your Visual Studio to start developing.

### References
- [Setup and building](https://devguide.python.org/getting-started/setup-building/#windows)