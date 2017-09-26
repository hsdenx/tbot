U-Boot Environment Variables
----------------------------

The U-Boot environment is a block of memory that is kept on persistent storage and copied to RAM when U-Boot starts. It is used to store environment variables which can be used to configure the system. The environment is protected by a CRC32 checksum.

This section lists the most important environment variables, some of which have a special meaning to U-Boot. You can use these variables to configure the behaviour of U-Boot to your liking.

- :redtext:`autoload`: if set to "no" (or any string beginning with 'n'), the :redtext:`rarpb`, :redtext:`bootp` or :redtext:`dhcp` commands will perform only a configuration lookup from the BOOTP / DHCP server, but not try to load any image using TFTP.

- :redtext:`autostart`: if set to "yes", an image loaded using the :redtext:`rarpb`, :redtext:`bootp`, :redtext:`dhcp`, :redtext:`tftp`, :redtext:`disk`, or :redtext:`docb` commands will be automatically started (by internally calling the :redtext:`bootm` command).

- :redtext:`baudrate`: a decimal number that selects the console baudrate (in bps). Only a predefined list of baudrate settings is available. When you change the baudrate (using the "setenv baudrate ..." command), U-Boot will switch the baudrate of the console terminal and wait for a newline which must be entered with the new speed setting. This is to make sure you can actually type at the new speed. If this fails, you have to reset the board (which will operate at the old speed since you were not able to :redtext:`saveenv` the new settings.) If no "baudrate" variable is defined, the default baudrate of 115200 is used.

- :redtext:`bootargs`: The contents of this variable are passed to the Linux kernel as boot arguments (aka "command line").

- :redtext:`bootcmd`: This variable defines a command string that is automatically executed when the initial countdown is not interrupted. This command is only executed when the variable :redtext:`bootdelay` is also defined!

- :redtext:`bootdelay`: After reset, U-Boot will wait this number of seconds before it executes the contents of the :redtext:`bootcmd` variable. During this time a countdown is printed, which can be interrupted by pressing any key. Set this variable to 0 boot without delay. Be careful: depending on the contents of your bootcmd variable, this can prevent you from entering interactive commands again forever! Set this variable to -1 to disable autoboot.

- :redtext:`bootfile`: name of the default image to load with TFTP

- :redtext:`ethaddr`: Ethernet MAC address for first/only ethernet interface (= eth0 in Linux). This variable can be set only once (usually during manufacturing of the board). U-Boot refuses to delete or overwrite this variable once it has been set.

- :redtext:`eth1addr`: Ethernet MAC address for second ethernet interface (= eth1 in Linux).

- :redtext:`eth2addr`: Ethernet MAC address for third ethernet interface (= eth2 in Linux).

    ...

- :redtext:`initrd_high`: used to restrict positioning of initrd ramdisk images: If this variable is not set, initrd images will be copied to the highest possible address in RAM; this is usually what you want since it allows for maximum initrd size. If for some reason you want to make sure that the initrd image is loaded below the CFG_BOOTMAPSZ limit, you can set this environment variable to a value of "no" or "off" or "0". Alternatively, you can set it to a maximum upper address to use (U-Boot will still check that it does not overwrite the U-Boot stack and data). For instance, when you have a system with 16 MB RAM, and want to reserve 4 MB from use by Linux, you can do this by adding "mem=12M" to the value of the "bootargs" variable. However, now you must make sure that the initrd image is placed in the first 12 MB as well - this can be done with

::

  => setenv initrd_high 00c00000
     

Setting initrd_high to the highest possible address in your system (0xFFFFFFFF) prevents U-Boot from copying the image to RAM at all. This allows for faster boot times, but requires a Linux kernel with zero-copy ramdisk support.

- :redtext:`ipaddr`: IP address; needed for tftp command

- :redtext:`loadaddr`: Default load address for commands like tftp or loads.

- :redtext:`loads_echo`: If set to 1, all characters received during a serial download (using the loads command) are echoed back. This might be needed by some terminal emulations (like cu), but may as well just take time on others.

- :redtext:`mtdparts`: This variable (usually defined using the mtdparts command) allows to share a common MTD partition scheme between U-Boot and the Linux kernel.

- :redtext:`pram`: If the "Protected RAM" feature is enabled in your board's configuration, this variable can be defined to enable the reservation of such "protected RAM", i. e. RAM which is not overwritten by U-Boot. Define this variable to hold the number of kB you want to reserve for pRAM. Note that the board info structure will still show the full amount of RAM. If pRAM is reserved, a new environment variable "mem" will automatically be defined to hold the amount of remaining RAM in a form that can be passed as boot argument to Linux, for instance like that:

::

  => setenv bootargs ${bootargs} mem=\${mem}
  => saveenv
     

This way you can tell Linux not to use this memory, either, which results in a memory region that will not be affected by reboots.

- :redtext:`serverip`: TFTP server IP address; needed for :redtext:`tftp` command.

- :redtext:`serial#`: contains hardware identification information such as type string and/or serial number. This variable can be set only once (usually during manufacturing of the board). U-Boot refuses to delete or overwrite this variable once it hass been set.

- :redtext:`silent`: If the configuration option :redtext:`CONFIG_SILENT_CONSOLE` has been enabled for your board, setting this variable to any value will suppress all console messages. Please see doc/README.silent for details.

- :redtext:`verify`: If set to n or no disables the checksum calculation over the complete image in the bootm command to trade speed for safety in the boot process. Note that the header checksum is still verified.

The following environment variables may be used and automatically updated by the network boot commands (bootp, dhcp, or tftp), depending the information provided by your boot server:

- :redtext:`bootfile`: see above
- :redtext:`dnsip`: IP address of your Domain Name Server
- :redtext:`gatewayip`: IP address of the Gateway (Router) to use
- :redtext:`hostname`: Target hostname
- :redtext:`ipaddr`: see above
- :redtext:`netmask`: Subnet Mask
- :redtext:`rootpath`: Pathname of the root filesystem on the NFS server
- :redtext:`serverip`: see above
- :redtext:`filesize`: Size (as hex number in bytes) of the file downloaded using the last bootp, dhcp, or tftp command.

