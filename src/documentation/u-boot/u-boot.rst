.. |Warning| image:: ./images/Warning-icon.png
   :height: 80
   :width: 80

.. |Help| image:: ./images/help.gif
   :height: 80
   :width: 80

.. |Tip| image:: ./images/tip.gif
   :height: 80
   :width: 80


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

.. raw:: pdf

   PageBreak

Get U-Boot code for the DUTS_BOARDNAME
======================================

define some PATH variables
--------------------------

Export our workdirectory:

tbot_ref:export_TBOT_BASEDIR=_work_hs_tbot_tb_ctrl_1_1.txt

and cd into it

tbot_ref:cd_$TBOT_BASEDIR_tb_ctrl_1_1.txt

.. raw:: pdf

   PageBreak

clone the U-Boot code
---------------------

Now we simply clone the U-Boots source code with git:

tbot_ref:u-boot_clone_tb_ctrl_1_1.txt

cd into it

tbot_ref:cd2u-boot_tb_ctrl_1_1.txt

checkout the branch you want to test

tbot_ref:u-boot_checkout_tb_ctrl_1_1.txt

just for the records, print some info of the branch

tbot_ref:u-boot_describe_tb_ctrl_1_1.txt

.. raw:: pdf

   PageBreak

setup toolchain
===============

This depends on the toolchain you use.

tbot_ref:tc_workfd_set_toolchain.py_tb_ctrl_1_1.txt

If you have no toolchain installed, may you try buildman (see U-Boot code
tools/buildman) to fetch a toolchain:

::

   cd /path/to/u-boot
   PATH=$PATH:`pwd`/tools/buildman
   buildman --fetch-arch DUTS_UBOOT_ARCH

.. raw:: pdf

   PageBreak

compile U-Boot for the DUTS_BOARDNAME
=====================================

.. only:: compile_uboot_set_dtc_tb_ctrl_1_1.txt

Add the path to the dtc command to your PATH variable

tbot_ref:compile_uboot_set_dtc_tb_ctrl_1_1.txt

.. only_end::

clean the source code

tbot_ref:compile_uboot_mrproper_tb_ctrl_1_1.txt

configure source for the DUTS_BOARDNAME

tbot_ref:compile_uboot_config_tb_ctrl_1_1.txt

Now compile it

tbot_ref:compile_uboot_make_tb_ctrl_1_1.txt

after U-Boot is compiled, copy the resulting binaries we need later to our tftpboot directory.


tbot_ref:tc_lab_cp_file.py_tb_ctrl_1_1.txt
tbot_ref:tc_lab_cp_file.py_tb_ctrl_2_1.txt
tbot_ref:tc_lab_cp_file.py_tb_ctrl_3_1.txt

We also copy the u-boot.dtb file to our tftp directory, as we do some
testing with it later.

tbot_ref:tc_lab_cp_file.py_tb_ctrl_4_1.txt

.. raw:: pdf

   PageBreak

U-Boot installation
===================

install U-Boot
--------------

for this example, we install the new U-Boot on the SD card, as we use SD card bootmode.

tbot_ref:print_upd_uboot_tb_con_1_1.txt

tfpt the new u-boot image into ram and write it to the sd card.

tbot_ref:upd_uboot_tb_con_1_1.txt

install SPL
-----------

for this example, we install the new SPL on the SD card, as we use SD card bootmode.

tbot_ref:print_upd_spl_tb_con_1_1.txt

tfpt the new SPL image into ram and write it to the sd card.

tbot_ref:upd_spl_tb_con_1_1.txt

.. raw:: pdf

   PageBreak

Tool Installation
=================

U-Boot uses a special image format when loading the Linux kernel or ramdisk or other images. This image contains (among other things) information about the time of creation, operating system, compression type, image type, image name and CRC32 checksums.

The tool :redtext:`mkimage` is used to create such images or to display the information they contain. When using the ELDK_, the :redtext:`mkimage` command is already included with the other ELDK_ tools.

