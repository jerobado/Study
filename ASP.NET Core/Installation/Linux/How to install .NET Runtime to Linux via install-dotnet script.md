How to install .NET Runtime in Linux via `install-dotnet` script
---

There are three [(3) ways](https://docs.microsoft.com/en-us/dotnet/core/install/linux-ubuntu#unable-to-find-package) to install the .NET Runtime in Ubuntu. This tutorial will teach you how to install the .NET Runtime via `install-dotnet` script.

1. Download the script from https://dot.net/v1/dotnet-install.sh

2. Convert the script as an executable
    ```bash
    sudo chmod +x ./dotnet-install.sh
    ```

3. Run the following command to install **only** the .NET Runtime:
    ```bash
    ./dotnet-install.sh -c Current --runtime aspnetcore
    ```

4. Set environment variables system-wide
    ```bash
    # ~/.bashrc
    export DOTNET_ROOT=$HOME/.dotnet
    export PATH=$PATH:$HOME/.dotnet:$HOME/.dotnet/tools

    # run source ~/.bashrc to update your shell
    ```

5. Run the following command if working:
    ```bash
    dotnet --info  
    ```

6. Test your application if working:
    ```
    dotnet <appname>.dll
    ```

Resources
---
- [Install the .NET SDK or the .NET Runtime on Ubuntu](https://docs.microsoft.com/en-us/dotnet/core/install/linux-ubuntu)
- [Scripted install](https://docs.microsoft.com/en-us/dotnet/core/install/linux-scripted-manual#scripted-install)
- [dotnet-install scripts reference](https://docs.microsoft.com/en-us/dotnet/core/tools/dotnet-install-script)



