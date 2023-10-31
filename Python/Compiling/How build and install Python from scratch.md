# How to build and install Python from scratch

1. Download your preferred version of Python [here](https://www.python.org/downloads/) or in CPython's GitHub repository [here](https://github.com/python/cpython/tags)
    ```bash
    wget https://www.python.org/ftp/python/3.8.18/Python-3.8.18.tar.xz
    ```

2. Extract downloaded Python version
    ```bash
    tar -xf *.tar.xz
    cd Python-*
    ```
    This will extract the folder `Python-3.8.18` and change the current working directory.

3. Configure before compiling and installing
    ```bash
    ./configure --enable-shared --enable-optimizations --with-lto
    ```
      
    `--enable-shared` - adding this will ensure that shared libraries (i.e., mod_wsgi) are built for Python

    `--enable-optimizations` - enable Profile Guided Optimization (PGO) using PROFILE_TASK (disabled by default).

    `--with-lto` - enable Link Time Optimization (LTO) in any build (disabled by default).

    It took my laptop **2:38 minutes** to complete.

4. Compile using `make` with parallel compilation of `j4`
    ```bash
    make -j4
    ```
    Compile time took **12:54 minutes** on my laptop.

5. Install compiled files to your system
    ```bash
    sudo make install       # upgrade your current installed Python version
    ```
    or
    ```bash
    sudo make altinstall    # install a separate versions of Python
    ```

6. Check and run your freshly upgraded version of Python. Enjoy!
    ```bash
    $ python3
    Python 3.8.18 (default, Oct 30 2023, 13:49:50)
    [GCC 9.4.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```

## Resources
- [Build Instructions](https://github.com/python/cpython#build-instructions)
- [Installing multiple versions](https://github.com/python/cpython#installing-multiple-versions)
