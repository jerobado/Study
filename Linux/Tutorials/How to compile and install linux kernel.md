# How to compile and install linux kernel

Requirements
- Debian
- Linux mainline or stable repository


## Steps

1. Install build tools and dependencies

    ```
    sudo apt update
    sudo apt install build-essential vim git cscope libncurses-dev libssl-dev bison flex libelf-dev bc binutils dwarves openssl pahole perl-base
    ```

2. Clone mainline repository

    ```
    git clone git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
    ```

    As of this writing, the size of the repository is 3.70 GiB. This will take a while depending on your download speed.

3. Copy your current's OS config from `/boot` to `.config`

    ```
    cp /boot/config-$(uname -r) .config
    ```

4. Setup build configuration

    There different ways to setup your .config:

    Reads your existing `.config` and prompts interactively for any new options introduced in the kernel version.
    ```
    make oldconfig
    ```

    Reads your existing `.config` and applies default answers automatically for new options. No prompts.
    ```
    make olddefconfig
    ```

    Scans your currently loaded modules (lsmod) and generates a `.config` that includes only those drivers. The yes "" part auto-answers prompts.
    ```
    yes "" | make localmodconfig
    ```

5. Compile 

    ```
    make -j $(nproc)
    ```

    It took 32 minutes to compile on a 16-core Intel Core Ultra 7 255H processor

6. Install

    ```
    sudo make modules_install install
    ```

7. Verify installed locations

    ```
    ls /lib/modules/$(make kernelrelease)
    ls /boot/
    ```

7. Reboot your system

8. Check linux version

    ```
    uname -r
    ```

## Troubleshooting

### error: bad shim signature
- SecureBoot is preventing the custom built kernel to boot
- You need to disable it by using `mokutil` tool

```
sudo mokutil --disable-validation
```

### Can't detect Wi-Fi adapter after booting?

- Check logs 
    ```bash
    # check kernel logs
    sudo dmesg | grep iwlwifi
    
    # check current boot logs
    journalctl -b
    ```

    `iwlwifi` is the kernel driver for Intel wireless network cards

- Cause: the linux kernel version that I compiled is looking for a specific/latest firmware version of my wifi device

    ```
    [    9.816308] iwlwifi 0000:00:14.3: no suitable firmware found!
    [    9.816312] iwlwifi 0000:00:14.3: iwlwifi-bz-b0-gf-a0-100 is required
    [    9.816317] iwlwifi 0000:00:14.3: check git://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git
    ```


- Download the firmware and copy to `/lib/firmware` directory
    ```bash
    wget https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/iwlwifi-bz-b0-gf-a0-100.ucode
    sudo cp iwlwifi-bz-b0-gf-a0-100.ucode /lib/firmware/
    ```
- Update `/boot/initrd-img-<your kernel version>` so that it will include your downloaded firmware when you boot

    ```bash
    sudo update-initramfs -u -k <your kernel version>
    ```
- Reboot to your compiled kernel version

