Sudoers file
---

The sudoers file which is located in `/etc/sudoers` allows you to manage the use of `sudo` command for all your users.

How-Tos
---

### Allowing a user to execute a command without sudo password

1. Create a sudoers file for that user

    ```
    sudo visudo -f /etc/sudoers.d/<filename>
    ```

2. In the created sudoers file, add the following:
    
    ```
    # Syntax: <user> <hostname> = <Tag_Spec> <command list>
    jerobado computer-name = NOPASSWD: /usr/bin/apt
    ```

3. Test `apt` command if it will no longer ask for a sudo password

    ```
    apt update
    ```


### Reference(s)
- [Sudoers Manual](https://www.sudo.ws/man/1.8.13/sudoers.man.html)