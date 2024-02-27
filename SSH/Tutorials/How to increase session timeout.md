# How to increase session timeout

1. Open `/etc/ssh/sshd_config` file using **vim** editor
    ```bash
    sudo vim /etc/ssh/sshd_config
    ```

2. Find and uncomment the line `ClientAliveInterval` and set time in milliseconds
    ```bash
    ClientAliveInterval 3600
    ```

    This will set the time in **1 hour**.

3. Restart or reload SSH daemon
    ```bash
    sudo systemctl restart sshd
    ```

# References
- [How to Increase SSH Connection Timeout in Linux](https://www.tecmint.com/increase-ssh-connection-timeout/)