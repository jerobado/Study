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

3. Run `Configure`
    ```
    $ ./Configure --prefix=/opt/openssl --openssldir=/usr/local/ssl
    ```

4. Run `make`
    ```
    $ make -j4
    ```

5. Install
    ```
    $ sudo make install
    ```

6. Run `ldconfig`
    ```
    $ sudo ldconfig /usr/local/lib64/
    ```

7. Run and check installed version
    ```
    $ openssl version
    ```


# References
- [Build and Install](https://github.com/openssl/openssl/blob/master/INSTALL.md)
- [How to Install OpenSSL on Debian 12](https://itslinuxfoss.com/install-openssl-debian-12/)