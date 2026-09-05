# How to create a kernel moduel

Objective
- create a kernel module
- load and unload module

## Steps

1. Create the source code

    ```c
    #include <linux/init.h>
    #include <linux/kernel.h>
    #include <linux/module.h>

    MODULE_AUTHOR("Jero");
    MODULE_DESCRIPTION("My first kernel module");
    MODULE_LICENSE("GPL");

    static int __init jero_init(void)
    {
        printk(KERN_INFO "Ola! Linux kernel!\n");
        return 0;
    }

    static void __exit jero_exit(void)
    {
        printk(KERN_INFO "Exiting jero module\n");
    }

    module_init(jero_init);
    module_exit(jero_exit);
    ```

2. Create a `Makefile`

    ```make
    obj-m += jero.o

    all:
        make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

    clean:
        make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
    ```

3. Build the module using `make`

    ```
    make
    ```

4. Load the module

    ```
    sudo insmod jero.ko
    ```

5. Unload the module

    ```
    sudo rmmod jero
    ```

6. Check kernel logs

    ```
    sudo dmesg | tail
    ```

    Expected output

    ```
    [ 4088.594160] jero: loading out-of-tree module taints kernel.
    [ 4088.594167] jero: module verification failed: signature and/or required key missing - tainting kernel
    [ 4088.602007] Ola! Linux kernel!
    [ 4133.971385] Exiting jero module
    ```