If you don't use the ELDK_ then you should install :redtext:`mkimage` in some directory that is in your command search PATH, for instance:

::

  $ cp tools/mkimage /usr/local/bin/

mkimage is readily available in several distributions; for example, in Ubuntu_ it is part of the :redtext:`u-boot-tools` package, so it can be installed with:

::

  $ sudo apt-get install u-boot-tools

In Fedora_ the package name is :redtext:`uboot-tools`, and the command to install it is:

::

  $ sudo dnf install uboot-tools

Finally, if you're building with OpenEmbedded_ or `Yocto Project`_, you would want to add the :redtext:`u-boot-fw-utils` recipe to your image. 

.. raw:: pdf

   PageBreak

U-Boot Command Line Interface
=============================

The following section describes the most important commands available in U-Boot. Please note that U-Boot is highly configurable, so not all of these commands may be available in the configuration of U-Boot installed on your hardware, or additional commands may exist. You can use the help command to print a list of all available commands for your configuration.

For most commands, you do not need to type in the full command name; instead it is sufficient to type a few characters. For instance, help can be abbreviated as h.

|Warning| The behaviour of some commands depends on the configuration of U-Boot and on the definition of some variables in your U-Boot environment.

Almost all U-Boot commands expect numbers to be entered in hexadecimal input format. (Exception: for historical reasons, the sleep command takes its argument in decimal input format.)

Be careful not to use edit keys besides 'Backspace', as hidden characters in things like environment variables can be very difficult to find. 

.. raw:: pdf

   PageBreak

Information Commands
--------------------

bdinfo - print Board Info structure
...................................

tbot_ref:help_bdinfo_tb_con_1_1.txt

The :redtext:`bdinfo` command (:redtext:`bdi`) prints the information that U-Boot passes about the board such as memory addresses and sizes, clock frequencies, MAC address, etc. This information is mainly needed to be passed to the Linux kernel. 


tbot_ref:bdi_tb_con_1_1.txt

.. raw:: pdf

   PageBreak

coninfo - print console devices and informations
................................................

tbot_ref:help_conin_tb_con_1_1.txt

The :redtext:`coninfo` command (:redtext:`conin`) displays information about the available console I/O devices. 

tbot_ref:conin_tb_con_1_1.txt

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

.. only:: mtest_run_tb_con_1_1.txt

.. raw:: pdf

   PageBreak

.. include:: u-boot-mtest.rst
.. only_end::

.. only:: mw_run_tb_con_1_1.txt
.. raw:: pdf

   PageBreak

.. include:: u-boot-mw.rst
.. only_end::

.. only:: nm_run_tb_con_1_1.txt
.. raw:: pdf

   PageBreak

.. include:: u-boot-nm.rst
.. only_end::

.. raw:: pdf

   PageBreak

.. include:: u-boot-loop.rst

.. raw:: pdf

   PageBreak

.. include:: u-boot-execution.rst

.. raw:: pdf

   PageBreak

.. include:: u-boot-download.rst

.. raw:: pdf

   PageBreak

.. include:: u-boot-env.rst

.. raw:: pdf

   PageBreak

.. include:: u-boot-fdt.rst

.. raw:: pdf

   PageBreak

.. include:: u-boot-special.rst

.. raw:: pdf

   PageBreak

.. include:: u-boot-misc.rst

.. raw:: pdf

   PageBreak

.. include:: u-boot-vars.rst

.. raw:: pdf

   PageBreak

.. include:: u-boot-script.rst

.. only:: test_py_start_tb_con_1_1.txt
.. raw:: pdf

   PageBreak

.. include:: u-boot-testpy.rst
.. only_end::


links
=====

.. _tbot: https://github.com/hsdenx/tbot

.. _ELDK: http://www.denx.de/wiki/DULG/ELDK

.. _Ubuntu: http://www.ubuntu.com/

.. _Fedora: http://fedoraproject.org/

.. _OpenEmbedded: http://openembedded.org/wiki/Main_Page

.. _`Yocto Project`: https://www.yoctoproject.org/
