# How to build and install OpenSSL

### Prerequisites
- `perl` code modules
- `libtext-template-perl` library (for building)

### Download and Building

1. Download the source code here https://github.com/openssl/openssl/releases
    ```
    wget https://github.com/openssl/openssl/releases/download/openssl-3.2.1/openssl-3.2.1.tar.gz
    ```

2. Extract `openssl-3.2.1.tar.gz` and navigate to `openssl-3.2.1` directory
    ```
    tar -xf openssl-3.2.1.tar.gz
    cd openssl-3.2.1
    ```

3. Run `config`
    ```
    $ ./config --prefix=/opt/openssl-3.2.1 --openssldir=/opt/openssl/3.2.1
    ```

4. Run `make`
    ```
    $ make -j4
    ```

5. Run tests
    ```
    $ make test
    ```

6. Install
    ```
    $ sudo make install
    ```

7. Run `ldconfig`
    ```
    $ sudo ldconfig /usr/local/lib64/
    ```

8. Run and check installed version
    ```
    $ openssl version
    ```


# References
- [Build and Install](https://github.com/openssl/openssl/blob/master/INSTALL.md)
- [How to Install OpenSSL on Debian 12](https://itslinuxfoss.com/install-openssl-debian-12/)
- [Compilation and Installation](https://wiki.openssl.org/index.php/Compilation_and_Installation)