# How to install OpenSSL library for MinGW-w64 in MSYS2


### Objective
- You want to download OpenSSL libraries that you can reference to develop your C++ projects
- You want to create C++ executables targeting Windows 

### Requirements
- MSYS2

### Steps

1. Install OpenSSL library built for MinGW-x64 using pacman

    ```
    pacman -S mingw-w64-ucrt-x86_64-openssl 
    ```