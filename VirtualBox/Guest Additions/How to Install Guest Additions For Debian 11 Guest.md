# How to Install Guest Additions For Debian 11 Guest

1. Update the package repository and install dependencies

    ```bash
    sudo apt update
    sudo apt install build-essential dkms linux-headers-$(uname -r)
    ```
2. Insert Guest Addition CD Image

    ```
    Devices > Insert Guest Additions CD Image...
    ```

3. Mount the Guest Addition ISO Image

    ```
    sudo mkdir -p /mnt/cdrom
    ```

4. Mount the optical disk from `/dev/` to `/mnt` directory

    ```
    sudo mount /dev/cdrom /mnt/cdrom
    ```

5. Navigate to the `/mnt/cdrom` directory

    ```
    cd /mnt/cdrom
    ```

6. Execute the **VBOxLinuxAdditions.run** script

    ```
    sudo sh ./VBoxLinuxAdditions.run --nox11
    ```

7. Reboot the system

    ```
    sudo shutdown -r now
    ```

References:
- https://kifarunix.com/install-virtualbox-guest-additions-on-debian-11/
- https://itslinuxfoss.com/virtualbox-guest-additions-debian-11/
- https://www.virtualbox.org/manual/ch04.html