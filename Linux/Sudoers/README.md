# Sudoers file

The sudoers file which is located in `/etc/sudoers` allows you to manage the use of `sudo` command for all your users.

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


### Check syntax if correct

```
sudo visudo -c
```

# Reference(s)
- [How To Edit the Sudoers File](https://www.digitalocean.com/community/tutorials/how-to-edit-the-sudoers-file)
- [Sudoers Manual](https://www.sudo.ws/man/1.8.13/sudoers.man.html)