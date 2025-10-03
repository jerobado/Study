# How to upgrade Debian to latest version

#### Before doing anything
- backup your server
- clone your instance (Linode)

### Steps
1. Install availalbe updates in your **current** Debian system

    ```
    sudo apt update
    sudo apt upgrade
    ```

2. Stop currently running services if you have one running like PostgreSQL

    ```
    sudo systemctl stop postgresql
    ```

3. Edit `sources.list` to change current distro codename to new codename

    ```
    deb http://deb.debian.org/debian trixie main
    deb-src http://deb.debian.org/debian trixie main

    deb http://deb.debian.org/debian trixie-updates main
    deb-src http://deb.debian.org/debian trixie-updates main

    deb http://security.debian.org/debian-security trixie-security main
    deb-src http://security.debian.org/debian-security trixie-security main

    deb http://ftp.debian.org/debian trixie-backports main
    deb-src http://ftp.debian.org/debian trixie-backports main
    ```

    In this file, `trixie` is the codename of the latest Debian version we want to have.

4. Update and remove old packages

    ```
    sudo apt update
    sudo apt-get clean
    ```

5. Upgrade packages

    ```
    sudo apt upgrade
    ```

6. Do main upgrade

    ```
    sudo apt dist-upgrade
    ```

7. Remove old and unused packages

    ```
    sudo apt-get autoremove
    ```

##  References
- [Upgrade Debian to the Newest Release](https://www.linode.com/docs/guides/upgrade-debian-to-the-newest-release/)
- [Clone a Compute Instance](https://techdocs.akamai.com/cloud-computing/docs/clone-a-compute-instance)