# How to build Mixxx in Linux

### Steps
1. Clone repository

    ```
    git clone https://github.com/mixxxdj/mixxx.git
    ```

2. Install dependencies

    ```
    tools/debian_buildenv.sh setup
    ```

3. Configure 

    ```
    cmake -DCMAKE_INSTALL_PREFIX=/usr/local -S ~/mixxx -B ~/mixxx/build
    ```

4. Build mixxx binary

    ```
    cmake --build build --target mixxx --parallel `nproc`
    ```

5. Run mixxx

    ```
    build/mixxx
    ```

## References
- [Compiling On Linux](https://github.com/mixxxdj/mixxx/wiki/Compiling%20on%20Linux)