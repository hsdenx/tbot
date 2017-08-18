Execution Control Commands
--------------------------

source - run script from memory
...............................

tbot_ref:help_source_tb_con_1_1.txt

With the :redtext:`source` command you can run "shell" scripts under U-Boot: You create a U-Boot script image by simply writing the commands you want to run into a text file; then you will have to use the :redtext:`mkimage` tool to convert this text file into a U-Boot image (using the image type script).

This image can be loaded like any other image file, and with :redtext:`source` you can run the commands in such an image. For instance, the following text file: 

tbot_ref:cat_source_example.txt_tb_ctrl_1_1.txt

can be converted into a U-Boot script image using the :redtext:`mkimage` command like this: 

tbot_ref:source_mkimage_tb_ctrl_1_1.txt

Now you can load and execute this script image in U-Boot: 

tbot_ref:tc_ub_tftp_file.py_tb_con_1_1.txt
tbot_ref:source_console_tb_con_1_1.txt

.. raw:: pdf

   PageBreak

bootm - boot application image from memory
..........................................

tbot_ref:help_bootm_tb_con_1_1.txt

The :redtext:`bootm` command is used to start operating system images. From the image header it gets information about the type of the operating system, the file compression method used (if any), the load and entry point addresses, etc. The command will then load the image to the required memory address, uncompressing it on the fly if necessary. Depending on the OS it will pass the required boot arguments and start the OS at it's entry point.

The first argument to :redtext:`bootm` is the memory address (in RAM, ROM or flash memory) where the image is stored, followed by optional arguments that depend on the OS.

:redtext:`Linux` requires the flattened device tree blob to be passed at boot time, and :redtext:`bootm` expects its third argument to be the address of the blob in memory. Second argument to :redtext:`bootm` depends on whether an initrd initial ramdisk image is to be used. If the kernel should be booted without the initial ramdisk, the second argument should be given as "-", otherwise it is interpreted as the start address of initrd (in RAM, ROM or flash memory).

To boot a Linux kernel image without a initrd ramdisk image, the following command can be used:

::

  => bootm ${kernel_addr} - ${fdt_addr}

If a ramdisk image shall be used, you can type: 

::

  => bootm ${kernel_addr} ${ramdisk_addr} ${fdt_addr}

Both examples of course imply that the variables used are set to correct addresses for a kernel, fdt blob and a initrd ramdisk image.

.. image:: ./images/Warning-icon.png

When booting images that have been loaded to RAM (for instance using TFTP download) you have to be careful that the locations where the (compressed) images were stored do not overlap with the memory needed to load the uncompressed kernel. For instance, if you load a ramdisk image at a location in low memory, it may be overwritten when the Linux kernel gets loaded. This will cause undefined system crashes. 

.. raw:: pdf

   PageBreak

go - start application at address 'addr'
........................................

tbot_ref:help_go_tb_con_1_1.txt

U-Boot has support for so-called standalone applications. These are programs that do not require the complex environment of an operating system to run. Instead they can be loaded and executed by U-Boot directly, utilizing U-Boot's service functions like console I/O or malloc() and free().

This can be used to dynamically load and run special extensions to U-Boot like special hardware test routines or bootstrap code to load an OS image from some filesystem.

The :redtext:`go` command is used to start such standalone applications. The optional arguments are passed to the application without modification.

TODO
For more information see 5.12. U-Boot Standalone Applications. 

