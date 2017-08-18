U-Boot
######

Current Versions
================

Das U-Boot (or just "U-Boot" for short) is Open Source Firmware for Embedded Power Architecture®, ARM, MIPS, x86 and other processors. The U-Boot project is hosted by DENX, where you can also find the project home page: http://www.denx.de/wiki/U-Boot/

The current version of the U-Boot source code can be retrieved from the DENX "git" repository.

You can browse the "git" repositories at http://git.denx.de/

The trees can be accessed through the git, HTTP, and rsync protocols. For example you can use one of the following commands to create a local clone of one of the source trees:

::

  git clone git://git.denx.de/u-boot.git u-boot/
  git clone http://git.denx.de/u-boot.git u-boot/
  git clone rsync://git.denx.de/u-boot.git u-boot/

For details please see here.

Official releases of U-Boot are also available through FTP. Compressed tar archives can downloaded from the directory ftp://ftp.denx.de/pub/u-boot/. 

U-Boot Command Line Interface
=============================

The following section describes the most important commands available in U-Boot. Please note that U-Boot is highly configurable, so not all of these commands may be available in the configuration of U-Boot installed on your hardware, or additional commands may exist. You can use the help command to print a list of all available commands for your configuration.

For most commands, you do not need to type in the full command name; instead it is sufficient to type a few characters. For instance, help can be abbreviated as h.

.. image:: ./images/Warning-icon.png

The behaviour of some commands depends on the configuration of U-Boot and on the definition of some variables in your U-Boot environment.

Almost all U-Boot commands expect numbers to be entered in hexadecimal input format. (Exception: for historical reasons, the sleep command takes its argument in decimal input format.)

Be careful not to use edit keys besides 'Backspace', as hidden characters in things like environment variables can be very difficult to find. 

.. raw:: pdf

   PageBreak

Information Commands
--------------------

bdinfo - print Board Info structure
...................................


::

  => help bdinfo
  bdinfo - print Board Info structure
  
  Usage:
  bdinfo 
  => 

The :redtext:`bdinfo` command (:redtext:`bdi`) prints the information that U-Boot passes about the board such as memory addresses and sizes, clock frequencies, MAC address, etc. This information is mainly needed to be passed to the Linux kernel. 



::

  => bdi
  arch_number = 0x00000E05
  boot_params = 0x80000100
  DRAM bank   = 0x00000000
  -> start    = 0x80000000
  -> size     = 0x20000000
  baudrate    = 115200 bps
  TLB addr    = 0x9FFF0000
  relocaddr   = 0x9FF4F000
  reloc off   = 0x1F74F000
  irq_sp      = 0x9DF264E0
  sp start    = 0x9DF264D0
  Early malloc usage: 178 / 400
  fdt_blob = 9df264f8
  => 

.. raw:: pdf

   PageBreak

coninfo - print console devices and informations
................................................


::

  => help conin
  coninfo - print console devices and information
  
  Usage:
  coninfo 
  => 

The :redtext:`coninfo` command (:redtext:`conin`) displays information about the available console I/O devices. 


::

  => conin
  List of available devices:
  serial@44e09000 00000003 IO stdin stdout stderr 
  serial   00000003 IO 
  => 

The output contains the device name, flags, and the current usage. For example, the output

::

  serial@44e09000 00000003 IO stdin stdout stderr 
  
means that the serial device provides input (flag 'I') and output (flag 'O') functionality and is currently assigned to the 3 standard I/O streams stdin, stdout and stderr. 

.. raw:: pdf

   PageBreak

.. include:: u-boot-flinfo.rst

.. raw:: pdf

   PageBreak

.. include:: u-boot-help.rst

.. raw:: pdf

   PageBreak

.. include:: u-boot-memory.rst


.. raw:: pdf

   PageBreak

.. include:: u-boot-mw.rst

.. raw:: pdf

   PageBreak

.. include:: u-boot-nm.rst

.. raw:: pdf

   PageBreak

.. include:: u-boot-loop.rst

.. raw:: pdf

   PageBreak

.. include:: u-boot-execution.rst

