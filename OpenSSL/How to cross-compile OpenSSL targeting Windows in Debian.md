# How to cross-compile OpenSSL targeting Windows in Debian

### Prerequisites
- mingw-w64
- make

### Steps

1. Download source code

2. Extract 

    ```
    tar -xvf openssl-3.6.2.tar.gz
    cd openssl-3.6.2
    ```

3. Configure

    ```
    ./Configure mingw64 --cross-compile-prefix=x86_64-w64-mingw32- --prefix=/opt/openssl-windows-x64
    ```

4. Compile using make

    ```
    make
    ```

5. Install to directory

    ```
    make install
    ```

    This will be installed in directory specified in the `--prefix` option.