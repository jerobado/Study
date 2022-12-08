# How to compile/build Python from scratch

1. Download your preferred version of Python [here](https://www.python.org/downloads/) or in CPython's GitHub repository [here](https://github.com/python/cpython/tags)
    ```bash
    wget https://github.com/python/cpython/archive/refs/tags/v3.8.16.tar.gz
    ```

2. Extract downloaded Python version
    ```bash
    tar -xf *.tar.gz
    cd cpython-*
    ```
    This will extract the folder `cpython-3.8.16` to the current working directory.

3. Configure before compiling and installing
    ```bash
    ./configure --enable-optimizations --with-lto
    ```
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
    Python 3.8.16 (default, Dec  8 2022, 20:26:29)
    [GCC 10.2.1 20210110] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```

## Resources
- [Build Instructions](https://github.com/python/cpython#build-instructions)
- [Installing multiple versions](https://github.com/python/cpython#installing-multiple-versions)
