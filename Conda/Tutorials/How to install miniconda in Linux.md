# How to install miniconda in Linux


### Steps

1. Download installer script

    ```bash
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    ```

2. Run script

    ```
    bash ~/Miniconda3-latest-Linux-x86_64.sh
    ```

3. Follow the guided installation prompts

4. Restart shell

    This will  activate the `base` environment everytime you open a new shell.

    If you want to disable the base environmen, just run the following command:

    ```
    conda config --set auto_activate_base false
    ```

5. Check conda commands

    ```
    conda --version
    conda list
    conda info
    ```

## References
- [Installing Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install#macos-linux-installation)