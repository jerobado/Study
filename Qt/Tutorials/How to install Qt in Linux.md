# How to install Qt in Linux

### Objective
- install Qt in Linux like Debian

## Steps

1. Install Requirements

    ```
    sudo apt install \
            libfontconfig1-dev \
            libfreetype-dev \
            libgtk-3-dev \
            libx11-dev \
            libx11-xcb-dev \
            libxcb-cursor-dev \
            libxcb-glx0-dev \
            libxcb-icccm4-dev \
            libxcb-image0-dev \
            libxcb-keysyms1-dev \
            libxcb-randr0-dev \
            libxcb-render-util0-dev \
            libxcb-shape0-dev \
            libxcb-shm0-dev \
            libxcb-sync-dev \
            libxcb-util-dev \
            libxcb-xfixes0-dev \
            libxcb-xkb-dev \
            libxcb1-dev \
            libxext-dev \
            libxfixes-dev \
            libxi-dev \
            libxkbcommon-dev \
            libxkbcommon-x11-dev \
            libxrender-dev
    ```

2. Install compiler and OpenGL and GLX header files and libraries

    ```
    sudo apt install build-essential libgl1-mesa-dev
    ```

3. Check version

    ```
    $ qmake6 --version
    QMake version 3.1
    Using Qt version 6.8.2 in /usr/lib/x86_64-linux-gnu
    ```


## References
- [Qt for Linux](https://doc.qt.io/qt-6/linux.html)