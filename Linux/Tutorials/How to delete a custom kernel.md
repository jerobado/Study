# How to delete a custom kernel

### Objective
- remove custom kernel that you compile

Installed kernel files can be found in the `/boot` and `/lib/modules` directories.

## Steps

1. Check your current installed kernel

    ```
    uname -r
    ```

2. List the files related to the kernel you want to delete in `/boot` directory

    ```
    ls /boot | grep <kernel version>
    ```

3. Delete files

    ```
    sudo rm /boot/config-<version>
    sudo rm /boot/initrd.img-<version>
    sudo rm /boot/System.map-<version>
    sudo rm /boot/vmlinuz-<version>
    ```

4. List the files in `/lib/modules`

    ```
    ls /lib/modules
    ```

5. Delete modules for your kernel

    ```
    sudo rm -rf /lib/modules/<version>
    ```

6. Update GRUB menu entry

    ```
    sudo update-grub
    ```