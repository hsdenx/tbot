Miscellaneous Commands
----------------------

echo - echo args to console
...........................


::

  => help echo
  echo - echo args to console
  
  Usage:
  echo [args..]
      - echo args to console; \c suppresses newline
  => 

The :redtext:`echo` command echoes the arguments to the console:


::

  => echo The quick brown fox jumped over the lazy dog.
  The quick brown fox jumped over the lazy dog.
  => 

reset - Perform RESET of the CPU
................................


::

  => help reset
  reset - Perform RESET of the CPU
  
  Usage:
  reset 
  => 

The :redtext:`reset` command reboots the system.


::

  => reset

  resetting ...
  
  U-Boot SPL 2017.09-00396-g6ca43a5 (Sep 30 2017 - 07:16:03)
  Trying to boot from MMC2
  *** Warning - bad CRC, using default environment
  
  reading u-boot.img
  reading u-boot.img
  reading u-boot.img
  reading u-boot.img
  
  
  U-Boot 2017.09-00396-g6ca43a5 (Sep 30 2017 - 07:16:03 +0200)
  
  CPU  : AM335X-GP rev 2.1
  Model: TI AM335x BeagleBone Black
  DRAM:  512 MiB
  NAND:  0 MiB
  MMC:   OMAP SD/MMC: 0, OMAP SD/MMC: 1
  *** Warning - bad CRC, using default environment
  
  ERROR: No USB device found
  
  at drivers/usb/gadget/ether.c:2709/usb_ether_init()
  <ethaddr> not set. Validating first E-fuse MAC
  Net:   CACHE: Misaligned operation at range [9df2f580, 9df2f624]
  eth0: ethernet@4a100000
  Hit any key to stop autoboot:  2  0
  => 

sleep - delay execution for some time
.....................................


::

  => help sleep
  sleep - delay execution for some time
  
  Usage:
  sleep N
      - delay execution for N seconds (N is _decimal_ and can be
        fractional)
  => 

The :redtext:`sleep` command pauses execution for the number of seconds given as the argument: 


::

  => sleep 5
  => 

version - print monitor version
...............................


::

  => help version
  version - print monitor, compiler and linker version
  
  Usage:
  version 
  => 

You can print the version and build date of the U-Boot image running on your system using the :redtext:`version` command (short: :redtext:`vers`): 


::

  => version
  U-Boot 2017.09-00396-g6ca43a5 (Sep 30 2017 - 07:16:03 +0200)
  
  arm-unknown-linux-gnueabi-gcc (GCC) 4.9.0
  GNU ld (GNU Binutils) 2.24
  => 

? - alias for 'help'
....................

You can use :redtext:`?` as a short form for the :redtext:`help` command (see description above). 
