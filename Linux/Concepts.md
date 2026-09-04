# Concepts

**kernel module**
- is a piece of code that can be dynamically loaded into or removed from the Linux kernel at runtime without system reboot
- `.ko` extension
- extends the functionality of a linux kernel
- can be a software only kernel module 

**driver**
- is a specific type of kernel module that enables the operating system to communicate with physical devices.
- can be written as kernel module

**firmware**
- the software the runs inside the device
- `.ucode` extension

**device**
- the physical device of a computer
- Bluetooth, Wi-fi, keyboard, mouse, etc.

`/lib/modules`
- location of kernel modules

`/lib/firmware`
- location of device firmwares